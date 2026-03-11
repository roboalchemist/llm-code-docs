# Source: https://docs.axonius.com/docs/exabeam-update-context-table.md

# Exabeam - Update Context Table

**Exabeam - Update Context Table** updates and/or creates a context table in Exabeam Advanced Analytics for:

* Assets returned by the selected query or assets selected on the relevant asset page.
  ​

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

* **Use stored credentials from the Exabeam adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      To use this option, you must successfully configure a [Exabeam](/docs/exabeam) adapter connection.
    </Callout>

* **Context Table Name** - Enter the name of the table where the new records will be created. If the table already exists, the Action adds the data to the existing table. If it doesn't exist, it will be created.

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain Name or IP Address** - The domain name or IP address of the Exabeam server.

  * **Login Method** - Select the log in method to use:

    * **Username and Password**

    * **Cluster Authentication Token**

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to create and update assets.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Key field** - Specify which adapter field should be mapped onto the Key field in the indicated Exabeam Context table. For example, *hostname*, *last\_seen*, or *first\_seen*.
* **Value field** - Specify which adapter field should be mapped onto the Value field in the indicated Exabeam Context table. For example, *hostname*, *last\_seen*, or *first\_seen*.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).

​