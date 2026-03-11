# Source: https://docs.axonius.com/docs/sentinelone-execute-remote-script.md

# SentinelOne - Execute Remote Script

**SentinelOne - Execute Remote Script Orchestration** executes a remote script on assets from SentinelOne for:

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

* **Use stored credentials from the SentinelOne Adapter** - Select this option to use [SentinelOne](/docs/sentinelone) adapter credentials.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [SentinelOne](/docs/sentinelone) adapter connection.
  </Callout>

* **Script Name** - Enter a name for the script.

* **Task Description** - Enter a description of the task the script performs.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **SentinelOne Domain** - The domain of the SentinelOne service.

  * **User Name** - The username to use to access SentinelOne.

  * **Password** - The password to use to access SentinelOne.

  * **API token** - The API token used to access SentinelOne.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Input Parameters** - Add any input parameters for the script.
* **Output Directory** - Specify a directory for script output.
* **Output Destination** - Select the destination for the output: Local , None , SentinelCloud, SingularityXDR.
* **Requires Approval** - Select if the script requires approval before running.
* **Singularity XDR URL** - Provide the URL for the Singularity XDR.
* **Singularity XDR Keyword** - Provide the keyword for the Singularity XDR.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## API

Axonius uses the [SentinelOne API](https://euce1-100.sentinelone.net/api-doc).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have either Write or Admin permissions.