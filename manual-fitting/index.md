# Manual Fitting

Continue working in `exploration.py`. You already have the scatter plot of yearly maximum temperatures. In order to predict future temperatures, we would like to do linear regression, meaning we need to fit a straight line through the data. In this assignment we will try out some lines by hand.

Copy the `apply_affine` and `mse` functions from week 5 into your file.

## Part 1: first fit

Apply the affine function with $$w = 0.022$$ and $$b = -29.0$$ to the list of years to get a list of predicted temperatures. Plot the resulting line on top of your scatter plot and print the MSE.

### Expected output

    MSE for w=0.022, b=-29.0: 0.9007

## Part 2: second fit

Try a second parameterisation: $$w = 0.01$$ and $$b = -6.0$$. Add this line to the same plot. Make clear in the legend which line belongs to which parameterisation.

Print the MSE for this fit as well.

### Expected output

    MSE for w=0.022, b=-29.0: 0.9007
    MSE for w=0.01, b=-6.0: 0.6523

## Part 3: experiment

The second fit is already better (it has a lower MSE than the first). Can you find a combination of $$w$$ and $$b$$ that does better still? Add your best fit to the plot and print its MSE.

## Run

    python exploration.py

## Checkpy

    checkpy exploration
