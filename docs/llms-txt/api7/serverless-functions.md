# Source: https://docs.api7.ai/hub/serverless-functions.md

# Serverless Functions

The serverless functions consist of two plugins, `serverless-pre-function` and `serverless-post-function`. These plugins enable the execution of user-defined logic at the beginning and end of the [execution phases](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle) the functions hook to.

## Tips for Writing Functions[â](#tips-for-writing-functions "Direct link to Tips for Writing Functions")

Only Lua functions are allowed in the serverless plugins and not other Lua code.

For example, anonymous functions are legal:

```
return function()
    ngx.log(ngx.ERR, 'one')
end
```

Closures are also legal:

```
local count = 1
return function()
    count = count + 1
    ngx.say(count)
end
```

But code other than functions are illegal:

```
local count = 1
ngx.say(count)
```

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure the `serverless-pre-function` and `serverless-post-function` plugins for different scenarios.

### Log Information before and after a Phase[â](#log-information-before-and-after-a-phase "Direct link to Log Information before and after a Phase")

The example below demonstrates how you can configure the serverless plugins to execute custom logics to log information to error logs before and after the `rewrite` [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle).

Create a route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "id": "serverless-pre-route",
    "uri": "/anything",
    "plugins": {
      "serverless-pre-function": {
        "phase": "rewrite",
        "functions" : [
          "return function()
            ngx.log(ngx.ERR, \"serverless pre function\");
          end"
        ]
      },
      "serverless-post-function": {
        "phase": "rewrite",
        "functions" : [
          "return function(conf, ctx)
            ngx.log(ngx.ERR, \"match uri \", ctx.curr_req_matched and ctx.curr_req_matched._path);
          end"
        ]
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

â¶ Hook the serverless pre-function logic to the `rewrite` [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle).

â· Define a Lua function that logs a message of `serverless pre function` in the error log.

â¸ Hook the serverless post-function logic to the `rewrite` [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle).

â¹ Define a Lua function that logs the matched URI in the error log. `conf` and `ctx` can be passed as the first two arguments like other plugins, where `conf` is the plugin configurations and `ctx` is the request context.

Send the request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response and see the following entries in the error log:

```
2024/05/09 15:07:09 [error] 51#51: *3963 [lua] [string "return function() ngx.log(ngx.ERR, "serverles..."]:1: func(): serverless pre function, client: 172.21.0.1, server: _, request: "GET /test HTTP/1.1", host: "127.0.0.1:9080"
2024/05/09 15:16:58 [error] 50#50: *9343 [lua] [string "return function(conf, ctx) ngx.log(ngx.ERR, "..."]:1: func(): match uri /test, client: 172.21.0.1, server: _, request: "GET /test HTTP/1.1", host: "127.0.0.1:9080"
```

The first entry is added by the pre-function and the second entry is added by the post-function.

### Register Custom Variables[â](#register-custom-variables "Direct link to Register Custom Variables")

The example below demonstrates how you can register [custom built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) using the serverless plugins and use the newly created variable in logs.

Start an example rsyslog server in Docker:

```
docker run -d -p 514:514 --name example-rsyslog-server rsyslog/syslog_appliance_alpine
```

Create a [service](https://docs.api7.ai/apisix/key-concepts/services.md) with a serverless function to register a custom variable `a6_route_labels`, enable a logging plugin to later log the custom variable, and configure an upstream:

```
curl "http://127.0.0.1:9180/apisix/admin/services" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "id":"srv_custom_var",
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
      },
      "syslog": {
        "host" : "172.0.0.1",
        "port" : 514,
        "flush_limit" : 1
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ `functions`: register a custom variable `a6_route_labels` and fetch the variable value from the matched route's `labels` property.

â· `host` and `port`: replace with the address of your syslog server.

â¸ `flush_limit`: set to 1 to push log to the syslog server immediately.

Next, update the log format for all `syslog` instances with the new variable by configuring the [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md):

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/syslog" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "log_format": {
      "host": "$host",
      "client_ip": "$remote_addr",
      "labels": "$a6_route_labels"
    }
  }'
```

â¶ `$host` and `$remote_addr`: [NGINX variables](#nginx-variables).

â· `$a6_route_labels`: custom variable.

Finally, create a route in the service:

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

â¶ `service_id`: correspond to the previously created service.

â· `labels`: route information to be logged with the custom variable.

To verify the variable registration, send a request to the route:

```
curl "http://127.0.0.1:9080/get"
```

You should see a log entry in your syslog server similar to the following:

```
{
  "host":"127.0.0.1",
  "route_id":"route_custom_var",
  "client_ip":"172.19.0.1",
  "labels":{
    "key":"test_a6_route_labels"
  },
  "service_id":"srv_custom_var"
}
```

This verifies the custom variable was registered and it logs the `labels` information in a route successfully.

### Modify a Specific Field in Response Body[â](#modify-a-specific-field-in-response-body "Direct link to Modify a Specific Field in Response Body")

The example below demonstrates how you can use the serverless plugins to remove a specific field from a JSON response body.

Before proceeding with the removal, first configure a route as follows to see the unmodified response:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "id":"serverless-remove-body-info",
    "uri": "/get",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/get"
```

You should see a response similar to the following with your host and proxy's IP information:

```
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "127.0.0.1", 
    "User-Agent": "curl/8.4.0", 
    "X-Amzn-Trace-Id": "Root=1-663db30f-51448a1b635f2f4338a4fcfc", 
    "X-Forwarded-Host": "127.0.0.1"
  },
  "origin": "172.19.0.1, 123.456.122.90", 
  "url": "http://127.0.0.1/get"
}
```

To remove the `origin` field from the response, update the route with serverless plugins:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/serverless-remove-body-info" -X PATCH \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "plugins": {
      "serverless-pre-function": {
        "phase": "header_filter",
        "functions" : [
          "return function(conf, ctx)
            local core = require(\"apisix.core\")
            core.response.clear_header_as_body_modified()
          end"
        ]
      },
      "serverless-post-function": {
        "phase": "body_filter",
        "functions" : [
          "return function(conf, ctx)
            local cjson = require(\"cjson\")
            local core = require(\"apisix.core\")
            local body = core.response.hold_body_chunk(ctx)
            if not body then
              return
            end
            body = cjson.decode(body)
            body.origin = nil
            body = cjson.encode(body)
            ngx.arg[1] = body
          end"
        ]
      }
    }
  }'
```

â¶ Execute a pre-function in the `header_filter` [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle).

â· Use `clear_header_as_body_modified` method to clear body-related response headers such as `Content-Length` to help with response modification.

â¸ Execute a post-function in the `body_filter` [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle).

â¹ Use `hold_body_chunk` method to collect the response body.

âº Decode the JSON response body.

â» Set the `origin` field to `nil` to remove the field.

Send another request to the route:

```
curl "http://127.0.0.1:9080/get"
```

You should see a response without the `origin` information:

```
{
  "url":"http://127.0.0.1/get",
  "args":{},
  "headers":{
    "X-Forwarded-Host":"127.0.0.1",
    "Host":"127.0.0.1",
    "Accept":"*/*",
    "User-Agent":"curl/8.4.0",
    "X-Amzn-Trace-Id":"Root=1-663db276-1c15276864294d963c6e1755"
  }
}
```

For simpler response modifications, such as modifying HTTP status codes, request headers, or the entire response body, please use the [`response-rewrite`](https://docs.api7.ai/hub/response-rewrite.md) plugin.
