# Source: https://docs.axonius.com/docs/ivanti-unified-endpoint-manager.md

# Ivanti Unified Endpoint Manager (Landesk)

Ivanti Unified Endpoint Manager (formerly Landesk) helps IT administrators gather detailed device data, automate software and OS deployments, personalize workspace environments, and fix user issues.

### Asset Types Fetched

* Devices, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Landesk API MBSDK](https://forums.ivanti.com/s/article/Getting-Started-with-the-MBSDK-Example-Scripts-Included?language=en_US).

### Permissions

The following permissions are required for Ivanti credentials:

* Grant a role in EPM ("Auditor")
* Add to Windows Security Group ("Landesk Management Suite")

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Ivanti UEM Domain** - The hostname of the Ivanti server.
2. **User Name** and **Password** - The user name and password for an account that has read access to the API.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Ivanti Unified Endpoint Manager" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ivanti%20Unified%20Endpoint%20Manager.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Comma separated custom fields** *(optional)* - Provide a comma separated list of fields that will be queried from the Landesk instance and added as a list of values in the device, for example to show:
   * "Computer".”Device Name”
   * "Computer"."Display Name"
   * "Computer"."OS"."Name"
   * "Computer"."Software"."Package"."Name"
     Enter in the field:
     `"Computer".”Device Name”`,`"Computer"."Display Name"`, `"Computer"."OS"."Name"`,`"Computer"."Software"."Package"."Name"`

2. **Filter devices with unassigned GUID from fetch** -  If selected, the adapter won't fetch devices with an “Unassigned” GUID, and the API query won't show devices lacking a GUID. If cleared, then devices without a GUID can be fetched. For example, there might be devices in the Discovery table that still weren't assigned an agent.

3. **Compensate for day/month order inconsistencies** - Select this option to compensate for day/month order inconsistencies in the date field.

4. **Use Service Short Name as Service Name** - Select this option to use short name instead of full name for service complex field.

5. **Additional endpoints to fetch** - This setting contains a list of additional endpoints that are fetched by default.

6. **Specific Fields to Query by Default** - This setting contains a list of fields that are fetched by default. Remove fields to make fetch faster.

7. **Number Of Threads To Run For Fetching** *(default: 1)* - Enter the number of worker threads to perform the query. This can make a fetch faster.

8. **Canonical Software Names** *(optional)* - Enter a list of cannonical software names to use for software normalization. If a software name matches one of the names in the list (case-insensitive), the canonical name will be used.
   * Example: If a software name is `7-Zip 23.01 (x64 edition)` and the list includes the canonical name `7-Zip`, the software name will be shortened to be `7-Zip`.

9. **Custom Parsing** - See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Related Enforcement Actions

* [Ivanti Unified Endpoint Manager (Landesk) - Create or Update Asset](/docs/landesk-create-or-update-asset)