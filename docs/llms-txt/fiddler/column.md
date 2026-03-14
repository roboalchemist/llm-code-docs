# Source: https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/column.md

# Column

Represents a single column in a model schema with its metadata and constraints.

A Column defines the structure and properties of a data column that will be used in a Fiddler model. It includes information about the column's data type, value ranges, categorical values, binning configuration, and other metadata necessary for proper data validation and monitoring.

This class is used within ModelSchema to define the complete structure of data that a model expects to receive.

## Examples

Creating a numeric column:

```python
column = Column(
    name="age",
    data_type=DataType.INTEGER,
    min=0,
    max=120
)
```

Creating a categorical column:

```python
column = Column(
    name="category",
    data_type=DataType.CATEGORY,
    categories=["A", "B", "C"]
)
```

Creating a vector column:

```python
column = Column(
    name="embedding",
    data_type=DataType.VECTOR,
    n_dimensions=128
)
```

Column name provided by the customer

Data type of the column

Min value of integer/float column

Max value of integer/float column

List of unique values of a categorical column

Bins of integer/float column

Replace the list of given values to NULL if found in the events data

Number of dimensions of a vector column

## *class* Config

## smart\_union *= True*
