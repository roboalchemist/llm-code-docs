# Source: https://docs.datafold.com/datafold-deployment/dedicated-cloud/gcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Datafold VPC Deployment on GCP

> Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on GCP.

<Note>
  **INFO**

  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## Create a Domain Name (optional)

You can either choose to use your domain (for example, `datafold.domain.tld`) or to use a Datafold managed domain (for example, `yourcompany.dedicated.datafold.com`).

### Customer Managed Domain Name

Create a DNS A-record for the domain where Datafold will be hosted. For the DNS record, there are two options:

* **Public-facing:** When the domain is publicly available, we will provide an SSL certificate for the endpoint.
* **Internal:** It is also possible to have Datafold disconnected from the internet. This would require an internal DNS (for example, AWS Route 53) record that points to the Datafold instance. It is possible to provide your own certificate for setting up the SSL connection.

Once the deployment is complete, you will point that A-record to the IP address of the Datafold service.

## Create a New Project

For isolation reasons, it is best practice to [create a new project](https://console.cloud.google.com/projectcreate) within your GCP organization. Please call it something like `yourcompany-datafold` to make it easy to identify:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=723db80c5ab11885a5c68f4783de2795" data-og-width="1972" width="1972" data-og-height="906" height="906" data-path="images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=66c280f699f6c7fb8dd2030440654b30 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ae23c8cf867466a00a27c8bfb66925aa 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9b22f156d54fbb52d9c51757be289d1a 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d624b674fad3bf9cfdbe937843ca0cac 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=71c9fb467747ddce2ad410f0f13c7e67 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_create-2b10d24df91f7f09ff3bd8c216edb511.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=83160e2df8dd689757d55c9a27877f76 2500w" />
</Frame>

After a minute or so, you should receive confirmation that the project has been created. Afterward, you should be able to see the new project.

## Set IAM Permissions

Navigate to the **IAM** tab in the sidebar and click **Grant Access** to invite Datafold to the project.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1f120a9192d42aa0f142a68ce3cfd12c" data-og-width="1954" width="1954" data-og-height="720" height="720" data-path="images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ebcc1af578ef3bfae3d84d10a15b5e7 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b0f878553c3ebdd32f60a768cf149844 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0feac9134f245a4083d5849a6e2a5be2 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9362c81f7959768af1098cc2449989dc 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=138a377b7b8e9959c8ff5e4674833041 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_gcp_iam-7c29989550ec1f3636e6270d866fe740.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=00dabc22d0cca62db4b4ce56c721e458 2500w" />
</Frame>

Add your Datafold solutions engineer as a **principal**. You have two options for assigning IAM permissions to the Datafold Engineers.

1. Assign them as an **owner** of your project.
2. Assign the extended set of [Minimal IAM Permissions](#minimal-iam-permissions).

The owner role is only required temporarily while we configure and test the initial Datafold deployment. We'll inform you when it is ok to revoke this permission and provide us with only the [Minimal IAM Permissions](#minimal-iam-permissions).

### Required APIs

The following GCP APIs need to be additionally enabled to run Datafold:

1. [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)
2. [Secret Manager API](https://console.cloud.google.com/apis/api/secretmanager.googleapis.com)

The following GCP APIs we use are already turned on by default when you created the project:

1. [Cloud Logging API](https://console.cloud.google.com/apis/api/logging.googleapis.com)
2. [Cloud Monitoring API](https://console.cloud.google.com/apis/api/monitoring.googleapis.com)
3. [Cloud Storage](https://console.cloud.google.com/apis/api/storage-component.googleapis.com)
4. [Service Networking API](https://console.cloud.google.com/apis/api/servicenetworking.googleapis.com)

Once the access has been granted, make sure to notify Datafold so we can initiate the deployment.

### Minimal IAM Permissions

Because we work in a Project dedicated to Datafold, there is no direct access to your resources unless explicitly configured (e.g., VPC Peering). The following IAM roles are required to update and maintain the infrastructure.

```Bash  theme={null}
Cloud SQL Admin
Compute Load Balancer Admin
Compute Network Admin
Compute Security Admin
Compute Storage Admin
IAP-secured Tunnel User
Kubernetes Engine Admin
Kubernetes Engine Cluster Admin
Role Viewer
Service Account User
Storage Admin
Viewer
```

Some roles we need from time to time. For example, when we do the first deployment. Since those are IAM-related, we will ask for temporary permissions when required.

```Bash  theme={null}
Role Administrator
Security Admin
Service Account Key Admin
Service Account Admin
Service Usage Admin
```

# Datafold Google Cloud infrastructure details

This document provides detailed information about the Google Cloud infrastructure components deployed
by the Datafold Terraform module, explaining the architectural decisions and operational considerations for each component.

## Persistent disks

The Datafold application requires 3 persistent disks for storage, each deployed as encrypted Google Compute Engine
persistent disks in the primary availability zone. This also means that pods cannot be deployed outside the availability
zone of these disks, because the nodes wouldn't be able to attach them.

**ClickHouse data disk** serves as the analytical database storage for Datafold. ClickHouse is a columnar database
that excels at analytical queries. The default 40GB allocation usually provides sufficient space for typical deployments,
but it can be scaled up based on data volume requirements. The pd-balanced disk type provides consistent
performance for analytical workloads with automatically managed IOPS and throughput.

**ClickHouse logs disk** stores ClickHouse's internal logs and temporary data. The separate logs disk prevents
log data from consuming IOPS and I/O performance from actual data storage.

**Redis data disk** provides persistent storage for Redis, which handles task distribution and distributed locks in
the Datafold application. Redis is memory-first but benefits from persistence for data durability across restarts.
The 50GB default size accommodates typical caching needs while remaining cost-effective.

All persistent disks are encrypted by default using Google-managed encryption keys, ensuring data security at rest.
The disks are deployed in the first availability zone to minimize latency and simplify backup strategies.

## Load balancer

The load balancer serves as the primary entry point for all external traffic to the Datafold application.
The module offers 2 deployment strategies, each with different operational characteristics and trade-offs.

**External Load Balancer Deployment** (the default approach) creates a Google Cloud Load Balancer through Terraform.
This approach provides centralized control over load balancer configuration and integrates well with existing Google Cloud infrastructure.
The load balancer automatically handles SSL termination, health checks, and traffic distribution across Kubernetes pods.
This method is ideal for organizations that prefer infrastructure-as-code management and want consistent load balancer configurations across environments.

**Kubernetes-Managed Load Balancer** deployment sets `deploy_lb = false` and relies on the Google Cloud Load Balancer Controller
running within the GKE cluster. This approach leverages Kubernetes-native load balancer management, allowing for
dynamic scaling and easier integration with Kubernetes ingress resources. The controller automatically provisions and manages load balancers based on Kubernetes service definitions, which can be more flexible for applications that need to scale load balancer resources dynamically.

For external load balancers deployed through Kubernetes, the infrastructure developer needs to create SSL policies and
Cloud Armor policies separately and attach them to the load balancer through annotations. Internal load balancers cannot
have SSL policies or Cloud Armor applied. Our Helm charts support various deployment types including internal/external
load balancers with uploaded certificates or certificates stored in Kubernetes secrets.

The choice between these approaches often depends on operational preferences and existing infrastructure patterns.
External deployment provides more predictable resource management, while Kubernetes-managed deployment offers greater flexibility for dynamic workloads.

**Security** A firewall rule shared between the load balancer and the GKE nodes allows traffic to reach only the GKE nodes and nothing else.
The load balancer allows traffic to land directly into the GKE private subnet.

**Certificate** The certificate can be pre-created by the customer and then attached, or a Google-managed SSL certificate can be created on the fly.
The application will not function without HTTPS, so a certificate is mandatory. After the certificate is created either
manually or through this repository, it must be validated by the DNS administrator by adding an A record. This puts the
certificate in "ACTIVE" state. The certificate cannot be found when it's still provisioning.

## GKE cluster

The Google Kubernetes Engine (GKE) cluster forms the compute foundation for the Datafold application,
providing a managed Kubernetes environment optimized for Google Cloud infrastructure.

**Network Architecture** The entire cluster is deployed into private subnets. This means the data plane
is not reachable from the Internet except through the load balancer. A Cloud NAT allows the cluster to reach the
internet (egress traffic) for downloading pod images, optionally sending Datadog logs and metrics,
and retrieving the version to apply to the cluster from our portal. The control plane is accessible via a private endpoint
using a Private Service Connect setup from, for example, a VPN VPC elsewhere. This is a private+public endpoint,
so the control plane can also be made accessible through the Internet, but then the appropriate CIDR restrictions should be put in place.

For a typical dedicated cloud deployment of Datafold, only around 100 IPs are needed.
This assumes 3 e2-standard-8 instances where one node runs ClickHouse+Redis, another node runs the application,
and a third node may be put in place when version rollovers occur. This means a subnet of size /24 (253 IPs)
should be sufficient to run this application, but you can always apply a different CIDR per subnet if needed.

By default, the repository creates a VPC and subnets, but by specifying the VPC ID of an already existing VPC,
the cluster and load balancer get deployed into existing network infrastructure.
This is important for some customers where they deploy a different architecture without Cloud NAT, firewall options that check egress, and other DLP controls.

**Add-ons**

The cluster includes essential add-ons like CoreDNS for service discovery, the VPC-native networking for networking,
and the GCE persistent disk CSI driver for persistent volume management. These components are automatically updated
and maintained by Google, reducing operational overhead.

**Node Management** supports up to three managed node pools, allowing for workload-specific resource allocation.
Each node pool can be configured with different machine types, enabling cost optimization and performance tuning
for different application components. The cluster autoscaler automatically adjusts node count based on resource demands,
ensuring efficient resource utilization while maintaining application availability. One typical way to deploy
is to let the application pods go on a wider range of nodes, and set up tolerations and labels on the second node pool,
which are then selected by both Redis and ClickHouse. This is because Redis and ClickHouse have restrictions
on the zone they must be present in because of their disks, and ClickHouse is a bit more CPU intensive.
This method optimizes CPU performance for the Datafold application.

**Security Features** include several critical security configurations:

* **Workload Identity** is enabled and configured with the project's workload pool, providing fine-grained IAM permissions to Kubernetes pods without requiring Google Cloud credentials in container images
* **Shielded nodes** are enabled with secure boot and integrity monitoring for enhanced node security
* **Binary authorization** is configured with project singleton policy enforcement to ensure only authorized container images can be deployed
* **Network policy** is enabled using Calico for pod-to-pod communication control
* **Private nodes** are enabled, ensuring all node traffic goes through the VPC network

These security features follow the principle of least privilege and integrate seamlessly with Google Cloud security services.

## IAM roles and permissions

The IAM architecture follows the principle of least privilege, providing specific permissions only where needed.
Service accounts in Kubernetes are mapped to IAM roles using Workload Identity, enabling secure access to Google
Cloud services without embedding credentials in application code.

**GKE service account** is created with basic permissions for logging, monitoring, and storage access.
This service account is used by the GKE nodes and provides the foundation for cluster operations.

**ClickHouse backup service account** is created with a custom role that allows ClickHouse to make backups and store them on Cloud Storage.
This service account uses Workload Identity to securely access Cloud Storage without embedding credentials.

**Datafold roles** Datafold has roles per pod pre-defined which can have their permissions assigned when they need them.
At the moment, we have two specific roles in use. One is for the ClickHouse pod to be able to make backups and store them on Cloud Storage.
The other is for the use of the Vertex AI service for our AI offering.

These roles are automatically created and configured when the cluster is deployed, ensuring that the
necessary permissions are in place for the cluster to function properly. The Datafold and ClickHouse service accounts
authenticate using Workload Identity, which means these permissions are automatically rotated and managed by Google, reducing security risks associated with long-lived credentials.

## Cloud SQL database

The PostgreSQL Cloud SQL instance serves as the primary relational database for the Datafold application,
storing user data, configuration, and application state.

**Storage configuration** starts with a 20GB initial allocation that can automatically scale up to 100GB based on usage patterns.
This auto-scaling feature prevents storage-related outages while avoiding over-provisioning.
For typical deployments, storage usage remains under 200GB, though some high-volume deployments may approach 400GB.
The pd-balanced storage type provides consistent performance with configurable IOPS and throughput.

**High availability** is intentionally disabled by default, meaning the database runs in a single availability zone.
This configuration reduces costs and complexity while still providing excellent reliability. The database includes
automated backups with 7-day retention, ensuring data can be recovered in case of failures. For organizations requiring higher availability,
multi-zone deployment can be enabled, though this significantly increases costs.

**Security and encryption** always encrypts data at rest using Google-managed encryption keys by default.
The database is deployed in private subnets with firewall rules that restrict access to only the GKE cluster,
ensuring network-level security.

The database configuration prioritizes operational simplicity and cost-effectiveness while maintaining the security
and reliability required for production workloads. The combination of automated backups, encryption,
and network isolation provides a robust foundation for the application's data storage needs.
