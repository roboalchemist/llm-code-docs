# patito.DataFrame.read_csv

*classmethod *DataFrame.read_csv(**args*, ***kwargs*)

Read CSV and apply correct column name and types from model.

If any fields have `derived_from` specified, the given expression will be used
to populate the given column(s).

Parameters:

- 

***args** – All positional arguments are forwarded to `polars.read_csv`.

- 

****kwargs** – All keyword arguments are forwarded to `polars.read_csv`.

Returns:

A dataframe representing the given CSV file data.

Return type:

DataFrame[Model]

Examples

The `DataFrame.read_csv` method can be used to automatically set the
correct column names when reading CSV files without headers.

```
>>> import io
>>> import patito as pt
>>> class CSVModel(pt.Model):
...     a: float
...     b: str
...
>>> csv_file = io.StringIO("1,2")
>>> CSVModel.DataFrame.read_csv(csv_file, has_header=False)
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ f64 ┆ str │
╞═════╪═════╡
│ 1.0 ┆ 2   │
└─────┴─────┘

```