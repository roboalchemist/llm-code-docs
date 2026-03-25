# Source: https://docs.axonius.com/docs/deploying-the-salesforce-adapter-part-1.md

# Deploying the Salesforce Adapter in Axonius

## 1. Salesforce Initial Setup

### 1.1. Create a User Account and User Profile

Having a Salesforce User Account and User Profile is a mandatory requirement to successfully deploy the adapter in Axonius. To create these, follow these steps in Salesforce:

<Accordion title="User Account/Profile Setup" icon="fa-info-circle">
  #### Create a User Account

  1. Navigate to **Users`>` Users**.

  2. Click **New User**.

  3. Fill in information for the new user, in the email field enter an email that you have access to.

  4. Click **Save**.

  5. Copy the user's username.

  6. Set Password:

     1. Open the email you receive from Salesforce.
     2. Click **Verify Account**. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VerifyAccount.png)
     3. Enter a password for the user.
     4. Copy the password. It's best practice for the password to contain 32 characters.
     5. Enter a security question and answer.
     6. Click **Change Password**.<br />
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordScreen\(1\).png)

  7. Connect the new user to the user profile you created earlier:

     1. In Salesforce, from the Administration menu, navigate to **Users`>` Users.**
     2. Select the user you just created.
     3. From the User License drop-down list, select **Salesforce**.
     4. From the profile drop-down list, select the profile you created earlier.
     5. Click **Save**.

  8. To verify that the user you created has the correct permissions, make sure it has access to the following URLs. There is no need to modify any of the configurations on these pages.

     * https\://`{account}`.lightning.force.com/lightning/setup/EnhancedProfiles/home
     * https\://`{account}`.lightning.force.com/lightning/setup/SecuritySession/home
     * https\://`{account}`.lightning.force.com/lightning/setup/SecurityPolicies/home
     * https\://`{account}`.lightning.force.com/lightning/setup/LoginAccessPolicies/home
     * https\://`{account}`.lightning.force.com/lightning/setup/IdentityVerification/home
     * https\://`{account}`.lightning.force.com/lightning/setup/FileTypeSetting/home
     * https\://`{account}`.lightning.force.com/lightning/setup/OrgDomain/home

  #### Create a User Profile

  Create a user profile to configure the right permissions and password policies in your user account.

  1. In Salesforce, navigate to **Users > Profiles**.

  2. Locate the **System Administrator** profile and in that row, click **Clone**.

  3. Enter a profile name (for example, *Axonius*).

  4. Click **Save**.

  5. Set permissions for the profile: a.

     1. From the profile page, click **Edit**.
     2. Configure the permissions so that the following permissions are selected:

        * Every permission from the General User section starting with the word "View" except for **View Encrypted Data**.<br />
          ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ViewPermissions.png)
        * Lightning Experience User
        * API Enabled
        * Manage IP addresses
        * Manage Login Access Policies
        * Manage Password Policies
        * Manage Profiles and Permissions Sets
        * Manage Roles
        * Manage Sharing
        * View All Profiles
        * View All Users
        * Apex REST Services
        * Manage Users
        * Manage Connected Apps
        * Modify Metadata Through Metadata API Functions
        * Customize Application
        * Is Single Sign-On Enabled
          c. In the **Connected App Access** section, select the application you created earlier.

  6. Set the password policy:

     1. Locate the **Password Policies** section.
     2. From the **User Passwords Expire in** drop-down list, select **Never Expires**.
     3. Select **Don't immediately expire links in forgot password emails**.
     4. Click **Save**.

     <Callout icon="📘" theme="info">
       Note

       Before performing the following steps, contact Axonius support for the list of trusted IP ranges to include. If you do not have such list, and you want to authenticate with the Username-Password flow, you must generate a user secret.
     </Callout>

  7. Configure access to trusted IPs:

     1. From the left hand menu, navigate to **Security`>` Network Access**.
     2. Click **New**. <br />
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Network%20Access\(1\).png)
     3. Add the Axonius IP ranges and click **Save**.

        <Callout icon="📘" theme="info">
          **Note**

          The IP ranges you provide here are trusted for **all apps connected to this user profile**. Alternatively, you can provide trusted IP ranges **for a specific app**.
        </Callout>

  8. Navigate to **Users > Users**. Select the user you created above.

  9. From the Profile drop-down list, find the profile you just created to continue working.
