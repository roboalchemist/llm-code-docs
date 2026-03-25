# Source: https://docs.axonius.com/docs/azure-ad-update-windows-defender-security-intelligence.md

# Microsoft Entra ID (formerly Azure AD) - Update Windows Defender Security Intelligence

**Microsoft Entra ID (formerly Azure AD) - Update Windows Defender Security Intelligence** updates the Windows Defender Security Intelligence app for:

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID (formerly Azure Active Directory) and Microsoft intune Adapter](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - The ID for Microsoft Entra ID.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **Enable Certificate-Based Authentication** - Select to enable Axonius to send requests using the Azure certificates uploaded to allow secure Azure authentication for this adapter.

  * Click **Upload File** next to **Private Key File** to upload an Azure private key file in PEM format.

  * Click **Upload File** next to **Certificate File** to upload an Azure public key file in PEM format.

  <Callout icon="📘" theme="info">
    Note:

    The following parameters are only relevant for customers who have SaaS Management enabled.
  </Callout>

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).
  * **Username** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user.
  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-windowsdefenderupdatesignatures?view=graph-rest-beta) API.

* Use the `https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-windowsdefenderupdatesignatures?view=graph-rest-beta` endpoint.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* DeviceManagementManagedDevices.PrivilegedOperations.All

## Version Matrix

This Enforcement Action was tested only with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| beta    | yes       |       |
| v1.0    | yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).