# Source: https://docs.axonius.com/docs/flexera-uninstall-software.md

# Flexera - Create Retirement Campaign

**Flexera - Create Retirement Campaign** creates a Retirement Campaign for:

* Devices returned by the selected query or devices selected on the Devices asset page.

The Retirement Campaign retires (uninstalls) the software that is no longer in use in your organization from the returned or selected devices.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

<Callout icon="📘" theme="info">
  Note

  * This Enforcement Action runs on Devices only.

  * You do not need to configure a Flexera adapter to use this Enforcement Action. Communication is via a REST connection other than the Flexera agent and not via the Flexera main management module.

  * There is no formal Flexera API.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Flexera IT Asset Management adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Flexera IT Asset Management](/docs/flexera-it-asset-management) adapter connection.
</Callout>

* **Campaign Type** (*default: 3 (retirement)*) - The identifier of the new campaign’s type.
* **Property Type** (*default: Group*) - The type of policy assigned to the campaign.
* **Property Name** (*default: memberOf*) - The name of the policy assigned to the campaign.
* **Property Value** (*default: \[AD group GUID]*) - The value of the policy assigned to the campaign. For Group property type, this is the group membership ID of the software that is to be uninstalled.
* **Property Display Name** (*default: All Users*) - The display name of the policy assigned to the campaign.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Flexera REST Agent command url** (*default: `http://my_flexera.domain.com/`*) - The encoded URL with encoded user and password of a specific Flexera agent.
* **User Name and Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTP Proxy**(optional) - Connect the adapter to an HTTP proxy instead of directly connecting it to the domain.
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
* **Visible** - Select this option to make this campaign visible. Selecting this option sets the *visible* attribute on the policy.
* **Apply Child OU** - Select this option to apply the retirement to all of the Organizational Unit's (OU) child OUs. Selecting this option sets the *applyChildOU* attribute on the policy.
* **Deployment Technology** (*default: 8*) - The code of the deployment technology used for software distribution. If an uninstall program is associated with the application in this deployment technology, this action sends an Uninstall request to the deployment technology.
* **Notify User (Always False)** - Select this checkbox to notify the user that this campaign has been enabled.
* **Enable Campaign** - Select this checkbox to enable the campaign after creation and modification. Selecting this option automatically uninstalls unused software without any user intervention.
* **Catalog ID** - The Flexera catalog ID to assign to the campaign. The ID of the Flexera software that is to be removed as part of the action.
* **Software Name Allow List** - Enter a comma-separated list of software names that can be included in this campaign.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

Permission is required to activate the Flexera - Create Retirement Campaign operation.

For more details about other enforcement actions available, see [Action Library](/docs/action-library).