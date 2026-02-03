# openapi2

You can use Postman to identify any potential security and formatting issues when defining your API.

![OpenAPI 2.0 rule violations](https://assets.postman.com/postman-docs/v11/api-definition-rule-violations-openapi2-v11.jpg)

## Warnings for OpenAPI 2

For all APIs defined in OpenAPI 2.0, the following list describes possible warning messages and potential ways to resolve them.

* [Broken object level authorization](#broken-object-level-authorization)
    * [Scope for OAuth scheme used in security field is not defined in the securityDefinition declaration](#scope-for-oauth-scheme-used-in-security-field-is-not-defined-in-the-securitydefinition-declaration)
    * [Scope for OAuth scheme used is not defined in the securityDefinition declaration](#scope-for-oauth-scheme-used-is-not-defined-in-the-securitydefinition-declaration)
* [Broken user authentication](#broken-user-authentication)
    * [Security field is not defined](#security-field-is-not-defined)
    * [Security field does not contain any item](#security-field-does-not-contain-any-item)
    * [Security field does not contain any scheme](#security-field-does-not-contain-any-scheme)
    * [Security definition object not defined](#security-definition-object-not-defined)
    * [Security definition object does not contain any scheme](#security-definition-object-does-not-contain-any-scheme)
    * [Scheme used in security field is not defined in the security definition object](#scheme-used-in-security-field-is-not-defined-in-the-security-definition-object)
    * [Security field for the operation does not contain any item](#security-field-for-the-operation-does-not-contain-any-item)
    * [Security field for the operation does not contain any scheme](#security-field-for-the-operation-does-not-contain-any-scheme)
    * [Operation does not enforce any security scheme](#operation-does-not-enforce-any-security-scheme)
* [Excessive data exposure](#excessive-data-exposure)
    * [API accepts credentials from OAuth authentication in plain text](#api-accepts-credentials-from-oauth-authentication-in-plain-text)
    * [API accepts API key in plain text](#api-accepts-api-key-in-plain-text)
    * [API accepts basic authentication credentials in plain text](#api-accepts-basic-authentication-credentials-in-plain-text)
    * [Global schemes have HTTP scheme defined](#global-schemes-have-http-scheme-defined)
    * [Operation accepts credentials from OAuth authentication in plain text](#operation-accepts-credentials-from-oauth-authentication-in-plain-text)
    * [Operation accepts API key in plain text](#operation-accepts-api-key-in-plain-text)
    * [Operation accepts basic authentication credentials in plain text](#operation-accepts-basic-authentication-credentials-in-plain-text)
    * [Schemes of the operation have HTTP scheme defined](#schemes-of-the-operation-have-http-scheme-defined)
    * [Authorization URL uses HTTP protocol; credentials will be transferred as plain text](#authorization-url-uses-http-protocol-credentials-will-be-transferred-as-plain-text)
    * [Token URL uses HTTP protocol](#token-url-uses-http-protocol)
    * [Produces field is not defined](#produces-field-is-not-defined)
    * [Produces field does not contain any item](#produces-field-does-not-contain-any-item)
    * [Produces field for the operation does not contain any item](#produces-field-for-the-operation-does-not-contain-any-item)
    * [Operation does not contain produces field](#operation-does-not-contain-produces-field)
* [Injection](#injection)
    * [Consumes field is not defined](#consumes-field-is-not-defined)
    * [Consumes field does not contain any item](#consumes-field-does-not-contain-any-item)
    * [Consumes field for the operation does not contain any item](#consumes-field-for-the-operation-does-not-contain-any-item)
    * [Operation does not contain consumes field](#operation-does-not-contain-consumes-field)
* [Improper assets management](#improper-assets-management)
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

### Scope for OAuth scheme used in security field is not defined in the securityDefinition declaration

| Issue description | Possible fix |
| --- | --- |
| The OAuth2 scopes used in the global security field need to be defined in the security schemes field. Otherwise, an attacker can introduce their scopes to fill the gap and exploit the system. | Make sure that all the OAuth2 scopes used are defined in the OAuth2 security scheme. |

#### Resolution

```json
swagger: '2.0'
#...
security:
  - OAuth2:
    - read
    - write
securityDefinitions:
  OAuth2:
    type: oauth2
    flow: accessCode
    scopes:
      read: read object
      write: writes object
    authorizationUrl: https://example.com/authorize
    tokenUrl: https://example.com/token
```

### Scope for OAuth scheme used is not defined in the securityDefinition declaration

| Issue description | Possible fix |
| --- | --- |
| The OAuth2 scopes used in the security field of the operation need to be defined in the security schemes field. Otherwise, an attacker can introduce their scopes to fill the gap and exploit the system. | Make sure that all the OAuth2 scopes used are defined in the OAuth2 security scheme. |

#### Resolution

```json
swagger: '2.0'
#...
paths:
  '/user':
    get:
      summary: 'Sample endpoint: Returns details about a particular user'
      operationId: listUser
      security:
        - OAuth2:
          - read
          - write
securityDefinitions:
  OAuth2:
    type: oauth2
    flow: accessCode
    scopes:
      read: read object
      write: writes object
    authorizationUrl: https://example.com/authorize
    tokenUrl: https://example.com/token
```

## Broken user authentication

### Security field is not defined

| Issue description | Possible fix |
| --- | --- |
| If the global security field isn't defined, the API doesn't require any authentication by default. Anyone can access the API operations that don't have a security field defined. | The security field needs to be defined in the schema. |

#### Resolution

```json
swagger: '2.0'
#...
securityDefinitions:
  basicAuth:
    type: basic
security:
    - basicAuth: []
```

### Security field does not contain any item

| Issue description | Possible fix |
| --- | --- |
| If the security field has an empty array, no security scheme is applied to the operations by default. | The security field needs to have at least one item in the array. |

#### Resolution

```json
swagger: '2.0'
#...
securityDefinitions:
  basicAuth:
    type: basic
security:
    - basicAuth: []
```

### Security field does not contain any scheme

| Issue description | Possible fix |
| --- | --- |
| An empty object in the security field deactivates the authentication. Without security fields defined for each operation, anyone can access the API operations without any authentication. | Security field array items can't have an empty object. |

#### Resolution

```json
swagger: '2.0'
#...
securityDefinitions:
  basicAuth:
    type: basic
security:
    - basicAuth: []
```

### Security definition object not defined

| Issue description | Possible fix |
| --- | --- |
| The components object of the API doesn't declare any security definitions which can be used in the security field of the API or individual operations. | Security definitions need to be defined in the schema of the component. |

#### Resolution

```json
swagger: '2.0'
#...
securityDefinitions:
  basicAuth:
    type: basic
```

### Security definition object does not contain any scheme

| Issue description | Possible fix |
| --- | --- |
| An empty object in the reusable security definition means that no authentication scheme is defined for each operation, anyone can access the API operations without any authentication. | Security definitions need to have at least one item in the object. |

#### Resolution

```json
swagger: '2.0'
#...
securityDefinitions:
  basicAuth:
    type: basic
```

### Scheme used in security field is not defined in the security definition object

| Issue description | Possible fix |
| --- | --- |
| The authentication scheme used in global or operation security field isn't defined in the security definition object. | The scheme used in the security field needs to be defined in the security definition object. |

#### Resolution

```json
swagger: '2.0'
#...
securityDefinitions:
  basicAuth:
    type: basic
security:
    - basicAuth: []
```

### Security field for the operation does not contain any item

| Issue description | Possible fix |
| --- | --- |
| No security scheme is applied to the API operation by default. | The security field in any operation needs to have at least one item in the array. |

#### Resolution

```json
swagger: '2.0'
#...
paths:
  /user:
    get:
      description: 'Returns details about a particular user'
      security:
          - basicAuth: []
      #...
securityDefinitions:
  basicAuth:
    type: basic
```

### Security field for the operation does not contain any scheme

| Issue description | Possible fix |
| --- | --- |
| An empty object in the security field deactivates the authentication for the operation. Anyone can access the API operation without any authentication. | Specify at least one security requirement in the operation. |

#### Resolution

```json
swagger: '2.0'
#...
paths:
  /user:
    get:
      description: 'Returns details about a particular user'
      security:
          - basicAuth: []
      #...
securityDefinitions:
  basicAuth:
    type: basic
```

### Operation does not enforce any security scheme

| Issue description | Possible fix |
| --- | --- |
| If both the global security field and operation's security field aren't defined, anyone can access the API without any authentication. | Define a security field in the operation. |

#### Resolution

```json
swagger: '2.0'
#...
paths:
  /user:
    get:
      description: 'Sample endpoint: Returns details about a particular user'
      security:
          - basicAuth: []
      #...
securityDefinitions:
  basicAuth:
    type: basic
```

## Excessive data exposure

### API accepts credentials from OAuth authentication in plain text

| Issue description | Possible fix |
| --- | --- |
| The access tokens are sent as plain text over an unencrypted network. Attackers can intercept the access tokens by listening to the network traffic in a public Wi-Fi network. | Make sure that the scheme used in the schemes array is HTTPS. |

#### Resolution

```json
swagger: '2.0'
#...
host: 'example.com'
schemes:
  - https
securityDefinitions:
  OAuth2:
    type: oauth2
    flow: accessCode
    authorizationUrl: https://my.auth.example.com/
    tokenUrl: https://my.token.example.com/
security:
 - OAuth2: []
```

### API accepts API key in plain text

| Issue description | Possible fix |
| --- | --- |
| API keys are sent as plain text over an unencrypted channel. Attackers can intercept API key by listening to the network traffic in a public Wi-Fi network. | Make sure that the scheme used in the scheme array is HTTPS. |

#### Resolution

```json
swagger: '2.0'
#...
host: 'example.com'
schemes:
  - https
securityDefinitions:
  apiKeyAuth:
    type: apiKey
    name: api_key
    in: header
security:
  - apiKeyAuth: []
```

### API accepts basic authentication credentials in plain text

| Issue description | Possible fix |
| --- | --- |
| The credentials are sent as plain text over an unencrypted network. Attackers can intercept the credentials by listening to the network traffic in a public Wi-Fi network. | Make sure that the scheme used in the scheme array is HTTPS. |

#### Resolution

```json
swagger: '2.0'
#...
host: 'example.com'
schemes:
  - https
securityDefinitions:
  basicAuth:
    type: basic
security:
 - basicAuth: []
```

### Global schemes have HTTP scheme defined

| Issue description | Possible fix |
| --- | --- |
| The server supports unencrypted HTTP connections, all requests and responses will be transmitted in the open. Anyone listening to the network traffic while the calls are being made can intercept them. | Make sure that the scheme used in the scheme array is HTTPS. |

#### Resolution

```json
swagger: '2.0'
#...
host: 'example.com'
schemes:
  - https
#...
```

### Operation accepts credentials from OAuth authentication in plain text

| Issue description | Possible fix |
| --- | --- |
| The API operation accepts the access tokens from a flow that are transported in plain text over an unencrypted channel. Attackers can intercept API calls and retrieve the unencrypted tokens. They can then use the tokens to make other API calls. | Make sure that the scheme used in the scheme array of the operation is HTTPS.|