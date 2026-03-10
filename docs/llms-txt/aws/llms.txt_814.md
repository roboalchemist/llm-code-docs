# Source: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/llms.txt

# AWS Systems Manager Automation Runbook Reference User Guide

> AWS Systems Manager Automation simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. This reference includes AWS provided runbooks to help you complete common tasks for various AWS services and third-party softwares.

## [Automation Runbook Reference](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.html)

### [API Gateway](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-abp.html)

The following runbooks complete various Amazon API Gateway (API Gateway) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-DeleteAPIGatewayStage](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-apigw-stage.html): Delete an Amazon API Gateway (API Gateway) stage.
- [AWSConfigRemediation-EnableAPIGatewayTracing](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-apigw-tracing.html): Enable tracing on an Amazon API Gateway (API Gateway) stage.
- [AWSConfigRemediation-UpdateAPIGatewayMethodCaching](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-update-api-gateway.html): Update the cache method setting for method for an Amazon API Gateway stage resource.
- [AWSSupport-TroubleshootAPIGatewayHttpErrors](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootapigatewayhttp-errors.html): Troubleshoots 5XX/4XX errors when invoking a deployed Amazon API Gateway REST API.

### [AWS Batch](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-batch.html)

The following runbooks complete various AWS Batch tasks with AWS Systems Manager Automation.

- [AWSSupport-TroubleshootAWSBatchJob](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-aws-batch-job.html): Automate troubleshooting of AWS Batch jobs.

### [CloudFormation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-cfn.html)

The following runbooks complete various AWS CloudFormation (CloudFormation) tasks with AWS Systems Manager Automation.

- [AWS-DeleteCloudFormationStack](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletecloudformationstack.html): Delete an CloudFormation stack.
- [AWS-EnableCloudFormationSNSNotification](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableCloudFormationStackSNSNotification.html): Enable Amazon SNS notifications for a CloudFormation stack.
- [AWS-RunCfnLint](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-runcfnlint.html): Use a AWS CloudFormation Linter to validate YAML and JSON templates against the CloudFormation resource specification.
- [AWSSupport-TroubleshootCFNCustomResource](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-TroubleshootCFNCustomResource.html): Troubleshoot a CloudFormation stack that failed because of a custom resource.
- [AWS-UpdateCloudFormationStack](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-updatecloudformationstack.html): Update an AWS CloudFormation stack by using an CloudFormation template stored in an Amazon S3 bucket.

### [CloudFront](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-cf.html)

The following runbooks complete various Amazon CloudFront (CloudFront) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-EnableCloudFrontDefaultRootObject](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-root-object.html): Configures the default root object for the Amazon CloudFront distribution you specify.
- [AWSConfigRemediation-EnableCloudFrontAccessLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-access-logs.html): Enables access logging for the Amazon CloudFront (CloudFront) distribution you specify.
- [AWSConfigRemediation-EnableCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-origin-access.html): Enables origin access identity for the Amazon CloudFront (CloudFront) distribution you specify.
- [AWSConfigRemediation-EnableCloudFrontOriginFailover](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-failover.html): Enables origin failover for the Amazon CloudFront (CloudFront) distribution you specify.
- [AWSConfigRemediation-EnableCloudFrontViewerPolicyHTTPS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-viewer-policy.html): Enables the viewer protocol policy for the Amazon CloudFront (CloudFront) distribution you specify.

### [CloudTrail](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ct.html)

The following runbooks complete various AWS CloudTrail (CloudTrail) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-CreateCloudTrailMultiRegionTrail](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-create-ct-mr.html): Create a CloudTrail trail that delivers log files from multiple AWS Regions to an Amazon S3 bucket.
- [AWS-EnableCloudTrail](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enablecloudtrail.html): Create an AWS CloudTrail trail and configure logging to an S3 bucket.
- [AWS-EnableCloudTrailCloudWatchLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-cloudtrail-cloudwatch-logs.html): Update the configuration of one or more CloudTrail trails to send events to a CloudWatch Logs log group.
- [AWSConfigRemediation-EnableCloudTrailEncryptionWithKMS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-ctrail-kms.html): Update a CloudTrail trail to be encrypted using a AWS KMS customer managed key.
- [AWS-EnableCloudTrailKmsEncryption](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-cloudtrail-kms-encryption.html): Update a CloudTrail trail to be encrypted using a AWS KMS customer managed key.
- [AWSConfigRemediation-EnableCloudTrailLogFileValidation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-ctrail-log-validation.html): Enable log file validation for your AWS CloudTrail trail.
- [AWS-EnableCloudTrailLogFileValidation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-cloudtrail-log-validation.html): Enable log file validation for your AWS CloudTrail trails.
- [AWS-QueryCloudTrailLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-querycloudtraillogs.html): Creates an Amazon Athena table of CloudTrail logs to query.

### [CloudWatch](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-cw.html)

The following runbooks complete various Amazon CloudWatch (CloudWatch) tasks with AWS Systems Manager Automation.

- [AWS-ConfigureCloudWatchOnEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configurecloudwatchonec2instance.html): Enable or disable Amazon CloudWatch detailed monitoring on managed instances.
- [AWS-EnableCWAlarm](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-cw-alarm.html): Create Amazon CloudWatch alarms for AWS resources.
- [AWSSupport-TroubleshootCloudWatchAgent](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootcloudwatchagent.html): Automates troubleshooting the Amazon CloudWatch Agent on your Amazon Elastic Compute Cloud instances.
- [AWSSupport-TroubleshootCloudWatchAlarm](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-cloudwatchalarm.html): Troubleshoot Amazon CloudWatch Alarm

### [Amazon DocumentDB](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-docdb.html)

The following runbooks complete various Amazon DocumentDB (with MongoDB compatibility) (Amazon DocumentDB) tasks with AWS Systems Manager Automation.

- [AWS-EnableDocDbClusterBackupRetentionPeriod](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enabledocdbclusterbackupretentionperiod.html): Enable a backup retention period for an Amazon DocumentDB cluster.

### [CodeBuild](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-acb.html)

The following runbooks complete various AWS CodeBuild (CodeBuild) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-ConfigureCodeBuildProjectWithKMSCMK](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-codebuild-cmk.html): Encrypt your AWS CodeBuild (CodeBuild) project's build artifacts using a AWS Key Management Service (AWS KMS) customer managed key.
- [AWSConfigRemediation-DeleteAccessKeysFromCodeBuildProject](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-cb-keys.html): Delete the access key environment variables from the AWS CodeBuild (CodeBuild) project you specify.

### [AWS CodeDeploy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-acd.html)

The following runbooks complete various CodeDeploy tasks with AWS Systems Manager Automation.

- [AWSSupport-TroubleshootCodeDeploy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootcodedeploy.html): Troubleshoot a failed CodeDeploy deployment

### [AWS Config](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-cc.html)

The following runbooks complete various AWS Config tasks with AWS Systems Manager Automation.

- [AWSSupport-SetupConfig](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-setup-config.html): Setup AWS Config for your AWS account.

### [Amazon Connect](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-con.html)

The following runbooks complete various Amazon Connect tasks with AWS Systems Manager Automation.

- [AWSSupport-AssociatePhoneNumbersToConnectContactFlows](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-associate-phone-numbers-to-connect-contact-flows.html): Automate association of phone numbers and Amazon Connect Contact Flows
- [AWSSupport-CollectAmazonConnectContactFlowLog](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-collect-amazon-connect-contact-flow-log.html): Automate collecting Amazon Connect Contact Flow Logs

### [AWS Directory Service](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ads.html)

