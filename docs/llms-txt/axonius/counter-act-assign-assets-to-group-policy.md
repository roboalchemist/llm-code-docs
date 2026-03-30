# Source: https://docs.axonius.com/docs/counter-act-assign-assets-to-group-policy.md

# Forescout CounterACT - Assign Assets to Group Policy

**Forescout CounterACT Assign Assets to Group Policy** assigns assets to a Forescout group policy, for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

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

* **Use stored credentials from Forescout CounterACT adapter** - Enable this option to use Forescout CounterACT connected adapter credentials. When not enabled, see [Connection Parameters](/docs/counter-act-assign-assets-to-group-policy#connection-parameters).
  * When you enable this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Action.

* **Agent group ID** -  Specify the Forescout group policy ID to which to assign the assets returned by the query.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Forescout CounterAct Domain** - The full URL of the Forescout server.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

## APIs

Axonius uses the [Forescout eyeExtend Connect Module: Web API](https://docs.forescout.com/bundle/web-api-1-5-4-h/page/t-configure-web-api-plugin.html).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).