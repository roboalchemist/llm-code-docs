# Source: https://directus.io/docs/raw/configuration/auth-sso.md

# Auth & SSO

> Configuration for authentication methods, including local email/password, OAuth 2.0, OpenID, LDAP, and SAML.

<partial content="config-env-vars">



</partial>

Directus offers a variety of authentication methods, including local email/password, OAuth 2.0, OpenID, LDAP, and SAML.

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        AUTH_PROVIDERS
      </code>
    </td>
    
    <td>
      A comma-separated list of auth providers. You can use any names you like for these keys.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_DISABLE_DEFAULT
      </code>
    </td>
    
    <td>
      Disable the default auth provider.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_ALLOWED_PUBLIC_URLS
      </code>
    </td>
    
    <td>
      A comma-separated list of allowed API PUBLIC_URLs used to generate <code>
        OAuth 2.0
      </code>
      
       / <code>
        OpenID
      </code>
      
       SSO callback URLs. This is useful for multi-domain deployments.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

For each of the auth providers listed, you must provide the following configuration (variable name must be uppercase in these options):

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_DRIVER
      </code>
    </td>
    
    <td>
      Which driver to use, either <code>
        local
      </code>
      
      , <code>
        oauth2
      </code>
      
      , <code>
        openid
      </code>
      
      , <code>
        ldap
      </code>
      
      , <code>
        saml
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_MODE
      </code>
    </td>
    
    <td>
      Whether to use <code>
        'cookie'
      </code>
      
       or <code>
        'session'
      </code>
      
       authentication mode when redirecting. Applies to the following drivers <code>
        oauth2
      </code>
      
      , <code>
        openid
      </code>
      
      , <code>
        saml
      </code>
      
      .
    </td>
    
    <td>
      <code>
        session
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

Cookie and session configuration settings such as `REFRESH_TOKEN_COOKIE_*`, `SESSION_COOKIE_*`, and related security parameters can be found in [Security & Limits](/configuration/security-limits).

</callout>

Based on your configured drivers, you must also provide additional variables, where `<PROVIDER>` is the capitalized name of the item in the `AUTH_PROVIDERS` value.

<callout icon="material-symbols:warning-rounded" color="warning">

**PUBLIC_URL and AUTH_ALLOWED_PUBLIC_URLS**

- Our `oauth2`, `openid` and `saml` SSO drivers rely on `PUBLIC_URL` for redirection, with `oauth2` and `openid` also using it for the callback URL generation. If set incorrectly, the login process for these drivers may behave unexpectedly.
- In environments where the API is accessible from multiple domains, `AUTH_ALLOWED_PUBLIC_URLS` should be configured for the domains you wish to support SSO sign-in. When a request's origin matches an entry, the corresponding PUBLIC_URL is used for the login flow. If no match is found, the default `PUBLIC_URL` is used instead.

**Example:**

```text
PUBLIC_URL="https://<your_primary_domain>"
AUTH_ALLOWED_PUBLIC_URLS="https://<your_secondary_domain>,https://<your_tertiary_domain>"
```

**Cookie Limitations**

- Subdomains of the same parent domain: Since they share a common parent domain (e.g. `api.example.com` and `admin.example.com`), the cookie domain should be set to the parent domain prefixed by `.` (e.g `.example.com`) so the session will be shared across both subdomains. Loggins in on one subdomain will result in a session valid for all subdomains.
- Different domains: Because they are separate domains (e.g. `example.com` and `example.org`), the cookie domain should be left unset. Due to browser security restrictions, cookies cannot be shared across different domains. Each domain will maintain its own independent session, logging in on one domain will not result in a valid session on the other.

</callout>

## Local (`local`)

The default Directus email/password authentication flow. No additional configuration required.

