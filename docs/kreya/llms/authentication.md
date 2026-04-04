# Source: https://kreya.app/docs/authentication.md

# Authentication

Kreya centralizes authentication management. Often, you only need a few different "authentication configurations" in your projects.

You can add, edit and delete authentication configurations via Project → Authentications.

## Supported authentication types[​](#supported-authentication-types "Direct link to Supported authentication types")

Kreya supports a range of authentication types out of the box. The authentication values are automatically transmitted in the correct format.

### Basic authentication[​](#basic-authentication "Direct link to Basic authentication")

To add a basic authentication configuration, choose the type `Basic`, enter your username and password, then click `Save`.

### Windows authentication [Pro / Enterprise](/pricing.md)[​](#windows-authentication- "Direct link to windows-authentication-")

To use Windows (or any other Kerberos- or NTLM-based) authentication, create a new authentication configuration with the type `System credentials (Kerberos/NTLM)`. Kreya uses the information of the currently logged in user to authenticate to the API.

### OAuth2 / OpenID-Connect[​](#oauth2--openid-connect "Direct link to OAuth2 / OpenID-Connect")

To add an authentication configuration for OAuth2 or OpenID-Connect, choose the type `OAuth2 / OpenID-Connect`. Enter the required values. Note that depending on your authentication provider and settings, not all fields need to be filled in.

#### Supported flows[​](#supported-flows "Direct link to Supported flows")

The following OAuth2 flows are supported:

* Authorization Code (with and without PKCE)
* Implicit
* Client Credentials
* Resource Owner Password Credentials
* Device Authorization (Device Code)

#### Native browser[​](#native-browser "Direct link to Native browser")

Using the native browser opens the default browser of your system instead of Kreya's built-in web window. This approach allows you to leverage browser extensions, password managers, passkeys, and other browser-specific features. However, it requires a localhost redirect URI with an available port to complete the authentication flow.

### JWT[​](#jwt "Direct link to JWT")

The `JWT` (JSON Web Token) authentication type allows you to generate a locally signed token on the fly. This is particularly useful during development or testing when you need to simulate a token with specific claims (e.g. roles, permissions, user IDs) without going through a full identity provider flow. You can configure the payload, header, and the secret/private key used for signing.

### JWT Profile (RFC 7523)[​](#jwt-profile-rfc-7523 "Direct link to JWT Profile (RFC 7523)")

The `JWT Profile` type implements the "JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants" ([RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523)). This method is often used for server-to-server authentication where a client needs to access resources without user interaction. Instead of sending a static client secret, the client creates and signs a JWT assertion to request an access token from the authorization server.

### Static authentication values[​](#static-authentication-values "Direct link to Static authentication values")

Select the `Static value` type if your authentication value changes infrequently, such as an API key. This value will be sent as-is in the HTTP `Authorization` header.

### Google Service Account[​](#google-service-account "Direct link to Google Service Account")

The `Google Service Account` type allows you to access Google APIs. Simply provide a JSON key file and a scope.

### AWS Signature v4[​](#aws-signature-v4 "Direct link to AWS Signature v4")

The `AWS Signature v4` type is a protocol for authenticating inbound API requests to AWS services.

## Templating[​](#templating "Direct link to Templating")

You can use templating in authentications like nearly everywhere else. This will save you a lot of time, for example when you have different passwords for each environment.

![Using templating in authentication configuration](/assets/ideal-img/authentication-templating.e26749b.400.png)

## Storing sensitive information[​](#storing-sensitive-information "Direct link to Storing sensitive information")

Values entered in authentication configurations (such as Basic authentication passwords) are stored in plain-text in the Kreya project. If you share your project, you may want to extract sensitive information. Use the [Environment](/docs/environments.md) feature and store sensitive information in `User specific data`. While this still stores your sensitive data in plain text, it will be stored outside of the Kreya project and thus won't be shared.

## Using authentication configurations[​](#using-authentication-configurations "Direct link to Using authentication configurations")

To reference an authentication configuration from an operation, simply click the `Auth` tab and select your desired authentication configuration. Kreya now adds the correct authentication value to the request.

![Configuration an operation to use an authentication configuration](/assets/ideal-img/using-authentications.f5bda82.400.png)
