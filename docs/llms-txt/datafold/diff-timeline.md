# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/diff-timeline.md

# Diff Timeline

> Specify a `time_column` to visualize match rates between tables for each column over time.

```Bash  theme={null}
models:
  - name: users
    meta:
      datafold:
        datadiff:
          time_column: created_at
```
