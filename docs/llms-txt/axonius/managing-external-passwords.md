# Source: https://docs.axonius.com/docs/managing-external-passwords.md

# Managing External Passwords

## Enterprise Password Management Settings

Axonius allows you to configure a range of external password managers to securely pull privileged credentials from the password manager defined.

Configuring a password manager enables you to manage the passwords used for adapters and enforcement actions using the password manager configured. When you enable and configure a password manager, this does not make any immediate change to your configured adapters or Enforcement Actions. An icon is displayed in the credential fields of the adapters or Enforcement Actions so that users can enter credentials using the password manager according to their company guidelines.

**To enable password managers:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Access Management**, and select **External Password Managers**. A toggle for enabling Password Manager integration is displayed (see below), with a list of Password Managers that can be enabled, together with their credentials.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnterprisePasswordManagementSettings\(1\).png)
3. Toggle on **Use Password Manager**.
4. Toggle on each password manager you want to use. You can enable more than one password manager.

These password managers are available:

* [1Password Connect Server](/docs/managing-external-passwords#1password-connect-server)
* [Akeyless Vault](/docs/managing-external-passwords#akeyless-vault)
* [AWS Secrets Manager](/docs/managing-external-passwords#aws-secrets-manager)
* [Azure Key Vault](/docs/managing-external-passwords#azure-key-vault)
* [BeyondTrust Privileged Identity](/docs/managing-external-passwords#beyondtrust-privileged-identity)
* [BeyondTrust Password Safe](/docs/managing-external-passwords#beyondtrust-password-safe)
* [Bitwarden Vault](/docs/managing-external-passwords#bitwarden-vault)
* [Click Studios Passwordstate](/docs/managing-external-passwords#click-studios-passwordstate)
* [CyberArk Vault](/docs/managing-external-passwords#cyberark-vault)
* [CyberArk Privilege Cloud Vault](/docs/managing-external-passwords#cyberark-privilege-cloud-vault)
* [Delinea Secret Server](/docs/managing-external-passwords#delinea-secret-server)
* [GCP Secret Manager](/docs/managing-external-passwords#gcp-secrets-manager)
* [HashiCorp Vault](/docs/managing-external-passwords#hashicorp-vault)
* [Keeper Secrets Manager](/docs/managing-external-passwords#keeper-secrets-manager)
* [ManageEngine Password Manager Pro Vault](/docs/managing-external-passwords#manageengine-password-manager-pro-vault)
* [ManageEngine PAM360 Vault](/docs/managing-external-passwords#manageengine-pam360-vault)

When you choose more than one password manager, the system lets you choose which password manager to use in the password field.

<Image alt="ChooseMultiplePAss.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChooseMultiplePAss(1).png" />

### 1Password Connect Server

<Image alt="1PasswordConnectServer" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/1PasswordConnectServer.png" />

Axonius pulls credentials from 1Password Connect Server. Follow [1Password Connect Server  integration](/docs/1password-connect-server) configuration guidelines.

**To use 1Password Connect Server**

1. Toggle on **1Password Connect Server**.
2. Specify the following parameters:
   * **1Password Connect Server URL** *(required)* - The URL of 1Password Connect Server.
   * **Port** *(required, default 8080)* - The port that 1Password Connect Server listens to.
   * **API Token** *(required* - The AUTH token needed to authenticate the 1Password Connect Server request. Create the server and API key, as described in [Deployment](https://developer.1password.com/docs/connect/get-started#deployment). Make sure to copy down this key and store it in a secure location for your future reference.

### Akeyless Vault

<Image alt="PasswordManageAKeyLessVault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManageAKeyLessVault.png" />

**To use Akeyless Vault**
Axonius pulls credentials from Akeyless Vault. Follow [Akeyless  Vault](/docs/akeyless-vault-integration) configuration guidelines.

1. Toggle on **Akeyless Vault**.
2. Specify the following parameters:
   **Akeyless Domain** (required) - The URL or IP address of the Akeyless Vault server.
   **Port** (optional) - The port that the Akeyless Vault listens to 8080/443.
   **Akeyless Access ID** (required) - An ID for Akeyless
   **Akeyless Access key** (required) - The key used to unseal the vault.
   Refer to [Akeyless API Key](https://docs.akeyless.io/docs/api-key) for details on how to generate the Access ID and Key
   **Gateway Name** - Select the gateway through which to connect to the Akeyless Vault  if required.

### AWS Secrets Manager

<Image align="center" border={false} width="600px" src="https://files.readme.io/d0fcb2902bb4bd10d9f291dae778e8db5a0ccfc2fe94ca28ce79a5a09a63c096-image.png" />

<br />

**To use AWS Secrets Manager**

1. Toggle on **AWS Secrets Manager**.
2. Specify the following parameters to fetch secrets from AWS Secrets Manager:
   * **Instance profile** *(optional)* - Check this to authenticate with the role assigned to the Axonius Instance installed on your EC2 instance. When you authenticate with an instance profile, the **Access Key ID** and **Access Key Secret** parameters are **not** required, and if you populate them, they will be ignored.
   * **Region** *(required)* - Specify the region name for a specific region.
   * **Access Key ID** *(required if **Instance profile** is unchecked)* - Provide AWS Access Key ID.
   * **Access Key Secret** *(required if **Instance profile** is unchecked)* - Provide AWS Access Key Secret.
   * **Role to assume** *(optional)* - Provide an ARN role that points to a specific IAM role in AWS, which has its own set of permissions defined in its IAM policy. If you select Instance profile, then role to assume is not used. Click **Upload File** to upload a .json file containing the role.The role should be in the following format:

     ```json
     [
       {
         "arn": "{arn_value}",
       }
     ]
     ```

* To fetch secrets from AWS Secrets Manager, you must have the following permissions:
  * secretsmanager:GetSecretValue
  * kms:Decrypt - required only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.

For more details about **AWS Secrets Manager** configuration and guidelines, see [AWS Secrets Manager Integration](/docs/aws-secrets-manager-integration).

### Azure Key Vault

<Image alt="PasswordManagerAzureKeyVault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerAzureKeyVault.png" />

**To use Azure Key Vault**
Axonius pulls credentials from Azure Key Vault. Follow [Azure Key  Vault](/docs/azure-key-vault) configuration guidelines,

1. Toggle on **Azure Key Vault**.
2. Specify the following parameters:
   * **Client ID** (required) -   The Application ID of the Axonius application.
   * **Client Secret** (required) - Specify a non-expired key generated from the new client secret.
   * **Tenant ID** (required) - Microsoft Azure Tenant ID.
   * **Gateway Name** *(optional)* - Select the gateway through which to connect to the Azure Key Vault if required.

### BeyondTrust Privileged Identity

<Image alt="PasswordManagerBeyondTrustPrivilegedIdentity" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerBeyondTrustPrivilegedIdentity.png" />

**To use BeyondTrust Privileged Identity**
Axonius pulls credentials from BeyondTrust Privileged Identity.

1. Toggle on **BeyondTrust Privileged Identity**.
2. Specify the following parameters:
   * **Hostname or IP address** (required) -   The hostname or IP address of the BeyondTrust Privileged Identity server.
   * **Login type** (required) - The login type of the authentication. Valid values:
     NativeStaticAccount (Privileged Identity explicit accounts) or FullyQualifiedAccount.
   * **Username** and **Password** (required) - The credentials for the user account

### BeyondTrust Password Safe

<Image alt="BeyondTrustPasswordSafe(2)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustPasswordSafe(2).png" />

Axonius pulls credentials from BeyondTrust Password Safe.

**To use BeyondTrust Password Safe**

1. Toggle on **BeyondTrust Password Safe**.
2. Follow [BeyondTrust Password Safe ](/docs/beyondtrust-password-safe-integration) configuration guidelines, and specify the following parameters:
   * **BeyondTrust Domain** (required) -   The hostname or IP address of the BeyondTrust Password Safe server.
   * **API Token** (required) - The API key configured in BeyondInsight for the application.
   * **Username** - The username of a BeyondInsight user who has been granted permission to use the API key.
   * **Password** - The relevant password.
   * **Gateway Name** *(optional)* - Select the gateway through which to connect to the BeyondTrust Password Safe Password Manager if required.

### Bitwarden Vault

<Image align="center" alt="image.png" border={false} width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-6WNNOFOH.png" />

**To use Bitwarden Vault**

1. Toggle on **Bitwarden Vault**.
2. Follow the [Bitwarden Vault integration guidelines](/docs/bitwarden-vault-integration), and specify the following parameters - all required unless noted otherwise:

   * **Domain for API calls** - The domain where the “get vault” request will be sent to.
   * **Domain for authentication** - The domain in which to authenticate and get a token. The default value is `https://identity.bitwarden.com`.
   * **Client ID** and **Client Key** - to get these, from your Bitwarden account, navigate to **Security**, select the **Keys** tab, and then click **View API key**. The account you use must be an organization account and not a personal account, as the **Client ID** must start with the word “organization”, for example: `organization.32242dc3-2402-34a6-97b0-b26700ccb8f2`.
   * **Verify SSL** *(default: false)* - Select whether to verify the SSL certificate offered by the value supplied in Delinea Secret Server URL. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * **Master Password** - The password used to log into your Bitwarden account.
   * **Gateway Name** *(optional)* - Select the gateway through which to connect to the Bitwarden Vault if required.

   ### Click Studios Passwordstate

<Image alt="PasswordManagerClickStudiosPasswordstate" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerClickStudiosPasswordstate.png" />

**To use Click Studios Passwordstate**
Axonius pulls credentials from Click Studios Passwordstate. Follow [Click Studios Passwordstate](/docs/click-studios-passwordstate) configuration guidelines,

1. Toggle on **Click Studios Passwordstate**.
2. Specify the following parameters:
   * **PasswordState Domain** (required) - The domain for the PasswordState password manager.

   * **API Key** (required) -  The key needed to authenticate the PasswordState request. Get the API Key by generating an API Key for the password list on Passwordstate. If you are using more than one password list, you should generate a 'System Wide API Key'.

   * **Gateway Name** - Select the gateway through which to connect to the Click Studios Passwordstate Password Manager if required.

### CyberArk Vault

<Image alt="PasswordManagerCyberArkVault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerCyberArkVault.png" />

**To use CyberArk Vault**
Axonius uses CyberArk’s Application Access Manager (AAM) to pull credentials from CyberArk Vault.

1. Toggle on **CyberArk Vault**
2. Follow [CyberArk integration](/docs/cyberark-integration-1) configuration guidelines, and specify the following parameters:

   * **CyberArk Domain** *(required)* - The base URL of the Central Credential Provider (CCP).
   * **Port** *(required)* - The port the Central Credential Provider (CCP) is listening to.
   * **Application ID** *(required)* - The Application ID which identifies the Axonius application created in CyberArk.
   * **Certificate key (PEM format)** *(optional)* - The certificate (PEM format) which will be authenticated against the Certificate Serial Number defined on the Application.
     * **Certificate Key:** You need to upload the unencrypted Private Key + Certificate bundle.
     * To do this `cat private.key cert.pem > cyberarkcert.pem`.
     * Click **Upload File** to upload it the generated cyberarkcert.pem file.
     * If you open the file in a text editor, it should begin with "PRIVATE KEY" and also have a "BEGIN CERTIFICATE" section below.
     * Note that the Private Key can't be password encrypted.
   * **API Prefix** -  Select the API Prefix that is accessible to your CyberArk Vault service. The following options are available:
     * AIMWebService
     * AIMWebServiceCert
     * AIMWebServiceIP
   * **Gateway Name** - Select the gateway through which to connect to the CyberArk Vault if required.
   * **HTTP Proxy**   - Connect CyberArk Vault to a proxy instead of directly connecting it to the domain.
   * **HTTPS Proxy**   - Connect CyberArk Vault to a proxy instead of directly connecting it to the domain.
   * **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS or HTTP Proxy**.
   * **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS or HTTP Proxy**.

### CyberArk Privilege Cloud Vault

You can add multiple domains (tenants) of the CyberArk Privilege Cloud to the external password manager. When setting up an Adapter, you can choose which domain you want to use.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArkPrivCloudVault.png)

**To use CyberArk Privilege Cloud Vault**

1. Toggle on **CyberArk Privilege Cloud Vault**.
2. Follow [CyberArk Privilege Cloud integration](/docs/cyberark-privilege-cloud-vault) configuration guidelines, and specify the following parameters:

   * **CyberArk Privilege Cloud domain** *(required)* - The base URL of the Central Credential Provider (CCP).
   * **Authentication Method** *(required; default: CyberArk)* - The authentication method used for the connection. The following authentication methods are supported: **CyberArk**, **Windows**, **LDAP**, **Radius**, **SAML**, and **OAuth2**.
   * **Username** and **Password** *(required; optional for SAML authentication)* - The credentials for a CyberArk Privilege Cloud user account that has the [Required Permissions](#required-permissions) to fetch assets.
   * **Tenant ID - Cloud Only** *(optional)* - Tenant ID required for **OAuth2** authentication method. The OAuth2 method only works with the cloud version.
   * **SAML Response** *(optional)* - Required for the **SAML** authentication method.
   * **Gateway Name** *(optional)* - Select the gateway through which to connect to the CyberArk Privilege Cloud Vault if required.
3. If you want to add a domain (tenant), click **+ Add New CyberArk Privilege Cloud domain**. Configure the **CyberArk Privilege Cloud** fields that open for the new domain as described in step 2.

#### APIs

Axonius uses the [CyberArk REST API](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.1/en/Content/WebServices/API%20Commands.htm).

To use the SAML authentication method you need to enable the SAML IdP initiated SSO flow. Follow instructions in [Configure the IdP](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.1/en/Content/PAS%20INST/SAML-Authentication.htm#!#Configur) to implement this. This returns the SAML Response.

#### Required Permissions

The value supplied in **User Name** must have **Audit users** permission.

The Client ID/Secret permissions must be updated to match the [Create a Service user for API requests](https://docs.cyberark.com/privilege-cloud-shared-services/Latest/en/Content/ISPSS/ISPSS-API-Authentication.htm#Step1CreateaServiceuserforAPIrequests) section.

The following permissions are only relevant if you are using the OAuth2 authentication (i.e., with the cloud version):

You must update the domain to be `.privilegecloud.cyberark.cloud`.

Example: `https://ihg.privilegecloud.cyberark.cloud`

### Delinea Secret Server

<Image alt="DelineaSecretServer" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DelineaSecretSErver.png" />

**To use Delinea Secret Server:**
Follow [Delinea Integration](/docs/thycotic-integration) configuration guidelines.

1. Toggle on **Delinea Secret Server**.
2. Specify the following parameters:

   * **Delinea Secret Server URL** *(required)*
     * **On-premise** - Use the format: https\://*\<hostname>*/SecretServer (for example: `https://demo-server/SecretServer`
     * **Cloud** - Use the format: https\://*\<tenant>*.secretservercloud.com (for example: `https://mycompany.secretservercloud.com`
   * **User name** and **Password** (required) - The credentials of a local Delinea user. The required permissions depend on the state of the 'hide launcher password' security setting.
     * If 'hide launcher password' is activated, the user must be an Owner or Editor of the secret to access the real password and properly populate the vault with secrets. Otherwise, the password will display as **\* Not Valid For Display** \*.
     * If the setting is not activated, a User with Viewer (read-only) permission is sufficient.

<Callout icon="📘" theme="info">
  Note

  If **Use Oauth2** is enabled, enter **client\_id** under **User name** and **client\_secret** under **Password**
</Callout>

* **Port** *(optional, default: 443)* - If specified, this port will be used for the connection. Otherwise, the system defaults to **443** for https URLs or if http/https not supplied in URL, and **80** for http URL.
  * **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate offered by the value supplied in **Delinea Secret Server URL**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
  * **API Version** (default: V10) - Select the API version to use.
  * **Use Oauth2** - This option is relevant for API V10. Enable this option to use the Delinea Secret Server OAuth 2.0 endpoints for authentication instead of a username and password. When enabled, enter your **client\_id** and **client\_secret** in the respective **User name**  under **Password** fields.
  * **Certificate File** - Upload a certificate file, if needed.
  * **Gateway Name** - Select the gateway through which to connect to the Thycotic Secret Server Vault if required.

### GCP Secrets Manager

<Image alt="GCPSecretManager" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPSecretManager.png" />

**To use GCP Secret Manager**

1. Toggle on **GCP Secret Manager**.
2. Configure a connection of [Axonius to Google Cloud Platform](/docs/google-cloud-platform-gcp#connect-axonius-to-google-cloud-platform).
3. To fetch secrets from GCP Secrets Manager, you must have the following permissions:
   Add to the relevant IAM Principal the following role: Secret Manager Secret Accessor.
4. Specify the following parameters to fetch secrets from GCP Secrets Manager:
   * **JSON Key Pair** *(required)* - A JSON-document containing service-account credentials for GCP. Refer to [ Connect Axonius to Google Cloud Platform](/docs/google-cloud-platform-gcp#2-create-a-service-account-and-grant-permissions-to-that-service-account).

Refer to [GCP Secret Manager](/docs/gcp-secret-manager) for further information

### HashiCorp Vault

<Image alt="PasswordManagerHashiCorpVault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerHashiCorpVault.png" />

**To use HashiCorp Vault**
Axonius  pulls credentials from HashiCorp Vault.  Follow [HashiCorp Vault  integration](/docs/hashicorp-vault) configuration guidelines.

1. Toggle on **HashiCorp Vault**.
2. Specify the following parameters:
   * **HashiCorp Vault Domain** *(required)* - The URL or IP address of the HashiCorp Vault server.
   * **Secrets Engine** *(required, default Cubbyhole)* - Set the secrets engine, either KV Version 1, KV Version 2, Cubbyhole, or Active Directory.
   * **Port** *(required, default 8200)* - The port the HashiCorp Vault listens to.
   * **Token** *(optional)* - The token for authentication.
   * **Unseal key** *(optional)* - The key used to unseal the vault.
   * **Role ID**  and **Role secret ID** *(optional)* - Use these settings  to authenticate using AppRole.
     * Refer to [Get RoleID and SecretID](https://developer.hashicorp.com/vault/tutorials/auth-methods/approle#step-3-get-roleid-and-secretid) for information on retrieving the Role ID
     * Enter the parameters as defined in the AppRole the user defined.   Refer to Step 1 and Step 2 in [AppRole Pull Authentication](https://developer.hashicorp.com/vault/tutorials/auth-methods/approle#step-1-enable-approle-auth-method). Modify policies according to the secrets you want   this AppRole to access.
   * **Namespace** *(optional)* - Enter a customized namespace to fetch secrets from, if it is configured.
   * **Gateway Name** *(optional)* - Select the gateway through which to connect to the HashiCorp Vault if required.

### Keeper Secrets Manager

<Image align="center" alt="KeeperSecretsManager" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/KeeperSecretsManager.png" />

**To use Keeper Secrets Manager:**
Follow [Keeper Secrets Manager Integration](/docs/keeper-secrets-manager-integration) configuration guidelines,

1. Toggle on **Keeper Secrets Manager**.
2. Specify the following parameters:

   * **Hostname**   -   The destination host where your Enterprise tenant is located: by default this is keepersecurity.com
   * **Client ID** -  The hashed clientKey where clientKey is the Unique Client Device Identifier
   * **Private Key**  Client Device Private Key
   * **Server Public Key ID**  - Keeper Infrastructure's Public Key ID
   * **App Key** -  Application Private Key
   * **App Owner Public Key** -  Application Owner's Public Key
   * **Gateway Name** - Select the gateway through which to connect to the Keeper Secrets Manager if required.

### ManageEngine Password Manager Pro Vault

<Image alt="ManageEnginePasswordManagerProVault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEnginePasswordManagerProVault.png" />

Axonius pulls credentials from ManageEngine Password Manager Pro Vault. Follow [ManageEngine Password Manager Pro Vault  integration](/docs/manageengine-password-manager-pro-vault) configuration guidelines.

**To use ManageEngine Password Manager Pro Vault**

1. Toggle on **ManageEngine Password Manager Pro Vault**.
2. Specify the following parameters:
   * **ManageEngine Password Manager Pro Server URL** *(required)* - The URL of the ManageEngine Password Manager Pro Vault server.
   * **Port** *(required, default 8282)* - The port that the ManageEngine Password Manager Pro Vault listens to.
   * **API Key** *(required* - The AUTH token needed to authenticate the ManageEngine Password Manager Pro Vault request. To create an API key, add an API User and generate an API key, as described in [Adding an API User](https://www.manageengine.com/products/passwordmanagerpro/help/add_api_user.html). Make sure to copy down this key and store it in a secure location for your future reference.

<Callout icon="📘" theme="info">
  Note

  * The API user must have permission to view each resource for which a customer wants to fetch a password.

  * The vault’s API allows access from a single host per user. When creating the user, the customer must supply the Axonius-Instance’s IP as the Host Name. This vault is not supported for Axonius multi node systems.
</Callout>

### ManageEngine PAM360 Vault

<Image alt="ManageEnginePAM360Vault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEnginePAM360Vault.png" />

Axonius pulls credentials from ManageEngine PAM360 Vault. Follow [ManageEngine PAM360 Vault  integration](/docs/manageengine-pam360-vault) configuration guidelines.

**To use ManageEngine PAM360 Vault**

1. Toggle on **ManageEngine PAM360 Vault**.
2. Specify the following parameters:
   * **ManageEngine PAM360 Server URL** *(required)* - The URL of the ManageEngine PAM360 Vault server.
   * **Port** *(required, default 8282)* - The port that the ManageEngine PAM360 Vault listens to.
   * **API Key** *(required* - The AUTH token needed to authenticate the ManageEngine PAM360 Vault request. To create an API key, add an API User and generate an API key, as described in [Adding an API User](https://www.manageengine.com/privileged-access-management/help/add_api_user.html). Make sure to copy down this key and store it in a secure location for your future reference.

<Callout icon="📘" theme="info">
  Note

  * The API user must have permission to view each resource for which a customer wants to fetch a password.

  * The vault’s API allows access from a single host per user. When creating the user, the customer must supply the Axonius-Instance’s IP as the Host Name. This vault is not supported for Axonius multi node systems.
</Callout>