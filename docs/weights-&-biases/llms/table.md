# Source: https://docs.wandb.ai/models/ref/query-panel/table.md

# Source: https://docs.wandb.ai/models/ref/python/data-types/table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/sdk/data_types/table.py" />

## <kbd>class</kbd> `Table`

The Table class used to display and analyze tabular data.

Unlike traditional spreadsheets, Tables support numerous types of data: scalar values, strings, numpy arrays, and most subclasses of `wandb.data_types.Media`. This means you can embed `Images`, `Video`, `Audio`, and other sorts of rich, annotated media directly in Tables, alongside other traditional scalar values.

This class is the primary class used to generate W\&B Tables [https://docs.wandb.ai/guides/models/tables/](https://docs.wandb.ai/guides/models/tables/).

### <kbd>method</kbd> `Table.__init__`

```python  theme={null}
__init__(
    columns=None,
    data=None,
    rows=None,
    dataframe=None,
    dtype=None,
    optional=True,
    allow_mixed_types=False,
    log_mode: "Literal['IMMUTABLE', 'MUTABLE', 'INCREMENTAL'] | None" = 'IMMUTABLE'
)
```

Initializes a Table object.

The rows is available for legacy reasons and should not be used. The Table class uses data to mimic the Pandas API.

**Args:**

* `columns`:  (List\[str]) Names of the columns in the table.  Defaults to \["Input", "Output", "Expected"].
* `data`:  (List\[List\[any]]) 2D row-oriented array of values.
* `dataframe`:  (pandas.DataFrame) DataFrame object used to create the table.  When set, `data` and `columns` arguments are ignored.
* `rows`:  (List\[List\[any]]) 2D row-oriented array of values.
* `optional`:  (Union\[bool,List\[bool]]) Determines if `None` values are allowed. Default to True
  * If a singular bool value, then the optionality is enforced for all  columns specified at construction time
  * If a list of bool values, then the optionality is applied to each  column - should be the same length as `columns`  applies to all columns. A list of bool values applies to each respective column.
* `allow_mixed_types`:  (bool) Determines if columns are allowed to have mixed types  (disables type validation). Defaults to False
* `log_mode`:  Optional\[str] Controls how the Table is logged when mutations occur.  Options:
  * "IMMUTABLE" (default): Table can only be logged once; subsequent  logging attempts after the table has been mutated will be no-ops.
  * "MUTABLE": Table can be re-logged after mutations, creating  a new artifact version each time it's logged.
  * "INCREMENTAL": Table data is logged incrementally, with each log creating  a new artifact entry containing the new data since the last log.

***

### <kbd>method</kbd> `Table.add_column`

```python  theme={null}
add_column(name, data, optional=False)
```

Adds a column of data to the table.

**Args:**

* `name`:  (str) - the unique name of the column
* `data`:  (list | np.array) - a column of homogeneous data
* `optional`:  (bool) - if null-like values are permitted

***

### <kbd>method</kbd> `Table.add_computed_columns`

```python  theme={null}
add_computed_columns(fn)
```

Adds one or more computed columns based on existing data.

**Args:**

* `fn`:  A function which accepts one or two parameters, ndx (int) and  row (dict), which is expected to return a dict representing  new columns for that row, keyed by the new column names.
  * `ndx` is an integer representing the index of the row. Only included if `include_ndx`  is set to `True`.
  * `row` is a dictionary keyed by existing columns

***

### <kbd>method</kbd> `Table.add_data`

```python  theme={null}
add_data(*data)
```

Adds a new row of data to the table.

The maximum amount ofrows in a table is determined by `wandb.Table.MAX_ARTIFACT_ROWS`.

The length of the data should match the length of the table column.

***

### <kbd>method</kbd> `Table.add_row`

```python  theme={null}
add_row(*row)
```

Deprecated. Use `Table.add_data` method instead.

***

### <kbd>method</kbd> `Table.cast`

```python  theme={null}
cast(col_name, dtype, optional=False)
```

Casts a column to a specific data type.

This can be one of the normal python classes, an internal W\&B type, or an example object, like an instance of wandb.Image or wandb.Classes.

**Args:**

* `col_name` (str):  The name of the column to cast.
* `dtype` (class, wandb.wandb\_sdk.interface.\_dtypes.Type, any):  The  target dtype.
* `optional` (bool):  If the column should allow Nones.

***

### <kbd>method</kbd> `Table.get_column`

```python  theme={null}
get_column(name, convert_to=None)
```

Retrieves a column from the table and optionally converts it to a NumPy object.

**Args:**

* `name`:  (str) - the name of the column
* `convert_to`:  (str, optional)
  * "numpy": will convert the underlying data to numpy object

***

### <kbd>method</kbd> `Table.get_dataframe`

```python  theme={null}
get_dataframe()
```

Returns a `pandas.DataFrame` of the table.

***

### <kbd>method</kbd> `Table.get_index`

```python  theme={null}
get_index()
```

Returns an array of row indexes for use in other tables to create links.

***
