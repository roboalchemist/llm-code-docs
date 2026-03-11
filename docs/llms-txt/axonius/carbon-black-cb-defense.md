# Source: https://docs.axonius.com/docs/carbon-black-cb-defense.md

# VMware Carbon Black Cloud (Carbon Black CB Defense)

VMware Carbon Black Cloud (formerly Carbon Black CB Defense) is a cloud native platform delivering next-generation antivirus and endpoint detection and response. This adapter is also compatible with Carbon Black Cloud Enterprise EDR (formerly CB ThreatHunter) and Carbon Black Cloud Audit and Remediation (formerly CB LiveOps).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications, Users, Roles

## Parameters

1. **VMware Carbon Black Cloud Domain** *(required)* - Use your VMware Carbon Black Cloud domain, in the following format:
   * To use the latest Carbon Black Devices API: `https://defense-\<environment>.conferdeploy.net/`

2. **API ID** and **API Secret Key** *(required)* - Use the API ID and the API Secret Key you generated from the Connectors page of the VMware Carbon Black Cloud console.
   For details on generating the API token and the Connector ID, see the [CB Defense API authentication reference](https://developer.carbonblack.com/reference/cb-defense/authentication/).

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **VMware Carbon Black Cloud Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **VMware Carbon Black Cloud Domain**.

5. **Organization Key** *(required)* - Your organization key, used to fetch data from the VMware Carbon Black Cloud adapter connection.
   You can find your organization key in the **VMware Carbon Black Cloud Console** under **Settings** `>` **API Keys**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="connection parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-6ANQUWZ9.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch deregistered devices** *(required, default: true)* - Select to fetch deregistered devices.
2. **Fetch Vulnerabilities** - Select to fetch vulnerabilities on devices.

<Callout icon="📘" theme="info">
  Note

  In addition to selecting this option, you must enter a value in the **Organization Key** parameter. Vulnerabilities are only available via [Carbon Black Devices API](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/devices-api/).
</Callout>

3. **Fetch only active devices** *(optional)* - Select to exclude inactive devices from the fetch.
4. **Fetch users** - Select to fetch Users.
5. **Fetch user roles** - Select to fetch Roles. You must enable **Fetch users** as well for this to work.
6. **Page Size** *(required, default: 100)* - Specify the number of entities returned per page request.
7. **Filter duplicates based on device hostname** - When selected, the adapter will only fetch the latest asset for each hostname based on the field "last\_contact\_time" from the API.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Carbon Black Devices API](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/devices-api/).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have 'Device - General Information - Read' custom permissions.
'vulnerabilityAssessment.data READ' - permissions are required to fetch vulnerabilities.
In addition, to create:

* [Change VMware Carbon Black Cloud Policy Enforcement Actions](/docs/change-carbon-black-cb-defense-policy-by-policy-id)
* [Isolate and Unisolate in VMware Carbon Black Cloud Enforcement Actions](/docs/isolate-and-unisolate-in-carbon-black-cb-defense)

you also need 'Device - Quarantine - Execute' permissions.

Refer to [Carbon Black Cloud API Access](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/#creating-a-custom-access-level) for full details of the custom access level steps.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                   | Supported | Notes |
| ----------------------------------------- | --------- | ----- |
| Latest version of Carbon Black Device API | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5

### Related Enforcement Actions

[VMware CB Cloud - Quarantine/Unquarantine Assets](/docs/isolate-and-unisolate-in-carbon-black-cb-defense)

[VMware CB Cloud - Change Policy by Policy ID](/docs/change-carbon-black-cb-defense-policy-by-policy-id)

[VMware CB Cloud - Change Policy by Name](/docs/change-vmware-carbon-black-cloud-policy-by-name)

[VMware CB Cloud - Delete Assets](/docs/carbonblack-defense-delete-devices)

[VMware CB Cloud - Create User](/docs/carbon-black-cb-defense-create-user)

[VMware CB Cloud - Delete User](/docs/carbon-black-cb-defense-delete-user)

[VMware CB Cloud - Assign Role to User](/docs/carbonblack-defense-assign-role-to-user)