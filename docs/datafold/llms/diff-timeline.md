# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/diff-timeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

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
