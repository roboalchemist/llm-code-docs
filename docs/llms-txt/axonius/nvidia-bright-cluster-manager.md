# Source: https://docs.axonius.com/docs/nvidia-bright-cluster-manager.md

# NVIDIA Bright Cluster Manager

NVIDIA Bright Cluster Manager is a system management tool that provides centralized provisioning, monitoring, and administration of high-performance computing clusters across on-premises and hybrid environments.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name / Password
* Certificate File / Certificate Key File

### APIs

Axonius uses the [NVIDIA Bright Cluster Manager 9.2 Docs](https://docs.nvidia.com/bright-cluster-manager/latest-release/index.html).

### Permissions

To interact with the Bright Cluster Manager REST API (e.g., `/rest/v1/device`), the user account or certificate used for authentication must have sufficient privileges within the Bright Cluster Manager environment. Specifically, the account must have permissions to:

* Access CMDaemon’s REST interface.
* View cluster and node/device-level information such as hostname, IP, MAC address, network roles, and node type.
* If the account is restricted via Bright's internal role-based access or certificate-based access controls, API requests may:
  * Return only partial data (e.g., limited device fields) or
  * Be denied entirely.

#### Supported From Version

Supported from Axonius version 7.0.9

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the NVIDIA Bright Cluster Manager server.
2. **Authentication Method** *(default: Certificate-Based Auth)* - Select the authentication method, either **Certificate-Based Auth** or **Basic Auth (Username and Password)**.
   * **Certificate-Based Auth**:
     * **Certificate File (.pem)** - Upload the certificate file containing the public key for the keypair being used to authenticate.
     * **Certificate Key File (.key)** - Upload the certificate key file for the certificate being used to authenticate.
   * **Basic Auth (Username and Password)**:
     * **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.

![NVIDIABrightClusterManager.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NVIDIABrightClusterManager.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).