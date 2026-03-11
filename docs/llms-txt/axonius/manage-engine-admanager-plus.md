# Source: https://docs.axonius.com/docs/manage-engine-admanager-plus.md

# ManageEngine ADManager Plus

ManageEngine ADManager Plus is an IT management software suite that offers solutions for IT operations and service management.

### Asset Types Fetched

* Devices, Users, Groups

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Auth Token

### APIs

Axonius uses the [ManageEngine ADManager Plus REST API](https://www.manageengine.com/products/ad-manager/active-directory-api/).

### Permissions

The following permissions are required:

* Read all users

* Read all groups

* Read all devices

#### Supported From Version

Supported from Axonius version 6.1.67

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ManageEngine ADManager Plus server.
2. **Asset Domain** - The domain or domains containing the assets you want to fetch. You can enter multiple domains, entered as a comma-separated list.
3. **Product Name** - The name of the product associated with your Auth Token, for example, "Axonius Adapter Fetch".
4. **AuthToken** - An Authentication Token associated with a user account that has the Required Permissions to fetch assets. For more information, see [How authtoken works in ADManager Plus](https://www.manageengine.com/products/ad-manager/help/help-desk-delegation/authtoken-management-in-admanager-plus.html?lhs).

![ManageEngineAdManagerPlusAddConnection](https://files.readme.io/26be31906e921c4189a1f4091585ed9a4330784b1b8d7c662e94b50674eba01e-image.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).