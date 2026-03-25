# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/authentication.md

# Authentication

With this feature, you can embed another website that's protected by SSO authentication. To do this, you'll need the required parameters to create a JWT token.

## Authentication code flow + PKCE[â](#authentication-code-flow--pkce "Direct link to Authentication code flow + PKCE")

The following diagram outlines the login scheme used to authenticate with your SSO and gain access to the private resource:

![AuthorizationCodeFlow.png](/assets/images/AuthorizationCodeFlow-dfc247f27206d592e984bac1c3e13d72.png)

Here is an explanation of the login flow:

1. The widget will generate a PKCE `code_verifier` & `code_challenge`;
2. The widget URL is set to the `authorizationUrl` along with the `clientId` and the generated `code_challenge`;
3. The widget will then be redirected to the SSO sign-in page;
4. The user will sign in using the SSO (If the user is already signed in to the SSO, this step will happen automatically);
5. The SSO sign-in page will redirect the widget back to <https://app.getport.io> with the authorization `code` as a URL hash parameter;
6. The widget will send the `code`, `clientId` and the `code_verifier` to the `tokenURL`;
7. The SSO will validate the PKCE code;
8. A response will come back with an access token;
9. The widget will pass the access token as a query parameter `auth_token={accessToken}` to the URL specified in the property value;
10. Your page should be displayed now!

## Required Parameters[â](#required-parameters "Direct link to Required Parameters")

To set up the authentication, you'll need the following parameters:

* `clientId`
* `authorizationUrl`
* `tokenUrl`

Here's an example of how to apply these parameters in your Blueprint:

```
{
  "title": "Grafana",
  "type": "string",
  "format": "url",
  "spec": "embedded-url",
  "specAuthentication": {
    "clientId": "your-client-id",
    "authorizationUrl": "your-authorization-url",
    "tokenUrl": "your-token-url"
  }
}
```

## Examples[â](#examples "Direct link to Examples")

### Okta[â](#okta "Direct link to Okta")

Setup

**Steps:**

