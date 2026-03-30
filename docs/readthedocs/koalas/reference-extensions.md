# Extensions

## Accessors

Accessors can be written and registered with Koalas Dataframes, Series, and
Index objects. Accessors allow developers to extend the functionality of
Koalas objects seamlessly by writing arbitrary classes and methods which are
then wrapped in one of the following decorators.

`register_dataframe_accessor`(name)

Register a custom accessor with a DataFrame

`register_series_accessor`(name)

Register a custom accessor with a Series object

`register_index_accessor`(name)

Register a custom accessor with an Index