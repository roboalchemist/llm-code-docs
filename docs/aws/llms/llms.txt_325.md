# Source: https://docs.aws.amazon.com/eks/latest/eksctl/llms.txt

# Eksctl User Guide Amazon EKS

> Eksctl User Guide

- [Tutorial](https://docs.aws.amazon.com/eks/latest/eksctl/tutorial.html)
- [Installation options for Eksctl](https://docs.aws.amazon.com/eks/latest/eksctl/installation.html)
- [Cluster Config Schema](https://docs.aws.amazon.com/eks/latest/eksctl/schema.html)
- [Troubleshooting](https://docs.aws.amazon.com/eks/latest/eksctl/troubleshooting.html)
- [Announcements](https://docs.aws.amazon.com/eks/latest/eksctl/announcements.html)

## [What is Eksctl?](https://docs.aws.amazon.com/eks/latest/eksctl/what-is-eksctl.html)

- [Eksctl FAQ](https://docs.aws.amazon.com/eks/latest/eksctl/faq.html)
- [Dry Run](https://docs.aws.amazon.com/eks/latest/eksctl/dry-run.html): The dry-run feature allows you to inspect and change the instances matched by the instance selector before proceeding to creating a nodegroup.


## [Clusters](https://docs.aws.amazon.com/eks/latest/eksctl/clusters.html)

- [Creating and managing clusters](https://docs.aws.amazon.com/eks/latest/eksctl/creating-and-managing-clusters.html): This topic covers how to create and delete EKS clusters using Eksctl.
- [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/eksctl/auto-mode.html): eksctl supports EKS Auto Mode, a feature that extends AWS management of Kubernetes clusters beyond the cluster itself, to allow AWS to also set up and manage the infrastructure that enables the smooth operation of your workloads.
- [EKS Access Entries](https://docs.aws.amazon.com/eks/latest/eksctl/access-entries.html): You can use eksctl to manage EKS Access Entries.
- [Non eksctl-created clusters](https://docs.aws.amazon.com/eks/latest/eksctl/unowned-clusters.html): You can run eksctl commands against clusters which were not created by eksctl.
- [EKS Connector](https://docs.aws.amazon.com/eks/latest/eksctl/eks-connector.html): You can use the EKS Connector to view clusters outside of AWS in the EKS Console.
- [Configure kubelet](https://docs.aws.amazon.com/eks/latest/eksctl/customizing-the-kubelet.html): System resources can be reserved through the configuration of the kubelet.
- [CloudWatch logging](https://docs.aws.amazon.com/eks/latest/eksctl/cloudwatch-cluster-logging.html): This topic explains how to configure Amazon CloudWatch logging for your EKS clusterâs control plane components.
- [EKS Fully-Private Cluster](https://docs.aws.amazon.com/eks/latest/eksctl/eks-private-cluster.html): eksctl supports creation of fully-private clusters that have no outbound internet access and have only private subnets.
- [Addons](https://docs.aws.amazon.com/eks/latest/eksctl/addons.html): This topic describes how to manage Amazon EKS Add-Ons for your Amazon EKS clusters using eksctl.
- [Amazon EMR](https://docs.aws.amazon.com/eks/latest/eksctl/emr-access.html): In order to allow EMR to perform operations on the Kubernetes API, its SLR needs to be granted the required RBAC permissions. eksctl provides a command that creates the required RBAC resources for EMR, and updates the aws-auth ConfigMap to bind the role with the SLR for EMR.
- [EKS Fargate Support](https://docs.aws.amazon.com/eks/latest/eksctl/fargate.html): AWS Fargate is a managed compute engine for Amazon ECS that can run containers.
- [Cluster upgrades](https://docs.aws.amazon.com/eks/latest/eksctl/cluster-upgrade.html): An `eksctl`-managed cluster can be upgraded in 3 easy steps:
- [Default add-on updates](https://docs.aws.amazon.com/eks/latest/eksctl/addon-upgrade.html): This topic explains how to update the default pre-installed add-ons that are included on EKS clusters.
- [Enable Zonal Shift](https://docs.aws.amazon.com/eks/latest/eksctl/zonal-shift.html): EKS now supports Amazon Application Recovery Controller (ARC) zonal shift and zonal autoshift that enhances the resiliency of multi-AZ cluster environments.
- [Karpenter Support](https://docs.aws.amazon.com/eks/latest/eksctl/eksctl-karpenter.html): eksctl provides support for adding Karpenter to a newly created cluster.


## [Nodegroups](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroups.html)

- [Work with node groups](https://docs.aws.amazon.com/eks/latest/eksctl/general-nodegroups.html)
- [Unmanaged nodegroups](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-unmanaged.html): In eksctl, setting --managed=false or using the nodeGroups field creates an unmanaged nodegroup.
- [EKS managed nodegroups](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-managed.html): Amazon EKS managed nodegroups is a feature that automates the provisioning and lifecycle management of nodes (EC2 instances) for Amazon EKS Kubernetes clusters.
- [Node bootstrapping](https://docs.aws.amazon.com/eks/latest/eksctl/node-bootstrapping.html)
- [Launch template support](https://docs.aws.amazon.com/eks/latest/eksctl/launch-template-support.html): eksctl supports launching managed nodegroups using a provided EC2 Launch Template.
- [Custom subnets](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-with-custom-subnet.html): Itâs possible to extend an existing VPC with a new subnet and add a Nodegroup to that subnet.
- [Custom DNS](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-customize-dns.html): There are two ways of overwriting the DNS server IP address used for all the internal and external DNS lookups.
- [Taints](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-taints.html): To apply taints to a specific nodegroup use the taints config section like this:
- [Instance Selector](https://docs.aws.amazon.com/eks/latest/eksctl/instance-selector.html): eksctl supports specifying multiple instance types for managed and self-managed nodegroups, but with over 270 EC2 instance types, users have to spend time figuring out which instance types would be well suited for their nodegroup.
- [Spot instances](https://docs.aws.amazon.com/eks/latest/eksctl/spot-instances.html)
- [GPU Support](https://docs.aws.amazon.com/eks/latest/eksctl/gpu-support.html): Eksctl supports selecting GPU instance types for nodegroups.
- [ARM Support](https://docs.aws.amazon.com/eks/latest/eksctl/arm-support.html): This topic covers how to create a cluster with an ARM node group, and how to add an ARM node group to an existing cluster.
- [Auto Scaling](https://docs.aws.amazon.com/eks/latest/eksctl/autoscaling.html)
- [Custom AMI support](https://docs.aws.amazon.com/eks/latest/eksctl/custom-ami-support.html)
- [Windows Worker Nodes](https://docs.aws.amazon.com/eks/latest/eksctl/windows-worker-nodes.html): From version 1.14, Amazon EKS supports Windows Nodes that allow running Windows containers.
- [Additional Volume Mappings](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-additional-volume-mappings.html): As an additional configuration option, when dealing with volume mappings, itâs possible to configure extra mappings when the nodegroup is created.
- [EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/eksctl/hybrid-nodes.html)
- [Node Repair Config](https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-node-repair-config.html): EKS Managed Nodegroups supports Node Repair, where the health of managed nodes are monitored, and unhealthy worker nodes are replaced or rebooted in response. eksctl now provides comprehensive configuration options for fine-grained control over node repair behavior.


## [Networking](https://docs.aws.amazon.com/eks/latest/eksctl/networking.html)

- [VPC Configuration](https://docs.aws.amazon.com/eks/latest/eksctl/vpc-configuration.html)
- [Subnet Settings](https://docs.aws.amazon.com/eks/latest/eksctl/vpc-subnet-settings.html)
- [Cluster Access](https://docs.aws.amazon.com/eks/latest/eksctl/vpc-cluster-access.html)
- [Control plane networking](https://docs.aws.amazon.com/eks/latest/eksctl/cluster-subnets-security-groups.html): This documentation explains how to modify the networking configuration of your EKS clusterâs control plane after initial creation.
- [IPv6 Support](https://docs.aws.amazon.com/eks/latest/eksctl/vpc-ip-family.html)


## [IAM](https://docs.aws.amazon.com/eks/latest/eksctl/iam.html)

- [Minimum IAM policies](https://docs.aws.amazon.com/eks/latest/eksctl/minimum-iam-policies.html): This document describes the minimum IAM policies needed to run the main use cases of eksctl.
- [IAM permissions boundary](https://docs.aws.amazon.com/eks/latest/eksctl/iam-permissions-boundary.html): A permissions boundary is an advanced AWS IAM feature in which the maximum permissions that an identity-based policy can grant to an IAM entity have been set; where those entities are either users or roles.
- [IAM policies](https://docs.aws.amazon.com/eks/latest/eksctl/iam-policies.html): You can attach Instance Roles to node groups.
- [Manage IAM users and roles](https://docs.aws.amazon.com/eks/latest/eksctl/iam-identity-mappings.html)
- [IAM Roles for Service Accounts](https://docs.aws.amazon.com/eks/latest/eksctl/iamserviceaccounts.html)
- [EKS Pod Identity Associations](https://docs.aws.amazon.com/eks/latest/eksctl/pod-identity-associations.html): Amazon EKS has introduced a new enhanced mechanism called Pod Identity Association for cluster administrators to configure Kubernetes applications to receive IAM permissions required to connect with AWS services outside of the cluster.


## [Deployment options](https://docs.aws.amazon.com/eks/latest/eksctl/deployment.html)

- [EKS Anywhere](https://docs.aws.amazon.com/eks/latest/eksctl/eksctl-anywhere.html): eksctl provides access to AWS' feature called EKS Anywhere with the sub command eksctl anywhere.
- [AWS Outposts Support](https://docs.aws.amazon.com/eks/latest/eksctl/outposts.html)


## [Security](https://docs.aws.amazon.com/eks/latest/eksctl/security.html)

- [KMS Encryption](https://docs.aws.amazon.com/eks/latest/eksctl/kms-encryption.html)
