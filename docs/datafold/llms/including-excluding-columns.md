# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/including-excluding-columns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Including/Excluding Columns

> Specify columns to include or exclude from the data diff using `include_columns` and `exclude_columns`.

```Bash  theme={null}
models:
  - name: users
    meta:
      datafold:
        datadiff:
          include_columns:
            - user_id
            - created_at
            - name
          exclude_columns:
            - full_name
```
