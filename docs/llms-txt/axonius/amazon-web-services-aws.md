# Source: https://docs.axonius.com/docs/amazon-web-services-aws.md

# Amazon Web Services (AWS)

Amazon Web Services (AWS) adapter includes a broad set of global cloud-based products. It supports EC2, ECS, EKS, IAM, EBS, ELB, RDS, S3, VPC, Workspaces, Lambda, Route 53 and more.

## About AWS

Amazon Web Services is one of the most comprehensive and broadly adopted public cloud platforms, allowing users to easily deploy virtual machines and networks, as well as access over 200 native AWS services.

**Use cases the adapter solves**
Connecting AWS to Axonius gives you the ability to quickly and accurately catalog key resources within your AWS public cloud across your entire AWS Organization. AWS data within Axonius can be used to review resource/region usage, analyze access policies for users or other AWS principals, and evaluate the configuration of different resources to ensure they adhere to industry best practices.

## Types of Assets Fetched

This adapter fetches the following types of assets and AWS services:

<Table>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        Fetched AWS Services
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Accounts
      </td>

      <td>
        Organizations (Accounts)
      </td>
    </tr>

    <tr>
      <td>
        Alerts/Incidents
      </td>

      <td>
        Cloud Watch Alarm, Guard Duty
      </td>
    </tr>

    <tr>
      <td>
        Application Services
      </td>

      <td>
        Elastic Cache Replication Groups, Sagemaker, SNS
      </td>
    </tr>

    <tr>
      <td>
        Certificates
      </td>

      <td>
        Amazon Certificate Manager (ACM)
      </td>
    </tr>

    <tr>
      <td>
        Compute Images
      </td>

      <td>
        AWS Snapshot
      </td>
    </tr>

    <tr>
      <td>
        Compute Services
      </td>

      <td>
        ASG, Athena, Elastic Kubernetes Service (EKS), ECR, Outposts
      </td>
    </tr>

    <tr>
      <td>
        Configurations
      </td>

      <td>
        AWS Systems Manager (SSM) Parameters
      </td>
    </tr>

    <tr>
      <td>
        Containers
      </td>

      <td>
        ECS
      </td>
    </tr>

    <tr>
      <td>
        Databases
      </td>

      <td>
        Relational Database Service (RDS), Redshift, DynamoDB
      </td>
    </tr>

    <tr>
      <td>
        Devices
      </td>

      <td>
        Elastic Container Service (ECS), Elastic Cloud Compute (EC2), ELB, Kinesis Analytics, Kinesis Data Stream, Light Sail, SSM

        * The following services are fetched as Legacy Devices: API Gateways, App Stream, Athena, Backup Plan, Cloud Front, ECR, Elastic Cache Cluster, Elastic Search, FSX, Global Accelerator, Glue, Internet Gateway, Lambda, NAT, Organizations (Accounts), RDS, Redshift, Elastic Cache Replication Groups, Route53, RouteTable, S3, Sagemaker, SecretManager, SNS, SQS, Transit Gateway, VPC, VPN, Workspaces
      </td>
    </tr>

    <tr>
      <td>
        Disks
      </td>

      <td>
        Volumes, Orphan EBS Volumes
      </td>
    </tr>

    <tr>
      <td>
        Groups
      </td>

      <td>
        Group, IdentityStore Group
      </td>
    </tr>

    <tr>
      <td>
        File Systems
      </td>

      <td>
        EFS, FSX
      </td>
    </tr>

    <tr>
      <td>
        Network/Firewall Rules
      </td>

      <td>
        SecurityGroup, WAF devices
      </td>
    </tr>

    <tr>
      <td>
        Load Balancers
      </td>

      <td>
        ELB
      </td>
    </tr>

    <tr>
      <td>
        Networks
      </td>

      <td>
        VPC
      </td>
    </tr>

    <tr>
      <td>
        Network Services
      </td>

      <td>
        Cloud Front, Direct Connect, Global Accelerator, Internet Gateway, NAT, Route53, RouteTable, Transit Gateway, VPN
      </td>
    </tr>

    <tr>
      <td>
        Object Storage
      </td>

      <td>
        Simple Storage Service (S3)
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        Role
      </td>
    </tr>

    <tr>
      <td>
        Secrets
      </td>

      <td>
        SecretManager
      </td>
    </tr>

    <tr>
      <td>
        Serverless Functions
      </td>

      <td>
        Lambda, StepFunctions
      </td>
    </tr>

    <tr>
      <td>
        Users
      </td>

      <td>
        App Stream User, Groups (Legacy User), IAM Root User, Identity Store User, Policy, Role (Legacy User), Regular IAM user
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  Note

  The AWS adapter also fetches Inspector and Security Hub and uses them as data enrichment sources for other services fetched as assets, for example: enriching vulnerability data for EC2, ECR, Lambda, and other services.
</Callout>

### Related Enforcement Actions

Axonius has several useful enforcement actions for AWS to assist with managing EC2 instance power states, tagging, and also installed software via SSM.

* [AWS - Start/Stop EC2 Instances](/docs/startstop-ec2-instances)
* [AWS - Add Tags to Resource](/docs/add-tag-to-amazon-resource)
* [AWS - Delete or Suspend IAM Users](/docs/aws-delete-or-suspend-iam-users)
* [AWS - Remove Tags from Resource](/docs/remove-tag-from-amazon-resource)
* [AWS - Install Software Using SSM](/docs/install-software-using-aws-ssm)
* [AWS - Patch Software Using SSM](/docs/patch-software-using-aws-ssm)
* [AWS - Assign Group to Users](https://docs.axonius.com/axonius-help-docs/docs/assign-aws-group-to-user)

<br />

This section contains the following topics:

* [Connecting the AWS Adapter Using CloudFormation/Organizations](/docs/connecting-the-aws-adapter-using-cf-organizations) -  How to configure Axonius if you're using the AWS Organizations service to manage your AWS accounts.
* [Parameters](/docs/aws-parameters) - The general parameters to configure to work with the Amazon Web Service (AWS) adapter.
* [Advanced Settings](/docs/aws-advanced-settings) - Explanation of all Advanced Configuration Settings for the AWS adapter.
* [Advanced Configuration File](/docs/aws-advanced-configuration-file) - Information about  an advanced configuration JSON file that you can upload.
* [Configuring an S3 Bucket to use with Axonius](/docs/configuring-an-s3-bucket-to-use-with-axonius) - Setting up an S3 bucket to save files on AWS S3 buckets.
* [Connecting the AWS Adapter Using an IAM User](/docs/connecting-aws-adapter-using-iam-user) - Connecting the adapter using an IAM user and an EC2 instance.
* [AWS Permissions](/docs/aws-permissions) - A summary of permissions that Axonius requires to fetch various AWS resources.