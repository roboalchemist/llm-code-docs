# patito.duckdb.Relation.cast

Relation.cast(*model=None*, *strict=False*, *include=None*, *exclude=None*)

Cast the columns of the relation to types compatible with the associated model.

The associated model must either be set by invoking
Relation.set_model() or provided with the
`model` parameter.

Any columns of the relation that are not part of the given model schema will be
left as-is.

Parameters:

- 

**model** (`Optional`[`TypeVar`(`ModelType`, bound= Model)]) – If Relation.set_model() has not
been invoked or is intended to be overwritten.

- 

**strict** (`bool`) – If set to `False`, columns which are technically compliant with
the specified field type, will not be casted. For example, a column
annotated with `int` is technically compliant with `SMALLINT`, even
if `INTEGER` is the default SQL type associated with `int`-annotated
fields. If `strict` is set to `True`, the resulting dtypes will
be forced to the default dtype associated with each python type.

- 

**include** (`Optional`[`Collection`[`str`]]) – If provided, only the given columns will be casted.

- 

**exclude** (`Optional`[`Collection`[`str`]]) – If provided, the given columns will not be casted.

Return type:

`TypeVar`(`RelationType`, bound= Relation)

Returns:

New relation where the columns have been casted according to the model
schema.

Examples

```
>>> import patito as pt
>>> class Schema(pt.Model):
...     float_column: float
...
>>> relation = pt.duckdb.Relation("select 1 as float_column")
>>> relation.types["float_column"]
INTEGER
>>> relation.cast(model=Schema).types["float_column"]
DOUBLE

```