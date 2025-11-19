# Source: https://www.aptible.com/docs/core-concepts/architecture/reliability-division.md

# Reliability Division of Responsibilities

## Overview

Aptible is a Platform as a Service that simplifies infrastructure management for developers. However, it's important to note that users have certain responsibilities as well.

This document builds on the [Divisions of Responsibility](https://www.aptible.com/assets/deploy-division-of-responsibilities.pdf) between Aptible and users, focusing on use cases related to Reliability and Disaster Recovery. The goal is to provide users with a clear understanding of the monitoring and processes that Aptible manages on their behalf, as well as areas that are not covered.

While this document covers essential aspects, it's important to remember that it doesn't include all responsibilities in detail. Nevertheless, it's a valuable resource to help users navigate their infrastructure responsibilities effectively within the Aptible ecosystem.

## Uptime

Uptime refers to the percentage of time that the Aptible platform is operational and available for use. Aptible provides a 99.95% uptime SLA guarantee for dedicated stacks and on the Enterprise Plan.

Aptible

* Aptible will send notifications of availability incidents for all dedicated environments and corresponding resources, including but not limited to stacks and databases.

  * For service-wide availability incidents, Aptible will notify users of the incident within the Aptible Dashboard and our [Status Page](https://status.aptible.com/). For all other availability incidents on dedicated stacks, Aptible will notify the Ops Alert contact.
* Aptible will issue a credit for SLA breaches as defined by our SLA guarantee for dedicated stacks and organizations on the Enterprise Plan.

Users

* To receive Aptible’s 99.95% uptime SLA, Enterprise users are responsible for ensuring their critical resources, such as production environments, are provisioned on dedicated stacks.

* To receive email notifications of availability incidents impacting the Aptible platform, users are responsible for subscribing to email notifications on our [Status Page](https://status.aptible.com/).

* Users are responsible for providing a valid Ops Alert Contact. Ops Alert Contact should be reachable by [support@aptible.com](mailto:support@aptible.com)

## Maintenance

Maintenance can occur at any time, causing unavailability of Aptible resources (including but not limited to stacks, databases, VPNs, and log drains). Scheduled maintenance typically occurs between 9 pm and 9 am ET on weekdays, or between 6 pm and 10 am ET on weekends. Unscheduled maintenance may occur in situations like critical security patching.

Aptible

* Aptible will notify the Ops Alert contact of scheduled maintenance for dedicated stacks or service-wide with at least two weeks out whenever possible. However, there may be cases where Aptible provides less notice, such as AWS instance retirement, or no prior notice, such as critical security patching.

Users

* Users are responsible for providing a valid Ops Alert Contact.

## Hosts

Aptible

* Aptible is solely responsible for the host and the host's health. If a host becomes unhealthy, impacted containers will be moved to a healthy host. This extends to AWS-scheduled hardware maintenance.

## Databases

Aptible

* While Aptible avoids unnecessary database restarts, Aptible may restart your database at any time for the purposes of security or availability. This may include but is not limited to restarts which:

  * Resolve existing availability issue

  * Avoid an imminent, unavoidable availability issue that would have a greater impact than a restart

  * Resolve critical and/or urgent security incident

* Aptible restarts database containers that have exited (see: [Container Recovery](/core-concepts/architecture/containers/container-recovery)).

* Aptible restarts database containers that have run out of memory (see: [Memory Management](/core-concepts/scaling/memory-limits)).

* Aptible monitors database containers stuck in restart loops and will take action to resolve the root cause of the restart loop.

  * Common cases include the database running out of disk space, memory, or incorrect/invalid settings. The on-call Aptible engineer will contact the Ops Alert contact with information about the root cause and action taken.

* Aptible's SRE team receives a list of databases using more than 98% of disk space roughly once a day. Any action taken is on a "best effort" basis, and at the discretion of the responding SRE. Typically, the responding SRE will scale the database and notify the Ops Alert contact, but depending on usage patterns and growth rates, they may instead contact the Ops Alert contact before taking action.

  * Aptible is considering automating this process as part of our roadmap. With this automation, any Database that exceeds 99% disk utilization will be scaled up, and the Ops Alert contact will be notified.

* Aptible ensures that database replicas are distributed across availability zones.

  * There are times when this may not be possible. For example, when recovering a primary or replica after an outage, the fastest path to recovery may be temporarily running both a primary and replica in the same availability zone. In these cases, the Aptible SRE team is notified and will reach out to schedule a time to migrate the database to a new availability zone.

* Aptible automatically takes backups of databases once a day and monitors for failed backups. Backups are created via point-in-time snapshots of the database's disk. As a result, taking a backup causes no performance degradation. The resulting backup is not stored on the primary volume.

* If enabled as part of the retention policy, Aptible copies database backups to another region as long as another geographically appropriate region is available.

Users

* Users are responsible for monitoring performance, resource consumption, latency, network connectivity, or any other metrics for databases other than the metrics explicitly outlined above.

* Users are responsible for monitoring database replica health or replication lag.

* To achieve cross-region replication, users are responsible for enabling cross-region replication.

## Apps

Aptible

* While Aptible avoids unnecessary restarts, Aptible may restart your app at any time. This may include but is not limited to restarts which:

  * Resolve existing availability issue

  * Avoid an imminent, unavoidable availability issue that would have a greater impact than a restart

  * Resolve critical and/or urgent security incident

* Aptible automatically restarts containers that have exited (see: [Container Recovery](/core-concepts/architecture/containers/container-recovery)).

* Aptible restarts containers that have run out of memory (see: [Memory Management](/core-concepts/scaling/memory-limits)).

* Aptible monitors App host disk utilization. When Apps that are writing to the ephemeral file system cause utilization issues, we may restart the Apps to reset the container filesystem back to a clean state.

Users

* Users are responsible for ensuring your container correctly exits (see: "Cases where Container Recovery will not work" in [Container Recovery](/core-concepts/architecture/containers/container-recovery)). If a container is not correctly designed to exit on failure, Aptible does not restart it and has no monitoring that will catch that failure condition.

* Users are responsible for monitoring app containers stuck in restart loops.

* Aptible does not proactively run your apps in another region, nor do we retain a copy of your code or Docker Images required to fail your Apps over to another region. In the event of a regional outage, users are responsible for coordinating with Aptible to restore apps in a new region.

* Users are responsible for monitoring performance, resource consumption, latency, network connectivity, or any other metrics for apps other than the metrics explicitly outlined above.

## VPNs

Aptible

* Aptible provides connectivity between resource(s) in an Aptible customer's [Dedicated Stack](/core-concepts/architecture/stacks) and resource(s) in a customer-specified peer network. Aptible is responsible for the configuration and setup of the Aptible VPN peer. (See [Site-to-site VPN Tunnels](/core-concepts/integrations/network-integrations#site-to-site-vpn-tunnels))

Users

* Users are responsible for coordinating the configuration of the non-Aptible peer.

* Users are responsible for monitoring the connectivity between resources across the VPN Tunnel (this is the responsibility of the customer and/or their partner network operator).
