# Vector Operations

For this assignment we consider three more simple but essential operations on vectors.

## Scalar multiply

Multiplying a vector by a scalar $$c$$ scales every element:

$$
(c \cdot \mathbf{v})_i = c \cdot v_i
$$

## Vector add

Adding two vectors adds their corresponding elements:

$$
(\mathbf{a} + \mathbf{b})_i = a_i + b_i
$$

## Vector diff

Subtracting two vectors subtracts their corresponding elements:

$$
(\mathbf{a} - \mathbf{b})_i = a_i - b_i
$$

## Assignment

Create a file called `vec_operations.py` and define the following three functions:

- `scalar_multiply(c, v)` — returns a new list with every element of `v` multiplied by `c`
- `vector_add(a, b)` — returns a new list with the elementwise sum of `a` and `b`
- `vector_diff(a, b)` — returns a new list with the elementwise difference of `a` and `b`

### Example Usage

    print(scalar_multiply(3.0, [1.0, 2.0, 3.0]))
    print(scalar_multiply(0.5, [2.0, 4.0]))

    print(vector_add([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]))
    print(vector_add([1.0, -1.0], [1.0, 1.0]))

    print(vector_diff([4.0, 5.0, 6.0], [1.0, 2.0, 3.0]))
    print(vector_diff([1.0, 1.0], [1.0, -1.0]))

### Expected Output

    [3.0, 6.0, 9.0]
    [1.0, 2.0]

    [5.0, 7.0, 9.0]
    [2.0, 0.0]

    [3.0, 3.0, 3.0]
    [0.0, 2.0]

## Run

Run your program and verify that it indeed displays the expected text:

    python vec_operations.py

## Checkpy

You can use checkpy to verify that it meets our requirements:

    checkpy vec_operations
