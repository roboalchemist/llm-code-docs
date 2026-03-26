# Source: https://docs.api7.ai/hub/kafka-logger.md

# kafka-logger

The `kafka-logger` plugin pushes request and response logs as JSON objects to Apache Kafka clusters in batches and supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `kafka-logger` plugin for different scenarios.

To follow along the examples, start a sample Kafka cluster using the below Docker compose file:

docker-compose.yml

```
services:
  zookeeper-server1:
    image: bitnami/zookeeper:3.6.0
    environment:
      ALLOW_ANONYMOUS_LOGIN: "yes"
    restart: unless-stopped
    ports:
      - "2181:2181"
    networks:
      kafka_net:

  zookeeper-server2:
    image: bitnami/zookeeper:3.6.0
    environment:
      ALLOW_ANONYMOUS_LOGIN: "yes"
    restart: unless-stopped
    ports:
      - "12181:12181"
    networks:
      kafka_net:

  kafka-server1:
    image: bitnami/kafka:2.8.1
    container_name: notkafka
    environment:
      KAFKA_CFG_ZOOKEEPER_CONNECT: zookeeper-server1:2181
      ALLOW_PLAINTEXT_LISTENER: "yes"
      KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE: "true"
      KAFKA_CFG_ADVERTISED_LISTENERS: PLAINTEXT://127.0.0.1:9092
    restart: unless-stopped
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper-server1
      - zookeeper-server2
    networks:
      kafka_net:

networks:
  kafka_net:
```

Start containers:

```
docker compose up -d
```

Wait for messages in the configured Kafka topic:

```
docker exec -it notkafka kafka-console-consumer.sh --bootstrap-server kafka-server1:9092 --topic test2 --from-beginning
```

Open a new terminal session for the following steps working with APISIX.

### Log in Different Meta Log Formats[â](#log-in-different-meta-log-formats "Direct link to Log in Different Meta Log Formats")

The following example demonstrates how you can enable the `kafka-logger` plugin on a route, which logs client requests to the route and pushes logs to Kafka. You will also understand the differences between the `default` and `origin` meta log formats.

Create a route with `kafka-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "kafka-logger-route",
    "uri": "/get",
    "plugins": {
      "kafka-logger": {
        "meta_format": "default",
        "brokers": [
          {
            "host": "127.0.0.1",
            "port": 9092
          }
        ],
        "kafka_topic": "test2",
        "key": "key1",
        "batch_max_size": 1
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ `meta_format`: set to the `default` log format.

â· `batch_max_size`: set to 1 to send the log entry immediately.

Send a request to the route to generate a log entry:

```
curl -i "http://127.0.0.1:9080/get"
```

You should see an `HTTP/1.1 200 OK` response.

You should see a log entry in the Kafka topic similar to the following:

```
{
  "latency": 411.00001335144,
  "request": {
    "querystring": {},
    "headers": {
      "host": "127.0.0.1:9080",
      "user-agent": "curl/7.74.0",
      "accept": "*/*"
    },
    "method": "GET",
    "size": 83,
    "uri": "/get",
    "url": "http://127.0.0.1:9080/get"
  },
  "response": {
    "headers": {
      "content-length": "233",
      "access-control-allow-credentials": "true",
      "content-type": "application/json",
      "connection": "close",
      "access-control-allow-origin": "*",
      "date": "Fri, 10 Nov 2023 06:02:44 GMT",
      "server": "APISIX/3.8.0"
    },
    "status": 200,
    "size": 475
  },
  "route_id": "kafka-logger-route",
  "client_ip": "127.0.0.1",
  "server": {
    "hostname": "debian-apisix",
    "version": "3.8.0"
  },
  "apisix_latency": 18.00001335144,
  "service_id": "",
  "upstream_latency": 393,
  "start_time": 1699596164550,
  "upstream": "54.90.18.68:80"
}
```

Update the meta log format to `origin`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/kafka-logger-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "kafka-logger": {
        "meta_format": "origin"
      }
    }
  }'
```

Send a request to the route again to generate a new log entry:

```
curl -i "http://127.0.0.1:9080/get"
```

You should see an `HTTP/1.1 200 OK` response.

You should see a log entry in the Kafka topic similar to the following:

```
GET /get HTTP/1.1
host: 127.0.0.1:9080
user-agent: curl/7.74.0
accept: */*
```

### Log Request and Response Headers With Plugin Metadata[â](#log-request-and-response-headers-with-plugin-metadata "Direct link to Log Request and Response Headers With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

First, create a route with `kafka-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "kafka-logger-route",
    "uri": "/get",
    "plugins": {
      "kafka-logger": {
        "meta_format": "default",
        "brokers": [
          {
            "host": "127.0.0.1",
            "port": 9092
          }
        ],
        "kafka_topic": "test2",
        "key": "key1",
        "batch_max_size": 1
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ `meta_format`: set to the `default` log format. It is important to note that this is mandatory if you would like to customize log format with plugin metadata. If `meta_format` is set to `origin`, the log entries will remain in `origin` format.

â· `batch_max_size`: set to 1 to send the log entry immediately.

Next, configure the plugin metadata for `kafka-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/kafka-logger" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "log_format": {
      "host": "$host",
      "@timestamp": "$time_iso8601",
      "client_ip": "$remote_addr",
      "env": "$http_env",
      "resp_content_type": "$sent_http_Content_Type"
    }
  }'
```

â¶ log the custom request header `env`.

â· log the response header `Content-Type`.

Send a request to the route with the `env` header:

```
curl -i "http://127.0.0.1:9080/get" -H "env: dev"
```

You should see a log entry in the Kafka topic similar to the following:

```
{
  "@timestamp": "2023-11-10T23:09:04+00:00",
  "host": "127.0.0.1",
  "client_ip": "127.0.0.1",
  "route_id": "kafka-logger-route",
  "env": "dev",
  "resp_content_type":"application/json"
}
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with `kafka-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "kafka-logger-route",
    "uri": "/post",
    "plugins": {
      "kafka-logger": {
        "brokers": [
          {
            "host": "127.0.0.1",
            "port": 9092
          }
        ],
        "kafka_topic": "test2",
        "key": "key1",
        "batch_max_size": 1,
        "include_req_body": true,
        "include_req_body_expr": [["arg_log_body", "==", "yes"]]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ `include_req_body`: set to true to include request body.

â· `include_req_body_expr`: only include request body if the URL query string `log_body` is `yes`.

Send a request to the route with a URL query string satisfying the condition:

```
curl -i "http://127.0.0.1:9080/post?log_body=yes" -X POST -d '{"env": "dev"}'
```

You should see the request body logged:

```
{
  ...,
    "method": "POST",
    "body": "{\"env\": \"dev\"}",
    "size": 179
  }
}
```

Send a request to the route without any URL query string:

```
curl -i "http://127.0.0.1:9080/post" -X POST -d '{"env": "dev"}'
```

You should not observe the request body in the log.

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "kafka-logger": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```
