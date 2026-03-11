# Source: https://docs.axonius.com/docs/trend-micro-apex-one-manage-security-agent.md

# Trend Micro Apex One (OfficeScan) - Isolate, Restore, Relocate Security Agent

**Trend Micro Apex One (OfficeScan) - Isolate, Restore, Relocate Security Agent**  isolates, restores, relocates, or uninstalls the security agent assigned to each entity that is the result of the saved query supplied as a trigger (or assets selected in the asset table).

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

**Use stored credentials from the Trend Micro Apex One Adapter** - Select this option to use [Trend Micro Apex One](/docs/trend-micro-apex-one) connected adapter credentials. When you select this option, the Select Adapter Connection drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Action Settings

* **Action type** - Select the action to run. Possible options (in dropdown) are:
  * **Isolate Security Agent** - Isolate the agent on all queried devices.
  * **Restore Security Agent** - Restore the agent on all queried devices.
  * **Uninstall Security Agent** - Uninstall the agent from all queried devices.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Trend Micro Apex Central IP Address** -The hostname or IP address of the Trend Micro Apex One server that Axonius can communicate with.
  * **Application ID** -  The application unique Identifier assigned for Axonius to consume Trend Micro Control Manager Automation APIs.
  * **API Key** - Enter your Trend Micro Apex One API Key.
  * The api-key and api-secret are retrieved via the Axonius website. See [Get an API Key](/docs/axonius-rest-api).
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).