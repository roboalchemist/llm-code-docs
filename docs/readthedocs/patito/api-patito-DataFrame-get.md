# patito.DataFrame.get

DataFrame.get(*predicate=None*)

Fetch the single row that matches the given polars predicate.

If you expect a data frame to already consist of one single row,
you can use `.get()` without any arguments to return that row.

Raises:

- 

**RowDoesNotExist** – If zero rows evaluate to true for the given predicate.

- 

**MultipleRowsReturned** – If more than one row evaluates to true for the given
    predicate.

- 

**RuntimeError** – The superclass of both `RowDoesNotExist` and
    `MultipleRowsReturned` if you want to catch both exceptions with the
    same class.

Parameters:

**predicate** (`Optional`[`Expr`]) – A polars expression defining the criteria of the filter.

Returns:

A pydantic-derived base model representing the given row.

Return type:

Model

Example

```
>>> import patito as pt
>>> import polars as pl
>>> df = pt.DataFrame({"product_id": [1, 2, 3], "price": [10, 10, 20]})

```