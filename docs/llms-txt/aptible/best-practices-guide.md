# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/best-practices-guide.md

# Best Practices Guide

> Learn how to deploy your infrastructure with best practices for setting up your Aptible account

## Overview

This guide will provide all the essential information you need to confidently make key setup decisions for your Aptible platform. With our best practices, you'll be able to deploy your infrastructure with best practices for performance, reliability, and security.

## Resource Planning

### Stacks

An [Aptible Stack](/core-concepts/architecture/stacks) is the underlying virtualized infrastructure (EC2 instances, private network, etc.) on which resources (Apps, Databases) are deployed. Consider the following when planning and creating stacks:

* Establish Network Boundaries

  * Stacks provide network-level isolation of resources and are therefore used to protect production resources. Environments or apps used for staging, testing or other purposes that may be configured with less stringent security controls may have direct access to production resources if they are deployed in the same stack. There are also issues other than CPU/Memory limits, such as open file limits on the host, where it's possible for a misbehaving testing container to affect production resources. To prevent these scenarios, it is recommended to use stacks as network boundaries.
* Use IP Filtering with [Stack IP addresses](/core-concepts/apps/connecting-to-apps/outbound-ips)

  * Partners or vendors that use IP filtering may require users to provide them with the outbound IP addresses of the apps they interact with. There are instances where Aptible may need to fail over to other IP addresses to maintain outbound internet connectivity on a stack. It is important to add all Stack IP Addresses to the IP filter lists.

### Environments

[Environments](/core-concepts/architecture/environments) are used for access control, to control backup policy and to provide logical isolation.  Remember network isolation is established at the Stack level; Environments on the same Stack can talk to each other.  Environments are used to group resources by logging, retention, and access control needs as detailed below:

* Group resources based on least-access principle

  * Aptible uses Environments and Roles to [manage user access](/core-concepts/security-compliance/access-permissions).  Frequently, teams or employees do not require access to all resources.  It is good practice to identify the least access required for users or groups, and restrict access to that minimum set of permissions.

* Group Databases based on backup retention needs

  * Backup needs for databases can vary greatly. For example, backups for Redis databases used entirely as an in-memory cache or transient queue, or replica databases used by BI tools are not critical, or even useful, for disaster recovery. These types of databases can be moved to other Environments with a shorter backup retention configured, or without cross-region copies. More on Database Retention and Disposal [here](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal).

* Group resources based on logging needs

  * [Logs](/core-concepts/observability/logs/overview) are delivered separately for each environment. When users have access and retention needs that are specific to different classes of resources (staging versus production), using separate environments is an excellent way to deliver logs to different destinations or to uniquely tag logs.

* Configure [Log Drains](/core-concepts/observability/logs/log-drains/overview) for all environments

  * Reviewing the output of a process is a very important troubleshooting step when issues arise. Log Drains provide the output, and more: users can collect the request logs as recorded at the Endpoint, and may also capture Aptible SSH sessions to audit commands run in Ephemeral Containers.

* Configure [Metric Drains](/core-concepts/observability/metrics/metrics-drains/overview) for all environments

* Monitoring resource usage is a key step to detect issues as early as possible. While it is imperative to set up metric drains in production environments, there is also value in setting up metric drains for staging environments.

## Operational Practices

### Services

[Services](/core-concepts/apps/deploying-apps/services) are metadata that define how many Containers Aptible will start for an App, what Container Command they will run, their Memory Limits, and their CPU Limits. Here are some considerations to keep in mind when working with services:

* [Scale services](/core-concepts/scaling/overview) horizontally where possible

* Aptible recommends horizontally scaling all services to multiple containers to ensure high-availability. This will allow the app's services to handle container failures gracefully by routing traffic to healthy containers while the failed container is restarted. Horizontal scaling also ensures continued effectiveness in the case that performance needs to be scaled up. Aptible also recommend following this practice for at least one non-production environment because this will allow users to identify any issues with horizontal scaling (reliance on local session storage for example) in staging, rather than in production.

* Avoid unnecessary tasks, commands and scripts in the ENTRYPOINT, CMD or [Procfile](/how-to-guides/app-guides/define-services).

  * Aptible recommends users ensure containers do nothing but start the desired process such as the web server for example.  If the container downloads, installs or configures any software before running the desired process, this introduces both a chance for failure and a delay in starting the desired process.  These commands will run every time the container starts, including if the container restarts unexpectedly. Therefore, Aptible recommends ensuring the container starts serving requests immediately upon startup to limit the impact of such restarts.

