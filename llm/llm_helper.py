"""
llm_helper.py - a tiny wrapper around a small local language model.

You only need three things from this file:

    tokenize(text)          -> the text split into tokens, as a list of strings
    next_token_probs(tokens) -> list of [token, probability] pairs, most likely first
    END                     -> the token the model produces when its turn is over

Example:
    >>> tokens = tokenize("The capital of France is")
    >>> tokens
    ['The', ' capital', ' of', ' France', ' is']
    >>> options = next_token_probs(tokens)
    >>> options[0]
    [' Paris', 0.32...]

Putting the tokens back together gives the original text again:
"".join(tokenize(text)) == text.

Chat format this model was trained on (each message looks like this):

    <|im_start|>system
    You are a helpful assistant.<|im_end|>
    <|im_start|>user
    Hello!<|im_end|>
    <|im_start|>assistant

The model then continues the text after "assistant" and ends its reply with END.

Setup:
    pip install torch --index-url https://download.pytorch.org/whl/cpu
    pip install transformers

The first run downloads the model (about 1 GB) and may take a few minutes.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
END = "<|im_end|>"
TOP_K = 50

print(f"Loading {MODEL_NAME} ...")
_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# float32: on a CPU this is several times faster than bfloat16, the format
# the model is stored in
_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, dtype=torch.float32)
_model.eval()
print("Model loaded.")

# The model's work on the previous text is kept between calls. When the new
# text is the previous text plus a few tokens, only those tokens are computed.
_cached_ids = []
_cached_state = None
_cached_logits = None


def tokenize(text):
    """Split text into the tokens the model works with, as a list of strings."""
    tokens = []
    pending = []
    for token_id in _tokenizer(text).input_ids:
        pending.append(token_id)
        piece = _tokenizer.decode(pending)
        # some characters (emoji, for instance) are spread over several
        # token ids: wait until the character is complete
        if "\ufffd" not in piece:
            tokens.append(piece)
            pending = []
    if pending:
        tokens.append(_tokenizer.decode(pending))
    return tokens


def next_token_probs(tokens, top_k=TOP_K):
    """Return a list of [token, probability] pairs for the most likely next tokens.

    tokens is the text so far, as a list of strings. The list returned is
    sorted from most to least likely, and the probabilities are renormalised
    so they add up to 1.
    """
    ids = _tokenizer("".join(tokens)).input_ids
    logits = _next_token_scores(ids)
    probs = torch.softmax(logits.float(), dim=-1)
    top = torch.topk(probs, top_k)

    merged = {}
    for p, token_id in zip(top.values.tolist(), top.indices.tolist()):
        token = _tokenizer.decode([token_id])
        if "\ufffd" in token:  # half of a multi-byte character: skip it
            continue
        if token == "<|endoftext|>":  # treat both end markers the same
            token = END
        # different token ids can decode to the same text: add them together
        merged[token] = merged.get(token, 0) + p

    total = sum(merged.values())
    result = [[token, p / total] for token, p in merged.items()]
    result.sort(key=lambda pair: pair[1], reverse=True)
    return result


def _next_token_scores(ids):
    """Return the model's scores for the token after ids, reusing the cache."""
    global _cached_ids, _cached_state, _cached_logits
    if ids == _cached_ids:
        return _cached_logits

    n = len(_cached_ids)
    if _cached_state is not None and ids[:n] == _cached_ids:
        new_ids = ids[n:]
    else:  # the text changed in some other way: start again
        _cached_state = None
        new_ids = ids

    with torch.no_grad():
        output = _model(torch.tensor([new_ids]), past_key_values=_cached_state,
                        use_cache=True)
    _cached_ids = ids
    _cached_state = output.past_key_values
    _cached_logits = output.logits[0, -1]  # scores for the next position only
    return _cached_logits


if __name__ == "__main__":
    # Quick check: show the 5 most likely continuations of a prompt.
    tokens = tokenize("The capital of France is")
    print(tokens)
    for token, p in next_token_probs(tokens)[:5]:
        print(f"{token!r:>12}  {p:.3f}")
