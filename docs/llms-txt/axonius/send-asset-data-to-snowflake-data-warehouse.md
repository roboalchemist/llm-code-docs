# Source: https://docs.axonius.com/docs/send-asset-data-to-snowflake-data-warehouse.md

# Send Assets Data - Snowflake Data Warehouse

**Snowflake Data Warehouse - Ingest Data Files from Cloud Storage** takes files from a cloud data storage (e.g., S3 on AWS) and uses a predefined pipe to insert the data from the files into Snowflake's Data Warehouse for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from Snowflake Data Warehouse adapter** - Select this option to use credentials from the adapter connection.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Snowflake Data Warehouse](/docs/snowflake) adapter connection.
  </Callout>

* **Pipe Name** - Case-sensitive fully-qualified name of a pipe that loads data from files as soon as they are available. For example, *myDatabase.mySchema.myPipe*.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Account Identifier** - The Snowflake account within your organization. The preferred structure is: `<organization_name>-<account_name>`

    For more information, see [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html).

  * **Warehouse** *(default: COMPUTE\_WH)*  - Enter the relevant data warehouse. Note that the value is case-sensitive.

  * **Username** - The credentials for a user account that has [required permissions](/docs/snowflake-data-warehouse#required-permissions) to  perform this action.

  * **RSA Private Key** - Upload the [RSA Private Key](https://docs.snowflake.com/en/user-guide/key-pair-auth.html#configuring-key-pair-authentication) associated with a user account that has permissions  perform this action.

  * **Devices View Name** - Enter the View/Table that you want to push data to.

    * The View/Table requires one of the following identifiers in order to fetch devices:  'ID', 'id', 'SERIAL', 'assetname'. Note that the values are case-sensitive.

    * In each Snowflake account, the name of the View/Table is user-defined, such as ACCOUNT\_USAGE.DATABASES.

    * The primary use of this field is to test that a connection to the vendor can be established.

  * **Key Passphrase** - Enter the passphrase for an encrypted key.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **Request ID** - The ID of the request.
</Callout>

* **Files** - Click + for each CSV file with asset data that you want to push into the Snowflake data warehouse.

  * **File Path** - The path to the CSV file.
  * **File Size** - The size of the CSV file.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Snowpipe REST API](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-rest-apis).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).