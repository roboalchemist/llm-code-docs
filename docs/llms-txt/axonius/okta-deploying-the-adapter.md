# Source: https://docs.axonius.com/docs/okta-deploying-the-adapter.md

# Deploying the Okta Adapter

To deploy the Okta adapter, perform the following steps:

## 1. Create Okta credentials with the appropriate permissions

<Callout icon="📘" theme="info">
  Note:

  An admin on your system who has Super Administrator permissions needs to create the user account for the Axonius User. Note that the Axonius user itself does not require Admin permissions.
</Callout>

### 1.1 Create a User Account in Okta (Only Required for the API Key Authentication)

<Accordion title="Add User" icon="fa-user">
  You only need to create a specific user when working with the API Key Authentication.

  1. Log in to your [Okta Admin Console](https://login.okta.com/) using an administrator account.
  2. Go to **Directory**, select **People**, and click **Add Person**.

     ![](https://files.readme.io/aceb318530355ae2bb30b4a24f4f08a4588f750e59b9ecb7600ffb7cd6ddee1c-AddPerson.png)
  3. Fill the below user details:
     * **First name**
     * **Last name**
     * **Username**
     * **Password**
  4. For the password, choose **I will set password** and provide the password.

     * If you want the user to reset or change the password on first login, choose the **User must change password on first login** option.
  5. Click **Save** to add the new user.

     ![](https://files.readme.io/f8556e0301d37195e7f2d04b8f3c1fb47c89831596ed33e6b2f6fed8be46867b-Add_Person.png)
  6. Assign roles to the user:

     a. Navigate to **Security** then clcik **Administrators**, and select the **Roles** tab.

     b. Locate the **Read-only Administrator** role, click **Edit**, and select **View or edit assignments**.

     ![](https://files.readme.io/4f6d07ccda924ae5de7be9183a898abfacb296e58fa6344b35e1fcdbd6aced1c-image_3.png)

     c. Click **Add assignment**, and select the newly created user account and click **Save Changes**.

     ![](https://files.readme.io/2d796b903e0c1d0ef3941b5bc0b9f6ec14040adb8028b7d3309fd605406790c0-image_4.png)

     d. Repeat steps a-c for the following roles, as required:

     * **Super Admin** – Required to fetch other admin roles (Asset Management)
     * **Report Administrator** – Required for Axonius SaaS Applications
     * **API Access Management Administrator** – Required for Axonius SaaS Applications

  For a detailed mapping of roles and permissions per asset type, see the [Required Permissions](/docs/okta#required-permissions).
</Accordion>

### 1.2 Authentication Methods

<Callout icon="📘" theme="info">
  Note:

  Username and password authentication may be required to fetch certain elevated application settings. For standard read-only access, **API Key** or **OAuth2** is recommended.
</Callout>

Axonius supports the following authentication methods for connecting to Okta:

<Accordion title="API Key" icon="fa-key">
  1. From the left side menu in the **Admin Console**, click **Security** dropdown and then click **API**.
  2. In the **Tokens** tab, click **Create Token**.
     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateToken.jpg" />
  3. In the pop-up window, provide a name for the token and choose the required option from the drop-down menu to enable the API call origin.

     <Image align="center" src="https://files.readme.io/2ba2bca81c995f738a458f9d9e8cdd918c75d5d5b2d891271ad14dc7660dc166-image.png" />
  4. Click **Create token**.

     <Image align="center" src="https://files.readme.io/af3b06096c4396d2676883e8cc2f4e5fb8184180bc050d4e7999733aa8a33724-image.png" />
  5. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CopyToken.jpg) to copy the token value and save it for later use as it will be displayed only once.
     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TokenValue.jpg" />
</Accordion>

<Accordion title="OAuth2" icon="fa-code">
  1. From the left-side menu in the **Okta Admin Console**, click **Applications**, then select **Applications**.

  2. Click **Create App Integration**.

  3. Select **API Services** as the sign-in method and click **Next**.

  4. Enter a name for the application and click **Save**.

  5. Copy the **Client ID** displayed under the **Client Credentials** section in the **General** tab.

  6. Generate the JSON Web Key (JWK):

     a. In the same **General** tab, click **Edit** under the **Client Credentials**.\
     b. Select **Public key / Private key** option in the **Client authentication**.\
     b. Ensure **Save keys in Okta** is selected under the **Configuration** section.\
     c. Click **Add Key**, then click on **Generate new key** from the pop-up to generate new keys.\
     d. Copy the **Private Key** value only in JSON format by clicking on  **Copy to clipboard**, then paste it into a text file, and save the file securely on your device as the **Private key** will be displayed only once.

  7. Assign required Okta API scopes:

     a. Open the **Okta API Scopes** tab in the application.\
     b. Grant the required scopes.

  <Callout icon="📘" theme="info">
    **Note**

    When using Okta API Key, you can set up a DPoP requirement on Okta when they are creating the OAuth client app to add an extra level of security. While the DPoP header improves overall security, not using it doesn’t pose a particular risk, as the communication between the adapter and the Okta server remains encrypted.
  </Callout>

  8. In the Admin Roles tab

     a. Click **Edit Assignments**.\
     b. From the Role drop-down list, select **Read-only Administrator** (recommended).\
     c. Additional roles may be required depending on the data you want to retrieve. See the [Required Permissions](/docs/okta#required-permissions) section for details.\
     d. Click **Save Changes**.
</Accordion>

### 1.3 Configure a Group in Okta (Optional)

You only need to add a group if you want to use the **Filter Users by Group Name** configuration option.

<Accordion title="Add Group" icon="fa-users">
  1. Login to the Okta Admin Console with a user account that has a **Super Administrator** or **API Access Management Admin** role.

  2. Navigate to **Directory** and select **Groups**.

  3. Click **Add Group**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddGroup.jpg)

  4. Specify a group **Name** and an optional **Description**.

  5. Click **Save**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GroupName.jpg)

  6. In the group, select the **Rules** tab and choose **Add Rule**.

  7. On the Add Rule pop-up, within the `IF` section under **Use basic condition** select User attribute and the condition to add would be email, contains, and add the domain.

  8. On the same Add Rule pop-up, within the `THEN` section select a group of your choice where the user needs to be added or assigned automatically. Note: This rule will not add users to a group they've been manually removed from.

  9. *(Optional)* On the same Add Role pop-up, If you want to explicitly exclude specific users from the rule then add those emails within the `EXCEPT` section.

  10. Click **Save** to to create the rule. On the rules list, from **Actions**, select **Activate** to activate the rule.

      ![](https://files.readme.io/76913b311fd9022ecbecf89a47744b5063e0eccfda046283d64779158e74fa95-image.png)
</Accordion>

### 1.4 Configure Authentication for SaaS Application Settings (Optional)

<Callout icon="🚧" theme="warn">
  This section is only relevant for accounts using Axonius SaaS Applications and is only necessary for fetching high-privilege settings that cannot be fetched with an API token.
</Callout>

Depending on your organization’s security policies, you can either enable 2-step verification (MFA) for the user you just created, or exclude the user from the 2-step verification policy.

You only need to complete **one** of the following sections:

* Enable Multi-Factor Authentication (recommended)
* Optional: How to Exclude the User From MFA

<Accordion title="Enable Multi-Factor Authentication (MFA) in Okta" icon="fa-lock">
  1. Add the Admin user to the group:

     a. Navigate to Groups, select the group you have created.

     b. In the **People** tab, click **Assign people**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignPeople.jpg)

     c. Locate the user account and click the corresponding `+` to assign the user.

     d. Click **Done**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SelectUserForGroup.jpg)

  2. Add Google Authenticator:

     a. Navigate to **Security`>` Authenticators**.

     b. In the **Setup** tab, click **Add Authenticator**.

     ![](https://files.readme.io/9dcee73d7949d3a92b22d6fb7a5f4dbff311640a7f14f3634ceeb3f9c51df2bc-AuthenticatorsSetup.png)

     c. Select the Authenticator type of your choice and click **Add**

     ![](https://files.readme.io/5c6a1b46308ca21f19b64abc148ebba04718856733da7789f1314a509974717c-AddAuthenticator.png)

     d. Click **Add**

     ![](https://files.readme.io/304c3c8d30cb029fbd3bf0f133d4cb53b7256897a735203c1f2a83c797fc41a5-AddGoogleAuthenticator.png)

  3. Enroll Google Authenticator in a policy:

     a. Navigate to **Security`>` Authenticators**.

     b. On the **Enrollment** tab, click **Add a policy**.

     ![](https://files.readme.io/c20437dd0735b47179d15921631703aa0164c6cf8388a10a687803d69149ccf0-Enrollment.png)

     c. Specify a **Policy name**

     d. In **Assign to Groups**, select the group that your created earlier.

     e. From the **Google Authenticator** drop-down, select **Required**.

     f. Click **Create Policy**.

     ![](https://files.readme.io/89ba81e556da454174df834651122c31e66708f8ed09a11465ec848d1d13d441-Add_Policy.png)

     g. In the **Add Rule** window, enter the **Rule name** and click **Create rule**.

     ![](https://files.readme.io/f7c48c42b1744fdf3c935ac2f67e09918fa88cc4676509f0b9180fb3a4de85cc-Add_Rule.png)

  4. Add a rule for MFA:

     a. Navigate to **Security** then select **Authentication Policies** in the Admin Console.

     b. Under **App sign-in policies**, click **Create policy**.

     ![](https://files.readme.io/04a51bb6118befae4f65dfcffb4beaa8996e157e7ea1d59619fadcf7ac0954c1-Authentication_Policies.png)

     c. In the **Create policy** pop-up:

     * Enter a **Name**
     * Enter a **Description** (Optional)
     * Click **Create policy**

       ![](https://files.readme.io/89ba81e556da454174df834651122c31e66708f8ed09a11465ec848d1d13d441-Add_Policy.png)

     d. Open the newly created policy and click **Add rule**.

     e. In the **Add rule** pop-up.

     * Enter a Rule name
     * Configure the required IF conditions based on your organization’s requirements
     * In Assign to Groups, select the group you created earlier
     * From the User must authenticate with dropdown, select the required factor type
       * Recommended: Authentication method chain (Custom)

     ![](https://files.readme.io/f7c48c42b1744fdf3c935ac2f67e09918fa88cc4676509f0b9180fb3a4de85cc-Add_Rule.png)

     f. Click **Save**.

  5. Set up MFA for the user account:

     a. Login to Okta with the account you created.

     b. In the 'Set Up 2 Factor Authentication' window, select Authenticator of your choice.

     ![](https://files.readme.io/d6f955732116fe13d4eec8002f04a8b6b178b033240f7cd818c5cd034b1df041-User_Google_Authenticator.png)
</Accordion>

### Setting Up Multi-Factor Authentication

Axonius enables you to use Multi-factor Authentication in several ways: You can use your organization's SSO according to its policy, Google's authenticator, or the Axonius built-in Multi-factor authentication.

<Accordion title="Set Up Google Authenticator" icon="fa-mobile">
  1. Install Google Authenticator on your phone or add the [Chrome extension](https://chrome.google.com/webstore/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?hl=en).

  2. Select your device type. A QR code will be displayed.

  3. Click **Can't scan QR Code?**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-AFXDWLMU.png)

  4. Copy the displayed secret key.

  5. Click **Next** and enter the verification code displayed in Google Authenticator.

  6. Click **Verify**. (**The verification is one-time process.**)
</Accordion>

<Accordion title="Set Up Axonius 2FA Authenticator" icon="fa-key">
  1. On the adapter's **Add Connection** screen, click the **Generate Secret Key** icon. The Set 2FA Secret Key screen opens. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-SX7EXZS2.png)
  2. Paste the secret key in the 2FA Secret Key field and click **Next**.
  3. The system displays a 6-digit code for you to copy. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ONFRHRQD.png)
  4. Back in Axonius, paste the 6-digit code in the **2FA Secret Key** field to get a verification code.
  5. Back in Okta, paste the verification code.
</Accordion>

MFA adds an additional layer of security, but if it is not required for service users in your organization, you can follow the steps below to exclude the Okta user from MFA.

<Accordion title="Optional: How to Exclude the User From MFA" icon="fa-user-times">
  1. Login to the Okta Admin Console with a user account that has a **Super Administrator** or **API Access Management Admin** role.

  2. Navigate to **Directory`>` Groups**.

  3. Locate and open the group you created earlier.

  4. In the **People** tab, click **Assign people**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignPeople.jpg)

  5. Locate the newly created user account and click the corresponding `+` to assign the user.

  6. Click **Done**.

     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SelectUserForGroup.jpg)

  7. Navigate to **Security`>` Global Session Policy** in the Admin Console.

  8. Click **Add policy**.

  9. Specify a policy name (for example, 'axonius-sm-mfa-policy') and an optional description.

  10. In the **Assign to Groups** field, add the group you just created.

  11. Click **Create policy and add rule**.

      ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreatePolicy.jpg)

  12. Use the default configuration and ensure **Multifactor authentication (MFA)** is set to **Not Required**.

  13. Click **Create Rule**.

      ![](https://files.readme.io/c46f77d4d58933d6c867f620b7bce65f68cce7912ecf0bae10e5232475b52f25-image_1.png)
</Accordion>

### 1.5 Permissions Required to Fetch Roles and Permissions

To fetch Roles and Role Assignments from Okta, complete the following steps:

<Accordion title="Configure Okta to Fetch Roles and Role Assignments" icon="fa-user-shield">
  1. Create a resource set for Roles and Role Assignments:

     a. Navigate to **Security > Administrators**.

     b. Select the **Resources** tab.

     c. Click the **Create resource set** button.

     b. Add the **All Identity and Access Management** resource to the resource set.

     ![](https://files.readme.io/ed80c5a12cce9065ef7a6207d5665d864c2097d5bc6c6b4a7d619cf6b3f2ec25-image.png)

  2. Create a custom role:

     a. Create a **Custom Role**.

     b. Assign the permission **View roles, resources, and admin assignments** to the role.

     <Image align="center" src="https://files.readme.io/7cc05988fabb907f822afaf718937b27030fd049f8b3ef29273a1f71af9c8214-image.png" width="500px" />

  3. Assign the custom role to the Okta user:

     a. Assign the custom role you created to the user account for which the **API key** was generated.
</Accordion>

## 2. Set up the Okta adapter in Axonius

Create the adapter connection in Axonius. Depending on the authentication method you used, fill in the specific fields and configure any optional settings.

## Add a New Connection

* Navigate to the **Adapters** page, search for `Okta`, and click on the adapter tile.

  <Image align="left" border={true} src="https://files.readme.io/a48874676caa778a858f6dd842068a13bf58a1d59c6fcefd7d0421e5f28faa5c-image.png" className="border" />

* On the top right side, click on **Add Connection**.

* The **Add Connection** drawer opens.
  ![](https://files.readme.io/710688b2a2bb54a2e63f7577a8104e02a1d715447a1163ab289818f7cebacb4e-image.png)

### Required Fields

* **Okta URL** – The hostname or IP address of the Okta server. This field format is '\[instance].okta.com'.
* **Authentication** - Select whether to authenticate this adapter connection with an **API Key** or **OAuth2**.
* **Connection Label** – A name to identify this adapter connection

<Callout icon="📘" theme="info">
  **Note:**

  The adapter can fetch many of the Application Settings with just an API token/OAuth credentials. However, to fetch **high-privilege settings**, the adapter requires admin credentials (Admin username/password and 2FA secret key).
</Callout>

<Tabs>
  <Tab title="API Key">
    * **Okta API Key** - The generated API key provided by Okta that allows Axonius to fetch data from the Okta API. This is required when **API Key** is selected in the Authentication drop-down. For details, see  API Key in [Authenticatoin Methods](/docs/okta-deploying-the-adapter#12-authentication-methods).
  </Tab>

  <Tab title="OAuth2">
    * **Okta Client ID** - Client ID of the service app. This is required when **OAuth2** is selected in the Authentication drop-down.
    * **Okta JWK Private/Public Keys** - The JSON web key which was generated and assigned in the OAuth 2.0 service app integration in the Admin Console of Okta. This is required when **OAuth2** is selected in the Authentication drop-down.
  </Tab>
</Tabs>

* **Admin Username** – The value you enter in the User Name field in Okta for the new user you created to allow Axonius to fetch Axonius SaaS Applications data.
* **Admin Password** – The password you set for the new user in Okta.
* **2FA Secret Key** – The secret generated in Okta for setting up 2-factor authentication for the Okta user created for collecting Axonius SaaS Applications data.

### Optional Fields

<Accordion title="Expand/Collapse" icon="fa-cog">
  * **Throttling rate percentage** – Specify the threshold percentage of the Okta API rate limit when connecting to the value supplied in Okta URL. Axonius will stop the data fetch when the API rate limit reaches the supplied value.
  * **Number of parallel requests** – Specify the maximum parallel requests that will be created when connecting to the value supplied in Okta URL.
  * **Admin URL** – The hostname or IP address of the Okta admin server. This field format is `[instance]-admin.okta.com`.
  * **SSO Provider** – If your organization uses Okta for SSO, you can select this check box (selected by default). For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
  * **Department Field** – This is the mapping of the department value for the Okta authentication object. Check if your organization's 'department' value is different from the default value ('department').
  * **User Filter Params** – You can use the [Okta Expression language](https://developer.okta.com/docs/reference/okta-expression-language-in-identity-engine/#unsupported-features) to filter a subset of users (for example, users who belong to specific departments) to be retrieved by the Okta adapter and displayed in Axonius.
  * **Filters users by group name** –  Enter a group name to only fetch users from the specific group. Refer to Configuring a Group in Okta for details.
  * **Add users inside the devices** – Select this option to fetch user information to populate in the relevant device-specific fields.
  * **HTTPS Proxy** – Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **Notes** – Add a note of up to 250 characters for this adapter connection.
  * **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network. To use this option, you need to set up an Axonius Gateway.
</Accordion>

## 3. (Optional) Configure Advanced Settings

Refer to Okta <Anchor label="Advanced Settings" target="_blank" href="/docs/okta-advanced-settings">Advanced Settings</Anchor>.