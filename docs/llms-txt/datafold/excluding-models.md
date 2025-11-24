# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/excluding-models.md

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
