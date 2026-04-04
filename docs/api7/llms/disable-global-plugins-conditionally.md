# Source: https://docs.api7.ai/enterprise/best-practices/disable-global-plugins-conditionally.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/disable-global-plugins-conditionally.md

# Conditionally Disable Global Plugins

Global plugins apply to all routes by default, which is useful for enforcing organization-wide policies such as authentication, logging, or monitoring. However, in some cases you may want to disable certain global plugins for specific routes or services to meet business or technical requirements.

This guide will walk you through how to fine-tune global plugin execution so that plugins run where they are needed while being skipped where they are not. You will enable `multi-auth` globally and disable the execution of the plugin on the selected route.

note

API7 Ingress Controller does not currently support configuring route labels, which is required to complete this guide.

## Use RegEx Match in Condition[â](#use-regex-match-in-condition "Direct link to Use RegEx Match in Condition")

In this section, you will be using RegEx matching to conditionally skip global plugin execution based on route labels.

caution

Complex RegEx expressions may incur more processing overhead compared to [list-based match](#use-list-based-match-in-condition).

### Create a Serverless Function[â](#create-a-serverless-function "Direct link to Create a Serverless Function")

Create a serverless function that registers the variable `api7_disable_global_rules` when a route includes this label. The variableâs value will later be used to determine whether a global plugin should be disabled.

1. Navigate to your gateway group.

2. In the left menu bar, click on **Plugin Settings** and add a new plugin.

3. Add the `serverless-pre-function` plugin.

4. Apply the following configuration:

   ```
   functions:
     - |-
       return function(conf, ctx)
           local core = require "apisix.core"
           core.ctx.register_var("api7_disable_global_rules", function(ctx)
               local route = ctx.matched_route and ctx.matched_route.value
               if route and route.labels then
                   return route.labels.api7_disable_global_rules
               end
               return 1
           end)
       end
   phase: rewrite
   ```

### Configure a Global Plugin[â](#configure-a-global-plugin "Direct link to Configure a Global Plugin")

Configure a sample global plugin with `_meta.filter` using a RegEx match to conditionally determine whether it should be executed. If the value of `api7_disable_global_rules` matches the plugin name, the global plugin will be skipped.

1. Navigate to your gateway group.

2. In the left menu bar, click on **Plugin Settings** and add a new plugin.

3. Add the `multi-auth` plugin.

4. Apply the following configuration:

   ```
   {
       "_meta": {
         "filter": [
           [
             "api7_disable_global_rules",
             "!",
             "~~",
             ".*multi-auth.*"
           ]
         ]
       },
       "auth_plugins": [
         {
           "basic-auth": {}
         },
         {
           "key-auth": {
             "header": "apikey",
             "hide_credentials": true,
             "query": "apikey"
           }
         }
       ]
     }
   ```

The global plugin will skip execution on resources whose `api7_disable_global_rules` label contains `multi-auth`.

### Configure a Route[â](#configure-a-route "Direct link to Configure a Route")

1. Follow the [getting started tutorial](https://docs.api7.ai/enterprise/3.8.x/getting-started/launch-your-first-api.md#create-service-and-route) to create a service. In the service, create two routes: `/ip` and `/get`.
2. Configure a label `api7_disable_global_rules` with the value `multi-auth` on the `/get` route.

### Create a Consumer[â](#create-a-consumer "Direct link to Create a Consumer")

1. Follow [Manage Consumer Credentials](https://docs.api7.ai/enterprise/3.8.x/api-consumption/manage-consumer-credentials.md) to create two consumers: `consumer1` and `consumer2`.
2. Configure the basic authentication credential for `consumer1`, using `consumer1` as the username and `consumer1_pwd` as the password.
3. Configure the key authentication credential for `consumer2`, using `consumer2_pwd` as the key.

### Verify[â](#verify "Direct link to Verify")

Send a request to the `/get` route without any credentials:

```
curl -i "http://127.0.0.1:9080/get"
```

You should receive an `HTTP/1.1 200 OK` response, since `multi-auth` is disabled for the route.

Send a request to the `/ip` route without any credentials:

```
curl -i "http://127.0.0.1:9080/ip"
```

You should receive an `HTTP/1.1 401 Unauthorized` response, since `multi-auth` is active for the route.

Send two requests to the `/ip` route, one using basic authentication and the other one using key authentication:

```
curl -i "http://127.0.0.1:9080/anything" -u 'consumer1:consumer1_pwd'
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: consumer2_pwd'
```

You should receive `HTTP/1.1 200 OK` responses for both requests, as the credentials are valid.

## Use List-Based Match in Condition[â](#use-list-based-match-in-condition "Direct link to Use List-Based Match in Condition")

In this section, you will be using list-based matching to conditionally skip global plugin execution based on route labels.

### Create a Serverless Function[â](#create-a-serverless-function-1 "Direct link to Create a Serverless Function")

Create a serverless function that registers the variable `api7_disable_global_rules` when a route includes this label. The label can contain one or more comma-separated plugin names, which will be split and trimmed to form a list. This list will later be used to determine which global plugins should be disabled.

1. Navigate to your gateway group.

2. In the left menu bar, click on **Plugin Settings** and add a new plugin.

3. Add the `serverless-pre-function` plugin.

4. Apply the following configuration:

   ```
   functions:
     - >-
       return function(conf, ctx)
           local core = require "apisix.core"
           core.ctx.register_var("api7_disable_global_rules", function(ctx)
               local route = ctx.matched_route and ctx.matched_route.value
               if route and route.labels then
                   local value = route.labels.api7_disable_global_rules
                   if value then
                       local disable_plugins = {}
                       for plugin_name in string.gmatch(value, "[^,]+") do
                           local trimmed_name = string.gsub(plugin_name, "^%s*(.-)%s*$", "%1")
                           if trimmed_name and trimmed_name ~= "" then
                               table.insert(disable_plugins, trimmed_name)
                           end
                       end
                       core.log.error("disable_plugins: ", core.json.encode(disable_plugins))
                       return disable_plugins
                   end

               end
               return 1
           end)
       end
   phase: rewrite
   ```

### Configure a Global Plugin[â](#configure-a-global-plugin-1 "Direct link to Configure a Global Plugin")

Configure a sample global plugin with `_meta.filter` using a list-based match to conditionally determine whether it should be executed. If the `api7_disable_global_rules` variable contains the plugin name, the global plugin will be skipped.

1. Navigate to your gateway group.

2. In the left menu bar, click on **Plugin Settings** and add a new plugin.

3. Add the `multi-auth` plugin.

4. Apply the following configuration:

   ```
   {
     "_meta": {
       "disable": false,
       "filter": [
         [
           "api7_disable_global_rules",
           "!",
           "has",
           "multi-auth"
         ]
       ]
     },
     "auth_plugins": [
       {
         "basic-auth": {}
       },
       {
         "key-auth": {
           "header": "apikey",
           "hide_credentials": true,
           "query": "apikey"
         }
       }
     ]
   }
   ```

The global plugin will skip execution on resources whose `api7_disable_global_rules` label includes `multi-auth` in its list of disabled plugins.

### Configure a Route[â](#configure-a-route-1 "Direct link to Configure a Route")

1. Follow the [getting started tutorial](https://docs.api7.ai/enterprise/3.8.x/getting-started/launch-your-first-api.md#create-service-and-route) to create a service. In the service, create two routes: `/ip` and `/get`.
2. Configure a label `api7_disable_global_rules` with the value `multi-auth, cors, limit-count` on the `/get` route.

### Create a Consumer[â](#create-a-consumer-1 "Direct link to Create a Consumer")

1. Follow [Manage Consumer Credentials](https://docs.api7.ai/enterprise/3.8.x/api-consumption/manage-consumer-credentials.md) to create two consumers: `consumer1` and `consumer2`.
2. Configure the basic authentication credential for `consumer1`, using `consumer1` as the username and `consumer1_pwd` as the password.
3. Configure the key authentication credential for `consumer2`, using `consumer2_pwd` as the key.

### Verify[â](#verify-1 "Direct link to Verify")

Send a request to the `/get` route without any credentials:

```
curl -i "http://127.0.0.1:9080/get"
```

You should receive an `HTTP/1.1 200 OK` response, since `multi-auth` is disabled for the route.

Send a request to the `/ip` route without any credentials:

```
curl -i "http://127.0.0.1:9080/ip"
```

You should receive an `HTTP/1.1 401 Unauthorized` response, since `multi-auth` is active for the route.

Send two requests to the `/ip` route, one using basic authentication and the other one using key authentication:

```
curl -i "http://127.0.0.1:9080/anything" -u 'consumer1:consumer1_pwd'
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: consumer2_pwd'
```

You should receive `HTTP/1.1 200 OK` responses for both requests, as the credentials are valid.