## OAuth 2.0

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_ID
      </code>
    </td>
    
    <td>
      Client identifier for the OAuth provider.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_SECRET
      </code>
    </td>
    
    <td>
      Client secret for the OAuth provider.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_*
      </code>
    </td>
    
    <td>
      Client options overrides passed to the <a href="https://github.com/panva/openid-client" rel="nofollow">
        underlying client
      </a>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_SCOPE
      </code>
    </td>
    
    <td>
      A white-space separated list of permissions to request.
    </td>
    
    <td>
      <code>
        email
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_AUTHORIZE_URL
      </code>
    </td>
    
    <td>
      Authorization page URL of the OAuth provider.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ACCESS_URL
      </code>
    </td>
    
    <td>
      Access token URL of the OAuth provider.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_PROFILE_URL
      </code>
    </td>
    
    <td>
      User profile URL of the OAuth provider.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_IDENTIFIER_KEY
      </code>
    </td>
    
    <td>
      User profile identifier key <sup>
        <span>
          1
        </span>
      </sup>
      
      . Will default to <code>
        EMAIL_KEY
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_EMAIL_KEY
      </code>
    </td>
    
    <td>
      User profile email key.
    </td>
    
    <td>
      <code>
        email
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_FIRST_NAME_KEY
      </code>
    </td>
    
    <td>
      User profile first name key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_LAST_NAME_KEY
      </code>
    </td>
    
    <td>
      User profile last name key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ALLOW_PUBLIC_REGISTRATION
      </code>
    </td>
    
    <td>
      Automatically create accounts for authenticating users.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_DEFAULT_ROLE_ID
      </code>
    </td>
    
    <td>
      A Directus role ID to assign created users.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_SYNC_USER_INFO
      </code>
    </td>
    
    <td>
      Set user's first name, last name and email from provider's user info on each login.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ICON
      </code>
    </td>
    
    <td>
      SVG icon to display with the login link. Can be a Material Icon or Font Awesome Social Icon.
    </td>
    
    <td>
      <code>
        account_circle
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_LABEL
      </code>
    </td>
    
    <td>
      Text to be presented on SSO button within the Data Studio.
    </td>
    
    <td>
      <code>
        <PROVIDER>
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_PARAMS
      </code>
    </td>
    
    <td>
      Custom query parameters applied to the authorization URL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_REDIRECT_ALLOW_LIST
      </code>
    </td>
    
    <td>
      A comma-separated list of external URLs (including paths) allowed for redirecting after successful login.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ROLE_MAPPING
      </code>
    </td>
    
    <td>
      A JSON object in the form of <code>
        { "openid_group_name": "directus_role_id" }
      </code>
      
       that you can use to map OAuth claim groups to Directus roles <sup>
        <span>
          2
        </span>
      </sup>
      
      . If not specified, falls back to <code>
        AUTH_<PROVIDER>_DEFAULT_ROLE_ID
      </code>
      
       URL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_GROUP_CLAIM_NAME
      </code>
    </td>
    
    <td>
      The name of the OAuth claim that contains your user's groups.
    </td>
    
    <td>
      <code>
        groups
      </code>
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 When authenticating, Directus will match the identifier value from the external user profile to a Directus users "External Identifier".

<sup>
<span>

2

</span>
</sup>

 As Directus only allows one role per user, evaluating stops after the first match. An OAuth user that is member of both e.g. developer and admin groups may be assigned different roles depending on the order that you specify your role-mapping in: In the following example said OAuth user will be assigned the role `directus_developer_role_id`

```text
AUTH_<PROVIDER>_ROLE_MAPPING: json:{ "developer": "directus_developer_role_id", "admin": "directus_admin_role_id" }"
```

Whereas in the following example the OAuth user will be assigned the role `directus_admin_role_id`:

```text
AUTH_<PROVIDER>_ROLE_MAPPING: json:{ "admin": "directus_admin_role_id", "developer": "directus_developer_role_id" }"
```

## OpenID Connect

