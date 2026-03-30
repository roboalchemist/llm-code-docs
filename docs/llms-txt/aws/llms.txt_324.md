# Source: https://docs.aws.amazon.com/eks/latest/best-practices/llms.txt

# Amazon EKS Best Practices Guide

> Learn best practices for operating EKS clusters.

- [Introduction](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html)
- [Cluster Upgrades](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html)
- [Contribute](https://docs.aws.amazon.com/eks/latest/best-practices/contribute.html)

## [Security](https://docs.aws.amazon.com/eks/latest/best-practices/security.html)

- [EKS Auto Mode - Security](https://docs.aws.amazon.com/eks/latest/best-practices/autosecure.html)
- [Identity and Access Management](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)
- [Pod Security](https://docs.aws.amazon.com/eks/latest/best-practices/pod-security.html)
- [Multi-tenancy](https://docs.aws.amazon.com/eks/latest/best-practices/tenant-isolation.html): When we think of multi-tenancy, we often want to isolate a user or application from other users or applications running on a shared infrastructure.
- [Detective Controls](https://docs.aws.amazon.com/eks/latest/best-practices/auditing-and-logging.html)
- [Network security](https://docs.aws.amazon.com/eks/latest/best-practices/network-security.html)
- [Data encryption and secrets management](https://docs.aws.amazon.com/eks/latest/best-practices/data-encryption-and-secrets-management.html)
- [Runtime security](https://docs.aws.amazon.com/eks/latest/best-practices/runtime-security.html): Runtime security provides active protection for your containers while theyâre running.
- [Infrastructure Security](https://docs.aws.amazon.com/eks/latest/best-practices/protecting-the-infrastructure.html): Inasmuch as itâs important to secure your container images, itâs equally important to safeguard the infrastructure that runs them.
- [Regulatory Compliance](https://docs.aws.amazon.com/eks/latest/best-practices/compliance.html): Compliance is a shared responsibility between AWS and the consumers of its services.
- [Incident response and forensics](https://docs.aws.amazon.com/eks/latest/best-practices/incident-response-and-forensics.html): Your ability to react quickly to an incident can help minimize damage caused from a breach.
- [Image security](https://docs.aws.amazon.com/eks/latest/best-practices/image-security.html): You should consider the container image as your first line of defense against an attack.
- [Multi Account Strategy](https://docs.aws.amazon.com/eks/latest/best-practices/multi-account-strategy.html): AWS recommends using a multi account strategy and AWS organizations to help isolate and manage your business applications and data.
- [Cluster access management](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-access-management.html): Effective access management is crucial for maintaining the security and integrity of your Amazon EKS clusters.


## [Cluster Autoscaling](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-autoscaling.html)

- [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/best-practices/automode.html)
- [Karpenter](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html)
- [Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html)


## [Reliability](https://docs.aws.amazon.com/eks/latest/best-practices/reliability.html)

- [Applications](https://docs.aws.amazon.com/eks/latest/best-practices/application.html): Your customers expect your application to be always available, including when youâre making changes and especially during spikes in traffic.
- [Control Plane](https://docs.aws.amazon.com/eks/latest/best-practices/control-plane.html)
- [Data Plane](https://docs.aws.amazon.com/eks/latest/best-practices/data-plane.html): To operate high-available and resilient applications, you need a highly-available and resilient data plane.


## [Networking](https://docs.aws.amazon.com/eks/latest/best-practices/networking.html)

- [VPC and Subnets Considerations](https://docs.aws.amazon.com/eks/latest/best-practices/subnets.html): VPC and Subnet Considerations
- [Amazon VPC CNI](https://docs.aws.amazon.com/eks/latest/best-practices/vpc-cni.html): Amazon VPC CNI
- [Optimizing IP Address Utilization](https://docs.aws.amazon.com/eks/latest/best-practices/ip-opt.html)
- [Running IPv6 Clusters](https://docs.aws.amazon.com/eks/latest/best-practices/ipv6.html): Running IPv6 EKS Clusters
- [Custom Networking](https://docs.aws.amazon.com/eks/latest/best-practices/custom-networking.html): Custom Networking
- [Prefix Mode for Linux](https://docs.aws.amazon.com/eks/latest/best-practices/prefix-mode-linux.html): Prefix Mode for Linux
- [Prefix Mode for Windows](https://docs.aws.amazon.com/eks/latest/best-practices/prefix-mode-win.html): In Amazon EKS, each Pod that runs on a Windows host is assigned a secondary IP address by the VPC resource controller by default.
- [Security Groups Per Pod](https://docs.aws.amazon.com/eks/latest/best-practices/sgpp.html): Security Groups Per Pod
- [Load Balancing](https://docs.aws.amazon.com/eks/latest/best-practices/load-balancing.html)
- [Monitoring for Network performance issues](https://docs.aws.amazon.com/eks/latest/best-practices/monitoring_eks_workloads_for_network_performance_issues.html)
- [Running kube-proxy in IPVS Mode](https://docs.aws.amazon.com/eks/latest/best-practices/ipvs.html): EKS in IP Virtual Server (IPVS) mode solves the network latency issue often seen when running large clusters with over 1,000 services with kube-proxy running in legacy iptables mode.


## [Scalability](https://docs.aws.amazon.com/eks/latest/best-practices/scalability.html)

- [Control Plane](https://docs.aws.amazon.com/eks/latest/best-practices/scale-control-plane.html)
- [Data Plane](https://docs.aws.amazon.com/eks/latest/best-practices/scale-data-plane.html): Selecting EC2 instance types is possibly one of the hardest decisions customers face because in clusters with multiple workloads.
- [Cluster Services](https://docs.aws.amazon.com/eks/latest/best-practices/scale-cluster-services.html): Cluster services run inside an EKS cluster, but they are not user workloads.
- [Workloads](https://docs.aws.amazon.com/eks/latest/best-practices/scale-workloads.html): Workloads have an impact on how large your cluster can scale.
- [The theory behind scaling](https://docs.aws.amazon.com/eks/latest/best-practices/kubernetes_scaling_theory.html)
- [Control Plane Monitoring](https://docs.aws.amazon.com/eks/latest/best-practices/control_plane_monitoring.html)
- [Node efficiency and scaling](https://docs.aws.amazon.com/eks/latest/best-practices/node_and_workload_efficiency.html): Being efficient with our workloads and nodes reduces complexity/cost while increasing performance and scale.
- [Kubernetes SLOs](https://docs.aws.amazon.com/eks/latest/best-practices/kubernetes_upstream_slos.html): Amazon EKS runs the same code as the upstream Kubernetes releases and ensures that EKS clusters operate within the SLOs defined by the Kubernetes community.
- [Known Limits and Service Quotas](https://docs.aws.amazon.com/eks/latest/best-practices/known_limits_and_service_quotas.html)


## [Cost Optimization](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt.html)

- [Framework](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-framework.html): AWS Cloud Economics is a discipline that helps customers increase efficiency and reduce their costs through the adoption of modern compute technologies like Amazon EKS.
- [Awareness](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-awareness.html): Expenditure awareness is understanding who, where and what is causing expenditures in your EKS cluster.
- [Compute](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-compute.html): As a developer, youâll make estimates about your applicationâs resource requirements, e.g.
- [Network](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-networking.html): Architecting systems for high availability (HA) is a best practice in order to accomplish resilience and fault-tolerance.
- [Storage](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-storage.html)
- [Observability](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-observability.html)


## [Windows](https://docs.aws.amazon.com/eks/latest/best-practices/windows.html)

- [AMI Management](https://docs.aws.amazon.com/eks/latest/best-practices/windows-ami.html): Windows Amazon EKS optimized AMIs are built on top of Windows Server 2019 and Windows Server 2022.
- [gMSA for Windows Containers](https://docs.aws.amazon.com/eks/latest/best-practices/windows-gmsa.html)
- [Windows Server Hardening](https://docs.aws.amazon.com/eks/latest/best-practices/windows-hardening.html): OS Hardening is a combination of OS configuration, patching, and removing unnecessary software packages, which aim to lock down a system and reduce the attack surface.
- [Scanning Windows Images](https://docs.aws.amazon.com/eks/latest/best-practices/windows-images.html): Image Scanning is an automated vulnerability assessment feature that helps improve the security of your applicationâs container images by scanning them for a broad range of operating system vulnerabilities.
- [Windows Versions and Licensing](https://docs.aws.amazon.com/eks/latest/best-practices/windows-licensing.html)
- [Logging](https://docs.aws.amazon.com/eks/latest/best-practices/windows-logging.html): Containerized applications typically direct application logs to STDOUT.
- [Monitoring Windows Containers](https://docs.aws.amazon.com/eks/latest/best-practices/windows-monitoring.html): Prometheus, a graduated CNCF project is by far the most popular monitoring system with native integration into Kubernetes.
- [Windows Networking](https://docs.aws.amazon.com/eks/latest/best-practices/windows-networking.html)
- [Memory and Systems Management](https://docs.aws.amazon.com/eks/latest/best-practices/windows-oom.html): Windows does not have an out-of-memory process killer as Linux does.
- [Infrastructure Management](https://docs.aws.amazon.com/eks/latest/best-practices/windows-patching.html): Patching Windows Server is a standard management task for Windows Administrators.
- [Scheduling](https://docs.aws.amazon.com/eks/latest/best-practices/windows-scheduling.html): Kubernetes has support for heterogeneous clusters where you can have a mixture of Linux and Windows nodes in the same cluster.
- [Pod Security for Windows Containers](https://docs.aws.amazon.com/eks/latest/best-practices/windows-security.html): Pod Security Policies (PSP) and Pod Security Standards (PSS) are two main ways of enforcing security in Kubernetes.
- [Storage Options](https://docs.aws.amazon.com/eks/latest/best-practices/windows-storage.html)
- [Hardening Windows containers images](https://docs.aws.amazon.com/eks/latest/best-practices/windows-hardening-containers-images.html): Are you hardening your Windows container images? Over the years, Iâve worked with customers globally to help them migrate legacy workloads to containers, particularly Windows workloads.


## [Hybrid](https://docs.aws.amazon.com/eks/latest/best-practices/hybrid.html)

### [Network Disconnection](https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-network-disconnections.html)

The EKS Hybrid Nodes architecture can be new to customers who are accustomed to running local Kubernetes clusters entirely in their own data centers or edge locations.

- [Best practices](https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-network-disconnection-best-practices.html)
- [Kubernetes pod failover](https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-kubernetes-pod-failover.html): We begin with a review of the key concepts, components, and settings that influence how Kubernetes behaves during network disconnections between nodes and the Kubernetes control plane.
- [Application network traffic](https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-app-network-traffic.html): The topics on this page are related to Kubernetes cluster networking and the application traffic during network disconnections between nodes and the Kubernetes control plane.
- [Host credentials](https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-host-creds.html): EKS Hybrid Nodes is integrated with AWS Systems Manager (SSM) hybrid activations and AWS IAM Roles Anywhere for temporary IAM credentials that are used to authenticate the node with the EKS control plane.


## [AI/ML](https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html)

- [Compute](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html)
- [Networking](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-networking.html)
- [Security](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-security.html)
- [Storage](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-storage.html)
- [Observability](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-observability.html)
- [Performance](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-performance.html)
