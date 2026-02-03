# openapi3

You can use Postman to identify any potential security and formatting issues when defining your API.

![Image 1: OpenAPI 3.0 rule violations](https://assets.postman.com/postman-docs/v11/api-definition-rule-violations-openapi3-v11-b.jpg)

## Warnings for OpenAPI 3

For all APIs defined in OpenAPI 3.0 and 3.1, the following list describes possible warning messages and potential ways to resolve them.

* [Broken object level authorization](#broken-object-level-authorization)
    * [Scope for OAuth scheme used in security field is not defined in the securityScheme declaration](#scope-for-oauth-scheme-used-in-security-field-is-not-defined-in-the-securityscheme-declaration)
    * [Scope for OAuth scheme used is not defined in the securityScheme declaration](#scope-for-oauth-scheme-used-is-not-defined-in-the-securityscheme-declaration)
* [Broken user authentication](#broken-user-authentication)
    * [Security field is not defined](#security-field-is-not-defined)
    * [Security field does not contain any item](#security-field-does-not-contain-any-item)
    * [Security field does not contain any scheme](#security-field-does-not-contain-any-scheme)
    * [Security scheme object not defined](#security-scheme-object-not-defined)
    * [Security scheme object does not contain any scheme](#security-scheme-object-does-not-contain-any-scheme)
    * [Scheme used in security field is not defined in the security scheme object](#scheme-used-in-security-field-is-not-defined-in-the-security-scheme-object)
    * [HTTP authentication scheme is using an unknown scheme](#http-authentication-scheme-is-using-an-unknown-scheme)
    * [Security field for the operation does not contain any item](#security-field-for-the-operation-does-not-contain-any-item)
    * [Security field for the operation does not contain any scheme](#security-field-for-the-operation-does-not-contain-any-scheme)
    * [Operation does not enforce any security scheme](#operation-does-not-enforce-any-security-scheme)
* [Excessive data exposure](#excessive-data-exposure)
    * [API accepts credentials from OAuth authentication in plain text](#api-accepts-credentials-from-oauth-authentication-in-plain-text)
    * [API accepts credentials from OpenID Connect authentication in plain text](#api-accepts-credentials-from-openid-connect-authentication-in-plain-text)
    * [API accepts credentials from OAuth 1.0 authentication in plain text](#api-accepts-credentials-from-oauth-10-authentication-in-plain-text)
    * [API accepts API key in plain text](#api-accepts-api-key-in-plain-text)
    * [API accepts auth credentials in plain text](#api-accepts-auth-credentials-in-plain-text)
    * [Global server URL uses HTTP protocol](#global-server-url-uses-http-protocol)
    * [Operation accepts credentials from OAuth authentication in plain text](#operation-accepts-credentials-from-oauth-authentication-in-plain-text)
    * [Operation accepts credentials from OpenID Connect authentication as plain text](#operation-accepts-credentials-from-openid-connect-authentication-as-plain-text)
    * [Operation accepts credentials from OAuth 1.0 authentication in plain text](#operation-accepts-credentials-from-oauth-10-authentication-in-plain-text)
    * [Operation accepts API key in plain text](#operation-accepts-api-key-in-plain-text)
    * [Operation accepts authentication credentials in plain text](#operation-accepts-authentication-credentials-in-plain-text)
    * [Server URL of the operation is using HTTP protocol](#server-url-of-the-operation-is-using-http-protocol)
    * [Authorization URL uses HTTP protocol; credentials will be transferred as plain text](#authorization-url-uses-http-protocol-credentials-will-be-transferred-as-plain-text)
    * [Token URL uses HTTP protocol](#token-url-uses-http-protocol)
    * [Refresh URL uses HTTP protocol](#refresh-url-uses-http-protocol)
    * [OpenID Connect URL uses HTTP protocol](#openid-connect-url-uses-http-protocol)
* [Improper assets management](#improper-assets-management)
    * [Deprecated OAuth 1.0 scheme is used](#deprecated-oauth-10-scheme-is-used)
    * [OAuth authentication uses the deprecated implicit flow](#oauth-authentication-uses-the-deprecated-implicit-flow)
    * [OAuth authentication uses the deprecated password flow](#oauth-authentication-uses-the-deprecated-password-flow)
* [API information](#api-information)
    * [The info object should have a description](#the-info-object-should-have-a-description)
    * [The info object should have a license](#the-info-object-should-have-a-license)
    * [The info object should have a license URL](#the-info-object-should-have-a-license-url)
    * [The info object should have a terms of service](#the-info-object-should-have-a-terms-of-service)
    * [API must have contact information available](#api-must-have-contact-information-available)
    * [API must have a contact name available](#api-must-have-a-contact-name-available)
    * [API must have a contact URL or email available](#api-must-have-a-contact-url-or-email-available)
    * [API must have a contact email available](#api-must-have-a-contact-email-available)
    * [API must have a contact URL available](#api-must-have-a-contact-url-available)
* [Operations](#operations)
    * [There should be no trailing slashes on paths](#there-should-be-no-trailing-slashes-on-paths)
    * [All operations should have summaries](#all-operations-should-have-summaries)
    * [Operation summaries shouldn't end with a period](#operation-summaries-shouldnt-end-with-a-period)
    * [All operations should have descriptions](#all-operations-should-have-descriptions)
    * [All parameters should have descriptions](#all-parameters-should-have-descriptions)
    * [All parameters should have examples](#all-parameters-should-have-examples)
    * [POST methods should have request bodies](#post-methods-should-have-request-bodies)
    * [PUT methods should have request bodies](#put-methods-should-have-request-bodies)
    * [PATCH methods should have request bodies](#patch-methods-should-have-request-bodies)
    * [All request bodies should have examples](#all-request-bodies-should-have-examples)
    * [Operation should return a 2xx HTTP status code](#operation-should-return-a-2xx-http-status-code)
    * [Operation should return a 5xx HTTP status code](#operation-should-return-a-5xx-http-status-code)
    * [All responses should have examples](#all-responses-should-have-examples)
    * [A 204 response can't have a body](#a-204-response-cant-have-a-body)
* [Models](#models)
    * [A schema property should reference a reusable schema](#a-schema-property-should-reference-a-reusable-schema)
    * [All reusable schemas should have descriptions](#all-reusable-schemas-should-have-descriptions)
    * [All schema properties should have descriptions](#all-schema-properties-should-have-descriptions)
    * [Arrays must have `minItems` and `maxItems` defined](#arrays-must-have-minitems-and-maxitems-defined)

## Broken object level authorization

### Scope for OAuth scheme used in security field is not defined in the securityScheme declaration

| Issue description | Possible fix |
| --- | --- |
| The OAuth2 scopes used in the global security field need to be defined in the security schemes field. Otherwise, an attacker can introduce their scopes to fill the gap and exploit the system. | Make sure that all the OAuth2 scopes used are defined in the OAuth2 security scheme. |

#### Resolution

```json
security:
  - OAuth2:
    - read
    - write
components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          scopes:
            read: read objects in your account
            write: write objects to your account
```

### Scope for OAuth scheme used is not defined in the securityScheme declaration

| Issue description | Possible fix |
| --- | --- |
| The OAuth2 scopes used in the security field of the operation need to be defined in the security schemes field. Otherwise, an attacker can introduce their scopes to fill the gap and exploit the system. | Make sure that all the OAuth2 scopes used are defined in the OAuth2 security scheme. |

#### Resolution

```json
paths:
  /user:
    get:
      summary: 'Sample endpoint: Returns details about a particular user'
      operationId: listUser
      security:
      - OAuth2:
        - read
        - write
components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          scopes:
            read: read objects in your account
            write: write objects to your account
```

## Broken user authentication

### Security field is not defined

| Issue description | Possible fix |
| --- | --- |
| If the global security field isn't defined, the API doesn't require any authentication by default. Anyone can access the API operations that don't have a security field defined. | The security field needs to be defined in the schema. |

#### Resolution

```json
openapi: 3.0.0
info:
paths:
security:
    - testAuth : []
```

### Security field does not contain any item

| Issue description | Possible fix |
| --- | --- |
| If the security field has an empty array, no security scheme is applied to the operations by default. | The security field needs to have at least one item in the array. |

#### Resolution

```json
openapi: 3.0.0
info:
paths:
security:
    - testAuth : []
```

### Security field does not contain any scheme

| Issue description | Possible fix |
| --- | --- |
| An empty object in the security field deactivates the authentication. Without security fields defined for each operation, anyone can access the API operations without any authentication. | Security field array items can't have an empty object. |

#### Resolution

```json
openapi: 3.0.0
info:
paths:
security:
    - testAuth : []
```

### Security scheme object not defined

| Issue description | Possible fix |
| --- | --- |
| The components object of the API doesn't declare any security schemes which can be used in the security field of the API or individual operations. | Security schemes need to be defined in the schema of the component. |

#### Resolution

```json
components:
  securitySchemes:
    testAuth:
      type: http
      scheme: basic
```

### Security scheme object does not contain any scheme

| Issue description | Possible fix |
| --- | --- |
| An empty object in the reusable security schemes means that no authentication scheme is defined for each operation, anyone can access the API operations without any authentication. | Security schemes need to have at least one item in the object. |

#### Resolution

```json
components:
  securitySchemes:
    BasicAuth:
      type: http
      scheme: basic
```

### Scheme used in security field is not defined in the security scheme object

| Issue description | Possible fix |
| --- | --- |
| The authentication scheme used in global or operation security field isn't defined in the security scheme object. | The scheme used in the security field needs to be defined in the security scheme object. |

#### Resolution

```json
components:
  securitySchemes:
    BasicAuth:
      type: http
      scheme: basic
#...
security:
- BasicAuth: []
```

## Excessive data exposure

### API accepts credentials from OAuth authentication in plain text

| Issue description | Possible fix |
| --- | --- |
| The access tokens are sent as plain text over an unencrypted network. Attackers can intercept the access tokens by listening to the network traffic in a public Wi-Fi network. | Make sure that the server URL is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
servers:
  - url: https://my.api.example.com/
    description: API server
# ...
components:
  securitySchemes:
    OAuth2:
      type: oauth2
# ...
security:
  - OAuth2:
      - write
      - read
```

### API accepts credentials from OpenID Connect authentication in plain text

| Issue description | Possible fix |
| --- | --- |
| The credentials are sent as plain text over an unencrypted network. Attackers can intercept the access tokens by listening to the network traffic in a public Wi-Fi network. | Make sure that the server URL is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
components:
  securitySchemes:
    OpenIdScheme:
      type: openIdConnect
      openIdConnectUrl: https://example.com/connect
paths:
  '/pets':
  post:
   operationId: addPet
   servers:
   - url: https://example.com/
     description: API server
   security:
   - OpenIdScheme: []
```

### API accepts credentials from OAuth 1.0 authentication in plain text

| Issue description | Possible fix |
| --- | --- |
| The authentication tokens are sent as plain text over an unencrypted channel. Attackers can intercept the token by listening to the network traffic in a public Wi-Fi network. | Make sure that the server URL is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
servers:
  - url: https://my.api.example.com/
    description: API server
#...
components:
  securitySchemes:
    OAuth1:
      type: http
      scheme: oauth
#...
security:
  - OAuth1: []
```

### API accepts API key in plain text

| Issue description | Possible fix |
| --- | --- |
| API keys are sent as plain text over an unencrypted channel. Attackers can intercept API key by listening to the network traffic in a public Wi-Fi network. | Make sure that the server URL is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
servers:
- url: https://example.com/
  description: Example server
components:
 securitySchemes:
  BasicAuth:
   type: http
   scheme: basic
security:
- BasicAuth: []
```

### API accepts auth credentials in plain text

| Issue description | Possible fix |
| --- | --- |
| The credentials are sent as plain text over an unencrypted network. Attackers can intercept the credentials by listening to the network traffic in a public Wi-Fi network. | Make sure that the server URL is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
servers:
  - url: https://example.com/
    description: Example server
# ...
components:
  securitySchemes:
    AuthKeyAuth:
      type: apiKey
      name: api-key
      in: header
#...
security:
  - AuthKeyAuth: []
```

### API accepts authentication credentials in plain text

| Issue description | Possible fix |
| --- | --- |
| The API operation accepts the credentials that are transported in plain text over an unencrypted channel. Attackers can intercept API calls and retrieve the authentication credentials to make other API calls. | Make sure that the server URL of the operation is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
components:
 securitySchemes:
  BasicAuth:
   type: http
   scheme: basic
paths:
  '/pets':
  post:
   operationId: addPet
   servers:
   - url: https://example.com/
     description: Example server
   security:
   - BasicAuth: []
```

### Server URL of the operation is using HTTP protocol

| Issue description | Possible fix |
| --- | --- |
| The API operation supports unencrypted HTTP connections, all requests and responses will be transmitted in the open. Anyone listening to the network traffic while the calls are being made can intercept them. | Make sure that the server URL is a valid URL and uses HTTPS protocol. |

#### Resolution

```json
get:
  operationId: getPetsById
  servers:
    - url: https://my.api.example.com/
```

### Authorization URL uses HTTP protocol; credentials will be transferred as plain text

| Issue description | Possible fix |
| --- | --- |
| OAuth authorization credentials are transported over an unencrypted channel. Anyone listening to the network traffic while the calls are being made can intercept them. | Make sure that the authorization URL is a valid URL and follows HTTPS protocol. |

#### Resolution

```json
components:
  securitySchemes:
     OauthScheme:
        type: oauth2
        flows:
          authorizationCode:
            authorizationUrl: https://my.auth.example.com/
```

### Token URL uses HTTP protocol

| Issue description | Possible fix |
| --- | --- |
| OAuth authentication tokens are transported over an unencrypted channel. Anyone listening to the network traffic while the token is being sent can intercept it. | Make sure that the token URL is a valid URL and follows HTTPS protocol. |

#### Resolution

```json
components:
  securitySchemes:
     OauthScheme:
        type: oauth2
        flows:
          authorizationCode:
            tokenUrl: https://my.token.example.com/
```

### Refresh URL uses HTTP protocol

| Issue description | Possible fix |
| --- | --- |
| OAuth authentication refresh tokens are transported over an unencrypted channel. Anyone listening to the network traffic while the token is being sent can intercept it. | Make sure that the refresh URL is a valid URL and follows HTTPS protocol. |

#### Resolution

```json
components:
  securitySchemes:
    OauthFlow:
      type: oauth2
      flows:
        authorizationCode
          authorizationUrl: https://my.auth.example.com/
          tokenUrl: https://my.token.example.com/
          refreshUrl: https://my.refresh.example.com/
          scopes:
            write: modify data
            read: read data
```

## Improper assets management

### Deprecated OAuth 1.0 scheme is used

| Issue description | Possible fix |
| --- | --- |
| Security scheme uses OAuth 1.0 authentication which has been deprecated and replaced by OAuth 2.0. | Make sure that the security scheme isn't using the deprecated OAuth 1.0 authentication. |

#### Resolution

```json
components:
  securitySchemes:
    OauthFlow:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://my.auth.example.com/
          tokenUrl: https://my.token.example.com/
          scopes:
            write: modify data
            read: read data
```

### OAuth authentication uses the deprecated implicit flow

| Issue description | Possible fix |
| --- | --- |
| In OAuth implicit flow, authorization server issues access tokens in the authorization request's response. Attackers can intercept API calls and retrieve the access tokens to make other API calls. | It's recommended to use authorizationCode flow. Make sure that the OAuth authentication scheme isn't using the implicit flow. |

#### Resolution

```json
components:
  securitySchemes:
    OauthFlow:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://my.auth.example.com/
          tokenUrl: https://my.token.example.com/
          scopes:
            write: modify data
            read: read data
```

### OAuth authentication uses the deprecated password flow

| Issue description | Possible fix |
| --- | --- |
| OAuth password grant flow uses the user's credentials to retrieve the access token. Attackers can intercept API calls and retrieve the access tokens to make other API calls. | It's recommended to use authorizationCode flow. Make sure that the OAuth authentication scheme isn't using the password grant flow. |

#### Resolution

```json
components:
  securitySchemes:
    OauthFlow:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://my.auth.example.com/
          tokenUrl: https://my.token.example.com/
          scopes:
            write: modify data
            read: read data
```

## API information

This rule category deals with the OpenAPI info object, which has metadata about the API.

### The info object should have a description

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [info object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#info-object) doesn't have a description. Although a description isn't required, including one enables you to provide your API's consumers with information about what the API does and how to use it. This can be anything from a short description to a long explanation of possible uses cases. For your organization, defining the API's description during the design phase can help set the boundaries of the API. | Add a description to your API definition's info object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  description: An API description
```

### The info object should have a license

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [info object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#info-object) doesn't have a [license object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#license-object), which helps your API's consumers know how the API can be copied and used. | Add a license object to your API definition's info object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  license:
    name: Apache 2.0
    url: https://opensource.org/licenses/Apache-2.0
```

### The info object should have a license URL

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [license object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#license-object) doesn't have a license URL, which provides a link to a web page that describes the license. Although a license URL isn't required, a license name alone may not be not enough information for your API's consumers, especially when you use a custom license. | Add a URL to your API definition's license object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  license:
    name: Apache 2.0
    url: https://opensource.org/licenses/Apache-2.0
```

### The info object should have a terms of service

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [info object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#info-object) doesn't have the URL of the API's Terms of Service. A terms of service is often mandatory for public APIs. It's also recommended that private APIs provide a link to a Terms and Conditions web page. | Add the URL of the API's Terms of Service to your API definition's info object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  termsOfService: https://example.com/tos
```

### API must have contact information available

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [info object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#info-object) doesn't have a [contact object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#contact-object), which has contact information like a name, email address, or URL. Contact information defines a designated owner for each of your organization's APIs. The contact data may be used directly by your API's consumers, or through an API portal or catalog. | Add a contact object to your API definition's info object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  contact:
    email: support@example.com
    url: https://example.com/support
```

### API must have a contact name available

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [contact object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#contact-object) doesn't have a contact name. Although a contact name isn't required, it helps your API's consumers understand who owns the API. It also makes your organization consider the API's ownership. | Add a name to your API definition's contact object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  contact:
    name: A contact name
```

### API must have a contact URL or email available

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [contact object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#contact-object) doesn't have a contact URL or email address. Although a contact URL or email aren't required, including one or both gives your API's consumers a way to contact your organization or the API owner. | Add a contact URL, an email address, or both to your API definition's contact object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  contact:
    email: contact@example.com
```

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  contact:
    url: https://example.com/support
```

### API must have a contact email available

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [contact object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#contact-object) doesn't have an email address. Although a contact email isn't required, including one gives your API's consumers a way to contact your organization or the API owner. | Add an email address to your API definition's contact object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  contact:
    email: support@example.com
```

### API must have a contact URL available

| Issue description | Possible fix |
| --- | --- |
| Your API definition's [contact object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#contact-object) doesn't have a contact URL. Although a contact URL isn't required, including one gives your API's consumers a way to contact your organization or the API owner. | Add a URL to your API definition's contact object. |

#### Resolution

```json
openapi: '3.0.3'
info:
  title: An API name
  version: '1.0'
  contact:
    url: https://example.com/support
```

## Operations

This rule category deals with operations on an API path.

### There should be no trailing slashes on paths

| Issue description | Possible fix |
| --- | --- |
| One or more [path item objects](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#path-item-object) in your API definition's [paths object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#paths-object) have a trailing slash at the end of the path. Some tools treat a path that ends with a trailing slash (`/path/`) differently from the way that they treat paths without a trailing slash (`/path`), which can lead to problems that require long hours of debugging. | Remove any trailing slashes from paths in your API definition's paths object. |

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  '/resources':
```

### All operations should have summaries

| Issue description | Possible fix |
| --- | --- |
| One or more [operation objects](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object) in your API definition don't have a summary. A summary of what the operation does provides your API's consumers with important context that the HTTP method and path don't provide on their own. Many organizations use the API operation description that they create during the define phase of the API development process as the summary. | Add a summary for each operation object. |

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    get:
      summary: A GET operation summary
```

### Operation summaries shouldn't end with a period

| Issue description | Possible fix |
| --- | --- |
| One or more [operation objects](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object) in your API definition have a summary that ends with a period (`.`). API documentation tools use the summary as a title, so it shouldn't end with a period. | Remove the final period from all summaries at the operations object level in your API definition. |

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    get:
      summary: A GET operation summary
```

### All operations should have descriptions

| Issue description | Possible fix |
| --- | --- |
| One or more [operation objects](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object) in your API definition don't have a description. When the resource path, HTTP method, and summary don't provide enough context for your API's consumers, a description can provide them with useful information about the API operation and its behavior. | Add a description for each operation object. |

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    get:
      description: A GET operation description
```

### All parameters should have descriptions

| Issue description | Possible fix |
| --- | --- |
| One or more [parameter objects](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#parameter-object) in an [operations object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object) in your API definition don't have a `description` field. When the API name and context don't provide enough information for your API's consumers, a description can provide them with useful information about the parameter. | Add a `description` field for each parameter object. |

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    get:
      parameters:
        - name: status
          description: Filters resources on their status
          in: query
          schema:
            type: string
```

### All parameters should have examples

| Issue description | Possible fix |
| --- | --- |
| One or more [parameter objects](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#parameter-object) in an [operations object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object) in your API definition don't have an `example` or `examples` field. It's important to provide undocumented examples (using the `example` property) or documented examples (using the `examples` property) to help your API's consumers understand what data to provide. It may also help them to generate [mock servers](/docs/design-apis/mock-apis/set-up-mock-servers/) or a [collection](/docs/getting-started/first-steps/creating-the-first-collection/). | Add an `example` or `examples` field to provide your API's consumers with an example of the parameter's potential value. |

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    get:
      parameters:
        - name: status
          description: Filters resources on their status
          in: query
          example: done
          schema:
            type: string
```

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    get:
      parameters:
        - name: status
          description: Filters resources on their status
          in: query
          examples:
            anExample:
              summary: An example
              description: A description of an example
              value:
                aProperty: example value
```

### POST methods should have request bodies

| Issue description | Possible fix | 
| --- | --- | 

* [POST methods should have request bodies](#post-methods-should-have-request-bodies)

#### Resolution

```json
openapi: '3.0.3'
# ...
paths:
  /resources:
    post:
      requestBody:
        content:
          'application/json':
            schema:
              type: object
```