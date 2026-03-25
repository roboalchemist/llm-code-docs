# Source: https://docs.axonius.com/docs/run-kace-scripts.md

# Quest KACE - Run Script

**Quest KACE - Run Script** runs a KACE script for:

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

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Quest KACE adapter** - Select this option to use the first connected Quest KACE adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a [Quest KACE](/docs/quest-kace-endpoint-systems-management-appliances) adapter connection.

  * The user name and the password used for the adapter connection must have the [Required Permissions](#required-permissions) to fetch assets.
</Callout>

## Required Fields

These fields are required to run the Enforcement Set.

* **Script ID** - The ID of the KACE script to run.
  * Identify the correct [Script ID](https://support.quest.com/kb/111231/how-to-determine-the-kace-sma-script-number-or-id)

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **KACE SMA Domain** - The hostname of the KACE Systems Management Appliance (SMA) server.

  * **User Name** and **Password** - The user name and password for an account that has permissions to run scripts on machines.

  * **Organization Name** - The organization name. If the KACE Systems Management Appliance (SMA) appliance is configured for multiple organizations, The connection is limited to a single specified organization for the requesting user.

  * **Quest KACE Version** - From the dropdown, select the Quest Kace version to use: **V11**, **V12**, **V13**, or **V14**.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* For V12.0 - [KACE Systems Management Appliance 12.0 - API Reference Guide](https://support-public.cfm.quest.com/63445_KACE_SMA_12.0_API_Reference_en-US.pdf).
* For V14.0 - [KACE Systems Management Appliance 14.0 Common Documents - API Reference Guide](https://support.quest.com/technical-documents/kace-systems-management-appliance/14.0%20common%20documents/api-reference-guide/7#TOPIC-2209039)

## Required Permissions

The user account specified must have:

* *Administrator* role to run scripts.
* Select the **Manage Device Access** option:

<Image align="center" alt="Admin Role - Mobile Device Access.png" border={false} width="250px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Admin%20Role%20-%20Mobile%20Device%20Access.png" />

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the following ports:

* **TCP port 443**

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).