# Source: https://docs.snowflake.com/en/migrations/sma-docs/issue-analysis/issue-codes-by-source/pandas/PNDSPY1262.md

# PNDSPY1262

**Message** Pandas < **pandas.io.parsers.readers.read_csv** > has a partial mapping with a few scenarios not supported in Snowpark.

**Category** Warning

## Description

This issue appears when the SMA detects the use of a pandas element that has a direct equivalent in Snowpark pandas, but some scenarios might behave differently than pandas.

**Reason:** Reads both local and staged file(s) into a Snowpark pandas DataFrame. Note, the order of rows in the may differ from the order of rows in the original file(s) if using staged csvs. Local files are parsed with native pandas and thus support most of the parameters supported by pandas itself. The usecols and names parameter are applied after creating a temp table in snowflake. Previously staged files will use the Snowflake COPY FROM parser and schema inference. If you need to use staged files often, it is recommended that you upload these as parquet files to improve performance. You can force the use of the Snowflake parser with engine=snowflake.

## Scenario

A method with a few scenarios that aren’t supported in Snowpark.

### Input

The following example shows a method with a few unsupported scenarios in Snowpark.

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = pd.read_csv(df)
```

### Output

The SMA adds the EWI `PNDSPY1262` to the output code to let you know that this element has a few scenarios that aren’t supported in Snowpark.

```python
import snowflake.snowpark.modin.pandas as pd

#EWI: PNDSPY1262 => pandas.io.parsers.readers.read_csv has a partial mapping, with few scenarios not supported. Check Snowpark pandas documentation for more detail.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = pd.read_csv(df)
```

## Recommended fix

**NULL/NaN handling difference**: Reads both local and staged file(s) into a Snowpark pandas DataFrame. Note, the order of rows in the may differ from the order of rows in the original file(s) if using staged csvs. Local files are parsed with native pandas and thus support most of the parameters supported by pandas itself. The usecols and names parameter are applied after creating a temp table in snowflake. Previously staged files will use the Snowflake COPY FROM parser and schema inference. If you need to use staged files often, it is recommended that you upload these as parquet files to improve performance. You can force the use of the Snowflake parser with engine=snowflake.

Snowpark pandas may handle NULL/NaN values differently:

* Pre-filter NULL values using `.dropna()` or `.fillna()` before the operation
* Verify NULL handling behavior with a small sample dataset
* Use explicit NULL checks: `df[df['column'].notna()]`

## Additional recommendations

Check the [Snowpark pandas documentation](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/modin/supported/index) to verify which scenarios aren’t supported for that specific element.
