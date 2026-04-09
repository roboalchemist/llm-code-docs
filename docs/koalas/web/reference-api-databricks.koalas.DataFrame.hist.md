# databricks.koalas.DataFrame.hist

`DataFrame.``hist`(*bins=10*, ***kwds*)

Draw one histogram of the DataFrame’s columns.
A histogram [https://en.wikipedia.org/wiki/Histogram] is a representation of the distribution of data.
This function calls `plotting.backend.plot()`,
on each series in the DataFrame, resulting in one histogram per column.

Parameters

**bins**integer or sequence, default 10

Number of histogram bins to be used. If an integer is given, bins + 1
bin edges are calculated and returned. If bins is a sequence, gives
bin edges, including left edge of first bin and right edge of last
bin. In this case, bins is returned unmodified.

****kwds**

All other plotting keyword arguments to be passed to
plotting backend.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`.
Return an ndarray when `subplots=True` (matplotlib-only).

Examples

Basic plot.

For Series:

```
>>> s = ks.Series([1, 3, 2])
>>> s.plot.hist()  

```