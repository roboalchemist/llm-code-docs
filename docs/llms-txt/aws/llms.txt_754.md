# Source: https://docs.aws.amazon.com/secretsmanager/latest/userguide/llms.txt

# AWS Secrets Manager User Guide

> Walks you through creating and managing your secrets, retrieving them in your application, and automatically rotating them to help keep them secure.

- [What is Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [Access Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/asm_access.html)
- [Best practices](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [AWS CDK](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cdk.html)
- [Compliance validation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/secretsmanager-compliance.html)
- [Troubleshooting](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html)
- [Quotas](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_limits.html)
- [Document history](https://docs.aws.amazon.com/secretsmanager/latest/userguide/document-history.html)

## [Tutorials](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials.html)

- [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-codeguru.html): Learn how to use CodeGuru Reviewer to find unprotected secrets in your Java and Python code.
- [Replace hardcoded secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded.html): Replace hardcoded secrets in your code with AWS Secrets Manager secrets.
- [Replace hardcoded DB credentials](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded-db-creds.html): Learn how to replace hardcoded credentials with AWS Secrets Manager secrets.
- [Alternating users rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_rotation-alternating.html): Learn how to set up automatic rotation for database credentials.
- [Single user rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_rotation-single.html): Learn how to set up automatic rotation for database credentials.


## [Create secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html)

- [What's in a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/whats-in-a-secret.html): Describes the components of a Secrets Manager secret.
- [JSON structure of a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_secret_json_structure.html): Learn what to store in a secret.


## [Manage secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html)

- [Update a secret value](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret-value.html): Learn how to update AWS Secrets Manager secrets.
- [Generate a password with Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/generate-password.html): A common pattern for using Secrets Manager is to generate a password in Secrets Manager and then use that password in your database or service.
- [Roll back a secret to a previous version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/roll-back-secret.html): Learn how to roll back an AWS Secrets Manager secret to a previous version.
- [Change the encryption key for a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-encryption-key.html): Learn how to change the encryption key for an AWS Secrets Manager secret.
- [Modify a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html): Learn how you can update a secret.
- [Find secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html): Learn how to find secrets using a variety of filters, including name and the service that manages the secret.
- [Delete a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html): Learn how to delete a secret.
- [Restore a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_restore-secret.html): In Secrets Manager, restore a secret that was scheduled to be deleted.
- [Tag secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html): Learn how to use tags to organize and manage your secrets in AWS Secrets Manager.


## [Multi-region replication](https://docs.aws.amazon.com/secretsmanager/latest/userguide/replicate-secrets.html)

- [Promote a replica secret to a standalone secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/standalone-secret.html): Learn how to promote a replica secret to a standalone secret.
- [Prevent replication](https://docs.aws.amazon.com/secretsmanager/latest/userguide/replicate-secrets-permissions.html): Learn how to prevent users from replicating secrets to other Regions in AWS Secrets Manager.
- [Troubleshoot replication](https://docs.aws.amazon.com/secretsmanager/latest/userguide/replicate-secrets_troubleshoot.html): Troubleshoot issues with AWS Secrets Manager secret replication.


## [Get secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html)

### [Java](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-java.html)

In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Java with client-side caching](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-java.html)

In Secrets Manager, retrieve secrets in Java applications.

- [SecretCache](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-java-ref_SecretCache.html): An in-memory cache for secrets requested from Secrets Manager.
- [SecretCacheConfiguration](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-java-ref_SecretCacheConfiguration.html): Cache configuration options for a , such as max cache size and Time to Live (TTL) for cached secrets.
- [SecretCacheHook](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-java-ref_SecretCacheHook.html): An interface to hook into a to perform actions on the secrets being stored in the cache.
- [JDBC connection with credentials in a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_jdbc.html): Use JDBC to connect to a database using credentials stored in a secret.
- [Java AWS SDK](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-java-sdk.html): In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Python](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-python.html)

In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Python with client-side caching](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-python.html)

In Secrets Manager, retrieve secrets in Python applications.

- [SecretCache](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-ref-secretcache.html): An in-memory cache for secrets retrieved from Secrets Manager.
- [SecretCacheConfig](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-ref-secretcacheconfig.html): Cache configuration options for a such as max cache size and Time to Live (TTL) for cached secrets.
- [SecretCacheHook](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-ref-secretcachehook.html): An interface to hook into a to perform actions on the secrets being stored in the cache.
- [@InjectSecretString](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-decor-string.html): This decorator expects a secret ID string and as the first and second arguments.
- [@InjectKeywordedSecretString](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-decor-keyword.html): This decorator expects a secret ID string and as the first and second arguments.
- [Python AWS SDK](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-python-sdk.html): In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.
- [Get a batch of secret values](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-python-batch.html): The following code example shows how to get a batch of Secrets Manager secret values.

### [.NET](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-net.html)

In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [.NET with client-side caching](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-net.html)

Learn how to retrieve secrets in .NET applications.

- [SecretsManagerCache](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-net-SecretsManagerCache.html): An in-memory cache for secrets requested from Secrets Manager.
- [SecretCacheConfiguration](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-net-SecretCacheConfiguration.html): Cache configuration options for a , such as maximum cache size and Time to Live (TTL) for cached secrets.
- [ISecretCacheHook](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-net-ISecretCacheHook.html): An interface to hook into a to perform actions on the secrets being stored in the cache.
- [SDK for .NET](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-net-sdk.html): In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Go](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-go.html)

In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Go with client-side caching](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-go.html)

In Secrets Manager, retrieve secrets in Go applications.

- [type Cache](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-go_cache.html): An in-memory cache for secrets requested from Secrets Manager.
- [type CacheConfig](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-go_CacheConfig.html): Cache configuration options for a Cache, such as maximum cache size, default version stage, and Time to Live (TTL) for cached secrets.
- [type CacheHook](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-go_CacheHook.html): An interface to hook into a Cache to perform actions on the secret being stored in the cache.
- [Go AWS SDK](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-go-sdk.html): In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Rust](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-rust.html)

