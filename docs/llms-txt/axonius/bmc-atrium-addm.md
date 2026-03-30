# Source: https://docs.axonius.com/docs/bmc-atrium-addm.md

# BMC Atrium ADDM

BMC Atrium ADDM is a digital enterprise management solution that automates application discovery and dependency mapping.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BMC Atrium ADDM server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Token** *(required)* - A token used for “API Access”.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![BMC Atrium ADDM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BMC%20Atrium%20ADDM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch installed software** *(required, default: Disabled)* - From the dropdown, select how to fetch installed software data for fetched devices (either 'Disabled', 'Enabled in Normal Fetch', or 'Enabled in Background').
2. **Fetch info fields from RuntimeEnvironment table** - Select this option to fetch devices with info from the RuntimeEnvironment table. If enabled, this setting will add the following fields: BMC Name, Command, OS Class, OS Type, Full Version, and Device Type.
3. **Additional fields for query** *(optional)*

<Callout icon="📘" theme="info">
  Note

  Only use this setting after guidance from Axonius Support.
</Callout>

Use this option to modify the query by adding additional SHOW directives to the SEARCH Host    query. Parameters should be formatted according to the [BMC Discovery (ADDM) query  language](https://docs.bmc.com/docs/discovery/221/the-show-clause-1051985722.html).

3. **Async chunks in parallel** *(required, default: 20)* - Specify the number of parallel requests all connections for this adapter will send to the BMC Atrium ADDM server in parallel at any given point.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BMC Discovery API](https://docs.bmc.com/docs/discovery/113/endpoints-in-the-rest-api-946702524.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**: SOAP API

## Required Permissions

The value supplied in [API Token](#parameters) must be associated to a user who must be member of the following groups: (or equivalent)

* api-access- baseline for any API access
* read-only minimal access to system resources.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version            | Supported | Notes |
| ------------------ | --------- | ----- |
| BMC Discovery v1.1 | Yes       |       |