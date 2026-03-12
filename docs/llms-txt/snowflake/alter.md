# Source: https://docs.snowflake.com/en/sql-reference/sql/alter.md

# ALTER *<object>*

Modifies the metadata of an account-level or database object, or the parameters for a session.

See also:
:   [CREATE <object>](create.md) , [DESCRIBE <object>](desc.md) , [SHOW <objects>](show.md)

## ALTER commands

For specific syntax, usage notes, and examples, see:

**Account and Session Operations:**

> * [ALTER ACCOUNT](alter-account.md) (account administrators only)
> * [ALTER SESSION](alter-session.md) (all users)

**Account Objects:**

> * [ALTER APPLICATION](alter-application.md)
> * [ALTER APPLICATION PACKAGE](alter-application-package.md)
> * [ALTER APPLICATION PACKAGE … RELEASE DIRECTIVE](alter-application-package-release-directive.md)
> * [ALTER APPLICATION PACKAGE … VERSION](alter-application-package-version.md)
> * [ALTER APPLICATION ROLE](alter-application-role.md)
> * [ALTER AUTHENTICATION POLICY](alter-authentication-policy.md)
> * [ALTER CATALOG INTEGRATION](alter-catalog-integration.md)
> * [ALTER COMPUTE POOL](alter-compute-pool.md)
> * [ALTER CONNECTION](alter-connection.md)
> * [ALTER DATABASE](alter-database.md)
> * [ALTER DATABASE (catalog-linked)](alter-database-catalog-linked.md)
> * [ALTER DATABASE ROLE](alter-database-role.md)
> * [ALTER DYNAMIC TABLE](alter-dynamic-table.md)
> * [ALTER EXTERNAL ACCESS INTEGRATION](alter-external-access-integration.md)
> * [ALTER EXTERNAL VOLUME](alter-external-volume.md)
> * [ALTER FAILOVER GROUP](alter-failover-group.md)
> * [ALTER FEATURE POLICY](alter-feature-policy.md)
> * [ALTER NETWORK POLICY](alter-network-policy.md)
> * [ALTER NOTIFICATION INTEGRATION](alter-notification-integration.md)
> * [ALTER ORGANIZATION PROFILE](alter-organization-profile.md)
> * [ALTER POSTGRES INSTANCE](alter-postgres-instance.md)
> * [ALTER REPLICATION GROUP](alter-replication-group.md)
> * [ALTER RESOURCE MONITOR](alter-resource-monitor.md)
> * [ALTER SECURITY INTEGRATION](alter-security-integration.md)
> * [ALTER SHARE](alter-share.md)
> * [ALTER STORAGE INTEGRATION](alter-storage-integration.md)
> * [ALTER ROLE](alter-role.md)
> * [ALTER USER](alter-user.md)
> * [ALTER WAREHOUSE](alter-warehouse.md)

**Database Objects:**

> * [ALTER AGENT](alter-agent.md)
> * [ALTER AGGREGATION POLICY](alter-aggregation-policy.md)
> * [ALTER ALERT](alter-alert.md)
> * [ALTER AUTHENTICATION POLICY](alter-authentication-policy.md)
> * [ALTER BACKUP POLICY](alter-backup-policy.md)
> * [ALTER BACKUP SET](alter-backup-set.md)
> * [ALTER CONTACT](alter-contact.md)
> * [ALTER CORTEX SEARCH SERVICE](alter-cortex-search.md)
> * [ALTER DATASET](alter-dataset.md)
> * [ALTER DATASET … ADD VERSION](alter-dataset-add-version.md)
> * [ALTER DATASET … DROP VERSION](alter-dataset-drop-version.md)
> * [ALTER DBT PROJECT](alter-dbt-project.md)
> * [ALTER EXPERIMENT](alter-experiment.md)
> * [ALTER EXTERNAL TABLE](alter-external-table.md)
> * [ALTER FILE FORMAT](alter-file-format.md)
> * [ALTER FUNCTION](alter-function.md)
> * [ALTER FUNCTION (DMF)](alter-function-dmf.md)
> * [ALTER GIT REPOSITORY](alter-git-repository.md)
> * [ALTER ICEBERG TABLE](alter-iceberg-table.md)
> * [ALTER JOIN POLICY](alter-join-policy.md)
> * [ALTER LISTING](alter-listing.md)
> * [ALTER MAINTENANCE POLICY](alter-maintenance-policy.md)
> * [ALTER MASKING POLICY](alter-masking-policy.md)
> * [ALTER MATERIALIZED VIEW](alter-materialized-view.md)
> * [ALTER MODEL](alter-model.md)
> * [ALTER MODEL … ADD VERSION](alter-model-add-version.md)
> * [ALTER MODEL … DROP VERSION](alter-model-drop-version.md)
> * [ALTER MODEL … MODIFY VERSION](alter-model-modify-version.md)
> * [ALTER MODEL MONITOR](alter-model-monitor.md)
> * [ALTER NETWORK RULE](alter-network-rule.md)
> * [ALTER NOTEBOOK](alter-notebook.md)
> * [ALTER OPENFLOW DATA PLANE](alter-oflow-data-plane.md)
> * [ALTER ONLINE FEATURE TABLE](alter-online-feature-table.md)
> * [ALTER PACKAGES POLICY](alter-packages-policy.md)
> * [ALTER PASSWORD POLICY](alter-password-policy.md)
> * [ALTER PIPE](alter-pipe.md)
> * [ALTER PRIVACY POLICY](alter-privacy-policy.md)
> * [ALTER PROCEDURE](alter-procedure.md)
> * [ALTER PROJECTION POLICY](alter-projection-policy.md)
> * [ALTER ROW ACCESS POLICY](alter-row-access-policy.md)
> * [ALTER SCHEMA](alter-schema.md)
> * [ALTER SECRET](alter-secret.md)
> * [ALTER SEMANTIC VIEW](alter-semantic-view.md)
> * [ALTER SEQUENCE](alter-sequence.md)
> * [ALTER SERVICE](alter-service.md)
> * [ALTER SESSION POLICY](alter-session-policy.md)
> * [ALTER SNAPSHOT](alter-snapshot.md)
> * [ALTER SNAPSHOT POLICY — Deprecated](alter-snapshot-policy.md) (deprecated; prefer [ALTER BACKUP POLICY](alter-backup-policy.md))
> * [ALTER SNAPSHOT SET — Deprecated](alter-snapshot-set.md) (deprecated; prefer [ALTER BACKUP SET](alter-backup-set.md))
> * [ALTER STAGE](alter-stage.md)
> * [ALTER STORAGE LIFECYCLE POLICY](alter-storage-lifecycle-policy.md)
> * [ALTER STREAM](alter-stream.md)
> * [ALTER STREAMLIT](alter-streamlit.md)
> * [ALTER TABLE](alter-table.md)
> * [ALTER TABLE (event tables)](alter-table-event-table.md)
> * [ALTER TAG](alter-tag.md)
> * [ALTER TASK](alter-task.md)
> * [ALTER VIEW](alter-view.md)

**Classes**:

> * [ALTER BUDGET](../classes/budget/commands/alter-budget.md)
> * [ALTER SNOWFLAKE.ML.CLASSIFICATION](../classes/classification/commands/alter-classification.md)
