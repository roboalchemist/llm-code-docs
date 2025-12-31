# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/sql-filters.md

# SQL Filters

> Use dbt YAML configuration to set model-specific filters for Datafold CI.

SQL filters can be helpful in two scenarios:

1. When **Production** and **Staging** environments are not built using the same data. For example, if **Staging** is built using a subset of production data, filters can be applied to ensure that both environments are on par and can be diffed.
2. To improve Datafold CI performance by reducing the volume of data compared, e.g., only comparing the last 3 months of data.

SQL filters are an effective technique to speed up diffs by narrowing the data diffed. A SQL filter adds a `WHERE` clause to allow you to filter data on both sides using standard SQL filter expressions. They can be added to dbt YAML under the `meta.datafold.datadiff.filter` tag:

```
models:
  - name: users
    meta:
      datafold:
        datadiff:
          filter: "user_id > 2350 AND source_timestamp >= current_date() - 7"
```
