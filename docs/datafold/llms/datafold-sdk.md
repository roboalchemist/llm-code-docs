# Source: https://docs.datafold.com/api-reference/datafold-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Datafold SDK

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
