# Source: https://docs.api7.ai/enterprise/3.8.x/api-portal/developer-sso.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-portal/developer-sso.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-portal/developer-sso.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-portal/developer-sso.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-portal/developer-sso.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-portal/developer-sso.md

# Support Developer Portal SSO

API7 Portal can be configured to support Single Sign-On (SSO) for seamless login for both internal and partner developers, enhancing user experience and security.

* SSO is typically not recommended for public developers, as it may require them to create accounts with your organization's identity provider.
* Developer SSO configuration is independent of the API7 Enterprise SSO used for API7 Gateway users and API providers.

## Integrate with SSO[â](#integrate-with-sso "Direct link to Integrate with SSO")

For internal API7 Portals where both API providers and developers belong to the same organization, a single Identity Provider (IDP) can be integrated to support both Developer SSO and API7 Enterprise SSO.

* LDAP
* OIDC
* SAML

1. Switch to API7 Provider Portal using the button on the top-left corner of the navigation bar.

2. Select **Login Settings** from the side navigation bar, then select **Login Options** tab.

3. Click **Add Login Option**.

4. Fill in the form:

   <!-- -->

   * **Name**: the unique login name. The name should be identifiable for users. For example, if you configure the name to be `Employee Account`, you will see `Login with Employee Account` option in the Dashboard login.
   * **Provider**: choose `LDAP`.
   * **Host**: the LDAP host domain. For example, `ldap.example.com`.
   * **Port**: For example, `1563`.
   * **Base Distinguished Name**: For example, `oc=users,dc=org,dc=example`.
   * **Bind Distinguished Name**: the LDAP Bind Distinguished Name (DN) used to perform LDAP search for the user. This LDAP Bind DN should have permissions to search for the user being authenticated. For example, `cn=admin,dc=org,dc=example`.
   * **Bind Password**: the LDAP bind password used to authenticate with the LDAP server.
   * **Identifier**: the attribute used to identify LDAP users. For example, `cn`.
   * **Attributes Mapping**: map API7 internal fields to related LDAP attributes to seamlessly integrate and synchronize data.

5. Click **Add**.

1) Switch to API7 Provider Portal using the button on the top-left corner of the navigation bar.

2) Select **Login Settings** from the side navigation bar, then select **Login Options** tab.

3) Click **Add Login Option**.

4) Fill in the form:

   <!-- -->

   * **Name**: the unique login name. The name should be identifiable for users. For example, if you configure the name to be `Employee Account`, you will see `Login with Employee Account` option in the Dashboard login.
   * **Provider**: choose `OIDC`.
   * **Issuer**: the identifier of the OpenID Connect provider. For example, `https://accounts.example.com`.
   * **Client ID**: the unique identifier of your application, assigned by the OIDC provider. For example, `API7`.
   * **Client Secret**: secret key used for authentication, assigned by the OIDC provider.
   * **Request Scope**: Access tokens often possess different scopes, which limit their usage. For example, `profile,email`.
   * **Root URL**: the URL used to access API7 for generating callback URL. For example, `https://auth.example.com/oidc`.
   * **SSL verify**: default value is enabled.

5) Click **Add**.

1. Switch to API7 Provider Portal using the button on the top-left corner of the navigation bar.

2. Select **Login Settings** from the side navigation bar, then select **Login Options** tab.

3. Click **Add Login Option**.

4. Fill in the form:

   <!-- -->

   * **Name**: the unique login name. The name should be identifiable for users. For example, if you configure the name to be `Employee Account`, you will see `Login with Employee Account` option in the Dashboard login.
   * **Provider**: choose `SAML`.
   * **Identity Provider Metadata URL**: URL used to obtain information about the Identity Provider, such as its public key, supported SAML versions, signature algorithms, etc. For example, `https://idp.example.com/metadata`.
   * **Service Provider Root URL**: the entity that requests authentication and authorization from the Identity Provider (IdP). For example, `https://sp.example.com`.
   * **Entity ID**: a unique identifier for the Service Provider (SP) or Identity Provider (IdP) entity. It typically serves as a globally unique identifier for the entity within the SAML federation. For example, `https://sp.example.com/saml/metadata`.

5. Click **Add**.

## Sync Developer Data from IdP[â](#sync-developer-data-from-idp "Direct link to Sync Developer Data from IdP")

SCIM (System for Cross-domain Identity Management) is a protocol that can be used to synchronize user and group information from the original Identity Provider (IdP) to API7 Enterprise. This can eliminate the need to manually manage developer and group information in multiple systems, which can save time and reduce the risk of errors.

With SCIM Provisioning, API7 Enterprise automatically synchronizes developer data whenever a new user is registered or deleted in your IdP.

note

When using a single Identity Provider (IDP) for both Developer SSO and API7 Enterprise SSO, ensure separate SCIM configurations are defined for each.

1. Switch to API7 Provider Portal using the button on the top-left corner of the navigation bar.

2. Select **Login Settings** from the side navigation bar, then select **SCIM** tab.

3. Click **Enable**.

4. Copy the `API7 SCIM Endpoint URL` and `SCIM Token`.

5. Configure Your IdP (if it supports SCIM):

   <!-- -->

   * Log in to your IdP administration console.
   * Locate the SCIM configuration settings (these may vary depending on your IdP).
   * Paste the copied API7 SCIM Endpoint URL and SCIM Token into the appropriate fields.
   * Save your configuration changes and configure them on your IdP side (make sure your IdP supports SCIM protocol).

### Delete a Developer Login Option[â](#delete-a-developer-login-option "Direct link to Delete a Developer Login Option")

warning

Deleting a login option will result in the removal of all developers associated with it.

1. Switch to API7 Provider Portal using the button on the top-left corner of the navigation bar.
2. Select **Login Settings** from the side navigation bar, then select **Login Options** tab.
3. Click **Delete** of the target login option.
4. Double-confirm.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Developers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/developers.md)
