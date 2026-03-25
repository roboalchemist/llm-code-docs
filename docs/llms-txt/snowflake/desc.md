# Source: https://docs.snowflake.com/en/sql-reference/sql/desc.md

# DESCRIBE *<object>*

Describes the details for the specified object.

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE <object>](create.md) , [SHOW <objects>](show.md)

## DESCRIBE commands

For specific syntax, usage notes, and examples, see:

**Session/Query Operations:**

> * [DESCRIBE RESULT](desc-result.md)
> * [DESCRIBE TRANSACTION](desc-transaction.md)

**Account Objects:**

> * [DESCRIBE APPLICATION](desc-application.md)
> * [DESCRIBE APPLICATION PACKAGE](desc-application-package.md)
> * [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md)
> * [DESCRIBE COMPUTE POOL](desc-compute-pool.md)
> * [DESCRIBE DATABASE](desc-database.md)
> * [DESCRIBE EXTERNAL VOLUME](desc-external-volume.md)
> * [DESCRIBE INTEGRATION](desc-integration.md)
> * [DESCRIBE OPENFLOW DATA PLANE INTEGRATION](desc-oflow-data-plane-integration.md)
> * [DESCRIBE NETWORK POLICY](desc-network-policy.md)
> * [DESCRIBE NOTIFICATION INTEGRATION](desc-notification-integration.md)
> * [DESCRIBE ORGANIZATION PROFILE](desc-organization-profile.md)
> * [DESCRIBE POSTGRES INSTANCE](desc-postgres-instance.md)
> * [DESCRIBE SHARE](desc-share.md)
> * [DESCRIBE SPECIFICATION](desc-specification.md)
> * [DESCRIBE USER](desc-user.md)
> * [DESCRIBE WAREHOUSE](desc-warehouse.md)

**Database Objects:**

> * [DESCRIBE AGENT](desc-agent.md)
> * [DESCRIBE AGGREGATION POLICY](desc-aggregation-policy.md)
> * [DESCRIBE ALERT](desc-alert.md)
> * [DESCRIBE AUTHENTICATION POLICY](desc-authentication-policy.md)
> * [DESCRIBE BACKUP POLICY](desc-backup-policy.md)
> * [DESCRIBE BACKUP SET](desc-backup-set.md)
> * [DESCRIBE CONFIGURATION](desc-configuration.md)
> * [DESCRIBE CORTEX SEARCH SERVICE](desc-cortex-search.md)
> * [DESCRIBE DBT PROJECT](desc-dbt-project.md)
> * [DESCRIBE DYNAMIC TABLE](desc-dynamic-table.md)
> * [DESCRIBE EVENT TABLE](desc-event-table.md)
> * [DESCRIBE EXTERNAL TABLE](desc-external-table.md)
> * [DESCRIBE FEATURE POLICY](desc-feature-policy.md)
> * [DESCRIBE FILE FORMAT](desc-file-format.md)
> * [DESCRIBE FUNCTION](desc-function.md)
> * [DESCRIBE GATEWAY](desc-gateway.md)
> * [DESCRIBE GIT REPOSITORY](desc-git-repository.md)
> * [DESCRIBE ICEBERG TABLE](desc-iceberg-table.md)
> * [DESCRIBE JOIN POLICY](desc-join-policy.md)
> * [DESCRIBE LISTING](desc-listing.md)
> * [DESCRIBE MAINTENANCE POLICY](desc-maintenance-policy.md)
> * [DESCRIBE MASKING POLICY](desc-masking-policy.md)
> * [DESCRIBE MATERIALIZED VIEW](desc-materialized-view.md)
> * [DESCRIBE MCP SERVER](desc-mcp-server.md)
> * [DESCRIBE MODEL MONITOR](desc-model-monitor.md)
> * [DESCRIBE NETWORK RULE](desc-network-rule.md)
> * [DESCRIBE NOTEBOOK](desc-notebook.md)
> * [DESCRIBE ONLINE FEATURE TABLE](desc-online-feature-table.md)
> * [DESCRIBE PACKAGES POLICY](desc-packages-policy.md)
> * [DESCRIBE PASSWORD POLICY](desc-password-policy.md)
> * [DESCRIBE PIPE](desc-pipe.md)
> * [DESCRIBE PRIVACY POLICY](desc-privacy-policy.md)
> * [DESCRIBE PROCEDURE](desc-procedure.md)
> * [DESCRIBE PROJECTION POLICY](desc-projection-policy.md)
> * [DESCRIBE ROW ACCESS POLICY](desc-row-access-policy.md)
> * [DESCRIBE SCHEMA](desc-schema.md)
> * [DESCRIBE SECRET](desc-secret.md)
> * [DESCRIBE SEMANTIC VIEW](desc-semantic-view.md)
> * [DESCRIBE SEQUENCE](desc-sequence.md)
> * [DESCRIBE SERVICE](desc-service.md)
> * [DESCRIBE SESSION POLICY](desc-session-policy.md)
> * [DESCRIBE SNAPSHOT](desc-snapshot.md)
> * [DESCRIBE SNAPSHOT POLICY](desc-snapshot-policy.md) (deprecated; prefer [DESCRIBE BACKUP POLICY](desc-backup-policy.md))
> * [DESCRIBE SNAPSHOT SET](desc-snapshot-set.md) (deprecated; prefer [DESCRIBE BACKUP SET](desc-backup-set.md))
> * [DESCRIBE SPECIFICATION](desc-specification.md)
> * [DESCRIBE STAGE](desc-stage.md)
> * [DESCRIBE STORAGE LIFECYCLE POLICY](desc-storage-lifecycle-policy.md)
> * [DESCRIBE STREAMLIT](desc-streamlit.md)
> * [DESCRIBE STREAM](desc-stream.md)
> * [DESCRIBE TABLE](desc-table.md)
> * [DESCRIBE TASK](desc-task.md)
> * [DESCRIBE VIEW](desc-view.md)
