# Source: https://www.aptible.com/docs/core-concepts/observability/metrics/metrics-drains/influxdb-metric-drain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# InfluxDB Metric Drain

> Learn about sending Aptible logs to an InfluxDB

Aptible can deliver your [Metrics](/core-concepts/observability/metrics/overview) to any InfluxDB Database (hosted on Aptible or not). There are two types of InfluxDB Metric Drains on Aptible:

* Aptible-hosted: This method allows you to route metrics to an InfluxDB Database hosted on Aptible. This Database must live in the same Environment as the Metrics you are retrieving. Additionally, the [Aptible Metrics Terraform Module](https://registry.terraform.io/modules/aptible/metrics/aptible/latest) uses this method to deploy prebuilt Grafana dashboards with alerts for monitoring RAM & CPU usage for your Apps & Databases - so you can instantly start monitoring your Aptible resources.
* Hosted anywhere: This method allows you to route Metrics to any InfluxDB. This might be useful if you are leveraging InfluxData's [hosted InfluxDB offering](https://www.influxdata.com/).

# InfluxDB Metrics Structure

Aptible InfluxDB Metric Drains publish metrics in a series named `metrics`.

The following values are published (approximately every 30 seconds):

* `running`: a boolean indicating whether the Container was running when this point was sampled.
* `milli_cpu_usage`: the Container's average CPU usage (in milli CPUs) over the reporting period.
* `milli_cpu_limit`: the maximum CPU accessible to the container.
* `memory_total_mb`: the Container's total memory usage.
* `memory_rss_mb`: the Container's RSS memory usage. This memory is typically not reclaimable. If this exceeds the `memory_limit_mb`, the container will be restarted.
* `memory_limit_mb`: the Container's [Memory Limit](/core-concepts/scaling/memory-limits).
* `disk_read_kbps`: the Container's average disk read bandwidth over the reporting period.
* `disk_write_kbps`: the Container's average disk write bandwidth over the reporting period.
* `disk_read_iops`: the Container's average disk read IOPS over the reporting period.
* `disk_write_iops`: the Container's average disk write IOPS over the reporting period.
* `disk_usage_mb`: the Database's Disk usage (Database metrics only).
* `disk_limit_mb`: the Database's Disk size (Database metrics only).
* `pids_current`: the current number of tasks in the Container (see [Other Limits](/core-concepts/security-compliance/ddos-pid-limits)).
* `pids_limit`: the maximum number of tasks for the Container (see [Other Limits](/core-concepts/security-compliance/ddos-pid-limits)).

> 📘 Review [Understanding Memory Utilization](/core-concepts/scaling/memory-limits#understanding-memory-utilization) for more information on the meaning of the `memory_total_mb` and `memory_rss_mb` values.

> 📘 Review [I/O Performance](/core-concepts/scaling/database-scaling#i-o-performance) for more information on the meaning of the `disk_read_iops` and `disk_write_iops` values.

All points are enriched with the following tags:

* `environment`: Environment handle
* `app`: App handle (App metrics only)
* `database`: Database handle (Database metrics only)
* `service`: Service name
* `host_name`: [Container Hostname (Short Container ID)](/core-concepts/architecture/containers/overview#container-hostname)
* `container`: full Container ID

# Getting Started

<AccordionGroup>
  <Accordion title="Creating a Influx Metric Drain">
    You can set up an InfluxDB Metric Drain in the following ways:

    * (Aptible-hosted only) Using [Aptible Metrics Terraform Module](https://registry.terraform.io/modules/aptible/metrics/aptible/latest). This provision an Influx Metric Drain with pre-built Grafana dashboards and alerts for monitoring RAM & CPU usage for your Apps & Databases. This simplifies the setup of Metric Drains so you can start monitoring your Aptible resources immediately, all hosted within your Aptible account.
    * Within the Aptible Dashboard by navigating to the respective Environment > selecting the "Metrics Drain" tab > selecting "Create Metric Drain" > selecting "InfluxDB (This Environment)" or "InfluxDB (Anywhere)"
      <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=95460e221fa355689af77e9c7d0907d2" alt="" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/App_UI_InfluxDB-self.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=bf1cff0cf333539d4f194505dfa1b50b 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=c587d4050e558836fc65b6728b0b3c47 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=92a34978182c6b25ef4b0fbcc47f6171 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b576da4dc74e6718e5d3ce65ad004d9e 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=de95f17bcd8dc568dbe650420d14003e 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_InfluxDB-self.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=c09d0e8eb567eeb8c681d832a3d83338 2500w" />
    * Using the [`aptible metric_drain:create:influxdb`](/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb) command
  </Accordion>

  <Accordion title="Accessing Metrics in DB">
    The best approach to accessing metrics from InfluxDB is to deploy [Grafana](https://grafana.com). Grafana is easy to deploy on Aptible.

    * **Recommended:** [Using Aptible Metrics Terraform Module](https://registry.terraform.io/modules/aptible/metrics/aptible/latest). This provisions Metric Drains with pre-built Grafana dashboards and alerts for monitoring RAM & CPU usage for your Apps & Databases. This simplifies the setup of Metric Drains so you can start monitoring your Aptible resources immediately, all hosted within your Aptible account.
    * You can also follow this tutorial [Deploying Grafana on Aptible](https://www.aptible.com/docs/deploying-grafana-on-deploy), which includes suggested queries to set up within Grafana.
  </Accordion>
</AccordionGroup>
