# Source: https://docs.axonius.com/docs/aws-permissions.md

# AWS Permissions

These tables summarize permissions that Axonius requires to fetch various AWS resources. Use this information both to enable required permissions, and to only apply necessary permissions.

All permissions are also listed in JSON format under each table. Note that each JSON lists all permissions and resources, so when copying it, ensure to change it according to your needs.

## Adapter Fetch Permissions

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        AWS Service
      </th>

      <th>
        Permissions
      </th>

      <th>
        Axonius Setting
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        API Gateway
      </td>

      <td>
        * GET
      </td>

      <td>
        * Fetch information about API Gateways
      </td>
    </tr>

    <tr>
      <td>
        API Gateway v2
      </td>

      <td>
        * apigateway:GET
      </td>

      <td>
        * Fetch information about API Gateways v2
      </td>
    </tr>

    <tr>
      <td>
        ACM
      </td>

      <td>
        * acm:DescribeCertificate
        * acm:ListCertificates
      </td>

      <td>
        * Basic fetch
      </td>
    </tr>

    <tr>
      <td>
        AppStream
      </td>

      <td>
        * appstream:DescribeUsers appstream:DescribeUserStackAssociations
      </td>

      <td>
        * Fetch information about AWS AppStream users
      </td>
    </tr>

    <tr>
      <td>
        AppStream
      </td>

      <td>
        * appstream:DescribeStacks appstream:ListAssociatedFleets appstream:DescribeFleets
      </td>

      <td>
        * Fetch information about AWS AppStream devices
      </td>
    </tr>

    <tr>
      <td>
        Athena
      </td>

      <td>
        * athena:ListDataCatalogs
        * athena:ListDatabases
        * athena:ListQueryExecutions
        * athena:ListTableMetadata
      </td>

      <td>
        * Fetch Athena tables as Devices - BETA
      </td>
    </tr>

    <tr>
      <td>
        Autoscaling
      </td>

      <td>
        * autoscaling:DescribeAutoScalingGroups autoscaling:DescribePolicies autoscaling:DescribeAutoScalingInstances
      </td>

      <td>
        * Basic Fetch
      </td>
    </tr>

    <tr>
      <td>
        Backup
      </td>

      <td>
        * backup:ListBackupPlans
        * backup:ListBackupVaults
      </td>

      <td>
        * Fetch backup plans and vaults
      </td>
    </tr>

    <tr>
      <td>
        CloudFormation
      </td>

      <td>
        * cloudformation:DescribeStacks
        * cloudformation:ListStackSets
        * cloudformation:ListStacks
      </td>

      <td>
        * Fetch information about CloudFormation
      </td>
    </tr>

    <tr>
      <td>
        Cloudfront
      </td>

      <td>
        * cloudfront:GetDistribution
        * cloudfront:ListDistributions
      </td>

      <td>
        * Fetch information about Cloudfront
      </td>
    </tr>

    <tr>
      <td>
        Cloudwatch
      </td>

      <td>
        * cloudwatch:GetMetricStatistics cloudwatch:DescribeAlarms
      </td>

      <td>
        * Disk volume used by Aurora DB from RDS cloudwatch, Fetch CloudWatch Alarms as assets.
      </td>
    </tr>

    <tr>
      <td>
        Direct Connect
      </td>

      <td>
        * directconnect:DescribeConnections
        * directconnect:DescribeLags
        * directconnect:DescribeVirtualGateways
        * directconnect:DescribeVirtualInterfaces
      </td>

      <td>
        * Fetch Direct Connect Data
      </td>
    </tr>

    <tr>
      <td>
        DynamoDB
      </td>

      <td>
        * dynamodb:DescribeTable
        * dynamodb:DescribeGlobalTable dynamodb:DescribeGlobalTableSettings dynamodb:ListGlobalTables
        * dynamodb:ListTables
        * dynamodb:ListTagsOfResource
      </td>

      <td>
        * Fetch information about DynamoDB
      </td>
    </tr>

    <tr>
      <td>
        EC2
      </td>

      <td>
        * ec2:CreateSnapshot
        * ec2:DescribeAddresses
        * ec2:DescribeFlowLogs
        * ec2:DescribeImages
        * ec2:DescribeInstances
        * ec2:DescribeInstanceStatus
        * ec2:DescribeInternetGateways
        * ec2:DescribeManagedPrefixLists
        * ec2:DescribeNatGateways
        * ec2:DescribeRouteTables
        * ec2:DescribeSnapshotAttribute
        * ec2:DescribeSnapshots
        * ec2:DescribeSecurityGroups
        * ec2:DescribeSubnets
        * ec2:DescribeTags
        * ec2:DescribeVolumes
        * ec2:DescribeVpcPeeringConnections
        * ec2:DescribeVpcs
        * ec2:DescribeVpnConnections
        * ec2:DescribeCustomerGateways
        * ec2:DescribeTransitGatewayAttachments
        * ec2:DescribeTransitGatewayPeeringAttachments
        * ec2:DescribeTransitGatewayRouteTables
        * ec2:DescribeTransitGateways
        * ec2:DescribeNetworkInterfaces
      </td>

      <td>
        * Basic Fetch
        * ec2:DescribeVpnConnections - only required when the Fetch VPNs advanced configuration is turned on.
      </td>
    </tr>

    <tr>
      <td>
        ECR
      </td>

      <td>
        * ecr:DescribeImages
        * ecr:DescribeRegistry
        * ecr:DescribeRepositories
        * ecr-public:DescribeImages
        * ecr-public:DescribeRegistries
        * ecr-public:DescribeRepositories
      </td>

      <td>
        * Fetch ECR images as devices
        * Correlate ECR-hosted images with compatible containers
      </td>
    </tr>

    <tr>
      <td>
        ECS
      </td>

      <td>
        * ecs:DescribeClusters
        * ecs:DescribeContainerInstances
        * ecs:DescribeServices
        * ecs:DescribeTasks
        * ecs:ListClusters
        * ecs:ListContainerInstances
        * ecs:ListServices
        * ecs:ListTagsForResource
        * ecs:ListTasks
      </td>

      <td>
        * Basic Fetch
      </td>
    </tr>

    <tr>
      <td>
        EKS
      </td>

      <td>
        * eks:DescribeCluster
        * eks:ListClusters
        * eks:DescribeClusterVersions
      </td>

      <td>
        * Basic Fetch
      </td>
    </tr>

    <tr>
      <td>
        ELB
      </td>

      <td>
        * elasticloadbalancing:DescribeLoadBalancerPolicies elasticloadbalancing:DescribeLoadBalancers elasticloadbalancing:DescribeListeners elasticloadbalancing:DescribeSSLPolicies elasticloadbalancing:DescribeTargetGroups elasticloadbalancing:DescribeTargetHealth
        * elasticloadbalancing:DescribeTags
        * elasticloadbalancing:DescribeRules
      </td>

      <td>
        * Fetch information about ELB (Elastic Load Balancers)
      </td>
    </tr>

    <tr>
      <td>
        ELB v2
      </td>

      <td>
        * elasticloadbalancing:DescribeLoadBalancers
        * elasticloadbalancing:DescribeTags
        * elasticloadbalancing:DescribeListeners
        * elasticloadbalancing:DescribeTargetGroups
        * elbv2:DescribeRules
      </td>

      <td>
        * Fetch information about ELB (Elastic Load Balancers) v2
      </td>
    </tr>

    <tr>
      <td>
        Elastic Beanstalk
      </td>

      <td>
        * elasticbeanstalk:DescribeEnvironments
      </td>

      <td>
        * Fetch information about Elastic Beanstalk environments
      </td>
    </tr>

    <tr>
      <td>
        ElastiCache
      </td>

      <td>
        * elasticache:DescribeCacheClusters
        * elasticache:DescribeReplicationGroups
        * elasticache:ListTagsForResource
      </td>

      <td>
        * Fetch information about ElastiCache cluster
      </td>
    </tr>

    <tr>
      <td>
        Elasticsearch
      </td>

      <td>
        * es:DescribeElasticsearchDomains
        * es:ListDomainNames
      </td>

      <td>
        * Fetch information about Elasticsearch
      </td>
    </tr>

    <tr>
      <td>
        FSx
      </td>

      <td>
        * fsx:DescribeFileSystems
      </td>

      <td>
        * Fetch FSx metadata
      </td>
    </tr>

    <tr>
      <td>
        Globalaccelerator
      </td>

      <td>
        * globalaccelerator:ListAccelerators globalaccelerator:ListCustomRoutingAccelerators
      </td>

      <td>
        * Fetch Global Accelerators
      </td>
    </tr>

    <tr>
      <td>
        Glue
      </td>

      <td>
        * glue:GetDatabases
        * glue:GetTables
      </td>

      <td>
        * Fetch Glue data
      </td>
    </tr>

    <tr>
      <td>
        GuardDuty
      </td>

      <td>
        * guardduty:GetFindings
        * guardduty:GetDetector
        * guardduty:GetMembers
        * guardduty:GetFilter
        * guardduty:ListDetectors
        * guardduty:ListFilters
        * guardduty:ListMembers
        * guardduty:ListFindings
      </td>

      <td>
        * Add information about GuardDuty findings to assets
      </td>
    </tr>

    <tr>
      <td>
        IAM
      </td>

      <td>
        * iam:GenerateCredentialReport iam:GenerateServiceLastAccessedDetails iam:GetAccessKeyLastUsed iam:GetAccountPasswordPolicy iam:GetAccountSummary
        * iam:GetCredentialReport
        * iam:GetLoginProfile
        * iam:GetPolicy
        * iam:GetPolicyVersion
        * iam:GetRole
        * iam:GetRolePolicy iam:GetServiceLastAccessedDetails
        * iam:GetUser
        * iam:GetUserPolicy
        * iam:ListAccessKeys
        * iam:ListAccountAliases iam:ListAttachedGroupPolicies iam:ListAttachedRolePolicies iam:ListAttachedUserPolicies iam:ListEntitiesForPolicy
        * iam:ListGroups
        * iam:ListGroupsForUser iam:ListInstanceProfilesForRole
        * iam:ListMFADevices
        * iam:ListPolicies
        * iam:ListRolePolicies
        * iam:ListRoles
        * iam:ListUserPolicies
        * iam:ListUserTags
        * iam:ListUsers
        * iam:ListVirtualMFADevices
        * iam:GetGroup (used when **Fetch groups as users** is set)
      </td>

      <td>
        * Fetch information about IAM Users
        * Fetch IAM roles as users
        * Parse IAM policies
      </td>
    </tr>

    <tr>
      <td>
        Identity Store
      </td>

      <td>
        * identitystore:ListGroups
        * identitystore:ListUsers
        * sso:ListInstances
        * sso:ListPermissionSets
        * sso:ListAccountsForProvisionedPermissionSet
        * sso:ListAccountAssignments
        * identitystore:ListGroupMembershipsForMember
      </td>

      <td>
        * Fetch Identity Store users and groups
      </td>
    </tr>

    <tr>
      <td>
        Inspector
      </td>

      <td>
        * inspector:ListFindings
        * inspector:DescribeFindings
        * inspector2:ListFindings
        * inspector2:ListMembers
      </td>

      <td>
        * Fetch Inspector Findings
      </td>
    </tr>

    <tr>
      <td>
        Kinesis
      </td>

      <td>
        * kinesis:ListStreams
      </td>

      <td>
        * Fetch Kinesis Data Stream
      </td>
    </tr>

    <tr>
      <td>
        Kinesis Data Analytics
      </td>

      <td>
        * kinesisanalytics:DescribeApplication, kinesisanalytics:ListApplications
        * kinesis:DescribeStream
      </td>

      <td>
        * Kinesis Data Analytics as devices.
      </td>
    </tr>

    <tr>
      <td>
        Lambda
      </td>

      <td>
        * lambda:GetPolicy
        * lambda:GetFunctionUrlConfig
        * lambda:ListFunctions
        * lambda:ListTags
      </td>

      <td>
        * Fetch information about Lambdas
      </td>
    </tr>

    <tr>
      <td>
        Lightsail
      </td>

      <td>
        * lightsail:GetInstances
      </td>

      <td>
        * Fetch Lightsail Instances
      </td>
    </tr>

    <tr>
      <td>
        Macie
      </td>

      <td>
        * macie2:GetFindings
        * macie2:ListFindings
        * macie2:ListMembers
      </td>

      <td>
        * Fetch information about Macie findings
      </td>
    </tr>

    <tr>
      <td>
        Organizations - Base
      </td>

      <td>
        * organizations:DescribeAccount organizations:DescribeOrganization organizations:ListPoliciesForTarget organizations:ListTagsForResource
      </td>

      <td>
        * Basic Fetch
      </td>
    </tr>

    <tr>
      <td>
        Organizations - Account Name
      </td>

      <td>
        * organizations:ListAccounts
      </td>

      <td>
        * Required for discovery of member accounts when fetching AWS Organizations
      </td>
    </tr>

    <tr>
      <td>
        Organizations - Complete
      </td>

      <td>
        * organizations:DescribeOrganization organizations:DescribeEffectivePolicy organizations:DescribePolicy
      </td>

      <td>
        * Fetch Organizations as assets
      </td>
    </tr>

    <tr>
      <td>
        Outposts
      </td>

      <td>
        * outposts:ListAssets
        * outposts:ListSites
        * outposts:ListOutposts
      </td>

      <td>
        * Fetch information about AWS Outposts assets
      </td>
    </tr>

    <tr>
      <td>
        RDS
      </td>

      <td>
        * rds:DescribeDBClusters
        * rds:DescribeDBInstances
        * rds:DescribeOptionGroups
        * rds:describePendingMaintenanceActions
      </td>

      <td>
        * Fetch information about RDS (Relational Database Service) RDS (Relational Database Service) Instances, Clusters and Global Clusters
      </td>
    </tr>

    <tr>
      <td>
        Redshift
      </td>

      <td>
        * redshift:DescribeClusters
      </td>

      <td>
        * Fetch Redshift Clusters as devices
      </td>
    </tr>

    <tr>
      <td>
        Route53
      </td>

      <td>
        * route53:ListHostedZones route53:ListResourceRecordSets
        * route53domains:ListDomains route53domains:GetDomainDetail route53resolver:ListResolverRules route53resolver:ListResolverRuleAssociations
        * route53domains:ListDomains
      </td>

      <td>
        * Fetch information about Route 53
      </td>
    </tr>

    <tr>
      <td>
        S3
      </td>

      <td>
        * s3:GetAccountPublicAccessBlock
        * s3:GetBucketAcl
        * s3:GetBucketLocation
        * s3:GetBucketLogging
        * s3:GetBucketPolicy
        * s3:GetBucketPolicyStatus s3:GetBucketPublicAccessBlock
        * s3:GetBucketTagging
        * s3:GetEncryptionConfiguration
        * s3:ListAllMyBuckets
        * s3:ListBucket
      </td>

      <td>
        * Fetch information about S3
      </td>
    </tr>

    <tr>
      <td>
        S3 Outposts
      </td>

      <td>
        * outposts:ListOutposts
        * s3-outposts:ListOutpostsWithS3
        * s3-outposts:ListRegionalBuckets
      </td>

      <td>
        * Fetch information about S3
        * Fetch information about Outpost as Compute Service Assets
      </td>
    </tr>

    <tr>
      <td>
        SageMaker
      </td>

      <td>
        * sagemaker:ListNotebookInstances
        * sagemaker:DescribeNotebookInstance
        * sagemaker:ListTags
      </td>

      <td>
        * Fetch SageMaker notebooks as devices
      </td>
    </tr>

    <tr>
      <td>
        SecurityHub
      </td>

      <td>
        * securityhub:DescribeHub
        * securityhub:GetFindings
        * securityhub:ListMembers securityhub:ListTagsForResource
      </td>

      <td>
        * Add information about Security Hub findings to assets
      </td>
    </tr>

    <tr>
      <td>
        SNS
      </td>

      <td>
        * sns:ListSubscriptionsByTopic
      </td>

      <td>
        * Fetch SNS topics as devices
      </td>
    </tr>

    <tr>
      <td>
        Step Functions
      </td>

      <td>
        * states:listStateMachines
        * states:describeStateMachine
      </td>

      <td>
        * Fetch step functions
      </td>
    </tr>

    <tr>
      <td>
        Service Catalog
      </td>

      <td>
        * servicecatalog:ListPortfolios, servicecatalog:DescribePortfolio
      </td>

      <td>
        * Fetch Services Catalog as assets
      </td>
    </tr>

    <tr>
      <td>
        Secrets Manager
      </td>

      <td>
        * secretsmanager:ListSecrets secretsmanager:GetResourcePolicy
      </td>

      <td>
        * Fetch information about Secrets Manager
      </td>
    </tr>

    <tr>
      <td>
        SQS Queues
      </td>

      <td>
        * sqs:ListQueues
        * sqs:GetQueueAttributes
        * sqs:ListQueueTags
      </td>

      <td>
        * Fetch SQS queues as devices
        * Enrich SQS queues with tags
      </td>
    </tr>

    <tr>
      <td>
        SSM
      </td>

      <td>
        * ssm:DescribeAvailablePatches ssm:DescribeInstanceInformation ssm:DescribeInstancePatches ssm:DescribePatchGroups ssm:GetInventorySchema ssm:ListInventoryEntries ssm:ListResourceComplianceSummaries ssm:ListTagsForResource
        * ssm:DescribeParameters
        * ssm:GetParameter
      </td>

      <td>
        * Fetch information about SSM (System Manager)
      </td>
    </tr>

    <tr>
      <td>
        WAFv1
      </td>

      <td>
        * waf:GetWebACL
        * waf:ListWebACLs
      </td>

      <td>
        * Add WAF to devices
      </td>
    </tr>

    <tr>
      <td>
        WAFRegional
      </td>

      <td>
        * waf-regional:GetWebACL
        * waf-regional:GetWebACLForResource
        * waf-regional:ListWebACLs
      </td>

      <td>
        * Add WAF to devices
      </td>
    </tr>

    <tr>
      <td>
        WAFv2
      </td>

      <td>
        * wafv2:GetWebACL
        * wafv2:GetWebACLForResource
        * wafv2:ListWebACLs
      </td>

      <td>
        * Add WAF to devices
      </td>
    </tr>

    <tr>
      <td>
        Workspaces
      </td>

      <td>
        * workspaces:DescribeTags workspaces:DescribeWorkspaceDirectories workspaces:DescribeWorkspaces workspaces:DescribeWorkspacesConnectionStatus
      </td>

      <td>
        * Fetch information about Workspaces
      </td>
    </tr>
  </tbody>
