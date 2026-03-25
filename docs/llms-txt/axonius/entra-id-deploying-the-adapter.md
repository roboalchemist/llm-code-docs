# Source: https://docs.axonius.com/docs/entra-id-deploying-the-adapter.md

# Deploying the Microsoft Entra ID (Azure AD) and Microsoft Intune Adapter

To deploy the Microsoft Entra ID adapter, perform the following steps:

## 1. Create Entra ID credentials with the appropriate permissions

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

Axonius supports the following authentication methods for connecting to Microsoft Entra ID adapter:

<Accordion title="Enterprise Application (Client ID / Client Secret)" icon="fa-key">
  1. **Create a Client Secret**

     a. Open the application you registered.\
     b. Within the app registration, navigate to **Certificates & secrets**, then go to **Client secrets** and select **New client secret**.\
     c. Choose an expiration period for the client secret.

     ![AzureConfig3.png](https://files.readme.io/3d856bec0ef3de18058842c2c76575bd48c6c4f02e56300cc1cfb04feb7da7fd-image_2.png)

     d. Click **Add** and copy the **Client Secret Value** to use when you configure the adapter in Axonius. Note that you cannot view it again once you leave the page.

  2. **Assign Required Roles**

     a. Navigate to **API Permissions** in the application menu. Click **Add a permission**, select **Microsoft Graph**, and then choose **Application permissions**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApplicationPermissions.png" />

     b. Add all the permissions required for the adapter and click **Grant admin consent**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GrantPermissions.png" />
</Accordion>

<Accordion title="Enterprise Application (Certificate)" icon="fa-certificate">
  1. **Upload a Certificate**

     a. Open the application you registered.\
     b. In the app registration, navigate to **Certificates & secrets**, then go to **Certificates** and select **Upload certificate**.\
     c. Upload your public certificate file (<code>.cer</code>, <code>.pem</code>, or <code>.crt</code>).

     ![image.png](https://files.readme.io/f9beda096feb8120c95f43bd9390ea5e8c70b5a38cea52c3802c688d9abefda2-image.png)

     d. The certificate’s thumbprint will be used as the authentication key for the adapter.

  2. **Assign Required Roles**

     a. Navigate to **API Permissions** in the application menu. Click **Add a permission**, select **Microsoft Graph**, and then choose **Application permissions**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApplicationPermissions.png" />

     b. Add all the permissions required for the adapter and click **Grant admin consent**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GrantPermissions.png" />
</Accordion>

<Accordion title="OAuth" icon="fa-code">
  1. **Configure Redirect URI**

     a. Open the application you registered in Entra ID.\
     b. Search and select **Manage**, then **Authentication**.\
     c. In the Web area, copy the redirect URL. The recommended value is `http://localhost:8080`.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedirectURI(1).png" />

     d. Configure the **Redirect URI** if required. Open **Authentication**, click **Add a platform**, select **Web**, and enter the redirect URL for your OAuth flow.

  2. **Generate OAuth Authorization Code**

     a. Copy and paste the following URL into a browser window, replacing Tenant ID, Client ID, and Redirect URI accordingly:

     ```
     https://login.microsoftonline.com/[TENANT]/oauth2/v2.0/authorize?client_id=[CLIENT_ID]&scope=https://graph.microsoft.com/.default&redirect_uri=[REDIRECT_URL]&response_mode=query&response_type=code
     ```

     b. Authorize if required.\
     c. Copy the value for the `code` parameter in the URL to use when you configure the adapter in Axonius.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AuthorizationCodeParameter.png" width="1861px" height="auto" alt="AuthorizationCodeParameter" />

  3. **Create a Client Secret**

     a. Open the application you registered.\
     b. Within the app registration, navigate to **Certificates & secrets**, then go to **Client secrets** and select **New client secret**.\
     c. Choose an expiration period for the client secret.

     ![AzureConfig3.png](https://files.readme.io/3d856bec0ef3de18058842c2c76575bd48c6c4f02e56300cc1cfb04feb7da7fd-image_2.png)

     d. Click **Add** and copy the **Client Secret Value** to use when you configure the adapter in Axonius. Note that you cannot view it again once you leave the page.

  4. **Assign Required Roles**

     a. Navigate to **API Permissions** in the application menu. Click **Add a permission**, select **Microsoft Graph**, and then choose **Application permissions**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApplicationPermissions.png" />

     b. Add all the permissions required for the adapter and click **Grant admin consent**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GrantPermissions.png" />
</Accordion>

### 1.3 (Optional) SaaS Applications

This method is only required when fetching SaaS Applications data for the following Asset Types:\
**User and Application Extensions**, **Licenses**, **Application Settings**, **SaaS Application** and **Accounts**.

<Accordion title="Username / Password" icon="fa-user">
  1. Open the [Microsoft 365 Admin Center](https://admin.microsoft.com) and navigate to **Users** then **Active users**.
  2. Click **Add a user** to create a new account.
     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddUser(2).png" alt="Add User" />
  3. Enter a **display name** for the new user.
  4. Enter a **username** (e.g., `usr_axonius`).
  5. Back in Axonius, enter the username in the format: `username@domainname` (e.g., `sr_axonius@axoniusonmicrosoft.com`).
  6. Enter a strong password for the account. A 32-character password is recommended.
  7. Copy the password securely into Axonius.
  8. Clear **Require this user to change their password on first sign-in** to allow automatic login.
  9. In the user creation workflow, select Create user without product license, then proceed to the next step.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateUserWithoutProduct.png)
  10. Assign the user the required roles. Open the Roles section, access the Admin center access options, and choose the Global reader role for the user.
      ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GlobalReader.png)
  11. Click **Finish adding**, then close the dialog.
  12. Log into this account at [https://login.microsoftonline.com](https://login.microsoftonline.com).
  13. Record the following values for Axonius:
      * **Username** – Dedicated service account username
      * **Password** – Account password
      * **Tenant ID** – Azure directory tenant ID
  14. If Multi-Factor Authentication (MFA) is required:
      * Configure the Authenticator app in Microsoft 365 then Security Info.
      * Generate and copy the 2FA Secret Key to use in Axonius.
</Accordion>

<Accordion title="Steps to Enable MFA" icon="fa-lock">
  1. Navigate to **Microsoft 365 Admin Center → Users → Active users → Multi-Factor Authentication**. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MFAButton.png)
  2. Open the **Service settings** tab. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Service%20Settings.png)
  3. Select **Verification code from mobile app or hardware token** → **Save**. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MethodsAvailable.png)
  4. Go to the **Users** tab → select the new user → **Enable** MFA. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MFAEnable.png)
  5. Configure **conditional access authentication strength**: [Overview of Microsoft Entra Authentication Strength](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths) ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AuthenticationStrength.png)
  6. Configure the Authenticator app and generate a secret key: - Log in → **View account → Security Info → Add sign-in method → Authenticator app → Add** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Microsoft_UseDifferentAuthenticator.png) - Copy the Secret Key: ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MSCopyButton.png) - Paste into Axonius **2FA Secret Key**.
  7. Generate and verify the MFA code via Google Authenticator.
