# databricks.koalas.DataFrame.filter

`DataFrame.``filter`(*items=None*, *like=None*, *regex=None*, *axis=None*) → databricks.koalas.frame.DataFrame

Subset rows or columns of dataframe according to labels in
the specified index.

Note that this routine does not filter a dataframe on its
contents. The filter is applied to the labels of the index.

Parameters

**items**list-like

Keep labels from axis which are in items.

**like**string

Keep labels from axis for which “like in label == True”.

**regex**string (regular expression)

Keep labels from axis for which re.search(regex, label) == True.

**axis**int or string axis name

The axis to filter on.  By default this is the info axis,
‘index’ for Series, ‘columns’ for DataFrame.

Returns

same type as input object

See also

`DataFrame.loc`