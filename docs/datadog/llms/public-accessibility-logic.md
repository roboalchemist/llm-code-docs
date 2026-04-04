# Source: https://docs.datadoghq.com/security/cloud_security_management/guide/public-accessibility-logic.md

---
title: How Datadog Determines if Resources are Publicly Accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Guides > How Datadog
  Determines if Resources are Publicly Accessible
---

# How Datadog Determines if Resources are Publicly Accessible

Datadog uses a graph processing framework to map relationships between cloud resources to determine whether they are accessible from the internet. This guide outlines the logic used to classify resources as publicly accessible within the graph framework.

## Resource dependency graph{% #resource-dependency-graph %}

The following diagrams show how related resources are used to determine whether other resources are publicly accessible. For example, an AWS CloudTrail Trail stored in a public Amazon S3 bucket is itself publicly accessible. If a resource is publicly accessible because of another resource, the relationship is shown in the Cloud Security Misconfigurations resource relationships graph.

**Note**: Not all resources with the Publicly Accessible attribute are shown in these diagrams.

### AWS{% #aws %}

{% image
   source="https://datadog-docs.imgix.net/images/security/cloud_security_management/guide/public_accessibility_relationships_aws.8f7dac9ee35073a540170dcfc54d3c66.png?auto=format"
   alt="A graph diagram showing the relationships between resources that are used to determine public accessibility for AWS" /%}

### Azure{% #azure %}

{% image
   source="https://datadog-docs.imgix.net/images/security/cloud_security_management/guide/public_accessibility_relationships_azure.91c7252fe298257fa3931b5ea6c12ed1.png?auto=format"
   alt="A graph diagram showing the relationships between resources that are used to determine public accessibility for Azure" /%}

### Google Cloud{% #google-cloud %}

{% image
   source="https://datadog-docs.imgix.net/images/security/cloud_security_management/guide/public_accessibility_relationships_gcp.fa1ba2570cf205fe72cd594b93b13107.png?auto=format"
   alt="A graph diagram showing the relationships between resources that are used to determine public accessibility for Google Cloud" /%}

## AWS public accessibility logic by resource{% #aws-public-accessibility-logic-by-resource %}

