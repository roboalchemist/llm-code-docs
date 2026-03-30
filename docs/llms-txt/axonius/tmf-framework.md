# Source: https://docs.axonius.com/docs/tmf-framework.md

# Amdocs TMF639 Inventory

TMF Framework is a tool that provides a standardized approach to managing telecommunications services and operations.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the Amdocs Resource Inventory REST API.

### Permissions

The following permissions are required:

* **Read Access**: The account needs read permissions for inventory, resource, device, application, logicalResource, and physicalResource.

* **Endpoint Access**: Specific read access is needed for the following API endpoints:
  * `/resourceInventoryManagement/v4/resource`
  * `/resourceInventoryManagement/v4/logicalResource`
  * `/resourceInventoryManagement/v4/physicalResource`

**Additional Permissions**

To fetch devices, VMs, and business applications, the account also requires these read permissions:

* `physicalResource:read`
* `logicalResource:read`
* `device:physical:read`
* `device:virtual:read`
* `application:read`
* `service:read`

#### Supported From Version

Supported from Axonius version 7.0.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Amdocs TMF639 Inventory server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

<Image align="center" border={false} width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/amdocs_metf_add%20connaction.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **API Gateway Connection** - Enable this to use API gateway parameters for authentication. After enabling this option, under **API Gateway Type**, choose **Layer7** and fill in the parameters that are displayed (in addition to **Host Name or IP Address**). Read about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).