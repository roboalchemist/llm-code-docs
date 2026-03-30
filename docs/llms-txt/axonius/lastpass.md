# Source: https://docs.axonius.com/docs/lastpass.md

# LastPass

LastPass is a password manager that stores encrypted passwords online.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS data

## Parameters

1. **Account Type** *(required, default: LastPass API)* - Select the Account Type from the dropdown.
   * If the Account Type selected is **LastPass API**, the following parameters are displayed:
     1. **Host Name or IP Address** *(required, default: `https://identity-api.lastpass.com`)* - The hostname or IP address of the LastPass server that Axonius can communicate via the [Required Ports](#required-ports).
     2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
     3. **Public Key File** and  **Private Key File** *(required)* - Click **Choose file** to upload the Public key file and Private key file, used for authentication. For more information, refer to [Generating Keys](#generating-keys).

![lastPassAPI](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/lastPassAPI.png)

* If the Account Type selected is **LastPass Business API**, the following parameters are displayed:
  1. **Host Name or IP Address** *(required, default: `https://lastpass.com`)* - The hostname or IP address of the LastPass server that Axonius can communicate via the [Required Ports](#required-ports).

  2. **CID (Account number)** *(required)* - Specify the CID (account number) used to make requests to the LastPass Business API.

  3. **Provisioning hash** *(required)* - Specify the provisioning hash used to make requests to the LastPass Business API.
     To obtain the CID and provisioning hash, see [Generating the CID and Provisioning Hash](/docs/lastpass#generating-the-cid-and-provisioning-hash).

![lastpassbusinees](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/lastpassbusinees.png)

4. **Username** and **Password** *(only used to fetch SaaS data)* Credentials for an account dedicated to Axonius SaaS Applications to fetch SaaS data only.

5. **2FA Secret Key** *(only used to fetch SaaS data)* - The secret generated in the adapter for setting up 2-factor authentication for the adapter  user created to collect SaaS data.

6. **Verify SSL**  - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).

7. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

8. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![LsstPassSM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LsstPassSM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch only Enabled Accounts** - Select whether to only fetch accounts that are enabled.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius integrates with APIs for LastPass Personal and LastPass Business accounts.

* If you have a LastPass Personal account, you can use the legacy [ LastPass Plain Auth API](https://mfa-developer.lastpass.com/index.html@p=263.html).
* If you have a LastPass Business account, use the [LastPass Business API](https://admin.lastpass.com/advanced/enterpriseApi/api-reference).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.

## Adapter Integration Setup

### Generating Keys

**For LastPass API authenication using Axonius CyberSecurity Asset Management**
**To generate key files**

1. Navigate to the LastPass Portal [LastPass Portal](https://identity.lastpass.com/Keys).
2. From the left pane, select **Advanced Options**.
3. From the submenu, select **Keys**. The Keys Management page is displayed.

<Image alt="lastpasskeys.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/lastpasskeys.png" />

4. Under Existing Keys, from the **Generic API** row, click **Refresh** (1). When requested to download **public-key.cer**, save this file to your system.
5. Click the yellow **Download** (2) button. When requested to save the **private-key.cer**, save this file to your system.
6. Click the green **Copy** (3) button to copy the API key.

### Step 1: Create a staged user account

<Callout icon="💡" theme="warn">
  Relevant only to Axonius SaaS Applications. Write permissions are needed to fetch SaaS data
</Callout>

1. Login into **LastPass** as an administrator and navigate to **Admin Console `>` Users**.
2. Click on **Add User**. In the opened side panel do the following:
   1. Select Stage: **Add to company without sending activation email**
   2. Enter an email address that you have credentials for.

<Callout icon="📘" theme="info">
  Note

  Copy the **email address**, that is required for the [Username](#connection-parameters) adapter configuration parameter.
</Callout>

3. Click on **Add Users**
4. Go to **Admin levels** and click on **Admin**. In the opened side panel, click on **Assign users**, select the newly created staged user account, and click on **Assign users**.

### Step 2: Exclude from multi-factor authentication policies

<Callout icon="📘" theme="info">
  Note

  Relevant only to Axonius SaaS Applications.
  Skip this step if multi-factor authentication is disabled.
</Callout>

1. Go to the **LastPass Admin Console `>` Users `>` General Policies**.
2. Use the Search policies bar to find MFA policies. For any Enabled policy found, click the policiy to add the newly created user account to its exclusion list:
   1. Click on **Edit policy users**.
   2. Select **All except these user/groups**.
   3. Click **Assign users & groups**.
   4. In the **Users** tab, select the newly created user and click on **Assign Users**.
   5. Click on **Back** and save the changes.

### Step 3: Activate the user account

Relevant only to Axonius SaaS Applications.

1. Go to the **LastPass Admin Console `>` Users**.
2. Select the newly created staged user account and click on **Activate user**.
3. Login to the user’s email account and complete the LastPass registration process.

<Callout icon="📘" theme="info">
  NOTE

  Copy the **new master password**, that is required for the [Password](#connection-parameters) adapter configuration parameter.
</Callout>

### Generating the CID and Provisioning Hash

**To generate the CID and provisioning hash**

1. Log in with your email address and master password to access the new Admin Console at the [LastPass Login Page](https://admin.lastpass.com).
2. Navigate to the **Dashboard** tab. The CID (account number) is located at the top of the page, preceded by the words "Account number". Jot down the CID information, as you will subsequently need it.
3. Navigate to **Advanced `>` Enterprise API**.
4. Do one of the following:
   * If you have not previously created your provisioning hash, click **Create provisioning hash `>` OK**.  The provisioning hash appears at the top of the page.
   * If you previously created your provisioning hash but have since forgotten it, generate a new one.

<Callout icon="📘" theme="info">
  Warning

  If you have already created a provisioning hash, then generating a new hash will invalidate the previous hash, and will require you to update all integrations with the newly generated hash.
  To proceed with creating a new provisioning hash, click **Reset your provisioning hash `>` OK**. Your new provisioning hash is displayed at the top of the page.
</Callout>

<Callout icon="📘" theme="info">
  Note

  Update all integrations that used the previous provisioning hash.
</Callout>

## **Related Enforcement Actions**

[LastPass - Disable Users](/docs/disable-lastpass-user)