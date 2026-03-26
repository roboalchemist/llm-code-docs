# Source: https://docs.api7.ai/apisix/how-to-guide/observability/log-with-clickhouse.md

# Log with ClickHouse

APISIX supports collecting route access information and recording it as logs, such as host, client IP, and request timestamp. This key information will be of great help in troubleshooting related problems.

[ClickHouse](https://clickhouse.com/) is an open-source column-oriented database management system (DBMS) for online analytical processing (OLAP). It allows users to generate analytical reports such as log analytics using SQL queries in real-time.

This guide will show you how to enable the `clickhouse-logger` plugin to record the APISIX logs into ClickHouse databases.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Configure ClickHouse[â](#configure-clickhouse "Direct link to Configure ClickHouse")

Start a ClickHouse instance named `quickstart-clickhouse-server` with a default database `quickstart_db`, a default user `quickstart-user` and password `quickstart-pass`:

```
docker run -d \
  --name quickstart-clickhouse-server \
  --network=apisix-quickstart-net \
  -e CLICKHOUSE_DB=quickstart_db \
  -e CLICKHOUSE_USER=quickstart-user \
  -e CLICKHOUSE_PASSWORD=quickstart-pass \
  -e CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT=1 \
  --ulimit nofile=262144:262144 \
  clickhouse/clickhouse-server
```

Connect to the ClickHouse instance using the command line tool `clickhouse-client` in Docker:

```
docker exec -it quickstart-clickhouse-server clickhouse-client
```

Create a table `test` in database `quickstart_db` with fields `host`, `client_ip`, `route_id`, `@timestamp` of `String` type, or adjust the command accordingly based on your needs:

```
CREATE TABLE quickstart_db.test (
  `host` String,
  `client_ip` String,
  `route_id` String,
  `@timestamp` String,
   PRIMARY KEY(`@timestamp`)
) ENGINE = MergeTree()
```

If successful, you should see `Ok` on the output.

Enter `exit` to exit the command line interface in Docker.

## Enable `clickhouse-logger` Plugin[â](#enable-clickhouse-logger-plugin "Direct link to enable-clickhouse-logger-plugin")

Enable the `clickhouse-logger` plugin globally. Alternatively, you can enable the plugin on a route.

* Admin API
* ADC

Enable the `clickhouse-logger` plugin globally:

```
curl -i "http://127.0.0.1:9180/apisix/admin/global_rules" -X PUT -d '
{
  "id": "clickhouse",
  "plugins": {
    "clickhouse-logger": {
      "log_format": {
        "host": "$host",
        "@timestamp": "$time_iso8601",
        "client_ip": "$remote_addr"
      },
      "user": "quickstart-user",
      "password": "quickstart-pass",
      "database": "quickstart_db",
      "logtable": "test",
      "endpoint_addrs": ["http://quickstart-clickhouse-server:8123"]
    }
  }
}'
```

â Specify fields corresponding to the ClickHouse table in the log format

â ClickHouse server information

Create a sample route on which you will collect logs:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "getting-started-ip",
  "uri": "/ip",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

Enable the `clickhouse-logger` plugin globally:

adc-global-rule.yaml

```
global_rules:
  clickhouse-logger:
    log_format:
      host: "$host"
      "@timestamp": "$time_iso8601"
      client_ip: "$remote_addr"
    user: "quickstart-user"
    password: "quickstart-pass"
    database: "quickstart_db"
    logtable: "test"
    endpoint_addrs:
      - "http://quickstart-clickhouse-server:8123"
```

â Specify fields corresponding to the ClickHouse table in the log format.

â ClickHouse server information.

Create a sample route on which you will collect logs:

adc-route.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /ip
        name: getting-started-ip
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc-global-rule.yaml -f adc-route.yaml
```

## Submit Logs in Batches[â](#submit-logs-in-batches "Direct link to Submit Logs in Batches")

The `clickhouse-logger` plugin supports using a batch processor to aggregate and process logs in batches. This avoids frequent submissions of log entries to ClickHouse, which slows down the operations.

By default, the batch processor submits data every 5 seconds or when the data size in a batch reaches 1000 KB. You can adjust the time interval of submission `inactive_timeout` and maximum batch size `batch_max_size` for the plugin. For example, this is how you can set `inactive_timeout` to 10 seconds and `batch_max_size` to 2000 KB:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/global_rules/clickhouse" -X PATCH -d '
{
  "plugins": {
    "clickhouse-logger": {
      "batch_max_size": 2000,
      "inactive_timeout": 10
    }
  }
}'
```

Update your global rule configuration to set `inactive_timeout` to 10 seconds and `batch_max_size` to 2000 KB:

adc-global-rule.yaml

```
global_rules:
  clickhouse-logger:
    log_format:
      host: "$host"
      "@timestamp": "$time_iso8601"
      client_ip: "$remote_addr"
    user: "quickstart-user"
    password: "quickstart-pass"
    database: "quickstart_db"
    logtable: "test"
    endpoint_addrs:
      - "http://quickstart-clickhouse-server:8123"
    batch_max_size: 2000
    inactive_timeout: 10
```

Synchronize the configurations to APISIX:

```
adc sync -f adc-global-rule.yaml -f adc-route.yaml
```

## Verify Logging[â](#verify-logging "Direct link to Verify Logging")

Send a request to the route to generate an access log entry:

```
curl -i "http://127.0.0.1:9080/ip"
```

Connect to the ClickHouse instance using the command line tool `clickhouse-client` in Docker:

```
docker exec -it quickstart-clickhouse-server clickhouse-client
```

Query all records in table `quickstart_db.test`:

```
SELECT * from quickstart_db.test
```

You should see an access record similar to the following, which verifies that the `clickhouse-logger` plugin works as intended.

```
   ââhostâââââââ¬âclient_ipââ¬âroute_idââ¬â@timestampâââââââââââââââââ
1. â 127.0.0.1 â 127.0.0.1 â 5e835ead â 2025-08-12T09:17:04+00:00 â
   âââââââââââââ´ââââââââââââ´âââââââââââ´ââââââââââââââââââââââââââââ
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

See [`clickhouse-logger`](https://docs.api7.ai/hub/clickhouse-logger.md) plugin doc to learn more about the plugin configuration options.
