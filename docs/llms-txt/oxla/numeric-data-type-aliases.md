# Source: https://docs.oxla.com/sql-reference/sql-data-types/numeric-type/numeric-data-type-aliases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Numeric Data Type - Aliases

We allow aliases that can be used interchangeably with the primary data types. However, while these aliases can be used, they will be mapped to their corresponding primary data types during data processing.

Here, we'll discuss the numeric data type aliases:

### **INTEGER Alias**

The `INTEGER` alias is an alternative name for the `INT` data type. For example, the following two queries are functionally the same:

```sql  theme={null}
CREATE TABLE ExampleTable (
    id INTEGER,
);

-- Functionally the same as the previous table
CREATE TABLE AnotherTable (
    id INT,
);
```

<Warning>It's important to note that even though `INTEGER` is used, the data is stored and treated as `INT`.</Warning>

### **LONG Alias**

The `LONG` alias is often used to represent larger integer values. For example:

```sql  theme={null}
CREATE TABLE LargeValues (
    value LONG,
);

-- Functionally the same as the previous table
CREATE TABLE LargeValuesEquivalent (
    value BIGINT,
);
```

<Warning>Any usage of `LONG` is stored and treated as `BIGINT`.</Warning>

### **FLOAT Alias**

The `FLOAT` alias corresponds to the `REAL` data type. For example:

```sql  theme={null}
CREATE TABLE FloatExample (
    price FLOAT,
);

-- Functionally the same as the previous table
CREATE TABLE FloatEquivalent (
    price REAL,
);
```

<Warning>When you use `FLOAT`, it's stored and treated as `REAL`.</Warning>

### **DOUBLE Alias**

The `DOUBLE` alias is used to define `DOUBLE PRECISION` floating-point numbers. For example:

```sql  theme={null}
CREATE TABLE DoubleExample (
    measurement DOUBLE,
);

-- Functionally the same as the previous table
CREATE TABLE DoubleEquivalent (
    measurement DOUBLE PRECISION,
);
```

<Warning>When you use `DOUBLE`, it's stored and treated as `DOUBLE PRECISION`.</Warning>
