# Source: https://tyk.io/docs/api-management/traffic-transformation/ignore-authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ignore Authentication

> How to configure Ignore Authentication traffic transformation middleware in Tyk

## Overview

<a id="ignore-authentication-overview" />

The Ignore Authentication middleware instructs Tyk Gateway to skip the authentication step for calls to an endpoint, even if authentication is enabled for the API.

### Use Cases

#### Health and liveness endpoints

This plugin can be very useful if you have an endpoint (such as a ping or health check) that you don’t need to secure.

### Working

When the Ignore Authentication middleware is configured for a specific endpoint, it instructs the gateway to bypass the client authentication process for requests made to that endpoint. If other (non-authentication) middleware are configured for the endpoint, they will still execute on the request.

It is important to exercise caution when using the Ignore Authentication middleware, as it effectively disables Tyk's security features for the ignored paths. Only endpoints that are designed to be public or have independent security mechanisms should be configured to bypass authentication in this way. When combining Ignore Authentication with response transformations be careful not to inadvertently expose sensitive data or rely on authentication or session data that is not present.

#### Case sensitivity

By default the ignore authentication middleware is case-sensitive. If, for example, you have defined the endpoint `GET /ping` in your API definition then only calls to `GET /ping` will ignore the authentication step: calls to `GET /Ping` or `GET /PING` will require authentication. You can configure the middleware to be case insensitive at the endpoint level.

