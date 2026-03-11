# Source: https://docs.axonius.com/docs/set-unit-count-meetgradient.md

# Set Unit Count - Gradient

**Set Unit Count - Gradient** passes to Gradient the number of devices that have been seen by the selected adapter / adapter connection and sets the unit count in Gradient, which tracks customer billing data.
This action is performed for:

* Devices that match the results of the selected saved query, and match the Enforcement Action Dynamic Value Statement, if defined, or devices selected on the relevant asset page.

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

<Callout icon="📘" theme="info">
  Note

  This enforcement action runs on devices only.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Full Host Name or IP Address** *(default: `https://app.usegradient.com`)* - The hostname or IP address of the Gradient server.

* **Gradient Token** - The token used to communicate changes from your vendor account to the specific managed service provider (MSP). Gradient Token is created using Base64 encryption of a Vendor API Key and a Partner API Key. A valid GRADIENT-TOKEN is required to perform the <Anchor label="Create an Account" target="_blank" href="https://meetgradient.readme.io/reference/createaccount">Create an Account</Anchor> API Call. With a valid GRADIENT-TOKEN and properly mapped Accounts and Services, you will receive a 201 Success message.

* **Account ID** - This represents the ID for the Account you created in the <Anchor label="Create an Account" target="_blank" href="https://meetgradient.readme.io/reference/createaccount">Create an Account</Anchor> API Call. To retrieve the Account ID, perform the <Anchor label="Get Accounts" target="_blank" href="https://meetgradient.readme.io/reference/getaccounts">Get Accounts</Anchor> API Call.

* **Service ID** - This represents the ID for the service. To get the Service ID, perform the <Anchor label="Get Vendor" target="_blank" href="https://meetgradient.readme.io/reference/getaccounts">Get Vendor</Anchor> API Call.

* **Select adapters or adapter connections** - From the dropdown, select an adapter or adapter connection. The number of devices that the selected adapter / adapter connection has seen, is passed to Gradient.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

## APIs

Axonius uses the following:

* API documentation: \[<Anchor label="Set unit count" target="_blank" href="https://meetgradient.readme.io/reference/createbilling">Set unit count</Anchor>] API - Sets the route for adding a new unit count for one account, and one service. Subsequent calls debounce until calls are complete, after which billing views update.

* Integration walk-through: <Anchor label="Integration Build Guide" target="_blank" href="https://support.meetgradient.com/">Integration Build Guide</Anchor> - a step-by-step guide to building an integration with the Synthesize API.

## Required Permissions

The user account must have write/admin permissions.

For more details about other enforcement actions available, see [Action Library](/docs/action-library).