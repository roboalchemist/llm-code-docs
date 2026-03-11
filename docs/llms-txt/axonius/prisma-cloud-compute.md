# Source: https://docs.axonius.com/docs/prisma-cloud-compute.md

# Palo Alto Networks Prisma Cloud Workload Protection

Prisma Cloud Workload Protection (CWPP) provides protection across hosts, containers, and serverless deployments in any cloud, throughout the application lifecycle.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Software, SaaS Applications, Containers, Compute Images

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Prisma Cloud Access Key ID / Prisma Cloud Secret Key

### APIs

Axonius uses the [CWPP API](https://prisma.pan.dev/api/cloud/cwpp).

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 4.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The full URL of the CWPP server.
2. **API Version** *(default: 32.07)* - Enter the CWPP version that you're running.
   To find your version, see [How to Find Your Version](https://prisma.pan.dev/api/cloud/cwpp/#how-to-find-your-version).
3. **Prisma Cloud Access Key ID** and **Prisma Cloud Secret Key** - The credentials for a user account that has permissions to fetch assets.

<Image alt="Palo Alto Networks Prisma Cloud Workload Protect" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Palo%20Alto%20Networks%20Prisma%20Cloud%20Workload%20Protect.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch containers as Devices** - Select this option to fetch software containers as devices.
2. **Fill vulnerabilities for containers** - Select this option to include vulnerability data for container devices.
3. **Fetch Container Image Information** - Select this option to fetch image information for containers.
4. **Fetch Container Images as Devices** - Select this option to create devices from images.
5. **Fetch Container Images as Compute Images** - Select this option to fetch Container Images as Compute Images.
6. **Fetch Registry Image Scan Reports** - Select this option to fetch reports listed under **Monitor** `>` **Compliance** `>` **Images** `>` **Registries** in the Prisma UI.
7. **Parse hostname from cloudMetadata** - Select this option to parse the device's hostname from the cloud metadata.
8. **Trim UUID from hostname** - Select this option to remove UUID from hostname.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>