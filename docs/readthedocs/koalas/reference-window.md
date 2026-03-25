# Window

Rolling objects are returned by `.rolling` calls: `koalas.DataFrame.rolling()`, `koalas.Series.rolling()`, etc.
Expanding objects are returned by `.expanding` calls: `koalas.DataFrame.expanding()`, `koalas.Series.expanding()`, etc.

## Standard moving window functions

`Rolling.count`()

The rolling count of any non-NaN observations inside the window.

`Rolling.sum`()

Calculate rolling summation of given DataFrame or Series.

`Rolling.min`()

Calculate the rolling minimum.

`Rolling.max`()

Calculate the rolling maximum.

`Rolling.mean`()

Calculate the rolling mean of the values.