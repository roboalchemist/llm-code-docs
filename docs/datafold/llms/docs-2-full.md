# Docs 2 Documentation

Source: https://docs.datafold.com/llms-full.txt

---

# Get Audit Logs
Source: https://docs.datafold.com/api-reference/audit-logs/get-audit-logs

get /api/v1/audit_logs



# Create a DBT BI integration
Source: https://docs.datafold.com/api-reference/bi/create-a-dbt-bi-integration

post /api/v1/lineage/bi/dbt/



# Create a Hightouch integration
Source: https://docs.datafold.com/api-reference/bi/create-a-hightouch-integration

post /api/v1/lineage/bi/hightouch/



# Create a Looker integration
Source: https://docs.datafold.com/api-reference/bi/create-a-looker-integration

post /api/v1/lineage/bi/looker/



# Create a Mode Analytics integration
Source: https://docs.datafold.com/api-reference/bi/create-a-mode-analytics-integration

post /api/v1/lineage/bi/mode/



# Create a Power BI integration
Source: https://docs.datafold.com/api-reference/bi/create-a-power-bi-integration

openapi-public.json post /api/v1/lineage/bi/powerbi/



# Create a Tableau integration
Source: https://docs.datafold.com/api-reference/bi/create-a-tableau-integration

post /api/v1/lineage/bi/tableau/



# Get an integration
Source: https://docs.datafold.com/api-reference/bi/get-an-integration

get /api/v1/lineage/bi/{bi_datasource_id}/
Returns the integration for Mode/Tableau/Looker/HighTouch by its id.



# List all integrations
Source: https://docs.datafold.com/api-reference/bi/list-all-integrations

get /api/v1/lineage/bi/
Return all integrations for Mode/Tableau/Looker



# Remove an integration
Source: https://docs.datafold.com/api-reference/bi/remove-an-integration

delete /api/v1/lineage/bi/{bi_datasource_id}/



# Rename a Power BI integration
Source: https://docs.datafold.com/api-reference/bi/rename-a-power-bi-integration

openapi-public.json put /api/v1/lineage/bi/powerbi/{bi_datasource_id}/
It can only update the name. Returns the integration with changed fields.



# Sync a BI integration
Source: https://docs.datafold.com/api-reference/bi/sync-a-bi-integration

get /api/v1/lineage/bi/{bi_datasource_id}/sync/
Start an unscheduled synchronization of the integration.



# Update a DBT BI integration
Source: https://docs.datafold.com/api-reference/bi/update-a-dbt-bi-integration

put /api/v1/lineage/bi/dbt/{bi_datasource_id}/
Returns the integration with changed fields.



# Update a Hightouch integration
Source: https://docs.datafold.com/api-reference/bi/update-a-hightouch-integration

put /api/v1/lineage/bi/hightouch/{bi_datasource_id}/
It can only update the schedule. Returns the integration with changed fields.



# Update a Looker integration
Source: https://docs.datafold.com/api-reference/bi/update-a-looker-integration

put /api/v1/lineage/bi/looker/{bi_datasource_id}/
It can only update the schedule. Returns the integration with changed fields.



# Update a Mode Analytics integration
Source: https://docs.datafold.com/api-reference/bi/update-a-mode-analytics-integration

put /api/v1/lineage/bi/mode/{bi_datasource_id}/
It can only update the schedule. Returns the integration with changed fields.



# Update a Tableau integration
Source: https://docs.datafold.com/api-reference/bi/update-a-tableau-integration

put /api/v1/lineage/bi/tableau/{bi_datasource_id}/
It can only update the schedule. Returns the integration with changed fields.



# List CI runs
Source: https://docs.datafold.com/api-reference/ci/list-ci-runs

get /api/v1/ci/{ci_config_id}/runs



# Trigger a PR/MR run
Source: https://docs.datafold.com/api-reference/ci/trigger-a-prmr-run

post /api/v1/ci/{ci_config_id}/trigger



# Upload PR/MR changes
Source: https://docs.datafold.com/api-reference/ci/upload-prmr-changes

post /api/v1/ci/{ci_config_id}/{pr_num}



# Create a data diff
Source: https://docs.datafold.com/api-reference/data-diffs/create-a-data-diff

post /api/v1/datadiffs



# Get a data diff
Source: https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff

get /api/v1/datadiffs/{datadiff_id}



# Get a data diff summary
Source: https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff-summary

get /api/v1/datadiffs/{datadiff_id}/summary_results



# List data diffs
Source: https://docs.datafold.com/api-reference/data-diffs/list-data-diffs

get /api/v1/datadiffs
All fields support multiple items, using just comma delimiter
Date fields also support ranges using the following syntax:

- ``<DATETIME`` = before DATETIME
- ``>DATETIME`` = after DATETIME
- ``DATETIME`` = between DATETIME and DATETIME + 1 MINUTE
- ``DATE`` = start of that DATE until DATE + 1 DAY
- ``DATETIME1<<DATETIME2`` = between DATETIME1 and DATETIME2
- ``DATE1<<DATE2`` = between DATE1 and DATE2



# Update a data diff
Source: https://docs.datafold.com/api-reference/data-diffs/update-a-data-diff

patch /api/v1/datadiffs/{datadiff_id}



# Create a data source
Source: https://docs.datafold.com/api-reference/data-sources/create-a-data-source

post /api/v1/data_sources



# Get a data source
Source: https://docs.datafold.com/api-reference/data-sources/get-a-data-source

get /api/v1/data_sources/{data_source_id}



# Get a data source summary
Source: https://docs.datafold.com/api-reference/data-sources/get-a-data-source-summary

get /api/v1/data_sources/{data_source_id}/summary



# Get data source testing results
Source: https://docs.datafold.com/api-reference/data-sources/get-data-source-testing-results

get /api/v1/data_sources/test/{job_id}



# List data source types
Source: https://docs.datafold.com/api-reference/data-sources/list-data-source-types

get /api/v1/data_sources/types



# List data sources
Source: https://docs.datafold.com/api-reference/data-sources/list-data-sources

get /api/v1/data_sources



# Test a data source connection
Source: https://docs.datafold.com/api-reference/data-sources/test-a-data-source-connection

post /api/v1/data_sources/{data_source_id}/test



# Datafold SDK
Source: https://docs.datafold.com/api-reference/datafold-sdk



The Datafold SDK allows you to accomplish certain actions using a thin programmatic wrapper around the Datafold REST API, in particular:

* **Custom CI Integrations**: Submitting information to Datafold about what tables to diff in CI
* **dbt CI Integrations**: Submitting dbt artifacts via CI runner
* **dbt development**: Kick off data diffs from the command line while developing in your dbt project

## Install

First, create and activate your virtual environment for Python:

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
```

Now, you're ready to install the Datafold SDK:

```
pip install datafold-sdk
```

#### CLI environment variables

To use the Datafold CLI, you need to set up some environment variables:

```bash  theme={null}
export DATAFOLD_API_KEY=XXXXXXXXX
```

If your Datafold app URL is different from the default `app.datafold.com`, set the custom domain as the variable:

```bash  theme={null}
export DATAFOLD_HOST=<CUSTOM_DATAFOLD_APP_DOMAIN>
```

## Custom CI Integrations

Please follow [our CI orchestration docs](../integrations/orchestrators/custom-integrations) to set up a custom CI integration levering the Datafold SDK.

## dbt Core CI Integrations

When you set up Datafold CI diffing for a dbt Core project, we rely on the submission of `manifest.json` files to represent the production and staging versions of your dbt project.

Please see our detailed docs on how to [set up Datafold in CI for dbt Core](../integrations/orchestrators/dbt-core), and reach out to our team if you have questions.

#### CLI

```bash  theme={null}
    datafold dbt upload \
    --ci-config-id <ci_config_id> \
    --run-type <run-type> \
    --target-folder <artifacts_path> \
    --commit-sha <git_sha>
```

#### Python

```python  theme={null}
import os

from datafold_sdk.sdk.dbt import submit_artifacts

api_key = os.environ.get('DATAFOLD_API_KEY')

# only needed if your Datafold app url is not app.datafold.com
host = os.environ.get("DATAFOLD_HOST")

submit_artifacts(host=host,
                 api_key=api_key,
                 ci_config_id=<ci_config_id>,
                 run_type='<run-type>',
                 target_folder='<artifacts_path>',
                 commit_sha='<git_sha>')
```

## Diffing dbt models in development

It can be beneficial to diff between two dbt environments before opening a pull request. This can be done using the Datafold SDK from the command line:

```bash  theme={null}
datafold diff dbt
```

That command will compare data between your development and production environments. By default, all models that were built in the previous `dbt run` or `dbt build` command will be compared.

### Running Data Diffs before opening a pull request

It can be helpful to view Data Diff results in your ticket before creating a pull request. This enables faster code reviews by letting developers QA changes earlier.

To do this, you can create a draft PR and run the following command:

```
dbt run && datafold diff dbt
```

This executes dbt locally and triggers a Data Diff to preview data changes without committing to Git. To automate this workflow, see our guide [here](/faq/datafold-with-dbt#can-i-run-data-diffs-before-opening-a-pr).

### Update your dbt\_project.yml with configurations

#### Option 1: Add variables to the `dbt_project.yml`

```yaml  theme={null}
# dbt_project.yml
vars:
  data_diff:
    prod_database: my_default_database # default database for the prod target
    prod_schema: my_default_schema # default schema for the prod target
    prod_custom_schema: PROD_<custom_schema> # Optional: see dropdown below
```

**Additional schema variable details**
The value for `prod_custom_schema:` will vary based on how you have setup dbt.

This variable is used when a model has a custom schema and becomes ***dynamic*** when the string literal `<custom_schema>` is present. The `<custom_schema>` substring is replaced with the custom schema for the model in order to support the various ways schema name generation can be overridden <a href="https://docs.getdbt.com/docs/build/custom-schemas">here</a> -- also referred to as "advanced custom schemas".

**Examples (not exhaustive)**

**Single production schema**

*If your prod environment looks like this ...*

```bash  theme={null}
PROD.ANALYTICS
```

*... your data-diff configuration should look like this:*

```yaml  theme={null}
  vars:
      data_diff:
          prod_database: PROD
          prod_schema: ANALYTICS
```

**Some custom schemas in production with a prefix like "prod\_"**

*If your prod environment looks like this ...*

```bash  theme={null}
PROD.ANALYTICS
PROD.PROD_MARKETING
PROD.PROD_SALES
```

*... your data-diff configuration should look like this:*

```yaml  theme={null}
  vars:
      data_diff:
          prod_database: PROD
          prod_schema: ANALYTICS
          prod_custom_schema: PROD_<custom_schema>
```

**Some custom schemas in production with no prefix**

*If your prod environment looks like this ...*

```yaml  theme={null}
PROD.ANALYTICS
PROD.MARKETING
PROD.SALES
```

*... your data-diff configuration should look like this:*

```yaml  theme={null}
vars:
  data_diff:
    prod_database: PROD
    prod_scheam: ANALYTICS
    prod_custom_schema: <custom_schema>
```

#### Option 2: Specify a production `manifest.json` using `--state`

**Using the `--state` option is highly recommended for dbt projects with multiple target database and schema configurations. For example, if you customized the [`generate_schema_name`](https://docs.getdbt.com/docs/build/custom-schemas#understanding-custom-schemas) macro, this is the best option for you.**

> Note: `dbt ls` is preferred over `dbt compile` as it runs faster and data diffing does not require fully compiled models to work.

```bash  theme={null}
dbt ls -t prod # compile a manifest.json using the "prod" target
mv target/manifest.json prod_manifest.json # move the file up a directory and rename it to prod_manifest.json
dbt run # run your entire dbt project or only a subset of models with `dbt run --select <model_name>`
data-diff --dbt --state prod_manifest.json # run data-diff to compare your development results to the production database/schema results in the prod manifest
```

#### Add your Datafold data connection integration ID to your dbt\_project.yml

To connect to your database, navigate to **Settings** → **Integrations** → **Data connections** and click **Add new integration** and follow the prompts.

After you **Test and Save**, add the ID (which can be found on Integrations > Data connections) to your **dbt\_project.yml**.

```yaml  theme={null}
# dbt_project.yml
vars:
  data_diff:
      ...
      datasource_id: <DATA_SOURCE_ID>
```

The following optional arguments are available:

| Options                            | Description                                                                                                                                                                                                        |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--version`                        | Print version info and exit.                                                                                                                                                                                       |
| `-w, --where EXPR`                 | An additional 'where' expression to restrict the search space. Beware of SQL Injection!                                                                                                                            |
| `--dbt-profiles-dir PATH`          | Which directory to look in for the `profiles.yml` file. If not set, we follow the default `profiles.yml` location for the dbt version being used. Can also be set via the `DBT_PROFILES_DIR` environment variable. |
| `--dbt-project-dir PATH`           | Which directory to look in for the `dbt_project.yml` file. Default is the current working directory and its parents.                                                                                               |
| `--select SELECTION or MODEL_NAME` | Select dbt resources to compare using dbt selection syntax in dbt versions >= 1.5. In versions \< 1.5, it will naively search for a model with `MODEL_NAME` as the name.                                           |
| `--state PATH`                     | Specify manifest to utilize for 'prod' comparison paths instead of using configuration.                                                                                                                            |
| `-pd, --prod-database TEXT`        | Override the dbt production database configuration within `dbt_project.yml`.                                                                                                                                       |
| `-ps, --prod-schema TEXT`          | Override the dbt production schema configuration within `dbt_project.yml`.                                                                                                                                         |
| `--help`                           | Show this message and exit.                                                                                                                                                                                        |


# Get column downstreams
Source: https://docs.datafold.com/api-reference/explore/get-column-downstreams

openapi-public.json get /api/v1/explore/db/{data_connection_id}/columns/{column_path}/downstreams
Retrieve a list of columns or tables which depend on the given column.



# Get column upstreams
Source: https://docs.datafold.com/api-reference/explore/get-column-upstreams

openapi-public.json get /api/v1/explore/db/{data_connection_id}/columns/{column_path}/upstreams
Retrieve a list of columns or tables which the given column depends on.



# Get table downstreams
Source: https://docs.datafold.com/api-reference/explore/get-table-downstreams

openapi-public.json get /api/v1/explore/db/{data_connection_id}/tables/{table_path}/downstreams
Retrieve a list of tables which depend on the given table.



# Get table upstreams
Source: https://docs.datafold.com/api-reference/explore/get-table-upstreams

openapi-public.json get /api/v1/explore/db/{data_connection_id}/tables/{table_path}/upstreams
Retrieve a list of tables which the given table depends on.



# Introduction
Source: https://docs.datafold.com/api-reference/introduction



Our REST API allows you to interact with Datafold programmatically. To use it, you'll need an API key. Follow the instructions below to get started.

## Create an API Key

Open the Datafold app, visit Settings > Account, and select **Create API Key**.

<Note>
  Store your API key somewhere safe. If you lose it, you'll need to generate a new one.
</Note>

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e01e1d4e974f64bc105d9f84be2832ad" alt="Create an API key" data-og-width="2742" width="2742" data-og-height="1126" height="1126" data-path="images/create-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=097e301bb425134d419f5faa9f02de32 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c8496a16d3e4f24af0c1712d485bfe91 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=60e57f3cc4b71dbf91fe669ff9218fd5 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=fc6b27ac503686211a5846e47156b028 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=12e9e42e7a7b002e41ea4cb78dfc20a1 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0b53a6f6a3a1235e43db9f5ae21c9ac5 2500w" />

## Use your API Key

When making requests to the Datafold API, you'll need to include the API key as a header in your HTTP request for authentication. The header should be named `Authorization`, and the value should be in the format:

```
Authorization: Key {API_KEY}
```

For example, if you're using cURL:

```bash  theme={null}
curl https://api.datafold.com/api/v1/... -H "Authorization: Key {API_KEY}"
```

## Datafold SDK

Rather than hit our REST API endpoints directly, we offer a convenient Python SDK for common development and deployment testing workflows. You can find more information about our SDK [here](/api-reference/datafold-sdk).

## Need help?

If you have any questions about how to use our REST API, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# Create a Data Diff Monitor
Source: https://docs.datafold.com/api-reference/monitors/create-a-data-diff-monitor

openapi-public.json post /api/v1/monitors/create/diff



# Create a Data Test Monitor
Source: https://docs.datafold.com/api-reference/monitors/create-a-data-test-monitor

openapi-public.json post /api/v1/monitors/create/test



# Create a Metric Monitor
Source: https://docs.datafold.com/api-reference/monitors/create-a-metric-monitor

openapi-public.json post /api/v1/monitors/create/metric



# Create a Schema Change Monitor
Source: https://docs.datafold.com/api-reference/monitors/create-a-schema-change-monitor

openapi-public.json post /api/v1/monitors/create/schema



# Delete a Monitor
Source: https://docs.datafold.com/api-reference/monitors/delete-a-monitor

openapi-public.json delete /api/v1/monitors/{id}



# Get Monitor
Source: https://docs.datafold.com/api-reference/monitors/get-monitor

openapi-public.json get /api/v1/monitors/{id}



# Get Monitor Run
Source: https://docs.datafold.com/api-reference/monitors/get-monitor-run

openapi-public.json get /api/v1/monitors/{id}/runs/{run_id}



# List Monitor Runs
Source: https://docs.datafold.com/api-reference/monitors/list-monitor-runs

openapi-public.json get /api/v1/monitors/{id}/runs



# List Monitors
Source: https://docs.datafold.com/api-reference/monitors/list-monitors

openapi-public.json get /api/v1/monitors



# Toggle a Monitor
Source: https://docs.datafold.com/api-reference/monitors/toggle-a-monitor

openapi-public.json put /api/v1/monitors/{id}/toggle



# Trigger a run
Source: https://docs.datafold.com/api-reference/monitors/trigger-a-run

openapi-public.json post /api/v1/monitors/{id}/run



# Update a Monitor
Source: https://docs.datafold.com/api-reference/monitors/update-a-monitor

openapi-public.json patch /api/v1/monitors/{id}/update



# Connection Budgets
Source: https://docs.datafold.com/data-diff/connection-budgets

How connection budgets are enforced across data diffs in Datafold

## Overview

Datafold now supports **shared connection budgeting** across

* in-database diffs
* cross-database diffs
* in-memory diffs

This feature ensures consistent, predictable behavior for database usage across the system—particularly important in environments with limited database connection capacity.

***

## ✨ Shared Connection Budgeting

Datafold now enforces a **shared connection limit per database** across all supported diff runs.

When a maximum number of connections is configured on a data source, this limit is respected **collectively** across all running diffs that target that source—regardless of the type of diff.

This ensures that no combination of diff runs will exceed the specified connection cap for the database, providing:

* ✅ More predictable resource usage
* ✅ Protection against overloading the database
* ✅ Simpler configuration and expectation management

Connection limits are enforced automatically once set—no need to configure them at the individual diff level.

***

## ✅ Scope of This Feature

| Jobs                 | Connection Budget Applied? |
| -------------------- | -------------------------- |
| in-database diffs    | ✅ Yes                      |
| cross-database diffs | ✅ Yes                      |
| in-memory diffs      | ✅ Yes                      |
| Schema Fetching      | ❌ No                       |
| Lineage & Profiling  | ❌ No                       |
| SQL History          | ❌ No                       |
| Monitors             | ❌ No                       |

***

## ⚙️ Configuration

Shared connection budgeting is controlled via your **data source configuration**.

Once a `Max Connections` limit is set, it will be automatically enforced **across all supported diff runs** targeting that database.

## 📬 Feedback

Questions, suggestions, or unexpected behavior? Reach out to the Datafold team via your usual support or engineering channels.

***


# Best Practices
Source: https://docs.datafold.com/data-diff/cross-database-diffing/best-practices

When dealing with large datasets, it's crucial to approach diffing with specific optimization strategies in mind. We share best practices that will help you get the most accurate and efficient results from your data diffs.

## Enable sampling

[Sampling](/data-diff/cross-database-diffing/creating-a-new-data-diff#row-sampling) can be helpful when diffing between extremely large datasets as it can result in a speedup of 2x to 20x or more. The extent of the speedup depends on various factors, including the scale of the data, instance sizes, and the number of data columns.

The following table illustrates the speedup achieved with sampling in different databases, varying instance sizes, and different numbers of data columns:

|      Databases      | vCPU | RAM, GB |    Rows   | Columns | Time full | Time sampled | Speedup |    RDS type   | Diff full | Diff sampled | Per-col noise |
| :-----------------: | :--: | :-----: | :-------: | :-----: | :-------: | :----------: | :-----: | :-----------: | :-------: | :----------: | :-----------: |
| Oracle vs Snowflake |   2  |    2    | 1,000,000 |    1    |  0:00:33  |    0:00:27   |   1.22  |  db.t3.small  |    5399   |     5400     |       0       |
| Oracle vs Snowflake |   8  |    32   | 1,000,000 |    1    |  0:07:23  |    0:00:18   |  24.61  | db.m5.2xlarge |    5422   |     5423     |     0.005     |
|  MySQL vs Snowflake |   2  |    8    | 1,000,000 |    1    |  0:00:57  |    0:00:24   |   2.38  |  db.m5.large  |    5409   |     5413     |       0       |
|  MySQL vs Snowflake |   2  |    8    | 1,000,000 |    29   |  0:40:00  |    0:02:14   |  17.91  |  db.m5.large  |    5412   |     5411     |       0       |

When sampling is enabled, Datafold compares a randomly chosen subset of the data. Sampling is the tradeoff between the diff detail and time/cost of the diffing process. For most use cases, sampling does not reduce the informational value of data diffs as it still provides the magnitude and specific examples of differences (e.g., if 10% of sampled data show discrepancies, it suggests a similar proportion of differences across the entire dataset).

<Tip>
  Although configuring sampling can seem overwhelming at first, a good rule of thumb is to select an initial value of 95% for the sampling confidence and adjust it as needed. Tweaking the parameters can be helpful to see how they impact the sample size and the tradeoff between performance and accuracy.
</Tip>

## Handling data type differences

Datafold automatically manages data type differences during cross-database diffing. For example, when comparing decimals with different precisions (e.g., `DECIMAL(38,15)` in SQL Server and `DECIMAL(38,19)` in Snowflake), Datafold automatically casts values to a common precision before comparison, flagging any differences appropriately. Similarly, for timestamps with different precisions (e.g., milliseconds in SQL Server and nanoseconds in Snowflake), Datafold adjusts the precision as needed for accurate comparisons, simplifying the diffing process.

## Optimizing OLTP databases: indexing best practices

When working with row-oriented transactional databases like PostgreSQL, optimizing the database structure is crucial for efficient data diffing, especially for large tables. Here are some best practices to consider:

* **Create indexes on key columns**:

* It's essential to create indexes on the columns that will be compared, particularly the primary key columns defined in the data diffs.

* **Example**: If your data diff involves primary key columns `colA` and `colB`, ensure that indexes are created for these specific columns.

* **Use separate indexes for primary key columns:**

* Indexes for primary key columns should be distinct and start with these columns, not as subsets of other indexes. Having a dedicated primary key index is critical for efficient diffing.

* **Example**: Consider a primary key consisting of `colA` and `colB`. Ensure that the index is structured in the same order, like (`colA`, `colB`), to align with the primary key. An index with an order of (`colB`, `colA`) is strongly discouraged due to the impact on performance.

* **Example**: If the index is defined as (`colA`, `colB`, `colC`) and the primary key is a combination of `colA` and `colB`, then when setting up the diff operation, ensure that the primary key is specified as `colA`, `colB.` If the order is reversed as `colB`, `colA`, the diffing process won’t be able to fully utilize indexing, potentially leading to slower performance.

* **Leverage compound indexes**:

* Compound indexes, which involve multiple columns, can significantly improve query performance during data diffs as they efficiently handle complex queries and filtering.

* **Example**: An index defined as (`colA`, `colB`, `colC`) can be beneficial for diffing operations involving these columns, as it aligns with the order of columns in the primary key.

## Handling high percentage of differences

Data diff is optimized to perform best when the percent of different rows/values is relatively low, to support common data validation scenarios like data replication and migration.

While the tool strives to maximize the database's computational power and minimize data transfer, in extreme cases with very high difference percentages (up to 100%), it may result in transferring every row over the network, which is considerably slower.

In order to avoid long-running diffs, we recommend the following:

* **Start with diffing [primary keys](/data-diff/cross-database-diffing/creating-a-new-data-diff#primary-key)** only to identify row-level completeness first, before diffing all or more columns.
* **Set an [egress](/data-diff/cross-database-diffing/creating-a-new-data-diff#primary-key) limit** to automatically stop the diffing process after set number of rows are downloaded over the network.
* **Set a [per-column diff](/data-diff/cross-database-diffing/creating-a-new-data-diff#primary-key) limit** to stop finding differences for each column after a set number are found. This is especially useful in data reconciliation where identifying a large number of discrepancies (e.g., large percentage of missing/different rows) early on indicates that a detailed row-by-row diff may not be required, thereby saving time and computational resources.

In the screenshot below, we see that exactly 4 differences were found in `user_id`, but “at least 4,704 differences” were found in `total_runtime_seconds`. `user_id` has a number of differences below the per-column diff limit, and so we state the exact number. On the other hand, `total_runtime_seconds` has a number of differences greater than the per-column diff limit, so we state “at least.” Note that due to our algorithm’s approach, we often find significantly more differences than the limit before diffing is halted, and in that scenario, we report the value that was found, while stating that more differences may exist.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e5e4bc527ed248a8f06c1e6910dcf75e" data-og-width="1476" width="1476" data-og-height="1523" height="1523" data-path="images/screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a5d6f86893b6306a12b78e7aa08bcf2a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8b1ec0d83758bfbbe37f93688390ce42 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cbb81cf1d896810821449a957e2a1f4e 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3d2aa8c5375d44bb76757f76691be05a 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=df4562154b3d6a8af753fa041a61117e 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1ee252f9dccad4d836c2990ac8719f88 2500w" />
</Frame>

## Executing queries in parallel

Increase the number of concurrent connections to the database in Datafold. This enables queries to be executed in parallel, significantly accelerating the diff process.

Navigate to the **Settings** option in the left sidebar menu of Datafold. Adjust the **max connections** setting to increase the number of concurrent connections Datafold can establish with your data. Note that the maximum allowable value for concurrent connections is 64.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cd52afb88ab462f6b3f69f3ea6ead45b" data-og-width="1534" width="1534" data-og-height="836" height="836" data-path="images/connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4cb4a75c28a66a51fa69e7cec884ce7c 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b7dde14c80d168e9c43fd2968b3abe51 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=45bb326072ea3b59e2f7cecaf834ecfd 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4f2090603a806a9f4f360d889684a2ef 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=325f96db65116e034e81c64df6882339 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=98926e3cb27d393a85d09803377423d7 2500w" />
</Frame>

## Optimize column selection

The number of columns included in the diff directly impacts its speed: selecting fewer columns typically results in faster execution. To optimize performance, refine your column selection based on your specific use case:

* **Comprehensive verification**: For in-depth analysis, include all columns in the diff. This method is the most thorough, suitable for exhaustive data reviews, albeit time-intensive for wide tables.
* **Minimal verification**: Consider verifying only the primary key and `updated_at` columns. This is efficient and sufficient if you need to validate rows have not been added or removed, and that updates are current between databases, but do not need to check for value-level differences between rows with common primary keys.
* **Presence verification**: If your main concern is just the presence of data (whether data exists or has been removed), such as identifying missing hard deletes, verifying only the primary key column can be sufficient.
* **Hybrid verification**: Focus on key columns that are most critical to your operations or data integrity, such as monetary values in an `amount` column, while omitting large serialized or less critical columns like `json_settings`.

## Managing primary key distribution

Significant gaps in the primary key column can decrease diff efficiency (e.g., 10s of millions of continuous rows missing). Datafold will execute queries for non-existent row ranges, which can slow down the data diff.

## Handling different primary key types

As a general rule, primary keys should be of the same (or similar) type in both datasets for diffing to work properly. Comparing primary keys of different types (e.g., `INT` vs `VARCHAR`) will result in a type mismatch error. You can still diff such datasets by casting the primary key column to the same type in both datasets explicitly.

<Note>
  Indexes on the primary key typically cannot be utilized when the primary key is cast to a different type. This may result in slower diffing performance. Consider creating a separate index, such as [expression index in PostgreSQL](https://www.postgresql.org/docs/current/indexes-expressional.html), to improve performance.
</Note>

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aea91ec007c4c3b6f02a651d1f509141" data-og-width="1434" width="1434" data-og-height="1726" height="1726" data-path="images/data1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f77fe2030286efa0f69414ab836db7e0 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=72d4d2cfbb2ff26c44af7705b2d88c32 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=319b67c88bdd689f984061b21579496b 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dbdc457cf596af8e77748b0f288ea6f9 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e340b852cbe1711e8ba79c496fef6d2e 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c1d00e992e47d24a9dbab3317028c7fe 2500w" />
</Frame>


# Creating a New Data Diff
Source: https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff

Datafold's Data Diff can compare data across databases (e.g., PostgreSQL <> Snowflake, or between two SQL Server instances) to validate migrations, meet regulatory and compliance requirements, or ensure data is flowing successfully from source to target.

This powerful algorithm provides full row-, column-, and value-level detail into discrepancies between data tables.

## Creating a new data diff

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=51b3d0c833d953bc4c773a3cb9852a1a" data-og-width="1414" width="1414" data-og-height="1540" height="1540" data-path="images/creating.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=25d6e6399462fda4e49a15595530b1da 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=46933ba2c7f36514ff9f64d951073f3e 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=39df2f5bbff7af814d08f317266874f9 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a2084bf150cb297459092928e06120a6 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b3a327e131204aba94717368790a338a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4ee7a1980c87da54411e4ceafaa13d48 2500w" />
</Frame>

Setting up a new data diff in Datafold is straightforward. You can configure your data diffs with the following parameters and options:

### Source and Target datasets

#### Data connection

Pick your data connection(s).

#### Diff type

Choose how you want to compare your data:

* Table: Select this to compare data directly from database tables
* Query: Use this to compare results from specific SQL queries

#### Dataset

Choose the dataset you want to compare. This can be a table or a view in your relational database.

#### Filter

Insert your filter clause after the WHERE keyword to refine your dataset. For example: `created_at > '2000-01-01'` will only include data created after January 1, 2000.

### Materialize inputs

Select this option to improve diffing speed when query is heavy on compute, or if filters are applied to non-indexed columns, or if primary keys are transformed using concatenation, coalesce, or another function.

## Column remapping

Designate columns with the same data type and different column names to be compared. Data Diff will surface differences under the column name used in the Source dataset.
<Note>Datafold automatically handles differences in data types to ensure accurate comparisons. See our best practices below for how this is handled.</Note>

## General

### Primary key

The primary key is one or more columns used to uniquely identify a row in the dataset during diffing. The primary key (or keys) does not need to be formally defined in the database or elsewhere as it is used for unique row identification during diffing.

<Note>
  Textual primary keys do not support values outside the set of characters `a-zA-Z0-9!"()*/^+-<>=`. If these values exist, we recommend filtering them out before running the diff operation.
</Note>

### Columns

#### Columns to compare

Specify which columns to compare between datasets.
Note that this has performance implications when comparing a large number of columns, especially in wide tables with 30 or more columns. It is recommended to initially focus on comparisons using only the primary key or to select a limited subset of columns.

### Row sampling

Use sampling to compare a subset of your data instead of the entire dataset. This is best for diffing large datasets. Sampling can be configured to select a percentage of rows to compare, or to ensure differences are found to a chosen degree of statistical confidence.

#### Sampling tolerance

Sampling tolerance defines the allowable margin of error for our estimate. It sets the acceptable percentage of rows with primary key errors (e.g., nulls, duplicates, or primary keys exclusive to one dataset) before disabling sampling.
When sampling is enabled, not every row is examined, which introduces a probability of missing certain discrepancies. This threshold represents the level of difference we are willing to accept before considering the results unreliable and thereby disabling sampling. It essentially sets a limit on how much variance is tolerable in the sample compared to the complete dataset.
Default: 0.001%

#### Sampling confidence

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset. It represents the minimum confidence level that the rate of primary key errors is below the threshold defined in sampling tolerance.
To put it simply, a 95% confidence level with a 5% tolerance means we are 95% certain that the true value falls within 5% of our estimate.
Default: 99%

#### Sampling threshold

Sampling is automatically disabled when the total row count of the largest table in the comparison falls below a specified threshold value. This approach is adopted because, for smaller datasets, a complete dataset comparison is not only more feasible but also quicker and more efficient than sampling. Disabling sampling in these scenarios ensures comprehensive data coverage and provides more accurate insights, as it becomes practical to examine every row in the dataset without significant time or resource constraints.

#### Sample size

This provides an estimated count of the total number of rows included in the combined sample from Datasets A and B, used for the diffing process. It's important to note that this number is an estimate and can vary from the actual sample size due to several factors:
The presence of duplicate primary keys in the datasets will likely increase this estimate, as it inflates the perceived uniqueness of rows.

* Applying filters to the datasets tends to reduce the estimate, as it narrows down the data scope.
* The number of rows we sample is not fixed; instead, we use a statistical approach called the Poisson distribution. This involves picking rows randomly from an infinite pool of rows with uniform random sampling. Importantly, we don't need to perform a full diff (compare every single row) to establish a baseline.

Example: Imagine there are two datasets we want to compare, Source and Target. Since we prefer not to check every row, we use a statistical approach to determine the number of rows to sample from each dataset. To do so, we set the following parameters:

* Sampling tolerance: 5%
* Sampling confidence: 95%

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset, while sampling tolerance defines the allowable margin of error for our estimate. Here, with a 95% sampling confidence and a 5% sampling tolerance, we are 95% confident that the true value falls within 5% of our estimate. Datafold will then estimate the sample size needed (e.g., 200 rows) to achieve these parameters.

### Advanced

#### Materialize diff results to table

Create a detailed table from your diff results, indicating each row where differences occur. This table will include corresponding values from both datasets and flags showing whether each row matches or mismatches.


# Results
Source: https://docs.datafold.com/data-diff/cross-database-diffing/results

Once your data diff is complete, Datafold provides a concise, high-level summary of the detected changes in the Overview tab.

## Overview

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dfb2b6c8d95632782f33082cd32fef46" data-og-width="3032" width="3032" data-og-height="1716" height="1716" data-path="images/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f781b8b739c36996213743bfdc4672f3 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=13405f054e2b826a3674ef43e4bfab2f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=12d421fac1618936be457938eaa78a7c 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9fcea4c4a22bc1f43f7dd73b5b7604fe 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=95f372d97128840e8f445ca97b510946 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/overview.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5c15b56749bd776c57fcd56a7efe7198 2500w" />
</Frame>

The top-level menu displays the diff status, job ID, creation and completed times, runtime, and data connection.

## Columns

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ac6c1544f226b273327ecc43cd48d73f" data-og-width="2984" width="2984" data-og-height="1692" height="1692" data-path="images/columns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a9460414bdee320a50efcb48c76b6691 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e1a2ba2a72f07642c021b6a70abd5d36 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1b7ad4841814550a14c18242a8556ec0 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ed71f0451159487de75976ff9c8a389d 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a6174dcc4937b49a86cd45331320ea9a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/columns.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=339e7bc4dc6ff2531202512abcf625d7 2500w" />
</Frame>

The Columns tab displays a table with detailed column and type mappings from the two datasets being diffed, with status indicators for each column comparison (e.g., identical, percentage of values different). This provides a quick way to identify data inconsistencies and prioritize updates.

## Primary keys

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c37832ea5462bba8e883165c1b4f3e71" data-og-width="2986" width="2986" data-og-height="1718" height="1718" data-path="images/primarykeys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cd2a6b78def0d742873821dca35c6827 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=875e5e8e3e9876dc050c8e8dabd60158 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5d767e5850460b8c1d1153ac90701782 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4fb58adce588950286daf490d3e3eb18 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=50d3ebdaa886dea515022f6eff83c485 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/primarykeys.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cd23ad6685d95488bc2d210a0895d8cc 2500w" />
</Frame>

This tab highlights rows that are unique to the Target dataset in a data diff ("Rows exclusive to Target"). As this identifies rows that exist only in the Target dataset and not in the Source dataset based on the primary key, it flags potential data discrepancies.

The Clone **diffs and materialize results** button allows you to rerun existing data diffs with results materialized in the warehouse, as well as any other desired modifications.

## Values

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=eeefef58cfe6776d6d768b4062b03a59" data-og-width="3038" width="3038" data-og-height="1720" height="1720" data-path="images/values.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a234902e17b71d481d5e9ec7300d9f92 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=cd4ed9f61cc6bc53f1392f6a770cd1f9 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=4a907912eb3a9cf8bd39683f44fa37e6 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=83f8e29e4f0b869ac75572940a35b6c7 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=2a46e3fd9f201d65775a6409984fac40 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/values.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=df76fcf99f3b2c8433c2e3598b8bb1e4 2500w" />
</Frame>

This tab displays rows where at least one column value differs between the datasets being compared. It is useful for quickly assessing the extent of discrepancies between the two datasets.

The **Show filters** button enables the following features:

* Highlight characters: highlight value differences between tables
* % of difference: filters and displays columns based on the specified percentage range of value differences


# File Diffing
Source: https://docs.datafold.com/data-diff/file-diffing

Datafold allows you to diff files (e.g. CSV, Excel, Parquet, etc.) in a similar way to how you diff tables.

<Note>
  If you'd like to enable file diffing for your organization, please contact [support@datafold.com](mailto:support@datafold.com).
</Note>

In addition to diffing data in tables, views, and SQL queries, Datafold allows you to diff data in files hosted in cloud storage. For example, you can diff between an Excel file and a Snowflake table, or between a CSV file and an Excel file.

## Supported cloud storage providers

Datafold supports diffing files in the following cloud storage providers, with plans to support more in the future:

* Amazon S3
* Azure Blob Storage
* Azure Data Lake Storage (ADLS)
* Google Cloud Storage

## Supported file types

Datafold supports diffing the following file types:

* Tabular text files (e.g. `.csv`, `.tsv`, `.txt`, `.dat`)
* Excel (`.xlsx`, `.xls`)
* Parquet (`.parquet`)

## Type-specific options

Depending on the type of file you're diffing, you'll have a few options to specify how you'd like to parse the file.

For example, when diffing a tabular text file, you can specify the delimiter and skip header/footer rows.

<img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bfbe8fbf183c9bf80bdedd39a5f8e110" alt="File diffing options" data-og-width="1440" width="1440" data-og-height="732" height="732" data-path="images/data_diff/file-diffing/adls-file-diff-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=5607d6a653192d345ede77ab89f7ff25 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=7f0bbf12eecac1b5c0ac76468c72daa7 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c2f297820dd0c454d8c563a1c31982f7 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=f5721a09b770a556877b6859c45d4539 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=54d0ef8b5cfb2b49492cdaba2158361b 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=61a426a8f98cb76c65b487577fd486bb 2500w" />


# How Datafold Diffs Data
Source: https://docs.datafold.com/data-diff/how-datafold-diffs-data

Data diffs allow you to perform value-level comparisons between any two datasets within the same database, across different databases, or even between files.

The basic inputs required to run a diff are the data connections, names/paths of the datasets to be compared, and the primary key (one or more columns that uniquely identify rows in the datasets).

## What types of data can data diffs compare?

Diffs can compare data in tables, views, SQL queries (in relational databases and data lakes), and even files (e.g. CSV, Excel, Parquet, etc.).

Datafold facilitates data diffing by supporting a wide range of basic data types across major database systems like Snowflake, Databricks, BigQuery, Redshift, PostgreSQL, and many more.

## Creating data diffs

Diffs can be created in several ways:

* Interactively through the Datafold app
* Programmatically via our [REST API](/api-reference/data-diffs/create-a-data-diff)
* As part of a Continuous Integration (CI) workflow for [Deployment Testing](/deployment-testing/how-it-works)

## How in-database diffing works

When diffing data within the same physical database or data lake namespace, diffs compare data by executing various SQL queries in the target database. It uses several `JOIN`-type queries and various aggregate queries to provide detailed insights into differences at the row, value, and column levels, and to calculate differences in metrics and distributions.

## How cross-database diffing works

Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.


# Best Practices
Source: https://docs.datafold.com/data-diff/in-database-diffing/best-practices

We share best practices that will help you get the most accurate and efficient results from your data diffs.

## Comparing numeric columns: tolerance for floats

When comparing numerical columns or of `FLOAT` type which is inherently noisy, it can be helpful to specify tolerance levels for differences below which the values are considered equal.
Set appropriate tolerance levels for floating-point comparisons to avoid flagging inconsequential differences.

## Materialize diff results

While Datafold UI provides advanced exploration of diff results, sometimes it can be helpful to materialize diff results back to the database to investigate them further with SQL or for audit logging.

## Optimizing diff performance at scale

Since data diff pushes down the compute to your database (which usually has sufficient capacity to store and compute the datasets in the first place), the diffing speed and scalability depends on the performance of the underlying SQL engine. In most cases, the diffing performance is comparable to typical transformation jobs and analytical queries running in the database and has scaled to trillions of rows.
When diffs run longer or consume more database resources than desired, consider the following measures:

1. **Enable Sampling** to dramatically reduce the amount of data processed for in-database diffing.
   Sampling can be helpful when diffing extremely large datasets. When sampling is enabled, Datafold compares a randomly chosen subset of the data. Sampling is the tradeoff between the diff detail and time/cost of the diffing process. For most use cases, sampling does not reduce the informational value of data diffs as it still provides the magnitude and specific examples of differences (e.g., if 10% of sampled data show discrepancies, it suggests a similar proportion of differences across the entire dataset).
   Sampling is less ideal when you need to audit every changed value with 100% confidence, but this scenario is rare in practice.

<Tip>
  Although configuring sampling can seem overwhelming at first, a good rule of thumb is to select an initial value of 95% for the sampling confidence and adjust it as needed. Tweaking the parameters can be helpful to see how they impact the sample size and the tradeoff between performance and accuracy.
</Tip>

2. **Add a SQL filter** if you actually need to compare just a subset of data (e.g., for a particular city or last two weeks).

3. **Optimize SQL queries** to enhance the performance and efficiency of database operations, reduce execution time, minimize resource usage, and ensure faster retrieval of data diff results.

4. **Leverage database performance** by ensuring proper configuration to match the typical workload patterns of your diff operations. Many modern databases come with performance-enhancing features like query optimization, caching, and parallel processing.

5. Consider **increasing resources** available to Datafold in your data warehouse (e.g., for Snowflake, increase warehouse size).


# Creating a New Data Diff
Source: https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff

Setting up a new data diff in Datafold is straightforward.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=25b0433c23469aff83f6603b3a7d05f3" data-og-width="1442" width="1442" data-og-height="1088" height="1088" data-path="images/in-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=14a32e8169a208e9273e29e7a07a4f17 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8fff25fd285124e58075e96e7cbe8999 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0c3f4e8a649e6d7f6a3d0bd58b83e8ff 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e238dbbd86db167374f84b51f2b58507 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=24f536b65aad54de72fac9f1ca9c4c7c 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-diff.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=86bd17bda0cdfd99c65c8e444638ef6a 2500w" />
</Frame>

You can configure your data diffs with the following parameters and options:

## Dataset

### Data connection

Pick your data connection(s).

### Diff type

Choose how you want to compare your data:

* Table: Select this to compare data directly from database tables
* Query: Use this to compare results from specific SQL queries

Datafold can also diff views, materialized views, and dynamic tables (Snowflake-only) across both options too.

### Dataset

Choose the dataset you want to compare, Main and Test. This can be a table or a view in your relational database.

### Time travel point

If your database supports time travel, like [Snowflake](https://docs.snowflake.com/en/user-guide/data-time-travel#querying-historical-data), you can query data at a specified timestamp. This is useful for tracking changes over time, conducting audits, or correcting mistakes from accidental data modifications. You can adjust the database's session parameters as needed for your query.
Supported time travel expressions:

|  Database |           Timestamp          |        Negative Offset       |
| :-------: | :--------------------------: | :--------------------------: |
|  BigQuery | <Icon icon="square-check" /> |                              |
| Snowflake | <Icon icon="square-check" /> | <Icon icon="square-check" /> |

Timestamp examples:

* `2024-01-01`
* `2024-01-01 10:04:23`
* `2024-01-01 10:04:23-09:00`
* `2024-07-16T10:04:23+05:00`

Negative offset examples (in seconds):

* `130`
* `3600`

### Filter

Insert your filter clause after the `WHERE` keyword to refine your dataset. For example: `created_at >'2000-01-01` will only include data created after January 1, 2000.

## Column remapping

When columns are the same data type but are named differently, column remapping allows you to align and compare them. This is useful when datasets have semantically identical columns with different names, such as `userID` and `user_id`. Datafold will surface any differences under the column name used in the Main dataset.

## General parameters

### Primary key

The primary key is one or more columns used to uniquely identify a row in the dataset during diffing. The primary key (or keys) does not need to be formally defined in the database or elsewhere as it is used for unique row identification during diffing. Multiple columns support compound primary key definitions.

### Time-series dimension column

If a time-series dimension is selected, this produces a Timeline plot of diff results over time to identify any time-based patterns.
This is useful for identifying trends or anomalies when a given column does not match between tables in a certain date range. By selecting a time-based column, you can visualize differences and patterns across time, measured as column match rates.

<Frame type="glass">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=161da454ca34d1d8f4a37bd5f874a2e1" data-og-width="2564" width="2564" data-og-height="1242" height="1242" data-path="images/timeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=7244fa9ff4adc20953d2ee1f8d53e7e6 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=fffd38b458593ead056bd8971467f7a6 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0b10dec6830905e889547e1ee83f0f10 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=16ce589445187f6ec73b99035f7da443 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f8deb9b6b3d195c9474ef25f728399e8 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=724568a3fdf9746783f05b0cb831ee7d 2500w" />
</Frame>

### Materialize diff results to table

Create a detailed table from your diff results, indicating each row where differences occur. This table will include corresponding values from both datasets and flags showing whether each row matches or mismatches.

### Materialize full diff result

For in-depth analysis, you can opt to materialize the full diff result. This disables sampling, allowing for a complete row-by-row comparison across datasets. Otherwise, Datafold defaults to diffing only a sample of the data.

## Row sampling

### Enable sampling

Use this to compare a subset of your data instead of the entire dataset. This is best for assessing large datasets.

### Sampling tolerance

Sampling tolerance defines the allowable margin of error for our estimate. It sets the acceptable percentage of rows with primary key errors (like nulls, duplicates, or primary keys exclusive to one dataset) before disabling sampling.
When sampling is enabled, not every row is examined, which introduces a probability of missing certain discrepancies. This threshold represents the level of difference we are willing to accept before considering the results unreliable and thereby disabling sampling. It essentially sets a limit on how much variance is tolerable in the sample compared to the complete dataset.

Default: 0.001%

### Sampling confidence

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset. It represents the minimum confidence level that the rate of primary key errors is below the threshold defined in sampling tolerance.
To put it simply, a 95% confidence level with a 5% tolerance means we are 95% certain that the true value falls within 5% of our estimate.

Default: 99%

### Sampling threshold

Sampling is automatically disabled when the total row count of the largest table in the comparison falls below a specified threshold value. This approach is adopted because, for smaller datasets, a complete dataset comparison is not only more feasible but also quicker and more efficient than sampling. Disabling sampling in these scenarios ensures comprehensive data coverage and provides more accurate insights, as it becomes practical to examine every row in the dataset without significant time or resource constraints.

### Sample size

This provides an estimated count of the total number of rows included in the combined sample from Datasets A and B, used for the diffing process. It's important to note that this number is an estimate and can vary from the actual sample size due to several factors:

* the presence of duplicate primary keys in the datasets will likely increase this estimate, as it inflates the perceived uniqueness of rows
* applying filters to the datasets tends to reduce the estimate, as it narrows down the data scope
* The number of rows we sample is not fixed; instead, we use a statistical approach called the Poisson distribution. This involves picking rows randomly from an infinite pool of rows with uniform random sampling. Importantly, we don't need to perform a full diff (compare every single row) to establish a baseline.

Example: Imagine there are two datasets we want to compare, Main and Test. Since we prefer not to check every row, we use a statistical approach to determine the number of rows to sample from each dataset. To do so, we set the following parameters:

* sampling tolerance: 5%
* sampling confidence: 95%

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset, while sampling tolerance defines the allowable margin of error for our estimate. Here, with a 95% sampling confidence and a 5% sampling tolerance, we are 95% confident that the true value falls within 5% of our estimate. Datafold will then estimate the sample size needed (e.g., 200 rows) to achieve these parameters.

## Tolerance for floats

An acceptable delta between numeric values is used to determine if they match. This is particularly useful for addressing rounding differences in long floating-point numbers.
Add tolerance by choosing a column name, mode, and value. For mode:

* *Relative*: Defines a percentage-based tolerance. For example, a 2% relative tolerance means no difference is noted if the absolute value of (A/B - 1) is less than or equal to 2%.
* *Absolute*: Sets a fixed numerical margin. For instance, an absolute tolerance of 0.5 means values are matched if the absolute difference between A and B is 0.5 or less.


# Results
Source: https://docs.datafold.com/data-diff/in-database-diffing/results

Once your data diff is complete, Datafold provides a concise, high-level summary of the detected changes in the Overview tab

## Overview

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=56d613ef5b60a81549939fd5d3ea419f" data-og-width="2958" width="2958" data-og-height="1713" height="1713" data-path="images/in-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=12a0391f570b88009bc3f474800f32f7 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1b97820bde958760470b1ed532beb949 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=25e137ba597ec73fea4f1756ae13fa83 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=82c8c1a2285fd141e196a448382671cc 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ece29a760cdef2f792abaeded442a0d7 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-overview.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=64fabb64fc190d3aa2499c08cbd06478 2500w" />
</Frame>

The top-level menu displays the diff status, job ID, creation and completed times, runtime, and data connection.

## Columns

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ee2f7d3885d5508738a30d1f088eec15" data-og-width="2990" width="2990" data-og-height="1680" height="1680" data-path="images/in-columns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9eded42869908a4ee041918d6ca6fae4 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=eacedfd1b2b044424953e303041f0c09 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5e274d1e0ca64b1e0edf5f4ccca0cfa6 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9adbb3f95cf30d8c298057a4e9a0c473 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=172cf03e96cd60563f12d77e0d58923b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-columns.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=befe3e9abd9e3e0207da1945f5375f26 2500w" />
</Frame>

The Columns tab displays a table with detailed column and type mappings from the two datasets being diffed, with status indicators for each column comparison (e.g., identical, percentage of values different). This provides a quick way to identify data inconsistencies and prioritize updates.

## Primary keys

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=fc7a9f9e39ff4f0c6df74980d535e2c2" data-og-width="2990" width="2990" data-og-height="1728" height="1728" data-path="images/in-primary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=82ff789de0718c8f62d22223a0df2f27 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9884e9642f9f1b05f7e707ce4eba678f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=632974d975998807d81bd1824c54aafd 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bee160f4fef40c912c631412758c3789 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b6fa3f1aec05f784a10e6d639a96d6aa 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-primary.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4a2cbcf62e3fa196d90909dc918b62a9 2500w" />
</Frame>

This tab highlights rows that are unique to the Test dataset in a data diff ("Rows exclusive to Test"). As this identifies rows that exist only in the Test dataset and not in the Main dataset based on the primary key, it flags potential data discrepancies.

The **Show filters** button allows you to filter these rows by selected column(s).

The **Clone diffs and materialize** results button allows you to rerun existing data diffs with results materialized in the warehouse, as well as any other desired modifications.

## Column Profiles

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8b42ff31ff3dec65f2261c2827bf3270" data-og-width="3044" width="3044" data-og-height="1732" height="1732" data-path="images/in-profiles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ab068999c886c5dfd17e47697037fd79 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=42dce3c20cbfccddb55384e9ea59df2f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c36f03c1179dc217377711e3f3c6ae18 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9855ed1b9b31fddfefa0cce9bb528718 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=144efa39045abb960039b1848c0c2271 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-profiles.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3a172f3962ca08f74b62eda7ed587617 2500w" />
</Frame>

Column Profiles displays aggregate statistics and distributions including averages, counts, ranges, and histogram charts representing column-level differences.

The **Show filters** button allows you to adjust chart values by relative (percentage) or absolute numbers.

## Values

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=48c363eee25ed62c10fb43aba69db754" data-og-width="3040" width="3040" data-og-height="1716" height="1716" data-path="images/in-values.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=748f95900bedc05f851bbb3b7b0f1647 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0b33e7e1d93ea27122d7de13bef64fc6 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=474bbaa67a573a6c9c8285163cf6c58e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9140512b92e149a55ebe16f952711138 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9d635058b2c1c296f3791d874dc60799 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/in-values.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a5e1ad787282cf446a7eef2a926a30ca 2500w" />
</Frame>

This tab displays rows where at least one column value differs between the datasets being compared. It is useful for quickly assessing the extent of discrepancies between the two datasets.

The **Show** filters button enables the following features:

* Highlight characters: highlight value differences between tables
* % of difference: filters and displays columns based on the specified percentage range of value differences

## Timeline

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=161da454ca34d1d8f4a37bd5f874a2e1" data-og-width="2564" width="2564" data-og-height="1242" height="1242" data-path="images/timeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=7244fa9ff4adc20953d2ee1f8d53e7e6 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=fffd38b458593ead056bd8971467f7a6 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0b10dec6830905e889547e1ee83f0f10 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=16ce589445187f6ec73b99035f7da443 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f8deb9b6b3d195c9474ef25f728399e8 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/timeline.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=724568a3fdf9746783f05b0cb831ee7d 2500w" />
</Frame>

The Timeline tab is a specialized feature that only appears if the time-series dimension column has been selected. It graphically represents data differences over time to highlight discrepancies. It only displays columns with data differences, and differences are presented as the share of mismatched data (percentage mismatched).

This feature offers enhanced clarity in pinpointing inconsistencies, supports informed decision-making through visual data representation, and increases efficiency in identifying and resolving data-related issues.

The Timeline feature is particularly useful in scenarios where an incremental model is mismanaged, leading to improper backfilling. It allows users to visually track the inconsistencies that arise over time due to the mismanagement. This graphical representation makes it easier to pinpoint the specific time frames where the errors occurred, facilitating a more targeted approach to rectify these issues.

It is also useful in correlating data differences with specific time intervals that coincide with changing data connections. When switching over or stitching together different data connections, there's often a shift in how data behaves over time. The Timeline graph helps flag the potential impact of the source change on data consistency and integrity.

## Downstream Impact

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=77ee5e8334440ebcfe24ad80b9bd25c3" data-og-width="3042" width="3042" data-og-height="1706" height="1706" data-path="images/downstream.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c5bc92b3b97c36bfdb2bd850189430e6 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ce10d6a9a5ee9c517f00afd9a2bd6b77 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9fd790cad393047aacf9d929f5597d4b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=71181b15370f77f5f63aa08e0b2acbd0 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cba768caffa7cf0f52e668ce74387a7e 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/downstream.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5784cf4b1f0553b22e35d8ae758f37d6 2500w" />
</Frame>

This tab displays all associated BI and data app dependencies, such as dashboards and views, linked to the compared datasets. This helps visually illustrate the impact of data changes on downstream data assets.

Each listed dependency is shown with a link to its lineage diagram within Datafold's [column-level lineage](https://docs.datafold.com/data-explorer/how-it-works). You can you can filter by tables or columns within tables, or [open this view](https://docs.datafold.com/data-explorer/how-it-works) in Data Explorer for further analysis.


# What's a Data Diff?
Source: https://docs.datafold.com/data-diff/what-is-data-diff

A data diff is the value-level comparison between two tables, used to identify critical changes to your data and guarantee data quality.

When you **git diff** your code, you’re comparing two versions of your code files to see what has changed, such as lines added, removed, or modified. Similarly, a **data diff** compares two versions of a dataset or two databases to identify differences in individual cells in the data.

<img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9c6fdaf4be1e5f7ff097e35e236aad4c" alt="what's a data diff" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="images/data_diff/what_is_data_diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=729bba594d308250446243de02d4f99d 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a4db13429bfb4d5dff9c2d4c9b0fb488 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8e2907a41e5244333a7393d9ee5f4e48 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a98f715a31041441606278f26f2b9c7a 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=0f8f72e0eded067cf0258b1e06ab3aa1 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/what_is_data_diff.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3ef6e9f7143d2a03512dc5b304cb0fb5 2500w" />

## Why do I need to diff data?

Just as diffing code and text is fundamental to software engineering and working with text documents, diffing data is essential to the data engineering workflow.

Why? In data engineering, both data and the code that processes it are constantly evolving. Without the ability to easily diff data, understanding and tracking data changes becomes challenging. This slows down the development process and makes it harder to ensure data quality.

There is a lot you can do with data diff:

* Test SQL code by comparing development or staging environment data to production
* Compare tables in source and target systems to identify discrepancies when migrating data between databases
* Detect value-level outliers, or unexpected changes, in data flowing through your ETL/ELT pipelines
* Verify that reports generated for regulatory compliance accurately reflect the underlying data by comparing report outputs with source data

## Why Datafold?

Data diffing is a fundamental capability in data engineering that every engineer should have access to.

Datafold's [Data Diff](https://www.datafold.com/data-diff) is a tool that compares datasets fast, within or across databases. Datafold offers an enterprise-ready solution for comparing datasets within or across databases at scale. It includes comprehensive, optimized, and automated diffing solutions, API access, and secure deployment options.

Here's how you can identify row-level discrepancies in Datafold:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=414ebe833488adcc05e8c6f196db307a" data-og-width="8271" width="8271" data-og-height="6306" height="6306" data-path="images/data-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ea5f6d9604a64fc668bcd6a05377dad7 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2033ff369770ceed8eb7c9aaf7040b3b 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=54b5f3618d3fb0b7a0f5b61d205e5803 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d324c0f4af625fc0dd044a3739aedaea 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6fd0a5f4f4551a5c258ed6b364438b5c 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-diff.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8575823e25178f8407b3fae24672df6b 2500w" />
</Frame>

Datafold provides end-to-end solutions for automating testing, including column-level lineage, ML-based anomaly detection, and enterprise-scale infrastructure support. It caters to complex and production-ready scenarios, including:

* Automated and collaborative diffing and testing for data transformations in CI
* Data diffing informed by column-level lineage, and validation of code changes with visibility into BI applications
* Validating large data migrations or continuous replications with automated cross-database diffing capabilities

Here's a high-level overview of what Datafold offers:

|                                                        Feature Category                                                       |                     Datafold                     |
| :---------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------: |
|                      **Database Support**<br />*Databases that are supported for source-destination diff*                     | Any SQL database, inquire about specific support |
|                                    **Scale**<br />*Size of datasets supported for diffing*                                    | Unlimited with advanced performance optimization |
|               **Primary Key Data Type Support**<br />*Data types of primary keys that are supported for diffing*              |  Numerical, string, datetime, boolean, composite |
|                   **Data Types Diffing Support**<br />*Data types that are supported for per-column diffing*                  |                  All data types                  |
|               **Export Diff Results to Database**<br />*Materialize diffing results in your database of choice*               |           <Icon icon="square-check" />           |
|     **Value-level diffs**<br />*Investigate row-by-row column value differences between source and destination databases*     |     <Icon icon="square-check" /> (JSON & GUI)    |
|                **Diff UI**<br />*Explore diffs visually and easily share them with your team and stakeholders*                |           <Icon icon="square-check" />           |
|           **API Access**<br />*Automatically create diffs and receive results at scale using the Datafold REST API*           |           <Icon icon="square-check" />           |
| **Persisting Diff History**<br />*Persist the result history of diffs to know how your data and diffs have changed over time* |           <Icon icon="square-check" />           |
|                          **Scheduled Checks**<br />*Run scheduled diffs for a defined list of tables*                         |           <Icon icon="square-check" />           |
|      **Alerting**<br />*Receive automatic alerts about detected discrepancies between tables within or across databases*      |           <Icon icon="square-check" />           |
|                       **Security and Compliance**<br />*Run diffs in secure and compliant environments*                       |        HIPAA, SOC2 Type II, GDPR compliant       |
|            **Deployment Options**<br />*Deploy your diffs in secure environments that meet your security standards*           |     Multi-tenant SaaS or Single-tenant in VPC    |
|                **Support**<br />*Choose which channels offer the greatest support to your use cases and users*                |   Enterprise support from Datafold team members  |
|        **SLA**<br />*The types of SLAs that exist to guarantee your team can diff and interact with diffs as expected*        |    <Icon icon="square-check" /> (Coming soon)    |

## Three ways to learn more

If you're new to Datafold or data diffing, here are three easy ways to get started:

1. **Explore our CI integration guides**: See how Datafold fits into your continuous integration (CI) pipeline by checking out our guides for [No-Code](../deployment-testing/getting-started/universal/no-code), [API](../deployment-testing/getting-started/universal/api), or [dbt](../integrations/orchestrators) integrations.
2. **Try it yourself**: Use your own data with our [14-day free trial](https://app.datafold.com/) and experience Datafold in action.
3. **Book a demo**: Get a deeper technical understanding of how Datafold integrates with your company’s data infrastructure by [booking a demo](https://www.datafold.com/booktime) with our team.


# dbt Metadata Sync
Source: https://docs.datafold.com/data-explorer/best-practices/dbt-metadata-sync

Datafold can automatically ingest dbt metadata from your production environment and display it in Data Explorer.

<Note>
  **INFO**

  You can enable the metadata sync in your Orchestration settings.
</Note>

Please note that when this feature is enabled, user editing of table metadata is disabled.

### Model-level

The following model-level information can be synced:

* `description` is synchronized into the description field of the table into Lineage.
* The `owner` of the table is set to the user identified by the `user@company.com` field. This user must exist in Datafold with that email.
* The `foo` meta-information is added to the description field with the value `bar`.
* The tags `pii` and `bar` are applied to the table as tags.

Here's an example configuration in YAML format:

```Bash  theme={null}
models:
  - name: users
    description: "Description of the table"
    meta:
      owner: user@company.com
      foo: bar
    tags:
      - pii
      - abc

```

### Column-level

The following column-level information can be synced:

* The column `user_id` has two tags applied: `pk` and `id`.
* The metadata for `user_id` is ignored because it reflects the primary key tag.
* The `email` column has the description applied.
* The `email` column has the tag `pii` applied.
* The `email` column has extra metadata information in the description field: `type` with the value `email`.

Here's an example configuration for columns in YAML format:

```Bash  theme={null}
models:
  - name: users
    ...
    columns:
      - name: user_id
        tags:
          - pk
          - id
        meta:
          pk: true
      - name: email
        description: "The user's email"
        tags:
          - pii
        meta:
          type: email
```


# How It Works
Source: https://docs.datafold.com/data-explorer/how-it-works

The UI visually maps workflows and tracks column-level or tabular lineages, helping users understand the impact of upstream changes.

Our **Data Explorer** offers a comprehensive overview of your data assets, including [Lineage](/data-explorer/lineage) and [Profiles](/data-explorer/profile).

You can filter data assets by Data Connections, Tags, Data Owners, and Asset Types (e.g., tables, columns, and BI-created assets such as views, reports, and syncs). You can also search directly to find specific data assets for lineage analysis.

<Frame caption="Data App Lineage Overview">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9014fc5bee3d6f583a7ea851cf7558fe" data-og-width="1703" width="1703" data-og-height="887" height="887" data-path="images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8a1a5e2cfab0c5b299b49a93215ccd01 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=630385a4c30cf26ebdb5c1c6e8cde749 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a94f066e41e1a6776f1b0f0bfa1876a4 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6ea25f18b750438941c9fd88dfe044fe 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=df229108a49b3697e09fa89ceea0369e 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cdb6e9c57eb24c8b9f6fb2afa82e7e82 2500w" />
</Frame>

After selecting a table or data asset, the UI will display a **graph of table-level lineage** by default. You can toggle between **Upstream** and **Downstream** perspectives and customize the lineage view by adjusting the **Max Depth** parameter to your preference.

<Frame caption="Lineage Graph">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e55cacaf6922d256a43f3f78d90ea8b4" data-og-width="1703" width="1703" data-og-height="767" height="767" data-path="images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b4f9bf05eb17c2adb144347d3fe1b778 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c815bd96fa6fdb0ca3a4a534daa30288 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d000be10b365da1e8e06ba4e952def9d 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f4b67b0d071d16c4b05f7e8f687b3b4 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=90b34018ad4eea7f9a50d48d2f9680a6 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=179c1da5fc08e093049589ac22aebbb0 2500w" />
</Frame>


# Lineage
Source: https://docs.datafold.com/data-explorer/lineage

Datafold offers a column-level and tabular lineage view.

## Column-level lineage

Datafold's column-level lineage helps users trace and document the history, transformations, dependencies, and both downstream and upstream processes of a specific data column within an organization's data assets. This feature allows you to pinpoint the origins of data validation issues and comprehensively identify downstream data processes and applications.

To view column-level lineage, click on the **Columns** dropdown menu of the selected asset.

<Frame caption="Lineage Graph Columns Dropdown">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a02dc2c18664786f79cf7bd4524e704e" data-og-width="1288" width="1288" data-og-height="717" height="717" data-path="images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9c130d844b643b166ae9c463cfcaadd8 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6444916bc9372372c91ebbe23fb182b1 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=661b8a083b296f41c04cf75e14b2a87a 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8e89ac4be0530963c65fe8e57005299b 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f34ded861320eacb7669d0ce3854d48a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=493551ea4043f4bb8a70e8fc9a53bd07 2500w" />
</Frame>

### Highlight path between assets

To highlight the column path between assets, click the specific column. Reset the view by clicking the **Exit the selected path** button.

<Frame caption="Selected Path in Lineage Graph">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=0e261d393437069ff59ed1dd705569d8" data-og-width="1293" width="1293" data-og-height="704" height="704" data-path="images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=85ec0c08ca5571b544020a049a15e129 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4ad457085f4061895693d9726c70a31f 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b7c97e3362a57d82b8b1789a445b7d51 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c5863c1fe1ca5b72c4d1501de23ffeb2 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=f5057227221485113c49196dbf14838c 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=72bb9126db549b41e5c72af6ea5abcba 2500w" />
</Frame>

## Tabular lineage

Datafold also offers a tabular lineage view.

You can sort lineage information by depth, asset type, identifier, and owner. Click on the **Actions** button for further options:

<Frame caption="Tabular Lineage Actions Dropdown">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a2b72b5aafae515768c8f6bf8163ce66" data-og-width="1354" width="1354" data-og-height="432" height="432" data-path="images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=3daefd5b54ef180640eb3deb64e113bd 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=081c4d17bebe79f6dccc8f5f3d359f49 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=bfee4d7eda4bbf77d5fba112221e992e 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=9fa959dcf2358129f123981519ed7ef3 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=16970be473f622f0f0e9abd6ceca2fa0 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=920fe4f1ceca3857b536787d4a9980a9 2500w" />
</Frame>

### Focus lineage on current node

Drill down onto the data node or column of interest.

### Show SQL query

Access the SQL query associated with the selected column to understand how the data was queried from the source:

<Frame caption="Show SQL Query in Tabular Lineage">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=285cc3de38895e398d74761a28927821" data-og-width="1229" width="1229" data-og-height="843" height="843" data-path="images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f12dcffce34beaa8ad4bfb0434e2333d 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e96b0225d99ce65bc67d0975b8b0377a 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f1500087ef7bde586d1bd2d86b856bd2 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=bf8960aabf1aaf015413805961daec3c 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=17e50d7085c2a4b7a5419343f68e3695 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=db96f6c20a7785ad87267bff806439ba 2500w" />
</Frame>

### Show usage details

Access detailed information about the column's read, write, and cumulative read (the sum of read count including read count of downstream columns) for the previous 7 days:

<Frame caption="Usage Details in Tabular Lineage">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=962e7831072bdca9461ea7af185013ba" data-og-width="822" width="822" data-og-height="386" height="386" data-path="images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0934f90a0698e59d071c0f902a1617b7 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=756536e2c1a7e72138599791b8cd5391 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=122bbab0f679498212f36d1809e50201 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=5d7834b2f9f087f922affb5f3aa41c98 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=77a66bcd0c894b7d96acee1dd3277a71 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=96229297db67384394c45837691729a0 2500w" />
</Frame>

## Search and filters

Datafold offers powerful search and filtering capabilities to help users quickly locate specific data assets and isolate data connections of interest.

In both the graphical and tabular lineage views, you can filter by tables or columns within tables, allowing you to go as granular as needed.

<Frame caption="Search and Filter in Tabular Lineage">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e43f245bfe7f2a29932374343f0dd517" data-og-width="1351" width="1351" data-og-height="317" height="317" data-path="images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a5a1facf226109031703a89d1f5a05bd 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=6a28c0454db7627b922a1da187fef03f 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=8df129d079244a5d215ac03e697d6cc8 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=6c435a95a550e571ebc81efade558be4 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=50cdbd69157005ac330044d95380659c 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=65de7f503af7c341b30029275457241c 2500w" />
</Frame>

### Table filtering

Simply enter the table's name in the search bar to filter and display all relevant information associated with that table.

### Column filtering

To focus specifically on columns, you can search using a combination of keywords. For instance, searching "column table" will display columns associated with a table, while a query like "column dim customer" narrows the search to columns within the "dim customer" table.

## Settings

You can configure the settings for Lineage under Settings > Data Connections > Advanced Settings:

<Frame caption="Lineage Advanced Settings">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=685c29c694dcf151d533fb4d6922293f" data-og-width="1180" width="1180" data-og-height="581" height="581" data-path="images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=28e503fd88a4b984ee5657bd1e55c1ae 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9fdeb699720d9174b6fe8ba74a505cbd 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d960bb0706bce3d3d75e16d75d52db7d 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be841f4e6e774ab5b146b2eae9cb5829 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b08aa127e50c1476119ce04388cb927d 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f3ce489186e05783c2855f6cd8796520 2500w" />
</Frame>

### Schema indexing schedule

Customize the frequency and timing of when to update the indexes on database schemas. The schedule is defined through a cron tab expression.

### Table inclusion/exclusion

You can filter to include and/or exclude specific tables to be shown in Lineage.

When the inclusion list is set, only the tables specified in this list will be visible in the lineage and search results.

When the inclusion list is not set, all tables will be visible by default, except for those explicitly specified in the exclusion list.

### Lineage update schedule

Customize the frequency and timing of when to scan the query history of your data warehouse to build and update the data lineage. The schedule is defined through a cron tab expression.

## FAQ

<AccordionGroup>
  <Accordion title="How is lineage computed?">
    Datafold computes column-level lineage by:

    1. Ingesting, parsing and analyzing SQL logs from your databases and data warehouses. This allows Datafold to infer dependencies between SQL statements, including those that create, modify, and read data.
    2. Augmenting the metadata graph with data from various sources. This includes metadata from orchestration tools (e.g., dbt), BI tools, and user-provided documentation.
  </Accordion>

  <Accordion title="Is there a programmatic way to retrieve lineage?">
    Currently, the schema of the Datafold GraphQL API, which we use to expose lineage information, is not yet stable and is considered to be in beta. Therefore, we do not include this API in our public documentation.

    If you would like to programmatically access lineage information, you can explore our GitHub repository with a few examples: [datafold/datafold-api-examples](https://github.com/datafold/datafold-api-examples). Simply clone the repository and follow the instructions provided in the `README.md` file.
  </Accordion>
</AccordionGroup>


# Profile
Source: https://docs.datafold.com/data-explorer/profile

View a data profile that summarizes key table and column-level statistics, and any upstream dependencies.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=93b2e9ead80d9ae101833634957832d8" data-og-width="1186" width="1186" data-og-height="879" height="879" data-path="images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=da067d78595210d086ac15ae7bfe748b 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=82e5038fe9a5b1a442d582fad3ce24e5 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aa2bbb45b4e4ee0f7b5f179a9493f2b2 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b9696dd27de9899a7bfd3dd91e070eb2 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2b751ead0ebb70e60cd82647682086d1 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_data_explorer_profile-347ca38a3ae0a32084fd9d02f3a0d667.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6fad6be593cce611ef0e6616df22261a 2500w" />
</Frame>


# Cross-Database Diffing for Migrations
Source: https://docs.datafold.com/data-migration-automation/cross-database-diffing-migrations

Validate migration parity with Datafold's cross-database diffing solution.

When migrating data from one system to another, ensuring that the data is accurately transferred and remains consistent is critical. Datafold’s cross-database diffing provides a robust method to validate parity between the source and target databases. It compares data across databases, identifying discrepancies at the dataset, column, and row levels, ensuring full confidence in your migration process.

## How cross-database diffing works

Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.

### What kind of information does Datafold output?

Datafold’s cross-database diffing will produce the following results:

* **High-Level Summary:**
  * Total number of different rows
  * Total number of rows (primary keys) that are present in one database but not the other
  * Aggregate schema differences
* **Schema Differences:** Per-column mapping of data types, column order, etc.
* **Primary Key Differences:** Sample of specific rows that are present in one database but not the other.
* **Value-Level Differences:** Sample of differing column values for each column with identified discrepancies. The full dataset of differences can be downloaded or materialized to the warehouse.

### How does a user run a data diff?

Users can run data diffs through the following methods:

* Via Datafold’s interactive UI
* Via the Datafold API
* On a schedule (as a monitor) with optional alerting via Slack, email, PagerDuty, etc.

### Can I run multiple data diffs at the same time?

Yes, users can run as many diffs as they would like, with concurrency limited by the underlying database.

### What if my data is changing and replicated live, how can I ensure proper comparison?

In such cases, we recommend using watermarking—diffing data within a specified time window of row creation or update (e.g., `updated_at timestamp`).

### What if the data types do not match between source and target?

Datafold performs best-effort type matching for cases where deterministic type casting is possible, e.g., comparing `VARCHAR` type with `STRING` type. When automatic type casting without information loss is not possible, the user can define type casting manually using diffing in Query mode.

### Can data diff help if the dataset in the source and target databases has a different shape/schema/column naming?

Yes, users can reshape input datasets by writing a SQL query and diffing in Query mode to bring the dataset to a comparable shape. Datafold also supports column remapping for datasets with different column names between tables.

## Learn more

To learn more, check out our guide on [how cross-database diffing works](../data-diff/cross-database-diffing/creating-a-new-data-diff) in Datafold, or explore our extensive [FAQ section](../faq/data-migration-automation) covering cross-database diffing and data migration.


# Datafold Migration Agent
Source: https://docs.datafold.com/data-migration-automation/datafold-migration-agent

Automatically migrate data environments of any scale and complexity with Datafold's Migration Agent.

Datafold provides a full-cycle migration automation solution for data teams, which includes code translation and cross-database reconciliation.

## How does DMA work?

Datafold performs complete SQL codebase translation and validation using an AI-powered architecture. This approach leverages a large language model (LLM) with a feedback loop optimized for achieving full parity between the migration source and target. DMA analyzes metadata, including schema, data types, and relationships, to ensure accuracy in translation.

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4472535367a2544e0fc7bce54d43b9e6" alt="datafold migration agent architecture" data-og-width="1561" width="1561" data-og-height="974" height="974" data-path="images/data-migration/datafold_migration_agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a4f2f90cfea623e5d276e4befb1375a2 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=33e9c4d42a7721007c3a036a27afb7a4 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6c11775d4c737d0dd5dc6ef2f4b9e1ab 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=603b1e80b7b5cfa35ed59651729e0b65 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f38f8488278f57d2b976e5c6e517356a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=567ee1b4c54d471dd0dacaed97c15233 2500w" />

Datafold provides a comprehensive report at the end of the migration. This report includes links to data diffs validating parity and highlighting any discrepancies at the dataset, column, and row levels between the source and target databases.

## Why migrate with DMA?

Unlike traditional deterministic transpilers, DMA offers several distinct benefits:

* **Full parity between source and target:** DMA ensures not just code that compiles, but code that delivers the same results in your new database, complete with explicit validation.
* **Flexible dialect handling:** DMA can adapt to any arbitrary input/output dialect without requiring a full grammar definition, which is especially valuable for legacy systems.
* **Self-correction capabilities:** The AI-driven DMA can account for and correct mistakes based on both compilation errors and data discrepancies.
* **Modernizing code structure:** DMA can convert complex stored procedures into clean, modern formats such as dbt projects, following best practices.

## Getting started with DMA

<Note>
  **Want to learn more?**

  If you're interested in diving deeper, please take a moment to [fill out our intake form](https://nw1wdkq3rlx.typeform.com/to/VC2TbEbz) to connect with the Datafold team.
</Note>

1. Connect your source and target data sources to Datafold.
2. Provide Datafold access to your codebase, typically by installing the Datafold GitHub/GitLab/ADO app or via system catalog access for stored procedures.

Once you connect your source and target systems and Datafold ingests the codebase, DMA's translation process is supervised by the Datafold team. In most cases, no additional input is required from the customer.

The migration process timeline depends on the technologies, scale, and complexity of the migration. After setup, migrations typically take several days to several weeks.

## Security

Datafold is SOC 2 Type II, GDPR, and HIPAA-compliant. We offer flexible deployment options, including in-VPC setups in AWS, GCP, or Azure. The LLM infrastructure is local, ensuring no data is exposed to external subprocessors beyond the cloud provider. For VPC deployments, data stays entirely within the customer’s private network.

## FAQ

For more information, please see our extensive [FAQ section](../faq/data-migration-automation).


# Datafold for Migration Automation
Source: https://docs.datafold.com/data-migration-automation/datafold-migration-automation

Datafold provides full-cycle migration automation with SQL code translation and cross-database validation for data warehouse, transformation framework, and hybrid migrations.

Datafold offers flexible migration validation options to fit your data migration workflow. Data teams can choose to leverage the full power of the [Datafold Migration Agent (DMA)](../data-migration-automation/datafold-migration-agent) alongside [cross-database diffing](../data-diff/how-datafold-diffs-data#how-cross-database-diffing-works), or use ad-hoc diffing exclusively for validation.

## Supported migrations

Datafold supports a wide range of migrations to meet the needs of modern data teams. The platform enables smooth transitions between different databases and transformation frameworks, ensuring both code translation and data validation throughout the migration process. Datafold can handle:

* **Data Warehouse Migrations:** Seamlessly migrate between data warehouses, for example, from PostgreSQL to Databricks.

* **Data Transformation Framework Migrations:** Transition your transformation framework from legacy stored procedures to modern tools like dbt.

* **Hybrid Migrations:** Migrate across a combination of data platforms and transformation frameworks. For example, moving from MySQL + stored procedures to Databricks + dbt.

## Migration options

<AccordionGroup>
  <Accordion title="Option 1: DMA + Ad-Hoc Diffing">
    The AI-powered Datafold Migration Agent (DMA) provides automated SQL code translation and validation to simplify and automate data migrations. Teams can pair DMA with ad-hoc cross-database diffing to enhance the validation process with additional manual checks when necessary.

    **How it works:**

    * **Step 1:** Connect your legacy and new databases to Datafold, along with your codebase.
    * **Step 2:** DMA translates and validates SQL code automatically.
    * **Step 3:** Pair the DMA output with ad-hoc cross-database diffing to reconcile data between legacy and new databases.

    This combination streamlines the migration process, offering automatic validation with the flexibility of manual diffing for fine-tuned control.
  </Accordion>

  <Accordion title="Option 2: Ad-Hoc Diffing Only">
    For teams that prefer to handle code translation manually or are working with third-party migrations, Datafold's ad-hoc cross-database diffing is available as a stand-alone validation tool.

    **How it works:**

    * Validate data across databases manually without using DMA for code translation.
    * Run ad-hoc diffing as needed, via the [Datafold REST API](../api-reference/introduction), or schedule it with [Monitors](../data-monitoring) for continuous validation.

    This option gives you full control over the migration validation process, making it suitable for in-house or outsourced migrations.
  </Accordion>
</AccordionGroup>


# Monitor Types
Source: https://docs.datafold.com/data-monitoring/monitor-types

Monitoring your data for unexpected changes is one of the cornerstones of data observability.

Datafold supports all your monitoring needs through a variety of different monitor types:

1. [**Data Diff**](/data-monitoring/monitors/data-diff-monitors) → Detect differences between any two datasets, within or across databases
2. [**Metric**](/data-monitoring/monitors/metric-monitors) → Identify anomalies in standard metrics like row count, freshness, and cardinality, or in any custom metric
3. [**Data Test**](/data-monitoring/monitors/data-test-monitors) → Validate your data with business rules and see specific records that fail your tests
4. [**Schema Change**](/data-monitoring/monitors/schema-change-monitors) → Receive alerts when a table schema changes

If you need help creating your first few monitors, deciding which type of monitor to use in a particular situation, or developing an overall monitoring strategy, please reach out via email ([support@datafold.com](mailto:support@datafold.com)) and our team of experts will be happy to assist.


# Monitors as Code
Source: https://docs.datafold.com/data-monitoring/monitors-as-code

Manage Datafold monitors via version-controlled YAML for greater scalability, governance, and flexibility in code-based workflows.

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


# Data Diff Monitors
Source: https://docs.datafold.com/data-monitoring/monitors/data-diff-monitors

Data Diff monitors compare datasets across or within databases, identifying row and column discrepancies with customizable scheduling and notifications.

## Ways to create a data diff monitor

There are 3 ways to create a data diff monitor:

1. From the **Monitors** page by clicking **Create new monitor** and then selecting **Data diff** as a type of monitor.
2. Clone an existing monitor by clicking **Actions** and then **Clone** in the header menu. This will pre-fill the form with the existing monitor configuration.
3. Create a monitor directly from the data diff results by clicking **Actions** and **Create monitor**. This will pre-fill the configuration with the parent data diff settings, requiring updates only for the **Schedule** and **Notifications** sections.

Once a monitor is created and initial metrics collected, you can set up [thresholds](/data-monitoring/monitors/data-diff-monitors#monitoring) for the two metrics.

## Create a new data diff monitor

Setting up a new diff monitor in Datafold is straightforward. You can configure it with the following parameters and options:

### General

Choose how you want to compare your data and whether the diff type is in-database or cross-database.

Pick your data connections. Then, choose the two datasets you want to compare. This can be a table or a view in your relational database.

If you need to compare just a subset of data (e.g., for a particular city or last two weeks), add a SQL filter.

Select **Materialize inputs** to improve diffing speed when query is heavy on compute, or if filters are applied to non-indexed columns, or if primary keys are transformed using concatenation, coalesce, or another function.

<Frame caption="Data Diff General Settings">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a06294be7daca047c2f4d40d47f2c69f" data-og-width="1497" width="1497" data-og-height="1005" height="1005" data-path="images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=213af5fdb48e1012d925a8be5203943a 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=51eb58c7cfd9012a4e801be46e44880e 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=89639c2d9c761dcfbdabf9d3900f9161 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1f0b0df1baeaa5f720449433d3a2f62a 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=e047642410f555d62c95b5ddc98bdf0d 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=21c33bf84a0a60743205df808fcb2b8d 2500w" />
</Frame>

### Column remapping

When columns are the same data type but are named differently, column remapping allows you to align and compare them. This is useful when datasets have semantically identical columns with different names, such as `userID` and `user_id`. Datafold will surface any differences under the column name used in Dataset A.

<Frame caption="Column Remapping Settings">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=30f8c1dfd4fc510154c421eeb817cc21" data-og-width="1499" width="1499" data-og-height="455" height="455" data-path="images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=0c0a4eed190fa23f92df206b7ea5bfe9 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bf3a422997eab6ba6643a8c831cfd5dd 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=026c103728585781724d615ac7603092 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cd3cf76a5f59560645284b636c3a4d72 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=ff1e41e1b13a26651a145972bd981a9e 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b5211e308e7986c49164bf9f167beec7 2500w" />
</Frame>

### Diff settings

<Frame caption="Diff Settings">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8eabf23bd47e14ba6dcd5337c99c6f20" data-og-width="1494" width="1494" data-og-height="1263" height="1263" data-path="images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2acf7e0252c0342a0a0d2107b6b11b45 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b52751b92261f735321ebefe513908a2 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3d13cdec6683755445b58d4a9464169e 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1ecde098cc2ed4039b19edd30baa294c 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3d37646ea7df295d3e31a9c97e69b04f 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=7b749a57785dd6d6d310ed45cad1c7a5 2500w" />
</Frame>

#### Primary key

The primary key is one or more columns used to uniquely identify a row in the dataset during diffing. The primary key (or keys) does not need to be formally defined in the database or elsewhere as it is used for unique row identification during diffing. Multiple columns support compound primary key definitions.

#### Columns to compare

Determine whether to compare all columns or select specific one(s). To optimize performance on large tables, it's recommended to exclude columns known to have unique values for every row, such as timestamp columns like "updated\_at," or apply filters to limit the comparison scope.

#### Materialize diff results

Choose whether to store diff results in a table.

#### Sampling

Use this to compare a subset of your data instead of the entire dataset. This is best for assessing large datasets.

There are two ways to enable sampling in Monitors: [Tolerance](#tolerance) and [% of Rows](#-of-rows).

<Tip>
  **TIP**

  When should I use sampling tolerance instead of percent of rows?

  Each has its specific use cases and benefits, please [see the FAQ section](#sampling-tolerance-vs--of-rows) for a more detailed breakdown.
</Tip>

##### Tolerance

Tolerance defines the allowable margin of error for our estimate. It sets the acceptable percentage of rows with primary key errors (like nulls, duplicates, or primary keys exclusive to one dataset) before disabling sampling.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4febbf2598a8185c272232032d52de65" data-og-width="1494" width="1494" data-og-height="640" height="640" data-path="images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c6efacf6edb6b8c79ea1b606fcc8a1c6 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=28a2b6ae6a74f6016306275e487447a5 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=34b87a7124ceaeeb1af06576fe24d4a8 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a5ac9fcaf55e9b75177cca0f4acd53f4 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=71c98168b3b65380d590d3925051e87b 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=286afa738b16dc2f4f2f9d98d590270d 2500w" />
</Frame>

When sampling tolerance is enabled, not every row is examined, which introduces a probability of missing certain discrepancies. This threshold represents the level of difference we are willing to accept before considering the results unreliable and thereby disabling sampling. It essentially sets a limit on how much variance is tolerable in the sample compared to the complete dataset.

Default: 0.001%

###### Sampling confidence

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset. It represents the minimum confidence level that the rate of primary key errors is below the threshold defined in sampling tolerance.

To put it simply, a 95% confidence level with a 5% tolerance means we are 95% certain that the true value falls within 5% of our estimate.

Default: 99%

###### Sampling threshold

Sampling will be disabled if total row count of the largest table is less that the threshold value.

###### Sample size

This provides an estimated count of the total number of rows included in the combined sample from Datasets A and B, used for the diffing process. It's important to note that this number is an estimate and can vary from the actual sample size due to several factors:

* The presence of duplicate primary keys in the datasets will likely increase this estimate, as it inflates the perceived uniqueness of rows
* Applying filters to the datasets tends to reduce the estimate, as it narrows down the data scope

The number of rows we sample is not fixed; instead, we use a statistical approach called the Poisson distribution. This involves picking rows randomly from an infinite pool of rows with uniform random sampling. Importantly, we don't need to perform a full diff (compare every single row) to establish a baseline.

Example: Imagine there are two datasets we want to compare, Main and Test. Since we prefer not to check every row, we use a statistical approach to determine the number of rows to sample from each dataset. To do so, we set the following parameters:

* Sampling tolerance: 5%
* Sampling confidence: 95%

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset, while sampling tolerance defines the allowable margin of error for our estimate. Here, with a 95% sampling confidence and a 5% sampling tolerance, we are 95% confident that the true value falls within 5% of our estimate. Datafold will then estimate the sample size needed (e.g., 200 rows) to achieve these parameters.

##### % of rows

Percent of rows sampling defines the proportion of the dataset to be included in the sample by specifying a percentage of the total number of rows. For example, setting the sampling percentage to 0.1% means that only 0.1% of the total rows will be sampled for analysis or comparison.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c682330c2d754021ef6b20164c2cf3c9" data-og-width="1482" width="1482" data-og-height="498" height="498" data-path="images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=6d14ee08e3e68fec35d1d2f173ddc174 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=edf6b8bb2703d6f79f1d579cb2fd2888 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=97119c1709e2a26dca8df8aa80c5ce5b 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c9e0b7637dfee4e8d1edba0bf510acf2 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=065ee528210828e9a0d45b26286b27c8 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a55178c8b732905ba9a01585e7da4c12 2500w" />
</Frame>

When percent of rows sampling is enabled, a fixed percentage of rows is selected randomly from the dataset. This method simplifies the sampling process, making it easy to understand and configure without needing to adjust complex statistical parameters. However, it lacks the statistical assurances provided by methods like sampling tolerance.

It doesn't dynamically adjust based on data characteristics or discrepancies but rather adheres strictly to the specified percentage, regardless of the dataset's variability. This straightforward approach is ideal for scenarios where simplicity and quick setup are more important than precision and statistical confidence. It provides a basic yet effective way to estimate the dataset's characteristics or differences, suitable for less critical data validation tasks.

###### Sampling rate

This refers to the percentage of the total number of rows in the largest table that will be used to determine the sample size. This ensures that the sample size is proportionate to the size of the dataset, providing a representative subset for comparison. For instance, if the largest table contains 1,000,000 rows and the sampling rate is set to 1%, the sample size will be 10,000 rows.

###### Sampling threshold

Sampling is automatically disabled when the total row count of the largest table in the comparison falls below a specified threshold value. This approach is adopted because, for smaller datasets, a complete dataset comparison is not only more feasible but also quicker and more efficient than sampling. Disabling sampling in these scenarios ensures comprehensive data coverage and provides more accurate insights, as it becomes practical to examine every row in the dataset without significant time or resource constraints.

###### Sampling size

This parameter is the [same one used in sampling tolerance](#sample-size).

### Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

### Add notifications

You can add notifications, sent through Slack or emails, which indicate whether a monitor has been executed.

Notifications are sent when either or both predefined thresholds are reached during a Diff Monitor. You can set a maximum threshold for the:

* Number of different rows
* Percentage of different rows

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## Results

The diff monitor run history shows the results from each run.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=d069f23a21e684fb6401fa7502f120a0" data-og-width="3059" width="3059" data-og-height="1502" height="1502" data-path="images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=74049ae838daa9b01486825d44485e92 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=23712bc34bd61835cc6e57263cddf9ac 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3aa7dae0bf0f4eaed0d379d0f987c539 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=6ab08d1c38569298ed0670526706564a 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=e916691a3ed08749f8448c03d9c63520 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=db0aba8cb426d05c65c76f2e0ca06d58 2500w" />
</Frame>

Each run includes basic stats, along with metrics such as:

* The total rows different: number of different rows according to data diff results.
* Rows with different values: percentage of different rows relative to the total number of rows in dataset A according to data diff results. Note that the status `Different` doesn't automatically map into a notification/alert.

Click the **Open Diff** link for more granular information about a specific Data Diff.

## FAQ

<AccordionGroup>
  <Accordion title="Sampling tolerance vs. % of rows">
    Use sampling tolerance when you need statistical confidence in your results, as it is more efficient and stops sampling once a difference is confidently detected. This method is ideal for critical data validation tasks that require precise accuracy.

    On the other hand, use the percent of rows method for its simplicity and ease of use, especially in less critical scenarios where you just need a straightforward, quick sampling approach without worrying about statistical parameters. This method is perfect for general, easy-to-understand sampling needs.
  </Accordion>

  <Accordion title="Need help?">
    If you have any questions about how to use Data Diff monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
  </Accordion>
</AccordionGroup>


# Data Test Monitors
Source: https://docs.datafold.com/data-monitoring/monitors/data-test-monitors

Data Tests validate your data against off-the-shelf checks or custom business rules.

Data Test monitors allow you to validate your data using off-the-shelf checks for non-null or unique values, numeric ranges, accepted values, referential integrity, and more. Custom tests let you write custom SQL queries to validate your own business rules.

Think of Data Tests as pass/fail—either a test returns no records (pass) or it returns at least one record (fail). Failed records are viewable in the app, materialized to a temporary table in your warehouse, and can even be [attached to notifications as a CSV](/data-monitoring/monitors/data-test-monitors#attach-csvs-to-notifications).

## Create a Data Test monitor

There are two ways to create a Data Test monitor:

1. Open the **Monitors** page, select **Create new monitor**, and then choose **Data Test**.
2. Clone an existing Data Test monitor by clicking **Actions** and then **Clone**. This will pre-fill the form with the existing monitor configuration.

## Set up your monitor

Select your data connection, then choose whether you'd like to use a [Standard](/data-monitoring/monitors/data-test-monitors#standard-data-tests) or [Custom](/data-monitoring/monitors/data-test-monitors#custom-data-tests) test.

### Standard Data Tests

Standard tests allow you to validate your data against off-the-shelf checks for non-null or unique values, numeric ranges, accepted values, referential integrity, and more.

After choosing your data connection, select **Standard** and the specific test that you'd like to run. If you don't see the test you're looking for, you can always write a [Custom test](/data-monitoring/monitors/data-test-monitors#custom-data-tests).

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6b3e4ff63c23d378a1afa1b9f5333e12" data-og-width="1182" width="1182" data-og-height="646" height="646" data-path="images/monitors/standard_data_test_types.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a346f265b2fb277ccb5a81594e066b2b 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=16a80272596a95655accea963760bec0 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d423caaacff78f3591f7b641fec1773e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d82c4d294e0289df2ee4b63bc3955e34 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f417b36d008c59024b1cbe4f7e7f6c20 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=462eb1ef1287f983e137e231b64933a0 2500w" />
</Frame>

#### Quoting variables

Some test types (e.g. accepted values) require you to provide one or more values, which you may want to have quoted in the final SQL. The **Quote** flag, which is enabled by default, allows you to control this behavior. Here's an example.

Quoting **enabled** for `EXAMPLE_VALUE` (default):

```sql  theme={null}
SELECT *
FROM DB.SCHEMA.TABLE1
WHERE "COLUMN1" < 'EXAMPLE_VALUE';
```

Quoting **disabled** for `EXAMPLE_VALUE`:

```sql  theme={null}
SELECT *
FROM DB.SCHEMA.TABLE1
WHERE "COLUMN1" < EXAMPLE_VALUE;
```

### Custom Data Tests

When you need to test something that's not available in our [Standard tests](/data-monitoring/monitors/data-test-monitors#standard-data-tests), you can write a Custom test. Select your data connection, choose **Custom**, then write your SQL query.

Importantly, keep in mind that your query should return records that *fail* the test. Here are some examples to illustrate this.

**Custom business rule**

Say your company defines active users as individuals who have signed into your application at least 3 times in the past week. You could write a test that validates this logic by checking for users marked as active who *haven't* reached this threshold:

```sql  theme={null}
SELECT *
FROM users
WHERE status = 'active'
    AND signins_last_7d < 3;
```

**Data formatting**

If you wanted to validate that all phone numbers in your contacts table are 10 digits and only contain numbers, you'd return records that are not 10 digits or use non-numeric characters:

```sql  theme={null}
SELECT *
FROM contacts
WHERE LENGTH(phone_number) != 10
    OR phone_number REGEXP '[^0-9]';
```

## Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

## Add notifications

Receive notifications via Slack or email when at least one record fails your test:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## Attach CSVs to notifications

Datafold allows attaching a CSV of failed records to Slack and email notifications. This is useful if, for example, you have business users who don't have a Datafold license but need to know about records that fail your tests.

This option is configured separately per notification destination as shown here:

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=622b524bab2bb9ef79c263ec2f46ea87" alt="Attach CSVs to Data Tests notifications" data-og-width="1180" width="1180" data-og-height="742" height="742" data-path="images/data-test-csv-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7876e84a312785296030b43008f2c1c9 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d605241e8d8717b8dc79ab185eb303d1 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=98936a7b2311a8ef3e0dff84c78b0ca9 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6ebe2a07c4573a310491353e536663c6 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1432625f83e7ed5e73086b6f012201d0 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dff2347dfe87444ad794488769039c7a 2500w" />

<Note>
  CSV attachments are limited to the lesser of 1,000 rows or 1 MB in file size.
</Note>

### Attaching CSVs in Slack

In order to attach CSVs to Slack notifications, you need to complete 1-2 additional steps:

1. If you installed the Datafold Slack app prior to October 2024, you'll need to reinstall the app by visiting Settings > Integrations > Notifications, selecting your Slack integration, then **Reinstall Slack integration**.
2. Invite the Datafold app to the channel you wish to send notifications to using the `/invite` command shown below:

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0442451287ed6a89c1c9c680ae6a32d2" alt="Invite Datafold app to Slack channel" data-og-width="1068" width="1068" data-og-height="666" height="666" data-path="images/data-test-csv-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f6e7b2a1da58a51aff55d6a884840a9a 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=21996a48dce46a32b0f97130d545a373 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c1c34e7b106bd225191ac63bb3404603 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=16b04f6cdf970298e1ee84c3faaf74d1 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c4a74cdac2ddd9875608fe87dcf0e2af 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=650487221f06e815f762b7dc13adaf01 2500w" />

## Run Tests in CI

Standard Data Tests run on a schedule against your production data. But often it's useful to test data before it gets to production as part of your deployment workflow. For this reason, Datafold supports running tests in CI.

Data Tests in CI work very similarly to our [Monitors as Code](/data-monitoring/monitors-as-code) feature, in the sense that you define your tests in a version-controled YAML file. You then use the Datafold SDK to execute those tests as part of your CI workflow.

### Write your tests

First, create a new file (e.g. `tests.yaml`) in the root of your repository. Then write your tests use the same format described in our [Monitors as Code](/data-monitoring/monitors-as-code) docs with two exceptions:

1. Add a `run_in_ci` flag to each test and set it to `true` (assuming you'd like to run the test)
2. (Optional) Add placeholders for variables that you'd like to populate dynamically when executing your tests

Here's an example:

```yaml  theme={null}
monitors:
  null_pk_test:
    type: test
    name: No NULL pk in the users table
    run_in_ci: true
    connection_id: 8
    query: select * from {{ schema }}.USERS where id is null

  duplicate_pk_test:
    type: test
    name: No duplicate pk in the users table
    run_in_ci: true
    connection_id: 8
    query: |
        select *
        from {{ schema }}.USERS
        where id in (
            select id
            from {{ schema }}.USERS
            group by id
            having count(*) > 1
        );
```

### Execute your tests

<Note>
  **INFO**

  This section describes how to get started with GitHub Actions, but the same concepts apply to other hosted version control platforms like GitLab and Bitbucket. Contact us if you need help getting started.
</Note>

If you're using GitHub Actions, create a new YAML file under `.github/workflows/` using the following template. Be sure to tailor it to your particular setup:

```yaml  theme={null}
  on:
    push:
      branches:
        - main
    pull_request:
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/checkout@v2
          with:
            token: ${{ secrets.GH_TOKEN }}
            repository: datafold/datafold-sdk
            path: datafold-sdk
            ref: data-tests-in-ci-demo
        - uses: actions/setup-python@v2
          with:
            python-version: '3.12'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Set schema env var in PR
          run: |
            echo "SCHEMA=ANALYTICS.PR" >> $GITHUB_ENV
          if: github.event_name == 'pull_request'
        - name: Set schema env var in main
          run: |
            echo "SCHEMA=ANALYTICS.CORE" >> $GITHUB_ENV
          if: github.event_name == 'push'
        - name: Run tests
          run: |
            datafold tests run --var schema:$SCHEMA --ci-config-id 1 tests.yaml # use the correct file name/path
          env:
            DATAFOLD_HOST: https://app.datafold.com # different for dedicated deployments
            DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }} # remember to add to secrets
```

### View the results

When your CI workflow is triggered (e.g. by a pull request), you can view the terminal output for your test results:

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8343173f20f186775988ed8edc5e7f07" data-og-width="1498" width="1498" data-og-height="812" height="812" data-path="images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9fc0a8d51af0d5bd0e39a2b43685269f 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fe3e2e88ba833cb4dd8f5599a360adca 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=61f7f849fe901b4a9230ea6f647f6138 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fcb782b280969c750172fd1b9fc8f19d 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1cc0fbc6734157601122b1c62a2111b2 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=184d1348cbf54c03144147559c32a356 2500w" />
</Frame>

## Need help?

If you have any questions about how to use Data Test monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# Metric Monitors
Source: https://docs.datafold.com/data-monitoring/monitors/metric-monitors

Metric monitors detect anomalies in your data using ML-based algorithms or manual thresholds, supporting standard and custom metrics for tables or columns.

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to enable this feature for your organization.
</Note>

Metric monitors allow you to perform anomaly detection—either automatically using our ML-based algorithm or by setting manual thresholds—on the following metric types:

1. Standard metrics (e.g. row count, freshness, and cardinality)
2. Custom metrics (e.g. sales volume per region)

## Create a Metric monitor

There are two ways to create a Metric Monitor:

1. Open the **Monitors** page, select **Create new monitor**, and then choose **Metric**.
2. Clone an existing Metric monitor by clicking **Actions** and then **Clone**. This will pre-fill the form with the existing monitor configuration.

## Set up your monitor

Select your data connection, then choose the type of metric you'd like: **Table**, **Column**, or **Custom**.

If you select table or column, you have the option to add a SQL filter to refine your dataset. For example, you could implement a 7-day rolling time window with the following: `timestamp >= dateadd(day, -7, current_timestamp)`. Please ensure the SQL is compatible with your selected data connection.

## Metric types

### Table metrics

| Metric    | Definition                        | Additional Notes                                                                                               |
| --------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Freshness | Time since table was last updated | Measured in minutes. Derived from INFORMATION\_SCHEMA. Only supported for Snowflake, BigQuery, and Databricks. |
| Row Count | Total number of rows              |                                                                                                                |

### Column metrics

| Metric             | Definition                     | Supported Column Types | Additional Notes           |
| ------------------ | ------------------------------ | ---------------------- | -------------------------- |
| Cardinality        | Number of distinct values      | All types              |                            |
| Uniqueness         | Proportion of distinct values  | All types              | Proportion between 0 and 1 |
| Minimum            | Lowest numeric value           | Numeric columns        |                            |
| Maximum            | Highest numeric value          | Numeric columns        |                            |
| Average            | Mean value                     | Numeric columns        |                            |
| Median             | Median value (50th percentile) | Numeric columns        |                            |
| Sum                | Sum of all values              | Numeric columns        |                            |
| Standard Deviation | Measure of data spread         | Numeric columns        |                            |
| Fill Rate          | Proportion of non-null values  | All types              | Proportion between 0 and 1 |

### Custom metrics

Our custom metric framework is extremely flexible and supports several approaches to defining metrics. Depending on the approach you choose, your query should return some combination of the following columns:

* **Metric value (required)**: a numeric column containing your *metric values*
* **Timestamp (optional)**: a date/time column containing *timestamps* corresponding to your metric values
* **Group (optional)**: a string column containing *groups/dimensions* for your metric

<Note>
  **INFO**

  The names and order of your columns don't matter. Datafold will automatically infer their meaning based on data type.
</Note>

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=538ed4183ea523c46e2a3fa093697e1f" data-og-width="4768" width="4768" data-og-height="3200" height="3200" data-path="images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=fc94579a5279f3ba6036ff574f9eb30b 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=add70a4caf25b88e6de28371f8533ae3 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e34f719fcf3fdaecf30f0aa11845ea80 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=95e0a279fc8cea4d3940f55e9df6fa98 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cee550c72ac472133a84c5d3728577e7 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/custom_metric_matrix-7f38681722ab77f7d52e0b9350af9ab9.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cddada2b6514065818b7d8117b5bcaa7 2500w" />
</Frame>

The following questions will help you decide which approach is best for you:

1. **Do you want to group your metric by the value of a column in your query?** For example, if your metric is *sales volume per day*, rather than looking at a single metric that encompasses all sales globally, it might be more informative to group by country. In this case, Datafold will automatically compute sales volume separately for each country to assist with root cause analysis when there’s an unexpected change.
2. **Will your query return a single metric value (per group, if relevant) on every monitor run, or an entire time series?** We generally recommend starting with the simpler approach of providing a single metric value (per group) per monitor run. However, if you’ve already defined a time series elsewhere (e.g. in your BI tool) and simply want to copy/paste that query into Datafold, then you may prefer the latter approach.

<Note>
  **INFO**

  Datafold will only log a single data point per timestamp per group, which means you should only send data for a particular time period once that period is complete.
</Note>

1. **If your metric returns a single value per monitor run, will you provide your own timestamps or use the timestamps of monitor runs?** If your query returns a single value per run, we generally recommend letting Datafold provide timestamps based on monitor runs unless you have a compelling reason to provide your own. For example, if your metric always lags by one day, you could explicitly associate yesterday's date with each observation.

As you're writing your query, Datafold will let you know if the result set doesn't match one of the accepted patterns. If you have questions, please contact us and we'll be happy to help.

## Configure anomaly detection

Enable anomaly detection to get the most out of metric monitors. You have several options:

* **Automatic**: our automated anomaly detection uses machine learning to flag metric values that are out of the ordinary. Dial the sensitivity up or down depending on how many alerts you'd like to receive.
* **Manual**: specific thresholds beyond which you'd like the monitor to trigger an alert. **Fixed Values** are specific minimum and/or maximum values, while **Percent Change** measure the magnitude of change from one observation to the next.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dde08288db7476b9dde7ea5bdcf74fb7" data-og-width="1184" width="1184" data-og-height="532" height="532" data-path="images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d124cd790d7ccb2a3b4ccb9d8aa37362 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3252044af65d97323bed87564d17e65b 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3e9bdbb3e4ccc1babacddaf8ad5e6829 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e64d316d1dd09d938d20d609f0cff7f 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c9a611a0f41235b45c912276bdbaaa68 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/anomaly_detection_menu-bec86b18752d4a0a3081de8ce1983485.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f2c1502ca43decc8de2b523fcdd565da 2500w" />
</Frame>

## Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

## Add notifications

Send notifications via Slack or email when your monitor exceeds a threshold (automatic or manual):

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## Need help?

If you have any questions about how to use Metric monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# Schema Change Monitors
Source: https://docs.datafold.com/data-monitoring/monitors/schema-change-monitors

Schema Change monitors notify you when a table’s schema changes, such as when columns are added, removed, or data types are modified.

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to enable this feature for your organization.
</Note>

Schema change monitors alert you when a table’s schema changes in any of the following ways:

* Column added
* Column removed
* Data type changed

## Create a Schema Change monitor

There are two ways to create a Schema Change monitor:

1. Open the **Monitors** page, select **Create new monitor**, and then choose **Schema Change**.
2. Clone an existing Schema Change monitor by clicking **Actions** and then **Clone**. This will pre-fill the form with the existing monitor configuration.

## Set up your monitor

To set up a Schema Change monitor, simply select your data connection and the table you wish to monitor for changes.

## Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

## Add notifications

Receive notifications via Slack or email when at least one record fails your test:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## FAQ

<Accordion title="Don't data diffs detect schema changes too?">
  Yes, but in a different context. While data diffs report on schema differences *between two tables at the same time* (unless you’re using the time travel feature), data diff monitors alert you to schema changes for the *same table over time*.
</Accordion>

## Need help?

If you have any questions about how to use Schema Change monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# Deployment Options
Source: https://docs.datafold.com/datafold-deployment/datafold-deployment-options

Datafold is a web-based application with multiple deployment options, including multi-tenant SaaS and dedicated cloud (either customer- or Datafold-hosted).

## SaaS / Multi-Tenant

Our standard multi-tenant deployment is a cost-efficient option for most teams and is available in two AWS regions:

| Region Name      | Region      | Sign-Up Page                                                               |
| :--------------- | :---------- | :------------------------------------------------------------------------- |
| US West (Oregon) | `us-west-2` | [https://app.datafold.com/org-signup](https://app.datafold.com/org-signup) |
| Europe (Ireland) | `eu-west-1` | [https://eu.datafold.com/org-signup](https://eu.datafold.com/org-signup)   |

For additional security, we provide the following options:

1. [IP Whitelisting](/security/securing-connections#ip-whitelisting): only allow access to specific IP addresses
2. [AWS PrivateLink](/security/securing-connections#private-link): set up a limited network point to access your RDS in the same region
3. [VPC Peering](/security/securing-connections#vpc-peering-saas): securely join two networks together
4. [SSH Tunnel](/security/securing-connections#ssh-tunnel): set up a secure tunnel between your network and Datafold with the SSH server on your side
5. [IPSec Tunnel](/security/securing-connections#ipsec-tunnel): an IPSec tunnel setup

## Dedicated Cloud

We also offer a single-tenant deployment of the Datafold application in a dedicated Virtual Private Cloud (VPC). The options are (from least to most complex):

1. **Datafold-hosted, Datafold-managed**: the Cloud account belongs to Datafold and we manage the Datafold application for you.
2. **Customer-hosted, Datafold-managed**: the Cloud account belongs to you, but we manage the Datafold application for you.
3. **Customer-hosted, Customer-managed**: the Cloud account belongs to you and you manage the Datafold application. Datafold does not have access.

Dedicated Cloud can be deployed to all major cloud providers:

* [AWS](/datafold-deployment/dedicated-cloud/aws)
* [GCP](/datafold-deployment/dedicated-cloud/gcp)
* [Azure](/datafold-deployment/dedicated-cloud/azure)

<Tip>
  **VPC vs. VNet**

  We use the term VPC across all major cloud providers. However, Azure refers to this concept as a Virtual Network (VNet).
</Tip>

### Datafold Dedicated Cloud FAQ

<AccordionGroup>
  <Accordion title="What is the benefit of a Dedicated Cloud deployment?">
    Dedicated Cloud deployment may be the preferred deployment method by customers with special privacy and security concerns and in highly regulated domains. In a Dedicated Cloud deployment, the entire Datafold stack runs on dedicated cloud infrastructure and network, which usually means it is:

    1. Not accessible to public Internet (sits behind customer's VPN)
    2. Uses internal network to communicate with customer's databases and other resources – none of the data is sent using public networks
  </Accordion>

  <Accordion title="How does a Customer-hosted Dedicated Cloud deployment work?">
    Datafold is deployed to customer's cloud infrastructure but is fully managed by Datafold. The only DevOps involvement needed from the customer's side is to set up a cloud project and role (steps #1 and #2 below).

    1. Customer creates a Datafold-specific namespace in their cloud account (subaccount in AWS / project in GCP / subscription or resource group in Azure)
    2. Customer creates a Datafold-specific IAM resource with permissions to deploy the Datafold-specific namespace
    3. Datafold Infrastructure team provisions the Datafold stack on the customer's infrastructure using fully-automated procedure with Terraform
    4. Customer and Datafold Infrastructure teams collaborate to implement the security and networking requirements, see [all available options](#additional-security-dedicated-cloud)

    See cloud-specific instructions here:

    * [AWS](/datafold-deployment/dedicated-cloud/aws)
    * [GCP](/datafold-deployment/dedicated-cloud/gcp)
    * [Azure](/datafold-deployment/dedicated-cloud/azure)

    After the initial deployment, the Datafold team uses the same procedure to roll out software updates and perform maintenance to keep the uptime SLA.
  </Accordion>

  <Accordion title="How does a Datafold-hosted Dedicated Cloud deployment work?">
    Datafold is deployed in the customer's region of choice on AWS, GCP, or Azure that is owned and managed by Datafold. We collaborate to implement the security and networking requirements ensuring that traffic either does not cross the public internet or, if it does, does so securely. All available options are listed below.
  </Accordion>

  <Accordion title="How does a Customer-hosted, Customer-managed deployment work?">
    This deployment method follows the same process as the standard customer-hosted deployment (see above), but with a key difference: the customer is responsible for managing both the infrastructure and the application. Datafold engineers do not have any access to the deployment in this case.

    We offer open-source projects that facilitate this deployment, with examples for every major cloud provider. You can find these projects on GitHub:

    * [AWS](https://github.com/datafold/terraform-aws-datafold)
    * [GCP](https://github.com/datafold/terraform-google-datafold)
    * [Azure](https://github.com/datafold/terraform-azure-datafold)

    Each of these projects uses a Helm chart for deploying the application. The Helm chart is also available on GitHub:

    * [Helm Chart](https://github.com/datafold/helm-charts)

    By providing these open-source projects, Datafold enables you to integrate the deployment into your own infrastructure, including existing clusters. This allows your infrastructure team to manage the deployment effectively.

    <Tip>
      **Deployment Secrets:** Datafold provides the necessary secrets for downloading images as part of the license agreement. Without this agreement, the deployment will not complete successfully.
    </Tip>
  </Accordion>

  <Accordion title="What additional security and networking options are available?">
    Because the Datafold application is deployed in a dedicated VPC, your databases/integrations are not directly accessible when they are not exposed to the public Internet. The following solutions enable secure connections to your databases/integrations without exposing them to the public Internet:

    <Tabs>
      <Tab title="AWS">
        1. [PrivateLink](/security/securing-connections?current-cloud=aws#private-link "PrivateLink")
        2. [VPC Peering](/security/securing-connections#vpc-peering-dedicated-cloud "VPC Peering")
        3. [SSH Tunnel](/security/securing-connections#ssh-tunnel "SSH Tunnel")
        4. [IPSec Tunnel](/security/securing-connections#ipsec-tunnel "IPSec Tunnel")
      </Tab>

      <Tab title="GCP">
        1. [Private Service Connect](/security/securing-connections?current-cloud=gcp#private-link "Private Service Connect")
        2. [VPC Peering](/security/securing-connections#vpc-peering-dedicated-cloud "VPC Peering")
        3. [SSH Tunnel](/security/securing-connections#ssh-tunnel "SSH Tunnel")
      </Tab>

      <Tab title="Azure">
        1. [Private Link](/security/securing-connections?current-cloud=azure#private-link "Private Link")
        2. [VNet Peering](/security/securing-connections#vpc-peering-dedicated-cloud "VNet Peering")
        3. [SSH Tunnel](/security/securing-connections#ssh-tunnel "SSH Tunnel")
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Can Datafold be deployed and managed by the customer's internal team?">
    Please inquire with [sales@datafold.com](mailto:sales@datafold.com) about customer-managed deployment options.
  </Accordion>
</AccordionGroup>


# Datafold VPC Deployment on AWS
Source: https://docs.datafold.com/datafold-deployment/dedicated-cloud/aws

Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on AWS.

<Note>
  **INFO**

  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## Create a Domain Name (optional)

You can either choose to use your domain (for example, `datafold.domain.tld`) or to use a Datafold managed domain (for example, `yourcompany.dedicated.datafold.com`).

### Customer Managed Domain Name

Create a DNS A-record for the domain where Datafold will be hosted. For the DNS record, there are two options:

* **Public-facing:** When the domain is publicly available, we will provide an SSL certificate for the endpoint.
* **Internal:** It is also possible to have Datafold disconnected from the internet. This would require an internal DNS (for example, AWS Route 53) record that points to the Datafold instance. It is possible to provide your own certificate for setting up the SSL connection.

Once the deployment is complete, you will point that A-record to the IP address of the Datafold service.

## Give Datafold Access to AWS

For setting up Datafold, it is required to set up a separate account within your organization where we can deploy Datafold. We're following the [best practices of AWS to allow third-party access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Froles%5Fcommon-scenarios%5Fthird-party.html).

### Create a separate AWS account for Datafold

First, create a new account for Datafold. Go to **My Organization** to add an account:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ecb7e602c3b08de265dacb1df1eac10e" data-og-width="1593" width="1593" data-og-height="878" height="878" data-path="images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1d1dd34b489ca092788995df5ba5a6a5 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c631068d953452483122091b2ff8aa42 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d7abac8ab1dc7620a03a5ba1f59d0a03 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5004316cbd8cacc25d30522a4e869640 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2cd359c13851e11163c35f3e3492af1b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8ad47cba5e59c951e16413618733c07d 2500w" />
</Frame>

Click **Add an AWS Account**:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=549b03369b95e7623fe57e5dc532b957" data-og-width="1593" width="1593" data-og-height="878" height="878" data-path="images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3add6311c17236abacca7c817aafe03a 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=97e5fa312b986eecde33780f82eb2f1f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=29998282119a491d95edee409fc00ff7 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bccdcc52d6c5d7ee423188ff4ab8c88a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=63bff3ac6c8e33920fd9568c8130dab0 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d54a5a18bb61f457c16a44bd0ac0201d 2500w" />
</Frame>

You can name this account anything that helps identify it clearly. In our examples, we name it **Datafold**. Make sure that the email address of the owner isn't used by another account.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e0b959106f88d7ede59ded7fb7997a54" data-og-width="1593" width="1593" data-og-height="1136" height="1136" data-path="images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7bd72307ea05f4bcdd77d35826744103 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=966d93f01380181036384e4a1e7e8ee0 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=eaab173b708c779b307e492ccb756219 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=932ad5b38472837e76e6a747fb645dc3 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5c53c5787dc6dd9c6aadc9bfe15144fd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=055e3adc3b951f5eba043280543f7886 2500w" />
</Frame>

When you click the **Create AWS Account** button, you'll be returned back the organization screen, and see the notification that the new account is being created. After refresh a few minutes later, the account should appear in the organizations list.

### Grant Third-Party access to Datafold

To make sure that deployment runs as expected, your Datafold Support Engineer may need access to the Datafold-specific AWS account that you created. The access can be revoked after the deployment if needed.

To grant access, log into the account created in the previous step. You can switch to the newly created account using the [Switch Role page](https://signin.aws.amazon.com/switchrole):

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=43de213f0410fc802ed38ef6f6f44ded" data-og-width="1593" width="1593" data-og-height="872" height="872" data-path="images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=47b26c7efda81871101e132b5972f853 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=94d86401db3b4ab1303a0c956d06287d 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7d058ff7c3af83e9ebfec6fe3da143e6 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=51afba04ebc6c906b68db9a2eac01cbd 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=502d5ec9a4535a063dae99adb31bdddf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=18413ef3f774045bb57cffa4eff6fd6a 2500w" />
</Frame>

By default, the role name is **OrganizationAccountAccessRole**.

Click **Switch Role** to log in to the Datafold account.

## Grant Access to Datafold

Next, we need to allow Datafold to access the account. We do this by allowing the Datafold AWS account to access your AWS workspace. Go to the [IAM page](https://console.aws.amazon.com/iam/home) or type **IAM** in the search bar:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8132e03e72c2f723790206113dbf13b2" data-og-width="1484" width="1484" data-og-height="854" height="854" data-path="images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0224906492782f6b4ad2190c1cf22f16 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0f49a249de61c0cbc37db5652e026c26 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e58a1a6015f9e70bff52be81c7a2f963 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=77c44b7423dbf73e4131a4cad605a091 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=854526199c25a4b4835a88e11619c60b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=132fa23b5cb5c06a71f789b1266fe412 2500w" />
</Frame>

Go to the Roles page, and click the **Create Role** button:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8417176c60c7b467090588b20b216222" data-og-width="1484" width="1484" data-og-height="854" height="854" data-path="images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f67e6f63b968dbab9b24a2f601e8d2a0 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d8032e0c8fbfeb25cf3b08f2953e7e48 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=99edbba40c4799d4455b03b0557ee4e3 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=136f812410de0edc50bff12a05cc161b 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0f77d10a11640acf8e5b7cd201e05b43 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=199490033f59d5e2b308109502255523 2500w" />
</Frame>

Select **Another AWS Account**, and use account ID `710753145501`, which is Datafold's account ID. Select **Require MFA** and click **Next: Permissions**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6f71fb94b0427e11f18738e9c9639bb5" data-og-width="1484" width="1484" data-og-height="854" height="854" data-path="images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=95c2292924300065c552da526a647474 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87c379d8fe9f02b9b24d971008f0c114 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=93d44d5470c9d7541bd7c13bd51443b4 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cbfdd71748f7512c10b5d6f9b6b97181 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be4801b775469da2befae6b399dcc242 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ec36f881a225bffc97015169773425db 2500w" />
</Frame>

On the Permissions page, attach the **AdministratorAccess** permissions for Datafold to have control over the resources within the account, or see [Minimal IAM Permissions](#minimal-iam-permissions).

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8da938f9d77fffe2fbb7b419fd52e14e" data-og-width="1484" width="1484" data-og-height="933" height="933" data-path="images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d8cc13e9f3674b5e74ec2ad2d05adfb8 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f15b9f9974e816105d6aebf313ab6aed 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fd552639c1f531f8dc46a597f451eaa4 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=99b1cfafe1afd6b54b93489f42f00670 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0b2ec43ba66d36dc09a8a48f23920a95 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9406b62f38814e4fe7861fccf33e1af1 2500w" />
</Frame>

Next, you can set **Tags**; however, they are not a requirement.

Finally, give the role a name of your choice. Be careful not to duplicate the account name. If you named the account in an earlier step `Datafold`, you may want to name the role `Datafold-role`.

Click **Create Role** to complete this step.

Now that the role is created, you should be routed back to a list of roles in your organization.

Click on your newly created role to get a sharable link for the account and store this in your password manager. When setting up your deployment with a support engineer, Datafold will use this link to gain access to the account.

After validating the deployment with your support engineer, and making sure that everything works as it should, we will let you know when it's clear to revoke the credentials.

### Minimal IAM Permissions

Because we work in a Account dedicated to Datafold, there is no direct access to your resources unless explicitly configured (e.g., VPC Peering). The following IAM policy are required to update and maintain the infrastructure.

```JSON  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "acm:AddTagsToCertificate",
                "acm:DeleteCertificate",
                "acm:DescribeCertificate",
                "acm:GetCertificate",
                "acm:ListCertificates",
                "acm:ListTagsForCertificate",
                "acm:RemoveTagsFromCertificate",
                "acm:RequestCertificate",
                "acm:UpdateCertificateOptions",
                "apigateway:DELETE",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "apigateway:UpdateRestApiPolicy",
                "autoscaling:*",
                "ec2:*",
                "eks:*",
                "elasticloadbalancing:*",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetOpenIDConnectProvider",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:GetUserPolicy",
                "iam:GetUser",
                "iam:ListAccessKeys",
                "iam:ListAttachedRolePolicies",
                "iam:ListGroupsForUser",
                "iam:ListInstanceProfilesForRole",
                "iam:ListPolicies",
                "iam:ListPolicyVersions",
                "iam:ListRolePolicies",
                "iam:PassRole",
                "iam:TagOpenIDConnectProvider",
                "iam:TagPolicy",
                "iam:TagRole",
                "iam:TagUser",
                "kms:CreateAlias",
                "kms:CreateGrant",
                "kms:CreateKey",
                "kms:Decrypt",
                "kms:DeleteAlias",
                "kms:DescribeKey",
                "kms:DisableKey",
                "kms:EnableKeyRotation",
                "kms:GenerateDataKey",
                "kms:GetKeyPolicy",
                "kms:GetKeyRotationStatus",
                "kms:ListAliases",
                "kms:ListResourceTags",
                "kms:PutKeyPolicy",
                "kms:RevokeGrant",
                "kms:ScheduleKeyDeletion",
                "kms:TagResource",
                "logs:CreateLogGroup",
                "logs:DeleteLogGroup",
                "logs:DescribeLogGroups",
                "logs:ListTagsLogGroup",
                "logs:ListTagsForResource",
                "logs:PutRetentionPolicy",
                "logs:TagResource",
                "rds:*",
                "ssm:GetParameter",
                "secretsmanager:CreateSecret",
                "secretsmanager:DeleteSecret",
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetResourcePolicy",
                "secretsmanager:PutSecretValue",
                "secretsmanager:TagResource",
                "s3:*"
            ],
            "Resource": "*"
        }
    ]
}
```

Some policies we need from time to time. For example, when we do the first deployment. Since those are IAM-related, we will ask for temporary permissions when required.

```JSON  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreateAccessKey",
                "iam:CreateOpenIDConnectProvider",
                "iam:CreatePolicy",
                "iam:CreateRole",
                "iam:CreateUser",
                "iam:DeleteAccessKey",
                "iam:DeleteOpenIDConnectProvider",
                "iam:DeletePolicy",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DeleteUser",
                "iam:DeleteUserPolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy",
                "iam:PutUserPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

It is easier to allow `PowerUserAccess` and then selectively add iam permissions given above.
PowerUserAccess has explicit denies for `account:*`, `organization:*` and `iam:*.`

# Datafold AWS infrastructure details

This document provides detailed information about the AWS infrastructure components deployed by the Datafold Terraform module, explaining the architectural decisions and operational considerations for each component.

## EBS volumes

The Datafold application requires 3 volumes for persistent storage, each deployed as encrypted Elastic Block Store (EBS) volumes in the primary availability zone. This also means that pods cannot be deployed outside the availability zone of these volumes, because the nodes wouldn't be able to attach them.

**ClickHouse data volume** serves as the analytical database storage for Datafold. ClickHouse is a columnar database that excels at analytical queries. The default 40GB allocation usually provides sufficient space for typical deployments, but it can be scaled up based on data volume requirements. The GP3 volume type with 3000 IOPS ensures consistent performance for analytical workloads.

**ClickHouse Logs Volume** stores ClickHouse's internal logs and temporary data. The separate logs volume prevents log data from consuming IOPS and I/O performance from actual data storage.

**Redis Data Volume** provides persistent storage for Redis, which handles task distribution and distributed locks in the Datafold application. Redis is memory-first but benefits from persistence for data durability across restarts. The 50GB default size accommodates typical caching needs while remaining cost-effective.

All EBS volumes are encrypted using AWS KMS, managed by AWS, ensuring data security at rest. The volumes are deployed in the first availability zone to minimize latency and simplify backup strategies.

## Load balancer

The load balancer serves as the primary entry point for all external traffic to the Datafold application. The module offers 2 deployment strategies, each with different operational characteristics and trade-offs.

**External Load Balancer Deployment** (the default approach) creates an AWS Application Load Balancer through Terraform. This approach provides centralized control over load balancer configuration and integrates well with existing AWS infrastructure. The load balancer automatically handles SSL termination, health checks, and traffic distribution across Kubernetes pods. This method is ideal for organizations that prefer infrastructure-as-code management and want consistent load balancer configurations across environments.

**Kubernetes-Managed Load Balancer** deployment sets `deploy_lb = false` and relies on the AWS Load Balancer Controller running within the EKS cluster. This approach leverages Kubernetes-native load balancer management, allowing for dynamic scaling and easier integration with Kubernetes ingress resources. The controller automatically provisions and manages load balancers based on Kubernetes service definitions, which can be more flexible for applications that need to scale load balancer resources dynamically.

Both load balancers apply the currently recommended and strictest ELB security policies: `ELBSecurityPolicy-TLS13-1-2-Res-2021-06` and security settings.

The choice between these approaches often depends on operational preferences and existing infrastructure patterns. External deployment provides more predictable resource management, while Kubernetes-managed deployment offers greater flexibility for dynamic workloads.

**Security** A security group shared between the load balancer and the EKS nodes allows traffic to reach only the EKS nodes and nothing else. The load balancer allows traffic to land directly into the EKS private subnet.

**Certificate** The certificate can be pre-created by the customer and then attached, or a cloud-managed certificate can be created on the fly.
The application will not function without HTTPS, so a certificate is mandatory. After the certificate is created either manually or through this repository, it must be validated by the DNS administrator by adding a CNAME record. This puts the certificate in "Issued" state. The certificate cannot be found when it's still provisioning.

## EKS cluster

The Elastic Kubernetes Service (EKS) cluster forms the compute foundation for the Datafold application, providing a managed Kubernetes environment optimized for AWS infrastructure.

**Network Architecture** The entire cluster is deployed into private subnets. This means the data plane is not reachable from the Internet except through the load balancer. A NAT gateway allows the cluster to reach the internet (egress traffic) for downloading pod images, optionally sending Datadog logs and metrics, and retrieving the version to apply to the cluster from our portal. The control plane is accessible via a private endpoint using a PrivateLink setup from, for example, a VPN VPC elsewhere. This is a private+public endpoint, so the control plane can also be made accessible through the Internet, but then the appropriate CIDR restrictions should be put in place.

For a typical dedicated cloud deployment of Datafold, only around 100 IPs are needed. This assumes 3 r7a.2xlarge instances where one node runs ClickHouse+Redis, another node runs the application, and a third node may be put in place when version rollovers occur. This means a subnet of size /24 (253 IPs) should be sufficient to run this application.

By default, the repository creates a VPC and subnets, but by specifying the VPC ID of an already existing VPC, the cluster and load balancer
get deployed into existing network infrastructure. This is important for some customers where they deploy a different architecture without NAT gateways, firewall options that check egress, and other DLP controls.

**Add-ons**

The cluster includes essential add-ons like CoreDNS for service discovery, the VPC CNI for networking, and the EBS CSI driver for persistent volume management. These components are automatically updated and maintained by AWS, reducing operational overhead.

The AWS load balancer controller and metrics-server are deployed separately via Helm charts in the application deployment, not through this Terraform infrastructure. The Load Balancer Controller manages at least the AWS target group that enables ingress for the Datafold application. Optionally, it may also manage the entire external load balancer.

**Node Management** supports up to three managed node groups, allowing for workload-specific resource allocation. Each node group can be configured with different instance types, enabling cost optimization and performance tuning for different application components. The cluster autoscaler automatically adjusts node count based on resource demands, ensuring efficient resource utilization while maintaining application availability. One typical way to deploy is to let the application pods go on a wider range of nodes, and set up tolerations and labels on the second node group, which are then selected by both Redis and ClickHouse. This is because Redis and ClickHouse have restrictions on the zone they must be present in because of their volumes, and ClickHouse is a bit more CPU intensive. This method optimizes CPU performance for the Datafold application.

**Security Features** include IAM Roles for Service Accounts (IRSA), which provide fine-grained IAM permissions to Kubernetes pods without requiring AWS credentials in container images. This approach enhances security by following the principle of least privilege and integrates seamlessly with AWS security services.

## IAM Roles and Permissions

The IAM architecture follows the principle of least privilege, providing specific permissions only where needed. Service accounts in Kubernetes are mapped to IAM roles using IRSA, enabling secure access to AWS services without embedding credentials in application code.

**EBS CSI Controller Role** enables the Kubernetes cluster to manage EBS volumes dynamically. This role allows pods to request persistent storage that's automatically provisioned and attached to the appropriate nodes or attach static volumes. The permissions are scoped to only the EBS operations needed for volume lifecycle management.

**Load Balancer Controller Role** provides the permissions necessary for Kubernetes to manage AWS load balancers. This includes creating target groups, registering and deregistering targets, and managing load balancer listeners. The controller can automatically provision load balancers based on Kubernetes service definitions, enabling seamless integration between Kubernetes and AWS networking.

**Cluster Autoscaler Role** allows the cluster to automatically scale node groups based on resource demands. This role can describe and modify Auto Scaling groups, enabling the cluster to add or remove nodes as needed. The autoscaler considers pod resource requests and node capacity when making scaling decisions.

**Datafold Roles** Datafold has roles per pod pre-defined which can have their permissions assigned when they need them. At the moment, we have two specific roles in use. One is for the ClickHouse pod to be able to make backups and store them on S3. The other is for the use of the Bedrock service for our AI offering.

These roles are automatically created and configured when the cluster is deployed, ensuring that the necessary permissions are in place for the cluster to function properly. The use of IRSA means that these permissions are automatically rotated and managed by AWS, reducing security risks associated with long-lived credentials.

## RDS database

The PostgreSQL Relational Database Service (RDS) instance serves as the primary relational database for the Datafold application, storing user data, configuration, and application state.

**Storage Configuration** starts with a 20GB initial allocation that can automatically scale up to 100GB based on usage patterns. This auto-scaling feature prevents storage-related outages while avoiding over-provisioning. For typical deployments, storage usage remains under 200GB, though some high-volume deployments may approach 400GB. The GP3 storage type provides consistent performance with configurable IOPS and throughput.

**High Availability** is intentionally disabled by default, meaning the database runs in a single availability zone. This configuration reduces costs and complexity while still providing excellent reliability. The database includes automated backups with 14-day retention, ensuring data can be recovered in case of failures. For organizations requiring higher availability, multi-AZ deployment can be enabled, though this significantly increases costs.

**Security and Encryption** always encrypts data at rest using AWS KMS. A dedicated KMS key is created for the database, providing better security isolation and audit capabilities compared to using the default AWS RDS key. The database is deployed in private subnets with security groups that restrict access to only the EKS cluster, ensuring network-level security.

The database configuration prioritizes operational simplicity and cost-effectiveness while maintaining the security and reliability required for production workloads. The combination of automated backups, encryption, and network isolation provides a robust foundation for the application's data storage needs.


# Datafold VPC Deployment on Azure
Source: https://docs.datafold.com/datafold-deployment/dedicated-cloud/azure

Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on Azure.

<Note>
  **INFO**

  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## Create a Domain Name (optional)

You can either choose to use your domain (for example, `datafold.domain.tld`) or to use a Datafold managed domain (for example, `yourcompany.dedicated.datafold.com`).

### Customer Managed Domain Name

Create a DNS A-record for the domain where Datafold will be hosted. For the DNS record, there are two options:

* **Public-facing:** When the domain is publicly available, we will provide an SSL certificate for the endpoint.
* **Internal:** It is also possible to have Datafold disconnected from the internet. This would require an internal DNS (for example, Azure DNS) record that points to the Datafold instance. It is possible to provide your own certificate for setting up the SSL connection.

Once the deployment is complete, you will point that A-record to the IP address of the Datafold service.

## Create a New Subscription

For isolation reasons, it is best practice to [create a new subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription) within your Microsoft Entra directory/tenant. Please call it something like `yourcompany-datafold` to make it easy to identify.

## Set IAM Permissions

Go to **Microsoft Entra ID** and navigate to **Users**. Click **Add**, **User**, **Invite external user** and add the Datafold engineers.

Navigate to the subscription you just created and go to **Access control (IAM)** tab in the side bar.

* Navigate to the subscription you just created. Go to **Access control (IAM)**. Under **Add** select **Add role assignment**.
* Under **Role**, navigate to **Priviledged administrator roles** and select **Owner**.
* Under **Members**, click **Select members** and add the Datafold engineers.
* When you are done, select **Review + assign**.

The owner role is only required temporarily while we configure and test the initial Datafold deployment. We'll inform you when it is ok to revoke this permission.

### Required APIs

The following Azure APIs need to be enabled to run Datafold:

1. [Microsoft.ContainerService](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Container%20Service)
2. [Microsoft.Network](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Network)
3. [Microsoft.Compute](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Compute)
4. [Microsoft.KeyVault](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Key%20Vault)
5. [Microsoft.Storage](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Storage)
6. [Microsoft.DBforPostgreSQL](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/PostgreSQL)

Once the access has been granted, make sure to notify Datafold so we can initiate the deployment.

# Datafold Azure infrastructure details

This document provides detailed information about the Azure infrastructure components deployed by the Datafold Terraform module,
explaining the architectural decisions and operational considerations for each component.

## Managed disks

The Datafold application requires 3 managed disks for persistent storage, each deployed as encrypted Azure managed disks in the
primary availability zone. This also means that pods cannot be deployed outside the availability zone of these disks, because
the nodes wouldn't be able to attach them.

**ClickHouse data disk** serves as the analytical database storage for Datafold. ClickHouse is a columnar database that excels
at analytical queries. The default 40GB allocation usually provides sufficient space for typical deployments, but it can be
scaled up based on data volume requirements. The StandardSSD\_LRS disk type with configurable IOPS and throughput ensures
consistent performance for analytical workloads.

**ClickHouse logs disk** stores ClickHouse's internal logs and temporary data. The separate logs disk prevents log data from
consuming IOPS and I/O performance from actual data storage.

**Redis data disk** provides persistent storage for Redis, which handles task distribution and distributed locks in the Datafold
application. Redis is memory-first but benefits from persistence for data durability across restarts. The 50GB default size
accommodates typical caching needs while remaining cost-effective.

All managed disks are encrypted by default using Azure-managed encryption keys, ensuring data security at rest. The disks are
deployed in the first availability zone to minimize latency and simplify backup strategies. For Premium and Ultra SSD disk
types, IOPS and throughput can be configured to optimize performance for specific workloads.

## Application Gateway

The Application Gateway serves as the primary entry point for all external traffic to the Datafold application. The module
offers 2 deployment strategies, each with different operational characteristics and trade-offs.

**External Application Gateway Deployment** (the default approach) creates an Azure Application Gateway through Terraform.
This approach provides centralized control over load balancer configuration and integrates well with existing Azure
infrastructure. The Application Gateway automatically handles SSL termination, health checks, and traffic distribution across
Kubernetes pods. This method is ideal for organizations that prefer infrastructure-as-code management and want consistent
load balancer configurations across environments.

**Kubernetes-Managed Application Gateway** deployment sets `deploy_lb = false` and relies on the Azure Application Gateway
Ingress Controller (AGIC) running within the AKS cluster. This approach leverages Kubernetes-native load balancer management,
allowing for dynamic scaling and easier integration with Kubernetes ingress resources. The controller automatically provisions
and manages Application Gateways based on Kubernetes service definitions, which can be more flexible for applications that
need to scale load balancer resources dynamically.

Both Application Gateways apply the currently recommended and strictest SSL policies: `AppGwSslPolicy20220101S` and security
settings.

The choice between these approaches often depends on operational preferences and existing infrastructure patterns. External
deployment provides more predictable resource management, while Kubernetes-managed deployment offers greater flexibility for
dynamic workloads.

**Security** A network security group shared between the Application Gateway and the AKS nodes allows traffic to reach only
the AKS nodes and nothing else. The Application Gateway allows traffic to land directly into the AKS private subnet.

**Certificate** The certificate can be pre-created by the customer and then attached, or a cloud-managed certificate can be
created on the fly. The application will not function without HTTPS, so a certificate is mandatory. After the certificate is
created either manually or through this repository, it must be validated by the DNS administrator by adding a CNAME record.
This puts the certificate in "Issued" state. The certificate cannot be found when it's still provisioning.

## AKS cluster

The Azure Kubernetes Service (AKS) cluster forms the compute foundation for the Datafold application, providing a managed
Kubernetes environment optimized for Azure infrastructure.

**Network Architecture** The entire cluster is deployed into private subnets. This means the data plane is not reachable from
the Internet except through the Application Gateway. A NAT gateway allows the cluster to reach the internet (egress traffic)
for downloading pod images, optionally sending Datadog logs and metrics, and retrieving the version to apply to the cluster
from our portal. The control plane is accessible via a private endpoint using a Private Link setup from, for example, a VPN
VNet elsewhere. This is a private+public endpoint, so the control plane can also be made accessible through the Internet, but
then the appropriate CIDR restrictions should be put in place.

For a typical dedicated cloud deployment of Datafold, only around 100 IPs are needed. This assumes 3 Standard\_DS2\_v2 instances
where one node runs ClickHouse+Redis, another node runs the application, and a third node may be put in place when version
rollovers occur. This means a subnet of size /24 (253 IPs) should be sufficient to run this application.

By default, the repository creates a VNet and subnets, but by specifying the VNet ID of an already existing VNet, the cluster
and Application Gateway get deployed into existing network infrastructure. This is important for some customers where they
deploy a different architecture without NAT gateways, firewall options that check egress, and other DLP controls.

**Add-ons**

The cluster includes several essential add-ons configured through Terraform:

**Workload Identity** is enabled to provide fine-grained IAM permissions to Kubernetes pods without requiring Azure credentials
in container images. This is essential for ClickHouse to access Azure Storage for backups and other services.

**Ingress Application Gateway** is integrated with the cluster to handle external traffic routing and SSL termination. The
Application Gateway Ingress Controller (AGIC) manages the Application Gateway configuration based on Kubernetes ingress resources.

**Storage Profile** includes the Azure Disk CSI driver for persistent volume management, file driver for Azure Files, and
snapshot controller for volume snapshots. These components enable dynamic provisioning and management of Azure storage resources.

**Node Management** supports up to three managed node pools, allowing for workload-specific resource allocation. Each node
pool can be configured with different VM sizes, enabling cost optimization and performance tuning for different application
components. The cluster autoscaler automatically adjusts node count based on resource demands, ensuring efficient resource
utilization while maintaining application availability. One typical way to deploy is to let the application pods go on a wider
range of nodes, and set up tolerations and labels on the second node pool, which are then selected by both Redis and
ClickHouse. This is because Redis and ClickHouse have restrictions on the zone they must be present in because of their
disks, and ClickHouse is a bit more CPU intensive. This method optimizes CPU performance for the Datafold application.

**Security Features** include Azure Workload Identity, which provides fine-grained IAM permissions to Kubernetes pods without
requiring Azure credentials in container images. This approach enhances security by following the principle of least privilege
and integrates seamlessly with Azure security services. The cluster also supports private clusters with restricted control
plane access and network policies for pod-to-pod communication control.

## IAM Roles and Permissions

The IAM architecture follows the principle of least privilege, providing specific permissions only where needed. Service
accounts in Kubernetes are mapped to IAM roles using Azure Workload Identity, enabling secure access to Azure services without
embedding credentials in application code.

**Azure Disk CSI Controller Role** enables the Kubernetes cluster to manage Azure managed disks dynamically. This role allows
pods to request persistent storage that's automatically provisioned and attached to the appropriate nodes or attach static
disks. The permissions are scoped to only the Azure Disk operations needed for disk lifecycle management.

**Application Gateway Ingress Controller Role** provides the permissions necessary for Kubernetes to manage Azure Application
Gateways. This includes creating backend address pools, registering and deregistering targets, and managing Application
Gateway listeners. The controller can automatically provision Application Gateways based on Kubernetes service definitions,
enabling seamless integration between Kubernetes and Azure networking.

**Cluster Autoscaler Role** allows the cluster to automatically scale node pools based on resource demands. This role can
describe and modify Virtual Machine Scale Sets, enabling the cluster to add or remove nodes as needed. The autoscaler considers
pod resource requests and node capacity when making scaling decisions.

**Datafold Roles** Datafold has roles per pod pre-defined which can have their permissions assigned when they need them. At
the moment, we have two specific roles in use. One is for the ClickHouse pod to be able to make backups and store them on
Azure Storage. The other is for the use of the Azure OpenAI service for our AI offering.

These roles are automatically created and configured when the cluster is deployed, ensuring that the necessary permissions are
in place for the cluster to function properly. The use of Azure Workload Identity means that these permissions are automatically
rotated and managed by Azure, reducing security risks associated with long-lived credentials.

## Azure Database for PostgreSQL

The Azure Database for PostgreSQL Flexible Server instance serves as the primary relational database for the Datafold
application, storing user data, configuration, and application state.

**Storage Configuration** starts with a 32GB initial allocation that can automatically scale up to 100GB based on usage
patterns. This auto-scaling feature prevents storage-related outages while avoiding over-provisioning. For typical deployments,
storage usage remains under 200GB, though some high-volume deployments may approach 400GB. The GP\_Standard storage type
provides consistent performance with configurable IOPS and throughput.

**High Availability** is intentionally disabled by default, meaning the database runs in a single availability zone. This
configuration reduces costs and complexity while still providing excellent reliability. The database includes automated backups
with 7-day retention, ensuring data can be recovered in case of failures. For organizations requiring higher availability,
multi-zone deployment can be enabled, though this significantly increases costs.

**Security and Encryption** always encrypts data at rest using Azure-managed encryption keys. The database is deployed in
private subnets with network security groups that restrict access to only the AKS cluster, ensuring network-level security.
The database supports Azure Private Link for secure, private connectivity from the VNet.

The database configuration prioritizes operational simplicity and cost-effectiveness while maintaining the security and
reliability required for production workloads. The combination of automated backups, encryption, and network isolation
provides a robust foundation for the application's data storage needs.


# Datafold VPC Deployment on GCP
Source: https://docs.datafold.com/datafold-deployment/dedicated-cloud/gcp

Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on GCP.

<Note>
  **INFO**

  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## Create a Domain Name (optional)

You can either choose to use your domain (for example, `datafold.domain.tld`) or to use a Datafold managed domain (for example, `yourcompany.dedicated.datafold.com`).

### Customer Managed Domain Name

Create a DNS A-record for the domain where Datafold will be hosted. For the DNS record, there are two options:

* **Public-facing:** When the domain is publicly available, we will provide an SSL certificate for the endpoint.
* **Internal:** It is also possible to have Datafold disconnected from the internet. This would require an internal DNS (for example, AWS Route 53) record that points to the Datafold instance. It is possible to provide your own certificate for setting up the SSL connection.

Once the deployment is complete, you will point that A-record to the IP address of the Datafold service.

## Create a New Project

For isolation reasons, it is best practice to [create a new project](https://console.cloud.google.com/projectcreate) within your GCP organization. Please call it something like `yourcompany-datafold` to make it easy to identify:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=723db80c5ab11885a5c68f4783de2795" data-og-width="1972" width="1972" data-og-height="906" height="906" data-path="images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=66c280f699f6c7fb8dd2030440654b30 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ae23c8cf867466a00a27c8bfb66925aa 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9b22f156d54fbb52d9c51757be289d1a 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d624b674fad3bf9cfdbe937843ca0cac 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=71c9fb467747ddce2ad410f0f13c7e67 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=83160e2df8dd689757d55c9a27877f76 2500w" />
</Frame>

After a minute or so, you should receive confirmation that the project has been created. Afterward, you should be able to see the new project.

## Set IAM Permissions

Navigate to the **IAM** tab in the sidebar and click **Grant Access** to invite Datafold to the project.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1f120a9192d42aa0f142a68ce3cfd12c" data-og-width="1954" width="1954" data-og-height="720" height="720" data-path="images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ebcc1af578ef3bfae3d84d10a15b5e7 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b0f878553c3ebdd32f60a768cf149844 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0feac9134f245a4083d5849a6e2a5be2 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9362c81f7959768af1098cc2449989dc 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=138a377b7b8e9959c8ff5e4674833041 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=00dabc22d0cca62db4b4ce56c721e458 2500w" />
</Frame>

Add your Datafold solutions engineer as a **principal**. You have two options for assigning IAM permissions to the Datafold Engineers.

1. Assign them as an **owner** of your project.
2. Assign the extended set of [Minimal IAM Permissions](#minimal-iam-permissions).

The owner role is only required temporarily while we configure and test the initial Datafold deployment. We'll inform you when it is ok to revoke this permission and provide us with only the [Minimal IAM Permissions](#minimal-iam-permissions).

### Required APIs

The following GCP APIs need to be additionally enabled to run Datafold:

1. [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)
2. [Secret Manager API](https://console.cloud.google.com/apis/api/secretmanager.googleapis.com)

The following GCP APIs we use are already turned on by default when you created the project:

1. [Cloud Logging API](https://console.cloud.google.com/apis/api/logging.googleapis.com)
2. [Cloud Monitoring API](https://console.cloud.google.com/apis/api/monitoring.googleapis.com)
3. [Cloud Storage](https://console.cloud.google.com/apis/api/storage-component.googleapis.com)
4. [Service Networking API](https://console.cloud.google.com/apis/api/servicenetworking.googleapis.com)

Once the access has been granted, make sure to notify Datafold so we can initiate the deployment.

### Minimal IAM Permissions

Because we work in a Project dedicated to Datafold, there is no direct access to your resources unless explicitly configured (e.g., VPC Peering). The following IAM roles are required to update and maintain the infrastructure.

```Bash  theme={null}
Cloud SQL Admin
Compute Load Balancer Admin
Compute Network Admin
Compute Security Admin
Compute Storage Admin
IAP-secured Tunnel User
Kubernetes Engine Admin
Kubernetes Engine Cluster Admin
Role Viewer
Service Account User
Storage Admin
Viewer
```

Some roles we need from time to time. For example, when we do the first deployment. Since those are IAM-related, we will ask for temporary permissions when required.

```Bash  theme={null}
Role Administrator
Security Admin
Service Account Key Admin
Service Account Admin
Service Usage Admin
```

# Datafold Google Cloud infrastructure details

This document provides detailed information about the Google Cloud infrastructure components deployed
by the Datafold Terraform module, explaining the architectural decisions and operational considerations for each component.

## Persistent disks

The Datafold application requires 3 persistent disks for storage, each deployed as encrypted Google Compute Engine
persistent disks in the primary availability zone. This also means that pods cannot be deployed outside the availability
zone of these disks, because the nodes wouldn't be able to attach them.

**ClickHouse data disk** serves as the analytical database storage for Datafold. ClickHouse is a columnar database
that excels at analytical queries. The default 40GB allocation usually provides sufficient space for typical deployments,
but it can be scaled up based on data volume requirements. The pd-balanced disk type provides consistent
performance for analytical workloads with automatically managed IOPS and throughput.

**ClickHouse logs disk** stores ClickHouse's internal logs and temporary data. The separate logs disk prevents
log data from consuming IOPS and I/O performance from actual data storage.

**Redis data disk** provides persistent storage for Redis, which handles task distribution and distributed locks in
the Datafold application. Redis is memory-first but benefits from persistence for data durability across restarts.
The 50GB default size accommodates typical caching needs while remaining cost-effective.

All persistent disks are encrypted by default using Google-managed encryption keys, ensuring data security at rest.
The disks are deployed in the first availability zone to minimize latency and simplify backup strategies.

## Load balancer

The load balancer serves as the primary entry point for all external traffic to the Datafold application.
The module offers 2 deployment strategies, each with different operational characteristics and trade-offs.

**External Load Balancer Deployment** (the default approach) creates a Google Cloud Load Balancer through Terraform.
This approach provides centralized control over load balancer configuration and integrates well with existing Google Cloud infrastructure.
The load balancer automatically handles SSL termination, health checks, and traffic distribution across Kubernetes pods.
This method is ideal for organizations that prefer infrastructure-as-code management and want consistent load balancer configurations across environments.

**Kubernetes-Managed Load Balancer** deployment sets `deploy_lb = false` and relies on the Google Cloud Load Balancer Controller
running within the GKE cluster. This approach leverages Kubernetes-native load balancer management, allowing for
dynamic scaling and easier integration with Kubernetes ingress resources. The controller automatically provisions and manages load balancers based on Kubernetes service definitions, which can be more flexible for applications that need to scale load balancer resources dynamically.

For external load balancers deployed through Kubernetes, the infrastructure developer needs to create SSL policies and
Cloud Armor policies separately and attach them to the load balancer through annotations. Internal load balancers cannot
have SSL policies or Cloud Armor applied. Our Helm charts support various deployment types including internal/external
load balancers with uploaded certificates or certificates stored in Kubernetes secrets.

The choice between these approaches often depends on operational preferences and existing infrastructure patterns.
External deployment provides more predictable resource management, while Kubernetes-managed deployment offers greater flexibility for dynamic workloads.

**Security** A firewall rule shared between the load balancer and the GKE nodes allows traffic to reach only the GKE nodes and nothing else.
The load balancer allows traffic to land directly into the GKE private subnet.

**Certificate** The certificate can be pre-created by the customer and then attached, or a Google-managed SSL certificate can be created on the fly.
The application will not function without HTTPS, so a certificate is mandatory. After the certificate is created either
manually or through this repository, it must be validated by the DNS administrator by adding an A record. This puts the
certificate in "ACTIVE" state. The certificate cannot be found when it's still provisioning.

## GKE cluster

The Google Kubernetes Engine (GKE) cluster forms the compute foundation for the Datafold application,
providing a managed Kubernetes environment optimized for Google Cloud infrastructure.

**Network Architecture** The entire cluster is deployed into private subnets. This means the data plane
is not reachable from the Internet except through the load balancer. A Cloud NAT allows the cluster to reach the
internet (egress traffic) for downloading pod images, optionally sending Datadog logs and metrics,
and retrieving the version to apply to the cluster from our portal. The control plane is accessible via a private endpoint
using a Private Service Connect setup from, for example, a VPN VPC elsewhere. This is a private+public endpoint,
so the control plane can also be made accessible through the Internet, but then the appropriate CIDR restrictions should be put in place.

For a typical dedicated cloud deployment of Datafold, only around 100 IPs are needed.
This assumes 3 e2-standard-8 instances where one node runs ClickHouse+Redis, another node runs the application,
and a third node may be put in place when version rollovers occur. This means a subnet of size /24 (253 IPs)
should be sufficient to run this application, but you can always apply a different CIDR per subnet if needed.

By default, the repository creates a VPC and subnets, but by specifying the VPC ID of an already existing VPC,
the cluster and load balancer get deployed into existing network infrastructure.
This is important for some customers where they deploy a different architecture without Cloud NAT, firewall options that check egress, and other DLP controls.

**Add-ons**

The cluster includes essential add-ons like CoreDNS for service discovery, the VPC-native networking for networking,
and the GCE persistent disk CSI driver for persistent volume management. These components are automatically updated
and maintained by Google, reducing operational overhead.

**Node Management** supports up to three managed node pools, allowing for workload-specific resource allocation.
Each node pool can be configured with different machine types, enabling cost optimization and performance tuning
for different application components. The cluster autoscaler automatically adjusts node count based on resource demands,
ensuring efficient resource utilization while maintaining application availability. One typical way to deploy
is to let the application pods go on a wider range of nodes, and set up tolerations and labels on the second node pool,
which are then selected by both Redis and ClickHouse. This is because Redis and ClickHouse have restrictions
on the zone they must be present in because of their disks, and ClickHouse is a bit more CPU intensive.
This method optimizes CPU performance for the Datafold application.

**Security Features** include several critical security configurations:

* **Workload Identity** is enabled and configured with the project's workload pool, providing fine-grained IAM permissions to Kubernetes pods without requiring Google Cloud credentials in container images
* **Shielded nodes** are enabled with secure boot and integrity monitoring for enhanced node security
* **Binary authorization** is configured with project singleton policy enforcement to ensure only authorized container images can be deployed
* **Network policy** is enabled using Calico for pod-to-pod communication control
* **Private nodes** are enabled, ensuring all node traffic goes through the VPC network

These security features follow the principle of least privilege and integrate seamlessly with Google Cloud security services.

## IAM roles and permissions

The IAM architecture follows the principle of least privilege, providing specific permissions only where needed.
Service accounts in Kubernetes are mapped to IAM roles using Workload Identity, enabling secure access to Google
Cloud services without embedding credentials in application code.

**GKE service account** is created with basic permissions for logging, monitoring, and storage access.
This service account is used by the GKE nodes and provides the foundation for cluster operations.

**ClickHouse backup service account** is created with a custom role that allows ClickHouse to make backups and store them on Cloud Storage.
This service account uses Workload Identity to securely access Cloud Storage without embedding credentials.

**Datafold roles** Datafold has roles per pod pre-defined which can have their permissions assigned when they need them.
At the moment, we have two specific roles in use. One is for the ClickHouse pod to be able to make backups and store them on Cloud Storage.
The other is for the use of the Vertex AI service for our AI offering.

These roles are automatically created and configured when the cluster is deployed, ensuring that the
necessary permissions are in place for the cluster to function properly. The Datafold and ClickHouse service accounts
authenticate using Workload Identity, which means these permissions are automatically rotated and managed by Google, reducing security risks associated with long-lived credentials.

## Cloud SQL database

The PostgreSQL Cloud SQL instance serves as the primary relational database for the Datafold application,
storing user data, configuration, and application state.

**Storage configuration** starts with a 20GB initial allocation that can automatically scale up to 100GB based on usage patterns.
This auto-scaling feature prevents storage-related outages while avoiding over-provisioning.
For typical deployments, storage usage remains under 200GB, though some high-volume deployments may approach 400GB.
The pd-balanced storage type provides consistent performance with configurable IOPS and throughput.

**High availability** is intentionally disabled by default, meaning the database runs in a single availability zone.
This configuration reduces costs and complexity while still providing excellent reliability. The database includes
automated backups with 7-day retention, ensuring data can be recovered in case of failures. For organizations requiring higher availability,
multi-zone deployment can be enabled, though this significantly increases costs.

**Security and encryption** always encrypts data at rest using Google-managed encryption keys by default.
The database is deployed in private subnets with firewall rules that restrict access to only the GKE cluster,
ensuring network-level security.

The database configuration prioritizes operational simplicity and cost-effectiveness while maintaining the security
and reliability required for production workloads. The combination of automated backups, encryption,
and network isolation provides a robust foundation for the application's data storage needs.


# Best Practices
Source: https://docs.datafold.com/deployment-testing/best-practices

Explore best practices for CI/CD testing in Datafold.

<CardGroup>
  <Card title="Slim Diff" href="/deployment-testing/best-practices/slim-diff" icon="file" horizontal>
    Optimize time and cost by choosing which downstream tables to diff.
  </Card>

  <Card title="Handling Data Drift" href="/deployment-testing/best-practices/handling-data-drift" icon="file" horizontal>
    Learn how to prevent and manage data drift in CI pipelines.
  </Card>
</CardGroup>


# Handling Data Drift
Source: https://docs.datafold.com/deployment-testing/best-practices/handling-data-drift

Ensuring Datafold in CI executes apples-to-apples comparison between staging and production environments.

<Note>
  **Note**

  This section of the docs is only relevant if the data used as inputs during the PR build are inconsistent with the data used as inputs during the last production build. Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to learn more.
</Note>

## What is data drift in CI?

Datafold is used in CI to illuminate the impact of a pull request's proposed code change by comparing two versions of the data and identifying differences.

**Data drift in CI** happens when those data differences occur due to *changes in upstream data sources*—not because of proposed code changes.

Data drift in CI adds "noise" to your CI testing analysis, making it tricky to tell if data differences are due to new code, or changes in the source data. Unless both versions rely on the same snapshot of upstream data, data drift can compromise your ability to see the true effect of the code changes.

<Tip>
  **Tip**

  dbt users should implement Slim CI in [dbt Core](https://www.datafold.com/blog/taking-your-dbt-ci-pipeline-to-the-next-level) or [dbt Cloud](https://www.datafold.com/blog/slim-ci-the-cost-effective-solution-for-successful-deployments-in-dbt-cloud) to prevent most instances of data drift. Slim CI reduces build time and eliminates most instances of data drift because the CI build depends on upstreams in production due to state deferral. However, Slim CI will not *completely* eliminate data drift in CI, specifically in cases where the model being modified in the PR depends on a source. In those cases, we recommend [**building twice in CI**](/deployment-testing/best-practices/handling-data-drift#build-twice-in-ci).
</Tip>

## Why prevent data drift in CI?

By eliminating data drift entirely, you can be confident that any differences detected in CI are driven only by your code, not unexpected data changes.

You can think of this as similar to a scientific experiment, where the control versus treatment groups ideally exist in identical baseline conditions, with the treatment as the only variable which would cause differential outcomes.

In practice, many organizations do not completely eliminate data drift, and still derive value from automatic data diffing and analysis conducted by Datafold in CI, in spite of minor noise that does exist.

## Handling data drift

We recommend two options for removing data drift to the greatest extent possible:

* [Build twice in CI](#build-twice-in-ci)
* [Build CI data from clone of prod sources](#build-ci-data-from-clone-of-prod-sources)

In both of these approaches, Datafold compares transformations of identical upstream data, so that any detected differences will be due to the code changes alone, ensuring an accurate comparison with no false positives.

By building two versions of the data in CI, you can ensure an "apples-to-apples" comparison that depends on the same version of upstream data.

When deciding between the two, choose the one that best matches your workflow:

| Workflow                                              | Approach                      | Why                                                                                           |
| ----------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------- |
| Data changes frequently in production                 | Build twice in CI             | Isolates PR impact without waiting on recent production updates, using a consistent snapshot. |
| Production has complex orchestration or multiple jobs | Build CI data from prod clone | Allows a stable comparison by freezing upstream data from a fixed production state.           |
| Performance and speed are critical                    | Build CI data from prod clone | Limits CI build to a single snapshot, reducing the processing load on the pipeline.           |
| Simplified orchestration with minimal dependencies    | Build twice in CI             | Reduces the need to manage production snapshots by running both environments in CI.           |

### Build twice in CI

This method involves two CI builds: one representing PR data, and another representing production data, both based on an identical snapshot of upstream data.

1. Create a fixed snapshot of the upstream data that both builds will use.
2. The CI pipeline executes two builds: one using the PR branch of code, and another using the base branch of code.
3. Datafold compares these two data environments, both created in CI, and detects differences.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4af6a3be0e9c23b3749718e509b3f685" data-og-width="1600" width="1600" data-og-height="1073" height="1073" data-path="images/deployment_testing/data-drift-architecture-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=efb5672ba068149181dd52467eced4a9 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e16e4dab91e5ab3262259f3cbf6a757e 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84776475ba7379451f5c7083f6ef3e85 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=94e2c2b507e3b053e3ebec23a43a9fdc 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=448aa14941898078c2f6811b2f848b62 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a456e60067785874ff9f7c53fffe93c1 2500w" />
</Frame>

<Note>
  If performance is a concern, you can use a reduced or filtered upstream data set to speed up the CI process while still providing rich insight into the data.
</Note>

<Note>
  This method assumes the production build doesn’t involve multiple jobs that process different sets of models at different times.
</Note>

### Build CI data from clone of prod sources

This method involves comparing a CI build based on a snapshot of the upstream source data *from the time of the last production build* to the production version of transformed data.

1. Update orchestration to create and store a snapshot of the upstream source data at the time of the production transformation job.
2. The CI pipeline executes a data transformation build using the PR branch of code, with the snapshotted upstream data as the upstream source.
3. Datafold compares the CI data environment with production data and detects differences.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=dfb3fea3a072ed93dfd9d1df61e612a7" data-og-width="1600" width="1600" data-og-height="1073" height="1073" data-path="images/deployment_testing/data-drift-solution-clone-of-prod.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c3135ad5a87531f0dbfcfb42d8bb0888 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3cd32956e685bd09274d50f67b602a33 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=07b9d676204f1b700433ca859948a5d0 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=82eb0091dbcddd7a4197eb3624c1a830 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a5476d1c597ae7efbfcf5b3ec973a690 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=edea7eb9c4fb444a74b30f6d8f129135 2500w" />
</Frame>


# Slim Diff
Source: https://docs.datafold.com/deployment-testing/best-practices/slim-diff

Choose which downstream tables to diff to optimize time, cost, and performance.

By default, Datafold diffs all modified models and downstream models. However, it won't make sense for all organizations to diff every downstream table every time you make a code update. Tradeoffs of time, cost, and risk must be considered.

That's why we created Slim Diff.

With Slim Diff enabled, Datafold will only diff models with dbt code changes in your Pull Request (PR).

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=7f8df7c3088ee7de6303eba741627e5b" data-og-width="1600" width="1600" data-og-height="1073" height="1073" data-path="images/deployment_testing/slim-diff-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=7c1e3d7326d4b2c4bcdf5c8a9408d6ed 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e0477c72f52c568e2a17b3ae87cc8caf 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4da34a62237b4a9c780b179a87fc8d25 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e6101b2ee0015bcb5bcee4522883ac77 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f2894cb5950383fd85990d9d66374c94 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4bf3a98d8595c537b00533e39f4a02a1 2500w" />
</Frame>

## Setting up Slim Diff

In Datafold, Slim Diff can be enabled by adjusting your diff settings by navigating to Settings → Integrations → CI → Select your CI tool → Advanced Settings and check the Slim Diff box:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=47702904f2d17c9cdeb39b99e6454b95" data-og-width="883" width="883" data-og-height="688" height="688" data-path="images/deployment_testing/slim-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8adae9bb4e6df64a9a4ecb4ae16733d1 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6d01d60c69efa14b65dcc562f485929f 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=709b877b189afb6f3d648639e5bb285e 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5fceec0f457ccd32402349936bf79a73 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=beecbe434fb9d97388d72a0406727454 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=532581c6f5c4c052e6d18219b3e59d31 2500w" />
</Frame>

## Diffing only modified models

With this setting turned on, only the modified models will be diffed by default.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e0707c61bf5e85634a3924ef30650492" data-og-width="1886" width="1886" data-og-height="802" height="802" data-path="images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1eb8c1594ac03c0c2d5bcfaf30d2b13f 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f57bd3e88ed16e9db6267a690319b6cb 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1d6db32c3365da0ac92a5f634432a2cf 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0f490ba01fbe6c53f44b30d09737dbca 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=345a3a197c39924a24e6b38229344bcb 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=04e1b5fca810ee9c2b42b2730dc84e0f 2500w" />
</Frame>

## Diff individual downstream models

Once Datafold has diffed only the modified models, you still have the option of diffing individual downstream models right within your PR.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dc39127b63705424aa89cc2f504d7b4a" data-og-width="1734" width="1734" data-og-height="700" height="700" data-path="images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b3884df7d44e0ef5430cf095a546d55c 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9a1cff3b0991afcddbe46dc7bcbdea8e 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=74cd9f3e2d5c3a7bcd18a637da99615c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fe210acaef87f3e69fcb946d113743eb 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2f1585b55169073505a424cd434bb3c3 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bde7b6c2b15c7f153bbf869996812100 2500w" />
</Frame>

## Diff all downstream models

You can also add the `datafold:diff-all-downstream` label within your PR, which will automatically diff *all* downstream models.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ee1105716276b26d932c303a0db51733" data-og-width="1884" width="1884" data-og-height="870" height="870" data-path="images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f36e4fedc137345a6d7314542a118289 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2152ddb5c3d92e55f124621d8960b625 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1637c775d06e35b5f03679002e8364e4 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=18d225eb875b9a1fd6c0fc07a5fa50c6 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b7ad5d7ade28ed877cb2c5325e71489c 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=97ba0d9d4a62d99b078673e9093b6d2b 2500w" />
</Frame>

## Explicitly define which models to always diff

Finally, with Slim Diff turned on, there might be certain models or subdirectories that you want to *always* diff when downstream. You can think of this as an exclusion to the Slim Diff behavior.

Apply the `slim_diff: diff_when_downstream` meta tag to individual models or entire folders in your `dbt_project.yml` file:

```Bash  theme={null}
models:
  <project_name>:
    <directory_name>:
      +materialized: view
      <model_name>:
        +meta:
          datafold:
            datadiff:
              slim_diff: diff_when_downstream

    <directory_name>:
      +meta:
        datafold:
          datadiff:
            slim_diff: diff_when_downstream
```

These meta tags can also be added in individual yaml files or in config blocks. More details about using meta tags are available in [the dbt docs](https://docs.getdbt.com/reference/resource-configs/meta).

With this configuration in place, Slim Diff will prevent downstream models from being run *unless* they have been designated as exceptions with the `slim_diff: diff_when_downstream` dbt meta tag.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1f117e6880687fabc1575f4964a91722" data-og-width="1924" width="1924" data-og-height="874" height="874" data-path="images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=faa6bc4aeefa6ab362cc19ee1f7fb28d 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f41b1cb4db53e415bf3030f44e80200d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=04313891c34afe163d0741ebf059b5bf 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c1fbf4c72b4ba74fb70203548c0b6cc9 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0f6efbef8db741e874fefa7ae030a211 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c848d3307d3760207c2d6a7f683765ff 2500w" />
</Frame>

As usual, once the PR has been opened, you'll still have the option of diffing individual downstream models that weren't diffed, or diffing all downstream models using the `datafold:diff-all-downstream` label.


# Configuration
Source: https://docs.datafold.com/deployment-testing/configuration

Explore configuration options for CI/CD testing in Datafold.

<CardGroup>
  <Card title="Primary Key Inference" href="/deployment-testing/configuration/primary-key" icon="file" horizontal>
    Learn how Datafold infers primary keys for accurate Data Diffs.
  </Card>

  <Card title="Column Remapping" href="/deployment-testing/configuration/column-remapping" icon="file" horizontal>
    Map renamed columns in PRs to their production counterparts.
  </Card>

  <Card title="Datafold CI Triggers" href="/deployment-testing/configuration/datafold-ci/on-demand" icon="folder-open" horizontal>
    Configure when Datafold runs in CI, including on-demand triggers.
  </Card>

  <Card title="Model-specific CI Configs" href="/deployment-testing/configuration/model-specific-ci/sql-filters" icon="folder-open" horizontal>
    Set model-specific filters and configurations for CI runs.
  </Card>
</CardGroup>


# Column Remapping
Source: https://docs.datafold.com/deployment-testing/configuration/column-remapping

Specify column renaming in your git commit message so Datafold can map renamed columns to their original counterparts in production for accurate comparison.

When your PR includes updates to column names, it's important to specify these updates in your git commit message using the following syntax. This allows Datafold to understand how renamed columns should be compared to the column in the production data with the original name.

## Example

By specifying column remapping in the commit message, instead of interpreting the change as a removing one column and adding another:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c492d769326e6c4c3a8882a3198332c8" data-og-width="2326" width="2326" data-og-height="602" height="602" data-path="images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=24e5cd73df50dc8ca97c3de3b0d4cdac 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=06f4da44a0f76e49812320b077d875c7 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=be2d7bd3cb7f9b1e8718568449b5f454 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9b2716806833b8d9967a3b4bf715b72b 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8edae7e8b4d940c119038abce698c45d 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=09cca214fdc5908a8d36c0e51df3dfd7 2500w" />
</Frame>

Datafold will recognize that the column has been renamed:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dac069059db9f6c994eac39bdfab09a6" data-og-width="2360" width="2360" data-og-height="884" height="884" data-path="images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4a51e513227eab1210b06b7fab9cc41f 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bb90eca4fa0a7970ca1e3a953cfff443 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9c11cec9893cea6f21e0f2a2f56fc905 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=eb4351b13b52430ffb7aacab6e0ed05e 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0105a05b53050cad0cf531805a471769 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5e30f215d3d1fe885b836247d5d2f228 2500w" />
</Frame>

## Syntax for column remapping

You can use any of the following syntax styles as a single line to a commit message to instruct Datafold in CI to remap a column from `oldcol` to `newcol`.

```Bash  theme={null}
# All models/tables in the PR:
datafold remap oldcol newcol
X-Datafold: rename oldcol newcol
/datafold renamed oldcol newcol
datafold: remapped oldcol newcol

# Filtered models/tables by shell-like glob:
datafold remap oldcol newcol model_NAME
X-Datafold: rename oldcol newcol TABLE
/datafold renamed oldcol newcol VIEW_*

```

## Chaining together column name updates

Commit messages can be chained together to reflect sequential changes. This means that a commit message does not lock you in to renaming a column.

For example, if your commit history looks like this:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f980e14e0eee444c14eedb9b75f094c" data-og-width="1098" width="1098" data-og-height="254" height="254" data-path="images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aebc576141e678c0ff75e3742df43e41 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=628675b62c028d16bfdf20c4be130b7b 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2ca1f2c9129c3fbd7c92011a02087cb4 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0689e2432d0ec94a4ae177b8b1cdc716 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=70e977b6cb99a56272f63f8221ccaec8 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a2989342a14ba2047110a914b3a0234d 2500w" />
</Frame>

Datafold will understand that the production column `name` has been renamed to `first_name` in the PR branch.

## Handling column renaming in git commits and PR comments

### Git commits

Git commits track changes on a change-by-change basis and linearize history assuming merged branches introduce new changes on top of the base/current branch (1st parent).

### PR comments

PR comments apply changes to the entire changeset.

### When to use git commits or PR comments?

When handling chained renames:

* **Git commits:** Sequential renames (`col1 > col2 > col3`) result in the final rename (`col1 > col3`).
* **PR comments:** It's best to specify the final result directly (`col1 > col3`). Sequential renames (`col1 > col2 > col3`) can also work, but specifying the final state simplifies understanding during review.

| Aspect                    | Git Commits                                                                                                       | PR Comments                                                                                                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tracking Changes**      | Tracks changes on a change-by-change basis.                                                                       | Applies changes to the entire changeset.                                                                                                                                                    |
| **History Linearization** | Linearizes history assuming merged branches introduce new changes on top of the base/current branch (1st parent). | N/A                                                                                                                                                                                         |
| **Chained Renames**       | Sequential renames (col1 > col2 > col3) result in the final rename (col1 > col3).                                 | It's best to specify the final result directly (col1 > col3). Sequential renames (col1 > col2 > col3) can also work, but specifying the final state simplifies understanding during review. |
| **Precedence**            | Renames specified in git commits are applied in sequence unless overridden by subsequent commits.                 | PR comments take precedence over renames specified in git commits if applied during the review process.                                                                                     |

These guidelines ensure consistency and clarity when managing column renaming in collaborative development environments, leveraging Datafold's capabilities effectively.


# Running Data Diff for Specific PRs/MRs
Source: https://docs.datafold.com/deployment-testing/configuration/datafold-ci/on-demand

By default, Datafold CI runs on every new pull/merge request and commits to existing ones.

To **only** run Datafold CI when the user explicitly requests it, you can set **Run only when tagged** option in the Datafold app [CI settings](https://app.datafold.com/settings/integrations/ci) which will only allow Datafold CI to run if a `datafold` tag/label is assigned to the pull/merge request.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a1872bbe27be3779fa79908ecff53ba1" data-og-width="1980" width="1980" data-og-height="1030" height="1030" data-path="images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c04d7824efb2d2943058fabfd4bd3740 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=667677d57e58e9acae205bf7fdf1cc1d 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=59f3ccbc8e78e3b696090910cce116af 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9368ce4d5832ca5f77f1b38cfad40328 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a8819937fa20899398b770f344d1c92f 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a978e793c77796292c89145d197df739 2500w" />
</Frame>

## Running data diff on specific file changes

By default, Datafold CI will run on any file change in the repo. To skip Datafold CI runs for certain modified files (e.g., if the dbt code is placed in the same repo with non-dbt code), you can specify files to ignore. The pattern uses the syntax of .gitignore. Excluded files can be re-included by using the negation.

### Example

Let's say the dbt project is a folder in a repo that contains other code (e.g., Airflow). We want to run Datafold CI for changes to dbt models but skip it for other files. For that, we exclude all files in the repo except those the /dbt folder. We also want to filter out `.md` files in the /dbt folder:

```Bash  theme={null}
*!dbt/*dbt/*.md
```

<Tip>
  **SKIPPING SPECIFIC DBT MODELS**

  To skip diffing individual dbt models in CI, use the [never\_diff](/deployment-testing/configuration/model-specific-ci/excluding-models) option in the Datafold dbt yaml config.
</Tip>


# Running Data Diff on Specific Branches
Source: https://docs.datafold.com/deployment-testing/configuration/datafold-ci/specifc

By default, Datafold CI runs on every new pull/merge request and commits to existing ones.

You can set **Custom base branch** option in the Datafold app [CI settings](https://app.datafold.com/settings/integrations/ci), to only run Datafold CI on pull requests that have a specific base branch. This might be useful if you have multiple environments built from different branches. For example, `staging` and `production` environments built from `staging` and `main` branches respectively. Using the option, you can have 2 different CI configurations in Datafold, one for each environment, and only run the CI for the corresponding branch.


# Diff Timeline
Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/diff-timeline

Specify a `time_column` to visualize match rates between tables for each column over time.

```Bash  theme={null}
models:
  - name: users
    meta:
      datafold:
        datadiff:
          time_column: created_at
```


# Excluding Models
Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/excluding-models

Use `never_diff` to exclude a model or subdirectory of models from data diffs.

```Bash  theme={null}
models:
  - name: users
    meta:
      datafold:
        datadiff:
          never_diff: true
```


# Including/Excluding Columns
Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/including-excluding-columns

Specify columns to include or exclude from the data diff using `include_columns` and `exclude_columns`.

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


# SQL Filters
Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/sql-filters

Use dbt YAML configuration to set model-specific filters for Datafold CI.

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


# Time Travel
Source: https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/time-travel

Use `prod_time_travel` and `pr_time_travel` to diff tables from specific points in time.

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


# Primary Key Inference
Source: https://docs.datafold.com/deployment-testing/configuration/primary-key

Datafold requires a primary key to perform data diffs. Using dbt metadata, Datafold identifies the column to use as the primary key for accurate data diffs.

Datafold supports composite primary keys, meaning that you can assign multiple columns that make up the primary key together.

## Metadata

The first option is setting the `primary-key` key in the dbt metadata. There are [several ways to configure this](https://docs.getdbt.com/reference/resource-configs/meta) in your dbt project using either the `meta` key in a yaml file or a model-specific config block.

```Bash  theme={null}
models:
  - name: users
    columns:
      - name: user_id
        meta:
          primary-key: true
    ## for compound primary keys, set all parts of the key as a primary-key ##
    # - name: company_id
    #   meta:
    #     primary-key: true
```

## Tags

If the primary key is not found in the metadata, it will go through the [tags](https://docs.getdbt.com/reference/resource-properties/tags).

```Bash  theme={null}
models:
  - name: users
    columns:
      - name: user_id
        tags:
          - primary-key
    ## for compound primary keys, tag all parts of the key ##
    # - name: company_id
    #   tags:
    #       - primary-key

```

## Inferred

If the primary key isn't provided explicitly, Datafold will try to infer a primary key from dbt's uniqueness tests. If you have a single column uniqueness test defined, it will use this column as the PK.

```Bash  theme={null}
models:
  - name: users
    columns:
      - name: user_id
        tests:
          - unique
```

Also, model-level uniqueness tests can be used for inferring the PK.

```Bash  theme={null}
models:
  - name: sales
    columns:
      - name: col1
      - name: col2
      ...
    tests:
      - unique:
          column_name: "col1 || col2"
          # or
          column_name: "CONCAT(col1, col2)"
      # we also support dbt_utils unique_combination_of_columns test
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns:
            - order_no
            - order_line
```

Keep in mind that this is a failover mechanism. If you change the uniqueness test, this will also impact the way Datafold performs the diff.


# Getting Started with CI/CD Testing
Source: https://docs.datafold.com/deployment-testing/getting-started

Learn how to set up CI/CD testing with Datafold by integrating your data connections, code repositories, and CI pipeline for automated testing.

<Tip>
  **TEAM CLOUD**

  <Icon icon="wrench" /> Interested in adding Datafold Team Cloud to your CI pipeline? [Let's talk](https://calendly.com/d/zkz-63b-23q/see-a-demo?email=clay%20analytics%40datafold.com\&first_name=Clay\&last_name=Moeller\&a1=\&month=2024-07)! <Icon icon="phone-rotary" />
</Tip>

## Getting Started with Deployment Testing

<Steps>
  <Step title="Set up your data connection">
    To get started, first set up your [data connection](https://docs.datafold.com/integrations/databases) to ensure that Datafold can access and monitor your data sources.
  </Step>

  <Step title="Integrate with code repositories">
    Next, integrate Datafold with your version control system by following the instructions for [code repositories](https://docs.datafold.com/integrations/code-repositories). This allows Datafold to track and test changes in your data pipelines.
  </Step>

  <Step title="Add Datafold to your CI pipeline">
    Add Datafold to your continuous integration (CI) pipeline to enable automated deployment testing. You can do this through our universal [Fully-Automated](../deployment-testing/getting-started/universal/fully-automated), [No-Code](../deployment-testing/getting-started/universal/no-code), [API](../deployment-testing/getting-started/universal/api), or [dbt](../integrations/orchestrators) integrations.
  </Step>

  <Step title="Optional: Connect data apps">
    Optionally, you can [connect data apps](https://docs.datafold.com/integrations/bi_data_apps) to extend your testing and monitoring to data applications like BI tools.
  </Step>
</Steps>


# API
Source: https://docs.datafold.com/deployment-testing/getting-started/universal/api

Learn how to set up and configure Datafold's API for CI/CD testing.

## 1. Create a repository integration

Integrate your code repository using the appropriate [integration](/integrations/code-repositories).

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=45fd70946a2add757d79098af039b429" data-og-width="2084" width="2084" data-og-height="742" height="742" data-path="images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a69e88590a390b61e72569c53a496d24 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd0d01e133d73d97290b898e2f53623b 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3cc0312866dc746c1654834ce3d07382 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2ada31061cc7d4abc5d4939d4e8d80c3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cf99b0fd987b5dbc15bc46d84fc7d927 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b4ab64b5e13ef955ff4aab55f4d16879 2500w" />
</Frame>

## 2. Create an API integration

In the Datafold app, create an API integration.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7be3befc9aa261a2f155ee155143944f" data-og-width="2072" width="2072" data-og-height="1094" height="1094" data-path="images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5d13b05cc2d3dd048ad48377bb57949f 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e86d492621fd5f2659d3cb40a837dbd 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=50a25d67b9a037262eb9b655aff8fa47 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e1e685b014a75fc3fb1c2089c72618a 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=128ba338ad334a2fe0d45e75905ded8a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4a47c0ba9c62d731a7da05666aac7cd5 2500w" />
</Frame>

## 3. Set up the API integration

Complete the configuration by specifying the following fields:

### Basic settings

| Field Name         | Description                                               |
| ------------------ | --------------------------------------------------------- |
| Configuration name | Choose a name for your for your Datafold dbt integration. |
| Repository         | Select the repository you configured in step 1.           |
| Data Source        | Select the data source your repository writes to.         |

### Advanced settings: Configuration

| Field Name                     | Description                                                                                                                                                                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Diff Hightouch Models          | Run data diffs for Hightouch models affected by your PR.                                                                                                                                                                                                                   |
| CI fails on primary key issues | If null or duplicate primary keys exist, CI will fail.                                                                                                                                                                                                                     |
| Pull Request Label             | When this is selected, the Datafold CI process will only run when the 'datafold' label has been applied.                                                                                                                                                                   |
| CI Diff Threshold              | Data Diffs will only be run automatically for given CI Run if the number of diffs doesn't exceed this threshold.                                                                                                                                                           |
| Custom base branch             | If defined, the Datafold CI process will only run on pull requests with the specified base branch.                                                                                                                                                                         |
| Files to ignore                | Datafold CI diffs all changed models in the PR if at least one modified file doesn’t match the ignore pattern. Datafold CI doesn’t run in the PR if all modified files should be ignored. ([Additional details.](/deployment-testing/configuration/datafold-ci/on-demand)) |

### Advanced settings: Sampling

| Field Name          | Description                                                                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable sampling     | Enable sampling for data diffs to optimize analyzing large datasets.                                                                                                   |
| Sampling tolerance  | The tolerance to apply in sampling for all data diffs.                                                                                                                 |
| Sampling confidence | The confidence to apply when sampling.                                                                                                                                 |
| Sampling threshold  | Sampling will be disabled automatically if tables are smaller than specified threshold. If unspecified, default values will be used depending on the Data Source type. |

## 4. Obtain a Datafold API Key and CI config ID

Generate a new Datafold API Key and obtain the CI config ID from the CI API integration settings page:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e65dd3975cef3b16ad203a0e6dfc1e7c" data-og-width="2310" width="2310" data-og-height="972" height="972" data-path="images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e0e7022637f64e95d0f4c01e6f09db1 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4fc016fc32528e5f1f08b4f9edc88cc7 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b570523c1b5d58809b253754f6fbe82f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc99d5527fc2951e3c3919f784b15955 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=23aaa8a8a35b8d3bfe814868517fca80 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8d376a542ad6683d9418572183ba8542 2500w" />
</Frame>

You will need these values later on when setting up the CI Jobs.

## 5. Install Datafold SDK into your Python environment

```Bash  theme={null}
pip install datafold-sdk
```

## 6. Configure your CI script(s) with the Datafold SDK

Using the Datafold SDK, configure your CI script(s) to use the Datafold SDK `ci submit` command. The example below should be adapted to match your specific use-case.

```Bash  theme={null}
datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num <pr_num> --diffs ./diffs.json
```

Since Datafold cannot infer which tables have changed, you'll need to manually provide this information in a specific `json` file format. Datafold can then determine which models to diff in a CI run based on the `diffs.json` you pass in to the Datafold SDK `ci submit` command.

```Bash  theme={null}
[
  {
    "prod": "MY.PROD.TABLE", // Production table to compare PR changes against
    "pr": "MY.PR.TABLE", // Changed table containing data modifications in the PR
    "pk": ["MY", "PK", "LIST"], // Primary key; can be an empty array
    // These fields are not required and can be omitted from the JSON file:
    "include_columns": ["COLUMNS", "TO", "INCLUDE"],
    "exclude_columns": ["COLUMNS", "TO", "EXCLUDE"]
  }
]
```

Note: The `JSON` file is optional and you can also achieve the same effect by using standard input (stdin) as shown here. However, for brevity, we'll use the `JSON` file approach in this example:

```Bash  theme={null}
datafold ci submit \
    --ci-config-id <datafold_ci_config_id> \
    --pr-num <pr_num> <<- EOF
[{
        "prod": "MY.PROD.TABLE",
        "pr": "MY.PR.TABLE",
        "pk": ["MY", "PK", "LIST"]
}]
```

Implementation details will vary depending on [which CI tool](#ci-implementation-tools) you use. Please review the following instructions and examples for your organization's CI tool.

<Info>
  **NOTE**

  Populating the `diffs.json` file is specific to your use case and therefore out of scope for this guide. The only requirement is to adhere to the `JSON` schema structure explained above.
</Info>

## CI Implementation Tools

We've created guides and templates for three popular CI tools.

<Tip>
  **HAVING TROUBLE SETTING UP DATAFOLD IN CI?**

  <Icon icon="hand-wave" /> We're here to help! Please [reach out and chat with a Datafold Solutions Engineer](https://www.datafold.com/booktime). <Icon icon="phone-rotary" />
</Tip>

To add Datafold to your CI tool, add `datafold ci submit` step in your PR CI job.

<Tabs>
  <Tab title="GitHub Actions">
    ```Bash  theme={null}
    name: Datafold PR Job

    # Run this job when a commit is pushed to any branch except main
    on:
      pull_request:
      push:
        branches:
          - '!main'

    jobs:
      run:
        runs-on: ubuntu-20.04 # your image will vary

        steps:

          - name: Install Datafold SDK
            run: pip install -q datafold-sdk
        # ...
          - name: Upload what to diff to Datafold
            run: datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num ${PR_NUM} --diffs <path_to_diffs_json_file>
            env:
              # env variables used by Datafold SDK internally
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
              DATAFOLD_HOST: ${DATAFOLD_HOST}
              # For Dedicated Cloud/private deployments of Datafold,
              # Set the "https://custom.url.datafold.com" variable as the base URL as an environment variable, either as a string or a project variable
              # There are multiple ways to get the PR_NUM, this is just a simple example
              PR_NUM: ${{ github.event.number }}
    ```

    Be sure to replace `<datafold_ci_config_id>` with the [CI config ID](#4-obtain-a-datafold-api-key-and-ci-config-id) value.

    <Info>
      **NOTE**

      It is beyond the scope of this guide to provide guidance on generating the `<path_to_diffs_json_file>`, as it heavily depends on your specific use case. However, ensure that the generated file adheres to the required schema outlined above.
    </Info>

    Finally, store [your Datafold API Key](#4-obtain-a-datafold-api-key-and-ci-config-id) as a secret named `DATAFOLD_API_KEY` [in your GitHub repository settings](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

    Once you've completed these steps, Datafold will run data diffs between production and development data on the next GitHub Actions CI run.
  </Tab>

  <Tab title="CircleCI">
    ```Bash  theme={null}
    version: 2.1

    jobs:
      artifacts-job:
        filters:
          branches:
            only: main # or master, or the name of your default branch
        docker:
          - image: cimg/python:3.9 # your image will vary
              env:
                # env variables used by Datafold SDK internally
                DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
                DATAFOLD_HOST: ${DATAFOLD_HOST}
                # For Dedicated Cloud/private deployments of Datafold,
                # Set the "https://custom.url.datafold.com" variable as the base URL as an environment variable, either as a string or a project variable, per https://circleci.com/docs/set-environment-variable/
                # There are multiple ways to get the PR_NUM, this is just a simple example
                PR_NUM: ${{ github.event.number }}
        steps:
          - checkout
          - run:
              name: "Install Datafold SDK"
              command: pip install -q datafold-sdk

          - run:
              name: "Upload what to diff to Datafold"
              command: datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num ${CIRCLE_PULL_REQUEST} --diffs <path_to_diffs_json_file>
    ```

    Be sure to replace `<datafold_ci_config_id>` with the [CI config ID](#4-obtain-a-datafold-api-key-and-ci-config-id) value.

    <Info>
      **NOTE**

      It is beyond the scope of this guide to provide guidance on generating the `<path_to_diffs_json_file>`, as it heavily depends on your specific use case. However, ensure that the generated file adheres to the required schema outlined above.
    </Info>

    Then, enable [**Only build pull requests**](https://circleci.com/docs/oss#only-build-pull-requests) in CircleCI. This ensures that CI runs on pull requests and production, but not on pushes to other branches.

    Finally, store [your Datafold API Key](#4-obtain-a-datafold-api-key-and-ci-config-id) as a secret named `DATAFOLD_API_KEY` [your CircleCI project settings.](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

    Once you've completed these steps, Datafold will run data diffs between production and development data on the next CircleCI run.
  </Tab>

  <Tab title="GitLab CI">
    ```Bash  theme={null}

    image:
    name: ghcr.io/dbt-labs/dbt-core:1.x # your name will vary
    entrypoint: [ "" ]
    variables:
      # env variables used by Datafold SDK internally
      DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
      DATAFOLD_HOST: ${DATAFOLD_HOST}
      # For Dedicated Cloud/private deployments of Datafold,
      # Set the "https://custom.url.datafold.com" variable as the base URL as an environment variable, either as a string or a project variable
      # There are multiple ways to get the PR_NUM, this is just a simple example
      PR_NUM: ${{ github.event.number }}

    run_pipeline:
      stage: test
      before_script:
        - pip install -q datafold-sdk

      script:
        # Upload what to diff to Datafold
        - datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num $CI_MERGE_REQUEST_ID --diffs <path_to_diffs_json_file>
     rules:
        - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    ```

    Be sure to replace `<datafold_ci_config_id>` with the [CI config ID](#4-obtain-a-datafold-api-key-and-ci-config-id) value.

    <Info>
      **NOTE**

      It is beyond the scope of this guide to provide guidance on generating the `<path_to_diffs_json_file>`, as it heavily depends on your specific use case. However, ensure that the generated file adheres to the required schema outlined above.
    </Info>

    Finally, store [your Datafold API Key](#4-obtain-a-datafold-api-key-and-ci-config-id) as a secret named `DATAFOLD_API_KEY` [in your GitLab project's settings](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

    Once you've completed these steps, Datafold will run data diffs between production and development data on the next GitLab CI run.
  </Tab>
</Tabs>

## Optional CI Configurations and Strategies

### Skip Datafold in CI

To skip the Datafold step in CI, include the string `datafold-skip-ci` in the last commit message.


# Fully-Automated
Source: https://docs.datafold.com/deployment-testing/getting-started/universal/fully-automated

Automatically diff tables modified in a pull request with Datafold's Fully-Automated CI integration.

Our Fully-Automated CI integration enables you to automatically diff tables modified in a pull request so you know exactly how your data will change before going to production.

We do this by analyzing the SQL in any changed files, extracting the relevant table names, and diffing those tables between your staging and production environments. We then post the results of those diffs—including any downstream impact—to your pull request for all to see. All without manual intervention.

## Prerequisites

* Your code must be hosted in one of our supported version control integrations
* Your tables/views must be defined in SQL
* Your schema names must be parameterized ([see below](#4-parameterize-schema-names))
* You must be automatically generating staging data ([more info](/deployment-testing/how-it-works))

## Get Started

Get started in just a few easy steps.

### 1. Generate a Datafold API key

If you haven't already generated an API key (you only need one), visit Settings > Account and select **Create API Key**. Save the key somewhere safe like a password manager, as you won't be able to view it later.

### 2. Set up a version control integration

Open the Datafold app and navigate to Settings > Integrations > Repositories to connect the repository that contains the code you'd like to automatically diff.

### 3. Add a step to your CI workflow

<Note>This example assumes you're using GitHub actions, but the approach generalizes to any version control tool we support including GitLab, Bitbucket, etc.</Note>

Either [create a new GitHub Action](https://docs.github.com/en/actions/writing-workflows/quickstart) or add the following steps to an existing one:

```yaml  theme={null}
- name: Install datafold-sdk
  run: pip install -q datafold-sdk

- name: Trigger Datafold CI
  run: |
    datafold ci auto trigger --ci-config-id $CI_CONF_ID --pr-num $PR_NUM 
    --base-sha $BASE_SHA --pr-sha $PR_SHA --reference-params "$REFERENCE_PARAMS" 
    --pr-params "$PR_PARAMS"
  env:
    DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
    CI_CONF_ID: 436
    PR_NUM:  "${{ steps.findPr.outputs.pr }}"
    PR_SHA: "${{ github.event.pull_request.head.sha }}"
    BASE_SHA: ${{ github.event.pull_request.base.sha }}
    REFERENCE_PARAMS: '{ "target_schema": "nc_default" }'
    PR_PARAMS: "{ \"target_schema\": \"${{ env.TARGET_SCHEMA }}\" }"
```

### 4. Parameterize schema names

If it's not already the case, you'll need to parameterize the schema for any table paths you'd like Datafold to diff. For example, let's say you have a file called `dim_orgs.sql` that defines a table called `DIM_ORGS` in your warehouse. Your SQL should look something like this:

```sql  theme={null}
-- datafold: pk=org_id
CREATE OR REPLACE TABLE analytics.${target_schema}.dim_orgs AS (
  SELECT
    org_id,
    org_name,
    employee_count,
    created_at
  FROM analytics.${target_schema}.org_created
);
```

### 5. Provide primary keys (optional)

<Note>While this step is technically optional, we strongly recommend providing primary keys for any tables you'd like Datafold to diff.</Note>

In order for Datafold to perform full value-level comparisons between staging and production tables, Datafold needs to know the primary keys. To provide this information, place a comment above each query using the `-- datafold: pk=<your_pk>` syntax shown below:

```sql  theme={null}
-- datafold: pk=org_id
CREATE OR REPLACE TABLE analytics.${target_schema}.dim_orgs AS (
  SELECT
    org_id,
...
```

### 6. Create a pull request

When you create a pull request, Datafold will automatically detect it, attempt to diff any tables modified in the code, and post a summary as a comment in the PR. You can click through on the comment to view a more complete analysis of the changes in the Datafold app. Happy diffing!

## Need help?

If you have any questions about Fully-Automated CI, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# No-Code
Source: https://docs.datafold.com/deployment-testing/getting-started/universal/no-code

Set up Datafold's No-Code CI integration to create and manage Data Diffs without writing code.

Monitors are easy to create and manage in the Datafold app. But for teams (or individual users) who prefer a more code-based approach, our monitors as code feature allows managing monitors via version-controlled YAML.

## Getting Started

Get up and running with our No-Code CI integration in just a few steps.

### 1. Create a repository integration

Connect your code repository using the appropriate [integration](/integrations/code-repositories).

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=45fd70946a2add757d79098af039b429" data-og-width="2084" width="2084" data-og-height="742" height="742" data-path="images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a69e88590a390b61e72569c53a496d24 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd0d01e133d73d97290b898e2f53623b 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3cc0312866dc746c1654834ce3d07382 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2ada31061cc7d4abc5d4939d4e8d80c3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cf99b0fd987b5dbc15bc46d84fc7d927 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b4ab64b5e13ef955ff4aab55f4d16879 2500w" />
</Frame>

### 2. Create a No-Code integration

From the integrations page, create a new No-Code CI integration.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7be3befc9aa261a2f155ee155143944f" data-og-width="2072" width="2072" data-og-height="1094" height="1094" data-path="images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5d13b05cc2d3dd048ad48377bb57949f 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e86d492621fd5f2659d3cb40a837dbd 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=50a25d67b9a037262eb9b655aff8fa47 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e1e685b014a75fc3fb1c2089c72618a 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=128ba338ad334a2fe0d45e75905ded8a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4a47c0ba9c62d731a7da05666aac7cd5 2500w" />
</Frame>

### 3. Set up the No-Code integration

Complete the configuration by specifying the following fields:

#### Basic settings

| Field Name         | Description                                           |
| ------------------ | ----------------------------------------------------- |
| Configuration name | Choose a name for your Datafold integration.          |
| Repository         | Select the repository you configured in step 1.       |
| Data Connection    | Select the data connection your repository writes to. |

#### Advanced settings

| Field Name         | Description                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Pull request label | When this is selected, the Datafold CI process will only run when the `datafold` label has been applied to your pull request. |
| Custom base branch | If provided, the Datafold CI process will only run on pull requests against the specified base branch.                        |

### 4. Create a pull request and add diffs

Datafold will automatically post a comment on your pull request with a link to generate a CI run that corresponds to the latest set of changes.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e8dc9f691dd36c5b59f8a832f7c5ef90" data-og-width="1033" width="1033" data-og-height="622" height="622" data-path="images/1-7a001321004a1afa68a3bd74a4bb822d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=59cb82e2ee41b716816ede9085085353 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=239b202662245ccb9c78fd41786d5f91 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f387cd9dc8c008824f6eeca5ec21e71c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a8b9eee6e6aef7d0c0f8d280858cfb15 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5c44de689cfb9f78de714064eb6d3609 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dc5ca756ef235c762cde0f0f9e941212 2500w" />
</Frame>

### 5. Add diffs to your CI run

Once in Datafold, add as many pull requests as you'd like to the CI run. If you need a refresher on how to configure data diffs, check out [our docs](/data-diff/in-database-diffing/creating-a-new-data-diff).

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b8de0e72e6d42738e3538834bd51ad19" data-og-width="1292" width="1292" data-og-height="696" height="696" data-path="images/4-800a438c5251d6888b83a1f9e3c811bb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a322fb992c2f19bc19aeee0370e1e0bb 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8d24e8bbd9faf0e9e0968391dc7a4da9 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a556956ee858b83f15df1183405742eb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=46d75ba6cb4e9f6d2987c9f97fd58186 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2654e257f99837a8e9311575632577d0 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1f77b255c440ee8f54e24e4f91efbd22 2500w" />
</Frame>

### 6. Add a summary to your pull request

Click on **Save and Add Preview to PR** to post a summary to your pull request.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=386e1a389aae5b12600fc22912f5f48b" data-og-width="1321" width="1321" data-og-height="522" height="522" data-path="images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=eca70eecd76a85c1bc0240f7049ef059 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e4bb9cfe5324703779943c9db4324bc0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d962ce1398ce803578a3af02bcaa851f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0e88cf6e1992e2bbe6b9f4282698f6e8 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e4de295c456d6de6f98e79c40e20eedb 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=488eae433e397515264c7ec6c7f75055 2500w" />
</Frame>

### 7. View the summary in your pull request

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b43855e4da91adf49b0dfbab2da269f1" data-og-width="934" width="934" data-og-height="789" height="789" data-path="images/3-33123cf19f9ff7f5fa1aef9952d8208d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=847b01768e805d2de27656f71b4d6a14 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e870cd6078f7a841649326c90ae40faa 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1123c9dbd70ed78a60a10431feab998a 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=76db4ba13ca6dbd931f2cca19715120a 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d788e7d68bac7eb90e8e204e8dd467a9 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0decfea251860812a4fdca7bfcade7b4 2500w" />
</Frame>

## Cloning diffs from the last CI run

If you make additional changes to your pull request, clicking the **Add data diff** button generates a new CI run in Datafold. From there, you can:

* Create a new Data Diff from scratch
* Clone diffs from the last CI run

You can also diff downstream tables by clicking on the **Add Data Diff** button in the Downstream Impact table. This creates additional Data Diffs:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cfddbf0cccec7c25713c3ef567b27096" data-og-width="1143" width="1143" data-og-height="743" height="743" data-path="images/5-c411b13fcdaebb9587fabcfcef92c740.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a8f12789bbbc07e1c70f14fbc19b7581 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=24b431abf786e2daa6e4711c8f55e007 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3a1d9f4d32c7393e774a5fd1fc05f0b4 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dd996cbef054a8180126ac567c6b2fb0 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=282130b7029845acf13096e609cdfa0b 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=adbf58519948c822bc29e4dce9c64fdb 2500w" />
</Frame>

You can then post another summary to your pull request by clicking **Save and Add Preview to PR**.


# How Datafold in CI Works
Source: https://docs.datafold.com/deployment-testing/how-it-works

Learn how Datafold integrates with your Continuous Integration (CI) process to create Data Diffs for all SQL code changes, catching issues before they make it into production.

## What is CI?

Continuous Integration (or CI) is a process for building and testing changes to your code before deploying to production. This ensures early detection of potential issues and improves the quality of code deployment.

| Without CI                                                                       | With CI                                                                  |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Updates are manually coordinated and become a complex synchronization chore.     | Smoothly manage code changes, and scale as your team and code base grow. |
| Testing is done manually, if at all.                                             | Automate high-confidence test coverage.                                  |
| Code changes are released at a slower cadence, and with higher rates of failure. | Boost the quantity and quality of developer output.                      |

### Datafold in CI

For Datafold to work in CI, you need to add a step that builds <Tooltip tip="Staging data is created using the version of the code in your PR/MR branch, which contains the edits you're currently working on.">staging data</Tooltip> in your CI process (e.g., GitHub).

<Note>
  **Prerequisite: Building staging data in CI**

  If you're using dbt, you'll need to add a dbt build step to your CI pipeline first. This can be done through either [dbt Cloud](https://www.datafold.com/blog/slim-ci-the-cost-effective-solution-for-successful-deployments-in-dbt-cloud) or [dbt Core](https://www.datafold.com/blog/accelerating-dbt-core-ci-cd-with-github-actions-a-step-by-step-guide).

  For other orchestrators like Airflow, follow [this guide](https://www.datafold.com/blog/datafold-in-ci-is-for-everyone) to build staging data in CI, or contact us for custom recommendations based on your infrastructure.
</Note>

In this short clip, see how the Datafold bot automatically comments on your PR, highlighting data differences between the production and development versions of your code:

<Frame>
  <video src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/small-video-01.mp4?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=547067fb87c55ddcf11071999197c33e" controls data-path="images/small-video-01.mp4" />
</Frame>

## Creating production and staging data

When Datafold is integrated into your CI, it automatically detects and highlights value-level differences between production data and staging data.

These summarized Data Diff results are written directly in your pull request (PR) as a comment. From the comment, you can access the Datafold App to explore value-level differences, understand the impact on downstream BI tools, and other context-rich information about the impact of your PR code changes.

### Production data

Production data refers to the data that your organization depends on for daily operations, such as powering dashboards and BI tools. Your orchestrator (e.g., dbt, Airflow) is responsible for running SQL code that builds and maintains this data in your warehouse.

If you use dbt, we'll assume that you have a production job in either [dbt Cloud](https://docs.getdbt.com/docs/deploy/dbt-cloud-job) or [dbt Core](https://docs.getdbt.com/docs/deploy/deployment-tools) that builds or updates your dbt models in the warehouse on a schedule. Or, you might have a scheduled job in Airflow or another orchestrator that builds production data on a regular basis.

### Staging data

For Datafold to run Data Diffs in CI, you need a step in your CI process that builds staging data (a version of your data in a dedicated schema) using the code in your PR/MR branch. Datafold will compares this staging data against your production data when diffing.

<Tip>
  **Tip**

  You can use either dbt Cloud or dbt Core to add a step in your CI process that builds staging data.
</Tip>

* [Setting up dbt in CI for dbt Cloud users](https://www.datafold.com/blog/slim-ci-the-cost-effective-solution-for-successful-deployments-in-dbt-cloud)
* [Setting up dbt in CI for dbt Core users](https://www.datafold.com/blog/accelerating-dbt-core-ci-cd-with-github-actions-a-step-by-step-guide)
* [Building staging data in CI using Airflow](https://www.datafold.com/blog/datafold-in-ci-is-for-everyone)

## Comparing production and staging data

Once you have a job in CI that builds staging data, you're ready to get started with Datafold in CI!

By comparing production and staging data, Datafold ensures that any code changes are thoroughly validated before being merged, helping to prevent data issues from reaching production.

We'll walk through the setup steps in more detail in the [Getting Started](/deployment-testing/getting-started) section.

### Datafold in CI for dbt users

While Datafold can be added to CI no matter what orchestrator you use, it's worth detailing exactly how this works with dbt, a popular and opinionated tool for which we have specific recommendations.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fc7be62f6921f1442259d7ab7a16dbbf" data-og-width="2700" width="2700" data-og-height="1650" height="1650" data-path="images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=79fbf7fc5316de70238ee374a2bb8f92 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3c29bc65f8b9b8790ba7b86e6bab86f0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=549d668227fc5d89efd287d1f5a4a321 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1a7df0e01c5f28f56d98de5138f978ad 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c03bb87c3a2fc317f00fb6d3ade17d99 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/Datafold_in_dbt_CI-750487e5bd8ef031a87c205cbc6e5fea.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f5c30b8af26e3c37106d963a69dc7042 2500w" />
</Frame>

Here is how Datafold + dbt in CI works:

<Steps>
  <Step title="Submit dbt Project Manifests">
    Two versions of your dbt project's `manifest.json` are submitted to Datafold, representing the state of the production code and the PR/MR code.

    * For dbt Cloud users, this submission happens automatically.
    * dbt Core users need to add steps in their CI configuration (e.g., Circle CI, GitHub Actions, or GitLab) to submit the artifacts.
  </Step>

  <Step title="Identify Code Differences">
    Datafold compares the two versions of the `manifest.json` to identify differences in the code.
  </Step>

  <Step title="Run Data Diffs">
    Datafold queries your data warehouse to run Data Diffs on the modified dbt models. It also identifies downstream assets (e.g., BI tools, reverse ETL pipelines) that might be impacted by the changes.

    * Datafold can diff dbt models that are materialized as both tables and views.
    * If your dbt project has many downstream dependencies, you can use [Slim Diff](/deployment-testing/best-practices/slim-diff) or other [configuration options](/deployment-testing/configuration) to manage scale, ensuring critical models are prioritized.
  </Step>

  <Step title="Summarize Data Diffs in Pull Request">
    The results of the Data Diffs are summarized in a comment on your pull request (e.g., in GitHub). You can click the comment to view more detailed information in the Datafold application.
  </Step>
</Steps>


# CI/CD Testing
Source: https://docs.datafold.com/faq/ci-cd-testing



<AccordionGroup>
  <Accordion title="What if my staging/dev environment contains only a subset of data from production?">
    You can use [SQL filters](/deployment-testing/configuration/model-specific-ci/sql-filters) to ensure that Datafold compares equivalent subsets of data between your staging/dev and production environments, allowing for accurate data quality checks despite the difference in data volume.
  </Accordion>

  <Accordion title="Can I use Datafold in development?">
    Yes, you can use Datafold in development. It helps catch data quality issues early by comparing data changes in your development environment before they reach production. This proactive approach ensures that errors and inconsistencies are identified and resolved during the development process, enhancing overall data reliability and preventing potential issues in production. Data teams can leverage the Datafold SDK to run data diffs from the command line while developing and testing data models.
  </Accordion>

  <Accordion title="How does Datafold handle data drift?">
    Data drift in CI occurs when the two data transformation builds that are compared by Datafold in CI have differing data outputs due to the upstream data changing over time.

    We have a few recommended strategies for dealing with data drift [in our docs here](/deployment-testing/best-practices/handling-data-drift).
  </Accordion>

  <Accordion title="Can I run Data Diffs before opening a PR?">
    Some teams want to show Data Diff results in their tickets *before* creating a pull request. This speeds up code reviews as developers can QA code changes before requesting a PR review.

    If you use dbt, we explain [how you can automate this workflow here](/faq/datafold-with-dbt#can-i-run-data-diffs-before-opening-a-pr).
  </Accordion>
</AccordionGroup>


# Data Diffing
Source: https://docs.datafold.com/faq/data-diffing



<AccordionGroup>
  <Accordion title="What’s a data diff?">
    A [data diff](/data-diff/what-is-data-diff) is a value-level comparison between two tables—used to identify critical changes to your data and guarantee data quality.

    Similar to how git diff highlights changes in code by comparing different versions of files to show what lines have been added, modified, or deleted, a data diff compares rows and columns in two tables to pinpoint specific data changes.
  </Accordion>

  <Accordion title="What types of data can Datafold compare?">
    Datafold can compare data in tables, views, and SQL queries in databases and data lakes.

    Datafold facilitates data diffing by supporting a wide range of basic data types across popular database systems like Snowflake, Databricks, BigQuery, Redshift, and PostgreSQL. Datafold can also diff data across legacy warehouses like Oracle, SQL Server, Teradata, IBM Netezza, MySQL, and more.
  </Accordion>

  <Accordion title="Can you data diff unstructured data?">
    No, Datafold cannot perform data diffs on unstructured data such as files. However, it supports diffing structured and semi-structured data in tabular formats, including `JSON` columns.
  </Accordion>

  <Accordion title="How should I compare numeric columns, especially those with floating-point values?">
    When comparing numerical columns or columns of the `FLOAT` type, it is beneficial to [set tolerance levels for differences](/data-diff/in-database-diffing/creating-a-new-data-diff#tolerance-for-floats) to avoid flagging inconsequential discrepancies. This practice ensures that only meaningful differences are highlighted, maintaining the focus on significant changes.
  </Accordion>

  <Accordion title="Can you explain how Datafold handles expected changes?">
    When a change is detected, Datafold highlights the differences in the App or through PR comments, allowing data engineers and other users to review, validate, and approve these changes during the CI process.
  </Accordion>

  <Accordion title="How does Datafold’s in-database diffing work?">
    When diffing data within the same physical database or data lake namespace, data diff compares data by executing various SQL queries in the target database. It uses several JOIN-type queries and various aggregate queries to provide detailed insights into differences at the row, value, and column levels, and to calculate differences in metrics and distributions.
  </Accordion>

  <Accordion title="How does Datafold’s cross-database diffing work?">
    Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
  </Accordion>

  <Accordion title="Can I materialize diff results back to my database?">
    Yes, while the Datafold App UI provides advanced exploration of diff results, you can also materialize these results back to your database. This allows you to further investigate with SQL queries or maintain audit logs, providing flexibility in how you handle and review diff outcomes. Teams may additionally choose to download diff results as a CSV directly from the Datafold App to share with their team members.
  </Accordion>
</AccordionGroup>


# Data Migration Automation
Source: https://docs.datafold.com/faq/data-migration-automation



<AccordionGroup>
  <Accordion title="How does DMA work?">
    Datafold performs complete SQL codebase translation and validation. It uses an AI agent architecture that performs the translation leveraging an LLM model with a feedback loop optimized for achieving full parity between migration source and target. DMA takes into account metadata, including schema, data types, and relationships in the source system.
  </Accordion>

  <Accordion title="How is this approach different from other tools on the market?">
    DMA offers several key advantages over deterministic transpilers that rely on static code parsing with predefined grammars:

    * **Full parity between source and target:** DMA not only returns code that compiles, but code that produces the same result in your new database with explicit validation.
    * **Flexible dialect handling:** Ability to adapt to any arbitrary dialect for input/output without the need to provide full grammar, which is especially valuable for numerous legacy systems and their versions.
    * **Self-correction capabilities:** DMA can self-correct mistakes, taking into account compilation errors and data discrepancies.
    * **Modernizing code structure:** DMA can convert convoluted stored procedures into dbt projects following best practices.
  </Accordion>

  <Accordion title="How do I know if the output is correct?">
    Upon delivery, customers get a comprehensive report with links to data diffs validating parity and discrepancies (if any) on dataset-, column-, and row-level between source and target.
  </Accordion>

  <Accordion title="How does my team use DMA?">
    Once source and target systems are connected and Datafold ingests the code base, translations with DMA are automatically supervised by the Datafold team. In most cases, no input is required from the customer.
  </Accordion>

  <Accordion title="What do I need to start working with DMA?">
    Connect source and target data sources to Datafold. Provide Datafold access to the codebase (usually by installing the Datafold GitHub/GitLab/ADO app or via system catalog for stored procedures).
  </Accordion>

  <Accordion title="What are the security implications of using DMA?">
    Datafold is SOC 2 Type II, GDPR, and HIPAA-compliant and provides flexible deployment options, including in-VPC deployment in AWS, GCP, or Azure. The LLM infrastructure relies on local models and does not expose data to any sub-processor besides the cloud provider. In case of a VPC deployment, none of the data leaves the customer’s private network.
  </Accordion>

  <Accordion title="How long will it take to translate?">
    After the initial setup, the migration process can take several days to several weeks, depending on the source and target technologies, scale, and complexity.
  </Accordion>

  <Accordion title="What if I want to change data model/definitions?">
    DMA is an ideal fit for lift-and-shift migrations with parity between source and target as the goal. Some customization is possible and needs to be scoped on a case-by-case basis.
  </Accordion>

  <Accordion title="How does cross-database diffing work?">
    Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
  </Accordion>

  <Accordion title="What kind of information does Datafold output?">
    Datafold’s cross-database diffing will produce the following results:

    * **High-Level Summary:**
      * Total number of different rows
      * Total number of rows (primary keys) that are present in one database but not the other
      * Aggregate schema differences
    * **Schema Differences:** Per-column mapping of data types, column order, etc.
    * **Primary Key Differences:** Sample of specific rows that are present in one database but not the other
    * **Value-Level Differences:** Sample of differing column values for each column with identified discrepancies; full dataset of differences can be downloaded or materialized to the warehouse
  </Accordion>

  <Accordion title="How does a user run a data diff?">
    * Via Datafold’s interactive UI
    * Via the Datafold API
    * On schedule (as a monitor) with optional alerting via Slack, email, PagerDuty, etc.
  </Accordion>

  <Accordion title="Can I run multiple data diffs at the same time?">
    Yes, users can run as many diffs as they would like with concurrency limited by the underlying database.
  </Accordion>

  <Accordion title="What if my data is changing and replicated live, how can I ensure proper comparison?">
    In such cases, we recommend using watermarking—diffing data within a specified time window of row creation/update (e.g., `updated_at timestamp`).
  </Accordion>

  <Accordion title="What if the data types do not match between source and target?">
    Datafold performs best-effort type matching for cases where deterministic type casting is possible, e.g., comparing `VARCHAR` type with `STRING` type. When automatic type casting without information loss is not possible, the user can define type casting manually using diffing in Query mode.
  </Accordion>

  <Accordion title="Can data diff help if the dataset in the source and target databases has a different shape/schema/column naming?">
    Users can reshape input datasets by writing a SQL query and diffing in Query mode to bring the dataset to a comparable shape. Datafold also supports column remapping for datasets with different column names between tables.
  </Accordion>
</AccordionGroup>


# Data Monitoring and Observability
Source: https://docs.datafold.com/faq/data-monitoring-observability



<Accordion title="How does Datafold compare to data observability tools?">
  Most data observability tools focus on monitoring metrics (e.g., null counts, row counts) in the data warehouse. But catching data quality issues in the data warehouse is usually too late: the bad data has already affected downstream processes and negatively impacted the business.

  Our platform focuses on prevention rather than detection of data quality issues. By [integrating deeply into your CI process](/deployment-testing/how-it-works), Datafold's [Data Diff](/data-diff/what-is-data-diff) helps data teams fix potential regressions during development and deployment, before bad code and data get into the production environment.

  Our [Data Monitors](/data-monitoring/monitor-types) make it easy to monitor production data to catch issues early before they are propagated through the warehouse to business stakeholders.

  This proactive data quality strategy not only enhances the reliability and accuracy of your data pipelines but also reduces the risk of disruptions and the need for reactive troubleshooting.
</Accordion>


# Data Reconciliation
Source: https://docs.datafold.com/faq/data-reconciliation



<AccordionGroup>
  <Accordion title="How does cross-database diffing work?">
    Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
  </Accordion>

  <Accordion title="What kind of information does Datafold output?">
    Datafold’s cross-database diffing will produce the following results:

    1. High-Level Summary:
       * Total number of different rows
       * Total number of rows (primary keys) that are present in one database, but not the other
       * Aggregate schema differences
    2. Schema Differences: Per-column mapping of data types, column order, etc.
    3. Primary Key Differences: Sample of specific rows that are present in one database, but not the other
    4. Value-Level Differences: Sample of differing values for each column with identified discrepancies; full dataset of differences can be downloaded or materialized to the warehouse

    You can check out [what the results look like in the App](/data-diff/cross-database-diffing/results).
  </Accordion>

  <Accordion title="How does a user run a data diff?">
    1. Via Datafold’s interactive UI
    2. Via the Datafold API
    3. On a schedule (as a monitor) with optional alerting via Slack, email, PagerDuty, etc.
  </Accordion>

  <Accordion title="Can I run multiple data diffs at the same time?">
    Yes, users can run as many diffs as they would like with concurrency limited by the underlying database.
  </Accordion>

  <Accordion title="How can I ensure accurate data comparison if my data is changing and being replicated in real-time?">
    In such cases, we recommend using watermarking – diffing data within a specified time window of row creation / update (e.g. `updated_at timestamp`).
  </Accordion>

  <Accordion title="What if the data types do not match between source and target?">
    Datafold performs best-effort type matching for cases when deterministic type casting is possible, e.g. comparing `VARCHAR` type with `STRING` type. When automatic type casting without information loss is not possible, the user can define type casting manually using diffing in Query mode.
  </Accordion>

  <Accordion title="Can data diff help if the source and target datasets have a different shape/schema/column naming?">
    Yes, users can reshape the input dataset by writing a SQL query and diffing in Query mode to bring the dataset to a shape that can be compared with another. Datafold also supports column remapping for datasets with different column names between tables.
  </Accordion>

  <Accordion title="How can data diffs be provisioned at scale, e.g. we need to create hundreds / thousands of data diffs?">
    To make the provisioning at scale easier, you can create data diffs via the [Datafold API](https://docs.datafold.com/reference/cloud/rest-api).
  </Accordion>
</AccordionGroup>


# Data Storage and Security
Source: https://docs.datafold.com/faq/data-storage-and-security



<Accordion title="What data does Datafold ingest and store?">
  Datafold ingests and stores various types of data to ensure accurate data quality checks and insights:

  * **Metadata**: This includes table names, column names, and queries executed in the data warehouse.
  * **Data for Data Diffs**:
    * For **in-database diffs**, all data visible in the app, including data samples, is fetched and stored.
    * For **cross-database diffs**, all data visible in the app, including data samples, is fetched and stored. Larger amounts of data are fetched for comparison purposes, but only data samples are stored.
  * **Table Profiling in Data Explorer**: Datafold stores samples and distributions of data to provide detailed profiling.
</Accordion>


# Integrating Datafold with dbt
Source: https://docs.datafold.com/faq/datafold-with-dbt



<AccordionGroup>
  <Accordion title="Why do I need Datafold if I already have dbt tests?">
    You need Datafold in addition to dbt tests because while dbt tests are effective for validating specific assertions about your data, they can't catch all issues, particularly unknown unknowns. Datafold identifies value-level differences between staging and production datasets, which dbt tests might miss.

    Unlike dbt tests, which require manual configuration and maintenance, Datafold automates this process, ensuring continuous and comprehensive data quality validation without additional overhead. This is all embedded within Datafold’s unified platform that offers end-to-end data quality testing with our [Column-level Lineage](/data-explorer/lineage) and [Data Monitors](/data-monitoring/monitor-types).

    Hence, we recommend combining dbt tests with Datafold to achieve complete test coverage that addresses both known and unknown data quality issues, providing a robust safeguard against potential data integrity problems in your CI pipeline.
  </Accordion>

  <Accordion title="What do I need to implement Datafold for dbt?">
    For dbt Core users, create an integration in Datafold, specify the necessary settings, obtain a Datafold API Key and CI config ID, and configure your CI scripts with the Datafold SDK to upload manifest.json files. Our detailed setup guide [can be found here](/integrations/orchestrators/dbt-core).

    For dbt Cloud users, set up dbt Cloud CI to run Pull Request jobs and create an Artifacts Job that generates production manifest.json on merges to main/master. Obtain your dbt Cloud access URL and a Service Token, then create a dbt Cloud integration in Datafold using these credentials. Configure the integration with your repository, data connection, primary key tag, and relevant jobs. Our detailed setup guide [can be found here](/integrations/orchestrators/dbt-cloud).
  </Accordion>

  <Accordion title="We currently have a dbt Cloud Slim CI job. Does Datafold work with the custom PR schema that dbt Cloud creates?">
    Yes, Datafold is fully compatible with the custom PR schema created by dbt Cloud for Slim CI jobs.
  </Accordion>

  <Accordion title="How can I optimize diff performance in dbt?">
    We outline effective strategies for efficient and scalable data diffing in our[performance and scalability guide](faq/performance-and-scalability#how-can-i-optimize-diff-performance-at-scale).

    For dbt-specific diff performance, you can exclude certain columns or tables from data diffs in your CI/CD pipeline by adjusting the **Advanced settings** in your Datafold CI/CD configuration. This helps reduce processing load by focusing diffs on only the most relevant columns.

        <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1a22a2d006506c4181030d7a6417daf4" alt="" data-og-width="2090" width="2090" data-og-height="1772" height="1772" data-path="images/faq/advanced_ci_columns_to_ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=08c8c210035ff613a62d8453b70a3964 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d0766e0559b5093c0204882b7cd2896d 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6b1fe94bfdfa7eb27d6c26aac1f9bda1 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9b22e9e57064d8fba203c166040f83da 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=96cfef3957167e0b7d52269211c6c2a7 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4c4c4b4bcc81d2854b11bdaa31c4bb68 2500w" />
  </Accordion>

  <Accordion title="Can I run Data Diffs before opening a PR?">
    Some teams want to show Data Diff results in their tickets *before* creating a pull request. This speeds up code reviews as developers can QA code changes before requesting a PR review.

    You can trigger a Data Diff by first creating a **draft PR** and then running the following command via the CLI:

    ```bash  theme={null}
    dbt run && datafold diff dbt
    ```

    This command runs `dbt` locally and then triggers a Data Diff, allowing you to preview data changes without pushing to Git.

    To automate this process of kicking off a Data Diff before pushing code to git, we recommend creating a GitHub Actions job for draft PRs. For example:

    ```
    name: Data Diff on draft dbt PR

    on:
      pull_request:
        types: [opened, reopened, synchronize]
        branches:
          - '!main'

    jobs:
      run:
        if: github.event.pull_request.draft == true  # Run only on draft PRs
        runs-on: ubuntu-latest

        steps:
          - name: Checkout Code
            uses: actions/checkout@v2

          - name: Set Up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'

          - name: Install requirements
            run: pip install -r requirements.txt  

          - name: Install dbt dependencies
            run: dbt deps

          # Update with your S3 bucket details
          - name: Grab production manifest from S3
            run: |
              aws s3 cp s3://advanced-ci-manifest-demo/manifest.json ./manifest.json
            env:
              AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
              AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
              AWS_REGION: us-east-1

          - name: Run dbt and Data Diff
            env:
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
            run: |
              dbt run
              datafold diff dbt
              
          # Optional: Submit artifacts to Datafold for more analysis or logging
          - name: Submit artifacts to Datafold
            run: |
              set -ex
              datafold dbt upload --ci-config-id 350 --run-type pull_request --commit-sha ${GIT_SHA}
            env:
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
              GIT_SHA: "${{ github.event.pull_request.head.sha }}"

    ```
  </Accordion>
</AccordionGroup>


# Overview
Source: https://docs.datafold.com/faq/overview

Get answers to the most common questions regarding our product.

Have a question that isn’t answered here? Feel free to reach out to us at [support@datafold.com](mailto:support@datafold.com), and we’ll be happy to assist you!

<CardGroup cols={2}>
  <Card title="Data Diffing" href="/faq/data-diffing" horizontal />

  <Card title="CI/CD Testing" href="/faq/ci-cd-testing" horizontal />

  <Card title="Data Migration Automation" href="/faq/data-migration-automation" horizontal />

  <Card title="Data Reconciliation" href="/faq/data-reconciliation" horizontal />

  <Card title="Data Monitoring & Observability" href="/faq/data-monitoring-observability" horizontal />

  <Card title="Datafold with dbt" href="/faq/datafold-with-dbt" horizontal />

  <Card title="Data Storage & Security" href="/faq/data-storage-and-security" horizontal />

  <Card title="Performance & Scalability" href="/faq/performance-and-scalability" horizontal />

  <Card title="Resource Management" href="/faq/resource-management" horizontal />
</CardGroup>


# Performance and Scalability
Source: https://docs.datafold.com/faq/performance-and-scalability



<AccordionGroup>
  <Accordion title="How scalable is Datafold?">
    Datafold is highly scalable, supporting data teams working with billion-row datasets and thousands of data transformation/dbt models. It offers powerful performance optimization features such as [SQL filtering](/deployment-testing/configuration/model-specific-ci/sql-filters), [sampling](/data-diff/cross-database-diffing/best-practices), and [Slim Diff](/deployment-testing/best-practices/slim-diff), which allow you to focus on testing the datasets that are most critical to your business, ensuring efficient and targeted data quality validation.
  </Accordion>

  <Accordion title="How can I optimize diff performance at scale?">
    Datafold pushes down compute to your database, and the performance of data diffs largely depends on the underlying SQL engine. Here are some in-app strategies to optimize performance:

    1. [Enable sampling](/data-diff/cross-database-diffing/best-practices): Sampling reduces the amount of data processed by comparing a randomly chosen subset. This approach balances diff detail with processing time and cost, suitable for most use cases.

    2. [Use SQL Filters](/deployment-testing/configuration/model-specific-ci/sql-filters): If you only need to compare a specific subset of data (e.g., for a particular city or a recent time period), adding a SQL filter can streamline the diff process.

    3. **Exclude columns/tables**: When certain columns or tables are unnecessary for critical comparisons—such as temporary tables with dynamic values, metadata fields, or timestamp columns that always differ—you can exclude these to increase diff efficiency and speed.

    You can exclude columns when you create a new Data Diff or when you clone an existing one:

    <Frame>
            <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=115abf94cf44b4455815c3ba6590fffe" alt="" data-og-width="1384" width="1384" data-og-height="884" height="884" data-path="images/faq/new_diff_exclude_columns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=60532a82cd20ef169777bed2b18daa2f 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=7b9258cb4d2db96623ed5759de7381d4 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=958c95dc67f34afc38445e991a4cfe76 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1675889d188645eee642fee41a3179d4 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=64fa8499cce7deddfd8f5730d04c910a 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=394aff3dbd3bef65acc013a6baa2e521 2500w" />
    </Frame>

    To exclude them in your CI/CD pipeline, [follow this guide](/integrations/orchestrators/dbt-core#advanced-settings-configuration) to specify them in the Advanced settings of your CI/CD configuration in Datafold.

    4. **Optimize SQL queries**: Refactor your SQL queries to improve the efficiency of database operations, reducing execution time and resource usage.
    5. **Leverage database performance features**: Ensure your database is configured to match typical diff workload patterns. Utilize features like query optimization, caching, and parallel processing to boost performance.
    6. **Increase data warehouse resources**: If using a platform like Snowflake, consider increasing the size of your warehouse to allocate more resources to Datafold operations.
  </Accordion>
</AccordionGroup>


# Resource Management
Source: https://docs.datafold.com/faq/resource-management



<Accordion title="What is Datafold’s resource consumption footprint? How will Datafold affect my data warehouse costs?">
  Recognizing the importance of efficient data reconciliation, we provide a number of strategies to make the diffing process as efficient as possible:

  **Efficient Algorithm**

  Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.

  **Flexible Controls**

  Users can easily control the volume of data used in diffing by using:

  * [Filters](/deployment-testing/configuration/model-specific-ci/sql-filters): Focus on the most relevant part of the dataset
  * [Sampling](/data-diff/cross-database-diffing/best-practices): Set sampling as a percentage of rows or desired confidence level
  * [Slim Diff](/deployment-testing/best-practices/slim-diff): Selectively diff only the models that have dbt code changes in your pull request.

  **Workload Management**

  Users can apply controls to enforce low diffing footprint:

  * On the Datafold side: Set desired concurrency
  * On the database side: Most databases support workload management settings to ensure that Datafold does not consume more than X% CPU or Y% RAM

  Also, consider that using a data quality tool like Datafold to catch issues before production will reduce cost over time as it lowers the need for expensive reprocessing and troubleshooting. Datafold's features like filtering, sampling, and Slim Diff ensure that only relevant datasets are tested, minimizing the computational load on your data warehouse. This targeted approach can lead to more efficient resource usage and potentially lower data warehouse operation costs.
</Accordion>


# dbt Exposures
Source: https://docs.datafold.com/integrations/bi-data-apps/dbt

Incorporate dbt Exposures into your Datafold lineage.

In dbt, Exposures allow you to define downstream uses of your data (e.g., in dashboards). You can include dbt Exposures in lineage within Data Explorer using our dbt Exposures integration.

## Set up the integration

<Note>
  If you haven't aleady created a dbt CI integration, please start [there](/integrations/orchestrators/).
</Note>

1. Visit Settings > BI & Data Apps > Add new integration
2. Select "dbt Exposures"
3. Enter a name for the integration (this can be anything)
4. Select your existing dbt CI integration from the dropdown
5. Save the integration

<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=46667baf3b545a6f0665c15874359703" alt="Add dbt Exposures integration" data-og-width="2176" width="2176" data-og-height="766" height="766" data-path="images/dbt-exposures-add-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ae8ea705a4713091682b412adb5b5f13 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=58b3982ad41999bed202c0719b217e51 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fb0fbf4dedd43ae2400d43b0b22e3e15 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5cd052a02b04d0f2caf8fd0abc2a1e4a 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6723bcf6bad8c9b6ce2e137d91341c80 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=52cf2abad78cf3b0b7cf87b0d6bf2ea6 2500w" />
<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ebeb4396e6ef3fa3eda620f1783950fa" alt="Configure dbt Exposures integration" data-og-width="1378" width="1378" data-og-height="318" height="318" data-path="images/dbt-exposures-integration-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c85f719dfda4413e898551a6758e6bd4 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=daae5797a2c526c102e4c4518af37317 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=97f74960a66aae3376cefbdba316435b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=27d566789c4c9c7be1bd6bad4dec745e 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=011bcf46f08639a3065fd87da95a752a 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=65f9196b17a53707b96c6e10dc5615e9 2500w" />

## View dbt Exposures in Data Explorer

<Note>
  Your dbt Exposures may not appear in lineage immediately after setting up the integration. To force an update, return to the integration settings and select "Sync now".
</Note>

When you visit Data Explorer, you'll now see the option to filter for dbt Exposures:

<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2269a6543d2ef3112cd727d79e717bb2" alt="Filter for dbt Exposures" data-og-width="3420" width="3420" data-og-height="1436" height="1436" data-path="images/dbt-exposures-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f2e5dae9572c375abdd47d185998c94b 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8ec7cf3f0bc7b5a5b6eec594e1478ed4 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1e5b7e8106c84f5475a1e6374b8f703a 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=58803f774dfde2d2be4089f71f4742e6 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=19b1754db1f11145fa86a2d38fa4abcd 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=824b540aefcc17bcacd7c2b896734f8d 2500w" />

Your dbt Exposures will also appear in lineage:

<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f0f28de9f5aa1e521d94184efe3d9342" alt="View dbt Exposures in lineage" data-og-width="3420" width="3420" data-og-height="1962" height="1962" data-path="images/dbt-exposures-lineage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=901ebd14c0f0c372f49d08043c0c1af9 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=16b748b2821b30abea415022e45c3bec 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=44ba5a4d17759b61c1b63851e5b1729e 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4d8bde289da0695e6d6540d4ea6418df 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1773f4a8d1730e2f90e0415ed8b7b7f8 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c98d0fc7fdea2fed0b983154e8a482e3 2500w" />


# Hightouch
Source: https://docs.datafold.com/integrations/bi-data-apps/hightouch

Navigate to Settings > Integrations > Data Apps and add a Hightouch Integration.

## Create a Hightouch Integration

<Frame caption="Create Integration">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bd09718379ccede369a6e1b6738524c4" data-og-width="2102" width="2102" data-og-height="646" height="646" data-path="images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83919832e4b23599314017b45690d2c1 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1414d4d3bb1c055da9b1c52341916473 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b8f0350c0caf989153ac7c824fc516df 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd39b2c1819b171dcbab2fd23bee84d3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=710aebc070a215d8943c9cf7321b8406 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3558cfab5dc27eff9323d9e64d4902b7 2500w" />
</Frame>

<Frame caption="Create Integration">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0c5ab498f228ff4c438a41c191f1b1ec" data-og-width="1890" width="1890" data-og-height="1382" height="1382" data-path="images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=656bab2e4aec843fafc46429901adc7a 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b18f7c09fb9a54aee4b7a43565dc91b8 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=642cbcacea223543b26f9d0917d50607 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=599441c611a6b2f3ef84757eb8ed7560 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=90daee1aa50b35123b04d14ca899ddd4 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_blank_integration_form-379e98ee744aa52224d2dd6ccd110a44.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=88054a2835acec251412be410f3bf96d 2500w" />
</Frame>

Complete the configuration by specifying the following fields:

| Field Name              | Description                                                                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integration name        | An identifier used in Datafold to identify this Data App configuration.                                                                                                                                                                                                                                                |
| Workspace URL           | Then, grab your workspace URL, by navigating to **Settings** → **Workspace** tab → **Workspace slug** or by finding the workspace name in the search bar ([https://app.hightouch.io/](https://app.hightouch.io/) \<workspace\_slug/>).                                                                                 |
| API Key                 | Log into your [Hightouch account](https://app.hightouch.com/login) and navigate to **Settings** → **API keys** tab → **Add API key** to generate a new, unique API key.  <Icon icon="triangle-exclamation" /> Your API key will appear only once, so please copy and save it to your password manager for further use. |
| Data connection mapping | When the correct credentials are entered we will begin to populate data connections in Hightouch (on the left side) that will need to be mapped to data connections configured in Datafold (on the right side). See image below.                                                                                       |

<Frame caption="Create Integration">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b9a551a7e7aabd27daee6405532d7fa4" data-og-width="1739" width="1739" data-og-height="1456" height="1456" data-path="images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=56663b1343950a02570cbc5ed80b29b8 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=439ce7ac9e8386fde85b64c15ef04a03 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=769d278bf05c33f41032a97ae3d6cc8e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5683b5897a085405d14a9ca439ed6f72 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bfdbc027916f0366260f4c2f5adae5cc 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_data_source_match-3ed927400af746ec7b2b637b09cdd055.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6f44f5335e5f150d202353e1145d82b0 2500w" />
</Frame>

When completed, click **Submit**.

It may take some time to sync all the Hightouch entities to Datafold and for Data Explorer to populate. When completed, your Hightouch models and sync will appear in Data Explorer as search results.

<Frame caption="Create Integration">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=325349ccd3e600e527208667d58908b4" data-og-width="1716" width="1716" data-og-height="810" height="810" data-path="images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4109de427de9da033df0e8f60473cd71 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2a3986ab719cc7bd675706ad362732f3 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0a79dbdec28e5a302b69af2d584a7730 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8788cfdbe768de579d85bd18acf39089 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be8c670f5a39c7725eb1a0fc2a487c31 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/hightouch_sync_results-6865862cb8cd146928f7783fd2a67f56.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4d7679d3bfdcc41470350e1e0c99f80c 2500w" />
</Frame>

<Tip>
  **TIP**

  [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) explains how to find out when your data app integration is ready.
</Tip>


# Looker
Source: https://docs.datafold.com/integrations/bi-data-apps/looker



## Create a code repositories integration

[Create a code repositories integration](/integrations/code-repositories) that connects Datafold to your Looker repository.

## Create a Looker integration

Navigate to Settings > Integrations > Data Apps and add a Looker integration.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bd09718379ccede369a6e1b6738524c4" alt="Add New Integration" data-og-width="2102" width="2102" data-og-height="646" height="646" data-path="images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83919832e4b23599314017b45690d2c1 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1414d4d3bb1c055da9b1c52341916473 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b8f0350c0caf989153ac7c824fc516df 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd39b2c1819b171dcbab2fd23bee84d3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=710aebc070a215d8943c9cf7321b8406 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3558cfab5dc27eff9323d9e64d4902b7 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9d4bc08ae0d3c7a49dc97e61d314518f" alt="Looker Integration Form" data-og-width="2368" width="2368" data-og-height="1476" height="1476" data-path="images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a773a6f47f081d0274890d3654cb3b60 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=dbdb207bd25b3a6ea8949a8cafdd49ed 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3558d7d083e00569cf4d1339bda59912 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b61a6aedfe005f461ed44a4396b4e399 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=baf3d3f5a1fad6c055f11a759b0240b1 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_blank_integration_form-2891846b6665064a633f376d99acbde0.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=db094298f134e63291ad6a7c481e7ef5 2500w" />
</Frame>

Complete the configuration by specifying the following fields:

| Field Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Integration name        | An identifier used in Datafold to identify this Data App configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Project Repository      | Select the same repository as used in your Looker project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| API Host URL            | The Looker [API Host URL](https://cloud.google.com/looker/docs/admin-panel-platform-api#api%5Fhost%5Furl). It has the following format: https\://\<instance\_name>.cloud.looker.com:\<port>. The port defaults are 19999 (legacy) and 443 (new), see the [Looker Docs](https://cloud.google.com/looker/docs/api-getting-started#looker%5Fapi%5Fpath%5Fand%5Fport) for hints. Examples: Legacy ([https://datafold.cloud.looker.com:19999](https://datafold.cloud.looker.com:19999)), New ([https://datafold.cloud.looker.com:443](https://datafold.cloud.looker.com:443)) |
| Client ID               | Follow [these steps](https://cloud.google.com/looker/docs/api-auth#authentication%5Fwith%5Fan%5Fsdk) to generate Client ID and Client Secret. These are always user specific. We recommend using a group email for continuity. See [Looker User Minimum Access Policy](/integrations/bi-data-apps/looker#looker-user-minimum-access-policy) for the required permissions.                                                                                                                                                                                                |
| Client Secret           | See Client ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Data connection mapping | When the correct credentials are entered we will begin to populate data connections in Looker (on the left side) that will need to be mapped to data connections configured in Datafold (on the right side). See image below.                                                                                                                                                                                                                                                                                                                                            |

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=981c663e0a1ec781941ea554bd1d7d58" alt="Looker Configuration" data-og-width="1900" width="1900" data-og-height="1956" height="1956" data-path="images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=52f156d66bdee410a63e58ac889d310d 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4bc90dafdd128278c14eea268e64a065 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1b3d4ca6ede404f1a02fcce3892a637e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d6bfcce9c9ff3ae9815339b991c858a8 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f319647cf8af529b02c66a36f7d523a2 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_configuration-0410bbaf211f889bf36bb8f93d378500.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5f597a0ac5030cb8710fcb63368ac0ea 2500w" />
</Frame>

When completed, click **Submit**.

It may take some time to sync all the Looker entities to Datafold and for Data Explorer to populate. When completed, your Looker assets will appear in Data Explorer as search results.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b4ba365cff063876985e52e3fa0b7462" alt="Looker Sync Results" data-og-width="1722" width="1722" data-og-height="976" height="976" data-path="images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=40d4a67c89d46ddbdef3daf8b84723f9 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2976d7c058a3cd398dc0d8714a40d37d 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c5f61aa4fbb3b8c67d60424d16e45181 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9a9a0ee2f6c1d5221d7553c86f791c41 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=579b68573daf518b8bfb8e6e29d6c48a 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/looker_sync_results-e610d030d6891b22cffbceeae9d9a8d1.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=835f1340c118927efac7804f5b6fd455 2500w" />
</Frame>

<Tip>
  **TIP**

  [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) explains how to find out when your data app integration is ready.
</Tip>

## Looker user: minimum access policy

The user linked to the API credentials needs the predefined Developer role, or you can create a custom role with these permissions:

* `access_data`
* `download_without_limit`
* `explore`
* `login_special_email`
* `manage_spaces`
* `see_drill_overlay`
* `see_lookml`
* `see_lookml_dashboards`
* `see_looks`
* `see_pdts`
* `see_sql`
* `see_user_dashboards`
* `send_to_integration`

## Database/schema connection context

### Database specification

Using the Fully Qualified Names in your Looker view files is not always possible. If a view references a table as`my_schema.my_table`, Datafold might have difficulty finding which database this table actually is in. There are multiple ways to guide Datafold to make a correct choice, as summarized in the table below.

<Note>
  **INFO**

  Priority #1 takes precedence over #2, and so forth.
</Note>

| # | Source, if defined                                                                                                                                                            | Example                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| 1 | datafold\_force\_database **User Attribute** in Looker                                                                                                                        | looker\_db                  |
| 2 | **Fully Qualified Names** in your Looker view files                                                                                                                           | my\_db.my\_schema.my\_table |
| 3 | datafold\_default\_database **User Attribute** in Looker                                                                                                                      | another\_looker\_db         |
| 4 | **Database** specified in Looker, at Database connection settings\_(We can only read these if Datafold connects to Looker via an admin user, which is probably suboptimal.)\_ | my\_db                      |
| 5 | **Database** specified in Datafold, at [Database Connection settings](/integrations/databases/)                                                                               | my\_db                      |

### Supported custom Looker user attributes

| User Attribute              | Impact                                                                                                   |
| --------------------------- | -------------------------------------------------------------------------------------------------------- |
| datafold\_force\_database   | Database to use in all cases, even if a fully qualified path in LookML refers to another database.       |
| datafold\_default\_database | Database to use if Looker View does not explictly specify a database.                                    |
| datafold\_default\_schema   | Schema to use if Looker view does not explicitly specify a schema (which equals a dataset for BigQuery). |
| datafold\_default\_host     | *(BigQuery only)* Default project name.                                                                  |

<Note>
  **INFO**

  Make sure attributes are:

  * Explicitly defined for the user in question (not just falling back to a default);
  * Not marked as hidden.
</Note>

## Integration limitations

Datafold lets you connect to Looker and extend our capabilities to your Looker Views, Explores, Looks, and Dashboards. But this is a new feature, so there are some things we don’t support yet:

* **PDT/Derived Tables**:Datafold only works with the tables that come from your data connections, but not with the [tables](https://cloud.google.com/looker/docs/derived-tables#important%5Fconsiderations%5Ffor%5Fimplementing%5Fpersisted%5Ftables) that Looker makes from your SQL queries.
* **Merge Queries**: Datafold supports the Queries and Looks that make up your Dashboards, but [Merge Queries](https://cloud.google.com/looker/docs/merged-results) are not one of them. For some use cases you could achieve the same by joining the underlying views with an explore.
* **Usage metrics and popularity**: Datafold shows you your Looker objects - such as dashboards, looks, and fields - but not how much you use or like them.

We are improving our Looker integration and adding more features soon. We welcome your feedback and suggestions.


# Mode
Source: https://docs.datafold.com/integrations/bi-data-apps/mode



## Obtain credentials from Mode

<Note>
  **INFO**

  To complete this integration, your **Mode** account must be a part of a [Mode Business Workspace](https://mode.com/compare-plans) in order to generate an API Token.
</Note>

<Note>
  **INFO**

  You need to have **Admin** privileges in your Mode Workspace to be able to create an API Token.
</Note>

In **Mode**, navigate to **Workspace Settings** → **Privacy & Security** → **API**.

Click the <Icon icon="gear" /> icon, and choose **Create new token**.

<Frame caption="Tokens">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=218032a87bc1d3f56b623a1eec0a9a00" data-og-width="1691" width="1691" data-og-height="267" height="267" data-path="images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=58c1cb56a809187118184cd69200a35b 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e8b3268bc2db3bb2aa31045bce9631b2 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e817ac0717fd115a7d277df6cc108027 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a59203a5a10594174ea08cdd2b97af9e 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=633af3fa499865c6c8d363c01c987e7e 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=83502a7e22c1f9a5d96203f221833d84 2500w" />
</Frame>

Take note of:

* Token Name,
* Token Password,
* And the URL of the page that lists the tokens. It should look like this:

  [https://app.mode.com/organizations/\{workspace}/api\_keys](https://app.mode.com/organizations/\{workspace}/api_keys)

Take note of `{workspace}` part, we will need it when configuring Datafold.

## Configure Datafold

Navigate to **Settings** → **Integrations** → **BI & Data Apps**.

<Frame caption="Add New Integration">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bd09718379ccede369a6e1b6738524c4" data-og-width="2102" width="2102" data-og-height="646" height="646" data-path="images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83919832e4b23599314017b45690d2c1 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1414d4d3bb1c055da9b1c52341916473 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b8f0350c0caf989153ac7c824fc516df 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd39b2c1819b171dcbab2fd23bee84d3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=710aebc070a215d8943c9cf7321b8406 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3558cfab5dc27eff9323d9e64d4902b7 2500w" />
</Frame>

Choose **Mode** Integration to add.

<Frame caption="Choose Type">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=064bac3962b7e9812daae5972457b5c2" data-og-width="1073" width="1073" data-og-height="667" height="667" data-path="images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dbdaaf4597a7d6cba715ab6df01d9fca 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7fcd5d2a579d4623982ce61dad054fa1 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a302a76e06c0ad63b8658519c10bba04 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=11102d708ea0b66c27013da12bbcc548 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=700f899f072a1b4da648e15ed4e9c3d4 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e436b0081860afe17c309aa747e604f 2500w" />
</Frame>

This will bring up **Mode** integration parameters.

<Frame caption="Create Integration">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7ec9e93eb717c2a1c1becefe2c29a768" data-og-width="1059" width="1059" data-og-height="706" height="706" data-path="images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f88f8562400cd02c7b32b2421b4b33b 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=590aaaa136ed31c276f8b85e0828f470 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=662051cc22c31fcc70cfc762ff9610c7 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=337a027c1e0bc4bb091de29f18c1491c 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4c6105cbd370fffab35add37d5ccfa38 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ef510d1b9ffa273419ac34279184095b 2500w" />
</Frame>

Complete the configuration by specifying the following fields:

| Field Name       | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| Integration name | An identifier used in Datafold to identify this Data App configuration. |
| Token            | API token, as generated above.                                          |
| Password         | API token password, as generated above.                                 |
| Workspace        | Workspace name obtained from your workspace URL.                        |

<Note>
  **INFO**

  **Workspace Name** field is not marked as required on this screen. That's for backwards compatibility: the legacy type of Mode API token, known as **Personal Token**, does not require that parameter. However, such tokens can no longer be created, so we're no longer providing instructions for them.
</Note>

When completed, click **Save**.

Datafold will try to connect to Mode and, if any issues with the connection arise you will be alerted.

Datafold will start to sync your reports. It can take some time to fetch all the reports, depending on how many of them there are.

<Tip>
  **TIP**

  [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) explains how to find out when your data app integration is ready.
</Tip>

Now that Mode sync has completed — you can browse your Mode reports!

<Frame caption="Tokens">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5d53ed5013896c0e70df4d551e6478ab" data-og-width="1720" width="1720" data-og-height="1082" height="1082" data-path="images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5172bb0c7607aa6a4b8a96dcfa869ba9 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a52b6998b01c3799b768cc0c0a8f22c6 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f5e659695bdc8ffcd6b904b191554511 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c5ab2ddfed858c2ba9637742dfb8db79 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e29cda5dc55550bcee43f6c027012ea1 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d31fdcc6533c62543ba8918e76ef860d 2500w" />
</Frame>


# Power BI
Source: https://docs.datafold.com/integrations/bi-data-apps/power-bi

Include Power BI entities in Data Explorer and column-level lineage.

## Overview

Our Power BI integration can help you visualize column-level lineage dependencies between warehouse tables and Power BI entities using [Data Explorer](/data-explorer/how-it-works). Datafold supports the following Power BI entity types:

* Tables (with Columns)
* Reports (with Fields)
* Dashboards

## Set up the integration

<Steps>
  <Step title="Open Microsoft 365 admin center">
    Navigate to [**Microsoft 365 admin center** -> 👤 **Active users**](https://admin.microsoft.com/#/users) and choose the user that Datafold will authenticate under.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=38be66f2206263532520e4dc5ccd56a9" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/microsoft-admin-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c239123f4290a9343a5f9623578fc50a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a6e8e8e842a76bf59f82e9280918d639 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a8d05276bfa28413b56ca27c0fc7647 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9a5d3dfb92285c4ee6e660835b477699 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3a4fc4206ed16e884f9286dc23c3332c 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-admin-user.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f5ef23e3b54795de89b11cd448b91dd7 2500w" />
    </Frame>

    As highlighted in the screenshot above, this user should have the **Power Platform Administrator** role assigned to it.
  </Step>

  <Step title="If the role is missing, assign it">
    Click **Manage roles**, enable the **Power Platform Administrator** role, and save changes.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=10a2d7a38614008498702ea653240b45" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/microsoft-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=135fedd2022b556e6c743e17c6a874d1 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=707191572a27daa24a7c19ec9cf98775 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2c255e4049b67b1c23bcdef6409c0923 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e19cf19b04387d5e640612acc9a5cc5c 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ceb86ec7519bb644dde283c300fd82c7 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/microsoft-role.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=53811079ed2129f6eaed889c2a02c3d1 2500w" />
    </Frame>
  </Step>

  <Step title="Configure Power BI API">
    Navigate to [Power BI Admin Portal](https://app.powerbi.com/admin-portal/tenantSettings?experience=power-bi) and enable the following two settings:

    * Enhance admin APIs responses with detailed metadata
    * Enhance admin APIs responses with DAX and mashup expressions

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=947277d450e3507854f041e1dc1bf924" data-og-width="2060" width="2060" data-og-height="1179" height="1179" data-path="images/power-bi/admin-portal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=03c6e0431149d3b69eccc559613c6233 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c4a9720692c6da78b09d6e2ebcd5f252 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e34423eff722ab3da9a50584f45fe096 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0b26f8d48a81d35a829f7a95d4aa2f4e 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ae52e01cc773182c4222690ceb182ef 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/admin-portal.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=efc8d3ccca4113fb3d9171dbb74659f8 2500w" />
    </Frame>
  </Step>

  <Step title="Create Power BI integration in Datafold">
    In the Datafold app, navigate to **Settings** -> **BI & Data Apps**, and click **+ Add new integration**. Choose **Power BI** from the list.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b19abe212823cc0404644d16668aa588" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cb41d2c71af15c48ccf4b5fe13cca705 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7ef487fcf9f95185a0b17a47e27deb4a 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4fab71dda7d3bcbc45a72b75932c8586 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=876a313842469e44916c7b58369ba5a7 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e3f9c38e910776ce55d9bf271ed17bfe 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/create.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=527c729ffc3699385eb9c2044e5995e5 2500w" />
    </Frame>
  </Step>

  <Step title="Fill in the name for your new integration">
    ...and then **Save**.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dd2456c5ce5f75e9a21a3e7512f6a185" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a8331be34f53169e87489d717dd79a2f 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d8c5750189a08759f887454212b6a8bb 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4dc6e1ae5da5f606957852bd83e728cf 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a2cc9a84fba89dc44bdf8436dcf70edd 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=eba79ddc95ec4195db9141301e044524 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/new.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dbd0c8fe63944e77f4898e16efe65b6e 2500w" />
    </Frame>

    On clicking **Save**, the system will redirect you to Power BI.
  </Step>

  <Step title="Sign in to Power BI">
    ...if not already signed in.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9bb6c26dca422fdc86ee250477dc0d5c" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/sign-in.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9af33152cd51cb5e02045af45a22225a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=628c843aaae78cecda7331ba1aa0bf55 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0ba10f215486c0d56ed48eb05fac81cb 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=483e864be52f27b1d2df28dc0009d17b 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=20a52a33dd3ac6e3d67b7c6869dbf69d 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/sign-in.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c9ad62068f7a74d7907c40f903f3c2ae 2500w" />
    </Frame>
  </Step>

  <Step title="Grant permissions to Datafold">
    Allow the Datafold integration to use Power BI. Depending on the roles configured for your user in the Admin center, you may require a confirmation from a **Global Administrator**. Follow the steps in the wizard.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6a1ad1535bbf09d220fb5c2783e1d6aa" data-og-width="2060" width="2060" data-og-height="1179" height="1179" data-path="images/power-bi/consent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=42bab1e9bc0bfffa60c7f866b9fc7198 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=485af431c98886614bf02eef0f24ec6e 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5dda72b878229f133d2ff4a532622f96 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4d8d47bd55db39bcfae0cabea0d69119 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c940d24cf6c2cfa07f5280b31a35b152 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/consent.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7bd105a4ce6f55287b68f2cbc6ec1c9f 2500w" />
    </Frame>
  </Step>

  <Step title="Integration is ready">
    You will be redirected back to Datafold and see a message that Power BI is successfully connected.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=756557c082662c5834d34daa351ddc60" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=10a59c3d5bf3d152580f9da10d2cf3e5 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=286cfcce60a83035fb0ee2102fd7316e 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b683cd8370384a46df812b142e5ebe11 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=97695434f3d811edfd556acae9f63134 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6d403cde6068c0c5d9b7db41221cd68a 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/success.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cecdaca2a75ad077c6db925235195f1d 2500w" />
    </Frame>
  </Step>

  <Step title="Power BI integration needs some time to sync">
    You can check out **Jobs** -> **BI & Data Apps** for the status of the sync job.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a1288e76fb558f0c37875a812f1bc119" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/jobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=58cce51b5b9b130375500cd331dde57a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b89d04036a352969d0c940c6c088222f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=445452b8324ea69be064142a79795f53 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=95084316d73d3e0132819ae007393a26 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2a01cbad96e2516b90cda37be1bbe23b 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/jobs.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=afe0e676178e7fc871e8c04cc3802f1b 2500w" />
    </Frame>

    See [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) for more details.
  </Step>

  <Step title="Power BI entities are now searchable">
    When the sync is complete, you will see Power BI entities in **Data Explorer**.

    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4d97fd3f9b6da71c68b07af43723c3e5" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/data-explorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b3f4b58d3892ba3b88f52bd90a345d22 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=54197de01b02d766838a5f036949ecdb 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dccf4ff5939cf98aa43a9eb776a8c933 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ddd08530b3363569eaf07fe08771298e 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e5686245370a9e74d0ce07fb7b726166 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/data-explorer.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=15fbf0b692c6064f4d835103d4ae1a34 2500w" />
    </Frame>
  </Step>

  <Step title="Lineage is now available">
    <Frame>
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ab5d1896b8ccfa79e156cec7a604b6bb" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/power-bi/lineage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3e50a4292b7f81104131474360a6547e 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ee6a1bd7c66158437c917829881d0e2b 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cd61db20c1fbc090bb25d47e1d5f88e0 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1389caf0e01891afe363c01cb5547959 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ce0f73e05c0a5912bdcb655aa98b579f 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/power-bi/lineage.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=985117daf40d54d725ee6a1808086ca3 2500w" />
    </Frame>
  </Step>
</Steps>

## Need help?

If you have any questions about our Power BI integration, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# Tableau
Source: https://docs.datafold.com/integrations/bi-data-apps/tableau

Visualize downstream Tableau dependencies and understand how warehouse changes impact your BI layer.

## Overview

Our Tableau integration can help you visualise column-level lineage dependencies between warehouse tables and Tableau entities using [Data Explorer](/data-explorer/how-it-works).

<Info>
  **Note:** Lineage is only supported for Tableau assets in **Live** mode. Assets in **Extract** mode will not appear in Datafold lineage or dependency views.
</Info>

Lineage from upstream data warehouses into Tableau is supported for the following data warehouse types:

* Snowflake
* Redshift
* Databricks
* BigQuery

Potentially impacted Tableau entity names are also automatically identified in the Datafold CI printout.

The following Tableau entities types will appear in Data Explorer, data diff results, and the Datafold CI printout:

* Tableau **Data Connections** and related fields;
* **Workbooks** and related fields;
* **Dashboards**.

<Info>
  To declutter <Icon icon="sparkles" /> the Datafold lineage, Datafold filters out Tableau Data Connections and Data Connections fields that have no downstream dependencies.
</Info>

If you're interested in learning more about the Datafold integration, [please reach out to our team](https://www.datafold.com/booktime).

## Set up your Tableau instance

To connect Datafold to Tableau, you will require the following credentials from your Tableau site:

* Server URL,
* Site Name,
* Token Name,
* Token Value.

## If you are using Tableau Server

**Tableau Server** is an installation of Tableau that you are managing on your company's own infrastructure and domain. This is an alternative to using a Tableau Cloud subscription.

* Make sure that the [metadata-services](https://help.tableau.com/current/server/en-us/cli%5Fmaintenance%5Ftsm.htm#cat%5Fenable) are enabled by running the following command:

```
tsm maintenance metadata-services enable

```

* Ensure that your Tableau Server instance is accessible to Datafold. Please get in touch with our team to set this up.

## Obtaining server URL & Site Name

These can be found from URL of your Tableau home page. For instance, if your home page is:

```
https://eu-west-1a.online.tableau.com/#/site/mysupersite/home

```

Then:

* **Server URL** is `https://eu-west-1a.online.tableau.com` (the hostname with `https` in front)
* **Site Name** is `mysupersite` (the part directly after `#/site/` and until the next `/`)

## Obtaining Token Name & Token Value[](#obtaining-token-name--token-value "Direct link to Obtaining Token Name & Token Value")

Ensure that **Personal Access Tokens** are enabled on your Tableau site. For that, navigate to **Settings** and there, on the **General** tab, search for `Personal Access Tokens`. That feature needs to be enabled — not necessarily for everyone but for the user for whom we will be creating the token Datafold will use.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9147e3ad4b9630086b4b2a15094fe672" alt="Enable Personal Access Tokens" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=61703e834866aa0f644f6327f10030db 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b94c052f038e27e9ea686f69ed2b9e64 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=845a7fc83e6b2fac8fc0d09e976cafcf 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=839cadd96b3255caf253f3905b5535e6 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=11657c4aebc7313be52033c558956a57 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8c2afd4c26429bd332f19b7d442eaf2b 2500w" />
</Frame>

Now that Personal Access Tokens are enabled, click on your user’s avatar in the top right, choose **My Account Settings** in the pop-up menu, and then search for **Personal Access Tokens** on your settings page.

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=70570c0c794fc6664c8ed6febd7fb95d" alt="Personal Access Token" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=26a0b77aa78e1696eb0cb8151ceeff75 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=2e3db19e49035cf91f69e5e5241df4d5 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=d79c59740cfd51aa58be6c0e67f56d8d 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=6ee36de0e9148448313842543a1094f8 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=d78e0f48dfa13785633663915f498621 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=31c439ef3bb28b25c212755889944166 2500w" />
</Frame>

Input a desired name, say `datafold`, into the **Token Name** field, and click **Create Token**.

This will open a popup window. Click **Copy Secret** and save the copied value somewhere — you will use this when setting up Datafold. You can read more about personal access tokens on the official Tableau documentation [here](https://help.tableau.com/current/server/en-us/security%5Fpersonal%5Faccess%5Ftokens.htm).

## Create a Tableau Integration

Navigate to **<Icon icon="gear" /> Settings** → **Integrations** → **Data Apps**. Click **<Icon icon="plus" /> Add new integration**.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bd09718379ccede369a6e1b6738524c4" alt="Add New Integration" data-og-width="2102" width="2102" data-og-height="646" height="646" data-path="images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83919832e4b23599314017b45690d2c1 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1414d4d3bb1c055da9b1c52341916473 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b8f0350c0caf989153ac7c824fc516df 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd39b2c1819b171dcbab2fd23bee84d3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=710aebc070a215d8943c9cf7321b8406 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3558cfab5dc27eff9323d9e64d4902b7 2500w" />
</Frame>

A click on **Tableau** will lead you to the integration creation screen. Fill in the fields with data we obtained earlier. See the screenshot for hints.

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=99a0ac07d9cf4d1c93d6301663773993" alt="Tableau Integration Settings" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=7ac8a831e722ccb0aeb3493b9ed7d7c3 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=837dbea1c86db2cd6191a62c73ead900 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=82c984a8d119b70831679f974be9620e 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0f40f9ef8e9e536b398c955705d3e8a0 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=57470c8ec01687f50bd8d5294f53f197 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0272092dec7b91e1d6e4bcad7e426034 2500w" />
</Frame>

…and click **Save**.

## What's next?

The initial sync might take some time; it depends on the number of objects at your Tableau site. Eventually, Tableau entities — **Data Connections**, **Workbooks**, and **Dashboards** should appear at your **Lineage** tab.

<Tip>
  **TIP**

  [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) explains how to find out when your data app integration is ready.
</Tip>

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5c50a2f796a1b466fe221383084af2bc" alt="Search Tableau Entities" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=26d31ae71d4396e9f41492ca3ddc93f9 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=764c6f049e78c350c444967ff78b576f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ef01f54fdc4a078f33843d80c236d3e2 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0f8f3a9981eb9523b427e7c128fce4c4 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9f451b2233ba03700748f084d6924e91 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f1e3ce5b6c7a4135a177556c8d5a055d 2500w" />
</Frame>

Clicking on a Tableau entity will lead you to the Lineage screen:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a47f739973d5178eba9b9d1b9160e034" alt="Tableau Lineage Screen" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/lineage-cbcb37952c6d09346c7877038c9f3e39.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8cff9920b5413823694c2513f9c90b74 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8985891daae8f58656eb4cd208441e73 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e240416086ff4eaff8ffee6826d22888 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0523d2936aa81b4501449255c3d46b41 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=03e340e89f327ce4da9473f937fd305b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=479546b7f2f99b1088b3cbaeec21eb9b 2500w" />
</Frame>

<Tip>
  **TIP**

  As you might have noticed on the screenshots above, Datafold does not display Tableau **Sheets**. Instead, we group, and deduplicate, all **Fields** of all **Sheets** within a **Workbook** and display them as **Fields** of the **Workbook**.

  On the screenshot directly above, `Demo Workbook` might include one **Sheet** with `Created At` field and another with `Sub Plan` field, but for our purposes we unite all of those fields beneath the **Workbook** — which makes the Lineage graph much less cluttered, and much easier to browse <Icon icon="face-smirking" />
</Tip>

## FAQ

<AccordionGroup>
  <Accordion title="Why aren't my Tableau Extracts showing up in Datafold?">
    Lineage is only supported for Tableau assets in <strong>Live</strong> mode. Assets in <strong>Extract</strong> mode will not appear in Datafold lineage or dependency views.
  </Accordion>

  <Accordion title="I changed something in Tableau — but Datafold does not reflect my changes">
    Datafold retrieves Tableau metadata using the Tableau API, which may not immediately reflect recent changes due to internal caching. If your updates aren’t showing up in Datafold, give it a few hours — they should appear once Tableau refreshes its metadata.
  </Accordion>
</AccordionGroup>


# Tracking Jobs
Source: https://docs.datafold.com/integrations/bi-data-apps/tracking-jobs

Track the completion and success of your data app integration syncs.

To track the progress of your data app integration, go to the **<Icon icon="wrench" /> Jobs** tab in the left sidebar.

<Frame caption="Data App Jobs">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1902c9e03d710e05d544f1cdecc60abb" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=72a2a7e53dd001979e0079240fefa85d 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0643c3c9e9a8efb5aa27513b4d299244 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=459dcbec87eb73fc17a1427d6b116c4f 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1b4fc0db04805c030014979ac6e6e142 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b5c0640c3d0c316629e0ca694a432bcc 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_jobs-46476d10e9860210c1889b5b9ff196f8.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=be3ab6c21579ed8f6d0958bcb4573073 2500w" />
</Frame>

Your **Search** and **Lineage** features will be available once you see a job marked as `Done` for your integration on this screen.

<Note>
  **INFO**

  After the initial sync, Datafold will automatically re-sync every hour to keep your Data App assets up to date.
</Note>


# Integrate with Code Repositories
Source: https://docs.datafold.com/integrations/code-repositories

Connect your code repositories with Datafold.

<Info>
  **NOTE**

  To integrate with code repositories, first connect a [Data Connection](/integrations/databases).

  Next, go to **Settings** → **Repositories** and click **Add New Integration**. Then, choose your code repository provider.
</Info>

<CardGroup>
  <Card title="GitHub" icon="file" href="/integrations/code-repositories/github" horizontal />

  <Card title="GitLab" icon="file" href="/integrations/code-repositories/gitlab" horizontal />

  <Card title="Bitbucket" icon="file" href="/integrations/code-repositories/bitbucket" horizontal />

  <Card title="Azure DevOps" icon="file" href="/integrations/code-repositories/azure-devops" horizontal />
</CardGroup>


# Azure DevOps
Source: https://docs.datafold.com/integrations/code-repositories/azure-devops



## 1. Issue an Access Token

To get your [repository access token](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows#create-a-pat), navigate to your Azure DevOps settings and create a new token.

When configuring your token, enable following permissions:

* **Code** -> **Read & write**
* **Identity** -> **Read**

We need write access to the repository to post reports with Data Diff results to pull requests, and read access to identities to be able to properly display Azure DevOps users in the Datafold UI.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=79b790bb635c11e7b92e046ff26ff193" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1a9c8b05e52cd7cc63fa37a0856e9eaa 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a9b631782274cc2200e89fd0dbb92ffe 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c7af01cd57c6ce4d42ffe11912e50df7 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=315e5317bf383a490093666fdcb99325 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0a2bdbaf542c8837df118334980bf94b 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5855c1335750b1b7ada5081fd672b267 2500w" />
</Frame>

## 2. Configure integration in Datafold

Navigate back to Datafold and fill in the configuration form.

* **Personal/project Access Token**: the token you created in step 1.
* **Organization**: your Azure DevOps organization name.
* **Project**: your Azure DevOps project name.
* **Repository**: your Azure DevOps repository name.

For example, if your Azure DevOps repository URL is `https://dev.azure.com/datafold/analytics/_git/dbt`:

* Your **Organization** is `datafold`
* your **Project** is `analytics`
* your **Repository** is `dbt`


# Bitbucket
Source: https://docs.datafold.com/integrations/code-repositories/bitbucket



## 1. Issue an Access Token

### Bitbucket Cloud

To get the [repository access token](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/), navigate to your Bitbucket repository settings and create a new token.

When configuring your token, enable following permissions:

* **Pull requests** -> **Write**, so that Datafold can post reports with Data Diff results to pull requests.
* **Webhooks** -> **Read and write**, so that Datafold can configure all webhooks that we need automatically.

<Frame caption="Bitbucket Access Token">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8f59ced50090f42d1c8126a9a816c86a" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a8c5abd09425e95ad760081c3a461fe1 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5956cdaead951b18d186e4fa896f1480 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=597c82abfed30f0c62b2ae780249ffdf 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5f108a2379805bd2202d12826ac7396e 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=75df67fbd366291cb00b18b4a7c0d15f 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ab81b22af16b5f1e373c98f1f86d14d1 2500w" />
</Frame>

### Bitbucket Data Center / Server

To get a [repository access token](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html), navigate to your Bitbucket repository settings and create a new token.

When configuring your token, enable **Repository admin** permissions.
We need admin access to the repository to be able to post reports with Data Diff results to pull requests, and also configure all necessary webhooks automatically.

<Frame caption="Bitbucket Server Access Token">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=fe7a17de6da297d97624585a9c6415ba" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=24c9641828996ace84a453d73f2fcb79 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a015dacba7bca059ccc2bd0cd2fb0ff5 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5d55f42df68f5f9e804882cdceb00557 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c03ff8b4f2236f7f4efae41ac718ab67 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b1a45716ff752606d26f83f4d4e69b92 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=59e569fcb832271a9dfc56596828d516 2500w" />
</Frame>

## 2. Configure integration in Datafold

Navigate back to Datafold and fill in the configuration form.

### Bitbucket Cloud

* **Personal/project Access Token**: the token you created in step 1.
* **Repository**: your Bitbucket repository name.
  For example, if your Bitbucket project URL is `https://bitbucket.org/datafold/dbt/`, your Project Name is `datafold/dbt`.

### Bitbucket Data Center / Server

* **Personal/project Access Token**: the token you created in step 1.
* **Repository**: the full URL of your Bitbucket repository.
  For example, `https://bitbucket.myorg.com/projects/datafold/repos/dbt`.


# GitHub
Source: https://docs.datafold.com/integrations/code-repositories/github



<Note>
  **PREREQUISITES**

  * Datafold Admin role
  * Your GitHub account must be a member of the GitHub organization where the Datafold app is to be installed
  * Approval of your request to add the Datafold app to your repo must be granted by a GitHub repo admin or GitHub organization owner.
</Note>

To set up a new integration, click the repository field and select the **Install GitHub app** button.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=05a583165e696cf4d8191cefb37d6ed9" data-og-width="2200" width="2200" data-og-height="926" height="926" data-path="images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84e1ae6bce9b0005b6bebe64cdd50419 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9938eca7a9b6e490e78b5cdb157e0c90 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fcadb062275a2f2a19a1cad8565afd12 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=aa5415f0b1d845bf78dd0fb9f394dff3 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5bb5b709bf66c29e08f9278a03d5912f 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=226f0c8dcc9b79efee20a28cc23ab2ce 2500w" />
</Frame>

From here, GitHub will redirect you to login to your account and choose which organization you would like to connect. After choosing the right organization, you may choose to allow access to all repositories or specific ones.

Once complete, you will be redirected back to Datafold, where you can select the appropriate repository for connection.

<Tip>
  **TIP**

  If you lack permission to add the Datafold app, request approval from a GitHub admin.

  After installation, click **Refresh** to display the newly added repositories in the dropdown list.
</Tip>

To complete the setup, click **Save**!

<Note>
  **INFO**
  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## GitHub integration for VPC / single-tenant Datafold deployments

### Create a GitHub application

VPC clients of Datafold need to create their own GitHub app, rather than use the shared Datafold GitHub application.

Start by navigating to **Settings** → **Global Settings**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=064ce50091eaab88a16f0314e60103b0" data-og-width="2522" width="2522" data-og-height="1252" height="1252" data-path="images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3e56fc9b9cd2b1c23e4dc6afca485b59 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=33871ca1d5cd170f7b0393445b8dc553 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa0b6b1cfc74be40ee5eb534ce0972fe 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=508aa055d66678e9fc08fe19be33d61b 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e5903eb74f03ac6d5b07109d61114e9d 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2244e0facc8b84411a791d5d7c78c8ae 2500w" />
</Frame>

To begin the set up process, enter the domain that was registered for the VPC deployment in [AWS](/datafold-deployment/dedicated-cloud/aws) or [GCP](/datafold-deployment/dedicated-cloud/gcp). Then, enter the name of the GitHub organization where you'd like to install the application. When filled, click **Create GitHub App**.

This will redirect the admin to GitHub, where they may need to authenticate. **The GitHub user must be an admin of the GitHub organization.**

After authentication, you should be directed to enter a description for the GitHub App. After entering the description, click **Create GitHub app**.

Once the application is created, you should be returned to the Datafold settings screen. The button should then have disappeared, and the details for the GitHub App should be visible.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1f647e225a50e347520543a74fb723f5" data-og-width="1421" width="1421" data-og-height="1017" height="1017" data-path="images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c023b6d6e7864ca9472c63ce96232117 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=77e0cc92b48c790229f8b19c3aaf4a97 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cdaaa3e226a502fa20d171c786652bbc 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3b3b4d3a9d91b52dacc47b170e1b0eaf 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=af589570089dce593316a501c0ac0902 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=47b8dd90d161524aecfb53fdeb1794fb 2500w" />
</Frame>

### Making the GitHub application public

If you have a private GitHub instance with multiple organizations and want to use the Datafold app across all of them, you'll need to make the app public on your private server.

You can do so in GitHub by following these steps:

1. Navigate to the GitHub organization where the app was created.
2. Click **Settings**.
3. Go to **Developer Settings** → **GitHub Apps**.
4. Select the **Datafold app**.
5. Click **Advanced**, then **Make public**.

<Note>
  The app will be public **only on your private GitHub server**, ensuring it can be accessed across all your organizations.
</Note>

### Configure GitHub in Datafold

If you see this screen with all the details, you've successfully created a GitHub App! Now that the app is created, you have to install it using the [GitHub integration setup](/integrations/code-repositories/github).


# GitLab
Source: https://docs.datafold.com/integrations/code-repositories/gitlab



To get the [project access token](https://docs.gitlab.com/ee/user/project/settings/project%5Faccess%5Ftokens.html), navigate to your GitLab project settings and create a new token.

<Tip>
  **TIP**

  Project access tokens are preferred over personal tokens for security.
</Tip>

When configuring your token, select the **Maintainer** role and select the **api** scope.

<Frame caption="GitLab Access Token">
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3b4f13fecd884a73f79fc5f29ed635d0" data-og-width="1541" width="1541" data-og-height="970" height="970" data-path="images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e14c77bfa9c922fe95bf31ca0816daa5 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=49cafe904b45ca280c0277eaae1990f9 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=415d7a83e6355e9af220a0b29301c702 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=921ef53fc15fc1f17c35dcc0beb58e8a 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5b2ef6941943b34a7149dfa897643ab1 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f92882e757e73d4396d4dba68b5eb700 2500w" />
</Frame>

**Project Name** is your Gitlab project URL after `gitlab.com/`. For example, if your Gitlab project URL is `https://gitlab.com/datafold/dbt/`, your Project Name is `datafold/dbt/`

Finally, navigate back to Datafold and enter the **Project Token** and the name of your **Project** before hitting **Save**:

<Frame caption="New GitLab Integration in Datafold">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1c65ed01289e60b48693cca20d5e9d75" data-og-width="897" width="897" data-og-height="423" height="423" data-path="images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=542c25d2b59aa6f014e80327300c85f9 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9586ccb24ce5515ac01d1ec30bbca3ec 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ef74c6101145fc1fb404dce3769b286f 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a8572ad991d2ff8989fd8ca64f09521f 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a37dde70dedfc2cb91012079968455f0 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a9998b17350a04b42154524cd793d8b3 2500w" />
</Frame>

If you want to change the GitLab URL, you can do so after setting up the integration. To do so, navigate to **Settings**, then **Org Settings**:

<Frame caption="Change GitLab URL">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bcfd8113d0beecd9fc51341f22ce3c8b" data-og-width="1058" width="1058" data-og-height="819" height="819" data-path="images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=33418eb4e8b420075d4bbb4ce3c3a0a2 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f31735ff0fe22efda30df333e113f09c 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=29d5e7a86c9de7e402ef9280f26c52b2 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=95df988be241f25cfd157960193515da 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=43560ac997f5146c34681ca6a9c0a1d5 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=84ffdd694df48e54815ec8bcdc34a9e6 2500w" />
</Frame>


# Set Up Your Data Connection
Source: https://docs.datafold.com/integrations/databases

Set up your Data Connection with Datafold.

<Info>
  **NOTE**

  To set up your Data Connection, navigate to **Settings** → **Data Connection** and click **Add New Integration**.
</Info>

<CardGroup>
  <Card title="Amazon S3" icon="file" href="/integrations/databases/amazon-s3" horizontal />

  <Card title="Azure Data Lake Storage (ADLS)" icon="file" href="/integrations/databases/adls" horizontal />

  <Card title="Athena" icon="file" href="/integrations/databases/athena" horizontal />

  <Card title="BigQuery" icon="file" href="/integrations/databases/bigquery" horizontal />

  <Card title="Databricks" icon="file" href="/integrations/databases/databricks" horizontal />

  <Card title="Dremio" icon="file" href="/integrations/databases/dremio" horizontal />

  <Card title="Google Cloud Storage (GCS)" icon="file" href="/integrations/databases/google-cloud-storage" horizontal />

  <Card title="MongoDB" icon="file" href="/integrations/databases/mongodb" horizontal />

  <Card title="MySQL" icon="file" href="/integrations/databases/mysql" horizontal />

  <Card title="MariaDB" icon="file" href="/integrations/databases/mariadb" horizontal />

  <Card title="Netezza" icon="file" href="/integrations/databases/netezza" horizontal />

  <Card title="Oracle" icon="file" href="/integrations/databases/oracle" horizontal />

  <Card title="Snowflake" icon="file" href="/integrations/databases/snowflake" horizontal />

  <Card title="PostgreSQL" icon="file" href="/integrations/databases/postgresql" horizontal />

  <Card title="Redshift" icon="file" href="/integrations/databases/redshift" horizontal />

  <Card title="SAP HANA" icon="file" href="/integrations/databases/sap-hana" horizontal />

  <Card title="Teradata" icon="file" href="/integrations/databases/teradata" horizontal />

  <Card title="Trino" icon="file" href="/integrations/databases/trino" horizontal />

  <Card title="Vertica" icon="file" href="/integrations/databases/vertica" horizontal />

  <Card title="Microsoft SQL Server" icon="file" href="/integrations/databases/sql-server" horizontal />

  <Card title="Starburst" icon="file" href="/integrations/databases/starburst" horizontal />
</CardGroup>


# Azure Data Lake Storage (ADLS)
Source: https://docs.datafold.com/integrations/databases/adls



<Note>
  This integration supports both Azure Data Lake Storage and Azure Blob Storage.
</Note>

**Steps to complete:**

1. [Create an app and service principal in Microsoft Entra](#create-an-app-and-service-principal-in-microsoft-entra)
2. [Configure your data connection in Datafold](#configure-your-data-connection-in-datafold)
3. [Create your first file diff](#create-your-first-file-diff)

## Create an app and service principal in Microsoft Entra

Create an app and service principal in Entra using a client secret (not certificate). Check out [Microsoft's documentation](https://learn.microsoft.com/en-us/entra/architecture/service-accounts-principal) on this topic if you need help.

<img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e710f7b59ebdd0cbe835516cb7419841" alt="Use client secret" data-og-width="1612" width="1612" data-og-height="1008" height="1008" data-path="images/adls-client-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5f1a774c196aa3ca0a0d94684e2a4f25 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2cc28f7dad1af49b7c530f5ab0fc9b61 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=12f01e13d8ff8ccb9fa7ac1fb19f2bd1 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0fd552548c9e3d81ed987c483d28c5c3 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4829d2e4473dffcf074a506b12769400 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=241ff1a2ff4b3bfc61f4201ca9359f8d 2500w" />

## Configure your data connection in Datafold

<img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3e431654ca4c81a250d38eb240d5cbaa" alt="ADLS Data Connection" data-og-width="2084" width="2084" data-og-height="856" height="856" data-path="images/adls-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=66bad0a74f27f22f3c6e2762b752838d 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ec7b672ace0875d685304d00a5322e74 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=29f1f2c17174c58b3f7691fbcfa9c1dd 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c1f8754079db110a411fbbc0cd5bd56b 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4f243432651b296c800952cd86e96e03 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f94b7a55513d23bf3d0fd96c10cbf6b2 2500w" />

| Field Name      | Description                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| Connection name | The name you'd like to give to this connection in Datafold                                               |
| Account Name    | This is in the URL of any filepath in ADLS, e.g. `<account>.dfs.core.windows.net/<container>/<filepath>` |
| Client ID       | The client ID of the app you created in Microsoft Entra                                                  |
| Client Secret   | The client secret of the app you created in Microsoft Entra                                              |
| Tenant ID       | The tenant ID of the app you created in Microsoft Entra                                                  |

## Create your first file diff

For general guidance on how file diffs work in Datafold, check out our [file diffing docs](/data-diff/file-diffing).

When creating a diff, note that the file path you provide may differ depending on whether you're using ADLS or Blob Storage. For example:

* ADLS: `abfss://<my_filesystem>/<path>/<my_file>.<csv, xlsx, parquet, etc.>`
* Blob Storage: `az://<my_container>/<path>/<my_file>.<csv, xlsx, parquet, etc.>`


# Amazon S3
Source: https://docs.datafold.com/integrations/databases/amazon-s3



**Steps to complete:**

1. [Create a user with access to S3](/integrations/databases/google-cloud-storage#create-a-service-account)
2. [Assign the user to the S3 bucket](/integrations/databases/google-cloud-storage#service-account-access-and-permissions)
3. [Create an access key for the user](/integrations/databases/google-cloud-storage#generate-a-service-account-key)
4. [Configure your data connection in Datafold](/integrations/databases/google-cloud-storage#configure-in-datafold)

## Create a user with access to S3

To connect your Amazon S3 bucket, you will need to create a user for Datafold to use.

* Navigate to the [AWS Console](https://console.aws.amazon.com/).
* Click on the search bar in the top header, then find **IAM** service and click on it.
* Click on the **Users** item of the Access Management section.
* Click on the **Create user** button.
* Create a user named `Datafold`.
* Assign the user to the `AmazonS3FullAccess` policy.
* When done, keep ARN of the user handy as you'll need it in the next step.

## Assign the user to the S3 bucket

* Go to S3 panel and select the bucket.
* Click on the **Permissions** tab.
* Click on **Edit** next to the **Bucket Policy**.
* Add the following policy:
  ```json  theme={null}
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam:::user/Datafold" // Replace with your user's ARN
        },
        "Action": [
          "s3:GetObject",
          "s3:PutObject" // Optional: Only needed if you're planning to use this data connection as a destination for materialized diff results.
        ],
        "Resource": [
          "arn:aws:s3:::your-bucket-name/*", // Replace with your bucket's ARN
          "arn:aws:s3:::your-bucket-name" // Replace with your bucket's ARN
        ]
      }
    ]
  }
  ```

<Note>
  The Datafold user requires the following roles and permissions:

  * **s3:GetObject** for read access.
  * **s3:PutObject** for write access if you're planning to use this data connection as a destination for materialized diff results.
</Note>

## Create an access key for the user

Next, go back to the **IAM** page to generate a key for Datafold.

* Click on the **Users** page.
* Click on the **Datafold** user.
* Click on the **Security Credentials** tab.
* Click on **Create access key** and select **Create new access key**.
* Select **JSON** and click **Create**.

## Configure in Datafold

| Field Name                                                | Description                                                                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Connection name                                           | A name given to the data connection within Datafold                                                                                   |
| Bucket Name                                               | The name of the bucket you want to connect to.                                                                                        |
| Bucket region                                             | The region of the bucket you want to connect to.                                                                                      |
| Key ID                                                    | The key file generated in the [Create an access key for the user](#create-an-access-key-for-the-user) step                            |
| Secret Access Key                                         | The secret access key generated in the [Create an access key for the user](#create-an-access-key-for-the-user) step                   |
| Directory for writing diff results                        | Optional. The directory in the bucket where diff results will be written. Service account should have write access to this directory. |
| Default maximum number of rows to include in diff results | Optional. The maximum number of rows that a file with materialized results will contain.                                              |

Click **Create**. Your data connection is ready!


# Athena
Source: https://docs.datafold.com/integrations/databases/athena



**Steps to complete:**

1. [Create an S3 bucket](/integrations/databases/athena#create-s3-bucket)
2. [Run SQL Script for permissions](/integrations/databases/athena#run-sql-script)
3. [Configure your data connection in Datafold](/integrations/databases/athena#configure-in-datafold)

### Create an S3 bucket

If you don't already have an S3 bucket for your cluster, you'll need to create one. Datafold uses this bucket to create temporary tables and store data in it. You can learn how to create an S3 bucket in AWS by referring to the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

### Run SQL Script and Create Schema for Datafold

To connect to AWS Athena, you must generate an `AWS Access Key ID` and an `AWS Secret Access Key`. These keys provide read-only access to all tables in all schemas and write access to the Datafold-specific schema for temporary tables. If you don't have these keys yet, follow the steps outlined in the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Faccess-keys.html).

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

```
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing witin your data warehouse. */

CREATE SCHEMA IF NOT EXISTS awsdatacatlog.datafold_tmp;
```

### Configure in Datafold

| Field Name                  | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ |
| AWS Access Key ID           | Your AWS Access Key, which can be found in your AWS Account.                   |
| AWS Secret Access Key       | The AWS Secret Key (generate it in your AWS account if you don't have it yet). |
| S3 Staging Directory        | The S3 bucket where table data is stored.                                      |
| AWS Region                  | The region of your Athena cluster.                                             |
| Catalog                     | The catalog, which is typically awsdatacatalog by default.                     |
| Database                    | The database or schema with tables, typically default by default.              |
| Schema for Temporary Tables | The schema (datafold\_tmp) created in our SQL script.                          |

Click **Create** to complete the setup of your data connection in Datafold.


# BigQuery
Source: https://docs.datafold.com/integrations/databases/bigquery



**Steps to complete:**

1. [Create a Service Account](/integrations/databases/bigquery#create-a-service-account)
2. [Give the Service Account BigQuery Data Viewer, BigQuery Job User, BigQuery Resource Viewer access](/integrations/databases/bigquery#service-account-access-and-permissions)
3. [Create a temporary dataset and give BiqQuery Data Editor access to the service account](/integrations/databases/bigquery#create-a-temporary-dataset)
4. [Generate a Service Account JSON key](/integrations/databases/bigquery#generate-a-service-account-key)
5. [Configure your data connection in Datafold](/integrations/databases/bigquery#configure-in-datafold)

## Create a Service Account

To connect Datafold to your BigQuery project, you will need to create a *service account* for Datafold to use.

* Navigate to the [Google Developers Console](https://console.developers.google.com/), click on the drop-down to the left of the search bar, and select the project you want to connect to.
  * *Note: If you do not see your project, you may need to switch accounts.*
* Click on the hamburger menu in the upper left, then select **IAM & Admin** followed by **Service Accounts**.
* Create a service account named `Datafold`.

## Service Account Access and Permissions

The Datafold service account requires the following roles and permissions:

* **BigQuery Data Viewer** for read access on all the datasets in the project.
* **BigQuery Job User** to run queries.
* **BigQuery Resource Viewer** to fetch the query logs for parsing lineage.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d519e227abd888a332872e582764c3c3" data-og-width="1632" width="1632" data-og-height="1080" height="1080" data-path="images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=51fd294a51129d4c58c48030d39f68be 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f5b37ca01498895ee6214b4c42988edf 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8a93d315df5aa90f2f2774311a5c95c1 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=216434403ab8d42368e76cc5c7b55930 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bec30f822676a52428d61e5e82de1469 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=213d9b15664c6924c53f9bdd14dd65c5 2500w" />
</Frame>

## Create a Temporary Dataset

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in your warehouse.

**Caution** - Make sure that the dataset lives in the same region as the rest of the data, otherwise, the dataset will not be found.

Let's navigate to BigQuery in the console and create a new dataset.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=80e39c735cf8b56cb83911e5b89bd29f" data-og-width="1632" width="1632" data-og-height="1080" height="1080" data-path="images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6df91c1c6119ad83e48f072d4f18cfad 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=387a99b64f99a91a69f9dd055b05c126 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a6b8f7dc3852a90f5b35160e08e7be16 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0920bafeaad7a67472f868f74baf327e 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0c59f9877e2d49ab39a4eee644b03920 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d6045097feb58d974bbe7c09d8ca3203 2500w" />
</Frame>

* Give the dataset a name like `datafold_tmp` and grant the Datafold service account the **BigQuery Data Editor** role.

## Generate a Service Account Key

Next, go back to the **IAM & Admin** page to generate a key for Datafold.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8507cf5601ad67bf1757082daee45bf9" data-og-width="1632" width="1632" data-og-height="1080" height="1080" data-path="images/bigquery_key-368911548a71c512d065b1a227dace96.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=18b2b546fd64d40c1261cb66d072844f 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b8a730cd3879954da974790fc9047304 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9254addd372c20c779d0dd3ba2590437 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d00fe16de4302197e6c174abb1e226de 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=99d9d2490db846e5d2e75e65a51dc78a 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fb26fd122245d0151cfb3d7643a3161d 2500w" />
</Frame>

We recommend using the json formatted key. After creating the key, it will be saved on your local machine.

## Configure in Datafold

| Field Name                  | Description                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                        | A name given to the data connection within Datafold                                                                                                                                                                                                    |
| Project ID                  | Your BigQuery project ID. It can be found in the URL of your Google Developers Console: [https://console.developers.google.com/apis/library?project=MY\\\_PROJECT\\\_ID](https://console.developers.google.com/apis/library?project=MY\\_PROJECT\\_ID) |
| JSON Key File               | The key file generated in the [Generate a Service Account JSON key](/integrations/databases/bigquery#generate-a-service-account-key) step                                                                                                              |
| Schema for temporary tables | The schema name that was created in [Create a temporary dataset](/integrations/databases/bigquery#create-a-temporary-dataset). It should be formatted as \<project\_id>.datafold\_tmp                                                                  |
| Processing Location         | Which processing zone your project uses                                                                                                                                                                                                                |

Click **Create**. Your data connection is ready!


# Databricks
Source: https://docs.datafold.com/integrations/databases/databricks



**Steps to complete:**

1. [Generate a Personal Access Token](/integrations/databases/databricks#generate-a-personal-access-token)
2. [Retrieve SQL warehouse settings](/integrations/databases/databricks#retrieve-sql-warehouse-settings)
3. [Create schema for Datafold](/integrations/databases/databricks#create-schema-for-datafold)
4. [Configure your data connection in Datafold](/integrations/databases/databricks#configure-in-datafold)

## Generate a Personal Access Token

Visit **Settings** → **User Settings**, and then switch to **Personal Access Tokens** tab.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=77790371e1ab9da75072541115e76ef3" data-og-width="2638" width="2638" data-og-height="1644" height="1644" data-path="images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c7b74e10b593263d0cc301624721bfb3 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=ae39c6e82f203dd6c3c5b1f9334b48d0 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83b3833dc6231cc68cd41e6ab3551d0b 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=6150f351a20c0d48f7fddeea8bdf2e91 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4db8795496564e463a41237244b5636c 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_new_token-a2d1a65a0105ce7ad38fca457967b07c.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b1e324220abdd51fe0c8b8e2bb41c4c2 2500w" />
</Frame>

Then, click **Generate new token**. Save the generated token somewhere, you'll need it later on.

## Retrieve SQL warehouse settings

In **SQL** mode, navigate to **SQL Warehouses**.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b9b5121c2a90cc855b8c2a5b0ef447ef" data-og-width="724" width="724" data-og-height="455" height="455" data-path="images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4e71648f9866e2051eca35f6f4b1930b 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=41bc7c67a4c9ce7a7f4ac2f7d7db8765 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=15e096e254600bfb0de3bb96b30de6f3 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cca8159fd049d6198ae0f02809e134ed 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=5ab9363e2bdab2a0254bf7640e95b6dc 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databricks_sql_warehouse-80e1f70713a973cb310a7b1d4d32a409.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c538938c20ac5236d8eda63c3de67072 2500w" />
</Frame>

Choose the preferred warehouse and copy the following fields values from its **Connection Details** tab:

* Server hostname
* HTTP path

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c08e73c1c329dfe0120cc7a6287dd4a7" data-og-width="2638" width="2638" data-og-height="1644" height="1644" data-path="images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a554bf925d1acb4c0d65f7c459ba901c 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9e38ad072bd7875aae1731d6f835bb76 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=04b92efdc808ad8ad63eb4b25c55d8ab 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c6b1832bae9efb023c665709eb1d72af 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=20a9617da84665fd3f8ffcf7bc7bacc9 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/databrick_connection_details-5b5208f53126fa0d4dd18dc21f3ffd61.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8fec93f2fc8b8b819c4304d93895260f 2500w" />
</Frame>

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                   | Description                                                                                                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                         | A name given to the data connection within Datafold                                                                                                                                                                                              |
| Host                         | The hostname retrieved in the Connection Details tab                                                                                                                                                                                             |
| HTTP Path                    | The HTTP Path retrieved in the Connection Details tab                                                                                                                                                                                            |
| Access Token                 | The token retrieved in [Generate a Personal Access Token](/integrations/databases/databricks#generate-a-personal-access-token)                                                                                                                   |
| Catalog                      | The catalog and schema name of your Databricks account. Formatted as catalog\_name.schema\_name (In most cases, catalog\_name is hive\_metastore.)                                                                                               |
| Dataset for temporary tables | Certain operations require Datafold to materialize intermediate results, which are stored in a dedicated schema. The input for this field should be in the catalog\_name.schema\_name format. (In most cases, catalog\_name is hive\_metastore.) |

Click **Create**. Your data connection is ready!


# Dremio
Source: https://docs.datafold.com/integrations/databases/dremio



<Note>
  **INFO**

  Column-level Lineage is not currently supported for Dremio.
</Note>

<Note>
  **INFO**

  Schemas for tables in external data sources need to be specified with quotes e.g., "Postgres prod.analytics.sales".
</Note>

**Steps to complete:**

1. [Configure user in Dremio](/integrations/databases/dremio#configure-user-in-dremio)
2. [Create schema for Datafold](/integrations/databases/dremio#create-schema-for-datafold)
3. [Configure your data connection in Datafold](/integrations/databases/dremio#configure-in-datafold)

## Configure user in Dremio

To connect to Dremio, create a user with read-only access to all data sources you wish to diff and generate an access token.

Temporary tables will be created in the `$scratch` schema that doesn't require special permissions.

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection name             | A name given to the data connection within Datafold.                                                                                                       |
| Host                        | The hostname for your Dremio instance (data.dremio.cloud for Dremio SaaS).                                                                                 |
| Port                        | Dremio endpoint port; default value is 433.                                                                                                                |
| Encryption                  | Should be checked for Dremio Cloud, possibly unchecked for local deployments.                                                                              |
| User ID                     | User ID as created in Dremio, typically an email address.                                                                                                  |
| Project ID                  | Dremio Project UID. If left blank, the default project will be used.                                                                                       |
| Token                       | Access token generated in Dremio.                                                                                                                          |
| Password                    | Alternatively, provide a password.                                                                                                                         |
| Schema for temporary views  | A Dremio space for temporary views.                                                                                                                        |
| Schema for temporary tables | \$scratch should suit most applications, or use "\<Datasource>.\<schema>" (with quotes) if you wish to create temporary tables in an external data source. |

Click **Create**. Your data connection is now ready!


# Google Cloud Storage (GCS)
Source: https://docs.datafold.com/integrations/databases/google-cloud-storage



**Steps to complete:**

1. [Create a Service Account](/integrations/databases/google-cloud-storage#create-a-service-account)
2. [Give the Service Account Storage Object Admin access](/integrations/databases/google-cloud-storage#service-account-access-and-permissions)
3. [Generate a Service Account JSON key](/integrations/databases/google-cloud-storage#generate-a-service-account-key)
4. [Configure your data connection in Datafold](/integrations/databases/google-cloud-storage#configure-in-datafold)

## Create a Service Account

To connect Datafold to your Google Cloud Storage bucket, you will need to create a *service account* for Datafold to use.

* Navigate to the [Google Cloud Console](https://console.cloud.google.com/), click on the drop-down to the left of the search bar, and select the project you want to connect to.
  * *Note: If you do not see your project, you may need to switch accounts.*
* Click on the hamburger menu in the upper left, then select **IAM & Admin** followed by **Service Accounts**.
* Create a service account named `Datafold`.

## Service Account Access and Permissions

The Datafold service account requires the following roles and permissions:

* **Storage Object Admin** for read and write access on all the datasets in the project.

## Generate a Service Account Key

Next, go back to the **IAM & Admin** page to generate a key for Datafold.

* Click on the **Service Accounts** page.
* Click on the **Datafold** service account.
* Click on the **Keys** tab.
* Click on **Add Key** and select **Create new key**.
* Select **JSON** and click **Create**.

We recommend using the JSON formatted key. After creating the key, it will be saved on your local machine.

## Configure in Datafold

| Field Name                                                | Description                                                                                                                                           |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection name                                           | A name given to the data connection within Datafold                                                                                                   |
| Bucket Name                                               | The name of the bucket you want to connect to.                                                                                                        |
| Bucket region                                             | The region of the bucket you want to connect to.                                                                                                      |
| JSON Key File                                             | The key file generated in the [Generate a Service Account JSON key](/integrations/databases/google-cloud-storage#generate-a-service-account-key) step |
| Directory for writing diff results                        | Optional. The directory in the bucket where diff results will be written. Service account should have write access to this directory.                 |
| Default maximum number of rows to include in diff results | Optional. The maximum number of rows that a file with materialized results will contain.                                                              |

Click **Create**. Your data connection is ready!


# MariaDB
Source: https://docs.datafold.com/integrations/databases/mariadb



<Note>
  **INFO**

  Column-level Lineage is not currently supported for MariaDB.
</Note>

**Steps to complete:**

1. [Run SQL script for permissions and create schema for Datafold](/integrations/databases/mariadb#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/mariadb#configure-in-datafold)

### Run SQL script and create schema for Datafold

To connect to MariaDB, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific dataset:

```Bash  theme={null}
-- Create a temporary dataset for Datafold to utilize
CREATE DATABASE IF NOT EXISTS datafold_tmp;

-- Create a Datafold user
CREATE USER 'datafold_user'@'%' IDENTIFIED BY 'SOMESECUREPASSWORD';

-- Grant read access to diff tables in YourSchema
GRANT SELECT ON `YourSchema`.* TO 'datafold_user'@'%';

-- Grant access to all tables in a datafold_tmp database
GRANT ALL ON `datafold_tmp`.* TO 'datafold_user'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
```

Datafold utilizes a temporary dataset, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

### Configure in Datafold

| Field Name                   | Description                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------- |
| Connection name              | A name given to the data connection within Datafold                               |
| Host                         | The hostname for your MariaDB instance                                            |
| Port                         | MariaDB connection port; default value is 3306                                    |
| Username                     | The user created in our SQL script, named datafold\_user                          |
| Password                     | The password created in our SQL script                                            |
| Database                     | The name of the MariaDB database (schema) you want to connect to, e.g. YourSchema |
| Dataset for temporary tables | The datafold\_tmp database created in our SQL script                              |

Click **Create**. Your data connection is ready!


# MongoDB
Source: https://docs.datafold.com/integrations/databases/mongodb

Our MongoDB integration allows you to diff data within MongoDB, or between MongoDB and a relational database (or even a file!).

<Note>
  Our MongoDB integration is still in beta. Some features, such as column-level lineage, are not yet supported. Please contact us if you need assistance.
</Note>

**Steps to complete:**

1. [Configure user in MongoDB](#configure-user-in-mongodb)
2. [Configure your data connection in Datafold](#configure-in-datafold)
3. [Diff your data](#diff-your-data)

## Configure user in MongoDB

To connect to MongoDB, create a user with read-only access to all databases you plan to diff.

## Configure in Datafold

| Field Name              | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| Connection Name         | The name you'd like to assign to this connection in Datafold     |
| Host                    | The hostname for your MongoDB instance                           |
| Port                    | MongoDB endpoint port (default value is 27017)                   |
| User ID                 | User ID (e.g. `DATAFOLD`)                                        |
| Password                | Password for the user provided above                             |
| Database                | Database to connect to                                           |
| Authentication Database | Database name associated with the user credentials (e.g. `main`) |

Click **Create**. Your data connection is now ready!

## Diff your data

<img src="https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=b34d51e42a44012a9a8bb7f1c838d123" alt="Write your MongoDB query" data-og-width="1156" width="1156" data-og-height="786" height="786" data-path="images/mongodb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=280&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=1e5d1e043b3e2d6ac81b3a7bb74c48d9 280w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=560&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=70602df16b4660d64755427f261133ba 560w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=840&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=11e11ba68b97e45b21dadd64cb45441f 840w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=1100&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=4213b5d6dca1b6b0cee35fb668d0fee1 1100w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=1650&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=55ccabd3ac64ec4244e9750df68b57f7 1650w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=2500&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=8af2b8e31c760ae48d6cf12cc0da9857 2500w" />

MongoDB works a bit differently from our other integrations. Under the hood, we flatten your collections into datasets you can query with SQL. Here's how to diff your MongoDB data:

1. Create a new data diff
2. Select your MongoDB data connection
3. Select `Query` diff (`Table` diffs aren't supported at this time)
4. Write a SQL query against the flattened dataset, including a `PRAGMA` statement with the collection name on the first line. Here's an example:
   ```sql  theme={null}
   PRAGMA mongodb_collections('tracks_v1_1m');

   SELECT point_id,
       device_id,
       timestamp,
       location.longitude as longitude,
       location.latitude as latitude
   FROM mongo_tracks_v1_1m
   WHERE point_id < 100000;
   ```
5. Configure the rest of your diff and run it!


# MySQL
Source: https://docs.datafold.com/integrations/databases/mysql



<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you use a MySQL version \< 8.x.
</Note>

<Note>
  **INFO**

  Column-level Lineage is not currently supported for MySQL.
</Note>

**Steps to complete:**

1. [Run SQL script for permissions and create schema for Datafold](/integrations/databases/mysql#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/mysql#configure-in-datafold)

### Run SQL script and create schema for Datafold

To connect to MySQL, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific dataset:

```Bash  theme={null}
-- Create a temporary dataset for Datafold to utilize
CREATE DATABASE IF NOT EXISTS datafold_tmp;

-- Create a Datafold user
CREATE USER 'datafold_user'@'%' IDENTIFIED BY 'SOMESECUREPASSWORD';

-- Grant read access to diff tables in YourSchema
GRANT SELECT ON `YourSchema`.* TO 'datafold_user'@'%';

-- Grant access to all tables in a datafold_tmp database
GRANT ALL ON `datafold_tmp`.* TO 'datafold_user'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
```

Datafold utilizes a temporary dataset, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

### Configure in Datafold

| Field Name                   | Description                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------- |
| Connection name              | A name given to the data connection within Datafold                             |
| Host                         | The hostname for your MySQL instance                                            |
| Port                         | MySQL connection port; default value is 3306                                    |
| Username                     | The user created in our SQL script, named datafold\_user                        |
| Password                     | The password created in our SQL script                                          |
| Database                     | The name of the MySQL database (schema) you want to connect to, e.g. YourSchema |
| Dataset for temporary tables | The datafold\_tmp database created in our SQL script                            |

Click **Create**. Your data connection is ready!


# Netezza
Source: https://docs.datafold.com/integrations/databases/netezza



<Note>
  **INFO**

  Column-level Lineage is not currently supported for Netezza.
</Note>

**Steps to complete:**

1. [Configure user in Netezza](#configure-user-in-netezza)
2. [Create schema for Datafold](#create-a-temporary-database-for-datafold)
3. [Configure your data connection in Datafold](#configure-in-datafold)

## Configure user in Netezza

To connect to Netezza, create a user with read-only access to all databases you may wish to diff.

## Create a temporary database for Datafold

Datafold requires a schema with full permissions to store temporary data.

## Configure in Datafold

| Field Name                  | Description                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection Name             | A name given to the data connection within Datafold.                                                                                          |
| Host                        | The hostname for your Netezza instance (e.g., nz-85dcf66c-69aa-4ba6-b7cb-827643da5a.us-east-1.data-warehouse.cloud.ibm.com for Netezza SaaS). |
| Port                        | Netezza endpoint port; the default value is 5480.                                                                                             |
| Encryption                  | Whether to use TLS.                                                                                                                           |
| User ID                     | User ID, e.g., DATAFOLD.                                                                                                                      |
| Password                    | Password from above.                                                                                                                          |
| Default DB                  | The database to connect to.                                                                                                                   |
| Schema for Temporary Tables | Use DATABASE.SCHEMA format.                                                                                                                   |

Click **Create**. Your data source is now ready!


# Oracle
Source: https://docs.datafold.com/integrations/databases/oracle



<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you use an Oracle version \< 19.x.
</Note>

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Oracle.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/oracle#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/oracle#configure-in-datafold)

## Run SQL script and create schema for datafold\_group

To connect to Oracle, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific temp schema:

```Bash  theme={null}
-- Switch container context (default is "XEPDB1")
ALTER SESSION SET CONTAINER = YOURCONTAINER;

-- Create a Datafold user/schema
CREATE USER DATAFOLD IDENTIFIED BY somesecurepassword;

-- Allow Datafold user to connect
GRANT CREATE SESSION TO DATAFOLD;

-- Allow user to create tables in DATAFOLD schema
GRANT CREATE TABLE TO DATAFOLD;

-- Grant read access to diff tables in your schema
GRANT SELECT ON "YOURSCHEMA"."YOURTABLE" TO DATAFOLD;

-- Grant access to DBMS_CRYPTO utilities (hashing functions, etc.)
GRANT EXECUTE ON SYS.DBMS_CRYPTO TO DATAFOLD;

-- Allow Datafold users/schemas to use disk space (adjust if needed)
GRANT UNLIMITED TABLESPACE TO DATAFOLD;

-- Apply the changes
COMMIT;

```

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold                                            |
| Host                        | The hostname address for your database                                                         |
| Port                        | Postgres connection port; default value is 1521                                                |
| User                        | The user role created in our SQL script, named DATAFOLD                                        |
| Password                    | The password created in our SQL script                                                         |
| Connection type             | Choose Service or SID depending on your connection type; default value is Service              |
| Service (or SID)            | The name of the database (Service or SID) you want to connect to, e.g. XEPDB1 or YOURCONTAINER |
| Schema for temporary tables | The user/schema created in our SQL script - DATAFOLD                                           |

Click **Create**. Your data connection is ready!


# PostgreSQL
Source: https://docs.datafold.com/integrations/databases/postgresql



<Note>
  **INFO**

  Column-level Lineage is supported for AWS Aurora and RDS Postgres and *requires* Cloudwatch to be configured.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/postgresql#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/postgresql#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Postgres, you need to create a user with read-only access to all tables in all schemas, write access to Datafold-specific schema for temporary tables:

```Bash  theme={null}
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in your warehouse. */

CREATE SCHEMA datafold_tmp;

/* Create a datafold user */

CREATE ROLE datafold WITH LOGIN ENCRYPTED PASSWORD 'SOMESECUREPASSWORD';

/* Give the datafold role write access to the temporary schema */

GRANT ALL ON SCHEMA datafold_tmp TO datafold;

/* Make sure that the postgres user has read permissions on the tables */

GRANT USAGE ON SCHEMA <myschema> TO datafold;
GRANT SELECT ON ALL TABLES IN SCHEMA <myschema> TO datafold;

```

Datafold utilizes a temporary schema, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold             |
| Host                        | The hostname address for your database; default value 127.0.0.1 |
| Port                        | Postgres connection port; default value is 5432                 |
| User                        | The user role created in our SQL script, named datafold         |
| Password                    | The password created in our SQL script                          |
| Database Name               | The name of the Postgres database you want to connect to        |
| Schema for temporary tables | The schema (datafold\_tmp) created in our SQL script            |

Click **Create**. Your data connection is ready!

***

## Column-level Lineage with Aurora & RDS

This will guide you through setting up Column-level Lineage with AWS Aurora & RDS using CloudWatch.

**Steps to complete:**

1. [Setup Postgres with Permissions](#run-sql-script)
2. [Increase the logging verbosity of Postgres](#increase-logging-verbosity) so Datafold can parse lineage
3. [Set up an account for fetching the logs from CloudWatch.](#connect-datafold-to-cloudwatch)
4. [Configure your data connection in Datafold](#configure-in-datafold)

### Run SQL Script

To connect to Postgres, you need to create a user with read-only access to all tables in all schemas, write access to Datafold-specific schema for temporary tables:

```Bash  theme={null}
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse. */

CREATE SCHEMA datafold_tmp;

/* Create a datafold user */

CREATE ROLE datafold WITH LOGIN ENCRYPTED PASSWORD 'SOMESECUREPASSWORD';

/* Give the datafole role write access to the temporary schema */

GRANT ALL ON SCHEMA datafold_tmp TO datafold;

/* Make sure that the postgres user has read permissions on the tables */

GRANT USAGE ON SCHEMA <myschema> TO datafold;
GRANT SELECT ON ALL TABLES IN SCHEMA <myschema> TO datafold;

```

### Increase logging verbosity

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9714c4922ccea50fd944c73765583084" data-og-width="1277" width="1277" data-og-height="820" height="820" data-path="images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5892e6b7f262fd48952d484b7fbeecd0 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5e5f0c59794c822122d6d068027ec288 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=186f4698af0774324dd98257b5473cca 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa0f4b0353acda27d205cf19db73ff58 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6bde0405bbeb3bf9ce3a351c7efdf250 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f448733acfbb18e4b43ccda538d934f8 2500w" />
</Frame>

Then, create a new `Parameter Group`. Database instances run with default parameters that do not include logging verbosity. To turn on the logging verbosity, you'll need to create a new Parameter Group. Hit **Parameter Groups** on the menu and create a new Parameter Group.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6bffe4b697e92e129c84c504967b3b4e" data-og-width="1277" width="1277" data-og-height="886" height="886" data-path="images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2041e8487561dc68a632f4b0e2146a57 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3f4bdd72d5beca4ef1d1ab3786e5238c 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6030776af5fa07f7f9c3c829b03f2504 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9c1abf936a8486048f9df6770bbb33e8 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2b76bb13e41e3036efdff2202abce1de 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=eba29682db0813d1cd2fc571d138ba25 2500w" />
</Frame>

Next, select the `aurora-postgresql10` parameter group family. This depends on the cluster that you're running. For Aurora serverless, this is the appropriate family.

Finally, set the `log_statement` enum field to `mod` - meaning that it will log all the DDL statements, plus data-modifying statements. Note: This field isn't set by default.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b1243c6b87aaa2c4b9efea52f51b8b61" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=59e3a715d3073f4e86fede0f67b76618 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=902351c9a3648501d87d4e5c3b5e8202 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d3fb96d7d514ef4e653ab88fde3bf946 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9767a83de15f37aae0411f5e0d80d7f1 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c6dd5452612e966f6552444b3f965c2d 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9edc31c9df62dc827068629124d59ccd 2500w" />
</Frame>

After saving the parameter group, go back to your database, and select the database cluster parameter group.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5fed528e2e74cbc506ca4ddda648eede" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e0c72e0110c73e39886248a33bc88d8b 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f9df5cb6534a765cca36ad27a1b5a484 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cfc93b154ba010abd7b33494ccd60029 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1533f80eeafef52f89330efe764ed921 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=12f6acc1a4312b193baaf31a1698cee8 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8a9ee9cb47064620821294b0c82fd031 2500w" />
</Frame>

### Connect Datafold to CloudWatch

Start by creating a new user to isolate the permissions as much as possible. Go to IAM and create a new user.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=aa54c7573e13e8eaff8e277bd549b692" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=96e5b50dfd4a19ef3d614ea73a18f33a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=21a72f6e384694ff0720c3e79b8d5a0d 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c4c587d5be8b2798703061b4bd6282fd 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fceab1ef25b9cc390873b16a61b4b335 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3ec007a2e3ea3628f010734dae89ee9c 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=eacf5a8a9d312cacbf028d16244c3124 2500w" />
</Frame>

Next, create a new group named `CloudWatchLogsReadOnly` and attach the `CloudWatchLogsReadOnlyAccess` policy to it. Next, select the group.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=130f10b905ba8f0c7360b671ec6459b1" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=14889ace18815496827c61737f4502e9 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=004bf17bb2b50ed79e38922b010171fd 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=94a4957af7561fe701efe0b1ca0628cd 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7765c8d5939dcead840e602494e5ea2e 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=58e3d859eea26a6a22d162c4117476c1 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=06db75d6ad2b1ef631329ac4ebce8eed 2500w" />
</Frame>

When reviewing the user, it should have the freshly created group attached to it.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6f96f214f462c92d2304250cad4c11e5" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=07ee7e456f35447302edcd92861c9175 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=19abeb9bebff8315c7e66b8dedc598f1 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=408286dc865ce8808d5b91cec556a3ea 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2a056ee5a24578d14afd3fcce43e1f81 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ab153ddbf6bd25f4e3b06d134247e960 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=adee5a0232d4f6a4c27a41602d6f11b7 2500w" />
</Frame>

After confirming the new user you should be given the `Access Key` and `Secret Key`. Save these two codes securely to finish configurations on Datafold.

The last piece of information Datafold needs is the CloudWatch Log Group. You will find this in CloudWatch under the Log Group section in the sidebar. It will be formatted as `/aws/rds/cluster/<my_cluster_name>/postgresql`.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0178488e4be5c0b38a28d569bf0d799f" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7ef3458807c7936a1cbbdf293c4ce462 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d82747cd6550946fcb86d0f0f03373cc 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f60eafe13510cae11665893aca6b32a8 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=219611a2a8db03a439b44921dc5e6b61 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=17536d004b1d58015cb6a7c9899967fd 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=54ef54cd781e6b548f4e2f4026065b4c 2500w" />
</Frame>

### Configure in Datafold

| Field Name                    | Description                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Name                          | A name given to the data connection within Datafold                                                                                     |
| Host                          | The hostname address for your database; default value 127.0.0.1                                                                         |
| Port                          | Postgres connection port; default value is 5432                                                                                         |
| User                          | The user role created in the SQL script; datafold                                                                                       |
| Password                      | The password created in the SQL permissions script                                                                                      |
| Database Name                 | The name of the Postgres database you want to connect to                                                                                |
| AWS Access Key                | The Access Key provided in the [Connect Datafold to CloudWatch](/integrations/databases/postgresql#connect-datafold-to-cloudwatch) step |
| AWS Secret                    | The Secret Key provided in the [Connect Datafold to CloudWatch](/integrations/databases/postgresql#connect-datafold-to-cloudwatch) step |
| Cloudwatch Postgres Log Group | The path of the Log Group; formatted as /aws/rds/cluster/\<my\_cluster\_name>/postgresql                                                |
| Schema for temporary tables   | The schema created in the SQL setup script; datafold\_tmp                                                                               |

Click **Create**. Your data connection is ready!


# Redshift
Source: https://docs.datafold.com/integrations/databases/redshift



**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/redshift#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/redshift#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Amazon Redshift, you must create a user with the following permissions:

* **Read-only access** to all tables in all schemas
* **Write access** to a dedicated temporary schema for Datafold
* **Access to SQL logs** for lineage construction

Datafold uses a temporary dataset to materialize scratch work and keep data processing in the your warehouse. Create the schema with:

```
CREATE SCHEMA datafold_tmp;
```

Next, create the Datafold user. To grant read access to all schemas, the user must have superuser-level privileges in Redshift:

```
CREATE USER datafold CREATEUSER PASSWORD 'SOMESECUREPASSWORD';
```

Grant unrestricted access to system logs so Datafold can build column-level lineage:

```
ALTER USER datafold WITH SYSLOG ACCESS UNRESTRICTED;
```

<Note>Datafold utilizes a temporary schema, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in your warehouse.</Note>

## Configure in Datafold

| Field Name                  | Description                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold                                                                                                 |
| Host                        | The hostname of your cluster. (Go to Redshift in your AWS console, select your cluster, the hostname is the endpoint listed at the top of the page) |
| Port                        | Redshift connection port; default value is 5439                                                                                                     |
| User                        | The user created in our SQL script, named `datafold`                                                                                                |
| Password                    | The password created in our SQL script                                                                                                              |
| Database Name               | The name of the Redshift database you want to connect to                                                                                            |
| Schema for temporary tables | The schema (`datafold_tmp`) created in our SQL script                                                                                               |

Click **Create**. Your data connection is ready!


# SAP HANA
Source: https://docs.datafold.com/integrations/databases/sap-hana



<Note>
  **INFO**

  Column-level Lineage is not currently supported for SAP HANA.
</Note>

**Steps to complete:**

1. [Create and authorize a user](#create-and-authorize-a-user)
2. [Create schema for Datafold](#create-schema-for-datafold)
3. [Configure in Datafold](#configure-in-datafold)

## Create and authorize a user

Create a new user `DATAFOLD` using SAP HANA Administration console (Systems-Security-Users). Specify password authentication, and set "Force password change on next logon" to "No". Grant MONITORING privileges for the databases to be diffed.

## Create schema for Datafold

Datafold utilizes a temporary schema to materialize scratch work and keep data processing in the your warehouse.

```
CREATE SCHEMA datafold_tmp OWNED BY DATAFOLD;

```

## Configure in Datafold

| Field Name                  | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold. |
| Host                        | The hostname address for your database.              |
| Port                        | Sap HANA connection port; default value is 443.      |
| User                        | The user created above, named DATAFOLD.              |
| Password                    | The password for user DATAFOLD.                      |
| Schema for temporary tables | The schema created above, named datafold\_tmp        |

Click **Create**. Your data connection is ready!


# Snowflake
Source: https://docs.datafold.com/integrations/databases/snowflake



**NOTE**: Datafold needs permissions in your Snowflake dataset to read your table data. You will need to be a Snowflake *Admin* in order to grant the required permissions.

**Steps to complete:**

* [Create a user and role for Datafold](/integrations/databases/snowflake#create-a-user-and-role-for-datafold)
* [Setup password-based](/integrations/databases/snowflake#set-up-password-based-authentication) or [Use key-pair authentication](/integrations/databases/snowflake#use-key-pair-authentication)
* [Create a temporary schema](/integrations/databases/snowflake#create-schema-for-datafold)
* [Give the Datafold role access to your warehouse](/integrations/databases/snowflake#give-the-datafold-role-access)
* [Configure your data connection in Datafold](/integrations/databases/snowflake#configure-in-datafold)

## Create a user and role for Datafold

> A [full script](/integrations/databases/snowflake#full-script) can be found at the bottom of this page.

It is best practice to create a separate role for the Datafold integration (e.g., `DATAFOLDROLE`):

```
CREATE ROLE DATAFOLDROLE;
CREATE USER DATAFOLD DEFAULT_ROLE = "DATAFOLDROLE" MUST_CHANGE_PASSWORD = FALSE;
GRANT ROLE DATAFOLDROLE TO USER DATAFOLD;

```

To provide column-level lineage, Datafold needs to read & parse all SQL statements executed in your Snowflake account:

```
GRANT MONITOR EXECUTION ON ACCOUNT TO ROLE DATAFOLDROLE;
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE DATAFOLDROLE;

```

## Set up password-based authentication

Datafold supports username/password authentication, but also key-pair authentication.

```
ALTER USER DATAFOLD SET PASSWORD = 'SomethingSecret';

```

You can set the username/password in the Datafold web UI.

### Use key-pair authentication

If you would like to use key-pair authentication, go to **Settings** -> **Data Connections** -> **Your Snowflake Connection**, and change Authentication method from **Password** to **Key Pair**.
Generate and Download the Key Pair file, and use the value within the file when running the following command in Snowflake to set the key for this Snowflake role:

```
ALTER USER DATAFOLD SET rsa_public_key='...'

```

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

```
CREATE SCHEMA <database_name>.DATAFOLD_TMP;
GRANT ALL ON SCHEMA <database_name>.DATAFOLD_TMP TO DATAFOLDROLE;

```

## Give the Datafold role access

Datafold will only scan the tables that it has access to. The snippet below will give Datafold read access to a database. If you have more than one database that you want to use in Datafold, rerun the script below for each one.

```Bash  theme={null}
/* Repeat for every DATABASE to be usable in Datafold. This allows Datafold to
correctly discover, profile & diff each table */
GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT USAGE ON ALL SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT ALL PRIVILEGES ON ALL DYNAMIC TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE DYNAMIC TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

```

## Full Script

```Bash  theme={null}
--Step 1: Create a user and role for Datafold
CREATE ROLE DATAFOLDROLE;
CREATE USER DATAFOLD DEFAULT_ROLE = "DATAFOLDROLE" MUST_CHANGE_PASSWORD = FALSE;
GRANT ROLE DATAFOLDROLE TO USER DATAFOLD;

GRANT MONITOR EXECUTION ON ACCOUNT TO ROLE DATAFOLDROLE;
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE DATAFOLDROLE;

--Step 2a: Use password-based authentication
ALTER USER DATAFOLD SET PASSWORD = 'SomethingSecret';
--OR
--Step 2b: Use key-pair authentication
--ALTER USER DATAFOLD SET rsa_public_key='abc..'

--Step 3: Create schema for Datafold
CREATE SCHEMA <database_name>.DATAFOLD_TMP;
GRANT ALL ON SCHEMA <database_name>.DATAFOLD_TMP TO DATAFOLDROLE;

--Step 4: Give the Datafold role access to your data connection
/*
  Repeat for every DATABASE to be usable in Datafold. This allows Datafold to
  correctly discover, profile & diff each table
*/
GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT USAGE ON ALL SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

```

## Validate Snowflake Grants for Datafold

Run these queries to validate that the grants have been set up correctly:

> Note: More results may be returned than shown in the screenshots below if you have granted access to multiple roles/users

Example Placeholders:

* `<database_name>` = `DEV`
* `<warehouse_name>` = `DEMO`

```
-- Validate database usage for the DATAFOLDROLE
SHOW GRANTS ON DATABASE <database_name>;
```

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=242ae31d65b18810648b26d7124c8161" data-og-width="1634" width="1634" data-og-height="167" height="167" data-path="images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a8b95f3f0969bb3eb017d9aa87cb1a7c 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bce109e8aa6bb78f4f7b89acdf376e92 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a4b3404e2b21c32411676d7a7844f7d0 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2e768bab9f7a701c32495dec981919d8 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=54c6fdeb3e359eefcdfec99a0f78a7cc 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ea23f295a92e29580646b27723c97505 2500w" />
</Frame>

```
-- Validate warehouse usage for the DATAFOLDROLE
SHOW GRANTS ON WAREHOUSE <warehouse_name>;
```

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5e98412c95861ed744dcfd60275a5b6d" data-og-width="1643" width="1643" data-og-height="170" height="170" data-path="images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=caafcc40d0f21ad5a07865393981d714 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7497892f736cefbe3a09d9988ebdb464 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6c242b835643e7e112a27da7d9d29f51 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=08e81bfd1b66ee1aec62e851b6a3ed66 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=974ef96a9e48f1f8aeb443d6736834e4 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6da58b89ba217cccb3531a0363eb008c 2500w" />
</Frame>

```
-- Validate schema permissions for the DATAFOLDROLE
SHOW GRANTS ON SCHEMA <database_name>.DATAFOLD_TMP;
```

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5513f6f7210fcf3ead5b3c2049da36a4" data-og-width="1644" width="1644" data-og-height="926" height="926" data-path="images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4e1ad627c40506aeaf0d7d6a38ac8171 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=29b4e004070780f24db2d9ee7e5f943d 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4fc4fb151564fdaaa2dd278006281aa8 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9aba8c9f8c64bc46333c503056b61bcf 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1e8222b8cf320c449c77287e97f1b1bc 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8b6ab2cf2fe70c524d2e38e04b00ed6e 2500w" />
</Frame>

## A note on future grants

The above database grants will be insufficient if any future grants have been defined at the schema level, because [schema-level grants will override database-level grants](https://docs.snowflake.com/en/sql-reference/sql/grant-privilege#considerations). In that case, you will need to execute future grants for every existing *schema* that Datafold will operate on.

```Bash  theme={null}
GRANT SELECT ON FUTURE TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE MATERIALIZED VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON ALL TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON ALL VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON ALL MATERIALIZED VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;

```

## Configure in Datafold

| Field Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold                                                                                                                                                                                                                                                                                                                                          |
| Account identifier          | The Org name-Account name pair for your Snowflake account. This can be found in the browser address string. It may look like [https://orgname-accountname.snowflakecomputing.com](https://orgname-accountname.snowflakecomputing.com) or [https://app.snowflake.com/orgname/accountname](https://app.snowflake.com/orgname/accountname). In the setup form, enter \<orgname>-\<accountname>. |
| User                        | The username set in the [Setup password-based](/integrations/databases/snowflake#set-up-password-based-authentication) authentication section                                                                                                                                                                                                                                                |
| Password                    | The password set in the [Setup password-based](/integrations/databases/snowflake#set-up-password-based-authentication) authentication section                                                                                                                                                                                                                                                |
| Key Pair file               | The key file generated in the [Use key-pair authentication](/integrations/databases/snowflake#use-key-pair-authentication) section                                                                                                                                                                                                                                                           |
| Warehouse                   | The Snowflake warehouse name                                                                                                                                                                                                                                                                                                                                                                 |
| Schema for temporary tables | The schema name you created with our script (\<database\_name>.DATAFOLD\_TMP)                                                                                                                                                                                                                                                                                                                |
| Role                        | The role you created for Datafold (Typically DATAFOLDROLE)                                                                                                                                                                                                                                                                                                                                   |
| Default DB                  | A database the role above can access. If more than one database was added, whichever you prefer to be the default                                                                                                                                                                                                                                                                            |

> Note: Please review the documentation for the account name. Datafold uses Format 1 (Preferred): [https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier)

Click **Create**. Your data connection is ready!


# Microsoft SQL Server
Source: https://docs.datafold.com/integrations/databases/sql-server



<Note>
  **INFO**

  Column-level Lineage is not currently supported for Microsoft SQL Server.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/sql-server#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/sql-server#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Microsoft SQL Server, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific temp schema:

```Bash  theme={null}
/* Select the database that will contain the temp schema */
USE DatabaseName;

/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse. */
CREATE SCHEMA datafold_tmp;

/* Create the Datafold user */
CREATE LOGIN DatafoldUser WITH PASSWORD = 'SOMESECUREPASSWORD';
CREATE USER DatafoldUser FOR LOGIN DatafoldUser;

/* Grant read access to diff tables */
GRANT SELECT ON SCHEMA::YourSchema TO DatafoldUser;

/* Grant read + write access to datafold_tmp schema */
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::datafold_tmp TO DatafoldUser;
```

## Configure in Datafold

| Field Name                   | Description                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Connection name              | A name given to the data connection within Datafold                                                              |
| Host                         | The hostname for your SQL Server instance                                                                        |
| Port                         | SQL Server connection port; default value is 1433                                                                |
| Username                     | The user created in our SQL script, named DatafoldUser                                                           |
| Password                     | The password created in our SQL script                                                                           |
| Database                     | The name of the SQL Server database you want to connect to                                                       |
| Dataset for temporary tables | The schema created in our SQL script, in database.schema format: DatabaseName.datafold\_tmp in our script above. |

Click **Create**. Your data connection is ready!


# Starburst
Source: https://docs.datafold.com/integrations/databases/starburst



<Note>
  **INFO**

  Column-level Lineage is not currently supported for Starburst.
</Note>

**Steps to complete:**

1. [Configure user in Starburst](#configure-user-in-starburst)
2. [Create schema for Datafold](#create-schema-for-datafold)
3. [Configure your data connection in Datafold](#configure-in-datafold)

## Configure user in Starburst

To connect to Starburst, create a user with read-only access to all data sources you wish to diff and optionally generate an access token. Datafold requires a schema to be set up within one of the catalogs, typically hosted on platforms like Amazon S3 or similar services.

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                                                                          |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Connection name             | A name given to the data connection within Datafold.                                                                 |
| Host                        | The hostname for your Starburst instance (e.g., `sample-free-cluster.trino.galaxy.starburst.io` for Starburst SaaS). |
| Port                        | Starburst endpoint port; default value is 433.                                                                       |
| Encryption                  | Should be checked for Starburst Galaxy, possibly unchecked for local deployments.                                    |
| User ID                     | User ID as created in Starburst, typically an email address.                                                         |
| Token                       | Access token generated in Starburst.                                                                                 |
| Password                    | Alternatively, provide a password.                                                                                   |
| Schema for temporary tables | Use `<catalog>.<schema>` format.                                                                                     |

Click **Create**. Your data source is now ready!


# Teradata
Source: https://docs.datafold.com/integrations/databases/teradata



<Note>
  **INFO**

  Column-level Lineage is not currently supported for Teradata.
</Note>

**Steps to complete:**

1. [Configure user in Teradata](#configure-user-in-tedadata)
2. [Create a temporary database for Datafold](#create-a-temporary-database-for-datafold)
3. [Configure data connection in Datafold](#configure-in-datafold)

## Configure user in Teradata

To connect to Teradata, create a user with read-only access to all databases you may wish to diff, including the login database:

```
CREATE USER DATAFOLD AS PERMANENT=1000000000 BYTES PASSWORD= <PASSWORD> COLLATION = ASCII TIME ZONE ='GMT';
GRANT EXECUTE FUNTION ON DB1 TO DATAFOLD;
GRANT SELECT ON DB1 TO DATAFOLD;
...
GRANT SELECT ON DB9 TO DATAFOLD;
```

## Create a temporary database for Datafold

Datafold requires a database to store temporary data with full permissions:

```
CREATE DATABASE DATAFOLD_TMP AS PERMANENT=10000000000 BYTES;
GRANT ALL ON DATAFOLD_TMP TO DATAFOLD;
```

## Configure data connection in Datafold

| Field Name                    | Description                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Connection Name               | A name given to the data connection within Datafold.                                                                       |
| Host                          | The hostname for your Teradata instance (e.g., account-name-2e3ba8b32qac9d.env.clearscape.teradata.com for Teradata SaaS). |
| Port                          | Teradata endpoint port; the default value is 1025.                                                                         |
| User ID                       | User ID, e.g., DATAFOLD.                                                                                                   |
| Password                      | Password from above.                                                                                                       |
| Database                      | The connection database, e.g., DB1 from above.                                                                             |
| Database for Temporary Tables | The temporary database, e.g., DATAFOLD\_TMP from above.                                                                    |

Click **Create**. Your data connection is now ready!


# Trino
Source: https://docs.datafold.com/integrations/databases/trino



<Note>
  **INFO**

  Lineage is not currently supported for Trino.
</Note>

**Steps to complete:**

1. [Configure user in Trino](#configure-user-in-trino)
2. [Create schema for Datafold](#create-schema-for-datafold)
3. [Configure your data connection in Datafold](#configure-in-datafold)

## Configure user in Trino

To connect to Trino, create a user with read-only access to all data sources you wish to diff. Datafold also requires a schema set up with read/write permissions within one of the catalogs.

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| Connection name             | A name given to the data connection within Datafold.         |
| Host                        | The hostname for your trino instance.                        |
| Port                        | Trino endpoint port; default value is 443.                   |
| Encryption                  | Should be checked, possibly unchecked for local deployments. |
| User ID                     | User ID as created in Trino.                                 |
| Password                    | Password, as created in Trino.                               |
| Schema for temporary tables | Use `<catalog>.<schema>` format.                             |

Click **Create**. Your data source is now ready!


# OpenText Analytics Database (Vertica)
Source: https://docs.datafold.com/integrations/databases/vertica



<Note>
  **INFO**

  Column-level Lineage is not supported for Vertica.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/vertica#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/vertica#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Vertica, you need to create a user with read-only access to all tables in all schemas, write access to Datafold-specific schema for temporary tables:

```Bash  theme={null}
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in your warehouse. */

CREATE SCHEMA datafold_tmp;

/* Create a datafold user */

CREATE ROLE datafold WITH LOGIN ENCRYPTED PASSWORD 'SOMESECUREPASSWORD';

/* Give the datafold role write access to the temporary schema */

GRANT ALL ON SCHEMA datafold_tmp TO datafold;

/* Make sure that the user has read permissions on the tables */

GRANT USAGE ON SCHEMA <myschema> TO datafold;
GRANT SELECT ON ALL TABLES IN SCHEMA <myschema> TO datafold;

```

Datafold utilizes a temporary schema, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

### Configure in Datafold

| Field Name    | Description                                                               |
| ------------- | ------------------------------------------------------------------------- |
| Name          | A name given to the data connection within Datafold                       |
| Host          | The hostname address for your database; default value 127.0.0.1           |
| Port          | Vertica connection port; default value is 5433                            |
| User          | The user role created in the SQL script; datafold                         |
| Password      | The password created in the SQL permissions script                        |
| Database Name | The name of the Vertica database you want to connect to, default is VMart |

Click **Create**. Your data connection is ready!


# Microsoft Teams
Source: https://docs.datafold.com/integrations/notifications/microsoft-teams

Receive notifications for monitors in Microsoft Teams.

## Prerequisites

* Microsoft Teams admin access or permissions to manage integrations
* A Datafold account with admin privileges

## Configure the Integration

1. In Datafold, go to Settings > Integrations > Notifications
2. Click "Add New Integration"
3. Select "Microsoft Teams"
4. You'll be automatically redirected to the Microsoft Office login page
5. Sign in using the Microsoft Office account with admin privileges
6. Click "Accept" to grant Datafold the necessary permissions
7. You'll be redirected back to Datafold
8. Open the Teams app in a separate browser tab
9. Next to the channel where you'd like to receive notifications, click "..." and select "Workflows"
10. Select the template called "Post to a channel when a webhook request is received"
11. Advance through the wizard (the defaults should be fine)
12. At the end of the wizard, copy the webhook URL
13. Return to Datafold and click "Add channel configuration"
14. Select the relevant Team and Channel, then paste the webhook URL
15. Repeat steps 8-14 for as many channels as you'd like
16. Save the integration settings in Datafold

You're all set! When you configure a monitor in Datafold, you'll now have the option to send notifications to the Teams channel(s) you configured.

## Monitors as Code Configuration

If you're using [monitors as code](/data-monitoring/monitors-as-code), you can configure Teams notifications by adding a `notifications` section to your monitor definition as follows:

```yaml  theme={null}
monitors:
  <monitor_name>:
    ...
    notifications:
      - type: teams
        integration: <integration_id>
        channel: <team_name>:<channel_name>
        mentions:
          - <tag_name>
          - <user_name>
          ...
```

* `<integration_id>` can be found in Datafold -> Settings -> Integrations -> Notifications -> \<your\_ms\_teams\_integration>

#### Full example

```yaml  theme={null}
monitors:
  uniqueness_test_example:
    type: test
    enabled: true
    connection_id: 1123
    test:
      type: unique
      tables:
        - path: DEV.DATA_DEV.USERS
          columns:
            - USERNAME
    schedule:
      interval:
        every: hour
    notifications:
      - type: teams
        integration: 23
        channel: Dev Team:Notifications Channel
        mentions:
          - NotifyDevCustomTag
          - Dima Cherenkov
```

## Need help?

If you have any questions about integrating with Microsoft Teams, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# PagerDuty
Source: https://docs.datafold.com/integrations/notifications/pagerduty

Receive notifications for monitors in PagerDuty.

## Prerequisites

* PagerDuty access with permissions to manage `Services`
* A Datafold account with admin privileges

## Configure the Integration

1. In Datafold, go to Settings > Integrations > Notifications
2. Click "Add New Integration"
3. Select "PagerDuty"
4. Go to the PagerDuty console and [create a new `Service`](https://support.pagerduty.com/main/docs/services-and-integrations#create-a-service)
5. Select `Events API V2` as a service integration
6. Go to your service's `Integrations` page and copy the `Integration Key` (or [generate a new one](https://support.pagerduty.com/main/docs/services-and-integrations#generate-a-new-integration-key))
7. Return to Datafold and provide `Service Name` and `Integration Key`
8. Save the integration settings in Datafold

You're all set! When you configure a monitor in Datafold, you'll now have the option to send notifications to the PagerDuty integration you configured.

## Need help?

If you have any questions about integrating with PagerDuty, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# Slack
Source: https://docs.datafold.com/integrations/notifications/slack

Receive notifications for monitors in Slack.

## Prerequisites

* Slack admin access or permissions to manage integrations
* A Datafold account with admin privileges

## Configure the Integration

1. In Datafold, go to Settings > Integrations > Notifications
2. Click "Add New Integration"
3. Select "Slack"
4. You'll be automatically redirected to Slack
5. If you're not already signed in, sign in to your Slack account
6. Click "Allow" to grant Datafold the necessary permissions
7. You'll be redirected back to Datafold

You're all set! When you configure a monitor in Datafold, you'll now have the option to send notifications to Slack.

## Monitors as Code Configuration

If you're using [monitors as code](/data-monitoring/monitors-as-code), you can configure Slack notifications by adding a `notifications` section to your monitor definition as follows:

```yaml  theme={null}
monitors:
  <monitor_name>:
    ...
    notifications:
      - type: slack
        integration: <integration_id>
        channel: <channel_name>
        mentions:
          - <user_name>
          - here
          - channel
          ...
```

* `<integration_id>` can be found in Datafold -> Settings -> Integrations -> Notifications -> \<your\_slack\_integration>

#### Full example

```yaml  theme={null}
monitors:
  uniqueness_test_example:
    type: test
    enabled: true
    connection_id: 1123
    test:
      type: unique
      tables:
        - path: DEV.DATA_DEV.USERS
          columns:
            - USERNAME
    schedule:
      interval:
        every: hour
    notifications:
      - type: slack
        integration: 13
        channel: dev-notifications
        mentions:
          - John Doe
          - channel
```

## Need help?

If you have any questions about integrating with Slack, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).


# OAuth Support
Source: https://docs.datafold.com/integrations/oauth

Set up OAuth App Connections in your supported data warehouses to securely execute data diffs on behalf of your users.

<Note>
  This feature is currently supported for Databricks, Snowflake, Redshift, and BigQuery.
</Note>

OAuth support empowers users to run data diffs based on their individual permissions and roles configured within the data warehouses. This ensures that data access is governed by existing security policies and protocols.

## How it works

### 1. Create a Data Diff

When you attempt to run a data diff, you will notice that it won't run without authentication:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cd7e4bebaad25ee87ee8f9af1276b394" data-og-width="1351" width="1351" data-og-height="506" height="506" data-path="images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=195e49c927a5fe592e1b102f2a29b7be 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f0cb562f9843f7ce6dab563e5b59bed0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d02eaac4cdaf17c39ccc1e59e13417dc 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7a2da244a27834108940f1678e31978c 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cdc4d1406b80309fd8b0af97a9e2c49d 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e476b20694e97943353a1137c225ad8f 2500w" />
</Frame>

### 2. Authorize the Data Diff

Authorize the data diff by clicking the **Authenticate** button. This will redirect you to the data warehouse for authentication:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ed69e89b64e6a3d78420304cad83aa56" data-og-width="692" width="692" data-og-height="689" height="689" data-path="images/2-01bbf79b7aaf007bc33dc4652a825e31.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc3033abe34ccb7baae0e1a4275c94d1 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d33a10f83a772a4d80313f38d627a0b0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=14172780ba3b63b6ccbaf4ea6b9b6f03 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c48a994bb8c896960bd3512d88c52048 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0559d8f1be5b5a75fab27b48c0624d2d 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4e3214159c568cf8c5ea1505da0dbdb7 2500w" />
</Frame>

Upon successful authentication, you will be redirected back.

### 3. The Data Diff is now running <Icon icon="party-horn" />

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0cd380754dc3b5894e055590d2638473" data-og-width="1444" width="1444" data-og-height="660" height="660" data-path="images/3-7d49f847dba2d6ebefe0215a7251d3e7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6d875f7e171d67f3b3df4116ba70508d 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e49c8e8d0b648191c88f47526212fb21 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bcd2d270da75b7c4e3b597057a1ed24f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=badcae551df707e90656f61fc1e25eb2 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4ff503167e0ed264596f730d485a3bbc 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8f1948bba26c08ba890505297c338e36 2500w" />
</Frame>

### 4. View the Data Diff results

The results reflect your permissions within the data warehouse:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=897aa005c633ba7fdea578447a97828a" data-og-width="616" width="616" data-og-height="329" height="329" data-path="images/4-1e3cf172b19bd6616700f3c82f17b256.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc7668dbfdeb95b0e6324454303aaeea 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c9b739c02576debd0b5ff99c8e4561dc 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=671d55c6418991662e95fa42fbd67fb8 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e2efd53df3ab32f243b0d3ec6054401e 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=edea40bb30e8b0b022442b10797aea60 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=613e912826a8622e7bc4227bdbd8c0ef 2500w" />
</Frame>

Note that running the same data diff, as a different user, renders different results:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5e89ea4ea01811b1ffcdab58f0c7990e" data-og-width="668" width="668" data-og-height="348" height="348" data-path="images/5-585c0ee49689bb8af229ad44eb260ace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=431e0250ed4b32083ed9c3eebd0bf709 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f8f7871c7a7c078733d187d781ee7dc1 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9f6eebe93cf67954ec76fc73649d111c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e52cfccd6a7532e9f9aa559154b64cc9 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=96039c2a7908da697d0d8e046dabd9cf 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=616915ffae6110716f613cd70d9f6995 2500w" />
</Frame>

The masked values represent the data retrieved from the data warehouse. We do not conduct any post-processing:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3783c5502d8e301edc487ddb2d7fbef3" data-og-width="2019" width="2019" data-og-height="522" height="522" data-path="images/6-f09d99fb5db326846be80a54d24606b0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=898f215c8d9f08234cd03eab7fc97b5b 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d99bce0c4d6369d098264344a65b94ef 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f18094e55a094528dbbb1a8e61b2f10b 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=25b02a547eaca94a10e4186325a7b206 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=abd90ef895528566cd7c2cc3446b35c9 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2f91c45870ff384f6046de39f0b55202 2500w" />
</Frame>

By default, results are only visible for their authors. Users can still clone the data diffs, but the results might be different depending on their data warehouse access levels.

For example, as a different user, I won't be able to access the data diff results for Filip's data diff:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=abbc65d13fd6f9fd766ae84fb815d9b1" data-og-width="1253" width="1253" data-og-height="526" height="526" data-path="images/7-0e23da80a3e63960a91301cdf38d8207.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0378959d5f546b39a207f8f024a24074 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d24b78901f302d1da0b8a4d7896247a1 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=91a5499844c9e2099ff8f9a422d6bba4 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c4c591f7d274d17ab4f32e296a091e7c 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=aea6ad16c4fa9c52f362d83ef0ca4b08 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4853922ce3561089f308e9a890d4df6a 2500w" />
</Frame>

### 5. Sharing Data Diffs

Data diff sharing is a feature that enables you to share data diffs with other users. This is useful in scenarios such as compliance verification, where auditors can access specific data diffs without first requiring permissions to be set up in the data warehouse.

Sharing can be accessed via the **Actions** dropdown on the data diff page:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=789165034442807be5003399934f40f7" data-og-width="379" width="379" data-og-height="356" height="356" data-path="images/1-2f00e7c34ec87bada9d464dcb97053df.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1c47a66df147dae821908122196e1b8c 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3d465a16f8a27bbc4b5265efc71ac3e4 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5bf23de8a42cefdfae16c515b15dfdf1 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ff9442ca8ad8369bba31d0553f45f74b 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=afde9ca1305e4527f972cef28244d84c 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=47d15d0d6d5532f6ac22c76e1880844e 2500w" />
</Frame>

Note that data diff sharing is disabled by default:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ebfb0bfc01a1ced78c489906b41354fc" data-og-width="693" width="693" data-og-height="329" height="329" data-path="images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=327942722007ab9d72a72e26c4ef4972 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f3e66b6655803bb6820ced0d5b9c9fbc 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8462a78617cc020dd74b34f5d90a6e96 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5decc53f6eaaaa66a560412009e69a5c 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=70d95b33939cecbcd4b2262afd528914 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ae3ce479550c239cb9a85fe3c697cb2f 2500w" />
</Frame>

It can be enabled under **Org Settings** by clicking on **Allow Data Diff sharing**:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bc1bf09028d88aa65d3a3ce75508810f" data-og-width="1154" width="1154" data-og-height="422" height="422" data-path="images/3-889664da5c85c56985659d0c9e675340.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=85a09f0a67c449242acbdf091905b5a7 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a2f515b93844dd745b05a6363f017209 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5f138b74c733b74d576673be4b1e314c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9c18444a04effb2a40ca19c9c83d4125 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6b20db867e2b9f9f6f1971a4b41e9f75 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a46ab3bc37c9301847e3b235017da8aa 2500w" />
</Frame>

Once enabled, you can share data diffs with other users:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=12830c2279779e7344273e1b9ce72aab" data-og-width="913" width="913" data-og-height="774" height="774" data-path="images/4-58827ded9574bddc7ef7ce0d4f156bf8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d74d11242338eeee30293c968916c526 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d37928e13b15fa8ffc1602edeb9ae532 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5232f81d8a7dc8ec0d6e96188902d003 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c532fa8733fd87c2f04e6cd3b3a484e9 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0f4e85b16c10c2ffb857567661da38cd 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a7527c6188f94bb08df9704e036aaccc 2500w" />
</Frame>

## Configuring OAuth

Navigate to **Settings** and click on your data connection. Then, click on **Advanced settings** and under **OAuth**, set the **Client Id** and **Client Secret** fields:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=483e82a0cfd9eb259f7423eb1ff97498" data-og-width="1639" width="1639" data-og-height="623" height="623" data-path="images/1-6541ee9948bb173fe28a64cb72b7ba8d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=408053f47c35658e971dda9d833c69b6 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=15bb1af0700abb2cb4deb39481091c77 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8824e49c7507464fc9b7dbf5303d7d27 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e7cba352e262d8d64812aeb3e9f9d294 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=693f103e21314927d4d68169bde97d19 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2805e57d72531297123e2b9e5e6aea28 2500w" />
</Frame>

## Example: Databricks

To create a new Databricks app connection:

1. Go to **Settings** and **App connections**.
2. Click **Add connection** in the top right of the screen.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a69989f57df0f8720e00a76f98816b38" data-og-width="714" width="714" data-og-height="835" height="835" data-path="images/2-f59b84118a8979128d2476989b4f5262.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d4f2ea05d78059e3a3300a763969df76 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d2c8eb7c9d29ba6945e1416ea48f10f5 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5d148bb26eb06c028c864464184f20ae 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6e8adc1d158298733ba2e415a4a5ac52 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8568eb3d1032c28650f861d84cd1a244 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2d260e633142df1e9fe7f8baeea766d8 2500w" />
</Frame>

3. Fill in the required fields:

Application Name:

```
Datafold OAuth connection
```

Redirect URLs:

```
https://app.datafold.com/api/internal/oauth_dwh/callback
```

<Note>
  **INFO**

  Datafold caches **access tokens** and using **refresh tokens** fetches new valid tokens in order to complete the diffs and reduce the number of times users need to authenticate against the data warehouses.

  One hour is sufficient for the access token.

  The refresh token will determine the frequency of user reauthentication, whether it's daily, weekly, or monthly.
</Note>

### 3. Click **Add** to obtain the **Client ID** and **Client Secret** <Icon icon="hand-sparkles" />

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=589b0cf2f42d86c1ec263cc47fb33365" data-og-width="628" width="628" data-og-height="391" height="391" data-path="images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=788520c072a39c4b79e5f9f445318717 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1b6edd2eba304c11f6f6137ed63c222f 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=32c72eaaf56e232a33466419557c0deb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=628e6af54f7d45d902d37367e5894e6a 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b5e1ed3327453efe695e140c4e25a4d2 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d48001fa82d678b45d86d1a32c8b9c2e 2500w" />
</Frame>

### 4. Fill in the **Client ID** and **Client Secret** fields in Datafold's Data Connection advanced settings:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=52b22b3c356fb6b6d7e4a905687d2715" data-og-width="1584" width="1584" data-og-height="338" height="338" data-path="images/4-75640ad5d18710fced1d22c108bbd0c9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d4a4a92da61693b411ef9a6f0c8d72fc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=460a00a3e82040db37043021196ff93d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e5e4d08f2c193f8757110771197341c6 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f8d16340673a6cae96b9c1004a113741 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1222e977e30b8fdf9ab67cb3db8e5ffe 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=02ced3c862f91a53fd7a982f2f820216 2500w" />
</Frame>

### 5. Click **Test and save OAuth**

You will be redirected to Databricks to complete authentication. If you are already authenticated, you will be redirected back.

This notification signals a successful OAuth configuration:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=821eded0675f2c3319efee82e368caed" data-og-width="1647" width="1647" data-og-height="1284" height="1284" data-path="images/5-63f6c2f97041e030191e9abc5ca70637.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ec404016b242bc7beb77b9b4ba87a4dc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=166115bb5eddaa0dbb2d647224c70cfd 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7637451d19df712e3ea3eaf27b6a37cb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e067e3595978265bb27f425993f1c25 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c0c30eff5a3404e582c8539b19ead006 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=df269d44e95b405748512cfa1198c32d 2500w" />
</Frame>

### Additional steps for Databricks

To ensure that users have correct access rights to temporary tables (stored in **Dataset for temporary tables** provided in the **Basic settings** for the Databricks connection), follow these steps:

1. Update the permissions for the **Dataset for temporary tables** in Databricks.
2. Grant these permissions to Datafold users: **USE SCHEMA** and **CREATE TABLE**.

This will ensure that materialization results from data diffs are only readable by their authors.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6a231a976529a7d6fbfdfa11e9638197" data-og-width="1138" width="1138" data-og-height="1239" height="1239" data-path="images/6-c4186dd5e91cd8aabf283649efe7461e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1c55ec5ab9301d127e478adc3d818454 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a52216ec9ffb28ae8230685bac7b22f2 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4cf511433f16971d49d64a3b3241d8a9 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e8aee9090c7cf5302d325d269173bcf8 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=483d6c66c63e65d6f64e8c31acf20275 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9631df3758a018a8bf371883486e7edf 2500w" />
</Frame>

## Example: Snowflake

To create a new Snowflake app connection:

1. Go to Snowflake and run this SQL:

```Bash  theme={null}
CREATE SECURITY INTEGRATION DATAFOLD_OAUTH
TYPE = OAUTH
ENABLED = TRUE
OAUTH_CLIENT = CUSTOM
OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
OAUTH_REDIRECT_URI = 'https://app.datafold.com/api/internal/oauth_dwh/callback'
PRE_AUTHORIZED_ROLES_LIST=(<ROLENAME1>, <ROLENAME2>, ...)
OAUTH_ISSUE_REFRESH_TOKENS = TRUE
OAUTH_REFRESH_TOKEN_VALIDITY = 604800
OAUTH_ENFORCE_PKCE=TRUE;
```

It should result in this message:

<Warning>
  **CAUTION**

  * `PRE_AUTHORIZED_ROLES_LIST` must include all roles allowed to use the current security integration.
  * By default, `ACCOUNTADMIN`, `SECURITYADMIN`, and `ORGADMIN` are not allowed to be included in `PRE_AUTHORIZED_ROLES_LIST`.
</Warning>

<Note>
  **INFO**

  Datafold caches **access tokens** and uses **refresh tokens** to fetch new valid tokens in order to complete the diffs and reduce the number of times users need to authenticate against the data warehouses.

  `OAUTH_REFRESH_TOKEN_VALIDITY` can be in the range of 3600 (1 hour) to 7776000 (90 days).
</Note>

1. To retrieve `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`, run the following SQL:

```
select system$show_oauth_client_secrets('DATAFOLD_OAUTH');
```

### Example result:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ce9a57e787e1d1a98b9cb10bc77cc2be" data-og-width="1471" width="1471" data-og-height="71" height="71" data-path="images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e967abadcafc11c197a5581463da69dd 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=11553ac290971c5a55596b0335f2c76d 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7ad4f68ee71fecd7f62edd169c77d2c3 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=57586b5686ef991a592b731b92714ac2 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1775b83d05ba34fab6b6731375ec405e 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c90744de328ea48873a9eebe68c44000 2500w" />
</Frame>

1. Fill in the **Client ID** and **Client Secret** fields in Datafold's Data Connection advanced settings:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=52b22b3c356fb6b6d7e4a905687d2715" data-og-width="1584" width="1584" data-og-height="338" height="338" data-path="images/4-75640ad5d18710fced1d22c108bbd0c9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d4a4a92da61693b411ef9a6f0c8d72fc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=460a00a3e82040db37043021196ff93d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e5e4d08f2c193f8757110771197341c6 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f8d16340673a6cae96b9c1004a113741 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1222e977e30b8fdf9ab67cb3db8e5ffe 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=02ced3c862f91a53fd7a982f2f820216 2500w" />
</Frame>

2. Click **Test and save OAuth**

You will be redirected to Snowflake to complete authentication.

info

Your default Snowflake role will be used for the generated **access token**.

This notification signals a successful OAuth configuration:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=821eded0675f2c3319efee82e368caed" data-og-width="1647" width="1647" data-og-height="1284" height="1284" data-path="images/5-63f6c2f97041e030191e9abc5ca70637.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ec404016b242bc7beb77b9b4ba87a4dc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=166115bb5eddaa0dbb2d647224c70cfd 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7637451d19df712e3ea3eaf27b6a37cb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e067e3595978265bb27f425993f1c25 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c0c30eff5a3404e582c8539b19ead006 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=df269d44e95b405748512cfa1198c32d 2500w" />
</Frame>

### Additional steps for Snowflake

To guarantee correct access rights to temporary tables (stored in **Dataset for temporary tables** provided in the **Basic settings** for Snowflake connection):

* Grant the required privileges on the database and `TEMP` schema for all roles that will be using the OAuth flow. This must be done for all roles that will be utilizing the OAuth flow.

```Bash  theme={null}
GRANT USAGE ON WAREHOUSE <WH_NAME> TO ROLE <ROLENAME>;
GRANT USAGE ON DATABASE <DB_NAME> TO ROLE <ROLENAME>;
GRANT USAGE ON ALL SCHEMAS IN DATABASE <DB_NAME> TO ROLE <ROLENAME>;
GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <DB_NAME> TO ROLE <ROLENAME>;
GRANT ALL ON SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> TO ROLE <ROLENAME>;
```

* Revoke `SELECT` privileges for tables in the `TEMP` schema for all roles that will be using the OAuth flow (except for the `DATAFOLDROLE` role), if they were provided. This action must be performed for all roles utilizing the OAuth flow\..

```Bash  theme={null}
-- Revoke SELECT privileges for the TEMP SCHEMA
revoke SELECT ON ALL TABLES IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE TABLES IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL MATERIALIZED VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE MATERIALIZED VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
-- Revoke SELECT privileges for a Database
revoke SELECT ON ALL TABLES IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE TABLES IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL MATERIALIZED VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE MATERIALIZED VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
```

<Warning>
  **CAUTION**

  If one of the roles will have `FUTURE GRANTS` at the database level, this role will also will have `FUTURE GRANTS` on the `TEMP` schema.
</Warning>

## Example: Redshift

Redshift does not support OAuth2. To execute data diffs on behalf of a specific user, that user needs to provide their own credentials to Redshift.

1. Configure permissions on the Redshift side. Grant the necessary access rights to temporary tables (stored in the **Dataset for temporary tables** provided in the **Basic settings** for Redshift connection):

```Bash  theme={null}
GRANT USAGE on SCHEMA <TEMP_SCHEMA_NAME> to <USERNAME>;
GRANT CREATE on SCHEMA <TEMP_SCHEMA_NAME> to <USERNAME>;
```

1. As an Administrator, select the **Enabled** toggle in Datafold's Redshift Data Connection **Advanced settings**:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1225a8001fa74dbeeead41b1675b2af1" data-og-width="573" width="573" data-og-height="357" height="357" data-path="images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fb743cd936ef569429288dc7f9783463 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6903a604b069ec8507e82d18c0c3abe8 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b88989e4cae2f4dc098776904f830144 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0259bf2891b63e2b6d5df436dfa9fae9 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2e2eb149539e059e5a34c186288638db 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4e343749a80f2d5a4fbf8c5caadec60f 2500w" />
</Frame>

Then, click the **Test and Save** button.

1. As a User, add your Redshift credentials into Datafold. Click on your Datafold username to **Edit Profile**:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=94bb0a38ce1502c37884fbfdcce735b4" data-og-width="428" width="428" data-og-height="276" height="276" data-path="images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=11b8e43702d1bd72c843979730163c74 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f94d7f62dbf31b31730c8cb8b2697317 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b3226c0af0dd1340fa57135097e75679 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ea6b6fe0b6d2740fff30c9a44d3b2e51 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7d91a7ddf0d2b3394b12aa06ea363296 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4b343c2b6e1ec13859f0819046a49ec6 2500w" />
</Frame>

Then, click **Add credentials** and select the required Redshift data connection from the **Data Connections** list:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4bd6e92d2df678a8625f8b69be7c4580" data-og-width="533" width="533" data-og-height="365" height="365" data-path="images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dc5a30a103a1ecbad292db61119689ab 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f40447f504254a4ecb3018473e8cf372 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f7fd9cce0fd6316814a34974de843267 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=391c4cbc8e222ac90b219f3a2e0087ce 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fdb5b74a3b8cec8d82f56ceef57d4f97 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=790da9b6820bb16d72ebaeec28c081c3 2500w" />
</Frame>

Finally, provide your Redshift username and password, and configure the **Delete on** field (after this date, your credentials will be removed from Datafold):

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d3f72a0e9d5dabfb88870f81f1e7bdfc" data-og-width="531" width="531" data-og-height="475" height="475" data-path="images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=40b9e30cd983f877c1f3444d2fd8507f 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=04b711aaf0388fdb3eca481dc1d9670e 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93404ca422fb458ccdd2586170ef37c3 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3d0cad66495744e7a99927326cbcd5da 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=df4f8d3c2c4b222165507ff4faf0dd3a 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ca6d4dff56a9f605c93e1db9604b15fe 2500w" />
</Frame>

Click **Create credentials**.

## Example: BigQuery

1. To create a new Google Cloud OAuth 2.0 Client ID, go to the Google Cloud console, navigate to **APIs & Services**, then **Credentials**, and click **+ CREATE CREDENTIALS**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4905913a31f2f328e7a755ac5d09650d" data-og-width="1034" width="1034" data-og-height="304" height="304" data-path="images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f84077faf4c5f9d8a0a0dd793074ab1c 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f471870433e12a1e2b2c0ee329aa3e04 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5af4cee4f923ee74e7454cd4015bee5b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f47c3a4ffb798c56e66dd627559a4fa1 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=64fe7791bddeb58e0e3b1f33d6f651aa 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=496a6fa90f5d61129e2bf2024dc72217 2500w" />
</Frame>

Select **OAuth client ID**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0e709d4a6a5916bf21c6f940553c2a9c" data-og-width="502" width="502" data-og-height="275" height="275" data-path="images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=898c4b21c76bcfa8e5176ca2530f2343 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6b8ad94acd03f8926abc0178d91b8227 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=41e45dec682a86e69e0c04decf3c8b14 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=558b1b690e8969ea444ee02c7a4a897c 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9db85c16d696451c7891343a181fca0d 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=db5c1c7d7e8c78a87b91d8d182936de7 2500w" />
</Frame>

From the list of **Application type**, select **Web application**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c197423a208dc2d144b9dcd2cbc905a9" data-og-width="617" width="617" data-og-height="459" height="459" data-path="images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d7b7aa8076045631f2bed9f8082c48b7 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=aae4f30e3c363dde551fb7bd7b952b68 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=45737eb052d7829449d01573da6e2eb1 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e4e8eab900e3bb47b1a2ab30ce278a67 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=073a9e055566e913b524cfc319eae15c 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=312eedd9efd3adf3467abab254fc53e7 2500w" />
</Frame>

Provide a name in the **Name** field:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d35dc1be31c0bc487576675f6e6d07ea" data-og-width="605" width="605" data-og-height="335" height="335" data-path="images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cdace1632c44a6c2a3e7c94c1edb6743 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2324d310af9db1d69df98251d6b759f7 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=21f44cc1336e67c55309c0fc1154114c 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e8434dd68bf74cdc3f6f523732319ce6 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4a2b937c2579b5676480ab890a3abd72 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e9ddce0aecb9360480f4701926c144f8 2500w" />
</Frame>

In **Authorized redirect URIs**, provide `https://app.datafold.com/api/internal/oauth_dwh/callback`:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6a5dee352c37fa168fa413932070893e" data-og-width="606" width="606" data-og-height="391" height="391" data-path="images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=df5bdb9757734ec9f2703fa7b1557312 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5fdd1e2603724c593b3a749e40a0ca9e 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=48747cd3568ab6de8d6ba6b32495fdd6 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=decdeb4b34ba1cbb86986fe63cbb6a25 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=db48b4fb4904a31499857d8961c53dc4 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3af4afe07a253c2d98a75f20efb1462f 2500w" />
</Frame>

Click **CREATE**. Then, download the OAuth Client credentials as a JSON file:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1d5f2345d0c3b8dae42fd05ff31010a7" data-og-width="959" width="959" data-og-height="157" height="157" data-path="images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=62661927034a0a7190e848eac80a0fda 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f3ff896f467d2eddc5815f1e5db7eb7e 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=81f66feec8f4e354f62496c51b3cf57d 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=33ddf7aef7b4996b1618f2828e7e2b39 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fe6c5ed672f9d69de489c9eebf6cd8b2 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a3fa18761b17014b9284e4986ceed700 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=dce5fb185e1daeccad692b9e2de95ce5" data-og-width="570" width="570" data-og-height="464" height="464" data-path="images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f61119b3df9b48fcdcb6049ef7f73b5c 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4b33ed12674578fd86ab8455cfbfed71 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0756eb523c38eebeced406ab85d6fac2 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a3f9c163ab7ab6f5db00997f846b0be3 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4a45ab9e608dc23a8de2f5f08673dcc5 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1f38bd4ea7b00fbb549ee6bd2c5fa9e4 2500w" />
</Frame>

1. Activate BigQuery OAuth in Datafold by uploading the JSON OAuth credentials in the **JSON OAuth keys file** section, in Datafold's BigQuery Data Connection **Advanced settings**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ec7651764c65ca5944a9fba3ecc7abff" data-og-width="565" width="565" data-og-height="364" height="364" data-path="images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9436aa79fdadce93824eab16119ea947 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3ccbfb449fd888aed90a7d9cc0fbf083 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c935fb29b47c9b401ecc973b8cc63a47 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0ade161dfdf86396751f758cf36ec253 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=50241ab3380af18544eb7adcf9b9a2c9 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=70df8d3ce62aa6ae1285f026246758be 2500w" />
</Frame>

Click **Test and Save**.

### Additional steps for BigQuery

1. Create a new temporary schema (dataset) for each OAuth user.

Go to Google Cloud console, navigate to BigQuery, select your project in BigQuery, and click on **Create dataset**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d96e1d0baa2f541b8982e561ccd7dec0" data-og-width="854" width="854" data-og-height="461" height="461" data-path="images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=88cf832b4449cb152cb26812acea5198 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=231980b9bbbef86b2cccfaa52d2a722d 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e700db87e381d871cb2730bd0d17255b 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=42dbfb7bdad770d3837a7fb6608b976a 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=da30326201a549ab8e6ede307f6f0b0c 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9d1633799da92ff4a2d72919c629c8bb 2500w" />
</Frame>

Provide `datafold_tmp_<username>` as the **Dataset ID** and set the same region as configured for other datasets. Click **CREATE DATASET**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6f5eee9e23b5e0cc17ac5cf4cf3bbfea" data-og-width="600" width="600" data-og-height="717" height="717" data-path="images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=04f480bd675d118869dcdbeb72a2fe80 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5fe7c1fc99db3fe9bf276f7ea7c4af10 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2ce3538d70cf07e4df09d864c7231e5c 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=630de468106efe6f17e0380bc4e5f96f 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8b333589474cbd5a28ee7adb41f41581 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=54acc1cfdb6d8039b7c8a169a22f3e58 2500w" />
</Frame>

1. Configure permissions for `datafold_tmp_<username>`.

Grant read/write/create/delete permissions to the user for their `datafold_tmp_<username>` schema. This can be done by granting roles like **BigQuery Data Editor** or **BigQuery Data Owner** or any custom roles with the required permissions.

Go to Google Cloud console, navigate to BigQuery, select `datafold_tmp_<username>` dataset, and click **Create dataset** → **Manage Permissions**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9989c77e33d9c8d40101e5aac7c2a979" data-og-width="739" width="739" data-og-height="361" height="361" data-path="images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f0b1f01e2b49e73fcb542a1ed7a69aeb 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0a2ba425ab7469349354c9aa984b1804 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e81e037ad7933777de21dad0147e31f3 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=63f72fdf7be3976d4c84a81bb930018d 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9167ba1e691a3657ee37d853b4fddc9e 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9b37b86665feec3ee743aa49de073855 2500w" />
</Frame>

Click **+ ADD PRINCIPAL**, specify the user and role, then click **SAVE**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a3e60b12eaa6d54d9e221013bed04a21" data-og-width="604" width="604" data-og-height="732" height="732" data-path="images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7f1050dc093e9657511d7bf62daf4016 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=32691682ea6ebf87393fb27461736e65 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=23d9328c76f4a7b8caf926d911509a0d 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dce6e5f68c8ad6fcafd51eaa4dbe1895 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4426be737dbe82574a823a6a0cc72025 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=05fc2a428a4afa31225c9afc459f42ca 2500w" />
</Frame>

caution

Ensure that only the specified user (excluding admins) has read/write/create/delete permissions on `datafold_tmp_<username>`.

1. Configure temporary schema in Datafold.

As a user, navigate to `https://app.datafold.com/users/me`. If the user lacks credentials for BigQuery, click on **+ Add credentials**, select BigQuery datasource from the list, and click **Create credentials**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e2622cd1e1be8568cfc8c3c2de089d8f" data-og-width="528" width="528" data-og-height="308" height="308" data-path="images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=56a929eb8b7c869a94460bdb249d78d7 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bd1de29114cc4240425340791a1f2916 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9ee2c65f1dd8ad5256c977966112b2d3 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4524a4c45873f75f4f742b2332a05e3d 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6eaa79c59e13da3bc8a50dcb0c270c80 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6711bc955c5a8ff7885aea5840121027 2500w" />
</Frame>

The user will be redirected to `accounts.google.com` and then returned to the previous page:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ec94dfc0f8a0cad000a4e5ed291d278d" data-og-width="945" width="945" data-og-height="568" height="568" data-path="images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f58954c9249c8d998ea97b2500fed64a 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b9dd1c7d4728b27d2f837ba0302e6000 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8b722f3609424923fa411ef497e72aae 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=89ec8306292fa155aab0924abc201877 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9dd6a09b7ace6eb77195913e500f0b96 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b2322e97a0d94120955d68b7feaecb90 2500w" />
</Frame>

Select BigQuery credentials from the list, input the **Temporary Schema** field in the format `<project>.<datafold_tmp_<username>>`, and click **Update**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8ec2d70ffeee17a7318a66784aca373a" data-og-width="526" width="526" data-og-height="365" height="365" data-path="images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5058d821083509dde08712f76a87bd90 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=419485442d5532209ff26f1fb8b2eaa7 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1d10d6ac876cd7f2c4b115fe4ca1c33d 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=01b731418e545edf5f9d67d2e7243feb 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a01890857e91623ce9a2e6beaff1c190 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=be3ef9191263981497cad5e8ff623cfa 2500w" />
</Frame>

<Note>
  **INFO**

  Users can update BigQuery credentials only if they have the correct permissions for `<datafold_tmp_<username>`.
</Note>


# Integrate with Orchestrators
Source: https://docs.datafold.com/integrations/orchestrators

Integrate Datafold with dbt Core, dbt Cloud, Airflow, or custom orchestrators to streamline your data workflows with automated monitoring, testing, and seamless CI integration.

<Info>
  **NOTE**

  To integrate with dbt, first set up a [Data Connection](/integrations/databases) and integrate with [Code Repositories](/integrations/code-repositories).
  Then navigate to **Settings** → **dbt** and click **Add New Integration**.
</Info>

<CardGroup>
  <Card title="dbt Core" icon="file" href="/integrations/orchestrators/dbt-core" horizontal>
    Set up Datafold with dbt Core to enable automated data diffs and CI/CD integration.
  </Card>

  <Card title="dbt Cloud" icon="file" href="/integrations/orchestrators/dbt-cloud" horizontal>
    Integrate with dbt Cloud to enable automated data diffs and CI/CD integration.
  </Card>

  <Card title="Custom Integrations" icon="file" href="/integrations/orchestrators/custom-integrations" horizontal>
    Use Datafold's API and SDK to build custom CI integrations tailored to your workflow.
  </Card>
</CardGroup>


# Custom Integrations
Source: https://docs.datafold.com/integrations/orchestrators/custom-integrations

Integrate Datafold with your custom orchestration using the Datafold SDK and REST API.

<Info>
  To use the Datafold REST API, you should first create a Datafold API key in Settings > Account.
</Info>

## Install

Then, create your virtual environment for Python:

```
> python3 -m venv venv
> source venv/bin/activate
> pip install --upgrade pip setuptools wheel
```

Now, you're ready to install the Datafold SDK:

```
> pip install datafold-sdk
```

## Configure

Navigate in the Datafold UI to Settings > Integrations > CI. After selecting `datafold-sdk` from the available options, complete configuration with the following information:

| Field Name                               | Description                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Repository                               | Select the repository that generates the webhooks and where pull / merge requests will be raised.                                                                                                                                                                  |
| Data Connection                          | Select the data connection where the code that is changed in the repository will run.                                                                                                                                                                              |
| Name                                     | An identifier used in Datafold to identify this CI configuration.                                                                                                                                                                                                  |
| Files to ignore                          | If defined, the files matching the pattern will be ignored in the PRs. The pattern uses the syntax of .gitignore. Excluded files can be re-included by using the negation; re-included files can be later re-excluded again to narrow down the filter.             |
| Mark the CI check as failed on errors    | If the checkbox is disabled, the errors in the CI runs will be reported back to GitHub/GitLab as successes, to keep the check "green" and not block the PR/MR. By default (enabled), the errors are reported as failures and may prevent PR/MRs from being merged. |
| Require the `datafold` label to start CI | When this is selected, the Datafold CI process will only run when the 'datafold' label has been applied. This label needs to be created manually in GitHub or GitLab and the title or name must match 'datafold' exactly.                                          |
| Sampling tolerance                       | The tolerance to apply in sampling for all data diffs.                                                                                                                                                                                                             |
| Sampling confidence                      | The confidence to apply when sampling.                                                                                                                                                                                                                             |
| Sampling Threshold                       | Sampling will be disabled automatically if tables are smaller than specified threshold. If unspecified, default values will be used depending on the Data Connection type.                                                                                         |

## Add commands to your custom orchestration

```bash  theme={null}
export DATAFOLD_API_KEY=XXXXXXXXX

# only needed if your Datafold app url is not app.datafold.com
export DATAFOLD_HOST=<CUSTOM_DATAFOLD_APP_DOMAIN>
```

To submit diffs for a CI run, replace `ci_config_id`, `pr_num`, and `diffs_file` with the appropriate values for your CI configuration ID, pull request number, and the path to your diffs `JSON` file.

#### CLI

```bash  theme={null}
datafold ci submit \
  --ci-config-id <ci_config_id> \
  --pr-num <pr_num> \
  --diffs <diffs_file> \
```

#### Python

```python  theme={null}
import os

from datafold_sdk.sdk.ci import run_diff

api_key = os.environ.get('DATAFOLD_API_KEY')

# Only needed if your Datafold app URL is not app.datafold.com
host = os.environ.get("DATAFOLD_HOST")

run_diff(host=host,
         api_key=api_key,
         ci_config_id=<ci_config_id>,
         pr_num=<pr_num>,
         diffs='<diffs_file>')
```

##### Example JSON format for diffs file

The `JSON` file should define the production and pull request tables to compare, along with any primary keys and columns to include or exclude in the comparison.

```json  theme={null}
[
  {
    "prod": "YOUR_PROJECT.PRODUCTION_TABLE_A",
    "pr": "YOUR_PROJECT.PR_TABLE_NUM",
    "pk": ["ID"],
    "include_columns": ["Column1", "Column2"],
    "exclude_columns": ["Column3"]
  },
  {
    "prod": "YOUR_PROJECT.PRODUCTION_TABLE_B",
    "pr": "YOUR_PROJECT.PR_TABLE_NUM",
    "pk": ["ID"],
    "include_columns": ["Column1"],
    "exclude_columns": []
  }
]
```


# dbt Cloud
Source: https://docs.datafold.com/integrations/orchestrators/dbt-cloud

Integrate Datafold with dbt Cloud to automate Data Diffs in your CI pipeline, leveraging dbt jobs to detect changes and ensure data quality before merging.

<Note>
  **NOTE**

  You will need a dbt **Team** account or higher to access the dbt Cloud API that Datafold uses to connect the accounts.
</Note>

## Prerequisites

### Set up dbt Cloud CI

In dbt Cloud, [set up dbt Cloud CI](https://docs.getdbt.com/docs/deploy/cloud-ci-job) so that your Pull Request job runs when you open or update a Pull Request. This job will provide Datafold information about the changes included in the PR.

### Create an Artifacts Job in dbt Cloud

The Artifacts job generates production `manifest.json` on merge to main/master, giving Datafold information about the state of production. The simplest method is to set up a dbt Cloud job that executes the `dbt ls` command on merge to main/master.

> Note: `dbt ls` is preferred over `dbt compile` as it runs faster and data diffing does not require fully compiled models to work.

Example dbt Cloud artifact job settings and successful run:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cf58a3156778571d811e995c186a60ab" data-og-width="1592" width="1592" data-og-height="916" height="916" data-path="images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=b49999afef6210c65540b26b35405d8d 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=b826caa7c2d0ef0d9935e28b31aed4d7 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4a71e7da80a014c6fdc5ba72fa92d55f 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=13a4e60fc51d4ab8845071b01cf7c301 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a7beb8c2ce700409b4205346b77640b0 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e267803f50ef3e2ac00562ea12a8063d 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6e21263f5fa0b9317a58d335f59d02ec" data-og-width="2010" width="2010" data-og-height="1854" height="1854" data-path="images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0775d8bbe2360ce68a896d09ffa670a7 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d6a5b6271d4073fc60eb86f6b346d01b 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a526b0ac3e33ceab5fce9a35ef557a86 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d73678e8ddd48d24eaacea3a642f9989 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e8dbdee5ce84f68d4334b716f22fe5d4 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fac813f0fe74aeee26672f67271ffd5e 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5889e462f19a3cbba05fd60f7f1a26bf" data-og-width="1841" width="1841" data-og-height="1210" height="1210" data-path="images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e9c9f109f7a7273b442e7276d5d2a950 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9ad27fd2667a61813bcde95460f2c93f 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=79f2d1de22adc241d3dabb4574f2dd71 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=37e8dc56d3f3e10723743d7f4eb7a4fe 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8777748ffa6404d73bfd7632b3ec3632 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f1c41706ec622fbc37c82810a29841a7 2500w" />
</Frame>

<Accordion title="Continuous Deployment">
  If you are interested in continuous deployment, you can use a [Merge Trigger Production Job](https://docs.datafold.com/cd#merge-trigger-production-job) instead of the Artifacts Job listed above.
</Accordion>

### dbt Cloud Access URL

You will need your [access url](https://docs.getdbt.com/docs/cloud/about-cloud/regions-ip-addresses) to connect Datafold to your dbt Cloud account.

### Add dbt Cloud Service Account Token

To connect Datafold to your dbt Cloud account, you will need to use a [Service Token](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens).

info

Please note that the use of User API Keys for this purpose is no longer recommended due to a [recent security update](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens) in dbt Cloud. [Learn more below](/integrations/orchestrators/dbt-cloud#deprecating-user-tokens)

1. Navigate to **Account Settings → Service Tokens → + New Token**.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a1853f25fa9a05cd5346385fe9de836b" data-og-width="2023" width="2023" data-og-height="832" height="832" data-path="images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=75f7c9808844db6e8f375e03264adbdf 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=884faa5d94bc096d9478521a925c7aca 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1858d0ef767eadb26037b57e0e7b1578 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0ddea931e0c9a5ba475e437fe40f6931 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=98b4c7baa4cb7b9d4eb7af0a8a74ce4a 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8603849aa46bdfdbfc2f0e89972bd238 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84146d65087fe8a89d0037d5b158018d" data-og-width="1322" width="1322" data-og-height="864" height="864" data-path="images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=834fbaca8bab6e64f77c140a5774e715 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e7672e8ec2a88e2e66aadf52071706cc 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cd502aad0a0716ed1ea25be21605c63a 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4f0757783da2259ad5b4b6f95e8d8fd8 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a0e8887e9d3b56dcfb8cec48c8853083 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3c0c5054d2879c4bb61cc9baca41996e 2500w" />
</Frame>

1. Add a Permission Set and select `Member` or `Developer`.
2. Select `All Projects`, or check only the projects you intend to use with Datafold.
3. Save your changes.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=87fc12ff14d1a74898d821e87b935c77" data-og-width="1308" width="1308" data-og-height="886" height="886" data-path="images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=10e3c018d832c6a955d7243ccc3a58a3 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=70bfb9cdf1d7db62075057264b25fff5 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6cefe9e7c967c8d56cd852b7b36f4e84 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=edfc4503837b70c884003ed5abe8c0dc 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=03436a64c167e679b6911c1fb94d39d7 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9a9d578f71fd670b3ee9231344f0143f 2500w" />
</Frame>

1. Navigate to **Your Profile → API Access** and copy the token.

#### Deprecating User Tokens

dbt Cloud is transitioning away from the use of User API Keys for authentication. The User API Key will be replaced by account-scoped Personal Access Tokens (PATs).

This update will affect the functionality of certain API endpoints. Specifically, `/v2/accounts`, `/v3/accounts`, and `/whoami` (undocumented API) will no longer return information about all the accounts tied to a user. Instead, the response will be filtered to include only the context of the specific account in the request.

dbt Cloud users have until April 30, 2024, to implement this change. After this date, all user API keys will be scoped to an account. New customers are required to use the new account-scoped PATs.

For more information, please refer to the [dbt Cloud API Documentation](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens).

If you have any questions or require further assistance, please don't hesitate to contact our support team.

## Create a dbt Cloud Integration in the Datafold app

* Navigate to Settings > Integrations > CI and create a new dbt Cloud integration.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f7e0c8fb8d7fd554c4fdc36adf746cb7" data-og-width="2306" width="2306" data-og-height="496" height="496" data-path="images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f45ee4ad2bd8d407c1108c591cfcdf28 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=41827079f10c7fa05944138c2a7c1bd8 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cff0a79a8878070ff17a997fbdc20a51 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fc241868e30d85d6306c9e18051a1391 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a4cc47cc9738ace1cf6d827fb98d7a2d 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f71b1ca704af7318afca6fd774f42c2c 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=52c6d10f5b06085543f09dcff9106f97" data-og-width="1436" width="1436" data-og-height="640" height="640" data-path="images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f6c08b4a490fdda4c93ff0347d388dce 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e179f0a9cb37cc6b8c0a34f26f03497a 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=36acbde6d839dd22b1025263f3bbc254 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cd8ebc2c3207c0d5a004d202fb6351d7 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1551ad0d625bb0ed3bcb907e09df3e48 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bae50b6b6085801874fe965a421dd38f 2500w" />
</Frame>

## Configuration

### Basic Settings

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cffb2b8c4bc7893601e6268b88fcbdc3" data-og-width="2294" width="2294" data-og-height="1354" height="1354" data-path="images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=98da01d5853b7937aa6b7383fbbd66d0 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d744c777a4f34448b8bad2403f0b10b1 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4900264b8e46454f00a7684d8e1754c2 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=15dfbfe23d1d65df71070d08bc96ddda 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=496dd997a76f6706071de42485d914b7 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=06c5de14ae2640627cda4eef6ded9d2a 2500w" />
</Frame>

* **Repository**: Select a repository that you set up in [the Code Repositories setup step](/integrations/code-repositories).
* **Data Connection**: Select a connection that you set up in [the Data Connections setup step](/integrations/databases).
* **Name**: This can be anything!
* **Primary key tag**: This is a text string that you may use to tag primary keys in your dbt project yaml. Note that to avoid the need for tagging, [primary keys can be inferred from dbt uniqueness tests](/deployment-testing/configuration/primary-key).
* **Account name**: This will be autofilled using your dbt API key.
* **Job that creates dbt artifacts**: This will be [the Artifacts Job that you created](#create-an-artifacts-job-in-dbt-cloud). Or, if you have a dbt production job that runs on each merge to main, select that job.
* **Job that builds pull requests**: This is the dbt CI job that is triggered when you open a Pull Request or Merge Request.

### Advanced Settings

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ac03933bcc83efe52d9fae35874ee500" data-og-width="2306" width="2306" data-og-height="1432" height="1432" data-path="images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=36be894c12c54d680c65c00ec31e7377 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9e424e6606c2bc34bb2ed7b2bf025d18 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4cd6464cb569f6d61c3f28bfb257bdc3 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4617f1e0877d5d5dd2d3b855a1c83868 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3b221781ca235a27113b3943825ba23e 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=655f696a55d9a7d6c0a8c0f3f260e218 2500w" />
</Frame>

* **Enable Datafold in CI/CD**: High-level switch to turn Datafold off or on in CI (but we hope you'll leave it on!).
* **Import dbt tags and descriptions**: Populate our Lineage tool with dbt metadata. ⚠️ This feature is in development. ⚠️
* **Slim Diff**: Only diff modified models in CI, instead of all models. [Please read more about Slim Diff](/deployment-testing/best-practices/slim-diff), which is highly configurable using dbt yaml, and each organization will need to set a strategy based on their data environment.
  * Downstream Hightouch models will be diffed even when Slim Diff is turned on.
* **Diff Hightouch Models**: Hightouch customers can see diffs of downstream Hightouch assets in Pull Requests.
* **CI fails on primary key issues**: The existence of null or duplicate primary keys causes the Datafold CI check to fail.
* **Pull Request Label**: For when you want Datafold to *only* run in CI when a label is manually applied in GitHub/GitLab.
* **CI Diff Threshold**: For when you want Datafold to *only* run automatically if the number of diffs doesn't exceed this threshold for a given CI run.
* **Files to ignore**: If at least one modified file doesn’t match the ignore pattern, Datafold CI diffs all changed models in the PR. If all modified files should be ignored, Datafold CI does not run in the PR. ([Additional details.](/deployment-testing/configuration/datafold-ci/on-demand))
* **Custom base branch**: For when you want Datafold to **only** run in CI when a PR is opened against a specific base branch. You might need this if you have multiple environments built from different branches. See [Custom branch](https://docs.getdbt.com/faqs/Environments/custom-branch-settings) in dbt Cloud docs.

Click save, and that's it! <Icon icon="party-horn" />

Now that you've set up a dbt Cloud integration, Datafold will diff your impacted tables whenever you push commits to a PR. A summary of the diff will appear in GitHub, and detailed results will appear in the Datafold app.


# dbt Core
Source: https://docs.datafold.com/integrations/orchestrators/dbt-core

Set up Datafold’s integration with dbt Core to automate Data Diffs in your CI pipeline.

<Note>
  **PREREQUISITES**

  * Create a [Data Connection Integration](/integrations/databases) where your dbt project data is built.
  * Create a [Code Repository Integration](/integrations/code-repositories) where your dbt project code is stored.
</Note>

## Getting started

To add Datafold to your continuous integration (CI) pipeline using dbt Core, follow these steps:

### 1. Create a dbt Core integration.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6dc1d0706b51de98a38563f38d646ade" data-og-width="3012" width="3012" data-og-height="848" height="848" data-path="images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9738742fe98563394a86ee75b79b76e7 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e7d85efc1e91f61da211521ea152ab5c 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c62eda8b4ce4668324e0fcb57b4137ba 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cd836180d5f6000e9ff94e363801408b 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=03acf893f29bf6a0cb3239fe49cc0c9e 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_integration-e8e0468f1f20a3436a47cb37d08639c0.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e188550bb0508832a5ceee3f1b923936 2500w" />
</Frame>

### 2. Set up the dbt Core integration.

Complete the configuration by specifying the following fields:

#### Basic settings

| Field Name         | Description                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Configuration name | Choose a name for your for your Datafold dbt integration.                                  |
| Repository         | Select your dbt project.                                                                   |
| Data Connection    | Select the data connection your dbt project writes to.                                     |
| Primary key tag    | Choose a string for [tagging primary keys](/deployment-testing/configuration/primary-key). |

#### Advanced settings: Configuration

| Field Name                       | Description                                                                                                                                                                                                                                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Import dbt tags and descriptions | Import dbt metadata (including column and table descriptions, tags, and owners) to Datafold.                                                                                                                                                                                                                |
| Slim Diff                        | Data diffs will be run only for models changed in a pull request. See our [guide to Slim Diff](/deployment-testing/best-practices/slim-diff) for configuration options.                                                                                                                                     |
| Diff Hightouch Models            | Run Data Diffs for Hightouch models affected by your PR.                                                                                                                                                                                                                                                    |
| CI fails on primary key issues   | The existence of null or duplicate primary keys will cause CI to fail.                                                                                                                                                                                                                                      |
| Pull Request Label               | When this is selected, the Datafold CI process will only run when the `datafold` label has been applied.                                                                                                                                                                                                    |
| CI Diff Threshold                | Data Diffs will only be run automatically for a given CI run if the number of diffs doesn't exceed this threshold.                                                                                                                                                                                          |
| Branch commit selection strategy | Select "Latest" if your CI tool creates a merge commit (the default behavior for GitHub Actions). Choose "Merge base" if CI is run against the PR branch head (the default behavior for GitLab).                                                                                                            |
| Custom base branch               | If defined, CI will run only on pull requests with the specified base branch.                                                                                                                                                                                                                               |
| Columns to ignore                | Use standard gitignore syntax to identify columns that Datafold should never diff for any table. This can [improve performance](/faq/performance-and-scalability#how-can-i-optimize-diff-performance-at-scale) for large datasets. Primary key columns will not be excluded even if they match the pattern. |
| Files to ignore                  | If at least one modified file doesn’t match the ignore pattern, Datafold CI diffs all changed models in the PR. If all modified files should be ignored, Datafold CI does not run in the PR. ([Additional details.](/deployment-testing/configuration/datafold-ci/on-demand))                               |

#### Advanced settings: Sampling

Sampling allows you to compare large datasets more efficiently by checking only a randomly selected subset of the data rather than every row. By analyzing a smaller but statistically meaningful sample, Datafold can quickly estimate differences without the overhead of a full dataset comparison. To learn more about how sampling can result in a speedup of 2x to 20x or more, see our [best practices on sampling](/data-diff/cross-database-diffing/best-practices#enable-sampling).

| Field Name          | Description                                                                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable sampling     | Enable sampling for data diffs to optimize analyzing large datasets.                                                                                                       |
| Sampling tolerance  | The tolerance to apply in sampling for all data diffs.                                                                                                                     |
| Sampling confidence | The confidence to apply when sampling.                                                                                                                                     |
| Sampling threshold  | Sampling will be disabled automatically if tables are smaller than specified threshold. If unspecified, default values will be used depending on the Data Connection type. |

### 3. Obtain an Datafold API Key and CI config ID.

After saving the settings in step 2, scroll down and generate a new Datafold API Key and obtain the CI config ID.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e65dd3975cef3b16ad203a0e6dfc1e7c" data-og-width="2310" width="2310" data-og-height="972" height="972" data-path="images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e0e7022637f64e95d0f4c01e6f09db1 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4fc016fc32528e5f1f08b4f9edc88cc7 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b570523c1b5d58809b253754f6fbe82f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc99d5527fc2951e3c3919f784b15955 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=23aaa8a8a35b8d3bfe814868517fca80 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8d376a542ad6683d9418572183ba8542 2500w" />
</Frame>

### 4. Configure your CI script(s) with the Datafold SDK.

Using the Datafold SDK, configure your CI script(s) to upload dbt `manifest.json` files.

The `datafold dbt upload` command takes this general form and arguments:

```
datafold dbt upload --ci-config-id <your-ci_config-id> --run-type <job-type> --commit-sha <commit-sha>
```

You will need to configure orchestration to upload the dbt `manifest.json` files in 2 scenarios:

1. **On merges to main.** These `manifest.json` files represent the state of the dbt project on the base/production branch from which PRs are created.
2. **On updates to PRs.** These `manifest.json` files represent the state of the dbt project on the PR branch.

The dbt Core integration creation form automatically generates code snippets that can be added to CI runners.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f16553310e2b26b26e5d4b2a2c76c002" data-og-width="2678" width="2678" data-og-height="1344" height="1344" data-path="images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d41ecff2ee924e3178072beef8fd2320 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c54d42a6a1ff01d4e9fe988fefa77637 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5af384917ff7c83177e0f0bb4447ab38 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=efb57b00d07f874cb04ae7ae5f3f6df5 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2022c86903d2d8dd48405a8fed515025 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config-b0a800dc1e86cfa3c0af64d97ca52af8.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84045f617f0fe9d4eae200cba3d9a131 2500w" />
</Frame>

By storing and comparing these `manifest.json` files, Datafold determines which dbt models to diff in a CI run.

Implementation details vary depending on which CI tool you use. Please review [these instructions and examples](#ci-implementation-tools) to help you configure updates to your organization's CI scripts.

### 5. Test your dbt Core integration.

After updating your CI scripts, trigger jobs that will upload `manifest.json` files represent the base/production state.

Then, open a new pull request with changes to a SQL file to trigger a CI run.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=14dbcf392db072b3af4f9dbb7ab3860e" data-og-width="1306" width="1306" data-og-height="560" height="560" data-path="images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9bab4f4b53965a53df7e33ac3a3be0f5 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d3c6edc647c091269d3849f9d18857c3 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0425c279a0c6aa9f74b0e5aae6c6fc98 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d1e11df09a985d7e1e386a0c84cc3c66 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fe0198eb1cddd43a81e51bbf46f37855 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_core_ci_config_test-7c78a7e83802c4273cdec4600a09e01d.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8b8f378175ac7cc466e950cc4144402f 2500w" />
</Frame>

## CI implementation tools

We've created guides and templates for three popular CI tools.

<Tip>
  **Having trouble setting up Datafold in CI?**

  We're here to help! Please reach out and [chat with a Datafold Solutions Engineer](https://www.datafold.com/booktime). <Icon icon="phone-rotary" />
</Tip>

To add Datafold to your CI tool, add `datafold dbt upload` steps in two CI jobs:

* **Upload Production Artifacts:** A CI job that build a production `manifest.json`. *This can be either your Production Job or a special Artifacts Job that runs on merge to main (explained below).*
* **Upload Pull Request Artifacts:** A CI job that builds a PR `manifest.json`.

This ensures Datafold always has the necessary `manifest.json` files, enabling us to run data diffs comparing production data to dev data.

<Tabs>
  <Tab title="GitHub Actions">
    **Upload Production Artifacts**

    Add the `datafold dbt upload` step to *either* your Production Job *or* an Artifacts Job.

    **Production Job**

    If your dbt prod job kicks off on merges to the base branch, add a `datafold dbt upload` step after the `dbt build` step.

    ```bash  theme={null}
    name: Production Job
    on:
      push:
        branches:
          - main
    jobs:
      run:
        runs-on: ubuntu-20.04
        steps:
          - name: Install Datafold SDK
            run: pip install -q datafold-sdk
          - name: Upload dbt artifacts to Datafold
            run: datafold dbt upload --ci-config-id <datafold_ci_config_id> --run-type production --commit-sha ${GIT_SHA}
            env:
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
              GIT_SHA: "${{ github.sha }}"
    ```

    **Artifacts Job**

    If your existing Production Job runs on a schedule and not on merges to the base branch, create a dedicated job that runs on merges to the base branch which generates and uploads a `manifest.json` file to Datafold.

    ```bash  theme={null}
    name: Artifacts Job
    on:
      push:
        branches:
          - main
    jobs:
      run:
        runs-on: ubuntu-20.04
        steps:
          - name: Install Datafold SDK
            run: pip install -q datafold-sdk
          - name: Generate dbt manifest.json
            run: dbt ls
          - name: Upload dbt artifacts to Datafold
            run: datafold dbt upload --ci-config-id <datafold_ci_config_id> --run-type production --commit-sha ${BASE_GIT_SHA}
            env:
              DATAFOLD_APIKEY: ${{ secrets.DATAFOLD_APIKEY }}
              BASE_GIT_SHA: "${{ github.sha }}"
    ```

    **Pull Request Artifacts**

    Include the `datafold dbt upload` step in your CI job that builds PR data.

    ```bash  theme={null}
    name: Pull Request Job
    on:
      pull_request:
      push:
        branches:
          - '!main'
    jobs:
      run:
        runs-on: ubuntu-20.04
        steps:
          - name: Install Datafold SDK
            run: pip install -q datafold-sdk
          - name: Upload PR manifest.json to Datafold
            run: |
              datafold dbt upload --ci-config-id <datafold_ci_config_id> --run-type pull_request --commit-sha ${PR_GIT_SHA}
            env:
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
              PR_GIT_SHA: "${{ github.event.pull_request.head.sha }}"
    ```

    **Store Datafold API Key**

    Save the API key as `DATAFOLD_API_KEY` in your [GitHub repository settings](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).
  </Tab>

  <Tab title="CircleCI">
    **Upload Production Artifacts**

    Add the `datafold dbt upload` step to *either* your Production Job *or* an Artifacts Job.

    **Production Job**

    If your dbt prod job kicks off on merges to the base branch, add a `datafold dbt upload` step after the `dbt build` step.

    ```bash  theme={null}
    version: 2.1
    jobs:
      prod-job:
        filters:
          branches:
            only: main
        docker:
          - image: cimg/python:3.9
        steps:
          - checkout
          - run:
              name: "Install Datafold SDK"
              command: pip install -q datafold-sdk
          - run:
              name: "Build dbt project"
              command: dbt build
          - run:
              name: "Upload production manifest.json to Datafold"
              command: |
                datafold dbt upload --ci-config-id <datafold_ci_config_id> --run-type production --target-folder ./target/ --commit-sha ${CIRCLE_SHA1}
    ```

    **Artifacts Job**

    If your existing Production Job runs on a schedule and not on merges to the base branch, create a dedicated job that runs on merges to the base branch which generates and uploads a `manifest.json` file to Datafold.

    ```bash  theme={null}
    version: 2.1
    jobs:
      artifacts-job:
        filters:
          branches:
            only: main
        docker:
          - image: cimg/python:3.9
        steps:
          - checkout
          - run:
              name: "Install Datafold SDK"
              command: pip install -q datafold-sdk
          - run:
              name: "Generate manifest.json"
              command: dbt ls --profiles-dir ./
          - run:
              name: "Upload production manifest.json to Datafold"
              command: datafold dbt upload --ci-config-id <datafold_ci_config_id> --run-type production --target-folder ./target/ --commit-sha ${CIRCLE_SHA1}
    ```

    **Store Datafold API Key**

    Save the API key in the [CircleCI interface](https://circleci.com/docs/set-environment-variable/).
  </Tab>

  <Tab title="GitLab CI">
    **Upload Production Artifacts**

    Add the `datafold dbt upload` step to *either* your Production Job *or* an Artifacts Job.

    **Production Job**

    If your dbt prod job kicks off on merges to the base branch, add a `datafold dbt upload` step after the `dbt build` step.

    ```bash  theme={null}
    image:
      name: ghcr.io/dbt-labs/dbt-core:1.x
    run_pipeline:
      stage: deploy
      before_script:
        - pip install -q datafold-sdk
      script:
        - dbt build --profiles-dir ./
        - datafold dbt upload --ci-config-id <ci-config-id> --run-type production --commit-sha $CI_COMMIT_SHA
    ```

    **Artifacts Job**

    If your existing Production Job runs on a schedule and not on merges to the base branch, create a dedicated job that runs on merges to the base branch which generates and uploads a `manifest.json` file to Datafold.

    ```bash  theme={null}
    image:
      name: ghcr.io/dbt-labs/dbt-core:1.x
    run_pipeline:
      stage: deploy
      before_script:
        - pip install -q datafold-sdk
      script:
        - dbt ls --profiles-dir ./
        - datafold dbt upload --ci-config-id <ci-config-id> --run-type production --commit-sha $CI_COMMIT_SHA
    ```

    **Store Datafold API Key**

    Save the API key as `DATAFOLD_API_KEY` in [GitLab repository settings](https://docs.gitlab.com/ee/ci/yaml/index.html#secrets).
  </Tab>
</Tabs>

## CI for dbt multi-projects

When setting up CI for dbt multi-projects, each project should have its own dedicated CI integration to ensure that changes are validated independently.

## CI for dbt multi-projects within a monorepo

When managing multiple dbt projects within a monorepo (a single repository), it’s essential to configure individual Datafold CI integrations for each project to ensure proper isolation.

This approach prevents unintended triggering of CI processes for projects unrelated to the changes made. Here’s the recommended approach for setting it up in Datafold:

**1. Create separate CI integrations:** Create separate CI integrations within Datafold, one for each dbt project within the monorepo. Each integration should be configured to reference the same GitHub repository.

**2. Configure file filters**: For each CI integration, define file filters to specify which files should trigger the CI run. These filters prevent CI runs from being initiated when files from other projects in the monorepo are updated.

**3. Test and validate**: Before deployment, test each CI integration to validate that it triggers only when changes occur within its designated dbt project. Verify that modifications to files in one project do not inadvertently initiate CI processes for unrelated projects in the monorepo.

###

## Advanced configurations

### Skip Datafold in CI

To skip the Datafold step in CI, include the string `datafold-skip-ci` in the last commit message.

### Programmatically trigger CI runs

The Datafold app relies on the version control service webhooks to trigger the CI runs. When the dedicated cloud deployments is behind a VPN, webhooks cannot directly reach the deployment due to the network's restricted access.

We can overcome this by triggering the CI runs via the [datafold-sdk](/api-reference/datafold-sdk) in the Actions/Job Runners, assuming they're running in the same network.

Add a new Datafold SDK command after uploading the manifest in a PR job:

<Tip>
  **Important**

  When configuring your CI script, be sure to use `${{ github.event.pull_request.head.sha }}` for the **Pull Request Job** instead of `${{ github.sha }}`, which is often mistakenly used.

  `${{ github.sha }}` defaults to the latest commit SHA on the branch and **will not work correctly for pull requests**.
</Tip>

```Bash  theme={null}
  - -name: Trigger CI
    run: |
      set -ex
      datafold ci trigger --ci-config-id <datafold_ci_config_id> \
        --pr-num ${PR_NUM} \
        --base-branch ${BASE_BRANCH} \
        --base-sha ${BASE_SHA} \
        --pr-branch ${PR_BRANCH} \
        --pr-sha ${PR_SHA}
    env:
      DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
      DATAFOLD_HOST: ${{ secrets.DATAFOLD_HOST }}
      PR_NUM: ${{ github.event.number }}
      PR_BRANCH: ${{ github.event.pull_request.head.ref }}
      BASE_BRANCH: ${{ github.event.pull_request.base.ref }}
      PR_SHA: ${{ github.event.pull_request.head.sha }}
      BASE_SHA: ${{ github.event.pull_request.base.sha }}

```

### Running diffs before opening a PR

Some teams want to show Data Diff results in their tickets *before* creating a pull request. This speeds up code reviews as developers can QA code changes before requesting a PR review.

Check out how to automate this workflow [here](/faq/datafold-with-dbt#can-i-run-data-diffs-before-opening-a-pr).


# Compliance & Trust Center
Source: https://docs.datafold.com/security/compilance-trust-center





# Database OAuth
Source: https://docs.datafold.com/security/database-oauth

Datafold enables secure workflows like data diffs through OAuth, ensuring compliance with user-specific database permissions.

To improve data security and privacy, Datafold supports running workflows like data diffs through OAuth. This ensures queries are executed using the user's own database credentials, fully complying with granular access controls like data masking and object-level permissions.

The diagram below illustrates how the authentication flow proceeds:

1. Users authenticate using the configured OAuth provider.
2. Users can then create diffs between data sets that their user can access using OAuth database permissions.
3. During Continuous Integration (CI), Datafold executes diffs using a Service Account with the least privileges, thus masking sensitive/PII data.
4. If a user needs to see sensitive/PII data from a CI diff, and they have permission via OAuth to do so, they can rerun the diff, and then Datafold will authenticate the user using OAuth database permissions. Then, the user will have access to the data based on these permissions.

This structure ensures that diffs are executed with the user's database credentials with their configured roles and permissions. Data access permissions are thus fully managed by the database, and Datafold only passes through queries.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c97a5cc781ff4bd1209c9efe06e5c1c6" data-og-width="3898" width="3898" data-og-height="2950" height="2950" data-path="images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4cb1a240af1a8ef1c8a1a6fe4d5042e0 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3c4de42e0b5ce184e5bf2a29771e1245 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=59dddd239015bd7ca4a9db203ecd3e17 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ded86dded41cde0752adc01c543bfd2a 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ccf9b36a6cf6963c5274185a20bd867 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=50eb3fcc49b9bbe49b592547905a46ff 2500w" />
</Frame>


# Securing Connections
Source: https://docs.datafold.com/security/securing-connections

Datafold supports multiple options to secure connections between your resources (e.g., databases and BI tools) and Datafold.

## Encryption

When you connect to Datafold to query your data in a database (e.g., BigQuery), communications are secured using HTTPS encryption.

## IP whitelisting

If access to your data connection is restricted to IP addresses on an allowlist, you will need to manually add Datafold's addresses in order to use our product. Otherwise, you will receive a connection error when setting up your data connection.

For SaaS (app.datafold.com) deployments, whitelist the following IP addresses:

* `23.23.71.47`
* `35.166.223.86`
* `52.11.132.23`
* `54.71.177.163`
* `54.185.25.103`
* `54.210.34.216`

Note that at any given time, you will only see one of these addresses in use. However, the active IP address can change, so you should add them all to your IP whitelist to ensure no interruptions in service.

## Private Link

<Tabs>
  <Tab title="AWS">
    ### AWS PrivateLink

    AWS PrivateLink allows you to connect Datafold to your databases without exposing data to the internet. This option is available for both Datafold SaaS Cloud and all Datafold Dedicated Cloud options.

    The following diagram shows the architecture for a customer with a High Availability RDS setup:

    <Frame caption="SaaS with PrivateLink">
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=65b88c7ff34cc84894b60d27691bbe88" data-og-width="2480" width="2480" data-og-height="1296" height="1296" data-path="images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ce35baacdc5cdfd99ecca2350df43249 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=01d156c2eff63bdb78b10e4109d86b67 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f569417d66283f168b84c4cb23ea92a9 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b6529b2dd6158a729dd4185760904f76 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=73881be7675758882f8de1ef81698b14 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=892c9b54e12f3de7dc08df77a01ebfae 2500w" />
    </Frame>

    ### Setup

    <Info>
      Supported databases

      The following setup assumes you have an RDS/Aurora database you want to connect to. Datafold also supports PrivateLink connections to other databases such as Snowflake, which should only be accessed from your VPC. Please contact [support@datafold.com](mailto:support@datafold.com) to get assistance with connecting to your specific database.
    </Info>

    Our support team will send you the following:

    * The role ARN to establish the PrivateLink connection.
    * Datafold SaaS Cloud VPC CIDR range.

    You need to do the following steps:

    1. Send us the region(s) where your database(s) are located.
    2. Create a VPC Endpoint Service and NLB.
       * The core concepts of this setup are described in this AWS blog: [Access Amazon RDS across VPCs using AWS PrivateLink and Network Load Balancer](https://aws.amazon.com/blogs/database/access-amazon-rds-across-vpcs-using-aws-privatelink-and-network-load-balancer/).
       * If your databases are HA, please implement the failover mechanics described in the blog.
         * A CloudFormation template for inspiration can be found [here](https://github.com/aws-samples/amazon-rds-crossaccount-access/blob/main/CrossAccountRDSAccess.yml).
       * You'll need to create a Network Load Balancer that points to your database and a VPC Endpoint Service that exposes the NLB.
       * Configure security groups to allow traffic from Datafold's VPC to your database.
       * If your databases are HA (High Availability), implement automatic failover mechanics to ensure the NLB routes to the active database instance.
       * For detailed step-by-step instructions, see our [**AWS PrivateLink Setup Guide**](/security/aws_privatelink_setup).
    3. Add the provided role ARN as 'Allowed Principal' on the VPC Endpoint Service.
    4. Allow ingress from the Datafold SaaS Cloud VPC.
    5. Send us the:
       * Service name(s), e.g. `com.amazonaws.vpce.us-west-2.vpce-svc-0cfd2f258c4395ad6`.
       * Availability Zone ID(s) used in the VPCE Service(s), e.g. `use1-az6` or `usw2-az3`.
       * RDS/Aurora hostname(s), e.g. `datafold.c2zezoge6btk.us-west-2.rds.amazonaws.com`.

    At the end, the database hostname used to configure the data source will be the original RDS/Aurora hostname. But with private DNS resolution, we will resolve the hostname to the VPC Endpoint. Our support team will let you know when everything is set up and you can accept the PrivateLink connection and start configuring the data source.

    <Tip>
      **Detailed Instructions**

      For comprehensive step-by-step instructions including security group configuration, target group setup, Lambda-based automatic failover for HA setups, and troubleshooting, see our [**AWS PrivateLink Setup Guide**](/security/aws_privatelink_setup).
    </Tip>

    ### Cross-Region PrivateLink

    Datafold SaaS Cloud supports cross-region PrivateLink for all North American regions. Datafold SaaS Cloud is located in `us-west-2`. Datafold manages the cross-region networking, allowing you to connect to a VPC Endpoint in the same region as your VPC Endpoint Service. For Datafold Dedicated Cloud customers, deployment occurs in your chosen region. If you need to connect to databases in multiple regions, Datafold also supports this through cross-region PrivateLink.

    The setup will be similar to the regular PrivateLink setup.
  </Tab>

  <Tab title="GCP">
    ### Private Service Connect

    Google Cloud's Private Service Connect is only available if both parties are in the same cloud region. This option is only available for Datafold Dedicated Cloud customers. The diagram below illustrates how the solution works:

    <Frame>
      <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=38c439b9f588193c87956ef53895a424" data-og-width="1008" width="1008" data-og-height="586" height="586" data-path="images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=be06d8ff89a08b4df409ecfede8a683b 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0b583f6cb0578ee985d1195d03834a21 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ccf8914007440e0cb88fe9839abd2f89 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2753bd770bb50ff04c7bc89d428df1f9 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4f33eb651737d66fef59dd4c929f52b0 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d94d78eb8007a0a5b49ecb36ddbc2711 2500w" />
    </Frame>

    The basics of Private Service Connect are available [here](https://cloud.google.com/vpc/docs/private-service-connect).
  </Tab>

  <Tab title="Azure">
    ### Azure Private Link

    Azure Private Link is only available if both parties are in the same cloud region. This option is only available for Datafold Dedicated Cloud customers. The diagram below illustrates how the solution works:

    <Frame>
      <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e8a1369ee4fd7f7866ec7550337f0c23" data-og-width="1140" width="1140" data-og-height="729" height="729" data-path="images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0cdc802a43333d995b7161feb6021374 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=05bbed6ba750dbb4538db193265bf181 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d01a70b96bf8e75b3a26cf6ae91c9e45 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=315e8750c5cda55724d638efa3f5c899 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b8d4907b690435efb419d259574260af 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f788286a9ffaa42293d3ea1e22f03742 2500w" />
    </Frame>

    The basics of Private Link are available [here](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview).

    For Customer-Hosted Dedicated Cloud, achieving cross-tenant access requires using Private Link. The documentation can be accessed [here](https://learn.microsoft.com/en-us/azure/architecture/guide/networking/cross-tenant-secure-access-private-endpoints).
  </Tab>
</Tabs>

## VPC Peering (SaaS)

VPC Peering is easier to set up than Private Link, but a drawback is that both networks are joined and the IP ranges must not overlap. For Datafold SaaS Cloud, this setup is an AWS-only option.

The basics of VPC peering are covered [here](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

To set up VPC peering, please contact [support@datafold.com](mailto:support@datafold.com) and provide us with the following information:

* AWS region where your database is hosted.
* ID of the VPC that you would like to connect.
* CIDR of the VPC.

If there are no address collisions, we'll send you a peering request and CIDR that we use on our end, and whitelist the CIDR range for your organization. You'll need to set up routing to this CIDR through the peering connection.

If you activate DNS on your side of the peering connection, you can use the private DNS hostname to connect. Otherwise, you need to use the IP.

## VPC Peering (Dedicated Cloud)

VPC Peering is a supported option for all cloud providers, both for Datafold-hosted and customer-hosted deployments. Basic information for each cloud provider can be found here:

* [AWS](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html)
* [GCP](https://cloud.google.com/vpc/docs/vpc-peering)
* [Azure](https://learn.microsoft.com/en-us/azure/virtual-network/create-peering-different-subscriptions?tabs=create-peering-portal)

<Tip>
  **VPC vs VNet**

  We use the term VPC across all major cloud providers. However, Azure calls this concept a Virtual Network (VNet).
</Tip>

## SSH Tunnel

To set up a tunnel, please contact our team at [support@datafold.com](mailto:support@datafold.com) and provide the following information:

* Hostname of your bastion host and port number used for SSH service.
* Hostname of and port number of your database.
* SSH fingerprint of the bastion host (optional).

We'll get back to you with:

* SSH public key that you need to add to `~/.ssh/authorized_hosts`.
* IP address and port to use for data connection configuration in the Datafold application.

## IPSec tunnel

Please contact our team at [support@datafold.com](mailto:support@datafold.com) for more information.


# Single Sign-On
Source: https://docs.datafold.com/security/single-sign-on

Set up Single Sign-On with one of the following options.

<CardGroup>
  <Card title="Okta (OIDC)" href="/security/single-sign-on/okta" icon="file" horizontal />

  <Card title="Google OAuth" href="/security/single-sign-on/google-oauth" icon="file" horizontal />

  <Card title="SAML" href="/security/single-sign-on/saml/" icon="folder-open" horizontal />
</CardGroup>

<Tip>
  **Tip**

  You can force all users to use the configured SSO provider by unchecking the *Allow non-admin users to login with email and password* checkbox under the organization settings.

  Admin users will still be able to login using email and password.

  <Frame>
    <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=29f90cc886243d77cd3ceac6fa825ad7" data-og-width="843" width="843" data-og-height="399" height="399" data-path="images/disable_non_admin_email_password_login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=795d023925dfc27b455e5478c8488b92 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bd259b872d305adce12884d34822ef76 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9fbff485e2d7b6c18b909f7e8f4a0bcc 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2e8feed2012315c85c5b6fa6503c1107 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2d479a6c5825d4695a12fa25cc6ac1ef 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9976e83d3bb4e81221150dc1e6c24618 2500w" />
  </Frame>
</Tip>

<Warning>
  **Caution**

  Ensure only authorized users keep using Datafold by setting up Okta webhooks or setting up credentials for the Microsoft Entra app if you're using Microsoft Entra ID (formerly known Azure Active Directory)

  This will disable non-admin users that don't have access to the configured SSO app.

  [Configure this for Okta](/security/single-sign-on/okta#synchronize-state-with-datafold-optional)

  [Configure this for Microsoft Entra ID](/security/single-sign-on/saml/examples/microsoft-entra-id-configuration#synchronize-user-with-datafold-optional)
</Warning>


# Google OAuth
Source: https://docs.datafold.com/security/single-sign-on/google-oauth



<Info>
  **NOTE**

  Google SSO is available for both SaaS and VPC installations of Datafold.
</Info>

## Datafold SaaS

For Datafold SaaS the setup only involves enabling Google SSO integration.

If Google SSO is already enabled for your organization you will see it in the **Settings** → **Integrations** → **SSO**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e7bb80685a41723dfa3c34b3b1d7a805" data-og-width="2658" width="2658" data-og-height="680" height="680" data-path="images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f51be9cc7fef460deba05481652f7192 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c2d390e4ebb466aa3741d6c8bd58c003 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=39a1e787718342851cb3faf64d47743b 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9625b01d4558d8e1bef2d065d0aeb820 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=903f432652191545e0c04ad5384cd171 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_list-5b0c84c5bdddde31c6e82cce055ba758.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=69202005106959bd93244e33b67af714 2500w" />
</Frame>

If this is not the case, create a new Google SSO Integration by clicking on the **Add new integration** button.

Enable the **Allow Google logins in organization** switch and click **Save**. That's it!
If you are not using Datafold SaaS, please see below.

## Create OAuth Client ID

To begin, navigate to the [Google admin console](https://console.cloud.google.com/apis/credentials?authuser=1%5C\&folder=%5C) for your organization, click **Create Credentials**, and select **OAuth Client ID**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2dd9a41200dbec554854e8f2152d4967" data-og-width="2546" width="2546" data-og-height="1212" height="1212" data-path="images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5c04ab9c87f3433a4321ad094cff0444 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3237419a4fbc116379685d0f3baf3ee0 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d79b7171c609bafcf9f214a74ceaa2b7 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0d6e57a10068535692854bb690d680dc 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=81386a187e89ad982cd136fc168b44ec 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create_credential-95776eb793bc1a1115c5fe1b18d9203f.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=738ceb21992881ed330289cc0d781296 2500w" />
</Frame>

<Tip>
  **TIP**

  To configure OAuth, you may need to first configure your consent screen. We recommend selecting **Internal** to keep access limited to users in your Google workspace and organization.
</Tip>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f8fbe61a51916af96fac74baba6e0c57" data-og-width="1100" width="1100" data-og-height="928" height="928" data-path="images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=85a18952eaa280999dca0b9d7d7c4fac 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bda6ab56698d40e1e0bf0981ea705725 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1d8b214ee69deba0807a3d8265484b4b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=43e2ef08d691297c9f52ce6dd1d6ea40 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d2f3fd70ae47170db93229c4ac7f5db4 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_consent_screen-6fd858ff5d1fc5fd43be910f055fe0ca.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ab043b43d1570852e18186d29c44d827 2500w" />
</Frame>

### Configure OAuth[](#configure-oauth "Direct link to Configure OAuth")

* **Application type**: "Web application"
* **Authorized JavaScript origins**: `https://<your.domain.name>`
* **Authorized redirect URIs**: `https://<your.domain.name>/oauth/google`

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d81a93fc47ce61af186a44b1e3032d73" data-og-width="1301" width="1301" data-og-height="1224" height="1224" data-path="images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d38aff3864a2f31b85cf4279d768b225 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ef1fda51909f5b439221d1775330bfe5 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=05ded4cda10a1342c47b4199e0fff443 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9dbfe9a60e75feaa9b053b4611cab4f7 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f44d8a4fbc916f5e92488c87deb604e1 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/google_oauth_authorizations-002a9446a71ba66ba4d375d897c4cdf7.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=88e03d3a62ead7ce5afd9c8c771d8922 2500w" />
</Frame>

Finally, click **Create**. You will see a set of credentials that you will copy over to your Datafold Global Settings.

## Configure Google OAuth in Datafold

To finish the configuration, create a Google SSO Integration in Datafold.

To complete the integration in Datafold, create a new integration by navigating to **Settings** → **Integrations** → **SSO** → **Add new integration** → **Google**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f6236303e7386aa134d770bc9004ba80" data-og-width="2070" width="2070" data-og-height="666" height="666" data-path="images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7e3406de67b5c070cd7ac99c440f248e 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ebc3357ab62687407deb5d9fd63e6067 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b10e57e922bcfb26dd6fc27031b41555 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=224b5d6d21fcec28cb2a45aece520f5f 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=184fecd1f44546ff584188b888aba4a9 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/google_oauth_create-463bc5c0d7cd049e0ba4ae8fdd577185.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=921da1190b889757ca1f86f21f8ddd34 2500w" />
</Frame>

* Enable the **Google OAuth** switch.
* Enter the **domain** or URL of your OAuth client Id on the respective field.
* Paste the **Client Secret** on the respective field.
* Enable the **Allow Google logins in Organization** switch.
* Finally, click **Save**.


# Okta (OIDC)
Source: https://docs.datafold.com/security/single-sign-on/okta



<Info>
  **NOTE**

  Okta SSO is available for both SaaS and dedicated cloud installations of Datafold.
</Info>

## Create Okta App Integration[](#create-okta-app-integration "Direct link to Create Okta App Integration")

<Note>
  **INFO**

  Creating an App Integration in Okta may require admin privileges.
</Note>

Start the integration by creating a web app integration in Okta.

Next, log in to Okta interface and navigate to **Applications** and click **Create App Integration**.

Then, in the configuration form, select **OpenId Connect (OIDC)** and **Web Application** as the Application Type.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cd99a119a39d2e15d3ca3584783311d1" data-og-width="2796" width="2796" data-og-height="2120" height="2120" data-path="images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cb914e5cd780c78edb7d4387d9e6dda8 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cf9347ff420148fb85989217583fed0c 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0a56b06a16cfb02e8d16798d37545725 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0a820232d15b1226f6ca3eac5a8ddb2c 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ca39877292b3a2b12449ae01affeedde 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create_new_app-0b8566bc3dd329ef3d80f849c0065fef.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c8a2be1ae8ac2402e9be775b34bdd58e 2500w" />
</Frame>

In the following section, you will set:

* **App integration name**: A name to identify the integration. We suggest you use `Datafold`.
* **Grant type**: Should be set to `Authorization code` automatically.
* **Sign-in redirect URI**:

<Tabs>
  <Tab title=" SaaS">
    The redirect URL should be `https://app.datafold.com/oauth/okta/client_id`, where `client_id` is the Client ID of the configuration.

    <Warning>
      **CAUTION**
      You will be given the Client ID after saving the integration and need to come back to update the client ID afterwards.
    </Warning>
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    The redirect URL should be `https://your-dns-name/oauth/okta`, replacing `your-dns-name` with the DNS name for your installation.
  </Tab>
</Tabs>

* **Sign-out redirect URIs**: Leave this empty.
* **Trusted Origins**: Leave this empty too.
* **Assignments**: Select `Skip group assignment for now`. Later you should assign the correct groups and users.
* Click "Save" to create the app integration in Okta.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=47fe81beba56d13cbbc6e3e5e7cd061c" data-og-width="915" width="915" data-og-height="733" height="733" data-path="images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9c7caf3ed96608bf9639fcf93f993253 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2b8d1aa51a2b32c28c7c6fadbffa3f44 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ab630f62ba5587489e2ba9ea76df774e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e4fcfbc510a482468b8239fa89680449 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c303f1bb514d6ab2dae609b168bb7353 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_redirect_uri-b64d1ac6c24ab8577bf8a52f14da842b.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2044f3cc5192388676699fe9eea5a7b1 2500w" />
</Frame>

Once the save is successful, on the next screen, you'll be presented with Client ID and Client Secret. We need these IDs to update the redirect URLs that Datafold needs. We'll also apply the Client ID and Client Secret in the Datafold integration later.

* Edit "General settings"
* Scroll down to the **Login** section
* Update the **Sign-in redirect URI**. See above for details.
* Click "Save" to persist the changes.

## Set Up Okta-initiated login

<Tip>
  **TIP**

  Organization admins will always be able to log in with either password or Okta. Non-admin users will be required to log in through Okta once configured.
</Tip>

This step is optional and should be done at the discretion of the Okta administrator.

Users in your organization can log in to the application directly from the Okta end-user dashboard. To enable this feature, configure the integration as follows:

1. Edit "General settings"
2. Set **Login initiated by** to `Either Okta or App`.
3. Set **Application visibility** to `Display application icon to users`.
4. Set **Login flow** to `Redirect to app to initiate login (OIDC Compliant)`.
5. Set **Initiate login URI**:

<Tabs>
  <Tab title=" SaaS">
    * `https://app.datafold.com/login/sso/client-id?action=desired_action`
    * Replace `client-id` with the Client ID of the configuration, and
    * Replace `desired_action` with `signup` if you enabled users auto-creation, or `login` otherwise.
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    * `https://your-dns-name/login/sso/client-id?action=desired_action`
    * Replace `client-id` with the Client ID of the configuration, and
    * Replace `desired_action`with `signup` if you enabled users auto-creation, or `login` otherwise.
    * Replace `your-dns-name` with the DNS name for your installation.
  </Tab>
</Tabs>

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b6ee8ab50310409a28abd3d7de8d6461" data-og-width="1398" width="1398" data-og-height="1206" height="1206" data-path="images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=fcf22e2b4132131726db58c35ce17172 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4f08bc2138da08428cff82a9b023ce4f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=73f277df42db7db8092fbdde06cf8144 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a63bc6f8d1be025ce82640f95ffc0fbb 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8a90c035fad8640ab3cf1620b90ac05b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_initiated_login-8a7541151582487dd21f8381207e25fd.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=fe75b2e60c9b96cb0db5d1fa06373a4f 2500w" />
</Frame>

1. Click "Save" to persist the changes.

The Okta configuration is now complete.

## Configure Okta in Datafold

To finish the configuration, create an Okta integration in Datafold.

To complete the integration in Datafold, create a new integration by navigating to **Settings** → **Integrations** → **SSO** → **Add new integration** → **Okta**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=805f5b088b6fb89000adb5533c4df0da" data-og-width="2072" width="2072" data-og-height="762" height="762" data-path="images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=840215cc19908a03df300dd3100c2952 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a40fcabb66de9c8003303075dc3c64f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b5c462ec60a76a86f944a98bae702e05 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a7531d669ae279ed8749e1eb93b4219a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0ff47734f6144b3494b6d7220ce41c61 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_create-8269c208d4fa7df43a8c5ad99e675297.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5d439d069e5acc348e9897de5d21182e 2500w" />
</Frame>

* Paste in your Okta **Client Id** and **Client Secret**.
* The **Metadata Url** of Okta OAuth server is `https://<okta-server-name>/.well-known/openid-configuration`, replace `okta-server-name` with the name of your Okta domain.
* If you'd like to auto-create users in Datafold that are authorized in Okta, enable the **Allow Okta to auto-create users in Organization** switch.
* Finally, click **Save**.

<Tip>
  **TIP**

  Users can either be explicitly invited in Datafold by an admin user, using the same email as used in Okta, or they can be auto-created. When the `signup` action is set in the login URI, authenticated users on Okta who have been assigned as a user in Okta of the Datafold application will then be able to login. If that user has not yet been invited, Datafold will then automatically create a user for them, since they're already authenticated by the Okta server of your domain. The user will then receive an email to confirm their email address.
</Tip>

## Synchronize state with Datafold \[Optional]

This step is essential if you want to ensure that users from your organization are automatically logged out when they are unassigned or deactivated in Okta.

1. Navigate to **Okta Admin panel** → **Workflow** → **Event Hooks**
2. Click **Create Event Hook**
3. Set **Name** to `Datafold`
4. Set **URL** to `https://app.datafold.com/hooks/oauth/okta/<client-id>`
5. Set **Authentication field** to `secret`
6. Go to Datafold and generate a secret token in **Settings** → **Integrations** → **SSO** → **Okta**. Click the **Generate** button, copy it by using the **Copy** button and click **Save**. Use the pasted code in the **Authentication secret** field in Okta.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=36e3752ce79f7e792d543efcb9012fc0" data-og-width="1756" width="1756" data-og-height="216" height="216" data-path="images/generate_token_input-3ef82f777565226aa5da10b52464549e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=42cdb90429a3a9c1ac36888fc9277617 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bf21a126379a58a2fa8dd94bd21cd30c 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ca29ed5c6a2fd6a7dfebc34891031ebb 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c06e7ece043a1c514be15aaa9484b529 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3c20b9682b00d32fdd6cb6ee2625dacc 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/generate_token_input-3ef82f777565226aa5da10b52464549e.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=da00aaac4c96e48594c0bde2039ce3ef 2500w" />
</Frame>

<Warning>
  **CAUTION**

  Keep this secret token safe as you won't be able to see after saving your Integration.
</Warning>

7. In **Subscribe to events** add events: `User suspended`, `User deactivated`, `Deactivate application`, `User unassigned from app`
8. Click **Save & Continue**

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aa1f13e3d70bef5f4a2660eb91da93cd" data-og-width="1466" width="1466" data-og-height="1484" height="1484" data-path="images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f61f0553001c73c059076e15531fa8d 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1fb17f3a93e18e547fa114cc75a34390 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=086e57959bf93c73d5c0dae7ecc5262f 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7e2739c1430dd272623cf379caeda9bc 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6126ae5abd4292a7386a5bd21afca293 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/config_okta_event_hooks-ed108690a4e2e94d8158527dcc2f4196.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=38ef84c1a464f499ee3d02ab6c66a0ff 2500w" />
</Frame>

. On **Verify Endpoint Ownership** click **Verify**

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=697f26bc7f857a68847d006d0fa4d9c7" data-og-width="1368" width="1368" data-og-height="650" height="650" data-path="images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=5a2317b502377f247113237261a3d467 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=df89bf3c345b9d9445864a73199931fe 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f24c0068d11085cea226aa4f527a1540 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=63658165aaf8da903275cda34e0efb55 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=bcbb4899597517b563e03c3388725a29 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/verify_okta_event_hooks-57c17ee772834faf39e6c7689743d1f5.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=c0d3d8173cd58326b94639dcb77cc066 2500w" />
</Frame>

* If the verification is successful, you have completed the setup.

## Testing the Okta integration

<Tabs>
  <Tab title="SaaS">
    * Visit [https://app.datafold.com](https://app.datafold.com)
    * Type in your email and wait up to five seconds.
    * The Okta button should switch from disabled to enabled.
    * Click the Okta login button.
    * The browser should be redirected to your Okta domain, authenticate the user there and be redirected back to the Datafold application.
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    * Visit `https://your-dns-name`, replacing your-dns-name with the domain name of your installation.
    * Type in your email and wait up to five seconds.
    * The Okta button should switch from disabled to enabled.
    * Click the Okta login button.
    * The browser should be redirected to your Okta domain, authenticate the user there and be redirected back to the Datafold application.
  </Tab>
</Tabs>

If this didn't work, pay close attention to any error messages, or contact `support@datafold.com`.


# SAML
Source: https://docs.datafold.com/security/single-sign-on/saml

SAML (Security Assertion Markup Language) is a protocol that enables secure user authentication by integrating Identity Providers (IdPs) with Service Providers (SPs).

<Info>
  **NOTE**

  SAML SSO is available for both SaaS and VPC installations of Datafold.
</Info>

In this case, Datafold is the service provider. The Identity Providers can be anything used by the organization (e.g., Google, Okta, Duo).

We also support SAML SSO [group provisioning](/security/single-sign-on/saml/group-provisioning).

## Generic SAML Identity Providers

<Tip>
  **TIP**

  We also provide SAML identity providers configurations for ([Okta](/security/single-sign-on/saml/examples/okta), [Microsoft Entra ID](/security/single-sign-on/saml/examples/microsoft-entra-id-configuration), and [Google](/security/single-sign-on/saml/examples/google))
</Tip>

To configure a SAML provider:

1. Go to `Datafold`. Create a new integration by navigating to **Settings** → **Integrations** → **SSO** → **Add new integration** → **SAML**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d664571269b205f66ed0bfb051107a91" data-og-width="2088" width="2088" data-og-height="1452" height="1452" data-path="images/saml_create-3716c6fe01352ea69c647a7856adf189.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=76044b6a16ff8722c525b333d51fbd12 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa234c47b6a466e6cba5e6ab39b26651 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a6dc91b3981557cbe15b08e888a42aa 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93bfe67c8679b40af1d1f92daac66ad2 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=642e67455b35e8e364736f993039efbf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=242b9f474139a637af404a556c3746f2 2500w" />
</Frame>

1. Go to the organization's `Identity Provider`, create a **SAML application** (sometimes called a **single sign-on** or **SSO** method).

If you have the option, enable the SAML Response signature and set it to **whole-response signing**.

1. Copy and paste the Service Provider URLs from the `Datafold` SAML Integration into the `Identity Provider`'s application setup. The only two mandatory fields are **Service Provider Entity ID** and the **Service Provider ACS URL**.

After creation, The `Identity Provider` will show you the metadata XML. It may be presented as raw XML, a URL to the XML, or an XML file to download.

<Info>
  **INFO**

  The Identity Providers sometimes provide additional parameters, such as SSO URLs, ACS URLs, SLO URLs, etc. We gather this information from the XML directly so these can be safely ignored.
</Info>

1. Paste either the **metadata XML** *or* **metadata URL** from your `Identity Provider` into the respective `Datafold` SAML integration fields.
2. Finally, click the **Save** button to create the integration.

After creation, the SAML login button will be available for Datafold users in your organization.

1. In your `Identity Provider`, activate the SAML application for all users or for select groups.

<Warning>
  **CAUTION**

  Only configured users in your identity provider will be able to login into Datafold *using* SAML SSO.
</Warning>

### Auto-create users in Datafold

Go to `Datafold` and navigate to **Settings** → **Integrations** → **SSO** → **SAML**.

Enable the **Allow SAML to auto-create users in Organization** switch and save the integration.

<Tabs>
  <Tab title="SaaS">
    If the **Allow SAML to auto-create users in Organization** switch from the SAML Integration in Datafold is enabled, identity provider-initiated logins will automatically create users in Datafold for authenticated users.
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    If the **Allow SAML to auto-create users in Organization** switch from the SAML Integration in Datafold is enabled, the SAML login button will always be enabled, and all authenticated users will be automatically created in Datafold.
  </Tab>
</Tabs>


# Google
Source: https://docs.datafold.com/security/single-sign-on/saml/examples/google



## Google as a SAML Identity Provider

Enable SAML in your Google Workspace. Check [Set up your own custom SAML app](https://support.google.com/a/answer/6087519?hl=en) for more details.

<Warning>
  **CAUTION**

  You need to be a **super-admin** in the Google Workspace to configure a SAML application.
</Warning>

* Go to `Google`, click on **Download Metadata** in the left sidebar and **copy** the XML.
* Select **Email** as the Name ID format.
* Select **Basic Information > Primary email** as the Name ID.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8d366ab86b7b5ea4da4f28610f663a7a" data-og-width="1036" width="1036" data-og-height="1092" height="1092" data-path="images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=031e650d4205833f3c37804f02f91163 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3e95a625f8140fa3eb94acc2d3bcd046 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5eadb572afb12e36279b4bb353f883d1 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e0b07aa098ee8c5109e157716a701447 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2f3e3605ac2301683f9b01f410ee8835 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8405af2810d95e13cb7cf2b851817f82 2500w" />
</Frame>

* Go to `Datafold` and create a new SSO integration. Navigate to **Settings** → **Integrations** → **Add new integration** → **SAML**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d664571269b205f66ed0bfb051107a91" data-og-width="2088" width="2088" data-og-height="1452" height="1452" data-path="images/saml_create-3716c6fe01352ea69c647a7856adf189.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=76044b6a16ff8722c525b333d51fbd12 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa234c47b6a466e6cba5e6ab39b26651 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a6dc91b3981557cbe15b08e888a42aa 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93bfe67c8679b40af1d1f92daac66ad2 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=642e67455b35e8e364736f993039efbf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=242b9f474139a637af404a556c3746f2 2500w" />
</Frame>

* Copy the read-only field **Service Provider ACS URL**, go to `Google` and paste it into **ACS URL**.
* Copy the read-only field **Service Provider Entity ID**, go to `Google` and paste it into **Entity ID**.
* Paste the **copied** XML into `Datafold`'s **Identity Provider Metadata XML** field.
* Click **Save** to create the integration.
* (Optional step) Configure the attribute mapping as follows:
  * **First Name** → `first_name`
  * **Last Name** → `last_name`

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ab8e093dd14d4ee27f8ace796fcbde82" data-og-width="710" width="710" data-og-height="454" height="454" data-path="images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7dd71eaebd2d6367b7b5ac4b4caeb567 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=86be5fdb3065ef5eeacdd5b5a8bfe13f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fc03a15b3ddf993248d758df5923d659 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ee4c189d5fde064c7c7ec80ede0214c 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2a2aa8ce965eb043a66b51cad1fe75b4 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=300534eb2e002dbeef1036a2c7a21bb0 2500w" />
</Frame>


# Microsoft Entra ID
Source: https://docs.datafold.com/security/single-sign-on/saml/examples/microsoft-entra-id-configuration



## Azure AD / Entra ID as a SAML Identity Provider

You can create an **Enterprise Application** and use that to configure access to Datafold. Click on **New application** and **Create your own application**.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f046f4325a41d25294d72b72bc7e7f32" data-og-width="1724" width="1724" data-og-height="1402" height="1402" data-path="images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=de93f751f26594bf7ceccae6faf8e77e 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=898fdf7626a40eb02aad3faf01df5ac2 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=51e99f275914f83519d44b439cc53a96 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6d2345fce559388084ea7c67b993a9f3 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2ccb5f8f0c12a7e52eee28f086dc3c9b 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseApp-ac80b4305fc06a4a80a45532d718710a.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=00c5efffa1fc825981f4cafa1e8f7446 2500w" />
</Frame>

**Copy** the **App Federation Metadata Url**.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c0e3cd95b03d1101df57c76076ad7b50" data-og-width="1334" width="1334" data-og-height="1798" height="1798" data-path="images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=026b9993d32dfe5bceac3978be48843c 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e5ba0a04ae8b5cc94a617c60af845a47 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=08e9563168b51212b2679b6fa6090e9f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0b776887156cc1c241e25abbdd399863 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9661eb58da718e492d8d3a3516c20046 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppInitialConfig-6d5935f0a7efeec4595856d5171c3182.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=39f380af3ef1d5835ffe852ce15a1f5b 2500w" />
</Frame>

Go to `Datafold` and create a new SSO integration. Navigate to **Settings** → **Integrations** → **Add new Integration** → **SAML**.

Paste the **copied** URL into **Identity Provider Metadata URL**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d664571269b205f66ed0bfb051107a91" data-og-width="2088" width="2088" data-og-height="1452" height="1452" data-path="images/saml_create-3716c6fe01352ea69c647a7856adf189.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=76044b6a16ff8722c525b333d51fbd12 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa234c47b6a466e6cba5e6ab39b26651 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a6dc91b3981557cbe15b08e888a42aa 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93bfe67c8679b40af1d1f92daac66ad2 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=642e67455b35e8e364736f993039efbf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=242b9f474139a637af404a556c3746f2 2500w" />
</Frame>

Go to `Azure` and edit the **Basic SAML Configuration** in your Enterprise App.

Copy from Datafold the read-only field **Service Provider ACS URL** and paste it into **Reply URL**.

Copy from Datafold the read-only field **Service Provider Entity ID** and paste it into **Identifier**.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=914fa717d4ab2ed87ffc04a67c99cf0e" data-og-width="1204" width="1204" data-og-height="1468" height="1468" data-path="images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6873da5c93e3285802f4baa7f63de352 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8d29d9e0220af510ca1f43012d733c6b 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ac5df0793d3e284d24dc3827f06259c6 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cbe142abb7edde1201f94f447eb837f3 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1559322e5f79844cdfc5b60b54162be4 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLConfig-f04cd556cd232163a85a3ff2e47e5e7e.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d457a8b558e1471283770e9c35b5570c 2500w" />
</Frame>

Go to `Datafold` and click **Save** to create the SAML integration.

Next, edit the **Attributes & Claims**. By default, the **Unique User Identifier** is already correctly set to `user.userprincipalname`. If you have multiple domains (i.e., `@datafold.com` and `@datafoldonmicrosoft.com`), please make sure this maps correctly to the email addresses of the users in Datafold.

(Optional step) Add two attributes: `first_name` and `last_name`.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0e1e60e7e3feeff95983c959da115188" data-og-width="1146" width="1146" data-og-height="682" height="682" data-path="images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=059871ba16b0dca0df447d4a96345169 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7f1f56994ee73a39f36f9df4b2975e97 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6e96d0da5262399f7a4307635acb2fce 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3b4ff99a38d1abc00139b71c39756cb6 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=557c9791479c726fbf9b85cd165804ca 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppSAMLAttribute-99692a9fa1d102a1eaa818d36c6b812e.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=07c12c1155388628296ca370e8230cfd 2500w" />
</Frame>

Finally, edit the **SAML Certificates**. Set the signing option to **Sign SAML response and assertion**.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8fd247f9d4d784561868cf9359a16d6f" data-og-width="1338" width="1338" data-og-height="602" height="602" data-path="images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f1766d6b5ba167419c6bb2d52d398a9e 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d0f09c10f614a3ea19e5b0641ecf2fac 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8faa2bc002e73892f79c8ebd6fcabc79 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1962a7fd24c571a4aa7a9fa0fdfc9454 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9be749d54d9e3d8a19fa7f9f991d4321 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/AzureEntraIDSAMLEnterpriseAppCertificates-c4582a0cf51f8dcdae03013810278e00.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9cea58d918d93857cba205444fedbbaa 2500w" />
</Frame>

After you made sure you are added as a user to the Enterprise Application, log out from Datafold. Click on **Test** under **Test single sign-on with DatafoldSSO**.

## Synchronize user with Datafold \[Optional]

This step is essential if you want to ensure that users from your organization are disabled if they are no longer assigned to the configured Microsoft Entra App.

1. Navigate to App registrations → API permissions.
2. Add the following permissions: `Group.Read.All` and `User.ReadBasic.All`.
   2.1 Click `Add a permission`.
   2.2 Select Microsoft Graph.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a720a15fa9d640f9391f8fab7c9211c0" data-og-width="1480" width="1480" data-og-height="866" height="866" data-path="images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a25702f6a99c94c2cdbf5bd3127ce974 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7f562bc34d34d354980b285c455ceffe 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5a683ac0aa1d92a51cfc323bf09f5b92 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a97a7878468733590510d7cf6974dcda 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a151bee4d4843e1a242d16b9305ff61e 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-e2efd77a0267ffe5f9fb14ef6be44c1f.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6ff7f11fc5d973b8473801e0e60fa825 2500w" />
</Frame>

2.3 Select application permissions and add the required permissions.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=13b9a24078632afb55d8c665f4e40f1f" data-og-width="1514" width="1514" data-og-height="834" height="834" data-path="images/2-00a764fe8abf4ef520abeaf7ae07d49e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e47cf793035c8d3adda0dfe576e73645 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=58930216ba894ce2ab91a95e363b2413 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4b0469c605fbcbcb6a8eef7c5e2b2eb1 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5bd6f5ac487bed1e3ca3dd12ff79537a 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bf2f7ac7b77c5a1414f53807864bb5f4 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-00a764fe8abf4ef520abeaf7ae07d49e.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c9310570c1f792009f9c0ab656ad63f6 2500w" />

  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fd83b4f6265f71cc3ca338d47104ada1" data-og-width="1506" width="1506" data-og-height="398" height="398" data-path="images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=651036156b7cc97e6ffaa7ddf75bfb19 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8735ba819b72607bb5961d95e2c4bc0d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=de9b2a3b4ec77e482e56fcc78863d98c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=698c12aa77ead7b1ea0bc165d2d64fc5 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f16f68e97dda83d07e0d6bcef17fa297 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-eadbef3fd2f9c1d0326ed8a9721c16c2.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c895f2b2fd4f783b242f8fefc05d6306 2500w" />
</Frame>

3. Grant admin consent.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fb0aa1f158f2aec6d6f4a1b3a081c20f" data-og-width="1580" width="1580" data-og-height="784" height="784" data-path="images/4-40f90f212a27572e669806bc36325bc7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=51ee70d63cf050166ae395368bde47c5 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1d169c59f4d35f2c981ebd100042d765 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8e13134c745e095000a314f5ca732224 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=97f61ab8401a3e7d45458fe8c4beec31 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1a76d9ba1937a7f05fbd2a810e902925 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-40f90f212a27572e669806bc36325bc7.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=114422090662fc1ae07dc5a095f9e79c 2500w" />
</Frame>

4. You should now see a <Icon icon="square-check" /> next to the permissions.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f28ea21f758290a2876d69fa51dc2da7" data-og-width="1544" width="1544" data-og-height="482" height="482" data-path="images/5-257e23569930de31a6168ac10aaf5bf3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b1d0875d532398d95008632958452b2e 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fa7943196a09d31f37b403fd4c99e35f 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4d7c28a4ea0369882cace5789d860e33 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=936d8a3fa927bb9d5f8ee3fcce5df48f 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5d926e9b710be602ffa685f6bdb84c27 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-257e23569930de31a6168ac10aaf5bf3.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=382fda0f951a59164bf7de038bd8a908 2500w" />
</Frame>

5. Generate a secret so that Datafold can interact with the API.
   5.1 Click `Certificates & secrets`.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=53b9bd989e8c0fabbe436dfd3464a1c1" data-og-width="2044" width="2044" data-og-height="446" height="446" data-path="images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e2f726689f11faddc7f0bc477b7b4d99 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5852df798cfd0208f65cb8e1ebbe44ce 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=74d8b57a302f04acc6c885f302c1e89c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6744fd8c2c8e689994b987a5da8540b1 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=336ff98fb4f3de13b872314e2b344a31 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-015ef3a0d51e4ee205d6bd5d5c888e8d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d9532ee1fda03cf024f2c06244453f5c 2500w" />
</Frame>

5.2 Click `New client secret`.
5.3 Type in a description and click `Add`.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=552b5f52d806aa8b90681cc449584711" data-og-width="1042" width="1042" data-og-height="478" height="478" data-path="images/7-a95118698bae900f1620b47905433fc4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=45b2016d891ab27ff93834e318e42a05 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4f061905fce7d16a58067712917b8d75 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d350b8860f9056026379653cf89f984e 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e72580916c2efb756d0f800bcf59c5e5 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=029758725feefdfd5ebe1bac525614bf 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-a95118698bae900f1620b47905433fc4.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5fb5b80a5c36cd7dd9b354cca544c872 2500w" />
</Frame>

6. Go to `Datafold` and navigate to **Settings** → **Integrations** → **SSO** → **Add new Integration** and select the Microsoft Entra ID Logo.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=53e7d8df3ed9743261d59ffb842bd934" data-og-width="2072" width="2072" data-og-height="622" height="622" data-path="images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=695f6ad6681d3b195df963e5d8e038bd 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=34c3175a4ce27ee1ffe2a24c0d2c78db 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=13861a8cce2a92c8c2026838abb41191 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=121071fbb10fbb61183e0480edfd08ae 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7c2fa73221f65be599a4a290d503bf35 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/8-bfcf9d1f0679293415dad2a9b7c5ef6c.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2782c0fb51f3237343f075d977442562 2500w" />
</Frame>

7. Paste in the four required fields:<br />
   7.1 Tenant ID - [you can find this in the overview page](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)<br />
   7.2 Navigate to the application overview<br />
   7.3 Copy Application ID and paste it into Client Id<br />
   7.4 Copy the secret we created in the previous steps and paste it into Client Secret<br />
   7.5 Navigate to the enterprise application and copy Object ID and paste it into Principal Id.<br />
   7.6 Click **Save** to create the integration.<br />

If the update is successful, it means that the integration is valid. Users that do not have access to the configured application will be disabled and logged out in at most one hour.


# Okta
Source: https://docs.datafold.com/security/single-sign-on/saml/examples/okta



## Okta as a SAML Identity Provider

You can create an **Application** and use that to configure access to Datafold. Click on **Applications** and **Create App Integration**.

Select **SAML 2.0**

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f1e88c43eab60863bde238f5a35e84b4" data-og-width="1928" width="1928" data-og-height="1198" height="1198" data-path="images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=065f897e1373c16c11d208f5b2684d96 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=38d8159b3000a9fd76a0f5532dc586c6 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=675cb8f5b2e908d9f4221dc25b813310 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=831e2ea74ba5dca9f7348506b074934a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a0c19c262a31a8e883560a0aa6ded124 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_2_0-f56d1d05fe14ca913026c4618dc1518b.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e27a73428efaded05ef86b01baa752a2 2500w" />
</Frame>

Enter "Datafold" in **App name** and click **Next**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c35496d4b016980452723e6f355c14af" data-og-width="1462" width="1462" data-og-height="760" height="760" data-path="images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=85dc7bb56960acbd31053e4d37283417 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b2dc3d43c79924382c5ef676b571d8f4 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1e9647f795b2a5b51d14f00884b49973 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d725841ce4aa54c45f252dfecc1f7293 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e903aad0df74a49abd4395a915b7c880 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_app_name-495773bcc2261378919673c58e49b91b.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=dd16b9331292f8f9da08aeb196aaaa3a 2500w" />
</Frame>

Go to `Datafold` and create a new SSO integration. Navigate to **Settings** → **Integrations** → **Add new Integration** → **SAML**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d664571269b205f66ed0bfb051107a91" data-og-width="2088" width="2088" data-og-height="1452" height="1452" data-path="images/saml_create-3716c6fe01352ea69c647a7856adf189.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=76044b6a16ff8722c525b333d51fbd12 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa234c47b6a466e6cba5e6ab39b26651 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a6dc91b3981557cbe15b08e888a42aa 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93bfe67c8679b40af1d1f92daac66ad2 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=642e67455b35e8e364736f993039efbf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=242b9f474139a637af404a556c3746f2 2500w" />
</Frame>

* Copy the read-only field **Service Provider ACS URL** and paste it into **Single sign-on URL**.
* Copy the read-only field **Service Provider Entity ID** and paste it into **Audience URI (SP Entity ID)**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3d7efa5d1edc4303f2e99ab252ca37a3" data-og-width="1454" width="1454" data-og-height="1222" height="1222" data-path="images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b56b79c5f7aa164461fb2da87b525a34 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aec39beb8a250784523b42e83b7aa1f7 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9593f9bec36d853f25b850c3bf307cf1 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f3fd976dd4c320182bb1dcc2ca26261c 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6726530e699a933d97de7fcefd4d3b4c 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_settings1-a3440ff6356c33c17b630039f9d0401f.jpeg?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e46220fe1a58e0462739b0cecd690aa2 2500w" />
</Frame>

(Optional step) In **Attribute Statements (optional)** add fields:

* Name: `first_name`, Value: `user.firstName`
* Name: `last_name`, Value: `user.lastName`

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=45f14e02b732212e1b2258fd00348222" data-og-width="1472" width="1472" data-og-height="628" height="628" data-path="images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ea6a4db29e1c55bcb0bf8440a5de5ee3 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ed79b3805fbee166406fd3d779b2a5ee 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2f52e463d4f9e579aa89b3ab0cd9fcff 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c91dec1834154752b7a2719cfa481513 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9923abb0b0479c0efb7b21ca6692e487 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_attr_statements-e51a953c5ef2853fdbd6821d07322e9f.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2dbe632c9fd07ab9ebbbab9172e9153c 2500w" />
</Frame>

Click **Next** and **Finish**.

Go to `Okta` and copy the **Metadata URL** field from **Datafold** → **Sign On** → **Metadata details**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7cfdd7e54f625e288fab124fb02c8019" data-og-width="1448" width="1448" data-og-height="1530" height="1530" data-path="images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4b1bdad40566ec0bf868e4143fc9a843 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=067c83302e8cee16196f10c81c4817a1 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ac9ee21d6d5576085261a91ca7f9c2d6 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e5565b1d8ec44206b8b57bf4eeea0fd7 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0756e1590df84c626664362699098951 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_saml_meta_url-137efd7dd40576337ee02f984c8841bc.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=56a76605830ededd38d07f7828b88842 2500w" />
</Frame>

Go back to `Datafold` and paste it into **Identity Provider Metadata URL** field.

Finally, click **Save** to create the integration.

Navigate to **Settings** → **Integrations** → **SSO** → **SAML**.

If everything is correct, the **Identity Provider Metadata XML** field will contain XML.


# null
Source: https://docs.datafold.com/security/single-sign-on/saml/group-provisioning

Automatically sync group membership with your SAML Identity Provider (IdP).

## 1. Create desired groups in the IdP

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7b1a4b911b31f70a7d7db3b95739586c" data-og-width="2206" width="2206" data-og-height="1138" height="1138" data-path="images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ea9ebef6fb14013d8e93b161c30a1c0f 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5d9c07e5cf547a9638b5c766696d95bd 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7fd3d8be8c721165c57b80f415645e71 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2c0eef63671955ee29df544c44c0be8a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6ca9d7d82602d721f63b1b73bdb20a70 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0234e8f1489f0f5e752db118555790b5 2500w" />
</Frame>

## 2. Assign the desired users to groups

Assign the relevant users to groups reflecting their roles and permissions.

## 3. Configure the SAML SSO provider

Configure your SAML SSO provider to include a `groups` attribute. This attribute should list all the groups you want to sync.

```Bash  theme={null}
  <saml2:Attribute Name="groups" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified"><saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">datafold_admin</saml2:AttributeValue><saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">datafold_read_write</saml2:AttributeValue></saml2:Attribute></saml2:AttributeStatement></saml2:Assertion></saml2p:Response>
```

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7754980607aca71912bd8372bd5500a4" data-og-width="1536" width="1536" data-og-height="580" height="580" data-path="images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0cb877d6a9f30c6c6ec70faa455c783c 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5b77cb7d1f4495562e6ee8878fc4ff60 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=52e4c47f3d047b82818692b39cd9afd2 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e00c227f7a09d308161b6b9420cb21db 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=53a08b08ee61f52f31390974cb5c63e0 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4f4c1fb489b45a227cf379b42065ab2c 2500w" />
</Frame>

## 4. Map IdP groups to Datafold groups

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=30af41ee0d9f1d6d35f0f5103e7df359" data-og-width="1534" width="1534" data-og-height="828" height="828" data-path="images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=aafe7736b71c01e627d381a3a92c86e5 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=95366201a0c794119c68cff9a4bf0152 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c6799569133c31debca635d36199a38e 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2cf8a00fba05fd8832e016c6f636cd91 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9ab032dd79103de6d0d03629277a117b 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9e9ba0246f56f34ca8ee3fdd2a891000 2500w" />
</Frame>

The `datafold_admin` group, created in the IdP through [step 1](#1-create-desired-groups-in-the-idp), will be automatically synced. Users in this IdP group will also be members of the corresponding group in Datafold.

**Note:** Manual Datafold user group memberships will be overridden upon the user's next login to Datafold. Therefore, group memberships should be managed exclusively within the IdP once the `groups` attribute is configured.

## Example configuration

Here's how you might configure three groups to map to the three default Datafold groups, `admin`, `default` and `viewonly`:

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c2f082b931c0619c6c740eb0269f2a48" data-og-width="1934" width="1934" data-og-height="758" height="758" data-path="images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9615a1b078a16f35ccdefadf3ef858ad 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3244a994952564cdbdda2f48bb3bc5c9 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c83f2424d4872e9da9b7e613a5a3b95a 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b68cfadcee9109ac44efea44bec022e4 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4efb937d6fda70251701bcb3e0960e0e 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b1573c190d7ce95d53bb126532c0c02e 2500w" />
</Frame>


# User Roles and Permissions
Source: https://docs.datafold.com/security/user-roles-and-permissions

Datafold uses role-based access control to manage user permissions and actions.

Datafold has three default roles:

| Role     | Description    | Permissions                                                                                          |
| -------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| default  | Full user role | Create and modify monitors, create diffs, explore data and lineage                                   |
| admin    | Administrator  | Default permissions plus the ability to manage users and configurations such as database connections |
| viewonly | View-only role | View diffs and monitors without the ability to create or modify them                                 |


# FAQ
Source: https://docs.datafold.com/support/faq-redirect





# Support
Source: https://docs.datafold.com/support/support

Datafold offers multiple support channels to assist users with troubleshooting and inquiries.

## Datafold Support

* **Email**: Contact support at [support@datafold.com](mailto:support@datafold.com) for any assistance.
* **In-app Chat**: Reach out directly from the Datafold app via live chat for quick help.
* **Shared Slack Channel**: Collaborate with the Datafold team through a dedicated Slack channel (please inquire with your account executive to set up).
* **FAQ**: Explore our [Frequently Asked Questions](/faq/overview) for detailed answers to common queries and troubleshooting tips.

### Grant access to Datafold's team for troubleshooting

For faster resolution of support issues, you can temporarily grant Datafold Support access to your account. This enables a Datafold team member to view the same in-app context as you, minimizing back-and-forth communication.

To grant access:

1. Navigate to **Settings** → **Org Settings**.
2. Check the box next to *"Allow Datafold access to your account for troubleshooting purposes."*

To revoke access, simply uncheck the box at any time.

<Info>
  **Note:** Admin privileges are required to modify this setting in Org Settings.
</Info>


# Welcome
Source: https://docs.datafold.com/welcome

Datafold is the unified platform proactive data quality that combines automated data testing, data reconciliation, and observability to help data teams prevent data quality issues and accelerate their development velocity.

## Why Datafold?

Datafold automates the most error-prone and time-consuming aspects of the data engineering workflow by **preventing and detecting data quality issues**. In addition to standard observability features like monitoring, profiling, and lineage, we integrate deeply into the development cycle with automated CI/CD testing. This enables data teams to prevent bad code deployments and detect issues upstream of the data warehouse.

Whether it's for [CI/CD testing](deployment-testing/how-it-works) or [data migration automation](data-migration-automation), Datafold ensures data quality at every stage of the data pipeline.

## Key features

Data quality is a complex and multifaceted problem. Datafold’s unified platform helps embed proactive data quality testing in your workflows:

<CardGroup cols={2}>
  <Card title="Data Diffs" href="/data-diff/what-is-data-diff" horizontal>
    Use value-level data diffs to isolate and identify changes in your data. Catch unintended modifications before they disrupt production or downstream data usage.
  </Card>

  <Card title="Data Monitors" href="/data-monitoring/monitor-types" horizontal>
    Create monitors for data diffs, data quality metrics, SQL metrics, SQL rules, and schema changes to send alerts when inconsistencies are detected.
  </Card>

  <Card title="Datafold Migration Agent" href="/data-migration-automation" horizontal>
    Discover how DMA provides full-cycle migration automation with SQL code translation and cross-database validation.
  </Card>

  <Card title="Data Explorer & Column-Level Lineage" href="/data-explorer/how-it-works" horizontal>
    Learn how your data assets move and change across systems with column-level lineage, metadata, and profiles, to track the impacts of changes made upstream.
  </Card>
</CardGroup>

## Use cases

<CardGroup cols={3}>
  <Card title="CI/CD Data Testing" href="" horizontal>
    Catch data quality issues early with automated testing during development and deployment.
  </Card>

  <Card title="Accelerated Data Migrations" href="" horizontal>
    Speed up migrations with our full-cycle migration automation solution for data teams.
  </Card>

  <Card title="Data Monitoring & Observability" href="" horizontal>
    Shift monitoring upstream to proactively prevent disruptions and ensure data quality.
  </Card>
</CardGroup>

## Getting started

There are a few ways to get started with your first data diff:

<Steps>
  <Step title="Create a data diff" stepNumber="1">
    Once you’ve integrated a [data connection](/integrations) and [code repository](/integrations/code-repositories), you can run a new [in-database](/data-diff/in-database-diffing/creating-a-new-data-diff) or [cross-database](/data-diff/cross-database-diffing/creating-a-new-data-diff) data diff or explore your [data lineage](data-explorer/lineage).
  </Step>
</Steps>

<Steps>
  <Step title="Create automated monitors" stepNumber="2">
    Create [monitors](data-monitoring/monitor-types) to send alerts when data diffs fall outside predefined ranges.
  </Step>
</Steps>

<Steps>
  <Step title="Set up CI/CD testing" stepNumber="3">
    Get started with deployment testing through our universal ([No-Code](deployment-testing/getting-started/universal/no-code), [API](deployment-testing/getting-started/universal/api)) or [dbt](integrations/orchestrators/dbt-core) integrations.
  </Step>
</Steps>

## Learn more

Curious to learn more about why and how data quality matters? We wrote a whole guide (with illustrations of medieval castles, moats, and knights) called the [Data Quality Guide](https://www.datafold.com/data-quality-guide) which covers:

* A practical roadmap towards creating a robust data quality system
* Data quality metrics to keep, and metrics to ignore
* Nurturing a strong data quality culture within and beyond data teams


