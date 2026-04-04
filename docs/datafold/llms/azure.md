# Source: https://docs.datafold.com/datafold-deployment/dedicated-cloud/azure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Datafold VPC Deployment on Azure

> Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on Azure.

<Note>
  **INFO**

  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## Create a Domain Name (optional)

You can either choose to use your domain (for example, `datafold.domain.tld`) or to use a Datafold managed domain (for example, `yourcompany.dedicated.datafold.com`).

### Customer Managed Domain Name

Create a DNS A-record for the domain where Datafold will be hosted. For the DNS record, there are two options:

* **Public-facing:** When the domain is publicly available, we will provide an SSL certificate for the endpoint.
* **Internal:** It is also possible to have Datafold disconnected from the internet. This would require an internal DNS (for example, Azure DNS) record that points to the Datafold instance. It is possible to provide your own certificate for setting up the SSL connection.

Once the deployment is complete, you will point that A-record to the IP address of the Datafold service.

## Create a New Subscription

For isolation reasons, it is best practice to [create a new subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription) within your Microsoft Entra directory/tenant. Please call it something like `yourcompany-datafold` to make it easy to identify.

## Set IAM Permissions

Go to **Microsoft Entra ID** and navigate to **Users**. Click **Add**, **User**, **Invite external user** and add the Datafold engineers.

Navigate to the subscription you just created and go to **Access control (IAM)** tab in the side bar.

* Navigate to the subscription you just created. Go to **Access control (IAM)**. Under **Add** select **Add role assignment**.
* Under **Role**, navigate to **Priviledged administrator roles** and select **Owner**.
* Under **Members**, click **Select members** and add the Datafold engineers.
* When you are done, select **Review + assign**.

The owner role is only required temporarily while we configure and test the initial Datafold deployment. We'll inform you when it is ok to revoke this permission.

### Required APIs

The following Azure APIs need to be enabled to run Datafold:

1. [Microsoft.ContainerService](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Container%20Service)
2. [Microsoft.Network](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Network)
3. [Microsoft.Compute](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Compute)
4. [Microsoft.KeyVault](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Key%20Vault)
5. [Microsoft.Storage](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/Storage)
6. [Microsoft.DBforPostgreSQL](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/PostgreSQL)

Once the access has been granted, make sure to notify Datafold so we can initiate the deployment.

# Datafold Azure infrastructure details

This document provides detailed information about the Azure infrastructure components deployed by the Datafold Terraform module,
explaining the architectural decisions and operational considerations for each component.

## Managed disks

The Datafold application requires 3 managed disks for persistent storage, each deployed as encrypted Azure managed disks in the
primary availability zone. This also means that pods cannot be deployed outside the availability zone of these disks, because
the nodes wouldn't be able to attach them.

**ClickHouse data disk** serves as the analytical database storage for Datafold. ClickHouse is a columnar database that excels
at analytical queries. The default 40GB allocation usually provides sufficient space for typical deployments, but it can be
scaled up based on data volume requirements. The StandardSSD\_LRS disk type with configurable IOPS and throughput ensures
consistent performance for analytical workloads.

**ClickHouse logs disk** stores ClickHouse's internal logs and temporary data. The separate logs disk prevents log data from
consuming IOPS and I/O performance from actual data storage.

**Redis data disk** provides persistent storage for Redis, which handles task distribution and distributed locks in the Datafold
application. Redis is memory-first but benefits from persistence for data durability across restarts. The 50GB default size
accommodates typical caching needs while remaining cost-effective.

All managed disks are encrypted by default using Azure-managed encryption keys, ensuring data security at rest. The disks are
deployed in the first availability zone to minimize latency and simplify backup strategies. For Premium and Ultra SSD disk
types, IOPS and throughput can be configured to optimize performance for specific workloads.

## Application Gateway

The Application Gateway serves as the primary entry point for all external traffic to the Datafold application. The module
offers 2 deployment strategies, each with different operational characteristics and trade-offs.