OpenID Connect (OIDC) is an authentication protocol built on OAuth 2.0, and should be preferred over standard OAuth 2.0 where possible.

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_ID
      </code>
    </td>
    
    <td>
      Client identifier for the external service.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_SECRET
      </code>
    </td>
    
    <td>
      Client secret for the external service.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_*
      </code>
    </td>
    
    <td>
      Client options overrides passed to the <a href="https://github.com/panva/openid-client" rel="nofollow">
        underlying client
      </a>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_PRIVATE_KEYS
      </code>
    </td>
    
    <td>
      An array of JSON Web Key Set (JWKS) private keys used to sign client assertions <sup>
        <span>
          1
        </span>
      </sup>
      
       when <code>
        AUTH_<PROVIDER>_CLIENT_TOKEN_ENDPOINT_AUTH_METHOD
      </code>
      
       is set to <code>
        private_key_jwt
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_SCOPE
      </code>
    </td>
    
    <td>
      A white-space separated list of permissions to request.
    </td>
    
    <td>
      <code>
        openid profile email
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ISSUER_URL
      </code>
    </td>
    
    <td>
      OIDC <code>
        .well-known
      </code>
      
       discovery document URL of the external service.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_IDENTIFIER_KEY
      </code>
    </td>
    
    <td>
      User profile identifier key <sup>
        <span>
          2
        </span>
      </sup>
      
      .
    </td>
    
    <td>
      <code>
        sub
      </code>
      
      <sup>
        <span>
          3
        </span>
      </sup>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ALLOW_PUBLIC_REGISTRATION
      </code>
    </td>
    
    <td>
      Automatically create accounts for authenticating users.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_REQUIRE_VERIFIED_EMAIL
      </code>
    </td>
    
    <td>
      Require created users to have a verified email address.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_DEFAULT_ROLE_ID
      </code>
    </td>
    
    <td>
      A Directus role ID to assign created users.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_SYNC_USER_INFO
      </code>
    </td>
    
    <td>
      Set user's first name, last name and email from provider's user info on each login.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ICON
      </code>
    </td>
    
    <td>
      SVG icon to display with the login link. Can be a Material Icon or Font Awesome Social Icon.
    </td>
    
    <td>
      <code>
        account_circle
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_LABEL
      </code>
    </td>
    
    <td>
      Text to be presented on SSO button within the Data Studio.
    </td>
    
    <td>
      <code>
        <PROVIDER>
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_PARAMS
      </code>
    </td>
    
    <td>
      Custom query parameters applied to the authorization URL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_REDIRECT_ALLOW_LIST
      </code>
    </td>
    
    <td>
      A comma-separated list of external URLs (including paths) allowed for redirecting after successful login.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ROLE_MAPPING
      </code>
    </td>
    
    <td>
      A JSON object in the form of <code>
        { "openid_group_name": "directus_role_id" }
      </code>
      
       that you can use to map OpenID groups to Directus roles <sup>
        <span>
          4
        </span>
      </sup>
      
      . If not specified, falls back to <code>
        AUTH_<PROVIDER>_DEFAULT_ROLE_ID
      </code>
      
       URL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_GROUP_CLAIM_NAME
      </code>
    </td>
    
    <td>
      The name of the OIDC claim that contains your user's groups.
    </td>
    
    <td>
      <code>
        groups
      </code>
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 To ensure correct parsing the env must be prefixed with `json:`.

<sup>
<span>

2

</span>
</sup>

 When authenticating, Directus will match the identifier value from the external user profile to a Directus users "External Identifier".

<sup>
<span>

3

</span>
</sup>

 `sub` represents a unique user identifier defined by the OIDC provider. For users not relying on `PUBLIC_REGISTRATION` it is recommended to use a human-readable identifier, such as `email`.

<sup>
<span>

4

</span>
</sup>

 As Directus only allows one role per user, evaluating stops after the first match. An OIDC user that is member of both e.g. developer and admin groups may be assigned different roles depending on the order that you specify your role-mapping in: In the following example said OIDC user will be assigned the role `directus_developer_role_id`

```text
AUTH_<PROVIDER>_ROLE_MAPPING: json:{ "developer": "directus_developer_role_id", "admin": "directus_admin_role_id" }"
```

Whereas in the following example the OIDC user will be assigned the role `directus_admin_role_id`:

```text
AUTH_<PROVIDER>_ROLE_MAPPING: json:{ "admin": "directus_admin_role_id", "developer": "directus_developer_role_id" }"
```

## LDAP (`ldap`)

