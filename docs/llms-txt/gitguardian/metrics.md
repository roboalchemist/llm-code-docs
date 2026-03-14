# Source: https://docs.gitguardian.com/self-hosting/management/application-management/metrics.md

# Applicative metrics

> Export Prometheus metrics from your GitGuardian self-hosted installation for monitoring and alerting.

## Export Application Metrics to Prometheus

Applicative metrics are gathered thanks to [Prometheus](https://prometheus.io/),
a software used for event monitoring and alerting, which permits scraping the
data captured in the application.

:::info
The Prometheus exporter is not supported for [embedded clusters](../../installation/choose-embedded-existing#what-is-an-embedded-cluster-installation).
:::

### Metrics available

The Prometheus exporter gives access to the
following metrics:

| Metric                                | Type    | Description                                 | Dimensions                          |
| ------------------------------------- | ------- | ------------------------------------------- | ----------------------------------- |
| gim_active_users_total                | Gauge   | All users in the GitGuardian instance       | _None_                              |
| gim_issues_total                      | Gauge   | All incidents in the GitGuardian instance   | Severity, Status                    |
| gim_occurrences_total                 | Gauge   | All occurrences in the GitGuardian instance | Hidden, Status                      |
| gim_commits_total                     | Gauge   | Commits processed                           | Account, Scan type                  |
| gim_repo_scan_active_statuses_total   | Gauge   | Count of historical scans                   | scan_feature, status                |
| gim_public_api_quota_total            | Gauge   | Maximum allowed usage of the Public API     | Account                             |
| gim_public_api_usage_total            | Gauge   | Current usage of the Public API             | Account                             |
| gim_public_api_token_total            | Gauge   | Count of active tokens for the Public API   | Account, Type                       |
| gim_postgres_used_disk_bytes          | Gauge   | Disk space used by PostgreSQL data          | _None_                              |
| gim_redis_used_memory_bytes           | Gauge   | Memory used by Redis data                   | _None_                              |
| gim_redis_available_memory_bytes      | Gauge   | Memory available for Redis data             | _None_                              |
| gim_celery_queue_length               | Gauge   | Current size of the queue (tasks waiting)   | queue_name                          |
| gim_celery_active_consumer_count      | Gauge   | Celery workers running                      | queue_name                          |
| gim_http_request_started_total        | Counter | HTTP requests initiated                     | api, method, view_name              |
| gim_http_request_success_total        | Counter | Successful HTTP requests                    | api, method, view_name              |
| gim_http_request_failure_total        | Counter | Failed HTTP requests                        | api, method, status_code, view_name |
| gim_periodic_task_period_seconds      | Gauge   | Periodicity of periodic tasks               | task_name, queue_name               |
| gim_periodic_task_not_run_for_seconds | Gauge   | Time since periodic tasks were run          | task_name, queue_name               |
| gim_check_runs_long_running           | Gauge   | Check runs taking times                     | plan                                |
| gim_health_check_result_count         | Gauge   | Health checks results                       | service_name, status                |
| gim_outdated_health_check_count       | Gauge   | Health Checks older than the periodic range | service_name                        |

### Enable or disable Application metrics

Applicative metrics are deactivated by default.
Two steps are needed to activate Application Metrics:

- authorize collection of metrics by the application
- activate Prometheus export

#### Authorize metrics collection

To authorize the metrics collection, you should go to the **Preferences section**
in the **Admin Area**, check the `prometheus_metrics_active` feature flag and
save settings.

![Activate Applicative Metrics](/img/self-hosting/management/application-management/activate_applicative_metrics.png)

To disable it, you should uncheck this parameter and save settings.

this requires to (not included in this chart) See: https://prometheus-operator.dev

#### Install Prometheus Operator

Metrics are collected by Prometheus using the
[Prometheus Operator](https://prometheus-operator.dev/).

For Existing Clusters, you should manually install it
([installation documentation](https://prometheus-operator.dev/docs/getting-started/installation/)).

#### Activate Prometheus export using KOTS

To create exporter resources and allow automatic discovery, you should go in the
**KOTS Admin Console** and check the **Activate Prometheus Exporter** checkbox in
the Prometheus section of the configuration section.

![Activate Applicative Metrics](/img/self-hosting/management/application-management/activate_prometheus_exporter.png)

Then save the configuration, and **Deploy** the application to apply the new
configuration.

To disable it, you should uncheck this parameter, save configuration, and apply
it through a new deployment.

#### Activate Prometheus export using Helm

Applicative metrics exporter can be enabled by setting `observability.exporters.webAppExporter.enabled=true` in values file.

```yaml
observability:
  exporters:
    webAppExporter:
      enabled: true
```

Please note that Helm application also features a [Celery Exporter](https://github.com/danihodovic/celery-exporter) allowing to monitor several Celery metrics like "count of active tasks by queue". The [full list of metrics is available here](https://github.com/danihodovic/celery-exporter#metrics).

You can activate Celery Exporter in your values file:

```yaml
observability:
  exporters:
    webAppExporter:
      enabled: true
    statefulAppExporter:
      enabled: true
```

If you use Prometheus Operator, you may want to use the Service Monitor provided for automatic discovery of the exporter by Prometheus:

```yaml
observability:
  exporters:
    webAppExporter:
      enabled: true
    statefulAppExporter:
      enabled: true
  serviceMonitors:
    enabled: true
```

Otherwise, you can manually scrape exporters.

- Applicative metrics can be scrapped from the app-exporter service at: `http://app-exporter:9808/metrics`
- Celery metrics can be scrapped from the celery-exporter service at: `http://celery-exporter:9808/metrics`

### How to collect metrics

On Existing Clusters, Prometheus must be installed and configured manually. If
the [Kube-Prometheus](https://github.com/coreos/kube-prometheus) Operator is
used, all the applicative metrics will be automatically listed thanks to the
Discovery service of Kube-Prometheus Operator.

Otherwise, a manual configuration may be needed.
Applicative metrics discovery is possible through the `app-monitoring` headless service.
This service exposes an `exporter` pod serving metrics at http://_exporter-xxxxx-xxxxx_:9808/metrics

## Usage data

GitGuardian collects usage data to improve the user experience and support. It can be easily deactivated by
adjusting the `custom_telemetry_active` setting found in the [preferences](./preferences#on-premise)
section in the Admin area.

:::info
Why keep usage data enable?

- **Continuous Product Improvement**: usage data greatly helps us understand how our application is used in various environments. This allows us to specifically target areas needing improvements and direct our testing efforts. This ensures that our product evolves to meet our users' needs effectively while contributing to better quality and stability.

- **Targeted and Efficient Support**: in case of technical problems, usage data enables GitGuardian to identify and resolve issues much more quickly. This means reduced downtime for you and a better overall user experience.

- **Security and Privacy**: we want to reassure you that data privacy and security are our top priority. We do not collect any personal or sensitive data. Our goal is solely to improve user experience and the performance of our product.

:::

Here are the categories and metrics we collect:

- **Replicated**

  - Various deployment-related metrics such as cloud status, version, and uptime

- **System**

  - SSO Provider
  - Network Gateway Type
  - Custom CA and proxy status
  - Prometheus Application metrics activation status

- **Users & Teams**

  - Number of pending invitees, registered users with different access levels, active users.

- **Historical Scan**

  - Number of historical scans canceled, failed, and finished
  - Percentile durations of historical scans
  - Number of secrets found per day and source scans per day in historical scans
  - Number of historical scans considered too large

- **Integrations**

  - Number of instances, installations, projects, sites for VCS and Other Data Sources
  - Number of monitored and unmonitored sources, along with source size percentiles and estimated users per VCS

- **Secret**

  - Number of deactivated detectors per category, registered and unregistered feedbacks, and various metrics related to secret validity checks and incidents

- **Public API**
  - Number of calls for ggshield secrets scans, including different modes and repositories
  - Number of active personal access tokens and service accounts
  - Number of public API calls