The following runbooks complete various AWS Directory Service tasks with AWS Systems Manager Automation.

- [AWS-CreateDSManagementInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-create-ds-management-instance.html): Create an Amazon EC2 Windows instance to manage your AWS Directory Service directory.
- [AWSSupport-TroubleshootADConnectorConnectivity](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootadconnectorconnectivity.html): Performs connectivity tests required for an AD Connector.
- [AWSSupport-TroubleshootDirectoryTrust](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootdirectorytrust.html): Diagnose trust creation issues between an AWS Managed Microsoft AD and a Microsoft Active Directory.

### [AWS AppSync](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-apsy.html)

The following runbooks complete various AWS AppSync tasks with AWS Systems Manager Automation.

- [AWS-EnableAppSyncGraphQLApiLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enable-appsync-graphql-api-logging.html): Enable field-level logging and request-level logging on the specified AWS AppSync GraphQL API.

### [Amazon Athena](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ate.html)

The following runbooks complete various Amazon Athena tasks with AWS Systems Manager Automation.

- [AWS-EnableAthenaWorkGroupEncryptionAtRest](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enable-athena-workgroup-encryption-at-rest.html): Enable encryption at rest for Athena workgroup.

### [DynamoDB](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ddb.html)

The following runbooks complete various Amazon DynamoDB (DynamoDB) tasks with AWS Systems Manager Automation.

- [AWS-ChangeDDBRWCapacityMode](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/change-read-write-capacity.html): Change the read/write capacity mode of Amazon DynamoDB tables.
- [AWS-CreateDynamoDBBackup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createdynamodbbackup.html): Create a backup of an Amazon DynamoDB table.
- [AWS-DeleteDynamoDbBackup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletedynamodbbackup.html): Delete the backup of a DynamoDB table.
- [AWSConfigRemediation-DeleteDynamoDbTable](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletedynamodbtable.html): Description
- [AWS-DeleteDynamoDbTableBackups](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletedynamodbtablebackups.html): Delete DynamoDB table backups based on retention days or count.
- [AWSConfigRemediation-EnableEncryptionOnDynamoDbTable](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-ddb-encrypt.html): Encrypt a DynamoDB table using the AWS KMS customer managed key you specify for the KMSKeyId parameter.
- [AWSConfigRemediation-EnablePITRForDynamoDbTable](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-pitr-ddb.html): Enable point-in-time recovery on the DynamoDB table you specify.
- [AWS-EnableDynamoDbAutoscaling](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableDynamoDbAutoscaling.html): Enable Application Auto Scaling for a DynamoDB table.
- [AWS-RestoreDynamoDBTable](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-restore-dynamodb-table.html): Restore the DynamoDB table that you specify using point-in-time recovery.

### [AWS Database Migration Service](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-dms.html)

AWS Systems Manager Automation provides predefined runbooks for AWS Database Migration Service.

- [AWSSupport-TroubleshootDMSTableErrors](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-troubleshoot-dms-table-errors.html): Automate troubleshooting process of Table errors found in Database migration tasks (or) Serverless Replications.
- [AWSSupport-TroubleshootDMSEndpointConnection](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootdmsendpointconnection.html): The AWSSupport-TroubleshootDMSEndpointConnection automation runbook assists you troubleshoot connectivity issues between AWS Database Migration Service replication instances and AWS DMS endpoints.

### [Amazon EBS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ebs.html)

The following runbooks complete various Amazon Elastic Block Store (Amazon EBS) tasks with AWS Systems Manager Automation.

- [AWSSupport-AnalyzeEBSResourceUsage](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-analyze-ebs-resource-usage.html): Automate analysis of Amazon EBS resource usage.
- [AWS-ArchiveEBSSnapshots](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-archiveebssnapshots.html): Archive snapshots of an Amazon EBS volume.
- [AWS-AttachEBSVolume](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-attachebsvolume.html): Attach an Amazon EBS volume to an Amazon EC2 instance.
- [AWSSupport-CalculateEBSPerformanceMetrics](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-calculate-ebs-performance-metrics.html): The AWSSupport-CalculateEBSPerformanceMetrics runbook helps diagnose Amazon Elastic Block Store (Amazon EBS) performance issues by calculating metrics and publishes them to Amazon CloudWatch.
- [AWS-CopySnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-copysnapshot.html): Copy a point-in-time snapshot of an Amazon EBS volume.
- [AWS-CreateSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createsnapshot.html): Create a snapshot of an Amazon EBS volume.
- [AWS-DeleteSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletesnapshot.html): Delete a snapshot of an Amazon EBS volume.
- [AWSConfigRemediation-DeleteUnusedEBSVolume](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-ebs-volume.html): Delete an unused Amazon Elastic Block Store (Amazon EBS) volume.
- [AWS-DeregisterAMIs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-deregisteramis.html): Deregister AMIs.
- [AWS-DetachEBSVolume](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-detachebsvolume.html): Detach an Amazon EBS volume from an Amazon EC2 instance.
- [AWSConfigRemediation-EnableEbsEncryptionByDefault](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-ebs-encryption.html): Enable encryption on all new Amazon EBS volumes in the AWS account and AWS Region where you run automations.
- [AWS-ExtendEbsVolume](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-extendebsvolume.html): Increase the size of an Amazon EBS volume and extend the file system.
- [AWSSupport-ModifyEBSSnapshotPermission](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-modifyebssnapshotpermission.html): Modify permissions for multiple Amazon EBS snapshots.
- [AWSConfigRemediation-ModifyEBSVolumeType](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-ebs-type.html): Modify the volume type of an Amazon EBS volume.

### [Amazon EC2](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ec2.html)

The following runbooks complete various Amazon Elastic Compute Cloud (Amazon EC2) tasks with AWS Systems Manager Automation.

