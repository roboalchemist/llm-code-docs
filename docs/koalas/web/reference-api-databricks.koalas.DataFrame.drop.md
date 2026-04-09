# databricks.koalas.DataFrame.drop

`DataFrame.``drop`(*labels=None*, *axis=1*, *columns: Union[Any, Tuple, List[Any], List[Tuple]] = None*) → databricks.koalas.frame.DataFrame

Drop specified labels from columns.

Remove columns by specifying label names and axis=1 or columns.
When specifying both labels and columns, only labels will be dropped.
Removing rows is yet to be implemented.

Parameters

**labels**single label or list-like

Column labels to drop.

**axis**{1 or ‘columns’}, default 1
**columns**single label or list-like

Alternative to specifying axis (`labels, axis=1`
is equivalent to `columns=labels`).

Returns

**dropped**DataFrame

See also

`Series.dropna`