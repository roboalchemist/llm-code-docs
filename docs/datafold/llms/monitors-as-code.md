# Source: https://docs.datafold.com/data-monitoring/monitors-as-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitors as Code

> Manage Datafold monitors via version-controlled YAML for greater scalability, governance, and flexibility in code-based workflows.

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to enable this feature for your organization.
</Note>

This is particularly useful if any of the following are true:

* You have (or plan to have) 100s or 1000s of monitors
* Your team is accustomed to managing things in code
* Strict governance and change management are important to you

## Getting started

<Note>
  **INFO**

  This section describes how to get started with GitHub Actions, but the same concepts apply to other hosted version control platforms like GitLab and Bitbucket. Contact us if you need help getting started.
</Note>

### Set up version control integration

To start using monitors as code, you'll need to decide which repository will contain your YAML configuration.

If you've already connected a repository to Datafold, you could use that. Or, follow the instructions [here](/integrations/code-repositories) to connect a new repository.

### Generate a Datafold API key

If you've already got a Datafold API key, use it. Otherwise, you can create a new one in the app by visiting **Settings > Account** and selecting **Create API Key**.

### Create monitors config

In your chosen repository, create a new YAML file where you'll define your monitors config.

For this example, we'll name the file `monitors.yaml` and place it in the root directory, but neither of these choices are hard requirements.

Leave the file blank for now—we'll come back to it in a moment.

### Add CI workflow

If you're using GitHub Actions, create a new YAML file under `.github/workflows/` using the following template. Be sure to tailor it to your particular setup:

```yaml  theme={null}
name: Apply monitors as code config to Datafold

on:
  push:
    branches:
      - main # or master

jobs:
  apply:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.12
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install datafold-sdk
      - name: Update monitors
        run: datafold monitors provision monitors.yaml # use the correct file name/path
        env:
          DATAFOLD_HOST: https://app.datafold.com # different for dedicated deployments
          DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }} # remember to add to secrets
```

### Create a monitor

Now return to your YAML configuration file to add your first monitor. Reference the list of examples below and select one that makes sense for your organization.

## Examples

<Note>
  **INFO**

  These examples are intended to serve as inspiration and don't demonstrate every possible configuration. Contact us if you have any questions.
</Note>

### Data Diff

[Data Diff monitors](/data-monitoring/monitors/data-diff-monitors) detect differences between any two datasets, within or across databases.

```yaml  theme={null}
monitors:
  replication_test_example:
    name: 'Example of a custom name'
    description: 'Example of a custom description'
    type: diff
    enabled: true
    datadiff:
      diff_type: 'inmem'
      dataset_a:
        connection_id: 734
        table: db.schema.table
        time_travel_point: '2020-01-01'
        materialize: false
      dataset_b:
        connection_id: 736
        table: db.schema.table1
        time_travel_point: '2020-01-01'
        materialize: true
      primary_key:
        - pk_column
      columns_to_compare:
        - col1
      materialize_results: true
      materialize_results_to: 734
      column_remapping:
        col1: col2
      sampling:
        tolerance: 0.2
        confidence: 0.95
        threshold: 5000
      ignore_string_case: true
    schedule:
      interval:
        every: hour

  replication_test_example_with_thresholds:
    type: diff
    enabled: true
    datadiff:
      diff_type: 'inmem'
      dataset_a:
        connection_id: 734
        table: db.schema.table
      dataset_b:
        connection_id: 736
        table: db.schema.table2
        session_parameters:
          k: v
      primary_key:
        - pk_column
      tolerance:
        float:
          default: 
            type: absolute
            value: 50
          column_tolerance:
            A:
              type: relative
              value: 20 # %
            B:
              type: absolute
              value: 30.0
    schedule:
      interval:
        every: hour
    alert:
      different_rows_count: 100
      different_rows_percent: 10

  replication_test_example_with_thresholds_and_notifications:
    type: diff
    enabled: true
    datadiff:
      diff_type: 'indb'
      dataset_a:
        connection_id: 734
        table: db.schema.table
      dataset_b:
        connection_id: 734
        table: db.schema.table3
      primary_key:
        - pk_column
    schedule:
      interval:
        every: hour
    sampling:
      rate: 0.1
      threshold: 100000
    materialize_results: true
    tolerance:
      float:
        default: 
          type: absolute
          value: 50
        column_tolerance:
          A:
            type: relative
            value: 20 # %
          B:
            type: absolute
            value: 30.0
    notifications:
      - type: email
        recipients:
          - valentin@datafold.com
      - type: slack
        integration: 123
        channel: datafold-alerts
        mentions:
          - "here"
          - "channel"
        features:
          - attach_csv
          - notify_first_triggered_only
      - type: pagerduty
        integration: 124
      - type: webhook
        integration: 125
    alert:
      different_rows_count: 100
      different_rows_percent: 10
```