For more information on AWS network reachability, see the [AWS documentation](https://docs.aws.amazon.com/) and the [AWS Network Reachability Analyser](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html).

### Amazon S3 bucket{% #amazon-s3-bucket %}

An [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#BasicsBucket) (`aws_s3_bucket`) is considered publicly accessible if:

- *Public by bucket policy:*

| **Criteria**                                                                                                                                                                            | **Explanation**                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The bucket policy allows the `s3:GetObject` permission unconditionally, with resource and principal set to `"*"`.                                                                       | This defines a public policy on the bucket, meaning that unauthenticated access is allowed. `"*"` is a wildcard, meaning access is given to any resource and principal. |
| None of the bucket's `public_access_block_configuration` and the AWS account's public access block (`aws_s3_account_public_access_block`) have `restrict_public_buckets` set to `true`. | None of the buckets or accounts explicitly block public access, meaning that the public bucket policy takes effect.                                                     |

***OR***

- *Public by Access Control List (ACL):*

| **Criteria**                                                                                                                                                                       | **Explanation**                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The bucket has ACL grants that allow insecure permissions to public grantees.                                                                                                      | The bucket's ACL grants one or more of the following permissions (`full_control`, `read`, `write`, `write_acp`) to either authenticated users (`http://acs.amazonaws.com/groups/global/authenticatedusers`) or all users (`http://acs.amazonaws.com/groups/global/allusers`). |
| None of the bucket's `public_access_block_configuration` and the AWS account's public access block (`aws_s3_account_public_access_block`) have `ignore_public_acls` set to `true`. | None of the buckets or accounts explicitly ignore public ACLs, meaning that the public ACL grants take effect.                                                                                                                                                                |

See [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) for more information.

### AWS CloudTrail trail{% #aws-cloudtrail-trail %}

A [CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-trails) (`aws_cloudtrail_trail`) is considered publicly accessible if:

| **Criteria**                                                                                | **Explanation**                                                                                                                                         |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The trail's `s3_bucket_name` is set to an S3 bucket that is considered publicly accessible. | CloudTrail Trails are log files that are delivered to S3 buckets. If the trail is stored in a public S3 bucket, then that trail is publicly accessible. |

### Amazon VPC subnet{% #amazon-vpc-subnet %}

A [subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-basics) (`aws_subnet`) is considered public if:

| **Criteria**                                                                                                                                                                                                                                                                                                                                             | **Explanation**                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| It's connected to one or more [route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#RouteTables) that are connected to an [Internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) and that route to a destination CIDR block of `"0.0.0.0/0"`, or an IPv6 CIDR block of `"::/0"`. | The route table attached to this subnet routes egress traffic through an internet gateway, meaning resources in the subnet can access the public internet.                                                                                                                                                                               |
| It's connected to one or more [network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) that have at least one ingress and at least one egress entry that have a CIDR block of `"0.0.0.0/0"`, or an IPv6 CIDR block of `"::/0"`.                                                                                            | Network ACLs control traffic that can leave or enter the subnet at the subnet level. When a network ACL rule allows ingress traffic from the Internet and allows egress traffic to ephemeral ports, it allows resources in the subnet to be exposed to the Internet if they are assigned a public IP and their security group allows it. |

See [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) for the AWS definition of a public subnet.

### Amazon Redshift cluster{% #amazon-redshift-cluster %}

A [Redshift cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#working-with-clusters-overview) (`aws_redshift_cluster`) is considered publicly accessible if:

| **Criteria**                                                                                                                                                                                                                                                                                                                                              | **Explanation**                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| If it has `publicly_accessible` set to `true` in its configuration.                                                                                                                                                                                                                                                                                       | See [Managing clusters in a VPC](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html).                                                                                                                        |
| It's in a public [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html).                                                                                                                                                                                                                                                         | A public VPC is a VPC with at least one public subnet, connected to one or more network ACLs that have at least one ingress and at least one egress entry that have a CIDR block of `"0.0.0.0/0"`, or an IPv6 CIDR block of `"::/0"`. |
| It's associated with a [security group](https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html) that has rules allowing access from a CIDR range of `"0.0.0.0/0"`, or an IPv6 CIDR range of `"::/0"`.                                                                                                                                      | A security group controls inbound traffic to a VPC. With an open CIDR range, all IP addresses are able to gain access.                                                                                                                |
| It's connected to one or more [route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#RouteTables) that are connected to an [Internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), and that route to a destination CIDR block of `"0.0.0.0/0"`, or an IPv6 CIDR block of `"::/0"`. | The route table attached to this subnet routes egress traffic through an Internet gateway, meaning resources in the subnet can access the public Internet.                                                                            |

See [Make a private Amazon Redshift Cluster publicly accessible](https://repost.aws/knowledge-center/redshift-cluster-private-public) for more information about Redshift Clusters and public accessibility.

### Amazon RDS DB instance{% #amazon-rds-db-instance %}

An [RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html) (`aws_rds_instance`) is considered publicly accessible if:

| **Criteria**                                                                                                                                                                                                         | **Explanation**                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| It has `publicly_accessible` set to `true` in its connectivity configuration.                                                                                                                                        | This setting makes the DB publicly accessible, meaning its DNS endpoint will resolve to the private IP address within its VPC, and a public IP address from outside the VPC. However, access to the cluster will still be controlled by a related security group. |
| It's in a public [subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-basics).                                                                                                    | -                                                                                                                                                                                                                                                                 |
| It's associated with a [security group](https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html) that has rules allowing access from a CIDR range of `"0.0.0.0/0"`, or an IPv6 CIDR range of `"::/0"`. | A security group controls inbound traffic to a VPC. With an open CIDR range, all IP addresses are able to gain access.                                                                                                                                            |

See [Fix connectivity to an RDS DB instance that uses a VPC's subnet](https://repost.aws/knowledge-center/rds-connectivity-instance-subnet-vpc) for more information about public access to an RDS DB Instance.

### Amazon RDS DB snapshot{% #amazon-rds-db-snapshot %}

An [RDS DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) (`aws_rds_db_snapshot`) is considered publicly accessible if:

| **Criteria**                                                                   | **Explanation**                                                                                                                                    |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| It has an attribute set to `"restore"` with an attribute value set to `"all"`. | If you set DB snapshot visibility to Public, all AWS accounts can restore a DB instance from your manual DB snapshot and have access to your data. |

See [Sharing a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html) for more information.

### Amazon Elastic Load Balancer{% #amazon-elastic-load-balancer %}

An ELB (`aws_elbv2_load_balancer`) is considered publicly accessible if:

| **Criteria**                                                                                                                                                                                                          | **Explanation**                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| The [scheme](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#load-balancer-scheme) is set to `internet-facing`.                                               | The scheme determines whether the load balancer is an internal load balancer or an Internet-facing load balancer.      |
| It is associated with a [security group](https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html) that has rules allowing access from a CIDR range of `"0.0.0.0/0"`, or an IPv6 CIDR range of `"::/0"`. | A security group controls inbound traffic to a VPC. With an open CIDR range, all IP addresses are able to gain access. |

See [Create an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html) for more information about Internet-facing load balancers.

### Amazon EC2 instance{% #amazon-ec2-instance %}

An [EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) (`aws_ec2_instance`) is considered publicly accessible if:

- *"Public subnet"-determined access:*

| **Criteria**                                                                                                                                                                                                         | **Explanation**                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| It has one or more [public IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses).                                                              | A public IP address allows your instance to be reached from the internet.                                              |
| It's in a public [subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-basics).                                                                                                    | -                                                                                                                      |
| It's associated with a [security group](https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html) that has rules allowing access from a CIDR range of `"0.0.0.0/0"`, or an IPv6 CIDR range of `"::/0"`. | A security group controls inbound traffic to a VPC. With an open CIDR range, all IP addresses are able to gain access. |

***OR***

- *ELB-determined access:*

| **Criteria**                                                                                                                                                                                                                                                             | **Explanation**                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A security group (for example, `SG1`) attached to the load balancer is publicly accessible and allows ingress traffic to some port `X`.                                                                                                                                  | This opens the load balancer to incoming traffic from the internet on a specific port.                                                                                                                                                  |
| The load balancer has a listener accepting traffic on port `X`.                                                                                                                                                                                                          | A [listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html) is a process that checks for connection requests using the protocol and port that you configure.                         |
| The load balancer has a target group forwarding traffic to some port `Y`.                                                                                                                                                                                                | [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html) route requests to one or more registered targets, such as EC2 instances, on a protocol and port that you specify. |
| The EC2 instance is listed as a target of the target group, and has a security group with at least one rule that allows ingress traffic on port `Y` from `0.0.0.0/0`, from the VPC CIDR (for example, `10.0.0.0/8`), or from the load balancer's security group (`SG1`). | Because the instance is registered as a target of the target group, the load balancer can forward traffic to it through port `Y`. The security group must allow traffic coming from the load balancer.                                  |

See [Authorize inbound traffic for your Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html) for more information about EC2 Instances and public access. See [Example: VPC with servers in private subnets and NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html) for an example of EC2 instances that are exposed through a load balancer.

### Amazon Elasticsearch Domain{% #amazon-elasticsearch-domain %}

An [Elasticsearch Domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html) (`aws_elasticsearch_domain`) is considered publicly accessible if:

| **Criteria**                                                                         | **Explanation**                                                                                                                                                                 |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| It has an endpoint that matches the regex pattern `^search-.*\.es\.amazonaws\.com$`. | This is the form taken by [endpoints](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html#vpc-architecture) for domains that are publicly accessible. |

See [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) for more information about making your Elasticsearch domain no longer publicly accessible.

### Amazon Machine Images (AMI){% #amazon-machine-images-ami %}

A [Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (`aws_ami`) is considered publicly accessible if:

| **Criteria**                                                                                                                     | **Explanation**                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| It is customer-owned, which means it does not have an aliased owner (either `amazon` or `aws-marketplace` in the account field). | Public AMIs owned by verified providers (either Amazon or verified partners) have an aliased owner, which appears as `amazon` or `aws-marketplace` in the account field. See [Find a shared AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/usingsharedamis-finding.html#usingsharedamis-finding-cli) in the AWS docs. |
| Its image is set to `public`, meaning that the launch permissions for the image are public.                                      | By modifying the `launchPermission` property of an AMI, you can make the AMI public (which grants launch permissions to all AWS accounts), or share it with only the AWS accounts that you specify.                                                                                                                             |

See [Make an AMI public](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-intro.html) for an explanation of how to make an AMI public or private.

### Amazon EBS snapshots{% #amazon-ebs-snapshots %}

An [EBS snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) (`aws_ebs_snapshot`) is considered publicly accessible if:

| **Criteria**                                | **Explanation**                                                                                                                                                                                            |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_volume_permission` is set to `all`. | Each snapshot contains all of the information that is needed to restore the snapshot's data to a new EBS volume. If anyone can create a volume from the snapshot, that information is publicly accessible. |

See [Share an Amazon EBS snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html) for information about public EBS snapshots and how to make them private.

### Amazon EKS clusters{% #amazon-eks-clusters %}

An [EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) (`aws_eks_cluster`) is considered publicly accessible if:

| **Criteria**                                                                     | **Explanation**                                                                                                                                                |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `endpoint_public_access` is set to `true` in the cluster's configuration.        | This setting makes the cluster publicly accessible when combined with an open public CIDR.                                                                     |
| The cluster's `public_access_cidrs` contains an open CIDR block (`"0.0.0.0/0"`). | You can limit the CIDR blocks that can access the public endpoint of the EKS cluster. An open CIDR block means anyone on the internet can access the endpoint. |

See [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) for more information on public EKS clusters.

### Amazon SQS queue{% #amazon-sqs-queue %}

An [SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) (`aws_sqs_queue`) is considered publicly accessible if:

| **Criteria**                                                                                                                                             | **Explanation**                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| The queue has a policy that allows any principal (principal set to `"*"`) to perform actions unconditionally (`statement_has_condition` set to `false`). | This setting makes the queue accessible to everyone in the world or to any authenticated AWS user. |

See [Amazon SQS security best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security-best-practices.html) for more information about public SQS queues.

### AWS Lambda function{% #aws-lambda-function %}

A [Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) (`aws_lambda_function`) is considered publicly accessible if:

| **Criteria**                                                                                              | **Explanation**                                                                                       |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| The function has a policy that allows any principal (`principal_policy` or `principal_aws`) set to `"*"`. | This setting makes the function accessible to everyone in the world or to any authenticated AWS user. |

See [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) for more information about public Lambda functions.

## Azure public accessibility logic by resource{% #azure-public-accessibility-logic-by-resource %}

### Azure Network Security Group (NSG){% #azure-network-security-group-nsg %}

An Azure NSG (`azure_security_group`) grants public access if:

| Criteria                                                                                                                                     | Explanation                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The security group has rules with protocol `tcp`, `udp` or `*`.                                                                              | These are the protocol values that are relevant for determining public access for Azure resources.                                                                                                  |
| The security group has `inbound` rules with access set to `Allow`.                                                                           | These values indicates that the rule is allowing inbound traffic.                                                                                                                                   |
| The security group has rules with source_address_prefix equal to `*`, `0.0.0.0`, `/0`, `::/0`, `internet`, or `any`.                         | These CIDR prefixes allow access to the internet.                                                                                                                                                   |
| The rules which match the above properties combine with any other `Deny` rules of higher priority to open at least one port to the Internet. | See [Security rules](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview#security-rules) to learn how Azure combines security group rules to calculate access. |

For details on how Azure NSGs allow and deny Internet access for a resource, see [Network Security Groups](https://azure.microsoft.com/en-us/blog/network-security-groups/).

### Azure Virtual Machine Instance{% #azure-virtual-machine-instance %}

A Virtual Machine Instance (`azure_virtual_machine_instance`) is considered publicly accessible if:

- *Attached to Network Security Group allowing public access:*

| Criteria                                                                                                                    | Explanation                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| The virtual machine instance has a public IP address attached to one of its network interfaces.                             | A public IP is required for Internet access to a virtual machine instance.                         |
| The virtual machine instance has a network security group granting public access attached to one of its network interfaces. | To learn more about how a network can grant public access, see Azure Network Security Group (NSG). |

***OR***

- *Has Public IP with SKU "Basic":*

| Criteria                                                                                               | Explanation                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The virtual machine instance has a public IP address with SKU Basic attached to its network interface. | A public IP address with SKU basic is open by default (see [Public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)). |
| The virtual machine instance has no attached network security groups.                                  | If no network security groups are attached, then there are no rules blocking access through the open public IP address.                                                     |

To learn more about Azure Virtual Machine Instances and public access, see [Associate a public IP address to a virtual machine](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/associate-public-ip-address-vm?tabs=azure-portal).

### Azure Storage blob container{% #azure-storage-blob-container %}

A Storage blob container (`azure_storage_blob_container`) is considered publicly accessible if:

| Criteria                                                                                                                      | Explanation                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The storage blob container's storage account has no `allow_blob_public_access` attribute, or has the attribute set to `true`. | This means that the account allows public Internet access to Azure Blob Storage. To learn more about configuring anonymous read access with Azure Storage Accounts, see [Configure anonymous read access for containers and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal). |
| The storage blob container's `public_access` attribute is set to `blob` or `container`.                                       | This means that the account allows public Internet access to Azure Blob Storage.                                                                                                                                                                                                                                                       |
| The storage blob container is part of a storage account that does not explicitly block public access.                         | When a Storage Account doesn't explicitly block public access, Storage Blob Containers inside it can be made public.                                                                                                                                                                                                                   |

To learn more about disallowing blob public access on Azure Storage accounts, see [Choose to allow or disallow blob public access on Azure Storage accounts](https://azure.microsoft.com/en-us/updates/choose-to-allow-or-disallow-blob-public-access-on-azure-storage-accounts/).

### Azure Kubernetes Service (AKS) cluster{% #azure-kubernetes-service-aks-cluster %}

An [AKS cluster](https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes) (`azure_aks_cluster`) is considered publicly accessible if:

| **Criteria**                                                                                  | **Explanation**                                                                            |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `enable_private_cluster` is set to `false` in the cluster's configuration.                    | This setting makes the cluster publicly accessible when combined with an open public CIDR. |
| The cluster's `authorized_ip_ranges` contains an open CIDR block (`"0.0.0.0/0"`) or is unset. | An open CIDR block means anyone on the internet can access the endpoint.                   |

See [AKS best practices](https://learn.microsoft.com/en-us/azure/aks/best-practices) for more information on public AKS clusters.

## Google Cloud Public accessibility logic by resource{% #google-cloud-public-accessibility-logic-by-resource %}

### Google Cloud Compute firewall{% #google-cloud-compute-firewall %}

A Compute Firewall (`gcp_compute_firewall`) grants public access if:

| Criteria                                                                                                                       | Explanation                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| The firewall has one or more rules whose protocol is TCP or all and which have `0.0.0.0/0` or `::/0` in their `source_ranges`. | These CIDR prefixes allow access from the Internet, and are the protocol values that are relevant for determining public access. |
| The firewall's direction is `ingress`.                                                                                         | This means that the firewall is relevant for inbound access from the Internet.                                                   |

For more information about using Compute firewalls, [Choose to allow or disallow blob public access on Azure Storage accounts](https://azure.microsoft.com/en-us/updates/choose-to-allow-or-disallow-blob-public-access-on-azure-storage-accounts/).

### Google Cloud Compute instance{% #google-cloud-compute-instance %}

A Compute instance (`gcp_compute_instance`) is considered publicly accessible if:

| Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Explanation                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The compute instance has a public IP address, meaning at least one of its network interfaces has a public IP address defined in its access configurations,                                                                                                                                                                                                                                                                                                                                                                                          | To learn more about adding an external IP to a compute instance, see [Reserve a static external IP address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address).     |
| The compute instance has associated firewall rules that combine to open some range of ports to the internet. The firewall rules can be associated with the instance by:


  - Having no `target_tags` or `target_service_accounts`, meaning the rule applies to the whole network.
  - Having `target_service_accounts` associated with one of the compute instance's `service_accounts`.
  - Having some `target_tags` that match the compute instance's network tags.


The rules should grant public access (see Google Cloud Compute Firewall). | To learn how compute firewall rules are used to restrict port ranges for a compute instance, see [Firewall rule components](https://cloud.google.com/firewall/docs/firewalls#firewall_rule_components). |

Learn more about how compute firewall rules are used to restrict port ranges for a compute instance [here](https://cloud.google.com/compute/docs/instances).

### Google Cloud BigQuery dataset{% #google-cloud-bigquery-dataset %}

A BigQuery dataset (`gcp_bigquery_dataset`) is considered publicly accessible if:

| Criteria                                                                                                                                                                                                                                                                                                    | Explanation                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The dataset has an IAM policy attached that has a `member` value of either `AllUsers` or `AllAuthenticatedUsers`.                                                                                                                                                                                           | These members allow anyone on the internet to access the database. See [IAM overview](https://cloud.google.com/iam/docs/overview) for more information.                                                                      |
| The dataset has an IAM policy attached that binds it to one of the following roles: `roles/viewer`, `roles/owner`, `roles/editor`, `roles/bigquery.admin`, `roles/bigquery.metadataviewer`, `roles/bigquery.dataowner`, `roles/bigquery.dataeditor`, `roles/bigquery.dataviewer`, or `roles/bigquery.user`. | These roles allow the person who accesses the resource to perform dangerous operations on the database. See the [role reference](https://cloud.google.com/iam/docs/understanding-roles#bigquery-roles) for more information. |

Learn more about [BigQuery datasets](https://cloud.google.com/bigquery?hl=en).

### Google Cloud Storage bucket{% #google-cloud-storage-bucket %}

A Storage Bucket (`gcp_storage_bucket`) is considered publicly accessible if:

| Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Explanation                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The bucket has an IAM policy attached that has a `member` value of either `AllUsers` or `AllAuthenticatedUsers`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | These members allow anyone on the Internet to access the database. See more [here](https://cloud.google.com/iam/docs/overview).                                                                                                 |
| The bucket has `public_access_prevention` set to `inherited` in its `iam_configuration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | This setting block public access if set to `enforced`. For more information about the public access prevention setting, see [Public access prevention](https://cloud.google.com/storage/docs/public-access-prevention).         |
| The bucket has an IAM policy attached that binds it to one of the following roles:
  - `roles/backupdr.cloudstorageoperator`
  - `roles/bigquerymigration.worker`
  - `roles/cloudbuild.builds.builder`
  - `roles/clouddeploy.jobrunner`
  - `roles/cloudmigration.storageaccess`
  - `roles/cloudtestservice.testadmin`
  - `roles/cloudtestservice.testviewer`
  - `roles/composer.environmentandstorageobjectadmin`
  - `roles/composer.environmentandstorageobjectuser`
  - `roles/composer.environmentandstorageobjectviewer`
  - `roles/composer.worker`
  - `roles/config.agent`
  - `roles/container.nodeserviceaccount`
  - `roles/dataflow.admin`
  - `roles/dataflow.worker`
  - `roles/dataplex.storagedataowner`
  - `roles/dataplex.storagedatareader`
  - `roles/dataproc.hubagent`
  - `roles/dataproc.worker`
  - `roles/firebase.admin`
  - `roles/firebase.developadmin`
  - `roles/firebase.developviewer`
  - `roles/firebase.viewer`
  - `roles/firebaserules.system`
  - `roles/managedidentities.domaincontrolleroperator`
  - `roles/storage.admin`
  - `roles/storage.legacyobjectowner`
  - `roles/storage.legacyobjectreader`
  - `roles/storage.objectadmin`
  - `roles/storage.objectuser`
  - `roles/storage.objectviewer` | These roles allow the person who accesses the resource to perform dangerous operations on the bucket. See the [role reference](https://cloud.google.com/iam/docs/understanding-roles#cloud-storage-roles) for more information. |

Explore more information about making storage buckets public [here](https://cloud.google.com/storage/docs/access-control/making-data-public).

### Google Cloud Kubernetes Engine clusters{% #google-cloud-kubernetes-engine-clusters %}

A Kubernetes Engine cluster (`gcp_kubernetes_engine_cluster`) is considered publicly accessible if it meets **all** of the following **base criteria** AND **at least one** of the additional conditions listed below:

**Base criteria (all required):**

| **Criteria**                 | **Explanation**                                                                                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Private endpoint is disabled | The cluster's [private endpoint](https://cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#private_cp) is not enabled (`enable_private_endpoint` is false), meaning the control plane has a public IP address. |
| Public endpoint is enabled   | The cluster has a public endpoint configured (`public_endpoint` is true).                                                                                                                                                            |

**AND at least one of the following conditions:**

- *Authorized networks is disabled:*

| **Criteria**                                                                                                                    | **Explanation**                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Authorized networks](https://cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#overview) is not enabled. | There are no IP allowlist restrictions on who can access the cluster's control plane, allowing access from any IP address. |

***OR***

- *Unrestricted CIDR block allowed:*

| **Criteria**                                                               | **Explanation**                                                    |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| The authorized networks configuration includes the `0.0.0.0/0` CIDR block. | This CIDR block allows access from any IP address on the internet. |

***OR***

- *Google Cloud external IP addresses added to authorized networks:*

| **Criteria**                                                                                                          | **Explanation**                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Google Cloud external IP addresses are added to authorized networks (`gcpPublicCidrsAccessEnabled` is set to `true`). | This allows access from any external IP address assigned to Google Cloud VMs, meaning anyone can create a VM in Google Cloud and access the cluster's control plane. |

***OR***

- *Broad Google Cloud IP range allowed:*

| **Criteria**                                                                | **Explanation**                                                                                                      |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| The authorized networks configuration includes the `34.0.0.0/7` CIDR block. | This CIDR range is sometimes used to allow access from Google Cloud IP ranges and is considered publicly accessible. |

**Note**: A cluster with authorized networks enabled (`{"enabled":true}`) but with an empty CIDR blocks list (`{"enabled":true, "cidr_blocks":[]}`) is **not** considered publicly accessible, as it blocks all external access to the control plane.

## Further Reading{% #further-reading %}

- [Start tracking misconfigurations with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/)
- [Out-of-the-box Detection Rules](https://docs.datadoghq.com/security/default_rules/#cat-cloud-security-management)
