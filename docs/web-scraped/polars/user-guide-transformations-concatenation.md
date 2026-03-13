# Source: https://docs.pola.rs/user-guide/transformations/concatenation/

Title: Concatenation - Polars user guide

URL Source: https://docs.pola.rs/user-guide/transformations/concatenation/

Markdown Content:
There are a number of ways to concatenate data from separate DataFrames:

*   two dataframes with **the same columns** can be **vertically** concatenated to make a **longer** dataframe
*   two dataframes with **non-overlapping columns** can be **horizontally** concatenated to make a **wider** dataframe
*   two dataframes with **different numbers of rows and columns** can be **diagonally** concatenated to make a dataframe which might be longer and/ or wider. Where column names overlap values will be vertically concatenated. Where column names do not overlap new rows and columns will be added. Missing values will be set as `null`

Vertical concatenation - getting longer
---------------------------------------

In a vertical concatenation you combine all of the rows from a list of `DataFrames` into a single longer `DataFrame`.

Python  Rust

[`concat`](https://docs.pola.rs/api/python/stable/reference/api/polars.concat.html)

```
df_v1 = pl.DataFrame(
    {
        "a": [1],
        "b": [3],
    }
)
df_v2 = pl.DataFrame(
    {
        "a": [2],
        "b": [4],
    }
)
df_vertical_concat = pl.concat(
    [
        df_v1,
        df_v2,
    ],
    how="vertical",
)
print(df_vertical_concat)
```

[`concat`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/functions/fn.concat.html)

```
let df_v1 = df!(
        "a"=> &[1],
        "b"=> &[3],
)?;
let df_v2 = df!(
        "a"=> &[2],
        "b"=> &[4],
)?;
let df_vertical_concat =
    concat([df_v1.lazy(), df_v2.lazy()], UnionArgs::default())?.collect()?;
println!("{}", &df_vertical_concat);
```

```
shape: (2, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 3   │
│ 2   ┆ 4   │
└─────┴─────┘
```

Vertical concatenation fails when the dataframes do not have the same column names.

Horizontal concatenation - getting wider
----------------------------------------

In a horizontal concatenation you combine all of the columns from a list of `DataFrames` into a single wider `DataFrame`.

Python  Rust

[`concat`](https://docs.pola.rs/api/python/stable/reference/api/polars.concat.html)

```
df_h1 = pl.DataFrame(
    {
        "l1": [1, 2],
        "l2": [3, 4],
    }
)
df_h2 = pl.DataFrame(
    {
        "r1": [5, 6],
        "r2": [7, 8],
        "r3": [9, 10],
    }
)
df_horizontal_concat = pl.concat(
    [
        df_h1,
        df_h2,
    ],
    how="horizontal",
)
print(df_horizontal_concat)
```

[`concat`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/functions/fn.concat.html)

```
let df_h1 = df!(
        "l1"=> &[1, 2],
        "l2"=> &[3, 4],
)?;
let df_h2 = df!(
        "r1"=> &[5, 6],
        "r2"=> &[7, 8],
        "r3"=> &[9, 10],
)?;
let df_horizontal_concat =
    polars::functions::concat_df_horizontal(&[df_h1, df_h2], true, false, false)?;
println!("{}", &df_horizontal_concat);
```

```
shape: (2, 5)
┌─────┬─────┬─────┬─────┬─────┐
│ l1  ┆ l2  ┆ r1  ┆ r2  ┆ r3  │
│ --- ┆ --- ┆ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╪═════╪═════╡
│ 1   ┆ 3   ┆ 5   ┆ 7   ┆ 9   │
│ 2   ┆ 4   ┆ 6   ┆ 8   ┆ 10  │
└─────┴─────┴─────┴─────┴─────┘
```

Horizontal concatenation fails when dataframes have overlapping columns.

When dataframes have different numbers of rows, columns will be padded with `null` values at the end up to the maximum length.

Python  Rust

[`concat`](https://docs.pola.rs/api/python/stable/reference/api/polars.concat.html)

```
df_h1 = pl.DataFrame(
    {
        "l1": [1, 2],
        "l2": [3, 4],
    }
)
df_h2 = pl.DataFrame(
    {
        "r1": [5, 6, 7],
        "r2": [8, 9, 10],
    }
)
df_horizontal_concat = pl.concat(
    [
        df_h1,
        df_h2,
    ],
    how="horizontal",
)
print(df_horizontal_concat)
```

[`concat`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/functions/fn.concat.html)

```
let df_h1 = df!(
        "l1"=> &[1, 2],
        "l2"=> &[3, 4],
)?;
let df_h2 = df!(
        "r1"=> &[5, 6, 7],
        "r2"=> &[8, 9, 10],
)?;
let df_horizontal_concat =
    polars::functions::concat_df_horizontal(&[df_h1, df_h2], true, false, false)?;
println!("{}", &df_horizontal_concat);
```

```
shape: (3, 4)
┌──────┬──────┬─────┬─────┐
│ l1   ┆ l2   ┆ r1  ┆ r2  │
│ ---  ┆ ---  ┆ --- ┆ --- │
│ i64  ┆ i64  ┆ i64 ┆ i64 │
╞══════╪══════╪═════╪═════╡
│ 1    ┆ 3    ┆ 5   ┆ 8   │
│ 2    ┆ 4    ┆ 6   ┆ 9   │
│ null ┆ null ┆ 7   ┆ 10  │
└──────┴──────┴─────┴─────┘
```

Diagonal concatenation - getting longer, wider and `null`ier
------------------------------------------------------------

In a diagonal concatenation you combine all of the row and columns from a list of `DataFrames` into a single longer and/or wider `DataFrame`.

Python  Rust

[`concat`](https://docs.pola.rs/api/python/stable/reference/api/polars.concat.html)

```
df_d1 = pl.DataFrame(
    {
        "a": [1],
        "b": [3],
    }
)
df_d2 = pl.DataFrame(
    {
        "a": [2],
        "d": [4],
    }
)

df_diagonal_concat = pl.concat(
    [
        df_d1,
        df_d2,
    ],
    how="diagonal",
)
print(df_diagonal_concat)
```

[`concat`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/functions/fn.concat.html)

```
let df_d1 = df!(
    "a"=> &[1],
    "b"=> &[3],
)?;
let df_d2 = df!(
        "a"=> &[2],
        "d"=> &[4],)?;
let df_diagonal_concat = polars::functions::concat_df_diagonal(&[df_d1, df_d2])?;
println!("{}", &df_diagonal_concat);
```

```
shape: (2, 3)
┌─────┬──────┬──────┐
│ a   ┆ b    ┆ d    │
│ --- ┆ ---  ┆ ---  │
│ i64 ┆ i64  ┆ i64  │
╞═════╪══════╪══════╡
│ 1   ┆ 3    ┆ null │
│ 2   ┆ null ┆ 4    │
└─────┴──────┴──────┘
```

Diagonal concatenation generates nulls when the column names do not overlap.

When the dataframe shapes do not match and we have an overlapping semantic key then [we can join the dataframes](https://docs.pola.rs/user-guide/transformations/joins/) instead of concatenating them.

Rechunking
----------

Before a concatenation we have two dataframes `df1` and `df2`. Each column in `df1` and `df2` is in one or more chunks in memory. By default, during concatenation the chunks in each column are not made contiguous. This makes the concat operation faster and consume less memory but it may slow down future operations that would benefit from having the data be in contiguous memory. The process of copying the fragmented chunks into a single new chunk is known as **rechunking**. Rechunking is an expensive operation. Prior to version 0.20.26, the default was to perform a rechunk but in new versions, the default is not to. If you do want Polars to rechunk the concatenated `DataFrame` you specify `rechunk = True` when doing the concatenation.
