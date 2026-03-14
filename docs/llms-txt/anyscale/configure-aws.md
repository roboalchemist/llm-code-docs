# Source: https://docs.anyscale.com/admin/cloud/configure-aws.md

# Configure AWS resources for an Anyscale cloud

[View Markdown](/admin/cloud/configure-aws.md)

# Configure AWS resources for an Anyscale cloud

Before you run Ray workloads on Anyscale, an [organization](/administration/organization.md) owner must configure AWS resources for an Anyscale cloud. This integration enables Anyscale to manage resources like compute instances and storage directly in an AWS account.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1. Register a user on Anyscale at [`console.anyscale.com`](https://console.anyscale.com) and set up the Anyscale CLI locally.
2. Verify your ability to launch EC2 instances in the AWS region you plan to use on Anyscale. Anyscale supports all commercially available regions. Anyscale doesn't support regions outside the `aws` partition, meaning China regions and GovCloud regions.
3. Set up AWS credentials locally by running `aws configure`. For more details, see [the AWS configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
4. Set up AWS credentials to correspond to the AWS account that you're using for the Anyscale cloud. They should have permissions to manage all required resources. Ensure that you have [minimal IAM permissions](#minimal-iam) for cloud operations.

note

The following resources have low default quota:

* Number of VPCs per region
* Number of internet gateways per region

Anyscale requires one of these resources per cloud. If you've reached your quota, see **[how you can raise it](https://aws.amazon.com/getting-started/hands-on/request-service-quota-increase/)**.

## 1. Install the Anyscale CLI[​](#1-install-the-anyscale-cli "Direct link to 1. Install the Anyscale CLI")

1. Run the following command to install the Anyscale CLI and Python client package:

```
pip install -U anyscale
```

2. To authenticate your credentials, run the following command, which fetches and updates the token that confirms your identity in the `~/.anyscale/credentials.json` file.

```
anyscale login
```

If necessary, log in to the Anyscale console to complete authentication.

## 2. Choose a resource configuration method[​](#methods "Direct link to 2. Choose a resource configuration method")

Configuring AWS resources for an Anyscale cloud integrates Anyscale's capabilities into your AWS account to leverage its compute, storage, and networking resources for scalable, distributed computing.

You can use one of two different configuration methods that use the Anyscale CLI. Choose a method based on your organization's requirements:

* `anyscale cloud setup` - Use for rapid configuration and a straightforward, low-maintenance solution; deploy in public subnets and access over public IP addresses without setting up additional networking infrastructure.
* `anyscale cloud register` - Suitable for teams with advanced cloud expertise, seeking enhanced security, custom private networking, and specific compliance needs.

## 3. Configure cloud resources[​](#configure-resources "Direct link to 3. Configure cloud resources")

Based on the configuration method selected from the previous step, configure AWS resources for your Anyscale cloud with the following instructions.

* anyscale cloud setup (auto)
* anyscale cloud register (custom)

For the `anyscale cloud setup` method, Anyscale automatically creates and configures the necessary resources within your AWS account. You deploy Ray clusters in public subnets and access them using public IP addresses without needing to set up additional networking infrastructure like VPNs.

Note: To manually customize resources, use the (Custom) cloud register method instead.

An Anyscale cloud configured using `anyscale cloud setup` uses direct networking with an architecture similar to the following:

![Direct Networking](/assets/images/aws-direct-a114eb353fa632e975bf8fd34e346c2d.png)

**Configure a new cloud**

Run the following command to configure AWS resources for a new cloud:

```
anyscale cloud setup \
--name example_cloud_name \
--provider aws \
--region ap-southeast-1 \
--enable-head-node-fault-tolerance
```

🏁Optional flags

`--enable-head-node-fault-tolerance`: Enables [head node fault tolerance](/administration/resource-management/head-node-fault-tolerance.md) in Anyscale Services by configuring an additional MemoryDB instance for the Ray Global Control Store. Note that this flag extends the setup time by approximately 20 minutes.

note

By default, Anyscale doesn't set any retention policy for the S3 bucket created by managed cloud setup. If you have any preference or concern, you can set one on your own.

For the `anyscale cloud register` method, you are responsible for creating and configuring AWS resources needed to integrate with Anyscale. You define subnets to deploy Ray clusters and access them using public or private IP addresses.

This custom-defined networking requires you to configure the network paths between users, clusters, and the Anyscale control plane. Connectivity and network performance between users and clusters depends on your setup.

An Anyscale cloud configured using customer-defined networking has a similar architecture to the following:

![Customer defined networking](/assets/images/aws-customer-defined-8aa89173503e86a25a0f47d3b58363fb.png)

Notes:

* You should configure Anyscale clouds with multiple availability zones. By default, the `anyscale cloud setup` option creates a subnet in each availability zone.
* The Elastic Container Registry (ECR) is displayed to show a possible integration with ECR to support custom Docker environments. See [Use container images from an external registry](/container-image/image-registry.md).

### Step 1: Choose method for creating cloud resources[​](#create-method "Direct link to Step 1: Choose method for creating cloud resources")

You have three methods for creating custom AWS infrastructure resources to connect to Anyscale:

#### (Recommended) Anyscale provided Terraform module[​](#recommended-anyscale-provided-terraform-module "Direct link to (Recommended) Anyscale provided Terraform module")

Use this predefined set of configurations developed by Anyscale, which simplifies the setup process. Applying this module to your cloud environment configures the required resources in your AWS account. For details and instructions on using this module, see the following resources:

* [Terraform Modules for Anyscale Cloud Foundations on AWS](https://github.com/anyscale/terraform-aws-anyscale-cloudfoundation-modules)
* [Terraform Registry](https://registry.terraform.io/modules/anyscale/anyscale-cloudfoundation-modules/aws/latest)

#### Create your own Terraform module[​](#create-your-own-terraform-module "Direct link to Create your own Terraform module")

You can create custom Terraform modules to tailor cloud resources and configurations to meet compliance requirements.

#### Create resources manually in the AWS Management Console[​](#create-resources-manually-in-the-aws-management-console "Direct link to Create resources manually in the AWS Management Console")

You can manually create resources in the AWS Management Console, which offers maximum customization but can be prone to manual errors.

### Step 2: Create cloud resources[​](#create-resources "Direct link to Step 2: Create cloud resources")

Cloud resources created in an AWS account must meet a list of minimum requirements to work with Anyscale.

note

Elastic File System (EFS) is optional for all Anyscale clouds on AWS and not created by default.

Existing cloud configurations might include EFS. When EFS is present, Anyscale uses it for shared storage locations by default. In clouds without EFS, Anyscale uses the default S3 bucket you configure during cloud setup for these shared storage locations. See [Shared storage on Anyscale](/storage/shared.md).

Following the [Terraform Modules for Anyscale Cloud Foundations on AWS](https://github.com/anyscale/terraform-aws-anyscale-cloudfoundation-modules) satisfies these requirements by default. For all other methods, perform the following steps:

**VPC**

* Anyscale recommends a CIDR range of `/19` or more.
* The VPC has internet egress ability.
* *Strongly recommended*: Enable a Gateway VPC Endpoint for S3 to reduce cost and improve performance when interacting with S3 (for example, pulling container images or loading datasets).

**Subnets**

* Anyscale recommends a CIDR range of `/22` or more.
* The subnet is public with an internet gateway and route table, or the subnet is private when the `--private-network` flag is set in cloud registry for customer-defined resources.
* Must provide >= 2 subnets.
* No two public subnets should be in the same availability zone.

**Security group**

Inbound rules

* Allow all inbound TCP traffic on port 443 (can be restricted to your CIDR blocks) for inbound access to submit Ray jobs, the Grafana dashboard, web-based workspaces, workspace connections using VS Code Desktop, and other functionality.

* Allow all inbound traffic from the given security group to allow intra-cluster communication and access to Elastic File System (EFS) for workspaces.

  ![Inbound rules](/assets/images/inbound-rules-92ca94c989a4dc21e48dea53f2e991ac.png)

Outbound rules

* Allow all outbound traffic for reporting back to users and the Anyscale control plane.
* Allow the outbound traffic for all protocols from the given security group to allow intra-cluster communication. This is required by certain network devices such as [**EFA**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-security).

**IAM Role for cross account access**

`anyscale-iam-role-id`

Create an IAM role with the following permissions to allow Anyscale to manage resources in your account:

* Grant access to our control plane:![Anyscale IAM role](/assets/images/anyscale-iam-role-9445779a70268aa83b4b356102417e1b.png)

* Or manually set the trust relationship as follows:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "sts:AssumeRole",
              "Principal": {
                  "AWS": "525325868955"
              },
              "Condition": {}
          }
      ]
  }
  ```

  note

  The user running `anyscale cloud register` must have permission to edit this trust relationship. The `register` command updates the trust relationship to include a cloud-specific [**External ID**](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) in the Condition field.

* Attach the following IAM policy to this role for standard cluster operation:

  ```
  [
      {
          "Sid": "IAM",
          "Effect": "Allow",
          "Action": [
              "iam:PassRole",
              "iam:GetInstanceProfile"
          ],
          "Resource": "*"
      },
      {
          "Sid": "RetrieveGenericAWSResources",
          "Effect": "Allow",
          "Action": [
              "ec2:DescribeAvailabilityZones",
              "ec2:DescribeInstanceTypes",
              "ec2:DescribeRegions",
              "ec2:DescribeAccountAttributes"
          ],
          "Resource": "*"
      },
      {
          "Sid": "DescribeRunningResources",
          "Effect": "Allow",
          "Action": [
              "ec2:DescribeInstances",
              "ec2:DescribeSubnets",
              "ec2:DescribeRouteTables",
              "ec2:DescribeSecurityGroups"
          ],
          "Resource": "*"
      },
      {
          "Sid": "InstanceTagManagement",
          "Effect": "Allow",
          "Action": [
              "ec2:CreateTags",
              "ec2:DeleteTags"
          ],
          "Resource": "*"
      },
      {
          "Sid": "InstanceStart",
          "Effect": "Allow",
          "Action": [
              "ec2:StartInstances",
              "ec2:RunInstances"
          ],
          "Resource": "*"
      },
      {
          "Sid": "InstanceStop",
          "Effect": "Allow",
          "Action": [
              "ec2:TerminateInstances",
              "ec2:StopInstances"
          ],
          "Resource": "*"
      },
      {
          "Sid": "InstanceManagementSpot",
          "Effect": "Allow",
          "Action": [
              "ec2:CancelSpotInstanceRequests",
              "ec2:ModifyImageAttribute",
              "ec2:ModifyInstanceAttribute",
              "ec2:RequestSpotInstances"
          ],
          "Resource": "*"
      },
      {
          "Sid": "ResourceManagementExtended",
          "Effect": "Allow",
          "Action": [
              "ec2:AttachVolume",
              "ec2:CreateVolume",
              "ec2:DescribeVolumes",
              "ec2:AssociateIamInstanceProfile",
              "ec2:DisassociateIamInstanceProfile",
              "ec2:ReplaceIamInstanceProfileAssociation",
              "ec2:CreatePlacementGroup",
              "ec2:AllocateAddress",
              "ec2:ReleaseAddress",
              "ec2:DescribeIamInstanceProfileAssociations",
              "ec2:DescribeInstanceStatus",
              "ec2:DescribePlacementGroups",
              "ec2:DescribePrefixLists",
              "ec2:DescribeReservedInstancesOfferings",
              "ec2:DescribeSpotInstanceRequests",
              "ec2:DescribeSpotPriceHistory"
          ],
          "Resource": "*"
      },
      {
          "Sid": "EFSManagement",
          "Effect": "Allow",
          "Action": [
              "elasticfilesystem:DescribeMountTargets"
          ],
          "Resource": "*"
      },
      {
          "Sid": "CreateSpotServiceLinkedRole",
          "Effect": "Allow",
          "Action": ["iam:CreateServiceLinkedRole", "iam:PutRolePolicy"],
          "Resource": "arn:aws:iam::*:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot",
          "Condition": {"StringLike": {"iam:AWSServiceName": "spot.amazonaws.com"}}
      }
  ]
  ```

* To use Services, attach the following additional policies:

  ```
  [
      {
          "Sid": "CFN",
          "Effect": "Allow",
          "Action": [
              "cloudformation:TagResource",
              "cloudformation:UntagResource",
              "cloudformation:CreateStack",
              "cloudformation:UpdateStack",
              "cloudformation:DeleteStack",
              "cloudformation:DescribeStackEvents",
              "cloudformation:DescribeStackResources",
              "cloudformation:DescribeStacks",
              "cloudformation:GetTemplate"
          ],
          "Resource": "*"
      },
      {
          "Sid": "ELBDescribe",
          "Effect": "Allow",
          "Action": [
              "elasticloadbalancing:DescribeListeners",
              "elasticloadbalancing:DescribeLoadBalancers",
              "elasticloadbalancing:DescribeLoadBalancerAttributes",
              "elasticloadbalancing:DescribeRules",
              "elasticloadbalancing:DescribeTargetGroups",
              "elasticloadbalancing:DescribeTargetGroupAttributes",
              "elasticloadbalancing:DescribeTargetHealth",
              "elasticloadbalancing:DescribeListenerCertificates",
              "elasticloadbalancing:DescribeTags"
          ],
          "Resource": "*"
      },
      {
          "Sid": "EC2Describe",
          "Action": [
              "ec2:DescribeVpcs",
              "ec2:DescribeInternetGateways"
          ],
          "Effect": "Allow",
          "Resource": "*"
      },
      {
          "Sid": "ELBCerts",
          "Effect": "Allow",
          "Action": [
              "elasticloadbalancing:AddListenerCertificates",
              "elasticloadbalancing:RemoveListenerCertificates"
          ],
          "Resource": "*"
      },
      {
          "Sid": "ACMList",
          "Effect": "Allow",
          "Action": [
              "acm:ListCertificates"
          ],
          "Resource": "*"
      },
      {
          "Sid": "ACM",
          "Effect": "Allow",
          "Action": [
              "acm:DeleteCertificate",
              "acm:RenewCertificate",
              "acm:RequestCertificate",
              "acm:AddTagsToCertificate",
              "acm:DescribeCertificate",
              "acm:GetCertificate",
              "acm:ListTagsForCertificate"
          ],
          "Resource": "*"
      },
      {
          "Sid": "ELBWrite",
          "Effect": "Allow",
          "Action": [
              "elasticloadbalancing:AddTags",
              "elasticloadbalancing:RemoveTags",
              "elasticloadbalancing:CreateRule",
              "elasticloadbalancing:ModifyRule",
              "elasticloadbalancing:DeleteRule",
              "elasticloadbalancing:SetRulePriorities",
              "elasticloadbalancing:CreateListener",
              "elasticloadbalancing:ModifyListener",
              "elasticloadbalancing:DeleteListener",
              "elasticloadbalancing:CreateLoadBalancer",
              "elasticloadbalancing:DeleteLoadBalancer",
              "elasticloadbalancing:ModifyLoadBalancerAttributes",
              "elasticloadbalancing:CreateTargetGroup",
              "elasticloadbalancing:ModifyTargetGroup",
              "elasticloadbalancing:DeleteTargetGroup",
              "elasticloadbalancing:ModifyTargetGroupAttributes",
              "elasticloadbalancing:RegisterTargets",
              "elasticloadbalancing:DeregisterTargets",
              "elasticloadbalancing:SetIpAddressType",
              "elasticloadbalancing:SetSecurityGroups",
              "elasticloadbalancing:SetSubnets"
          ],
          "Resource": "*"
      },
      {
          "Sid": "LinkELBService",
          "Effect": "Allow",
          "Action": "iam:CreateServiceLinkedRole",
          "Resource": "*",
          "Condition": {
              "StringLike": {
                  "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
              }
          }
      },
      {
          "Sid": "IAMPolicies",
          "Effect": "Allow",
          "Action": [
              "iam:AttachRolePolicy",
              "iam:PutRolePolicy",
              "iam:UpdateRoleDescription",
              "iam:DeleteServiceLinkedRole",
              "iam:GetServiceLinkedRoleDeletionStatus"
          ],
          "Resource": "arn:aws:iam::*:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing"
      }
  ]
  ```

* If required, limit permissions by constraining actions to resources with the `anyscale-cloud-id` tag. Use the following policies by replacing `cld_ID` with your own cloud id (create a cloud first if you don't have one) and removing the `InstanceStop` and `InstanceStart` statements from the control plane policy:

  ```
  [
      {
          "Sid": "DenyTaggingOnOtherInstances",
          "Effect": "Deny",
          "Action": [
              "ec2:DeleteTags",
              "ec2:CreateTags"
          ],
          "Resource": "arn:aws:ec2:*:*:instance/*",
          "Condition": {
              "StringNotEquals": {
                  "aws:ResourceTag/anyscale-cloud-id": "cld_ID",
                  "ec2:CreateAction": [
                      "RunInstances",
                      "StartInstances"
                  ]
              }
          }
      },
      {
          "Sid": "RestrictedInstanceStop",
          "Effect": "Allow",
          "Action": [
              "ec2:TerminateInstances",
              "ec2:StopInstances"
          ],
          "Resource": "*",
          "Condition": {
              "StringEquals": {
                  "aws:ResourceTag/anyscale-cloud-id": "cld_ID"
              }
          }
      },
      {
          "Sid": "RestrictedInstanceStart",
          "Effect": "Allow",
          "Action": [
              "ec2:StartInstances",
              "ec2:RunInstances"
          ],
          "Resource": "*",
          "Condition": {
              "StringEquals": {
                  "aws:RequestTag/anyscale-cloud-id": "cld_ID"
              },
              "ForAnyValue:StringEquals": {
                  "aws:TagKeys": [
                      "anyscale-cloud-id"
                  ]
              }
          }
      },
      {
          "Sid": "AllowRunInstancesForUntaggedResources",
          "Effect": "Allow",
          "Action": "ec2:RunInstances",
          "Resource": [
              "arn:aws:ec2:*::image/*",
              "arn:aws:ec2:*::snapshot/*",
              "arn:aws:ec2:*:*:subnet/*",
              "arn:aws:ec2:*:*:network-interface/*",
              "arn:aws:ec2:*:*:security-group/*",
              "arn:aws:ec2:*:*:key-pair/*",
              "arn:aws:ec2:*:*:volume/*"
          ]
      }
  ]
  ```

**IAM Role or instance profile for cluster nodes**

`instance-iam-role-id`

* Create an IAM role for EC2 that clusters will run with. Attach the following permissions to this role: AmazonS3FullAccess or provide a custom S3 policy that permits R/W access for your application's needs:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "ListObjectsInBucket",
              "Effect": "Allow",
              "Action": ["s3:ListBucket"],
              "Resource": ["arn:aws:s3:::bucket-name"]
          },
          {
              "Sid": "AllObjectActions",
              "Effect": "Allow",
              "Action": "s3:*Object",
              "Resource": ["arn:aws:s3:::bucket-name/*"]
          }
      ]
  }
  ```

* Ensure this role can be assumed by EC2.

* Create an Instance Profile with the same name as the role.

note

Replace `bucket-name` in the policy with your actual S3 bucket name. If you wish to use the instance IAM role to work with other AWS services, additional permissions may be needed. Example common services that would need additional permissions:

* [Secret Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html)
* [RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html)
* [KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html)

**S3 bucket for persisting artifacts**

* Create an S3 bucket with a globally unique name.
* The bucket must be accessible by the instance IAM role or instance profile created above, and the control plane IAM role created above.
* You might need to update the S3 bucket policy to grant access to the control plane IAM role and/or instance IAM role.
* Anyscale-created clusters always have access to this bucket.

**EFS (Optional)**

* File system:
  <!-- -->
  * Create an EFS file system. Ensure the file system policy allows access from the security group created above.
* Mount targets:
  <!-- -->
  * Create at least one mount target for the file system in the same subnets configured for the cloud.

**MemoryDB (Optional - for head node fault tolerance)**

To enable [head node fault tolerance](/administration/resource-management/head-node-fault-tolerance.md), create a MemoryDB cluster with the following configuration:

* TLS must be enabled.
* Each shard should have at least 1 replica (2 nodes total) for high availability.
* The cluster should be accessible from the security group created above.

### Step 3: Register the Anyscale cloud[​](#register-cloud "Direct link to Step 3: Register the Anyscale cloud")

After setting up the necessary resources, use the following command to register your Anyscale cloud on AWS:

```
anyscale cloud register \
--private-network \ # for Customer defined networking
--provider aws \
--name example_cloud_name \
--vpc-id vpc-00000000000000000 \
--subnet-ids subnet-00000000000000000,subnet-00000000000000000,subnet-0000000000000000 \
--file-storage-id fs-00000000000000000 \ # Optional EFS ID
--anyscale-iam-role-id arn:aws:iam::000000000000:role/anyscale-iam-role-00000000 \
--instance-iam-role-id arn:aws:iam::000000000000:role/cluster_node_role-00000000 \
--security-group-ids sg-00000000000000000 \
--cloud-storage-bucket-name anyscale-production-data-cld-00000000000000000 \
--region us-west-2 \
--functional-verify workspace \ # to launch a workspace after the cloud is created
--memorydb-cluster-id memorydb-name # Optional for fault tolerance
```

🏁Optional flags

`--memorydb-cluster-id`: Enables [head node fault tolerance](/administration/resource-management/head-node-fault-tolerance.md) in Anyscale services. See MemoryDB in the [resource requirements](#create-resources) for configuration requirements.

`--private-network`: Enables private networking on private subnets and IP addresses.

`--functional-verify workspace`: Launches a test workspace to verify validity of resources.

`--functional-verify service`: Launches a test service to verify validity of resources.

### Steps to register a cloud with Terraform[​](#steps-to-register-a-cloud-with-terraform "Direct link to Steps to register a cloud with Terraform")

1. Customize your expected cloud environment by providing necessary values for parameters of the Terraform module.
2. Apply Terraform module to your cloud environment.
3. Run the `cloud register` command that the Terraform module returns. Note: Export your Anyscale and cloud credentials before running this command.
4. Rerun the Terraform module, using `cloud_id` returned from `cloud register` as an argument. This approach scopes down permissions to only resources with that specific `cloud_id` tag.

note

If you encounter any issue during the cloud registration step, validate the AWS resources created as noted above. You can revalidate the cloud configuration by running `anyscale cloud verify` to [verify your configuration](#verify).

## 4. Verify cloud resources[​](#verify "Direct link to 4. Verify cloud resources")

Anyscale provides a CLI command to verify cloud resources for both configuration methods. Anyscale runs verification automatically during cloud creation and you can also run the verification on demand.

Trigger functional verification by specifying `--functional-verify workspace` or `--functional-verify service`. Anyscale launches a workspace or a service to verify that the cloud is functional. You can also trigger both verifications (`--functional-verify workspace,service`).

```
anyscale cloud verify --name my-cloud-deployment
```

The following output displays:

```
Authenticating
Loaded Anyscale authentication token from ANYSCALE_CLI_TOKEN.

Output
(anyscale +0.4s) Verifying VPC ...
(anyscale +0.8s) VPC vpc-1234 verification succeeded.
(anyscale +0.8s) Verifying subnets ...
(anyscale +1.2s) Subnets ['subnet-1234', 'subnet-2345', 'subnet-3456', 'subnet-4567'] verification succeeded.
(anyscale +1.2s) Verifying IAM roles ...
(anyscale +2.8s) IAM roles ['arn:aws:iam::999999999999:role/anyscale-iam-role-1234', 'arn:aws:iam::999999999999:role/cld_1234-cluster_node_role'] verification succeeded.
(anyscale +2.8s) Verifying security groups ...
(anyscale +3.0s) Security group ['sg-1234'] verification succeeded.
(anyscale +3.0s) Verifying S3 ...
(anyscale +3.1s) S3 anyscale-production-data-cld-1234 verification succeeded.
(anyscale +3.1s) Verifying EFS ...
(anyscale +3.3s) S3 fs-1234 verification succeeded.
(anyscale +3.3s) Start functional verification...
Functional verification for WORKSPACE is about to begin.
It will spin up one m5.xlarge instance for each function and will incur a small amount of cost.
For workspace verification, it takes about 5 minutes.
The instances will be terminated after verification. Do you want to continue? [y/N]: y
╭──────────────────────────────────────────── workspace verification ────────────────────────────────────────────╮
│ 0:00:02 Workspace created at https://console.anyscale.com/workspaces/expwrk_abc/ses_abc                        │
│ 0:01:22 Workspace is active.                                                                                   │
│ 0:00:00 Workspace termination initiated.                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
0:01:24 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Workspace verification succeeded!
```

## Manage cloud resources[​](#manage "Direct link to Manage cloud resources")

### Update an existing cloud[​](#update-an-existing-cloud "Direct link to Update an existing cloud")

If you configured your cloud using `anyscale cloud setup`, you can update certain cloud features:

```
anyscale cloud update --name <cloud-name> --enable-head-node-fault-tolerance
```

### Delete cloud resources[​](#delete-cloud-resources "Direct link to Delete cloud resources")

To delete an Anyscale cloud and optionally its associated AWS resources:

```
anyscale cloud delete --name <cloud-name>
```

caution

For clouds created with `anyscale cloud setup`, this command deletes all AWS resources created by Anyscale, including:

* VPC and subnets
* Security groups
* IAM roles
* S3 buckets (and all data within them)
* EFS file systems
* MemoryDB clusters

For clouds registered with `anyscale cloud register`, this command only removes the cloud from Anyscale but doesn't delete any AWS resources. You must manually delete AWS resources or use your Terraform scripts.

## IAM permissions reference[​](#iam-permissions "Direct link to IAM permissions reference")

### Minimal IAM permissions for cloud operations[​](#minimal-iam "Direct link to Minimal IAM permissions for cloud operations")

The following sections describe the minimal IAM permissions required for different Anyscale CLI commands:

Required IAM permissions for `anyscale cloud setup`

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudformationManagement",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateChangeSet",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStacks",
                "cloudformation:ListStacks"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EC2Management",
            "Effect": "Allow",
            "Action": [
                "ec2:AssociateRouteTable",
                "ec2:AttachInternetGateway",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateInternetGateway",
                "ec2:CreateRoute",
                "ec2:CreateRouteTable",
                "ec2:CreateSecurityGroup",
                "ec2:CreateSubnet",
                "ec2:CreateTags",
                "ec2:CreateVpc",
                "ec2:CreateVpcEndpoint",
                "ec2:DeleteInternetGateway",
                "ec2:DeleteRoute",
                "ec2:DeleteRouteTable",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteSubnet",
                "ec2:DeleteVpc",
                "ec2:DeleteVpcEndpoints",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeRegions",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroupRules",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcAttribute",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcs",
                "ec2:DetachInternetGateway",
                "ec2:DisassociateRouteTable",
                "ec2:ModifySubnetAttribute",
                "ec2:ModifyVpcAttribute",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RevokeSecurityGroupIngress"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EFSManagement",
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:CreateFileSystem",
                "elasticfilesystem:CreateMountTarget",
                "elasticfilesystem:DeleteFileSystem",
                "elasticfilesystem:DeleteMountTarget",
                "elasticfilesystem:DescribeBackupPolicy",
                "elasticfilesystem:DescribeFileSystemPolicy",
                "elasticfilesystem:DescribeFileSystems",
                "elasticfilesystem:DescribeLifecycleConfiguration",
                "elasticfilesystem:DescribeMountTargetSecurityGroups",
                "elasticfilesystem:DescribeMountTargets",
                "elasticfilesystem:DescribeReplicationConfigurations",
                "elasticfilesystem:PutLifecycleConfiguration",
                "elasticfilesystem:TagResource"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "IAMManagement",
            "Effect": "Allow",
            "Action": [
                "iam:AddRoleToInstanceProfile",
                "iam:AttachRolePolicy",
                "iam:CreateInstanceProfile",
                "iam:CreateRole",
                "iam:DeleteInstanceProfile",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:GetInstanceProfile",
                "iam:GetRole",
                "iam:PassRole",
                "iam:PutRolePolicy",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:TagRole"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "S3Management",
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucketPolicy",
                "s3:GetAccelerateConfiguration",
                "s3:GetBucketCors",
                "s3:GetBucketLogging",
                "s3:GetBucketNotification",
                "s3:GetBucketObjectLockConfiguration",
                "s3:GetBucketOwnershipControls",
                "s3:GetBucketPolicy",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketTagging",
                "s3:GetBucketVersioning",
                "s3:GetBucketWebsite",
                "s3:PutBucketCors",
                "s3:PutBucketPolicy",
                "s3:PutBucketPublicAccessBlock",
                "s3:PutBucketTagging"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "Miscellaneous",
            "Effect": "Allow",
            "Action": [
                "acm:ListCertificates",
                "kms:CreateGrant",
                "kms:DescribeKey",
                "kms:GenerateDataKeyWithoutPlaintext",
                "servicequotas:GetServiceQuota"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Required IAM permissions for `anyscale cloud register`

note

When running `anyscale cloud register`, you will need both the register and verify IAM policies.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudformationManagement",
            "Effect": "Allow",
            "Action": [
                "cloudformation:DescribeStacks",
                "cloudformation:ListStacks"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EC2Management",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EFSManagement",
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:DescribeBackupPolicy",
                "elasticfilesystem:DescribeFileSystemPolicy",
                "elasticfilesystem:DescribeFileSystems",
                "elasticfilesystem:DescribeMountTargets"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "IAMManagement",
            "Effect": "Allow",
            "Action": [
                "acm:ListCertificates",
                "iam:GetPolicy",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListInstanceProfilesForRole",
                "iam:ListRolePolicies",
                "iam:UpdateAssumeRolePolicy"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "S3Management",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketCors",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy",
                "s3:ListBucket",
                "s3:ListAllMyBuckets"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "Miscellaneous",
            "Effect": "Allow",
            "Action": [
                "servicequotas:GetServiceQuota"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Required IAM permissions for `anyscale cloud verify`

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudformationManagement",
            "Effect": "Allow",
            "Action": [
                "cloudformation:DescribeStacks"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EC2Management",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EFSManagement",
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:DescribeBackupPolicy",
                "elasticfilesystem:DescribeFileSystemPolicy",
                "elasticfilesystem:DescribeFileSystems",
                "elasticfilesystem:DescribeMountTargets"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "IAMManagement",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:GetRolePolicy",
                "iam:GetPolicy",
                "iam:ListInstanceProfilesForRole"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "S3Management",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketCors",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy",
                "s3:ListBucket",
                "s3:ListAllMyBuckets"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "Miscellaneous",
            "Effect": "Allow",
            "Action": [
                "servicequotas:GetServiceQuota"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

### Control plane IAM permissions[​](#control-plane-iam-permissions "Direct link to Control plane IAM permissions")

The control plane IAM role requires extensive permissions to manage cloud resources on your behalf. The full policy includes permissions for:

* EC2 instance management (launch, terminate, modify)
* IAM role management for cluster nodes
* S3 access for artifacts and logs
* EFS access for shared storage
* Security group management
* Optional: MemoryDB for fault tolerance
* Optional: Services permissions for load balancers

View full control plane IAM policy

```
[
    {
        "Sid": "IAM",
        "Effect": "Allow",
        "Action": [
            "iam:PassRole",
            "iam:GetInstanceProfile"
        ],
        "Resource": "*"
    },
    {
        "Sid": "RetrieveGenericAWSResources",
        "Effect": "Allow",
        "Action": [
            "ec2:DescribeAvailabilityZones",
            "ec2:DescribeInstanceTypes",
            "ec2:DescribeRegions",
            "ec2:DescribeAccountAttributes"
        ],
        "Resource": "*"
    },
    {
        "Sid": "DescribeRunningResources",
        "Effect": "Allow",
        "Action": [
            "ec2:DescribeInstances",
            "ec2:DescribeSubnets",
            "ec2:DescribeRouteTables",
            "ec2:DescribeSecurityGroups"
        ],
        "Resource": "*"
    },
    {
        "Sid": "InstanceTagManagement",
        "Effect": "Allow",
        "Action": [
            "ec2:CreateTags",
            "ec2:DeleteTags"
        ],
        "Resource": "*"
    },
    {
        "Sid": "InstanceStart",
        "Effect": "Allow",
        "Action": [
            "ec2:StartInstances",
            "ec2:RunInstances"
        ],
        "Resource": "*"
    },
    {
        "Sid": "InstanceStop",
        "Effect": "Allow",
        "Action": [
            "ec2:TerminateInstances",
            "ec2:StopInstances"
        ],
        "Resource": "*"
    },
    {
        "Sid": "InstanceManagementSpot",
        "Effect": "Allow",
        "Action": [
            "ec2:CancelSpotInstanceRequests",
            "ec2:ModifyImageAttribute",
            "ec2:ModifyInstanceAttribute",
            "ec2:RequestSpotInstances"
        ],
        "Resource": "*"
    },
    {
        "Sid": "ResourceManagementExtended",
        "Effect": "Allow",
        "Action": [
            "ec2:AttachVolume",
            "ec2:CreateVolume",
            "ec2:DescribeVolumes",
            "ec2:AssociateIamInstanceProfile",
            "ec2:DisassociateIamInstanceProfile",
            "ec2:ReplaceIamInstanceProfileAssociation",
            "ec2:CreatePlacementGroup",
            "ec2:AllocateAddress",
            "ec2:ReleaseAddress",
            "ec2:DescribeIamInstanceProfileAssociations",
            "ec2:DescribeInstanceStatus",
            "ec2:DescribePlacementGroups",
            "ec2:DescribePrefixLists",
            "ec2:DescribeReservedInstancesOfferings",
            "ec2:DescribeSpotInstanceRequests",
            "ec2:DescribeSpotPriceHistory"
        ],
        "Resource": "*"
    },
    {
        "Sid": "EFSManagement",
        "Effect": "Allow",
        "Action": [
            "elasticfilesystem:DescribeMountTargets"
        ],
        "Resource": "*"
    },
    {
        "Sid": "CreateSpotServiceLinkedRole",
        "Effect": "Allow",
        "Action": ["iam:CreateServiceLinkedRole", "iam:PutRolePolicy"],
        "Resource": "arn:aws:iam::*:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot",
        "Condition": {"StringLike": {"iam:AWSServiceName": "spot.amazonaws.com"}}
    }
]
```

For services support, also attach:

```
[
    {
        "Sid": "CFN",
        "Effect": "Allow",
        "Action": [
            "cloudformation:TagResource",
            "cloudformation:UntagResource",
            "cloudformation:CreateStack",
            "cloudformation:UpdateStack",
            "cloudformation:DeleteStack",
            "cloudformation:DescribeStackEvents",
            "cloudformation:DescribeStackResources",
            "cloudformation:DescribeStacks",
            "cloudformation:GetTemplate"
        ],
        "Resource": "*"
    },
    {
        "Sid": "ELBDescribe",
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:DescribeListeners",
            "elasticloadbalancing:DescribeLoadBalancers",
            "elasticloadbalancing:DescribeLoadBalancerAttributes",
            "elasticloadbalancing:DescribeRules",
            "elasticloadbalancing:DescribeTargetGroups",
            "elasticloadbalancing:DescribeTargetGroupAttributes",
            "elasticloadbalancing:DescribeTargetHealth",
            "elasticloadbalancing:DescribeListenerCertificates",
            "elasticloadbalancing:DescribeTags"
        ],
        "Resource": "*"
    },
    {
        "Sid": "EC2Describe",
        "Action": [
            "ec2:DescribeVpcs",
            "ec2:DescribeInternetGateways"
        ],
        "Effect": "Allow",
        "Resource": "*"
    },
    {
        "Sid": "ELBCerts",
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:AddListenerCertificates",
            "elasticloadbalancing:RemoveListenerCertificates"
        ],
        "Resource": "*"
    },
    {
        "Sid": "ACMList",
        "Effect": "Allow",
        "Action": [
            "acm:ListCertificates"
        ],
        "Resource": "*"
    },
    {
        "Sid": "ACM",
        "Effect": "Allow",
        "Action": [
            "acm:DeleteCertificate",
            "acm:RenewCertificate",
            "acm:RequestCertificate",
            "acm:AddTagsToCertificate",
            "acm:DescribeCertificate",
            "acm:GetCertificate",
            "acm:ListTagsForCertificate"
        ],
        "Resource": "*"
    },
    {
        "Sid": "ELBWrite",
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:AddTags",
            "elasticloadbalancing:RemoveTags",
            "elasticloadbalancing:CreateRule",
            "elasticloadbalancing:ModifyRule",
            "elasticloadbalancing:DeleteRule",
            "elasticloadbalancing:SetRulePriorities",
            "elasticloadbalancing:CreateListener",
            "elasticloadbalancing:ModifyListener",
            "elasticloadbalancing:DeleteListener",
            "elasticloadbalancing:CreateLoadBalancer",
            "elasticloadbalancing:DeleteLoadBalancer",
            "elasticloadbalancing:ModifyLoadBalancerAttributes",
            "elasticloadbalancing:CreateTargetGroup",
            "elasticloadbalancing:ModifyTargetGroup",
            "elasticloadbalancing:DeleteTargetGroup",
            "elasticloadbalancing:ModifyTargetGroupAttributes",
            "elasticloadbalancing:RegisterTargets",
            "elasticloadbalancing:DeregisterTargets",
            "elasticloadbalancing:SetIpAddressType",
            "elasticloadbalancing:SetSecurityGroups",
            "elasticloadbalancing:SetSubnets"
        ],
        "Resource": "*"
    },
    {
        "Sid": "LinkELBService",
        "Effect": "Allow",
        "Action": "iam:CreateServiceLinkedRole",
        "Resource": "*",
        "Condition": {
            "StringLike": {
                "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
            }
        }
    },
    {
        "Sid": "IAMPolicies",
        "Effect": "Allow",
        "Action": [
            "iam:AttachRolePolicy",
            "iam:PutRolePolicy",
            "iam:UpdateRoleDescription",
            "iam:DeleteServiceLinkedRole",
            "iam:GetServiceLinkedRoleDeletionStatus"
        ],
        "Resource": "arn:aws:iam::*:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing"
    }
]
```

See also the [Anyscale Terraform modules for AWS](https://github.com/anyscale/terraform-aws-anyscale-cloudfoundation-modules/blob/main/modules/aws-anyscale-iam/main.tf) for infrastructure-as-code examples.

## Glossary of cloud resources[​](#glossary "Direct link to Glossary of cloud resources")

| Resource                              | Description                                                                                                                                                                                                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VPC & Subnets**                     | A VPC is a virtual network within your AWS account that's logically isolated from other virtual networks. A subnet is a range of IP addresses in your VPC to which AWS resources (such as EC2 instances) can be attached. Anyscale deploys workloads in your account within the VPC and subnets defined as part of setup. |
| **Security group**                    | Security groups help secure the cloud environment by controlling the traffic that's allowed to reach and leave AWS-hosted resources. Anyscale creates a security group with network rules to enable access to Anyscale's suite of components and applications.                                                            |
| **S3 bucket**                         | Amazon S3 provides object storage to store cluster logs, workspace snapshots, Ray checkpoints, and other artifacts. Anyscale-created clusters always have access to this bucket.                                                                                                                                          |
| **Cross account IAM role**            | An IAM role that enables the Anyscale control plane to configure and deploy infrastructure for your Ray clusters in your AWS account.                                                                                                                                                                                     |
| **Cluster IAM role/Instance profile** | The IAM role assumed by EC2 instances in your Ray clusters, granting them access to AWS resources from your Ray applications.                                                                                                                                                                                             |
| **EFS (Optional)**                    | Amazon Elastic File System provides scalable file storage for use with EC2 instances. When present, Anyscale uses EFS for shared storage between cluster nodes.                                                                                                                                                           |
| **MemoryDB (Optional)**               | Amazon MemoryDB for Redis provides a Redis-compatible in-memory database service used for head node fault tolerance in Anyscale services.                                                                                                                                                                                 |

## Next steps[​](#next-steps "Direct link to Next steps")

* [Configure IAM mapping](/iam/cloud-iam-mapping.md) to set different permissions for different users or projects
* [Access S3 buckets](/storage/s3.md) from your Ray applications
* [Use custom container images](/container-image.md) for your workloads
* [Deploy your first workspace](/platform/workspaces.md) to start developing
