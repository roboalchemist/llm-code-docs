# Source: https://docs.api7.ai/hub/error-log-logger.md

# error-log-logger

The `error-log-logger` plugin pushes APISIX's error logs (`error.log`) to TCP, Apache SkyWalking, Apache Kafka, or ClickHouse servers, in batches. You can specify the severity level of which the plugin should send the corresponding logs.

The plugin is disabled by default. Once enabled, it will automatically start pushing error logs to remote servers. You should configure remote server details in [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) only, instead of on other resources, such as routes.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `error-log-logger` plugin for different scenarios.

If you are using API7 Enterprise, the plugin is enabled by default. If you are using APISIX, the `error-log-logger` plugin is disabled by default. To enable the plugin, add the plugin to your [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as such:

config.yaml

```
plugins:
  - ...
  - error-log-logger
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

### Send Logs to TCP Server[â](#send-logs-to-tcp-server "Direct link to Send Logs to TCP Server")

The following example demonstrates how you can configure the `error-log-logger` plugin to send error logs to a TCP server.

Start a netcat listener on port `19000` as the example TCP server:

```
nc -l 19000
```

Configure the plugin metadata for `error-log-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/error-log-logger" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "tcp": {
      "host": "192.168.2.103",
      "port": 19000
    },
    "level": "INFO"
  }'
```

â¶ Replace with your internal IP address.

â· Configure the port to your TCP server listening port.

â¸ Configure the severity level to `INFO` so most logs would be sent, for easier verification.

To verify, you can manually generate a log at `warn` level by [reloading APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload).

In terminal session where netcat is listening, you should see a log entry similar to the following:

```
2025/01/26 20:15:29 [warn] 211#211: *35552 [lua] plugin.lua:205: load(): new plugins: {"cas-auth":true,"real-ip":true,"ai":true,"client-control":true,"proxy-control":true,"request-id":true,"zipkin":true,"ext-plugin-pre-req":true,"fault-injection":true,"mocking":true,"serverless-pre-function":true,"cors":true,"ip-restriction":true,"ua-restriction":true,"referer-restriction":true,"csrf":true,"uri-blocker":true,"request-validation":true,"chaitin-waf":true,"multi-auth":true,"openid-connect":true,"authz-casbin":true,"authz-casdoor":true,"wolf-rbac":true,"ldap-auth":true,"hmac-auth":true,"basic-auth":true,"jwt-auth":true,"redirect":true,"key-auth":true,"consumer-restriction":true,"attach-consumer-label":true,"authz-keycloak":true,"proxy-cache":true,"body-transformer":true,"ai-prompt-template":true,"ai-prompt-decorator":true,"proxy-mirror":true,"proxy-rewrite":true,"workflow":true,"api-breaker":true,"ai-proxy":true,"limit-conn":true,"limit-count":true,"limit-req":true,"gzip":true,"server-info":true,"traffic-split":true,"response-rewrite":true,"degraphql":true,"kafka-proxy":true,"grpc-transcode":true,"grpc-web":true,"http-dubbo":true,"public-api":true,"prometheus":true,"datadog":true,"loki-logger":true,"elasticsearch-logger":true,"echo":true,"loggly":true,"http-logger":true,"splunk-hec-logging":true,"skywalking-logger":true,"google-cloud-logging":true,"sls-logger":true,"tcp-logger":true,"kafka-logger":true,"rocketmq-logger":true,"syslog":true,"udp-logger":true,"file-logger":true,"clickhouse-logger":true,"tencent-cloud-cls":true,"inspect":true,"example-plugin":true,"aws-lambda":true,"azure-functions":true,"openwhisk":true,"openfunction":true,"error-log-logger":true,"ext-plugin-post-req":true,"ext-plugin-post-resp":true,"serverless-post-function":true,"opa":true,"forward-auth":true,"jwe-decrypt":true}, context: init_worker_by_lua*
```

### Send Logs to SkyWalking[â](#send-logs-to-skywalking "Direct link to Send Logs to SkyWalking")

The following example demonstrates how you can configure the `error-log-logger` plugin to send error logs to SkyWalking.

Start a SkyWalking storage, OAP and Booster UI with Docker Compose, following [Skywalking's documentation](https://skywalking.apache.org/docs/main/next/en/setup/backend/backend-docker/). Once set up, the OAP server should be listening on `12800` and you should be able to access the UI at <http://localhost:8080>.

Configure the plugin metadata for `error-log-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/error-log-logger" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "skywalking": {
      "endpoint_addr": "http://192.168.2.103:12800/v3/logs"
    },
    "level": "INFO"
  }'
