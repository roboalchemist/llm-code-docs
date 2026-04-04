# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/array_agg.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/array_agg.md

# Source: https://docs.pinot.apache.org/functions-1/array_agg.md

# ARRAY\_AGG

Concatenates the input values into an array.

## Signature

> ARRAY\_AGG(dataColumn, 'dataType', \[isDistinct])

## Usage Examples

```sql
SELECT ARRAY_AGG(firstName, 'STRING', true) AS firstNames from transcript;
```

| firstNames    |
| ------------- |
| Bob,Nick,Lucy |
