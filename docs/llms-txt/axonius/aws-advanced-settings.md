# Source: https://docs.axonius.com/docs/aws-advanced-settings.md

# AWS Advanced Settings

The **Amazon Web Services (AWS)** adapter has unique, advanced settings which enable configuring the logic around correlation of the AWS cloud servers (devices) and the information Axonius will fetch for each of them. Some of these settings required specific permissions. You can learn more about required permissions [here](/docs/aws-permissions).

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch ECS clusters** (default: true) - Select this option to fetch ECS clusters.
2. **Fetch EKS clusters** (default: true) - Select this option to fetch EKS clusters.
3. **Correlate ECS containers with their EC2 Instance** - Select whether to correlate ECS containers with the EC2 host they are running on.
   * If enabled, this adapter correlates ECS containers with the EC2 host they are running on.
   * If disabled,  this adapter will not correlate ECS containers with the EC2 host they are running on. Such ECS and EC2 resources will be created in Axonius as two different devices.
4. **Correlate EKS containers with their EC2 Instance** - Select whether to correlate EKS containers with the EC2 host they are running on.
   * If enabled,   this adapter correlates EKS containers with the EC2 host they are running on.
   * If disabled,   this adapter does not correlate EKS containers with the EC2 host they are running on. Such EKS and EC2 resources will be created in Axonius as two different devices.
5. **Add information about Security Hub findings to assets** - Select whether to fetch information about AWS Security Hub findings. When you enable this, you can also enable the following optional settings:
   1. Fetch Security Hub Findings with severity levels
   2. Fetch Security Hub Findings with Workflow Status (up to 100000)
   3. Fetch Security Hub Findings with Record States

