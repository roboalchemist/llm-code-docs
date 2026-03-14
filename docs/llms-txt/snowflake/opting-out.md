# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out.md

# Opt out of Snowflake AI features

Most Snowflake AI features are initially available to all users in your Snowflake account. Access to most features is
controlled by the SNOWFLAKE.CORTEX_USER database role, which is initially granted to the PUBLIC role. All users are
granted the PUBLIC role, giving them access to Cortex features by default. (Access to Snowflake Copilot is controlled by
the SNOWFLAKE.COPILOT_USER database role, also granted to PUBLIC by default.) Two features, Cortex Analyst and Document
AI, are opt-in features that are not accessible to users by default.

## Opt out of default features

To revoke access to all Snowflake AI features that are available to users by default, revoke the SNOWFLAKE.CORTEX_USER and
SNOWFLAKE.COPILOT_USER database roles from the PUBLIC role. You can grant these roles to specific roles that you want to have
access to the features, then grant those roles to specific users as needed. (You cannot grant database roles
directly to users, but must grant them to roles that can be assumed by users.)

Use SQL like the following to revoke access to the SNOWFLAKE.CORTEX_USER and SNOWFLAKE.COPILOT_USER roles from the PUBLIC role, then grant them
to specific roles and users.

```sqlexample
-- Revoke access to most Snowflake AI features from all users in the account
REVOKE DATABASE ROLE SNOWFLAKE.CORTEX_USER FROM ROLE PUBLIC;
REVOKE DATABASE ROLE SNOWFLAKE.COPILOT_USER FROM ROLE PUBLIC;

-- Optionally, grant access to specific roles
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE my_cortex_role;
GRANT DATABASE ROLE SNOWFLAKE.COPILOT_USER TO ROLE my_copilot_role;

-- Then grant those roles to specific users
GRANT ROLE my_cortex_role TO USER alice;
GRANT ROLE my_copilot_role TO USER bob;
```

> **Note:**
>
> If you granted SNOWFLAKE.CORTEX_USER and SNOWFLAKE.COPILOT_USER to other roles, revoke them from those roles
> to completely block users from using Snowflake AI features.

## Revoke access to opt-in features

Some Snowflake AI features are opt-in. Access to these features is disabled by default, so unless you grant
access to them, your users cannot use them. If you have granted access to any of these features, you can revoke access
to individual features:

* **Cortex Analyst:** Set the ENABLE_CORTEX_ANALYST account parameter to FALSE:

  ```sqlexample
  ALTER ACCOUNT SET ENABLE_CORTEX_ANALYST = FALSE;
  ```

* **Cortex Embedding Functions** (AI_EMBED, EMBED_TEXT_768, and EMBED_TEXT_1024): Calling these functions
  requires the SNOWFLAKE.CORTEX_EMBED_USER database role if the user does not have the SNOWFLAKE.CORTEX_USER database role.
  Revoke SNOWFLAKE.CORTEX_EMBED_USER role from any roles you have granted it to.

  ```sqlexample
  REVOKE DATABASE ROLE SNOWFLAKE.CORTEX_EMBED_USER FROM ROLE my_role;
  ```

* **Cortex Fine-tuning:** Revoke the CREATE MODEL privilege on schemas from any roles you have granted it to.

  ```sqlexample
  REVOKE CREATE MODEL ON SCHEMA my_schema FROM ROLE my_role;
  ```

* **Document AI:** Revoke the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role from any
  roles you have granted it to:

  ```sqlexample
  REVOKE DATABASE ROLE SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR FROM ROLE my_role;
  ```

  > **Note:**
  >
  > Existing pipelines continue to operate after access to Document AI is revoked. To stop the pipelines, suspend or drop the tasks associated
  > with the pipelines.
* **Provisioned Throughput:** Revoke the CREATE PROVISIONED THROUGHPUT privilege on schemas from any roles you have granted it to.

  ```sqlexample
  REVOKE CREATE PROVISIONED THROUGHPUT ON SCHEMA my_schema FROM ROLE my_role;
  ```

## Access control by feature

The following table has more detailed information on access control for individual Snowflake AI features:

| Feature | Opt in | Main access control method | Additional access control methods |
| --- | --- | --- | --- |
| [Cortex Agents](cortex-agents.md) |  | SNOWFLAKE.CORTEX_USER database role | USAGE on the search service that the agent queries, plus USAGE on the database, schema, and table used by the search service |
| [Cortex AI Functions](aisql.md) |  | SNOWFLAKE.CORTEX_USER database role |  |
| [Cortex Analyst](cortex-analyst.md) | ✔ | ENABLE_CORTEX_ANALYST account parameter |  |
| [Cortex Fine-tuning](cortex-finetuning.md) | ✔ | CREATE MODEL on the schema where you create fine-tuned models |  |
| [Cortex Knowledge Extensions](cortex-knowledge-extensions/cke-overview.md) |  | SNOWFLAKE.CORTEX_USER database role | Relies on access control for the underlying Cortex Search Service |
| [Cortex Provisioned Throughput](provisioned-throughput.md) | ✔ | CREATE PROVISIONED THROUGHPUT privilege on the schema where you create provisioned throughput objects |  |
| [Cortex Search](cortex-search/cortex-search-overview.md) |  | SNOWFLAKE.CORTEX_USER database role | USAGE on the search service, database, schema, and table used by the search service |
| [Document AI](document-ai/setting-up.md) | ✔ | SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role | Numerous object-level privileges for creating models and pipelines |
| [Snowflake Copilot](../snowflake-copilot.md) |  | SNOWFLAKE.COPILOT_USER database role |  |
| [Snowflake Intelligence](snowflake-intelligence.md) |  | SNOWFLAKE.CORTEX_USER database role | Relies on access control for the underlying Cortex Agent or Search Service |