**External Application Gateway Deployment** (the default approach) creates an Azure Application Gateway through Terraform.
This approach provides centralized control over load balancer configuration and integrates well with existing Azure
infrastructure. The Application Gateway automatically handles SSL termination, health checks, and traffic distribution across
Kubernetes pods. This method is ideal for organizations that prefer infrastructure-as-code management and want consistent
load balancer configurations across environments.

**Kubernetes-Managed Application Gateway** deployment sets `deploy_lb = false` and relies on the Azure Application Gateway
Ingress Controller (AGIC) running within the AKS cluster. This approach leverages Kubernetes-native load balancer management,
allowing for dynamic scaling and easier integration with Kubernetes ingress resources. The controller automatically provisions
and manages Application Gateways based on Kubernetes service definitions, which can be more flexible for applications that
need to scale load balancer resources dynamically.

Both Application Gateways apply the currently recommended and strictest SSL policies: `AppGwSslPolicy20220101S` and security
settings.

The choice between these approaches often depends on operational preferences and existing infrastructure patterns. External
deployment provides more predictable resource management, while Kubernetes-managed deployment offers greater flexibility for
dynamic workloads.

**Security** A network security group shared between the Application Gateway and the AKS nodes allows traffic to reach only
the AKS nodes and nothing else. The Application Gateway allows traffic to land directly into the AKS private subnet.

**Certificate** The certificate can be pre-created by the customer and then attached, or a cloud-managed certificate can be
created on the fly. The application will not function without HTTPS, so a certificate is mandatory. After the certificate is
created either manually or through this repository, it must be validated by the DNS administrator by adding a CNAME record.
This puts the certificate in "Issued" state. The certificate cannot be found when it's still provisioning.

## AKS cluster

The Azure Kubernetes Service (AKS) cluster forms the compute foundation for the Datafold application, providing a managed
Kubernetes environment optimized for Azure infrastructure.

**Network Architecture** The entire cluster is deployed into private subnets. This means the data plane is not reachable from
the Internet except through the Application Gateway. A NAT gateway allows the cluster to reach the internet (egress traffic)
for downloading pod images, optionally sending Datadog logs and metrics, and retrieving the version to apply to the cluster
from our portal. The control plane is accessible via a private endpoint using a Private Link setup from, for example, a VPN
VNet elsewhere. This is a private+public endpoint, so the control plane can also be made accessible through the Internet, but
then the appropriate CIDR restrictions should be put in place.

For a typical dedicated cloud deployment of Datafold, only around 100 IPs are needed. This assumes 3 Standard\_DS2\_v2 instances
where one node runs ClickHouse+Redis, another node runs the application, and a third node may be put in place when version
rollovers occur. This means a subnet of size /24 (253 IPs) should be sufficient to run this application.

By default, the repository creates a VNet and subnets, but by specifying the VNet ID of an already existing VNet, the cluster
and Application Gateway get deployed into existing network infrastructure. This is important for some customers where they
deploy a different architecture without NAT gateways, firewall options that check egress, and other DLP controls.

**Add-ons**

The cluster includes several essential add-ons configured through Terraform:

**Workload Identity** is enabled to provide fine-grained IAM permissions to Kubernetes pods without requiring Azure credentials
in container images. This is essential for ClickHouse to access Azure Storage for backups and other services.

**Ingress Application Gateway** is integrated with the cluster to handle external traffic routing and SSL termination. The
Application Gateway Ingress Controller (AGIC) manages the Application Gateway configuration based on Kubernetes ingress resources.

**Storage Profile** includes the Azure Disk CSI driver for persistent volume management, file driver for Azure Files, and
snapshot controller for volume snapshots. These components enable dynamic provisioning and management of Azure storage resources.

