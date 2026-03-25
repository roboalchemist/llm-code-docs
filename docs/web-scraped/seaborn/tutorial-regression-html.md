# Source: https://seaborn.pydata.org/tutorial/regression.html

Title: Estimating regression fits — seaborn 0.13.2 documentation

URL Source: https://seaborn.pydata.org/tutorial/regression.html

Markdown Content:
Many datasets contain multiple quantitative variables, and the goal of an analysis is often to relate those variables to each other. We [previously discussed](https://seaborn.pydata.org/tutorial/distributions.html#distribution-tutorial) functions that can accomplish this by showing the joint distribution of two variables. It can be very helpful, though, to use statistical models to estimate a simple relationship between two noisy sets of observations. The functions discussed in this chapter will do so through the common framework of linear regression.

In the spirit of Tukey, the regression plots in seaborn are primarily intended to add a visual guide that helps to emphasize patterns in a dataset during exploratory data analyses. That is to say that seaborn is not itself a package for statistical analysis. To obtain quantitative measures related to the fit of regression models, you should use [statsmodels](https://www.statsmodels.org/). The goal of seaborn, however, is to make exploring a dataset through visualization quick and easy, as doing so is just as (if not more) important than exploring a dataset through tables of statistics.

Functions for drawing linear regression models[#](https://seaborn.pydata.org/tutorial/regression.html#functions-for-drawing-linear-regression-models "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The two functions that can be used to visualize a linear fit are [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") and [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot").

In the simplest invocation, both functions draw a scatterplot of two variables, `x` and `y`, and then fit the regression model `y ~ x` and plot the resulting regression line and a 95% confidence interval for that regression:

tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips);

![Image 1: ../_images/regression_4_0.png](https://seaborn.pydata.org/_images/regression_4_0.png)

sns.lmplot(x="total_bill", y="tip", data=tips);

![Image 2: ../_images/regression_5_0.png](https://seaborn.pydata.org/_images/regression_5_0.png)
These functions draw similar plots, but [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") is an [axes-level function](https://seaborn.pydata.org/tutorial/function_overview.html), and [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot") is a figure-level function. Additionally, [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") accepts the `x` and `y` variables in a variety of formats including simple numpy arrays, [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "(in pandas v2.2.0)") objects, or as references to variables in a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)") object passed to `data`. In contrast, [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot") has `data` as a required parameter and the `x` and `y` variables must be specified as strings. Finally, only [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot") has `hue` as a parameter.

The core functionality is otherwise similar, though, so this tutorial will focus on [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot"):.

It’s possible to fit a linear regression when one of the variables takes discrete values, however, the simple scatterplot produced by this kind of dataset is often not optimal:

sns.lmplot(x="size", y="tip", data=tips);

![Image 3: ../_images/regression_7_0.png](https://seaborn.pydata.org/_images/regression_7_0.png)
One option is to add some random noise (“jitter”) to the discrete values to make the distribution of those values more clear. Note that jitter is applied only to the scatterplot data and does not influence the regression line fit itself:

sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05);

![Image 4: ../_images/regression_9_0.png](https://seaborn.pydata.org/_images/regression_9_0.png)
A second option is to collapse over the observations in each discrete bin to plot an estimate of central tendency along with a confidence interval:

sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean);

![Image 5: ../_images/regression_11_0.png](https://seaborn.pydata.org/_images/regression_11_0.png)
Fitting different kinds of models[#](https://seaborn.pydata.org/tutorial/regression.html#fitting-different-kinds-of-models "Permalink to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

The simple linear regression model used above is very simple to fit, however, it is not appropriate for some kinds of datasets. The [Anscombe’s quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) dataset shows a few examples where simple linear regression provides an identical estimate of a relationship where simple visual inspection clearly shows differences. For example, in the first case, the linear regression is a good model:

anscombe = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80});

![Image 6: ../_images/regression_14_0.png](https://seaborn.pydata.org/_images/regression_14_0.png)
The linear relationship in the second dataset is the same, but the plot clearly shows that this is not a good model:

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           ci=None, scatter_kws={"s": 80});

![Image 7: ../_images/regression_16_0.png](https://seaborn.pydata.org/_images/regression_16_0.png)
In the presence of these kind of higher-order relationships, [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot") and [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") can fit a polynomial regression model to explore simple kinds of nonlinear trends in the dataset:

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80});

![Image 8: ../_images/regression_18_0.png](https://seaborn.pydata.org/_images/regression_18_0.png)
A different problem is posed by “outlier” observations that deviate for some reason other than the main relationship under study:

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           ci=None, scatter_kws={"s": 80});

![Image 9: ../_images/regression_20_0.png](https://seaborn.pydata.org/_images/regression_20_0.png)
In the presence of outliers, it can be useful to fit a robust regression, which uses a different loss function to downweight relatively large residuals:

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80});

![Image 10: ../_images/regression_22_0.png](https://seaborn.pydata.org/_images/regression_22_0.png)
When the `y` variable is binary, simple linear regression also “works” but provides implausible predictions:

tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip", data=tips,
           y_jitter=.03);

![Image 11: ../_images/regression_24_0.png](https://seaborn.pydata.org/_images/regression_24_0.png)
The solution in this case is to fit a logistic regression, such that the regression line shows the estimated probability of `y = 1` for a given value of `x`:

sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03);

![Image 12: ../_images/regression_26_0.png](https://seaborn.pydata.org/_images/regression_26_0.png)
Note that the logistic regression estimate is considerably more computationally intensive (this is true of robust regression as well). As the confidence interval around the regression line is computed using a bootstrap procedure, you may wish to turn this off for faster iteration (using `ci=None`).

An altogether different approach is to fit a nonparametric regression using a [lowess smoother](https://en.wikipedia.org/wiki/Local_regression). This approach has the fewest assumptions, although it is computationally intensive and so currently confidence intervals are not computed at all:

sns.lmplot(x="total_bill", y="tip", data=tips,
           lowess=True, line_kws={"color": "C1"});

![Image 13: ../_images/regression_28_0.png](https://seaborn.pydata.org/_images/regression_28_0.png)
The [`residplot()`](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot "seaborn.residplot") function can be a useful tool for checking whether the simple regression model is appropriate for a dataset. It fits and removes a simple linear regression and then plots the residual values for each observation. Ideally, these values should be randomly scattered around `y = 0`:

sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              scatter_kws={"s": 80});

![Image 14: ../_images/regression_30_0.png](https://seaborn.pydata.org/_images/regression_30_0.png)
If there is structure in the residuals, it suggests that simple linear regression is not appropriate:

sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
              scatter_kws={"s": 80});

![Image 15: ../_images/regression_32_0.png](https://seaborn.pydata.org/_images/regression_32_0.png)
Conditioning on other variables[#](https://seaborn.pydata.org/tutorial/regression.html#conditioning-on-other-variables "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

The plots above show many ways to explore the relationship between a pair of variables. Often, however, a more interesting question is “how does the relationship between these two variables change as a function of a third variable?” This is where the main differences between [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") and [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot") appear. While [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") always shows a single relationship, [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot") combines [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") with [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid") to show multiple fits using `hue` mapping or faceting.

The best way to separate out a relationship is to plot both levels on the same axes and to use color to distinguish them:

sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips);

![Image 16: ../_images/regression_34_0.png](https://seaborn.pydata.org/_images/regression_34_0.png)
Unlike [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot"), it’s not possible to map a distinct variable to the style properties of the scatter plot, but you can redundantly code the `hue` variable with marker shape:

sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1");

![Image 17: ../_images/regression_36_0.png](https://seaborn.pydata.org/_images/regression_36_0.png)
To add another variable, you can draw multiple “facets” with each level of the variable appearing in the rows or columns of the grid:

sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips);

![Image 18: ../_images/regression_38_0.png](https://seaborn.pydata.org/_images/regression_38_0.png)

sns.lmplot(x="total_bill", y="tip", hue="smoker",
           col="time", row="sex", data=tips, height=3);

![Image 19: ../_images/regression_39_0.png](https://seaborn.pydata.org/_images/regression_39_0.png)
Plotting a regression in other contexts[#](https://seaborn.pydata.org/tutorial/regression.html#plotting-a-regression-in-other-contexts "Permalink to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

A few other seaborn functions use [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") in the context of a larger, more complex plot. The first is the [`jointplot()`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot") function that we introduced in the [distributions tutorial](https://seaborn.pydata.org/tutorial/distributions.html#distribution-tutorial). In addition to the plot styles previously discussed, [`jointplot()`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot") can use [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") to show the linear regression fit on the joint axes by passing `kind="reg"`:

sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg");

![Image 20: ../_images/regression_41_0.png](https://seaborn.pydata.org/_images/regression_41_0.png)
Using the [`pairplot()`](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot") function with `kind="reg"` combines [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot") and [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid") to show the linear relationship between variables in a dataset. Take care to note how this is different from [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot"). In the figure below, the two axes don’t show the same relationship conditioned on two levels of a third variable; rather, [`PairGrid()`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid") is used to show multiple relationships between different pairings of the variables in a dataset:

sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
             height=5, aspect=.8, kind="reg");

![Image 21: ../_images/regression_43_0.png](https://seaborn.pydata.org/_images/regression_43_0.png)
Conditioning on an additional categorical variable is built into both of these functions using the `hue` parameter:

sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
             hue="smoker", height=5, aspect=.8, kind="reg");

![Image 22: ../_images/regression_45_0.png](https://seaborn.pydata.org/_images/regression_45_0.png)