### Endpoints

[Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) let users expose Apps on Aptible to clients over the public internet or the Stack's internal network. Here are some considerations to keep in mind when setting up endpoints:

* TLS version

  * Use the `SSL_PROTOCOLS_OVERRIDE` [setting](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-protocols#ssl_protocols_override-control-ssl--tls-protocols) to set the desired acceptable TLS version. While TLS 1.0 and 1.1 can provide great backward compatibility, it is standard practice to allow only `TLSv1.2`, and even `TLSv1.2 PFS` to pass many security scans.
* SSL

  * Take advantage of the `FORCE_SSL` [setting](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-redirect#force_ssl-in-detail). Aptible can handle HTTP->HTTPS redirects on behalf of the app, ensuring all clients connect securely without having to enable or write such a feature into each service.

### Dependency Vulnerability Scanning

* Use an image dependency vulnerability scanner before deploying to production.

  * The built-in security scanner is designed for git-based deployments (Dockerfile Deploy), where Aptible builds the image and users have no method to inspect it directly. It can only be inspected after being deployed. Aptible recommends that users scan images before deploying to production. Using image-based deployment (Direct Docker Image Deploy) will be the easiest way to scan images and integrate the scans into the CI/CD pipeline. Quay and ECS can scan images automatically and support alerting. Otherwise, users will want to scan the deployed staging image before deploying that commit to production.

### Databases

* Create and use [least-privilege-required users](/core-concepts/managed-databases/connecting-databases/database-endpoints#least-privileged-access) on databases

  * While using the built-in `aptible` user may be convenient, for Databases which support it (MySQL, PostgreSQL, Mongo, ES 7), Aptible recommends creating a separate user that is granted only the permissions required by the application. This has two primary benefits:

    1. Limit the impact of security vulnerabilities because applications are not granted more permissions than they need

    2. If the need to remediate a credential leak arises, or if a user's security policy dictates that the user rotate credentials periodically, the only way to rotate database credentials without any downtime is to create separate database users and update apps to use the newly created user's credentials.  Rotating the `aptible` user credential requires notifying Aptible Support to update the API to avoid breaking functionality such as replication and Database Tunnels and any Apps using the credentials will lose access to the Database.

## Monitoring

* Set up monitoring for common errors:

  * The "container exceeded memory allocation" is logged when a container exceeds its RAM allocation. While the metrics in the Dashboard are captured every minute, if a Container exceeds its RAM allocation very quickly and is then restarted, the metrics in the Dashboard may not reflect the usage spike. Aptible recommends referring to logs as the authoritative source of information to know when a container exceeds [the memory allocation](/core-concepts/scaling/memory-limits#memory-management).

  * [Endpoint errors](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs#common-errors) occur when an app does not respond to a request. The existence and frequency of these errors are key indicators of issues affecting end users. Aptible recommends setting up alerts when runtime health check requests are failing as this will notify users when a portion of the containers are impacted, rather than waiting for all containers to fail before noticing an issue.

* Set up monitoring for database disk capacity and IOPS.

  * While disk capacity issues almost always cause obviously fatal issues, IOPS capacity exhaustion can also be incredibly impactful on application performance. Aptible recommends setting up alerts when users see sustained IOPS consumption near the limit for the disk. This will allow users to skip right from fielding "the application is slow" complaints right to identifying the root cause.

* Set up [application performance monitoring (APM)](/how-to-guides/observability-guides/setup-application-performance-monitoring) for applications.

  * Tools like New Relic or Datadog's APM can give users with great insights into how well (or poorly) specific portions of an application are performing - both from an end user's perspective, and from a per-function perspective. Since they run in the codebase, these tools are often able to shed light for users on what specifically is wrong much more accurately than combing through logs or container metrics.

* Set up external availability monitoring.

  * The ultimate check of the availability of an application comes not from monitoring the individual pieces, but the system as a whole. Services like [Pingdom](https://www.pingdom.com/) can monitor uptime of an application, including discovering problems with services like DNS configuration, which fall outside of the scope of the Aptible platform.
