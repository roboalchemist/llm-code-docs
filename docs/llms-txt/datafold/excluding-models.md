# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/excluding-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Excluding Models

> Use `never_diff` to exclude a model or subdirectory of models from data diffs.

```Bash  theme={null}
models:
  - name: users
    meta:
      datafold:
        datadiff:
          never_diff: true
```
