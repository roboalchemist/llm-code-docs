# Source: https://docs.api7.ai/hub/elasticsearch-logger.md

# elasticsearch-logger

The `elasticsearch-logger` plugin pushes request and response logs in batches to [Elasticsearch](https://www.elastic.co) and supports the customization of log formats. When enabled, the plugin will serialize the request context information to [Elasticsearch Bulk format](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html#docs-bulk) and add them to the queue, before they are pushed to Elasticsearch.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `elasticsearch-logger` plugin for different scenarios.

To follow along the examples, start an Elasticsearch instance in Docker:

```
docker run -d \
  --name elasticsearch \
  --network apisix-quickstart-net \
  -v elasticsearch_vol:/usr/share/elasticsearch/data/ \
  -p 9200:9200 \
  -p 9300:9300 \
  -e ES_JAVA_OPTS="-Xms512m -Xmx512m" \
  -e discovery.type=single-node \
  -e xpack.security.enabled=false \
  docker.elastic.co/elasticsearch/elasticsearch:7.17.1
```

Start a Kibana instance in Docker to visualize the indexed data in Elasticsearch:

```
docker run -d \
  --name kibana \
  --network apisix-quickstart-net \
  -p 5601:5601 \
  -e ELASTICSEARCH_HOSTS="http://elasticsearch:9200" \
  docker.elastic.co/kibana/kibana:7.17.1
```

If successful, you should see the Kibana dashboard on [localhost:5601](http://localhost:5601).

### Log in the Default Log Format[â](#log-in-the-default-log-format "Direct link to Log in the Default Log Format")

The following example demonstrates how you can enable the `elasticsearch-logger` plugin on a route, which logs client requests and responses, as well as pushing logs to Elasticsearch.

Create a route with `elasticsearch-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "elasticsearch-logger-route",
    "uri": "/anything",
    "plugins": {
      "elasticsearch-logger": {
        "endpoint_addrs": ["http://elasticsearch:9200"],
        "field": {
          "index": "gateway",
          "type": "logs"
        }
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

â¶ Configure the endpoint address to Elasticsearch.

â· Configure the `index` field as `gateway`.

â¸ Configure the `type` field as `logs`.

Send a request to the route to generate a log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the Kibana dashboard on [localhost:5601](http://localhost:5601) and under **Discover** tab, create a new index pattern `gateway` to fetch the data from Elasticsearch. Once configured, navigate back to the **Discover** tab and you should see a log generated, similar to the following:

```
{
  "_index": "gateway",
  "_type": "logs",
  "_id": "CE-JL5QBOkdYRG7kEjTJ",
  "_version": 1,
  "_score": 1,
  "_source": {
    "request": {
      "headers": {
        "host": "127.0.0.1:9080",
        "accept": "*/*",
        "user-agent": "curl/8.6.0"
      },
      "size": 85,
      "querystring": {},
      "method": "GET",
      "url": "http://127.0.0.1:9080/anything",
      "uri": "/anything"
    },
    "response": {
      "headers": {
        "content-type": "application/json",
        "access-control-allow-credentials": "true",
        "server": "APISIX/3.13.0",
        "content-length": "390",
        "access-control-allow-origin": "*",
        "connection": "close",
        "date": "Mon, 13 Jan 2025 10:18:14 GMT"
      },
      "status": 200,
      "size": 618
    },
    "route_id": "elasticsearch-logger-route",
    "latency": 585.00003814697,
    "apisix_latency": 18.000038146973,
    "upstream_latency": 567,
    "upstream": "50.19.58.113:80",
    "server": {
      "hostname": "0b9a772e68f8",
      "version": "3.13.0"
    },
    "service_id": "",
    "client_ip": "192.168.65.1"
  },
  "fields": {
    ...
  }
}
```

### Customize Log Format With Plugin Metadata[â](#customize-log-format-with-plugin-metadata "Direct link to Customize Log Format With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

First, create a route with `elasticsearch-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "elasticsearch-logger-route",
    "uri": "/anything",
    "plugins": {
      "elasticsearch-logger": {
        "endpoint_addrs": ["http://elasticsearch:9200"],
        "field": {
          "index": "gateway",
          "type": "logs"
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

Next, configure the plugin metadata for `elasticsearch-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/elasticsearch-logger" -X PUT \
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
curl -i "http://127.0.0.1:9080/anything" -H "env: dev"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the Kibana dashboard on [localhost:5601](http://localhost:5601) and under **Discover** tab, create a new index pattern `gateway` to fetch the data from Elasticsearch, if you have not done so already. Once configured, navigate back to the **Discover** tab and you should see a log generated, similar to the following:

```
{
  "_index": "gateway",
  "_type": "logs",
  "_id": "Ck-WL5QBOkdYRG7kODS0",
  "_version": 1,
  "_score": 1,
  "_source": {
    "client_ip": "192.168.65.1",
    "route_id": "elasticsearch-logger-route",
    "@timestamp": "2025-01-06T10:32:36+00:00",
    "host": "127.0.0.1",
    "resp_content_type": "application/json"
  },
  "fields": {
    ...
  }
}
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with `elasticsearch-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "elasticsearch-logger": {
        "endpoint_addrs": ["http://elasticsearch:9200"],
        "field": {
          "index": "gateway",
          "type": "logs"
        },
        "include_req_body": true,
        "include_req_body_expr": [["arg_log_body", "==", "yes"]]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    },
  "uri": "/anything",
  "id": "elasticsearch-logger-route"
}'
```

â¶ `include_req_body`: set to true to include request body.

â· `include_req_body_expr`: only include request body if the URL query string `log_body` is `true`.

Send a request to the route with an URL query string satisfying the condition:

```
curl -i "http://127.0.0.1:9080/anything?log_body=yes" -X POST -d '{"env": "dev"}'
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the Kibana dashboard on [localhost:5601](http://localhost:5601) and under **Discover** tab, create a new index pattern `gateway` to fetch the data from Elasticsearch, if you have not done so already. Once configured, navigate back to the **Discover** tab and you should see a log generated, similar to the following:

```
{
  "_index": "gateway",
  "_type": "logs",
  "_id": "Dk-cL5QBOkdYRG7k7DSW",
  "_version": 1,
  "_score": 1,
  "_source": {
    "request": {
      "headers": {
        "user-agent": "curl/8.6.0",
        "accept": "*/*",
        "content-length": "14",
        "host": "127.0.0.1:9080",
        "content-type": "application/x-www-form-urlencoded"
      },
      "size": 182,
      "querystring": {
        "log_body": "yes"
      },
      "body": "{\"env\": \"dev\"}",
      "method": "POST",
      "url": "http://127.0.0.1:9080/anything?log_body=yes",
      "uri": "/anything?log_body=yes"
    },
    "start_time": 1735965595203,
    "response": {
      "headers": {
        "content-type": "application/json",
        "server": "APISIX/3.13.0",
        "access-control-allow-credentials": "true",
        "content-length": "548",
        "access-control-allow-origin": "*",
        "connection": "close",
        "date": "Mon, 13 Jan 2025 11:02:32 GMT"
      },
      "status": 200,
      "size": 776
    },
    "route_id": "elasticsearch-logger-route",
    "latency": 703.9999961853,
    "apisix_latency": 34.999996185303,
    "upstream_latency": 669,
    "upstream": "34.197.122.172:80",
    "server": {
      "hostname": "0b9a772e68f8",
      "version": "3.13.0"
    },
    "service_id": "",
    "client_ip": "192.168.65.1"
  },
  "fields": {
    ...
  }
}
```

Send a request to the route without any URL query string:

```
curl -i "http://127.0.0.1:9080/anything" -X POST -d '{"env": "dev"}'
```

Navigate to the Kibana dashboard **Discover** tab and you should see a log generated, but without the request body:

```
{
  "_index": "gateway",
  "_type": "logs",
  "_id": "EU-eL5QBOkdYRG7kUDST",
  "_version": 1,
  "_score": 1,
  "_source": {
    "request": {
      "headers": {
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "content-length": "14",
        "host": "127.0.0.1:9080",
        "user-agent": "curl/8.6.0"
      },
      "size": 169,
      "querystring": {},
      "method": "POST",
      "url": "http://127.0.0.1:9080/anything",
      "uri": "/anything"
    },
    "start_time": 1735965686363,
    "response": {
      "headers": {
        "content-type": "application/json",
        "access-control-allow-credentials": "true",
        "server": "APISIX/3.13.0",
        "content-length": "510",
        "access-control-allow-origin": "*",
        "connection": "close",
        "date": "Mon, 13 Jan 2025 11:15:54 GMT"
      },
      "status": 200,
      "size": 738
    },
    "route_id": "elasticsearch-logger-route",
    "latency": 680.99999427795,
    "apisix_latency": 4.9999942779541,
    "upstream_latency": 676,
    "upstream": "34.197.122.172:80",
    "server": {
      "hostname": "0b9a772e68f8",
      "version": "3.13.0"
    },
    "service_id": "",
    "client_ip": "192.168.65.1"
  },
  "fields": {
    ...
  }
}
```

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "elasticsearch-logger": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```

### Include Request Date in Elasticsearch Index[â](#include-request-date-in-elasticsearch-index "Direct link to Include Request Date in Elasticsearch Index")

The following example demonstrates how you can configure the `elasticsearch-logger` plugin to include the request date in Elasticsearch index.

Create a route with `elasticsearch-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "elasticsearch-logger-route",
    "uri": "/anything",
    "plugins": {
      "elasticsearch-logger": {
        "endpoint_addrs": ["http://elasticsearch:9200"],
        "field": {
          "index": "api7-{%Y.%m.%d}",
          "type": "logs"
        }
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

â¶ Configure the endpoint address to Elasticsearch.

â· Configure the `index` field to use the current year, month, and date.

â¸ Configure the `type` field as `logs`.

Send a request to the route to generate a log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the Kibana dashboard on [localhost:5601](http://localhost:5601) and under **Discover** tab, create a new index pattern `api7*` to fetch the data from Elasticsearch. Once configured, navigate back to the **Discover** tab and you should see a log generated, similar to the following:

```
{
  "_index": "api7-2025.3.10",
  "_type": "logs",
  "_id": "CE-KL5QB0kdYRG7dEiTJ",
  "_version": 1,
  "_score": 1,
  "_source": {
    "request": {
      ...
    },
    "response": {
      ...
    },
    "status": 200,
    "size": 618
  },
  ...
}
```
