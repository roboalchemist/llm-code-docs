# Source: https://docs.snowflake.com/en/connectors/mysql6/prereqs.md

# Source: https://docs.snowflake.com/en/connectors/servicenow/prereqs.md

# Prepare your ServiceNow® instance

Before installing the Snowflake Connector for ServiceNow®, you must set up your ServiceNow® instance. Complete the following steps:

* ServiceNow® instance access - ensure your ServiceNow® instance is ready for use
* ServiceNow® user - Ensure the required user is properly configured
* Set up column indexes for optimized performance - Configure column indices for best performance
* Optional steps - review and perform optional configuration, if required

## ServiceNow® instance access

* Ensure the ServiceNow® instance is publicly available. The connector does not work with instances hidden behind a VPN.
* If you are using [IP Address Access Control](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/login/task/t_AccessControl.html) for your ServiceNow® instance, you won’t be able to successfully install the connector.
  For more information see [the community article](https://community.snowflake.com/s/article/Why-Snowflake-doesn-t-share-static-IP-address-with-customer).

## ServiceNow® user

Identify or create the ServiceNow® user for the connector.

To connect to the ServiceNow® instance, the connector must authenticate to the instance as a ServiceNow®
user. Choose a ServiceNow® user that meets the following requirements:

* The username cannot contain a colon (`:`).
* The user must have `read`, `query_match` and `query_range` access to all records in the ServiceNow® tables that
  you plan to ingest. Access control lists (ACLs) should not hide any records in these tables from this user.
* The user must have `read`, `query_match` and `query_range` access to all rows in the following tables in order
  to enable schema detection:

  * `sys_db_object` (with the fields `name`, `super_class`, `sys_id`),
  * `sys_glide_object` (with the fields `name`, `scalar_type`, `sys_id`),
  * `sys_dictionary` (with the fields `element`, `internal_type`, `name`, `sys_id`).
* The user must have `read`, `query_match` and `query_range` access to all rows in the following table in order to
  use the proper ingestion strategy:

  * `sys_table_rotation` (with the `name` and `sys_id` fields).
* The user must have `read`, `query_match` and `query_range` access to the `sys_updated_on` field in the
  below tables in order to not to use less cost-effective “truncate and load” ingestion mode:

  * `sys_db_object`,
  * `sys_glide_object`,
  * `sys_dictionary`,
  * `sys_table_rotation`,
  * journal table (usually `sys_audit_delete`).

> **Note:**
>
> Configuring the connection in Snowsight using the OAuth authentication to ServiceNow® is possible only
> with [interactive user](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/users-and-groups/concept/c_NonInteractiveSessions.html). The ServiceNow® user is interactive if the Web service access only
> setting is disabled for the user.
>
> You can use the OAuth authentication with non-interactive users only if you configure the connection with SQL commands.
> In this case, you cannot log in to ServiceNow® or get the OAuth refresh token using Snowsight.

## Set up column indexes for optimized performance

If you plan to ingest and synchronize a ServiceNow® table that has a `sys_updated_on` field, we recommend setting up
an index on that column. For information on setting up the indexes, see the [Create a Table Index](https://docs.servicenow.com/bundle/washingtondc-application-development/page/administer/table-administration/task/t_CreateCustomIndex.html) in the ServiceNow® documentation.

After you create the index through the user interface, it may take some time for the index to be constructed.
The indexing process runs as a background task.

If your instance has large tables, Snowflake recommends contacting ServiceNow® customer support to ask
about the best approach to indexing large tables.

## Optional steps

* If you plan to use the OAuth authentication method, and you have the [read-only role](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/user-administration/concept/c_ReadOnlyRole.html)
  assigned to your ServiceNow® user, make sure the `glide.security.snc_read_only_role.tables.exempt_create`
  system property has the `oauth_credential` table in its value list.

  Create or edit the `glide.security.snc_read_only_role.tables.exempt_create`
  property in the `sys_properties` table. For more details on editing this property, see [ServiceNow Knowledge Base](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783404).

  To learn how to add a new system property, see [Add a system property](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/reference-pages/reference/r_AvailableSystemProperties.html#t_AddAPropertyUsingSysPropsList) in the ServiceNow® documentation.
* To enable deleted records to be propagated, use the `sys_audit_delete` table as the source of information about deleted records.

  > **Note:**
  >
  > Please note that the connector must have access to all journal table records or the installation may fail.
  > Otherwise record deletions in other tables may not be correct.
  >
  > If journal table rows are hidden by ACLs, connector behavior is unpredictable.
  > Even if the installation is successful, some deletions may not be correctly synchronized at later points in the process.

  * To use `sys_audit_delete`:

    1. Set the `no_audit_delete` [dictionary attribute](https://docs.servicenow.com/bundle/washingtondc-application-development/page/administer/reference-pages/concept/c_DictionaryAttributes.html) to `false`.
    2. Make sure that the ServiceNow® user for the connector has access to the `sys_audit_delete` table and
       the `documentkey`, `tablename`, `sys_id`, and `sys_created_on` fields in this table.
    > **Note:**
    >
    > The connector is only able to synchronize deleted records if they are audited.
    > Delete operations that do not call `DBDelete.setWorkflow()` are not ingested in Snowflake.
    >
    > Refer to your ServiceNow® product documentation for more information on using `DBDelete.setWorkflow()`.
    >
    > Also, note the following about deleted records:
    >
    > * Record deletions are not tracked for tables with the `no_audit_delete=true` dictionary attribute.
    > * Record deletions from tables with a `sys` prefix are not tracked by default.
    > * The connector can only ingest records deleted with cascade record deletion if the reference field is on an
    >   audited table. Refer to your ServiceNow® product documentation for more information on cascade record deletion.

## Next steps

After completing these procedures, follow the steps in [Install and configure the connector with Snowsight](installing-snowsight.md) or [Install and configure the connector with SQL commands](installing-sql.md).
