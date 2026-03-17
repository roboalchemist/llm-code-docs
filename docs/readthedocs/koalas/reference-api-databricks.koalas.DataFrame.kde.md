# databricks.koalas.DataFrame.kde

`DataFrame.``kde`(*bw_method=None*, *ind=None*, ***kwds*)

Generate Kernel Density Estimate plot using Gaussian kernels.

Parameters

**bw_method**scalar

The method used to calculate the estimator bandwidth.
See KernelDensity in PySpark for more information.

**ind**NumPy array or integer, optional

Evaluation points for the estimated PDF. If None (default),
1000 equally spaced points are used. If ind is a NumPy array, the
KDE is evaluated at the points passed. If ind is an integer,
ind number of equally spaced points are used.

****kwargs**optional

Keyword arguments to pass on to `Koalas.Series.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`.
Return an ndarray when `subplots=True` (matplotlib-only).

Examples

A scalar bandwidth should be specified. Using a small bandwidth value can
lead to over-fitting, while using a large bandwidth value may result
in under-fitting:

```
>>> s = ks.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(bw_method=0.3)  

```