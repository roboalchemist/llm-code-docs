# Design Principles

This section outlines design principles guiding the Koalas project.

## Be Pythonic

Koalas targets Python data scientists. We want to stick to the convention that users are already familiar with as much as possible. Here are some examples:

- 

Function names and parameters use snake_case, rather than CamelCase. This is different from PySpark’s design. For example, Koalas has to_pandas(), whereas PySpark has toPandas() for converting a DataFrame into a pandas DataFrame. In limited cases, to maintain compatibility with Spark, we also provide Spark’s variant as an alias.

- 

Koalas respects to the largest extent the conventions of the Python numerical ecosystem, and allows the use of NumPy types, etc. that can be supported by Spark.

- 

Koalas docs’ style and infrastructure simply follow rest of the PyData projects’.