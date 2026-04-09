# databricks.koalas.DataFrame.at_time

`DataFrame.``at_time`(*time: Union[datetime.time, str]*, *asof: bool = False*, *axis: Union[int, str] = 0*) → databricks.koalas.frame.DataFrame

Select values at particular time of day (e.g., 9:30AM).

Parameters

**time**datetime.time or str
**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Returns

DataFrame

Raises

TypeError

If the index is not  a `DatetimeIndex`

See also

`between_time`

Select values between particular times of the day.

`DatetimeIndex.indexer_at_time`

Get just the index locations for values at particular time of the day.