- [AWS-ASGEnterStandby](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-asgenterstandby.html): Change the standby state of an Amazon EC2 instance in an Auto Scaling group.
- [AWS-ASGExitStandby](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-asgexitstandby.html): Change the standby state of an Amazon EC2 instance in an Auto Scaling group.
- [AWS-CreateImage](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.html): Create a new AMI from an EC2 instance.
- [AWS-DeleteImage](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deleteimage.html): Delete an AMI and all associated snapshots.
- [AWS-PatchAsgInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-patchasginstance.html): Patch EC2 instances in an Auto Scaling group.
- [AWS-PatchInstanceWithRollback](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-patchinstancewithrollback.html): Bring an EC2 instance into compliance with the applicable patch baseline.
- [AWS-QuarantineEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-quarantineec2instance.html): Assign a security group to an Amazon EC2 instance that doesn't allow any inbound or outbound traffic.
- [AWS-ResizeInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-resizeinstance.html): Change the instance type of an Amazon EC2 instance.
- [AWS-RestartEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-restartec2instance.html): Restart one or more Amazon EC2 instances.
- [AWS-SetupJupyter](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-setup-jupyter.html): Set up Jupyter Notebook on an Amazon EC2 instance.
- [AWS-StartEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-startec2instance.html): Start one or more Amazon EC2 instances.
- [AWS-StopEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-stopec2instance.html): Stops one or more Amazon EC2 instances.
- [AWS-TerminateEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-terminateec2instance.html): Terminate one or more Amazon EC2 instances.
- [AWS-UpdateLinuxAmi](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-updatelinuxami.html): Update an AMI with Linux distribution packages and Amazon software.
- [AWS-UpdateWindowsAmi](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-updatewindowsami.html): Update a Microsoft Windows AMI.
- [AWSConfigRemediation-EnableAutoScalingGroupELBHealthCheck](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-asg-health-check.html): Enable health checks for the auto scaling group you specify.
- [AWSConfigRemediation-EnforceEC2InstanceIMDSv2](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enforce-ec2-imdsv2.html): Require an Amazon Elastic Compute Cloud (Amazon EC2) instance to use Instance Metadata Service Version 2 (IMDSv2).
- [AWSEC2-CloneInstanceAndUpgradeSQLServer](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeSQLServer.html): Create an AMI from an EC2 instance for Windows Server running SQL Server 2008 or later, and then upgrade the AMI to a later version of SQL Server.
- [AWSEC2-CloneInstanceAndUpgradeWindows](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeWindows.html): Create an AMI from a Windows Server 2008 R2, 2012 R2, 2016, or 2019 instance, and then upgrade the AMI to Windows Server 2016, 2019, or 2022.
- [AWSEC2-PatchLoadBalancerInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-patch-load-balancer-instance.html): Upgrade and patch minor versions of an Amazon EC2 instance (Windows or Linux) attached to any load balancer (classic, ALB, or NLB).
- [AWSEC2-SQLServerDBRestore](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-sqlserverdbrestore.html): Restore Microsoft SQL Server database backups stored in Amazon S3 to SQL Server 2017 running on an Amazon EC2 Linux instance.
- [AWSSupport-ActivateWindowsWithAmazonLicense](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-activatewindowswithamazonlicense.html): Activate an EC2 instance for Windows Server and verify and configure required key management service operating system settings.
- [AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-analyzeawsendpointreachabilityfromec2.html): Analyze connectivity from an Amazon EC2 instance or elastic network interface to an AWS service endpoint using Reachability Analyzer.
- [AWSPremiumSupport-ChangeInstanceTypeIntelToAMD](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-changeinstancetypeinteltoamd.html): Automate migrations from Intel powered Amazon EC2 instances to the equivalent AMD powered instance types.
- [AWSSupport-CheckXenToNitroMigrationRequirements](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-checkxentonitromigrationrequirements.html): Checks whether a Xen type Amazon EC2 instance meets the prerequisites to change to a Nitro-based instance type.
- [AWSSupport-CloneXenEC2InstanceAndMigrateToNitro](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-clonexenec2instanceandmigratetonitro.html): Clones, prepares and migrates an Amazon EC2 Linux instance from Xen platform to Nitro platform.
- [AWSSupport-ConfigureEC2Metadata](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-configureec2metadata.html): Configure instance metadata service options for Amazon EC2 instances.
- [AWSSupport-ContainEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-containec2instance.html): Isolate an Amazon Elastic Compute Cloud (Amazon EC2); instance from network activity while leaving it running.
- [AWSSupport-CopyEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-copyec2instance.html): Copies an Amazon EC2 instance to another subnet or AWS Region.
- [AWSPremiumSupport-DiagnoseDiskUsageOnLinux](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awspremiumsupport-diagnosediskusageonlinux.html): Analyzes Amazon EBS volumes on a Linux Amazon EC2 instance to determine if they require expansion.
- [AWSSupport-EnableWindowsEC2SerialConsole](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-enable-windows-ec2-serial-console.html): Automate enabling of Windows Amazon EC2 Serial Console.
- [AWSPremiumSupport-ExtendVolumesOnWindows](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awspremiumsupport-extendvolumesonwindows.html): Extends Amazon EBS volumes, their partitions, and filesystems on a target Amazon EC2 instance running Windows Server.
- [AWSSupport-ExecuteEC2Rescue](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-executeec2rescue.html): Use the EC2Rescue tool to troubleshoot and repair common connectivity issues with the specified EC2 instance for Linux or Windows Server.
- [AWSSupport-ListEC2Resources](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-listec2resources.html): Get information about Amazon EC2 instances and related resources from specified AWS Regions
- [AWSSupport-ManageRDPSettings](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-managerdpsettings.html): Manage common Remote Desktop Protocol (RDP) settings, such as the RDP port and Network Layer Authentication (NLA).
- [AWSSupport-ManageWindowsService](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-managewindowsservice.html): Stop, start, restart, pause, or disable any Windows service on a target instance.
- [AWSSupport-MigrateEC2ClassicToVPC](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-migrate-ec2-classic-to-vpc.html): Migrates an Amazon Elastic Compute Cloud (Amazon EC2) instance from EC2-Classic to a virtual private cloud (VPC).
- [AWSSupport-MigrateXenToNitroLinux](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-migrate-xen-to-nitro.html): Clone and migrate Amazon EC2 Linux Xen instances to Nitro instance types.
- [AWSSupport-ResetAccess](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-resetaccess.html): Use the EC2Rescue tool on the specified EC2 instance to re-enable password decryption using the EC2 Console or to generate and add a new SSH key pair.
- [AWSSupport-ResetLinuxUserPassword](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-resetlinuxuserpassword.html): Reset the password for an OS user.
- [AWSSupport-RunEC2RescueForWindowsTool](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-runec2rescueforwindowstool.html): Runs the Amazon EC2 Rescue for Windows Server troubleshooting tool on Windows managed instances.
- [AWSPremiumSupport-ResizeNitroInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-resizenitroinstance.html): Automate the resizing process for Amazon EC2 instances built on the Nitro System.
- [AWSSupport-ShareEncryptedAMIOrEBSSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-share-encrypted-ami-or-ebs-snapshot.html): Automates the process of sharing encrypted Amazon EC2 AMIs or Amazon EBS snapshots with other AWS accounts.
- [AWSSupport-RestoreEC2InstanceFromSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-restoreec2instancefromsnapshot.html): Restore an Amazon EC2 instance from a working snapshot.
- [AWSSupport-SendLogBundleToS3Bucket](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-sendlogbundletos3bucket.html): Upload a log bundle generated by the EC2Rescue tool from the target instance to a specified S3 bucket.
- [AWSSupport-StartEC2RescueWorkflow](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-startec2rescueworkflow.html): Run a base64 encoded script (Bash or Powershell) on a helper instance created to rescue your instance.
- [AWSSupport-TroubleshootActiveDirectoryReplication](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootactivedirectoryreplication.html): Troubleshoot Microsoft Active Directory domain controller replication failures on Amazon EC2 Windows instances.
- [AWSPremiumSupport-TroubleshootEC2DiskUsage](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awspremiumsupport-troubleshootEC2diskusage.html): Investigate and potentially remediate issues with instance root and non-root disk usage.
- [AWSSupport-TroubleshootEC2InstanceConnect](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-troubleshoot-ec2-instance-connect.html): Automate troubleshooting connection issues to Amazon EC2 instances using Amazon EC2 Instance Connect.
- [AWSSupport-TroubleshootLinuxMGNDRSAgentLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-troublshoot-linux-mngdrs-agent-logs.html): Detect common errors when installing the AWS Application Migration Service (AWS MGN) and AWS Elastic Disaster Recovery (AWS DRS) replication agents in Linux servers to migrate source servers to the AWS cloud.
- [AWSSupport-TroubleshootRDP](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootrdp.html): Check or modify common settings on the target instance which may impact Remote Desktop Protocol (RDP) connections.
- [AWSSupport-TroubleshootSSH](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.html): Install the EC2Rescue tool for Linux and then use it to try to fix common issues that prevent a remote connection to the Linux machine via SSH.
- [AWSSupport-TroubleshootSUSERegistration](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-suse-registration.html): Troubleshoot and register an Amazon EC2 SUSE Linux Enterprise Server instance with SUSE Update Infrastructure.
- [AWSSupport-TroubleshootWindowsPerformance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-troubleshoot-windows-performance.html): The AWSSupport-TroubleshootWindowsPerformance runbook helps troubleshoot performance issues on Amazon Elastic Compute Cloud (Amazon EC2) Windows instances.
- [AWSSupport-TroubleshootWindowsUpdate](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-troubleshoot-windows-update.html): The AWSSupport-TroubleshootWindowsUpdate runbook is used to identify issues that could fail the Windows updates for Amazon Elastic Compute Cloud (Amazon EC2) Windows instances.
- [AWSSupport-UpgradeWindowsAWSDrivers](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-upgradewindowsawsdrivers.html): Upgrade or repair storage and network AWS drivers on the specified EC2 instance,

