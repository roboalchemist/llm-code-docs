# Source: https://docs.api7.ai/apisix/reference/file-standalone-configurations.md

# File-Driven Standalone Mode Configurations

In [file-driven standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#file-driven), APISIX fetches configuration from [`apisix.yaml`](https://docs.api7.ai/apisix/reference/configuration-files.md#apisixyaml) or [`apisix.json`](https://docs.api7.ai/apisix/reference/configuration-files.md#apisixjson) instead of using etcd as the configuration center. These configurations are loaded into memory at startup and monitored for changes at a regular interval, without the requirement of manually reloading APISIX.

important

If you are working with `apisix.yaml`, please note that APISIX will not load the configurations if there is no `#END` at the end of the file.

This document provides some configuration examples for APISIX deployed in file-driven standalone mode. To learn more about the available configuration options, see the [Admin API reference](https://docs.api7.ai/apisix/reference/admin-api/.md) (but do not use these endpoints). These configuration options can be translated into YAML or JSON for use in file-driven standalone mode.

## Configure Routes[â](#configure-routes "Direct link to Configure Routes")

This example creates two routes to forward requests to `/hello` and `/hello2` to different upstreams:

* YAML
* JSON

apisix.yaml

```
routes:
  -
    uri: /hello
    upstream:
      nodes:
        "127.0.0.1:1980": 1
      type: roundrobin
  -
    uri: /hello2
    upstream:
      nodes:
        "127.0.0.1:1981": 1
      type: roundrobin
#END
```

apisix.json

```
{
  "routes": [
    {
      "uri": "/hello",
      "upstream": {
        "nodes": {
          "127.0.0.1:1980": 1
        },
        "type": "roundrobin"
      }
    },
    {
      "uri": "/hello2",
      "upstream": {
        "nodes": {
          "127.0.0.1:1981": 1
        },
        "type": "roundrobin"
      }
    }
  ]
}
```

## Configure Routes and Services[â](#configure-routes-and-services "Direct link to Configure Routes and Services")

This example creates a [service](https://docs.api7.ai/apisix/key-concepts/services.md) and a [route](https://docs.api7.ai/apisix/key-concepts/routes.md) within the service:

* YAML
* JSON

apisix.yaml

```
routes:
  -
    uri: /hello
    service_id: 1
services:
  -
    id: 1
    upstream:
      nodes:
        "127.0.0.1:1980": 1
      type: roundrobin
#END
```

apisix.json

```
{
  "routes": [
    {
      "uri": "/hello",
      "service_id": 1
    }
  ],
  "services": [
    {
      "id": 1,
      "upstream": {
        "nodes": {
          "127.0.0.1:1980": 1
        },
        "type": "roundrobin"
      }
    }
  ]
}
```

## Configure Routes and Upstreams[â](#configure-routes-and-upstreams "Direct link to Configure Routes and Upstreams")

This example creates an [upstream](https://docs.api7.ai/apisix/key-concepts/upstreams.md) and a [route](https://docs.api7.ai/apisix/key-concepts/routes.md) that points to the upstream:

* YAML
* JSON

apisix.yaml

```
routes:
  -
    uri: /hello
    upstream_id: 1
upstreams:
  -
    id: 1
    nodes:
      "127.0.0.1:1980": 1
    type: roundrobin
#END
```

apisix.json

```
{
  "routes": [
    {
      "uri": "/hello",
      "upstream_id": 1
    }
  ],
  "upstreams": [
    {
      "id": 1,
      "nodes": {
        "127.0.0.1:1980": 1
      },
      "type": "roundrobin"
    }
  ]
}
```

## Configure Routes, Services, and Upstreams[â](#configure-routes-services-and-upstreams "Direct link to Configure Routes, Services, and Upstreams")

This example creates an [upstream](https://docs.api7.ai/apisix/key-concepts/upstreams.md), a [service](https://docs.api7.ai/apisix/key-concepts/services.md), and a [route](https://docs.api7.ai/apisix/key-concepts/routes.md) within the service:

* YAML
* JSON

apisix.yaml

```
routes:
  -
    uri: /hello
    service_id: 1
services:
  -
    id: 1
    upstream_id: 2
upstreams:
  -
    id: 2
    nodes:
      "127.0.0.1:1980": 1
    type: roundrobin
#END
```

apisix.json

```
{
  "routes": [
    {
      "uri": "/hello",
      "service_id": 1
    }
  ],
  "services": [
    {
      "id": 1,
      "upstream_id": 2
    }
  ],
  "upstreams": [
    {
      "id": 2,
      "nodes": {
        "127.0.0.1:1980": 1
      },
      "type": "roundrobin"
    }
  ]
}
```

## Configure Plugins[â](#configure-plugins "Direct link to Configure Plugins")

This example enables three [plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md):

* YAML
* JSON

apisix.yaml

```
plugins:
  - name: ip-restriction
  - name: jwt-auth
  - name: mqtt-proxy
    stream: true
#END
```

apisix.json

```
{
  "plugins": [
    {
      "name": "ip-restriction"
    },
    {
      "name": "jwt-auth"
    },
    {
      "name": "mqtt-proxy",
      "stream": true
    }
  ]
}
```

Set `stream` to `true` for L4 plugins.

Note that this configuration will override the list of plugins enabled by default or in the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample).

## Configure Plugin Configs[â](#configure-plugin-configs "Direct link to Configure Plugin Configs")

This example creates a [plugin config](https://docs.api7.ai/apisix/key-concepts/plugin-configs.md) which is referenced by a [route](https://docs.api7.ai/apisix/key-concepts/routes.md):

* YAML
* JSON

apisix.yaml

```
plugin_configs:
  -
    id: 1
    plugins:
      response-rewrite:
        body: "hello\n"
routes:
  - id: 1
    uri: /hello
    plugin_config_id: 1
    upstream:
    nodes:
      "127.0.0.1:1980": 1
    type: roundrobin
#END
```

apisix.json

```
{
  "plugin_configs": [
    {
      "id": 1,
      "plugins": {
        "response-rewrite": {
          "body": "hello\n"
        }
      }
    }
  ],
  "routes": [
    {
      "id": 1,
      "uri": "/hello",
      "plugin_config_id": 1,
      "upstream": {
        "nodes": {
          "127.0.0.1:1980": 1
        },
        "type": "roundrobin"
      }
    }
  ]
}
```

## Configure Plugin Global Rules[â](#configure-plugin-global-rules "Direct link to Configure Plugin Global Rules")

This example creates a [plugin global rule](https://docs.api7.ai/apisix/key-concepts/plugin-global-rules.md):

* YAML
* JSON

apisix.yaml

```
global_rules:
  -
    id: 1
    plugins:
      response-rewrite:
        body: "hello\n"
#END
```

apisix.json

```
{
  "global_rules": [
    {
      "id": 1,
      "plugins": {
        "response-rewrite": {
          "body": "hello\n"
        }
      }
    }
  ]
}
```

## Configure Plugin Metadata[â](#configure-plugin-metadata "Direct link to Configure Plugin Metadata")

This example creates [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md):

* YAML
* JSON

apisix.yaml

```
upstreams:
  - id: 1
    nodes:
      "127.0.0.1:1980": 1
    type: roundrobin
routes:
  -
    uri: /hello
    upstream_id: 1
    plugins:
      http-logger:
        batch_max_size: 1
        uri: http://127.0.0.1:1980/log
plugin_metadata:
  - id: http-logger
    log_format:
      host: "$host",
      remote_addr: "$remote_addr"
#END
```

apisix.json

```
{
  "upstreams": [
    {
      "id": 1,
      "nodes": {
        "127.0.0.1:1980": 1
      },
      "type": "roundrobin"
    }
  ],
  "routes": [
    {
      "uri": "/hello",
      "upstream_id": 1,
      "plugins": {
        "http-logger": {
          "batch_max_size": 1,
          "uri": "http://127.0.0.1:1980/log"
        }
      }
    }
  ],
  "plugin_metadata": [
    {
      "id": "http-logger",
      "log_format": {
        "host": "$host",
        "remote_addr": "$remote_addr"
      }
    }
  ]
}
```

## Configure SSL[â](#configure-ssl "Direct link to Configure SSL")

This example configures [SSL](https://docs.api7.ai/apisix/key-concepts/ssl-certificates.md):

* YAML
* JSON

apisix.yaml

```
ssls:
  - 
    cert: ${{SERVER_CERT}}
    key: ${{SERVER_KEY}}
    snis:
      - "yourdomain.com"
#END
```

apisix.json

```
{
  "ssls": [
    {
      "cert": "${{SERVER_CERT}}",
      "key": "${{SERVER_KEY}}",
      "snis": [
        "yourdomain.com"
      ]
    }
  ]
}
```

To learn more about setting environment variables, see [Use Environment Variables in Configuration Files](https://docs.api7.ai/apisix/reference/configuration-files.md#use-environment-variables-in-configuration-files).

## Configure Consumers[â](#configure-consumers "Direct link to Configure Consumers")

This example creates a [consumer](https://docs.api7.ai/apisix/key-concepts/consumers.md):

* YAML
* JSON

apisix.yaml

```
consumers:
  - username: jwt
    plugins:
      jwt-auth:
        key: user-key
        secret: my-secret-key
#END
```

apisix.json

```
{
  "consumers": [
    {
      "username": "jwt",
      "plugins": {
        "jwt-auth": {
          "key": "user-key",
          "secret": "my-secret-key"
        }
      }
    }
  ]
}
```

## Configure Stream Routes[â](#configure-stream-routes "Direct link to Configure Stream Routes")

This example creates a [stream route](https://docs.api7.ai/apisix/key-concepts/stream-routes.md):

* YAML
* JSON

apisix.yaml

```
stream_routes:
  - server_addr: 127.0.0.1
    server_port: 1985
    id: 1
    upstream:
       nodes:
         "127.0.0.1:1981": 1
       type: roundrobin
    plugins:
      mqtt-proxy:
        protocol_name: "MQTT"
        protocol_level: 4
#END
```

apisix.json

```
{
  "stream_routes": [
    {
      "server_addr": "127.0.0.1",
      "server_port": 1985,
      "id": 1,
      "upstream": {
        "nodes": {
          "127.0.0.1:1981": 1
        },
        "type": "roundrobin"
      },
      "plugins": {
        "mqtt-proxy": {
          "protocol_name": "MQTT",
          "protocol_level": 4
        }
      }
    }
  ]
}
```

## Configure Protos[â](#configure-protos "Direct link to Configure Protos")

This example creates a [proto object](https://docs.api7.ai/apisix/key-concepts/protos.md):

* YAML
* JSON

apisix.yaml

```
protos:
  - id: helloworld
    desc: hello world
    content: >
      syntax = "proto3";
      package helloworld;

      service Greeter {
        rpc SayHello (HelloRequest) returns (HelloReply) {}
      }
      message HelloRequest {
        string name = 1;
      }
      message HelloReply {
        string message = 1;
      }
#END
```

apisix.json

```
{
  "protos": [
    {
      "id": "helloworld",
      "desc": "hello world",
      "content": "syntax = \"proto3\";\npackage helloworld;\n\nservice Greeter {\n  rpc SayHello (HelloRequest) returns (HelloReply) {}\n}\nmessage HelloRequest {\n  string name = 1;\n}\nmessage HelloReply {\n  string message = 1;\n}"
    }
  ]
}
```
