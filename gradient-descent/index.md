# Gradient Descent

The more CO₂ humanity has emitted in total, the warmer the Earth has become. The plot below shows, for every year from 1850 to 2025, the total amount of CO₂ emitted so far (in thousands of gigatonnes) against how much warmer the Earth was than in 1850–1900:

![Scatter plot of global warming against cumulative CO2 emissions](emissions_scatter.png){: style="max-width:70%;"}

The points lie close to a straight line. We will find that line with **linear regression**, using **gradient descent**.

Download the data here: [emissions.csv](emissions.csv)

    year,cumulative_co2,warming
    1850,0.0028,-0.069
    1851,0.0057,0.094
    ...

<small>Sources: Global Carbon Budget and HadCRUT5 (Met Office Hadley Centre), via [Our World in Data](https://ourworldindata.org/co2-and-greenhouse-gas-emissions). The warming is relative to the 1850–1900 average.</small>

## The model

As in the lecture, we model the warming $$\hat{y}$$ for total emissions $$x$$ as:

$$\hat{y} = wx + b$$

where $$w$$ (weight) is the slope and $$b$$ (bias) is the intercept. Both are scalars. Here $$w$$ is the warming per thousand gigatonnes of CO₂.

## The loss

The loss is the squared error loss function from the lecture. On the left in sum notation, on the right the same thing in vector notation:

| sum | vector |
|---|---|
| $$\mathrm{Loss} = \frac{1}{2}\sum_{j=1}^{N}(y_j - \hat{y}_j)^2$$ | $$\mathrm{Loss} = \frac{1}{2}\,(\vec{y} - \hat{\vec{y}}) \cdot (\vec{y} - \hat{\vec{y}})$$ |

where $$\hat{y}_j = wx_j + b$$, and $$\hat{\vec{y}}$$ is what `apply_affine` returns.

## The gradients

To minimise the loss, we need its partial derivatives with respect to $$w$$ and $$b$$. Both are **scalars**:

| sum | vector |
|---|---|
| $$\frac{\partial\,\mathrm{Loss}}{\partial w} = -\sum_{j=1}^{N}(y_j - \hat{y}_j)\,x_j$$ | $$\frac{\partial\,\mathrm{Loss}}{\partial w} = -(\vec{y} - \hat{\vec{y}}) \cdot \vec{x}$$ |
| $$\frac{\partial\,\mathrm{Loss}}{\partial b} = -\sum_{j=1}^{N}(y_j - \hat{y}_j)$$ | $$\frac{\partial\,\mathrm{Loss}}{\partial b} = -(\vec{y} - \hat{\vec{y}}) \cdot \vec{1}$$ |

where $$\vec{1}$$ is a vector of ones with $$N$$ elements. The vector column translates directly into your functions from week 5.

## The update step

At each iteration, we nudge $$w$$ and $$b$$ in the direction that reduces the loss:

$$w := w - \alpha \frac{\partial\,\mathrm{Loss}}{\partial w}$$

$$b := b - \alpha \frac{\partial\,\mathrm{Loss}}{\partial b}$$

where $$\alpha$$ is the **learning rate** — a small positive number that controls the step size.

## Assignment

Create a file called `gradient_descent.py`. Read `emissions.csv` into two lists, `emissions` and `warming`, and copy in your `apply_affine`, `vector_diff`, `inner_product`, and `mse` functions from week 5.

Then implement the following function:

    def fit(xs, ys, w_start, b_start, n_iterations, learning_rate):
        ...
        return w, b, mse_list

The function runs gradient descent on the data `xs` and `ys` for `n_iterations` steps, starting from `w_start` and `b_start`. It returns the final $$w$$, the final $$b$$, and a list with the MSE after every step: after updating $$w$$ and $$b$$, compute the MSE of the new line and append it.

> Gradient descent minimises the loss above, but we follow its progress with the MSE from week 5. Both are the same sum, the MSE divided by $$N$$ instead of by $$2$$, so they are smallest for the same $$w$$ and $$b$$.

### Part 1: first run

Call the function with:

    w, b, mse_list = fit(emissions, warming, 0, 0, 50, 1e-4)

Print the result:

    print(f"w = {w:.6f}")
    print(f"b = {b:.6f}")
    print(f"MSE = {mse_list[-1]:.4f}")

### Expected output

    w = 0.250811
    b = 0.096327
    MSE = 0.0496

This is only a partial result — 50 iterations at this learning rate is not enough to fully converge. You will fix that in the next assignment.

### Part 2: plot

Plot the fitted line on top of the scatter data, and plot the `mse_list` as a second figure showing how the MSE decreased over the iterations.

## Run

    python gradient_descent.py

## Checkpy

    checkpy gradient_descent
