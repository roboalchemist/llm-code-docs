# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/stage-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/image-repository-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/compute-pool-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/package-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/object-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/notebook-commands/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/create.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/snowpark/create.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/create.md

# CREATE *<object>*

Creates a new object of the specified type.

See also:
:   [ALTER <object>](alter.md) , [DESCRIBE <object>](desc.md) , [SHOW <objects>](show.md)

## CREATE commands

For specific syntax, usage notes, and examples, see:

**Account Objects:**

> * [CREATE API INTEGRATION](create-api-integration.md)
> * [CREATE APPLICATION](create-application.md)
> * [CREATE APPLICATION PACKAGE](create-application-package.md)
> * [CREATE AUTHENTICATION POLICY](create-authentication-policy.md)
> * [CREATE CATALOG INTEGRATION](create-catalog-integration.md)
> * [CREATE COMPUTE POOL](create-compute-pool.md)
> * [CREATE CONNECTION](create-connection.md)
> * [CREATE DATABASE](create-database.md) , [CREATE DATABASE (catalog-linked)](create-database-catalog-linked.md) , [CREATE DATABASE … CLONE](create-clone.md)
> * [CREATE DATABASE ROLE](create-database-role.md)
> * [CREATE EXTERNAL ACCESS INTEGRATION](create-external-access-integration.md)
> * [CREATE EXTERNAL VOLUME](create-external-volume.md)
> * [CREATE FAILOVER GROUP](create-failover-group.md)
> * [CREATE FEATURE POLICY](create-feature-policy.md)
> * [CREATE NETWORK POLICY](create-network-policy.md)
> * [CREATE NOTIFICATION INTEGRATION](create-notification-integration.md)
> * [CREATE ORGANIZATION PROFILE](create-organization-profile.md)
> * [CREATE POSTGRES INSTANCE](create-postgres-instance.md)
> * [CREATE PROVISIONED THROUGHPUT](create-provisioned-throughput.md)
> * [CREATE REPLICATION GROUP](create-replication-group.md)
> * [CREATE RESOURCE MONITOR](create-resource-monitor.md)
> * [CREATE ROLE](create-role.md)
> * [CREATE SECURITY INTEGRATION](create-security-integration.md)
> * [CREATE SHARE](create-share.md)
> * [CREATE STORAGE INTEGRATION](create-storage-integration.md)
> * [CREATE USER](create-user.md)
> * [CREATE WAREHOUSE](create-warehouse.md)

**Database Objects:**