LDAP allows Active Directory users to authenticate and use Directus without having to be manually configured. User information and roles will be assigned from Active Directory.

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_CLIENT_URL
      </code>
    </td>
    
    <td>
      LDAP connection URL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_BIND_DN
      </code>
    </td>
    
    <td>
      Bind user <sup>
        <span>
          1
        </span>
      </sup>
      
       distinguished name.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_BIND_PASSWORD
      </code>
    </td>
    
    <td>
      Bind user password.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_USER_DN
      </code>
    </td>
    
    <td>
      Directory path containing users.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_USER_ATTRIBUTE
      </code>
    </td>
    
    <td>
      Attribute to identify the user.
    </td>
    
    <td>
      <code>
        cn
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_USER_SCOPE
      </code>
    </td>
    
    <td>
      Scope of the user search, either <code>
        base
      </code>
      
      , <code>
        one
      </code>
      
      , <code>
        sub
      </code>
      
       <sup>
        <span>
          2
        </span>
      </sup>
      
      .
    </td>
    
    <td>
      <code>
        one
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_MAIL_ATTRIBUTE
      </code>
    </td>
    
    <td>
      User email attribute.
    </td>
    
    <td>
      <code>
        mail
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_FIRST_NAME_ATTRIBUTE
      </code>
    </td>
    
    <td>
      User first name attribute.
    </td>
    
    <td>
      <code>
        givenName
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_LAST_NAME_ATTRIBUTE
      </code>
    </td>
    
    <td>
      User last name attribute.
    </td>
    
    <td>
      <code>
        sn
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_GROUP_DN
      </code>
      
      <sup>
        <span>
          3
        </span>
      </sup>
    </td>
    
    <td>
      Directory path containing groups.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_GROUP_ATTRIBUTE
      </code>
    </td>
    
    <td>
      Attribute to identify user as a member of a group.
    </td>
    
    <td>
      <code>
        member
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_GROUP_SCOPE
      </code>
    </td>
    
    <td>
      Scope of the group search, either <code>
        base
      </code>
      
      , <code>
        one
      </code>
      
      , <code>
        sub
      </code>
      
       <sup>
        <span>
          2
        </span>
      </sup>
      
      .
    </td>
    
    <td>
      <code>
        one
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_DEFAULT_ROLE_ID
      </code>
    </td>
    
    <td>
      A fallback Directus role ID to assign created users.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_SYNC_USER_INFO
      </code>
    </td>
    
    <td>
      Set user's first name, last name and email from provider's user info on each login.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 The bind user must have permission to query users and groups to perform authentication. Anonymous binding
can by achieved by setting an empty value for `BIND_DN` and `BIND_PASSWORD`.

<sup>
<span>

2

</span>
</sup>

 The scope defines the following behaviors:

- `base`: Limits the scope to a single object defined by the associated DN.
- `one`: Searches all objects within the associated DN.
- `sub`: Searches all objects and sub-objects within the associated DN.

<sup>
<span>

3

</span>
</sup>

 If `GROUP_DN` is specified, the user's role will always be updated on authentication to a matching group
configured in AD, or fallback to the `DEFAULT_ROLE_ID`.

## SAML

SAML is an open-standard, XML-based authentication framework for authentication and authorization between two entities without a password.

- Service provider (SP) agrees to trust the identity provider to authenticate users.
- Identity provider (IdP) authenticates users and provides to service providers an authentication assertion that indicates a user has been authenticated.

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_SP_metadata
      </code>
    </td>
    
    <td>
      String containing XML metadata for service provider
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_IDP_metadata
      </code>
    </td>
    
    <td>
      String containing XML metadata for identity provider
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_ALLOW_PUBLIC_REGISTRATION
      </code>
    </td>
    
    <td>
      Automatically create accounts for authenticating users.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_DEFAULT_ROLE_ID
      </code>
    </td>
    
    <td>
      A Directus role ID to assign created users.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_IDENTIFIER_KEY
      </code>
    </td>
    
    <td>
      User profile identifier key <sup>
        <span>
          1
        </span>
      </sup>
      
      .
    </td>
    
    <td>
      <code>
        http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_EMAIL_KEY
      </code>
    </td>
    
    <td>
      User profile email key.
    </td>
    
    <td>
      <code>
        http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_GIVEN_NAME_KEY
      </code>
    </td>
    
    <td>
      User first name attribute.
    </td>
    
    <td>
      <code>
        http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_FAMILY_NAME_KEY
      </code>
    </td>
    
    <td>
      User last name attribute.
    </td>
    
    <td>
      <code>
        http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        AUTH_<PROVIDER>_REDIRECT_ALLOW_LIST
      </code>
    </td>
    
    <td>
      A comma-separated list of external URLs (including paths) allowed for redirecting after successful login.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 When authenticating, Directus will match the identifier value from the external user profile to a Directus users "External Identifier".