</Table>

### Adapter Fetch Permissions - JSON

<Accordion title="Expand/Collapse" icon="fa-info-circle">
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
    	{
    		"Sid": "AdapterFetchPermissions",
    		"Effect": "Allow",
    		"Action": [
    			"apigateway:GET",
    			"acm:DescribeCertificate",
    			"acm:ListCertificates",
    			"appstream:DescribeUsers",
    			"appstream:DescribeUserStackAssociations",
    			"appstream:DescribeStacks",
    			"appstream:ListAssociatedFleets",
    			"appstream:DescribeFleets",
    			"athena:ListDataCatalogs",
    			"athena:ListDatabases",
    			"athena:ListQueryExecutions",
    			"athena:ListTableMetadata",
    			"autoscaling:DescribeAutoScalingGroups",
    			"autoscaling:DescribePolicies",
    			"autoscaling:DescribeAutoScalingInstances",
    			"backup:ListBackupPlans",
    			"backup:ListBackupVaults",
    			"cloudformation:DescribeStacks",
    			"cloudformation:ListStackSets",
    			"cloudformation:ListStacks",
    			"cloudfront:GetDistribution",
    			"cloudfront:ListDistributions",
    			"cloudwatch:GetMetricStatistics",
    			"cloudwatch:DescribeAlarms",
    			"directconnect:DescribeConnections",
    			"directconnect:DescribeLags",
    			"directconnect:DescribeVirtualGateways",
    			"directconnect:DescribeVirtualInterfaces",
    			"dynamodb:DescribeTable",
    			"dynamodb:DescribeGlobalTable",
    			"dynamodb:DescribeGlobalTableSettings",
    			"dynamodb:ListGlobalTables",
    			"dynamodb:ListTables",
    			"dynamodb:ListTagsOfResource",
    			"ec2:CreateSnapshot",
    			"ec2:DescribeAddresses",
    			"ec2:DescribeFlowLogs",
    			"ec2:DescribeImages",
    			"ec2:DescribeInstances",
    			"ec2:DescribeInstanceStatus",
    			"ec2:DescribeInternetGateways",
    			"ec2:DescribeNatGateways",
    			"ec2:DescribeRouteTables",
    			"ec2:DescribeSnapshotAttribute",
    			"ec2:DescribeSnapshots",
    			"ec2:DescribeSecurityGroups",
    			"ec2:DescribeSubnets",
    			"ec2:DescribeTags",
    			"ec2:DescribeVolumes",
    			"ec2:DescribeVpcPeeringConnections",
    			"ec2:DescribeVpcs",
    			"ec2:DescribeVpnConnections",
    			"ec2:DescribeCustomerGateways",
    			"ec2:DescribeTransitGatewayAttachments",
    			"ec2:DescribeTransitGatewayPeeringAttachments",
    			"ec2:DescribeTransitGatewayRouteTables",
    			"ec2:DescribeTransitGateways",
    			"ecr:DescribeImages",
    			"ecr:DescribeRegistry",
    			"ecr:DescribeRepositories",
    			"ecr-public:DescribeImages",
    			"ecr-public:DescribeRegistries",
    			"ecr-public:DescribeRepositories",
    			"ecs:DescribeClusters",
    			"ecs:DescribeContainerInstances",
    			"ecs:DescribeServices",
    			"ecs:DescribeTasks",
    			"ecs:ListClusters",
    			"ecs:ListContainerInstances",
    			"ecs:ListServices",
    			"ecs:ListTagsForResource",
    			"ecs:ListTasks",
    			"eks:DescribeCluster",
        "eks:ListClusters",
    			"eks:DescribeClusterVersions",
    			"elasticloadbalancing:DescribeLoadBalancerPolicies",
    			"elasticloadbalancing:DescribeLoadBalancers",
    			"elasticloadbalancing:DescribeListeners",
    			"elasticloadbalancing:DescribeSSLPolicies",
    			"elasticloadbalancing:DescribeTargetGroups",
    			"elasticloadbalancing:DescribeTargetHealth",
    			"elasticloadbalancing:DescribeTags",
    			"elasticloadbalancing:DescribeRules",
    			"elasticbeanstalk:DescribeEnvironments",
    			"elasticache:DescribeCacheClusters",
    			"elasticache:DescribeReplicationGroups",
    			"elasticache:ListTagsForResource",
    			"es:DescribeElasticsearchDomain",
    			"es:ListDomainNames",
    			"fsx:DescribeFileSystems",
    			"globalaccelerator:ListAccelerators",
    			"globalaccelerator:ListCustomRoutingAccelerators",
    			"glue:GetDatabases",
    			"glue:GetTables",
    			"guardduty:GetFindings",
    			"guardduty:GetDetector",
    			"guardduty:GetMembers",
    			"guardduty:GetFilter",
    			"guardduty:ListDetectors",
    			"guardduty:ListFilters",
    			"guardduty:ListMembers",
    			"guardduty:ListFindings",
    			"iam:GenerateCredentialReport",
    			"iam:GenerateServiceLastAccessedDetails",
    			"iam:GetAccessKeyLastUsed",
    			"iam:GetAccountPasswordPolicy",
    			"iam:GetAccountSummary",
    			"iam:GetCredentialReport",
    			"iam:GetLoginProfile",
    			"iam:GetPolicy",
    			"iam:GetPolicyVersion",
    			"iam:GetRole",
    			"iam:GetRolePolicy",
    			"iam:GetServiceLastAccessedDetails",
    			"iam:GetUser",
    			"iam:GetUserPolicy",
    			"iam:ListAccessKeys",
    			"iam:ListAccountAliases",
    			"iam:ListAttachedGroupPolicies",
    			"iam:ListAttachedRolePolicies",
    			"iam:ListAttachedUserPolicies",
    			"iam:ListEntitiesForPolicy",
    			"iam:ListGroups",
    			"iam:ListGroupsForUser",
    			"iam:ListInstanceProfilesForRole",
    			"iam:ListMFADevices",
    			"iam:ListPolicies",
    			"iam:ListRolePolicies",
    			"iam:ListRoles",
    			"iam:ListUserPolicies",
    			"iam:ListUserTags",
    			"iam:ListUsers",
    			"iam:ListVirtualMFADevices",
    			"identitystore:ListGroups",
    			"identitystore:ListUsers",
    			"identitystore:ListGroupMembershipsForMember",
    			"sso:ListInstances",
    			"sso:ListPermissionSets",
    			"sso:ListAccountsForProvisionedPermissionSet",
    			"sso:ListAccountAssignments",
    			"inspector:ListFindings",
    			"inspector:DescribeFindings",
    			"inspector2:ListFindings",
    			"inspector2:ListMembers",
    			"kinesis:ListStreams",
    			"kinesisanalytics:DescribeApplication",
    			"kinesisanalytics:ListApplications",
    			"lambda:GetPolicy",
    			"lambda:GetFunctionUrlConfig",
    			"lambda:ListFunctions",
    			"lambda:ListTags",
    			"lightsail:GetInstances",
    			"macie2:GetFindings",
    			"macie2:ListFindings",
    			"macie2:ListMembers",
    			"organizations:DescribeAccount",
    			"organizations:DescribeOrganization",
    			"organizations:ListPoliciesForTarget",
    			"organizations:ListTagsForResource",
    			"organizations:ListAccounts",
    			"organizations:DescribeEffectivePolicy",
    			"organizations:DescribePolicy",
    			"outposts:ListAssets",
    			"outposts:ListSites",
    			"outposts:ListOutposts",
    			"rds:DescribeDBClusters",
    			"rds:DescribeDBInstances",
    			"rds:DescribeOptionGroups",
    			"rds:DescribePendingMaintenanceActions",
    			"redshift:DescribeClusters",
    			"route53:ListHostedZones",
    			"route53:ListResourceRecordSets",
    			"route53domains:ListDomains",
    			"route53domains:GetDomainDetail",
    			"route53resolver:ListResolverRules",
    			"route53resolver:ListResolverRuleAssociations",
    			"s3:GetAccountPublicAccessBlock",
    			"s3:GetBucketAcl",
    			"s3:GetBucketLocation",
    			"s3:GetBucketLogging",
    			"s3:GetBucketPolicy",
    			"s3:GetBucketPolicyStatus",
    			"s3:GetBucketPublicAccessBlock",
    			"s3:GetBucketTagging",
    			"s3:GetEncryptionConfiguration",
    			"s3:ListAllMyBuckets",
    			"s3:ListBucket",
    			"sagemaker:ListNotebookInstances",
    			"sagemaker:DescribeNotebookInstance",
    			"sagemaker:ListTags",
    			"securityhub:DescribeHub",
    			"securityhub:GetFindings",
    			"securityhub:ListMembers",
    			"securityhub:ListTagsForResource",
    			"sns:ListSubscriptionsByTopic",
    			"states:ListStateMachines",
    			"states:DescribeStateMachine",
    			"servicecatalog:ListPortfolios",
    			"servicecatalog:DescribePortfolio",
    			"secretsmanager:ListSecrets",
    			"secretsmanager:GetResourcePolicy",
    			"sqs:ListQueues",
    				"sqs:ListQueueTags",
    			"sqs:GetQueueAttributes",
                "ssm:DescribeAvailablePatches",
                "ssm:DescribeInstanceInformation",
                "ssm:DescribeInstancePatches",
                "ssm:DescribePatchGroups",
                "ssm:GetInventorySchema",
                "ssm:ListInventoryEntries",
                "ssm:ListResourceComplianceSummaries",
                "ssm:ListTagsForResource",
                "ssm:DescribeParameters",
                "ssm:GetParameter",
                "waf:GetWebACL",
                "waf:ListWebACLs",
                "waf-regional:GetWebACL",
                "waf-regional:GetWebACLForResource",
                "waf-regional:ListWebACLs",
                "wafv2:GetWebACL",
                "wafv2:GetWebACLForResource",
                "wafv2:ListWebACLs",
                "workspaces:DescribeTags",
                "workspaces:DescribeWorkspaceDirectories",
                "workspaces:DescribeWorkspaces",
                "workspaces:DescribeWorkspacesConnectionStatus"
    		],
    		"Resource": "*"
    	}
    ]
  }
  ```
</Accordion>

## Enforcement Center Permissions

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        AWS Service
      </th>

      <th>
        Permissions
      </th>

      <th>
        Resource Scope
      </th>

      <th>
        Axonius Setting
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        S3
      </td>

      <td>
        * s3:GetObject
        * s3:PutObject
        * s3:ListAllMyBuckets
        * s3:PutObjectTagging
        * s3:DeleteObject
        * s3:ListBucket
      </td>

      <td>
        These permissions should be scoped to a bucket/objects that are specifically created for Axonius to write to. Do not scope these permissions to all resources.
      </td>

      <td>
        Enforcement Center Actions that involve sending data to S3. For more information, see the [Enforcement Center Action Index](https://docs.axonius.com/docs/enforcement-action-library-index)
      </td>
    </tr>

    <tr>
      <td>
        EC2
      </td>

      <td>
        * ec2:StartInstances
        * ec2:StopInstances
        * tag:GetResources
        * tag:TagResources
        * tag:UntagResources
        * tag:getTagKeys
        * tag:getTagValues
        * iam:ListUserTags
        * iam:TagUser
        * iam:UntagUser
      </td>

      <td />

      <td>
        Enforcement Center Actions that start and stop EC2 instances.
        Enforcement Center Actions that manage tags on EC2 instances.
      </td>
    </tr>

    <tr>
      <td>
        IAM
      </td>

      <td>
        * iam:UpdateLoginProfile
        * iam:DeleteUser
        * iam:ListGroupsForUser
        * iam:RemoveUserFromGroup
        * iam:ListAccessKeys
        * iam:DeleteAccessKey
      </td>

      <td />

      <td>
        Enforcement Center Actions that manage IAM users.
      </td>
    </tr>

    <tr>
      <td>
        SSM
      </td>

      <td>
        * ssm:CreateAssociation
        * ssm:RegisterTaskWithMaintenanceWindow
      </td>

      <td />

      <td>
        Enforcement Center Actions that install and patch software using SSM.
      </td>
    </tr>
  </tbody>
</Table>

### Enforcement Center Permissions - JSON

<Accordion title="Expand/Collapse" icon="fa-info-circle">
  ```json
  {
  "Version": "2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutObject",
        "s3:ListAllMyBuckets",
        "s3:PutObjectTagging",
        "s3:DeleteObject",
        "ec2:StartInstances",
        "ec2:StopInstances",
        "tag:GetResources",
        "tag:TagResources",
        "tag:UntagResources",
        "tag:GetTagKeys",
        "tag:GetTagValues",
        "iam:ListUserTags",
        "iam:TagUser",
        "iam:UntagUser",
        "iam:UpdateLoginProfile",
        "iam:DeleteUser",
        "iam:ListGroupsForUser",
        "iam:RemoveUserFromGroup",
        "iam:ListAccessKeys",
        "iam:DeleteAccessKey",
        "ssm:CreateAssociation",
        "ssm:RegisterTaskWithMaintenanceWindow"
      ],
      "Resource":"*"
    }
  ]
  }
  ```
</Accordion>

## Cloud Asset Compliance Permissions

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        AWS Service
      </th>

      <th>
        Permissions
      </th>

      <th>
        Resource Scope
      </th>

      <th>
        Axonius Setting
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        CloudTrail
      </td>

      <td>
        * cloudtrail:DescribeTrails
        * cloudtrail:GetEventSelectors
        * cloudtrail:GetTrailStatus
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        Cloudwatch
      </td>

      <td>
        * cloudwatch:DescribeAlarmsForMetric
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        IAM
      </td>

      <td>
        * iam:GenerateCredentialReport
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        Config
      </td>

      <td>
        * config:DescribeConfigurationRecorderStatus
        * config:DescribeConfigurationRecorders
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        Logs
      </td>

      <td>
        * logs:DescribeMetricFilters
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        KMS
      </td>

      <td>
        * kms:ListKeys
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        EC2
      </td>

      <td>
        * ec2:DescribeInstances
        * ec2:GetEbsEncryptionByDefault
        * ec2:DescribeRouteTables
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        RDS
      </td>

      <td>
        * rds:DescribeDbInstances
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        Elastic File System
      </td>

      <td>
        * elasticfilesystem:DescribeFileSystems
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        Security Hub
      </td>

      <td>
        * DescribeHub
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>

    <tr>
      <td>
        SNS
      </td>

      <td>
        * sns:ListSubscriptionsByTopic
      </td>

      <td>
        * <br />
      </td>

      <td>
        Axonius Cloud Asset Compliance
      </td>
    </tr>
  </tbody>
</Table>

### Cloud Asset Compliance Permissions - JSON

<Accordion title="Expand/Collapse" icon="fa-info-circle">
  ```json
  {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CloudAssetCompliance",
      "Effect": "Allow",
      "Action": [
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetEventSelectors",
        "cloudtrail:GetTrailStatus",
        "cloudwatch:DescribeAlarmsForMetric",
        "iam:GenerateCredentialReport",
        "config:DescribeConfigurationRecorderStatus",
        "config:DescribeConfigurationRecorders",
        "logs:DescribeMetricFilters",
        "kms:ListKeys",
        "ec2:DescribeInstances",
        "ec2:GetEbsEncryptionByDefault",
        "ec2:DescribeRouteTables",
        "rds:DescribeDbInstances",
        "elasticfilesystem:DescribeFileSystems",
        "securityhub:DescribeHub",
        "sns:ListSubscriptionsByTopic"
      ],
      "Resource": "*"
    }
  ]
  }
  ```
</Accordion>

## Other Permissions

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        AWS Service
      </th>

      <th>
        Permissions
      </th>

      <th>
        Resource Scope
      </th>

      <th>
        Axonius Setting
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        S3 – Data Sync (Central Core)
      </td>

      <td>
        * kms:GenerateDataKey
        * kms:Decrypt
      </td>

      <td>
        Needs to be scoped to a specific key store that has been created for Axonius.
      </td>

      <td>
        Central Core
      </td>
    </tr>

    <tr>
      <td>
        S3 – AssumeRole Fetch
      </td>

      <td>
        * s3:GetObject
      </td>

      <td>
        Specific bucket and object that contains the roles-to-assume file.
      </td>

      <td>
        Advanced Configuration File setting: `remote_roles_to_assume`
      </td>
    </tr>

    <tr>
      <td>
        Secrets Manager – Vault
      </td>

      <td>
        * secretsmanager:GetSecretValue
      </td>

      <td>
        Can be scoped to all resources; however, Axonius recommends managing access to secrets within Secrets Manager through resource-based policies.
      </td>

      <td>
        Only needed if using AWS Secrets Manager as a Vault.
      </td>
    </tr>

    <tr>
      <td>
        SSM
      </td>

      <td>
        * ssm:CreateAssociation
        * ssm:RegisterTaskWithMaintenanceWindow
      </td>

      <td>
        * <br />
      </td>

      <td>
        EC Action for Install Software and Patches Instances
      </td>
    </tr>

    <tr>
      <td>
        STS
      </td>

      <td>
        * sts:AssumeRole
      </td>

      <td>
        Should be scoped to roles utilized by Axonius as a part of our Roles-to-Assume / Organizations Discovery implementation.
      </td>

      <td>
        Roles to Assume
      </td>
    </tr>
  </tbody>
</Table>

### Other Permissions - JSON

<Accordion title="Expand/Collapse" icon="fa-info-circle">
  ```json
  {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "OtherPermissions",
      "Effect": "Allow",
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "s3:GetObject",
        "secretsmanager:GetSecretValue",
        "ssm:CreateAssociation",
        "ssm:RegisterTaskWithMaintenanceWindow",
        "sts:AssumeRole"
      ],
      "Resource": "*"
    }
  ]
  }
  ```
</Accordion>