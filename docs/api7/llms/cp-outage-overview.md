# Source: https://docs.api7.ai/enterprise/high-availability/cp-outage-overview.md

# Source: https://docs.api7.ai/enterprise/3.8.x/high-availability/cp-outage-overview.md

# Data Plane Resilience Overview

Resilience refers to a system's ability to withstand and recover from failures, disruptions, or unexpected events.

Consider situations where Data Plane (DP) nodes are unable to communicate with the Control Plane (CP). Potential causes include:

* Poor network connectivity between DP and CP instances
* CP database crash
* CP upgrade
* Resource contention on the CP host
* CP host hardware failure

In this chapter, you will learn how to implement the data plane (DP) resilience pattern, such that when the control plane (CP) becomes unavailable, the DP instances can still operate normally. This helps you formulate a disaster recovery plan and quickly resume mission-critical functions when the control plane (CP) becomes unavailable, ensuring the high availability of your system.

## DP Resilience Pattern[â](#dp-resilience-pattern "Direct link to DP Resilience Pattern")

API7 offers a fallback CP feature that helps you implement DP resilience, where a backup gateway node exports the latest CP-derived configuration to external storage. When the CP cannot be reached, traffic gateway nodes fetch the configuration from the external storage.

info

Backup gateway nodes do not expose HTTP or HTTPS ports to handle API traffic. They are not counted toward the API7 Enterprise license limit.

The following diagram illustrates the normal operation, where the Control Plane (CP) pushes configuration to traffic gateway nodes and the backup gateway node, and the backup node periodically exports the configuration to external storage:

<!-- -->

<br />

During the fallback operation, traffic gateway nodes fetch configuration from external storage when the Control Plane (CP) cannot be reached:

<!-- -->

<br />

The fallback CP feature supports Azure Blob Storage and AWS S3 as external storage backends.
