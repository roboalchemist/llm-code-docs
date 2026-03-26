# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/proxy-transport-layer-l4-traffic.md

# Proxy Transport Layer (L4) Traffic

By default, APISIX operates as an application layer (L7) proxy. APISIX also supports the handling of transport layer (L4) TCP and UDP traffic, either dedicated or on top of the handling of application layer (L7) traffic.

This guide will show you how to configure APISIX to proxy transport layer (L4) traffic and configure a [stream route](https://docs.api7.ai/apisix/key-concepts/stream-routes.md) to establish a connection with MySQL server.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.
* Install [MySQL Shell](https://dev.mysql.com/downloads/shell/) to initiate connections with MySQL server.

## Start a MySQL Server[â](#start-a-mysql-server "Direct link to Start a MySQL Server")

Start a MySQL instance as a sample upstream service and configure the root password to be `my-secret-pw`:

```
docker run -d \
  --name mysql \
  --network=apisix-quickstart-net \
  -e MYSQL_ROOT_PASSWORD=my-secret-pw \
  mysql:9.4
```

## Enable Transport Layer (L4) Proxy[â](#enable-transport-layer-l4-proxy "Direct link to Enable Transport Layer (L4) Proxy")

By default, APISIX only has application layer (L7) proxy enabled. To also proxy transport layer (L4) traffic, configure `proxy_mode` and `stream_proxy`.

Update the `config.yaml` [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as follows:

```
docker exec apisix-quickstart /bin/sh -c "echo '
apisix:
  enable_control: true
  control:
    ip: 0.0.0.0
    port: 9092
  proxy_mode: http&stream
  stream_proxy:
    tcp:
      - 9100
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
' > /usr/local/apisix/conf/config.yaml"
```

â¶ `proxy_mode`: accept both transport layer (L4) and application layer (L7) traffic.

â· `stream_proxy`: configure the interface for transport layer (L4) proxy.

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

If you started APISIX in Docker with [Getting Started quickstart](https://docs.api7.ai/apisix/getting-started/.md#get-apisix), port `9100` is already mapped (`-p 9100:9100`).

## Create a Stream Route[â](#create-a-stream-route "Direct link to Create a Stream Route")

Create a [stream route](https://docs.api7.ai/apisix/key-concepts/stream-routes.md) and configure MySQL server to be the upstream service.

```
curl "http://127.0.0.1:9180/apisix/admin/stream_routes" -X PUT -d '
{
  "id": "stream-route-mysql",
  "server_port": 9100,
  "upstream": {
    "nodes": {
      "mysql:3306": 1
    },
    "type": "roundrobin"
  }
}'
```

## Verify[â](#verify "Direct link to Verify")

Connect with the MySQL server as root and key in the password `my-secret-pw` once prompted:

```
mysql --host=127.0.0.1 --port=9100 -u root -p
```

If successful, you should see a welcome text similar to the following:

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 9.4.0 MySQL Community Server - GPL
Copyright (c) 2000, 2025, Oracle and/or its affiliates.
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

APISIX also supports TLS over TCP connections as a transport layer (L4) proxy when accepting requests from downstream clients or proxying to upstream services. See the configure TLS over TCP how-to guide to learn more (coming soon).
