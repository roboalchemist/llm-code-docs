# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/minimize-downtown-outages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimize Downtime Caused by AWS Outages

> Learn how to optimize your Aptible resource to reduce the potential downtime caused by AWS Outages

## Overview

Aptible is designed to provide a baseline level of tools and services to minimize downtime from AWS outages. This includes:

* Automated configuration of [availability controls](https://www.aptible.com/secured-by-aptible/) designed to prevent outages

* Expert SRE response to outages backed by [our 99.95% Uptime SLA](https://www.aptible.com/legal/service-level-agreement/) (Enterprise Plan only)

* Simplification of additional downtime prevention measures (as described in the rest of this guide)

In this guide, we will cover into the various configurations and steps that can be implemented to enhance the Recovery Point Objective (RPO) and Recovery Time Objective (RTO). These improvements will assist in ensuring a more seamless and efficient recovery process in the event of any disruptions or disasters.

## Outage Notifications

If you think you are experiencing an outage, check Aptible's [Status Page](https://status.aptible.com/). We highly recommend subscribing to Aptible Status Page Notifications. If you still have questions, contact [Support](/how-to-guides/troubleshooting/aptible-support).

> **Recommended Action:**

> 🎯 [Subscribe to Aptible Status Page Notifications](https://status.aptible.com/)

## Understanding AWS Infrastructure

Aptible runs on AWS so it helps to have a basic understanding of AWS's concept of [Regions and Availability Zones (AZs)](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).

## Regions

AWS regions are physical locations where AWS data centers are clustered. Communication between regions has a much higher-latency compared to communication within the same region and the farther two regions are from one another, the higher the latency. This means that it's generally better to deploy resources that work together within the same region.

Aptible Stacks are deployed in a single region in order to ensure resources can communicate with minimal latency.

## Availability Zones

AWS regions are comprised of multiple Availability Zones (AZs). AZs are sets of discrete data centers with redundant power, networking, and connectivity in a region. As mentioned above, communication within a region, and therefore between AZs in the same region, is very low latency. This allows resources to be distributed across AZs, increasing their availability, while still allowing them to communicate with minimal latency.

Aptible Stacks are distributed across 2 to 4 AZs depending on the region they're in. This enables all Stacks to distribute resources configured for high availability across AZs.

## High Availability

High Availability (HA) refers to distributing resources across data centers to increase the likelihood that one of the resources will be available at any given point in time.

As described above, Aptible Stacks will automatically distribute resources across the AZs in their region in order to maximize availability. Specifically, it does this by:

* Deploying the Containers for [Services scaled to multiple Containers](/core-concepts/scaling/overview#horizontal-scaling) across AZs.

* Deploying [Database Replicas](/core-concepts/managed-databases/managing-databases/replication-clustering) to a different AZ than the source Database is deployed to.

This alone enables you to be able to handle most outages and doesn't require a lot of effort which is why we recommend scaling production Services to at least 2 Containers and creating replicas for production Databases in the [Best Practices Guide](https://www.aptible.com/docs/best-practices-guide).

## Failover

Failover is the process of switching from one resource to another, generally in response to an outage or other incident that renders the resource unavailable. Some resources support automated failover whereas others require some manual intervention.

For Apps, Aptible [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) perform [Runtime Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#runtime-health-checks) to determine the status of App Containers and only send traffic to those that are considered "healthy". This means that all HTTP(S) Endpoints on Services scaled to 2 or more Containers will automatically be prepared for most minor outages.

Most Database types support manual failover in the form of promoting a replica and updating all of the Apps that used the original Database to use the promoted replica, instead. [MongoDB](/core-concepts/managed-databases/supported-databases/mongodb) can dynamically failover between nodes in a cluster, similar to how HTTP(S) Endpoints only route traffic to "healthy" Containers, which enables them to handle minor outages without any action but can make multi-region failover more difficult. See the documentation for your [Database Type](/core-concepts/managed-databases/supported-databases/overview) for details on setting up replication and failing over to a replica.

## Configuration and Planning

Organizations should decide how much downtime they can tolerate for their resources as the more fault-proof a solution is, the more it costs. We recommend planning for most common outages as Aptible makes it fairly easy to do so.

## Coverage for most outages

*Maturity Level: Standard*

The majority of AWS outages are limited hardware or networking failures affecting a small number of machines. Frequently this affects only a single [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html), as AZs are isolated by design to share the minimum common causes of failures. Aptible's SRE team is notified in the event of AWS outages and responds to restore service based on what AWS resources are available. Most outages are able to be resolved in under 30 minutes by action of either AWS or Aptible without user action being required.

### Apps

The strongest basic step for making Apps resilient to most outages is [scaling each Service](https://www.aptible.com/docs/best-practices-guide#services) to 2 or more Containers. Aptible automatically schedules Containers to be run on hosts in different availability zones. In an outage affecting a single availability zone, traffic will be served only to Containers which are reachable and passing [health checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#release-health-checks). Optimizing your App image to minimize tasks on container startup (such as installing or configuring software which could be built into the image instead) will allow Containers to be restarted more quickly to replace unhealthy or unreachable Containers and restore full capacity of the Service.

> **Recommended Action:**

> 🎯 [Scale Apps to 2+ Containers](https://dashboard.aptible.com/controls/12/implementation?scope=4591%2C4115%2C2431%2C2279%2C1458%2C111%2C1\&sort=cumulativeMetrics.statusSort%3Aasc)

### Databases

The simplest form of recovery that's available to all Database types is restoring one of the [Database's Backups](/core-concepts/managed-databases/managing-databases/database-backups) to a new Database. However, Aptible automatically backups up Databases daily so the latest backup may be missing up to 24 hours of data so this approach is generally only recommended as a last resort.

[Replicas](/core-concepts/managed-databases/managing-databases/replication-clustering), on the other hand, continuously stream data from their source Database so they're usually not more than a few seconds behind at any point in time. This means that replicas can be failed over to in the event that the source Database is unavailable for an extended period of time with minimal data loss. As mentioned in the [High Availability](/how-to-guides/platform-guides/minimize-downtown-outages#high-availability) section, we recommend creating a replica for all production Databases that support replication. See the documentation for your [Database Type](/core-concepts/managed-databases/supported-databases/overview) for details on setting up replication and failing over to a replica.

> **Recommended Action:**

> 🎯 [Implement Database Replication and Clustering](https://dashboard.aptible.com/controls/14/implementation?scope=4591%2C4115%2C2431%2C2279%2C1458%2C111%2C1\&sort=cumulativeMetrics.statusSort%3Aasc)

## Coverage for major outages

*Maturity Level: Advanced*

Major outages are much more rare and cost more to prepare for. See the [pricing page](https://www.aptible.com/pricing-plans/) for the current costs for each resource type. As such, organizations should evaluate the cost of preparing for an outage like this against the likelihood and impact it would have on their business before implementing these solutions.

To date, there's only been one AWS regional outage that would require this level of planning to be prepared for.

### Stacks

Since Stacks are deployed in a single region, an additional dedicated Stack is required in order to be able to handle region-wide outages. Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) if you'd like to provision an additional dedicated Stack.

When choosing what region to use as a backup, keep in mind that the further two regions are from each other the more latency there will be between them. Looking at the region that Aptible copies Backups to is a good starting point if you aren't sure.

You'll likely want to peer your two Stacks so that their resources can communicate with one another. In other words, this allows resources on one Stack can connect to Databases and Internal Endpoints on the other. This is also something that [Aptible Support](/how-to-guides/troubleshooting/aptible-support) can set up for you.

> **Recommended Action:**

> 🎯 [Request a backup Dedicated Stack to be provisioned and/or peered](http://contact.aptible.com/)

### Apps

For a major outage, Apps will require manual intervention to failover to a different Stack in a healthy region. If you need a new Dedicated Stack provisioned as above, deploying your App to the new Stack will be equivalent to deploying it from scratch. If you maintain a Dedicated Stack in another region to be prepared in advance for a regional failure, there are several things you can do to speed the failover process.

You can deploy your production App's code to a second Aptible App on the backup Stack. Keeping the code and configuration in sync with your production Stack will allow you to failover to this App more quickly. To save costs, you can also scale all Services on this backup App to 0 Containers. In this case, failover will require [scaling each Service](/core-concepts/scaling/overview) up from 0 before redirecting traffic to this App. Optimizing your App image to minimize startup time will speed up this process.

You will need to update DNS to point traffic toward Endpoints on the new App. Provisioning these Endpoints ahead of time will speed this process but will incur a small ongoing cost per Endpoint to have ready. Lowering DNS TTL will reduce failover time, and configuring these backup Endpoints with [custom certificates](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) is suggested to avoid the effort required to keep [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls) certificates current on these Endpoints.

> **Recommended Action:**

> 🎯 [Deploy Apps to your backup Dedicated Stack](http://contact.aptible.com/)

> 🎯 [Provision Endpoints on your backup Dedicated Stack](/core-concepts/managed-databases/connecting-databases/database-endpoints)

### Databases

The options for preparing for a major outage are the same as for other outages, restore a [Backup](/core-concepts/managed-databases/managing-databases/database-backups) or failover to a [Replica](/core-concepts/managed-databases/managing-databases/replication-clustering). The main difference here is that the resulting Database would be on a Stack in a different region and you'd have to continue operating on this Stack indefinitely or fail back over to the original Stack once it was back online.

Additionally, Aptible currently does not allow you to specify what Environment to create the Replica in with the [`aptible db:replicate` CLI command](/reference/aptible-cli/cli-commands/cli-db-replicate) so Replicas are always created in the same Environment as the source Database. If you'd like to set up a Replica in another region, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for assistance.

> **Recommended Action:**

> 🎯 [Enable Cross-Region Copy Database Backups](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal)

> 🎯 [Request Replica(s) be moved to your backup Dedicated Stack](http://contact.aptible.com/)
