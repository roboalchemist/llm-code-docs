# Source: https://docs.aporia.com/data-sources/glue-data-catalog.md

# Source: https://docs.aporia.com/v1/data-sources/glue-data-catalog.md

# Glue Data Catalog

This guide describes how to use the Glue Data Catalog data source in order to monitor a new ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried exist as tables in Glue Data Catalog. This data source may also be used to connect to your model's training/test set to be used as a baseline for model monitoring.

### Create a IAM role for Glue access

#### Step 1: Create Role

1. Log into your AWS Console and go to the **IAM** console.
2. Click the **Roles** tab in the sidebar.
3. Click **Create role**.
4. In **Select type of trusted entity**, click the **Web Identity** tile.&#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2Fz60g25BU6vTMjkxoCxh0%2Faws-select-trusted-entity.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Under **Identity Provider**, click on **Create New**.
6. Under **Provider Type**, click the **OpenID Connect** tile.
7. In the **Provider URL** field, enter the Aporia cluster OIDC URL.
8. In the Audience field, enter "sts.amazonaws.com".
9. Click the **Add provider** button.
10. Close the new tab
11. Refresh the **Identity Provider** list.
12. Select the newly created identity provider.
13. In the **Audience** field, select “sts.amazonaws.com”.
14. Click the **Next** button.
15. Click the **Next** button.
16. In the **Role name** field, enter a role name.\
    &#x20;

    <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F08JmYjE2IHOX3iRiB2xG%2Faws-role-name.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Step 2: Create an access policy

1. In the list of roles, click the role you created.
2. Add an inline policy.
3. On the Permissions tab, click **Add permissions** then click **Create inline policy**.&#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FLf9zzxpNtYRN0uIWWSW6%2Faws-add-permissions.png?alt=media" alt=""><figcaption></figcaption></figure>
4. In the policy editor, click the **JSON** tab.\
   &#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FOATD3tYRzteARRLesFd0%2Fjson.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Copy the following access policy, and make sure to fill your correct region, account ID and restrict access to specific databases and tables if necessary.

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "glue:GetConnections"
               ],
               "Resource": [
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:catalog",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:connection/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "glue:GetDatabase",
                   "glue:GetDatabases"
               ],
               "Resource": [
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:catalog",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:database/default",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:database/global_temp",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:database/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "glue:GetTable",
                   "glue:GetTables",
                   "glue:GetPartitions",
                   "glue:GetPartition",
                   "glue:SearchTables"
               ],
               "Resource": [
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:catalog",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:database/*",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:table/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "glue:GetUserDefinedFunctions"
               ],
               "Resource": [
                   "*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "glue:CreateDatabase"
               ],
               "Resource": [
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:catalog",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:database/default",
                   "arn:aws:glue:<REGION>:<ACCOUNT_ID>:database/global_temp"
               ]
           }
       ]
   }
   ```
6. Click **Review Policy**.
7. In the **Name** field, enter a policy name.
8. Click **Create policy**.
9. If you use Service Control Policies to deny certain actions at the AWS account level, ensure that `sts:AssumeRoleWithWebIdentity` is allowlisted so Aporia can assume the cross-account role.
10. In the role summary, copy the **Role ARN**.

Next, please provide your Aporia account manager with the Role ARN for the role you've just created.

### Creating a Glue Data Catalog data source in Aporia

To create a new model to be monitored in Aporia, you can call the `aporia.create_model(...)` API:

```python
aporia.create_model("<MODEL_ID>", "<MODEL_NAME>")
```

Each model in Aporia contains different **Model Versions**. When you (re)train your model, you should create a new model version in Aporia.

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="binary"
  
  raw_inputs={
    "raw_text": "text",
  },

  features={
    "amount": "numeric",
    "owner": "string",
    "is_new": "boolean",
    "embeddings": {"type": "tensor", "dimensions": [768]},
  },

  predictions={
    "will_buy_insurance": "boolean",
    "proba": "numeric",
  },
)
```

Each raw input, feature or prediction is mapped by default to the column of the same name in the Glue table.

By creating a feature named `amount` or a prediction named `proba`, for example, Aporia will expect a column in the table named `amount` or `proba`, respectively.

If your data format does not fit exactly, you can use Spark SQL queries to shape it in any way you want.

Next, create an instance of `GlueDataSource` and pass it to `apr_model.connect_serving(...)` or `apr_model.connect_training(...)`:

```python
apr_model.connect_serving(
  data_source=GlueDataSource(
    query="SELECT * FROM model_db.model_predictions",
  ),

  # Names of the prediction ID and prediction timestamp columns
  id_column="prediction_id",
  timestamp_column="prediction_timestamp",
)
```

Note that as part of the `connect_serving` API, you are required to specify additional 2 columns:

* `id_column` - A unique ID to represent this prediction.
* `timestamp_column` - A column representing when did this prediction occur.

### What's Next

For more information on:

* Advanced feature / prediction <-> column mapping
* How to integrate delayed actuals
* How to integrate training / test sets

Please see the [Data Sources Overview](https://docs.aporia.com/v1/data-sources) page.
