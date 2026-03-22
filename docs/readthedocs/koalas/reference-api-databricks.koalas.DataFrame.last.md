# databricks.koalas.DataFrame.last

`DataFrame.``last`(*offset: Union[str, pandas._libs.tslibs.offsets.DateOffset]*) → databricks.koalas.frame.DataFrame

Select final periods of time series data based on a date offset.

When having a DataFrame with dates as index, this function can
select the last few rows based on a date offset.

Parameters

**offset**str or DateOffset

The offset length of the data that will be selected. For instance,
‘3D’ will display all the rows having their index within the last 3 days.

Returns

DataFrame

A subset of the caller.

Raises

TypeError

If the index is not a `DatetimeIndex`

Examples

```
>>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
>>> kdf = ks.DataFrame({'A': [1, 2, 3, 4]}, index=index)
>>> kdf
            A
2018-04-09  1
2018-04-11  2
2018-04-13  3
2018-04-15  4

```