> * [CREATE AGENT](create-agent.md)
> * [CREATE AGGREGATION POLICY](create-aggregation-policy.md)
> * [CREATE ALERT](create-alert.md)
> * [CREATE AUTHENTICATION POLICY](create-authentication-policy.md)
> * [CREATE BACKUP POLICY](create-backup-policy.md)
> * [CREATE BACKUP SET](create-backup-set.md)
> * [CREATE CONTACT](create-contact.md)
> * [CREATE CORTEX SEARCH SERVICE](create-cortex-search.md)
> * [CREATE DATA METRIC FUNCTION](create-data-metric-function.md)
> * [CREATE DATASET](create-dataset.md)
> * [CREATE DBT PROJECT](create-dbt-project.md)
> * [CREATE DYNAMIC TABLE](create-dynamic-table.md)
> * [CREATE EVENT TABLE](create-event-table.md)
> * [CREATE EXPERIMENT](create-experiment.md)
> * [CREATE EXTERNAL FUNCTION](create-external-function.md)
> * [CREATE EXTERNAL TABLE](create-external-table.md)
> * [CREATE FILE FORMAT](create-file-format.md) , [CREATE FILE FORMAT … CLONE](create-clone.md)
> * [CREATE FUNCTION](create-function.md)
> * [CREATE GATEWAY](create-gateway.md)
> * [CREATE GIT REPOSITORY](create-git-repository.md)
> * [CREATE HYBRID TABLE](create-hybrid-table.md)
> * [CREATE ICEBERG TABLE](create-iceberg-table.md)
> * [CREATE INTERACTIVE TABLE](create-interactive-table.md)
> * [CREATE INTERACTIVE WAREHOUSE](create-interactive-warehouse.md)
> * [CREATE IMAGE REPOSITORY](create-image-repository.md)
> * [CREATE JOIN POLICY](create-join-policy.md)
> * [CREATE LISTING](create-listing.md)
> * [CREATE MAINTENANCE POLICY](create-maintenance-policy.md)
> * [CREATE MASKING POLICY](create-masking-policy.md)
> * [CREATE MATERIALIZED VIEW](create-materialized-view.md)
> * [CREATE MCP SERVER](create-mcp-server.md)
> * [CREATE MODEL](create-model.md)
> * [CREATE MODEL MONITOR](create-model-monitor.md)
> * [CREATE NETWORK RULE](create-network-rule.md)
> * [CREATE NOTEBOOK](create-notebook.md)
> * [CREATE NOTEBOOK PROJECT](create-notebook-project.md)
> * [CREATE ONLINE FEATURE TABLE](create-online-feature-table.md)
> * [CREATE ORGANIZATION LISTING](create-organization-listing.md)
> * [CREATE PACKAGES POLICY](create-packages-policy.md)
> * [CREATE PASSWORD POLICY](create-password-policy.md)
> * [CREATE PIPE](create-pipe.md)
> * [CREATE PRIVACY POLICY](create-privacy-policy.md)
> * [CREATE PROCEDURE](create-procedure.md)
> * [CREATE PROJECTION POLICY](create-projection-policy.md)
> * [CREATE ROW ACCESS POLICY](create-row-access-policy.md)
> * [CREATE SCHEMA](create-schema.md) , [CREATE SCHEMA … CLONE](create-clone.md)
> * [CREATE SECRET](create-secret.md)
> * [CREATE SEMANTIC VIEW](create-semantic-view.md)
> * [CREATE SEQUENCE](create-sequence.md) , [CREATE SEQUENCE … CLONE](create-clone.md)
> * [CREATE SERVICE](create-service.md)
> * [CREATE SESSION POLICY](create-session-policy.md)
> * [CREATE SNAPSHOT](create-snapshot.md)
> * [CREATE SNAPSHOT POLICY — Deprecated](create-snapshot-policy.md) (deprecated; prefer [CREATE BACKUP POLICY](create-backup-policy.md))
> * [CREATE SNAPSHOT SET — Deprecated](create-snapshot-set.md) (deprecated; prefer [CREATE BACKUP SET](create-backup-set.md))
> * [CREATE STAGE](create-stage.md) , [CREATE STAGE … CLONE](create-clone.md)
> * [CREATE STORAGE LIFECYCLE POLICY](create-storage-lifecycle-policy.md)
> * [CREATE STREAM](create-stream.md) , [CREATE STREAM … CLONE](create-clone.md)
> * [CREATE STREAMLIT](create-streamlit.md),
> * [CREATE TABLE](create-table.md) , [CREATE TABLE … CLONE](create-clone.md)
> * [CREATE TAG](create-tag.md)
> * [CREATE TASK](create-task.md) , [CREATE TASK … CLONE](create-clone.md)
> * [CREATE VIEW](create-view.md)

**Classes:**

> * [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](../classes/anomaly-detection/commands/create-anomaly-detection.md)
> * [CREATE BUDGET](../classes/budget/commands/create-budget.md)
> * [CREATE SNOWFLAKE.ML.CLASSIFICATION](../classes/classification/commands/create-classification.md)
> * [CREATE CLASSIFICATION_PROFILE](../classes/classification_profile/commands/create-classification-profile.md)
> * [CREATE CUSTOM_CLASSIFIER](../classes/custom_classifier/commands/create-custom-classifier.md)
> * [CREATE SNOWFLAKE.ML.FORECAST](../classes/forecast/commands/create-forecast.md)
