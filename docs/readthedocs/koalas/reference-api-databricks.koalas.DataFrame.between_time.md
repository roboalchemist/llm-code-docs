# databricks.koalas.DataFrame.between_time

`DataFrame.``between_time`(*start_time: Union[datetime.time, str]*, *end_time: Union[datetime.time, str]*, *include_start: bool = True*, *include_end: bool = True*, *axis: Union[int, str] = 0*) → databricks.koalas.frame.DataFrame

Select values between particular times of the day (e.g., 9:00-9:30 AM).

By setting `start_time` to be later than `end_time`,
you can get the times that are *not* between the two times.

Parameters

**start_time**datetime.time or str

Initial time as a time filter limit.

**end_time**datetime.time or str

End time as a time filter limit.

**include_start**bool, default True

Whether the start time needs to be included in the result.

**include_end**bool, default True

Whether the end time needs to be included in the result.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Determine range time on index or columns value.

Returns

DataFrame

Data from the original object filtered to the specified dates range.

Raises

TypeError

If the index is not  a `DatetimeIndex`

See also

`at_time`

Select values at a particular time of the day.

`first`

Select initial periods of time series based on a date offset.

`last`

Select final periods of time series based on a date offset.

`DatetimeIndex.indexer_between_time`

Get just the index locations for values between particular times of the day.