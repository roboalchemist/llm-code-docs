# databricks.koalas.DataFrame.clip

`DataFrame.``clip`(*lower: Union[float, int] = None*, *upper: Union[float, int] = None*) → databricks.koalas.frame.DataFrame

Trim values at input threshold(s).

Assigns values outside boundary to boundary values.

Parameters

**lower**float or int, default None

Minimum threshold value. All values below this threshold will be set to it.

**upper**float or int, default None

Maximum threshold value. All values above this threshold will be set to it.

Returns

DataFrame

DataFrame with the values outside the clip boundaries replaced.

Notes

One difference between this implementation and pandas is that running
pd.DataFrame({‘A’: [‘a’, ‘b’]}).clip(0, 1) will crash with “TypeError: ‘<=’ not supported
between instances of ‘str’ and ‘int’” while ks.DataFrame({‘A’: [‘a’, ‘b’]}).clip(0, 1)
will output the original DataFrame, simply ignoring the incompatible types.

Examples

```
>>> ks.DataFrame({'A': [0, 2, 4]}).clip(1, 3)
   A
0  1
1  2
2  3

```