The `SP_metadata` and `IDP_metadata` variables should be set to the XML metadata provided by the service provider and identity provider respectively.

<callout icon="material-symbols:warning-rounded" color="warning">

**SAML Attribute Keys**<br />

<br />


Most identity providers send simple attribute names like `email` rather than the full XML schema URIs shown as defaults above. Set `IDENTIFIER_KEY` and `EMAIL_KEY` to match your identity provider's attribute names. Make sure to check the attribute statements in your IdP's SAML configuration.<br />

<br />


Unlike OAuth 2.0, there is no fallback from `IDENTIFIER_KEY` to `EMAIL_KEY`. If the configured identifier key is not found in the SAML response, authentication will fail.

</callout>

## Multiple Auth Providers

You can configure multiple providers for handling authentication in Directus. This allows for different options when logging in. To do this, provide a comma-separated list of provider names, and a config block for each provider. For example;

```bash
AUTH_PROVIDERS="google,facebook"

AUTH_GOOGLE_DRIVER="openid"
AUTH_GOOGLE_CLIENT_ID="830d...29sd"
AUTH_GOOGLE_CLIENT_SECRET="la23...4k2l"
AUTH_GOOGLE_ISSUER_URL="https://accounts.google.com/.well-known/openid-configuration"
AUTH_GOOGLE_IDENTIFIER_KEY="email"
AUTH_GOOGLE_ICON="google"
AUTH_GOOGLE_LABEL="Google"

AUTH_FACEBOOK_DRIVER="oauth2"
AUTH_FACEBOOK_CLIENT_ID="830d...29sd"
AUTH_FACEBOOK_CLIENT_SECRET="jd8x...685z"
AUTH_FACEBOOK_AUTHORIZE_URL="https://www.facebook.com/dialog/oauth"
AUTH_FACEBOOK_ACCESS_URL="https://graph.facebook.com/oauth/access_token"
AUTH_FACEBOOK_PROFILE_URL="https://graph.facebook.com/me?fields=email"
AUTH_FACEBOOK_ICON="facebook"
AUTH_FACEBOOK_LABEL="Facebook"
```

<callout icon="material-symbols:info-outline">

**Multiple Providers**
Directus users can only authenticate using the auth provider they are created with. It is not possible to authenticate with multiple providers for the same user.

</callout>

## Example Auth Provider Configurations

Below is a collection of example Directus configurations for integrating with various OpenID, OAuth 2.0 and SAML platforms. Due to the large number of available SSO platforms, this list will only cover the most common configurations. Contributions to expand and maintain the list are encouraged.

### OpenID

#### Apple

```text
AUTH_APPLE_DRIVER="openid"
AUTH_APPLE_CLIENT_ID="..."
AUTH_APPLE_CLIENT_SECRET="..."
AUTH_APPLE_ISSUER_URL="https://appleid.apple.com/.well-known/openid-configuration"
AUTH_APPLE_SCOPE="name email"
AUTH_APPLE_IDENTIFIER_KEY="email"
AUTH_APPLE_PARAMS="{"response_mode":"form_post"}"
```

#### Auth0

```text
AUTH_AUTH0_DRIVER="openid"
AUTH_AUTH0_CLIENT_ID="..."
AUTH_AUTH0_CLIENT_SECRET="..."
AUTH_AUTH0_ISSUER_URL="https://<your_auth0_domain>/.well-known/openid-configuration"
AUTH_AUTH0_IDENTIFIER_KEY="email"
```

