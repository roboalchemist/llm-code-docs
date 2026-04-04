# Source: https://docs.api7.ai/enterprise/best-practices/scim/okta.md

# Source: https://docs.api7.ai/enterprise/best-practices/dashboard-sso/saml/okta.md

# Dashboard SSO using SAML with Okta

Single Sign-On (SSO) allows users to access multiple applications using a single set of credentials, streamlining the authentication process. In API7 Enterprise, SSO supports multiple protocols and provides the capability to manage users by importing them from existing identity providers.

This guide walks you through configuring Single Sign-On (SSO) for the API7 Enterprise Dashboard using Okta as the identity provider via the SAML protocol, and setting up role mappings for imported users.

## Set Up SSO Integration[â](#set-up-sso-integration "Direct link to Set Up SSO Integration")

This section guides you through configuring Single Sign-On (SSO) for the API7 Enterprise Dashboard using Okta as the identity provider.

### Configure Okta[â](#configure-okta "Direct link to Configure Okta")

This section describes example configuration in Okta. If you are using a different identity provider (IdP), refer to your IdP's documentation and adjust the configuration accordingly.

1. In Okta Admin Console, navigate to **Applications** > **Applications**, then click **Create App Integration**. Select **SAML 2.0**, then click **Next**.

![Create a SAML app integration in Okta](https://static.api7.ai/uploads/2026/01/23/ymVmidRe_1-okta-saml-create-select.png)

2. In **General Settings**, set the application name, for example, `API7 SAML`, and click **Next**.

![Configure general settings](https://static.api7.ai/uploads/2026/01/23/9mlIMCLx_2-okta-saml-create-step-1.png)

3. In **Configure SAML**, set the following values, then click **Next**:

   <!-- -->

   1. **Single sign-on URL**: set a placeholder, for example, `http://placeholder`. You will update this value after creating the login option in API7 Dashboard.
   2. Enable **Use this for Recipient URL and Destination URL**.
   3. **Audience URI (SP Entity ID)**: set a unique identifier, for example, `api7`. This value must match the **Entity ID** in API7 Dashboard.

![Configure SAML settings with placeholder values](https://static.api7.ai/uploads/2026/01/23/1I6SOQdG_3-okta-saml-step-4-set-placeholder-to-pass-config.png)

4. In **Feedback**, select **This is an internal app that we have created**, then click **Finish**.

![Finish the SAML integration wizard](https://static.api7.ai/uploads/2026/01/23/h2WJj4Bp_4-okta-saml-create-step-3.png)

5. In the application **Sign On** tab, copy the **Metadata URL**. You will use it in API7 Dashboard.

![Copy metadata URL](https://static.api7.ai/uploads/2026/01/23/AosDAjeC_5-okta-saml-copy-metadata-url.png)

6. In the **Sign On** tab, add the following **Attribute Statements**:

   <!-- -->

   * `email`: `user.profile.email`
   * `name`: `user.profile.displayName`
   * `username`: `user.profile.login`

![Add attribute statements](https://static.api7.ai/uploads/2026/01/23/XqTB2DtX_6-okta-saml-add-attrbute-mapping.png)

### Create a Dashboard Login Option[â](#create-a-dashboard-login-option "Direct link to Create a Dashboard Login Option")

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Click **Add Login Option**.

![Add login option in API7 Dashboard](https://static.api7.ai/uploads/2026/01/23/dH8x8EPj_7-okta-saml-dash-add-login-options.png)

3. Fill in the configuration:

* **Name**: The unique login name. The name should be identifiable for users. For example, if you configure the name to be `okta-saml`, you will see `Login with okta-saml` on the Dashboard login page.

* **Provider**: choose `SAML`.

* **Identity Provider Metadata URL**: The Okta metadata URL copied earlier.

* **Service Provider Root URL**: The root URL of your Service Provider. Typically, it is the API7 Dashboard address, for example, `https://dashboard.your-company.com`.

* **Entity ID**: The unique identifier that matches the **Audience URI (SP Entity ID)** configured in Okta, for example, `api7`.

* **Attributes Mapping**: API7 user fields mapping to SAML claims. For example:

  <!-- -->

  * **username**: `username`
  * **email**: `email`
  * **name**: `name`

![Configure SAML login option](https://static.api7.ai/uploads/2026/01/23/lxTxe0Jv_8-okta-saml-dash-add-config-saml.png)

4. Optional: Enable **Role Mapping** and configure a rule to map an Okta attribute to an API7 role.

![Configure role mapping](https://static.api7.ai/uploads/2026/01/23/lvgiP8KY_9-okta-saml-dash-attributes-mapping-role-mapping.png)

5. Click **Add**.
6. In the new SAML login option, copy the **Service Provider ACS URL**.

![Copy Service Provider ACS URL](https://static.api7.ai/uploads/2026/01/23/FO5RpBsL_10-okta-saml-dash-cp-acs-url.png)

### Update Okta with the ACS URL[â](#update-okta-with-the-acs-url "Direct link to Update Okta with the ACS URL")

1. Return to the Okta application and open the **Sign On** tab.
2. Click **Edit** in the **SAML Settings** section.
3. Update **Single sign-on URL** with the **Service Provider ACS URL** copied from API7 Dashboard, then save the changes.

![Update Single sign-on URL](https://static.api7.ai/uploads/2026/01/23/P7VmXfGc_11-okta-saml-update-sso-url.png)

### Assign Users to the Okta App[â](#assign-users-to-the-okta-app "Direct link to Assign Users to the Okta App")

1. In the Okta application, open the **Assignments** tab.
2. Click **Assign** and select **Assign to People**.
3. Select the users who should access API7 Dashboard, then click **Done**.

![Assign users in Okta](https://static.api7.ai/uploads/2026/01/23/LetUWPXP_12-okta-saml-assign-to-people.png)

### Verify SSO Login[â](#verify-sso-login "Direct link to Verify SSO Login")

1. Open the API7 Dashboard login page and select **Login with okta-saml**.

![Select the SAML login option](https://static.api7.ai/uploads/2026/01/23/Tk35XItL_13-okta-saml-dash-select-saml-login-option.png)

2. Sign in with your Okta credentials.

![Okta sign-in page](https://static.api7.ai/uploads/2026/01/23/IO5APWVQ_14-okta-saml-login.png)

3. Wait for the redirect to complete.

![Redirecting to API7 Dashboard](https://static.api7.ai/uploads/2026/01/23/5BI2RYnZ_15-okta-saml-waiting-redirecting.png)

4. Confirm that you can access the API7 Dashboard, and verify the role mapping if you enabled it.

![Logged in to API7 Dashboard](https://static.api7.ai/uploads/2026/01/23/kmizSr6O_16-okta-saml-logged-in.png)

### Enable Sign Request[â](#enable-sign-request "Direct link to Enable Sign Request")

If you want API7 Dashboard to sign SAML authentication requests, enable **Sign Request** and configure Okta with the API7 certificate.

1. In the SAML login option, enable **Sign Request**. If no certificate is configured, API7 Dashboard generates one automatically. You can optionally upload your own certificate and private key. Save the changes and copy the certificate value for Okta.

![Save the certificate in API7 Dashboard](https://static.api7.ai/uploads/2026/01/23/CsLkD48I_1-okta-saml-sigining-request-dash-cp-save-cert.png)

2. In the Okta application **General** tab, click **Edit** in **SAML Settings**.

![Edit SAML settings in Okta](https://static.api7.ai/uploads/2026/01/23/sQ29qBaL_2-okta-saml-sigining-request-edit.png)

3. Update **Name ID format**.

![Change Name ID format](https://static.api7.ai/uploads/2026/01/23/ihgleRUO_3-okta-saml-sigining-request-change-name-id-format.png)

4. Upload the certificate copied from API7 Dashboard to the **Signature Certificate** section, enable signed requests, and save the changes.

![Upload certificate to Okta](https://static.api7.ai/uploads/2026/01/23/1DrBFDLl_4-okta-saml-sigining-request-upload-cert.png)

5. Sign in again to verify the signed request flow.

![Logged in with signed requests](https://static.api7.ai/uploads/2026/01/23/ewd1camh_5-okta-saml-sigining-request-logged.png)

### Configure via Group Membership[â](#configure-via-group-membership "Direct link to Configure via Group Membership")

Use Okta group membership to map API7 roles based on the `groups` attribute in the SAML assertion.

1. In Okta Admin Console, navigate to **Directory** > **Groups**, click **Add Group**, and create a group such as `group_1`.

![Create an Okta group](https://static.api7.ai/uploads/2026/01/26/XOSWF1OV_1-okta-saml-group-add.png)

2. Confirm the group is created and open the group details.

![Check the group details](https://static.api7.ai/uploads/2026/01/26/WvV9QICf_2-okta-saml-group-check.png)

3. Click **Add People** and add users.

![Add people to the group](https://static.api7.ai/uploads/2026/01/26/VNn76fcW_3-okta-saml-group-add-people.png)

4. In the Okta app **Assignments** tab, click **Assign** and select **Assign to Groups**, then assign the `group_1` group to the app.

![Assign the group to the app](https://static.api7.ai/uploads/2026/01/26/sRhrZqgD_4-okta-saml-group-assign.png)

5. In the Okta app **Sign On** tab, edit **SAML Settings** and add a **Groups Attribute Statement**:

   <!-- -->

   * **Name**: `groups`
   * **Filter**: `user.getGroups({"group.profile.name": {"group_1"}}).![profile.name]`. Please refer to [Okta Group functions](https://developer.okta.com/docs/reference/okta-expression-language-in-identity-engine/#group-functions) for more details.

![Add the groups attribute statement](https://static.api7.ai/uploads/2026/01/26/8H1b6x4n_5-okta-saml-group-set-groups-attribute.png)

note

To inspect the SAML assertion, use a browser SAML tracing extension (for example, `SAML-tracer`). After you click the SAML login option in API7 Dashboard, capture the `POST /xxxx/acs` request and view the decoded assertion as shown.

![Check POST ACS Return](https://static.api7.ai/uploads/2026/01/26/Ow8ci3Kh_okta-saml-group-post-acs-return.png)

Use the `groups` value in this payload to configure role mapping in API7 Dashboard.

6. In API7 Dashboard, open the SAML login option, enable **Role Mapping**, and add a rule:

   <!-- -->

   * **Internal Role**: `Super Admin` (or another role)
   * **Role Attribute**: `groups`
   * **Operation**: `Exact Match in Array`
   * **Role Value**: `group_1`

![Edit role mapping in API7 Dashboard](https://static.api7.ai/uploads/2026/01/26/8xtyp7b7_6-okta-saml-group-dash-edit-role-mapping.png)

7. Save the login option and confirm the mapping rule is listed.

![Check role mapping in API7 Dashboard](https://static.api7.ai/uploads/2026/01/26/qkv5awSq_7-okta-saml-group-dash-check-role-mapping.png)

8. Log in with a user in the Okta group and confirm the role is applied.

![Log in and verify role mapping](https://static.api7.ai/uploads/2026/01/26/ncNqyg6V_8-okta-saml-group-dash-login.png) ![Verify role mapping](https://static.api7.ai/uploads/2026/01/26/Pg6od84y_9-okta-saml-group-dash-check-roles.png)

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Roles and Permission Policies](https://docs.api7.ai/enterprise/key-concepts/roles-and-permission-policies.md)

* Getting Started
  <!-- -->
  * [Create Custom Role](https://docs.api7.ai/enterprise/getting-started/create-custom-role.md)

* Best Practices

  <!-- -->

  * [Dashboard SSO using LDAP](https://docs.api7.ai/enterprise/best-practices/dashboard-sso/ldap.md)
  * [Configure Dashboard SSO with Microsoft Entra ID](https://docs.api7.ai/enterprise/best-practices/dashboard-sso/saml/azure-ad.md)
