# Source: https://docs.axonius.com/docs/sysdig-secure.md

# Sysdig - Secure

Sysdig is a monitoring, troubleshooting, cost-optimization, and alerting suite for containers, cloud, and Kubernetes environments.

### Asset Types Fetched

* Devices, Vulnerabilities, Users, Software, SaaS Applications, Compute Services, Containers

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Token

### APIs

Axonius uses the Sysdig Secure API.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 6.1.27.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://app.sysdigcloud.com`)* - The hostname or IP address of the Sysdig Secure server.

2. **Token** - The credentials for a user account that has permission to fetch assets.

3. **Client Type** - Select the type of client.

<Image alt="Sysdig Secure" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sysdig%20Secure.png" />

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

1. **Fetch Devices of sub type host from Inventory Hosts Endpoint** - Enable to fetch Hosts (Devices) from the Inventory Hosts endpoint. When this is enabled, the following setting also becomes available:
   * **Inventory Host Fields** - Select the fields you want to add to Hosts (Devices) assets.
2. **Fetch Devices of sub type workflow\_host from Workflows Hosts** - Enable to fetch Hosts from the Workflow Hosts endpoint. When this is enabled, the following setting also becomes available:
   * **Enrich Workflows Hosts with Result Details Endpoint** - Enable to add vulnerability information to Workflow Hosts.
   * **Enrich Workflows Hosts Endpoint with List Container Results Endpoint** - Enable to add container vulnerability information to Workflow Hosts. When this is enabled, the following setting also becomes available:
     * **Enrich List Container Results Endpoint with Get Container Details Endpoint** - Enable to enrich each container (listed in the previous setting) with its details.
3. **Fetch ComputeServices of sub type namespace from Namespaces Endpoint** - Enable to fetch Namespaces (Compute Services) from the Namespaces endpoint. When this is enabled, the following settings also become available:
   * **Inventory Namespace Fields** - Select the fields you want to add to Namespaces (Compute Services).
   * **Enrich Namespaces Endpoint with Results Endpoint** - Enable to add vulnerability information to Namespaces (Compute Services).
   * **Enrich Results Endpoint with Result Details Endpoint** - Enable to fetch Vulnerabilities for Compute Services (Containers). This setting is required in addition to **Enrich Namespaces Endpoint with Results Endpoint** in order to fetch Vulnerabilities for Containers fetched from the Namespaces endpoint.
4. **Fetch ComputeServices of sub type workflow\_container from Workflows Containers** - Enable to fetch Containers (Compute Services) from the Containers endpoint.  When this is enabled, the following setting also becomes available:
   * **Enrich Workflows Containers with Result Details Endpoint** - Enable to add vulnerability information to Containers (Compute Services).
5. **Fetch Users from User Details Endpoint** - Enable this option to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>