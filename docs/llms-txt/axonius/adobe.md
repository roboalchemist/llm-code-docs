# Source: https://docs.axonius.com/docs/adobe.md

# Adobe

Adobe offers digital content creation and publication applications across 20+ areas including graphics, photography, illustration, multimedia/video, and more.

## Asset Types Fetched

* Users, Roles, SaaS Applications, Licenses, Groups

## Before You Begin

To successfully connect this adapter, complete the following steps first:

1. [Step 1: Creating a new service account credential](/docs/adobe#step-1-creating-a-new-service-account-credential)
2. [Step 2: Creating a User Account](#step-2-creating-a-user-account)

### Step 1: Creating a New Service Account Credential

<Callout icon="📘" theme="info">
  Note

  While to access SaaS application data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
</Callout>

1. Login to <Anchor label="Adobe Admin Console" target="_blank" href="https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation">Adobe Admin Console</Anchor> with an admin user.
2. To begin adding an API:
   1. From within a templated project, first select the appropriate workspace to open the Workspace overview.
   2. Select **+ Add Service** in the left navigation and then select **API** from the drop down list.
   3. In an empty project, select **+Add to Project** in the left navigation of the Project overview and then choose API, or select Add **API** from the quick start buttons.
      The **Add an API** dialog shows a list of available services with the default view by setting to show only those services available to you.

<Image align="center" alt="image.png" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-RH1WXQWM.png" />

3. Add the following APIs:
   1. **Adobe Services - User Management API** (for user information)
   2. **Adobe Analytics API** (for last login information)
   3. **Experience Platform API** (for roles and permissions)

<Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-PQB9IF2E.png" />

4. Select **Next**.
5. Generate the Private Key *(required for JWT authentication; note that this option might be deprecated by the time you connect this adapter)*:

   a. Click **Generate keypair**. A file is downloaded to your computer containing your private key, as well as all of your app settings.

   b. Open the file to retrieve the private key and copy it.

   c. Back in Axonius, paste the key into the Private Key field.
6. In Adobe, click **Next** and then click **Save configured API**.
   With the API configured, you are redirected to the API overview page.

<Callout icon="📘" theme="info">
  Note

  Adobe does not record your private key, therefore you must make sure to securely store it. This includes downloaded private key files from Console or files generated elsewhere.
</Callout>

7. From the left menu, click **Service Account**.
8. Copy the following parameters and paste them into their respective fields in Axonius:

* Client ID
* Client secret
* Organization ID
* Technical account ID *(required for JWT authentication*)

### Step 2: Creating a User Account

<Callout icon="📘" theme="info">
  Note

  While to access SaaS data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
</Callout>

1. Login to the [Adobe Admin Console](https://adminconsole.adobe.com/) with an admin account.
2. From the top menu, select **Users**.
3. From the left menu, click **Administrators**.
4. Click **Add Admin** and specify an email address used for Axonius, first and last name.
5. Logout and then login with the newly created user.
   An email will be sent to the supplied address with a verification code.
6. Enter the received verification code, and then set a new password of at least 32 characters.

## Connecting the Adapter in Axonius

<Callout icon="💡" theme="warn">
  Important Note

  The **Technical account ID** and **Private Key** parameters are only required if you use JWT authentication. However, this authentication method might not work as by the time you connect this adapter, it might be deprecated. Therefore, we recommend using the OAuth Server-to-server authentication method. For more information, see [OAuth Server-to-Server credential implementation guide](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation/).
</Callout>

### Required Parameters

1. **Organization ID**  - The created service account's organization ID.
2. **Client ID** and **Client secret** - The created service account Client ID and Client secret.

**When using JWT authentication:**

1. **Technical account ID** - The created service account's technical account ID.
2. **Private Key (RS-256)** - Your service account's private key, including the '-----BEGIN PRIVATE KEY-----' prefix and the '-----END PRIVATE KEY-----' suffix.

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="AdobeParameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WSG0B6OP.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Usage from Adobe Analytics** - Select this option to fetch license usage data from Adobe Analytics.
2. **Backward Days for Usage Statistics** *(default: 120)* - Define how many days backwards you want to fetch usage statistics.
3. **Report Suit ID of the report suite from which data is collected** - Enter the ID of the Report Suit used to fetch usage data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>