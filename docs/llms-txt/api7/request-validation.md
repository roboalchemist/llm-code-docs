# Source: https://docs.api7.ai/hub/request-validation.md

# request-validation

The `request-validation` plugin validates requests before forwarding them to upstream services. This plugin uses [JSON Schema](https://github.com/api7/jsonschema) for validation and can validate headers and body of a request.

See [JSON schema specification](https://json-schema.org/specification) to learn more about the syntax.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `request-validation` for different scenarios.

### Validate Request Header[â](#validate-request-header "Direct link to Validate Request Header")

The following example demonstrates how to validate request headers against a defined JSON schema.

Create a route with `request-validation` plugin as follows:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "request-validation-route",
    "uri": "/get",
    "plugins": {
      "request-validation": {
        "header_schema": {
          "type": "object",
          "required": ["User-Agent", "Host"],
          "properties": {
            "User-Agent": {
              "type": "string",
              "pattern": "^curl\/"
            },
            "Host": {
              "type": "string",
              "enum": ["httpbin.org", "httpbin"]
            }
          }
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: request-validation-service
    routes:
      - name: request-validation-route
        uris:
          - /get
        plugins:
          request-validation:
            header_schema:
              type: object
              required:
                - User-Agent
                - Host
              properties:
                User-Agent:
                  type: string
                  pattern: "^curl/"
                Host:
                  type: string
                  enum:
                    - httpbin.org
                    - httpbin
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

request-validation-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: request-validation-plugin-config
spec:
  plugins:
    - name: request-validation
      config:
        header_schema:
          type: object
          required:
            - User-Agent
            - Host
          properties:
            User-Agent:
              type: string
              pattern: "^curl/"
            Host:
              type: string
              enum:
                - httpbin.org
                - httpbin
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /get
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: request-validation-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

request-validation-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  ingressClassName: apisix
  http:
    - name: request-validation-route
      match:
        paths:
          - /get
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: request-validation
        enable: true
        config:
          header_schema:
            type: object
            required:
              - User-Agent
              - Host
            properties:
              User-Agent:
                type: string
                pattern: "^curl/"
              Host:
                type: string
                enum:
                  - httpbin.org
                  - httpbin
```

Apply the configuration to your cluster:

```
kubectl apply -f request-validation-ic.yaml
```

â¶ `required`: require requests to include the specified headers.

â· `properties`: require headers to conform to the specified requirements.

#### Verify with Request Conforming to the Schema[â](#verify-with-request-conforming-to-the-schema "Direct link to Verify with Request Conforming to the Schema")

Send a request with header `Host: httpbin`, which complies with the schema:

```
curl -i "http://127.0.0.1:9080/get" -H "Host: httpbin"
```

You should receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin", 
    "User-Agent": "curl/7.74.0", 
    "X-Amzn-Trace-Id": "Root=1-6509ae35-63d1e0fd3934e3f221a95dd8", 
    "X-Forwarded-Host": "httpbin"
  }, 
  "origin": "127.0.0.1, 183.17.233.107", 
  "url": "http://httpbin/get"
}
```

#### Verify with Request Not Conforming to the Schema[â](#verify-with-request-not-conforming-to-the-schema "Direct link to Verify with Request Not Conforming to the Schema")

Send a request without any header:

```
curl -i "http://127.0.0.1:9080/get"
```

You should receive an `HTTP/1.1 400 Bad Request` response, showing that the request fails to pass validation:

```
property "Host" validation failed: matches none of the enum value
```

Send a request with the required headers but with non-conformant header value:

```
curl -i "http://127.0.0.1:9080/get" -H "Host: httpbin" -H "User-Agent: cli-mock"
```

You should receive an `HTTP/1.1 400 Bad Request` response showing the `User-Agent` header value does not match the expected pattern:

```
property "User-Agent" validation failed: failed to match pattern "^curl/" with "cli-mock"
```

### Customize Rejection Message and Status Code[â](#customize-rejection-message-and-status-code "Direct link to Customize Rejection Message and Status Code")

The following example demonstrates how to customize response status and message when the validation fails.

Configure the route with `request-validation` as follows:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "request-validation-route",
    "uri": "/get",
    "plugins": {
      "request-validation": {
        "header_schema": {
          "type": "object",
          "required": ["Host"],
          "properties": {
            "Host": {
              "type": "string",
              "enum": ["httpbin.org", "httpbin"]
            }
          }
        },
        "rejected_code": 403,
        "rejected_msg": "Request header validation failed."
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: request-validation-service
    routes:
      - name: request-validation-route
        uris:
          - /get
        plugins:
          request-validation:
            header_schema:
              type: object
              required:
                - Host
              properties:
                Host:
                  type: string
                  enum:
                    - httpbin.org
                    - httpbin
            rejected_code: 403
            rejected_msg: "Request header validation failed."
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

request-validation-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: request-validation-plugin-config
spec:
  plugins:
    - name: request-validation
      config:
        header_schema:
          type: object
          required:
            - Host
          properties:
            Host:
              type: string
              enum:
                - httpbin.org
                - httpbin
        rejected_code: 403
        rejected_msg: "Request header validation failed."
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /get
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: request-validation-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

request-validation-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  ingressClassName: apisix
  http:
    - name: request-validation-route
      match:
        paths:
          - /get
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: request-validation
        enable: true
        config:
          header_schema:
            type: object
            required:
              - Host
            properties:
              Host:
                type: string
                enum:
                  - httpbin.org
                  - httpbin
          rejected_code: 403
          rejected_msg: "Request header validation failed."
```

Apply the configuration to your cluster:

```
kubectl apply -f request-validation-ic.yaml
```

â¶ `rejected_code`: customize rejection code.

â· `rejected_msg`: customize rejection message.

Send a request with a misconfigured `Host` in the header:

```
curl -i "http://127.0.0.1:9080/get" -H "Host: httpbin2"
```

You should receive an `HTTP/1.1 403 Forbidden` response with the custom message:

```
Request header validation failed.
```

### Validate Request Body[â](#validate-request-body "Direct link to Validate Request Body")

The following example demonstrates how to validate request body against a defined JSON schema.

The `request-validation` plugin supports validation of two types of media types:

* `application/json`
* `application/x-www-form-urlencoded`

#### Validate JSON Request Body[â](#validate-json-request-body "Direct link to Validate JSON Request Body")

Create a route with `request-validation` plugin as follows:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "request-validation-route",
    "uri": "/post",
    "plugins": {
      "request-validation": {
        "header_schema": {
          "type": "object",
          "required": ["Content-Type"],
          "properties": {
            "Content-Type": {
            "type": "string",
            "pattern": "^application\/json$"
            }
          }
        },
        "body_schema": {
          "type": "object",
          "required": ["required_payload"],
          "properties": {
            "required_payload": {"type": "string"},
            "boolean_payload": {"type": "boolean"},
            "array_payload": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "integer",
                "minimum": 200,
                "maximum": 599
              },
              "uniqueItems": true,
              "default": [200]
            }
          }
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: request-validation-service
    routes:
      - name: request-validation-route
        uris:
          - /post
        plugins:
          request-validation:
            header_schema:
              type: object
              required:
                - Content-Type
              properties:
                Content-Type:
                  type: string
                  pattern: "^application/json$"
            body_schema:
              type: object
              required:
                - required_payload
              properties:
                required_payload:
                  type: string
                boolean_payload:
                  type: boolean
                array_payload:
                  type: array
                  minItems: 1
                  items:
                    type: integer
                    minimum: 200
                    maximum: 599
                  uniqueItems: true
                  default:
                    - 200
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

request-validation-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: request-validation-plugin-config
spec:
  plugins:
    - name: request-validation
      config:
        header_schema:
          type: object
          required:
            - Content-Type
          properties:
            Content-Type:
              type: string
              pattern: "^application/json$"
        body_schema:
          type: object
          required:
            - required_payload
          properties:
            required_payload:
              type: string
            boolean_payload:
              type: boolean
            array_payload:
              type: array
              minItems: 1
              items:
                type: integer
                minimum: 200
                maximum: 599
              uniqueItems: true
              default:
                - 200
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /post
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: request-validation-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

request-validation-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  ingressClassName: apisix
  http:
    - name: request-validation-route
      match:
        paths:
          - /post
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: request-validation
        enable: true
        config:
          header_schema:
            type: object
            required:
              - Content-Type
            properties:
              Content-Type:
                type: string
                pattern: "^application/json$"
          body_schema:
            type: object
            required:
              - required_payload
            properties:
              required_payload:
                type: string
              boolean_payload:
                type: boolean
              array_payload:
                type: array
                minItems: 1
                items:
                  type: integer
                  minimum: 200
                  maximum: 599
                uniqueItems: true
                default:
                  - 200
```

Apply the configuration to your cluster:

```
kubectl apply -f request-validation-ic.yaml
```

Send a request with JSON body that conforms to the schema to verify:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/json" \
  -d '{"required_payload":"hello", "array_payload":[301]}'
```

You should receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {}, 
  "data": "{\"array_payload\":[301],\"required_payload\":\"hello\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    ...
  }, 
  "json": {
    "array_payload": [
      301
    ],
    "required_payload": "hello"
  },
  "origin": "127.0.0.1, 183.17.233.107", 
  "url": "http://127.0.0.1/post"
}
```

If you send a request without specifying `Content-Type: application/json`:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -d '{"required_payload":"hello,world"}'
```

You should receive an `HTTP/1.1 400 Bad Request` response similar to the following:

```
property "Content-Type" validation failed: failed to match pattern "^application/json$" with "application/x-www-form-urlencoded"
```

Similarly, if you send a request without the required JSON field `required_payload`:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/json" \
  -d '{}'
```

You should receive an `HTTP/1.1 400 Bad Request` response:

```
property "required_payload" is required
```

#### Validate URL-Encoded Form Body[â](#validate-url-encoded-form-body "Direct link to Validate URL-Encoded Form Body")

Create a route with `request-validation` plugin as follows:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "request-validation-route",
    "uri": "/post",
    "plugins": {
      "request-validation": {
        "header_schema": {
          "type": "object",
          "required": ["Content-Type"],
          "properties": {
            "Content-Type": {
              "type": "string",
              "pattern": "^application\/x-www-form-urlencoded$"
            }
          }
        },
        "body_schema": {
          "type": "object",
          "required": ["required_payload","enum_payload"],
          "properties": {
            "required_payload": {"type": "string"},
            "enum_payload": {
              "type": "string",
              "enum": ["enum_string_1", "enum_string_2"],
              "default": "enum_string_1"
            }
          }
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: request-validation-service
    routes:
      - name: request-validation-route
        uris:
          - /post
        plugins:
          request-validation:
            header_schema:
              type: object
              required:
                - Content-Type
              properties:
                Content-Type:
                  type: string
                  pattern: "^application/x-www-form-urlencoded$"
            body_schema:
              type: object
              required:
                - required_payload
                - enum_payload
              properties:
                required_payload:
                  type: string
                enum_payload:
                  type: string
                  enum:
                    - enum_string_1
                    - enum_string_2
                  default: enum_string_1
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

request-validation-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: request-validation-plugin-config
spec:
  plugins:
    - name: request-validation
      config:
        header_schema:
          type: object
          required:
            - Content-Type
          properties:
            Content-Type:
              type: string
              pattern: "^application/x-www-form-urlencoded$"
        body_schema:
          type: object
          required:
            - required_payload
            - enum_payload
          properties:
            required_payload:
              type: string
            enum_payload:
              type: string
              enum:
                - enum_string_1
                - enum_string_2
              default: enum_string_1
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /post
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: request-validation-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

request-validation-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: request-validation-route
spec:
  ingressClassName: apisix
  http:
    - name: request-validation-route
      match:
        paths:
          - /post
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: request-validation
        enable: true
        config:
          header_schema:
            type: object
            required:
              - Content-Type
            properties:
              Content-Type:
                type: string
                pattern: "^application/x-www-form-urlencoded$"
          body_schema:
            type: object
            required:
              - required_payload
              - enum_payload
            properties:
              required_payload:
                type: string
              enum_payload:
                type: string
                enum:
                  - enum_string_1
                  - enum_string_2
                default: enum_string_1
```

Apply the configuration to your cluster:

```
kubectl apply -f request-validation-ic.yaml
```

Send a request with URL-encoded form data to verify:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "required_payload=hello&enum_payload=enum_string_1"
```

You should receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "enum_payload": "enum_string_1", 
    "required_payload": "hello"
  }, 
  "headers": {
    ...
  }, 
  "json": null, 
  "origin": "127.0.0.1, 183.17.233.107", 
  "url": "http://127.0.0.1/post"
}
```

Send a request without the URL-encoded field `enum_payload`:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "required_payload=hello"
```

You should receive an `HTTP/1.1 400 Bad Request` of the following:

```
property "enum_payload" is required
```

## Appendix: JSON Schema[â](#appendix-json-schema "Direct link to Appendix: JSON Schema")

The following section provides boilerplate JSON schema for you to adjust, combine, and use with this plugin. For a complete reference, see [JSON schema specification](https://json-schema.org/specification).

### Enumerated Values[â](#enumerated-values "Direct link to Enumerated Values")

```
{
  "body_schema": {
    "type": "object",
    "required": ["enum_payload"],
    "properties": {
      "enum_payload": {
        "type": "string",
        "enum": ["enum_string_1", "enum_string_2"],
        "default": "enum_string_1"
      }
    }
  }
}
```

### Boolean Values[â](#boolean-values "Direct link to Boolean Values")

```
{
  "body_schema": {
    "type": "object",
    "required": ["bool_payload"],
    "properties": {
      "bool_payload": {
        "type": "boolean",
        "default": true
      }
    }
  }
}
```

### Numeric Values[â](#numeric-values "Direct link to Numeric Values")

```
{
  "body_schema": {
    "type": "object",
    "required": ["integer_payload"],
    "properties": {
      "integer_payload": {
        "type": "integer",
        "minimum": 1,
        "maximum": 65535
      }
    }
  }
}
```

### Strings[â](#strings "Direct link to Strings")

```
{
  "body_schema": {
    "type": "object",
    "required": ["string_payload"],
    "properties": {
      "string_payload": {
        "type": "string",
        "minLength": 1,
        "maxLength": 32
      }
    }
  }
}
```

### RegEx for Strings[â](#regex-for-strings "Direct link to RegEx for Strings")

```
{
  "body_schema": {
    "type": "object",
    "required": ["regex_payload"],
    "properties": {
      "regex_payload": {
        "type": "string",
        "minLength": 1,
        "maxLength": 32,
        "pattern": "[[^[a-zA-Z0-9_]+$]]"
      }
    }
  }
}
```

### Arrays[â](#arrays "Direct link to Arrays")

```
{
  "body_schema": {
    "type": "object",
    "required": ["array_payload"],
    "properties": {
      "array_payload": {
        "type": "array",
        "minItems": 1,
        "items": {
          "type": "integer",
          "minimum": 200,
          "maximum": 599
        },
        "uniqueItems": true,
        "default": [200, 302]
      }
    }
  }
}
```
