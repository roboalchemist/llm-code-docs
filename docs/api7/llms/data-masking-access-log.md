# Source: https://docs.api7.ai/enterprise/best-practices/data-masking-access-log.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/data-masking-access-log.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/data-masking-access-log.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/data-masking-access-log.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/data-masking-access-log.md

# Mask Sensitive Data in Access Log

When deploying an API gateway in containerized environments like Kubernetes, access logs are often written directly to the containerâs standard output. These logs are then captured by the container runtime or a log collection tool and can be forwarded to a centralized logging system.

However, these logs may contain sensitive information, such as email addresses or access tokens, which could present privacy and security risks if stored or transmitted without proper processing. To mitigate this, it is essential to desensitize sensitive data during the logging process.

This guide will walk you through the process of masking an email address in the gateway's access log, by redefining a new log variable and applying it in `access_log_format` through NGINX's `map` module.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.5.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.5.x/getting-started/add-gateway-instance.md) in your gateway group.

## Update Gateway Configuration[â](#update-gateway-configuration "Direct link to Update Gateway Configuration")

In this section, you will mask the email address in the `request_uri` by replacing its value with `xxxxxx` while keeping the rest of the URI intact, to protect sensitive information in the logs.

Add the `http_configuration_snippet` configuration below to the `nginx_config` configuration in the gateway's [configuration file](https://docs.api7.ai/enterprise/3.5.x/reference/configuration.md), to evaluate the `request_uri` and map it to the new variable `masked_uri` based on the pattern matching inside the `map` block:

config.yaml

```
nginx_config:
  http_configuration_snippet: |
    map $request_uri $masked_uri {
      ~^(.*?email=)[^&\s]+(.*)$ $1xxxxxx$2;
      default $request_uri;
    }
```

Update the `access_log_format` configuration under `nginx_config` in the gateway's [configuration file](https://docs.api7.ai/enterprise/3.5.x/reference/configuration.md) and use the new variable `masked_uri` to log request URI:

config.yaml

```
nginx_config:
  http:
    access_log_format: '$masked_uri $remote_addr - $remote_user [$time_local] $status $body_bytes_sent $request_time "$http_referer" "$http_user_agent" $upstream_addr $upstream_status $upstream_response_time "$upstream_scheme://$upstream_host$upstream_uri"'
```

Reload API7 Gateway for configuration changes to take effect.

## Verify[â](#verify "Direct link to Verify")

You may use any existing route for verification. If the gateway does not have a route yet, [create a route](https://docs.api7.ai/enterprise/3.5.x/getting-started/launch-your-first-api.md) for verification.

Send a request to the route with an email address in the query parameter:

```
curl -i "http://127.0.0.1:9080/get?email=test@gmail.com&user=123"
```

Navigate to the API7 Gateway access log, you should see a log entry similar to the following, where the email address has been masked:

```
2025-02-19 11:48:21 /get?email=xxxxxx&user=123 172.17.0.1 - - [19/Feb/2025:03:48:18 +0000] 200 562 0.004 "-" "curl/8.7.1" 192.168.10.101:3030
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

If you would like to mask sensitive data in request headers, request bodies, and URL queries, see [`data-mask`](https://docs.api7.ai/hub/data-mask.md) plugin.
