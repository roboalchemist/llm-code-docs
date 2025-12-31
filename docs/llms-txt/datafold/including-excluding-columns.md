# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/including-excluding-columns.md

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
