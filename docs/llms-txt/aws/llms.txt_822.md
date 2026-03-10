# Source: https://docs.aws.amazon.com/tnb/latest/ug/llms.txt

# AWS Telco Network Builder User Guide

> AWS Telco Network Builder is a network automation service that helps you deploy and manage telecom networks.

- [What is AWS TNB?](https://docs.aws.amazon.com/tnb/latest/ug/what-is-tnb.html)
- [How AWS TNB works](https://docs.aws.amazon.com/tnb/latest/ug/how-tnb-works.html)
- [AWS TNB concepts](https://docs.aws.amazon.com/tnb/latest/ug/tnb-concepts.html)
- [Setting up AWS TNB](https://docs.aws.amazon.com/tnb/latest/ug/setting-up.html)
- [Getting started with AWS TNB](https://docs.aws.amazon.com/tnb/latest/ug/getting-started.html)
- [Quotas](https://docs.aws.amazon.com/tnb/latest/ug/quotas.html)
- [Document history](https://docs.aws.amazon.com/tnb/latest/ug/doc-history.html)

## [Function packages](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html)

- [Create](https://docs.aws.amazon.com/tnb/latest/ug/create-function-package.html): Learn how to create a function package in the AWS TNB network functions catalog.
- [View](https://docs.aws.amazon.com/tnb/latest/ug/view-function-package.html): Learn how to view the content of a function package.
- [Download a package](https://docs.aws.amazon.com/tnb/latest/ug/download-function-package.html): Learn how to download a function package from the AWS TNB network functions catalog.
- [Delete a package](https://docs.aws.amazon.com/tnb/latest/ug/delete-function-package.html): Learn how to delete a function package from the AWS TNB network functions catalog.


## [AWS TNB network packages](https://docs.aws.amazon.com/tnb/latest/ug/network-packages.html)

- [Create](https://docs.aws.amazon.com/tnb/latest/ug/create-network-package.html): Learn how to create a network package in the AWS TNB network service catalog.
- [View](https://docs.aws.amazon.com/tnb/latest/ug/view-network-package.html): Learn how to view the content of a network package.
- [Download](https://docs.aws.amazon.com/tnb/latest/ug/download-network-package.html): Learn how to download a network package from the AWS TNB network service catalog.
- [Delete](https://docs.aws.amazon.com/tnb/latest/ug/delete-network-package.html): Learn how to delete a network package from the AWS TNB network service catalog.


## [Network](https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html)

- [Life cycle operations](https://docs.aws.amazon.com/tnb/latest/ug/network-life-cycle.html): Understand the life cycle of a network instance.
- [Create](https://docs.aws.amazon.com/tnb/latest/ug/create-network-instance.html): Learn how to create a network instance.
- [Instantiate](https://docs.aws.amazon.com/tnb/latest/ug/instantiate-network-instance.html): Learn how to instantiate a network instance.
- [Update a function instance](https://docs.aws.amazon.com/tnb/latest/ug/update-function-instance.html): Learn how to update a function instance in a network instance.
- [Update a network instance](https://docs.aws.amazon.com/tnb/latest/ug/update-network-instance.html): Learn how to update a network instance.
- [View](https://docs.aws.amazon.com/tnb/latest/ug/view-network-instance.html): Learn how to view a network instance.
- [Terminate and delete](https://docs.aws.amazon.com/tnb/latest/ug/terminate-network-instance.html): Learn how to terminate and delete a network instance.


## [Network operations](https://docs.aws.amazon.com/tnb/latest/ug/network-operations.html)

- [View](https://docs.aws.amazon.com/tnb/latest/ug/view-network-operation.html): Learn how to view a network operation.
- [Cancel](https://docs.aws.amazon.com/tnb/latest/ug/cancel-network-operation.html): Learn how to cancel a network operation.


## [TOSCA reference](https://docs.aws.amazon.com/tnb/latest/ug/tosca-reference.html)

### [VNFD template](https://docs.aws.amazon.com/tnb/latest/ug/vnfd-template.html)

Learn the syntax for the virtual network function descriptor (VNFD).

- [AWS.VNF](https://docs.aws.amazon.com/tnb/latest/ug/node-vnf.html): Learn the syntax for the AWS virtual network function (VNF) node.
- [AWS.Artifacts.Helm](https://docs.aws.amazon.com/tnb/latest/ug/node-helm.html): Learn the syntax for the AWS helm node.

### [NSD template](https://docs.aws.amazon.com/tnb/latest/ug/nsd-template.html)

Learn the syntax to define the network service descriptor (NSD).

- [AWS.NS](https://docs.aws.amazon.com/tnb/latest/ug/node-ns.html): Learn the syntax to define the AWS network service (NS) node.
- [AWS.Compute.EKS](https://docs.aws.amazon.com/tnb/latest/ug/node-eks.html): Learn the syntax to define the AWS cluster and Kubernetes version and permissions.
- [AWS.Compute.EKS.AuthRole](https://docs.aws.amazon.com/tnb/latest/ug/node-eks-authrole.html): Learn the syntax to define the Amazon EKS compute AuthRole.
- [AWS.Compute.EKSManagedNode](https://docs.aws.amazon.com/tnb/latest/ug/node-eks-managed-node.html): Learn the syntax to define the Amazon EKS managed node.
- [AWS.Compute.EKSSelfManagedNode](https://docs.aws.amazon.com/tnb/latest/ug/node-eks-self-managed.html): Learn the syntax to define the Amazon EKS self-managed node.
- [AWS.Compute.PlacementGroup](https://docs.aws.amazon.com/tnb/latest/ug/node-compute-placement-group.html): Learn the syntax to define the AWS compute placement group node.
- [AWS.Compute.UserData](https://docs.aws.amazon.com/tnb/latest/ug/node-compute-user-data.html): Learn the syntax to define the AWS compute user data node.
- [AWS.Networking.SecurityGroup](https://docs.aws.amazon.com/tnb/latest/ug/node-networking-security-group.html): Learn the syntax to define the AWS networking security group node.
- [AWS.Networking.SecurityGroupEgressRule](https://docs.aws.amazon.com/tnb/latest/ug/node-networking-security-group-egress-rule.html): Learn the syntax to define the AWS networking security group egress rules.
- [AWS.Networking.SecurityGroupIngressRule](https://docs.aws.amazon.com/tnb/latest/ug/node-networking-security-group-ingress-rule.html): Learn the syntax to define the AWS networking security group ingress rules.
- [AWS.Resource.Import](https://docs.aws.amazon.com/tnb/latest/ug/node-resource-import.html): Learn the syntax to define how to import AWS resources into AWS TNB
- [AWS.Networking.ENI](https://docs.aws.amazon.com/tnb/latest/ug/node-eni.html): Learn the syntax to define the networking node.
- [AWS.HookExecution](https://docs.aws.amazon.com/tnb/latest/ug/node-hook-execution.html): Learn the syntax to define the lifecycle hook.
- [AWS.Networking.InternetGateway](https://docs.aws.amazon.com/tnb/latest/ug/node-internet-gateway.html): Learn the syntax to define the internet gateway node.
- [AWS.Networking.RouteTable](https://docs.aws.amazon.com/tnb/latest/ug/node-route-table.html): Learn the syntax to define the networking route table.
- [AWS.Networking.Subnet](https://docs.aws.amazon.com/tnb/latest/ug/node-subnet.html): Learn the syntax to specify details of the networking subnet.
- [AWS.Deployment.VNFDeployment](https://docs.aws.amazon.com/tnb/latest/ug/node-vnf-deployment.html): Learn the syntax to specify the network functions for your deployment.
- [AWS.Networking.VPC](https://docs.aws.amazon.com/tnb/latest/ug/node-vpc.html): Learn the syntax to specify the CIDR block for your VPC.
- [AWS.Networking.NATGateway](https://docs.aws.amazon.com/tnb/latest/ug/node-nat-gateway.html): Learn the syntax to define the NAT Gateway node.
- [AWS.Networking.Route](https://docs.aws.amazon.com/tnb/latest/ug/node-route.html): Learn the syntax to define the route node.
- [AWS.Store.SSMParameters](https://docs.aws.amazon.com/tnb/latest/ug/node-ssm.html): Learn the syntax to define the SSM parameters.

### [Common nodes](https://docs.aws.amazon.com/tnb/latest/ug/common-nodes.html)

Learn the syntax to define common node.

- [AWS.HookDefinition.Bash](https://docs.aws.amazon.com/tnb/latest/ug/node-hook-bash.html): Learn the syntax to define an AWS HookDefinition in bash.


## [Security](https://docs.aws.amazon.com/tnb/latest/ug/security.html)

- [Data protection](https://docs.aws.amazon.com/tnb/latest/ug/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS TNB.

### [Identity and access management](https://docs.aws.amazon.com/tnb/latest/ug/security-iam.html)

How to authenticate requests and manage access to your AWS TNB resources.

- [How AWS TNB works with IAM](https://docs.aws.amazon.com/tnb/latest/ug/security_iam_service-with-iam.html): Learn about the IAM features that you can use with AWS TNB.
- [Identity-based policy examples](https://docs.aws.amazon.com/tnb/latest/ug/security_iam_id-based-policy-examples.html): Learn how to use identity-based policies to grant users and roles access to AWS TNB.
- [Troubleshooting](https://docs.aws.amazon.com/tnb/latest/ug/security_iam_troubleshoot.html): Troubleshoot common issues with IAM in AWS TNB.
- [Compliance validation](https://docs.aws.amazon.com/tnb/latest/ug/compliance-validation.html): Learn about the security and compliance of AWS TNB.
- [Resilience](https://docs.aws.amazon.com/tnb/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS TNB features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/tnb/latest/ug/infrastructure-security.html): Learn how AWS Telco Network Builder isolates service traffic.
- [IMDS version](https://docs.aws.amazon.com/tnb/latest/ug/imds-version.html): AWS Telco Network Builder supported IMDS version.


## [Monitoring](https://docs.aws.amazon.com/tnb/latest/ug/monitoring-tnb.html)

- [CloudTrail logs](https://docs.aws.amazon.com/tnb/latest/ug/logging-using-cloudtrail.html): Capture detailed information about the calls made to AWS TNB using AWS CloudTrail.
- [Deployment tasks](https://docs.aws.amazon.com/tnb/latest/ug/deployment-tasks.html): Learn about the AWS TNB deployment tasks.
