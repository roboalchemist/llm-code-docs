# Source: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/llms.txt

# AWS GovCloud (US) User Guide

> Provides information about setting up your AWS GovCloud (US) account, identifies the differences between the AWS GovCloud (US) Regions and other AWS Regions, and defines usage guidelines for processing export-controlled data within the AWS GovCloud (US) Regions.

- [Welcome](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/welcome.html)
- [Document History](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/history.html)

## [What Is AWS GovCloud (US)?](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/whatis.html)

- [Differences with Standard AWS Accounts](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-differences.html): Describes the differences between AWS GovCloud (US) Regions compared to standard AWS Regions.
- [Account validation](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/validate-accounts.html): Describes how to validate AWS GovCloud (US) accounts using a standard AWS account.
- [Billing and Payment](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/usage-and-payment.html): Describes billing and payment for AWS GovCloud (US) using a standard AWS account.


## [Getting Started](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-set-up.html)

- [AWS GovCloud (US) Sign Up](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html): In order to sign up for an AWS GovCloud (US) account, you need to be an individual or entity that meets the requirement of AWS GovCloud (US).
- [AWS Standard Account Linking](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-standard-account-linking.html): AWS GovCloud (US) accounts are associated 1:1 with standard AWS accounts for billing, service, and support purposes.

### [Signing in to AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/signing-into-govcloud.html)

The AWS Management Console provides a web-based user interface that you can use to create and manage your AWS resources.

- [Your AWS GovCloud (US) account ID and its alias](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-account-ID-alias.html): To sign in to an AWS GovCloud (US) account as an IAM user, you must have an account alias or an account ID for the AWS GovCloud (US) account.
- [AWS GovCloud (US) sign-in issues](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sign-in-issues.html): Use the information here to help you troubleshoot sign-in and other AWS GovCloud (US) account issues.
- [AWS GovCloud (US) account root user](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-account-root-user.html): When you first create a standard AWS account (not an AWS GovCloud (US) account), you begin with one identity that has complete access to all AWS services and resources in the account.

### [Onboarding (Direct Customers)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-direct-customers.html)

AWS Direct Customers can follow the steps outlined in Configuring Your Account to set up their GovCloud accounts and ensure CloudTrail is enabled.

- [Configuring Your Account](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/configure-account.html): The steps in this section describe how to sign in and create an account alias and access keys.
- [Verifying AWS CloudTrail Is Enabled](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/verifying-cloudtrail.html): As part of the automated AWS GovCloud (US) activation process, the CloudTrail service should be enabled for each account and an Amazon S3 bucket should be created to store CloudTrail logs.
- [Onboarding to AWS GovCloud (US) as a Solution Provider reselling in AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-console.html): Describes how resellers access the AWS GovCloud (US) console and use an administrative IAM user.
- [Configure Your Account using AWS CLI](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/configure-using-cli.html): Describes how to configure Your Account using AWS CLI".
- [Enabling Multi-Factor Authentication (MFA) for users](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/mfa-device.html): Describes how to enable MFA devices in the AWS GovCloud (US).
- [Signing Up for AWS Support](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/customer-supp.html): Sign up for AWS GovCloud (US) Customer Support by using the standard AWS root account credentials that are associated with your AWS GovCloud (US) account.


## [Setting Up AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-services.html)

### [CloudFront with Your Resources](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-cloudfront.html)

Set up Amazon CloudFront to work with your AWS GovCloud (US) resources.

- [Credentials](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-credentials.html): If you use CloudFront with AWS GovCloud (US), be sure that you use the correct credentials:
- [Tips for Setting Up CloudFront](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-cloudfront-tips.html): As you set up CloudFront to serve your AWS GovCloud (US) content, keep the following in mind:
- [Migrating RouteÂ 53 public hosted zones from commercial AWS Region to AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/migrating-route53-hostedzone.html): Migrating a RouteÂ 53 public hosted zones to AWS GovCloud (US).
- [Route 53 Zone Apex Support with a Load Balancer](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-route53-zoneapex-elb.html): Set up Amazon RouteÂ 53 zone apex to work with your AWS GovCloud (US) Elastic Load Balancing load balancer.


