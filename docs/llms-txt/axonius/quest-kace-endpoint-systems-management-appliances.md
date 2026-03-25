# Source: https://docs.axonius.com/docs/quest-kace-endpoint-systems-management-appliances.md

# Quest KACE Endpoint Systems Management Appliances

Quest KACE Endpoint Systems Management Appliances provision, manage, secure, and service network-connected devices.

### Asset Types Fetched

* Devices, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the following APIs:

* For V12.0 -[KACE Systems Management Appliance 12.0 - API Reference Guide](https://support-public.cfm.quest.com/63445_KACE_SMA_12.0_API_Reference_en-US.pdf).
* For V14.0 -[KACE Systems Management Appliance 14.0 Common Documents - API Reference Guide](https://support.quest.com/technical-documents/kace-systems-management-appliance/14.0%20common%20documents/api-reference-guide/7#TOPIC-2209039)

### Permissions

The value supplied in [User Name and Password](/docs/quest-kace-endpoint-systems-management-appliances#required-parameters) must have read-only permissions in order to fetch assets.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **KACE SMA Domain** - The hostname of the KACE Systems Management Appliance (SMA) server.
2. **User Name** and **Password** - The user name and password for an account that has an assigned role as Read-only administrator.
3. **Quest KACE Version** *(default: V11)* - Select which version of Quest KACE you are using.

<Image alt="Kace" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Kace.png" />

### Optional Parameters

1. **Organization Name** - The organization name. If the KACE Systems Management Appliance (SMA) appliance is configured for multiple organizations, the connection is limited to a single specified organization for the requesting user.
   * If supplied, Axonius will use the specified organization name when connecting to the host defined for this connection and authenticating the API request.
   * If not supplied, Axonius will use the "Default" organization name connecting to the host defined for this connection and authenticating the API request.
2. **Verify SSL** - Select to verify the SSL certificate offered by the host supplied in **KACE SMA Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch drive encryption status for devices** - Select this option to fetch the drive encryption status for all devices, when that information is available.
2. **Fetch machine custom inventory for devices** - Select this option to fetch device information from the machine custom inventory.
3. **Fetch standard software data** - Select this option to fetch only standard software data (without additional fields).  This can help reduce fetch time and avoid memory errors on the appliance.
4. **Fetch Devices From Assets Endpoint** - Enable this option to fetch devices from the Assets endpoint. When this setting is enabled, the following setting may be configured:
   * **Skip Retired Devices From Assets Endpoint** - Select this option to not fetch retired devices from the Assets endpoint.
5. **Custom Parsing** - See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>