1. Follow the steps in [Okta's documentation](https://developer.okta.com/docs/guides/implement-grant-type/authcodepkce/main/) to create an Application in your Okta Organization;

2. Make sure the Port host is in the `Redirect Uris`:

   <!-- -->

   1. Go to Applications -> The application you just created -> Login;
   2. Add `https://app.getport.io` as a Sign-in redirect URI.

3. Enable IFrame for Sign-In Page:

   <!-- -->

   1. Go to Customizations -> Other;
   2. Scroll to "IFrame Embedding" and enable it.

<br />

**Configure Grafana with OAuth & Port embedding**

note

The following example is just for illustration purposes and may not reflect the actual URLs and client IDs used in your Okta setup.

Based on Grafana docs for [JWT Configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/jwt/) & [OAuth Configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/)

```
[security] ;Required for the embedding
allow_embedding = true

[auth.jwt] ;Required for the embedding
...
jwk_set_url = https://{your-okta-org}.okta.com/oauth2/default/v1/keys
expect_claims = {"iss": "https://{your-okta-org}.okta.com", "aud": "https://{your-okta-org}.okta.com"}
url_login = true
...

[auth.generic_oauth] ;Regular OAuth authentication
...
client_id = {CLIENT_ID}
client_secret = {CLIENT_SECRET}
auth_url = https://{your-okta-org}.okta.com/oauth2/v1/authorize
token_url = https://{your-okta-org}.okta.com/oauth2/v1/token
api_url = https://{your-okta-org}.okta.com/oauth2/v1/userinfo
enable_login_token = true
use_pkce = true
...
```

**Troubleshooting**

* "*Okta 400 Bad Request*"

  <!-- -->

  * Check that you used the correct authorizationUrl & clientId;
  * Check that your application is activated.

* "*Okta 400 Bad Request displayed. Your request resulted in an error. The 'redirect\_uri' parameter must be a Login redirect URI in the client app settings*".
  <!-- -->
  * Make sure you entered <https://app.getport.io> as a Sign-in redirect URI for your application as mentioned in the steps above.

* "*refused to connect.*"
  <!-- -->
  * Make sure you enabled "IFrame Embedding" as mentioned in the steps above.

* "*Could not fetch your auth token.*"
  <!-- -->
  * Make sure your tokenUrl is the correct url.

### Onelogin[â](#onelogin "Direct link to Onelogin")

Setup

**Steps:**

1. Follow steps 1 & 2 in [Onelogin's documentation](https://onelogin.service-now.com/support?id=kb_article\&sys_id=143e6c13dbfd0450ca1c400e0b9619d6#add) to add an OpenId Connect (OIDC) application in your Onelogin organization;

2. Make sure the Port host is in the `Redirect URIs`:

   <!-- -->

   1. Go to Applications -> The application you just added -> Configuration;
   2. Add `https://app.getport.io` as a Redirect URI.

<br />

**Configure Grafana with OAuth & Port embedding**

note

The following example is just for illustration purposes and may not reflect the actual URLs and client IDs used in your Onelogin setup.

Based on Grafana docs for [JWT Configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/jwt/) & [OAuth Configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/)

```
[security] ;Required for the embedding
allow_embedding = true

[auth.jwt] ;Required for the embedding
...
jwk_set_url = https://{your-onelogin-org}.onelogin.com/oidc/2/certs
expect_claims = {"iss": "https://{your-onelogin-org}/oidc/2"}
url_login = true
...

[auth.generic_oauth] ;Regular OAuth authentication
...
client_id = {CLIENT_ID}
client_secret = {CLIENT_SECRET}
auth_url = https://{your-onelogin-org}.onelogin.com/oidc/2/auth
token_url = https://{your-onelogin-org}.onelogin.com/oidc/2/token
api_url = https://{your-onelogin-org}.onelogin.com/oidc/2/me
enable_login_token = true
use_pkce = true
...
```

**Troubleshoot**

* "*unrecognized route or not allowed method*"
  <!-- -->
  * Check that you used the correct authorizationUrl.
* "*client is invalid*"
  <!-- -->
  * Check that you used the correct clientId.
* "*redirect\_uri did not match any client's registered redirect\_uris*".
  <!-- -->
  * Make sure you entered <https://app.getport.io> as a Redirect URI for your application as mentioned in the steps above.
* "*Could not fetch your auth token.*"
  <!-- -->
  * Make sure your tokenUrl is the correct URL.

### Azure AD[â](#azure-ad "Direct link to Azure AD")

Setup

**Steps:**

1. Follow the [Register an application](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application) steps in Azure Documentation to add an application in your Azure subscription;

2. Follow the [Add a redirect URI](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-redirect-uri) steps in Azure documentation to add `https://app.getport.io` as a Redirect URI;

3. Follow the [Configure platform settings](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#configure-platform-settings) to configure your application as `Single-page application`;

4. Add a custom scope to your new application:

   1. In your application click on the Expose an API button on the left sidebar;

   2. Click on the `Add a scope` button to add a scope that will allow Admins and users to consent `Read User`; ![Azure AD Scope](/assets/images/AzureAdScope-fcc8366e5ac9f8f67dbfcf34d85cd0eb.png)

   3. Add the scope you just created under the `Authorization Scope` field in the property in your blueprint inside Port.

      ```
      ...
      "schema": {
        "properties": {
          "ff": {
            "type": "string",
            "title": "ff",
            "format": "url",
            "spec": "embedded-url",
            "specAuthentication": {
              "authorizationUrl": "https://app.com",
              "tokenUrl": "https://app.com",
              "clientId": "1234",
              "authorizationScope": [
                "api://xxxx-xxxx-xxxx-xxxx-xxxx/user.read"
              ]
            }
          }
        }
      }
      ...
      ```

<br />

**Configure Grafana with OAuth & Port embedding**

note

The following example is just for illustration purposes and may not reflect the actual URLs and client IDs used in your Azure AD setup.

Based on Grafana docs for [JWT Configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/jwt/) & [Azure AD Configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/azuread/)

```
[security] ;Required for the embedding
allow_embedding = true

[auth.jwt] ;Required for the embedding
...
email_claim = preferred_username
username_claim = preferred_username
jwk_set_url = "https://login.microsoftonline.com/common/discovery/v2.0/keys"
expect_claims = {"iss": "https://login.microsoftonline.com/{YOUR_APPLICATION_UUID}/v2.0"}
url_login = true
...

[auth.azuread] ;Regular Azure AD authentication
...
client_id = {CLIENT_ID}
client_secret = {CLIENT_SECRET}
auth_url = "https://login.microsoftonline.com/{YOUR_APPLICATION_UUID}/oauth2/v2.0/authorize"
token_url = "https://login.microsoftonline.com/{YOUR_APPLICATION_UUID}/oauth2/v2.0/token"
allowed_domains = "{my-domain}.com"
use_pkce = true
...
```

**Troubleshoot**

* "*Could not fetch your auth token.*"
  <!-- -->
  * Make sure your tokenUrl is the correct URL.
