# Source: https://www.aptible.com/docs/core-concepts/integrations/datadog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Datadog Integration

> Learn about using the Datadog Integration for logging and monitoring

# Overview

Aptible integrates with [Datadog](https://www.datadoghq.com/), allowing you to send information about your Aptible resources directly to your Datadog account for monitoring and analysis. You can send the following data directly to your Datadog account:

* **Logs:** Send logs to Datadog’s [log management](https://docs.datadoghq.com/logs/) using a log drains
* **Container Metrics:** Send app and database container metrics to Datadog’s [container monitoring](https://www.datadoghq.com/product/container-monitoring/) using a metric drain
* **In-Process Instrumentation Data (APM):** Send instrumentation data to [Datadog’s APM](https://www.datadoghq.com/product/apm/) by deploying a single Datadog Agent app

> Please note, Datadog's documentation defaults to v2. Please use v1 Datadog documentation with Aptible.

## Datadog Log Integration

On Aptible, you can set up a Datadog [log drain](/core-concepts/observability/logs/log-drains/overview) within an environment to send logs for apps, databases, SSH sessions and endpoints directly to your Datadog account for [log management and analytics](https://www.datadoghq.com/product/log-management/).

<Info> On other platforms, you might configure this by installing the Datadog Agent and setting `DD_LOGS_ENABLED`.</Info>

<Accordion title="Creating a Datadog Log Drain">
  A Datadog Log Drain can be created in three ways on Aptible:

  * Within the Aptible Dashboard by:
    * Navigating to an Environment
    * Selecting the **Log Drains** tab
    * Selecting **Create Log Drain**
    * Selecting **Datadog**
  * Using the [`aptible log_drain:create:datadog`](/reference/aptible-cli/cli-commands/cli-log-drain-create-datadog) CLI command
</Accordion>

## Datadog Container Monitoring Integration

On Aptible, you can set up a Datadog [metric drain](/core-concepts/observability/metrics/metrics-drains/overview) within an environment to send metrics directly to your Datadog account. This enables you to use Datadog’s [container monitoring](https://www.datadoghq.com/product/container-monitoring/) for apps and databases. Please note that not all features of container monitoring are supported (including but not limited to Docker integrations and auto-discovery).

<Info>On other platforms, you might configure this by installing the Datadog Agent and setting `DD_PROCESS_AGENT_ENABLED`.</Info>

<Accordion title="Creating a Datadog Metric Drain">
  A Datadog Log Drain can be created in three ways on Aptible:
  A Datadog Metric Drain can be provisioned in three ways on Aptible:

  * Within the Aptible Dashboard by:
    * Navigating to an Environment:
    * Selecting the **Metric Drains** tab
    * Selecting **Create Metric Drain**
  * Using the [`aptible metric_drain:create:datadog`](/reference/aptible-cli/cli-commands/cli-metric-drain-create-datadog) CLI command
  * Using the Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs)
</Accordion>

### Datadog Metrics Structure

Aptible metrics are reported as [Custom Metrics](https://docs.datadoghq.com/developers/metrics/custom_metrics/) in Datadog. The following metrics are reported (all these metrics are reported as `gauge` in Datadog, approximately every 30 seconds):

* `enclave.running`: a boolean indicating whether the Container was running when this point was sampled.
* `enclave.milli_cpu_usage`: the Container's average CPU usage (in milli CPUs) over the reporting period.
* `enclave.milli_cpu_limit`: the maximum CPU accessible to the container.
* `enclave.memory_total_mb`: the Container's total memory usage. See [Understanding Memory Utilization](/core-concepts/scaling/memory-limits#understanding-memory-utilization) for more information on memory usage.
* `enclave.memory_rss_mb`: the Container's RSS memory usage. This memory is typically not reclaimable. If this exceeds the `memory_limit_mb`, the container will be restarted.
  <Note> Review [Understanding Memory Utilization](/core-concepts/scaling/memory-limits#understanding-memory-utilization) for more information on the meaning of the `enclave.memory_total_mb` and `enclave.memory_rss_mb` values. </Note>
* `enclave.memory_limit_mb`: the Container's [Memory Limit](/core-concepts/scaling/memory-limits).
* `enclave.disk_read_kbps`: the Container's average disk read bandwidth over the reporting period.
* `enclave.disk_write_kbps`: the Container's average disk write bandwidth over the reporting period.
* `enclave.disk_read_iops`: the Container's average disk read IOPS over the reporting period.
* `enclave.disk_write_iops`: the Container's average disk write IOPS over the reporting period.
  <Note> Review [I/O Performance](/core-concepts/scaling/database-scaling#i-o-performance) for more information on the meaning of the `enclave.disk_read_iops` and `enclave.disk_write_iops` values. </Note>
* `enclave.disk_usage_mb`: the Database's Disk usage (Database metrics only).
* `enclave.disk_limit_mb`: the Database's Disk size (Database metrics only).
* `enclave.pids_current`: the current number of tasks in the Container (see [Other Limits](/core-concepts/security-compliance/ddos-pid-limits)).
* `enclave.pids_limit`: the maximum number of tasks for the Container (see [Other Limits](/core-concepts/security-compliance/ddos-pid-limits)).

All metrics published in Datadog are enriched with the following tags:

* `environment`: Environment handle
* `app`: App handle (App metrics only)
* `database`: Database handle (Database metrics only)
* `service`: Service name
* `container`: Container ID

Finally, Aptible also sets the `host_name` tag on these metrics to the [Container Hostname (Short Container ID).](/core-concepts/architecture/containers/overview#container-hostname)

## Datadog APM

On Aptible, you can configure in-process instrumentation Data (APM) to be sent to [Datadog’s APM](https://www.datadoghq.com/product/apm/) by deploying a single Datadog Agent app and configuring each of your apps to:

* Enable Datadog in-process instrumentation and
* Forward those data through the Datadog Agent app separately hosted on Aptible

<Card title="How to set up Datadog APM" icon="book-open-reader" iconType="duotone" iconType="duotone" href="https://www.aptible.com/docs/datadog-apm" />
