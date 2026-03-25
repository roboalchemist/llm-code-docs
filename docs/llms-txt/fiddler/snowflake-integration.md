# Source: https://docs.fiddler.ai/integrations/data-platforms-and-pipelines/data-platforms/snowflake-integration.md

# Snowflake

In this article, we will be looking at loading data from Snowflake tables and using the data for the following tasks:

1. Onboarding a model to Fiddler
2. Uploading baseline data to Fiddler
3. Publishing production data to Fiddler

## Import data from Snowflake

In order to import data from Snowflake to a Jupyter notebook, we will use the snowflake library which can be installed using the following command in your Python environment.

```python
pip install snowflake-connector-python
```

The following information is required in order to establish a connection to Snowflake:

* Snowflake Warehouse
* Snowflake Role
* Snowflake Account
* Snowflake User
* Snowflake Password

These values can be obtained from your Snowflake account under the ‘Admin’ option in the Menu as shown below or by running the queries below:

* Warehouse - select CURRENT\_WAREHOUSE()
* Role - select CURRENT\_ROLE()
* Account - select CURRENT\_ACCOUNT()

'User' and 'Password' are the same that you use when logging in to your Snowflake account.

![Example Snowflake dashboard showing the Warehouse tab.](https://1800696242-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkcq97TxAnbTVaNJOQHbQ%2Fuploads%2Fgit-blob-f19f86ebeff75f15117eee3a8de9b47cdfcfda3c%2Fc2f4cf4-screen-shot-2022-06-14-at-41736-pm.png?alt=media)

Once you have this information, you can set up a Snowflake connector using the following code:

```python
# establish Snowflake connection
connection = connector.connect(
  user=snowflake_username,
  password=snowflake_password,
  account=snowflake_account,
  role=snowflake_role,
  warehouse=snowflake_warehouse
)
```

You can then write a custom SQL query and import the data to a pandas dataframe.

```python
# sample SQL query
sql_query = 'select * from FIDDLER.FIDDLER_SCHEMA.CHURN_BASELINE LIMIT 100'

# create cursor object
cursor = connection.cursor()

# execute SQL query inside Snowflake
cursor.execute(sql_query)

baseline_df = cursor.fetch_pandas_all()
```

## Publish Production Events

Now that we have data imported from Snowflake to a dataframe, we can refer to the following pages to:

1. [Onboard a model](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference/model-onboarding/create-a-project-and-model) using the baseline dataset for the model schema inference sample.
2. [Upload a Baseline dataset](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference/publishing-production-data/creating-a-baseline-dataset), which is optional but recommended for monitoring comparisons.
3. [Publish production events](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference/publishing-production-data) for continuous monitoring.
