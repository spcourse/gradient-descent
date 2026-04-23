# Inner Product

In mathematics, a **vector** can be interpreted as an ordered sequence of numbers, for example:

$$
\mathbf{a} = (1, 2, 3) \qquad \mathbf{b} = (4, 5, 6)
$$

In Python we can represent these vectors as lists:

    a = [1, 2, 3]
    b = [4, 5, 6]


The **inner product** (also called the *dot product*) of two vectors $$\mathbf{a}$$ and $$\mathbf{b}$$ of length $$n$$ is defined as:

$$
\langle \mathbf{a}, \mathbf{b} \rangle = \Sigma_{i=0}^{n-1} a_i \cdot b_i
$$

In words: multiply each pair of corresponding elements, then sum all those products. For example:

$$
\langle (1, 2, 3),\ (4, 5, 6) \rangle = 1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6 = 4 + 10 + 18 = 32
$$

## Assignment

Create a file called `inner_product.py` and define a function `inner_product(a, b)` that takes two lists of equal length and returns their inner product.

### Example Usage

    print(inner_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]))
    print(inner_product([2.0, 3.0], [2.0, 3.0]))
    print(inner_product([1.0, 0.0], [0.0, 1.0]))

### Expected Output

    32.0
    13.0
    0.0

> The second example computes the inner product of a vector with itself, the result is the sum of squared elements. The third example shows two perpendicular vectors: their inner product is always zero.

## Run

Run your program and verify that it indeed displays the expected text:

    python inner_product.py

## Checkpy

You can use checkpy to verify that it meets our requirements:

    checkpy inner_product
