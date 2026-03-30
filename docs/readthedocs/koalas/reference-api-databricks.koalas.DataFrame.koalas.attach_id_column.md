# databricks.koalas.DataFrame.koalas.attach_id_column

`koalas.``attach_id_column`(*id_type: str*, *column: Union[Any, Tuple]*) → DataFrame

Attach a column to be used as identifier of rows similar to the default index.

See also Default Index type [https://koalas.readthedocs.io/en/latest/user_guide/options.html#default-index-type].

Parameters

**id_type**string

The id type.

- 

‘sequence’ : a sequence that increases one by one.

Note

this uses Spark’s Window without specifying partition specification.
This leads to move all data into single partition in single machine and
could cause serious performance degradation.
Avoid this method against very large dataset.