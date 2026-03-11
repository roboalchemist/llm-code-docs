# Source: https://docs.axonius.com/docs/netskope.md

# Netskope

Netskope Security Cloud provides threat protection for cloud services, websites, and private applications.

## Asset Types Fetched

* Devices, Users, Application Extensions, Admin Managed Extensions, User Initiated Extensions, Application Add-Ons, Groups, Application Extension Instances, Admin Managed Extension Instances, User Initiated Extension Instances, Application Add-On Instances, Application Keys, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### Permissions

If using API V2 or API V3, the following permissions are required:

* Devices:

  * Recommended: /events/datasearch/clientstatus
  * If you have a PDEM license, the following API endpoints are optional (the above endpoint is still recommended):

    * /api/v2/adem/userlist
    * /api/v2/adem/users/device/getlist
    * /api/v2/adem/users/device/getdetails

Users and SaaS Applications/User Extensions (at least one of the below listed endpoints is required):

* events/dataexport/events/alert
* events/dataexport/events/application
* events/dataexport/events/audit
* events/dataexport/events/connection
* events/dataexport/events/incident
* events/dataexport/events/infrastructure
* events/dataexport/events/network
* events/dataexport/events/page
* events/dataexport/events/endpoint

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Netskope Domain** - The hostname of the Netskope server.
2. **API Token** - Specify your account API key or an API token you have created.

<br />

<Image align="center" border={false} width="auto" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetskopeAdapter.png" height="auto" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the host supplied in **Netskope Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to **Netskope Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch mobile devices** *(required, default: True)* - Choose whether to fetch mobile devices in addition to standard devices.
2. **Fetch users from alerts less than X hours old** *(required, default: 0)* - Set a number of hours to fetch alerts triggered by users created in the number of hours defined in the field. Note that the default value for this field is 0. If you do not enter a value in this field no users are fetched.
3. **Fetch user UCI scores** - Select this option to fetch user UCI scores. This setting only works when using the V2 API. Note that the API key must have read access to the `/api/v2/incidents/uba/getuci` API endpoint.
4. **Fetch the last seen date from events** - By default (when this option is not selected) Axonius fetches the last seen date for this adapter from the 'last\_event/timestamp' field. When you select this option it populates the Last Seen field with the latest event brought by the `/api/v1/events` endpoint with `access_method` equals `access_method eq Client` and `type` equals `application`
5. **Do not ingest duplicates** - Select this option so that the adapter will ignore assets with the same NS Device UID if any were ingested previously during the same fetch.
6. **Use API V2/V3** - Select this option to fetch data using the API V2 or API V3.

<Callout icon="📘" theme="info">
  Note:

  To be able to fetch devices from API V2 or V3, you need to generate an API key with access to specific API endpoints. For more information, see [Required Permissions](/docs/netskope#required-permissions) below.

  A PDEM license is required in order to use the ADEM endpoints in API V2 or V3. If you do not have this license, you can continue using API V1 to fetch device data.

  Due to the structure of the API V2 and API V3 endpoints, the device data is fetched in a time window. The adapter uses the "Ignore devices that have not been seen by the source in the last X hours" setting to define this window. If the setting is not configured it uses a default window of 10 days.
</Callout>

7. **Ignore SaaS Applications Repository and parse all applications** *(Only for accounts with SaaS Management capabilities)* - Select this option to ignore the SaaS Applications Repository and parse all apps found by the Netskope adapter.
8. **Fetch device os from sorted events** - Select this option to fetch the device OS data from sorted events.
9. **Fetch users/groups from SCIM API (V2/V3 only)** - Select this option to fetch users and groups from the SCIM API when using the API V2 or API V3.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](https://docs.axonius.com/docs/advanced-settings).
</Callout>

## Related Enforcement Actions

* [Create a new Netskope SCIM User](https://docs.axonius.com/axonius-help-docs/docs/create-a-new-netskope-scim-user)
* [Create a new Netskope SCIM Group](https://docs.axonius.com/axonius-help-docs/docs/create-a-new-netskope-scim-group)
* [Assign a netskope SCIM group to a SCIM user](https://docs.axonius.com/axonius-help-docs/docs/assign-a-netskope-scim-group-to-a-scim-user)
* [Remove a netskope SCIM group from a SCIM user](https://docs.axonius.com/axonius-help-docs/docs/remove-a-netskope-scim-group-from-a-scim-user)
* [Update a existing netskope SCIM user](https://docs.axonius.com/axonius-help-docs/docs/update-a-existing-netskope-scim-user)
* [Update a existing netskope SCIM group](https://docs.axonius.com/axonius-help-docs/docs/update-a-existing-netskope-scim-group)