### Metric

[Metric monitors](/data-monitoring/monitors/metric-monitors) identify anomalies in standard metrics like row count, freshness, and cardinality, or in any custom metric.

```yaml  theme={null}
monitors:
  table_metric_example:
    type: metric
    enabled: true
    connection_id: 736
    metric:
      type: table
      table: db.schema.table
      filter: deleted is false
      metric: freshness # see full list of options below
    alert:
      type: automatic
      sensitivity: 10
    schedule:
      interval:
        every: day
        hour: 8 # 0-23 UTC

  column_metric_example:
    type: metric
    enabled: true
    connection_id: 736
    metric:
      type: column
      table: db.schema.table
      column: some_col
      filter: deleted is false
      metric: sum # see full list of options below
    alert:
      type: percentage
      increase: 30 # %
      decrease: 0
    tags:
      - oncall
      - action-required
    schedule:
      cron: 0 0 * * * # every day at midnight UTC

  custom_metric_example:
    name: custom metric example
    type: metric
    connection_id: 123
    notifications: []
    tags: []
    enabled: true
    metric:
      type: custom
      query: select * from table
      alert_on_missing_data: true
    alert:
      type: absolute
      max: 22.0
      min: 12.0
    schedule:
      interval:
        every: day
        type: daily
```

#### Supported metrics