<Callout icon="📘" theme="info">
  Note

  * In order to fetch SecurityHub information, you must have **AWSSecurityHubReadOnlyAccess** permission. Additional configuration is needed. Refer to [Policies for GuardDuty, Macie, and SecurityHub](/docs/connecting-aws-adapter-using-iam-user#policies-for-guardduty-macie-and-securityhub).

  * To fetch SecurityHub findings from more than one region, navigate to AWS and select **Get All Regions**.
</Callout>

6. **Avoid fetching the EBS disks of no EC2s or of EC2s that were not fetched by the account** - Select this option to fetch only EBS volumes that belong to EC2s that are fetchable by the current connection’s accounts.
7. **Fetch ECR Images as devices** - Select this option to fetch AWS ECR (Elastic Container Registry) public and private images as devices.
8. **Enrich ECR Repositories with tags** - Select this option to enrich ECR Repositories with their tags.
9. **Correlate ECR hosted images with compatible containers** - Select to add more information to existing AWS ECS/EKS assets.
10. **Add information about Security Hub findings to assets** - Select whether you want to fetch Security Hub findings and which type of findings to fetch. You can choose between the following options:
    * Fetch Security Hub Findings (default)
    * Fetch SUPPRESSED Security Hub Findings with high severity (up to 100,000)
    * Fetch SUPPRESSED Security Hub Findings (up to 100,000)
    * False (do not fetch any Security Hub findings)
11. **Enrich assets with Managed Prefix Lists information** - Select this option to enrich assets - specifically, security groups - with prefix list information.
12. **Associate role policies to users and roles** - Select this option to fetch more information from Access Advisor so that you can can search for all services that a user or role has access to but they did not use within a certain number of days. This can be used to create a least access IAM policy.
    To activate this capability and fetch this information, you need to select the following additional options in the AWS Configuration Advanced Settings:

    * Fetch information about IAM users
    * Fetch IAM roles as users
    * Parse IAM policies
    * Fetch IAM User’s AWS Services\
      This feature only presents data after the second discovery cycle after you enable the feature.

* If enabled, this adapter  fetches additional information from the AWS IAM service.
* If disabled,   this adapter will not fetch additional information from the AWS IAM service.

9. **Fetch information about EC2 attached roles** - Select whether to fetch information about each EC2 attached roles.
   * If enabled, all connections for this adapter will fetch information about each EC2 attached role from AWS.
   * If disabled, all connections for this adapter will not fetch any information about each EC2 attached role from AWS.
10. **Add information about Guard Duty findings to assets** - Select to add information about Amazon GuardDuty findings to assets.

<Callout icon="📘" theme="info">
  Note

  To use this parameter, Axonius requires **AmazonGuardDutyReadOnlyAccess** permission. 	Additional configuration is needed. Refer to [Policies for GuardDuty, Macie, and SecurityHub](/docs/connecting-aws-adapter-using-iam-user#policies-for-guardduty-macie-and-securityhub).
</Callout>

11. **Fetch FSx metadata as assets** - Select to fetch Amazon FSx metadata as assets.

<Callout icon="📘" theme="info">
  Note

  The API for FSx metadata requires the fsx:DescribeFileSystems permission.
</Callout>

12. **Fetch EFS assets** - Select to fetch EFS assets as File Systems.

13. **Fetch Auto Scaling Groups as assets** - Select this option to fetch Auto Scaling Groups and Policies.

14. **Fetch Secret Manager information** - Select to fetch Secret Manager information.

15. **Fetch VPNs** - Select to fetch Site-to-Site VPNs.

16. **Fetch information about ELB (Elastic Load Balancers)** - Select whether to fetch the ELB as devices and enrich the ELB with EC2/ECS information.

17. **Fetch IAM groups as users** - Select this option to fetch IAM groups and create a user for each IAM group  fetched.

18. **Fetch policies as users** - Select this option to fetch polices  and create a user for each policy fetched.

19. **Fetch information about SSM (System Manager)** - Select whether to fetch additional information from AWS SSM for each host and display them as 'Configuration'  assets.
    * If enabled (default), all connections for this adapter will fetch additional information from AWS SSM for each host.
    * If disabled, all connections for this adapter will not fetch any information about AWS SSM.

20. **Fetch information about NAT Gateways** - Select whether to fetch NAT gateways as devices assets.
    * If enabled, all connections for this adapter will fetch all available NAT gateways data from AWS.
    * If disabled, all connections for this adapter will not fetch any NAT gateways data from AWS.

21. **Fetch internet gateways as devices** - Select whether to fetch internet gateways as devices assets.
    * If enabled (default), all connections for this adapter will fetch all available internet gateways data from AWS. Each internet gateway will be added as a unique device.
    * If disabled, all connections for this adapter will not fetch any internet gateways data from AWS.

22. **Fetch route tables as devices** - Select whether to route tables as devices assets.
    * If enabled, all connections for this adapter will fetch all available route table data from AWS. Each route table will be added as a unique device.
    * If disabled, all connections for this adapter will not fetch any route table data from AWS.

23. **Add route tables to devices** - Select whether to fetch information about route tables and add it to the appropriate devices.
    * If enabled, all connections for this adapter will fetch all route table data from AWS for the following services:
      * EC2
      * ELB
      * IGW
      * NAT
      * RDS
      * Workspaces
      * ECS - only if **Correlate ECS Containers with their EC2 Instance** checkbox is enabled.
      * EKS - only if **Correlate EKS Containers with their EC2 Instance** checkbox is enabled.
    * If disabled, all connections for this adapter will not fetch any route table data from AWS.

24. **Fetch information about Elasticsearch** - Select whether to fetch  information on the existing Elasticsearch instances.
    * If enabled, all connections for this adapter will fetch all existing Elasticsearch instance data from AWS.
    * If disabled, all connections for this adapter will not fetch any Elasticsearch instance data from AWS.

25. **Fetch SNS topics as devices** - Select this option to fetch  SNS topics as devices.

26. **Fetch SQS queues as devices** -  Select this option to fetch  SQS queues as devices.

27. **Enrich SQS queues with tags** - Select this option to enrich SQS queues with their tag information. You must select the previous setting **Fetch SQS queues as devices** for this to work.

28. **Fetch Backup data as devices** - Select this option to  fetch AWS backup plans and vaults. Backup plans define the backup requirements, including backup schedules, backup retention rules and lifecycle rules.
    Backup vaults are containers where the backups are stored. Note that permissions are required for this.

29. **Fetch Direct Connect data** - Select this option to fetch Direct Connect assets associated with Network Services.

30. **Fetch Glue data as devices** - Select this option to fetch glue data as devices. Note that permissions are required for this.

31. **Fetch Redshift Clusters as devices** - Select this option to fetch basic information about Redshift Clusters.

32. **Fetch Service Catalog** - Select this option to fetch AWS Services Catalog as assets.

33. **Fetch Step Functions** - Select this option to fetch AWS step functions as assets.

34. **Fetch Kinesis Data Stream** - Select this option to fetch the Kinesis Data Stream.

35. **Fetch Kinesis Data Analytics** - Select this option to fetch the Kinesis Data analytics as devices.

36. **Fetch Lightsail Data** - Select this option to fetch Lightsail instances as devices.

37. **Fetch ELB IP using current DNS** - Select whether to resolve the IP address of each ELB using the current DNS server.
    * If enabled (default), all connections for this adapter will resolve the IP address of each ELB using the current DNS server.
    * If disabled, all connections for this adapter will not resolve the IP address of each ELB.

<Callout icon="📘" theme="info">
  Note

  This setting will only take effect if the **Fetch information about ELB (Elastic Load Balancers)** option is selected.
</Callout>

38. **Fetch information about RDS (Relational Database Service)** - Select whether to fetch the information on the existing Amazon RDS instances. To fetch the disk volume used by Aurora DB from RDS cloudwatch 'GetMetricStatistics' permission must be enabled.
    * If enabled, all connections for this adapter will fetch all existing Amazon RDS instance data from AWS.
    * If disabled, all connections for this adapter will not fetch any Amazon RDS instance data from AWS.

39. **Fetch information about ElastiCache cluster** - Select this option to fetch information about ElastiCache cluster

40. **Fetch information about Elastic Cache Replication Groups** - Select this option to fetch information about Elastic Cache Replication Groups as an asset.

41. **Fetch information about DynamoDB (NoSQL Database Service)** - Select whether to fetch the information on AWS DynamoDB.
    * If enabled, all connections for this adapter will fetch information on DynamoDB from AWS.
    * If disabled, all connections for this adapter will not fetch information on DynamoDB from AWS.

42. **Fetch SageMaker notebooks as devices** - Select this option to fetch SageMaker notebooks as devices.

43. **Fetch Orphan EBS Volumes as assets** - Select this option to fetch Orphan EBS Volumes as Disks.

44. **Fetch information about S3** - Select whether to fetch information on Amazon S3 buckets, such as their ACL's, locations and their public status.
    * If enabled (default), all connections for this adapter will fetch information about Amazon S3 buckets data from AWS.
    * If disabled, all connections for this adapter will not fetch any Amazon S3 buckets data from AWS.
    * When using the [Cloud Asset Compliance](/docs/cloud-asset-compliance-page), this settings is required to view Affected Devices of type S3 buckets.
    * To fetch S3 Outposts Buckets, you must also enable **Fetch information about Outpost as Compute Service Assets** (see below).

45. **Add information about Macie to S3** - Select whether to fetch information obtained by Amazon Macie about S3 buckets. Additional configuration is needed. Refer to [Policies for GuardDuty, Macie, and SecurityHub](/docs/connecting-aws-adapter-using-iam-user#policies-for-guardduty-macie-and-securityhub).

46. **Enrich assets with KMS information** - Select to enrich RDS assets with KMS information.

47. **Enrich S3 Buckets With Bucket Size** - Select this option to enrich “S3 bucket” devices with their bucket size. Note that you have to select 'Fetch information about S3' to use this option.

48. **Fetch information about IAM Users** - Select whether to fetch information about IAM users, attached groups, attached policies and access keys.
    * If enabled, all connections for this adapter will fetch information about IAM users, attached groups, attached policies and access keys.
    * If disabled, all connections for this adapter will not fetch any information about IAM users from AWS.
    * When using the [Cloud Asset Compliance](/docs/cloud-asset-compliance-page), this setting is required to view Affected Devices of the type IAM Users.

49. **Fetch Transit Gateways** - Select to fetch transit gateways.

50. **Fetch IAM roles as users** - Select whether to add IAM roles as user assets.
    * If enabled, all connections for this adapter will fetch IAM roles from AWS. Each IAM role will be added as a unique user.
    * If disabled, all connections for this adapter will not fetch IAM roles from AWS.

51. **Fetch VPCs as assets** - Select whether to add VPCs as  assets.
    * If enabled, all connections for this adapter will fetch VPCs from AWS. Each VPC will be added as a unique asset.
    * If disabled, all connections for this adapter will not fetch VPCs from AWS.

52. **Fetch Subnets as assets** - Select this option to split the subnets of a VPC network into individual assets.

53. **Parse IAM policies** - Select whether to fetch information about the privileges that are granted to each AWS IAM user by group, inline and attached IAM policies.
    * If enabled, all connections for this adapter will query each AWS IAM user to determine the privileges that are granted to it by group, inline and attached IAM policies.
    * If disabled, all connections for this adapter will not fetch information about the privileges that are granted to each AWS IAM user.

54. **Fetch IAM Users'  and Roles' AWS Services** - Select whether to fetch the AWS Services accessed by an IAM User or IAM Role.
    * If enabled, all connections for this adapter will fetch the AWS Services accessed by an IAM User or Role.
    * If disabled, all connections for this adapter will not fetch the AWS Services accessed by an IAM User or Role.

55. **Fetch information about Workspaces** - Select whether to fetch information about Amazon Workspaces.
    * If enabled, all connections for this adapter will fetch Amazon Workspaces data from AWS.
    * If disabled, all connections for this adapter will not fetch any Amazon Workspaces data from AWS.

56. **Fetch information about Lambdas** - Select whether to fetch information on AWS Lambdas.
    * If enabled, all connections for this adapter will fetch AWS Lambdas data from AWS.
    * If disabled, all connections for this adapter will not fetch any AWS Lambdas data from AWS.

57. **Fetch information about Route 53** - Select this option to fetch information on Amazon Route 53 DNS records as Network Service assets. When appropriate permissions are assigned (route53domains:ListDomains, route53domains:GetDomainDetail), this setting also enriches the devices with Domain details information.

58. **Fetch CloudWatch Alarms as Assets** - Select this option to fetch CloudWatch Alarms as assets.

59. **Fetch Global Accelerators as devices** - Select this option to fetch Global Accelerators as devices, note that appropriate permissions (globalaccelerator:ListAccelerators,
    globalaccelerator:ListCustomRoutingAccelerators) are required.

60. **Fetch information about Cloudfront** - Select this option to fetch information about  Cloudfront from AWS.

61. **Fetch CloudFormation Stacks as Assets** - Select whether to fetch CloudFormation Stacks as assets.

62. **Add WAF to devices** - Select whether to enrich devices with WAF information. WAF (WebAcl) versions 1 and 2 for regional and Cloudfront devices.
    * If enabled, all connections for this adapter will enrich relevant devices with WAF information.
    * If disabled, all connections for this adapter will enrich devices with WAF information.

63. **Fetch Organizations as assets** - Select whether to add Organizations data as assets.
    * If enabled, all connections for this adapter will fetch Organizations data from AWS. Each Organization will be added as a unique asset.
    * If disabled, all connections for this adapter will not fetch Organizations data from AWS.

64. **Fetch information about API Gateway** - Select whether to fetch AWS API Gateways and their related data.
    * If enabled, all connections for this adapter will fetch AWS API Gateways and their related data.
    * If disabled, all connections for this adapter will not  fetch AWS API Gateways and their related data.

65. **Fetch Inspector Findings** *(required, default: Do not fetch)* - Select from the dropdown menu which AWS Inspector settings to fetch. If any of the **Severity** filters are selected, Axonius fetches security findings about EC2 instances directly from AWS Inspector (versions 1 and 2). ECR container findings are also fetched when **Fetch ECR Images as devices** is selected.

66. **Fetch information about AppStream devices** - Select to fetch information about AppStream devices.

67. **Fetch information about AppStream users** - Select to fetch information about AppStream users.

68. **Fetch information about Elastic Beanstalk Environments** - Select to fetch Elastic Beanstalk environments as assets. If enabled, these environments will appear under Application Services. Note that permissions are required for this.

69. **Fetch information about Outpost as Compute Service Assets** - Select to fetch outposts as Compute Services assets.
    * To fetch S3 Outpost Buckets, you must also enable **Fetch information about S3** (see above).

70. **Fetch Identity Store Users and Groups** - Select to fetch fetch Identity Store users and groups. They will be fetched as Users and Groups asset types.

71. **Use Cloud ID as manufacturer serial number** *(default: true)* - Select this option to use the Cloud ID as the manufacturer serial number.

72. **Shodan API key for more IP info** *(optional)* – Specify an API key which will be used to query information about public IP addresses.

73. **Verify all IAM roles** *(required, default: true)* - Select whether to verify all IAM roles.
    * If enabled, all connections for this adapter will verify all IAM roles. If one of the IAM roles is not valid, the adapter connection will fail.
    * If disabled, all connections for this adapter will not verify all IAM roles. Only if all the IAM roles are not valid, the adapter connection will fail.

74. **Verify primary account permissions** *(required, default: true)* - Whether or not the primary account permissions should be used when the adapter connections fetch data from AWS.
    * If enabled, all connections for this adapter will use the primary account permissions to fetch data from AWS. If the primary account permissions are insufficient, the adapter connections will fail to fetch the data.
    * If disabled, all connections for this adapter will only use the primary account to assume the roles attached to it, and the adapter connections will use those role permissions to fetch data from AWS. This setting should be disabled only if you want to use the primary account assumed roles permissions instead of the primary account permissions when fetching assets from AWS.

75. **Do not fetch EC2 machines that are turned off** - Whether or not to fetch EC2 devices whose power state is turned off.
    * If enabled, all connections for this adapter will only fetch EC2 devices whose power state is turned on.
    * If disabled, all connections for this adapter will fetch all EC2 devices, regardless of their power state.

76. **Fetch information about non active resources managed by SSM (System Manager)** - Select this option to fetch SSM information for all EC2 instances, including powered-off or terminated instances.

77. **Fetch only currently used images (AMIs)** *(optional, default: true)* - When this setting is unselected, the adapter fetches AMIs created by the client (self-owned).

78. **Expand AWS IAM Policies** *(optional, default: true)* - Select whether to expand AWS IAM policies.

79. **Propagate AWS Organizations account tags to associated assets** - Select to propagate all tags of each AWS account to its hosted devices. For example, if Account X has Tag Y, all devices belonging to Account X have Tag Y.

80. **Number of accounts to fetch in parallel** *(required, default: 5)* - For all connections for this adapter, specify the number of AWS accounts Axonius will fetch data from in parallel.

81. **Parallel workers amount in users fetch** *(required, default: 5)* - Specify the number of distributed workers (processes) to fetch data during the users fetch phase.

82. **Advanced Modes** -  Implemented in specific cases as instructed by Axonius team.

83. **List of tags to parse as fields** *(optional)* - Specify a comma-separated list of tag keys to be parsed as device or user fields. Each tag is a key-value pair that is part of the **Adapter Tags** complex field.
    * The tag is only parsed on AWS\_EC2 resource types by default. Meaning, adding AWS\_EC2 resource type tags into fields does not require a resource type. For example, if you add an the key `Horizontal` as an adapter type tag, it will be added to the field as `Horizontal`. You can then add additional values separated with a comma, for example: `Horizontal`, `Audit`, etc.

    * Tags with case-sensitive values are supported. Enter tags with case-sensitive values with double-quotes, e.g. . aws\_ec2:”DEVELOP”

    * To specify a different resource type, enter the tag name in the form `aws_resource_type:tag_name`. Examples: `aws_s3:bucketteam`, `aws_s3:bucketdept`, `aws_dynamodb:dbteam`

    * If supplied, all connections for this adapter will parse any of the listed tags that are associated with the fetched device or user as:
      * Values of the **Adapter Tags** field.
      * Designated field with the name of the tag key and the value of the tag value.

    * If not supplied, all connections for this adapter will only parse all tags as values of the **Adapter Tags** field.

84. **Perform distributed data processing** - Select to fetch and process data-intensive parts in parallel, using distribution. This option accelerates the processing stages during the fetch.

85. **Number of workers for distributed data processing** *(optional, default: 2)* - Specify the number of workers (independent processes that run in parallel) that process data.

86. **EC2 Host Name Population** *(optional, default: 'Public DNS or Private DNS')* - Select the EC2 hostname population. Options are:
    * Public DNS or Private DNS
    * Public DNS
    * Private DNS
    * Disable - No EC2 hostnames are populated

87. **Fetch cost by service** - Select "Yes" to fetch cost data for AWS services. When you select this, you can configure the following:
    * **Get cost data for the last X days:** (default: 30)
    * **Cost explorer group by tags** (default: empty)
      To fetch cost data, you must have an admin account with the following permissions:
    * organizations:ListAccounts
    * ce:GetCostAndUsage

<Callout icon="💡" theme="warn">
  Important

  Using the Cost Explorer API costs **1 cent per request**. You should take this into consideration before enabling this option, especially if you have numerous assets to fetch.
</Callout>

73. **Use Account Alias Instead of Name in Cloud Provider Account Name (Legacy)** *(optional, default: true)* - When this option is selected, the Cloud Provider Account Name field's value is the account name. When this option is unselected, this field's value the account alias.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>