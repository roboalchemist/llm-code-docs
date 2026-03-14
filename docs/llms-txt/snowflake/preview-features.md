# Source: https://docs.snowflake.com/en/release-notes/preview-features.md

# Preview Features

Preview features have been implemented and tested in Snowflake; however, full usability and corner-case handling may not be complete yet.
We do not guarantee the use of these features against defects that may produce unexpected or undesired results. Additionally, we may change
the behavior of features while they are in preview. If we change the behavior of a preview feature, we do our best to notify users before
making the change, but we do not guarantee to always pre-announce changes.

In addition, preview features can be disabled, enabled, or viewed for an entire account.
See Managing access to all preview features, on this page, for details.

> **Attention:**
>
> Preview features are provided primarily for evaluation and testing purposes. They should not be used in production systems or with
> production data.
>
> For more details about the usage of preview features, see the Snowflake
> [Preview Terms of Service](https://www.snowflake.com/legal/preview-terms-of-service/).

## Preview Availability

Availability is determined on a per-feature basis:

Open:
:   Most preview features are *Open*, meaning they are enabled by default for all accounts and, therefore, openly available for use.

On Request:
:   Some preview features are provided *On Request*, particularly in the early stages of the preview period. To request access to these
    features for your account, you must contact Snowflake.

Some preview features are available only in certain [Snowflake editions](../user-guide/intro-editions.md) or in specific
[cloud platforms](../user-guide/intro-cloud-platforms.md) or [regions](../user-guide/intro-regions.md).

## Features Currently in Preview

The following features are currently available for preview, listed roughly in the order in which they were introduced:

| Feature | Availability | Introduced | Additional reading | Notes |
| --- | --- | --- | --- | --- |
| Exporting a semantic view to a Tableau Data Source (TDS) file | Open | March 2026 | [Exporting a semantic view to a Tableau Data Source (TDS) file](../user-guide/views-semantic/sql.md) |  |
| AI_COMPLETE document intelligence | Open | March 2026 | [AI_COMPLETE with documents](../user-guide/snowflake-cortex/ai-complete-document-intelligence.md) | Enables the AI_COMPLETE function to process document files, such as PDFs or Microsoft Word files. |
| Support for version 3 of the Apache Iceberg™ table specification | Open | March 2026 | [Apache Iceberg™ tables: Support for Apache Iceberg™ v3 (Preview)](../user-guide/tables-iceberg-v3-specification-support.md) | Includes support for the `geography`, `geometry`, `nanosecond`, and `variant` data types and default values, deletion vectors, and row lineage. |
| pg_lake extension for Snowflake Postgres | Open | March 2026 | [Configuring S3 Storage for pg_lake](../user-guide/snowflake-postgres/postgres-pg_lake.md) |  |
| Apache Iceberg™ tables: Partitioned writes with a hierarchical path layout | Open | February 2026 | [Partitioning with hierarchical paths](../user-guide/tables-iceberg-metadata.md) |  |
| AGENT_RUN function | Open | February 2026 | [AGENT_RUN (SNOWFLAKE.CORTEX)](../sql-reference/functions/agent_run-snowflake-cortex.md) |  |
| Container Runtime version selection | Open | February 2026 | [Snowflake Container Runtime release notes](../developer-guide/snowflake-ml/container-runtime/releases.md) |  |
| Restricted caller’s rights in Streamlit in Snowflake | Open | February 2026 | [Restricted caller’s rights and Streamlit in Snowflake](../developer-guide/streamlit/features/restricted-callers-rights.md) |  |
| Semantic views: Joining tables containing ranges of values | Open | February 2026 | [Joining logical tables that contain ranges of values](../user-guide/views-semantic/sql.md) |  |
| Sharing Streamlit in Snowflake apps | Open | February 2026 | [Sharing Streamlit in Snowflake apps](../developer-guide/streamlit/features/sharing-streamlit-apps.md) |  |
| DATA_AGENT_RUN function | Open | February 2026 | [DATA_AGENT_RUN (SNOWFLAKE.CORTEX)](../sql-reference/functions/data_agent_run-snowflake-cortex.md) |  |
| Strong Authentication Hub | Open | February 2026 | [Strong Authentication Hub](../user-guide/strong-authentication-hub.md) |  |
| Cortex Code Data Science and Machine Learning skill | Open | February 2026 | [Cortex Code CLI](../user-guide/cortex-code/cortex-code-cli.md) |  |
| Overview tab in the Trust Center | Open | February 2026 | [Trust Center](../user-guide/trust-center/overview.md) |  |
| Collaboration Data Clean Rooms | Open | February 2026 | [About Snowflake Collaboration Data Clean Rooms](../user-guide/cleanrooms/v2/about.md) |  |
| Cortex Code in Snowsight | Open | February 2026 | [Cortex Code in Snowsight](../user-guide/cortex-code/cortex-code-snowsight.md) |  |
| Use Snowsight to manage external volumes | Open | February 2026 | *[Configure an external volume](../user-guide/tables-iceberg-configure-external-volume.md)* [Drop an external volume by using Snowsight](../user-guide/tables-iceberg-drop-external-volume.md) |  |
| Fine-tuning `arctic-extract` models | Open | January 2026 | [Fine-tuning arctic-extract models](../user-guide/snowflake-cortex/arctic-extract-finetuning.md) |  |
| Image extraction with AI_PARSE_DOCUMENT | Open | January 2026 | [Cortex AI Functions: Image extraction with AI_PARSE_DOCUMENT](../user-guide/snowflake-cortex/image-extraction.md) |  |
| Consumer-controlled maintenance policies | Open | January 2026 | [Consumer-controlled maintenance policies](../developer-guide/native-apps/consumer-maintenance-policies.md) |  |
| Sensitive data classification in the Trust Center | Open | January 2026 | [Use the Trust Center to set up sensitive data classification](../user-guide/classify-ui-trust-center.md) | Sensitive data classification using SQL is already generally available. |
| External lineage | Open | January 2026 | [External lineage](../user-guide/external-lineage.md) |  |
| Copy tags when running CREATE OR REPLACE TABLE | Open | January 2026 | [CREATE TABLE](../sql-reference/sql/create-table.md) |  |
| Using the Snowpark Python JDBC | Open | January 2026 | [Using the Snowpark Python JDBC](../developer-guide/snowpark/python/snowpark-jdbc.md) |  |
| Workspace replication | Open | January 2026 | [Workspace replication](../user-guide/ui-snowsight/workspaces-replication.md) |  |
| Data quality notifications | Open | January 2026 | [Sending notifications for data quality issues](../user-guide/data-quality-notifications.md) |  |
| Snowflake High Performance connector for Kafka | Open | December 2025 | [Snowflake High Performance connector for Kafka](../connectors/kafkahp/about.md) |  |
| Notebooks in Workspaces | Open | December 2025 | [Snowflake Notebooks in Workspaces](../user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-overview.md) |  |
| Container runtime support for Streamlit in Snowflake | Open | December 2025 | [Runtime environments for Streamlit apps](../developer-guide/streamlit/app-development/runtime-environments.md) |  |
| Support for Scala version 2.13 | Open | December 2025 | [Prerequisites](../developer-guide/udf/scala/udf-scala-introduction.md) |  |
| Optimize an existing semantic view or model with verified queries | Open | December 2025 | [Optimize an existing semantic view or model with verified queries](../user-guide/snowflake-cortex/cortex-analyst/analyst-optimization.md) |  |
| Import machine learning models from external services | Open | November 2025 | [Import and deploy models from an external service](../developer-guide/snowflake-ml/model-registry/snowsight-ui.md) |  |
| Document Processing Playground | Open | November 2025 | [Document Processing Playground](../user-guide/snowflake-cortex/document-processing-playground.md) |  |
| Query Snowflake-managed Apache Iceberg™ tables by using Microsoft Fabric | Open | November 2025 | [Query Snowflake-managed Apache Iceberg™ tables by using Microsoft Fabric](../user-guide/tables-iceberg-query-using-microsoft-fabric.md) |  |
| Configure a catalog integration for OneLake REST | Open | November 2025 | [Configure a catalog integration for OneLake REST](../user-guide/tables-iceberg-configure-catalog-integration-rest-onelake.md) |  |
| Cortex Analyst Routing Mode | Open | November 2025 | [Routing Mode for Cortex Analyst](../user-guide/snowflake-cortex/cortex-analyst/cortex-analyst-routing-mode.md) |  |
| Data quality anomaly detection | Open | November 2025 | [Detecting anomalies in data quality](../user-guide/data-quality-anomaly.md) |  |
| Configure replication for Snowflake-managed Apache Iceberg™ tables | Open | November 2025 | [Configure replication for Snowflake-managed Apache Iceberg™ tables](../user-guide/tables-iceberg-replication.md) |  |
| Trust Center extensions | Open | November 2025 | [Using Trust Center extensions](../user-guide/trust-center/trust-center-extensions.md) |  |
| Executing Scala code using Snowpark Connect for Spark | Open | November 2025 | [Run Scala code from your client](../developer-guide/snowpark-connect/snowpark-connect-workloads-jupyter.md) |  |
| Publishing and consuming public marketplace listings in VPS regions | Open | October 2025 | [Snowflake Marketplace version 2 listings in VPS deployments](../collaboration/collaboration-marketplace-about.md) |  |
| Listings in government regions can be shared on the internal marketplace | Open | October 2025 | [About organizational listings](../user-guide/collaboration/listings/organizational/org-listing-about.md) |  |
| Verified Query suggestions | Open | October 2025 | [Suggestions for semantic models and views](../user-guide/snowflake-cortex/cortex-analyst/verified-query-suggestions.md) |  |
| Use organization user groups with organizational listings | Open | October 2025 | [Use organization user groups with organizational listings](../user-guide/collaboration/listings/organizational/org-listings-org-user-groups.md) |  |
| Make database objects discoverable in Universal Search | Open | October 2025 | [Make database objects discoverable in Universal Search](../user-guide/ui-snowsight/object-visibility-universal-search.md) |  |
| Declarative Sharing for Native Apps | Open | September 2025 | [About Declarative Sharing in the Native Application Framework](../developer-guide/declarative-sharing/about.md) |  |
| Cortex Agent Monitoring | Open | September 2025 | [Monitor Cortex Agent requests](../user-guide/snowflake-cortex/cortex-agents-monitor.md) |  |
| Position row-level deletes for writing to externally managed Apache Iceberg™ tables | Open | September 2025 | *[Write support for externally managed Apache Iceberg™ tables](../user-guide/tables-iceberg-externally-managed-writes.md)* [Use row-level deletes](../user-guide/tables-iceberg-manage.md) |  |
| SnowConvert AI Verification | Open | September 2025 | [AI code conversion](../migrations/snowconvert-docs/snowconvert-ai-verification.md) |  |
| SnowConvert AI - ETL Migration | Open | October 2025 | [ETL Migration](../migrations/snowconvert-docs/general/user-guide/etl-migration-replatform.md) | Public preview feature for migrating SSIS packages to dbt projects on Snowflake. |
| Data quality in Snowsight | Open | September 2025 | *[Monitoring data quality checks in Snowsight](../user-guide/data-quality-ui-monitor.md)* [Use data profiling to understand your data](../user-guide/data-quality-profile.md) |  |
| Gap-filling time-series data | Open | September 2025 | [RESAMPLE](../sql-reference/constructs/resample.md) |  |
| Cortex Agents object REST API | Open | September 2025 | [Configure and interact with Agents](../user-guide/snowflake-cortex/cortex-agents-manage.md) |  |
| Surcharging of compute pool usage of a Snowflake Native App with containers | Open | August 2025 | *[Compute pool surcharges in Snowflake Native Apps with containers](../developer-guide/snowpark-container-services/provider-pricing-surcharges.md)* [MARKETPLACE_PROVIDER_SPCS_USAGE View](../collaboration/views/marketplace-provider-spcs-usage-ds.md) |  |
| Updated access control for data quality monitoring | Open | August 2025 | [Required privilege on the table or view](../user-guide/data-quality-access-control.md) |  |
| Cortex Search Service replication | Open | August 2025 | [Replicate a Cortex Search Service](../user-guide/snowflake-cortex/cortex-search/cortex-search-replication.md) |  |
| Snowpark Container Services new stage volume implementation | Open | August 2025 | [Using Snowflake stage volumes with services](../developer-guide/snowpark-container-services/snowflake-stage-volume.md) |  |
| Snapshots | Open | August 2025 | [Backups for disaster recovery and immutable storage](../user-guide/backups.md) |  |
| Reading data from external data sources using Snowpark Python DB-API | Open | August 2025 | [Using the Snowpark Python DB-API](../developer-guide/snowpark/python/reading-data-from-external-sources.md) | Use Snowpark Python to programmatically pull data from external databases into Snowflake. |
| Cortex Agents admin configuration UI | Open | August 2025 | [Configure and interact with Agents](../user-guide/snowflake-cortex/cortex-agents-manage.md) |  |
| Snowpark Container Services batch jobs | Open | August 2025 | [Run multiple replicas of a job service (batch jobs)](../developer-guide/snowpark-container-services/working-with-services.md) |  |
| Snowflake Intelligence | Open | August 2025 | [Overview of Snowflake Intelligence](../user-guide/snowflake-cortex/snowflake-intelligence.md) |  |
| Disable public access to privatelink-only accounts | Open | July 2025 | [Enforcement of privatelink-only access](../user-guide/security-disable-public-access-privatelink.md) |  |
| Manage integrations using Snowsight | Open | June 2025 | [Managing integrations in Snowsight](../user-guide/ui-snowsight-integrations.md) |  |
| Preconfigured Notebook runtimes | Open | June 2025 | [Create a notebook](../user-guide/ui-snowsight/notebooks-create.md) |  |
| Snowflake Copilot inline | Open | June 2025 | [Using Snowflake Copilot inline](../user-guide/snowflake-copilot-inline.md) |  |
| Snowflake Cortex Playground | Open | June 2025 | [Cortex Playground](../user-guide/snowflake-cortex/cortex-playground.md) |  |
| New in-app notifications from Trust Center in Snowsight | Open | May 2025 |  |  |
| Snowpark Container Services available to Snowflake accounts on Google Cloud | Open | May 2025 | [Snowpark Container Services](../developer-guide/snowpark-container-services/overview.md) |  |
| Automated refresh and auto-ingest pipes for internal named stages | Open | April 2025 | *[CREATE STAGE](../sql-reference/sql/create-stage.md)* [CREATE PIPE](../sql-reference/sql/create-pipe.md) * [Automated directory table refreshes for internal stages](../user-guide/data-load-dirtables-auto.md) | Currently available for Snowflake accounts hosted on AWS. |
| Configuring automatic suspension of a Snowpark Container Services service | Open | April 2025 | [CREATE SERVICE](../sql-reference/sql/create-service.md) |  |
| Google Cloud Private Service Connect in Streamlit in Snowflake | Open | April 2025 | [Private connectivity for Streamlit in Snowflake](../developer-guide/streamlit/object-management/privatelink.md) |  |
| Multi-file editing in Streamlit in Snowflake | Open | March 2025 | [Edit a Streamlit app](../developer-guide/streamlit/getting-started/create-streamlit-ui.md) |  |
| Git integration for Streamlit in Snowflake | Open | March 2025 | [Sync Streamlit in Snowflake apps with a Git repository](../developer-guide/streamlit/features/git-integration.md) |  |
| Cloning databases that contain hybrid tables | Open | March 2025 | [Clone databases that contain hybrid tables](../user-guide/tables-hybrid-clone.md) |  |
| Snowflake Native Apps with Snowpark Container Services - Support for Azure Private Link | Open | March 2025 | [Mar 03, 2025: Native Apps with Snowpark Container Services - Support for Azure Private Link (Preview)](2025/other/2025-03-03-na-spcs-azure-pl-pupr.md) |  |
| Release channels in Snowflake Native Apps | Open | February 2025 | [Publish an app using release channels](../developer-guide/native-apps/release-channels.md) |  |
| CREATE OR ALTER <OBJECT> | Open | February 2025 | *[CREATE OR ALTER AUTHENTICATION POLICY](../sql-reference/sql/create-authentication-policy.md)* [CREATE OR ALTER FILE FORMAT](../sql-reference/sql/create-file-format.md) * [CREATE OR ALTER TAG](../sql-reference/sql/create-tag.md) | Additional commands that create an object if it doesn’t exist, or alters it according to the object definition. |
| Viewing Snowpipe in Snowsight | Open | February 2025 | [Manage Snowpipe in Snowsight](../user-guide/data-load-snowpipe-snowsight.md) |  |
| Snowpark Checkpoints Library | Open | January 2025 | [Snowpark Checkpoints](../developer-guide/snowpark/python/snowpark-checkpoints-library.md) |  |
| Snowflake Python Demos API | Open | January 2025 | [Snowflake Python Demos API](../developer-guide/snowflake-python-api/snowflake-python-demos.md) |  |
| Join policies | Open | January 2025 | [Join policies](../user-guide/join-policies.md) |  |
| CREATE OR ALTER <OBJECT> | Open | December 2024 | *[CREATE OR ALTER DATA METRIC FUNCTION](../sql-reference/sql/create-data-metric-function.md)* [CREATE OR ALTER EXTERNAL FUNCTION](../sql-reference/sql/create-external-function.md) *[CREATE OR ALTER FUNCTION](../sql-reference/sql/create-function.md)* [CREATE OR ALTER FUNCTION (Snowpark Container Services)](../sql-reference/sql/create-function-spcs.md) * [CREATE OR ALTER PROCEDURE](../sql-reference/sql/create-procedure.md) | Additional commands that create an object if it doesn’t exist, or alters it according to the object definition. |
| Executing a Snowpark Container Services job service asynchronously | Open | December 2024 | [EXECUTE JOB SERVICE](../sql-reference/sql/execute-job-service.md) |  |
| Restricted caller’s rights | Open | December 2024 | [Restricted caller’s rights](../developer-guide/restricted-callers-rights.md) |  |
| Using block storage volumes with job services. | Open | November 2024 | [Using block storage volumes with services](../developer-guide/snowpark-container-services/block-storage-volume.md) |  |
| Apache Iceberg™ table support for Microsoft Fabric OneLake | Open | November 2024 | [CREATE EXTERNAL VOLUME (Azure)](../sql-reference/sql/create-external-volume.md) |  |
| CREATE OR ALTER <OBJECT> | Open | November 2024 | *[CREATE OR ALTER <object>](../sql-reference/sql/create-or-alter.md)* [CREATE OR ALTER APPLICATION ROLE](../sql-reference/sql/create-application-role.md) *[CREATE OR ALTER DATABASE](../sql-reference/sql/create-database.md)* [CREATE OR ALTER DATABASE ROLE](../sql-reference/sql/create-database-role.md) *[CREATE OR ALTER ROLE](../sql-reference/sql/create-role.md)* [CREATE OR ALTER SCHEMA](../sql-reference/sql/create-schema.md) *[CREATE OR ALTER STAGE](../sql-reference/sql/create-stage.md)* [CREATE OR ALTER VIEW](../sql-reference/sql/create-view.md) * [CREATE OR ALTER WAREHOUSE](../sql-reference/sql/create-warehouse.md) | Additional commands that create an object if it doesn’t exist, or alters it according to the object definition. |
| Snowflake Connector for SharePoint | Open | November 2024 | [About the Snowflake Connector for SharePoint](../connectors/unstructured-data-connectors/sharepoint/about.md) |  |
| Snowflake ML - Model Serving in Snowpark Container Services | Open | October 2024 | [Deploy models for Real time Inference (REST API)](../developer-guide/snowflake-ml/inference/real-time-inference-rest-api.md) |  |
| Writing files from Snowpark Python UDFs and UDTFs | Open | October 2024 | [Writing files from Snowpark Python UDFs and UDTFs](../developer-guide/snowpark/python/creating-udfs.md) |  |
| Cortex Analyst Suggested Questions | Open | October 2024 | [Onboarding questions in Cortex Analyst](../user-guide/snowflake-cortex/cortex-analyst/suggested-questions-feature.md) |  |
| Cortex Analyst and Search integration | Open | October 2024 | [Improve literal search to enhance Cortex Analyst responses](../user-guide/snowflake-cortex/cortex-analyst/cortex-analyst-search-integration.md) |  |
| Support for IAM authentication in external network access | Open | October 2024 | [External network access overview](../developer-guide/external-network-access/external-network-access-overview.md) |  |
| Sharing of Cortex fine-tuned models in model registry | Open | October 2024 | [Sharing models](../developer-guide/snowflake-ml/model-registry/overview.md) |  |
| Resource constraints for Snowpark-optimized warehouses | Open | September 2024 | [Snowpark-optimized warehouses](../user-guide/warehouses-snowpark-optimized.md) |  |
| Support for Cross-Cloud Auto-Fulfillment in a Snowflake Native App with Snowpark Container Services | Open | August 2024 | [Auto-fulfillment for listings](../collaboration/provider-listings-auto-fulfillment.md) | Currently only supported on Amazon Web Services and Microsoft Azure. |
| Snowflake Connector for PostgreSQL | Open | July 2024 | [About the Snowflake Connector for PostgreSQL](../connectors/postgres6/about.md) |  |
| Snowflake Connector for MySQL | Open | July 2024 | [About the Snowflake Connector for MySQL](../connectors/mysql6/about.md) |  |
| Create and manage a Snowflake Native App in the Snowflake VS Code extension | Open | July 2024 | [Work with the Snowflake Native App Framework](../user-guide/vscode-ext.md) |  |
| Snowsight Notebooks default warehouses | Open | July 2024 | *[Overview of warehouses](../user-guide/warehouses-overview.md)* [Warehouse considerations](../user-guide/warehouses-considerations.md) * [Set up Snowflake Notebooks](../user-guide/ui-snowsight/notebooks-setup.md) |  |
| Support for external and Apache Iceberg™ tables in the Snowflake Native App Framework | Open | July 2024 | [Support for external and Apache Iceberg™ tables](../developer-guide/native-apps/preparing-data-content.md) |  |
| Event definitions in the Snowflake Native App Framework | Open | July 2024 | [About event sharing](https://other-docs.snowflake.com/en/native-apps/consumer-enable-logging#about-event-sharing) |  |
| VS Code extension | Open | July 2024 | [Edit the Snowflake connections.toml file](../user-guide/vscode-ext.md) |  |
| Snowflake Notebooks external access support | Open | July 2024 | [Set up external access for Snowflake Notebooks](../user-guide/ui-snowsight/notebooks-external-access.md) |  |
| Snowflake Native SDK for Connectors | Open | June 2024 | [Snowflake Native SDK for Connectors](../developer-guide/native-apps/connector-sdk/about-connector-sdk.md) |  |
| CREATE OR ALTER TABLE | Open | May 2024 | [CREATE TABLE](../sql-reference/sql/create-table.md) | Creates a table if it doesn’t exist, or alters it according to the table definition. |
| CREATE OR ALTER TASK | Open | May 2024 | [CREATE TASK](../sql-reference/sql/create-task.md) | Creates a task if it doesn’t exist, or alters it according to the task definition. |
| EXECUTE IMMEDIATE FROM template file | Open | May 2024 | [EXECUTE IMMEDIATE FROM](../sql-reference/sql/execute-immediate-from.md) | Execute a template file using the Jinja2 templating language. |
| View more rows of query results in Snowsight worksheet | Open | March 2024 | [Exploring the worksheet results](../user-guide/ui-snowsight-query.md) | Not available to accounts in U.S. government regions, accounts using Virtual Private Snowflake (VPS), and accounts that use Private Connectivity to access Snowflake. |
| Limit functionality of Snowflake Native App | Open | March 2024 | *[Limit functionality of your Snowflake Native App for trial consumers](https://other-docs.snowflake.com/collaboration/provider-listings-preparing#label-listings-trial-limit-functionality-app)* [SYSTEM$IS_LISTING_TRIAL](../sql-reference/functions/system_is_listing_trial.md) |  |
| COPY FILES | Open | February 2024 | [COPY FILES](../sql-reference/sql/copy-files.md) |  |
| Snowflake Connector for Google Analytics Raw Data | Open | January 2024 | [Snowflake Connector for Google Analytics Raw Data](../connectors/google/gard/gard-connector-about.md) |  |
| Snowflake Connector for Google Analytics Aggregate Data | Open | January 2024 | [Snowflake Connector for Google Analytics Aggregate Data](https://other-docs.snowflake.com/connectors/google/gaad/gaad-connector-about.html) |  |
| Support for the Arrow format in the Snowflake .NET driver | Open | November 2023 | [snowflake-connector-net git repo](https://github.com/snowflakedb/snowflake-connector-net) |  |
| Set up and Monitor Client Redirect Using Snowsight | Open | November 2023 | [Redirecting client connections](../user-guide/client-redirect.md) |  |
| Python Package Version Range Support | Open | August 2023 | *[CREATE FUNCTION](../sql-reference/sql/create-function.md)* [CREATE PROCEDURE](../sql-reference/sql/create-procedure.md) |  |
| Snowflake ML - FileSystem and FileSet | Open | N/A | [Load and write data](../developer-guide/snowflake-ml/load-data.md) | This feature is currently supported, but will not be made generally available. |
| Custom Event Billing | Open | [June 2023](2023-06.md) | [Add billable events to an application package](../developer-guide/native-apps/adding-custom-event-billing.md) |  |
| Tracking DDL commands, tags, and policies in the ACCESS_HISTORY view | Open | [June 2023](2023-06.md) | [Access History](../user-guide/access-history.md) |  |
| ACCOUNTS view (Organization Usage) | Open | [June 2023](2023-06.md) | [ACCOUNTS view](../sql-reference/organization-usage/accounts.md) |  |
| External table support for Delta Lake | Open | February 2022 | [Introduction to external tables](../user-guide/tables-external-intro.md) |  |

## Managing access to all preview features

Snowflake provides the ability for account administrators to manage access to
preview features at the account level.

* Account administrators can enable or disable access to preview features for their entire Snowflake account.
  Additionally, account administrators can check whether all preview features are enabled or disabled.
* This setting affects all users and all preview features (including private preview features) within the account.
* By default, access to all preview features is enabled for most accounts.

> **Caution:**
>
> Before disabling or enabling preview features for your account, please review
> the associated documentation for a complete list of limitations and other information.

The following limitations apply to enabling and disabling preview feature access:

* Applies to both private and open preview features.
* This is an all-or-nothing setting that affects all users and all previews within an account.
* Any user in the account who is using a preview feature will lose access to that feature immediately after SYSTEM$DISABLE_PREVIEW_ACCESS is executed.
* Snowflake Marketplace products, which are managed separately through [IMPORTED PRIVILEGES](../user-guide/data-exchange-marketplace-privileges.md), are not covered as part of this capability.
* Client-side libraries (such as Snowpark API) are not covered as part of this capability.

### Checking the status of preview features in your account

To check whether preview features are enabled in your account, call the [SYSTEM$GET_PREVIEW_ACCESS_STATUS](../sql-reference/functions/system_get_preview_access_status.md) function.

For example:

```sqlexample
SELECT SYSTEM$GET_PREVIEW_ACCESS_STATUS();
```

Which returns:

```output
+-------------------------------------------------------+
| SYSTEM$GET_PREVIEW_ACCESS_STATUS()                    |
+-------------------------------------------------------+
| Preview access is [ENABLED|DISABLED] for this account |
+-------------------------------------------------------+
```

Indicating the current state of preview features for the account.

### Enabling preview features in your account

To enable preview features for your account, call the [SYSTEM$ENABLE_PREVIEW_ACCESS](../sql-reference/functions/system_enable_preview_access.md) function.

For example:

```sqlexample
SELECT SYSTEM$ENABLE_PREVIEW_ACCESS();
```

Which returns:

```output
+---------------------------------------------------------------+
| SELECT SYSTEM$ENABLE_PREVIEW_ACCESS();                        |
+---------------------------------------------------------------+
| Preview access has been successfully enabled for this account |
+---------------------------------------------------------------+
```

### Disabling preview features in your account

To disable preview features for your account, call the [SYSTEM$DISABLE_PREVIEW_ACCESS](../sql-reference/functions/system_disable_preview_access.md) function.

> **Caution:**
>
> Caution should be exercised when disabling preview features.
> All preview features, including both public and private, are disabled when you call SYSTEM$DISABLE_PREVIEW_ACCESS.
> Private preview features cannot be enabled by calling SYSTEM$ENABLE_PREVIEW_ACCESS.

```sqlexample
SELECT SYSTEM$DISABLE_PREVIEW_ACCESS();
```

Which returns:

```output
+----------------------------------------------------------------+
| SYSTEM$DISABLE_PREVIEW_ACCESS()                                |
+----------------------------------------------------------------+
| Preview access has been successfully disabled for this account |
+----------------------------------------------------------------+
```
