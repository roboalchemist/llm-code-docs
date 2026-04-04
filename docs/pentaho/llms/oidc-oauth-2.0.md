# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/oidc-oauth-2.0.md

# OIDC / OAuth 2.0

## Prerequisites <a href="#prerequisite" id="prerequisite"></a>

The security provider must have users, roles, and passwords correctly established by the Administrator prior to implementation.

The newly integrated OAuth authentication mechanism utilizes OIDC-based `authorization_code` authentication, while the security provider will handle the authorization.

Users have the flexibility to configure multiple OAuth providers.

To enable OAuth functionality with Pentaho login, make the following changes:

1. Enable OAuth & specify Security Provider
2. Update OIDC Configuration

## Enable OAuth & Specify Security Provider <a href="#importance-of-the-applicationcontext-spring-security-oauth.properties-file" id="importance-of-the-applicationcontext-spring-security-oauth.properties-file"></a>

For this Step you will be updating `<PENTAHO_HOME>/pentaho-server/pentaho-solutions/system/security.properties`.

OAuth is disabled by default with `enable-oauth-authentication=false`. Administrators can enable it by setting this flag to true: `enable-oauth-authentication=true`.

Next, you will need to establish the security provider.&#x20;

#### Specify Security Provider

Jackrabbit and LDAP serve as **security providers** while OAuth functions solely as an **authentication mechanism** in Pentaho Server. Please contact support to understand why these choices were made.

In order to specify the security provider, you must first decide the approach for managing user-role mappings.

1. If you expect to **manage user roles in Pentaho, then set `provider=jackrabbit`.** You will then have to assign roles to users in Pentaho User Console. See \<link> for details.
2. If you expect to manager user roles in LDAP, then \<waiting for input from Sathish and Vamsi to complete this>.

## Update OIDC Configuration <a href="#importance-of-the-applicationcontext-spring-security-oauth.properties-file" id="importance-of-the-applicationcontext-spring-security-oauth.properties-file"></a>

For this step, you will be updating `<PENTAHO_HOME>/pentaho-server/pentaho-solutions/system/applicationContext-spring-security-oauth.properties`

`applicationContext-spring-security-oauth.properties` is the **central configuration file** for OAuth2/OIDC authentication in Pentaho 11.0. It serves as the primary interface for administrators to:

* Enable/disable **OAuth authentication**
* Configure **multiple Identity Providers** simultaneously
* Set up client registrations for different IdPs (Keycloak, Okta, Azure, etc.)

**Core Identity Properties:**

1. `registration-id` - Unique identifier for the IdP configuration.
2. `client-name` - Display name for the IdP
3. `client-id/client-secret` - OAuth2 client credentials from the IdP
4. `position` - Display order on the login page
5. `user-name-attribute-name` - used for mapping with username created by administrator in Pentaho jackrabbit/LDAP.
6. `authorization-grant-type` - Auth flow type. By default, `authorization_code` is the OAuth2 flow type.
7. `scope` - Requested permissions (typically `openid,profile,email`). Scopes ensure IDP access token has necessary data

**The** `registration-id` **value must match the prefix used for all related properties.**

For e.g., `keycloak.registration-id=keycloak` ,

Then **ALL** related properties for that IdP must use the `keycloak.` prefix:

`keycloak.registration-id=keycloak keycloak.client-name=keycloak keycloak.client-id=your-client-id keycloak.client-secret=your-client-secret keycloak.scope=openid,profile,email keycloak.redirect-uri=http://... keycloak.token-uri=http://...`

**OIDC Endpoints:**

1. `token-uri` - IdP's token endpoint
2. `authorization-uri` - IdP's authorization endpoint
3. `jwk-set-uri` - IdP's public keys for token validation
4. `user-info-uri` - IdP's user information endpoint
5. `redirect-uri` - Callback URL after IdP authentication
6. `end-session-endpoint` - Logout endpoint for IdP
7. `post-logout-redirect-uri` - Redirection uri after IDP session is logged out

Once the above steps are completed and you restart Pentaho Server, the login screen should show options to login via the IdP(s) you have configured above. For example, if Azure Entra, Keycloak, and Okta are all configured you will see the following:

<figure><img src="https://1041214956-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiFWuQjAZNxh1EoQbRnsT%2Fuploads%2F0ZWxJDTQjiPFjN7TMPYi%2Fimage.png?alt=media&#x26;token=a611c4a3-9e7c-46ae-b1c1-685e38bce8f0" alt=""><figcaption></figcaption></figure>

OR (if you have the new experience configured):

<figure><img src="https://1041214956-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiFWuQjAZNxh1EoQbRnsT%2Fuploads%2FvEkvNObYNw9DLec4FbgX%2Fimage.png?alt=media&#x26;token=131374bc-1f90-43e3-b0c2-54a90124d983" alt=""><figcaption></figcaption></figure>
