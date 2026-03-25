# Source: https://docs.axonius.com/docs/stackrox.md

# StackRox

StackRox is a container security platform that protects cloud-based applications, detects threats, and manages vulnerabilities, compliance requirements, and configurations.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Software, SaaS Applications, Compute Services, Containers, Alerts/Findings, Compute Images

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the StackRox server.
2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="stackrox" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-41154CYJ.png" />

## APIs

Axonius uses the StackRox Security Platform API.

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config

To fetch specific assets from specific endpoints, enable the following options:

* **Fetch Devices from Nodes**
* **Fetch ComputeServices from Clusters** - When enabled, the following options become available:
  * **Enrich Clusters with Nodes**
  * **Enrich Clusters with Namespaces**
  * **Enrich Clusters with Deployment Details** - When enabled, the following option becomes available:
    * **Enrich Deployment Details with Cluster: Image Details**

#### Deployments - applies context on the following endpoints: Deployment Details

To configure additional settings for the Deployment Details endpoint, enable the following options:

* **Keep only latest created deployments** - Select to fetch only the latest deployment per namespace. If this is unselected, the system might display multiple deployments with different dates per namespace.
* **Fetch Containers of sub type pod from Pods**
* **Fetch Containers of sub type container from Containers** - When enabled, the following option becomes available:
  * **Enrich Containers with Container: Image Details**

#### Deployments - applies context on the following endpoints: Containers

To configure additional settings for the Containers endpoint, enable the following options:

* **Keep only latest created deployments** - Select to fetch only the latest deployment per namespace. If this is unselected, the system might display multiple deployments with different dates per namespace.
* **Fetch ComputeImage from Cluster: Image Details**
* **Fetch AlertFindings from Alerts**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.0