## Opt out of specific models and AI Functions

Because the cost of using different large language models varies, you can limit access to specific LLMs via an
account-level allowlist, by role-based access control, or by a combination of both. For more information, see
[Control model access](aisql.md).

## ACCOUNTADMIN and AI features

The ACCOUNTADMIN role has complete access to all features in a Snowflake account, including Snowflake AI features.
Revoking the SNOWFLAKE.CORTEX_USER and SNOWFLAKE.COPILOT_USER roles from PUBLIC does not prevent ACCOUNTADMIN from using these features.
Even if an ACCOUNTADMIN’s access to AI features is revoked, a user with access to ACCOUNTADMIN can always
grant access to that role (or any other role) again.

For this and other reasons, it is a best practice to grant the ACCOUNTADMIN role to trusted users only, or even more
strictly, to a single user in the account which is not used for any purpose other than Snowflake account administration
and whose login credentials are tightly controlled. Use ACCOUNTADMIN only for account setup and maintenance, and use
other administrative roles with more limited scope (that is, SECURITYADMIN, SYSADMIN, or USERADMIN) for day-to-day
administration.

It is possible to prevent ACCOUNTADMIN from using Snowflake AI features that are gated by means other than role-based
access control. For example, even a user with ACCOUNTADMIN can’t use Cortex Analyst if the ENABLE_CORTEX_ANALYST account
parameter is set to FALSE. Of course, this user can always set this parameter to TRUE.

## Monitor AI feature usage

To make sure that Snowflake AI features are not being used, monitor usage of Snowflake AI features using the
Cortex-related views in the [SNOWFLAKE.ACCOUNT_USAGE](../../sql-reference/account-usage.md) schema. These views are:

* [CORTEX_ANALYST_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_analyst_usage_history.md)
* [CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_document_processing_usage_history.md)
* [CORTEX_FINE_TUNING_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_fine_tuning_usage_history.md)
* [CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_functions_query_usage_history.md)
* [CORTEX_FUNCTIONS_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_functions_usage_history.md)
* [CORTEX_PROVISIONED_THROUGHPUT_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_provisioned_throughput_usage_history.md)
* [CORTEX_SEARCH_DAILY_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_search_daily_usage_history.md)
* [CORTEX_SEARCH_SERVING_USAGE_HISTORY view](../../sql-reference/account-usage/cortex_search_serving_usage_history.md)

> **Note:**
>
> CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY and CORTEX_FUNCTIONS_USAGE_HISTORY log essentially the same events. It
> is not necessary to monitor both.

[Create alerts on new data](../alerts.md) in these views to notify you when new AI features are
used in your account. For example, the following SQL statement creates an alert that sends a Slack message when any AI function is used:

```sqlexample
CREATE ALERT my_alert
  IF (EXISTS (
    SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY))
  THEN
    BEGIN
      CALL SYSTEM$SEND_SNOWFLAKE_NOTIFICATION(
        SNOWFLAKE.NOTIFICATION.TEXT_PLAIN('AI function used in account'),
        '{"my_slack_integration": {}}'
      );
    END;
```

Such alerts incur a nominal compute cost when new data is added to a Cortex usage history view, but if no AI features
are used, there is no cost because no data is ever added and the alert is never triggered.

## Control access to ML features

Snowflake ML features are not AI features, and access to them is not controlled by the SNOWFLAKE.CORTEX_USER role.

### ML Functions

[ML Functions](../../guides-overview-ml-functions.md) employ classical machine learning techniques for forecasting, anomaly
detection, classification, and other data analysis tasks. Creation of models by ML Functions is opt-in and controlled by
a function-specific privilege, such as CREATE SNOWFLAKE.ML.FORECAST, on schemas. Access to trained models is controlled
by the USAGE privilege on the model object. If you have granted these privileges already, revoke them to prevent users
from creating or using ML Functions models. You may want to DROP any models that have already been created.

Owners of schemas can create ML Functions models in them, regardless of whether they have CREATE privileges for a
specific type of model, so limit ownership and creation of schemas to trusted users. Grant specific privileges to create
models within each schema only to users who need them.

### Snowflake ML

[Snowflake ML](../../developer-guide/snowflake-ml/overview.md) lets you build, deploy, and manage custom machine learning
models developed in Python, at Snowflake scale. Creation and use of Snowflake ML objects, including the model registry,
the feature store, and models and their versions, is not controlled by the SNOWFLAKE.CORTEX_USER role.

Snowflake ML objects are schema-level objects, which means that users can create Snowflake ML objects in any schema on
which they have OWNERSHIP or an appropriate CREATE privilege (for example, CREATE MODEL REGISTRY). Therefore, access to
Snowflake ML is best controlled by limiting ownership and creation of schemas to trusted users. Grant specific
privileges to create Snowflake ML objects within each schema only to users who need them.

> **Note:**
>
> Users with the CREATE MODEL privilege in a schema can also create models using Cortex Fine-tuning. However, actually
> using Cortex fine-tuned models requires the SNOWFLAKE.CORTEX_USER database role.