### [Amazon ECS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ecs.html)

The following runbooks complete various Amazon Elastic Container Service (Amazon ECS) tasks with AWS Systems Manager Automation.

- [AWSSupport-CollectECSInstanceLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-collectecsinstancelogs.html): Collects operating system and Amazon ECS related log files from an Amazon EC2 instance to help you troubleshoot common issues.
- [AWS-InstallAmazonECSAgent](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-install-ecs-agent.html): Install the Amazon ECS agent on your Amazon EC2 instance.
- [AWS-ECSRunTask](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-run-ecs-task.html): Run an Amazon ECS task.
- [AWSSupport-TroubleshootECSContainerInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-ecs-container-instance.html): Troubleshoot an Amazon EC2 instance that fails to register with an Amazon ECS cluster.
- [AWSSupport-TroubleshootECSTaskFailedToStart](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootecstaskfailedtostart.html): Troubleshoot why an Amazon ECS task in an Amazon ECS cluster failed to start.
- [AWS-UpdateAmazonECSAgent](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-update-ecs-agent.html): Update the Amazon ECS agent on your Amazon EC2 instance.

### [Amazon EFS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-efs.html)

The following runbooks complete various Amazon Elastic File System (Amazon EFS) tasks with AWS Systems Manager Automation.

- [AWSSupport-CheckAndMountEFS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-check-and-mount-efs.html): Mounts an Amazon EFS file system to an Amazon EC2 instance.

### [Amazon EKS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-eks.html)

The following runbooks complete various Amazon Elastic Kubernetes Service (Amazon EKS) tasks with AWS Systems Manager Automation.

- [AWS-CreateEKSClusterWithFargateProfile](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-createeksclusterwithfargateprofile.html): Create an Amazon EKS cluster with a Fargate profile.
- [AWS-CreateEKSClusterWithNodegroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-createeksclusterwithnodegroup.html): Create an Amazon EKS cluster with a node group.
- [AWS-DeleteEKSCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deleteekscluster.html): Delete the resources associated with an Amazon EKS cluster, including node groups and Fargate profiles.
- [AWS-MigrateToNewEKSSelfManagedNodeGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-migratetoneweksselfmanagedlinuxnodegroup.html): Create a new Amazon EKS Linux node group to migrate your application to.
- [AWSPremiumSupport-TroubleshootEKSCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awspremiumsupport-troubleshootekscluster.html): Diagnoses common issues with an Amazon EKS cluster, underlying infrastructure and provides recommended remediation steps.
- [AWSSupport-TroubleshootEKSWorkerNode](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshooteksworkernode.html): Troubleshoot common issues that prevent an Amazon EC2 worker node from joining an Amazon EKS cluster.
- [AWS-UpdateEKSCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-updateekscluster.html): Update your Amazon EKS cluster to the Kubernetes version that you want to use.
- [AWS-UpdateEKSManagedNodeGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-updateeksmanagednodegroup.html): Makes updates to managed node groups in your Amazon EKS cluster.
- [AWS-UpdateEKSSelfManagedLinuxNodeGroups](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-updateeksselfmanagedlinuxnodegroup.html): Update managed node groups in your Amazon EKS cluster to the latest AMI version.
- [AWSSupport-CollectEKSInstanceLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-collecteksinstancelogs.html): Troubleshoot common issues by gathering operating system and Amazon EKS related log files from an Amazon EC2 instance.
- [AWSSupport-SetupK8sApiProxyForEKS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-setupk8sapiproxyforeks.html): The AWSSupport-SetupK8sApiProxyForEKS runbook helps manage infrastructure to allow communication from an AWS Lambda function to a private Amazon Elastic Kubernetes Service (Amazon EKS) cluster.
- [AWSSupport-TroubleshootEbsCsiDriversForEks](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-ebs-csi-drivers-for-eks.html): Troubleshoots issues with Amazon EBS CSI drivers for Amazon EKS clusters.
- [AWSSupport-TroubleshootEKSALBControllerIssues](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-eks-alb-controller-issues.html): Troubleshoots issues with AWS Load Balancer Controller in Amazon Elastic Kubernetes Service clusters.

### [Elastic Beanstalk](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-aeb.html)

The following runbooks complete various AWS Elastic Beanstalk (Elastic Beanstalk) tasks with AWS Systems Manager Automation.

- [AWSSupport-CollectElasticBeanstalkLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-collectbeanstalk-logs.html): Gather Elastic Beanstalk related log files from an Amazon EC2 Windows Server instance launched by Elastic Beanstalk to help you troubleshoot common issues.
- [AWSConfigRemediation-EnableElasticBeanstalkEnvironmentLogStreaming](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-eb-logging.html): Enable logging on the Elastic Beanstalk environment you specify.
- [AWSConfigRemediation-EnableBeanstalkEnvironmentNotifications](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-eb-notifications.html): Enable notifications for the Elastic Beanstalk environment you specify.
- [AWSSupport-TroubleshootElasticBeanstalk](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-elastic-beanstalk.html): Helps you troubleshoot the potential reasons why your Elastic Beanstalk environment is in a Degraded or Severe state.

### [Elastic Load Balancing](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-elb.html)

The following runbooks complete various Elastic Load Balancing tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-DropInvalidHeadersForALB](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-drop-alb-headers.html): Enable the application load balancer to remove HTTP headers with invalid headers.
- [AWS-EnableCLBAccessLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-clb-access-logs.html): Enable access logs for a Classic Load Balancer.
- [AWS-EnableCLBConnectionDraining](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableCLBConnectionDraining.html): Enable connection draining for a Classic Load Balancer.
- [AWSConfigRemediation-EnableCLBCrossZoneLoadBalancing](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-clb-crosszone.html): Enable cross-zone load balancing for the Classic Load Balancer (CLB) you specify.
- [AWSConfigRemediation-EnableELBDeletionProtection](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-elb-protection.html): Enable deletion protection for the elastic load balancer (ELB) you specify.
- [AWSConfigRemediation-EnableLoggingForALBAndCLB](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-logging-alb-clb.html): Enable logging for the specified Application Load Balancer or Classic Load Balancer.
- [AWSSupport-TroubleshootCLBConnectivity](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootclbconnectivity.html): Troubleshoot connectivity issues between a Classic Load Balancer and Amazon EC2 instances.
- [AWSConfigRemediation-EnableNLBCrossZoneLoadBalancing](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-nlb-crosszone.html): Enable cross zone load balancing for the network load balancer (NLB) you specify.
- [AWS-UpdateALBDesyncMitigationMode](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-UpdateALBDesyncMitigationMode.html): Update the desync mitigation mode on an Application Load Balancer (ALB).
- [AWS-UpdateCLBDesyncMitigationMode](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-UpdateCLBDesyncMitigationMode.html): Update the desync mitigation mode on an Classic Load Balancer (CLB).
- [AWSSupport-TroubleshootELBHealthChecks](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootelbhealthchecks.html): Troubleshoot Elastic Load Balancing health check issues by analyzing CloudWatch metrics, verifying network connectivity, and executing diagnostic commands.