#### Google

```text
AUTH_GOOGLE_DRIVER="openid"
AUTH_GOOGLE_CLIENT_ID="..."
AUTH_GOOGLE_CLIENT_SECRET="..."
AUTH_GOOGLE_ISSUER_URL="https://accounts.google.com/.well-known/openid-configuration"
AUTH_GOOGLE_IDENTIFIER_KEY="email"
```

#### Keycloak

```text
AUTH_KEYCLOAK_DRIVER="openid"
AUTH_KEYCLOAK_CLIENT_ID="..."
AUTH_KEYCLOAK_CLIENT_SECRET="..."
# For Keycloak < 18.0.0
AUTH_KEYCLOAK_ISSUER_URL="http://<your_keycloak_domain>/auth/realms/<your_keycloak_realm>/.well-known/openid-configuration"
# For Keycloak >= 18.0.0
AUTH_KEYCLOAK_ISSUER_URL="http://<your_keycloak_domain>/realms/<your_keycloak_realm>/.well-known/openid-configuration"
AUTH_KEYCLOAK_IDENTIFIER_KEY="email"
```

#### Microsoft Azure

```text
AUTH_MICROSOFT_DRIVER="openid"
AUTH_MICROSOFT_CLIENT_ID="..."
AUTH_MICROSOFT_CLIENT_SECRET="..."
AUTH_MICROSOFT_ISSUER_URL="https://login.microsoftonline.com/<your_tenant_id>/v2.0/.well-known/openid-configuration"
AUTH_MICROSOFT_IDENTIFIER_KEY="email"
```

#### Okta

```text
AUTH_OKTA_DRIVER="openid"
AUTH_OKTA_CLIENT_ID="..."
AUTH_OKTA_CLIENT_SECRET= "..."
AUTH_OKTA_ISSUER_URL="https://<your_okta_domain>/.well-known/openid-configuration"
AUTH_OKTA_IDENTIFIER_KEY="email"
```

#### Twitch

```text
AUTH_TWITCH_DRIVER="openid"
AUTH_TWITCH_CLIENT_ID="..."
AUTH_TWITCH_CLIENT_SECRET="..."
AUTH_TWITCH_ISSUER_URL="https://id.twitch.tv/oauth2/.well-known/openid-configuration"
AUTH_TWITCH_SCOPE="openid user:read:email"
AUTH_TWITCH_PARAMS__CLAIMS="string:{"id_token":{"email":null}}"
AUTH_TWITCH_IDENTIFIER_KEY="email"
```

### OAuth 2.0

#### Discord

```text
AUTH_DISCORD_DRIVER="oauth2"
AUTH_DISCORD_CLIENT_ID="..."
AUTH_DISCORD_CLIENT_SECRET="..."
AUTH_DISCORD_AUTHORIZE_URL="https://discord.com/api/oauth2/authorize"
AUTH_DISCORD_ACCESS_URL="https://discord.com/api/oauth2/token"
AUTH_DISCORD_PROFILE_URL="https://discord.com/api/users/@me"
```

#### Facebook

```text
AUTH_FACEBOOK_DRIVER="oauth2"
AUTH_FACEBOOK_CLIENT_ID="..."
AUTH_FACEBOOK_CLIENT_SECRET="..."
AUTH_FACEBOOK_AUTHORIZE_URL="https://www.facebook.com/dialog/oauth"
AUTH_FACEBOOK_ACCESS_URL="https://graph.facebook.com/oauth/access_token"
AUTH_FACEBOOK_PROFILE_URL="https://graph.facebook.com/me?fields=email"
```

#### GitHub

```text
AUTH_GITHUB_DRIVER="oauth2"
AUTH_GITHUB_CLIENT_ID="..."
AUTH_GITHUB_CLIENT_SECRET="..."
AUTH_GITHUB_AUTHORIZE_URL="https://github.com/login/oauth/authorize"
AUTH_GITHUB_ACCESS_URL="https://github.com/login/oauth/access_token"
AUTH_GITHUB_PROFILE_URL="https://api.github.com/user"
```

<callout icon="material-symbols:warning-rounded" color="warning">

