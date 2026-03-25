# Source: https://docs.axonius.com/docs/identity-providers-settings.md

# Managing LDAP and SAML

<br />An Axonius Admin user can enable login based on a broad range of supported identity access management providers. These identity providers can handle authentication and authorization using existing credentials of your organization to a Single Sign On solution (SSO). All are disabled by default.

Once enabled and configured, a designated login button appears in the Axonius login page, for example:

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(286).png" />

Axonius supports the following identity provider formats:

* LDAP
* SAML

**To enable an identity provider and configure its credentials:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Access Management**, and select **LDAP & SAML**.
3. Turn on the toggle for the identity provider you want to use: **Allow LDAP logins**, **Allow SAML-based logins**.
4. Configure the parameters for the identity provider.
   * [LDAP Login Settings](/docs/ldap-login-settings)
   * [SAML-Based Login Settings](/docs/saml-based-login-settings)

## Role Assignment Rules Logic

When a new or existing user logs in to Axonius with LDAP or SAML, the user's assigned role is determined based on the following logic:

| # | New / Existing User | User’s Assigned Role             | Evaluate role assignment on Value                                                                                                                      | Role Assignment Rules                                                                                                                   | New User’s Assigned Role                                                                                                                                                                   |
| - | ------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | New user            | N/A (logs in for the first time) | Any value: <br /> - New users only  <br />- New and existing users                                                                                     | Either one of the following: <br /> - No assignment rules configured  <br />- Assignment rules configured, but no matching rule found   | The value in the **Default role for new LDAP user (if no matching assignment rule found)** field or in the **Default role for new SAML user (if no matching assignment rule found)** field |
| 2 | New user            | N/A (logs in for the first time) | Any value:  <br /> - New users only  <br /> - New and existing users                                                                                   | Assignment rules configured and a matching rule found                                                                                   | Based on the first matching rule                                                                                                                                                           |
| 3 | Existing user       | Role X                           | New users only or the **[Add Ignore role assignment rules](/docs/manage-users#editing-an-existing-user)** checkbox, under the user settings is enabled | N/A   <br />– assignment rules will not be evaluated                                                                                    | Assigned role will remain as is (Role X)                                                                                                                                                   |
| 4 | Existing user       | Role X                           | New and existing users                                                                                                                                 | Either one of the following:  <br /> - No assignment rules configured  <br /> - Assignment rules configured, but no matching rule found | Assigned role will remain as is (i.e., Role X)                                                                                                                                             |
| 5 | Existing user       | Role X                           | New and existing users                                                                                                                                 | Assignment rules configured and a matching rule found                                                                                   | Based on the first matching rule                                                                                                                                                           |