### [Amazon EMR](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-emr.html)

The following runbooks complete various Amazon EMR tasks with AWS Systems Manager Automation.

- [AWSSupport-AnalyzeEMRLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-analyzeemrlogs.html): Identify errors while running a job on an Amazon EMR cluster.
- [AWSSupport-DiagnoseEMRLogsWithAthena](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-diagnose-emr-logs-with-athena.html): Support Automation Workflow (SAW) Runbook: AWSSupport-DiagnoseEMRLogsWithAthena automate diagnosis of Amazon EMR logs using Athena.

### [Amazon OpenSearch Service](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-opensearch.html)

The following runbooks complete various Amazon OpenSearch Service tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-DeleteOpenSearchDomain](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-opensearch-domain.html): Delete the given Amazon OpenSearch Service domain.
- [AWSConfigRemediation-EnforceHTTPSOnOpenSearchDomain](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enforce-https-opensearch.html): Enables EnforceHTTPS on a given Amazon OpenSearch Service domain.
- [AWSConfigRemediation-UpdateOpenSearchDomainSecurityGroups](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-update-opensearch-security-group.html): Updates the security group configuration on an Amazon OpenSearch Service domain.
- [AWSSupport-TroubleshootOpenSearchRedYellowCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-troubleshoot-opensearch-red-yellow-cluster.html): Automate troubleshooting of Amazon OpenSearch Service Red or Yellow health status.
- [AWSSupport-TroubleshootOpenSearchHighCPU](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-troubleshoot-opensearch-high-cpu.html): Support Automation Workflow (SAW) Runbook: AWSSupport-TroubleshootOpenSearchHighCPU troubleshoot Amazon OpenSearch Service cluster's High CPU issues.

### [EventBridge](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ev.html)

The following runbooks complete various Amazon EventBridge (EventBridge) tasks with AWS Systems Manager Automation.

- [AWS-AddOpsItemDedupStringToEventBridgeRule](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-add-dedup-string-ev.html): Add a deduplication string for all Systems Manager OpsItems associated with an EventBridge rule.
- [AWS-DisableEventBridgeRule](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disable-ev-rule.html): Disables an EventBridge rule.

### [AWS Glue](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-glu.html)

The following runbooks complete various AWS Glue (AWS Glue) tasks with AWS Systems Manager Automation.

- [AWSSupport-TroubleshootGlueConnection](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootglueconnection.html): The AWSSupport-TroubleshootGlueConnection automation runbook assists you troubleshoot errors when testing AWS Glue connections.

### [Amazon FSx](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-fsx.html)

The following runbooks complete various Amazon FSx tasks with Amazon FSx Automation.

- [AWSSupport-ValidateFSxWindowsADConfig](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-validate-fsxwindows-adconfig.html): The AWSSupport-ValidateFSxWindowsADConfig runbook is used to validate the self-managed Active Directory (AD) configuration of an Amazon FSx for Windows File Server

### [GuardDuty](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-gdu.html)

The following runbooks complete various Amazon GuardDuty (GuardDuty) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-CreateGuardDutyDetector](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-guard-detect.html): Create a GuardDuty detector in the AWS Region where you run automations.

### [IAM](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-iam.html)

The following runbooks complete various AWS Identity and Access Management (IAM) tasks with AWS Systems Manager Automation.

- [AWSSupport-TroubleshootIAMAccessDeniedEvents](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-troubleshootiamaccessdeniedevents.html): Troubleshoots issues with IAM access denied events
- [AWS-AttachIAMToInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-attachiamtoinstance.html): Attach an IAM role to a managed instance.
- [AWS-DeleteIAMInlinePolicy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/delete-iam-inline-policy.html): Delete the AWS Identity and Access Management (IAM) inline policy you specify.
- [AWSConfigRemediation-DeleteIAMRole](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-role.html): Delete the AWS Identity and Access Management (IAM) role you specify.
- [AWSConfigRemediation-DeleteIAMUser](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-user.html): Delete the IAM user you specify.
- [AWSConfigRemediation-DeleteUnusedIAMGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-group.html): Delete an IAM group that does not contain any users.
- [AWSConfigRemediation-DeleteUnusedIAMPolicy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-policy.html): Delete an IAM policy that is not attached to any users, groups, or roles.
- [AWSConfigRemediation-DetachIAMPolicy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-detach-iam-policy.html): Detach the AWS Identity and Access Management (IAM) policy you specify.
- [AWSConfigRemediation-EnableAccountAccessAnalyzer](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-account-access-analyzer.html): Create an IAM Access Analyzer in your AWS account.
- [AWSSupport-GrantPermissionsToIAMUser](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-grantpermissionstoiamuser.html): Grant the specified permissions to an IAM group (new or existing), and add the existing IAM user to it.
- [AWSConfigRemediation-RemoveUserPolicies](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-user-policies.html): Removes IAM policies from the user you specify.
- [AWSConfigRemediation-ReplaceIAMInlinePolicy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-replace-iam-policy.html): Replace the IAM inline policy you specify with an AWS managed policy.
- [AWSConfigRemediation-RevokeUnusedIAMUserCredentials](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-revoke-iam-user.html): Revoke unused AWS Identity and Access Management (IAM) credentials from a user.
- [AWSConfigRemediation-SetIAMPasswordPolicy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-set-iam-policy.html): Set the IAM user password policy for your AWS account.
- [AWSSupport-ContainIAMPrincipal](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-contain-iam-principal.html): The AWSSupport-ContainIAMPrincipal runbook helps to contain a compromised AWS Identity and Access Management (IAM) resource IAM Role, IAM User or Identity Center user (IDC).
- [AWSSupport-TroubleshootSAMLIssues](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-troubleshootsamlissues.html): Troubleshoots issues with IAM SAML federation

### [Incident Detection and Response](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-idr.html)

The following runbooks complete various AWS Incident Detection and Response tasks with AWS Systems Manager Automation.

- [AWSPremiumSupport-OnboardWorkloadToIDR](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awspremisumsupport-onboardworkloadtoidr.html): Helps AWS Enterprise Support (with additional fee) and Unified Operations customers onboard a workload for monitoring and critical incident management using AWS Incident Detection and Response.

### [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-aks.html)

The following runbooks complete various Amazon Kinesis Data Streams (Kinesis Data Streams) tasks with AWS Systems Manager Automation.

- [AWS-EnableKinesisStreamEncryption](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enablekinesisstreamencryption.html): Enable encryption for an Kinesis Data Streams.

### [AWS KMS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-kms.html)

The following runbooks complete various AWS Key Management Service (AWS KMS) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-CancelKeyDeletion](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-cancel-key-deletion.html): Cancel deletion of your AWS Key Management Service (AWS KMS) customer managed key.
- [AWSConfigRemediation-EnableKeyRotation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-key-rotation.html): Enables automatic key rotation for your AWS Key Management Service (AWS KMS) customer managed key.

### [Lambda](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-lam.html)

