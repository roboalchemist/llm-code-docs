# databricks.koalas.DataFrame.corr

`DataFrame.``corr`(*method='pearson'*) → Union[Series, DataFrame, Index]

Compute pairwise correlation of columns, excluding NA/null values.

Parameters

**method**{‘pearson’, ‘spearman’}

- 

pearson : standard correlation coefficient

- 

spearman : Spearman rank correlation

Returns

**y**DataFrame

See also

`Series.corr`