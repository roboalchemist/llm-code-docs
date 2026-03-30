# Source: https://docs.aws.amazon.com/controltower/latest/controlreference/llms.txt

# AWS Control Tower Controls Reference Guide

> Describes key concepts and reference pages for working with Control Tower controls to create a secure and compliant multi-account environment for enterprises or organizations at scale.

- [Introduction](https://docs.aws.amazon.com/controltower/latest/controlreference/introduction.html)
- [Control API examples](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html)
- [Enable controls with CloudFormation](https://docs.aws.amazon.com/controltower/latest/controlreference/enable-controls.html)
- [Tags for enabled controls](https://docs.aws.amazon.com/controltower/latest/controlreference/tagging.html)
- [Control availability tables by Region](https://docs.aws.amazon.com/controltower/latest/controlreference/control-region-tables.html)
- [Control metadata tables](https://docs.aws.amazon.com/controltower/latest/controlreference/control-metadata-tables.html)
- [All global identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/all-global-identifiers.html)
- [Document history](https://docs.aws.amazon.com/controltower/latest/controlreference/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/controltower/latest/controlreference/glossary.html)

## [About controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)

- [About control relationships](https://docs.aws.amazon.com/controltower/latest/controlreference/control-relationships.html): Certain controls stand in specified relationships to each other.
- [Controls that have non-deployable Regions](https://docs.aws.amazon.com/controltower/latest/controlreference/non-deployable.html): This section lists controls that are not activated when deployed in certain Regions, due to lack of underlying dependencies.
- [Control behavior and guidance](https://docs.aws.amazon.com/controltower/latest/controlreference/control-behavior.html): Controls are categorized according to their behavior and their guidance.
- [Considerations for controls and OUs](https://docs.aws.amazon.com/controltower/latest/controlreference/control-considerations.html): When working with controls and OUs, consider the following properties:
- [Exception to controls for the Security OU](https://docs.aws.amazon.com/controltower/latest/controlreference/exception-to-controls-security-ou.html): For customers on LZ v4.0:
- [Considerations for controls and accounts](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-and-accounts.html): When working with controls and accounts, consider the following properties:
- [Common controls](https://docs.aws.amazon.com/controltower/latest/controlreference/common-controls-list.html): This page provides an overview and a partial list of the common controls available for the Control Catalog.
- [Control objectives](https://docs.aws.amazon.com/controltower/latest/controlreference/control-catalog-objectives.html): This document gives details about the control objectives from the AWS Control Tower Control Catalog.
- [Legacy control objectives](https://docs.aws.amazon.com/controltower/latest/controlreference/list-of-control-objectives.html)
- [Frameworks supported](https://docs.aws.amazon.com/controltower/latest/controlreference/frameworks-supported.html): The controls available in Control Catalog support several industry frameworks.
- [View control details](https://docs.aws.amazon.com/controltower/latest/controlreference/control-details.html): You can view control details in the AWS Control Tower console or retrieve them programmatically using Control Catalog APIs.
- [View enabled controls](https://docs.aws.amazon.com/controltower/latest/controlreference/view-enabled-controls.html): To view your enabled controls in the AWS Control Tower console, navigate to the Enabled Controls page by selecting it from the left navigation pane.


## [Resource identifiers for APIs and controls](https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers.html)

- [Legacy control identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/identifiers-for-legacy-controls.html): The following section contains the Regional API controlIdentifier designations of the legacy Strongly recommended and Elective, preventive and detective, controls that are owned by AWS Control Tower, including the elective Data residency controls.
- [Non-API controls](https://docs.aws.amazon.com/controltower/latest/controlreference/cannot-change-with-gr-api.html): The following controls cannot be activated or deactivated by means of the AWS Control Tower APIs.


## [Control Catalog by category](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html)

- [Mandatory controls](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html): Mandatory controls are owned by AWS Control Tower, and they apply to every OU on your landing zone, with some exceptions for the Security OU.

### [Proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html)

A section about optional controls called proactive controls.

- [Update hooks](https://docs.aws.amazon.com/controltower/latest/controlreference/get-new-hooks.html): Learn how to update your proactive control hooks in AWS Control Tower
- [Amazon API Gateway controls](https://docs.aws.amazon.com/controltower/latest/controlreference/api-gateway-rules.html): A section about proactive controls for Amazon API Gateway and how the contols can be used, including details and examples.
- [AWS Certificate Manager controls](https://docs.aws.amazon.com/controltower/latest/controlreference/acm-rules.html): A section about the proactive controls for AWS Certificate Manager and how the controls can be used, including details and examples.
- [AWS AppSync controls](https://docs.aws.amazon.com/controltower/latest/controlreference/appsync-rules.html)
- [Amazon Athena controls](https://docs.aws.amazon.com/controltower/latest/controlreference/athena-rules.html)
- [Amazon CloudFront controls](https://docs.aws.amazon.com/controltower/latest/controlreference/cloudfront-rules.html): A section about the proactive controls for Amazon CloudFront and how the controls can be used, including details and examples.
- [AWS CloudTrail controls](https://docs.aws.amazon.com/controltower/latest/controlreference/cloudtrail-rules.html): A section about the proactive controls for AWS CloudTrail and how the controls can be used, including details and examples.
- [Amazon CloudWatch controls](https://docs.aws.amazon.com/controltower/latest/controlreference/cloudwatch-rules.html): A section about the proactive controls for Amazon CloudWatch and how the controls can be used, including details and examples.
- [AWS CodeBuild controls](https://docs.aws.amazon.com/controltower/latest/controlreference/codebuild-rules.html): A section about the proactive controls for AWS CodeBuild and how the controls can be used, including details and examples.
- [AWS Database Migration Service (AWS DMS) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/dms-rules.html): A section about the proactive controls for AWS Database Migration Service and how the controls can be used, including details and examples.
- [Amazon DocumentDB controls](https://docs.aws.amazon.com/controltower/latest/controlreference/documentdb-rules.html)
- [Amazon DynamoDB controls](https://docs.aws.amazon.com/controltower/latest/controlreference/dynamodb-rules.html): A section about the proactive controls for Amazon DynamoDB and how the controls can be used, including details and examples.
- [DynamoDB Accelerator controls](https://docs.aws.amazon.com/controltower/latest/controlreference/dax-rules.html): A section about the proactive controls for DynamoDB Accelerator and how the controls can be used, including details and examples.
- [AWS Elastic Beanstalk controls](https://docs.aws.amazon.com/controltower/latest/controlreference/ebs-rules.html): A section about the proactive controls for AWS Elastic Beanstalk and how the controls can be used, including details and examples.
- [Amazon Elastic Compute Cloud (Amazon EC2) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/ec2-rules.html): A section about the proactive controls for Amazon Elastic Compute Cloud and how the controls can be used, including details and examples.
- [Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling controls](https://docs.aws.amazon.com/controltower/latest/controlreference/ec2-auto-scaling-rules.html)
- [Amazon ElastiCache controls](https://docs.aws.amazon.com/controltower/latest/controlreference/elasticache-rules.html): A section about the proactive controls for Amazon ElastiCache and how the controls can be used, including details and examples.
- [Amazon Elastic Container Registry controls](https://docs.aws.amazon.com/controltower/latest/controlreference/ecr-rules.html): A section about the proactive controls for Amazon Elastic Container Registry and how the controls can be used, including details and examples.
- [Amazon Elastic Container Service controls](https://docs.aws.amazon.com/controltower/latest/controlreference/ecs-rules.html): A section about the proactive controls for Amazon Elastic Container Service and how the controls can be used, including details and examples.
- [Amazon Elastic File System controls](https://docs.aws.amazon.com/controltower/latest/controlreference/efs-rules.html): A section about the proactive controls for Amazon Elastic File System and how the controls can be used, including details and examples.
- [Amazon Elastic Kubernetes Service (EKS) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/eks-rules.html)
- [Elastic Load Balancing controls](https://docs.aws.amazon.com/controltower/latest/controlreference/elb-rules.html): A section about the proactive controls for Elastic Load Balancing and how the controls can be used, including details and examples.
- [Amazon Elastic Map Reduce (Amazon EMR) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/emr-rules.html): A section about the proactive controls for Amazon EMR and how the controls can be used, including details and examples.
- [AWS Glue controls](https://docs.aws.amazon.com/controltower/latest/controlreference/glue-rules.html): A section about the proactive controls for AWS Glue and how the controls can be used, including details and examples.
- [Amazon GuardDuty controls](https://docs.aws.amazon.com/controltower/latest/controlreference/guard-duty-rules.html): A section about the proactive controls for Amazon GuardDuty and how the controls can be used, including details and examples.
- [AWS Identity and Access Management (IAM) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/iam-rules.html): A section about the proactive controls for AWS Identity and Access Management and how the controls can be used, including details and examples.
- [AWS Key Management Service (AWS KMS) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/kms-rules.html): A section about the proactive controls for AWS Key Management Service and how the controls can be used, including details and examples.
- [Amazon Kinesis controls](https://docs.aws.amazon.com/controltower/latest/controlreference/kinesis-rules.html): A section about the proactive controls for Amazon Kinesis and how the controls can be used, including details and examples.
- [AWS Lambda controls](https://docs.aws.amazon.com/controltower/latest/controlreference/lambda-rules.html): A section about the proactive controls for AWS Lambda and how the controls can be used, including details and examples.
- [Amazon MQ controls](https://docs.aws.amazon.com/controltower/latest/controlreference/mq-rules.html)
- [Amazon Managed Streaming for Apache Kafka (Amazon MSK) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/msk-rules.html)
- [Amazon Neptune controls](https://docs.aws.amazon.com/controltower/latest/controlreference/neptune-rules.html)
- [AWS Network Firewall controls](https://docs.aws.amazon.com/controltower/latest/controlreference/network-firewall-rules.html): A section about the proactive controls for AWS Network Firewall and how the controls can be used, including details and examples.
- [Amazon OpenSearch controls](https://docs.aws.amazon.com/controltower/latest/controlreference/opensearch-rules.html)
- [Amazon Relational Database Service (Amazon RDS) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/rds-rules.html): A section about the proactive controls for Amazon Relational Database Service and how the controls can be used, including details and examples.
- [Amazon Redshift controls](https://docs.aws.amazon.com/controltower/latest/controlreference/redshift-rules.html): A section about the proactive controls for Amazon Relational Database Service and how the controls can be used, including details and examples.
- [Amazon Simple Storage Service (Amazon S3) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/s3-rules.html): A section about the proactive controls for Amazon Simple Storage Service and how the controls can be used, including details and examples.
- [Amazon SageMaker AI controls](https://docs.aws.amazon.com/controltower/latest/controlreference/sagemaker-rules.html)
- [Amazon Simple Queue Service (Amazon SQS) controls](https://docs.aws.amazon.com/controltower/latest/controlreference/sqs-rules.html): A section about the proactive controls for Amazon Simple Queue Service and how the controls can be used, including details and examples.
- [AWS Step Functions controls](https://docs.aws.amazon.com/controltower/latest/controlreference/stepfunctions-rules.html)
- [AWS WAF regional controls](https://docs.aws.amazon.com/controltower/latest/controlreference/waf-regional-rules.html): A section about the regional controls for AWS WAF and how the controls can be used, including details and examples.
- [AWS WAF controls](https://docs.aws.amazon.com/controltower/latest/controlreference/waf-rules.html): A section about the proactive controls for AWS WAF and how the controls can be used, including details and examples.
- [AWS WAFV2 controls](https://docs.aws.amazon.com/controltower/latest/controlreference/wafv2-rules.html): A section about the proactive controls for AWS WAFV2 and how the controls can be used, including details and examples.

### [Preventive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/preventive-controls.html)

A preventive control ensures that your accounts maintain compliance, because it disallows actions that lead to policy violations.

### [About RCP controls](https://docs.aws.amazon.com/controltower/latest/controlreference/rcp-controls.html)

This section provides information about AWS Control Tower controls that are implemented by resource control policies (RCPs).

- [RCP controls](https://docs.aws.amazon.com/controltower/latest/controlreference/list-of-rcp-controls.html): AWS Control Tower offers multiple RCP-based controls that each focus on a single type of resource associated with a specific service, such as Amazon S3 buckets.

### [Declarative policies](https://docs.aws.amazon.com/controltower/latest/controlreference/declarative-controls.html)

This section provides information about AWS Control Tower controls that are implemented by declarative policies from AWS Organizations.

- [CT.EC2.PV.7](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-7.html): This control blocks the public sharing of your Amazon EBS snapshots by configuring block public access for Amazon EBS snapshot settings at an account level.
- [CT.EC2.PV.8](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-8.html): This control blocks direct ingress and egress traffic from the internet to your VPCs through an IGW or EIGW, by configuring block public access for VPCs (VPC BPA) at an account level.
- [CT.EC2.PV.9](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-9.html): This control prevents access to the Amazon EC2 serial console of all EC2 instances for your account.
- [CT.EC2.PV.11](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-11.html): This control prevents the public sharing of your AMIs by configuring block public access for AMIs at an account level.

### [Controls for AWS Backup](https://docs.aws.amazon.com/controltower/latest/controlreference/backup-controls.html)

When you enable AWS Backup in your AWS Control Tower landing zone, some preventive controls are activated in your environment.

- [CT.BACKUP.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-backup-pv-1.html): This control limits changes to tags that AWS Control Tower applies to AWS Backup resources.
- [CT.BACKUP.PV.2](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-backup-pv-2.html): This control limits changes to the AWS Backup report plan that AWS Control Tower manages.
- [CT.BACKUP.PV.3](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-backup-pv-3.html): This control limits creation or modification of AWS Backup resources that AWS Control Tower manages.
- [CT.IAM.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-iam-pv-1.html): This control limits modification of the AWS IAM role (aws-controltower-BackupRole) that AWS Control Tower utilizes for management of AWS Backup resources.
- [CT.S3.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-s3-pv-1.html): This control limits modification of the Amazon S3 buckets that AWS Control Tower utilizes as a destination for storing AWS Backup reports.

### [Digital sovereignty group](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html)

Digital sovereignty means control over digital assets.

- [Landing zone region deny](https://docs.aws.amazon.com/controltower/latest/controlreference/primary-region-deny-policy.html): This control is commonly referred to as the Region deny control, or landing zone Region deny control.
- [Region deny for OU](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html): This control is commonly referred to as the OU Region deny control, or the configurable Region deny control.

### [Digital sovereignty preventive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/ds-preventive-controls.html)

These preventive controls are designed to assist you with your digital sovereignty governance posture.

- [CT.APPSYNC.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-appsync-pv-1.html): This control disallows creation of public AWS AppSync APIs by requiring APIs to be configured with private visibility.
- [CT.EC2.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-1.html): This control disallows creation of new snapshots that are based on unencrypted EBS volumes.
- [CT.EC2.PV.2](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-2.html): This control disallows attaching an unencrypted EBS volume to a running or stopped EC2 instance.
- [CT.EC2.PV.3](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-3.html): This control disallows sharing of an EBS snapshot with all AWS accounts.
- [CT.EC2.PV.4](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-4.html): This control disallows usage of all EBS direct APIs.
- [CT.EC2.PV.5](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-5.html): This control disallows use of EC2 VM Import/Export APIs that can be used to import and export EC2 instance, snapshot, image and volume data.
- [CT.EC2.PV.6](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-ec2-pv-6.html): This control disallows usage of EC2 RequestSpotFleet and RequestSpotInstances APIs, because they are legacy APIs with no planned investment.
- [CT.KMS.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-1.html): This control requires that KMS grants are issued only to AWS services that are integrated with AWS KMS, or to an AWS service principal.
- [CT.KMS.PV.2](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-2.html): This control disallows the creation of KMS keys used for encryption and decryption that also have a key spec of RSA_2048.
- [CT.KMS.PV.3](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-3.html): This control disallows bypassing the KMS key policy lockout safety check when creating a KMS key or updating its key policy.
- [CT.KMS.PV.4](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-4.html): This control disallows creation of KMS keys that do not have a key origin of AWS_CLOUDHSM.
- [CT.KMS.PV.5](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-5.html): This control disallows creation of KMS keys that do not have a key origin of EXTERNAL.
- [CT.KMS.PV.6](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-kms-pv-6.html): This control disallows creation of KMS keys that do not have a key origin of EXTERNAL_KEY_STORE.
- [CT.LAMBDA.PV.1](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-lambda-pv-1.html): Require an AWS Lambda function URL to restrict access to authenticated users by using AWS_IAM based authentication.
- [CT.LAMBDA.PV.2](https://docs.aws.amazon.com/controltower/latest/controlreference/ct-lambda-pv-2.html): This control requires an AWS Lambda function resource-based policy to grant access only to IAM principals that reside in your AWS account.

### [Data residency controls](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-controls.html)

These elective controls complement your enterprise's data residency posture.

- [Data residency preventive](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-preventive-controls.html): The following data residency controls have preventive behavior.
- [Data residency detective](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-detective-controls.html): The following data residency controls have detective behavior.

### [Detective controls](https://docs.aws.amazon.com/controltower/latest/controlreference/detective-controls.html)

A detective control detects noncompliance of resources within your accounts, such as policy violations, and provides alerts through the dashboard.

- [The Security Hub CSPM standard](https://docs.aws.amazon.com/controltower/latest/controlreference/security-hub-controls.html): AWS Control Tower is integrated with AWS Security Hub CSPM to provide detective controls that help you monitor your AWS environment.
- [AWS Config controls](https://docs.aws.amazon.com/controltower/latest/controlreference/config-controls.html): AWS Control Tower is integrated with AWS Config to provide over 500 selected additional detective controls that help you monitor and manage your AWS environment.
- [Parameterized controls](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html): In AWS Control Tower, RCP-based and certain SCP-based controls support configuration.
- [Optional controls](https://docs.aws.amazon.com/controltower/latest/controlreference/optional-controls.html): Optional controls in AWS Control Tower are applied at the OU level.

### [Strongly recommended controls](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-controls.html)

Strongly recommended controls are owned by AWS Control Tower.

- [Strongly recommended preventive](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-preventive-controls.html): The following strongly recommended controls have preventive behavior.
- [Strongly recommended detective](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-detective-controls.html): The following strongly recommended controls have detective behavior.

### [Elective controls](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-controls.html)

Elective controls enable you to lock down or track attempts at performing commonly restricted actions in an AWS enterprise environment.

- [Elective detective controls](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-detective-controls.html): The following elective controls have detective behavior.
- [Elective preventive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-preventive-controls.html): The following elective controls have preventive behavior.
- [Q search for controls](https://docs.aws.amazon.com/controltower/latest/controlreference/q-search.html): A section about using Amazon Q to help you find controls.


## [Controls and compliance](https://docs.aws.amazon.com/controltower/latest/controlreference/compliance.html)

- [How can administrators review compliance?](https://docs.aws.amazon.com/controltower/latest/controlreference/review-compliance.html): Compliance with detective controls is determined according to data retrieved from the AWS Config aggregator in the AWS Control Tower Audit account.
- [Compliance status in the console](https://docs.aws.amazon.com/controltower/latest/controlreference/compliance-statuses.html): Compliance is reported in the AWS Control Tower dashboard for accounts and OUs.
- [Drift prevention and notification](https://docs.aws.amazon.com/controltower/latest/controlreference/prevention-and-notification.html): You can enable certain controls and subscribe to certain SNS notifications that help you maintain compliance in AWS Control Tower.
- [Compliance notifications by SNS and email](https://docs.aws.amazon.com/controltower/latest/controlreference/receive-notifications.html)