The following runbooks complete various AWS Lambda (Lambda) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-ConfigureLambdaFunctionXRayTracing](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-config-lambda-xray.html): Enable AWS X-Ray live tracing on the AWS Lambda function you specify in the FunctionName parameter.
- [AWSConfigRemediation-DeleteLambdaFunction](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-lambda.html): Delete the AWS Lambda function you specify.
- [AWSConfigRemediation-EncryptLambdaEnvironmentVariablesWithCMK](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-encrypt-lambda-variables.html): Encrypt the environment variables for the AWS Lambda function you specify using a AWS KMS customer managed key.
- [AWSConfigRemediation-MoveLambdaToVPC](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-lambda-to-vpc.html): Moves an AWS Lambda (Lambda) function to an Amazon Virtual Private Cloud (Amazon VPC).
- [AWSSupport-RemediateLambdaS3Event](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-remediatelambdas3event.html): Identify and resolve issues with Amazon Simple Storage Service (Amazon S3) event trigger for Lambda.
- [AWSSupport-TroubleshootLambdaInternetAccess](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWSSupport-TroubleshootLambdaInternetAccess.html): Troubleshoot internet access for a Lambda function.
- [AWSSupport-TroubleshootLambdaS3Event](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootlambdas3event.html): Troubleshoot Amazon S3 event notifications that failed to trigger the specified Lambda function

### [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-mwaa.html)

The following runbooks complete various Amazon Managed Workflows for Apache Airflow (Amazon MWAA) tasks with AWS Systems Manager Automation.

- [AWSSupport-TroubleshootMWAAEnvironmentCreation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-troubleshoot-mwaa-environment-creation.html): The AWSSupport-TroubleshootMWAAEnvironmentCreation runbook helps diagnose Amazon Managed Workflows for Apache Airflow environment creation.

### [Neptune](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-neptune.html)

The following runbooks complete various Amazon Neptune (Neptune) tasks with AWS Systems Manager Automation.

- [AWS-EnableNeptuneDbAuditLogsToCloudWatch](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableNeptuneDbAuditLogsToCloudWatch.html): Send audit logs for a Neptune DB cluster to CloudWatch.
- [AWS-EnableNeptuneDbBackupRetentionPeriod](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableNeptuneDbBackupRetentionPeriod.html): Enable backups for a Neptune DB.
- [AWS-EnableNeptuneClusterDeletionProtection](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableNeptuneClusterDeletionProtection.html): Enable deletion protection for a Neptune cluster.

### [Amazon RDS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-rds.html)

The following runbooks complete various Amazon Relational Database Service (Amazon RDS) tasks with AWS Systems Manager Automation.

- [AWS-CreateEncryptedRdsSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/create-encrypted-rds-snapshot.html): Creates an encrypted Amazon RDS instance snapshot.
- [AWS-CreateRdsSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createrdssnapshot.html): Create an Amazon RDS snapshot for an Amazon RDS instance.
- [AWSConfigRemediation-DeleteRDSCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-cluster.html): Delete the Amazon RDS cluster you specify.
- [AWSConfigRemediation-DeleteRDSClusterSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-cluster-snap.html): Delete the given Amazon RDS cluster snapshot.
- [AWSConfigRemediation-DeleteRDSInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-instance.html): Delete the Amazon RDS instance you specify.
- [AWSConfigRemediation-DeleteRDSInstanceSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-snapshot.html): Delete the Amazon Relational Database Service (Amazon RDS) instance snapshot you specify.
- [AWSConfigRemediation-DisablePublicAccessToRDSInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disable-rds-instance-public-access.html): Disable public accessibility for the Amazon RDS database instance you specify.
- [AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-tags-snapshot-rds-cluster.html): Copy all tags from the DB cluster to snapshots of the DB cluster.
- [AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSDBInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-tags-snapshot-rds-instance.html): Copy all tags from the DB instance to snapshots of the DB instance.
- [AWSConfigRemediation-EnableEnhancedMonitoringOnRDSInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-rds-monitoring.html): Enable Enhanced Monitoring on the Amazon RDS database instance you specify.
- [AWSConfigRemediation-EnableMinorVersionUpgradeOnRDSDBInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-rds-minor-version.html): Enables the AutoMinorVersionUpgrade setting on the Amazon RDS database instance you specify.
- [AWSConfigRemediation-EnableMultiAZOnRDSInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-multi-az-rds.html): Change your Amazon RDS database instance to a Multi-AZ deployment.
- [AWSConfigRemediation-EnablePerformanceInsightsOnRDSInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-performance-insights-rds.html): Description
- [AWSConfigRemediation-EnableRDSClusterDeletionProtection](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-rds-cluster-deletion-protection.html): Enable deletion protection on the Amazon RDS cluster you specify.
- [AWSConfigRemediation-EnableRDSInstanceBackup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-rds-instance-backup.html): Enable backups for the Amazon RDS database instance you specify.
- [AWSConfigRemediation-EnableRDSInstanceDeletionProtection](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-rds-instance-deletion-protection.html): Enable deletion protection on the Amazon RDS database instance you specify.
- [AWSConfigRemediation-ModifyRDSInstancePortNumber](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-rds-port.html): Modify the port number on which the Amazon RDS database instance accepts connections.
- [AWSSupport-ModifyRDSSnapshotPermission](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-modifyrdssnapshotpermission.html): Modify permissions for multiple Amazon RDS snapshots.
- [AWSPremiumSupport-PostgreSQLWorkloadReview](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-postgresqlworkloadreview.html): Captures Amazon RDS PostgreSQL database usage statistics required for a Proactive Services expert to perform an operational review.
- [AWS-RebootRdsInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-rebootrdsinstance.html): Reboot an Amazon RDS DB instance if it isn't already rebooting.
- [AWSSupport-ShareRDSSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-sharerdssnapshot.html): Automate sharing an encrypted Amazon RDS DB snapshot with another account.
- [AWS-StartRdsInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-startrdsinstance.html): Start an Amazon RDS instance.
- [AWS-StartStopAuroraCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/start-stop-aurora-cluster.html): Start or stop an Amazon Aurora cluster.
- [AWS-StopRdsInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-stoprdsinstance.html): Stop an Amazon RDS instance.
- [AWSSupport-TroubleshootConnectivityToRDS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootconnectivitytords.html): Diagnose connectivity issues between an EC2 instance and an Amazon RDS instance.
- [AWSSupport-TroubleshootRDSIAMAuthentication](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-rds-iam-authentication.html): Automate troubleshooting of AWS Identity and Access Management (IAM) crednetials not working for Amazon Relational Database Service (Amazon RDS) Database Authentication
- [AWSSupport-ValidateRdsNetworkConfiguration](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-validate-rds-network-configuration.html): Support Automation Workflow (SAW) Runbook: Validate Amazon Relational Database Service (Amazon RDS) network configuration.

### [Amazon Redshift](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-rs.html)

The following runbooks complete various Amazon Redshift tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-DeleteRedshiftCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-redshift.html): Delete the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-DisablePublicAccessToRedshiftCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disable-redshift-public-access.html): Disable public accessibility for the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-EnableRedshiftClusterAuditLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-redshift-audit.html): Enable audit logging for the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-EnableRedshiftClusterAutomatedSnapshot](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-redshift-snapshot.html): Enable automated snapshots for the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-EnableRedshiftClusterEncryption](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-redshift-encrypt.html): Enable encryption on the Amazon Redshift cluster you specify using a AWS KMS customer managed key.
- [AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-redshift-enhanced-routing.html): Enable enhanced virtual private cloud (VPC) routing for the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-EnforceSSLOnlyConnectionsToRedshiftCluster](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enforce-redshift-ssl-only.html): Require incoming connections to use SSL for the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-ModifyRedshiftClusterMaintenanceSettings](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-redshift-maintenance.html): Modify maintenance settings for the Amazon Redshift cluster you specify.
- [AWSConfigRemediation-ModifyRedshiftClusterNodeType](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-redshift-cluster-node.html): Modify the node type for the Amazon Redshift cluster you specify.

