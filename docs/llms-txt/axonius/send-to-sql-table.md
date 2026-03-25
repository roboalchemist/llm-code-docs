# Source: https://docs.axonius.com/docs/send-to-sql-table.md

# SQL - Send Assets to Table

**SQL - Send Assets to Table** inserts the assets returned by the selected query, or assets selected on the relevant asset page, to the MSSQL table supplied.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **DB Type** - Select the type of database, either Oracle, MSSQL PostgreSQL or MySQL.

* **SQL Server host** - The hostname / domain of the SQL server.

* **SQL Server port** - The port of the SQL server.

* **User name** - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  NOTE

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/sql-server#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

* **Password** - The user's password. The password must not include ";".
* **SQL Server database name** - The database to connect to.
* **SQL Server table name** - The name of the table to write query information to. Axonius runs a `INSERT INTO [[specified value]] VALUES ([[query values]])` statement.
* **Chunk size** *(default: 50)* - When working with servers that are limited to certain data size in a request, break the message into chunks of the set size.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

* **MySQL Character Set** - Specify a custom character set (encoding) for connections to MySQL databases. Example values: 'utf8', 'latin1'. When no character set is specified, 'utf8' is used by default.
  Note: This option is only valid when MySQL is selected from the Database Type dropdown.
* **Truncate table data before update** - Select whether to truncate the table data before update.
  * If enabled, the table data will be truncated and the table will contain only the newly added records.
  * If disabled, the table data will not be truncated and new records will be added to the existing table.
* **Create table if not exist** - Select whether to create a new SQL table if the supplied table name does not exist.
  * If enabled, a new SQL table will be created if the supplied table name is not found.
  * If disabled, the action will fail, as the supplied table name is not found.
* **Re-create table each time** - Select to delete the table on the server side and create a new one every time the action is run
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Axonius to SQL Server field mapping** - Enter a list of SQL fields to map to Axonius fields is JSON format or in Python Dict format. For example:
  `{"machine_id": "id", "company_id": "org_id", "event_date": "event_timestamp"}`
* **Split by field values** - For complex fields and lists, you can create a CSV file where the values of complex fields and lists are represented as separate rows in the file.
* **MSSQL Connection Timeout** - Specify a custom timeout in seconds for MSSQL connections.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).