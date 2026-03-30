# Source: https://docs.api7.ai/apisix/reference/configuration-files.md

# Configuration Files

APISIX has the following configuration files under `/conf`:

* `config.yaml`
* `config.yaml.example`
* `apisix.yaml`
* `debug.yaml`

In addition, you can place `apisix.json` under `/conf` if you wish to work with JSON in the [file-driven standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#file-driven).

This document provides a reference for how configuration files are used and how to manage configuration files by environments.

## Usage[â](#usage "Direct link to Usage")

### `config.yaml` and `config.yaml.example`[â](#configyaml-and-configyamlexample "Direct link to configyaml-and-configyamlexample")

APISIX comes with a configuration file `config.yaml`, which is used to customize a number of parameters, including the listening interface, deployment mode, plugin attributes, and more.

The default values for these parameters can be found in [`apisix/cli/config.lua`](https://github.com/apache/apisix/blob/master/apisix/cli/config.lua).

You may find the sample configuration file for `config.yaml` at [`config.yaml.example`](https://github.com/apache/apisix/blob/master/conf/config.yaml.example):

```
apisix:
  # node_listen: 9080               # APISIX listening port (single)
  node_listen:                      # APISIX listening ports (multiple)
    - 9080
  #   - port: 9081
  #     enable_http2: true          # If not set, the default value is `false`.
  #   - ip: 127.0.0.2
  #     port: 9082
  #     enable_http2: true
  enable_admin: true
  enable_dev_mode: false
  enable_reuseport: true 
  ...
```

Configurations in `config.yaml` is loaded once at startup. If you make any updates to this file, [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

### `apisix.yaml`[â](#apisixyaml "Direct link to apisixyaml")

In APISIX file-driven standalone deployment mode, `apisix.yaml` is used to configure APISIX resources, such as [routes](https://docs.api7.ai/apisix/key-concepts/routes.md), [upstreams](https://docs.api7.ai/apisix/key-concepts/upstreams.md), [consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md), and others.

These configurations are loaded by APISIX into memory at startup. Changes to this file do not require a reload of APISIX as the file is monitored for changes at a regular interval.

For more information about how to configure `apisix.yaml`, see [File-Driven Standalone Mode](https://docs.api7.ai/apisix/reference/file-standalone-configurations.md).

### `apisix.json`[â](#apisixjson "Direct link to apisixjson")

`apisix.json` is `apisix.yaml`'s JSON-equivalent in the file-driven standalone deployment mode to configure APISIX resources.

For more information about how to configure `apisix.json`, see [File-Driven Standalone Mode](https://docs.api7.ai/apisix/reference/file-standalone-configurations.md).

### `debug.yaml`[â](#debugyaml "Direct link to debugyaml")

You can enable and customize APISIX debug mode using configuration options in `debug.yaml`.

Changes to this file do not require a reload of APISIX as the file is monitored for changes at a regular interval.

To learn more, see [Use Debug Mode](https://docs.api7.ai/apisix/how-to-guide/troubleshooting/debug-mode.md).

## Manage Configuration Files by Environments[â](#manage-configuration-files-by-environments "Direct link to Manage Configuration Files by Environments")

Keeping configuration files separate for different environments, such as development, staging, and production, can provide several benefits, including increased flexibility, improved security, and easier maintenance.

APISIX supports separation of configuration files by environment. You can set the `APISIX_PROFILE` environment variable to differentiate which set of other configuration files APISIX should use.

By default, when `APISIX_PROFILE` is not set, APISIX looks for the following configuration files:

* `conf/config.yaml`
* `conf/apisix.yaml`
* `conf/debug.yaml`

If the value of `APISIX_PROFILE` is set to `prod`, APISIX looks for the following configuration files:

* `conf/config-prod.yaml`
* `conf/apisix-prod.yaml`
* `conf/debug-prod.yaml`

You can set `APISIX_PROFILE` to any other value that matches your environment.

## Use Environment Variables in Configuration Files[â](#use-environment-variables-in-configuration-files "Direct link to Use Environment Variables in Configuration Files")

In APISIX, you can use environment variables in the [`config.yaml`](#configyaml-and-configyamlexample), [`apisix.yaml`](#apisixyaml), or [`apisix.json`](#apisixjson) configuration files for values that should be configurable during deployments, using the `${{ENV_VAR}}` or `${{ENV_VAR:=default_value}}` syntax.

### Examples[â](#examples "Direct link to Examples")

If you are running APISIX locally (outside Docker), you could use the export command to set the environment variable:

```
export YOUR_VARIABLE=value
```

If you are running APISIX in Docker, you should set the environment variable using the `-e` flag when starting the container.

#### Use Environment Variables in `config.yaml`[â](#use-environment-variables-in-configyaml "Direct link to use-environment-variables-in-configyaml")

The example below sets the listening ports of client requests and Admin API in environment variables.

For instance, set `APISIX_NODE_LISTEN:8132` and `ADMIN_API_PORT:9232` in environment variables. In `config.yaml`, you can reference the environment variables as follows:

config.yaml

```
apisix:
  node_listen:
    - ${{APISIX_NODE_LISTEN}}
deployment:
  admin:
    admin_listen:
      port: ${{ADMIN_API_PORT}}
```

After being started, APISIX will listen on port `8132` for client requests and port `9232` for Admin API requests.

#### Use Environment Variables in `apisix.yaml`[â](#use-environment-variables-in-apisixyaml "Direct link to use-environment-variables-in-apisixyaml")

The example below sets the upstream node address of a route in an environment variable.

For instance, set `UPSTREAM_ADDR:httpbin.org` in an environment variable. In `apisix.yaml`, you can reference the environment variable as follows:

apisix.yaml

```
routes:
  - uri: /ip
    upstream:
      nodes:
        "${{UPSTREAM_ADDR}}": 1
      type: roundrobin
```

In standalone mode, APISIX will hot reload the configurations and start proxying requests to this route to `httpbin.org`.

#### Use Environment Variables in `apisix.json`[â](#use-environment-variables-in-apisixjson "Direct link to use-environment-variables-in-apisixjson")

The example below sets the upstream node address of a route in an environment variable.

For instance, set `UPSTREAM_ADDR:httpbin.org` in an environment variable. In `apisix.json`, you can reference the environment variable as follows:

apisix.json

```
{
    "routes": [
      {
        "uri": "/ip",
        "upstream": {
          "nodes": {
            "${{UPSTREAM_ADDR}}": 1
          },
          "type": "roundrobin"
        }
      }
    ]
}
```

In standalone mode, APISIX will hot reload the configurations and start proxying requests to this route to `httpbin.org`.

#### Set a Fallback Value[â](#set-a-fallback-value "Direct link to Set a Fallback Value")

You can also configure default values to fall back to if no environment variables are set, for example:

config.yaml

```
apisix:
  node_listen:
    - ${{APISIX_NODE_LISTEN:=9080}}
deployment:
  admin:
    admin_listen:
      port: ${{ADMIN_API_PORT:=9180}}
```

If APISIX cannot resolve values for `APISIX_NODE_LISTEN` and `ADMIN_API_PORT` in the environment, it will default to listen on port `9080` for client requests and port `9180` for Admin API requests.
