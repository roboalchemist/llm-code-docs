# Source: https://docs.axonius.com/docs/qualys-container-security.md

# Qualys Container Security

Qualys Container Security provides the ability to discover, track, and secure containers.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications, Containers, Compute Images

## Before You Begin

### APIs

Axonius uses the [Qualys Container Security APIs](https://docs.qualys.com/en/cs/api/#t=get_started%2Fget_started.htm).

#### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Qualys Container Security server.
2. **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.

<Image alt="Qualys Container Security connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/QualysContainerSecurity_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks to fetch concurrently** *(optional, default: 50)* - In order to fetch container vulnerabilities in chunks, enter the amount to be fetched at one time.
2. **Only fetch containers that have been updated in the last X days (0: All)** *(optional, default: 0)* - Enter a number of days to fetch only containers that have been updated in Qualys Container Security in the last specified number of days. If you do not provide a number, the adapter fetches all containers.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>