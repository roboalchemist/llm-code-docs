# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/validation/file-format-validation.md

# SnowConvert AI - File Format Validation

## Description

This validation step verifies the file’s structure and indentation. If the average number of characters per line across all input code files is greater than the maximum allowed, the following warning is displayed:

```none
CREATE TABLE LongLines(

    COL1                                                                                                                                                                                                                                                                                                                                                                                                                                                    VARCHAR(22331) -- this line has more than 500 characters
);
```

> **Note:**
>
> Please scroll to the right to watch all the sample code