If the authenticating user has not marked their email as "public" in GitHub, it will not be accessible by Directus.

</callout>

#### Twitter

```text
AUTH_TWITTER_DRIVER="oauth2"
AUTH_TWITTER_CLIENT_ID="..."
AUTH_TWITTER_CLIENT_SECRET="-..."
AUTH_TWITTER_AUTHORIZE_URL="https://twitter.com/i/oauth2/authorize"
AUTH_TWITTER_ACCESS_URL="https://api.twitter.com/2/oauth2/token"
AUTH_TWITTER_PROFILE_URL="https://api.twitter.com/2/users/me"
AUTH_TWITTER_IDENTIFIER_KEY="data.username"
AUTH_TWITTER_SCOPE="tweet.read users.read"
```

<callout icon="material-symbols:warning-rounded" color="warning">

Twitter does not provide "email" so we define "username" as the identifier.

</callout>

### SAML

#### AWS

```text
AUTH_AWS_DRIVER="saml"
AUTH_AWS_IDP_metadata="{Your IAM Identity Center SAML metadata file}"
AUTH_AWS_SP_metadata=""
AUTH_AWS_ALLOW_PUBLIC_REGISTRATION="true"
AUTH_AWS_DEFAULT_ROLE_ID="{Needs to be a valid role on the instance}"
AUTH_AWS_IDENTIFIER_KEY="email"
AUTH_AWS_EMAIL_KEY="email"
```

<callout icon="material-symbols:warning-rounded" color="warning">

**Metadata**

- AWS IAM Docs are not that verbose. Users have found that the `SP_metadata` environment variable can be supplied empty.
- Users have found that replacing
`<md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://your-soo-portal-url"/>`
in the IAM Identity Center SAML metadata file with your AWS Portal URL is a fix for getting the 'Login With SSO'
button on Directus to work, rather the default redirect from AWS.
- Directus expects `<?xml version="1.0" encoding="UTF-8"?>` to be removed from the start of the XML.

</callout>

**Mapping:**

Maps the email address into Directus as `external_identifier`:

<table>
<thead>
  <tr>
    <th>
      User attribute in the application
    </th>
    
    <th>
      Maps to this string value or user attribute in IAM Identity Center
    </th>
    
    <th>
      type
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        Subject
      </code>
    </td>
    
    <td>
      <code>
        ${user:email}
      </code>
    </td>
    
    <td>
      <code>
        emailAddress
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        email
      </code>
    </td>
    
    <td>
      <code>
        ${user:email}
      </code>
    </td>
    
    <td>
      <code>
        unspecified
      </code>
    </td>
  </tr>
</tbody>
</table>

**Config:**

- Relay state: `admin/login`
- Application ACS URL: `https://your-directus-instance/auth/login/aws/acs`

#### Google

```text
AUTH_GOOGLE_DRIVER="saml"
AUTH_GOOGLE_IDP_metadata="{Your SAML metadata file from Google}"
AUTH_GOOGLE_SP_metadata="{Create your own SAML metadata file, see example below}"
AUTH_GOOGLE_ALLOW_PUBLIC_REGISTRATION="true"
AUTH_GOOGLE_DEFAULT_ROLE_ID="{Needs to be a valid role on the instance}"
AUTH_GOOGLE_IDENTIFIER_KEY="email"
AUTH_GOOGLE_EMAIL_KEY="email"
```

<callout icon="material-symbols:warning-rounded" color="warning">

**SP Metadata**

- The `entityID` should be the same as the one configured in Google in the `EntityDescriptor` tag
- The `Location` should be the ACS URL of your Directus instance in the format of
`https://your-directus-instance/auth/login/google/acs`
- Directus expects `<?xml version="1.0" encoding="UTF-8"?>` to be removed from the start of the XML.

**Example**

```xml
<EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" entityID="SHOULD_MATCH_GOOGLE_CONFIG">
  <SPSSODescriptor WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
    <AssertionConsumerService isDefault="true" index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="YOUR_DOMAIN/auth/login/google/acs"/>
  </SPSSODescriptor>
</EntityDescriptor>
```

</callout>