**Node Management** supports up to three managed node pools, allowing for workload-specific resource allocation. Each node
pool can be configured with different VM sizes, enabling cost optimization and performance tuning for different application
components. The cluster autoscaler automatically adjusts node count based on resource demands, ensuring efficient resource
utilization while maintaining application availability. One typical way to deploy is to let the application pods go on a wider
range of nodes, and set up tolerations and labels on the second node pool, which are then selected by both Redis and
ClickHouse. This is because Redis and ClickHouse have restrictions on the zone they must be present in because of their
disks, and ClickHouse is a bit more CPU intensive. This method optimizes CPU performance for the Datafold application.

**Security Features** include Azure Workload Identity, which provides fine-grained IAM permissions to Kubernetes pods without
requiring Azure credentials in container images. This approach enhances security by following the principle of least privilege
and integrates seamlessly with Azure security services. The cluster also supports private clusters with restricted control
plane access and network policies for pod-to-pod communication control.

## IAM Roles and Permissions

The IAM architecture follows the principle of least privilege, providing specific permissions only where needed. Service
accounts in Kubernetes are mapped to IAM roles using Azure Workload Identity, enabling secure access to Azure services without
embedding credentials in application code.

**Azure Disk CSI Controller Role** enables the Kubernetes cluster to manage Azure managed disks dynamically. This role allows
pods to request persistent storage that's automatically provisioned and attached to the appropriate nodes or attach static
disks. The permissions are scoped to only the Azure Disk operations needed for disk lifecycle management.

**Application Gateway Ingress Controller Role** provides the permissions necessary for Kubernetes to manage Azure Application
Gateways. This includes creating backend address pools, registering and deregistering targets, and managing Application
Gateway listeners. The controller can automatically provision Application Gateways based on Kubernetes service definitions,
enabling seamless integration between Kubernetes and Azure networking.

**Cluster Autoscaler Role** allows the cluster to automatically scale node pools based on resource demands. This role can
describe and modify Virtual Machine Scale Sets, enabling the cluster to add or remove nodes as needed. The autoscaler considers
pod resource requests and node capacity when making scaling decisions.

**Datafold Roles** Datafold has roles per pod pre-defined which can have their permissions assigned when they need them. At
the moment, we have two specific roles in use. One is for the ClickHouse pod to be able to make backups and store them on
Azure Storage. The other is for the use of the Azure OpenAI service for our AI offering.

These roles are automatically created and configured when the cluster is deployed, ensuring that the necessary permissions are
in place for the cluster to function properly. The use of Azure Workload Identity means that these permissions are automatically
rotated and managed by Azure, reducing security risks associated with long-lived credentials.

## Azure Database for PostgreSQL

The Azure Database for PostgreSQL Flexible Server instance serves as the primary relational database for the Datafold
application, storing user data, configuration, and application state.

**Storage Configuration** starts with a 32GB initial allocation that can automatically scale up to 100GB based on usage
patterns. This auto-scaling feature prevents storage-related outages while avoiding over-provisioning. For typical deployments,
storage usage remains under 200GB, though some high-volume deployments may approach 400GB. The GP\_Standard storage type
provides consistent performance with configurable IOPS and throughput.

**High Availability** is intentionally disabled by default, meaning the database runs in a single availability zone. This
configuration reduces costs and complexity while still providing excellent reliability. The database includes automated backups
with 7-day retention, ensuring data can be recovered in case of failures. For organizations requiring higher availability,
multi-zone deployment can be enabled, though this significantly increases costs.

**Security and Encryption** always encrypts data at rest using Azure-managed encryption keys. The database is deployed in
private subnets with network security groups that restrict access to only the AKS cluster, ensuring network-level security.
The database supports Azure Private Link for secure, private connectivity from the VNet.

The database configuration prioritizes operational simplicity and cost-effectiveness while maintaining the security and
reliability required for production workloads. The combination of automated backups, encryption, and network isolation
provides a robust foundation for the application's data storage needs.
