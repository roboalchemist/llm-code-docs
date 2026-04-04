# Source: https://docs.upsun.com/increase-observability/logs/forward-logs.md

# Forward Upsun Fixed and Blackfire logs

You might use a service to analyze logs from various parts of your fleet.
You might want to consolidate all your logs in one place that everyone has access to
without needing to grant them access to each project individually.

In such cases, forward your logs from Upsun and Blackfire to a third-party service.
You can use a [service with an integration](#use-a-log-forwarding-integration)
or any service that supports a [syslog endpoint](#forward-to-a-syslog-endpoint) or [HTTP endpoint](#forward-to-an-http-endpoint).

To enable log forwarding in a project, you need to be a [project admin](https://docs.upsun.com../../administration/users.md).
For pricing information for real-time logs forwarding, refer to the **Observability and performance monitoring** section of the [Upsun pricing page](https://upsun.com/pricing/).

### Which logs are forwarded?
When log forwarding is enabled, Upsun forwards logs sent to journald.

By default, Upsun sends the following logs to journald:
- `stdout` and `stderr` logs from your application
   Note: You can configure your application to use syslog to send these (or additional) messages to journald.
- MariaDB/MySQL slow query logs
- Redis logs (all except command-level operations and low-level internals)

Logs in files are not forwarded to journald.

## Use a log forwarding integration

Certain services have a specific integration for forwarding logs.
If your third-party service isn't supported, you can forward to a [syslog endpoint](#forward-to-a-syslog-endpoint).

### Integrated third-party services

Upsun supports forwarding logs not only to custom remote syslog endpoints but also directly to a set of
popular third‑party log management and observability services. These integrations allow you to centralize logs from
applications, services, and infrastructure into your existing monitoring stack:

- **[Sumo Logic](https://www.sumologic.com/)** – Cloud-based log management and analytics.
- **[New Relic](https://newrelic.com/)** – Unified observability platform with logs and metrics.
- **[Splunk](https://www.splunk.com/)** – Searchable log platform for monitoring and operational intelligence.
- **[Datadog](https://www.datadoghq.com/)** – Observability suite with log collection and processing.
- **[Loggly](https://www.loggly.com/)** – Cloud-native log monitoring, aggregation, and alerting.
- **[LogDNA (Mezmo)](https://www.mezmo.com/)** – Centralized log management and analysis in real time.
- **[Papertrail](https://www.papertrail.com/)** – Real-time log aggregation via syslog.
- **[Logz.io](https://logz.io/)** – ELK-based log analytics and monitoring.

### Enable a log forwarding integration

#### Using the CLI

To enable log forwarding for a specific project using the [Upsun CLI](https://docs.upsun.com/administration/cli.md),
follow the steps for your selected service.

View your logs in the **Logs** dashboard.

 - In Splunk, get an Event Collector token on [Splunk Platform](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#Create_an_Event_Collector_token_on_Splunk_Cloud_Platform)
or [Splunk Enterprise](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#Create_an_Event_Collector_token_on_Splunk_Enterprise).

 - Determine your host, which is the Splunk instance that’s collecting data.

 - Choose an index name.

 - Create the integration with the following command:

```bash {}
upsun integration:add --type splunk --url https://http-inputs.<HOST>.splunkcloud.com/services/collector/event --index <INDEX> --token <TOKEN>
```

View your logs in the **Apps->Search & Reporting** dashboard.
Filter by the index name to find the relevant events.

 - In Sumo Logic, [configure an HTTP source](https://www.sumologic.com/help/docs/send-data/hosted-collectors/http-source/logs-metrics/#configure-an-httplogs-and-metrics-source).
Make sure to copy the Source Category and collector URL.

 - Create the integration with the following command:

```bash {}
upsun integration:add --type sumologic --url <COLLECTOR_URL> --category <SOURCE_CATEGORY>
```

View your logs in the **Log Search** tab.

To start forwarding logs, [trigger a redeploy](https://docs.upsun.com../../development/troubleshoot.md#force-a-redeploy).

#### In the Console

To enable log forwarding for a specific project from the Console,
follow these steps:

1. Navigate to your project.
2. Click Settings **Settings**.
3. Click **Integrations**.
4. Click **Add Integration**.
5. Select the integration you want to enable.
6. In the **Configure your integration** window,
   specify your configuration options.
7. Click **Add Integration**.
   The new integration overview is displayed,
   and you can view your logs in the **Activity** section.

## Forward to a syslog endpoint

Syslog is a standard protocol for transferring log messages.
Many third-party services offer endpoints for ingesting syslog events.
You can forward your Upsun and Blackfire logs to any of those endpoints.

``type``, ``syslog-host``, and ``syslog-port`` are the only properties required for all endpoints.
The following table shows the other available properties:

| Property | Type | Default | Description |
| ``auth-token`` | ``string`` |  | The token to authenticate with the given service. |
| ``auth-mode`` | ``string`` | ``prefix`` | The mode for authentication with the given service. Can be ``prefix`` or ``structured_data``. Defaults to ``prefix``. |
| ``facility`` | ``string`` | ``1`` (user) | A [syslog facility code](https://en.wikipedia.org/wiki/Syslog#Facility) to attach with each log to identify the source. Can be a number from 0 to 23. |
| ``message-format`` | ``string`` | ``rfc5424`` | The standard to use for the message format. Can be ``rfc5424`` or ``rfc3164``. |
| ``protocol`` | ``string`` | ``tls`` | The network protocol to use in the connection. Can be one of ``tls``, ``tcp``, or ``udp``. Defaults to ``tls``. |
| ``verify-tls`` | ``boolean`` | ``true`` | Whether to verify Transport Layer Security (TLS) certification when using the TLS protocol. |
To include a property, add it as a flag, for example ``--protocol tcp``.
This should let you connect to any service that has syslog endpoints.
To start forwarding logs, once you’ve added the service [trigger a redeploy](https://docs.upsun.com/development/troubleshoot.md#force-a-redeploy).
To enable log forwarding to a syslog endpoint for a specific project using the [Upsun CLI](https://docs.upsun.com/administration/cli.md),
follow these steps:

 - Navigate to your project.
 - Click Settings **Settings**.
 - Click **Integrations**.
 - Click **Add Integration**.
 - Select the syslog integration.
 - In the **Configure your integration** window,
specify your configuration options.
 - Click **Add Integration**.
The new integration overview is displayed,
and you can view your logs in the **Activity** section.

## Forward to an HTTP endpoint

Some third-party services, such as [Elasticsearch](https://docs.upsun.com../../add-services/elasticsearch.md) and [OpenSearch](https://docs.upsun.com../../add-services/opensearch.md),
support ingesting log messages through an HTTP endpoint.
You can use HTTP forwarding to forward Upsun and Blackfire logs to such third-party services.

HTTP forwarding makes a `POST` HTTP request with an `application/json` body while forwarding the log messages to the endpoint.

As an example, to forward logs to Elasticsearch using HTTP log forwarding, run the following command:

```
upsun integration:add --type httplog --url "https://<ELASTICSEARCH_URL>/<INDEX_NAME>/_doc" --header "Authorization: Basic " --header "Content-Type: application/json"
```

`type` and `url` are the only properties required for all endpoints.
Optionally, you can use the `headers` property to pass additional headers in the HTTP requests.

Note that if your endpoint URL includes a `PORT`, that can also be included in the `--url` flag:

```
upsun integration:add --type httplog --url "https://<ELASTICSEARCH_URL>:<PORT>/<INDEX_NAME>/_doc" --header "Authorization: Basic " --header "Content-Type: application/json"
```

Once you've [added the service](https://docs.upsun.com../../add-services.md),
to start forwarding logs [trigger a redeploy](https://docs.upsun.com../../development/troubleshoot.md#force-a-redeploy).

### Excluding services from HTTP log forwarding

All log forwarding integrations support an `excluded_services` property. This allows you to prevent logs from specific applications or services (including workers) from being forwarded to an external logging provider.

This is useful for reducing noise, limiting log volume, or excluding non-critical services. The exclusion list is defined at the project level and applies to all environments.

#### Supported integrations

The `excluded_services` property is supported by all log forwarder types, including:

- Syslog
- Sumologic
- Splunk
- HTTP log forwarding
- New Relic
- OTLP

#### Excluding apps or services

By default, logs from all apps and services are forwarded. To exclude specific services, define them using `excluded_services`:

```yaml  {location=".upsun/config.yaml"}
logs_forwarders:
  - type: httplog
    endpoint: https://logs.example.com
    excluded_services:
      - cache
      - debug-worker
```
In this example, logs from the `cache` service and the `debug-worker` worker are not forwarded.

**Note**: 

Note that the same exclusion list applies to all environments. If a listed app or service does not exist in an environment, it is silently ignored. No error is raised.

**Note**: 

``excluded_services`` removes the specified apps or services from log forwarding while all other apps and services continue to forward logs as normal. Note that these exclusions apply globally across environments.

### Naming consistency

When defining exclusions, you can list:

- Apps (for example - `app`, `api`)
- Services (for example - `cache`, `database`)
- Workers (for example - `debug-worker`)

Make sure to use the `service` or `app` name **exactly as defined in your project configuration**.

#### Including services explicitly

You can optionally define an `included_services` list to control exactly which services are forwarded. If `included_services` is set, only the listed services are forwarded.

```yaml  {location=".upsun/config.yaml"}
logs_forwarders:
  - type: syslog
    host: syslog.example.com
    included_services:
      - app
      - api
```
#### Combining include and exclude rules

You can use both `included_services` and `excluded_services` together. The following rules apply:
- If `included_services` is not set, all services are included by default
- If `included_services` is set, only those services are included
- `excluded_services` always removes services from the active set

```yaml  {location=".upsun/config.yaml"}
logs_forwarders:
  - type: syslog
    host: syslog.example.com
    included_services:
      - app
      - api
      - worker
      - cache
    excluded_services:
      - cache
```
Result: logs from `app`, `api`, and `worker` are forwarded.

**Note**: 

Note that a service cannot appear in both lists. Configurations that include the same service in both lists are invalid.

## Log levels

Your app may output logs with distinct severity levels.
But as Upsun only reads logs from `stdout`,
this distinction is lost and everything gets logged at `INFO` level.

To preserve the original log level, use a language-specific syslog module/package for logging.

The following example code snippets show how logs can be written to Syslog:

Using the logging module:

```python {}
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address="/dev/log")
logger.addHandler(handler)

logger.info("Operation started")
logger.error("Operation failed")
```

Using the Syslog module:

```python {}
import syslog

syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0)
syslog.syslog(syslog.LOG_INFO, "Operation started")
syslog.syslog(syslog.LOG_ERR, "Operation failed")
syslog.closelog()
```

Using the log package:

```go {}
package main

import (
	"log"
	"log/syslog"
)

func main() {
	logger, err := syslog.NewLogger(syslog.LOG_LOCAL0|syslog.LOG_INFO, log.LstdFlags)
	if err != nil {
		panic(err)
	}

	logger.Println("Operation started...")
	logger.Fatalln("Operation failed")
}
```

Using the Syslog package:

```go {}
package main

import (
	"fmt"
	"log"
	"log/syslog"
)

func main() {
	syslogWriter, err := syslog.Dial("", "", syslog.LOG_LOCAL0|syslog.LOG_INFO, "")
	if err != nil {
		log.Fatal(err)
	}
	defer syslogWriter.Close()

	fmt.Fprintf(syslogWriter, "Operation has started")
	syslogWriter.Err("Operation failed")
}
```