</Accordion>

### 1.2. Generate a User Secret (Optional)

This part is mandatory only if:

* You are authenticating with the Username-Password flow.
* You didn't provide a list of trusted IP ranges.

For more information, see [Reset Your Security Token](https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm\&type=5).

<Accordion title="Generating a User Secret" icon="fa-info-circle">
  To generate a user secret:

  1. Log into Salesforce with an admin account with an email address that you have access to.
  2. Open the Profile menu and select **Settings**.
  3. Select **My Personal Information`>` Reset My Security Token**.
  4. Click **Reset Security Token**.
  5. Access the account's email and copy the new token from the Salesforce email.
  6. When creating an adapter connection in Axonius, paste the token into the **User Secret** field.
</Accordion>

## 2. Setting Axonius as a Salesforce's External Client App

After creating a User Account and User Profile, the next step is to **configure the Axonius app as an external app integration in Salesforce**. This is **mandatory** for retrieving the **Consumer Key** and **Consumer Secret** connection parameters.

<Accordion title="Creating a New External Client App" icon="fa-info-circle">
  1. In Salesforce, navigate to **Setup**.
  2. From the left hand menu, select **External Client App Manager**, then click **New External Client App**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Salesforce_create%20external%20app.png" width="700px" />
  3. Under **Basic Information**, fill in the required parameters:
     1. **External Client App Name** - For example, `Axonius_integration`.
     2. **API Name** - This is created automatically based on the App Name you provided.
     3. **Contact Email** - It is recommended to use an email address of an Administrator user.
     4. **Distribution State** - Leave the default value (Local).
  4. Under **API (Enable OAuth Settings)**, check **Enable OAuth**. Two new sections appear:
     1. **App Settings** - Provide a **Callback URL** here. This is the URL to which the created access token will be sent. It is recommended to use the Axonius default callback URL: `https://localhost/adapters/salesforce`
     2. **OAuth Scopes** - Add scopes from the **Available OAuth Scopes** list to the **Selected OAuth Scopes** list. To enable fetch of all asset types by the adapter, add the following scopes:

        * Access the Identity URL service (id, profile, email, address, phone)
        * Manage user data via APIs (api)
        * Perform requests at any time (refresh\_token, offline\_access)
        * Access unique user identifiers (openid)
        * Access Lightning Applications (Lightning)
        * Access content resources (content)
        * Access Interaction API resources (interaction\_api)
  5. Under **Flow Enablement**, check **Enable Client Credentials Flow**.
  6. Under **Security**, check the following:

     1. Require secret for Web Server Flow
     2. Require secret for Refresh Token Flow
     3. Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Salesforce_flow%20and%20security%20checkboxes.png" width="500px" />
  7. Click **Create**.

  Now you can see the newly created app in the **External Client App Manager** page:

  <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Salesforce_new%20app.png" width="500px" />

  **Defining Policies**

  In the **External Client App Manager** page:

  1. Select the **Policies** tab and click the **Edit** button on the left.
  2. Expand the **OAuth Policies** section.
  3. Check **Enable Client Credentials Flow**.
  4. Under **Run As (Username)**, enter the Email address defined for this app.
  5. Under **App Authorization** `>` **IP Relaxation**:
     * If you provided a list of trusted IP ranges when [creating a User Account and Profile](https://docs.axonius.com/axonius-help-docs/docs/deploying-the-salesforce-adapter-part-1), select **Enforce IP restrictions**.
     * If you did not provide such a list, select **Relax IP restrictions**.

       <Callout icon="📘" theme="info">
         **Note**

         If you didn't provide a list of trusted IP ranges and your organization's security policy doesn't allow to relax IP restrictions, contact your security team for guidance.

         Alternatively, you can add trusted IP ranges **for this specific app**. To do so:

         Go to **Settings** `>` Click **Edit** `>` under the **Trusted IP Ranges for OAuth Web Server Flow**, click `+` to add a range.

         <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Salesforce_add%20ip%20range.png" width="700px" />
       </Callout>
  6. Under **Refresh Token Validity Period**, leave the default value of 365 days (the maximum).
  7. Click **Save**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Salesforce_policies.png" width="700px" />

  If you want to edit the basic app settings, select the **Settings** tab (left of the **Policies** tab) click **Edit** and make the necessary changes.

  **Retrieving the Consumer Key and Secret**

  1. In the same page, select the **Settings** tab.
  2. Expand **OAuth Settings**.
  3. Under **App Settings**, click **Consumer Key and Secret**.

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Salesforce_find%20keys.png" width="500px" />
  4. A **Verify Your Identity** page opens in a new tab. Enter the verification code you received via email and click **Verify**.
  5. If the verification is successful, the **Consumer Key** and **Consumer Secret** are displayed. Click **Copy** under each of these parameters and paste them into the corresponding fields in Axonius.
</Accordion>

## 3. Adding a New Salesforce Adapter Connection in Axonius

After making all necessary configurations in Salesforce, you're ready to set up the adapter in your Axonius instance.

### 3.1. Create a Salesforce Adapter Connection

<Accordion title="Connection Parameters" icon="fa-info-circle">
  Create the adapter connection in Axonius. Based on the authentication method you're using (Client Credentials Flow or Username-Password flow), fill out the specific required fields, and configure optional settings.

  1. Navigate to the **Adapters** page → search for `Salesforce` → click on the adapter tile.

     ![](https://files.readme.io/af02b27a6f11c5a763179c1584c0b8fb15801114678851b57fe3ecd98a6fdf3c-image.png)
  2. On the top right side, click on **Add Connection**. The **Add Connection** drawer opens.

  ### Required Fields

  <Tabs>
    <Tab title="Client Credentials Flow">
      * **Domain** - The full URL of the Salesforce server.
      * **Consumer Key**
      * **Consumer Secret**

        <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/salesforce_client%20cred%20flow.png" width="500px" />
    </Tab>

    <Tab title="Username-Password Flow">
      * **Domain** - The full URL of the Salesforce server.
      * **Consumer Key**
      * **Consumer Secret**
      * **User Name** and **Password** - The credentials for a user account that has the required permissions to fetch assets.
      * **User Secret** - The Salesforce security token associated with a user account to fetch assets. This is only required if you didn't provide a list of trusted IP ranges when creating a user profile.
        <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/salesforce_us%20psw%20flow.png" width="500px" />
    </Tab>
  </Tabs>

  ### Required Fields When Fetching Application Settings and Licenses

  When fetching these asset types, **in addition to** one of the authentication flows listed above, you must also provide the following parameters:

  * **2FA Secret Key** - The secret generated in Salesforce when setting up 2-factor authentication for the Salesforce user created for collecting Application Settings and Licenses. For more information on how to generate this secret key, expand the following section:

  <Accordion title="Setting Up Two-Factor Authentication" icon="fa-info-circle">
    If your Salesforce login process requires 2-factor authentication, follow these steps to generate a secret key. Then, use the generated key to populate the **2FA Secret Key** parameter in Axonius.

    **In Salesforce:**

    1. On the **Connect Salesforce Authenticator** screen, select **Choose Another Verification Method**.

    <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Salesforce_2FA_AnotherVerification.png" width="300px" />

    <br />

    2. Select **Use verification codes from an authenticator app**.

    3. Click **Continue**.

       <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Salesforce_2FA_UseVerification.png" width="300px" />

    4. Click **I can’t Scan the QR Code**.

       <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Salesforce_2FA_CantScan.png" width="300px" />

    5. The next screen displays a one-time secret key. **Copy this key to a safe place (your password vault is recommended if you use one) for later use.**

       <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Salesforce_2FAKey.png" width="300px" />

    From here, you can complete the process with either the built-in Axonius 2FA Authenticator, or with an external Authenticator app.

    **To complete the process with Axonius 2FA Authenticator:**

    1. On the adapter's **Create Connection** screen, click the **Generate Secret Key** icon. The Set 2FA Secret Key screen opens.

       <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-SX7EXZS2.png" width="300px" />

    2. Enter the secret key you copied in step 5 above into the 2FA Secret Key field and click **Next**.

    3. The system displays a 6-digit code for you to copy.

       <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ONFRHRQD.png" width="300px" />

    4. Back in Axonius, paste the 6-digit code in the 2FA Secret Key field to get a verification code.

    5. Back in Salesforce, paste the verification code and click **Connect**.

       <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1148HTUE.png" width="300px" />

    **To complete the process with an external Authenticator app (such as Google Authenticator):**

    1. Back in Axonius, paste the one-time secret key you copied from Salesforce in the **2FA Secret Key** field.
    2. In your authenticator app, paste the same key and copy the one-time verification code.
    3. Back in Salesforce, paste the verification code and click **Connect**.
  </Accordion>

  * **SSO Username** and **SSO Password** - If your organization accesses Salesforce with an SSO provider (such as Google, Microsoft 365, Okta, etc.). enter your credentials for the SSO platform here.
  * **Use Unified Login Domain** - An alternative to using SSO credentials. Enable this option to use the `http://login.salesforce.com` URL for logging in instead of `sub-domain.salesforce.com` (if the main domain is a sandbox, the URL will be `test.salesforce.com`). This allows you to directly login with Salesforce credentials instead of using an external SSO.

  ### Optional Parameters

  * **Verify SSL -** Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust and CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
  * **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
  * **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
</Accordion>

### 3.2. Test the New Connection

It is recommended to use Curl commands to check the credentials you defined in the previous steps, to make sure they work for fetching Salesforce data with this adapter.

<Accordion title="Testing" icon="fa-info-circle">
  1. Open a terminal window.
  2. Enter the following command and replace the variables in angled brackets with the client credentials you generated in the adapter setup process:<br />
     `consumer_key='<consumer_key>'`<br />
     `consumer_secret='<consumer_secret>'`<br />
     `domain='https://.salesforce.com'`<br />
     `curl -X POST -u "$consumer_key":"$consumer_secret" "$domain/services/oauth2/token?grant_type=client_credentials"`<br />
     The command’s output indicates if the credentials are valid.<br />
  3. Enter the following command and replace the variables in the angled brackets with the Salesforce username and password you are associating with this adapter:<br />
     `username='<username>'`<br />
     `password='<password>'`<br />
     `user_secret='<user_secret>'`<br />
     `consumer_key='<consumer_key>'`<br />
     `consumer_secret='<consumer_secret>'`<br />
     `domain='https://.salesforce.com'`<br />
     `curl -X POST "$domain/services/oauth2/token" -d "grant_type=password&username=$username&password=$password$user_secret&client_id=$consumer_key&client_secret=$consumer_secret"`<br />
     The command’s output indicates if the username and password are valid.<br />
</Accordion>

<Accordion title="Troubleshooting" icon="fa-info-circle">
  Here’s how you can troubleshoot some of the common error messages that are output by the curl commands in the previous section.

  * **Client credentials flow not enabled** - Make sure that the Enable Client Credentials Flow check box is checked for the application you are using for this adapter.
  * **No client credentials user enabled** - Make sure that there is a value selected for ‘Run As’ in the app’s Client Credentials Flow section.
  * **Client identifier invalid** - Indicates that the consumer key or consumer secret is not right. Check to make sure the consumer key and consumer secret values were copied correctly.
  * **Authentication failure** - Check to make sure that the correct username and password were entered.
</Accordion>

## 4. (Optional) Configure Advanced Settings

Refer to [Salesforce Advanced Settings](https://docs.axonius.com/axonius-help-docs/docs/salesforce-advanced-settings).