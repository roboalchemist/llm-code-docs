# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/apisix/reference/built-in-variables.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/built-in-variables.md

# Source: https://docs.api7.ai/apisix/reference/built-in-variables.md

# Built-In Variables

*Built-in variables* in APISIX are pre-defined variables that can be directly referenced in configurations. They are often used in plugin configurations, route matching, and log customization.

APISIX supports three types of built-in variables:

* NGINX Variables
* APISIX Variables
* Custom Variables

These variables are evaluated in [a given order](#evaluation-order).

## NGINX Variables[â](#nginx-variables "Direct link to NGINX Variables")

NGINX provides a set of variables that can be used to access various request-specific information.

Some of the commonly used variables include:

* `upstream_addr`
* `remote_addr`
* `request_uri`
* `server_name`
* `uri`
* `http_user_agent`

See the [complete list of NGINX variables](https://nginx.org/en/docs/varindex.html) for more information.

## APISIX Variables[â](#apisix-variables "Direct link to APISIX Variables")

In addition to [NGINX variables](https://nginx.org/en/docs/varindex.html), APISIX offers a variety of built-in variables:

| Variable Name         | Description                                                                                                                                                                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `post_arg_*`          | HTTP POST form data when the content type is `application/x-www-form-urlencoded`. The asterisk is to be replaced with the actual name of the POST form data.                                                                                                                                                                    |
| `post_arg.*`          | HTTP POST body parameter when the content type is `application/json`, `application/x-www-form-urlencoded`, or `multipart/form-data`. The asterisk is to be replaced with the actual name of the POST parameter. Supports JSON path-like selection, such as `post_arg.model.version` and `post_arg.messages[*].content[*].type`. |
| `arg_*`               | URL query string. The asterisk is to be replaced with the actual query parameter name.                                                                                                                                                                                                                                          |
| `uri_param_*`         | URL parameter when APISIX uses the `radixtree_uri_with_parameter` [router](https://docs.api7.ai/apisix/reference/router-options.md#radixtree_uri_with_parameter). The asterisk is to be replaced with the actual query parameter name.                                                                                          |
| `http_*`              | HTTP request header. The asterisk is to be replaced with the actual name of the header.                                                                                                                                                                                                                                         |
| `cookie_*`            | Request cookie. The asterisk is to be replaced with the actual name of the cookie.                                                                                                                                                                                                                                              |
| `balancer_ip`         | Upstream server IP.                                                                                                                                                                                                                                                                                                             |
| `balancer_port`       | Upstream server port.                                                                                                                                                                                                                                                                                                           |
| `consumer_name`       | Consumer username.                                                                                                                                                                                                                                                                                                              |
| `consumer_group_id`   | Consumer group ID.                                                                                                                                                                                                                                                                                                              |
| `graphql_name`        | GraphQL [operation name](https://graphql.org/learn/queries/#operation-name).                                                                                                                                                                                                                                                    |
| `graphql_operation`   | GraphQL [operation type](https://graphql.org/learn/queries/#operation-name).                                                                                                                                                                                                                                                    |
| `graphql_root_fields` | GraphQL [root fields](https://graphql.org/learn/execution/#root-fields-resolvers).                                                                                                                                                                                                                                              |
| `route_id`            | Route ID.                                                                                                                                                                                                                                                                                                                       |
| `route_name`          | Route name.                                                                                                                                                                                                                                                                                                                     |
| `service_id`          | Service ID.                                                                                                                                                                                                                                                                                                                     |
| `service_name`        | Service name.                                                                                                                                                                                                                                                                                                                   |
| `resp_body`           | HTTP response body.                                                                                                                                                                                                                                                                                                             |
| `mqtt_client_id`      | Client ID in MQTT protocol.                                                                                                                                                                                                                                                                                                     |
| `redis_cmd_line`      | Redis command.                                                                                                                                                                                                                                                                                                                  |
| `rpc_time`            | RPC request round-trip time.                                                                                                                                                                                                                                                                                                    |

## Custom Variables[â](#custom-variables "Direct link to Custom Variables")

You can also register your own variables and use them as built-in variables. For instance, you can use custom variables to customize log format in logging plugins, or use them as keys in rate limiting plugins.

### Example[â](#example "Direct link to Example")

The following example demonstrates two approaches for custom variable registration and how you can leverage the variable to obtain information from a route, subsequently logging the information to a remote server.

#### Create a Service[â](#create-a-service "Direct link to Create a Service")

Create a service to configure `http-logger` plugin and upstream:

```
curl "http://127.0.0.1:9180/apisix/admin/services" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "id":"srv_custom_var",
    "plugins": {
      "http-logger": {
        "uri": "'"${REMOTE_SERVER_ADDR}"'"
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

#### Register a Custom Variable[â](#register-a-custom-variable "Direct link to Register a Custom Variable")

You can choose to register the custom variable in the source code or use the `serverless` plugins.

##### Method 1: In the Source Code[â](#method-1-in-the-source-code "Direct link to Method 1: In the Source Code")

Add the following snippet to your custom Lua file and source it to register a custom variable named `a6_route_labels`. The variable represents the value of `labels` in a request to a route, if available:

```
local core = require "apisix.core"

core.ctx.register_var("a6_route_labels", function(ctx)
  local route = ctx.matched_route and ctx.matched_route.value
  if route and route.labels then
    return route.labels
  end
  return nil
end)
```

[Start or reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md) accordingly. If APISIX is already running, send a PUT request to `/apisix/admin/plugins/reload` to [hot reload the plugins](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Plugin/paths/~1apisix~1admin~1plugins~1reload/put) for changes to take effect.

caution

While the snippet can technically be added anywhere the code is sourced, exercise caution when modifying the APISIX core codebase to avoid any negative impact on the standard functionalities.

It is recommended to keep your custom Lua code in a separate directory and source it by configuring `extra_lua_path` and `extra_lua_cpath` in the `config.yaml` [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md).

For more information, see [create Lua plugin guide](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md).

##### Method 2: In the `serverless` Plugins[â](#method-2-in-the-serverless-plugins "Direct link to method-2-in-the-serverless-plugins")

You can also register a custom variable using the `serverless-pre-function` or `serverless-post-function` [serverless function plugins](https://docs.api7.ai/hub/serverless-functions.md). These plugins run serverless functions before or after a specified [execution phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle), and you can register custom variables in these functions.

Add the `serverless-pre-function` plugin to the previously created service, where the function registers the custom variable `a6_route_labels`:

```
curl "http://127.0.0.1:9180/apisix/admin/services/srv_custom_var" -X PATCH \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "plugins": {
      "serverless-pre-function": {
        "phase": "rewrite",
        "functions": [
          "return function()
            local core = require \"apisix.core\"
            core.ctx.register_var(\"a6_route_labels\", function(ctx)
              local route = ctx.matched_route and ctx.matched_route.value
              if route and route.labels then
                return route.labels
              end
              return nil
            end); 
          end"
        ]
      }
    }
  }'
```

##### Method 3: In `_meta.prefunction` of Plugins[â](#method-3-in-_metaprefunction-of-plugins "Direct link to method-3-in-_metaprefunction-of-plugins")

If you prefer to register the custom variable in the plugin without using the serverless plugin, you can use `_meta.pre_function` to configure the custom code execution prior to each [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle) of plugin execution.

The following example will show you how to declare a `_meta.pre_function` in the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin to extract the `user_id` in the request path, register it as a variable, and use it to compose the new request path.

In order to use parameters in the route's URI, you should first update the router in the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) to be `radixtree_uri_with_parameter` as it is not the default setting:

config.yaml

```
apisix:
  router:
    http: radixtree_uri_with_parameter
```

Then [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

Create a route to the httpbin service to examine the rewritten path:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
-H "X-API-KEY: ${ADMIN_API_KEY}" \
-d '{
  "id": "pre-func-route",
  "uri": "/anything/:user_id/hello",
  "plugins": {
    "proxy-rewrite": {
      "_meta": {
        "pre_function": "
          return function(conf, ctx)
            local core = require \"apisix.core\"
            core.ctx.register_var(\"user_id\", function(ctx) return ctx.curr_req_matched.user_id end)
          end"
      },
      "uri": "/anything/$user_id/world"
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

â¶ Match requests to `/anything/:user_id/hello` where `user_id` is a parameter.

â· Customize the `_meta.pre_function` to extract the `user_id` value from the requested path and save it to a variable of the same name.

â¸ Rewrite the request path to `/anything/$user_id/world`, where `$user_id` will be replaced by the variable value.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything/johndoe/hello"
```

You should observe the following response, showing the request path has been rewritten partially with the `user_id`:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "text/html..."
    ...
  },
  "json": null,
  "method": "GET",
  "origin": "127.0.0.1, 59.71.xxx.xxx",
  "url": "http://127.0.0.1/anything/johndoe/world"
}
```

#### Configure Log Format[â](#configure-log-format "Direct link to Configure Log Format")

Create a [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) object to configure log format for all `http-logger` instances:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/http-logger" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "log_format": {
      "host": "$host",
      "client_ip": "$remote_addr",
      "labels": "$a6_route_labels"
    }
  }'
```

â¶ `host` and `remote_addr`: [NGINX variables](#nginx-variables).

â· `a6_route_labels`: custom variable.

#### Create a Route in Service[â](#create-a-route-in-service "Direct link to Create a Route in Service")

Create a [route](https://docs.api7.ai/apisix/key-concepts/routes.md) in the service:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "id":"route_custom_var",
    "uri":"/get",
    "service_id": "srv_custom_var",
    "labels": {
      "key": "test_a6_route_labels"
    }
}'
```

â¶ `service_id`: corresponds to the previously created service.

â· `labels`: route information to be logged with the custom variable.

#### Verify Custom Variable Registration[â](#verify-custom-variable-registration "Direct link to Verify Custom Variable Registration")

Send a request to verify that the custom variable logs the `labels` information in the route:

```
curl "http://127.0.0.1:9080/get"
```

You should see a log entry in your remote server created by a POST request with a body similar to the following:

```
[
  {
    "labels": {
      "key": "test_a6_route_labels"
    },
    "service_id": "srv_custom_var",
    "client_ip": "172.21.0.1",
    "route_id": "route_custom_var",
    "host": "127.0.0.1"
  }
]
```

This verifies the custom variable was registered and it logs the `labels` information in a route successfully.

## Evaluation Order[â](#evaluation-order "Direct link to Evaluation Order")

APISIX evaluates variables in the given order:

1. Custom Variables
2. APISIX Variables
3. NGINX Variables

If a variable is successfully sourced in custom variables, APISIX will not continue to look in APISIX variables or NGINX variables.

In other words, custom variables will **overwrite variables of the same names** defined in APISIX variables or NGINX variables, to better meet requirements of your specific use cases.