</Accordion>

<Accordion title="Steps to Exclude MFA" icon="fa-shield">
  1. Ensure **Enable 2FA** checkbox in Axonius is cleared.
  2. Go to **Microsoft Azure Admin Center → Entra ID → Security → Named Locations → Configure multifactor authentication trusted IPs**. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Configure_MFA_IP.png)
  3. Add Axonius IP ranges → **Save**.
  4. Exclude the user from Conditional Access policies: - **Entra ID → Security → Conditional Access → Policy → Users and groups → Exclude → Select user → Save** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsersAndGroups.png)
</Accordion>

## 2. Set up the Entra ID adapter in Axonius

Create the adapter connection in Axonius. Depending on the authentication method you used (Client Secret, Certificate, OAuth, or Username/Password), fill in the specific fields and configure any optional settings.

## Add a New Connection

* Navigate to the **Adapters** page, search for `Entra ID`, and click on the adapter tile.

  <Image align="left" border={false} src="https://files.readme.io/e15b92e6d850b229d30ef129ad9faa95aedeb5eaed4dad82479f76e1a3bc793e-Entra_ID.png" />
* On the top right side, click on **Add Connection**.
* The **Add Connection** drawer opens.
  ![](https://files.readme.io/dab9c6bc866c287cb576bcf343f8cd1b85268403e56e707f47c328d117dd1bb3-image.png)

### Required Fields

* **Azure Client ID** – The Application ID of the Axonius application.
* **Azure Tenant ID** – The ID for Microsoft Entra ID.
* **Connection Label** – Name to identify this adapter connection.
* **Authentication Method**

<Tabs>
  <Tab title="Enterprise Application (Client ID / Client Secret)">
    - **Azure Client Secret** – Specify a non-expired key generated from the new client secret.
  </Tab>

  <Tab title="Enterprise Application (Certificate)">
    * **Enable Certificate-Based Authentication** – Select to enable Axonius to send requests using the Azure certificates uploaded to allow secure Azure authentication for this adapter. To add the certificate to the App registration in Azure, see [Register an app in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate,expose-a-web-api).
      * Click **Upload file** next to **Private Key File** to upload an Azure private key file in PEM format.
      * Click **Upload file** next to **Certificate File** to upload an Azure public key file in PEM format.
  </Tab>

  <Tab title="OAuth">
    * **Azure OAuth Authorization Code** – The authorization code to connect to Microsoft Intune.
    * **Azure OAuth - Redirect URI/Reply URL** – The location where the authorization server sends the user once Azure has been successfully authorized and granted an authorization code or an access token. For more information, see [Redirect URI (reply URL) restrictions and limitations](https://learn.microsoft.com/en-us/azure/active-directory/develop/reply-url).
  </Tab>
</Tabs>

### Required Fields for SaaS Applications

* **Account Sub Domain** – The Microsoft account's sub domain (.onmicrosoft.com).
* **User Name** and **Password** – The credentials for a user account that has the permissions needed to fetch **Axonius SaaS Applications data**.
* **2FA Secret Key** – The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For more information, see [Enable or Exclude Multi-Factor Authentication](/docs/microsoft-azure-active-directory-ad#enable-or-exclude-multifactor-authentication).

### Optional Fields

<Accordion title="Expand/Collapse" icon="fa-cog">
  * **Verify SSL** – Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
  * **SSO Provider** – If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
  * **Cloud Environment (default - Global)** – Select Microsoft Azure cloud environment type.
  * **Is Azure AD B2C** – Select this option to cause Axonius to consider that this Microsoft Entra ID adapter connection is configured as B2C.
  * **Account Tag** – Specify a tag for Axonius to tag all devices fetched from this adapter for the Azure Cloud instance ("nickname").
  * **Device groups blocklist** – Enter a group or groups whose devices will be ignored and not fetched. If you want to enter more than one group, separate with commas.
  * **HTTPS Proxy** – A proxy to use when connecting to the selected Microsoft Azure/Entra ID cloud environment.
  * **HTTPS Proxy User Name** and **Password** – The user name and password to use when connecting to the selected Microsoft Azure cloud environment via the value supplied in **HTTPS Proxy**.
  * **Notes** – Add a note of up to 250 characters for this adapter connection.
  * **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network. To use this option, you need to set up an Axonius Gateway.
</Accordion>

## 3. (Optional) Configure Advanced Settings

Refer to Entra ID <Anchor label="Advanced Settings" target="_blank" href="https://docs.axonius.com/v1.0_Tudip_Project_branch/docs/entra-id-advanced-settings">Advanced Settings</Anchor>.