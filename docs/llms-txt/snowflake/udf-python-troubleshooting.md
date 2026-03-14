# Source: https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-troubleshooting.md

# Troubleshooting Python UDFs

This topic provides troubleshooting information about Python UDFs (user-defined functions).

## Troubleshooting

### Problem: A required Python library is not available through Anaconda

Third-party Python libraries, which do not have C/C++ extensions, can be imported by UDFs directly via Snowflake stages.
For more information, see [Creating a Python UDF with code uploaded from a stage](udf-python-creating.md).

To learn how to submit a request to support additional Anaconda packages, see [Using third-party packages](udf-python-packages.md).

### Problem: A UDF fails with the error “function available memory exhausted”

Reduce the amount of memory used by the UDF.

Check the UDF code for bugs or memory leaks.

For more information, see [Memory](udf-python-designing.md).

### Problem: I want to extract ZIP or other archives inside a UDF

To see an example of how to upload a ZIP file to a Snowflake stage and then unzip it into the `/tmp` directory
inside the UDF, see [Unzipping a staged file](udf-python-examples.md).

### Problem: UDF performance is slow

For information about how to improve the performance of UDFs, see [Optimizing for scale and performance](udf-python-designing.md).

### Problem: The ORGADMIN role is not enabled so Anaconda packages cannot be used

When going through the steps to [get started using third-party packages from Anaconda](udf-python-packages.md),
the organization administrator (ORGADMIN) role is required.

To resolve this problem, follow the instructions in [Enabling the ORGADMIN role in an account](../../../user-guide/organization-administrators.md).

### Problem: A UDF fails with the error “UnicodeDecodeError” when reading a file

When you use the `SnowflakeFile` class to read files that contain non-text data, you must specify the input mode as binary.
Otherwise you might encounter the following error:

```python
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf7 in position 12: invalid start byte
```

To resolve this problem, specify the input mode as binary by passing `'rb'` for the `mode` argument (the second argument). For example:

```python
with SnowflakeFile.open(file_name, 'rb') as f:
```

### Tips

Training machine learning (ML) models can sometimes be very resource intensive.
Snowpark-optimized warehouses are a type of Snowflake virtual warehouse that can be used for workloads
that require a large amount of memory and compute resources.
For information on machine learning models and Snowpark Python, see [Training Machine Learning Models with Snowpark Python](../../snowpark/python/python-snowpark-training-ml.md).

If using a Python UDF in a [masking policy](../../../sql-reference/sql/create-masking-policy.md), ensure the data type of the column, UDF, and
masking policy match.

For troubleshooting information about third-party packages, see [Known issues with third-party packages](udf-python-packages.md).
