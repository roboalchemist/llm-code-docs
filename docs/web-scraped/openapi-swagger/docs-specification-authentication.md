# Source: https://swagger.io/docs/specification/authentication/

# Authentication
Note

OAS3This guide is for OpenAPI 3.0. If you use OpenAPI 2.0, see ourOpenAPI 2.0 guide.

[OpenAPI 2.0 guide](/docs/specification/v2_0/authentication/authentication/) OpenAPI uses the termsecurity schemefor authentication and authorization schemes. OpenAPI 3.0 lets you describe APIs protected using the following security schemes:

- HTTP authentication schemes (they use theAuthorizationheader):BasicBearerother HTTP schemes as defined byRFC 7235andHTTP Authentication Scheme Registry
`Authorization` - Basic
[Basic](/docs/specification/authentication/basic-authentication/) - Bearer
[Bearer](/docs/specification/authentication/bearer-authentication/) - other HTTP schemes as defined byRFC 7235andHTTP Authentication Scheme Registry
[RFC 7235](https://tools.ietf.org/html/rfc7235) [HTTP Authentication Scheme Registry](https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml) - API keysin headers, query string or cookiesCookie authentication
[API keys](/docs/specification/authentication/api-keys/) - Cookie authentication
[Cookie authentication](/docs/specification/authentication/cookie-authentication/) - OAuth 2
[OAuth 2](/docs/specification/authentication/oauth2/) - OpenID Connect Discovery
[OpenID Connect Discovery](/docs/specification/authentication/openid-connect-discovery/) Follow the links above for the guides on specific security types, or continue reading to learn how to describe security in general.

### Changes from OpenAPI 2.0
If you used OpenAPI 2.0 before, here is a summary of changes to help you get started with OpenAPI 3.0:

- securityDefinitionswere renamed tosecuritySchemesand moved insidecomponents.
`securityDefinitions` `securitySchemes` `components` - type: basicwas replaced withtype: httpandscheme: basic.
`type: basic` `type: http` `scheme: basic` - The newtype: httpis an umbrella type for all HTTP security schemes, including Basic, Bearer and other, and theschemekeyword indicates the scheme type.
`type: http` `scheme` - API keys can now be sentin: cookie.
`in: cookie` - Added support for OpenID Connect Discovery (type: openIdConnect).
`type: openIdConnect` - OAuth 2 security schemes can now define multipleflows.
`flows` - OAuth 2 flows were renamed to match theOAuth 2 Specification:accessCodeis nowauthorizationCode, andapplicationis nowclientCredentials.
[OAuth 2 Specification](https://tools.ietf.org/html/rfc6749#section-1.3) `accessCode` `authorizationCode` `application` `clientCredentials` ### Describing Security
Security is described using thesecuritySchemesandsecuritykeywords. You usesecuritySchemesto define all security schemes your API supports, then usesecurityto apply specific schemes to the whole API or individual operations.

`securitySchemes` `security` `securitySchemes` `security` #### Step 1. Defining securitySchemes
All security schemes used by the API must be defined in the globalcomponents/securitySchemessection. This section contains a list of named security schemes, where each scheme can be oftype:

`components/securitySchemes` `type` - http– forBasic,Bearerand other HTTP authentications schemes
`http` [Basic](/docs/specification/authentication/basic-authentication/) [Bearer](/docs/specification/authentication/bearer-authentication/) - apiKey– forAPI keysandcookie authentication
`apiKey` [API keys](/docs/specification/authentication/api-keys/) [cookie authentication](/docs/specification/authentication/cookie-authentication/) - oauth2– forOAuth 2
`oauth2` [OAuth 2](/docs/specification/authentication/oauth2/) - openIdConnect– forOpenID Connect Discovery
`openIdConnect` [OpenID Connect Discovery](/docs/specification/authentication/openid-connect-discovery/) Other required properties for security schemes depend on thetype. The following example shows how various security schemes are defined. TheBasicAuth,BearerAuthnames and others are arbitrary names that will be used to refer to these definitions from other places in the spec.

`type` ```
1components:2  securitySchemes:3    BasicAuth:4      type: http5      scheme: basic6
7    BearerAuth:8      type: http9      scheme: bearer10
11    ApiKeyAuth:12      type: apiKey13      in: header14      name: X-API-Key15
16    OpenID:17      type: openIdConnect18      openIdConnectUrl: https://example.com/.well-known/openid-configuration19
20    OAuth2:21      type: oauth222      flows:23        authorizationCode:24          authorizationUrl: https://example.com/oauth/authorize25          tokenUrl: https://example.com/oauth/token26          scopes:27            read: Grants read access28            write: Grants write access29            admin: Grants access to admin operations```

#### Step 2. Applying security
After you have defined the security schemes in thesecuritySchemessection, you can apply them to the whole API or individual operations by adding thesecuritysection on the root level or operation level, respectively. When used on the root level,securityapplies the specified security schemes globally to all API operations, unless overridden on the operation level. In the following example, the API calls can be authenticated using either an API key or OAuth 2. TheApiKeyAuthandOAuth2names refer to the schemes previously defined insecuritySchemes.

`securitySchemes` `security` `security` `securitySchemes` ```
1security:2  - ApiKeyAuth: []3  - OAuth2:4      - read5      - write6# The syntax is:7# - scheme name:8#     - scope 19#     - scope 2```

For each scheme, you specify a list of security scopes required for API calls (seebelow). Scopes are used only for OAuth 2 and OpenID Connect Discovery; other security schemes use an empty array[]instead. Globalsecuritycan be overridden in individual operations to use a different authentication type, different OAuth/OpenID scopes, or no authentication at all:

[below](#scopes) `[]` `security` ```
1paths:2  /billing_info:3    get:4      summary: Gets the account billing info5      security:6        - OAuth2: [admin] # Use OAuth with a different scope7      responses:8        "200":9          description: OK10        "401":11          description: Not authenticated12        "403":13          description: Access token does not have the required scope14
15  /ping:16    get:17      summary: Checks if the server is running18      security: [] # No security19      responses:20        "200":21          description: Server is up and running22        default:23          description: Something is wrong```

### Scopes
OAuth 2 and OpenID Connect usescopesto control permissions to various user resources. For example, the scopes for a pet store may includeread_pets,write_pets,read_orders,write_orders,admin. When applyingsecurity, the entries corresponding to OAuth 2 and OpenID Connect need to specify a list of scopes required for a specific operation (ifsecurityis used on the operation level) or all API calls (ifsecurityis used on the root level).

`read_pets` `write_pets` `read_orders` `write_orders` `admin` `security` `security` `security` ```
1security:2  - OAuth2:3      - scope14      - scope25  - OpenId:6      - scopeA7      - scopeB8  - BasicAuth: []```

`1security:2-OAuth2:3-scope14-scope25-OpenId:6-scopeA7-scopeB8-BasicAuth:[]` - In case of OAuth 2, the scopes used insecuritymust be previously defined insecuritySchemes.
`security` `securitySchemes` - In case of OpenID Connect Discovery, possible scopes are listed in the discovery endpoint specified byopenIdConnectUrl.
`openIdConnectUrl` - Other schemes (Basic, Bearer, API keys and others) do not use scopes, so theirsecurityentries specify an empty array[]instead.
`security` `[]` Different operations typically require different scopes, such as read vs write vs admin. In this case, you should apply scopedsecurityto specific operations instead of doing it globally.

`security` ```
1# Instead of this:2# security:3#   - OAuth2:4#       - read5#       - write6
7# Do this:8paths:9  /users:10    get:11      summary: Get a list of users12      security:13        - OAuth2: [read]     # <------14      ...15
16    post:17      summary: Add a user18      security:19        - OAuth2: [write]    # <------20      ...```

### Using Multiple Authentication Types
Some REST APIs support several authentication types. Thesecuritysection lets you combine the security requirements using logical OR and AND to achieve the desired result.securityuses the following logic:

`security` `security` ```
1security: # A OR B2  - A3  - B```

`1security:# A OR B2-A3-B` ```
1security: # A AND B2  - A3    B```

`1security:# A AND B2-A3B` ```
1security: # (A AND B) OR (C AND D)2  - A3    B4  - C5    D```

`1security:# (A AND B) OR (C AND D)2-A3B4-C5D` That is,securityis an array of hashmaps, where each hashmap contains one or more named security schemes. Items in a hashmap are combined using logical AND, and array items are combined using logical OR. Security schemes combined via OR are alternatives – any one can be used in the given context. Security schemes combined via AND must be used simultaneously in the same request. Here, we can use either Basic authentication or an API key:

`security` ```
1security:2  - basicAuth: []3  - apiKey: []```

`1security:2-basicAuth:[]3-apiKey:[]` Here, the API requires a pair of API keys to be included in requests:

```
1security:2  - apiKey1: []3    apiKey2: []```

`1security:2-apiKey1:[]3apiKey2:[]` Here, we can use either OAuth 2 or a pair of API keys:

```
1security:2  - oauth2: [scope1, scope2]3  - apiKey1: []4    apiKey2: []```

`1security:2-oauth2:[scope1,scope2]3-apiKey1:[]4apiKey2:[]` ### Reference
Security Scheme Object

[Security Scheme Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.4.md#security-scheme-object) Security Requirement Object

[Security Requirement Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.4.md#security-requirement-object) Did not find what you were looking for?Ask the communityFound a mistake?Let us know

[Ask the community](https://community.smartbear.com/t5/Swagger-Open-Source-Tools/bd-p/SwaggerOSTools) [Let us know](https://github.com/swagger-api/swagger.io/issues)