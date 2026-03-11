# Source: https://docs.axonius.com/docs/ibm-tivoli-taddm.md

# IBM Tivoli Application Dependency Discovery Manager (TADDM)

IBM Tivoli Application Dependency Discovery Manager (TADDM) is a configuration management tool that helps IT operations personnel ensure and improve application availability in application environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host Address** *(required)* - The hostname or IP address of the IBM Tivoli Application Dependency Discovery Manager (TADDM) server.
2. **Username** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="IBM Tivoli TADDM.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IBM%20Tivoli%20TADDM.png" />

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.

To create a read-only user through the IBM Tivoli TADDM portal:

1. Sign in as an administrator to the data management portal of IBM Tivoli TADDM, then go to **Administration** -> **Roles**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(132\).png)
2. Click **Create Role**, and select the **Read** permissions.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(133\).png)
3. Go to **Administration** -> **Users**. Click **Create User**. Create a new user and select the role you just created. Select **DefaultAccessCollection**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(134\).png)