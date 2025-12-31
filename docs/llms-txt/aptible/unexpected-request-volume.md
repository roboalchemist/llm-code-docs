# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/unexpected-request-volume.md

# Managing a Flood of Requests in Your App

When your app experiences a sudden flood of requests, it can degrade performance, increase latency, or even cause downtime. This situation is common for apps hosted on public endpoints with infrastructure scaled for low traffic, such as MVPs or apps in the early stages of product development.

This guide outlines steps to detect, analyze, and mitigate such floods of requests on the Aptible platform, along with strategies for long-term preparation.

## Detecting and Analyzing Traffic

Use **Endpoint Logs** to analyze incoming requests:

* **What to Look For**: Endpoint logs can help identify traffic spikes, frequently accessed endpoints, and originating networks.

* **Steps**:
  * Enable [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs) for your app.
  * Send logs to a third-party service (e.g., Papertrail, LogDNA, Datadog) using a [Log Drain](/core-concepts/observability/logs/log-drains/overview). These services, depending on the features of each provider, allow you to:
    * Chart the volume of requests over time.
    * Analyze patterns such as bursts of requests targeting specific endpoints.

Use **APM Tools** to identify bottlenecks:

* **Purpose**: Application Performance Monitoring (APM) tools provide insight into performance bottlenecks.

* **Key Metrics**:
  * Endpoints with the highest request volumes.
  * Endpoints with the longest processing times.
  * Database queries or backend processes which represent bottlenecks with the increase in requests.

## Immediate Response

1. **Determine if Endpoint or resources should be public**:
   * If the app is not yet in production, consider implementing [IP Filtering](/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering) as a measure to only allow traffic from known IPs / networks.
   * Consider if all or portions of the app should be protected by authenticated means within your control.

2. **Investigate Traffic Source**:
   * **Authenticated Users**: If requests originate from authenticated users, verify the legitimacy and source.
   * **Public Activity**: Focus on high-traffic endpoints/pages and optimize their performance.

3. **Monitor App and Database Metrics**:
   * Use Aptible Metric Drains or viewing the in-app Aptible Metrics to observe CPU and memory usage of apps and databases during the event.

4. **Scale Resources Temporarily**:
   * Based on observations of metrics, scale app or database containers via the Aptible dashboard or CLI to handle increased traffic.
   * Specifically, if you see the `worker_connections are not enough` error message in your logs, horizontal scaling will help address this issue. See more about this error [here](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs#worker-connections-are-not-enough).

5. **Validate Performance of Custom Error Pages**:
   * Ensure error pages (e.g., 404, 500) are lightweight and avoid backend processing or serving large or uncached assets.

## Long-Term Mitigation

1. **Authentication and Access Control**:
   * Protect sensitive resources or endpoints with authentication.

2. **Periodic Load Testing**:
   * Conduct load tests to identify and address bottlenecks.

3. **Horizontal Auto Scaling**:
   * Configure [horizontal auto scaling](/how-to-guides/app-guides/horizontal-autoscaling-guide) for app containers.

4. **Optimize Performance**:
   * Use caching, database query optimization, and other performance optimization techniques to reduce processing time and load for high-traffic endpoints.

5. **Incident Response Plan**:
   * Document and rehearse a process for handling high-traffic events, including monitoring key metrics and scaling resources.

## Summary

A flood of requests doesn't have to bring your app down. By proactively monitoring traffic, optimizing performance, and having a well-rehearsed response plan, you can ensure that your app remains stable during unexpected surges.
