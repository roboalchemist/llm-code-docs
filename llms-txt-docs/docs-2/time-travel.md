# Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/time-travel.md

# Time Travel

> Use `prod_time_travel` and `pr_time_travel` to diff tables from specific points in time.

If your database supports <Tooltip tip="The ability to query or compare data from a specific point in the past, often using a timestamp or version history. Commonly used in databases like Snowflake and Big Query, which store historical snapshots of data.">time travel</Tooltip>, you can diff tables from a particular point in time by specifying `prod_time_travel` for a production model and `pr_time_travel` for a PR model.

```Bash  theme={null}
models:
  - name: users
    meta:
      datafold:
        datadiff:
          prod_time_travel:
            - 2022-02-07T00:00:00
          pr_time_travel:
            - 2022-02-07T00:00:00
```
