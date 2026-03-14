# Source: https://tyk.io/docs/tyk-cloud/environments-deployments/monitoring-how-it-works.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How monitoring works in Tyk Cloud

> Learn how Tyk Cloud monitors throughput and storage metrics for your deployments.

### Tyk Cloud Monitor Metrics

This section explains the various metrics that are monitored by Tyk Cloud.

#### Tyk Cloud Throughput

Tyk Cloud counts the total request/response sizes for traffic transferred through a deployment. Throughput metrics are displayed for the current day. These are calculated as the difference between the throughput usage at the current time and the throughput at last midnight.

External traffic is subject to billing, while internal traffic is exempt. The monitoring service aggregates traffic between different services:

<img src="https://mintcdn.com/tyk/WyMyc-aTqiGjdlz9/img/cloud/tyk-cloud-monitoring-priced-traffic.png?fit=max&auto=format&n=WyMyc-aTqiGjdlz9&q=85&s=38872d5018aba8ffc58da8a7dad079c7" alt="Monitoring Traffic Pricing" width="641" height="481" data-path="img/cloud/tyk-cloud-monitoring-priced-traffic.png" />

**Billed traffic**

* Traffic between user → Control Plane
* Traffic between user → Cloud Data Plane
* Traffic between user → Enterprise Developer Portal
* Traffic between user → Mserv (plugin upload)
* Traffic between Control Plane → Cloud Data Plane cross region
* Traffic between Cloud Data Plane → Mserv cross region
* Traffic between Control Plane → Portal cross region

**Unbilled traffic**

* Hybrid traffic is currently not counted
* Traffic between Control Plane → Cloud Data Plane in the same region
* Traffic between Cloud Data Plane → Mserv in the same region
* Traffic between Control Plane → Portal in the same region

#### Tyk Cloud Storage

When a client makes a request to a Tyk Gateway deployment, the details of the request and response are captured and [stored in Redis](/api-management/dashboard-configuration#traffic-analytics). Tyk Pump processes the records from Redis and forwards them to MongoDB. Finally, Tyk Cloud reads that data from MongoDB and displays its size(bytes) in the *Storage* section of *Monitoring*.

### Track Usage

##### How to check metrics

Login to Tyk Cloud and click on *Monitoring* within the *Operations* menu. Enable *Throughput* to display throughput metrics.

<img src="https://mintcdn.com/tyk/WyMyc-aTqiGjdlz9/img/cloud/tyk-cloud-monitoring-throughput.png?fit=max&auto=format&n=WyMyc-aTqiGjdlz9&q=85&s=0a7bfab3cb2ba0de18d99d0a8ea36021" alt="Monitoring Throughput" width="1630" height="857" data-path="img/cloud/tyk-cloud-monitoring-throughput.png" />

Enable *Storage* to display storage metrics.

<img src="https://mintcdn.com/tyk/WyMyc-aTqiGjdlz9/img/cloud/tyk-cloud-monitoring-storage.png?fit=max&auto=format&n=WyMyc-aTqiGjdlz9&q=85&s=1b66c3905814527deaf872d1839ecc86" alt="Monitoring Storage" width="1630" height="857" data-path="img/cloud/tyk-cloud-monitoring-storage.png" />

You can also optionally filter for metrics by date.

<img src="https://mintcdn.com/tyk/WyMyc-aTqiGjdlz9/img/cloud/tyk-cloud-monitoring-filtering-by-date.png?fit=max&auto=format&n=WyMyc-aTqiGjdlz9&q=85&s=65a58c6c37af86489cd0a162c5c275ab" alt="Monitoring Metric Filtering" width="1630" height="857" data-path="img/cloud/tyk-cloud-monitoring-filtering-by-date.png" />

Here you can see the metrics broken down per environment and a list of the top 5 control and cloud data planes.

<img src="https://mintcdn.com/tyk/WyMyc-aTqiGjdlz9/img/cloud/tyk-cloud-monitoring-break-down.png?fit=max&auto=format&n=WyMyc-aTqiGjdlz9&q=85&s=4f05d8c265b74f224cfab48130a815b2" alt="Monitoring Metric break down" width="1630" height="857" data-path="img/cloud/tyk-cloud-monitoring-break-down.png" />

Built with [Mintlify](https://mintlify.com).
