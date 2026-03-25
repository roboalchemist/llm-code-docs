# Source: https://docs.axonius.com/docs/red-hat-satellite.md

# Red Hat Satellite

Red Hat Satellite is a system management solution used to deploy, configure, and maintain systems across physical, virtual, and cloud environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* Software
* SaaS Applications

## Parameters

1. **Red Hat Satellite/Capsule Domain** *(required)* - The hostname or IP address of the Red Hat Satellite server that  Axonius can communicate with via the [Required Ports](#required-ports).
2. **User Name** and **Password** *(required)* - The credentials for a user account that has  Permissions to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Red Hat Satellite/Capsule Domain**. For more details, see [SSL Trust & CA Settings](/docs/global-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Red Hat Satellite/Capsule Domain**.

To learn more about the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Red Hat Satellite.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Red%20Hat%20Satellite.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch host facts** *(required, default: true)* - Select whether to fetch facts for every host.

2. **Fetch host packages** *(required, default: true)* - Select whether to fetch installed software for connected devices.

3. **Fetch host errata** - Select whether to fetch errata information (including vulnerable\_software and Red Hat Errata information) for connected devices.

4. **Host chunk size** *(required, default: 200)* - The number of hosts returned every fetch.

5. **Number of requests to perform in parallel** *(required, default: 50)* - Set the number of requests to perform in parallel.

6. **Fetch host subscriptions** - Select whether to fetch the subscriptions fields from Red Hat Satellite.

7. **Fetch host collections** - Select whether to fetch the host collections fields from Red Hat Satellite.

8. **Parse bridge interfaces as container interfaces** - Select this option to parse the docker IP addresses into   specific fields rather than the regular NICs.

9. **Serial number source priority** - Select which serial number type is parsed as the ‘Device Manufacturer Serial’: 'Chassis Serial (default)' or 'System Serial'.

## APIs

Axonius uses the [Red Hat Satellite API](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.8/html/api_guide/index).

## Required Ports

Axonius must be able to communicate with the value supplied in [Red Hat Satellite/Capsule Domain](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [User Name](#parameters):

* Must be a local user. Only local users can have API access.
* Must have view\_hosts permission.
* Must be assigned the proper organizations and locations.
* If you select  `Fetch host facts`,  view\_facts permission is required.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions.  Contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed which is not functioning as expected.

| Version                          | Supported | Notes  |
| -------------------------------- | --------- | ------ |
| Red Hat Satellite 6.6 and higher | Yes       | API v2 |
| Red Hat Satellite 6.8            | Yes       |        |