# Source: https://docs.axonius.com/docs/addremove-host-from-crowdstrike-falcon-host-group.md

# CrowdStrike Falcon - Add/Remove Assets to/from Host Group

**CrowdStrike Falcon - Add/Remove Assets to/from Host Group** (previously **Add/Remove Hosts from Crowdstrike Host Group**) adds or removes each of the devices from a Crowdstrike Host Group that are the result of the saved query supplied as a trigger (or devices selected in the asset table).

<Callout icon="📘" theme="info">
  Note

  To use the actions below, you must successfully configure a [CrowdStrike Falcon](/docs/crowdstrike-falcon) adapter connection.
</Callout>

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

These fields are required to run the Enforcement Action.

* **Action type** - Select either **Add Hosts** or **Remove Hosts**.
* **Host Group ID or Host Group Name** - The ID of the host group to which the asset will be added or from which it will be removed.

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **CrowdStrike Domain** - The hostname of the API server – this could be one of the following:
    * [https://falconapi.crowdstrike.com](https://falconapi.crowdstrike.com) (for "legacy" API)
    * [https://api.crowdstrike.com](https://api.crowdstrike.com) or [https://api.us-2.crowdstrike.com](https://api.us-2.crowdstrike.com) (for the latest API)

  * **User Name / Client ID** and **API Key / Secret** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Member CID** -  Specify a CrowdStrike CID to fetch data from all whether to fetch all tenants associated with it.
    * If supplied, Axonius will fetch data from all tenants associated with the Member CID (customer identification).
    * If not supplied , Axonius will only fetch data from the main tenant.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Create host group (if not exist)** - Creates the group in CrowdStrike if it does not exist.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Ports

Axonius must be able to communicate with the values supplied in [Connection Settings](#Connection-Settings) via the following ports:

* TCP Port 443

## Required Permissions

The values supplied in [**Username / Client ID** and **API Key / Secret**](#Connection-Settings) must have host-group write permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).