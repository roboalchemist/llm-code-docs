# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/snowflake-rest-api.md

# Snowflake REST APIs

Snowflake REST APIs for resource management provide a set of endpoints that lets users programmatically interact with and control various resources within the Snowflake Data Cloud.

The Snowflake REST APIs suite of APIs enables developers to build end-to-end automation and integration with Snowflake resources. These REST APIs are compliant with the [OpenAPI specification](https://spec.openapis.org/oas/v3.1.0). Snowflake REST APIs enable developers and partners to use the language of their choice to build integrations with Snowflake using the openAPI specifications.

The Snowflake REST APIs supports the following resources through the corresponding APIs. The APIs support CREATE OR ALTER operations for applicable resources.

* Working with accounts

  * [Accounts](account/account-introduction.md)
  * [Managed accounts](managed-account/managed-account-introduction.md)
* Working with users, roles, and privileges

  * [Users](users/users-introduction.md)
  * [Roles](roles/roles-introduction.md)
  * [Database roles](database-role/database-role-introduction.md)
  * [Grants](grants/grants-introduction.md)
* Managing virtual warehouses

  * [Warehouses](warehouses/warehouses-introduction.md)
* Working with databases and schemas

  * [Databases](databases/db-introduction.md)
  * [Schemas](schemas/schemas-introduction.md)
* Managing tables and views

  * [Tables](tables/tables-introduction.md)
  * [Dynamic tables](dynamic-tables/dynamic-tables-introduction.md)
  * [Event tables](event-table/event-table-introduction.md)
  * [Iceberg tables](iceberg-table/iceberg-table-introduction.md)
  * [Sequences](sequence/sequence-introduction.md)
  * [Views](view/view-introduction.md)
* Loading and unloading data

  * [Stages](stages/stages-introduction.md)
  * [External volumes](external-volume/external-volume-introduction.md)
  * [Pipes](pipe/pipe-introduction.md)
* Managing notebooks and Streamlit apps

  * [Notebooks](notebook/notebook-introduction.md)
  * [Streamlit](streamlit/streamlit-introduction.md)
* Working with Snowpark Container Services

  * [Compute Pools](compute-pools/cp-introduction.md)
  * [Image Repositories](image-repositories/images-introduction.md)
  * [Services](services/services-introduction.md)
* Using functions and procedures

  * [Artifact repositories](artifact-repository/artifact-repository-introduction.md)
  * [Functions](functions/functions-introduction.md)
  * [User-defined functions](user-defined-function/user-defined-function-introduction.md)
  * [Procedures](procedure/procedure-introduction.md)
* Managing security

  * [Network policies](network-policy/network-policy-introduction.md)
  * [Network rules](network-rule/network-rule-introduction.md)
  * [Password policies](password-policy/password-policy-introduction.md)
  * [Secrets](secret/secret-introduction.md)
* Managing alerts

  * [Alerts](alert/alert-introduction.md)
* Leveraging AI/ML

  * [Cortex Embed](cortex-embed/cortex-embed-introduction.md)
  * [Cortex Inference](cortex-inference/cortex-inference-introduction.md)
  * [Cortex Search Service](cortex-search/cortex-search-introduction.md)
* Managing streams and tasks

  * [Streams](stream/stream-introduction.md)
  * [Tasks](tasks/tasks-introduction.md)
* Managing integrations

  * [API integration](api-integration/api-integration-introduction.md)
  * [Use catalog integrations](catalog-integration/catalog-integration-introduction.md)
  * [Use notification integrations](notification-integration/notification-integration-introduction.md)
* Using Spark Connect

  * [Spark Connect](spark-connect/spark-connect-introduction.md)
* Managing tags

  * [Tags](tag/tag-introduction.md)

For reference information about the APIs and their endpoints, see [Snowflake REST APIs reference](reference.md).

You can access the Snowflake REST APIs OpenAPI specifications in the [snowflake-rest-api-specs](https://github.com/snowflakedb/snowflake-rest-api-specs) Git repository.

> **Note:**
>
> The Snowflake REST APIs reference documentation reflects the
> latest version of the Snowflake REST APIs. Note that not all resources in the API currently provide 100% coverage of their
> equivalent [SQL commands](../../sql-reference-commands.md), but the Snowflake REST APIs are under active development and are continuously expanding.

## Requirements

The Snowflake REST APIs has the following requirements:

* You must have a way to submit REST requests, such as the [Postman app](https://www.postman.com/downloads/), [curl](https://curl.se/), or an HTTP client in the programming language of your choice, installed on your machine.

## Suggested tools

* [Postman app](https://www.postman.com/downloads/)
* [curl](https://curl.se/)
* [Snowflake CLI](../snowflake-cli/index.md)
* [SnowSQL](../../user-guide/snowsql.md)
