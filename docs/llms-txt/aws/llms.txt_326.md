# Source: https://docs.aws.amazon.com/eks/latest/userguide/llms.txt

# Amazon EKS User Guide

> This is official Amazon Web Services (AWS) documentation for Amazon Elastic Kubernetes Service (Amazon EKS). Amazon EKS is a managed service that makes it easy for you to run Kubernetes on AWS without needing to install and operate your own Kubernetes clusters. Kubernetes is an open source system for automating the deployment, scaling, and management of containerized applications.

- [Quickstart](https://docs.aws.amazon.com/eks/latest/userguide/quickstart.html)
- [Learn Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/learn-eks.html)
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting.html)
- [Projects related to Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/related-projects.html)
- [New features and roadmap](https://docs.aws.amazon.com/eks/latest/userguide/roadmap.html)
- [Document history](https://docs.aws.amazon.com/eks/latest/userguide/doc-history.html)

## [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

- [Common use cases](https://docs.aws.amazon.com/eks/latest/userguide/common-use-cases.html): Discover how Amazon EKS helps deploy highly available containerized applications, build microservices architectures, automate software release processes, run serverless applications, execute machine learning workloads, deploy consistently on-premises and in the cloud, process big data cost-effectively, and ensure security and compliance.
- [Architecture](https://docs.aws.amazon.com/eks/latest/userguide/eks-architecture.html): Learn how Amazon EKS aligns with Kubernetes cluster architecture, offering a highly available and resilient control plane, and flexible compute options like AWS Fargate, Karpenter, managed node groups, and self-managed nodes to meet diverse workload requirements.
- [Kubernetes concepts](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-concepts.html): Learn core Kubernetes concepts and how they relate to deploying workloads, managing clusters, and working with control planes, nodes, Pods, containers, and networking on Amazon EKS.
- [Deployment options](https://docs.aws.amazon.com/eks/latest/userguide/eks-deployment-options.html): Learn to deploy Kubernetes clusters with Amazon EKS across cloud and on-premises environments to meet your operational needs, while leveraging AWS services and support.


## [Set up](https://docs.aws.amazon.com/eks/latest/userguide/setting-up.html)

- [Set up AWS CLI](https://docs.aws.amazon.com/eks/latest/userguide/install-awscli.html): Set up the AWS CLI for managing AWS resources needed to use Amazon EKS.
- [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html): Learn how to install or update the kubectl and eksctl command line tools to work with Kubernetes and Amazon EKS features.


## [Get started](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

- [Create cluster (EKS Auto Mode)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-automode.html): Like other EKS getting started experiences, creating your first cluster with EKS Auto Mode delegates the management of the cluster itself to AWS.
- [Create cluster (eksctl)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html): Learn how to create your first Amazon EKS cluster with nodes using the eksctl command line tool.
- [Create cluster (Console and CLI)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html): Learn how to create your first Amazon EKS cluster with nodes using the AWS Management Console and AWS CLI.


## [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html)

### [Create cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-auto.html)

Learn about the tools needed for creating and working with an Amazon EKS cluster in EKS Auto Mode.

- [eksctl CLI](https://docs.aws.amazon.com/eks/latest/userguide/automode-get-started-eksctl.html): This topic shows you how to create an Amazon EKS Auto Mode cluster using the eksctl command line interface (CLI).
- [AWS CLI](https://docs.aws.amazon.com/eks/latest/userguide/automode-get-started-cli.html): EKS Auto Mode Clusters automate routine cluster management tasks for compute, storage, and networking.
- [Management console](https://docs.aws.amazon.com/eks/latest/userguide/automode-get-started-console.html): Creating an EKS Auto Mode cluster in the AWS Management Console requires less configuration than other options.

### [Enable existing clusters](https://docs.aws.amazon.com/eks/latest/userguide/migrate-auto.html)

Learn about the tools needed for creating and working with an Amazon EKS cluster in EKS Auto Mode.

- [Enable on cluster](https://docs.aws.amazon.com/eks/latest/userguide/auto-enable-existing.html): This topic describes how to enable Amazon EKS Auto Mode on your existing Amazon EKS clusters.
- [Migrate from Karpenter](https://docs.aws.amazon.com/eks/latest/userguide/auto-migrate-karpenter.html): This topic walks you through the process of migrating workloads from Karpenter to Amazon EKS Auto Mode using kubectl.
- [Migrate from MNGs](https://docs.aws.amazon.com/eks/latest/userguide/auto-migrate-mng.html): When transitioning your Amazon EKS cluster to use EKS auto mode, you can smoothly migrate your existing workloads from managed node groups (MNGs) using the eksctl CLI tool.
- [Migrate from Fargate](https://docs.aws.amazon.com/eks/latest/userguide/auto-migrate-fargate.html): This topic walks you through the process of migrating workloads from EKS Fargate to Amazon EKS Auto Mode using kubectl.

### [Run workloads](https://docs.aws.amazon.com/eks/latest/userguide/auto-workloads.html)

Run workloads in EKS Auto Mode clusters

- [Deploy inflate workload](https://docs.aws.amazon.com/eks/latest/userguide/automode-workload.html): In this tutorial, youâll learn how to deploy a sample workload to an EKS Auto Mode cluster and observe how it automatically provisions the required compute resources.
- [Deploy load balancer](https://docs.aws.amazon.com/eks/latest/userguide/auto-elb-example.html): This guide walks you through deploying a containerized version of the 2048 game on Amazon EKS, complete with load balancing and internet accessibility.
- [Deploy stateful workload](https://docs.aws.amazon.com/eks/latest/userguide/sample-storage-workload.html): This tutorial will guide you through deploying a sample stateful application to your EKS Auto Mode cluster.
- [Deploy accelerated workload](https://docs.aws.amazon.com/eks/latest/userguide/auto-accelerated.html): This tutorial demonstrates how Amazon EKS Auto Mode simplifies launching hardware-accelerated workloads.

### [Configure](https://docs.aws.amazon.com/eks/latest/userguide/settings-auto.html)

Change EKS Auto cluster settings

- [Create node class](https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html): Amazon EKS Node Classes are templates that offer granular control over the configuration of your EKS Auto Mode managed nodes.
- [Create node pool](https://docs.aws.amazon.com/eks/latest/userguide/create-node-pool.html): Amazon EKS node pools offer a flexible way to manage compute resources in your Kubernetes cluster.
- [Create static node pool](https://docs.aws.amazon.com/eks/latest/userguide/auto-static-capacity.html): Amazon EKS Auto Mode supports static capacity node pools that maintain a fixed number of nodes regardless of pod demand.
- [Create ingress class](https://docs.aws.amazon.com/eks/latest/userguide/auto-configure-alb.html): EKS Auto Mode automates routine tasks for load balancing, including exposing cluster apps to the internet.
- [Create service](https://docs.aws.amazon.com/eks/latest/userguide/auto-configure-nlb.html): Learn how to configure Network Load Balancers (NLB) in Amazon EKS using Kubernetes service annotations.
- [Create StorageClass](https://docs.aws.amazon.com/eks/latest/userguide/create-storage-class.html): A StorageClass in Amazon EKS Auto Mode defines how Amazon EBS volumes are automatically provisioned when applications request persistent storage.
- [Disable EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/auto-disable.html): You can disable EKS Auto Mode on an existing EKS Cluster.
- [Update Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/auto-upgrade.html): This topic explains how to update the Kubernetes version of your Auto Mode cluster.
- [Review built-in node pools](https://docs.aws.amazon.com/eks/latest/userguide/set-builtin-node-pools.html): EKS Auto Mode has two built-in NodePools.
- [Control deployment](https://docs.aws.amazon.com/eks/latest/userguide/associate-workload.html): When running workloads in an EKS cluster with EKS Auto Mode, you might need to control whether specific workloads run on EKS Auto Mode nodes or other compute types.
- [Run critical add-ons](https://docs.aws.amazon.com/eks/latest/userguide/critical-workload.html): In this topic, you will learn how to deploy a workload with a CriticalAddonsOnly toleration so EKS Auto Mode will schedule it onto the system node pool.
- [Use network policies](https://docs.aws.amazon.com/eks/latest/userguide/auto-net-pol.html)
- [Tag subnets](https://docs.aws.amazon.com/eks/latest/userguide/tag-subnets-auto.html): If you use the load balancing capability of EKS Auto Mode, you need to add AWS tags to your VPC subnets.
- [Generate CIS report](https://docs.aws.amazon.com/eks/latest/userguide/auto-cis.html): This topic describes how to generate CIS (Center for Internet Security) compliance reports for Amazon EKS nodes using the kubectl debug command.
- [Encrypt root volumes](https://docs.aws.amazon.com/eks/latest/userguide/auto-kms.html): You can encrypt the ephemeral root volume for EKS Auto Mode instances with a customer managed KMS key.
- [Update AMI controls](https://docs.aws.amazon.com/eks/latest/userguide/auto-controls.html): Some organization controls can prevent EKS Auto Mode from functioning correctly.
- [Control Capacity Reservations](https://docs.aws.amazon.com/eks/latest/userguide/auto-odcr.html): You can control the deployment of workloads onto Capacity Reservations.
- [Use Local Zones](https://docs.aws.amazon.com/eks/latest/userguide/auto-local-zone.html): EKS Auto Mode provides simplified cluster management with automatic node provisioning.
- [Advanced security](https://docs.aws.amazon.com/eks/latest/userguide/auto-advanced-security.html): This topic describes how to configure advanced security settings for Amazon EKS Auto Mode nodes using the advancedSecurity specification in your Node Class.

### [How it works](https://docs.aws.amazon.com/eks/latest/userguide/auto-reference.html)

Reference information for EKS Auto Mode

- [Managed instances](https://docs.aws.amazon.com/eks/latest/userguide/automode-learn-instances.html): This topic explains how Amazon EKS Auto Mode manages Amazon EC2 instances in your EKS cluster.
- [Identity and access](https://docs.aws.amazon.com/eks/latest/userguide/auto-learn-iam.html): This topic describes the Identity and Access Management (IAM) roles and permissions required to use EKS Auto Mode.
- [Networking](https://docs.aws.amazon.com/eks/latest/userguide/auto-networking.html): This topic explains how to configure Virtual Private Cloud (VPC) networking and load balancing features in EKS Auto Mode.

### [Observability](https://docs.aws.amazon.com/eks/latest/userguide/auto-observability.html)

Monitor and observe your EKS Auto Mode clusters

- [EKS Auto Managed Component Logs](https://docs.aws.amazon.com/eks/latest/userguide/auto-managed-component-logs.html): You can access AWS-managed component logs from EKS Auto Mode to gain deeper observability into your cluster operations.
- [Troubleshoot](https://docs.aws.amazon.com/eks/latest/userguide/auto-troubleshoot.html): With EKS Auto Mode, AWS assumes more responsibility for EC2 Instances in your AWS account.
- [Release notes](https://docs.aws.amazon.com/eks/latest/userguide/auto-change.html): This page documents updates to Amazon EKS Auto Mode.


## [Configure clusters](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html)

- [Create auto cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster-auto.html): Learn how to create an Amazon EKS Auto Mode cluster to run Kubernetes applications, including prerequisites, networking options, and add-on configurations.
- [Create a cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html): Learn how to create an Amazon EKS cluster to run Kubernetes applications, including prerequisites, networking options, and add-on configurations.

### [Create Provisioned Control Plane](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html)

Learn how to use Amazon EKS Provisioned Control Plane for predictable and high performance from the clusterâs control plane.

- [Getting started with Provisioned Control Plane](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane-getting-started.html): Learn how to create and manage Amazon EKS clusters with Provisioned Control Plane using the AWS CLI and AWS Management Console.

### [Cluster insights](https://docs.aws.amazon.com/eks/latest/userguide/cluster-insights.html)

Discover how Amazon EKS cluster insights help monitor and resolve potential issues for enhanced reliability.

- [View cluster insights](https://docs.aws.amazon.com/eks/latest/userguide/view-cluster-insights.html): Amazon EKS provides two types of insights: Configuration insights and Upgrade insights.
- [Update Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html): Learn how to update your Amazon EKS cluster to the latest Kubernetes version, ensuring compatibility with nodes and add-ons, and maintaining high availability during the process.

### [Delete a cluster](https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html)

Learn how to delete Amazon EKS clusters, including managed and self-managed node groups, Fargate profiles, related services, and AWS CloudFormation stacks using eksctl, AWS Management Console, or AWS CLI for cost optimization and resource cleanup.

- [Protect EKS clusters from accidental deletion](https://docs.aws.amazon.com/eks/latest/userguide/deletion-protection.html): Accidentally deleting an EKS cluster may impair Kubernetes cluster operations.

### [Cluster endpoint access](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html)

Learn how to enable private access and limit public access to the Amazon EKS cluster Kubernetes API server endpoint for enhanced security with your Amazon EKS cluster.

- [Configure endpoint access](https://docs.aws.amazon.com/eks/latest/userguide/config-cluster-endpoint.html): Learn how to enable private access and limit public access to the Amazon EKS cluster Kubernetes API server endpoint for enhanced security with your Amazon EKS cluster.
- [Enable Windows support](https://docs.aws.amazon.com/eks/latest/userguide/windows-support.html): Learn how to enable and manage Windows support for your Amazon EKS cluster to run Windows containers alongside Linux containers.
- [Disable Windows support](https://docs.aws.amazon.com/eks/latest/userguide/disable-windows-support.html)
- [Private clusters](https://docs.aws.amazon.com/eks/latest/userguide/private-clusters.html): Learn how to deploy and operate an Amazon EKS cluster without outbound internet access, including requirements for private container registries, endpoint access control, and VPC interface endpoints for AWS services.
- [Autoscaling](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html): Discover how Amazon EKS integrates Kubernetes autoscaling with AWS, empowering rapid and efficient scaling of compute resources to meet application demands using Karpenter and Cluster Autoscaler.
- [Learn about zonal shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html): Kubernetes has native features that enable you to make your applications more resilient to events such as the degraded health or impairment of an Availability Zone (AZ).
- [Enable zonal shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift-enable.html): Amazon Application Recovery Controller (ARC) helps you manage and coordinate recovery for your applications across Availability Zones (AZs) and works with many services, including Amazon EKS.


## [Manage access](https://docs.aws.amazon.com/eks/latest/userguide/cluster-auth.html)

### [Kubernetes API access](https://docs.aws.amazon.com/eks/latest/userguide/grant-k8s-access.html)

Learn how to grant access to Kubernetes APIs on Amazon EKS clusters using IAM roles, users, or OpenID Connect providers, and manage permissions with access entries or the aws-auth ConfigMap.

### [Access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html)

Learn how to manage access entries for IAM principals to your Amazon EKS cluster, including creating, updating, and deleting access entries for fine-grained authentication and authorization.

- [Associate access policies](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html): Learn how to associate and disassociate Amazon EKS access policies to and from access entries to grant Kubernetes permissions to IAM principals.
- [Migrate to access entries](https://docs.aws.amazon.com/eks/latest/userguide/migrating-access-entries.html): If youâve added entries to the aws-auth ConfigMap on your cluster, we recommend that you create access entries for the existing entries in your aws-auth ConfigMap.
- [Review access policies](https://docs.aws.amazon.com/eks/latest/userguide/access-policy-permissions.html): Access policies include rules that contain Kubernetes verbs (permissions) and resources.
- [Authentication mode](https://docs.aws.amazon.com/eks/latest/userguide/setting-up-access-entries.html): To begin using access entries, you must change the authentication mode of the cluster to either the API_AND_CONFIG_MAP or API modes.
- [Create access entries](https://docs.aws.amazon.com/eks/latest/userguide/creating-access-entries.html): Before creating access entries, consider the following:
- [Update access entries](https://docs.aws.amazon.com/eks/latest/userguide/updating-access-entries.html): You can update an access entry using the AWS Management Console or the AWS CLI.
- [Delete access entries](https://docs.aws.amazon.com/eks/latest/userguide/deleting-access-entries.html): If you discover that you deleted an access entry in error, you can always recreate it.
- [Set custom username](https://docs.aws.amazon.com/eks/latest/userguide/set-custom-username.html): When creating access entries for Amazon EKS, you can either use the automatically generated username or specify a custom username.
- [Tutorial: Create with access policy](https://docs.aws.amazon.com/eks/latest/userguide/create-standard-access-entry-policy.html): Create Amazon EKS access entries that use AWS-managed EKS access policies to grant IAM identities standardized permissions for accessing and managing Kubernetes clusters.
- [Tutorial: Create with Kubernetes groups](https://docs.aws.amazon.com/eks/latest/userguide/create-k8s-group-access-entry.html): Create Amazon EKS access entries that use Kubernetes groups for authorization and require manual RBAC configuration.
- [aws-auth ConfigMap](https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html): Learn how to manage IAM principal access to your Amazon EKS cluster using the aws-auth ConfigMap and Kubernetes RBAC, allowing authorized users and roles to interact with the cluster securely.
- [Link OIDC provider](https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html): Learn how to authenticate users for your Amazon EKS cluster using OpenID Connect (OIDC) identity providers to manage access and permissions with roles, bindings, and RBAC authorization.
- [Unlink OIDC provider](https://docs.aws.amazon.com/eks/latest/userguide/disassociate-oidc-identity-provider.html): If you disassociate an OIDC identity provider from your cluster, users included in the provider can no longer access the cluster.
- [Access cluster resources](https://docs.aws.amazon.com/eks/latest/userguide/view-kubernetes-resources.html): Learn how to view Kubernetes resources in the AWS Management Console.
- [Modify cluster resources](https://docs.aws.amazon.com/eks/latest/userguide/mutate-kubernetes-resources.html): Learn about the permissions required to modify Kubernetes resources.
- [Access cluster with kubectl](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html): Learn how to create or update a kubeconfig file for authenticating with your Amazon EKS cluster using kubectl.

### [Workload access to AWS](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html)

### [Credentials with IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)

Learn how applications in your Pods can access AWS services.

- [IAM OIDC provider](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html): Learn how to create an AWS Identity and Access Management OpenID Connect provider for your cluster.
- [Assign IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html): Discover how to configure a Kubernetes service account to assume an IAM role, enabling Pods to securely access AWS services with granular permissions.
- [Assign to Pod](https://docs.aws.amazon.com/eks/latest/userguide/pod-configuration.html): Learn how to configure your Pods to use a Kubernetes service account that you allowed to assume an AWS Identity and Access Management role.
- [STS endpoints](https://docs.aws.amazon.com/eks/latest/userguide/configure-sts-endpoint.html): If youâre using a Kubernetes service account with IAM roles for service accounts, then you can configure the type of AWS Security Token Service endpoint thatâs used by the service account.
- [Cross-account IAM](https://docs.aws.amazon.com/eks/latest/userguide/cross-account-access.html): Learn how to configure cross-account IAM permissions for Amazon EKS clusters by creating an identity provider from another accountâs cluster or using chained AssumeRole operations, enabling secure access to AWS resources across multiple accounts.
- [Supported SDKs](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts-minimum-sdk.html)
- [Fetch signing keys](https://docs.aws.amazon.com/eks/latest/userguide/irsa-fetch-keys.html): Discover how to fetch the OIDC public signing keys (JSON Web Key Set) required to validate the ProjectedServiceAccountToken for Amazon EKS clusters, enabling external systems to authenticate with IAM roles for Kubernetes service accounts.

### [Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)

Learn how to provide AWS service access to your Kubernetes workloads with Amazon EKS Pod Identities, offering least privilege access, credential isolation, and auditability for enhanced security.

- [How it works](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-how-it-works.html): Learn how Amazon EKS Pod Identity works to provide temporary credentials to your Kubernetes workloads, using an agent running on each node and the AWS SDKs.
- [Set up the Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html): Learn how to set up the EKS Pod Identity Agent for your cluster.
- [Assign IAM role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-association.html): Learn how to configure a Kubernetes service account to assume an AWS IAM role with Amazon EKS Pod Identity for securely accessing AWS services from your pods.
- [Assign Target IAM role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-assign-target-role.html): Learn how to configure account role access for Amazon EKS workloads using Pod Identity.
- [Pod service account](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-configure-pods.html): Learn how to configure Pods to use a Kubernetes service account with an associated IAM role for accessing AWS services on Amazon EKS.
- [Grant Pods access](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html): Learn how to use Amazon EKS Pod Identity to attach tags for cluster, namespace, and service account to temporary credentials, enabling attribute-based access control (ABAC) for EKS Pods to AWS resources based on matching tags.
- [Supported SDKs](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-minimum-sdk.html)
- [Disable IPv6](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-config-ipv6.html)
- [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html): Learn how to configure the IAM trust policy for Amazon EKS Pod Identity to allow Kubernetes pods to assume IAM roles and access AWS resources securely using Amazon EKS condition keys.


## [Manage compute](https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html)

### [Managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)

Amazon EKS managed node groups automate the provisioning and lifecycle management of nodes (Amazon EC2 instances) for Amazon EKS Kubernetes clusters.

- [Create](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html): This topic describes how you can launch Amazon EKS managed node groups of nodes that register with your Amazon EKS cluster.
- [Update](https://docs.aws.amazon.com/eks/latest/userguide/update-managed-node-group.html): When you initiate a managed node group update, Amazon EKS automatically updates your nodes for you.
- [Update behavior details](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-update-behavior.html): The Amazon EKS managed worker node upgrade strategy has four different phases.
- [Launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html): For the highest level of customization, you can deploy managed nodes using your own launch template and a custom AMI.
- [Delete](https://docs.aws.amazon.com/eks/latest/userguide/delete-managed-node-group.html): This topic describes how you can delete an Amazon EKS managed node group.

### [Self-managed nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)

A cluster contains one or more Amazon EC2 nodes that Pods are scheduled on.

- [Amazon Linux](https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html): This topic describes how you can launch Auto Scaling groups of Linux nodes that register with your Amazon EKS cluster.
- [Bottlerocket](https://docs.aws.amazon.com/eks/latest/userguide/launch-node-bottlerocket.html): This topic describes how to launch Auto Scaling groups of Bottlerocket nodes that register with your Amazon EKS cluster
- [Windows](https://docs.aws.amazon.com/eks/latest/userguide/launch-windows-workers.html): This topic describes how to launch Auto Scaling groups of Windows nodes that register with your Amazon EKS cluster.
- [Ubuntu Linux](https://docs.aws.amazon.com/eks/latest/userguide/launch-node-ubuntu.html): This topic describes how to launch Auto Scaling groups of Ubuntu nodes that register with your Amazon EKS cluster

### [Update methods](https://docs.aws.amazon.com/eks/latest/userguide/update-workers.html)

When a new Amazon EKS optimized AMI is released, consider replacing the nodes in your self-managed node group with the new AMI.

- [Migration](https://docs.aws.amazon.com/eks/latest/userguide/migrate-stack.html): This topic describes how you can create a new node group, gracefully migrate your existing applications to the new group, and remove the old node group from your cluster.
- [CloudFormation stack](https://docs.aws.amazon.com/eks/latest/userguide/update-stack.html): This topic describes how you can update an existing AWS CloudFormation self-managed node stack with a new AMI.

### [AWS Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html)

This topic discusses using Amazon EKS to run Kubernetes Pods on AWS Fargate.

- [Get started](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html): This topic describes how to get started running Pods on AWS Fargate with your Amazon EKS cluster.
- [Define profiles](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html): Before you schedule Pods on Fargate in your cluster, you must define at least one Fargate profile that specifies which Pods use Fargate when launched.
- [Delete profiles](https://docs.aws.amazon.com/eks/latest/userguide/delete-fargate-profile.html): When you delete a Fargate profile, any Pods that were scheduled onto Fargate with the profile are deleted.
- [Pod configuration details](https://docs.aws.amazon.com/eks/latest/userguide/fargate-pod-configuration.html): This section describes some of the unique Pod configuration details for running Kubernetes Pods on AWS Fargate.
- [OS patching events](https://docs.aws.amazon.com/eks/latest/userguide/fargate-pod-patching.html): Amazon EKS periodically patches the OS for AWS Fargate nodes to keep them secure.
- [Collect metrics](https://docs.aws.amazon.com/eks/latest/userguide/monitoring-fargate-usage.html): You can collect system metrics and CloudWatch usage metrics for AWS Fargate.
- [Logging](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html): Amazon EKS on Fargate offers a built-in log router based on Fluent Bit.
- [Amazon EC2 instance types](https://docs.aws.amazon.com/eks/latest/userguide/choosing-instance-type.html): Each Amazon EC2 instance type offers different compute, memory, storage, and network capabilities.

### [Pre-built optimized AMIs](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-amis.html)

You can deploy nodes with pre-built Amazon EKS optimized Amazon Machine Images (AMIs) or your own custom AMIs.

- [AL2 AMI deprecation](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-deprecation-faqs.html): This document outlines the End of Support (EOS) information for Amazon EKS AL2-optimized and AL2-accelerated AMIs.

### [Amazon Linux](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html)

Select an Amazon EKS-optimized Amazon Linux AMI to provision your cluster nodes with support for standard, accelerated, and Arm-based architectures.

- [Upgrade to AL2023](https://docs.aws.amazon.com/eks/latest/userguide/al2023.html): AL2023 is a new Linux-based operating system designed to provide a secure, stable, and high-performance environment for your cloud applications.
- [Get version information](https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html): This topic gives the location of Amazon EKS optimized Amazon Linux AMIs version information.
- [Get latest IDs](https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id.html): You can programmatically retrieve the Amazon Machine Image (AMI) ID for Amazon EKS optimized AMIs by querying the AWS Systems Manager Parameter Store API.
- [Build a custom EKS-optimized Amazon Linux AMI](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-build-scripts.html): Amazon Elastic Kubernetes Service (Amazon EKS) has open-source scripts that are used to build the Amazon EKS optimized AMI.

### [Bottlerocket](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami-bottlerocket.html)

Bottlerocket is an open source Linux distribution thatâs sponsored and supported by AWS.

- [Get version information](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-bottlerocket.html): This topic gives resources for Amazon EKS optimized Bottlerocket AMIs version information.
- [Get latest IDs](https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id-bottlerocket.html): You can retrieve the Amazon Machine Image (AMI) ID for Amazon EKS optimized AMIs by querying the AWS Systems Manager Parameter Store API.
- [Compliance support](https://docs.aws.amazon.com/eks/latest/userguide/bottlerocket-compliance-support.html): Bottlerocket complies with recommendations defined by various organizations.
- [Bottlerocket FIPS AMIs](https://docs.aws.amazon.com/eks/latest/userguide/bottlerocket-fips-amis.html): Bottlerocket makes it easier to adhere to FIPS by offering AMIs with a FIPS kernel.
- [Ubuntu Linux](https://docs.aws.amazon.com/eks/latest/userguide/eks-partner-amis.html): Canonical has partnered with Amazon EKS to create node AMIs that you can use in your clusters.

### [Windows](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-windows-ami.html)

Windows Amazon EKS optimized AMIs are built on top of Windows Server 2019.

- [Windows Server 2022](https://docs.aws.amazon.com/eks/latest/userguide/self-managed-windows-server-2022.html): This topic includes a YAML file as reference for creating self-managed Windows Server 2022 nodes.
- [Get version information](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html): This topic lists versions of the Amazon EKS optimized Windows AMIs and their corresponding versions of kubelet, containerd, and csi-proxy.
- [Get latest IDs](https://docs.aws.amazon.com/eks/latest/userguide/retrieve-windows-ami-id.html): You can programmatically retrieve the Amazon Machine Image (AMI) ID for Amazon EKS optimized AMIs by querying the AWS Systems Manager Parameter Store API.
- [Custom builds](https://docs.aws.amazon.com/eks/latest/userguide/eks-custom-ami-windows.html): You can use EC2 Image Builder to create custom Amazon EKS optimized Windows AMIs.

### [Node health and repair](https://docs.aws.amazon.com/eks/latest/userguide/node-health.html)

Use the EKS node monitoring agent to detect health issues and EKS node repair to automatically repair nodes when issues are detected.

- [Node health detection](https://docs.aws.amazon.com/eks/latest/userguide/node-health-nma.html): Understand how the EKS node monitoring agent detects health issues and how to configure its behavior
- [Automatic node repair](https://docs.aws.amazon.com/eks/latest/userguide/node-repair.html): Use EKS automatic node repair to automatically fix node health issues without manual intervention
- [View node health](https://docs.aws.amazon.com/eks/latest/userguide/learn-status-conditions.html): This topic explains the tools and methods available for monitoring node health status in Amazon EKS clusters.
- [Get node logs](https://docs.aws.amazon.com/eks/latest/userguide/auto-get-logs.html): Learn how to retrieve node logs for an Amazon EKS managed node that has the node monitoring agent.

### [Hybrid nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html)

Join nodes from your data centers to Amazon EKS Kubernetes clusters with Amazon EKS Hybrid Nodes.

### [Prerequisites](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-prereqs.html)

Learn about the prerequisites and requirements for joining nodes from your data centers to Amazon EKS Kubernetes clusters with Amazon EKS Hybrid Nodes.

- [Prepare networking](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-networking.html): Learn about and configure the VPC and on-premises networking for joining nodes from your data centers to Amazon EKS Kubernetes clusters with Amazon EKS Hybrid Nodes.
- [Prepare operating system](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-os.html): Prepare operating system for use with Hybrid Nodes
- [Prepare credentials](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-creds.html): Prepare credentials to authenticate hybrid nodes with Amazon EKS clusters Prepare credentials to authenticate hybrid nodes with Amazon EKS clusters
- [Create cluster](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cluster-create.html): Create hybrid nodes cluster
- [Existing cluster](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cluster-update.html): Modify hybrid nodes configuration on an existing cluster
- [Prepare cluster access](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cluster-prep.html): Prepare cluster access for Amazon EKS hybrid nodes

### [Run hybrid nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-tutorial.html)

Join nodes from your data centers to Amazon EKS Kubernetes clusters with Amazon EKS Hybrid Nodes.

- [Connect hybrid nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-join.html): Connect hybrid nodes to Amazon EKS cluster.
- [Connect hybrid nodes with Bottlerocket](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-bottlerocket.html): Connect hybrid nodes running Bottlerocket to an Amazon EKS cluster.
- [Upgrade hybrid nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-upgrade.html): Upgrade Kubernetes versions on hybrid nodes
- [Patch hybrid nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-security.html): Perform security updates on your Hybrid nodes
- [Delete hybrid nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-remove.html): Delete hybrid nodes from your EKS cluster

### [Configure](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-configure.html)

Learn how to configure CNI, BGP, application networking, add-ons, webhooks, and proxy settings for hybrid nodes.

- [Configure CNI](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cni.html): Configure the Cilium CNI for hybrid nodes
- [Configure add-ons](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-add-ons.html): Configure common add-ons for hybrid nodes
- [Configure webhooks](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-webhooks.html): Configure webhooks for hybrid nodes
- [Configure proxy](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-proxy.html): Configure HTTP/S proxies for Amazon EKS hybrid nodes
- [Configure BGP](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cilium-bgp.html): Configure Cilium Border Gateway Protocol (BGP) for hybrid nodes
- [Configure Ingress](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-ingress.html): Configure Kubernetes Ingress for hybrid nodes
- [Configure LoadBalancer Services](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-load-balancing.html): Configure Services of type LoadBalancer for hybrid nodes
- [Configure Network Policies](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-network-policies.html): Configure Kubernetes Network Policies for hybrid nodes

### [How it works](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-concepts.html)

Learn about EKS Hybrid Nodes technical concepts and how it works

- [Networking concepts](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-concepts-networking.html): Learn about the networking concepts for EKS Hybrid Nodes.
- [Kubernetes concepts](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-concepts-kubernetes.html): Learn about the key Kubernetes concepts for EKS Hybrid Nodes.
- [Traffic flows](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-concepts-traffic-flows.html): Learn about the network traffic flows for EKS Hybrid Nodes.
- [Hybrid nodes nodeadm](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-nodeadm.html): Hybrid nodes nodeadm reference
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-troubleshooting.html): Troubleshoot, diagnose, and repair hybrid nodes from your data centers to Amazon EKS Kubernetes clusters.


## [App data storage](https://docs.aws.amazon.com/eks/latest/userguide/storage.html)

- [Amazon EBS](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html): The Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver manages the lifecycle of Amazon EBS volumes as storage for Kubernetes Volumes.
- [Amazon EFS](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html): The Amazon EFS Container Storage Interface (CSI) driver provides a CSI interface that allows Kubernetes clusters running on AWS to manage the lifecycle of Amazon EFS file systems.

### [Amazon FSx for Lustre](https://docs.aws.amazon.com/eks/latest/userguide/fsx-csi.html)

The Amazon FSx for Lustre Container Storage Interface (CSI) driver provides a CSI interface that allows Amazon EKS clusters to manage the lifecycle of Amazon FSx for Lustre file systems.

- [Deploy the driver](https://docs.aws.amazon.com/eks/latest/userguide/fsx-csi-create.html): This topic shows you how to deploy the FSx for Lustre CSI driver to your Amazon EKS cluster and verify that it works.
- [Optimize (EFA)](https://docs.aws.amazon.com/eks/latest/userguide/fsx-csi-tuning-efa.html): Learn how to set up Elastic Fabric Adapter (EFA) tuning with Amazon EKS and Amazon FSx for Lustre.
- [Optimize (non-EFA)](https://docs.aws.amazon.com/eks/latest/userguide/fsx-csi-tuning-non-efa.html): Learn how to optimize Amazon FSx for Lustre performance on your Amazon EKS nodes by applying tuning parameters during node initialization.
- [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/eks/latest/userguide/fsx-ontap.html): The NetApp Trident allows Amazon EKS clusters to manage the lifecycle of persistent volumes (PVs) backed by Amazon FSx for NetApp ONTAP file systems.
- [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/eks/latest/userguide/fsx-openzfs-csi.html): The Amazon FSx for OpenZFS Container Storage Interface (CSI) driver provides a CSI interface that allows Amazon EKS clusters to manage the life cycle of Amazon FSx for OpenZFS volumes.
- [Amazon File Cache](https://docs.aws.amazon.com/eks/latest/userguide/file-cache-csi.html): The Amazon File Cache Container Storage Interface (CSI) driver provides a CSI interface that allows Amazon EKS clusters to manage the life cycle of Amazon file caches.

### [Mountpoint for Amazon S3](https://docs.aws.amazon.com/eks/latest/userguide/s3-csi.html)

Learn about the Amazon S3 Container Storage Interface (CSI) driver, which provides a CSI interface for managing Amazon S3 files and buckets.

- [Deploy the driver](https://docs.aws.amazon.com/eks/latest/userguide/s3-csi-create.html): This procedure will show you how to deploy the Mountpoint for Amazon S3 CSI Amazon EKS driver.
- [Remove the driver](https://docs.aws.amazon.com/eks/latest/userguide/removing-s3-csi-eks-add-on.html): This procedure will show you how to remove the Mountpoint for Amazon S3 CSI driver.
- [CSI snapshot controller](https://docs.aws.amazon.com/eks/latest/userguide/csi-snapshot-controller.html): The Container Storage Interface (CSI) snapshot controller enables the use of snapshot functionality in compatible CSI drivers, such as the Amazon EBS CSI driver.


## [Configure networking](https://docs.aws.amazon.com/eks/latest/userguide/eks-networking.html)

- [VPC and subnet requirements](https://docs.aws.amazon.com/eks/latest/userguide/network-reqs.html): Learn how to configure the VPC and subnets to meet networking requirements for creating Amazon EKS clusters with sufficient IP addresses, subnet types, and availability zones.
- [Create a VPC](https://docs.aws.amazon.com/eks/latest/userguide/creating-a-vpc.html): Learn how to create an Amazon VPC for your cluster using an Amazon EKS provided AWS CloudFormation template.
- [Security group requirements](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html): Learn how to manage security groups for Amazon EKS clusters, including default rules, restricting traffic, and required outbound access for nodes to function properly with your cluster.

### [Manage networking add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-networking-add-ons.html)

Learn how to manage networking add-ons for your Amazon EKS cluster, including built-in components like Amazon VPC CNI plugin for Kubernetes, CoreDNS, and kube-proxy, as well as optional AWS add-ons for load balancing and service mesh.

### [Amazon VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html)

Discover how the Amazon VPC CNI plugin for Kubernetes add-on works to assign private IP addresses and create network interfaces for Pods and services in your Amazon EKS cluster.

- [Create](https://docs.aws.amazon.com/eks/latest/userguide/vpc-add-on-create.html): Use the following steps to create the Amazon VPC CNI plugin for Kubernetes Amazon EKS add-on.
- [Update (EKS add-on)](https://docs.aws.amazon.com/eks/latest/userguide/vpc-add-on-update.html): Update the Amazon EKS type of the Amazon VPC CNI plugin for Kubernetes add-on.
- [Update (self-managed)](https://docs.aws.amazon.com/eks/latest/userguide/vpc-add-on-self-managed-update.html)
- [Configure for IRSA](https://docs.aws.amazon.com/eks/latest/userguide/cni-iam-role.html): Learn how to configure the Amazon VPC CNI plugin for Kubernetes to use IAM roles for service accounts (IRSA) for Pod networking in Amazon EKS clusters.

### [Modes and configuration](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking-use-cases.html)

Discover how Amazon VPC CNI plugin for Kubernetes provides pod networking capabilities and settings for different Amazon EKS node types and use cases, including security groups, Kubernetes network policies, custom networking, IPv4, and IPv6 support.

### [IPv6](https://docs.aws.amazon.com/eks/latest/userguide/cni-ipv6.html)

Learn how to deploy an IPv6 cluster and nodes with Amazon EKS for assigning IPv6 addresses to Pods and services instead of IPv4, leveraging IP prefix delegation and the latest Amazon VPC CNI plugin.

- [Deploy](https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html): In this tutorial, you deploy an IPv6 Amazon VPC, an Amazon EKS cluster with the IPv6 family, and a managed node group with Amazon EC2 Amazon Linux nodes.
- [Outbound traffic](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html): Learn how Amazon EKS manages external communication for Pods using Source Network Address Translation (SNAT), allowing Pods to access internet resources or networks connected via VPC peering, Transit Gateway, or AWS Direct Connect.

### [Kubernetes policies](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html)

Learn how to configure your Amazon EKS cluster to use Kubernetes network policies with the Amazon VPC CNI plugin.

- [Restrict traffic](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy-configure.html): Learn how to deploy Kubernetes network policies on your Amazon EKS cluster.
- [Disable](https://docs.aws.amazon.com/eks/latest/userguide/network-policy-disable.html): Learn how to disable Kubernetes network policies for Amazon EKS Pod network traffic.
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html): Learn how to troubleshoot and investigate network connections that use network policies.
- [Stars policy demo](https://docs.aws.amazon.com/eks/latest/userguide/network-policy-stars-demo.html): This demo creates a front-end, back-end, and client service on your Amazon EKS cluster.

### [Custom networking](https://docs.aws.amazon.com/eks/latest/userguide/cni-custom-network.html)

Learn how to enable custom networking for Amazon EKS Pods to deploy them in different subnets or use different security groups than the nodeâs primary network interface, increasing IP address availability and network isolation.

- [Secondary interface](https://docs.aws.amazon.com/eks/latest/userguide/cni-custom-network-tutorial.html): Learn how your Pods can use different security groups and subnets than the primary elastic network interface of the Amazon EC2 node that they run on.

### [Increase IP addresses](https://docs.aws.amazon.com/eks/latest/userguide/cni-increase-ip-addresses.html)

Learn how to significantly increase the number of IP addresses that you can assign to Pods by assigning IP prefixes with Amazon EKS, improving scalability and reducing launch delays for large and spiky workloads.

- [Procedure](https://docs.aws.amazon.com/eks/latest/userguide/cni-increase-ip-addresses-procedure.html): You can increase the number of IP addresses that nodes can assign to Pods by assigning IP prefixes, rather than assigning individual secondary IP addresses to your nodes.

### [Security groups for Pods](https://docs.aws.amazon.com/eks/latest/userguide/security-groups-for-pods.html)

Learn how to configure security groups for Pods on Amazon EKS, integrating Amazon EC2 security groups with Kubernetes Pods to define network traffic rules.

- [Configure](https://docs.aws.amazon.com/eks/latest/userguide/security-groups-pods-deployment.html): If you use Pods with Amazon EC2 instances, you need to configure the Amazon VPC CNI plugin for Kubernetes for security groups
- [SecurityGroupPolicy](https://docs.aws.amazon.com/eks/latest/userguide/sg-pods-example-deployment.html): To use security groups for Pods, you must have an existing security group.
- [Multiple interfaces](https://docs.aws.amazon.com/eks/latest/userguide/pod-multiple-network-interfaces.html): Learn how to use VPC CNI to attach multiple network interfaces to a Pod in Amazon EKS for advanced networking scenarios with high bandwidth.
- [Alternate CNI plugins](https://docs.aws.amazon.com/eks/latest/userguide/alternate-cni-plugins.html): Learn how to use alternate network and security plugins on Amazon EKS to customize networking for your Kubernetes clusters on Amazon EC2 nodes.
- [Multus](https://docs.aws.amazon.com/eks/latest/userguide/pod-multus.html): Learn how to use Multus CNI to attach multiple network interfaces to a Pod in Amazon EKS for advanced networking scenarios, while leveraging the Amazon VPC CNI plugin for primary networking.

### [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

Learn how to configure and use the AWS Load Balancer Controller to expose Kubernetes cluster apps to the internet with AWS Elastic Load Balancing for Kubernetes services and ingresses.

- [Install with Helm](https://docs.aws.amazon.com/eks/latest/userguide/lbc-helm.html): Learn how to install the AWS Load Balancer Controller on Amazon EKS using Helm to manage K8s load balancing with AWS Cloud.
- [Install with manifests](https://docs.aws.amazon.com/eks/latest/userguide/lbc-manifest.html): Install the AWS Load Balancer Controller add-on for Amazon EKS using Kubernetes manifests to provision Elastic Load Balancing resources.
- [Migrate from deprecated](https://docs.aws.amazon.com/eks/latest/userguide/lbc-remove.html): Learn how to migrate from the deprecated ALB Ingress Controller to the latest AWS Load Balancer Controller release, ensuring smooth transition and uninterrupted load balancing capabilities.

### [CoreDNS](https://docs.aws.amazon.com/eks/latest/userguide/managing-coredns.html)

Learn how to manage the CoreDNS Amazon EKS add-on for DNS service discovery in Kubernetes clusters with configuration updates and version upgrades.

- [Create](https://docs.aws.amazon.com/eks/latest/userguide/coredns-add-on-create.html): Create the CoreDNS Amazon EKS add-on.
- [Update (EKS add-on)](https://docs.aws.amazon.com/eks/latest/userguide/coredns-add-on-update.html): Update the Amazon EKS type of the add-on.
- [Update (self-managed)](https://docs.aws.amazon.com/eks/latest/userguide/coredns-add-on-self-managed-update.html)
- [Scale for high traffic](https://docs.aws.amazon.com/eks/latest/userguide/coredns-autoscaling.html): Learn how the Amazon EKS add-on for CoreDNS autoscales to handle increased load on DNS pods, improving application availability and cluster scalability.
- [Monitor DNS resolution](https://docs.aws.amazon.com/eks/latest/userguide/coredns-metrics.html): Learn how to collect CoreDNS metrics in Amazon EKS using Prometheus or CloudWatch Agent, enabling monitoring and observability for your Kubernetes DNS resolution.

### [kube-proxy](https://docs.aws.amazon.com/eks/latest/userguide/managing-kube-proxy.html)

Learn how to manage the kube-proxy add-on on your Amazon EKS cluster to manage network rules and enable network communication to your Pods.

- [Update](https://docs.aws.amazon.com/eks/latest/userguide/kube-proxy-add-on-self-managed-update.html)


## [Workloads](https://docs.aws.amazon.com/eks/latest/userguide/eks-workloads.html)

- [Sample deployment (Linux)](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html): In this topic, you deploy a sample application to your cluster on linux nodes.
- [Sample deployment (Windows)](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment-win.html): In this topic, you deploy a sample application to your cluster on Windows nodes.
- [Vertical Pod Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/vertical-pod-autoscaler.html): Discover how the Kubernetes Vertical Pod Autoscaler automatically adjusts CPU and memory reservations for your Pods to optimize resource utilization and right-size applications on Amazon EKS.
- [Horizontal Pod Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html): Learn how to use the Kubernetes Horizontal Pod Autoscaler to automatically scale your Amazon EKS deployments based on CPU utilization for efficient resource management.
- [Network load balancing](https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html): Use the AWS Load Balancer Controller to create network load balancers for Amazon EKS workloads, supporting IP and instance targets with AWS Network Load Balancers.
- [Application load balancing](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html): Learn how to use Application Load Balancing on Amazon EKS to load balance application traffic at L7 with AWS Load Balancer Controller.
- [Restrict service external IPs](https://docs.aws.amazon.com/eks/latest/userguide/restrict-service-external-ip.html): Kubernetes services can be reached from inside of a cluster through:
- [Copy an image to a repository](https://docs.aws.amazon.com/eks/latest/userguide/copy-image-to-repository.html): This topic describes how to pull a container image from a repository that your nodes donât have access to and push the image to a repository that your nodes have access to.
- [View Amazon image registries](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-images.html): When you deploy AWS Amazon EKS add-ons to your cluster, your nodes pull the required container images from the registry specified in the installation mechanism for the add-on, such as an installation manifest or a Helm values.yaml file.

### [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)

Learn how to manage operational software add-ons on Amazon EKS clusters with Amazon EKS add-ons for observability, networking, storage, and security from AWS and third-party vendors.

- [AWS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html): Learn about the available Amazon EKS add-ons from AWS.
- [Community add-ons](https://docs.aws.amazon.com/eks/latest/userguide/community-addons.html): You can use AWS APIs to install community add-ons, such as the Kubernetes Metrics Server.
- [Marketplace add-ons](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-vendors.html): Learn about the Amazon EKS add-ons from independent software vendors.
- [Create an add-on](https://docs.aws.amazon.com/eks/latest/userguide/creating-an-add-on.html): Learn how to create an add-on for your Amazon EKS cluster.
- [Update an add-on](https://docs.aws.amazon.com/eks/latest/userguide/updating-an-add-on.html): Learn how to update your Amazon EKS add-on to a new version.
- [Verify compatibility](https://docs.aws.amazon.com/eks/latest/userguide/addon-compat.html): Learn how to verify the Amazon EKS add-on compatibility with your cluster before you create or update an Amazon EKS add-on.
- [Remove an add-on](https://docs.aws.amazon.com/eks/latest/userguide/removing-an-add-on.html): Learn how to remove an Amazon EKS add-on.

### [IAM roles](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html)

Grant an Amazon EKS add-on permission to call AWS APIs.

- [Retrieve IAM information](https://docs.aws.amazon.com/eks/latest/userguide/retreive-iam-info.html): Learn how to determine the role and policy to use for an Amazon EKS add-on.
- [Use Pod Identities](https://docs.aws.amazon.com/eks/latest/userguide/update-addon-role.html): Learn how to use a Pod Identity to assign a role for an Amazon EKS add-on.
- [Remove Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/remove-addon-role.html): Learn how to remove a Pod Identity from an Amazon EKS add-on.
- [Troubleshoot Identities](https://docs.aws.amazon.com/eks/latest/userguide/addon-id-troubleshoot.html): Learn how to troubleshoot Pod Identities for EKS add-ons.
- [Fields you can customize](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-field-management.html): Learn how to manage Amazon EKS add-on configurations using Kubernetes field management to customize settings without overwriting Amazon EKS managed fields.
- [Verify container images](https://docs.aws.amazon.com/eks/latest/userguide/image-verification.html): Learn how to verify signed container images during deployment on Amazon EKS using admission controllers like Gatekeeper with Ratify or Kyverno configured with AWS Signer plugins for validating image signatures.


## [EKS Capabilities](https://docs.aws.amazon.com/eks/latest/userguide/capabilities.html)

- [Working with capabilities](https://docs.aws.amazon.com/eks/latest/userguide/working-with-capabilities.html): Learn how to manage capability resources on your Amazon EKS clusters, including listing, describing, updating, and deleting capabilities.
- [Kubernetes resources](https://docs.aws.amazon.com/eks/latest/userguide/capability-kubernetes-resources.html): Learn about the Kubernetes custom resources provided by each EKS capability type and how to use them in your clusters.
- [Considerations](https://docs.aws.amazon.com/eks/latest/userguide/capabilities-considerations.html): Plan your EKS Capabilities deployment with guidance on choosing between managed and self-managed solutions, multi-cluster architecture patterns, and operational considerations.

### [AWS Controllers for Kubernetes](https://docs.aws.amazon.com/eks/latest/userguide/ack.html)

Manage AWS resources natively in Kubernetes with AWS Controllers for Kubernetes (ACK), a fully managed capability of Amazon EKS.

### [Create ACK capability](https://docs.aws.amazon.com/eks/latest/userguide/create-ack-capability.html)

Learn how to create an AWS Controllers for Kubernetes (ACK) capability on your Amazon EKS cluster using the Console, AWS CLI, or eksctl.

- [Console](https://docs.aws.amazon.com/eks/latest/userguide/ack-create-console.html): This topic describes how to create an AWS Controllers for Kubernetes (ACK) capability using the AWS Management Console.
- [AWS CLI](https://docs.aws.amazon.com/eks/latest/userguide/ack-create-cli.html): This topic describes how to create an AWS Controllers for Kubernetes (ACK) capability using the AWS CLI.
- [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/ack-create-eksctl.html): This topic describes how to create an AWS Controllers for Kubernetes (ACK) capability using eksctl.
- [ACK concepts](https://docs.aws.amazon.com/eks/latest/userguide/ack-concepts.html): Understand core ACK concepts including resource lifecycle, reconciliation, status conditions, and resource ownership.
- [Configure permissions](https://docs.aws.amazon.com/eks/latest/userguide/ack-permissions.html): Configure IAM permissions for ACK to manage AWS resources using Capability Roles and IAM Role Selectors.
- [Considerations](https://docs.aws.amazon.com/eks/latest/userguide/ack-considerations.html): Plan your ACK deployment with EKS-specific patterns, IAM configuration, and integration strategies.
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/ack-troubleshooting.html): Diagnose and resolve common issues with the EKS Capability for ACK.
- [Comparison to self-managed](https://docs.aws.amazon.com/eks/latest/userguide/ack-comparison.html): Understand the differences between the EKS Capability for ACK and self-managed ACK controllers.

### [Argo CD](https://docs.aws.amazon.com/eks/latest/userguide/argocd.html)

Implement GitOps-based continuous deployment with Argo CD, a fully managed capability of Amazon EKS.

### [Create Argo CD capability](https://docs.aws.amazon.com/eks/latest/userguide/create-argocd-capability.html)

Learn how to create an Argo CD capability on your Amazon EKS cluster using the Console, AWS CLI, or eksctl.

- [Console](https://docs.aws.amazon.com/eks/latest/userguide/argocd-create-console.html): This topic describes how to create an Argo CD capability using the AWS Management Console.
- [AWS CLI](https://docs.aws.amazon.com/eks/latest/userguide/argocd-create-cli.html): This topic describes how to create an Argo CD capability using the AWS CLI.
- [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/argocd-create-eksctl.html): This topic describes how to create an Argo CD capability using eksctl.
- [Argo CD concepts](https://docs.aws.amazon.com/eks/latest/userguide/argocd-concepts.html): Learn Argo CD fundamentals through a practical example, then explore core concepts including GitOps principles, sync behavior, and multi-cluster patterns.
- [Configure permissions](https://docs.aws.amazon.com/eks/latest/userguide/argocd-permissions.html): Configure authentication and authorization for Argo CD using AWS Identity Center integration and project-based access control.

### [Working with Argo CD](https://docs.aws.amazon.com/eks/latest/userguide/working-with-argocd.html)

Deploy and manage applications using GitOps with the Argo CD managed capability.

- [Configure repositories](https://docs.aws.amazon.com/eks/latest/userguide/argocd-configure-repositories.html): Configure Argo CD to access your Git repositories using various authentication methods.
- [Register clusters](https://docs.aws.amazon.com/eks/latest/userguide/argocd-register-clusters.html): Register Kubernetes clusters where Argo CD will deploy applications.
- [Projects](https://docs.aws.amazon.com/eks/latest/userguide/argocd-projects.html): Use Argo CD Projects to organize applications and enforce security boundaries for multi-tenant environments.
- [Create Applications](https://docs.aws.amazon.com/eks/latest/userguide/argocd-create-application.html): Create Argo CD Applications to deploy from Git repositories with automated or manual sync.
- [ApplicationSets](https://docs.aws.amazon.com/eks/latest/userguide/argocd-applicationsets.html): Deploy applications across multiple environments or clusters using ApplicationSet templates and generators.
- [Argo CD considerations](https://docs.aws.amazon.com/eks/latest/userguide/argocd-considerations.html): Plan your Argo CD deployment, configure IAM permissions, set up authentication with AWS Identity Center, and enable multi-cluster deployments.
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/argocd-troubleshooting.html): Diagnose and resolve common issues with the EKS Capability for Argo CD.
- [Comparison to self-managed](https://docs.aws.amazon.com/eks/latest/userguide/argocd-comparison.html): Understand the differences between the EKS Capability for Argo CD and self-managed Argo CD installations.

### [kro](https://docs.aws.amazon.com/eks/latest/userguide/kro.html)

Simplify resource management with kro (Kube Resource Orchestrator), a fully managed capability of Amazon EKS for Kubernetes resource composition and orchestration.

### [Create kro capability](https://docs.aws.amazon.com/eks/latest/userguide/create-kro-capability.html)

Learn how to create a kro (Kube Resource Orchestrator) capability on your Amazon EKS cluster using the Console, AWS CLI, or eksctl.

- [Console](https://docs.aws.amazon.com/eks/latest/userguide/kro-create-console.html): This topic describes how to create a kro (Kube Resource Orchestrator) capability using the AWS Management Console.
- [AWS CLI](https://docs.aws.amazon.com/eks/latest/userguide/kro-create-cli.html): This topic describes how to create a kro (Kube Resource Orchestrator) capability using the AWS CLI.
- [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/kro-create-eksctl.html): This topic describes how to create a kro (Kube Resource Orchestrator) capability using eksctl.
- [kro concepts](https://docs.aws.amazon.com/eks/latest/userguide/kro-concepts.html): Learn kro fundamentals through a practical example, then explore core concepts including SimpleSchema, CEL expressions, and resource composition.
- [Configure permissions](https://docs.aws.amazon.com/eks/latest/userguide/kro-permissions.html): Configure Kubernetes RBAC permissions to control access to kro ResourceGraphDefinitions and custom resource instances.
- [Considerations](https://docs.aws.amazon.com/eks/latest/userguide/kro-considerations.html): Plan your kro deployment with EKS-specific patterns, RBAC configuration, and integration strategies.
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/kro-troubleshooting.html): Diagnose and resolve common issues with the EKS Capability for kro.
- [Comparison to self-managed](https://docs.aws.amazon.com/eks/latest/userguide/kro-comparison.html): Understand the differences between the EKS Capability for kro and self-managed kro.
- [Troubleshoot capabilities](https://docs.aws.amazon.com/eks/latest/userguide/capabilities-troubleshooting.html): Diagnose and resolve common issues with EKS Capabilities.


## [Cluster management](https://docs.aws.amazon.com/eks/latest/userguide/eks-managing.html)

### [Cost monitoring](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring.html)

Learn how to monitor and optimize costs for your Amazon EKS clusters using AWS Billing split cost allocation data or Kubecost, a Kubernetes-native cost monitoring tool integrated with AWS.

- [View costs by Pod](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring-aws.html)
- [Install Kubecost](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring-kubecost.html): Amazon EKS supports Kubecost, which you can use to monitor your costs broken down by Kubernetes resources including Pods, nodes, namespaces, and labels.
- [Access Kubecost Dashboard](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring-kubecost-dashboard.html)
- [Learn more about Kubecost](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring-kubecost-bundles.html): Amazon EKS provides an AWS optimized bundle of Kubecost for cluster cost visibility.
- [Metrics server](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html): Use the Kubernetes Metrics Server to view resource usage data on your Amazon EKS cluster for autoscaling and monitoring.
- [Deploy apps with Helm](https://docs.aws.amazon.com/eks/latest/userguide/helm.html): Learn how to install and use Helm, a package manager for Kubernetes, with your Amazon EKS cluster to manage and deploy applications seamlessly.
- [Tagging your resources](https://docs.aws.amazon.com/eks/latest/userguide/eks-using-tags.html): Learn how to use tags to categorize and manage your Amazon EKS resources like clusters, managed node groups, and Fargate profiles for billing, cost allocation, and resource identification.
- [Service quotas](https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html): Use Service Quotas to view and manage Amazon EKS and AWS Fargate quotas from the AWS Management Console or AWS CLI.


## [Security](https://docs.aws.amazon.com/eks/latest/userguide/security.html)

- [Best practices](https://docs.aws.amazon.com/eks/latest/userguide/security-best-practices.html): Learn how to secure your Amazon EKS clusters by following the best practices from the community.
- [Analyze vulnerabilities](https://docs.aws.amazon.com/eks/latest/userguide/configuration-vulnerability-analysis.html): Learn how to analyze the security configuration and vulnerabilities of your Amazon EKS clusters and resources using tools like the CIS EKS Benchmark, platform versions, vulnerability lists, Amazon Inspector, and Amazon GuardDuty for comprehensive threat detection and protection.
- [Validate compliance](https://docs.aws.amazon.com/eks/latest/userguide/compliance.html): Discover compliance resources to help secure your AWS workloads, meet regulatory requirements like HIPAA, and validate adherence to security standards.

### [Considerations for EKS](https://docs.aws.amazon.com/eks/latest/userguide/security-eks.html)

Configure Amazon EKS clusters to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Amazon EKS clusters.

### [Infrastructure security](https://docs.aws.amazon.com/eks/latest/userguide/infrastructure-security.html)

Learn how Amazon EKS isolates service traffic.

- [AWS PrivateLink](https://docs.aws.amazon.com/eks/latest/userguide/vpc-interface-endpoints.html): Learn how to securely access Amazon Elastic Kubernetes Service (Amazon EKS) APIs from within your VPC using AWS PrivateLink, avoiding public internet exposure while benefiting from private connectivity, routing optimization, and built-in security controls for enhanced cluster management.
- [Resilience](https://docs.aws.amazon.com/eks/latest/userguide/disaster-recovery-resiliency.html): Learn how Amazon EKS ensures high availability, data resilience, and fault tolerance for your Kubernetes control plane by leveraging AWS infrastructure across multiple Availability Zones .
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/eks/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesnât have permission to perform an action can coerce a more-privileged entity to perform the action.

### [Considerations for Kubernetes](https://docs.aws.amazon.com/eks/latest/userguide/security-k8s.html)

Configure Kubernetes to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Kubernetes resources.

- [Certificate signing](https://docs.aws.amazon.com/eks/latest/userguide/cert-signing.html): Learn how to request and obtain X.509 certificates from the Certificate Authority (CA) using Certificate Signing Requests (CSRs) in Amazon EKS, including details on migrating from legacy signers, generating CSRs, approving requests, and handling certificate signing considerations.
- [Default roles and users](https://docs.aws.amazon.com/eks/latest/userguide/default-roles-users.html): Learn about the Kubernetes roles and users that Amazon EKS creates for cluster components and add-ons.
- [Enable secret encryption](https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html): Learn how to enable Kubernetes secrets encryption with AWS KMS on an existing Amazon EKS cluster, ensuring secure storage of sensitive data.
- [AWS Secrets Manager](https://docs.aws.amazon.com/eks/latest/userguide/manage-secrets.html): To show secrets from Secrets Manager and parameters from Parameter Store as files mounted in Amazon EKS Pods, you can use the AWS Secrets and Configuration Provider (ASCP) for the Kubernetes Secrets Store CSI Driver.
- [Default envelope encryption for all Kubernetes API Data](https://docs.aws.amazon.com/eks/latest/userguide/envelope-encryption.html): Amazon Elastic Kubernetes Service (Amazon EKS) provides default envelope encryption for all Kubernetes API data in EKS clusters running Kubernetes version 1.28 or higher.
- [Considerations for EKS Auto](https://docs.aws.amazon.com/eks/latest/userguide/auto-security.html): This topic describes the security architecture, controls, and best practices for Amazon EKS Auto Mode.
- [Considerations for EKS Capabilities](https://docs.aws.amazon.com/eks/latest/userguide/capabilities-security.html): Plan your EKS Capabilities deployment with security best practices, IAM configuration, and multi-cluster architecture patterns.

### [IAM Reference](https://docs.aws.amazon.com/eks/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your Amazon EKS resources.

- [Amazon EKS and IAM](https://docs.aws.amazon.com/eks/latest/userguide/security-iam-service-with-iam.html): Before you use IAM to manage access to Amazon EKS, you should understand what IAM features are available to use with Amazon EKS.
- [Identity-based policies](https://docs.aws.amazon.com/eks/latest/userguide/security-iam-id-based-policy-examples.html): By default, IAM users and roles donât have permission to create or modify Amazon EKS resources.

### [Service-linked roles](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give Amazon EKS access to resources in your AWS account.

- [Cluster role](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks.html): How to use service-linked roles to give Amazon EKS access to resources in your AWS account.
- [Node groups role](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-nodegroups.html): How to use service-linked roles to give Amazon EKS access to resources in your AWS account.
- [Fargate profile role](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-fargate.html): How to use service-linked roles to give Amazon EKS access to resources in your AWS account.
- [Cluster connector role](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-connector.html): How to use service-linked roles to give Amazon EKS access to resources in your AWS account.
- [Local cluster role](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-outpost.html): How to use service-linked roles to give Amazon EKS access to resources in your AWS account.
- [Dashboard role](https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-dashboard.html): How to use service-linked roles to give Amazon EKS access to resources in your AWS accounts for the Amazon EKS Dashboard.
- [Pod execution IAM role](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html): The Amazon EKS Pod execution role is required to run Pods on AWS Fargate infrastructure.
- [Connector IAM role](https://docs.aws.amazon.com/eks/latest/userguide/connector-iam-role.html): You can connect Kubernetes clusters to view them in your AWS Management Console.
- [AWS managed policies](https://docs.aws.amazon.com/eks/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon EKS and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/security-iam-troubleshoot.html): This topic covers some common errors that you may see while using Amazon EKS with IAM and how to work around them.
- [Cluster IAM role](https://docs.aws.amazon.com/eks/latest/userguide/cluster-iam-role.html): Learn how to create and configure the required AWS Identity and Access Management role for Amazon EKS clusters to manage nodes and load balancers using managed or custom IAM policies.
- [Node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html): The Amazon EKS node kubelet daemon makes calls to AWS APIs on your behalf.
- [Auto Mode cluster IAM role](https://docs.aws.amazon.com/eks/latest/userguide/auto-cluster-iam-role.html): Learn how to create and configure the required AWS Identity and Access Management role for Amazon EKS Auto Mode clusters to automate routine tasks for storage, networking, and compute autoscaling.
- [Auto Mode node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/auto-create-node-role.html)
- [Capability IAM role](https://docs.aws.amazon.com/eks/latest/userguide/capability-role.html): Learn how to create and configure the required AWS Identity and Access Management role for Amazon EKS capabilities to manage AWS resources and access Kubernetes resources.


## [Monitor clusters](https://docs.aws.amazon.com/eks/latest/userguide/eks-observe.html)

- [Observability dashboard](https://docs.aws.amazon.com/eks/latest/userguide/observability-dashboard.html): Learn how to configure logging for your Amazon EKS cluster.
- [Container network observability](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html): Amazon EKS provides enhanced network observability features that provide deeper insights into your container networking environment.

### [Prometheus metrics](https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html)

This topic explains how to deploy Prometheus and some of the ways that you can use it to view and analyze what your cluster is doing.

- [Deploy using Helm](https://docs.aws.amazon.com/eks/latest/userguide/deploy-prometheus.html): As an alternative to using Amazon Managed Service for Prometheus, you can deploy Prometheus into your cluster with supported Helm versions.
- [Control plane](https://docs.aws.amazon.com/eks/latest/userguide/view-raw-metrics.html): The Kubernetes control plane exposes a number of metrics that are represented in a Prometheus format.
- [Amazon CloudWatch](https://docs.aws.amazon.com/eks/latest/userguide/cloudwatch.html): With Amazon CloudWatch, you can view metrics, real-time logs, and trace data.
- [Control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html): Learn how to configure logging for your Amazon EKS cluster.

### [AWS CloudTrail](https://docs.aws.amazon.com/eks/latest/userguide/logging-using-cloudtrail.html)

Learn about logging Amazon EKS with AWS CloudTrail.

- [References](https://docs.aws.amazon.com/eks/latest/userguide/service-name-info-in-cloudtrail.html): When any activity occurs in Amazon EKS, that activity is recorded in a CloudTrail event.
- [Log file entries](https://docs.aws.amazon.com/eks/latest/userguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.
- [Auto Scaling group metrics](https://docs.aws.amazon.com/eks/latest/userguide/enable-asg-metrics.html): You can use Amazon EC2 Auto Scaling group metrics to track changes in an Auto Scaling group and to set alarms on threshold values.
- [ADOT Operator](https://docs.aws.amazon.com/eks/latest/userguide/opentelemetry.html): The AWS Distro for OpenTelemetry (ADOT) Operator makes it easier to enable your applications running on Amazon EKS to send metric and trace data to multiple monitoring service options.

### [Amazon EKS Dashboard](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard.html)

- [Configure organizations](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard-orgs.html): This section provides step-by-step instructions for configuring the EKS Dashboardâs integration with AWS Organizations.


## [Working with other services](https://docs.aws.amazon.com/eks/latest/userguide/eks-integrations.html)

- [AWS Backup](https://docs.aws.amazon.com/eks/latest/userguide/integration-backup.html): AWS Backup supports backups of Amazon EKS clusters, including Kubernetes cluster state and persistent storage attached to the EKS cluster via a persistent volume claim (EBS volumes, EFS file systems, and S3 buckets).
- [AWS CloudFormation](https://docs.aws.amazon.com/eks/latest/userguide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon EKS using an AWS CloudFormation template.
- [AWS CodeConnections](https://docs.aws.amazon.com/eks/latest/userguide/integration-codeconnections.html): AWS CodeConnections provides secure authentication to third-party Git repositories like GitHub, GitLab, and Bitbucket.
- [Amazon Detective](https://docs.aws.amazon.com/eks/latest/userguide/integration-detective.html): Amazon Detective helps you analyze, investigate, and quickly identify the root cause of security findings or suspicious activities.
- [Amazon GuardDuty](https://docs.aws.amazon.com/eks/latest/userguide/integration-guardduty.html): Amazon GuardDuty is a threat detection service that helps protect you accounts, containers, workloads, and the data with your AWS environment.
- [AWS Local Zones](https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html): An AWS Local Zone is an extension of an AWS Region in geographic proximity to your users.
- [AWS Resilience Hub](https://docs.aws.amazon.com/eks/latest/userguide/integration-resilience-hub.html): AWS Resilience Hub assesses the resiliency of an Amazon EKS cluster by analyzing its infrastructure.
- [AWS Secrets Manager](https://docs.aws.amazon.com/eks/latest/userguide/integration-secrets-manager.html): AWS Secrets Manager helps you manage, access, and rotate credentials, API keys, and other secrets throughout their lifecycle.
- [Amazon Security Lake](https://docs.aws.amazon.com/eks/latest/userguide/integration-securitylake.html): Amazon Security Lake integrates with Amazon EKS to provide a centralized and standardized solution for collecting, storing, and analyzing security data from clusters.
- [Amazon VPC Lattice](https://docs.aws.amazon.com/eks/latest/userguide/integration-vpc-lattice.html): Amazon VPC Lattice is a fully managed application networking service built directly into the AWS networking infrastructure that you can use to connect, secure, and monitor your services across multiple accounts and Virtual Private Clouds (VPCs).


## [Amazon EKS Connector](https://docs.aws.amazon.com/eks/latest/userguide/eks-connector.html)

- [Connect a cluster](https://docs.aws.amazon.com/eks/latest/userguide/connecting-cluster.html): Learn to connect an external Kubernetes cluster to an Amazon EKS Management Console and install the eks-connector agent via Helm or YAML manifests to enable visibility and management of the external cluster.
- [Grant access to clusters](https://docs.aws.amazon.com/eks/latest/userguide/connector-grant-access.html): Learn to grant IAM principals access to view Kubernetes cluster resources on an Amazon EKS Management Console.
- [Deregister a cluster](https://docs.aws.amazon.com/eks/latest/userguide/deregister-connected-cluster.html): Learn to deregister a Kubernetes cluster from Amazon EKS and uninstall the eks-connector agent to stop managing the cluster from the Amazon EKS Management Console.
- [Troubleshoot EKS Connector](https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting-connector.html): Troubleshoot and resolve common issues when using Amazon EKS Connector to connect your Kubernetes clusters to Amazon EKS.
- [Frequently asked questions](https://docs.aws.amazon.com/eks/latest/userguide/tsc-faq.html): Learn to connect and manage Kubernetes clusters outside AWS with Amazon EKS Connector, enabling unified cluster visibility and management across environments using a secure, outbound-only connection.
- [Security considerations](https://docs.aws.amazon.com/eks/latest/userguide/security-connector.html): Learn how the open-source EKS Connector affects security, and understand AWS and customer security responsibilities for connectivity, cluster management, and IAM access control.


## [Amazon EKS on AWS Outposts](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts.html)

### [Run local clusters](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-overview.html)

Learn to create and manage local Amazon EKS clusters on AWS Outposts for high availability across multiple regions.

- [Deploy a local cluster](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-create.html): Learn to create a local Amazon EKS cluster on AWS Outposts.
- [EKS platform versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-platform-versions.html): Learn the relationship between Amazon EKS and Kubernetes versions available on AWS Outposts.
- [Create a VPC and subnets](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-vpc-subnet-requirements.html): Learn about VPC and subnet requirements and considerations, then to create a VPC and subnets for Amazon EKS local clusters on AWS Outposts.
- [Prepare for disconnects](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-network-disconnects.html): Learn how to prepare your Amazon EKS local cluster on AWS Outposts for network disconnects, including x.509 certificate authentication, monitoring, scaling, and storage options.
- [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html): Learn how to select instance types and optionally use placement groups to meet high availability requirements for your Amazon EKS local cluster on AWS Outposts.
- [Troubleshoot clusters](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-troubleshooting.html): Learn how to troubleshoot common issues with Amazon EKS local clusters on AWS Outposts, including cluster creation failures, node join problems, and control plane instance reachability issues through AWS Systems Manager.
- [Nodes](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-self-managed-nodes.html): Learn how to launch Auto Scaling groups of Amazon Linux nodes on an Outpost that register with your Amazon EKS cluster.


## [AI/ML on EKS](https://docs.aws.amazon.com/eks/latest/userguide/machine-learning-on-eks.html)

### [Real-time inference](https://docs.aws.amazon.com/eks/latest/userguide/ml-realtime-inference.html)

Learn how to set up and manage real-time online inference workloads on Amazon EKS.

- [Create cluster](https://docs.aws.amazon.com/eks/latest/userguide/ml-realtime-inference-cluster.html): Learn how to set up an Amazon EKS cluster optimized for real-time online inference workloads using GPU-accelerated nodes, Karpenter for autoscaling, and integrate AWS services to serve a model.
- [LLM inference with vLLM](https://docs.aws.amazon.com/eks/latest/userguide/ml-realtime-inference-llm-inference-vllm.html): Deploy Large Language Models (LLMs) on Amazon EKS using vLLM and GPUs for text-based real-time inference applications.

### [Cluster configuration](https://docs.aws.amazon.com/eks/latest/userguide/ml-cluster-configuration.html)

Learn different ways to setup and configure Amazon EKS clusters for AI/ML workloads.

- [Use EKS Linux GPU AMIs](https://docs.aws.amazon.com/eks/latest/userguide/ml-eks-optimized-ami.html): Amazon EKS supports EKS-optimized Amazon Linux and Bottlerocket AMIs for GPU instances.
- [Install device plugin for GPUs](https://docs.aws.amazon.com/eks/latest/userguide/ml-eks-k8s-device-plugin.html): Kubernetes device plugins have been the primary mechanism for advertising specialized infrastructure such as GPUs, network interfaces, and network adaptors as consumable resources for Kubernetes workloads.
- [Set up Windows GPU AMIs](https://docs.aws.amazon.com/eks/latest/userguide/ml-eks-windows-optimized-ami.html)
- [Set up training clusters with EFA](https://docs.aws.amazon.com/eks/latest/userguide/node-efa.html): Learn how to integrate Elastic Fabric Adapter (EFA) with Amazon EKS to run machine learning training workloads requiring high inter-node communications at scale using p4d instances with GPUDirect RDMA and NVIDIA Collective Communications Library (NCCL).
- [Set up inference clusters with Inferentia](https://docs.aws.amazon.com/eks/latest/userguide/inferentia-support.html): Learn how to create an Amazon EKS cluster with nodes running Amazon EC2 Inf1 instances for machine learning inference using AWS Inferentia chips and deploy a TensorFlow Serving application.

### [Capacity management](https://docs.aws.amazon.com/eks/latest/userguide/ml-compute-management.html)

Learn how to manage compute resources for machine learning workloads in Amazon EKS.

- [Reserve GPUs for managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/capacity-blocks-mng.html): Capacity Blocks for machine learning (ML) allow you to reserve highly sought-after GPU instances on a future date to support your short duration ML workloads.
- [Reserve GPUs for self-managed nodes](https://docs.aws.amazon.com/eks/latest/userguide/capacity-blocks.html): Capacity Blocks for machine learning (ML) allow you to reserve highly sought-after GPU instances on a future date to support your short duration ML workloads.
- [Use P6e-GB200 with EKS](https://docs.aws.amazon.com/eks/latest/userguide/ml-eks-nvidia-ultraserver.html): Learn how to use the Amazon EC2 P6e-GB200 UltraServers with Amazon EKS, accelerated by NVIDIA GB200 NVL72

### [Recipes](https://docs.aws.amazon.com/eks/latest/userguide/ml-recipes.html)

Follow bite-sized recipes to optimize your Amazon EKS clusters for AI/ML workloads.

- [Prevent pods from being scheduled on specific nodes](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html): Taints and tolerations work together to ensure that Pods arenât scheduled onto inappropriate nodes.
- [Resources](https://docs.aws.amazon.com/eks/latest/userguide/ml-resources.html): Choose the Machine Learning on EKS tools and platforms that best suit your needs, then use quick start procedures to deploy ML workloads and EKS clusters to the AWS cloud.


## [Tools](https://docs.aws.amazon.com/eks/latest/userguide/eks-tools.html)

### [Model Context Protocol (MCP)](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-introduction.html)

Learn how to manage your Amazon EKS cluster, Kubernetes resources, diagnose issues, and query Amazon EKS documentation with the EKS MCP Server.

- [Get started](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-getting-started.html): This guide walks you through the steps to setup and use the EKS MCP Server with your AI code assistants.
- [Configuration](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html): This guide shows all the configurations available for the mcp-proxy-for-aws client-side tool that allows you to connect to the fully managed Amazon EKS MCP Server from your IDE.
- [Tools](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tools.html): The server exposes the following MCP tools.
- [Amazon Q](https://docs.aws.amazon.com/eks/latest/userguide/amazon-q-integration.html): Amazon Elastic Kubernetes Service (EKS) integrates with Amazon Q to provide AI-powered troubleshooting directly in the AWS Management Console.


## [Versioning](https://docs.aws.amazon.com/eks/latest/userguide/versioning.html)

### [Kubernetes versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)

Learn how Amazon EKS supports Kubernetes versions with standard and extended support periods, allowing you to proactively update clusters with the latest versions, features, and security patches.

- [Standard support versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions-standard.html): This topic gives important changes to be aware of for each Kubernetes version in standard support.
- [Extended support versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions-extended.html): This topic gives important changes to be aware of for each Kubernetes version in extended support.
- [View support period](https://docs.aws.amazon.com/eks/latest/userguide/view-support-status.html): The cluster support period section of the AWS console indicates if your cluster is currently on standard or extended support.
- [View upgrade policy](https://docs.aws.amazon.com/eks/latest/userguide/view-upgrade-policy.html): The cluster upgrade policy determines what happens to your cluster when it leaves the standard support period.
- [Enable extended support](https://docs.aws.amazon.com/eks/latest/userguide/enable-extended-support.html): This topic describes how to set the upgrade policy of an EKS cluster to enable extended support.
- [Disable extended support](https://docs.aws.amazon.com/eks/latest/userguide/disable-extended-support.html): This topic describes how to set the upgrade policy of an EKS cluster to disable extended support.
- [Platform versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html): Amazon EKS platform versions represent the capabilities of the Amazon EKS cluster control plane, such as which Kubernetes API server flags are enabled, as well as the current Kubernetes patch version.


## [Contribute](https://docs.aws.amazon.com/eks/latest/userguide/contribute.html)

- [Edit single page](https://docs.aws.amazon.com/eks/latest/userguide/edit-single-web.html): You can easily edit a single page in the EKS User Guide directly through your web browser.
- [Edit files with GitHub](https://docs.aws.amazon.com/eks/latest/userguide/edit-web.html): If you want to propose change to multiple pages, or create a new docs page, use the GitHub.dev web editor.
- [View style feedback](https://docs.aws.amazon.com/eks/latest/userguide/vale-local.html): You can see style feedback as you type.
- [Create page](https://docs.aws.amazon.com/eks/latest/userguide/create-page.html): This topic includes instructions for creating the initial page metadata and adding the page to the guide table of contents.
- [Insert link](https://docs.aws.amazon.com/eks/latest/userguide/insert-link.html): AsciiDoc supports multiple types of links.
- [Create with Amazon Q](https://docs.aws.amazon.com/eks/latest/userguide/create-content-q.html): You can use Amazon Q to create and revise docs content.
- [View PR preview](https://docs.aws.amazon.com/eks/latest/userguide/pr-preview.html): The Amazon EKS User Guide GitHub is configured to build and generate a preview of the docs site.
- [AsciiDoc syntax](https://docs.aws.amazon.com/eks/latest/userguide/asciidoc-syntax.html): This page provides a quick reference guide to AsciiDoc syntax for contributing to Amazon EKS documentation.
