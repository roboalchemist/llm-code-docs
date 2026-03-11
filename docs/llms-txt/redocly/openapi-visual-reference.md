# Source: https://redocly.com/learn/openapi/openapi-visual-reference.md

# Redocly's visual reference to OpenAPI

Before you start, it's helpful to:

- Know [what's an API](https://redocly.com/blog/whats-an-api/)
- Learn the [YAML essentials](/learn/yaml)
- Be comfortable with Markdown


## The OpenAPI Specification

From the specification:

> The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to HTTP APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic.
An OpenAPI definition can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.


**Restated:** OpenAPI describes HTTP APIs (sometimes referred to as REST APIs). It can be generated and consumed by both machines and people.

## Structure of this visual reference

Navigate throughout the OpenAPI file structure, and each page contains:

- Excerpts from the OAS
- YAML examples with Redocly rendered screenshots
- Type definitions (which is how you can interact with specs programmatically using custom rules and decorators).


## Difference from Swagger

Swagger is the former name of OpenAPI.

In 2015, SmartBear Software donated the Swagger specification to the Linux Foundation, and renamed the specification to the OpenAPI Specification.

Interested in the origin of the swagger name?
[Perfect for API trivia](https://twitter.com/adamaltman/status/1304060760583270402).

## OpenAPI file structure

An OpenAPI file is a YAML or JSON file with these root mapping keys:

- [openapi](/learn/openapi/openapi-visual-reference/openapi) (**REQUIRED**)
- [info](/learn/openapi/openapi-visual-reference/info) (**REQUIRED**)
- [servers](/learn/openapi/openapi-visual-reference/servers)
- [paths](/learn/openapi/openapi-visual-reference/paths) (**REQUIRED in 3.0**)
- [webhooks](/learn/openapi/openapi-visual-reference/webhooks) (Introduced in 3.1, and Redocly supports it in 3.0 as `x-webhooks` -- keys starting with `x-` are known as "specification extensions")
- [components](/learn/openapi/openapi-visual-reference/components)
- [security](/learn/openapi/openapi-visual-reference/security)
- [tags](/learn/openapi/openapi-visual-reference/tags)
- [externalDocs](/learn/openapi/openapi-visual-reference/external-docs)
- jsonSchemaDialect (Introduced in 3.1)


The Redocly type to describe the root is `Root`.

As a quick refresher from YAML maps, the order of the keys isn't important, so these may appear in any order within the OpenAPI root document.

The following is an example of a minimal OpenAPI 3.0 file:


```yaml
openapi: 3.0.3
info:
  title: Minimal example
  version: demo
paths: {}
```

Note that the three required root mapping keys have their own required properties.

## Reference structure

- [openapi](/learn/openapi/openapi-visual-reference/openapi)
- [info](/learn/openapi/openapi-visual-reference/info)
  - [contact](/learn/openapi/openapi-visual-reference/contact)
  - [license](/learn/openapi/openapi-visual-reference/license)
- [servers](/learn/openapi/openapi-visual-reference/servers)
  - [server variables](/learn/openapi/openapi-visual-reference/server-variables)
- [paths](/learn/openapi/openapi-visual-reference/paths)
  - [path items](/learn/openapi/openapi-visual-reference/path-item)
  - [operations](/learn/openapi/openapi-visual-reference/operation)
    - [parameters](/learn/openapi/openapi-visual-reference/parameters)
    - [media type objects](/learn/openapi/openapi-visual-reference/media-type)
    - [request body](/learn/openapi/openapi-visual-reference/request-body)
    - [responses](/learn/openapi/openapi-visual-reference/responses)
      - [response](/learn/openapi/openapi-visual-reference/response)
- [webhooks (or x-webhooks)](/learn/openapi/openapi-visual-reference/webhooks)
- [components](/learn/openapi/openapi-visual-reference/components)
  - [schemas](/learn/openapi/openapi-visual-reference/schemas)
    - [string](/learn/openapi/openapi-visual-reference/string)
    - [number](/learn/openapi/openapi-visual-reference/number)
    - [integer](/learn/openapi/openapi-visual-reference/integer)
    - [array](/learn/openapi/openapi-visual-reference/array)
    - [object](/learn/openapi/openapi-visual-reference/object)
    - [null](/learn/openapi/openapi-visual-reference/null)
  - [responses](/learn/openapi/openapi-visual-reference/named-responses)
  - [parameters](/learn/openapi/openapi-visual-reference/parameters)
    - [parameter](/learn/openapi/openapi-visual-reference/parameter)
  - [examples](/learn/openapi/openapi-visual-reference/examples)
    - [example](/learn/openapi/openapi-visual-reference/example)
  - [requestBodies](/learn/openapi/openapi-visual-reference/named-request-bodies)
  - [headers](/learn/openapi/openapi-visual-reference/header)
  - [pathItems](/learn/openapi/openapi-visual-reference/named-path-items)
  - [securitySchemes](/learn/openapi/openapi-visual-reference/security-schemes)
    - [OAuth2 flows](/learn/openapi/openapi-visual-reference/oauth-flows)
  - [links](/learn/openapi/openapi-visual-reference/links)
  - [callbacks](/learn/openapi/openapi-visual-reference/callbacks)
  - [reference objects (`$ref`)](/learn/openapi/openapi-visual-reference/reference)
- [security](/learn/openapi/openapi-visual-reference/security)
- [tags](/learn/openapi/openapi-visual-reference/tags)
- [externalDocs](/learn/openapi/openapi-visual-reference/external-docs)
- [specification extensions](/learn/openapi/openapi-visual-reference/specification-extensions)