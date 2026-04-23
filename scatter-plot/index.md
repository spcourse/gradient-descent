# Scatter Plot

In the apply affine assignment, we showed this plot:

![Scatter plot with a fitted line](../apply-affine/prices_fit.png){: style="max-width:60%;"}

Your job is to create a similar plot, but using the data from the MSE assignment:

    sizes  = [30.0, 45.0, 60.0, 75.0, 90.0, 120.0]
    actual = [280000.0, 400000.0, 540000.0, 660000.0, 760000.0, 1020000.0]

And the model we found earlier: $$w = 8000$$, $$b = 50000$$.

## Assignment

Create a file called `plot_regression.py`. Plot the six apartments as a scatter plot, then draw the regression line on top.

For the line, generate a list of x-values covering the range of the data and use your `apply_affine` function to compute the corresponding predicted prices.

Make sure to:

* Label the axes (`Size (m²)` and `Price (× €1000)`)
* Add a legend with `data` and `f(x) = 8000x + 50000`
* Show prices divided by 1000 on the y-axis, so the numbers stay readable
* You should use the `apply_affine()` function from before to get the correct values for the regression line.

## Hints

* Use `plt.scatter(x, y)` for the data points and `plt.plot(x, y)` for the line.
* Checkpy cannot judge whether your graph looks correct (but *you* can 😊).

## Run

    python scatter_plot.py

## Checkpy

    checkpy scatter_plot
