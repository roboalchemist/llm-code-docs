# Source: https://docs.axonius.com/docs/proofpoint.md

# Proofpoint

Proofpoint is a cybersecurity company that offers solutions to protect workers and their data from threats targeting email, mobile, social, cloud, and other digital channels.

## Asset Types Fetched

* Users, Application Settings

## Before You Begin

### APIs

Axonius uses the [Proofpoint Essentials Rest API](https://us1.proofpointessentials.com/api/v1/docs/index.php).

### Permissions

The value supplied as **User Name** must be part of the Proofpoint Organization Admin role or above to access the fetched data.

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The Base URL of the stack of the domain you are working with.
   * Example for US1: [https://us1.proofpointessentials.com](https://us1.proofpointessentials.com)
   * Example for US5: [https://us5.proofpointessentials.com](https://us5.proofpointessentials.com)

2. **User Name** and **Password** - The credentials for a user account that has the [required permissions](#permissions) to fetch assets.

3. **Organization Domain** - Specify the domain the data will be fetched for. For example: `mycompany.com`

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/proofpoint_connect.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch inactive users** - Select to fetch inactive users.
2. **Fetch settings** - Select to fetch application settings.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>