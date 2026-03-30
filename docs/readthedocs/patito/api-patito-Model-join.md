# patito.Model.join

*classmethod *Model.join(*other*, *how*)

Dynamically create a new model compatible with an SQL Join operation.

For instance, `ModelA.join(ModelB, how="left")` will create a model containing
all the fields of `ModelA` and `ModelB`, but where all fields of `ModelB`
has been made `Optional`, i.e. nullable. This is consistent with the LEFT JOIN
SQL operation making all the columns of the right table nullable.

Parameters:

- 

**other** (`Type`[`Model`]) – Another patito Model class.

- 

**how** (`Literal`[`'inner'`, `'left'`, `'outer'`, `'asof'`, `'cross'`, `'semi'`, `'anti'`]) – The type of SQL Join operation.

Return type:

`Type`[`Model`]

Returns:

A new model type compatible with the resulting schema produced by the given
join operation.

Examples

```
>>> class A(Model):
...     a: int
...
>>> class B(Model):
...     b: int
...

```