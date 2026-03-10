# Source: https://www.speakeasy.com/md/openapi/security/security-schemes/security-openid.md

# The OpenID Connect security scheme in OpenAPI

OpenID Connect is an authentication layer built on top of the OAuth 2.0 protocol. It allows clients to verify the identity of end-users based on the authentication performed by an authorization server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner.

As amazing as OAuth 2.0 is, it doesn't know much about a particular user. It recognizes a user as an entity that has an access token and has some conventions for identifying users, like using `GET /me` or inserting a user ID into a response. OpenID Connect standardizes these conventions and adds more convenience.

The OpenAPI Specification supports OpenID Connect as a security scheme, allowing you to define the scopes and requirements for authentication in your API specification. This enables better security, a more consistent developer experience, and seamless integration with various OpenID Connect providers.

## Defining the OpenID Connect security scheme

To define an OpenID Connect security scheme in your OpenAPI document, use the `openIdConnect` type in the `securitySchemes` section of the [Components Object](https://spec.openapis.org/oas/v3.1.0#components-object). The `openIdConnectUrl` field must point to a JSON OpenID Connect Discovery document, which provides metadata about the OpenID Connect provider.

```yaml
components:
  securitySchemes:
    OpenIDAuth:
      type: openIdConnect
      openIdConnectUrl: https://example.com/.well-known/openid-configuration
security:
  - OpenIDAuth:
    - drink:read
    - drink:write
paths:
  /drinks:
    get:
      operationId: listDrinks
      summary: Get a list of drinks
      # Operation requires read scope
      security:
        - OpenIDAuth:
          - drink:read
    post:
      operationId: createDrink
      summary: Create a new drink
      # Operation requires write scope
      security:
        - OpenIDAuth:
          - drink:write
```

In OpenAPI, the OpenID Connect security scheme is defined as part of the [Security Scheme Object](https://spec.openapis.org/oas/v3.1.0#security-scheme-object). This allows you to specify the type of security scheme as `openIdConnect`, along with the URL to the OpenID Connect Discovery document.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | String | ✅ | `openIdConnect` |
| `description` | String |  | Human-readable information. This may contain [CommonMark syntax](https://spec.commonmark.org/) to provide a rich description. |
| `openIdConnectUrl` | String | ✅ | The URL must point to a JSON OpenID Connect Discovery document. |
| `x-*` | [Extensions](/openapi/extensions) |  | Any number of extension fields can be added to the Security Scheme Object to be used by tooling and vendors. |

## Scopes in OpenID Connect

Scopes limit the access granted to an application when it uses OpenID Connect. They define the permissions that the application can request from the user, such as reading or writing data.

To use scopes in OpenID Connect, define them in the Security Scheme Object as an array of strings, where each string represents a specific permission that the application can request.

```yaml
components:
  securitySchemes:
    OpenIDAuth:
      type: openIdConnect
      openIdConnectUrl: https://example.com/.well-known/openid-configuration
      description: "OpenID Connect security scheme with scopes for drink management."
      scopes:
        drink:read: "Allows reading drink information"
        drink:write: "Allows writing drink information"
```

To use these scopes in your API operations, also define them in the [Security Requirement Object](/openapi/security). This allows you to control which operations require which scopes, providing fine-grained access control at the global level as well as the operation level.

```yaml
paths:
  /drinks:
    get:
      operationId: listDrinks
      summary: Get a list of drinks
      security:
        - OpenIDAuth:
          - drink:read
    post:
      operationId: createDrink
      summary: Create a new drink
      security:
        - OpenIDAuth:
          - drink:write
```

## The benefits of using OpenID Connect

Using OpenID Connect in your OpenAPI document provides advantages for SDK generation, documentation, and security, including the following key benefits:

- **Standardization**: OpenID Connect provides a standardized way to handle user authentication and authorization, making it easier for developers to implement and understand.
- **Interoperability**: OpenID Connect is widely supported by various identity providers, allowing seamless integration with existing systems.
- **Security**: By defining scopes and security requirements in your OpenAPI document, you can enforce fine-grained access control, ensuring that only authorized users can access specific operations.
- **Developer experience**: OpenAPI's support for OpenID Connect enhances the developer experience by providing clear documentation and guidelines for authentication, making it easier for developers to understand how to use your API securely.
- **Tooling support**: Many tools and libraries support OpenID Connect, allowing for easy integration with your API and simplifying the authentication process for developers.
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
