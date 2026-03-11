# Source: https://docs.axonius.com/docs/google-workspace-deploying-the-adapter.md

# Deploying the Google Workspace (G Suite) Adapter

To deploy the *Google Workspace (G Suite)* adapter, perform the following steps:

## 1. Create Google Workspace (G Suite) Credentials with the Appropriate Permissions

### 1.1 Create a Service Account and Enable Domain-Wide Delegation

<Accordion title="Step 1: Create a Service Account in Google Cloud Console" icon="fa-key">
  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

  2. Select an existing project or create a new one.

  3. Navigate to **IAM & Admin → Service Accounts**.

  <Image border={true} src="https://files.readme.io/a73f6b9134fcfef27dbebcbce107dfa8fcc1024ff9a46a90d045df0ad02fde7e-ServiceAccount.png" />

  4. Click **Create service account**.

     <Image border={true} src="https://files.readme.io/8fa11fb61f43e05f321207708d0a75a381ab594425fb60e6779a5aaa4259c190-CreateServiceAccount.png" />

  5. Enter a name (for example, **Axonius Google Workspace Adapter**).

  6. Click **Create and continue**.

  7. Skip granting roles (**roles are not required** for domain-wide delegation).

  8. Click **Done**.
</Accordion>

<Accordion title="Step 2: Create and download the Service Account Key" icon="fa-file-code">
  1. Click the newly created service account.

  2. Open the **Keys** tab.

  3. Click **Add Key → Create new key**.

  4. Select **JSON** as the key type.

  5. Click **Create**.

     <Image border={true} src="https://files.readme.io/91b5bae87c60149e502ae74e9fdb10a5517baaa7198682b30bd025a5720d375f-CreatePrivateKey.png" />

  6. Save the downloaded **JSON file** securely.
</Accordion>

<Accordion title="Step 3: Enable Domain-Wide Delegation" icon="fa-shield-alt">
  1. In the service account details page, click the **Details** tab.

  2. Click **Advanced settings** to expand the section.

     <Image border={true} src="https://files.readme.io/1dbf5ea4c14406afcbb97709323f2cdec784552141cd5bebf2f1fa23b9a51833-DomainWideDelegation.png" />

  3. Copy the **Client ID** displayed.

  4. Keep this ID ready for the next step in the **Google Workspace Admin console**.
</Accordion>