In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

- [Rust with client-side caching](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-rust.html): In Secrets Manager, retrieve secrets in Rust applications.
- [Rust](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-rust-sdk.html): In applications, you can retrieve your secrets by calling GetSecretValue or BatchGetSecretValuein any of the AWS SDKs.

### [Amazon EKS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrate_eks.html)

Learn about different approaches to integrate secrets with Amazon EKS and when to use each method.

- [Install ASCP for Amazon EKS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/ascp-eks-installation.html): Learn how to install and configure AWS Secrets and Configuration Provider for Amazon Elastic Kubernetes Service.
- [Integrate ASCP with Pod Identity for Amazon EKS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/ascp-pod-identity-integration.html): Learn how to retrieve secrets from Secrets Manager to use in your Amazon EKS Pods using Pod Identity.
- [Integrate ASCP with IRSA for Amazon EKS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ascp_irsa.html): Learn how to retrieve secrets from Secrets Manager to use in your Amazon EKS Pods.
- [ASCP examples](https://docs.aws.amazon.com/secretsmanager/latest/userguide/ascp-examples.html): Use these code examples to help you integrate ASCP with your Amazon EKS clusters.
- [AWS Lambda](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html): In Secrets Manager, access secrets in Lambda functions.
- [Secrets Manager Agent](https://docs.aws.amazon.com/secretsmanager/latest/userguide/secrets-manager-agent.html): Learn how to use the AWS Secrets Manager Agent to standardize and secure secret consumption across your AWS compute environments.
- [C++](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-cpp.html): For C++ applications, call the SDK directly with GetSecretValue or BatchGetSecretValue.
- [JavaScript](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-javascript.html): For JavaScript applications, call the SDK directly with getSecretValue or batchGetSecretValue.
- [Kotlin](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-kotlin.html): For Kotlin applications, call the SDK directly with GetSecretValue or BatchGetSecretValue.
- [PHP](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-php.html): For PHP applications, call the SDK directly with GetSecretValue or BatchGetSecretValue.
- [Ruby](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-ruby.html): For Ruby applications, call the SDK directly with get_secret_value or batch_get_secret_value.
- [AWS CLI](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cli.html): Required permissions: secretsmanager:GetSecretValue
- [AWS console](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-console.html)
- [AWS Batch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_BATCH.html): Learn how to access secrets in AWS Batch.
- [CloudFormation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_reference-secret.html): Create secrets using an AWS CloudFormation template.
- [GitHub jobs](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_github.html): In Secrets Manager, access secrets in GitHub jobs.
- [GitLab](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_gitlab.html): Learn how to integrate AWS Secrets Manager with GitLab to protect your credentials in CI/CD pipelines.
- [AWS IoT Greengrass](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-greengrass.html): Learn how to access secrets in AWS IoT Greengrass.
- [Parameter Store](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_parameterstore.html): Learn how to access secrets in Parameter Store.


## [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

- [Managed rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html): Learn how to set up automatic rotation for secrets that are managed by other services.
- [Rotate managed external secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_external.html): Learn how to rotate Secrets Manager managed external secrets.

### [Rotation by Lambda function](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda.html)

Learn how to rotate AWS Secrets Manager secrets using Lambda functions.

- [Automatic rotation for database secrets (console)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-db.html): Learn how to set up automatic rotation for database credentials using the console.
- [Automatic rotation for non-database secrets (console)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.html): Learn how to set up automatic rotation for secrets using the console.
- [Automatic rotation (AWS CLI)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-cli.html): Learn how to schedule automatic rotation for secrets.
- [Lambda function rotation strategies](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotation-strategy.html): In Secrets Manager, there are two strategies for rotating secrets.
- [Lambda rotation functions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda-functions.html): Learn how rotation functions work for AWS Secrets Manager.
- [Rotation function templates](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-rotation-templates.html): Learn about rotation function templates provided by Secrets Manager.
- [Permissions for rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-required-permissions-function.html): Learn how to set up automatic rotation for secrets.
- [Network access for AWS Lambda rotation function](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotation-function-network-access.html): Learn about the network access required to rotate Secrets Manager secrets.
- [Troubleshoot rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_rotation.html): Diagnose and fix issues that you might encounter when you're rotating AWS Secrets Manager secrets.
- [Rotation schedules](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html): Learn how to schedule automatic rotation for secrets.
- [Rotate a secret immediately](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_now.html): In Secrets Manager, you can rotate secrets immediately.
- [Find secrets that aren't rotated](https://docs.aws.amazon.com/secretsmanager/latest/userguide/find-secrets-not-rotating.html): Learn how to find AWS Secrets Manager secrets that aren't being rotated.
- [Cancel automatic rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cancel-automatic-rotation.html): Learn how to cancel automatic rotation for secrets.


## [Secrets managed by other services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html)

### [Services that use secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating.html)

Describes how AWS services use AWS Secrets Manager secrets.

- [App Runner](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_ARlong.html): Describes how AWS App Runner uses AWS Secrets Manager secrets.
- [AWS App2Container](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_App2Container.html): Describes how AWS App2Container uses AWS Secrets Manager secrets.
- [AWS AppConfig](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_APPC.html): Describes how AWS AppConfig uses AWS Secrets Manager secrets.
- [Amazon AppFlow](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_appflow.html): Describes how Amazon AppFlow uses AWS Secrets Manager secrets.
- [AWS AppSync](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_APSYlong.html): Describes how AWS AppSync uses AWS Secrets Manager secrets.
- [Amazon Athena](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_ATElong.html): Describes how Amazon Athena uses AWS Secrets Manager secrets.
- [Amazon Aurora](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-AUR.html): Describes how Amazon Aurora uses AWS Secrets Manager secrets.
- [AWS CodeBuild](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-codebuild.html): Describes how AWS CodeBuild uses AWS Secrets Manager secrets.
- [Amazon Data Firehose](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_AKF.html): Describes how Amazon Data Firehose uses AWS Secrets Manager secrets.
- [AWS DataSync](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_datasync.html): Describes how AWS DataSync uses AWS Secrets Manager secrets.
- [Amazon DataZone](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_datazone.html): Describes how Amazon DataZone uses AWS Secrets Manager secrets.
- [Direct Connect](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_directconnect.html): Describes how AWS Direct Connect uses AWS Secrets Manager secrets.
- [AWS Directory Service](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_Dir.html): Describes how Directory Service uses AWS Secrets Manager secrets.
- [Amazon DocumentDB](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_DocDBlong.html): Describes how Amazon DocumentDB (with MongoDB compatibility) uses AWS Secrets Manager secrets.
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_AEB.html): Describes how AWS Elastic Beanstalk uses AWS Secrets Manager secrets.
- [Amazon Elastic Container Registry](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ECR.html): Describes how Amazon ECR uses AWS Secrets Manager secrets.
- [Amazon Elastic Container Service](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_ecs-sc.html): Describes how Amazon ECS uses AWS Secrets Manager secrets.
- [Amazon ElastiCache](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ELC.html): Describes how Amazon ElastiCache uses AWS Secrets Manager secrets.
- [AWS Elemental Live](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ELVlong.html): Describes how AWS Elemental Live uses AWS Secrets Manager secrets.
- [AWS Elemental MediaConnect](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_EMXlong.html): Describes how AWS Elemental MediaConnect uses AWS Secrets Manager secrets.
- [AWS Elemental MediaConvert](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_EMClong.html): Describes how AWS Elemental MediaConvert uses AWS Secrets Manager secrets.
- [AWS Elemental MediaLive](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_EML.html): Describes how AWS Elemental MediaLive uses AWS Secrets Manager secrets.
- [AWS Elemental MediaPackage](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_EMPlong.html): Describes how AWS Elemental MediaPackage uses AWS Secrets Manager secrets.
- [AWS Elemental MediaTailor](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_MediaTailor.html): Describes how AWS Elemental MediaTailor uses AWS Secrets Manager secrets.
- [Amazon EMR](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-emr.html): Describes how Amazon EMR uses AWS Secrets Manager secrets.
- [Amazon EventBridge](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_events.html): Describes how Amazon EventBridge uses AWS Secrets Manager secrets.
- [Amazon FSx](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_FSx.html): Describes how Amazon FSx uses AWS Secrets Manager secrets.
- [AWS Glue DataBrew](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_databrew.html): Describes how AWS Glue DataBrew uses AWS Secrets Manager secrets.
- [AWS Glue Studio](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_glue.html): Describes how AWS Glue Studio uses AWS Secrets Manager secrets.
- [AWS IoT SiteWise](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_iotsitewise.html): Describes how AWS IoT SiteWise uses AWS Secrets Manager secrets.
- [Amazon Kendra](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_KEN.html): Describes how Amazon Kendra uses AWS Secrets Manager secrets.
- [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_AKVS.html): Describes how Amazon Kinesis Video Streams uses AWS Secrets Manager secrets.
- [AWS Launch Wizard](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_Launch.html): Describes how AWS Launch Wizard uses AWS Secrets Manager secrets.
- [Amazon Lookout for Metrics](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_LFMlong.html): Describes how Amazon Lookout for Metrics uses AWS Secrets Manager secrets.
- [Amazon Managed Grafana](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_GRAlong.html): Describes how Amazon Managed Grafana uses AWS Secrets Manager secrets.
- [AWS Managed Services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_AMSlong.html): Describes how AWS Managed Services uses AWS Secrets Manager secrets.
- [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_MSKlong.html): Describes how Amazon Managed Streaming for Apache Kafka uses AWS Secrets Manager secrets.
- [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_mwaa.html): Describes how Amazon Managed Workflows for Apache Airflow uses AWS Secrets Manager secrets.
- [AWS Marketplace](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_marketplace-deployment.html): Describes how AWS Marketplace uses AWS Secrets Manager secrets.
- [AWS Migration Hub](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_migration-hub.html): Describes how AWS Migration Hub uses AWS Secrets Manager secrets.
- [AWS Panorama](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_PAN.html): Describes how AWS Panorama uses AWS Secrets Manager secrets.
- [AWS Parallel Computing Service](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_pcs.html): AWS Parallel Computing Service (AWS PCS) is a managed service that makes it easier to run and scale high performance computing (HPC) and distributed machine learning workloads on AWS.
- [AWS ParallelCluster](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_parallelcluster.html): Describes how AWS ParallelCluster uses AWS Secrets Manager secrets.
- [Amazon Q](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-amazonq.html): Describes how Amazon Q uses AWS Secrets Manager secrets.
- [Amazon OpenSearch Ingestion](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-opensearch.html): Describes how OpenSearch Ingestion uses AWS Secrets Manager secrets.
- [AWS OpsWorks for Chef Automate](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_opsworks-cm.html): Describes how AWS OpsWorks for Chef Automate uses AWS Secrets Manager secrets.
- [Amazon Quick](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_QS.html): Describes how Amazon Quick uses AWS Secrets Manager secrets.
- [Amazon RDS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_RDS.html): Describes how Amazon RDS uses AWS Secrets Manager secrets.
- [Amazon Redshift](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_RS.html): Describes how Amazon Redshift uses AWS Secrets Manager secrets.
- [Amazon Redshift query editor v2](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_sqlworkbench.html): Describes how Amazon Redshift query editor v2 uses AWS Secrets Manager secrets.
- [Amazon SageMaker AI](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-sagemaker.html): Describes how Amazon SageMaker AI uses AWS Secrets Manager secrets.
- [AWS SCT](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_AWSSCT.html): Describes how the AWS Schema Conversion Tool (AWS SCT) uses AWS Secrets Manager secrets.
- [Amazon Timestream for InfluxDB](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrationg_how-services-use-secrets_TIME.html): Timestream for InfluxDB is a managed time-series database engine that makes it easy for you to run InfluxDB databases on AWS for real-time time-series applications using open-source APIs.
- [AWS Toolkit for JetBrains](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_JBIDE.html): Describes how AWS Toolkit for JetBrains uses AWS Secrets Manager secrets.
- [AWS Transfer Family](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_FTPlong.html): Describes how AWS Transfer Family uses AWS Secrets Manager secrets.
- [AWS Wickr](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_Wickr.html): Describes how AWS Wickr uses AWS Secrets Manager secrets.


## [Secrets managed by third party applications](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html)

### [Integration Partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html)

Secrets Manager natively integrates with third party applications to rotate secrets held by the partner.

- [Salesforce Client Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partner-salesforce.html)
- [Big ID Refresh Token](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partner-BigId.html)
- [Snowflake Key Pair](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partner-Snowflake.html)
- [Security and permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html): Managed external secrets does not require you to share admin-level privileges of your third party application accounts with AWS.
- [Monitor and troubleshoot](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-monitor.html): Managed external secrets provide comprehensive monitoring capabilities through AWS CloudTrail logs and Amazon CloudWatch metrics.
- [Migrating existing secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-migrating.html): You have an option to migrate your existing partner secrets to managed external secrets.
- [Limitations and considerations](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-limitations-and-considerations.html): Managed external secrets does not support ephemeral secrets with lifespans less than four hours.


## [CloudFormation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cloudformation.html)

- [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_secret.html): Learn how to create secrets using an AWS CloudFormation template.
- [Create a secret with Amazon RDS credentials with automatic rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_RDSsecret.html): Learn how to create an Amazon RDS database and a secret to manage the admin credentials.
- [Create a secret with Amazon Redshift credentials](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_Redshift-secret.html): Learn how to create an Amazon Redshift cluster and a secret to manage the admin credentials.
- [Create a secret with Amazon DocumentDB credentials](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_DocDB-secret.html): Learn how to create a Amazon DocumentDB instance and a secret to manage the admin credentials.


## [Monitor secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html)

### [Log with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring-cloudtrail.html)

Describes the logging available for AWS Secrets Manager.

- [CloudTrail entries](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cloudtrail_log_entries.html): Describes the logging available for AWS Secrets Manager.
- [Monitor with CloudWatch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring-cloudwatch.html): Learn about the Secrets Manager metrics available with CloudWatch.
- [Match Secrets Manager events with EventBridge](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring-eventbridge.html): Create EventBridge rules that match Secrets Manager events.
- [Monitor secrets scheduled for deletion](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring_cloudwatch_deleted-secrets.html): In Secrets Manager, get notified when there are attempts to use secrets that are scheduled to be deleted.
- [Monitor secrets for compliance](https://docs.aws.amazon.com/secretsmanager/latest/userguide/configuring-awsconfig-rules.html): Use AWS Config to monitor your secrets for compliance.
- [Monitor Secrets Manager costs](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitor-secretsmanager-costs.html): Monitor estimated charges in Secrets Manager using Amazon CloudWatch.
- [Detect threats with GuardDuty](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring-guardduty.html): Learn how to use GuardDuty for AWS Secrets Manager secrets.


## [Security](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security.html)

- [Mitigate the risks of using the AWS CLI to store your AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html): Learn how to use the AWS CLI to invoke Secrets Manager operations without compromising your secrets.

### [Authentication and access control](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html)

Learn how to control access to your secrets in AWS Secrets Manager.

- [Identity-based policies](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_iam-policies.html): Use IAM policies (identity-based policies) to specify permissions and control access to your secrets in AWS Secrets Manager.
- [Resource-based policies](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html): Use resource policies to specify permissions and control access to your secrets.
- [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access-abac.html): Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes or characteristics of the user, the data, or the environment, such as the department, business unit, or other factors that could affect the authorization outcome.
- [AWS managed policies](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-policies.html): Learn about AWS managed policies for AWS Secrets Manager and recent changes to those policies.
- [Determine who has permissions to your secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html): Learn how to determine who can access a secret in AWS Secrets Manager.
- [Cross-account access](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples_cross.html): Learn how to allow users in other accounts to access your secrets.
- [On-premises access](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access-on-prem.html): Learn how to access AWS Secrets Manager secrets from on-premises.
- [Data protection in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Secrets Manager.
- [Secret encryption and decryption](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html): Learn how AWS Secrets Manager uses AWS KMS to encrypt secrets.
- [Infrastructure security](https://docs.aws.amazon.com/secretsmanager/latest/userguide/infrastructure-security.html): Learn how Secrets Manager is protected by the AWS global network security.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html): Create, manage, and configure Secrets Manager for VPC endpoints.
- [IPv4 and IPv6 access](https://docs.aws.amazon.com/secretsmanager/latest/userguide/ip-access.html): Control API access with IAM policies.
- [Resilience](https://docs.aws.amazon.com/secretsmanager/latest/userguide/disaster-recovery-resiliency.html): Describes data resiliency for specific AWS Secrets Manager features, and how the AWS architecture supports data redundancy.
- [Post-quantum TLS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/pqtls.html): Learn how to use hybrid post-quantum key agreement algorithms for your Secrets Manager transactions.