```

â¶ Replace with your SkyWalking server address.

â· Configure the severity level to `INFO` so most logs would be sent, for easier verification.

To verify, you can manually generate a log at `warn` level by [reloading APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload).

In [Skywalking UI](http://localhost:8080), navigate to **General Service** > **Services**. You should see a service called `APISIX` with the following log entry:

```
2025/01/27 07:40:06 [warn] 211#211: *35552 [lua] plugin.lua:205: load(): new plugins: {"cas-auth":true,"real-ip":true,"ai":true,"client-control":true,"proxy-control":true,"request-id":true,"zipkin":true,"ext-plugin-pre-req":true,"fault-injection":true,"mocking":true,"serverless-pre-function":true,"cors":true,"ip-restriction":true,"ua-restriction":true,"referer-restriction":true,"csrf":true,"uri-blocker":true,"request-validation":true,"chaitin-waf":true,"multi-auth":true,"openid-connect":true,"authz-casbin":true,"authz-casdoor":true,"wolf-rbac":true,"ldap-auth":true,"hmac-auth":true,"basic-auth":true,"jwt-auth":true,"redirect":true,"key-auth":true,"consumer-restriction":true,"attach-consumer-label":true,"authz-keycloak":true,"proxy-cache":true,"body-transformer":true,"ai-prompt-template":true,"ai-prompt-decorator":true,"proxy-mirror":true,"proxy-rewrite":true,"workflow":true,"api-breaker":true,"ai-proxy":true,"limit-conn":true,"limit-count":true,"limit-req":true,"gzip":true,"server-info":true,"traffic-split":true,"response-rewrite":true,"degraphql":true,"kafka-proxy":true,"grpc-transcode":true,"grpc-web":true,"http-dubbo":true,"public-api":true,"prometheus":true,"datadog":true,"loki-logger":true,"elasticsearch-logger":true,"echo":true,"loggly":true,"http-logger":true,"splunk-hec-logging":true,"skywalking-logger":true,"google-cloud-logging":true,"sls-logger":true,"tcp-logger":true,"kafka-logger":true,"rocketmq-logger":true,"syslog":true,"udp-logger":true,"file-logger":true,"clickhouse-logger":true,"tencent-cloud-cls":true,"inspect":true,"example-plugin":true,"aws-lambda":true,"azure-functions":true,"openwhisk":true,"openfunction":true,"error-log-logger":true,"ext-plugin-post-req":true,"ext-plugin-post-resp":true,"serverless-post-function":true,"opa":true,"forward-auth":true,"jwe-decrypt":true}, context: init_worker_by_lua*
```

You should also observe logs at other severity levels, such as `error`, `emerg`, and `info`, when they are generated.

### Send Logs to ClickHouse[â](#send-logs-to-clickhouse "Direct link to Send Logs to ClickHouse")

The following example demonstrates how you can configure the `error-log-logger` plugin to send error logs to ClickHouse.

Start a sample ClickHouse server with user `default` and empty password:

```
docker run -d -p 8123:8123 -p 9000:9000 -p 9009:9009 --name clickhouse-server clickhouse/clickhouse-server
```

In ClickHouse database `default`, create a table named `default_logs` with a `data` column. Note that the `data` column is expected by the plugin to push logs to.

```
curl "http://127.0.0.1:8123" -X POST -d '
  CREATE TABLE default.default_logs (
    data String,
    PRIMARY KEY(`data`)
  )
  ENGINE = MergeTree()
' --user default:
```

Configure the plugin metadata for `error-log-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/error-log-logger" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "clickhouse": {
      "endpoint_addr": "http://192.168.2.103:8123",
      "user": "default",
      "password": "",
      "database": "default",
      "logtable": "default_logs"
    },
    "level": "INFO"
  }'
```

â¶ Replace with your ClickHouse server address.

â· Set the username to `default`.

â¸ Set the password to empty.

â¹ Set the database to `default`.

âº Set the database table to `default_logs`.

â» Configure the severity level to `INFO` so most logs would be sent, for easier verification.

To verify, you can manually generate a log at `warn` level by [reloading APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload).

Send a request to ClickHouse to see the log entries:

```
echo 'SELECT * FROM default.default_logs FORMAT Pretty' | curl "http://127.0.0.1:8123/?" -d @-
```

You should see a log entry similar to the following:

```
2025/01/27 08:21:13 [warn] 353#353: *106572 [lua] plugin.lua:205: load(): new plugins: {"client-control":true,"proxy-control":true,"request-id":true,"zipkin":true,"ext-plugin-pre-req":true,"fault-injection":true,"mocking":true,"serverless-pre-function":true,"cors":true,"ip-restriction":true,"ua-restriction":true,"referer-restriction":true,"csrf":true,"uri-blocker":true,"request-validation":true,"chaitin-waf":true,"multi-auth":true,"openid-connect":true,"authz-casbin":true,"authz-casdoor":true,"wolf-rbac":true,"ldap-auth":true,"hmac-auth":true,"basic-auth":true,"jwt-auth":true,"jwe-decrypt":true,"key-auth":true,"consumer-restriction":true,"attach-consumer-label":true,"forward-auth":true,"opa":true,"authz-keycloak":true,"proxy-cache":true,"body-transformer":true,"ai-prompt-template":true,"ai-prompt-decorator":true,"proxy-mirror":true,"proxy-rewrite":true,"workflow":true,"api-breaker":true,"ai-proxy":true,"limit-conn":true,"limit-count":true,"limit-req":true,"gzip":true,"server-info":true,"traffic-split":true,"response-rewrite":true,"degraphql":true,"kafka-proxy":true,"grpc-transcode":true,"grpc-web":true,"http-dubbo":true,"public-api":true,"error-log-logger":true,"google-cloud-logging":true,"sls-logger":true,"tcp-logger":true,"kafka-logger":true,"rocketmq-logger":true,"syslog":true,"udp-logger":true,"file-logger":true,"clickhouse-logger":true,"tencent-cloud-cls":true,"inspect":true,"example-plugin":true,"aws-lambda":true,"azure-functions":true,"openwhisk":true,"openfunction":true,"serverless-post-function":true,"ext-plugin-post-req":true,"ext-plugin-post-resp":true,"redirect":true,"skywalking-logger":true,"splunk-hec-logging":true,"http-logger":true,"loggly":true,"echo":true,"elasticsearch-logger":true,"cas-auth":true,"prometheus":true,"datadog":true,"loki-logger":true,"real-ip":true,"ai":true}, context: init_worker_by_lua* â
```