<Accordion title="Step 4: Authorize Service Account in Google Workspace Admin Console" icon="fa-cogs">
  1. Go to the [Google Workspace Admin Console](admin.google.com).

  2. Navigate to **Security → Access and data control → API controls**.

     <Image border={true} src="https://files.readme.io/d9e6de5290d121cf8bb20d8c273a19a7cef3da6bdda8d504639b1cdcf75acc90-Security_APIControl.png" />

  3. Scroll down to the **Domain-wide delegation** pane.

  4. Click **MANAGE DOMAIN WIDE DELEGATION**.

     <Image border={true} src="https://files.readme.io/14e7460cb60d8248ce53d39bf3c42381f1dbd3173716f1e6a8f84c658bf0afab-ManageDomainDelegation.png" />

  5. Click **Add new**.

     <Image border={true} src="https://files.readme.io/b66a89c06c11b1d7b345e1900c45060746d2ef067671a27a04314ab7979baa2d-AddNew.png" />

  6. In the **Client ID** field, paste the unique Client ID you copied before.

  7. In the **OAuth scopes** field, enter the comma-separated list of scopes. See [Required Permissions](/docs/google-workspace#required-permissions).

  8. Click **AUTHORIZE**.

     <Image border={true} src="https://files.readme.io/2e787eb2c0f70a53db9e8264534db97300a282992ead8d50e04e009ded589f73-AddNewClientID.png" />
</Accordion>

### 1.2 Enable Required Google Cloud APIs

<Accordion title="Enable Google Cloud APIs" icon="fa-cloud">
  1. Go to **[Google Cloud Console](https://console.cloud.google.com/) → APIs & Services → Library**.

     <Image border={true} src="https://files.readme.io/07bef978e963a75f192db936f48303e91765be332040aa7f2ebddb938be06cc8-APIsServices.png" />

  2. Select the same project where the service account was created.

  3. Search for the **Admin SDK API** in the Library.

     <Image border={true} src="https://files.readme.io/e02741529710eb3119dabece2daf641003c44f55b72ae01dba94a523b7866dac-AdminSDKAPI.png" />

  4. Click **Admin SDK API** from the search results.

  5. Click **Enable**.

     <Image border={true} src="https://files.readme.io/416f1d513e339e8d04eb55b2d89e255025c2f69ca5423b915af5e151f1da90b3-EnableSDKAPI.png" />

  6. Repeat as needed for other APIs.

  For additional APIs required for features like Cloud Identity devices, Groups, Calendars, and Chrome Management, refer to [Advanced Permissions](/docs/google-workspace-advanced-permissions).
</Accordion>

### 1.3 Create and Configure a User Account

<Accordion title="Step 1: Create a Dedicated User" icon="fa-user-plus">
  1. Go to **[Google Workspace Admin Console](admin.google.com) → Directory → Users**.

  2. Click **ADD NEW USER** and enter the user details (for example, `axonius-service@yourdomain.com`).

     <Image border={true} src="https://files.readme.io/fed45732154ca804cdd4c3daa971109e9c00b94f68affaa6d2953cb2557b3e10-AddNewUser.png" />

  3. Open the newly created user account and navigate to the **Security** tab.

  4. **Important:** Disable 2-step verification for this account:
     * Set **2-step verification** to **OFF**.

       <Image border={true} src="https://files.readme.io/09f84e09e8864a8230414243a260a2a67063c09fca41954a7739ebbcf92e25a1-Disable2FA.png" />

  5. Save the changes.
</Accordion>

<Accordion title="Step 2: Assign Admin Role with the Least-Privilege Permissions" icon="fa-user-shield">
  **Option A: Use a Pre-built Role (Quick)**

  1. Navigate to **Account → Admin roles**.
  2. Assign the user to a pre-built role (for example, **User Management Admin**) with **read-only access**.

  **Option B: Create a Custom Role (Recommended)**

  1. Navigate to **Account → Admin roles → Create new role**.
  2. Enter a role name (for example, `Axonius Read-Only`).
  3. Under **Privileges**, select the specific read-only permissions listed in the [Required Permissions](/docs/google-workspace#required-permissions).
  4. Click **Continue** and then **Create Role**.
  5. Click Assign users and select the user you created.
</Accordion>

### 1.4 SaaS Applications (Optional)

This unique authorization is required only for specific asset types and must be configured **only if you want to fetch Licenses and Application Settings**.

<Accordion title="Create an SSO-Excluded Organizational Unit" icon="fa-user-slash">
  1. In the Google Workspace Admin Console, from the navigation menu, navigate to **Directory`>` Organizational Unit**.

  2. Click **Create new organizational unit**.\
     ![Create OU](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateOU.png)

  3. Enter a **Name** for the Organizational Unit (for example, *Axonius SaaS Applications*).

  4. Click **Create**.\
     ![Create New OU](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewOU.png)

  5. From the left navigation menu, navigate to **Security`>` Authentication `>` SSO with third party IdP**.

  6. In the Manage SSO profile assignments section, click **Get Started** or **Manage**.\
     ![Manage IDP](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageIDP.png)

  7. In the Manage SSO profile assignments page, on the left pane, expand the **Organizational units** section and select the organizational unit you just created.\
     ![Locate OU](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LocateOU.png)

  8. Under **SSO profile assignment**, select **None**.

  9. Click **Save**.

     ![](https://files.readme.io/66637d92bc0f4c1d927c5067076d248236fe68d7bcebf1f72ba7ac234ac5b265-image.png)
</Accordion>

<Accordion title="Username / Password" icon="fa-user">
  1. Use the user you created before.
  2. **Licenses**: Ensure the Enterprise License Manager API is enabled and the scope `https://www.googleapis.com/auth/apps.licensing` is authorized.
  3. **Application Settings**: Ensure the Group Settings API is enabled and the scope `https://www.googleapis.com/auth/apps.groups.settings` is authorized.
  4. Record the Username and Password for later use.
</Accordion>

<Accordion title="Create a Custom Role in Google Cloud Console" icon="fa-user-shield">
  1. Log into [Google Cloud Console](https://console.cloud.google.com/) as an administrator.

  2. Navigate to **IAM & Admin → Roles**.

  3. Click **Create role**.

     <Image border={true} src="https://files.readme.io/5f3d305bc1b79600d01cf0ddea18be92499ec5cfcee5d4ee67a09cdc755f0137-CreateRole.png" />

  4. Enter a **Title** (for example, `srv-axonius-sm-role`).

  5. Click **Add permissions**.

  6. Search for [required permissions](/docs/google-workspace#required-permissions) (for example, `resourcemanager.projects.get`).

     <Image border={true} src="https://files.readme.io/1c560fbb38bb2a4af4e96e12057124f2b6be6aa70c76053952ca30b948517c3e-AddPermissionList.png" />

  7. Select the permission and click **Add**.

     <Image border={true} src="https://files.readme.io/261ca4d322ae1af0ad9ef96ffdab957497a1b18054b4e39dcde0722410ccb607-AddPermission.png" />

  8. Click **Create**.
</Accordion>

<Accordion title="Assign the Role to the User" icon="fa-user-plus">
  1. Navigate to **IAM & Admin → IAM**.
  2. Locate the principal associated with the account.
  3. Click the **Edit** icon next to the principal.
  4. Click **Add Another Role**.
  5. Locate and select the custom role you created.
  6. Click **Save**.
  7. If prompted, click **Continue**.
</Accordion>

<Accordion title="Enable Admin SDK API for the Project" icon="fa-plug">
  1. Open the following URL, replacing `<project_id>` with your project ID from the JSON key file:\
     `https://console.developers.google.com/apis/api/admin.googleapis.com/overview?project=<project_id>`
  2. Click **Enable** to activate the Admin SDK API.
</Accordion>

### 1.4.1 Configure Authentication for SaaS Application Settings (Optional)

Depending on your organization’s security policies, you can either enable 2-step verification (MFA) for the user you just created or exclude the user from the 2-step verification policy.

You only need to complete one of the following sections:

* Enable Multi-Factor Authentication (recommended)
* Optional: How to Exclude the User From MFA

<Accordion title="Enable Multi-Factor Authentication (Admin Console)" icon="fa-lock">
  **Prerequisite:** These steps must be performed by a **Super Admin**.

  1. Sign in to the **Google Workspace Admin Console**.

  2. Navigate to **Menu → Security → Authentication → 2-Step Verification**.

  3. Select the **Organizational Unit (OU) or Group** where the user resides.

  4. Enable **Allow users to turn on 2-Step Verification**.

  5. Under **Enforcement**, select **Off** (allows manual enrollment).

  6. Click **Save**.
</Accordion>

### Setting Up Multi-Factor Authentication

Axonius enables you to use Multi-Factor Authentication in several ways. You can use your organization’s SSO according to its policy, Google Authenticator, or the Axonius built-in Multi-Factor Authentication.

<Accordion title="Set Up Google 2-Step Verification" icon="fa-mobile">
  1. Sign in to [Google My Account](https://myaccount.google.com/).
  2. Navigate to **Security & sign-in**.
  3. Under **How you sign in to Google**, click **2-Step Verification**.

  ![2-Step Verification](https://files.readme.io/6a9f39bd8250eeeb3fc074fec4d8a5a489f8a1d0f28a45388bc749006e200197-2FA.png)

  4. Complete the initial setup (for example, phone number, SMS, or Google prompt).

  5. Enter the code you received from Google and click **Next**.

  6. Click **Turn on** to enable **2-Step Verification**.

  ![Add Mobile Number](https://files.readme.io/b28a3daa2bee95c73588b902bfd8cfa3f58c62ae6d71818988b4b6a50ab30ac0-2FA_AddMobileNumber.png)

  7. In the **2-Step Verification** page, scroll to the **Add more second steps to verify it’s you** section.

  8. Click **Authenticator app**.

  9. Use the **Axonius Built-In Multi-Factor Authenticator**, install **Google Authenticator** on your phone, or add a [Chrome extension](https://chromewebstore.google.com/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?hl=en\&pli=1).

  10. Scroll to **Authenticator app** and click **Set up authenticator**.

  11. Click **Can’t scan it?** to reveal the **Secret Key**.

  ![Authenticator Secret Key](https://files.readme.io/cf2d4caf3f391c6c4c41d9621c57cf5f9acb3fc35de621fbaf9ca2cf3e881342-Authenticator.png)

  12. Copy the **Secret Key**.
</Accordion>

<Accordion title="Set Up Axonius Built-In Multi-Factor Authentication" icon="fa-lock">
  1. On the adapter **Add Connection** screen in Axonius, click the **Generate Secret Key** icon.
  2. The **Set 2FA Secret Key** screen opens.
  3. Paste the **Secret Key** copied from Google into the **2FA Secret Key** field and click **Next**.

  ![Paste Secret Key](https://files.readme.io/0e2dcade6df9835f09993774310fc91bd2b834358b9ad8003e30af86312facda-secret2fa.png)

  4. Axonius generates a **6-digit verification code**.
  5. Copy the **6-digit code**.

  ![6-digit Code](https://files.readme.io/1ca36a4ce3a329ead0aa4262d861f512276740b026e4fdaa80de0f1fe1c3be98-secret2faotp.png)

  6. Return to the Google **Set up authenticator** screen, click **Next**, and paste the code to complete verification.
  7. Click **Verify**.
  8. Back in Axonius click **Complete** on the **Set 2FA Secret** Field dialog.
  9. Click **Save**.
</Accordion>

<Accordion title="Optional: How to Exclude the User from MFA" icon="fa-shield">
  If your organization enforces **2-Step Verification** globally, follow the steps below to exclude the service user.

  **Exclude the user using an Organizational Unit (OU)**

  1. In the Admin Console, navigate to **Directory → Users**.
  2. Select the user and move them to an **OU where 2-Step Verification enforcement is set to Off**.

  **Exclude the user using Group or OU enforcement settings**

  1. Navigate to **Security → Authentication → 2-Step Verification**.
  2. Select the **OU or Group** containing the user.
  3. Set **Enforcement** to **Off** and click **Save**.

  ![Disable 2FA](https://files.readme.io/62bf264d8c4f2482e3882f66113baf2e907c853d2558f0d6bf1a2e5c26a52dd3-Disable2FA.png)
</Accordion>

## 2. Set up the Google Workspace (G Suite) Adapter in Axonius

Create the Adapter connection in Axonius. Based on the authentication method, fill out the specific fields, and configure optional settings.

## Add a New Connection

1. Navigate to the **Adapters** page, search for `Google Workspace (G Suite)`, and click on the adapter tile.
2. On the top right side, click **Add Connection**.
3. The **Add Connection** drawer opens.

![](https://files.readme.io/413e6fd45de573754eb9d26297382fbf091631733576047c12048498594e5aaf-GoogleWorkspaeAddConnection.png)

### Required Fields

* **Email of an admin account to impersonate** - Enter the email of your Google Workspace (G Suite) admin.
* **JSON Key pair for the service account** - Upload the private key JSON file you created for your service account as described in [Step 2: Create and download the Service Account Key](/docs/google-workspace-deploying-the-adapter#11-create-a-service-account-and-enable-domain-wide-delegation)
* **Connection Label** - Enter the name to identify this adapter connection.

### Required Fields for SaaS Applications

This  authorization is required  only if you want to fetch **Licenses** and **Application Settings**.

* **Username** – The value you enter in the User Name field in Google for the user you created.

* **Password** – The password you set for the user in Google.

* **Login Url** – The hostname or IP address of the Google server.

* **2FA Secret Key** (optional) - The secret generated in Google Workspace for setting up 2-factor authentication for the Google user created. If you bypassed 2FA, then this field is not required.

### Optional Fields

<Accordion title="Expand/Collapse" icon="fa-cog">
  * **Account Profile Name** - [Google user name](https://admin.google.com/ac/accountsettings/profile) This field is used to link assets to the profile, such as linking the Applications and App Settings to the Account asset.

  * **Get OAuth Apps** - Select to fetch the OAuth applications used by each user. Note This data requires an additional scope to your Google Workspace (G Suite) admin account. For more information, see [Advanced Permissions](/docs/google-workspace-advanced-permissions).

  * **Fetch Cloud Identity Devices** - Select whether to fetch Cloud Identity devices. Note Fetching Cloud Identity devices requires: Adding the following scope to your Google Workspace (G Suite) admin account. It also requires enabling the Cloud Identity API. For more information, see [Advanced Permissions](/docs/google-workspace-advanced-permissions).

  * **Fetch Chrome Browsers** – Select this option to fetch Chrome browsers information. Note Fetching Chrome browsers information requires an additional privilege to your Google Workspace (G Suite) admin account. For more information, see [Advanced Permissions](/docs/google-workspace-advanced-permissions).

  * **Fetch Calendars** – Select this option to fetch users' calendars. Note Fetching calendar information requires an additional privilege to your Google Workspace (G Suite) admin account. It also requires enabling the Cloud Identity API. For more information, see [Advanced Permissions](/docs/google-workspace-advanced-permissions).

  * **SSO Provider** - If your organization uses Google for SSO, you can set this select this check box (selected by default). For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).

  * **Proxy address** - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Proxy port** - The port for the proxy server.

  * **Proxy username** - The user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in Proxy address.

  * **Proxy password** - The password to use when connecting to the server using the Proxy.

  * **Notes** – Add a note of up to 250 characters for this adapter connection.

  * **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network. To use this option, you need to set up an Axonius Gateway.
</Accordion>

## 3. (Optional) Configure Advanced Settings

Refer to [Google Workspace (G Suite) Advanced Settings](/docs/google-workspace-advanced-settings)