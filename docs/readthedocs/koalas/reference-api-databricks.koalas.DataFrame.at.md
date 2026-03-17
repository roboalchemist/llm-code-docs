# databricks.koalas.DataFrame.at

*property *`DataFrame.``at`

Access a single value for a row/column label pair.
If the index is not unique, all matching pairs are returned as an array.
Similar to `loc`, in that both provide label-based lookups. Use `at` if you only need to
get a single value in a DataFrame or Series.

Note

Unlike pandas, Koalas only allows using `at` to get values but not to set them.