## [Using AWS GovCloud (US) Regions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud.html)

- [Amazon Resource Names](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-arns.html): Use Amazon Resource Names (ARNs) to uniquely identify AWS resources in the AWS GovCloud (US) Regions.
- [Service Endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html): Access the AWS GovCloud (US-West) or AWS GovCloud (US-East) endpoints by using the command line interface or programmatically with the APIs.
- [VPC Endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-vpc-endpoints.html): Access the AWS GovCloud (US-West) or AWS GovCloud (US-East) endpoints by using the command line interface.
- [Compliance](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-compliance.html): Compliance in AWS GovCloud (US).
- [Export Compliance in AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-itar.html): Maintain compliance with U.S.
- [Accessing the AWS GovCloud (US) Regions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/accessing-govcloud.html): Access the AWS GovCloud (US) Regions by using your unique AWS GovCloud (US) credentials.
- [Controlling Access](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/controlling-access.html): Control access to your AWS GovCloud (US) account.
- [Command Line and API Access](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/cli-and-api-access.html): Control access to your AWS GovCloud (US) account using the command line interface, Query API, or REST interface.
- [Resource Limits](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-limits.html): Lists the limits for certain resources in your AWS GovCloud (US) account.
- [Penetration Testing](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/pen-testing.html): Describes the AWS policy that you must request permission for penetration testing.
- [Service Health Dashboard](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/health-dashboard.html): Describes the Service Health Dashboard that displays information on service availability in {govcloud-us-regions}.
- [Closing an AWS GovCloud (US) account](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/Closing-govcloud-account.html): Describes the process of closing standard and AWS GovCloud (US) account in AWS GovCloud (US) Regions.


## [Services in AWS GovCloud (US) Regions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-services.html)