### [Amazon S3](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-s3.html)

The following runbooks complete various Amazon Simple Storage Service (Amazon S3) tasks with AWS Systems Manager Automation.

- [AWS-ArchiveS3BucketToIntelligentTiering](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-archives3buckettointelligenttiering.html): Create or update an intelligent tiering configuration for an Amazon S3 bucket.
- [AWS-ConfigureS3BucketLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configures3bucketlogging.html): Enable logging on an Amazon S3 bucket.
- [AWS-ConfigureS3BucketVersioning](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configures3bucketversioning.html): Configure versioning for an Amazon S3 bucket.
- [AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-block-public-s3-bucket.html): Description
- [AWSConfigRemediation-ConfigureS3PublicAccessBlock](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-block-public-s3.html): Configure an AWS account's Amazon S3 public access block settings based on the values you specify in the runbook parameters.
- [AWS-CreateS3PolicyToExpireMultipartUploads](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-CreateS3PolicyToExpireMultipartUploads.html): Create a lifecycle policy for a specified bucket that expires incomplete, multi-part uploads in progress after a set number of days
- [AWS-DisableS3BucketPublicReadWrite](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disables3bucketpublicreadwrite.html): Disable read and write access for a public S3 bucket.
- [AWS-EnableS3BucketEncryption](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enableS3bucketencryption.html): Configure default encryption for an Amazon S3 bucket.
- [AWS-EnableS3BucketKeys](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enableS3bucketkeys.html): Enable Amazon S3 Bucket Keys.
- [AWSConfigRemediation-RemovePrincipalStarFromS3BucketPolicy](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-s3-wildcard.html): Remove principal policy statements with wildcards for allow actions from your Amazon S3 bucket policy.
- [AWSConfigRemediation-RestrictBucketSSLRequestsOnly](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-s3-deny-http.html): Description
- [AWSSupport-TroubleshootS3PublicRead](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoots3publicread.html): Diagnose issues reading objects from the public Amazon S3 bucket you specify in the S3BucketName parameter.
- [AWSSupport-ConfigureS3ReplicationSameAndCrossAccount](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configures3replicationsameandcrossaccount.html): Configures Amazon Simple Storage Service (Amazon S3) bucket replication between a source and destination bucket for same-account and cross-account scenarios.
- [AWSSupport-EmptyS3Bucket](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-empty-s3-bucket.html): Empties an existing Amazon Simple Storage Service (Amazon S3) bucket by using a lifecycle expiration configuration rule.
- [AWSSupport-TroubleshootS3EventNotifications](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-troubleshoot-s3-event-notifications.html): Troubleshoot Amazon Simple Storage Service (Amazon S3) Bucket Event Notification configurations.
- [AWSSupport-ContainS3Resource](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-contains3resource.html): Isolate a potentially compromised or suspicious Amazon Simple Storage Service (Amazon S3) Bucket while preserving its contents for further investigation.

### [Amazon SES](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ses.html)

The following runbooks complete various Amazon Simple Email Service (Amazon SES) tasks with AWS Systems Manager Automation.

- [AWSSupport-AnalyzeSESMessageSendingStatus](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-analyze-ses-message-sending-status.html): The AWSSupport-AnalyzeSESMessageSendingStatus automation runbook helps you troubleshoot undelivered emails sent from Amazon Simple Email Service.
- [AWSSupport-DeploySESSendingLogsToCloudWatchLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-deploysessendinglogstocloudwatchlogs.html): Configures infrastructure for Amazon Simple Email Service event publishing to Amazon CloudWatch Logs.

### [SageMaker AI](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-sm.html)

The following runbooks complete various Amazon SageMaker AI (SageMaker AI) tasks with AWS Systems Manager Automation.

- [AWS-DisableSageMakerNotebookRootAccess](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-DisableSageMakerNotebookRootAccess.html): Disable root access on Amazon SageMaker AI notebook instances.

### [Secrets Manager](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-asm.html)

The following runbooks complete various AWS Secrets Manager (Secrets Manager) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-DeleteSecret](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-secret.html): Deletes a secret stored in AWS Secrets Manager.
- [AWSConfigRemediation-RotateSecret](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-rotate-secret.html): Rotates a secret stored in AWS Secrets Manager.

### [Security Hub CSPM](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ash.html)

The following runbooks complete various AWS Security Hub CSPM (Security Hub CSPM) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-EnableSecurityHub](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-security-hub.html): Enable AWS Security Hub CSPM (Security Hub CSPM) for the AWS account and AWS Region where you run the automation.

### [AWS Shield](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-shd.html)

The following runbooks complete various AWS Shield tasks with AWS Systems Manager Automation.

- [AWSPremiumSupport-DDoSResiliencyAssessment](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-ddosresiliencyassessment.html): Automate DDoS vulnerability checks and configuration of resources in accordance with Shield Advanced protection.

### [Amazon SNS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-sns.html)

The following runbooks complete various Amazon Simple Notification Service (Amazon SNS) tasks with AWS Systems Manager Automation.

- [AWS-EnableSNSTopicDeliveryStatusLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enable-sns-topic-delivery-status-logging.html): Enable encryption on an Amazon Simple Notification Service (Amazon SNS) topic.
- [AWSConfigRemediation-EncryptSNSTopic](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-encrypt-sns-topic.html): Enable encryption on an Amazon Simple Notification Service (Amazon SNS) topic.
- [AWS-PublishSNSNotification](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-publishsnsnotification.html): Publish a notification to Amazon SNS.

### [Amazon SQS](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-sqs.html)

The following runbooks complete various Amazon SQS tasks with AWS Systems Manager Automation.

- [AWS-EnableSQSEncryption](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enablesqsencryption.html): Enable encryption at rest for an Amazon SQS queue.

### [Step Functions](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-sfn.html)

The following runbooks complete various Step Functions tasks with AWS Systems Manager Automation.

- [AWS-EnableStepFunctionsStateMachineLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enablestepfunctionsstatemachinelogging.html): Enable logging for a Step Functions state machine.

### [Systems Manager](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-sys.html)

The following runbooks complete various AWS Systems Manager (Systems Manager) tasks with Systems Manager Automation.

- [AWS-BulkDeleteAssociation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-bulkdeleteassociation.html): Delete multiple Systems Manager State Manager associations.
- [AWS-BulkEditOpsItems](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-bulk-edit-opsitems.html): Edit OpsItems that match the filter you specify.
- [AWS-BulkResolveOpsItems](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-bulk-resolve-opsitems.html): Resolve OpsItems that match the filter you specify.
- [AWS-ConfigureMaintenanceWindows](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-configuremaintenancewindows.html): Enable or disable Systems Manager maintenance windows.
- [AWS-CreateManagedLinuxInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createmanagedlinuxinstance.html): Create an EC2 instance for Linux that is configured for Systems Manager.
- [AWS-CreateManagedWindowsInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createmanagedwindowsinstance.html): Create an EC2 instance for a Windows Server that is configured for Systems Manager.
- [AWSConfigRemediation-EnableCWLoggingForSessionManager](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cw-log-sm.html): Enables Session Manager sessions to store output logs to a CloudWatch log group.
- [AWS-ExportOpsDataToS3](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-exportopsdatatos3.html): Retrieve a list of OpsData summaries in AWS Systems Manager Explorer and export them to an object in a specified S3 bucket.
- [AWS-ExportPatchReportToS3](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-exportpatchreporttos3.html): Retrieve lists of patch summary data and patch details in AWS Systems Manager Patch Manager and export them to a .csv file in a specified Amazon S3 bucket.
- [AWS-SetupInventory](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-setupinventory.html): Create a Systems Manager Inventory association for one or more managed instances.
- [AWS-SetupManagedInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-setupmanagedinstance.html): Configure an instance with an IAM role for Systems Manager access.
- [AWS-SetupManagedRoleOnEC2Instance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-setupmanagedroleonec2instance.html): Configure an instance with the SSMRoleForManagedInstance managed IAM role for Systems Manager access.
- [AWSSupport-TroubleshootManagedInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html): Troubleshoot why an Amazon EC2 Instance is not showing as managed by Systems Manager.
- [AWSSupport-TroubleshootPatchManagerLinux](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-troubleshoot-patch-manager-linux.html): Automate troubleshooting AWS Systems Manager Patch Manager for Linux.
- [AWSSupport-TroubleshootSessionManager](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-session-manager.html): Helps you troubleshoot common issues that prevent you from connecting to managed instances using Session Manager.

