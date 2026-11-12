# Visualize Learning

Continue working in `gradient_descent.py`.

In the previous assignment you ran `fit(emissions, warming, 0, 0, 50, 1e-4)` and got an MSE of 0.0496 — not yet a good fit. The loss curve you plotted shows why: 50 iterations at that learning rate is not enough to converge.

## Assignment

Find a combination of `learning_rate` and `n_iterations` that gets the MSE down to 0.0167. Run `fit` with your chosen values, print the result, and produce the two plots.

    w, b, mse_list = fit(emissions, warming, 0, 0, n_iterations, learning_rate)
    print(f"w = {w:.6f}")
    print(f"b = {b:.6f}")
    print(f"MSE = {mse_list[-1]:.4f}")

Make sure your final file produces **all** of the following when run:

1. The three plots from `visualize_learning`
2. The printed output from Part 2 (`fit(emissions, warming, 0, 0, 50, 1e-4)`)
3. The printed output from your converged fit
4. A plot of the converged fit on top of the scatter data
5. A plot of the MSE over iterations for the converged run

## Hints

- A larger learning rate converges faster but may overshoot and diverge. If you get `nan` or huge numbers, your learning rate is too large.
- The loss curve from Part 1 gives you a sense of the shape (the MSE drops steeply at first and then flattens). More iterations alone won't help much if the learning rate is too small.
- Try increasing the learning rate first, then adjust the number of iterations until the loss curve has clearly flattened out.

## Run

    python gradient_descent.py

## Checkpy

    checkpy gradient_descent
