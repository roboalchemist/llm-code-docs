# Source: https://docs.axonius.com/docs/crowd-strike-run-command.md

# CrowdStrike Falcon - RTR Run Command

**Crowdstrike Falcon - RTR Run Command** runs a Real-Time-Response command on hosts with a CrowdStrike agent installed. Refer to CrowdStrike RTR documentation for a list of valid commands and their syntax. This Enforcement Action uses the selected query to return a list of assets with CrowdStrike agents installed. Or the Action is run on assets selected on the relevant asset page.

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

* **Use stored credentials from  CrowdStrike Falcon Adapter** - Select this option to use [CrowdStrike Falcon](/docs/crowdstrike-falcon) connected adapter credentials.

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [CrowdStrike Falcon](/docs/crowdstrike-falcon) adapter connection.
  </Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **RTR Command** - The RTR command that the Enforcement Action will run. The default comment is:
  `runscript -CloudFile=test_script -CommandLine=__MDX_CODE_0__ `. You can also use the `put` command.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **CrowdStrike Domain** - The hostname of the API server – this could be one of the following:
    * [https://falconapi.crowdstrike.com](https://falconapi.crowdstrike.com) (for "legacy" API)
    * [https://api.crowdstrike.com](https://api.crowdstrike.com) or [https://api.us-2.crowdstrike.com](https://api.us-2.crowdstrike.com) (for the latest API)

  * **User Name / Client ID** and **API Key / Secret** - The credentials for a user account that has the [Required Permissions](#required-permissions) to run RTR commands.

  * **Member CID** - The Customer ID of the CrowdStrike member.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.
* **Queue command for offline devices** - When selected, adds the "queue\_offline" parameter as 'True' when sending the requests.

## APIs

Axonius uses the [CrowdStrike API](https://assets.falcon.crowdstrike.com/support/api/swagger.html).

## Required Ports

Axonius must be able to communicate via the following ports:

* TCP Port 443

## Required Permissions

The values supplied in **Username / Client ID** and **API Key / Secret** must have host-group write permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).