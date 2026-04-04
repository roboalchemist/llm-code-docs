# Source: https://docs.api7.ai/hub/splunk-hec-logging.md

# splunk-hec-logging

The `splunk-hec-logging` plugin serializes request and response context information to [Splunk Event Data format](https://docs.splunk.com/Documentation/Splunk/latest/Data/FormateventsforHTTPEventCollector#Event_metadata) and push to your [Splunk HTTP Event Collector (HEC)](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) in batches. The plugin also supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `splunk-hec-logging` plugin for different scenarios.

To follow along the examples, please complete the following steps to set up Splunk:

* Install [Splunk](https://www.splunk.com/en_us/download.html). Splunk Web should be running at `localhost:8000` by default.
* See [set up and use HTTP Event Collector in Splunk Web](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) to set up an HTTP Event Collector.
* Navigate to **Settings > Data Inputs** at the upper-right corner of the console. You should see at least one input for the HTTP Event Collector. Note down the token value.
* Navigate to **Settings > Data Inputs** at the upper-right corner of the console and select **HTTP Event Collector**. In **Global Settings**, enable all tokens.
* In **Global Settings**, you should also find the collector's default port to be `8088`.

To verify the setup, execute the following command with your token:

```
curl "http://localhost:8088/services/collector/event" \ 
  -H "Authorization: Splunk <replace-with-your-token>" \
  -d '{"event": "hello world"}'
```

You should see a `success` response.

### Push Log to Splunk[â](#push-log-to-splunk "Direct link to Push Log to Splunk")

The following example demonstrates how you can enable the `splunk-hec-logging` plugin on a route, which logs client requests and pushes logs to Splunk.

Create a route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "splunk-route",
    "uri": "/anything",
    "plugins": {
      "splunk-hec-logging":{
        "endpoint":{
          "uri":"http://192.168.2.108:8088/services/collector/event",
          "token":"26b15ddd-31db-455b-ak0c-9b5be3decc4a"
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

â¶ Configure to the Splunk HTTP collector's endpoint. Replace with your IP address.

â· Replace with your collector's token.

Send a few requests to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` responses.

Navigate to Splunk Web and select **Search & Reporting** in the left menu. In the search box, enter `source="apache-apisix-splunk-hec-logging"` and search for events from APISIX. You should see events corresponding to your requests, such as the following:

```
{
  "response_size": 617,
  "response_headers": {
    "server": "APISIX/3.10.0",
    "connection": "close",
    "content-type": "application/json",
    "access-control-allow-credentials": "true",
    "access-control-allow-origin": "*",
    "date": "Wed, 27 Nov 2024 19:49:27 GMT",
    "content-length": "389"
  },
  "request_headers": {
    "host": "127.0.0.1:9080",
    "user-agent": "curl/8.6.0",
    "accept": "*/*"
  },
  "request_query": {},
  "request_url": "http://127.0.0.1:9080/anything",
  "upstream": "18.208.8.205:80",
  "latency": 746.00005149841,
  "request_method": "GET",
  "request_size": 85,
  "response_status": 200
}
```

### Log Request and Response Headers With Plugin Metadata[â](#log-request-and-response-headers-with-plugin-metadata "Direct link to Log Request and Response Headers With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

Create a route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "splunk-route",
    "uri": "/anything",
    "plugins": {
      "splunk-hec-logging":{
        "endpoint":{
          "uri":"http://192.168.2.108:8088/services/collector/event",
          "token":"26b15ddd-31db-455b-ak0c-9b5be3decc4a"
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

â¶ Configure to the Splunk HTTP collector's endpoint. Replace with your IP address.

â· Replace with your collector's token.

Configure the plugin metadata for `splunk-hec-logging`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/splunk-hec-logging" -X PUT \
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

Navigate to Splunk Web and select **Search & Reporting** in the left menu. In the search box, enter `source="apache-apisix-splunk-hec-logging"` and search for events. You should see the latest event correspond to your request, similar to the following:

```
{
  "host":"127.0.0.1",
  "env":"dev",
  "client_ip":"192.168.65.1",
  "@timestamp":"2024-11-27T20:59:28+00:00",
  "route_id":"splunk-route",
  "resp_content_type":"application/json"
}
```
