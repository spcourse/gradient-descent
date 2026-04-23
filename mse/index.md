# Mean Squared Error

In the previous assignment, we used `apply_affine` to predict apartment prices:

    sizes       = [30.0,   45.0,   60.0,   75.0,   90.0,   120.0]
    predictions = [290000.0, 410000.0, 530000.0, 650000.0, 770000.0, 1010000.0]

Now suppose we also know the actual sale prices of those six apartments:

    actual = [280000.0, 400000.0, 540000.0, 660000.0, 760000.0, 1020000.0]

Our predictions are close, but not perfect. To know *how well* our model is doing, we need a single number that summarises the error across all predictions. This number is called a **loss**.

## Mean Squared Error

A commonly used loss function in machine learning is the **Mean Squared Error** (MSE). It computes the average of the squared differences between each prediction and the actual value:

$$
\text{MSE} = \frac{1}{n} \Sigma_{i=0}^{n-1} (\hat{y}_i - y_i)^2
$$

Squaring the differences has two effects: it makes all errors positive, and it penalises large errors more heavily than small ones.

In vector notation, using the inner product:

$$
\text{MSE} = \frac{1}{n} \langle \hat{\mathbf{y}} - \mathbf{y},\ \hat{\mathbf{y}} - \mathbf{y} \rangle
$$

This is a hint: you can implement MSE using `vector_diff` and `inner_product` from an earlier assignment.

## Assignment

Create a file called `mse.py` and define a function `mse(predictions, targets)` that returns the mean squared error between two lists of equal length.

### Example Usage

    predictions = [290000.0, 410000.0, 530000.0, 650000.0, 770000.0, 1010000.0]
    actual      = [280000.0, 400000.0, 540000.0, 660000.0, 760000.0, 1020000.0]

    print(mse(predictions, actual))
    print(mse([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]))

### Expected Output

    100000000.0
    0.0

The first result tells us our apartment predictions are off by €10,000 per apartment on average (since $$\sqrt{100000000} = 10000$$). The second confirms that perfect predictions give a loss of zero.

## Run

Run your program and verify that it indeed displays the expected text:

    python mse.py

## Checkpy

You can use checkpy to verify that it meets our requirements:

    checkpy mse
