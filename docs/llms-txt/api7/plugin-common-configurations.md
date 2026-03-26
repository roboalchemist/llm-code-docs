# Source: https://docs.api7.ai/apisix/reference/plugin-common-configurations.md

# Plugin Common Configurations

Plugin common configurations are a set of configuration options that can be applied universally to all APISIX plugins through the `_meta` attribute. They can be used to configure:

* [Plugin conditional execution](#_metafilter)
* [Plugin execution priorities](#_metapriority)
* [Plugin disablement](#_metadisable)
* [Plugin error response](#_metaerror_response)
* [Custom code execution before each plugin phase](#_metapre_function) (Enterprise feature)

## `_meta.filter`[â](#_metafilter "Direct link to _metafilter")

You can use `_meta.filter` to configure the conditional execution of plugins based on request parameters. Conditions are created with [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md) and configured as an array. A plugin only executes when all conditions are met.

For example, the following configuration sets a condition on the request's URI [query parameter](https://en.wikipedia.org/wiki/Query_string). Only requests with the URI query parameter `version` being `v2` will trigger the execution of the `proxy-rewrite` plugin, which rewrites the request's URI path to `/api/v2` before forwarding it to the upstream:

```
{
  ...,
  "plugins": {
    "proxy-rewrite": {
      "uri": "/api/v2",
      "_meta": {
        "filter": [
          ["arg_version", "==", "v2"]
        ]
      }
    }
  }
}
```

Requests not meeting the condition will not have their URI paths rewritten and will be forwarded as-is.

## `_meta.priority`[â](#_metapriority "Direct link to _metapriority")

You can use `_meta.priority` to adjust the execution order of **plugins of the same type** (i.e. global or non-global) **within a given phase**. Once defined, the value will take precedence over the default plugin priority defined in the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample).

Suppose two plugins that run in the same [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle), `limit-count` and `ip-restriction`, are configured on the same route. `limit-count` has a default priority of 1002 and `ip-restriction` has a default priority of 3000. When a request is sent to the route, `ip-restriction` is executed first as it has a higher default priority value. However, you can run `limit-count` before `ip-restriction` by assigning `_meta.priority` of `limit-count` a priority value higher than 3000, such as:

```
{
  ...,
  "plugins": {
    "limit-count": {
      ...,
      "_meta": {
        "priority": 3010
      }
    }
  }
}
```

To learn more about the execution order when global and non-global plugins are used together, see [plugin execution order](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-order).

## `_meta.disable`[â](#_metadisable "Direct link to _metadisable")

You can use `_meta.disable` to disable a plugin without removing the plugin from the object it is bound to entirely.

For example, you can disable the `proxy-rewrite` plugin with the following:

```
{
  "plugins": {
    "proxy-rewrite": {
      "_meta": {
        "disable": true
      }
    }
  }
}
```

## `_meta.error_response`[â](#_metaerror_response "Direct link to _metaerror_response")

You can use `_meta.error_response` to customize the error response returned by a plugin to a fixed value. This could be used to mitigate complications that may arise from the default error response in some cases.

For example, you can customize the error response of the `limit-count` plugin:

```
{
  "plugins": {
    "limit-count": {
      "count": 1,
      "time_window": 60,
      "_meta": {
        "error_response": {
          "message": "You have exceeded the rate limiting threshold."
        }
      }
    }
  }
}
```

If more than one request is sent within the 60-second window to the route that the plugin binds to, you should see the following response:

```
{"message":"You have exceeded the rate limiting threshold."}
```

## `_meta.pre_function`[â](#_metapre_function "Direct link to _metapre_function")

You can use `_meta.pre_function` to configure the custom code execution prior to each [phase](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle) of plugin execution.

The following example will show you how to declare a `_meta.pre_function` in the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin to extract the `user_id` in the request path, register it as a variable, and use it to compose the new request path.

In order to use parameters in the route's URI, you should first update the router in the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) to be `radixtree_uri_with_parameter` as it is not the default setting:

config.yaml

```
apisix:
  router:
    http: radixtree_uri_with_parameter
```

Then [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for the changes to take effect.

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

## Differentiate from Plugin Metadata[â](#differentiate-from-plugin-metadata "Direct link to Differentiate from Plugin Metadata")

When working with plugins, it is important to understand the distinctions between the `_meta` common configurations, as outlined in this document, and the [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md). These two concepts serve different purposes and should not be mixed.

While the `_meta` common configurations refer to configuration options that are available for all APISIX plugins, plugin metadata only applies to plugins that have metadata attributes. These metadata attributes could also be configured with the Admin API plugin metadata resource.

See [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) to learn more.