You can also set case sensitivity for the entire Tyk Gateway in its [configuration file](/tyk-oss-gateway/configuration#ignore_endpoint_case) `tyk.conf`. If case insensitivity is configured at the gateway level, this will override the endpoint-level setting.

#### Endpoint parsing

When using the ignore authentication middleware, we recommend that you familiarize yourself with Tyk's [URL matching](/getting-started/key-concepts/url-matching) options.

<br />

<Note>
  Tyk recommends that you use [exact](/getting-started/key-concepts/url-matching#exact-match) matching for maximum security, though prefix and wildcard strategies might also apply for your particular deployment or use case.
</Note>

<hr />

## Using Tyk OAS

<a id="ignore-authentication-using-tyk-oas" />

The [Ignore Authentication](/api-management/traffic-transformation/ignore-authentication) middleware instructs Tyk Gateway to skip the authentication step for calls to an endpoint, even if authentication is enabled for the API.

When working with Tyk OAS APIs the middleware is configured in the [Tyk OAS API Definition](/api-management/gateway-config-tyk-oas#operation). You can do this via the Tyk Dashboard API or in the API Designer.

If you're using the legacy Tyk Classic APIs, then check out the [Tyk Classic](#ignore-authentication-using-classic) page.

### API Definition

The design of the Tyk OAS API Definition takes advantage of the `operationId` defined in the OpenAPI Document that declares both the path and method for which the middleware should be added. Endpoint `paths` entries (and the associated `operationId`) can contain wildcards in the form of any string bracketed by curly braces, for example `/status/{code}`. These wildcards are so they are human readable and do not translate to variable names. Under the hood, a wildcard translates to the “match everything” regex of: `(.*)`.

The ignore authentication middleware (`ignoreAuthentication`) can be added to the `operations` section of the Tyk OAS Extension (`x-tyk-api-gateway`) in your Tyk OAS API Definition for the appropriate `operationId` (as configured in the `paths` section of your OpenAPI Document).

The `ignoreAuthentication` object has the following configuration:

* `enabled`: enable the middleware for the endpoint
* `ignoreCase`: if set to `true` then the path matching will be case insensitive

For example:

```json {hl_lines=["65-69"],linenos=true, linenostart=1} theme={null}
{
    "info": {
        "title": "example-ignore-authentication",
        "version": "1.0.0"
    },
    "openapi": "3.0.3",
    "servers": [
        {
            "url": "http://localhost:8181/example-ignore-authentication/"
        }
    ], 
    "security": [
        {
            "authToken": []
        }
    ],     
    "paths": {
        "/anything": {
            "get": {
                "operationId": "anythingget",
                "responses": {
                    "200": {
                        "description": ""
                    }
                }
            }
        }
    },
    "components": {
        "securitySchemes": {
            "authToken": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization"
            }
        }        
    },    
    "x-tyk-api-gateway": {
        "info": {
            "name": "example-ignore-authentication",
            "state": {
                "active": true,
                "internal": false
            }
        },
        "upstream": {
            "url": "http://httpbin.org/"
        },
        "server": {
            "authentication": {
                "enabled": true,
                "securitySchemes": {
                    "authToken": {
                        "enabled": true
                    }
                }
            },
            "listenPath": {
                "strip": true,
                "value": "/example-ignore-authentication/"
            }        
        },
        "middleware": {
            "operations": {
                "anythingget": {
                    "ignoreAuthentication": {
                        "enabled": true
                    }
                }
            }
        }
    }
}
```

In this example the ignore authentication middleware has been configured for requests to the `GET /anything` endpoint. Any such calls will skip the authentication step in the Tyk Gateway's processing chain.

* the middleware has been configured to be case sensitive, so calls to `GET /Anything` will not skip authentication

The configuration above is a complete and valid Tyk OAS API Definition that you can import into Tyk to try out the Ignore Authentication middleware.

### API Designer

Adding and configuring the Ignore Authentication middleware to your API endpoints is easy when using the API Designer in the Tyk Dashboard, simply follow these steps:

1. **Add an endpoint**

   From the **API Designer** add an endpoint that matches the path and method to which you want to apply the middleware.

   <img src="https://mintcdn.com/tyk/jzHiRUIhvyphWUhc/img/dashboard/api-designer/tyk-oas-no-endpoints.png?fit=max&auto=format&n=jzHiRUIhvyphWUhc&q=85&s=8af9cb5452bc838ce39b545399583f9e" alt="Tyk OAS API Designer showing no endpoints created" width="1237" height="711" data-path="img/dashboard/api-designer/tyk-oas-no-endpoints.png" />

   <img src="https://mintcdn.com/tyk/rz4rHtIOKIA9WnL8/img/dashboard/api-designer/tyk-oas-add-endpoint.png?fit=max&auto=format&n=rz4rHtIOKIA9WnL8&q=85&s=0a01cfad6cccb0246bdeadb5bcdb9a56" alt="Adding an endpoint to an API using the Tyk OAS API Designer" width="627" height="635" data-path="img/dashboard/api-designer/tyk-oas-add-endpoint.png" />

   <img src="https://mintcdn.com/tyk/jzHiRUIhvyphWUhc/img/dashboard/api-designer/tyk-oas-no-middleware.png?fit=max&auto=format&n=jzHiRUIhvyphWUhc&q=85&s=eae2532fcb625442cc5382b7e2ee3480" alt="Tyk OAS API Designer showing no middleware enabled on endpoint" width="1237" height="682" data-path="img/dashboard/api-designer/tyk-oas-no-middleware.png" />

2. **Select the Ignore Authentication middleware**

   Select **ADD MIDDLEWARE** and choose the **Ignore Authentication** middleware from the *Add Middleware* screen.

   <img src="https://mintcdn.com/tyk/rz4rHtIOKIA9WnL8/img/dashboard/api-designer/tyk-oas-ignore.png?fit=max&auto=format&n=rz4rHtIOKIA9WnL8&q=85&s=4ca041b8fdf542d4da926ad04b31bfc4" alt="Adding the Ignore Authentication middleware" width="153" height="158" data-path="img/dashboard/api-designer/tyk-oas-ignore.png" />

3. **Optionally configure case-insensitivity**

   If you want to disable case-sensitivity for the path that you wish to skip authentication, then you must select **EDIT** on the Ignore Authentication icon.

   <img src="https://mintcdn.com/tyk/rz4rHtIOKIA9WnL8/img/dashboard/api-designer/tyk-oas-ignore-added.png?fit=max&auto=format&n=rz4rHtIOKIA9WnL8&q=85&s=752618c631d9e8b500f8e9ebe6719a98" alt="Ignore Authentication middleware added to endpoint - click through to edit the config" width="1237" height="440" data-path="img/dashboard/api-designer/tyk-oas-ignore-added.png" />

   This takes you to the middleware configuration screen where you can alter the case sensitivity setting.

   <img src="https://mintcdn.com/tyk/rz4rHtIOKIA9WnL8/img/dashboard/api-designer/tyk-oas-ignore-config.png?fit=max&auto=format&n=rz4rHtIOKIA9WnL8&q=85&s=ce0ab12a6235d9664a7165e7b96e5d67" alt="Configuring case sensitivity for the path for which to ignore authentication" width="1237" height="737" data-path="img/dashboard/api-designer/tyk-oas-ignore-config.png" />

   Select **UPDATE MIDDLEWARE** to apply the change to the middleware configuration.

4. **Save the API**

   Select **SAVE API** to apply the changes to your API.

## Using Classic

<a id="ignore-authentication-using-classic" />

The [Ignore Authentication](/api-management/traffic-transformation/ignore-authentication) middleware instructs Tyk Gateway to skip the authentication step for calls to an endpoint, even if authentication is enabled for the API.

When working with Tyk Classic APIs the middleware is configured in the Tyk Classic API Definition. You can do this via the Tyk Dashboard API or in the API Designer.

If you're using the newer Tyk OAS APIs, then check out the [Tyk OAS](#ignore-authentication-using-tyk-oas) page.

If you're using Tyk Operator then check out the [configuring the middleware in Tyk Operator](#tyk-operator) section below.

### API Definition

To enable the middleware you must add a new `ignored` object to the `extended_paths` section of your API definition.

The `ignored` object has the following configuration:

* `path`: the endpoint path
* `method`: this should be blank
* `ignore_case`: if set to `true` then the path matching will be case insensitive
* `method_actions`: a shared object used to configure the [mock response](/api-management/traffic-transformation/mock-response#when-is-it-useful) middleware

The `method_actions` object should be configured as follows, with an entry created for each allowed method on the path:

* `action`: this should be set to `no_action`
* `code`: this should be set to `200`
* `headers` : this should be blank

For example:

```json {linenos=true, linenostart=1} theme={null}
{
    "extended_paths": {
        "ignored": [
            {
                "disabled": false,
                "path": "/status/200",
                "method": "",
                "ignore_case": false,
                "method_actions": {
                    "GET": {
                        "action": "no_action",
                        "code": 200,
                        "headers": {}
                    }          
                }
            }
        ]
    }
}
```

In this example the ignore authentication middleware has been configured for requests to the `GET /status/200` endpoint. Any such calls will skip the authentication step in the Tyk Gateway's processing chain.

* the middleware has been configured to be case sensitive, so calls to `GET /Status/200` will not skip authentication

### API Designer

You can use the API Designer in the Tyk Dashboard to configure the Ignore Authentication middleware for your Tyk Classic API by following these steps.

1. **Add an endpoint for the path and select the plugin**

   From the **Endpoint Designer** add an endpoint that matches the path for which you want to ignore authentication. Select the **Ignore** plugin.

   <img src="https://mintcdn.com/tyk/KDuaZqa4-E6L5KE7/img/dashboard/endpoint-designer/ignore-authentication.png?fit=max&auto=format&n=KDuaZqa4-E6L5KE7&q=85&s=43039163c1656c51612e0dc474ec3dd6" alt="Adding the ignore authentication middleware to a Tyk Classic API endpoint" width="1237" height="417" data-path="img/dashboard/endpoint-designer/ignore-authentication.png" />

2. **Configure the middleware**

   Once you have selected the Ignore middleware for the endpoint, the only additional feature that you need to configure is whether to make it case-insensitive by selecting **Ignore Case**.

   <img src="https://mintcdn.com/tyk/rcbuH4FawxAvTx_L/img/2.10/ignore.png?fit=max&auto=format&n=rcbuH4FawxAvTx_L&q=85&s=52c5006d90784f09dd7823ce7b5ff73b" alt="Ignore options" width="1264" height="416" data-path="img/2.10/ignore.png" />

3. **Save the API**

   Use the *save* or *create* buttons to save the changes and activate the middleware.

### Tyk Operator

The process for configuring the middleware in Tyk Operator is similar to that explained in configuring the middleware in the Tyk Classic API Definition. It is possible to configure an enforced timeout using the `ignored` object within the `extended_paths` section of the API Definition.

In the example below the ignore authentication middleware has been configured for requests to the `GET /get` endpoint. Any such calls will skip the authentication step in the Tyk Gateway's processing chain.

* the middleware has been configured to be case insensitive, so calls to `GET /Get` will also skip authentication

```yaml {linenos=true, linenostart=1, hl_lines=["27-35"]} theme={null}
apiVersion: tyk.tyk.io/v1alpha1
kind: ApiDefinition
metadata:
  name: httpbin-ignored
spec:
  name: httpbin-ignored
  use_keyless: false
  use_standard_auth: true
  protocol: http
  active: true
  proxy:
    target_url: http://httpbin.org/
    listen_path: /httpbin
    strip_listen_path: true
  version_data:
    default_version: Default
    not_versioned: true
    versions:
      Default:
        name: Default
        use_extended_paths: true
        paths:
          black_list: []
          ignored: []
          white_list: []
        extended_paths:
          ignored:
            - ignore_case: true
              method_actions:
                GET:
                  action: "no_action"
                  code: 200
                  data: ""
                  headers: {}
              path: "/get"
```


Built with [Mintlify](https://mintlify.com).