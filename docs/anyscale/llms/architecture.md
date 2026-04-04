# Source: https://docs.anyscale.com/get-started/architecture.md

# Platform architecture

[View Markdown](/get-started/architecture.md)

# Platform architecture

Anyscale uses a dual-plane architecture that separates the orchestration layer from your data and compute resources. This architecture ensures data sovereignty, enables geographic distribution, and provides network isolation while maintaining centralized cluster orchestration.

This page describes the technical architecture of the Anyscale platform and how components interact to deploy and manage Ray clusters. For more details on networking, see [Detailed network flows for Anyscale](/networking/overview.md).

## Overview[​](#overview "Direct link to Overview")

Anyscale simplifies building, running, and managing Ray applications by automating the creation, scaling, and termination of cloud resources required to run Ray workloads. The platform divides these responsibilities between two components:

* **Anyscale control plane**: Orchestrates and manages all platform operations.
* **Customer data plane**: Deploy and run your Ray clusters in your own cloud environment.

The following diagram shows how these components interact:

![Diagram showing Anyscale\&#39;s dual-plane architecture with control plane managing multiple customer data planes](/assets/images/anyscale-b039955af98833e26b57e032e64c5d24.png)

## Anyscale control plane[​](#control-plane "Direct link to Anyscale control plane")

The Anyscale control plane provides centralized orchestration for all Ray clusters across customer deployments. It operates as a multi-tenant SaaS application in Anyscale-managed infrastructure.

### Control plane responsibilities[​](#control-plane-responsibilities "Direct link to Control plane responsibilities")

The control plane handles:

* Cluster lifecycle management including provisioning, scaling, and termination.
* Resource scheduling and autoscaling decisions.
* User authentication and authorization.
* Cluster state and configuration management.
* Metrics and log aggregation from data planes.

## Customer data plane[​](#data-plane "Direct link to Customer data plane")

The customer data plane hosts Ray clusters within customer-owned cloud accounts or Kubernetes clusters. Each data plane operates independently with complete network and data isolation.

### Data plane components[​](#data-plane-components "Direct link to Data plane components")

The data plane includes:

* Ray clusters with head and worker nodes.
* Cloud compute resources: VMs or Kubernetes pods.
* Storage for logs, checkpoints, and artifacts.
* Network infrastructure configured by the customer.
* Container images for cluster nodes.

### Architectural benefits[​](#architectural-benefits "Direct link to Architectural benefits")

The separation of control and data planes enables:

* **Network isolation**: Customer workloads operate within their own network boundaries without traversing Anyscale infrastructure.
* **Geographic distribution**: Deploy data planes in any AWS, Google Cloud, or Azure region, or run Anyscale on Kubernetes anywhere.
* **Fault isolation**: Issues in one data plane don't affect other customers or the control plane.
* **Compliance alignment**: Local data plane deployment meets data residency and sovereignty requirements.
* **Scaling independence**: Each data plane scales based on its workload requirements without affecting shared infrastructure.

## Security architecture[​](#security-architecture "Direct link to Security architecture")

### Authentication mechanisms[​](#authentication "Direct link to Authentication mechanisms")

The platform uses cloud provider authentication mechanisms for cross-plane communication:

* **AWS**: Cross-account IAM roles with temporary credentials.
* **Google Cloud**: Workload Identity Federation.
* **Azure**: Entra ID cross-tenant JSON Web Tokens.
* **Kubernetes**: Service account tokens.

### Communication protocols[​](#communication-protocols "Direct link to Communication protocols")

All communication between control plane and data planes uses:

* **Encryption in transit**: TLS 1.2+ for all API calls and data transfers.
* **Role-based authentication**: Cloud provider IAM for resource management.
* **Audit logging**: The platform logs control plane API calls for monitoring.

## Data and control separation[​](#data-control-separation "Direct link to Data and control separation")

The platform maintains clear separation between control operations and data operations:

### Control operations[​](#control-operations "Direct link to Control operations")

The control plane manages cluster lifecycle through cloud provider APIs:

* Provisions and terminates cloud resources in customer accounts.
* Manages cluster scaling based on workload demands.
* Monitors cluster health and initiates recovery when needed.
* Maintains cluster configurations and metadata.

### Data operations[​](#data-operations "Direct link to Data operations")

Application data remains within the customer data plane:

* Workloads read and write directly to customer storage.
* Ray distributes data across cluster nodes without routing through Anyscale.
* Logs persist in customer-owned storage buckets.
* The platform aggregates metrics for monitoring while raw data stays local.

## Platform operations[​](#platform-operations "Direct link to Platform operations")

This section describes how user actions translate into platform operations across the control and data planes.

### Cluster provisioning flow[​](#cluster-provisioning "Direct link to Cluster provisioning flow")

When users request cluster creation, the following sequence executes:

1. **Authentication and authorization**: The control plane validates the user's CLI token or SSO session, then verifies permissions for the requested operation.

2. **Configuration processing**: The control plane accepts and validates:

   * Target Anyscale cloud specification for data plane location.
   * [Compute configuration](/configuration/compute.md) defining instance types and quantities.
   * [Container image](/container-image.md) specification for Ray runtime environment.

3. **Cloud resource provisioning**: If using Anyscale on Kubernetes, including AKS, EKS, and GKE, the control plane posts instructions for the Anyscale operator. Kubernetes handles all resource provisioning.

   If you use the virtual machine stack on AWS or Google Cloud, the control plane assumes a cross-account IAM role (AWS) or uses Workload Identity Federation (Google Cloud) to directly acquire resources in your cloud provider account using cloud provider APIs, tagging and organizing these resources according to the Anyscale cloud configuration.

4. **Cluster initialization**:

   * Newly provisioned nodes establish secure connection to control plane.
   * Nodes register their status and pull configuration details.
   * Nodes retrieve container images from the registry.
   * Ray runtime initializes with specified dependencies.

### Runtime communication patterns[​](#runtime-communication "Direct link to Runtime communication patterns")

During cluster operation, multiple communication channels maintain system state:

**Health monitoring**:

* Clusters send periodic heartbeats to the control plane.
* Control plane tracks node status and cluster health metrics.
* Failed health checks trigger automatic recovery procedures.

**Autoscaling coordination**:

* Ray autoscaler requests flow to the control plane for processing.
* Control plane evaluates resource availability and cost constraints.
* Scaling decisions execute through cloud provider APIs.
* This design minimizes IAM permissions required on cluster nodes.

**Workload execution**:

* User code runs entirely within the data plane.
* Application logs persist to customer-owned storage buckets.
* The control plane collects metrics locally and aggregates them.
* Data processing occurs without traversing Anyscale infrastructure.

### User access patterns[​](#user-access "Direct link to User access patterns")

Users interact with running clusters through multiple pathways:

**API and console access**:

* Control plane provides cluster status and management operations.
* Control plane vends temporary access tokens for secure cluster communication.
* Console displays real-time cluster metrics and logs.

**Direct cluster access**:

* Ray dashboard, Jupyter notebooks, and Grafana connect directly to cluster endpoints.
* Job submission uses cluster IP addresses without control plane routing.
* SSH access available for debugging and development workflows.
* All connections use control-plane-authenticated tokens.

### Cluster termination flow[​](#cluster-termination "Direct link to Cluster termination flow")

The termination process ensures clean resource cleanup:

1. **Termination request**: User initiates through console, API, SDK, or CLI.

2. **Graceful shutdown**: Control plane signals cluster to stop accepting new work.

3. **Resource cleanup**:

   <!-- -->

   * Control plane assumes cloud provider role.
   * Platform terminates cloud resources through provider APIs.
   * Persistent data remains in customer storage.

4. **State finalization**: Control plane updates cluster records and releases allocated quotas.
