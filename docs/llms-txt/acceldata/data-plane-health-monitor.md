# Source: https://docs.acceldata.io/documentation/data-plane-health-monitor.md

# Data Plane Health Monitor

The **Data Plane Observability Dashboard** in ADOC provides a real-time view of system health and performance, but it focuses specifically on the Data Plane and its components. This dashboard helps operations and data platform teams quickly assess the status of:

- Data pipeline execution within the Data Plane
- Underlying Kubernetes infrastructure used by the Data Plane
- Resource usage like CPU and memory
- Logs and system-level events tied to Data Plane services

Note This dashboard does not monitor your entire data ecosystem (like data sources, data warehouses, or BI tools). It only shows what’s happening inside the Data Plane environment.

## Core Dashboard Components

### 1. Cluster Overview

Shows the health of your entire Kubernetes cluster at a glance to detect capacity issues or stuck pods immediately

- Node readiness: Ensures all servers (nodes) are up and running
- CPU & Memory usage (Nodes): Current usage vs capacity
- Pod readiness & usage: Tracks workload health and resource consumption

### 2. Node-Level Performance

Gives detailed metrics for each individual node. These metrics are useful for load-balancing, identifying over or under utilized nodes.

- CPU & memory usage: Actual use, requested vs limited
- Pod density: How many pods each node is handling
- Node metadata: Age, labels, and system roles for troubleshooting

### 3. Workloads & Pods

To ensure data processes are running smoothly like whether pods are restarting too often, or want to view logs, the dashboard provides dashboards for monitoring operational units (e.g., jobs, microservices, ETL processes).

- Workloads readiness: Number of healthy workloads vs total
- Pod health & resource usage: CPU, memory, restarts, status icons
- Live logs: View real-time pod logs directly in ADOC

### 4. Services & Replica Sets

To ensure that the critical services are running as expected, ADOC provides insight into microservice-level stability and reliability.

- Service health: Uptime and namespace details
- Replica tuning: Desired vs actual pod count
- Replica metadata: Age, generation, and rollout history

### 5. Config Maps & Ingresses

Helps you manage configuration and routing rules and is visible for auditing and compliance.

- Config Maps: View and audit configuration settings
- Ingresses: Monitor external access rules and endpoints

### 6. User Profile & Access Summary

To provide transparency regarding your identity and capabilities within the system. ADOC includes access token details, such as issuance and expiration times, as well as authentication methods. Additionally, it displays user roles, enabling you to comprehend and confirm your assigned permissions. This is essential for maintaining security, conducting access audits, and ensuring compliance with relevant standards.