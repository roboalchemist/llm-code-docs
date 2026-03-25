# Source: https://docs.snowflake.com/en/migrations/sma-docs/issue-analysis/issue-codes-by-source/pandas/PNDSPY1162.md

# PNDSPY1162

**Message** Pandas < **pandas.core.reshape.concat.concat** > has a partial mapping with a few scenarios not supported in Snowpark.

**Category** Warning

## Description

This issue appears when the SMA detects the use of a pandas element that has a direct equivalent in Snowpark pandas, but some scenarios might behave differently than pandas.

**Missing or Unsupported Parameters:** `levels is not supported`, `copy is ignored`

## Scenario

A method with a few scenarios that aren’t supported in Snowpark.

### Input

The following example shows a method with a few unsupported scenarios in Snowpark.

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = pd.concat(df)
```

### Output

The SMA adds the EWI `PNDSPY1162` to the output code to let you know that this element has a few scenarios that aren’t supported in Snowpark.

```python
import snowflake.snowpark.modin.pandas as pd

#EWI: PNDSPY1162 => pandas.core.reshape.concat.concat has a partial mapping, with few scenarios not supported. Check Snowpark pandas documentation for more detail.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = pd.concat(df)
```

## Recommended fix

The following parameters are not supported in Snowpark pandas: `levels is not supported`, `copy is ignored`.

**Recommended approaches:**

1. **Avoid unsupported parameters**: Modify your code to not use these parameters if they are not essential.
2. **Use :code:`.to_pandas()` for full compatibility**: If you need these parameters, convert to native pandas first:
   .. code-block:: python

   > # Convert to native pandas when unsupported parameters are needed
>
   > native_df = df.to_pandas()
   > result = native_df.concat(…) # Use all parameters
3. **Split the operation**: Perform supported operations in Snowpark pandas, then use native pandas only for the unsupported functionality.

## Additional recommendations

Check the [Snowpark pandas documentation](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/modin/supported/index) to verify which scenarios aren’t supported for that specific element.
