# Source: https://fly.io/docs/monitoring/logs-api-options/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Logs API options for programmatic access 

## [](#overview)[Overview] 

Fly.io apps run on Firecracker microVMs we call Machines. Each Machine captures `stdout`/`stderr`, ships those logs over NATS, and stores them for a period of time in a Quickwit-backed search index. Most users consume logs via `fly logs` or by setting up log shipping to an external sink.

But sometimes you want to grab logs directly, without a CLI or setting up an exporter, because youâ€™re building a tool, automating something, or you just want to pipe logs into your own system.

------------------------------------------------------------------------

## [](#options-for-fetching-logs-programmatically)[Options for fetching logs programmatically] 

You can get logs programmatically via:

-   **Undocumented HTTP API**: What `fly logs` uses under the hood.
-   **NATS proxy**: Subscribe to real-time logs at the message level.
-   **Log shipper to external sink**: Ingest logs elsewhere, then query them via that system.

Each has tradeoffs. If you want durable search, export logs. If you want low-latency push, use NATS. If you want to `curl` something now, use the HTTP API.

### [](#1-http-api-same-as-fly-logs)[1. HTTP API (same as `fly logs`)] 

The Fly CLI hits an internal API to stream logs. You can use it too:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
GET /api/v1/apps/:app_name/logs
Authorization: <your-token>
```

Youâ€™ll get a stream of newline-delimited JSON log lines. You can pass query params like:

-   `region=cdg` (filter by region)
-   `instance=<id>` (filter by instance â€" sometimes flaky)
-   `start_time=2023-08-01T00:00:00Z` (to backfill)

This endpoint isnâ€™t officially documented, but itâ€™s mostly stable: `flyctl` depends on it. That said, filters donâ€™t always work as expected.

Use this for quick fetches or simple polling scripts. If you hit rate limits or auth issues, check that your token has `read` access to the app.

Importantly, this is the only option that gives you access to historical logs going back to the current retention window (about 15 days). The other options only start streaming from the moment they're connected.

### [](#2-subscribe-to-logs-via-nats-experimental)[2. Subscribe to logs via NATS (experimental)] 

Logs are streamed through NATS under subjects like:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
logs.<app>.<region>.<instance>
```

You can subscribe directly using NATS clients, connecting via the proxy URL and authenticating with your org slug and personal access token.

Example NATS subject:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
logs.my-app.lhr.*
```

This gives you structured JSON log messages in real time.

**Note:** The NATS proxy is a dusty corner of Flyâ€™s platform. It works, but itâ€™s unofficial, experimental, and may change as we evolve our logging infrastructure. If youâ€™re building something serious, we recommend exporting logs instead.

**Things to know:**

-   Youâ€™ll need to handle reconnections: if the network drops or the proxy restarts, your subscriber needs to reconnect and resume without losing messages.
-   Youâ€™ll need to handle backpressure: if your app canâ€™t process logs fast enough, messages might pile up and get dropped. Design your consumer to either keep up or fail gracefully.
-   If you want to dedupe across subscribers, use NATS queue groups.
-   NATS only streams logs from starting from the moment you connect. You wonâ€™t get any history unless youâ€™ve been subscribed the whole time.

For more details on connecting to Flyâ€™s NATS log stream (authentication, subject patterns, example clients), head over to the [Observability for User Apps](/docs/blueprints/observability-for-user-apps/?utm_source=chatgpt.com#streaming-fly-app-logs-to-your-end-users) guide.

### [](#3-log-shipper-to-external-sink)[3. Log Shipper to External Sink] 

If you want durable, queryable logs, export them. We maintain a small app called the [Fly Log Shipper](https://github.com/superfly/fly-log-shipper) that listens to NATS and forwards logs to sinks like Loki, Datadog, Elastic, Honeycomb, or even S3.

The log shipper is a prebuilt Fly app running Vector, with configuration you can customize via TOML. It subscribes to log subjects and streams data wherever you want.

Example config:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
[sinks.loki]
type = "loki"
inputs = ["fly_logs"]
endpoint = "https://my-loki-instance.example"
encoding.codec = "json"
```

To control which logs get forwarded, set the `SUBJECT` environment variable when deploying:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
SUBJECT="logs.my-app.*.*"
```

Like NATS, the log shipper only sees logs from the moment it connects onward. If you deploy it today, you wonâ€™t see logs from yesterday.

The log shipper is the most robust option if you want long-term retention, full-text search, alerting, or integration with your existing observability stack.

More details:

-   [Fly Docs: Export logs](/docs/monitoring/exporting-logs/)
-   [Fly Blog: Shipping Logs](https://fly.io/blog/shipping-logs/)
-   [GitHub: superfly/fly-log-shipper](https://github.com/superfly/fly-log-shipper)

------------------------------------------------------------------------

## [](#summary-so-what-should-i-use)[Summary: So what should I use?] 

-   Want to grep logs from a script? Try the HTTP API.
-   Want real-time stream into your own system? NATS (with caveats).
-   Want reliable search and dashboards? Export logs via shipper.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmonitoring%2Flogs-api-options.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Logs+API+options+for+programmatic+access%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fmonitoring%2Flogs-api-options%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fmonitoring%2Flogs-api-options.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Logs+API+options+for+programmatic+access%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/monitoring/logs-api-options.html.md)