For more details on supported metrics, see the docs for [Metric monitors](/data-monitoring/monitors/metric-monitors#metric-types).

**Table metrics:**

* Freshness: `freshness`
* Row Count: `row_count`

**Column metrics:**

* Cardinality: `cardinality`
* Uniqueness: `uniqueness`
* Minimum: `minimum`
* Maximum: `maximum`
* Average: `average`
* Median: `median`
* Sum: `sum`
* Standard Deviation: `std_dev`
* Fill Rate: `fill_rate`

### Data Test

[Data Test monitors](/data-monitoring/monitors/data-test-monitors) validate your data with business rules and surface specific records that fail your tests.

```yaml  theme={null}
monitors:
  custom_data_test_example:
    type: test
    enabled: true
    connection_id: 736
    query: select 1 from db.schema.table
    schedule:
      interval:
        every: hour
    tags:
      - team_1

  accepted_values_test_example:
    type: test
    enabled: true
    connection_id: 736
    test:
      type: accepted_values
      tables:
        - path: db.schema.table
          columns:
            - column_name
      variables:
          accepted_values:
            value:
              - 12
              - 15
            quote: false
    schedule:
      interval:
        every: hour

  numeric_range_test_example:
    type: test
    enabled: true
    connection_id: 736
    test:
      type: numeric_range
      tables:
        - path: db.schema.table
          columns:
            - column_name
      variables:
        maximum:
          value: 15
          quote: false
    schedule:
      interval:
        every: hour
```

**Supported variables by Standard Data Test (SDT) type**

| SDT Type              | Monitor-as-Code Type    | Supported Variables | Variable Type          |
| --------------------- | ----------------------- | ------------------- | ---------------------- |
| Unique                | `unique`                | -                   | -                      |
| Not Null              | `not_null`              | -                   | -                      |
| Accepted Values       | `accepted_values`       | `accepted_values`   | Collection with values |
| Referential Integrity | `referential_integrity` | -                   | -                      |
| Numeric Range         | `numeric_range`         | `minimum`           | Single value           |
|                       |                         | `maximum`           | Single value           |

### Schema Change

[Schema Change monitors](/data-monitoring/monitors/schema-change-monitors) detect when changes occur to a table's schema.

```yaml  theme={null}
monitors:
  schema_change_example:
    type: schema
    enabled: true
    connection_id: 736
    table: db.schema.table
    schedule:
      interval:
        every: day
        hour: 22 # 0-23 UTC
    tags:
      - team_2
```

## Bulk Manage with Wildcards

For certain monitor types—[Freshness](/data-monitoring/monitors/metric-monitors), [Row Count](/data-monitoring/monitors/metric-monitors), and [Schema Change](/data-monitoring/monitors/schema-change-monitors)—it's possible to create/manage many monitors at once using the following wildcard syntax:

```yaml  theme={null}
row_count_monitors:
  type: metric
  connection_id: 123
  metric:
    type: table
    metric: row_count
    # include all tables in the WAREHOUSE database
    include_tables: WAREHOUSE.*
    # exclude all tables in the INFORMATION_SCHEMA schema
    exclude_tables: WAREHOUSE.INFORMATION_SCHEMA.*
  schedule:
    interval:
      every: day
      hour: 10 # 0-23 UTC
```

This is particularly useful if you want to create the same monitor type for many tables in a particular database or schema. Note in the example above that you can specify both `include_tables` and `exclude_tables` to fine-tune your selection.

## FAQ

<AccordionGroup>
  <Accordion title="Can I still create/manage monitors in the app if I'm using monitors as code?">
    Yes, it's not all or nothing. You can still create/manage monitors in the app even if you're defining others in code.
  </Accordion>

  <Accordion title="What happens to a monitor in the app if it's removed from the code?">
    By default, nothing—it remains in the app. However, you can add the `--dangling-monitors-strategy [delete|pause]` flag to your `run` command to either delete or pause notifications if they're removed from your code. For example:

    ```bash  theme={null}
    datafold monitors provision monitors.yaml --dangling-monitors-strategy delete
    ```

    Note: this only applies to monitors that were created from code, not those created in the UI.
  </Accordion>

  <Accordion title="How do I delete or pause all of my monitors?">
    Add the `--dangling-monitors-strategy [delete|pause]` flag to your `run` command and replace the contents of your YAML file with the following:

    ```yaml  theme={null}
    monitors: {}
    ```

    Note that providing an empty YAML file will likely produce an error and not have the same effect.
  </Accordion>

  <Accordion title="Can I use the app to modify monitors managed in code?">
    No, any monitors created from code will be read-only in the app (though they can still be cloned).
  </Accordion>

  <Accordion title="Can I export monitors I've created in the app so I can manage them in code?">
    Yes, you can export all monitors from the app to manage them as code. There are two ways to do this:

    1. Exporting all monitors: Navigate to the Monitors list page and click the **View as Code** button
    2. Exporting a single monitor: Go to the specific monitor and click **Actions** and then select **View as Code**

    Note that when exporting monitors, pay attention to the `id` field in the YAML. If you want to preserve monitor history, keep the `id` field as this will update the original monitor to be managed as code. If you don't want to preserve your monitor history, **delete** the `id` field to create a new monitor as code while keeping the original monitor intact.

    <Frame>
      <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=270724bc299c4667a4779996f836c951" data-og-width="2156" width="2156" data-og-height="1360" height="1360" data-path="images/monitors/view_as_code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ce292c7e2b3a9b4ef0e9e013f5d7c634 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9608398b57c0c74c9a63030d89685b4b 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8b57b836482764fc8861b9de63af1b72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=72dfda906a348eb2e098481600620bab 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1b0f6867e6ee6506335dc1bdbcdc489b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/view_as_code.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5bed39ca385d47cdd515c0a24c6c8 2500w" />
    </Frame>
  </Accordion>
</AccordionGroup>

## Need help?

If you have any questions about how to use monitors as code, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
