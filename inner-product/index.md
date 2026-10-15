# Inner Product

In mathematics, a **vector** can be interpreted as an ordered sequence of numbers, its elements (*kentallen*). We put an arrow above the name and write the elements in a column, for example:

$$
\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \qquad \vec{b} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}
$$

In Python we can represent these vectors as lists:

    a = [1, 2, 3]
    b = [4, 5, 6]

We number the elements of a vector with $$n$$ elements from $$0$$ to $$n-1$$, so $$\vec{a}$$ has elements $$a_0 = 1$$, $$a_1 = 2$$ and $$a_2 = 3$$. Your maths course counted from $$1$$, but we programmers prefer to start at $$0$$: that way $$a_i$$ is exactly `a[i]` in Python.

The **inner product** (also called the *dot product*; in Dutch *inproduct*) of two vectors $$\vec{a}$$ and $$\vec{b}$$ with $$n$$ elements is defined as:

$$
\vec{a} \cdot \vec{b} = \sum_{i=0}^{n-1} a_i b_i
$$

In words: multiply each pair of corresponding elements, then sum all those products. For example:

$$
\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix} = 1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6 = 4 + 10 + 18 = 32
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

> The second example computes the inner product of a vector with itself, the result is the sum of squared elements. The third example shows two perpendicular (*loodrechte*) vectors: their inner product is always zero.

## Run

Run your program and verify that it indeed displays the expected text:

    python inner_product.py

## Checkpy

You can use checkpy to verify that it meets our requirements:

    checkpy inner_product
