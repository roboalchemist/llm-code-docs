# Source: https://docs.axonius.com/docs/azure-deploying-the-adapter.md

# Deploying the Azure Adapter

To deploy the Azure Adapter, perform the following steps:

## 1. Create Azure credentials with the appropriate permissions

<Callout icon="📘" theme="info">
  Note:

  If you already have an Application registered for Axonius, you do not need to create a new one. You can reuse the existing application and add the required additional permissions.
</Callout>

### 1.1 Register the Application in Entra ID

Follow the steps below:

<Accordion title="Prerequisites" icon="fa-info-circle">
  1. Log in to the [Azure Portal](https://portal.azure.com/) with an administrator account.

  2. In the **App registrations** click on **New registration**.

  3. Fill in the details:

     a. Enter the name <code>Axonius App</code> for the application.\
     b. Select <em>Single tenant</em> as the supported account type.

  4. Click <strong>Register</strong> to create the application.

     ![AzureConfig2.png](https://files.readme.io/98b0177ee1747884b8bbd7010c1dcd4f40483fc7ac955e8c07588d210c817655-image.png)

  5. After you have created the app, the *Application (client) ID* and *Directory (tenant) ID* values are displayed. Copy these values to use when you configure the adapter in Axonius.

     ![AzureConfig4.png](https://files.readme.io/70deb8f15407b13ff9103bc8dd512e95a00fc5a20fc79ed0ec4a180fb1ca0b8e-image.png)

  6. **Assign Directory Permissions (Entra ID)**

     a. Go to Microsoft Entra ID and select **Enterprise applications**.\
     b. Select the application you created.\
     c. Navigate to **Roles and administrators**.\
     d. Assign the **Directory Reader** role to the application.
</Accordion>

### 1.2 Authentication Methods

Axonius supports the following authentication methods for connecting to Microsoft Azure adapter:

<Accordion title="Enterprise Application (Client ID / Client Secret)" icon="fa-key">
  1. **Create a Client Secret**

     a. Open the application you registered.\
     b. Within the app registration, navigate to **Certificates & secrets**, then go to **Client secrets** and select **New client secret**.\
     c. Choose an expiration period for the client secret.

     ![AzureConfig3.png](https://files.readme.io/3d856bec0ef3de18058842c2c76575bd48c6c4f02e56300cc1cfb04feb7da7fd-image_2.png)

     d. Click **Add** and copy the **Client Secret Value** to use when you configure the adapter in Axonius. Note that you cannot view it again once you leave the page.

  2. **Assign Required Roles**

     Assign the **Reader** role at either the **Management Group level** (recommended) or the **Subscription level**. Management Group is recommended to prevent blank spots.

     **Option 1: Management Group Level (Recommended)**

     a. Navigate to **Management Groups**.\
     b. Select the Management Group that contains the subscriptions to be scanned.\
     c. Open **Access control (IAM)**.\
     d. Click **Add**, then select **Add role assignment**.

     ![image.png](https://files.readme.io/4d6fe06d7e87552dfbb5ad73ba439e702b0b9a5c03f23a0410045a3e38cc5ce2-image.png)

     e. Assign the **Reader** role to the Enterprise Application.

     **Option 2: Subscription Level**

     a. Navigate to **Subscriptions**.\
     b. Select the subscription to be scanned.\
     c. Open **Access control (IAM)**.\
     d. Click **Add**, then select **Add role assignment**.

     ![image.png](https://files.readme.io/b98c17130ae3b54fe317d8ec045933c5345e43e97c75c361675e3006fc560ae2-image.png)

     e. Assign the **Reader** role to the Enterprise Application.
</Accordion>

<Accordion title="Enterprise Application (Certificate)" icon="fa-certificate">
  1. **Upload a Certificate**

     a. Open the application you registered.\
     b. In the app registration, navigate to **Certificates & secrets**, then go to **Certificates** and select **Upload certificate**.\
     c. Upload your public certificate file (<code>.cer</code>, <code>.pem</code>, or <code>.crt</code>).

     ![image.png](https://files.readme.io/f9beda096feb8120c95f43bd9390ea5e8c70b5a38cea52c3802c688d9abefda2-image.png)

     d. The certificate’s thumbprint will be used as the authentication key for the adapter.

  2. **Assign Required Roles**

     Assign the **Reader** role at either the **Management Group level** (recommended) or the **Subscription level**, depending on your required scope.

     **Option 1: Management Group Level (Recommended)**

     b. Navigate to **Management Groups**.\
     c. Select the Management Group that contains the subscriptions to be scanned.\
     d. Open **Access control (IAM)**.\
     e. Click **Add**, then select **Add role assignment**.

     ![image.png](https://files.readme.io/4d6fe06d7e87552dfbb5ad73ba439e702b0b9a5c03f23a0410045a3e38cc5ce2-image.png)

     f. Assign the **Reader** role to the Enterprise Application.

     **Option 2: Subscription Level**

     a. Navigate to **Subscriptions**.\
     b. Select the subscription to be scanned.\
     c. Open **Access control (IAM)**.\
     d. Click **Add**, then select **Add role assignment**.

     ![image.png](https://files.readme.io/b98c17130ae3b54fe317d8ec045933c5345e43e97c75c361675e3006fc560ae2-image.png)

     e. Assign the **Reader** role to the Enterprise Application.
</Accordion>

### Service-Specific Permissions

<Accordion title="Keys & Certificates from Key Vaults" icon="fa-key">
  To fetch certificates or keys from Key Vaults (optional):

  1. In the Azure Portal search and select **Key Vaults**.

  2. Select the Key Vault you want Axonius to access.

  3. In the Key Vault menu, go to **Access control (IAM)**, click **Add**, and select **Add role assignment**.

     *To assign role:*\
     a. **Certificates:** Select the **Key Vault Certificates Reader** role and assign it to the Enterprise Application created for Axonius.\
     b. **Keys:** Select the **Key Vault Crypto Officer** role and assign it to the Enterprise Application created for Axonius.

  4. Click **Review + assign** to finalize each role assignment.
</Accordion>

## 2. Set up the Azure adapter in Axonius

Create the Adapter connection in Axonius. Based on the authentication method, fill out the specific fields, and configure optional settings.

### Add a New Connection

* Navigate to the **Adapters** page and search for `Azure` then click on the adapter tile.
  ![MicrosoftAzureTile](https://files.readme.io/17741ec06b8230a4b4770a08de59f4adf441090f23729e6ab89b61856dc38d8f-image.png)

* On the top right side, click on **Add Connection**.

* The **Add Connection** drawer opens.

  ![MicrosoftAzureAddConnection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MicrosoftAzureConnection.png)

### Required Fields

* **Azure Client ID** – The Application ID of the Axonius application.
* **Azure Tenant ID** – The ID for Microsoft Entra ID.
* **Connection Label** – Name to identify this adapter connection.
* **Azure Subscription IDs / Fetch All Subscriptions** – Either provide a comma-separated list of subscription IDs or select **Fetch All Subscriptions** to fetch data from all subscriptions in the tenant. One of these options is required.
* **Authentication Methods**

<Tabs>
  <Tab title="Enterprise Application (Client ID / Client Secret)">
    - <strong>Azure Client Secret</strong> – Specify a non-expired key generated from the new client secret.
  </Tab>

  <Tab title="Enterprise Application (Certificate Based)">
    * <strong>Certificate File</strong> – Upload a public certificate used for authentication
      * **Enable Certificate-Based Authentication** - Enable this so that Axonius can use certificate-based authentication on Microsoft required APIs.
      * Click **Upload file** next to **Private Key File** to upload an Azure private key file in PEM format.
      * Click **Upload file** next to **Certificate File** to upload an Azure public key file in PEM format.
  </Tab>

  <Tab title="Managed Identity (Tenant ID)">
    Use this method to run your Axonius instance on Azure virtual machines with managed identities to authenticate without storing client secrets or certificates. To use this method, ensure of the following:

    * Axonius is running on an Azure VM with a managed identity configured.
    * The managed identity has appropriate permissions to access Azure resources and Azure AD.
    * The Azure Tenant ID is configured correctly.

    The required parameters are:

    * **Azure Tenant ID**
    * **Azure Client ID** - Mandatory only if you're using a User-assigned managed identity. If you're using a System-assigned managed identity (Automatically created and tied to the Azure VM), leave this field empty.
  </Tab>
</Tabs>

### Optional Fields

<Accordion title="Expand/Collapse" icon="fa-sliders-h">
  * **Azure Management Group IDs** - Enter the Azure management group IDs associated with the subscriptions you want to fetch data from. The adapter will fetch data only from the subscriptions with the specified management groups.
  * **Cloud Environment** – Select Microsoft Azure cloud environment type.
  * **Azure Stack Hub Management URL** and **Azure Stack Hub Resource String** - Specify the hostname or IP address of the Microsoft Azure Stack Hub server (a Microsoft Azure on-premises server) and the URL for the Azure Stack Hub Resource String.
    * If supplied, Axonius will authenticate to the Microsoft Azure cloud server, and will fetch asset data from the Microsoft Azure Stack Hub server. Axonius will not fetch any asset data from Microsoft Azure cloud server.
    * If not supplied, Axonius will authenticate to the Microsoft Azure cloud server, and will fetch asset data from the Microsoft Azure cloud server. Axonius will not fetch any asset data from Microsoft Azure Stack Hub server.
  * **Azure Stack Hub Proxy Settings** *(default: Do not use proxy)* - Select one of the following proxy options:
    * **Do not use proxy** - Axonius will not use a proxy to authenticate to the Microsoft Azure cloud server and will not use a proxy to fetch asset data from the Microsoft Azure Stack Hub server.
    * **Proxy authentication only** - Axonius will only use the proxy specified in the **HTTPS Proxy** field to authenticate to the Microsoft Azure cloud server.
    * **Proxy Azure Stack Hub only** - Axonius will only use the proxy specified in the **HTTPS Proxy** field to fetch asset data from the Microsoft Azure Stack Hub server.
    * **Proxy all** - Axonius will use the proxy specified in the **HTTPS Proxy** field to authenticate to the Microsoft Azure cloud server and also to fetch asset data from the Microsoft Azure Stack Hub server.
  * **Account Tag** - Tag for the Azure Cloud instance ("nickname").
    * If supplied, Axonius will tag all devices fetched from this adapter connection.
    * If not supplied, Axonius will not tag any of the devices fetched from this adapter connection.
  * **Verify SSL** – Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** – A proxy to use when connecting to the selected Azure cloud environment.
  * **HTTPS Proxy User Name** and **Password** – The user name and password to use when connecting to the selected Microsoft Azure cloud environment via the value supplied in **HTTPS Proxy**.
  * **Enable Client Side Certificate** – Use certificate-based authentication instead of a client secret.
    * **Client Private Key File** – Upload the private key (.pem) used for certificate-based authentication.
    * **Client Certificate File (.pem)** – Upload the public certificate file (.pem) used for certificate-based authentication.
  * **Notes** – Add a note of up to 250 characters for this adapter connection.
  * **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network. To use this option, you need to set up an Axonius Gateway.
</Accordion>

## 3. (Optional) Configure Advanced Settings

Refer to Azure [Advanced Settings](https://docs.axonius.com/v1.0_Tudip_Project_branch/docs/azure-advance-settings).