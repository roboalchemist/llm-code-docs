# Source: https://docs.axonius.com/docs/snow-software-asset-management-send-software-xml-to-scp.md

# Snow Software Asset Management - Send Software XML to SCP

**Snow Software Asset Management - Send Software XML to SCP** exports XML software data in Snow Software format for:

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

* **Hostname** - The hostname or IP address of where to copy the Snow Software XML.

* **SSH port** - Enter a value for the SSH port to use for the connection. Otherwise, Axonius uses the default port 22.

* **XML target path** - Specify the full path on the SSH server, including the file name.

* **Install Date** - Click the calendar icon to select the date that software data is to be exported back into Snow Software.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to securely copy the XML.
* **Private key** - Click **Upload File** to choose and upload the Private key certificate file (in PEM format).
* **Private key passphrase** *(default: empty)* - Enter the password for the Private key file, if it is password-protected.
* **Associated Device Username** - Enter the name of the user associated with the device.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).