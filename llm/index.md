# Hackathon setup: build your own chatbot

In the hackathon you build a chatbot on top of a small language model that runs on your own laptop. The assignment itself is handed out on paper. This page is the preparation: install the packages and download the model **before** the hackathon, so you don't have to wait for it then.

## Install the packages

Open a terminal and activate your environment, so your prompt starts with `(uv-sp)`.

macOS/Linux:

    source ~/.venvs/uv-sp/bin/activate

Windows (PowerShell):

    & $HOME\.venvs\uv-sp\Scripts\Activate.ps1

Then install PyTorch and Transformers:

    uv pip install torch --index-url https://download.pytorch.org/whl/cpu
    uv pip install transformers

The first command installs the CPU-only version of PyTorch, which is a lot smaller than the default one. It can still take a few minutes.

If you installed Python without uv, use `pip` instead of `uv pip`.

## Download the model

Download [llm_helper.py](llm_helper.py) and put it in the folder where you will work on the hackathon. Then run it once:

    python llm_helper.py

The first run downloads the model, about 1 GB, so do this on a good connection. When it is done, it prints the five most likely words to follow "The capital of France is". If you see that list, you are ready.
