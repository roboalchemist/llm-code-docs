# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/copy-models.md

# Copy Document AI models between databases, schemas, and accounts

This topic explains how to copy Document AI models between databases or schemas in the same account or between different accounts in the same organization.
For example, you might want to copy a model from a development account to a production account.

Document AI stores any published or trained models within the model registry, which you can use to store and manage model versions
and model replication. For more information about the capabilities of the model registry, see [Snowflake Model Registry](../../../developer-guide/snowflake-ml/model-registry/overview.md).

> **Note:**
>
> You can’t replicate a Document AI model build (which includes the model, the data values to be extracted, and the documents uploaded
> to test and train the model). You can replicate only the model that was either published or trained out of a Document AI model build.
>
> [Sharing models](../../../developer-guide/snowflake-ml/model-registry/overview.md) is not currently supported for Document AI.

> **Important:**
>
> When using the [CREATE MODEL](../../../sql-reference/sql/create-model.md) and the [ALTER MODEL … ADD VERSION](../../../sql-reference/sql/alter-model-add-version.md) commands with Document AI models,
> ensure that the version identifier is in the form of `V<integer>` (for example, `V2`) so that you can use
> the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method. Note that the integer corresponds to the version of the
> Document AI model build that you published or trained.

## Prerequisites

To copy a model, you must:

* Grant all the privileges required to work with Document AI. For more information about the privileges, see [Document AI access control](setting-up.md).

  > **Note:**
  >
  > You must grant the CREATE MODEL privilege on any schema to which you copy a model.
* Publish or train the source model. For more information, see [Publish a Document AI model build](prepare-model-build.md).

## Copy Document AI models between databases and/or schemas within an account

1. Create the model from the source model using the role that created the source model:

   ```sqlexample
   CREATE MODEL prod_doc_ai_db.prod_doc_ai_schema.invoices_model
     WITH VERSION V1
     FROM MODEL dev_doc_ai_db.dev_doc_ai_schema.invoices_source_model
       VERSION V1;
   ```

2. Optional: Add another version of the model:

   ```sqlexample
   ALTER MODEL prod_doc_ai_db.prod_doc_ai_schema.invoices_model
     ADD VERSION V2
     FROM MODEL dev_doc_ai_db.dev_doc_ai_schema.invoices_source_model
       VERSION V2;
   ```

3. To enable the `prod_user` role to use the copied model, grant the OWNERSHIP privilege on the model to that role:

   ```sqlexample
   GRANT OWNERSHIP ON MODEL prod_doc_ai_db.prod_doc_ai_schema.invoices_model
     TO ROLE prod_user;
   ```

## Copy Document AI models between accounts

You can replicate a Document AI model from a source account to one or more target accounts in the same organization.
For more information about replication, see [Introduction to replication and failover across multiple accounts](../../account-replication-intro.md).

To replicate the model from a source account to a target account, you need to create a replication group in the source account to enable replication of the database
in which the model was created to a target account, and set up the production user role.

> **Note:**
>
> You must be a user with the ACCOUNTADMIN role to create a replication group and to set up the production user role.

### Replicate the database in which the model was created

> **Note:**
>
> If all of your model builds are stored in the same database, you only need to replicate that database once.

1. Create a primary replication group in the source account:

   ```sqlexample
   CREATE REPLICATION GROUP doc_ai_models_replication_group
   OBJECT_TYPES = DATABASES
   ALLOWED_DATABASES = dev_doc_ai_db
   ALLOWED_ACCOUNTS = org.production_account;
   ```

2. Create a secondary replication group in a target account as a replica of the primary replication group in the source account:

   ```sqlexample
   CREATE REPLICATION GROUP doc_ai_models_secondary_replication_group
   AS REPLICA OF org.dev_account.doc_ai_models_replication_group;
   ```

3. Refresh the database in the target account from the source account:

   ```sqlexample
   ALTER REPLICATION GROUP doc_ai_models_secondary_replication_group REFRESH;
   ```

4. Optional: Specify the schedule for refreshing the secondary replication group so that the account is synchronized automatically every 10 minutes:

   ```sqlexample
   ALTER REPLICATION GROUP doc_ai_models_secondary_replication_group
     SET REPLICATION_SCHEDULE = '10 MINUTE';
   ```

### Set up the production user role for information extraction

To ensure that the user working on the target production account (for example, a user with the `prod_user` role) can run
the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method using the replicated model, follow these steps:

1. Grant all the [privileges required](setting-up.md) for working with Document AI on the copied database and schema to the `prod_user` role.
2. Grant the USAGE privilege on the source database and schema, and ownership on all models in that schema, to the `prod_user` role:

   ```sqlexample
   GRANT USAGE ON DATABASE dev_doc_ai_db TO ROLE prod_user;
   GRANT USAGE ON SCHEMA dev_doc_ai_db.dev_doc_ai_schema TO ROLE prod_user;
   GRANT OWNERSHIP ON ALL MODELS IN SCHEMA dev_doc_ai_db.dev_doc_ai_schema TO ROLE prod_user;
   ```

3. Optional: Grant ownership on all the future models that will be replicated:

   ```sqlexample
   GRANT OWNERSHIP ON ALL FUTURE MODELS IN SCHEMA dev_doc_ai_db.dev_doc_ai_schema TO ROLE prod_user;
   ```

After you grant the required privileges, a user with the `prod_user` role must follow these steps:

1. Create the model from the source model:

   ```sqlexample
   CREATE MODEL prod_doc_ai_db.prod_doc_ai_schema.invoices_model
     WITH VERSION V1
     FROM MODEL dev_doc_ai_db.dev_doc_ai_schema.invoices_source_model
       VERSION V1;
   ```

   > **Note:**
   >
   > You must create the model from the source model. You can’t call the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method
   > directly on the model stored in the replicated database in the target (production) account.

   With the `prod_user` role, you can now extract information using the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method in the
   target (production) account.
2. Optional: Add another version of the model:

   ```sqlexample
   ALTER MODEL prod_doc_ai_db.prod_doc_ai_schema.invoices_model
     ADD VERSION V2
     FROM MODEL dev_doc_ai_db.dev_doc_ai_schema.invoices_source_model
       VERSION V2;
   ```

## Additional notes

* A new version of the model is not automatically copied after training. You must add the version manually using
  the [ALTER MODEL … ADD VERSION](../../../sql-reference/sql/alter-model-add-version.md) command.
* The copied model is not visible in the Document AI UI because it can’t be re-trained. You can see the copied model in the [Snowflake Model Registry user interface](../../../developer-guide/snowflake-ml/model-registry/snowsight-ui.md), and you can call the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method on that model.
* After the OWNERSHIP privilege is granted on the model to the production user role, you can’t change the ownership. To enable another role to use the model after the Document AI model build is published, copy the Document AI model, and grant the OWNERSHIP privilege on the copied model to that role.
