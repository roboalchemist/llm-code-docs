# Source: https://www.metabase.com/docs/latest/installation-and-operation/observability-with-prometheus

<div>

1.  [Home](/docs/latest/)
2.  [Installation and Operation](/docs/latest/installation-and-operation/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Observability with Prometheus

You can export metrics in [Prometheus](https://prometheus.io/) format from your Metabase.

## Running Metabase and Prometheus locally

To give you an idea of how Metabase and Prometheus would work in your production environment, we'll walk through how to set up Metabase and Prometheus locally.

## Start up Metabase with `MB_PROMETHEUS_SERVER_PORT`

Download the latest [Metabase JAR](/start/oss/), and run Metabase using an environment variable to specify the Prometheus server port:

``` highlight
MB_PROMETHEUS_SERVER_PORT=9191 java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

The `MB_PROMETHEUS_SERVER_PORT=9191` specifies which port (`9191`) Metabase will use to send data to Prometheus. To clarify the ports that will be involved here:

-   Port `3000` is the port Metabase uses to serve the Metabase app. You can set another port with `MB_JETTY_PORT` (e.g., `MB_JETTY_PORT=3001`).
-   Port `9191` (or whichever port you specified with the `MB_PROMETHEUS_SERVER_PORT` environment variable) is the port Prometheus uses to scrape metrics from Metabase.
-   Port `9090` is the port Prometheus uses to serve the Prometheus application.

When you start Metabase, the Metabase logs will tell you that Metabase is starting the `prometheus metrics collector` and `prometheus metrics web-server`.

``` highlight
(truncated logs)
2022-09-01 17:47:38,808 INFO metabase.util :: Database setup took 3.4 s
2022-09-01 17:47:38,826 INFO metabase.core :: Setting up prometheus metrics
2022-09-01 17:47:38,827 INFO metabase.prometheus :: Starting prometheus metrics collector
2022-09-01 17:47:38,839 INFO metabase.prometheus :: Starting prometheus metrics web-server on port 9,191
(truncated logs)
```

You can view your locally running Metabase at `http://localhost:3000`.

## Download and configure Prometheus

[Download Prometheus](https://prometheus.io/download), and extract the files.

Change into the Prometheus directory, add the following YAML file to configure your Prometheus:

## Prometheus configuration file example

``` highlight
global:
  scrape_interval: 15s # By default, scrape targets every 15 seconds.

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
    monitor: "codelab-monitor"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s
    # use whatever port here that you set for MB_PROMETHEUS_SERVER_PORT
    static_configs:
      - targets: ["localhost:9191"]
```

You need to change the "target" to where Metabase is, for this particular example, Metabase resides in the same host where Prometheus is running ("localhost").

## Running Prometheus Locally

In a new terminal process in the Prometheus directory, run:

``` highlight
./prometheus --config.file=prometheus.yml
```

Then check `http://localhost:9090`. You should see the Prometheus app, and be able to search for various metrics emitted by Metabase.

![Prometheus page showing \`jvm_thread_state\` graph](./images/prometheus.png)

## Sample metrics output

Here is some sample output from Metabase:

``` highlight
'# HELP jvm_threads_current Current thread count of a JVM
'# TYPE jvm_threads_current gauge
jvm_threads_current 81.0
'# HELP jvm_threads_daemon Daemon thread count of a JVM
'# TYPE jvm_threads_daemon gauge
jvm_threads_daemon 36.0
'# HELP jvm_threads_peak Peak thread count of a JVM
'# TYPE jvm_threads_peak gauge
jvm_threads_peak 81.0
'# HELP jvm_threads_started_total Started thread count of a JVM
'# TYPE jvm_threads_started_total counter
jvm_threads_started_total 104.0
'# HELP jvm_threads_deadlocked Cycles of JVM-threads that are in deadlock waiting to acquire object monitors or ownable synchronizers
'# TYPE jvm_threads_deadlocked gauge
jvm_threads_deadlocked 0.0
```

## Exported metrics

Metrics exported by Metabase include:

-   `c3p0_max_pool_size`
-   `c3p0_min_pool_size`
-   `c3p0_num_busy_connections`
-   `c3p0_num_connections`
-   `c3p0_num_idle_connections`
-   `c3p0_num_threads_awaiting_checkout_default_user`
-   `jetty_async_dispatches_total`
-   `jetty_async_requests_total`
-   `jetty_async_requests_waiting`
-   `jetty_async_requests_waiting_max`
-   `jetty_dispatched_active`
-   `jetty_dispatched_active_max`
-   `jetty_dispatched_time_max`
-   `jetty_dispatched_time_seconds_total`
-   `jetty_dispatched_total`
-   `jetty_expires_total`
-   `jetty_request_time_max_seconds`
-   `jetty_request_time_seconds_total`
-   `jetty_requests_active`
-   `jetty_requests_active_max`
-   `jetty_requests_total`
-   `jetty_responses_bytes_total`
-   `jetty_responses_total`
-   `jetty_stats_seconds`
-   `jvm_gc_collection_seconds_count`
-   `jvm_gc_collection_seconds_sum`
-   `jvm_memory_bytes_committed`
-   `jvm_memory_bytes_init`
-   `jvm_memory_bytes_max`
-   `jvm_memory_bytes_used`
-   `jvm_memory_objects_pending_finalization`
-   `jvm_memory_pool_bytes_committed`
-   `jvm_memory_pool_bytes_init`
-   `jvm_memory_pool_bytes_max`
-   `jvm_memory_pool_bytes_used`
-   `jvm_memory_pool_collection_committed_bytes`
-   `jvm_memory_pool_collection_init_bytes`
-   `jvm_memory_pool_collection_max_bytes`
-   `jvm_memory_pool_collection_used_bytes`
-   `jvm_threads_current`
-   `jvm_threads_daemon`
-   `jvm_threads_deadlocked`
-   `jvm_threads_deadlocked_monitor`
-   `jvm_threads_peak`
-   `jvm_threads_started_total`
-   `jvm_threads_state`
-   `process_cpu_seconds_total`
-   `process_max_fds`
-   `process_open_fds`
-   `process_start_time_seconds`
-   `process_virtual_memory_bytes`
-   `metabase_email_messages_total`
-   `metabase_email_messages_created`
-   `metabase_email_message_errors_total`
-   `metabase_email_message_errors_created`

## Further reading

-   [Running Metabase](../troubleshooting-guide/running)
-   [Monitoring Metabase](./monitoring-metabase)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/observability-with-prometheus.md) ]