# Source: https://docs.axonius.com/docs/sentinelone-enable-disable-agent.md

# SentinelOne - Enable Or Disable Agent

**SentinelOne - Enable Or Disable Agent** enables or disables SentinelOne agents for:

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

* **Use stored credentials from the SentinelOne adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [SentinelOne](/docs/sentinelone) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **SentinelOne Domain** - The domain of the SentinelOne service.
  * **User Name**, **Password**, **2FA Secret**, and **API token** - These parameters are required only for customers with the Axonius SaaS Applications product. For more information on these parameters, see [Required Parameters - Application Settings](/docs/sentinelone#required-parameters-application-settings).
  * **Singularity Data Lake (SDL) API Key** *(optional)* - You can leave this parameters empty as it's not relevant for this action.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

* **Disable agents instead of enabling** - This action enables agents by default. Check this option to disable agents instead.
* **Reboot the endpoint** - Select whether this action should reboot the endpoint (parameter required by the SentinelOne API).

## APIs

Axonius uses the following APIs:

[Enable Agent | SentinelOne ](https://www.postman.com/api-evangelist/sentinelone/request/ppxzplf/enable-agent)
[Disable Agent | SentinelOne](https://www.postman.com/api-evangelist/sentinelone/request/muxn9u4/disable-agent)

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Permissions for the account, site, or group where the agent needs to be enabled/disabled
* A role that allows to disable agents: Admin, IR team or IT

## Version Matrix

This Enforcement Action was tested only with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| API V2.1 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).