### [Third-party](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-third-party.html)

The following runbooks complete various tasks for third-party products and services with AWS Systems Manager Automation.

- [AWS-CreateJiraIssue](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createjiraissue.html): Create an issue in Jira.
- [AWS-CreateServiceNowIncident](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createservicenowincident.html): Create an incident in the ServiceNow incident table.
- [AWS-RunPacker](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-runpacker.html): Use the HashiCorp Packer tool to validate, fix, or build packer templates that are used to create machine images.

### [Amazon VPC](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-vpc.html)

The following runbooks complete various Amazon Virtual Private Cloud (Amazon VPC) tasks with AWS Systems Manager Automation.

- [AWS-CloseSecurityGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/close-security-group.html): Removes all ingress and egress rules from a security group.
- [AWSSupport-ConfigureDNSQueryLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configure-dns-query-logging.html): Log DNS queries that originate in your VPC or for RouteÂ 53 hosted zones.
- [AWSSupport-ConfigureTrafficMirroring](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configuretrafficmirroring.html): Troubleshoot connectivity issues between a load balancer and Amazon EC2 instances.
- [AWSSupport-ConnectivityTroubleshooter](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-connectivitytroubleshooter.html): Diagnose connectivity issues between different types of AWS resources.
- [AWSSupport-TroubleshootVPN](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-vpn.html): Automate troubleshooting of AWS Site-to-Site VPN connections.
- [AWSConfigRemediation-DeleteEgressOnlyInternetGateway](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-egress-igw.html): Delete the egress-only internet gateway you specify.
- [AWSConfigRemediation-DeleteUnusedENI](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-eni.html): Delete an elastic network interface that has a detached status.
- [AWSConfigRemediation-DeleteUnusedSecurityGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-ec2-security-group.html): Delete the security group you specify in the GroupId parameter as long as it is not a default security group.
- [AWSConfigRemediation-DeleteUnusedVPCNetworkACL](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-vpc-nacl.html): Delete a network access control list (ACL) that is not associated with a subnet.
- [AWSConfigRemediation-DeleteVPCFlowLog](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-vpc-flow-log.html): Delete a virtual private cloud (VPC) flow log.
- [AWSConfigRemediation-DetachAndDeleteInternetGateway](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-detach-delete-igw.html): Detach and delete the internet gateway you specify.
- [AWSConfigRemediation-DetachAndDeleteVirtualPrivateGateway](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-detach-delete-vpg.html): Detach and delete a given Amazon EC2 virtual private gateway attached to a virtual private cloud (VPC) created with Amazon VPC.
- [AWS-DisableIncomingSSHOnPort22](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/disable-incoming-ssh.html): Remove rules that allow unrestricted incoming SSH traffic on TCP port 22.
- [AWS-DisablePublicAccessForSecurityGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disablepublicaccessforsecuritygroup.html): Disable default SSH and RDP ports that are opened to all IP addresses.
- [AWSConfigRemediation-DisableSubnetAutoAssignPublicIP](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disable-subnet-auto-public-ip.html): Disable the IPv4 public addressing attribute for the subnet you specify.
- [AWSSupport-EnableVPCFlowLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-vpc-flowlogs.html): Create flow logs for resources in your VPC.
- [AWSConfigRemediation-EnableVPCFlowLogsToCloudWatch](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-flow-logs-cw.html): Publish VPC flow log data to Amazon CloudWatch Logs.
- [AWSConfigRemediation-EnableVPCFlowLogsToS3Bucket](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-flow-logs-s3.html): Publish VPC flow log data to Amazon Simple Storage Service.
- [AWS-ReleaseElasticIP](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-releaseelasticip.html): Release the specified Elastic IP address using the allocation ID.
- [AWS-RemoveNetworkACLUnrestrictedSSHRDP](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-remove-nacl-unrestricted-ssh-rdp.html): Remove network ACL rules that allow traffic from all source addresses to default SSH and RDP ports.
- [AWSConfigRemediation-RemoveUnrestrictedSourceIngressRules](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-unrestricted-source-ingress.html): Remove all ingress rules from the security group that allow traffic from all source addresses.
- [AWSConfigRemediation-RemoveVPCDefaultSecurityGroupRules](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-default-secg-rules.html): Remove all rules from the default security group of a virtual private cloud (VPC).
- [AWSSupport-SetupIPMonitoringFromVPC](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-setupipmonitoringfromvpc.html): Create an EC2 instance in the specified subnet.
- [AWSSupport-TerminateIPMonitoringFromVPC](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-terminateipmonitoringfromvpc.html): Terminate an IP monitoring test previously started by AWSSupport-SetupIPMonitoringFromVPC .

### [AWS WAF](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-waf.html)

The following runbooks complete various AWS WAF tasks with AWS Systems Manager Automation.

- [AWS-AddWAFRegionalRuleToRuleGroup](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-AddWAFRegionalRuleToRuleGroup.html): Add an existing AWS WAF regional rule to a AWS WAF regional rule group.
- [AWS-AddWAFRegionalRuleToWebAcl](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-AddWAFRegionalRuleToWebAcl.html): Add an existing AWS WAF regional rule to a AWS WAF regional rule group.
- [AWSConfigRemediation-EnableWAFClassicLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-waf-logging.html): Enable logging for the AWS WAF web access control list (ACL) you specify.
- [AWSConfigRemediation-EnableWAFClassicRegionalLogging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-waf-reg-logging.html): Enable logging for the AWS WAF web access control list (ACL) you specify.
- [AWSConfigRemediation-EnableWAFV2Logging](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-wafv2-logging.html): Enable logging for an AWS WAFV2 regional and global web access control list (ACL) with the specified Amazon Kinesis Data Firehose.

### [Amazon WorkSpaces](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-wsp.html)

The following runbooks complete various Amazon WorkSpaces tasks with AWS Systems Manager Automation.

- [AWS-CreateWorkSpace](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-create-workspace.html): Create an Amazon WorkSpaces virtual desktop.
- [AWSSupport-RecoverWorkSpace](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-recover-workspace.html): Recover an Amazon WorkSpaces virtual desktop.

### [X-Ray](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-xray.html)

The following runbooks complete various AWS X-Ray (X-Ray) tasks with AWS Systems Manager Automation.

- [AWSConfigRemediation-UpdateXRayKMSKey](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-update-xray-key.html): Enable encryption on your AWS X-Ray data with AWS Key Management Service (AWS KMS).
