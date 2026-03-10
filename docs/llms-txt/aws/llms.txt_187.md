# Source: https://docs.aws.amazon.com/cli/latest/userguide/llms.txt

# AWS Command Line Interface User Guide for Version 2

> The AWS CLI is an open source tool built using the AWS SDK for Python (Boto) that provides commands for interacting with AWS services. With minimal configuration, you can start using all of the functionality provided by the AWS Management Console from your favorite terminal program. This guide provides instructions for installing, configuring, and using the AWS CLI on Windows, macOS, and Linux. Learn how to use the AWS CLI to access the public API of any AWS service and write scripts to manage your AWS resources.

- [Uninstall](https://docs.aws.amazon.com/cli/latest/userguide/uninstall.html)
- [Document History](https://docs.aws.amazon.com/cli/latest/userguide/document-history.html)

## [About the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

- [About the examples](https://docs.aws.amazon.com/cli/latest/userguide/welcome-examples.html): The AWS CLI examples in this guide are formatted in a specific way.
- [Additional documentation and resources](https://docs.aws.amazon.com/cli/latest/userguide/welcome-resources.html): Additional documentations and resources for the AWS CLI.


## [Get started](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html): Before you install the AWS Command Line Interface version 2 on your system you need an AWS account and IAM credentials.
- [Install/Update](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html): Instructions to install or update the AWS CLI on your system.
- [Past releases](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html): Install past releases of the AWS Command Line Interface version 2 on support operating systems.
- [Build and install from source](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-source-install.html): Install the AWS CLI from the GitHub source on your system.
- [Amazon ECR Public/Docker](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-docker.html): This topic describes how to run, version control, and configure the AWS CLI version 2 on Docker using either the official Amazon ECR Public or Docker Hub image.
- [Setup](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html): Learn how to quickly configure basic settings that the AWS Command Line Interface uses to interact with your resources on AWS services.


## [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

- [Configuration settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html): You can save your frequently used configuration settings and credentials in files that are divided into named profiles.
- [Environment Variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html): Environment variables provide another way to specify configuration options and credentials, and can be useful for scripting or temporarily setting a named profile as the default.
- [Command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html): In the AWS CLI, command line options are global parameters you can use to override configuration settings for that command.
- [Command completion](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-completion.html): The AWS CLI includes a bash-compatible command-completion feature that enables you to use the Tab key to complete a partially entered command.
- [Retries](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html): Customize retries for failed AWS CLI API calls that can occur on the server side, or fail due to rate limiting from the AWS service you're calling.
- [HTTP proxies](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-proxy.html): Learn how to configure the AWS CLI to use an HTTP proxy through environment variables using DNS domain names, IP addresses, and port numbers.
- [Endpoints](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-endpoints.html): The AWS CLI automatically uses the default endpoint for each service in an AWS Region, but you can specify an alternate endpoint for your API requests.


## [Authentication and access credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)

- [Console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)

### [IAM Identity Center authentication](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)

This section directs you to instructions to configure the AWS CLI to authenticate users with IAM Identity Center to get credentials to run AWS CLI commands.

- [IAM Identity Center concepts](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso-concepts.html): This topic describes the key concepts of IAM Identity Center.
- [Tutorial: AWS IAM Identity Center and Amazon S3](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso-tutorial.html): This tutorial describes how to configure the AWS CLI to authenticate users with current IAM Identity Center to list your Amazon S3 buckets.
- [Short-term credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html): Configure the AWS CLI to authenticate using short-term credentials.
- [IAM roles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html): Configure the AWS CLI to use a role defined in AWS Identity and Access Management.
- [IAM users](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html): Configure the AWS CLI and specify the settings for interacting with AWS.
- [Amazon EC2 metadata](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html): When you run the AWS CLI from within an Amazon EC2 instance, the instance contains metadata that can be queried for temporary credentials.
- [External credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html): Sourcing external credentials that isn't directly supported by the AWS CLI.


## [Using the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html)

- [Get Help](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-help.html): Learn how to access help content for the AWS CLI including the built-in help command, online reference documentation, and community resources.
- [Command Structure](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html): Learn how to structure a multipart command and "wait" commands for the AWS Command Line Interface to communicate with AWS services.

### [Specify Parameter Values](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html)

Specify and pass parameters as values for the AWS CLI command options.

- [Common Parameter Types](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html): How to correctly specify parameter values of various types with the AWS CLI.
- [Quotes with Strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html): How to correctly use quotes with string values that contain spaces in the AWS CLI.
- [File Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html): How to correctly load the value of a AWS CLI parameter from a file on disk.
- [Generate a CLI Skeleton Template](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html): Use the generate-cli-skeleton option to create a template for parameter input to a command for the AWS Command Line Interface.
- [Shorthand Syntax](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html): Use a shorthand syntax for JSON-formatted data that allows simpler representation of your option parameters with the AWS CLI.
- [Auto-prompt](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-prompting.html): How to get the AWS CLI to dynamically prompt you for parameters.

### [Control Command Output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html)

Control the format of the output from the AWS CLI.

- [Output Format](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html): Control the format of the output from the AWS CLI.
- [Error Output Format](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-error-format.html): Control the format of error output from the AWS CLI.
- [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html): Use pagination options to optimize the output of AWS CLI API calls.
- [Filter output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html): Control the format of the output from the AWS CLI.
- [Return Codes](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-returncodes.html): Understand the return codes provided by the AWS CLI.
- [Wizards](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-wizard.html): Use the wizard subcommand to guide you through the input for a command in the AWS Command Line Interface.
- [Aliases](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-alias.html): Aliases are shortcuts you can create in the AWS Command Line Interface to shorten commands or scripts that you frequently use.
- [Troubleshoot errors](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html): This section covers common errors and troubleshooting steps to follow to diagnose and fix a variety of AWS Command Line Interface errors you may encounter.


## [AWS CLI examples](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-code-examples.html)

### [Guided command examples](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-services.html)

See examples of using the AWS CLI to perform administrator and user tasks in AWS services.

- [DynamoDB](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-dynamodb.html): Learn how to use AWS Command Line Interface with the database service Amazon DynamoDB to access and run common operations.

### [Amazon EC2](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)

Use the AWS CLI to access the features of Amazon EC2.

- [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html): Use the AWS CLI to create, display, and delete your Amazon EC2 key pairs.
- [Amazon EC2 Security Groups](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html): Use the AWS CLI to create, add rules to, and delete your security groups
- [EC2 Instances](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html): Use the AWS CLI to launch, list, and terminate your Amazon EC2 instances.
- [Change EC2 type with bash scripting](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instance-type-script.html): Bash scripting example for Amazon EC2 using the AWS CLI.
- [Amazon Glacier](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-glacier.html): Use the AWS CLI to manage Amazon Glacier resources.
- [IAM](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html): Describes how to perform some common identity and access tasks using the AWS CLI.

### [Amazon S3](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html)

Use the two tiers of AWS CLI commands to access Amazon S3 for high-level operations and low-level advanced operations.

- [High-level (s3) commands](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html): Use the high-level Amazon S3 commands in the aws s3 namespace to manage buckets and objects using the AWS CLI.
- [API-level (s3 api) commands](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-apicommands.html): You can use the API-level aws s3api commands to perform any Amazon S3 API operation by using the AWS CLI.
- [Bucket lifecycle scripting example (s3api)](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-lifecycle-example.html): Bash scripting example for Amazon S3 using the AWS CLI.
- [Amazon SNS](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-sns.html): Perform some common topic tasks for Amazon SNS using the AWS CLI commands.

### [Command examples](https://docs.aws.amazon.com/cli/latest/userguide/cli_code_examples.html)

Code examples that show how to use AWS Command Line Interface with AWS.

- [ACM](https://docs.aws.amazon.com/cli/latest/userguide/cli_acm_code_examples.html): Code examples that show how to use AWS Command Line Interface with ACM.
- [API Gateway](https://docs.aws.amazon.com/cli/latest/userguide/cli_api-gateway_code_examples.html): Code examples that show how to use AWS Command Line Interface with API Gateway.
- [API Gateway HTTP and WebSocket API](https://docs.aws.amazon.com/cli/latest/userguide/cli_apigatewayv2_code_examples.html): Code examples that show how to use AWS Command Line Interface with API Gateway HTTP and WebSocket API.
- [API Gateway Management API](https://docs.aws.amazon.com/cli/latest/userguide/cli_apigatewaymanagementapi_code_examples.html): Code examples that show how to use AWS Command Line Interface with API Gateway Management API.
- [App Mesh](https://docs.aws.amazon.com/cli/latest/userguide/cli_app-mesh_code_examples.html): Code examples that show how to use AWS Command Line Interface with App Mesh.
- [App Runner](https://docs.aws.amazon.com/cli/latest/userguide/cli_apprunner_code_examples.html): Code examples that show how to use AWS Command Line Interface with App Runner.
- [AWS AppConfig](https://docs.aws.amazon.com/cli/latest/userguide/cli_appconfig_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS AppConfig.
- [Application Auto Scaling](https://docs.aws.amazon.com/cli/latest/userguide/cli_application-auto-scaling_code_examples.html): Code examples that show how to use AWS Command Line Interface with Application Auto Scaling.
- [Application Discovery Service](https://docs.aws.amazon.com/cli/latest/userguide/cli_application-discovery-service_code_examples.html): Code examples that show how to use AWS Command Line Interface with Application Discovery Service.
- [Application Signals](https://docs.aws.amazon.com/cli/latest/userguide/cli_application-signals_code_examples.html): Code examples that show how to use AWS Command Line Interface with Application Signals.
- [AppRegistry](https://docs.aws.amazon.com/cli/latest/userguide/cli_service-catalog-appregistry_code_examples.html): Code examples that show how to use AWS Command Line Interface with AppRegistry.
- [Athena](https://docs.aws.amazon.com/cli/latest/userguide/cli_athena_code_examples.html): Code examples that show how to use AWS Command Line Interface with Athena.
- [Auto Scaling](https://docs.aws.amazon.com/cli/latest/userguide/cli_auto-scaling_code_examples.html): Code examples that show how to use AWS Command Line Interface with Auto Scaling.
- [Auto Scaling Plans](https://docs.aws.amazon.com/cli/latest/userguide/cli_auto-scaling-plans_code_examples.html): Code examples that show how to use AWS Command Line Interface with Auto Scaling Plans.
- [AWS Backup](https://docs.aws.amazon.com/cli/latest/userguide/cli_backup_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Backup.
- [AWS Batch](https://docs.aws.amazon.com/cli/latest/userguide/cli_batch_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Batch.
- [AWS Budgets](https://docs.aws.amazon.com/cli/latest/userguide/cli_budgets_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Budgets.
- [Amazon Chime](https://docs.aws.amazon.com/cli/latest/userguide/cli_chime_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Chime.
- [Cloud Control API](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudcontrol_code_examples.html): Code examples that show how to use AWS Command Line Interface with Cloud Control API.
- [AWS Cloud Map](https://docs.aws.amazon.com/cli/latest/userguide/cli_servicediscovery_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Cloud Map.
- [AWS Cloud9](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloud9_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Cloud9.
- [CloudFormation](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudformation_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudFormation.
- [CloudFront](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudfront_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudFront.
- [Amazon CloudSearch](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudsearch-domain_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon CloudSearch.
- [CloudTrail](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudtrail_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudTrail.
- [CloudWatch](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudwatch_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudWatch.
- [CloudWatch Logs](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudWatch Logs.
- [CloudWatch Network Monitoring](https://docs.aws.amazon.com/cli/latest/userguide/cli_networkmonitor_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudWatch Network Monitoring.
- [CloudWatch Observability Access Monitor](https://docs.aws.amazon.com/cli/latest/userguide/cli_oam_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudWatch Observability Access Monitor.
- [CloudWatch Observability Admin](https://docs.aws.amazon.com/cli/latest/userguide/cli_observabilityadmin_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudWatch Observability Admin.
- [CloudWatch Synthetics](https://docs.aws.amazon.com/cli/latest/userguide/cli_synthetics_code_examples.html): Code examples that show how to use AWS Command Line Interface with CloudWatch Synthetics.
- [CodeArtifact](https://docs.aws.amazon.com/cli/latest/userguide/cli_codeartifact_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodeArtifact.
- [CodeBuild](https://docs.aws.amazon.com/cli/latest/userguide/cli_codebuild_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodeBuild.
- [CodeCommit](https://docs.aws.amazon.com/cli/latest/userguide/cli_codecommit_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodeCommit.
- [CodeDeploy](https://docs.aws.amazon.com/cli/latest/userguide/cli_codedeploy_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodeDeploy.
- [CodeGuru Reviewer](https://docs.aws.amazon.com/cli/latest/userguide/cli_codeguru-reviewer_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodeGuru Reviewer.
- [CodePipeline](https://docs.aws.amazon.com/cli/latest/userguide/cli_codepipeline_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodePipeline.
- [AWS CodeStar Notifications](https://docs.aws.amazon.com/cli/latest/userguide/cli_codestar-notifications_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS CodeStar Notifications.
- [CodeConnections](https://docs.aws.amazon.com/cli/latest/userguide/cli_codestar-connections_code_examples.html): Code examples that show how to use AWS Command Line Interface with CodeConnections.
- [Amazon Cognito Identity](https://docs.aws.amazon.com/cli/latest/userguide/cli_cognito-identity_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Cognito Identity.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/cli/latest/userguide/cli_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Cognito Identity Provider.
- [Amazon Comprehend](https://docs.aws.amazon.com/cli/latest/userguide/cli_comprehend_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Comprehend.
- [Amazon Comprehend Medical](https://docs.aws.amazon.com/cli/latest/userguide/cli_comprehendmedical_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Comprehend Medical.
- [AWS Config](https://docs.aws.amazon.com/cli/latest/userguide/cli_config-service_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Config.
- [Amazon Connect](https://docs.aws.amazon.com/cli/latest/userguide/cli_connect_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Connect.
- [AWS Cost and Usage Report](https://docs.aws.amazon.com/cli/latest/userguide/cli_cost-and-usage-report-service_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Cost and Usage Report.
- [Cost Explorer Service](https://docs.aws.amazon.com/cli/latest/userguide/cli_cost-explorer_code_examples.html): Code examples that show how to use AWS Command Line Interface with Cost Explorer Service.
- [Firehose](https://docs.aws.amazon.com/cli/latest/userguide/cli_firehose_code_examples.html): Code examples that show how to use AWS Command Line Interface with Firehose.
- [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_dlm_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Data Lifecycle Manager.
- [AWS Data Pipeline](https://docs.aws.amazon.com/cli/latest/userguide/cli_data-pipeline_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Data Pipeline.
- [DataSync](https://docs.aws.amazon.com/cli/latest/userguide/cli_datasync_code_examples.html): Code examples that show how to use AWS Command Line Interface with DataSync.
- [DAX](https://docs.aws.amazon.com/cli/latest/userguide/cli_dax_code_examples.html): Code examples that show how to use AWS Command Line Interface with DAX.
- [Detective](https://docs.aws.amazon.com/cli/latest/userguide/cli_detective_code_examples.html): Code examples that show how to use AWS Command Line Interface with Detective.
- [Device Farm](https://docs.aws.amazon.com/cli/latest/userguide/cli_device-farm_code_examples.html): Code examples that show how to use AWS Command Line Interface with Device Farm.
- [Direct Connect](https://docs.aws.amazon.com/cli/latest/userguide/cli_direct-connect_code_examples.html): Code examples that show how to use AWS Command Line Interface with Direct Connect.
- [Directory Service](https://docs.aws.amazon.com/cli/latest/userguide/cli_directory-service_code_examples.html): Code examples that show how to use AWS Command Line Interface with Directory Service.
- [Directory Service Data](https://docs.aws.amazon.com/cli/latest/userguide/cli_directory-service-data_code_examples.html): Code examples that show how to use AWS Command Line Interface with Directory Service Data.
- [AWS DMS](https://docs.aws.amazon.com/cli/latest/userguide/cli_database-migration-service_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS DMS.
- [Amazon DocumentDB](https://docs.aws.amazon.com/cli/latest/userguide/cli_docdb_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon DocumentDB.
- [DynamoDB](https://docs.aws.amazon.com/cli/latest/userguide/cli_dynamodb_code_examples.html): Code examples that show how to use AWS Command Line Interface with DynamoDB.
- [DynamoDB Streams](https://docs.aws.amazon.com/cli/latest/userguide/cli_dynamodb-streams_code_examples.html): Code examples that show how to use AWS Command Line Interface with DynamoDB Streams.
- [Amazon EC2](https://docs.aws.amazon.com/cli/latest/userguide/cli_ec2_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon EC2.
- [Amazon EC2 Instance Connect](https://docs.aws.amazon.com/cli/latest/userguide/cli_ec2-instance-connect_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon EC2 Instance Connect.
- [Amazon ECR](https://docs.aws.amazon.com/cli/latest/userguide/cli_ecr_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon ECR.
- [Amazon ECR Public](https://docs.aws.amazon.com/cli/latest/userguide/cli_ecr-public_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon ECR Public.
- [Amazon ECS](https://docs.aws.amazon.com/cli/latest/userguide/cli_ecs_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon ECS.
- [Amazon EFS](https://docs.aws.amazon.com/cli/latest/userguide/cli_efs_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon EFS.
- [Amazon EKS](https://docs.aws.amazon.com/cli/latest/userguide/cli_eks_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon EKS.
- [Elastic Beanstalk](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-beanstalk_code_examples.html): Code examples that show how to use AWS Command Line Interface with Elastic Beanstalk.
- [Elastic Load Balancing - Version 1](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-load-balancing_code_examples.html): Code examples that show how to use AWS Command Line Interface with Elastic Load Balancing - Version 1.
- [Elastic Load Balancing - Version 2](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-load-balancing-v2_code_examples.html): Code examples that show how to use AWS Command Line Interface with Elastic Load Balancing - Version 2.
- [ElastiCache](https://docs.aws.amazon.com/cli/latest/userguide/cli_elasticache_code_examples.html): Code examples that show how to use AWS Command Line Interface with ElastiCache.
- [MediaStore](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediastore_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaStore.
- [Amazon EMR](https://docs.aws.amazon.com/cli/latest/userguide/cli_emr_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon EMR.
- [Amazon EMR on EKS](https://docs.aws.amazon.com/cli/latest/userguide/cli_emr-containers_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon EMR on EKS.
- [EventBridge](https://docs.aws.amazon.com/cli/latest/userguide/cli_eventbridge_code_examples.html): Code examples that show how to use AWS Command Line Interface with EventBridge.
- [EventBridge Pipes](https://docs.aws.amazon.com/cli/latest/userguide/cli_pipes_code_examples.html): Code examples that show how to use AWS Command Line Interface with EventBridge Pipes.
- [Firewall Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_fms_code_examples.html): Code examples that show how to use AWS Command Line Interface with Firewall Manager.
- [AWS FIS](https://docs.aws.amazon.com/cli/latest/userguide/cli_fis_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS FIS.
- [Amazon GameLift Servers](https://docs.aws.amazon.com/cli/latest/userguide/cli_gamelift_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon GameLift Servers.
- [Amazon Glacier](https://docs.aws.amazon.com/cli/latest/userguide/cli_glacier_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Glacier.
- [Global Accelerator](https://docs.aws.amazon.com/cli/latest/userguide/cli_global-accelerator_code_examples.html): Code examples that show how to use AWS Command Line Interface with Global Accelerator.
- [AWS Glue](https://docs.aws.amazon.com/cli/latest/userguide/cli_glue_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Glue.
- [GuardDuty](https://docs.aws.amazon.com/cli/latest/userguide/cli_guardduty_code_examples.html): Code examples that show how to use AWS Command Line Interface with GuardDuty.
- [AWS Health](https://docs.aws.amazon.com/cli/latest/userguide/cli_health_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Health.
- [HealthImaging](https://docs.aws.amazon.com/cli/latest/userguide/cli_medical-imaging_code_examples.html): Code examples that show how to use AWS Command Line Interface with HealthImaging.
- [HealthLake](https://docs.aws.amazon.com/cli/latest/userguide/cli_healthlake_code_examples.html): Code examples that show how to use AWS Command Line Interface with HealthLake.
- [HealthOmics](https://docs.aws.amazon.com/cli/latest/userguide/cli_omics_code_examples.html): Code examples that show how to use AWS Command Line Interface with HealthOmics.
- [IAM](https://docs.aws.amazon.com/cli/latest/userguide/cli_iam_code_examples.html): Code examples that show how to use AWS Command Line Interface with IAM.
- [IAM Access Analyzer](https://docs.aws.amazon.com/cli/latest/userguide/cli_accessanalyzer_code_examples.html): Code examples that show how to use AWS Command Line Interface with IAM Access Analyzer.
- [Image Builder](https://docs.aws.amazon.com/cli/latest/userguide/cli_imagebuilder_code_examples.html): Code examples that show how to use AWS Command Line Interface with Image Builder.
- [Incident Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm-incidents_code_examples.html): Code examples that show how to use AWS Command Line Interface with Incident Manager.
- [Incident Manager Contacts](https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm-contacts_code_examples.html): Code examples that show how to use AWS Command Line Interface with Incident Manager Contacts.
- [Amazon Inspector](https://docs.aws.amazon.com/cli/latest/userguide/cli_inspector2_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Inspector.
- [AWS IoT](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT.
- [Device Advisor](https://docs.aws.amazon.com/cli/latest/userguide/cli_iotdeviceadvisor_code_examples.html): Code examples that show how to use AWS Command Line Interface with Device Advisor.
- [AWS IoT data](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-data-plane_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT data.
- [AWS IoT Events](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-events_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Events.
- [AWS IoT Events-Data](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-events-data_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Events-Data.
- [AWS IoT Greengrass](https://docs.aws.amazon.com/cli/latest/userguide/cli_greengrass_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Greengrass.
- [AWS IoT Greengrass V2](https://docs.aws.amazon.com/cli/latest/userguide/cli_greengrassv2_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Greengrass V2.
- [AWS IoT Jobs SDK release](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-jobs-data-plane_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Jobs SDK release.
- [AWS IoT SiteWise](https://docs.aws.amazon.com/cli/latest/userguide/cli_iotsitewise_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT SiteWise.
- [AWS IoT Things Graph](https://docs.aws.amazon.com/cli/latest/userguide/cli_iotthingsgraph_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Things Graph.
- [AWS IoT Wireless](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-wireless_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS IoT Wireless.
- [Amazon IVS](https://docs.aws.amazon.com/cli/latest/userguide/cli_ivs_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon IVS.
- [Amazon IVS Chat](https://docs.aws.amazon.com/cli/latest/userguide/cli_ivschat_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon IVS Chat.
- [Amazon IVS Real-Time Streaming](https://docs.aws.amazon.com/cli/latest/userguide/cli_ivs-realtime_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon IVS Real-Time Streaming.
- [Amazon Kendra](https://docs.aws.amazon.com/cli/latest/userguide/cli_kendra_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Kendra.
- [Kinesis](https://docs.aws.amazon.com/cli/latest/userguide/cli_kinesis_code_examples.html): Code examples that show how to use AWS Command Line Interface with Kinesis.
- [AWS KMS](https://docs.aws.amazon.com/cli/latest/userguide/cli_kms_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS KMS.
- [Lake Formation](https://docs.aws.amazon.com/cli/latest/userguide/cli_lakeformation_code_examples.html): Code examples that show how to use AWS Command Line Interface with Lake Formation.
- [Lambda](https://docs.aws.amazon.com/cli/latest/userguide/cli_lambda_code_examples.html): Code examples that show how to use AWS Command Line Interface with Lambda.
- [License Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_license-manager_code_examples.html): Code examples that show how to use AWS Command Line Interface with License Manager.
- [Lightsail](https://docs.aws.amazon.com/cli/latest/userguide/cli_lightsail_code_examples.html): Code examples that show how to use AWS Command Line Interface with Lightsail.
- [Macie](https://docs.aws.amazon.com/cli/latest/userguide/cli_macie2_code_examples.html): Code examples that show how to use AWS Command Line Interface with Macie.
- [Amazon Managed Grafana](https://docs.aws.amazon.com/cli/latest/userguide/cli_grafana_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Managed Grafana.
- [MediaConnect](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediaconnect_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaConnect.
- [MediaConvert](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediaconvert_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaConvert.
- [MediaLive](https://docs.aws.amazon.com/cli/latest/userguide/cli_medialive_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaLive.
- [MediaPackage](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediapackage_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaPackage.
- [MediaPackage VOD](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediapackage-vod_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaPackage VOD.
- [MediaStore Data Plane](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediastore-data_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaStore Data Plane.
- [MediaTailor](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediatailor_code_examples.html): Code examples that show how to use AWS Command Line Interface with MediaTailor.
- [MemoryDB](https://docs.aws.amazon.com/cli/latest/userguide/cli_memorydb_code_examples.html): Code examples that show how to use AWS Command Line Interface with MemoryDB.
- [Amazon MSK](https://docs.aws.amazon.com/cli/latest/userguide/cli_kafka_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon MSK.
- [Network Flow Monitor](https://docs.aws.amazon.com/cli/latest/userguide/cli_networkflowmonitor_code_examples.html): Code examples that show how to use AWS Command Line Interface with Network Flow Monitor.
- [Network Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_networkmanager_code_examples.html): Code examples that show how to use AWS Command Line Interface with Network Manager.
- [OpenSearch Service](https://docs.aws.amazon.com/cli/latest/userguide/cli_elasticsearch-service_code_examples.html): Code examples that show how to use AWS Command Line Interface with OpenSearch Service.
- [Organizations](https://docs.aws.amazon.com/cli/latest/userguide/cli_organizations_code_examples.html): Code examples that show how to use AWS Command Line Interface with Organizations.
- [AWS Outposts](https://docs.aws.amazon.com/cli/latest/userguide/cli_outposts_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Outposts.
- [AWS Payment Cryptography](https://docs.aws.amazon.com/cli/latest/userguide/cli_payment-cryptography_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Payment Cryptography.
- [AWS Payment Cryptography Data Plane](https://docs.aws.amazon.com/cli/latest/userguide/cli_payment-cryptography-data_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Payment Cryptography Data Plane.
- [Amazon Pinpoint](https://docs.aws.amazon.com/cli/latest/userguide/cli_pinpoint_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Pinpoint.
- [Amazon Polly](https://docs.aws.amazon.com/cli/latest/userguide/cli_polly_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Polly.
- [AWS Price List](https://docs.aws.amazon.com/cli/latest/userguide/cli_pricing_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Price List.
- [AWS Private CA](https://docs.aws.amazon.com/cli/latest/userguide/cli_acm-pca_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Private CA.
- [AWS Proton](https://docs.aws.amazon.com/cli/latest/userguide/cli_proton_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Proton.
- [Amazon RDS](https://docs.aws.amazon.com/cli/latest/userguide/cli_rds_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/cli/latest/userguide/cli_rds-data_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon RDS Data Service.
- [Amazon RDS Performance Insights](https://docs.aws.amazon.com/cli/latest/userguide/cli_pi_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon RDS Performance Insights.
- [Amazon Redshift](https://docs.aws.amazon.com/cli/latest/userguide/cli_redshift_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Redshift.
- [Amazon Rekognition](https://docs.aws.amazon.com/cli/latest/userguide/cli_rekognition_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Rekognition.
- [AWS RAM](https://docs.aws.amazon.com/cli/latest/userguide/cli_ram_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS RAM.
- [Resource Explorer](https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-explorer-2_code_examples.html): Code examples that show how to use AWS Command Line Interface with Resource Explorer.
- [Resource Groups](https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-groups_code_examples.html): Code examples that show how to use AWS Command Line Interface with Resource Groups.
- [Resource Groups Tagging API](https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-groups-tagging-api_code_examples.html): Code examples that show how to use AWS Command Line Interface with Resource Groups Tagging API.
- [RouteÂ 53](https://docs.aws.amazon.com/cli/latest/userguide/cli_route-53_code_examples.html): Code examples that show how to use AWS Command Line Interface with RouteÂ 53.
- [RouteÂ 53 domain registration](https://docs.aws.amazon.com/cli/latest/userguide/cli_route-53-domains_code_examples.html): Code examples that show how to use AWS Command Line Interface with RouteÂ 53 domain registration.
- [Route 53 Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli_route53profiles_code_examples.html): Code examples that show how to use AWS Command Line Interface with Route 53 Profiles.
- [RouteÂ 53 Resolver](https://docs.aws.amazon.com/cli/latest/userguide/cli_route53resolver_code_examples.html): Code examples that show how to use AWS Command Line Interface with RouteÂ 53 Resolver.
- [Amazon S3](https://docs.aws.amazon.com/cli/latest/userguide/cli_s3_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon S3.
- [Amazon S3 Control](https://docs.aws.amazon.com/cli/latest/userguide/cli_s3-control_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon S3 Control.
- [Secrets Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_secrets-manager_code_examples.html): Code examples that show how to use AWS Command Line Interface with Secrets Manager.
- [Security Hub CSPM](https://docs.aws.amazon.com/cli/latest/userguide/cli_securityhub_code_examples.html): Code examples that show how to use AWS Command Line Interface with Security Hub CSPM.
- [Security Lake](https://docs.aws.amazon.com/cli/latest/userguide/cli_securitylake_code_examples.html): Code examples that show how to use AWS Command Line Interface with Security Lake.
- [AWS Serverless Application Repository](https://docs.aws.amazon.com/cli/latest/userguide/cli_serverlessapplicationrepository_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS Serverless Application Repository.
- [Service Catalog](https://docs.aws.amazon.com/cli/latest/userguide/cli_service-catalog_code_examples.html): Code examples that show how to use AWS Command Line Interface with Service Catalog.
- [Service Quotas](https://docs.aws.amazon.com/cli/latest/userguide/cli_service-quotas_code_examples.html): Code examples that show how to use AWS Command Line Interface with Service Quotas.
- [Amazon SES](https://docs.aws.amazon.com/cli/latest/userguide/cli_ses_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon SES.
- [Shield](https://docs.aws.amazon.com/cli/latest/userguide/cli_shield_code_examples.html): Code examples that show how to use AWS Command Line Interface with Shield.
- [Signer](https://docs.aws.amazon.com/cli/latest/userguide/cli_signer_code_examples.html): Code examples that show how to use AWS Command Line Interface with Signer.
- [Snowball Edge](https://docs.aws.amazon.com/cli/latest/userguide/cli_snowball_code_examples.html): Code examples that show how to use AWS Command Line Interface with Snowball Edge.
- [Amazon SNS](https://docs.aws.amazon.com/cli/latest/userguide/cli_sns_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/cli/latest/userguide/cli_sqs_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon SQS.
- [Storage Gateway](https://docs.aws.amazon.com/cli/latest/userguide/cli_storage-gateway_code_examples.html): Code examples that show how to use AWS Command Line Interface with Storage Gateway.
- [AWS STS](https://docs.aws.amazon.com/cli/latest/userguide/cli_sts_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS STS.
- [Support](https://docs.aws.amazon.com/cli/latest/userguide/cli_support_code_examples.html): Code examples that show how to use AWS Command Line Interface with Support.
- [Amazon SWF](https://docs.aws.amazon.com/cli/latest/userguide/cli_swf_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon SWF.
- [Systems Manager](https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm_code_examples.html): Code examples that show how to use AWS Command Line Interface with Systems Manager.
- [Amazon Textract](https://docs.aws.amazon.com/cli/latest/userguide/cli_textract_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Textract.
- [Amazon Transcribe](https://docs.aws.amazon.com/cli/latest/userguide/cli_transcribe_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Transcribe.
- [Amazon Translate](https://docs.aws.amazon.com/cli/latest/userguide/cli_translate_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon Translate.
- [Trusted Advisor](https://docs.aws.amazon.com/cli/latest/userguide/cli_trustedadvisor_code_examples.html): Code examples that show how to use AWS Command Line Interface with Trusted Advisor.
- [Verified Permissions](https://docs.aws.amazon.com/cli/latest/userguide/cli_verifiedpermissions_code_examples.html): Code examples that show how to use AWS Command Line Interface with Verified Permissions.
- [VPC Lattice](https://docs.aws.amazon.com/cli/latest/userguide/cli_vpc-lattice_code_examples.html): Code examples that show how to use AWS Command Line Interface with VPC Lattice.
- [AWS WAF Classic](https://docs.aws.amazon.com/cli/latest/userguide/cli_waf_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS WAF Classic.
- [AWS WAF Classic Regional](https://docs.aws.amazon.com/cli/latest/userguide/cli_waf-regional_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS WAF Classic Regional.
- [AWS WAFV2](https://docs.aws.amazon.com/cli/latest/userguide/cli_wafv2_code_examples.html): Code examples that show how to use AWS Command Line Interface with AWS WAFV2.
- [WorkDocs](https://docs.aws.amazon.com/cli/latest/userguide/cli_workdocs_code_examples.html): Code examples that show how to use AWS Command Line Interface with WorkDocs.
- [Amazon WorkMail](https://docs.aws.amazon.com/cli/latest/userguide/cli_workmail_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon WorkMail.
- [Amazon WorkMail Message Flow](https://docs.aws.amazon.com/cli/latest/userguide/cli_workmailmessageflow_code_examples.html): Code examples that show how to use AWS Command Line Interface with Amazon WorkMail Message Flow.
- [WorkSpaces](https://docs.aws.amazon.com/cli/latest/userguide/cli_workspaces_code_examples.html): Code examples that show how to use AWS Command Line Interface with WorkSpaces.
- [X-Ray](https://docs.aws.amazon.com/cli/latest/userguide/cli_xray_code_examples.html): Code examples that show how to use AWS Command Line Interface with X-Ray.

### [Bash script examples](https://docs.aws.amazon.com/cli/latest/userguide/bash_code_examples.html)

Code examples that show how to use AWS Command Line Interface with Bash script with AWS.

- [AWS Batch](https://docs.aws.amazon.com/cli/latest/userguide/bash_batch_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with AWS Batch.
- [AWS Cloud Map](https://docs.aws.amazon.com/cli/latest/userguide/bash_servicediscovery_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with AWS Cloud Map.
- [CloudFront](https://docs.aws.amazon.com/cli/latest/userguide/bash_cloudfront_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with CloudFront.
- [DynamoDB](https://docs.aws.amazon.com/cli/latest/userguide/bash_dynamodb_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/cli/latest/userguide/bash_ec2_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with Amazon EC2.
- [HealthImaging](https://docs.aws.amazon.com/cli/latest/userguide/bash_medical-imaging_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with HealthImaging.
- [IAM](https://docs.aws.amazon.com/cli/latest/userguide/bash_iam_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with IAM.
- [AWS KMS](https://docs.aws.amazon.com/cli/latest/userguide/bash_kms_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with AWS KMS.
- [Lightsail](https://docs.aws.amazon.com/cli/latest/userguide/bash_lightsail_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with Lightsail.
- [Amazon S3](https://docs.aws.amazon.com/cli/latest/userguide/bash_s3_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with Amazon S3.
- [AWS STS](https://docs.aws.amazon.com/cli/latest/userguide/bash_sts_code_examples.html): Code examples that show how to use AWS Command Line Interface with Bash script with AWS STS.


## [Security](https://docs.aws.amazon.com/cli/latest/userguide/security.html)

- [Data Protection](https://docs.aws.amazon.com/cli/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection when using the AWS CLI.
- [Identity and Access Management](https://docs.aws.amazon.com/cli/latest/userguide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/cli/latest/userguide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/cli/latest/userguide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/cli/latest/userguide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforcing a minimum TLS version](https://docs.aws.amazon.com/cli/latest/userguide/cli-security-enforcing-tls.html): Learn how to enforce a minimum version of TLS 1.2 for the AWS CLI.


## [Migration guide](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html)

- [New features and changes](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration-changes.html): Learn about new features and changes in behavior between AWS CLI version 1 and AWS CLI version 2.
- [Migration instructions](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration-instructions.html): Learn how to migrate from AWS CLI version 1 to AWS CLI version 2.
- [Using upgrade debug mode](https://docs.aws.amazon.com/cli/latest/userguide/cli-upgrade-debug-mode.html): Learn how to use upgrade debug mode to identify and resolve breaking changes when migrating from AWS CLI version 1 to version 2.
- [Using AWS CLI v1-to-v2 Migration Tool](https://docs.aws.amazon.com/cli/latest/userguide/cli-migration-tool.html): Learn how to use AWS CLI v1-to-v2 Migration Tool to detect and update AWS CLI commands in bash scripts to prevent breakage from changes introduced in AWS version 2.
