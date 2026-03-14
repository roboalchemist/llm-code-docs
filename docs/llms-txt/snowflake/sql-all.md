# Source: https://docs.snowflake.com/en/sql-reference/sql-all.md

# All commands (alphabetical)

This topic provides a list of all DDL and DML commands, as well as the SELECT command and other related commands, in alphabetical order.

| Command Name | Summary |
| --- | --- |
| **A** |  |
| [ALTER <object>](sql/alter.md) | Modifies the metadata of an account-level or database object, or the parameters for a session. |
| [ALTER ACCOUNT](sql/alter-account.md) | Modifies an account. |
| [ALTER AGENT](sql/alter-agent.md) | Modifies the properties or specification for an existing [Cortex Agent](../user-guide/snowflake-cortex/cortex-agents.md). |
| [ALTER AGGREGATION POLICY](sql/alter-aggregation-policy.md) | Replaces the existing rules or comment of an [aggregation policy](../user-guide/aggregation-policies.md). |
| [ALTER ALERT](sql/alter-alert.md) | Modifies the properties of an existing alert and suspends or resumes an existing [alert](../user-guide/alerts.md). |
| [ALTER API INTEGRATION](sql/alter-api-integration.md) | Modifies the properties of an existing API integration. |
| [ALTER APPLICATION](sql/alter-application.md) | Modifies the properties of an installed Snowflake Native App. |
| [ALTER APPLICATION DROP SPECIFICATION](sql/alter-application-drop-app-spec.md) | Drops an app specification from an app. |
| [ALTER APPLICATION DROP CONFIGURATION DEFINITION](sql/alter-application-drop-configuration-definition.md) | Deletes the [app configuration definition](../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App. |
| [ALTER APPLICATION PACKAGE](sql/alter-application-package.md) | Modifies the properties of an existing application package. |
| [ALTER APPLICATION PACKAGE … MODIFY RELEASE CHANNEL](sql/alter-application-package-release-channel.md) | Modifies the release channels defined for an existing application package. |
| [ALTER APPLICATION PACKAGE … RELEASE DIRECTIVE](sql/alter-application-package-release-directive.md) | Modifies the properties of an existing application package. |
| [ALTER APPLICATION PACKAGE … VERSION](sql/alter-application-package-version.md) | Modifies the versioning of an existing application package in the Snowflake Native App Framework. |
| [ALTER APPLICATION ROLE](sql/alter-application-role.md) | Modifies the properties for an existing application role. |
| [ALTER APPLICATION … { APPROVE | DECLINE} SPECIFICATION](sql/alter-application-sequence-number.md) | Approves or declines an [app specification](../developer-guide/native-apps/requesting-app-specs.md) using the specified sequence number. |
| [ALTER APPLICATION SET SPECIFICATION](sql/alter-application-set-app-spec.md) | Creates or updates an [app specification](../developer-guide/native-apps/requesting-app-specs.md) for a Snowflake Native App. |
| [ALTER APPLICATION SET CONFIGURATION DEFINITION](sql/alter-application-set-configuration-definition.md) | Creates or updates an [app configuration](../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App. |
| [ALTER APPLICATION SET CONFIGURATION VALUE](sql/alter-application-set-configuration-value.md) | Sets a value in an [app configuration definition](../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App. |
| [ALTER APPLICATION UNSET CONFIGURATION](sql/alter-application-unset-configuration.md) | Unsets an [app configuration definition](../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App. |
| [ALTER AUTHENTICATION POLICY](sql/alter-authentication-policy.md) | Modifies the properties of an [authentication policy](../user-guide/authentication-policies.md). |
| [ALTER BACKUP POLICY](sql/alter-backup-policy.md) | Modifies the properties of a [backup](../user-guide/backups.md) policy. |
| [ALTER BACKUP SET](sql/alter-backup-set.md) | Modifies the properties for a [backup](../user-guide/backups.md) set. |
| [ALTER CATALOG INTEGRATION](sql/alter-catalog-integration.md) | Modifies the properties of an existing [catalog integration](../user-guide/tables-iceberg.md). |
| [ALTER COMPUTE POOL](sql/alter-compute-pool.md) | Modifies the properties of an existing [compute pool](../developer-guide/snowpark-container-services/working-with-compute-pool.md). |
| [ALTER CONNECTION](sql/alter-connection.md) | Modifies the properties for an existing [connection](../user-guide/client-redirect.md). |
| [ALTER CONTACT](sql/alter-contact.md) | Modifies the properties of an existing [contact](../user-guide/contacts-using.md). |
| [ALTER CORTEX SEARCH SERVICE](sql/alter-cortex-search.md) | Suspends, resumes, or modifies the properties of an existing [Cortex Search service](../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md). |
| [ALTER DATABASE](sql/alter-database.md) | Modifies the properties for an existing database. |
| [ALTER DATABASE (catalog-linked)](sql/alter-database-catalog-linked.md) | Modifies the properties for an existing [catalog-linked database](../user-guide/tables-iceberg-catalog-linked-database.md). |
| [ALTER DATABASE ROLE](sql/alter-database-role.md) | Modifies the properties for an existing database role. |
| [ALTER DATASET](sql/alter-dataset.md) | Modifies a dataset by adding or dropping dataset versions. |
| [ALTER DATASET … ADD VERSION](sql/alter-dataset-add-version.md) | Adds a version to a dataset. |
| [ALTER DATASET … DROP VERSION](sql/alter-dataset-drop-version.md) | Drops a dataset version. |
| [ALTER DBT PROJECT](sql/alter-dbt-project.md) | Modifies the properties of an existing [dbt project object](../user-guide/data-engineering/dbt-projects-on-snowflake.md). |
| [ALTER DYNAMIC TABLE](sql/alter-dynamic-table.md) | Modifies the properties of a [dynamic table](../user-guide/dynamic-tables-about.md). |
| [ALTER EXPERIMENT](sql/alter-experiment.md) | Modifies the properties of an existing [experiment](../developer-guide/snowflake-ml/experiments.md). |
| [ALTER EXTERNAL ACCESS INTEGRATION](sql/alter-external-access-integration.md) | Modifies the properties of an existing [external access integration](../developer-guide/external-network-access/creating-using-external-network-access.md). |
| [ALTER EXTERNAL TABLE](sql/alter-external-table.md) | Modifies the properties, columns, or constraints for an existing external table. |
| [ALTER EXTERNAL VOLUME](sql/alter-external-volume.md) | Modifies the properties for an existing [external volume](../user-guide/tables-iceberg.md). |
| [ALTER FAILOVER GROUP](sql/alter-failover-group.md) | Modifies the properties for an existing [failover group](../user-guide/account-replication-intro.md). |
| [ALTER FEATURE POLICY](sql/alter-feature-policy.md) | Alters or renames a [feature policy](../developer-guide/native-apps/ui-consumer-feature-policies.md). |
| [ALTER FILE FORMAT](sql/alter-file-format.md) | Modifies the properties for an existing file format object. |
| [ALTER FUNCTION](sql/alter-function.md) | Modifies the properties of an existing user-defined or external function. |
| [ALTER FUNCTION (DMF)](sql/alter-function-dmf.md) | Modifies the properties of an existing data metric function (DMF). |
| [ALTER FUNCTION (Snowpark Container Services)](sql/alter-function-spcs.md) | Modifies the properties of an existing [service function](../developer-guide/snowpark-container-services/working-with-services.md). |
| [ALTER GATEWAY](sql/alter-gateway.md) | Modifies the configuration of an existing [gateway](../developer-guide/snowpark-container-services/gateway.md). |
| [ALTER GIT REPOSITORY](sql/alter-git-repository.md) | Modifies the properties of a Snowflake [Git repository clone](../developer-guide/git/git-overview.md). |
| [ALTER ICEBERG TABLE](sql/alter-iceberg-table.md) | Modifies properties such as clustering options and tags for an existing [Apache Iceberg™ table](../user-guide/tables-iceberg.md). |
| [ALTER ICEBERG TABLE … ALTER COLUMN … SET DATA TYPE (structured types)](sql/alter-iceberg-table-alter-column-set-data-type.md) | Modifies (evolves) a [structured type](data-types-structured.md) column in a Snowflake-managed [Apache Iceberg™ table](../user-guide/tables-iceberg.md). |
| [ALTER ICEBERG TABLE … CONVERT TO MANAGED](sql/alter-iceberg-table-convert-to-managed.md) | Converts an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) that uses an external Iceberg catalog into a table that uses Snowflake as the catalog (a Snowflake-managed Iceberg table). |
| [ALTER ICEBERG TABLE … REFRESH](sql/alter-iceberg-table-refresh.md) | Refreshes the metadata for an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) that uses an external Iceberg catalog. |
| [ALTER INTEGRATION](sql/alter-integration.md) | Modifies the properties for an existing integration. |
| [ALTER JOIN POLICY](sql/alter-join-policy.md) | Replaces the existing rules or comment for a [join policy](../user-guide/join-policies.md). |
| [ALTER LISTING](sql/alter-listing.md) | Modifies the properties of a [listings](../collaboration/collaboration-listings-about.md) with an inline YAML manifest, or from a file located in a stage location. |
| [ALTER MAINTENANCE POLICY](sql/alter-maintenance-policy.md) | Modifies an existing [maintenance policy](../developer-guide/native-apps/consumer-maintenance-policies.md). |
| [ALTER MASKING POLICY](sql/alter-masking-policy.md) | Replaces the existing masking policy rules with new rules or a new comment and allows the renaming of a masking policy. |
| [ALTER MATERIALIZED VIEW](sql/alter-materialized-view.md) | Alters a materialized view in the current/specified schema. |
| [ALTER MODEL](sql/alter-model.md) | Modifies the properties for an existing model, including its name, tags, default version, or comment. |
| [ALTER MODEL … ADD VERSION](sql/alter-model-add-version.md) | Adds a new version to an existing model from an existing model version. |
| [ALTER MODEL … DROP VERSION](sql/alter-model-drop-version.md) | Removes a version from the specified machine learning model. |
| [ALTER MODEL … MODIFY VERSION](sql/alter-model-modify-version.md) | Modifies a version of a model, changing the version’s comment or metadata. |
| [ALTER MODEL MONITOR](sql/alter-model-monitor.md) | Modifies the properties of a [model monitor](../developer-guide/snowflake-ml/model-registry/model-observability.md). |
| [ALTER NETWORK POLICY](sql/alter-network-policy.md) | Modifies the properties for an existing network policy. |
| [ALTER NETWORK RULE](sql/alter-network-rule.md) | Modifies an existing network rule. |
| [ALTER NOTEBOOK](sql/alter-notebook.md) | Modifies the properties of an existing [notebook](../user-guide/ui-snowsight/notebooks.md). |
| [ALTER NOTIFICATION INTEGRATION](sql/alter-notification-integration.md) | Modifies the properties for an existing notification integration. |
| [ALTER NOTIFICATION INTEGRATION (email)](sql/alter-notification-integration-email.md) | Modifies the properties for an existing notification integration for [sending email messages](../user-guide/notifications/email-notifications.md). |
| [ALTER NOTIFICATION INTEGRATION (inbound from an Azure Event Grid topic)](sql/alter-notification-integration-queue-inbound-azure.md) | Modifies the properties for an existing notification integration for receiving messages from an Azure Event Grid topic. |
| [ALTER NOTIFICATION INTEGRATION (inbound from a Google Pub/Sub topic)](sql/alter-notification-integration-queue-inbound-gcp.md) | Modifies the properties for an existing notification integration for receiving messages from a Google Pub/Sub topic. |
| [ALTER NOTIFICATION INTEGRATION (outbound to an Amazon SNS topic)](sql/alter-notification-integration-queue-outbound-aws.md) | Modifies the properties for an existing notification integration for [sending a message to an Amazon SNS topic](../user-guide/notifications/creating-notification-integration-amazon-sns.md). |
| [ALTER NOTIFICATION INTEGRATION (outbound to an Azure Event Grid topic)](sql/alter-notification-integration-queue-outbound-azure.md) | Modifies the properties for an existing notification integration for [sending a message to an Azure Event Grid topic](../user-guide/notifications/creating-notification-integration-azure-event-grid.md). |
| [ALTER NOTIFICATION INTEGRATION (outbound to a Google Pub/Sub topic)](sql/alter-notification-integration-queue-outbound-gcp.md) | Modifies the properties for an existing notification integration for [sending a message to a Google Pub/Sub topic](../user-guide/notifications/creating-notification-integration-google-pubsub.md). |
| [ALTER NOTIFICATION INTEGRATION (webhooks)](sql/alter-notification-integration-webhooks.md) | Modifies the properties for an existing notification integration for a [webhook](../user-guide/notifications/webhook-notifications.md). |
| [ALTER OPENFLOW DATA PLANE](sql/alter-oflow-data-plane.md) | Modifies an Openflow data plane integration. |
| [ALTER ONLINE FEATURE TABLE](sql/alter-online-feature-table.md) | Modifies the properties of an existing [online feature table](sql/create-online-feature-table.md). |
| [ALTER ORGANIZATION ACCOUNT](sql/alter-organization-account.md) | Modifies the properties of an existing [organization account](../user-guide/organization-accounts.md). |
| [ALTER ORGANIZATION PROFILE](sql/alter-organization-profile.md) | Modifies the properties of an [organization profile](../user-guide/collaboration/organization-profiles/org-profiles-create-manage.md) using an inline YAML manifest, or using a YAML manifest file located in a stage location. |
| [ALTER ORGANIZATION USER](sql/alter-organization-user.md) | Modifies the properties of an existing [organization user](../user-guide/organization-users.md). |
| [ALTER ORGANIZATION USER GROUP](sql/alter-organization-user-group.md) | Modifies the properties of an existing [organization user group](../user-guide/organization-users.md). |
| [ALTER PACKAGES POLICY](sql/alter-packages-policy.md) | Modifies the properties for an existing [packages policy](../developer-guide/udf/python/packages-policy.md). |
| [ALTER PASSWORD POLICY](sql/alter-password-policy.md) | Modifies the properties for an existing password policy. |
| [ALTER PIPE](sql/alter-pipe.md) | Modifies a limited set of properties for an existing pipe object. |
| [ALTER POSTGRES INSTANCE](sql/alter-postgres-instance.md) | Modifies the properties of an existing [Snowflake Postgres instance](../user-guide/snowflake-postgres/about.md). |
| [ALTER PRIVACY POLICY](sql/alter-privacy-policy.md) | Modifies the properties of an existing [privacy policy](../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md). |
| [ALTER PROCEDURE](sql/alter-procedure.md) | Modifies the properties for an existing stored procedure. |
| [ALTER PROJECTION POLICY](sql/alter-projection-policy.md) | Replaces the existing [projection policy](../user-guide/projection-policies.md) rules with new rules or a new comment and allows the renaming of a projection policy. |
| [ALTER REPLICATION GROUP](sql/alter-replication-group.md) | Modifies the properties for an existing [replication group](../user-guide/account-replication-intro.md). |
| [ALTER RESOURCE MONITOR](sql/alter-resource-monitor.md) | Modifies the properties and triggers for an existing [resource monitor](../user-guide/resource-monitors.md). |
| [ALTER ROLE](sql/alter-role.md) | Modifies the properties for an existing [custom role](../user-guide/security-access-control-overview.md). |
| [ALTER ROW ACCESS POLICY](sql/alter-row-access-policy.md) | Modifies the properties for an existing row access policy, including renaming the policy or replacing the policy rules. |
| [ALTER SCHEMA](sql/alter-schema.md) | Modifies the properties for an existing schema, including renaming the schema or swapping it with another schema, and changing the Time Travel data retention period (if you are using Snowflake Enterprise Edition or higher). |
| [ALTER SECRET](sql/alter-secret.md) | Modifies the properties of an existing secret. |
| [ALTER SECURITY INTEGRATION](sql/alter-security-integration.md) | Modifies the properties for an existing security integration. |
| [ALTER SECURITY INTEGRATION (External API Authentication)](sql/alter-security-integration-api-auth.md) | Modifies the properties of an existing security integration created for External API Authentication. |
| [ALTER SECURITY INTEGRATION (AWS IAM Authentication)](sql/alter-security-integration-aws-iam.md) | Modifies the properties of an existing security integration created for authenticating with AWS IAM. |
| [ALTER SECURITY INTEGRATION (External OAuth)](sql/alter-security-integration-oauth-external.md) | Modifies the properties of an existing security integration created for External OAuth. |
| [ALTER SECURITY INTEGRATION (Snowflake OAuth)](sql/alter-security-integration-oauth-snowflake.md) | Modifies the properties of an existing security integration created for a Snowflake OAuth client. |
| [ALTER SECURITY INTEGRATION (SAML2)](sql/alter-security-integration-saml2.md) | Modifies the properties of an existing SAML2 security integration. |
| [ALTER SECURITY INTEGRATION (SCIM)](sql/alter-security-integration-scim.md) | Modifies the properties of an existing SCIM security integration. |
| [ALTER SEMANTIC VIEW](sql/alter-semantic-view.md) | Modifies the comment for an existing [semantic view](../user-guide/views-semantic/overview.md) or renames a semantic view. |
| [ALTER SEQUENCE](sql/alter-sequence.md) | Modifies the properties for an existing sequence. |
| [ALTER SERVICE](sql/alter-service.md) | Modifies [Snowpark Container Services service](../developer-guide/snowpark-container-services/working-with-services.md) configuration, upgrades the code for the service, and allows you to suspend or resume a service. |
| [ALTER SESSION](sql/alter-session.md) | Sets parameters that change the behavior for the current session. |
| [ALTER SESSION POLICY](sql/alter-session-policy.md) | Modifies the properties for an existing session policy. |
| [ALTER SHARE](sql/alter-share.md) | Modifies the properties for an existing [share](../user-guide/data-sharing-intro.md). |
| [ALTER SNAPSHOT](sql/alter-snapshot.md) | Modifies the properties of an existing [snapshot of a block storage volume](../developer-guide/snowpark-container-services/block-storage-volume.md). |
| [ALTER SNAPSHOT POLICY — Deprecated](sql/alter-snapshot-policy.md) | Modifies the properties of a [snapshot](../user-guide/backups.md) policy. |
| [ALTER SNAPSHOT SET — Deprecated](sql/alter-snapshot-set.md) | Modifies the properties for a [snapshot](../user-guide/backups.md) set. |
| [ALTER STAGE](sql/alter-stage.md) | Modifies the properties for an existing named internal or external stage. |
| [ALTER STORAGE INTEGRATION](sql/alter-storage-integration.md) | Modifies the properties for an existing storage integration. |
| [ALTER STORAGE LIFECYCLE POLICY](sql/alter-storage-lifecycle-policy.md) | Modifies the properties of an existing [storage lifecycle policy](../user-guide/storage-management/storage-lifecycle-policies.md). |
| [ALTER STREAM](sql/alter-stream.md) | Modifies the properties, columns, or constraints for an existing [stream](../user-guide/streams-intro.md). |
| [ALTER STREAMLIT](sql/alter-streamlit.md) | Modifies the properties of an existing Streamlit object. |
| [ALTER TABLE](sql/alter-table.md) | Modifies the properties, columns, or constraints for an existing table. |
| [ALTER TABLE … ALTER COLUMN](sql/alter-table-column.md) | This topic describes how to modify one or more column properties for a table using an `ALTER COLUMN` clause in a [ALTER TABLE](sql/alter-table.md) statement. |
| [ALTER TABLE (event tables)](sql/alter-table-event-table.md) | Modifies the properties, columns, or constraints for an existing [event table](../developer-guide/logging-tracing/event-table-setting-up.md). |
| [ALTER TAG](sql/alter-tag.md) | Modifies the properties for an existing tag, including renaming the tag and setting a masking policy on a tag. |
| [ALTER TASK](sql/alter-task.md) | Modifies the properties for an existing task. |
| [ALTER USER](sql/alter-user.md) | Modifies the properties and object/session parameters for an existing user in the system. |
| [ALTER USER … ADD PROGRAMMATIC ACCESS TOKEN (PAT)](sql/alter-user-add-programmatic-access-token.md) | Creates a [programmatic access token](../user-guide/programmatic-access-tokens.md) for a user. |
| [ALTER USER … MODIFY PROGRAMMATIC ACCESS TOKEN (PAT)](sql/alter-user-modify-programmatic-access-token.md) | Changes the name of a [programmatic access token](../user-guide/programmatic-access-tokens.md) or a property of the token. |
| [ALTER USER … REMOVE PROGRAMMATIC ACCESS TOKEN (PAT)](sql/alter-user-remove-programmatic-access-token.md) | Revokes a [programmatic access token](../user-guide/programmatic-access-tokens.md) for a user. |
| [ALTER USER … ROTATE PROGRAMMATIC ACCESS TOKEN (PAT)](sql/alter-user-rotate-programmatic-access-token.md) | Rotates [programmatic access token](../user-guide/programmatic-access-tokens.md), generating a new token secret with an extended expiration time, and expiring the existing token secret. |
| [ALTER VIEW](sql/alter-view.md) | Modifies the properties for an existing view. |
| [ALTER WAREHOUSE](sql/alter-warehouse.md) | Suspends or resumes a [virtual warehouse](../user-guide/warehouses-overview.md), or aborts all queries (and other SQL statements) for a warehouse. |
| **B** |  |
| [BEGIN](sql/begin.md) | Begins a transaction in the current session. |
| **C** |  |
| [CALL](sql/call.md) | Calls a [stored procedure](../developer-guide/stored-procedure/stored-procedures-overview.md). |
| [CALL (with anonymous procedure)](sql/call-with.md) | Creates and calls an anonymous procedure that is like a [stored procedure](../developer-guide/stored-procedure/stored-procedures-overview.md) but is not stored for later use. |
| [COMMENT](sql/comment.md) | Adds a comment or overwrites an existing comment for an existing object. |
| [COMMIT](sql/commit.md) | Commits an open transaction in the current session. |
| [COPY FILES](sql/copy-files.md) | Copy files from a source location to an output stage. |
| [COPY INTO <location>](sql/copy-into-location.md) | Unloads data from a table (or query) into one or more files in one of the following locations. |
| [COPY INTO <table>](sql/copy-into-table.md) | Loads data from files to an existing table. |
| [CREATE <object>](sql/create.md) | Creates a new object of the specified type. |
| [CREATE ACCOUNT](sql/create-account.md) | Creates a new account in your organization. |
| [CREATE AGENT](sql/create-agent.md) | Creates a new [Cortex Agent](../user-guide/snowflake-cortex/cortex-agents.md) object with the specified attributes and specification. |
| [CREATE AGGREGATION POLICY](sql/create-aggregation-policy.md) | Creates a new [aggregation policy](../user-guide/aggregation-policies.md) in the current/specified schema or replaces an existing aggregation policy. |
| [CREATE ALERT](sql/create-alert.md) | Creates a new [alert](../user-guide/alerts.md) in the current schema. |
| [CREATE API INTEGRATION](sql/create-api-integration.md) | Creates a new API integration object in the account or replaces an existing API integration. |
| [CREATE APPLICATION](sql/create-application.md) | Creates a Snowflake Native App based on an application package or listing. |
| [CREATE APPLICATION PACKAGE](sql/create-application-package.md) | Creates a new application package that contains the data content and application logic of Snowflake Native App. |
| [CREATE APPLICATION ROLE](sql/create-application-role.md) | Creates a new application role or replaces an existing application role. |
| [CREATE AUTHENTICATION POLICY](sql/create-authentication-policy.md) | Creates a new [authentication policy](../user-guide/authentication-policies.md) in the current or specified schema or replaces an existing authentication policy. |
| [CREATE BACKUP POLICY](sql/create-backup-policy.md) | Creates a [backup](../user-guide/backups.md) policy. |
| [CREATE BACKUP SET](sql/create-backup-set.md) | Creates a [backup](../user-guide/backups.md) set for a table, a schema, or a database. |
| [CREATE CATALOG INTEGRATION](sql/create-catalog-integration.md) | Creates a new [catalog integration](../user-guide/tables-iceberg.md) for [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) in the account or replaces an existing catalog integration. |
| [CREATE CATALOG INTEGRATION (AWS Glue)](sql/create-catalog-integration-glue.md) | Creates a new [catalog integration](../user-guide/tables-iceberg.md) in the account or replaces an existing catalog integration for [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) that use AWS Glue as the catalog. |
| [CREATE CATALOG INTEGRATION (Object storage)](sql/create-catalog-integration-object-storage.md) | Creates a new [catalog integration](../user-guide/tables-iceberg.md) in the account or replaces an existing catalog integration for the following sources. |
| [CREATE CATALOG INTEGRATION (Snowflake Open Catalog)](sql/create-catalog-integration-open-catalog.md) | Creates a new [catalog integration](../user-guide/tables-iceberg.md) for [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) that integrate with [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview) in the account or replaces an existing catalog integration. |
| [CREATE CATALOG INTEGRATION (Apache Iceberg™ REST)](sql/create-catalog-integration-rest.md) | Creates a new [catalog integration](../user-guide/tables-iceberg.md) in the account or replaces an existing catalog integration for [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) managed in a remote catalog that complies with the open source [Apache Iceberg™ REST OpenAPI specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml). |
| [CREATE CATALOG INTEGRATION (SAP® Business Data Cloud)](sql/create-catalog-integration-sap.md) | Creates a new catalog integration in the account or replaces an existing catalog integration for SAP® Business Data Cloud to interact with SAP® Data Products managed in the SAP® Business Data Cloud object store. |
| [CREATE <object> … CLONE](sql/create-clone.md) | Creates a copy of an existing object in the system. |
| [CREATE COMPUTE POOL](sql/create-compute-pool.md) | Creates a new [compute pool](../developer-guide/snowpark-container-services/working-with-compute-pool.md) in the current account. |
| [CREATE CONNECTION](sql/create-connection.md) | Creates a new [connection](../user-guide/client-redirect.md) in the account. |
| [CREATE CONTACT](sql/create-contact.md) | Creates a new [contact](../user-guide/contacts-using.md) or replaces an existing contact. |
| [CREATE CORTEX SEARCH SERVICE](sql/create-cortex-search.md) | Creates a new [Cortex Search service](../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md) or replaces an existing one. |
| [CREATE DATA METRIC FUNCTION](sql/create-data-metric-function.md) | Creates a new data metric function (DMF) in the current or specified schema, or replaces an existing data metric function. |
| [CREATE DATABASE](sql/create-database.md) | Creates a new database in the system. |
| [CREATE DATABASE (catalog-linked)](sql/create-database-catalog-linked.md) | Creates a new [catalog-linked database](../user-guide/tables-iceberg-catalog-linked-database.md) for Apache Iceberg™ tables that use an external Iceberg REST catalog. |
| [CREATE DATABASE ROLE](sql/create-database-role.md) | Create a new [database role](../user-guide/security-access-control-considerations.md) or replace an existing database role in the system. |
| [CREATE DATASET](sql/create-dataset.md) | Creates a new [machine learning dataset](../developer-guide/snowflake-ml/dataset.md) in the current schema or the schema that you specify. |
| [CREATE DBT PROJECT](sql/create-dbt-project.md) | Creates a new [dbt project object](../user-guide/data-engineering/dbt-projects-on-snowflake.md) or replaces an existing dbt project. |
| [CREATE DYNAMIC TABLE](sql/create-dynamic-table.md) | Creates a [dynamic table](../user-guide/dynamic-tables-about.md), based on a specified query. |
| [CREATE EVENT TABLE](sql/create-event-table.md) | Creates an [event table](../developer-guide/logging-tracing/event-table-setting-up.md) that captures events, including logged messages from functions and procedures. |
| [CREATE EXPERIMENT](sql/create-experiment.md) | Creates a new [experiment](../developer-guide/snowflake-ml/experiments.md) or replaces an existing experiment. |
| [CREATE EXTERNAL ACCESS INTEGRATION](sql/create-external-access-integration.md) | Creates an [external access integration](../developer-guide/external-network-access/creating-using-external-network-access.md) for access to external network locations from a UDF or procedure handler. |
| [CREATE EXTERNAL FUNCTION](sql/create-external-function.md) | Creates a new [external function](external-functions.md). |
| [CREATE EXTERNAL TABLE](sql/create-external-table.md) | Creates a new [external table](../user-guide/tables-external-intro.md) in the current or specified schema or replaces an existing external table. |
| [CREATE EXTERNAL VOLUME](sql/create-external-volume.md) | Creates a new [external volume](../user-guide/tables-iceberg.md) for [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) in the account or replaces an existing external volume. |
| [CREATE FAILOVER GROUP](sql/create-failover-group.md) | Creates a new [failover group](../user-guide/account-replication-intro.md) of specified objects in the system. |
| [CREATE FEATURE POLICY](sql/create-feature-policy.md) | Creates a new [feature policy](../developer-guide/native-apps/ui-consumer-feature-policies.md). |
| [CREATE FILE FORMAT](sql/create-file-format.md) | Creates a named file format that describes a set of staged data to access or load into Snowflake tables. |
| [CREATE FUNCTION](sql/create-function.md) | Creates a new [UDF (user-defined function)](../developer-guide/udf/udf-overview.md). |
| [CREATE FUNCTION (Snowpark Container Services)](sql/create-function-spcs.md) | Creates a [service function](../developer-guide/snowpark-container-services/working-with-services.md). |
| [CREATE GATEWAY](sql/create-gateway.md) | Creates a new [gateway](../developer-guide/snowpark-container-services/gateway.md) in the current schema. |
| [CREATE GIT REPOSITORY](sql/create-git-repository.md) | Creates a Snowflake Git repository clone in the schema or replaces an existing Git repository clone. |
| [CREATE HYBRID TABLE](sql/create-hybrid-table.md) | Creates a new hybrid table in the current/specified schema or replaces an existing table. |
| [CREATE ICEBERG TABLE](sql/create-iceberg-table.md) | Creates or replaces an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) in the current/specified schema. |
| [CREATE ICEBERG TABLE (AWS Glue as the Iceberg catalog)](sql/create-iceberg-table-aws-glue.md) | Creates or replaces an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) in the current/specified schema using an Iceberg table that is registered in the AWS Glue Data Catalog. |
| [CREATE ICEBERG TABLE (Delta files in object storage)](sql/create-iceberg-table-delta.md) | Creates or replaces an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) in the current/specified schema using Delta table files in object storage (external cloud storage). |
| [CREATE ICEBERG TABLE (Iceberg files in object storage)](sql/create-iceberg-table-iceberg-files.md) | Creates or replaces an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) in the current/specified schema using Iceberg files in object storage (external cloud storage). |
| [CREATE ICEBERG TABLE (Iceberg REST catalog)](sql/create-iceberg-table-rest.md) | Creates or replaces an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) in the current/specified schema for an Iceberg REST catalog. |
| [CREATE ICEBERG TABLE (Snowflake as the Iceberg catalog)](sql/create-iceberg-table-snowflake.md) | Creates or replaces an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) that uses [Snowflake as the Iceberg catalog](../user-guide/tables-iceberg.md) in the current/specified schema. |
| [CREATE IMAGE REPOSITORY](sql/create-image-repository.md) | Creates a new [image repository](../developer-guide/snowpark-container-services/working-with-registry-repository.md) in the current schema. |
| [CREATE INDEX](sql/create-index.md) | Creates a new secondary index in an existing [hybrid table](../user-guide/tables-hybrid.md) and populates the index with data. |
| [CREATE INTEGRATION](sql/create-integration.md) | Creates a new integration in the system or replaces an existing integration. |
| [CREATE INTERACTIVE TABLE](sql/create-interactive-table.md) | Creates a new [interactive table](../user-guide/interactive.md) in the current/specified schema or replaces an existing table. |
| [CREATE INTERACTIVE WAREHOUSE](sql/create-interactive-warehouse.md) | Creates a new interactive [virtual warehouse](../user-guide/warehouses-overview.md) optimized for low-latency, high-concurrency workloads with interactive tables. |
| [CREATE JOIN POLICY](sql/create-join-policy.md) | Creates a new [join policy](../user-guide/join-policies.md) in the current/specified schema or replaces an existing join policy. |
| [CREATE LISTING](sql/create-listing.md) | Create a free listing to share directly with specific consumers, with an inline YAML manifest, or from a file located in a stage location. |
| [CREATE MAINTENANCE POLICY](sql/create-maintenance-policy.md) | Creates a new [maintenance policy](../developer-guide/native-apps/consumer-maintenance-policies.md) in the current or specified schema. |
| [CREATE MANAGED ACCOUNT](sql/create-managed-account.md) | Creates a new managed account. |
| [CREATE MASKING POLICY](sql/create-masking-policy.md) | Creates a new masking policy in the current/specified schema or replaces an existing masking policy. |
| [CREATE MATERIALIZED VIEW](sql/create-materialized-view.md) | Creates a new materialized view in the current/specified schema, based on a query of an existing table, and populates the view with data. |
| [CREATE MCP SERVER](sql/create-mcp-server.md) | Creates a new MCP (Model Context Protocol) server or replaces an existing MCP server. |
| [CREATE MODEL](sql/create-model.md) | Creates a new machine learning model in the current/specified schema or replaces an existing model. |
| [CREATE MODEL MONITOR](sql/create-model-monitor.md) | Create or replace a [model monitor](../developer-guide/snowflake-ml/model-registry/model-observability.md) in the current or specified schema. |
| [CREATE NETWORK POLICY](sql/create-network-policy.md) | Creates a network policy or replaces an existing network policy. |
| [CREATE NETWORK RULE](sql/create-network-rule.md) | Creates a network rule or replaces an existing network rule. |
| [CREATE NOTEBOOK](sql/create-notebook.md) | Creates a new [Snowflake notebook](../user-guide/ui-snowsight/notebooks.md) or replaces an existing notebook. |
| [CREATE NOTEBOOK PROJECT](sql/create-notebook-project.md) |  |
| [CREATE NOTIFICATION INTEGRATION](sql/create-notification-integration.md) | Creates a new notification integration in the account or replaces an existing integration. |
| [CREATE NOTIFICATION INTEGRATION (email)](sql/create-notification-integration-email.md) | Creates a new notification integration in the account or replaces an existing integration for [sending email messages](../user-guide/notifications/email-notifications.md). |
| [CREATE NOTIFICATION INTEGRATION (inbound from an Azure Event Grid topic)](sql/create-notification-integration-queue-inbound-azure.md) | Creates a new notification integration in the account or replaces an existing integration for receiving messages from an Azure Event Grid topic. |
| [CREATE NOTIFICATION INTEGRATION (inbound from a Google Pub/Sub topic)](sql/create-notification-integration-queue-inbound-gcp.md) | Creates a new notification integration in the account or replaces an existing integration for receiving messages from a Google Pub/Sub topic. |
| [CREATE NOTIFICATION INTEGRATION (outbound to an Amazon SNS topic)](sql/create-notification-integration-queue-outbound-aws.md) | Creates a new notification integration in the account or replaces an existing integration for [sending a message to an Amazon SNS topic](../user-guide/notifications/creating-notification-integration-amazon-sns.md). |
| [CREATE NOTIFICATION INTEGRATION (outbound to an Azure Event Grid topic)](sql/create-notification-integration-queue-outbound-azure.md) | Creates a new notification integration in the account or replaces an existing integration for [sending a message to an Azure Event Grid topic](../user-guide/notifications/creating-notification-integration-azure-event-grid.md). |
| [CREATE NOTIFICATION INTEGRATION (outbound to a Google Pub/Sub topic)](sql/create-notification-integration-queue-outbound-gcp.md) | Creates a new notification integration in the account or replaces an existing integration for [sending a message to a Google Pub/Sub topic](../user-guide/notifications/creating-notification-integration-google-pubsub.md). |
| [CREATE NOTIFICATION INTEGRATION (webhooks)](sql/create-notification-integration-webhooks.md) | Creates a new notification integration or replaces an existing integration for a [webhook](../user-guide/notifications/webhook-notifications.md). |
| [CREATE ONLINE FEATURE TABLE](sql/create-online-feature-table.md) | Creates a new online feature table in the current/specified schema or replaces an existing table. |
| [CREATE OR ALTER <object>](sql/create-or-alter.md) | CREATE OR ALTER commands are DDL commands that combine the functionality of the CREATE command and the ALTER command, enabling you to define an object using the syntax supported by the CREATE <object> command with the limitations of the ALTER <object> command. |
| [CREATE ORGANIZATION ACCOUNT](sql/create-organization-account.md) | Creates a new [organization account](../user-guide/organization-accounts.md). |
| [CREATE ORGANIZATION LISTING](sql/create-organization-listing.md) | Create an organization listing to share data products securely within your organization. |
| [CREATE ORGANIZATION PROFILE](sql/create-organization-profile.md) | Create the organization profile that forms part of the Uniform Listing Locator (ULL) used to publish organizational listings or query organizational listing information without mounting the listing. |
| [CREATE ORGANIZATION USER](sql/create-organization-user.md) | Creates a new [organization user](../user-guide/organization-users.md). |
| [CREATE ORGANIZATION USER GROUP](sql/create-organization-user-group.md) | Creates a new [organization user group](../user-guide/organization-users.md). |
| [CREATE PACKAGES POLICY](sql/create-packages-policy.md) | Creates a new [packages policy](../developer-guide/udf/python/packages-policy.md) or replaces an existing packages policy. |
| [CREATE PASSWORD POLICY](sql/create-password-policy.md) | Creates a new password policy or replaces an existing password policy. |
| [CREATE PIPE](sql/create-pipe.md) | Creates a new pipe in the system for defining the [COPY INTO <table>](sql/copy-into-table.md) statement used by [Snowpipe](../user-guide/data-load-snowpipe-intro.md) to load data from an ingestion queue, or by [Snowpipe Streaming with high-performance architecture](../user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview.md) to load data from a streaming source directly into tables. |
| [CREATE POSTGRES INSTANCE](sql/create-postgres-instance.md) | Creates a new [Snowflake Postgres instance](../user-guide/snowflake-postgres/about.md) or creates a fork of an existing instance. |
| [CREATE PRIVACY POLICY](sql/create-privacy-policy.md) | Creates a new [privacy policy](../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) or replaces an existing privacy policy. |
| [CREATE PROCEDURE](sql/create-procedure.md) | Creates a new [stored procedure](../developer-guide/stored-procedure/stored-procedures-usage.md). |
| [CREATE PROJECTION POLICY](sql/create-projection-policy.md) | Creates a new [projection policy](../user-guide/projection-policies.md) in the current/specified schema or replaces an existing projection policy. |
| [CREATE PROVISIONED THROUGHPUT](sql/create-provisioned-throughput.md) | Creates a new [Provisioned Throughput resource](../user-guide/snowflake-cortex/provisioned-throughput.md) or replaces an existing one. |
| [CREATE REPLICATION GROUP](sql/create-replication-group.md) | Creates a new [replication group](../user-guide/account-replication-intro.md) of specified objects in the system. |
| [CREATE RESOURCE MONITOR](sql/create-resource-monitor.md) | Creates a new [resource monitor](../user-guide/resource-monitors.md). |
| [CREATE ROLE](sql/create-role.md) | Create a new role or replace an existing role in the system. |
| [CREATE ROW ACCESS POLICY](sql/create-row-access-policy.md) | Creates a new row access policy in the current/specified schema or replaces an existing row access policy. |
| [CREATE SCHEMA](sql/create-schema.md) | Creates a new schema in the current database. |
| [CREATE SECRET](sql/create-secret.md) | Creates a new secret in the current or specified schema or replaces an existing secret. |
| [CREATE SECURITY INTEGRATION](sql/create-security-integration.md) | Creates a new security integration in the account or replaces an existing integration. |
| [CREATE SECURITY INTEGRATION (External API Authentication)](sql/create-security-integration-api-auth.md) | Creates a new security integration for external API Authentication in the account or replaces an existing integration. |
| [CREATE SECURITY INTEGRATION (AWS IAM Authentication)](sql/create-security-integration-aws-iam.md) | Creates a new security integration for external authentication using Amazon Web Services (AWS) Identity and Access Management (IAM). |
| [CREATE SECURITY INTEGRATION (External OAuth)](sql/create-security-integration-oauth-external.md) | Creates a new External OAuth security integration in the account or replaces an existing integration. |
| [CREATE SECURITY INTEGRATION (Snowflake OAuth)](sql/create-security-integration-oauth-snowflake.md) | Creates a new Snowflake OAuth security integration in the account or replaces an existing integration. |
| [CREATE SECURITY INTEGRATION (SAML2)](sql/create-security-integration-saml2.md) | Creates a new SAML2 security integration in the account or replaces an existing integration. |
| [CREATE SECURITY INTEGRATION (SCIM)](sql/create-security-integration-scim.md) | Creates a new SCIM security integration in the account or replaces an existing integration. |
| [CREATE SEMANTIC VIEW](sql/create-semantic-view.md) | Creates a new [semantic view](../user-guide/views-semantic/overview.md) in the current/specified schema. |
| [CREATE SEQUENCE](sql/create-sequence.md) | Creates a new sequence, which can be used for generating sequential, unique numbers. |
| [CREATE SERVICE](sql/create-service.md) | Creates a new [Snowpark Container Services service](../developer-guide/snowpark-container-services/working-with-services.md) in the current schema. |
| [CREATE SESSION POLICY](sql/create-session-policy.md) | Creates a new session policy or replaces an existing session policy. |
| [CREATE SHARE](sql/create-share.md) | Creates a new, empty [share](../user-guide/data-sharing-intro.md). |
| [CREATE SNAPSHOT](sql/create-snapshot.md) | Creates or replaces a [snapshot of a block storage volume](../developer-guide/snowpark-container-services/block-storage-volume.md) for a specified volume and service instance. |
| [CREATE SNAPSHOT POLICY — Deprecated](sql/create-snapshot-policy.md) | Creates a [snapshot](../user-guide/backups.md) policy. |
| [CREATE SNAPSHOT SET — Deprecated](sql/create-snapshot-set.md) | Creates a [snapshot](../user-guide/backups.md) set for a table, a schema, or a database. |
| [CREATE STAGE](sql/create-stage.md) | Creates a new named *internal* or *external* stage to use for loading data from files into Snowflake tables and unloading data from tables into files. |
| [CREATE STORAGE INTEGRATION](sql/create-storage-integration.md) | Creates a new storage integration in the account or replaces an existing integration. |
| [CREATE STORAGE LIFECYCLE POLICY](sql/create-storage-lifecycle-policy.md) | Creates a new [storage lifecycle policy](../user-guide/storage-management/storage-lifecycle-policies.md) in the current or specified schema, or replaces an existing policy. |
| [CREATE STREAM](sql/create-stream.md) | Creates a new stream in the current/specified schema or replaces an existing [stream](../user-guide/streams-intro.md). |
| [CREATE STREAMLIT](sql/create-streamlit.md) | Creates a new Streamlit object in Snowflake or replaces an existing Streamlit object in the same schema. |
| [CREATE TABLE](sql/create-table.md) | Creates a new table in the current/specified schema, replaces an existing table, or alters an existing table. |
| [CREATE | ALTER TABLE … CONSTRAINT](sql/create-table-constraint.md) | This topic describes how to create constraints by specifying a CONSTRAINT clause in a [CREATE TABLE](sql/create-table.md), [CREATE HYBRID TABLE](sql/create-hybrid-table.md), or [ALTER TABLE](sql/alter-table.md) statement. |
| [CREATE TAG](sql/create-tag.md) | Creates a new tag or replaces an existing tag in the system. |
| [CREATE TASK](sql/create-task.md) | Creates a new [task](../user-guide/tasks-intro.md) in the current/specified schema or replaces an existing task. |
| [CREATE USER](sql/create-user.md) | Creates a new user or replaces an existing user in the system. |
| [CREATE OR ALTER VERSIONED SCHEMA](sql/create-versioned-schema.md) | Creates a new versioned schema or modifies an existing versioned schema. |
| [CREATE VIEW](sql/create-view.md) | Creates a new view in the current/specified schema, based on a query of one or more existing tables (or any other valid query expression). |
| [CREATE WAREHOUSE](sql/create-warehouse.md) | Creates a new [virtual warehouse](../user-guide/warehouses-overview.md) in the system. |
| **D** |  |
| [DELETE](sql/delete.md) | Remove rows from a table. |
| [DESCRIBE <object>](sql/desc.md) | Describes the details for the specified object. |
| [DESCRIBE AGENT](sql/desc-agent.md) | Describes the properties of a [Cortex Agent](../user-guide/snowflake-cortex/cortex-agents.md). |
| [DESCRIBE AGGREGATION POLICY](sql/desc-aggregation-policy.md) | Describes the details about an [aggregation policy](../user-guide/aggregation-policies.md), including the creation date, name, and the SQL expression. |
| [DESCRIBE ALERT](sql/desc-alert.md) | Describes the properties of an [alert](../user-guide/alerts.md). |
| [DESCRIBE APPLICATION](sql/desc-application.md) | Displays information about a Snowflake Native App. |
| [DESCRIBE APPLICATION PACKAGE](sql/desc-application-package.md) | Displays information about an application package. |
| [DESCRIBE AUTHENTICATION POLICY](sql/desc-authentication-policy.md) | Describes the properties of an [authentication policy](../user-guide/authentication-policies.md). |
| [DESCRIBE AVAILABLE LISTING](sql/desc-available-listing.md) | Describes the columns in the listings that are available to the user who runs the command. |
| [DESCRIBE AVAILABLE ORGANIZATION PROFILE](sql/desc-available-organization-profile.md) | Describes the active organization profile that can be associated with organizational listings. |
| [DESCRIBE BACKUP POLICY](sql/desc-backup-policy.md) | Describes a specific [backup policy](../user-guide/backups.md). |
| [DESCRIBE BACKUP SET](sql/desc-backup-set.md) | Describes a specific [backup set](../user-guide/backups.md). |
| [DESCRIBE CATALOG INTEGRATION](sql/desc-catalog-integration.md) | Describes the properties of a [catalog integration](../user-guide/tables-iceberg.md). |
| [DESCRIBE COMPUTE POOL](sql/desc-compute-pool.md) | Describes the properties of a [compute pool](../developer-guide/snowpark-container-services/working-with-compute-pool.md). |
| [DESCRIBE CONFIGURATION](sql/desc-configuration.md) | Describes the properties of a [configuration](../developer-guide/native-apps/inter-app-communication.md). |
| [DESCRIBE CORTEX SEARCH SERVICE](sql/desc-cortex-search.md) | Describes the properties of a [Cortex Search service](../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md). |
| [DESCRIBE DATABASE](sql/desc-database.md) | Describes the database. |
| [DESCRIBE DBT PROJECT](sql/desc-dbt-project.md) | Describes the properties of a [dbt project object](../user-guide/data-engineering/dbt-projects-on-snowflake.md). |
| [DESCRIBE DYNAMIC TABLE](sql/desc-dynamic-table.md) | Describes the columns in a [dynamic table](../user-guide/dynamic-tables-about.md). |
| [DESCRIBE EVENT TABLE](sql/desc-event-table.md) | Describes the columns in an [event table](../developer-guide/logging-tracing/event-table-setting-up.md). |
| [DESCRIBE EXTERNAL TABLE](sql/desc-external-table.md) | Describes the VALUE column and virtual columns in an external table. |
| [DESCRIBE EXTERNAL VOLUME](sql/desc-external-volume.md) | Describes the properties of an [external volume](../user-guide/tables-iceberg.md). |
| [DESCRIBE FEATURE POLICY](sql/desc-feature-policy.md) | Describes the properties of a [feature policy](../developer-guide/native-apps/ui-consumer-feature-policies.md). |
| [DESCRIBE FILE FORMAT](sql/desc-file-format.md) | Describes the property type (for example, `String` or `Integer`), the defined value of the property, and the default value for each property in a file format object definition. |
| [DESCRIBE FUNCTION](sql/desc-function.md) | Describes the specified user-defined function (UDF) or external function, including the signature (i.e. arguments), return value, language, and body (i.e. definition). |
| [DESCRIBE FUNCTION (DMF)](sql/desc-function-dmf.md) | Describes the specified data metric function (DMF), including the signature (arguments), return value, language, and body (definition). |
| [DESCRIBE FUNCTION (Snowpark Container Services)](sql/desc-function-spcs.md) | Describes the specified [service function](../developer-guide/snowpark-container-services/working-with-services.md), including the signature (arguments), return value, language, and body (path to the Snowpark Container Services service). |
| [DESCRIBE GATEWAY](sql/desc-gateway.md) | Describes the properties of a [gateway](../developer-guide/snowpark-container-services/gateway.md). |
| [DESCRIBE GIT REPOSITORY](sql/desc-git-repository.md) | Describes an existing Snowflake [Git repository clone](../developer-guide/git/git-overview.md). |
| [DESCRIBE ICEBERG TABLE](sql/desc-iceberg-table.md) | Describes either the columns in an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) or the current values, as well as the default values, for the properties of an Iceberg table. |
| [DESCRIBE INTEGRATION](sql/desc-integration.md) | Describes the properties of an integration. |
| [DESCRIBE JOIN POLICY](sql/desc-join-policy.md) | Describes the details about a [join policy](../user-guide/join-policies.md), including the creation date, name, and the SQL expression. |
| [DESCRIBE LISTING](sql/desc-listing.md) | Describes the columns in a [listing](../collaboration/collaboration-listings-about.md). |
| [DESCRIBE MAINTENANCE POLICY](sql/desc-maintenance-policy.md) | Shows the details of a [maintenance policy](../developer-guide/native-apps/consumer-maintenance-policies.md). |
| [DESCRIBE MASKING POLICY](sql/desc-masking-policy.md) | Describes the details about a masking policy, including the creation date, name, data type, and SQL expression. |
| [DESCRIBE MATERIALIZED VIEW](sql/desc-materialized-view.md) | Describes the columns in a materialized view. |
| [DESCRIBE MCP SERVER](sql/desc-mcp-server.md) | Describes the properties of an MCP (Model Context Protocol) server. |
| [DESCRIBE MODEL MONITOR](sql/desc-model-monitor.md) | Displays information about a specific [model monitor](../developer-guide/snowflake-ml/model-registry/model-observability.md). |
| [DESCRIBE NETWORK POLICY](sql/desc-network-policy.md) | Describes the properties specified for a network policy. |
| [DESCRIBE NETWORK RULE](sql/desc-network-rule.md) | Describes the properties specified for a network rule. |
| [DESCRIBE NOTEBOOK](sql/desc-notebook.md) | Describes the properties of a [notebook](../user-guide/ui-snowsight/notebooks.md). |
| [DESCRIBE NOTIFICATION INTEGRATION](sql/desc-notification-integration.md) | Describes the properties of a notification integration. |
| [DESCRIBE OPENFLOW DATA PLANE INTEGRATION](sql/desc-oflow-data-plane-integration.md) | Describes the columns in an Openflow data plane integration. |
| [DESCRIBE ONLINE FEATURE TABLE](sql/desc-online-feature-table.md) | Describes the columns in an [online feature table](sql/create-online-feature-table.md). |
| [DESCRIBE ORGANIZATION PROFILE](sql/desc-organization-profile.md) | Describes the properties of an organization profile. |
| [DESCRIBE PACKAGES POLICY](sql/desc-packages-policy.md) | Describes the details about a packages policy. |
| [DESCRIBE PASSWORD POLICY](sql/desc-password-policy.md) | Describes the details about a password policy. |
| [DESCRIBE PIPE](sql/desc-pipe.md) | Describes the properties specified for a pipe, as well as the default values of the properties. |
| [DESCRIBE POSTGRES INSTANCE](sql/desc-postgres-instance.md) | Describes the properties of a [Snowflake Postgres instance](../user-guide/snowflake-postgres/about.md). |
| [DESCRIBE PRIVACY POLICY](sql/desc-privacy-policy.md) | Describes the properties of a [privacy policy](../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md). |
| [DESCRIBE PROCEDURE](sql/desc-procedure.md) | Describes the specified stored procedure, including the stored procedure’s signature (i.e. arguments), return value, language, and body (i.e. definition). |
| [DESCRIBE PROJECTION POLICY](sql/desc-projection-policy.md) | Describes the details about a [projection policy](../user-guide/projection-policies.md), including the creation date, name, and the SQL expression. |
| [DESCRIBE RESULT](sql/desc-result.md) | Describes the columns in the result of a query. |
| [DESCRIBE ROW ACCESS POLICY](sql/desc-row-access-policy.md) | Describes a row access policy, including the creation date, name, data type, and SQL expression. |
| [DESCRIBE SCHEMA](sql/desc-schema.md) | Describes the schema. |
| [DESCRIBE SEARCH OPTIMIZATION](sql/desc-search-optimization.md) | Describes the [search optimization configuration](../user-guide/search-optimization/enabling.md) for a specified table and its columns. |
| [DESCRIBE SECRET](sql/desc-secret.md) | Describes the properties of a secret. |
| [DESCRIBE SEMANTIC VIEW](sql/desc-semantic-view.md) | Describes the properties of the logical tables, dimensions, facts, and metrics that make up a [semantic view](../user-guide/views-semantic/overview.md). |
| [DESCRIBE SEQUENCE](sql/desc-sequence.md) | Describes a sequence, including the sequence’s interval. |
| [DESCRIBE SERVICE](sql/desc-service.md) | Describes the properties of a [Snowpark Container Services service](../developer-guide/snowpark-container-services/working-with-services.md) (including job services). |
| [DESCRIBE SESSION POLICY](sql/desc-session-policy.md) | Describes the details about a session policy. |
| [DESCRIBE SHARE](sql/desc-share.md) | Describes the data objects that are included in a [share](../user-guide/data-sharing-intro.md). |
| [DESCRIBE SNAPSHOT](sql/desc-snapshot.md) | Describes the properties of a [snapshot of a block storage volume](../developer-guide/snowpark-container-services/block-storage-volume.md). |
| [DESCRIBE SNAPSHOT POLICY](sql/desc-snapshot-policy.md) | Describes a specific [snapshot policy](../user-guide/backups.md). |
| [DESCRIBE SNAPSHOT SET](sql/desc-snapshot-set.md) | Describes a specific [snapshot set](../user-guide/backups.md). |
| [DESCRIBE SPECIFICATION](sql/desc-specification.md) | Describes the details about an [app specification](../developer-guide/native-apps/requesting-app-specs.md). |
| [DESCRIBE STAGE](sql/desc-stage.md) | Describes the values specified for the properties in a stage (file format, copy, and location), as well as the default values for each property. |
| [DESCRIBE STORAGE LIFECYCLE POLICY](sql/desc-storage-lifecycle-policy.md) | Describes the properties of a [storage lifecycle policy](../user-guide/storage-management/storage-lifecycle-policies.md). |
| [DESCRIBE STREAM](sql/desc-stream.md) | Describes the properties specified for a stream. |
| [DESCRIBE STREAMLIT](sql/desc-streamlit.md) | Describes the columns in a Streamlit object. |
| [DESCRIBE TABLE](sql/desc-table.md) | Describes either the columns in a table or the set of stage properties for the table (current values and default values). |
| [DESCRIBE TASK](sql/desc-task.md) | Shows information about a task. |
| [DESCRIBE TRANSACTION](sql/desc-transaction.md) | Describes the [transaction](transactions.md), including the start time and the state (running, committed, rolled back). |
| [DESCRIBE USER](sql/desc-user.md) | Describes a [user](../user-guide/admin-user-management.md), including the current and default values of the properties of the user. |
| [DESCRIBE VIEW](sql/desc-view.md) | Describes the columns in a view (or table). |
| [DESCRIBE WAREHOUSE](sql/desc-warehouse.md) | Describes a [virtual warehouse](../user-guide/warehouses-overview.md). |
| [DROP <object>](sql/drop.md) | Removes the specified object from the system. |
| [DROP ACCOUNT](sql/drop-account.md) | Drops an account, which initiates the process of [deleting the account](../user-guide/organizations-manage-accounts-delete.md). |
| [DROP AGENT](sql/drop-agent.md) | Removes the specified [Cortex Agent](../user-guide/snowflake-cortex/cortex-agents.md) with the specified name from the current or specified database and schema. |
| [DROP AGGREGATION POLICY](sql/drop-aggregation-policy.md) | Removes an [aggregation policy](../user-guide/aggregation-policies.md) from the current/specified schema. |
| [DROP ALERT](sql/drop-alert.md) | Drops an existing [alert](../user-guide/alerts.md). |
| [DROP APPLICATION](sql/drop-application.md) | Removes an application from the system in the Native Apps Framework. |
| [DROP APPLICATION PACKAGE](sql/drop-application-package.md) | Removes an application package from the system in the Native Apps Framework. |
| [DROP APPLICATION ROLE](sql/drop-application-role.md) | Removes the specified application role from the system. |
| [DROP AUTHENTICATION POLICY](sql/drop-authentication-policy.md) | Removes an [authentication policy](../user-guide/authentication-policies.md) from the system. |
| [DROP BACKUP POLICY](sql/drop-backup-policy.md) | Deletes a [backup](../user-guide/backups.md) policy. |
| [DROP BACKUP SET](sql/drop-backup-set.md) | Deletes a [backup](../user-guide/backups.md) set. |
| [DROP CATALOG INTEGRATION](sql/drop-catalog-integration.md) | Removes a [catalog integration](../user-guide/tables-iceberg.md) from the account. |
| [DROP COMPUTE POOL](sql/drop-compute-pool.md) | Removes the specified [compute pool](../developer-guide/snowpark-container-services/working-with-compute-pool.md) from the account. |
| [DROP CONNECTION](sql/drop-connection.md) | Removes a connection from the account. |
| [DROP CONTACT](sql/drop-contact.md) | Removes the specified [contact](../user-guide/contacts-using.md) from the current schema. |
| [DROP CORTEX SEARCH SERVICE](sql/drop-cortex-search.md) | Removes the specified [Cortex Search service](../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md) from the current schema. |
| [DROP DATABASE](sql/drop-database.md) | Removes a database from the system. |
| [DROP DATABASE ROLE](sql/drop-database-role.md) | Removes the specified database role from the system. |
| [DROP DBT PROJECT](sql/drop-dbt-project.md) | Removes the specified [dbt project object](../user-guide/data-engineering/dbt-projects-on-snowflake.md) from the current or specified schema. |
| [DROP DYNAMIC TABLE](sql/drop-dynamic-table.md) | Removes a [dynamic table](../user-guide/dynamic-tables-about.md) from the current/specified schema. |
| [DROP EXPERIMENT](sql/drop-experiment.md) | Removes the specified [experiment](../developer-guide/snowflake-ml/experiments.md) from the current/specified schema. |
| [DROP EXTERNAL TABLE](sql/drop-external-table.md) | Removes an external table from the current or specified schema. |
| [DROP EXTERNAL VOLUME](sql/drop-external-volume.md) | Removes an [external volume](../user-guide/tables-iceberg.md) from the account, but retains a version of the external volume so that it can be recovered using [UNDROP EXTERNAL VOLUME](sql/undrop-external-volume.md). |
| [DROP FAILOVER GROUP](sql/drop-failover-group.md) | Removes a [failover group](../user-guide/account-replication-intro.md) from the account. |
| [DROP FEATURE POLICY](sql/drop-feature-policy.md) | Removes the specified [feature policy](../developer-guide/native-apps/ui-consumer-feature-policies.md). |
| [DROP FILE FORMAT](sql/drop-file-format.md) | Removes the specified file format from the current/specified schema. |
| [DROP FUNCTION](sql/drop-function.md) | Removes the specified user-defined function (UDF) or external function from the current/specified schema. |
| [DROP FUNCTION (DMF)](sql/drop-function-dmf.md) | Removes the specified data metric function (DMF) from the current or specified schema. |
| [DROP FUNCTION (Snowpark Container Services)](sql/drop-function-spcs.md) | Removes the specified [service function](../developer-guide/snowpark-container-services/working-with-services.md). |
| [DROP GATEWAY](sql/drop-gateway.md) | Removes the specified [gateway](../developer-guide/snowpark-container-services/gateway.md) from the current or specified schema. |
| [DROP GIT REPOSITORY](sql/drop-git-repository.md) | Removes the specified Snowflake Git repository clone from the current/specified schema. |
| [DROP ICEBERG TABLE](sql/drop-iceberg-table.md) | Removes an [Apache Iceberg™ table](../user-guide/tables-iceberg.md) from the current/specified schema, but retains a version of the Iceberg table so that it can be recovered using [UNDROP ICEBERG TABLE](sql/undrop-iceberg-table.md). |
| [DROP IMAGE REPOSITORY](sql/drop-image-repository.md) | Removes the specified [image repository](../developer-guide/snowpark-container-services/tutorials/tutorial-1.md) from the current or specified schema. |
| [DROP INDEX](sql/drop-index.md) | Drops a secondary index. |
| [DROP INTEGRATION](sql/drop-integration.md) | Removes an integration from the account. |
| [DROP JOIN POLICY](sql/drop-join-policy.md) | Removes a [join policy](../user-guide/join-policies.md) from the current/specified schema. |
| [DROP LISTING](sql/drop-listing.md) | Removes the specified [listing](../collaboration/collaboration-listings-about.md) from the system and immediately revokes access for all consumers. |
| [DROP MAINTENANCE POLICY](sql/drop-maintenance-policy.md) | Removes a [maintenance policy](../developer-guide/native-apps/consumer-maintenance-policies.md) from the current or specified schema. |
| [DROP MANAGED ACCOUNT](sql/drop-managed-account.md) | Removes a managed account, including all objects created in the account, and immediately restricts access to the account. |
| [DROP MASKING POLICY](sql/drop-masking-policy.md) | Removes a masking policy from the system. |
| [DROP MATERIALIZED VIEW](sql/drop-materialized-view.md) | Removes the specified materialized view from the current/specified schema. |
| [DROP MCP SERVER](sql/drop-mcp-server.md) | Removes the specified MCP (Model Context Protocol) server from the current/specified schema. |
| [DROP MODEL](sql/drop-model.md) | Removes a machine learning model from the current/specified schema. |
| [DROP MODEL MONITOR](sql/drop-model-monitor.md) | Removes the specified [model monitor](../developer-guide/snowflake-ml/model-registry/model-observability.md) from the current or specified schema. |
| [DROP NETWORK POLICY](sql/drop-network-policy.md) | Removes the specified network policy from the system. |
| [DROP NETWORK RULE](sql/drop-network-rule.md) | Removes the specified network rule from the system. |
| [DROP NOTEBOOK](sql/drop-notebook.md) | Removes the specified [notebook](../user-guide/ui-snowsight/notebooks.md) from the current/specified schema, but retains a version of the notebook so that it can be recovered using [UNDROP NOTEBOOK](sql/undrop-notebook.md). |
| [DROP ONLINE FEATURE TABLE](sql/drop-online-feature-table.md) | Removes the specified [online feature table](sql/create-online-feature-table.md) from the current/specified schema. |
| [DROP ORGANIZATION PROFILE](sql/drop-organization-profile.md) | Removes an organization profile. |
| [DROP ORGANIZATION USER](sql/drop-organization-user.md) | Removes an [organization user](../user-guide/organization-users.md) from the organization. |
| [DROP ORGANIZATION USER GROUP](sql/drop-organization-user-group.md) | Removes an [organization user group](../user-guide/organization-users.md) from the organization. |
| [DROP PACKAGES POLICY](sql/drop-packages-policy.md) | Removes a packages policy from the system. |
| [DROP PASSWORD POLICY](sql/drop-password-policy.md) | Removes a password policy from the system. |
| [DROP PIPE](sql/drop-pipe.md) | Removes the specified pipe from the current/specified schema. |
| [DROP POSTGRES INSTANCE](sql/drop-postgres-instance.md) | Removes the specified [Snowflake Postgres instance](../user-guide/snowflake-postgres/about.md) from the account. |
| [DROP PRIVACY POLICY](sql/drop-privacy-policy.md) | Removes the specified [privacy policy](../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) from the current/specified schema. |
| [DROP PROCEDURE](sql/drop-procedure.md) | Removes the specified stored procedure from the current/specified schema. |
| [DROP PROJECTION POLICY](sql/drop-projection-policy.md) | Removes a [projection policy](../user-guide/projection-policies.md) from the current/specified schema. |
| [DROP REPLICATION GROUP](sql/drop-replication-group.md) | Removes a [replication group](../user-guide/account-replication-intro.md) from the account. |
| [DROP RESOURCE MONITOR](sql/drop-resource-monitor.md) | Removes the specified [resource monitor](../user-guide/resource-monitors.md) from the system. |
| [DROP ROLE](sql/drop-role.md) | Removes the specified role from the system. |
| [DROP ROW ACCESS POLICY](sql/drop-row-access-policy.md) | Removes a row access policy from the system. |
| [DROP SCHEMA](sql/drop-schema.md) | Removes a schema from the current/specified database. |
| [DROP SECRET](sql/drop-secret.md) | Removes a secret from the system. |
| [DROP SEMANTIC VIEW](sql/drop-semantic-view.md) | Removes the specified [semantic view](../user-guide/views-semantic/overview.md) from the current/specified schema. |
| [DROP SEQUENCE](sql/drop-sequence.md) | Removes a sequence from the current/specified schema. |
| [DROP SERVICE](sql/drop-service.md) | Removes the specified [Snowpark Container Services service](../developer-guide/snowpark-container-services/working-with-services.md) from the current or specified schema. |
| [DROP SESSION POLICY](sql/drop-session-policy.md) | Removes a session policy from the system. |
| [DROP SHARE](sql/drop-share.md) | Removes the specified [share](../user-guide/data-sharing-intro.md) from the system and immediately revokes access for all consumers (i.e. accounts who have created a database from the share). |
| [DROP SNAPSHOT](sql/drop-snapshot.md) | Removes a [snapshot of a block storage volume](../developer-guide/snowpark-container-services/block-storage-volume.md). |
| [DROP SNAPSHOT POLICY — Deprecated](sql/drop-snapshot-policy.md) | Deletes a [snapshot](../user-guide/backups.md) policy. |
| [DROP SNAPSHOT SET — Deprecated](sql/drop-snapshot-set.md) | Deletes a [snapshot](../user-guide/backups.md) set. |
| [DROP STAGE](sql/drop-stage.md) | Removes the specified named internal or external stage from the current/specified schema. |
| [DROP STORAGE LIFECYCLE POLICY](sql/drop-storage-lifecycle-policy.md) | Removes the specified [storage lifecycle policy](../user-guide/storage-management/storage-lifecycle-policies.md) from the current or specified schema. |
| [DROP STREAM](sql/drop-stream.md) | Removes a stream from the current/specified schema. |
| [DROP STREAMLIT](sql/drop-streamlit.md) | Removes the specified Streamlit object from the current/specified schema. |
| [DROP TABLE](sql/drop-table.md) | Removes a table from the current or specified schema, but retains a version of the table so that it can be recovered by using [UNDROP TABLE](sql/undrop-table.md). |
| [DROP TAG](sql/drop-tag.md) | Removes a tag from the system. |
| [DROP TASK](sql/drop-task.md) | Removes a task from the current/specified schema. |
| [DROP USER](sql/drop-user.md) | Removes the specified user from the system. |
| [DROP VIEW](sql/drop-view.md) | Removes the specified view from the current/specified schema. |
| [DROP WAREHOUSE](sql/drop-warehouse.md) | Removes the specified [virtual warehouse](../user-guide/warehouses-overview.md) from the system. |
| **E** |  |
| [EXECUTE ALERT](sql/execute-alert.md) | Manually executes an [alert](../user-guide/alerts.md) independent of the schedule for the alert. |
| [EXECUTE DBT PROJECT](sql/execute-dbt-project.md) | Executes the specified [dbt project object](../user-guide/data-engineering/dbt-projects-on-snowflake.md) or the dbt project in a Snowflake workspace using the dbt command and command-line options specified. |
| [EXECUTE IMMEDIATE](sql/execute-immediate.md) | Executes a string that contains a SQL statement or a [Snowflake Scripting statement](../developer-guide/snowflake-scripting/blocks.md). |
| [EXECUTE IMMEDIATE FROM](sql/execute-immediate-from.md) | EXECUTE IMMEDIATE FROM executes the SQL statements specified in a file in a stage. |
| [EXECUTE JOB SERVICE](sql/execute-job-service.md) | Executes a Snowpark Container Services service as a job. |
| [EXECUTE NOTEBOOK](sql/execute-notebook.md) | Executes the notebook outside the Notebook Editor. |
| [EXECUTE NOTEBOOK PROJECT](sql/execute-notebook-project.md) | Executes a notebook stored in a notebook project (NPO). |
| [EXECUTE TASK](sql/execute-task.md) | Manually triggers an asynchronous single run of a task (either a standalone task or the root task in a [task graph](../user-guide/tasks-graphs.md)) independent of the schedule defined for the task. |
| [EXPLAIN](sql/explain.md) | Returns the logical execution plan for the specified SQL statement. |
| **G** |  |
| [GET](sql/get.md) | Downloads data files from one of the following [internal stage](../user-guide/data-load-overview.md) types to a local directory or folder on a client machine. |
| [GRANT APPLICATION ROLE](sql/grant-application-role.md) | Assigns an application role to an account role, another application role, an application, or a user. |
| [GRANT CALLER](sql/grant-caller.md) | Grants [caller grants](../developer-guide/restricted-callers-rights.md) to a role. |
| [GRANT DATABASE ROLE](sql/grant-database-role.md) | Assigns a database role to an [account role, another database role](../user-guide/security-access-control-overview.md), or a user. |
| [GRANT DATABASE ROLE … TO SHARE](sql/grant-database-role-share.md) | Grants a database role to a share. |
| [GRANT OWNERSHIP](sql/grant-ownership.md) | Transfers ownership of an object or all objects of a specified type in a schema from one role to another role. |
| [GRANT <privileges> … TO ROLE](sql/grant-privilege.md) | Grants one or more access privileges on a securable object to a role or database role. |
| [GRANT <privileges> … TO APPLICATION](sql/grant-privilege-application.md) | Grants one or more access privileges on a securable object to an application. |
| [GRANT <privileges> … TO APPLICATION ROLE](sql/grant-privilege-application-role.md) | Grants one or more access privileges on a securable schema-level object to an application role. |
| [GRANT <privilege> … TO SHARE](sql/grant-privilege-share.md) | Grants access privileges for databases and other supported database objects (schemas, UDFs, tables, and views) to a share. |
| [GRANT <privileges> … TO USER](sql/grant-privilege-user.md) | Grants one or more access privileges on a securable object to a user. |
| [GRANT ROLE](sql/grant-role.md) | Assigns a role to a user or another role. |
| [GRANT SERVICE ROLE](sql/grant-service-role.md) | Assigns a service role to an account role, application role, or database role. |
| **I** |  |
| [INSERT](sql/insert.md) | Updates a table by inserting one or more rows into the table. |
| [INSERT (multi-table)](sql/insert-multi-table.md) | Updates multiple tables by inserting one or more rows with column values (from a query) into the tables. |
| **L** |  |
| [LIST](sql/list.md) | Returns a list of files from one of the following Snowflake storage features. |
| **M** |  |
| [MERGE](sql/merge.md) | Inserts, updates, and deletes values in a table that are based on values in a second table or a subquery. |
| **P** |  |
| [PUT](sql/put.md) | Uploads one or more data files from a local file system onto an [internal stage](../user-guide/data-load-local-file-system-create-stage.md). |
| **R** |  |
| [REMOVE](sql/remove.md) | Removes files from either an external (external cloud storage) or internal (i.e. Snowflake) stage. |
| [REVOKE APPLICATION ROLE](sql/revoke-application-role.md) | Revokes an application role from an account role or another application role. |
| [REVOKE CALLER](sql/revoke-caller.md) | Revokes privileges that were previously granted to an executable owner using a [caller grant](../developer-guide/restricted-callers-rights.md). |
| [REVOKE DATABASE ROLE](sql/revoke-database-role.md) | Revokes a database role from an [account role or another database role](../user-guide/security-access-control-overview.md). |
| [REVOKE DATABASE ROLE … FROM SHARE](sql/revoke-database-role-share.md) | Revokes a database role from a share. |
| [REVOKE <privileges> … FROM ROLE](sql/revoke-privilege.md) | Removes one or more privileges on a securable object from a role or database role. |
| [REVOKE <privileges> … FROM APPLICATION](sql/revoke-privilege-application.md) | Revokes one or more access privileges on a securable object from an application. |
| [REVOKE <privileges> … FROM APPLICATION ROLE](sql/revoke-privilege-application-role.md) | Revokes one or more access privileges on a securable schema-level object from an application role. |
| [REVOKE <privilege> … FROM SHARE](sql/revoke-privilege-share.md) | Revokes access privileges for databases and other supported database objects (schemas, tables, and views) from a share. |
| [REVOKE <privileges> … FROM USER](sql/revoke-privilege-user.md) | Removes one or more privileges on a securable object from a user. |
| [REVOKE ROLE](sql/revoke-role.md) | Removes a role from another role or a user. |
| [REVOKE SERVICE ROLE](sql/revoke-service-role.md) | Revokes a service role from an account role, application role, or database role. |
| [ROLLBACK](sql/rollback.md) | Rolls back an open transaction in the current session. |
| **S** |  |
| [SELECT](sql/select.md) | SELECT can be used as either a statement or as a clause within other statements. |
| [SET](sql/set.md) | Initializes the value of a [session variable](session-variables.md) to the result of a SQL expression. |
| [SHOW <objects>](sql/show.md) | Lists the existing objects for the specified object type. |
| [SHOW ACCOUNTS](sql/show-accounts.md) | Lists all the accounts in your organization, excluding [managed accounts](../user-guide/data-sharing-reader-create.md). |
| [SHOW AGENTS](sql/show-agents.md) | Lists the [Cortex Agents](../user-guide/snowflake-cortex/cortex-agents.md) for which you have access privileges. |
| [SHOW AGGREGATION POLICIES](sql/show-aggregation-policies.md) | Lists information about existing [aggregation policies](../user-guide/aggregation-policies.md), including the creation date, database and schema names, owner, and any available comments. |
| [SHOW ALERTS](sql/show-alerts.md) | Lists the [alerts](../user-guide/alerts.md) for which you have access privileges. |
| [SHOW APPLICATION PACKAGES](sql/show-application-packages.md) | Lists the application packages for which you have access privileges across your entire account in the Native Apps Framework. |
| [SHOW APPLICATION ROLES](sql/show-application-roles.md) | Lists the application roles in the specified app for which you have access privileges. |
| [SHOW APPLICATIONS](sql/show-applications.md) | Lists the Snowflake Native Apps that you have access privileges for across your entire account. |
| [SHOW AUTHENTICATION POLICIES](sql/show-authentication-policies.md) | Lists [authentication policy](../user-guide/authentication-policies.md) information, including the creation date, database and schema names, owner, and any available comments. |
| [SHOW AVAILABLE LISTINGS](sql/show-available-listings.md) | Lists the listings that are available to the user who runs the command. |
| [SHOW AVAILABLE OFFERS](sql/show-available-offers.md) | Lists the [offers](../user-guide/collaboration/listings/pricing-plans-offers/pricing-plans-and-offers.md) that are available to the user who runs the command. |
| [SHOW AVAILABLE ORGANIZATION PROFILES](sql/show-available-organization-profiles.md) | Lists the organization profiles available in the user’s organization. |
| [SHOW BACKUP POLICIES](sql/show-backup-policies.md) | Lists all the [backup](../user-guide/backups.md) policies in your account for which you have access privileges. |
| [SHOW BACKUP SETS](sql/show-backup-sets.md) | Lists all the [backup](../user-guide/backups.md) sets for which you have access privileges. |
| [SHOW BACKUPS IN BACKUP SET](sql/show-backups-in-backup-set.md) | Lists all the [backups](../user-guide/backups.md) in a backup set. |
| [SHOW CALLER GRANTS](sql/show-caller-grants.md) | Lists the [caller grants](../developer-guide/restricted-callers-rights.md) being used to implement restricted caller’s rights. |
| [SHOW CATALOG INTEGRATIONS](sql/show-catalog-integrations.md) | Lists the [catalog integrations](../user-guide/tables-iceberg.md) in your account. |
| [SHOW CHANNELS](sql/show-channels.md) | Lists the [Snowpipe Streaming channels](../user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview.md) for which you have access privileges. |
| [SHOW CLASSES](sql/show-classes.md) | Lists all available classes. |
| [SHOW COLUMNS](sql/show-columns.md) | Lists the columns in the tables or views and the dimensions, facts, and metrics in the [semantic views](../user-guide/views-semantic/overview.md) for which you have access privileges. |
| [SHOW COMPUTE POOL INSTANCE FAMILIES](sql/show-compute-pool-instance-families.md) | Lists the available [compute pool instance families](../developer-guide/snowpark-container-services/working-with-compute-pool.md) that you can use to create a compute pool. |
| [SHOW COMPUTE POOLS](sql/show-compute-pools.md) | Lists the [compute pools](../developer-guide/snowpark-container-services/working-with-compute-pool.md) in your account for which you have access privileges. |
| [SHOW CONFIGURATIONS](sql/show-configurations.md) | Lists the [configurations](../developer-guide/native-apps/inter-app-communication.md) in the specified app for which you have access privileges. |
| [SHOW CONNECTIONS](sql/show-connections.md) | Lists the [connections](../user-guide/client-redirect.md) for which you have access privileges. |
| [SHOW CONTACTS](sql/show-contacts.md) | Lists the [contacts](../user-guide/contacts-using.md) for which you have access privileges. |
| [SHOW CORTEX SEARCH SERVICES](sql/show-cortex-search.md) | Lists the [Cortex Search services](../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md) for which you have access privileges. |
| [SHOW DATA METRIC FUNCTIONS](sql/show-data-metric-functions.md) | Lists the [data metric functions](../user-guide/data-quality-intro.md) (DMFs) for which you have access privileges. |
| [SHOW DATABASE ROLES](sql/show-database-roles.md) | Lists all the database roles in the specified database. |
| [SHOW DATABASES](sql/show-databases.md) | Lists the databases for which you have access privileges across your entire account, including dropped databases that are still within the Time Travel retention period and, therefore, can be undropped. |
| [SHOW DATABASES IN FAILOVER GROUP](sql/show-databases-in-failover-group.md) | Lists databases in a [failover group](../user-guide/account-replication-intro.md). |
| [SHOW DATABASES IN REPLICATION GROUP](sql/show-databases-in-replication-group.md) | Lists databases in a [replication group](../user-guide/account-replication-intro.md). |
| [SHOW DATASETS](sql/show-datasets.md) | Displays information about the datasets in your account. |
| [SHOW DBT PROJECTS](sql/show-dbt-projects.md) | Lists the [dbt project objects](../user-guide/data-engineering/dbt-projects-on-snowflake.md) for which you have access privileges. |
| [SHOW DELEGATED AUTHORIZATIONS](sql/show-delegated-authorizations.md) | Lists the active delegated authorizations for which you have access privileges. |
| [SHOW DYNAMIC TABLES](sql/show-dynamic-tables.md) | Lists the [dynamic tables](../user-guide/dynamic-tables-about.md) for which you have access privileges. |
| [SHOW ENDPOINTS](sql/show-endpoints.md) | Lists the endpoints in a [Snowpark Container Services service](../developer-guide/snowpark-container-services/working-with-services.md) (or a job service). |
| [SHOW EVENT TABLES](sql/show-event-tables.md) | Lists the [event tables](../developer-guide/logging-tracing/event-table-setting-up.md) for which you have access privileges, including dropped tables that are still within the Time Travel retention period and, therefore, can be undropped. |
| [SHOW EXPERIMENTS](sql/show-experiments.md) | Lists the [experiments](../developer-guide/snowflake-ml/experiments.md) for which you have access privileges. |
| [SHOW EXTERNAL FUNCTIONS](sql/show-external-functions.md) | Lists all the external functions created for your account. |
| [SHOW EXTERNAL TABLES](sql/show-external-tables.md) | Lists the external tables for which you have access privileges. |
| [SHOW EXTERNAL VOLUMES](sql/show-external-volumes.md) | Lists the [external volumes](../user-guide/tables-iceberg.md) in your account for which you have access privileges. |
| [SHOW FAILOVER GROUPS](sql/show-failover-groups.md) | Lists the primary and secondary [failover groups](../user-guide/account-replication-intro.md) in your account, as well as the failover groups in other accounts that are associated with your account. |
| [SHOW FEATURE POLICIES](sql/show-feature-policies.md) | Lists the [feature policies](../developer-guide/native-apps/ui-consumer-feature-policies.md) for which you have access privileges. |
| [SHOW FILE FORMATS](sql/show-file-formats.md) | Lists the file formats for which you have access privileges. |
| [SHOW FUNCTIONS](sql/show-functions.md) | Lists all functions that you have privileges to access, including built-in, user-defined, and external functions. |
| [SHOW FUNCTIONS IN MODEL](sql/show-functions-in-model.md) | Lists functions defined in machine learning models. |
| [SHOW GATEWAYS](sql/show-gateways.md) | Lists the [gateway](../developer-guide/snowpark-container-services/gateway.md) for which you have access privileges. |
| [SHOW GIT BRANCHES](sql/show-git-branches.md) | Lists the branches in the specified Snowflake Git repository clone. |
| [SHOW GIT REPOSITORIES](sql/show-git-repositories.md) | Lists the [Git repository clones](../developer-guide/git/git-overview.md) that you have privileges to access. |
| [SHOW GIT TAGS](sql/show-git-tags.md) | Lists the tags in the specified Snowflake [Git repository clone](../developer-guide/git/git-overview.md). |
| [SHOW GLOBAL ACCOUNTS](sql/show-global-accounts.md) | Lists all the accounts in your organization that are enabled for replication and indicates the Snowflake Region in which each account is located. |
| [SHOW GRANTS](sql/show-grants.md) | Lists all access control privileges that have been explicitly granted to roles, users, and shares. |
| [SHOW HYBRID TABLES](sql/show-hybrid-tables.md) | Lists the [hybrid tables](../user-guide/tables-hybrid.md) for which you have access privileges. |
| [SHOW ICEBERG TABLES](sql/show-iceberg-tables.md) | Lists the [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) for which you have access privileges. |
| [SHOW IMAGE REPOSITORIES](sql/show-image-repositories.md) | Lists the [image repositories](../developer-guide/snowpark-container-services/tutorials/tutorial-1.md) for which you have access privileges. |
| [SHOW IMAGES IN IMAGE REPOSITORY](sql/show-images-in-image-repository.md) | Lists the images in an [image repository](../developer-guide/snowpark-container-services/working-with-registry-repository.md). |
| [SHOW INDEXES](sql/show-indexes.md) | Lists all the indexes in your account for which you have access privileges. |
| [SHOW INTEGRATIONS](sql/show-integrations.md) | Lists the integrations in your account. |
| [SHOW JOIN POLICIES](sql/show-join-policies.md) | Lists information about existing [join policies](../user-guide/join-policies.md), including the creation date, database and schema names, owner, and any available comments. |
| [SHOW LISTINGS](sql/show-listings.md) | Lists the [listings](../collaboration/collaboration-listings-about.md) that you have privileges to access. |
| [SHOW LOCKS](sql/show-locks.md) | Lists all running transactions that have locks on resources. |
| [SHOW MAINTENANCE POLICIES](sql/show-maintenance-policies.md) | Lists the [maintenance policies](../developer-guide/native-apps/consumer-maintenance-policies.md) applied to the specified account or app. |
| [SHOW MANAGED ACCOUNTS](sql/show-managed-accounts.md) | Lists the managed accounts created for your account. |
| [SHOW MASKING POLICIES](sql/show-masking-policies.md) | Lists masking policy information, including the creation date, database and schema names, owner, and any available comments. |
| [SHOW MATERIALIZED VIEWS](sql/show-materialized-views.md) | Lists the materialized views that you have privileges to access. |
| [SHOW MCP SERVERS](sql/show-mcp-servers.md) | Lists the MCP (Model Context Protocol) servers for which you have access privileges. |
| [SHOW MFA METHODS](sql/show-mfa-methods.md) | Lists the [second factors of authentication](../user-guide/security-mfa-second-factor.md) that a user enrolled in multi-factor authentication uses to sign in to Snowflake. |
| [SHOW MODEL MONITORS](sql/show-model-monitors.md) | Lists all [model monitor](../developer-guide/snowflake-ml/model-registry/model-observability.md) that you can access in the current or specified schema and displays information about each one. |
| [SHOW MODELS](sql/show-models.md) | Lists the machine learning models that you have privileges to access. |
| [SHOW NETWORK POLICIES](sql/show-network-policies.md) | Lists all network policies defined in the system. |
| [SHOW NETWORK RULES](sql/show-network-rules.md) | Lists all network rules defined in the system. |
| [SHOW NOTEBOOK PROJECTS](sql/show-notebook-projects.md) | Lists the notebook projects (Snowflake `NOTEBOOK` objects) visible to the current role. |
| [SHOW NOTEBOOKS](sql/show-notebooks.md) | Lists the [notebooks](../user-guide/ui-snowsight/notebooks.md) for which you have access privileges. |
| [SHOW NOTIFICATION INTEGRATIONS](sql/show-notification-integrations.md) | Lists the notification integrations in your account. |
| [SHOW OBJECTS](sql/show-objects.md) | Lists the tables and views for which you have access privileges. |
| [SHOW OBJECTS OWNED BY APPLICATION](sql/show-objects-owned-by-application.md) | Lists the objects owned by an app that exists outside the app. |
| [SHOW OFFERS](sql/show-offers.md) | Provides information about all [offers](../user-guide/collaboration/listings/pricing-plans-offers/pricing-plans-and-offers.md) added to a listing. |
| [SHOW OPENFLOW DATA PLANE INTEGRATIONS](sql/show-oflow-data-plane-integration.md) | List OPENFLOW DATA PLANE INTEGRATIONS. |
| [SHOW ONLINE FEATURE TABLES](sql/show-online-feature-tables.md) | Lists the [online feature tables](sql/create-online-feature-table.md) for which you have access privileges. |
| [SHOW ORGANIZATION ACCOUNTS](sql/show-organization-accounts.md) | Lists the [organization account](../user-guide/organization-accounts.md) of the organization. |
| [SHOW ORGANIZATION PROFILES](sql/show-organization-profiles.md) | Lists the organization profiles for which you have access privileges. |
| [SHOW ORGANIZATION USER GROUPS](sql/show-organization-user-groups.md) | Lists [organization user groups](../user-guide/organization-users.md). |
| [SHOW ORGANIZATION USERS](sql/show-organization-users.md) | Lists [organization users](../user-guide/organization-users.md). |
| [SHOW PACKAGES POLICIES](sql/show-packages-policies.md) | Lists packages policy information. |
| [SHOW PARAMETERS](sql/show-parameters.md) | Lists all the account, session, and object parameters that can be set, as well as the current and default values for each parameter. |
| [SHOW PASSWORD POLICIES](sql/show-password-policies.md) | Lists password policy information, including the creation date, database and schema names, owner, and any available comments. |
| [SHOW PIPES](sql/show-pipes.md) | Lists the pipes for which you have access privileges. |
| [SHOW POSTGRES INSTANCES](sql/show-postgres-instances.md) | Lists the [Snowflake Postgres instances](../user-guide/snowflake-postgres/about.md) for which you have access privileges. |
| [SHOW PRICING PLANS](sql/show-pricing-plans.md) | Lists visible and hidden [pricing plans](../user-guide/collaboration/listings/pricing-plans-offers/pricing-plans-and-offers.md). |
| [SHOW PRIMARY KEYS](sql/show-primary-keys.md) | Lists primary keys for one or more tables. |
| [SHOW PRIVACY POLICIES](sql/show-privacy-policies.md) | Lists the [privacy policies](../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) for which you have access privileges. |
| [SHOW PRIVILEGES](sql/show-privileges.md) | Lists the privileges granted to an application. |
| [SHOW PROCEDURES](sql/show-procedures.md) | Lists all stored procedures that you have privileges to access, including built-in and user-defined procedures. |
| [SHOW PROJECTION POLICIES](sql/show-projection-policies.md) | Lists [projection policy](../user-guide/projection-policies.md) information, including the creation date, database and schema names, owner, and any available comments. |
| [SHOW REFERENCES](sql/show-references.md) | Lists the references defined for an application in the manifest file and the references the consumer has associated to the application. |
| [SHOW REGIONS](sql/show-regions.md) | Lists all the [regions](../user-guide/intro-regions.md) in which accounts can be created. |
| [SHOW RELEASE CHANNELS](sql/show-release-channels.md) | Lists the [release channels](../developer-guide/native-apps/release-channels.md) for an application package or listing. |
| [SHOW RELEASE DIRECTIVES](sql/show-release-directives.md) | Lists the release directives defined for an application package. |
| [SHOW REPLICATION ACCOUNTS](sql/show-replication-accounts.md) | Lists all the accounts in your organization that are enabled for replication and indicates the [region](../user-guide/intro-regions.md) in which each account is located. |
| [SHOW REPLICATION DATABASES](sql/show-replication-databases.md) | Lists all the primary and secondary databases (that is to say, all the databases for which replication has been enabled) in your account and indicates the [region](../user-guide/intro-regions.md) in which each account is located. |
| [SHOW REPLICATION GROUPS](sql/show-replication-groups.md) | Displays information about [replication groups and failover groups](../user-guide/account-replication-intro.md). |
| [SHOW RESOURCE MONITORS](sql/show-resource-monitors.md) | Lists all the resource monitors in your account for which you have access privileges. |
| [SHOW ROLES](sql/show-roles.md) | Lists all the roles which you can view across your entire account, including the system-defined roles and any custom roles that exist. |
| [SHOW ROLES IN SERVICE](sql/show-roles-in-service.md) | Lists all the service roles associated with a service. |
| [SHOW ROW ACCESS POLICIES](sql/show-row-access-policies.md) | Lists the row access policies for which you have access privileges. |
| [SHOW RUN … IN EXPERIMENT](sql/show-run-in-experiment.md) | Displays logged parameters or metrics for [experiment runs](../developer-guide/snowflake-ml/experiments.md). |
| [SHOW RUNS IN EXPERIMENT](sql/show-runs-in-experiment.md) | Lists the runs in an [experiment](../developer-guide/snowflake-ml/experiments.md). |
| [SHOW SCHEMAS](sql/show-schemas.md) | Lists the schemas for which you have access privileges, including dropped schemas that are still within the Time Travel retention period and, therefore, can be undropped. |
| [SHOW SECRETS](sql/show-secrets.md) | Lists the secrets for which you have rights to see. |
| [SHOW SEMANTIC DIMENSIONS](sql/show-semantic-dimensions.md) | Lists the dimensions in the [semantic views](../user-guide/views-semantic/overview.md) for which you have access privileges. |
| [SHOW SEMANTIC DIMENSIONS FOR METRIC](sql/show-semantic-dimensions-for-metric.md) | Lists the dimensions that you can return when querying a specific metric in a [semantic view](../user-guide/views-semantic/overview.md). |
| [SHOW SEMANTIC FACTS](sql/show-semantic-facts.md) | Lists the facts in the [semantic views](../user-guide/views-semantic/overview.md) for which you have access privileges. |
| [SHOW SEMANTIC METRICS](sql/show-semantic-metrics.md) | Lists the metrics in the [semantic views](../user-guide/views-semantic/overview.md) for which you have access privileges. |
| [SHOW SEMANTIC VIEWS](sql/show-semantic-views.md) | Lists the [semantic views](../user-guide/views-semantic/overview.md) for which you have access privileges. |
| [SHOW SEQUENCES](sql/show-sequences.md) | Lists all the sequences for which you have access privileges. |
| [SHOW SERVICE CONTAINERS IN SERVICE](sql/show-service-containers-in-service.md) | Lists the containers in all instances of a [service](../developer-guide/snowpark-container-services/working-with-services.md). |
| [SHOW SERVICE INSTANCES IN SERVICE](sql/show-service-instances-in-service.md) | Lists instances of a [service](../developer-guide/snowpark-container-services/working-with-services.md). |
| [SHOW SERVICE VOLUMES IN SERVICE](sql/show-service-volumes-in-service.md) | Lists the storage volumes for all instances of a [service](../developer-guide/snowpark-container-services/working-with-services.md). |
| [SHOW SERVICES](sql/show-services.md) | Lists the [Snowpark Container Services services](../developer-guide/snowpark-container-services/working-with-services.md) (including job services) for which you have access privileges. |
| [SHOW SESSION POLICIES](sql/show-session-policies.md) | Lists session policy information, including the creation date, database and schema names, owner, and any available comments. |
| [SHOW SHARED CONTENT IN APPLICATION PACKAGE](sql/show-shared-content.md) | Shows all of the objects for which you have access privileges that have been shared from a Declarative Native App application package. |
| [SHOW SHARES](sql/show-shares.md) | Lists all [shares](../user-guide/data-sharing-intro.md) available in the system. |
| [SHOW SHARES IN FAILOVER GROUP](sql/show-shares-in-failover-group.md) | Lists shares in a [failover group](../user-guide/account-replication-intro.md). |
| [SHOW SHARES IN REPLICATION GROUP](sql/show-shares-in-replication-group.md) | Lists shares in a [replication group](../user-guide/account-replication-intro.md). |
| [SHOW SNAPSHOT POLICIES — Deprecated](sql/show-snapshot-policies.md) | Lists all the [snapshot](../user-guide/backups.md) policies in your account for which you have access privileges. |
| [SHOW SNAPSHOT SETS — Deprecated](sql/show-snapshot-sets.md) | Lists all the [snapshot](../user-guide/backups.md) sets for which you have access privileges. |
| [SHOW SNAPSHOTS](sql/show-snapshots.md) | Lists the [snapshots of block storage volumes](../developer-guide/snowpark-container-services/block-storage-volume.md) for which you have access privileges. |
| [SHOW SNAPSHOTS IN SNAPSHOT SET — Deprecated](sql/show-snapshots-in-snapshot-set.md) | Lists all the [snapshots](../user-guide/backups.md) in a snapshot set. |
| [SHOW SPECIFICATIONS](sql/show-specifications.md) | Lists the app specifications that have been defined for an app. |
| [SHOW STAGES](sql/show-stages.md) | Lists all the stages for which you have access privileges. |
| [SHOW STORAGE LIFECYCLE POLICIES](sql/show-storage-lifecycle-policies.md) | Lists the [storage lifecycle policies](../user-guide/storage-management/storage-lifecycle-policies.md) for which you have access privileges. |
| [SHOW STREAMLITS](sql/show-streamlits.md) | Lists the Streamlit objects for which you have access privileges. |
| [SHOW STREAMS](sql/show-streams.md) | Lists the streams for which you have access privileges. |
| [SHOW TABLES](sql/show-tables.md) | Lists the tables for which you have access privileges, including dropped tables that are still within the Time Travel retention period and, therefore, can be undropped. |
| [SHOW TAGS](sql/show-tags.md) | Lists the tag information. |
| [SHOW TASKS](sql/show-tasks.md) | Lists the tasks for which you have access privileges. |
| [SHOW TELEMETRY EVENT DEFINITIONS](sql/show-telemetry-event-definitions.md) | Lists the [event definitions](../developer-guide/native-apps/event-definition.md) for the specified app. |
| [SHOW TRANSACTIONS](sql/show-transactions.md) | List all running transactions. |
| [SHOW USER FUNCTIONS](sql/show-user-functions.md) | Lists all user-defined functions (UDFs) for which you have access privileges. |
| [SHOW USER PROCEDURES](sql/show-user-procedures.md) | Lists all user-defined procedures for which you have access privileges. |
| [SHOW USER PROGRAMMATIC ACCESS TOKENS](sql/show-user-programmatic-access-tokens.md) | Lists the [programmatic access tokens](../user-guide/programmatic-access-tokens.md) associated with a user. |
| [SHOW USER WORKLOAD IDENTITY AUTHENTICATION METHODS](sql/show-user-workload-identity-authentication-methods.md) | **Related Topics** |
| [SHOW USERS](sql/show-users.md) | Lists all [users](../user-guide/admin-user-management.md) in the system. |
| [SHOW VARIABLES](sql/show-variables.md) | Lists all [variables](session-variables.md) defined in the current session. |
| [SHOW VERSIONS IN APPLICATION PACKAGE](sql/show-versions.md) | Lists the versions defined in the specified application package. |
| [SHOW VERSIONS IN DATASET](sql/show-versions-in-dataset.md) | Displays information about the datasets in your account at either the schema or database level. |
| [SHOW VERSIONS IN DBT PROJECT](sql/show-versions-in-dbt-project.md) | Displays a list of all versions of a [dbt project object](../user-guide/data-engineering/dbt-projects-on-snowflake.md). |
| [SHOW VERSIONS IN LISTING](sql/show-versions-in-listing.md) | Lists and provides details of all listing versions. |
| [SHOW VERSIONS IN MODEL](sql/show-versions-in-model.md) | Lists the versions in a machine learning model. |
| [SHOW VERSIONS IN ORGANIZATION PROFILE](sql/show-versions-in-organization-profile.md) | Lists the organization profile versions for which you have access privileges. |
| [SHOW VIEWS](sql/show-views.md) | Lists the views, including secure views, for which you have access privileges. |
| [SHOW WAREHOUSES](sql/show-warehouses.md) | Lists all the [virtual warehouses](../user-guide/warehouses-overview.md) in your account for which you have access privileges. |
| [SHOW WORKSPACES](sql/show-workspaces.md) | Lists the [workspaces](../user-guide/ui-snowsight/workspaces.md) for which you have access privileges. |
| **T** |  |
| [TRUNCATE MATERIALIZED VIEW](sql/truncate-materialized-view.md) | Removes all rows from a materialized view, but leaves the view intact (including all privileges and constraints on the materialized view). |
| [TRUNCATE TABLE](sql/truncate-table.md) | Removes all rows from a table but leaves the table intact (including all privileges and constraints on the table). |
| **U** |  |
| [UNDROP <object>](sql/undrop.md) | Restores the specified object to the system. |
| [UNDROP ACCOUNT](sql/undrop-account.md) | Restores a [dropped account](../user-guide/organizations-manage-accounts-delete.md) that has not yet been permanently deleted (a dropped account that is within its grace period). |
| [UNDROP DATABASE](sql/undrop-database.md) | Restores the most recent version of a dropped database. |
| [UNDROP DYNAMIC TABLE](sql/undrop-dynamic-table.md) | Restores the most recent version of a dropped [dynamic table](../user-guide/dynamic-tables-about.md). |
| [UNDROP EXTERNAL VOLUME](sql/undrop-external-volume.md) | Restores the most recent version of a dropped [external volume](../user-guide/tables-iceberg.md). |
| [UNDROP ICEBERG TABLE](sql/undrop-iceberg-table.md) | Restores the most recent version of a dropped [Apache Iceberg™ table](../user-guide/tables-iceberg.md). |
| [UNDROP NOTEBOOK](sql/undrop-notebook.md) | Restores the most recent version of a dropped notebook. |
| [UNDROP SCHEMA](sql/undrop-schema.md) | Restore the most recent version of a dropped schema. |
| [UNDROP SNAPSHOT](sql/undrop-snapshot.md) | Restores a previously removed [snapshot of a block storage volume](../developer-guide/snowpark-container-services/block-storage-volume.md). |
| [UNDROP STREAMLIT](sql/undrop-streamlit.md) | Restores the most recent version of a dropped Streamlit object. |
| [UNDROP TABLE](sql/undrop-table.md) | Restores the most recent version of a dropped table. |
| [UNDROP TAG](sql/undrop-tag.md) | Restores the most recent version of a tag to the system. |
| [UNSET](sql/unset.md) | Drops a [session variable](session-variables.md). |
| [UPDATE](sql/update.md) | Updates specified rows in the target table with new values. |
| [USE <object>](sql/use.md) | Specifies the role, warehouse, database, or schema to use for the current session. |
| [USE DATABASE](sql/use-database.md) | Specifies the active/current database for the session. |
| [USE ROLE](sql/use-role.md) | Specifies the active/current primary role for the session. |
| [USE SCHEMA](sql/use-schema.md) | Specifies the active/current schema for the session. |
| [USE SECONDARY ROLES](sql/use-secondary-roles.md) | Specifies the active/current secondary roles for the session. |
| [USE WAREHOUSE](sql/use-warehouse.md) | Specifies the active/current [virtual warehouse](../user-guide/warehouses-overview.md) for the session. |
