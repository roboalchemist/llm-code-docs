# Source: https://docs.api7.ai/hub/google-cloud-logging.md

# google-cloud-logging

The `google-cloud-logging` plugin pushes request and response logs in batches to [Google Cloud Logging Service](https://cloud.google.com/logging?hl=en) and supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `google-cloud-logging` plugin for different scenarios.

To follow along with the examples, you should have a GCP account with active billing. You should also first obtain authentication credentials in GCP by completing the following steps:

* Visit **IAM & Admin** to create a service account.
* Assign the service account with the **Logs Writer** role, which assigns the account with `logging.logEntries.create` and `logging.logEntries.route` permissions.
* Create a private key for the service account and download the credentials in JSON format.

The credentials JSON file content should look similar to the following:

```
{
  "type": "service_account",
  "project_id": "api7ai-docs",
  "private_key_id": "[REDACTED-EXAMPLE-ID]",
  "private_key": "-----BEGIN PRIVATE KEY-----
[REDACTED-EXAMPLE-KEY]
-----END PRIVATE KEY-----
",
  "client_email": "api7-docs-log@api7ai-docs.iam.gserviceaccount.com",
  "client_id": "[REDACTED-EXAMPLE-CLIENT-ID]",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/api7-docs-log%40api7ai-docs.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

### Configure Authentication Using `auth_config`[â](#configure-authentication-using-auth_config "Direct link to configure-authentication-using-auth_config")

The following example demonstrates how you can configure the `google-cloud-logging` plugin on a route, which logs client requests and responses, as well as pushing logs to Google Cloud Logging. You will be using the `auth_config` option to configure GCP authentication details.

Create a route with `google-cloud-logging` as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "google-cloud-logging-route",
    "uri": "/anything",
    "plugins": {
      "google-cloud-logging": {
        "auth_config": {
          "client_email": "api7-docs-logging@api7ai-docs.iam.gserviceaccount.com",
          "project_id": "api7ai-docs",
          "private_key": "-----BEGIN PRIVATE KEY-----
[REDACTED-EXAMPLE-KEY]
-----END PRIVATE KEY-----
",
          "token_uri": "https://oauth2.googleapis.com/token"
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

â¶ Replace with your service account.

â· Replace with your project ID.

â¸ Replace with your private key.

â¹ Replace with your token URI.

Send a request to the route to generate a log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to Google Cloud Logs Explorer, you should see a log entry corresponding to your request, similar to the following:

```
{
  "insertId": "5400340ea330b35f2d557da2cbb9e88d",
  "jsonPayload": {
    "service_id": "",
    "route_id": "google-cloud-logging-route"
  },
  "httpRequest": {
    "requestMethod": "GET",
    "requestUrl": "http://127.0.0.1:9080/anything",
    "requestSize": "85",
    "status": 200,
    "responseSize": "615",
    "userAgent": "curl/8.6.0",
    "remoteIp": "192.168.107.1",
    "serverIp": "54.86.137.185:80",
    "latency": "1.083s"
  },
  "resource": {
    "type": "global",
    "labels": {
      "project_id": "api7ai-docs"
    }
  },
  "timestamp": "2025-02-07T07:39:51.859Z",
  "labels": {
    "source": "apache-apisix-google-cloud-logging"
  },
  "logName": "projects/api7ai-docs/logs/apisix.apache.org%2Flogs",
  "receiveTimestamp": "2025-02-07T07:39:58.012811475Z"
}
```

### Configure Authentication Using `auth_file`[â](#configure-authentication-using-auth_file "Direct link to configure-authentication-using-auth_file")

The following example demonstrates how you can configure the `google-cloud-logging` plugin on a route, which logs client requests and responses, as well as pushing logs to Google Cloud Logging. You will be using the `auth_file` option to configure GCP authentication details.

Copy the previously downloaded GCP service account credentials JSON file to a location accessible for APISIX. If you are running APISIX in Docker, you should copy the file into the container, for instance, to `/usr/local/apisix/conf/gcp-logging-auth.json`.

Create a route with `google-cloud-logging` as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "google-cloud-logging-route",
    "uri": "/anything",
    "plugins": {
      "google-cloud-logging": {
        "auth_file": "/usr/local/apisix/conf/gcp-logging-auth.json"
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

â¶ Replace with your GCP service account credentials JSON file path.

Send a request to the route to generate a log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to Google Cloud Logs Explorer, you should see a log entry corresponding to your request, similar to the following:

```
{
  "insertId": "5400340ea330b35f2d557da2cbb9e88d",
  "jsonPayload": {
    "service_id": "",
    "route_id": "google-cloud-logging-route"
  },
  "httpRequest": {
    "requestMethod": "GET",
    "requestUrl": "http://127.0.0.1:9080/anything",
    "requestSize": "85",
    "status": 200,
    "responseSize": "615",
    "userAgent": "curl/8.6.0",
    "remoteIp": "192.168.107.1",
    "serverIp": "54.86.137.185:80",
    "latency": "1.083s"
  },
  "resource": {
    "type": "global",
    "labels": {
      "project_id": "api7ai-docs"
    }
  },
  "timestamp": "2025-02-07T08:25:11.325Z",
  "labels": {
    "source": "apache-apisix-google-cloud-logging"
  },
  "logName": "projects/api7ai-docs/logs/apisix.apache.org%2Flogs",
  "receiveTimestamp": "2025-02-07T08:25:11.423190575Z"
}
```

### Customize Log Format With Plugin Metadata[â](#customize-log-format-with-plugin-metadata "Direct link to Customize Log Format With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

First, create a route with `google-cloud-logging` as such, and replace with your credentials:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "google-cloud-logging-route",
    "uri": "/anything",
    "plugins": {
      "google-cloud-logging": {
        "auth_config": {
          "client_email": "api7-docs-logging@api7ai-docs.iam.gserviceaccount.com",
          "project_id": "api7ai-docs",
          "private_key": "-----BEGIN PRIVATE KEY-----
[REDACTED-EXAMPLE-KEY]
-----END PRIVATE KEY-----
",
          "token_uri": "https://oauth2.googleapis.com/token"
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

Next, configure the plugin metadata for `google-cloud-logging`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/google-cloud-logging" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "log_format": {
      "host": "$host",
      "@timestamp": "$time_iso8601",
      "client_ip": "$remote_addr",
    }
  }'
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to Google Cloud Logs Explorer, you should see a log entry corresponding to your request, similar to the following:

```
{
  "@timestamp":"2025-02-07T09:10:42+00:00",
  "client_ip":"192.168.107.1",
  "host":"127.0.0.1",
  "route_id":"google-cloud-logging-route"
}
```

The log format configured in plugin metadata is effective for all instances of `google-cloud-logging` if the log format is not specifically specified on the individual instance.

If you specifically configure the log format in the `google-cloud-logging` plugin on the route:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/google-cloud-logging-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "google-cloud-logging": {
        "log_format": {
          "host": "$host",
          "@timestamp": "$time_iso8601",
          "client_ip": "$remote_addr",
          "env": "$http_env",
          "resp_content_type": "$sent_http_Content_Type"
        }
      }
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

Navigate to Google Cloud Logs Explorer, you should see a log entry corresponding to your request, similar to the following:

```
{
  "@timestamp":"2025-02-07T09:38:55+00:00",
  "client_ip":"192.168.107.1",
  "host":"127.0.0.1",
  "env":"dev",
  "resp_content_type":"application/json",
  "route_id":"google-cloud-logging-route"
}
```

The configuration of log format on the route has taken precedence over the log format configured on the `google-cloud-logging` plugin metadata.
