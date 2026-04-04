# Source: https://docs.api7.ai/enterprise/api-observability/log-consumer-label-in-access-log.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-observability/log-consumer-label-in-access-log.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-observability/log-consumer-label-in-access-log.md

# Source: https://docs.api7.ai/apisix/how-to-guide/observability/log-consumer-label-in-access-log.md

# Log Consumer Label in Access Log

Logging consumer labels in APISIXâs access log allows for more visibility and control over API traffic. By capturing consumer labels, organizations can easily identify which clients are accessing specific routes, track usage patterns, and enforce security policies based on these labels.

This guide will show you how to log consumer labels in the gateway's access log.

note

Ingress Controller currently does not support configuring consumer labels.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker.

## Create and Use the New Variable in Access Log[â](#create-and-use-the-new-variable-in-access-log "Direct link to Create and Use the New Variable in Access Log")

In the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample), initialize a custom variable for the consumer label and assign it a default value `-`. In this example, you will initialize a variable called `$consumer_company`, but you could always initialize more as needed:

conf/config.yaml

```
nginx_config:
  http_server_location_configuration_snippet: |
    set $consumer_company "-";
```

In the same file, update the access log format to include the newly initialized variable:

conf/config.yaml

```
nginx_config:
  http:
    access_log_format: >-
      $remote_addr - $remote_user [$time_local] $http_host \"$request\" $status $body_bytes_sent $request_time \"$http_referer\" \"$http_user_agent\" $upstream_addr $upstream_status $upstream_response_time \"$upstream_scheme://$upstream_host$upstream_uri\" "$consumer_company"
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

## Assign Value to the New Variable[â](#assign-value-to-the-new-variable "Direct link to Assign Value to the New Variable")

Use [serverless functions](https://docs.api7.ai/hub/serverless-functions.md) to assign consumer label value to the new variable.

For instance, configure the serverless plugin as a global plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/global_rules" -X PUT -d '
{
  "id": "serverless-consumer-label",
  "plugins": {
    "serverless-pre-function": {
      "phase": "log",
      "functions": [
        "return function (conf, ctx) ngx.var.consumer_company = ctx.consumer and ctx.consumer.labels and ctx.consumer.labels[\"company\"] or \"unknown\" end"
      ]
    }
  }
}'
```

The function obtains the consumer label `company` value and assigns it to the `consumer_company` variable. If the consumer does not have a `company` label, the `consumer_company` variable value will be assigned `unknown`.

## Configure Consumer and Authentication[â](#configure-consumer-and-authentication "Direct link to Configure Consumer and Authentication")

Create a consumer `john` with a custom label `company`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "john",
  "labels": {
    "company": "smart-technology"
  }
}'
```

Create `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT -d '
{
  "id": "cred-john-key-auth",
  "plugins": {
    "key-auth": {
      "key": "john-key"
    }
  }
}'
```

Create a route and enable `key-auth` on the route:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "key-auth-route",
  "uri": "/anything",
  "plugins": {
    "key-auth": {}
  },
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

## Verify[â](#verify "Direct link to Verify")

Send a request to the route with the valid key:

```
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: john-key'
```

You should receive an `HTTP/1.1 200 OK` response and see the following in the access log, where the company name is logged as `smart-technology`:

```
192.168.107.1 - - [18/Mar/2025:09:17:28 +0000] 127.0.0.1:9080 "GET /anything HTTP/1.1" 200 508 1.260 "-" "curl/8.6.0" 13.210.43.76:80 200 1.153 "http://127.0.0.1:9080" "smart-technology"
```

Send a request to the route without the key:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see an `HTTP/1.1 401 Unauthorized` response and see the following in the access log, where the company name is logged as `unknown`:

```
192.168.107.1 - - [18/Mar/2025:09:18:27 +0000] 127.0.0.1:9080 "GET /anything HTTP/1.1" 401 52 0.000 "-" "curl/8.6.0" - - - "http://127.0.0.1:9080" "unknown"
```
