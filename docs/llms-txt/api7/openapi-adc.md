# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/openapi-adc.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/openapi-adc.md

# OpenAPI Converter Reference

ADC can convert OpenAPI v3.0 specifications to ADC configuration with theÂ `adc convert openapi`Â command. This document provides a reference for the supported extensions/custom properties to configure API7 Enterprise-specific features like routes, plugins, and labels.

ADC OpenAPI extensions are supported at the following levels of a specification:

* Root level: The root level of the API specification. Properties at the root level are applied to the entire service.
* Path level: Path sections in the specification. Properties at the path level are applied to the specific route.
* Operation level: Each HTTP method in a path section. Properties at the operation level are applied to the specific HTTP method of the route.
* Server level: Server sections in the root, path, or operation level. Properties at the server level are applied to upstreams.

## Supported Extensions[â](#supported-extensions "Direct link to Supported Extensions")

The table below lists the supported extensions and their levels:

| Extension                    | Level              | Description                                                                                                                                                                |
| ---------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| x-adc-name                   | Root               | Set the service name.                                                                                                                                                      |
|                              | Operation          | Set the specific route name.                                                                                                                                               |
| x-adc-labels                 | Root               | Add labels to the service, route, or method as specified by the level. Value can be a string or a string array for multiple labels.                                        |
|                              | Path               |                                                                                                                                                                            |
|                              | Operation          |                                                                                                                                                                            |
| x-adc-plugins                | Root               | Add plugins globally to a service. Value is an object containing one or more plugins.                                                                                      |
|                              | Path               | Add plugins to a route or a method as specified by the level. Adding plugins at the operation level will split the routes, one including the plugin and the other without. |
|                              | Operation          |                                                                                                                                                                            |
| x-adc-plugin-\[plugin-name]  | Root               | Similar to `x-adc-plugins` but for a single plugin. These plugins will override the plugins with the same name configured in `x-adc-plugins`.                              |
|                              | Path               |                                                                                                                                                                            |
|                              | Operation          |                                                                                                                                                                            |
| x-adc-service-defaults       | Root               | Set the service parameters on a service, route, or method as specified by the level.                                                                                       |
|                              | Path               |                                                                                                                                                                            |
|                              | Operation          |                                                                                                                                                                            |
| x-adc-upstream-defaults      | Root               | Set the upstream parameters on a service, route, or method as specified by the level.                                                                                      |
|                              | Path               |                                                                                                                                                                            |
|                              | Operation          |                                                                                                                                                                            |
| x-adc-upstream-node-defaults | Root - Server      | Set the node parameters of the upstream on a service, route, or method as specified by the level.                                                                          |
|                              | Path - Server      |                                                                                                                                                                            |
|                              | Operation - Server |                                                                                                                                                                            |
| x-adc-route-defaults         | Root               | Set the route parameters on a service, route, or method as specified by the level.                                                                                         |
|                              | Path               |                                                                                                                                                                            |
|                              | Operation          |                                                                                                                                                                            |

## Example Specification[â](#example-specification "Direct link to Example Specification")

The example specification below shows how to use the extensions:

```
openapi: 3.1.0
info:
  title: httpbin API
  description: httpbin API for the API7 Enterprise Getting Started guides.
  version: 1.0.0
servers:
  - url: 'http://httpbin.org:80'
x-adc-labels:
  server: production
  api: httpbin
x-adc-plugins:
  key-auth:
    _meta:
      disable: false
paths:
  /anything/*:
    get:
      summary: Returns anything that is passed into the request.
      x-adc-name: httpbin-anything
      x-adc-service-defaults:
        path_prefix: /api
      x-adc-upstream-defaults:
        timeout:
          connect: 10
          send: 10
          read: 10
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: string
```