- [Application Auto Scaling](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-appas.html): Lists the differences for using Application Auto Scaling in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS AppConfig](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-appc.html): Lists the differences for using AWS AppConfig in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Application Migration Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-mgn.html): Lists the differences for using AWS Application Migration Service in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Artifact](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-artifact.html): Lists the differences for using AWS Artifact in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Auto Scaling](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-awsas.html): Lists the differences for using AWS Auto Scaling in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-bint.html): Lists the differences for using AWS Backint Agent for SAP HANA in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Backup](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-bkp.html): Lists the differences for using AWS Backup in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Batch](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-batch.html): Lists the differences for using AWS Batch in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Certificate Manager](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-acm.html): Lists the differences for using AWS Certificate Manager in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Private Certificate Authority](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-acmpca.html): Lists the differences for using AWS Private Certificate Authority in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Client VPN](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-vpnclient.html): Lists the differences for using AWS Client VPN in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Cloud Control API](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cloudcontrolapi.html): Lists the differences for using AWS Cloud Control API in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Cloud Map](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cm.html): Lists the differences for using AWS Cloud Map in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Cloud WAN](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cwan.html): Lists the differences for using AWS Cloud WAN in AWS GovCloud (US) Regions compared to other AWS Regions.
- [CloudFormation](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cfn.html): Lists the differences for using CloudFormation in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CloudHSM](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cloudhsm.html): Lists the differences for using AWS CloudHSM in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CloudHSM Classic](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cloudhsm-classic.html): Lists the differences for using AWS CloudHSM Classic in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CloudShell](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cloudshell.html): Lists the differences for using AWS CloudShell in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CloudTrail](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ct.html): Lists the differences for using AWS CloudTrail in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CodeBuild](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-acb.html): Lists the differences for using CodeBuild in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CodeStar Connections](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/CodeStar-connections.html): Lists the differences for using AWS CodeStar Connections in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CodeCommit](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-acc.html): Lists the differences for using CodeCommit in the AWS GovCloud (US-West) Region compared to other AWS Regions.
- [AWS CodeConnections](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/codeconnections.html): You can use the connections feature in the Developer Tools console to connect AWS resources to external code repositories.
- [AWS CodeDeploy](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-codedeploy.html): Lists the differences for using CodeDeploy in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS CodePipeline](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-acp.html): Lists the differences for using AWS CodePipeline in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Compute Optimizer](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-compute-optimizer.html): Lists the differences for using AWS Compute Optimizer in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Config](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-config.html): Lists the differences for using AWS Config in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Control Tower](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-controltower.html): Lists the differences for using AWS Control Tower in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Database Migration Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-dms.html): Lists the differences for using AWS Database Migration Service (AWS DMS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS DataSync](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-dsy.html): Lists the differences for using DataSync in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Deep Learning AMIs](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-deeplearningamis.html): Lists the differences for using AWS Deep Learning AMIs in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Direct Connect](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-dc.html): Lists the differences for using Direct Connect in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Directory Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ds.html): Lists the differences for using AWS Directory Service in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-beanstalk.html): Lists the differences for using AWS Elastic Beanstalk in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-drs.html): Lists the differences for using AWS Elastic Disaster Recovery in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Elemental MediaConvert](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-mediaconvert.html): Lists the differences for using AWS Elemental MediaConvert in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS End User Messaging](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-eum.html): Lists the differences for using AWS End User Messaging in the AWS GovCloud (US) compared to other AWS Regions.
- [AWS Fargate](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-fargate.html): Lists the differences for using AWS Fargate in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Fault Injection Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-fis.html): Lists the differences for using AWS Fault Injection Service in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Firewall Manager](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-fms.html): Lists the differences for using AWS Firewall Manager in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Glue](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-glue.html): Lists the differences for using AWS Glue in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Health](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-health.html): Lists the differences for using AWS Health Dashboard in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IAM Identity Center](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sso.html): Lists the differences for using AWS IAM Identity Center in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Identity and Access Management](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iam.html): Lists the differences for using AWS Identity and Access Management (IAM) in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT Core](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotcore.html): Lists the differences for using AWS IoT Core in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT Device Defender](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-IotDevDefender.html): Lists the differences for using AWS IoT Device Defender in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT Device Management](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotdevman.html): Lists the differences for using AWS IoT Device Management in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT Events](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotevents.html): Lists the differences for using AWS IoT Events in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT Greengrass V1](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotgreengrass.html): Lists the differences for using AWS IoT Greengrass V1 in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT Greengrass V2](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotgreengrassv2.html): Lists the differences for using AWS IoT Greengrass V2 in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT SiteWise](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotsitewise.html): Lists the differences for using AWS IoT SiteWise in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS IoT TwinMaker](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iot-twinmaker.html): Lists the differences for using AWS IoT TwinMaker in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS KMS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-kms.html): Lists the differences for using AWS Key Management Service in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Lake Formation](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-alf.html): Lists the differences for using AWS Lake Formation in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Lambda](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-lambda.html): Lists the differences for using AWS Lambda in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS License Manager](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-licensemanager.html): Lists the differences for using AWS License Manager in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AMS Accelerate](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ams-acc.html): Lists the differences for using AMS Accelerate in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Management Console](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-console.html): Lists the differences for using the AWS Management Console in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Mainframe Modernization](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-mainframe-modernization.html): Lists the differences for using AWS Mainframe Modernization in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Marketplace](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-marketplace.html): Lists the differences for using AWS Marketplace in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Modular Data Center](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-mdc.html): Lists the differences for using AWS MDC in AWS GovCloud (US-West) compared to other AWS Regions.
- [AWS Network Firewall](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-nf.html): Lists the differences for using AWS Network Firewall in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Organizations](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-organizations.html): Lists the differences for using AWS Organizations in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Outposts](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-outposts.html): Lists the differences for using AWS Outposts in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS ParallelCluster](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-parallelcluster.html): Lists the differences for using AWS ParallelCluster in the AWS GovCloud (US) compared to other AWS Regions.
- [AWS PCS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-pcs.html): Lists the differences for using AWS Parallel Computing Service (AWS PCS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Resilience Hub](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-arh.html): The following list details the differences for using this service in AWS GovCloud (US) Regions compared to other AWS Regions:
- [AWS Resource Access Manager](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ram.html): Lists the differences for using AWS Resource Access Manager in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Resource Groups](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-arg.html): Lists the differences for using AWS Resource Groups in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS SDK for SAP ABAP](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-abapsdk.html): Lists the differences for using AWS SDK for SAP ABAP in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Secrets Manager](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-asm.html): Lists the differences for using Secrets Manager in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ash.html): Lists the differences for using Security Hub CSPM in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Service Catalog](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sc.html): Lists the differences for using Service Catalog in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Serverless Application Repository](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sar.html): Lists the differences for using AWS Serverless Application Repository in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Server Migration Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sms.html): Lists the differences for using AWS Server Migration Service (AWS SMS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Signer](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-Signer.html): Lists the differences for using Signer in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS SimSpace Weaver](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-simspaceweaver.html): Lists the differences for using AWS SimSpace Weaver in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-vpn.html): Lists the differences for using AWS Site-to-Site VPN in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Snow Family](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-importexport.html): Lists the differences for using AWS Snow Family in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Step Functions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-step-functions.html): Lists the differences for using AWS Step Functions in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Storage Gateway](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-storagegateway.html): Lists the differences for using AWS Storage Gateway in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Support](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-support.html): Lists the differences for using AWS Support in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Systems Manager](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ssm.html): Lists the differences for using AWS Systems Manager in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Transfer Family](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-tf.html): Lists the differences for using AWS Transfer Family in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Trusted Advisor](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ta.html): Lists the differences for using AWS Trusted Advisor in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Verified Access](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-verified-access.html): Lists the differences for using AWS Verified Access in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS WAF](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-waf.html): Lists the differences for using AWS WAF in the AWS GovCloud (US-West) Region compared to other AWS Regions.
- [AWS Well-Architected Tool](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-wellarchitected.html): Lists the differences for using AWS Well-Architected Tool in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS WickrGov](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-wickr.html): Lists the differences for using AWS WickrGov in AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS X-Ray](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-xray.html): Lists the differences for using AWS X-Ray in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon API Gateway](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-abp.html): Lists the differences for using Amazon API Gateway in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-appstream2.html): Lists the differences for using WorkSpaces Applications in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Athena](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-athena.html): Lists the differences for using Amazon Athena in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Aurora - MySQL and PostgreSQL](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-aurora.html): Lists the differences for using Amazon Aurora in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Bedrock](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-bedrock.html): Lists the differences for using Amazon Bedrock in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Chime SDK](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-chime-sdk.html): Lists the differences for using Amazon Chime SDK in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Cloud Directory](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cds.html): Lists the differences for using Amazon Cloud Directory in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon CloudWatch](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cw.html): Lists the differences for using Amazon CloudWatch in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon CloudWatch Events](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cwe.html): Lists the differences for using Amazon CloudWatch Events in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cwl.html): Lists the differences for using Amazon CloudWatch Logs in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Cognito](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cog.html): Lists the differences for using Amazon Cognito in the AWS GovCloud (US) compared to other AWS Regions
- [Amazon Comprehend](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cmp.html): Lists the differences for using Amazon Comprehend in the AWS GovCloud (US-West) Region compared to other AWS Regions.
- [Amazon Comprehend Medical](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cmpm.html): Lists the differences for using Amazon Comprehend Medical in the AWS GovCloud (US) compared to other AWS Regions.
- [Amazon Connect](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-con.html): Lists the differences for using Amazon Connect in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Detective](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-det.html): Lists the differences for using Amazon Detective in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-dcdb.html): Lists the differences for using Amazon DocumentDB in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon DynamoDB](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ddb.html): Lists the differences for using Amazon DynamoDB in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon EBS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ebs.html): Lists the differences for using Amazon Elastic Block Store (Amazon EBS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon EC2](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ec2.html): Lists the differences for using Amazon Elastic Compute Cloud (Amazon EC2) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-as.html): Lists the differences for using Auto Scaling in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon EC2 Image Builder](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ec2ib.html): Lists the differences for using Amazon Elastic Compute Cloud Image Builder in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon ECR](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ecr.html): Lists the differences for using Amazon Elastic Container Registry (Amazon ECR) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon ECS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ecs.html): Lists the differences for using Amazon Elastic Container Service (Amazon ECS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Elastic File System](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-efs.html): Lists the differences for using Amazon Elastic File System in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-eks.html): Lists the differences for using Amazon EKS in the AWS GovCloud (US) compared to other AWS Regions.
- [Amazon ElastiCache](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-elc.html): Lists the differences for using Amazon ElastiCache in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon EMR](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-emr.html): Lists the differences for using Amazon EMR in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon EventBridge](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-eventbridge.html): Lists the differences for using Amazon EventBridge in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon FSx](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-fsx.html): Lists the differences for using Amazon FSx in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon GuardDuty](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-guardduty.html): Lists the differences for using Amazon GuardDuty in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Inspector Classic](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-inspector.html): Lists the differences for using Amazon Inspector Classic in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Inspector](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-inspector2.html): Lists the differences for using Amazon Inspector in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Kendra](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-kendra.html): Lists the differences for using Amazon Kendra in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-keyspaces.html): Lists the differences for using Amazon Keyspaces (for Apache Cassandra) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-aka.html): Lists the differences for using Amazon Managed Service for Apache Flink in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Data Firehose](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-kinesisfirehose.html): Lists the differences for using Amazon Data Firehose in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-kinesis.html): Lists the differences for using Amazon Kinesis Data Streams in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-kinesisvideo.html): Lists the differences for using Amazon Kinesis Video Streams in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Lex](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-lex.html): Lists the differences for using Amazon Lex in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Location Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-geo.html): Lists the differences for using Amazon Location Service in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Managed Blockchain](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-amb.html): Lists the differences for using Amazon Managed Blockchain in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Managed Grafana](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/grafana.html): This topic describes the functionality of Amazon Managed Grafana in the AWS GovCloud (US) Regions.
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-amp.html): Lists the differences for using Amazon Managed Service for Prometheus in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Managed Streaming for Apache Kafka (MSK)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-msk.html): Lists the differences for using Managed Streaming for Apache Kafka in the AWS GovCloud (US) compared to other AWS Regions.
- [Amazon MemoryDB](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-mdb.html): Lists the differences for using Amazon MemoryDB in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon MQ](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-mq.html): Lists the differences for using Amazon MQ in AWS GovCloud (US) Regions compared to other AAWS Regions.
- [Amazon Neptune](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-neptune.html): Lists the differences for using Amazon Neptune in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon OpenSearch Service](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-opensearch.html): Lists the differences for using Amazon OpenSearch Service in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Pinpoint](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-pinp.html): Lists the differences for using Amazon Pinpoint in the AWS GovCloud (US) compared to other AWS Regions.
- [Amazon Polly](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-polly.html): Lists the differences for using Amazon Polly in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Quick Suite](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-aqs.html): Lists the differences for using Amazon Quick Suite in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon RDS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-rds.html): Lists the differences for using Amazon Relational Database Service (Amazon RDS) in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Redshift](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-redshift.html): Lists the differences for using Amazon Redshift in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Rekognition](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-rekognition.html): Lists the differences for using Amazon Rekognition in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon RouteÂ 53](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-r53.html): Lists the differences for using Amazon RouteÂ 53 in the AWS GovCloud (US-West) Region compared to other AWS Regions.
- [Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-arc-zonal-shift.html): Lists the differences for using Amazon Application Recovery Controller (ARC) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon S3](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-s3.html): Lists the differences for using Amazon Simple Storage Service (Amazon S3) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Glacier](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-gl.html): Lists the differences for using Amazon Glacier in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon S3 on Outposts](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-s3-outposts.html): Lists the differences for using Amazon S3 on Outposts in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon SageMaker AI](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sagemaker.html): Lists the differences for using Amazon SageMaker AI in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon SES](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ses.html): Lists the differences for using Amazon SES in the AWS GovCloud (US) compared to other AWS Regions.
- [Amazon Security Lake](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-asl.html): Lists the differences for using Amazon Security Lake in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon SNS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sns.html): Lists the differences for using Amazon Simple Notification Service (Amazon SNS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon SQS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sqs.html): Lists the differences for using Amazon Simple Queue Service (Amazon SQS) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon SWF](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-swf.html): Lists the differences for using Amazon Simple Workflow Service (Amazon SWF) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Textract](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-txtrct.html): Lists the differences for using Amazon Textract in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Timestream](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-timestream.html): Lists the differences for using Amazon Timestream in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Transcribe](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-tsc.html): Lists the differences for using Amazon Transcribe in the AWS GovCloud (US) Regions compared to other AWS Regions.
- [AWS Transit Gateway](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-transit-gateway.html): Lists the differences for using AWS Transit Gateway in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Translate](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-translate.html): Lists the differences for using Amazon Translate in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon VPC](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-vpc.html): Lists the differences for using Amazon Virtual Private Cloud (Amazon VPC) in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon Verified Permissions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-verifiedpermissions.html): Lists the differences for using Amazon Verified Permissions in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Amazon WorkSpaces](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-workspaces.html): Lists the differences for using Amazon WorkSpaces in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Elastic Load Balancing](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-elb.html): Lists the differences for using Elastic Load Balancing in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Red Hat OpenShift Service on AWS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-rosa.html): Lists the differences for using Red Hat OpenShift Service on AWS in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Research and Engineering Studio on AWS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-res.html): Lists the differences for using Research and Engineering Studio on AWS in AWS GovCloud (US) Regions compared to other AWS Regions.
- [Service Quotas](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-servicequotas.html): Lists the differences for using Service Quotas in AWS GovCloud (US) Regions compared to other AWS Regions.
- [VMware Cloud on AWS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-vmware.html): VMware Cloud on AWS brings VMwareâs enterprise-class Software-Defined Data Center software to the AWS Cloud, and enables customers to run production applications in a managed service from VMware and AWS.
- [Kiro](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-kiro.html): Lists the differences for using Kiro in AWS GovCloud (US) Regions compared to other AWS Regions.


## [Troubleshooting](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-troubleshooting.html)

- [Client.UnsupportedOperation: Instances can only be launched within Amazon VPC in this region](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/Troubleshoot_launch-instance.html): Service: Amazon EC2
- [AWS GovCloud (US) Administrator Account Password Reset](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/Troubleshoot_administrator_account_password_reset.html): If youâve lost access to your AWS GovCloud (US) account, please review the following options:
- [Deactivating AWS GovCloud (US) MFA devices](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/Troubleshoot_deactivating_MFA_devices.html): If you are having trouble signing in with a multi-factor authentication (MFA) device as an IAM user, contact your administrator for help.


## [Related Resources](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-related-resources.html)

- [New to AWS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-additional-resources.html): The following table lists additional resources for users new to AWS:
- [Experienced with AWS](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-experienced.html): The following table lists additional resources for users experienced with AWS:
