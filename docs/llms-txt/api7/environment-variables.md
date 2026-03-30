# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/environment-variables.md

# Source: https://docs.api7.ai/apisix/reference/environment-variables.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/environment-variables.md

# Source: https://docs.api7.ai/apisix/reference/environment-variables.md

# Environment Variables

APISIX supports the use of environment variables in static [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) and certain plugins. There are a few environment variables reserved for special purposes, and others that can be created with custom names and referenced.

## Reserved Environment Variables[â](#reserved-environment-variables "Direct link to Reserved Environment Variables")

APISIX currently reserves the following environment variables:

| Variable Name                 | Description                                                                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `APISIX_DEPLOYMENT_ETCD_HOST` | etcd host address.                                                                                                                                                         |
| `APISIX_PROFILE`              | Deployment environment differentiating the [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md#manage-configuration-files-by-environments). |
| `APISIX_WORKER_PROCESSES`     | Number of worker processes.                                                                                                                                                |

To use these configurations, assign values to the environment variables before starting APISIX.

## Custom Environment Variables[â](#custom-environment-variables "Direct link to Custom Environment Variables")

You can use custom environment variables in configuration files and for certain plugins.

### Configuration Files[â](#configuration-files "Direct link to Configuration Files")

In APISIX, you can use environment variables in the [`config.yaml`](#configyaml-and-configyamlexample) or [`apisix.yaml`](#apisixyaml) configuration files for values that should be configurable during deployments, using the `${{ENV_VAR}}` or `${{ENV_VAR:=default_value}}` syntax.

The example below sets the listening ports for client requests and Admin API in environment variables:

```
export APISIX_NODE_LISTEN=8132
export ADMIN_API_PORT=9232
```

In `config.yaml`, reference the environment variables as follows:

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

### Plugins[â](#plugins "Direct link to Plugins")

APISIX supports the use of environment variables in plugin configurations for confidential information, such as [Redis password](https://docs.api7.ai/hub/limit-count/configuration.md#parameters) and [authentication key](https://docs.api7.ai/hub/jwt-auth.md#manage-secrets-in-environment-variables), through the [NGINX `env` directive](https://nginx.org/en/docs/ngx_core_module.html#env).

The following example demonstrates how you can configure the `key-auth` plugin to fetch user authentication key from an environment variable.

Save the value of the key to an environment variable:

```
export JACK_AUTH_KEY=jack-key
```

tip

If you are running APISIX in Docker, you should set the environment variable using the `-e` flag when starting the container.

Create a consumer `jack`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "jack"
  }'
```

Configure the `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/jack/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jack-key-auth",
    "plugins": {
      "key-auth": {
        "key": "$env://JACK_AUTH_KEY"
      }
    }
  }'
```

Create a route and enable `key-auth`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "key-auth-route",
    "uri": "/anything",
    "plugins": {
      "key-auth": {}
    },
    "upstream" : {
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

Send a request to the route with the authentication key:

```
curl "http://127.0.0.1:9080/anything" -H 'apikey: jack-key'
```

You should receive an `HTTP/1.1 200 OK` response.

For more information on the environment variable support in plugins, see [plugin docs](https://docs.api7.ai/hub.md).
