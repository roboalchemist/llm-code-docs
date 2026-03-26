# Source: https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md

# Create a Custom Plugin in Lua

One of the key features of APISIX is its extensibility through [plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md). In addition to a wide range of existing plugins, APISIX also allows you to build custom plugins to add extra functionalities and manage API traffic with custom flow. Oftentimes, you use [Lua](https://www.lua.org/) programming language to implement new plugins. APISIX processes requests in [phases](https://github.com/openresty/lua-nginx-module/blob/master/README.markdown#directives) and the relevant plugin logics get executed in each phase during the routing of requests.

This guide walks you through the example process of developing a new custom plugin in Lua for APISIX.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* InstallÂ [Docker](https://docs.docker.com/get-docker/).
* InstallÂ [cURL](https://curl.se/)Â to send requests to the services for validation.
* Follow theÂ [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md)Â to start a new APISIX instance in Docker or on Kubernetes.

## Develop File Proxy Plugin[â](#develop-file-proxy-plugin "Direct link to Develop File Proxy Plugin")

In this section, you will create a new custom plugin called **file-proxy** for APISIX using Lua. This plugin will be used to expose the static files (YAML, JSON, JavaScript, CSS, or image files) through API and fetch a file from a specified URL. For example, API users can access `openapi.yaml` file at the specified URL `http://127.0.0.1:9080/openapi.yaml`.

### Create a Lua File[â](#create-a-lua-file "Direct link to Create a Lua File")

Create a new Lua file for the plugin source code named `file-proxy.lua`.

### Import Modules[â](#import-modules "Direct link to Import Modules")

Import the necessary modules for the `file-proxy` plugin:

```
local core = require("apisix.core")
local io = require("io")
local ngx = ngx
```

### Define Plugin Name[â](#define-plugin-name "Direct link to Define Plugin Name")

Declare a unique name for the plugin:

```
local plugin_name = "file-proxy"
```

### Define Plugin Schema[â](#define-plugin-schema "Direct link to Define Plugin Schema")

Create a schema for plugin parameters. The schema defines the available parameters as well as their data types, properties, default values, valid values, and so on.

The `file-proxy` plugin requires to have a *file path* parameter, such that APISIX knows where to read the file from before returning its content in the response.

```
local plugin_schema = {
    type = "object",
    properties = {
        path = {
            type = "string"
        },
    },
    required = {"path"}
}
```

â¶ The path of the file to be served.

â· The path set be a required parameter.

### Define Lua Module Table[â](#define-lua-module-table "Direct link to Define Lua Module Table")

Define properties `version`, `priority`, `name`, and `schema` for the plugin. The `name` and `schema` are the plugin's name and schema defined previously. The `version` and `priority` are used by APISIX to manage the plugin.

```
local _M = {
    version = 1.0,
    priority = 1000,
    name = plugin_name,
    schema = plugin_schema
}
```

â¶ `version`: The field typically refers to the version that is currently in use. If you publish and update your plugin logic, it is going to be `1.1` (You can set any version you wish).

â· `priority`: The field is used to sort plugins before executing each of their phases. Plugins with a higher priority are executed first. Make sure the priority for the custom plugin fit into that of existing plugins. The priorities of existing plugins are documented in the [`config.yaml.example`](https://github.com/apache/apisix/blob/master/conf/config.yaml.example#L438) file.

â¸ `name`: The plugin's name.

â¹ `schema`: The plugin's schema.

### Define Schema Check Function[â](#define-schema-check-function "Direct link to Define Schema Check Function")

Define a schema checker to validate the user-input parameters against the defined schema:

```
function _M.check_schema(conf)
  local ok, err = core.schema.check(plugin_schema, conf)
  if not ok then
      return false, err
  end
  return true
end
```

### Define Custom Logic[â](#define-custom-logic "Direct link to Define Custom Logic")

APISIX allows you to inject custom logic in various [phases](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle). See [Lua NGINX Module Directives](https://openresty-reference.readthedocs.io/en/latest/Directives/) to learn more about different phases.

Implement custom logic for the `file-proxy` plugin in the `access` function, which would be executed during the access phase. The logic should open the file specified in the plugin configuration, read its content, and return the content as the response. If the file cannot be opened, it should log an error and return a `404 Not Found`.

```
function _M.access(conf, ctx)
  local fd = io.open(conf.path, "rb")
  if fd then
    local content = fd:read("*all")
    fd:close()
    ngx.header.content_length = #content
    ngx.say(content)
    ngx.exit(ngx.OK)
  else
    ngx.exit(ngx.HTTP_NOT_FOUND)
    core.log.error("File is not found: ", conf.path, ", error info: ", err)
  end
end
```

### Define Logging Logic[â](#define-logging-logic "Direct link to Define Logging Logic")

The `log` function is executed during the log phase. Logging is optional but helpful for debugging and checking if the plugin is working properly.

Implement a logging logic to log the plugin configuration, request to the plugin, and response:

```
function _M.log(conf, ctx)
    core.log.warn("conf: ", core.json.encode(conf))
    core.log.warn("ctx: ", core.json.encode(ctx, true))
end
```

### Put Everything Together[â](#put-everything-together "Direct link to Put Everything Together")

When you put together all the code above, `file-proxy.lua` should look like the following:

```
-- Introduce the necessary modules/libraries we need for this plugin 
local core     = require("apisix.core")
local io       = require("io")
local ngx      = ngx

-- Declare the plugin's name
local plugin_name = "file-proxy"

-- Define the plugin schema format
local plugin_schema = {
    type = "object",
    properties = {
        path = {
            type = "string" -- The path of the file to be served
        },
    },
    required = {"path"} -- The path is a required field
}

-- Define the plugin with its version, priority, name, and schema
local _M = {
    version = 1.0,
    priority = 1000,
    name = plugin_name,
    schema = plugin_schema
}

-- Function to check if the plugin configuration is correct
function _M.check_schema(conf)
  -- Validate the configuration against the schema
  local ok, err = core.schema.check(plugin_schema, conf)
  -- If validation fails, return false and the error
  if not ok then
      return false, err
  end
  -- If validation succeeds, return true
  return true
end

-- Function to be called during the access phase
function _M.access(conf, ctx)
  -- Open the file specified in the configuration
  local fd = io.open(conf.path, "rb")
  -- If the file is opened successfully, read its content and return it as the response
  if fd then
    local content = fd:read("*all")
    fd:close()
    ngx.header.content_length = #content
    ngx.say(content)
    ngx.exit(ngx.OK)
  else
    -- If the file cannot be opened, log an error and return a 404 Not Found status
    ngx.exit(ngx.HTTP_NOT_FOUND)
    core.log.error("File is not found: ", conf.path, ", error info: ", err)
  end
end


-- Function to be called during the log phase
function _M.log(conf, ctx)
    -- Log the plugin configuration and the request context
    core.log.warn("conf: ", core.json.encode(conf))
    core.log.warn("ctx: ", core.json.encode(ctx, true))
end

-- Return the plugin so it can be used by APISIX
return _M
```

## Source Custom Plugin[â](#source-custom-plugin "Direct link to Source Custom Plugin")

There are two approaches to load the custom plugin code into APISIX:

1. Place the plugin source code in the default APISIX plugins directory `/apisix/plugins` along with the other APISIX plugins.
2. Place the plugin source code in a separate directory and specify the search path in `extra_lua_path` in the `config.yaml`.

The following sections provide instructions for the second approach as it is recommended to manage custom code in a separate directory.

### Create Custom Plugin File

APISIX looks for L7 plugins within `/apisix/plugins` and L4 plugins within `/apisix/stream/plugins` in your custom directory.

For the custom plugin, create a directory with a customized name and `/apisix/plugins` within the directory:

```
docker exec apisix-quickstart /bin/sh -c "mkdir -p custom-plugin/apisix/plugins"
```

Save the plugin file to the directory:

```
docker exec apisix-quickstart /bin/sh -c "echo '
local core     = require(\"apisix.core\")
local io       = require(\"io\")
local ngx      = ngx

local plugin_name = \"file-proxy\"

local plugin_schema = {
    type = \"object\",
    properties = {
        path = {
            type = \"string\"
        },
    },
    required = {\"path\"}
}

local _M = {
    version = 1.0,
    priority = 1000,
    name = plugin_name,
    schema = plugin_schema
}

function _M.check_schema(conf)
  local ok, err = core.schema.check(plugin_schema, conf)
  if not ok then
      return false, err
  end
  return true
end

function _M.access(conf, ctx)
  local fd = io.open(conf.path,\"rb\")
  if fd then
    local content = fd:read(\"*all\")
    fd:close()
    ngx.header.content_length = #content
    ngx.say(content)
    ngx.exit(ngx.OK)
  else
    ngx.exit(ngx.HTTP_NOT_FOUND)
    core.log.error(\"File is not found: \", conf.path, \", error info: \", err)
  end
end

function _M.log(conf, ctx)
    core.log.warn(\"conf: \", core.json.encode(conf))
    core.log.warn(\"ctx: \", core.json.encode(ctx, true))
end

return _M
' > /usr/local/apisix/custom-plugin/apisix/plugins/file-proxy.lua"
```

### Update APISIX Configuration File

Update APISIX [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) with the search path to the custom plugin in `extra_lua_path` and add the plugin name to the plugin list:

```
docker exec apisix-quickstart /bin/sh -c "echo '
apisix:
  extra_lua_path: "/usr/local/apisix/custom-plugin/\?.lua"
  enable_control: true
  control:
    ip: 0.0.0.0
    port: 9092
deployment:
  role: traditional
  role_traditional:
    config_provider: etcd
  admin:
    admin_key_required: false
    allow_admin:
      - 0.0.0.0/0
plugin_attr:
  prometheus:
    export_addr:
      ip: 0.0.0.0
      port: 9091
plugins:       
  - file-proxy
' > /usr/local/apisix/conf/config.yaml"
```

â¶ `extra_lua_path`: Search path for the custom plugin.

caution

Note that adding only the `file-proxy` plugin to the plugin list will override all existing default plugins. To make the `file-proxy` plugin an addition to the existing plugins, you should copy over the names of the existing plugins and add them to the list.

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

## Test Custom Plugin[â](#test-custom-plugin "Direct link to Test Custom Plugin")

### Store Test File[â](#store-test-file "Direct link to Store Test File")

Store a static `openapi.yaml` file in the APISIX instance:

```
docker exec apisix-quickstart /bin/sh -c "echo '
openapi: 3.0.1
info:
  title: OpenAPI Spec
  description: OpenAPI Spec file description.  
' > /usr/local/apisix/openapi.yaml"
```

### Create a Route[â](#create-a-route "Direct link to Create a Route")

To use the `file-proxy` custom plugin, you need to create a route in APISIX that uses the plugin:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id":"openapi-file-proxy",
  "uri":"/openapi.yaml",
  "plugins":{
     "file-proxy":{
        "path":"/usr/local/apisix/openapi.yaml"
     }
  }
}'
```

adc.yaml

```
services:
  - name: OpenAPI File Proxy Service
    routes:
      - uris:
          - /openapi.yaml
        name: openapi-file-proxy
        plugins:
          file-proxy:
            path: /usr/local/apisix/openapi.yaml
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Validate the Plugin[â](#validate-the-plugin "Direct link to Validate the Plugin")

Send a request to the route:

```
curl "http://127.0.0.1:9080/openapi.yaml"
```

The response should be the content of the file `openapi.yaml`:

```
openapi: 3.0.1
info:
  title: OpenAPI Spec
  description: OpenAPI Spec file description.
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

Developing custom plugins for APISIX with Lua is a powerful way to extend the functionalities of the API gateway. You can also develop plugins in other programming languages such as Java, Go, and Python, with the support of plugin runners (coming soon).
