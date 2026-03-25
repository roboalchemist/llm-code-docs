# Source: https://docs.axonius.com/docs/beyond-trust-sql-send-block-policy-to-scp.md

# BeyondTrust BeyondInsight - Send Block Policy to SCP

**BeyondTrust BeyondInsight - Send Block Policy to SCP** sends a block policy, in XML format,  for the software that results from the saved query supplied as a trigger (or assets that were selected in the asset table), and sends it to a specific path on an SSH server using SCP.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Hostname** - DNS Address or IP of the SSH server.
* **User name**  - The SSH user name to connect with.
* **SSH port** *(default: 22)* - The SSH port.
* **XML target path** *(default: /home/policy.xml)* - Specify the full path on the SSH server, including the file name.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional:

<Callout icon="📘" theme="info">
  NOTE

  For authentication, you must specify at least **Password** or **Private key**, but you can also specify both.
</Callout>

* **Password** - A password for the SSH user, if it exists. If specified, the password is used for authentication.

* **Private key** - To use a private key for the SSH user, select a file and click **Upload File**.

* **Private key passphrase** - Specify a private key passphrase if the private key is protected by a passphrase.

* The following fields are section names in the XML that is created by the Enforcement Action. Enter a value for the relevant fields.

  * **Configuration ID**
  * **Configuration Version**
  * **Configuration Revision**
  * **Configuration Revision Number**
  * **GlobalOptionsSet ID**
  * **Trusted Application Protection Version**
  * **Trusted Application Protection Revision**
  * **Application Group ID**
  * **Application Group Name**
  * **Application Type** *(default: exe)*

  An XML tag is created for each installed application.

* **Get installed software from CSV adapter only** -
  * When this option is enabled (the default), the XML file only includes software titles that are from the CSV adapter connection.
  * When this option is disabled, the XML file includes software titles from the specified adapter connections.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).