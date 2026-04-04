# Source: https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/llms.txt

# Amazon Managed Workflows for Apache Airflow Serverless Amazon MWAA Serverless User Guide

- [Prerequisites](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/prerequisites-set-up.html)
- [Operators](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/operators.html)
- [Quotas](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/mwaa-serverless-quotas.html)
- [Document history](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/doc-history.html)

## [What is Amazon MWAA Serverless?](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/what-is-mwaa-serverless.html)

- [Key concepts](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/mwaas-concepts.html): Learn the key concepts and terminology used in Amazon MWAA Serverless to understand how serverless workflow orchestration works and how it differs from traditional Airflow deployments.
- [Supported Parameters](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/supported-airflow-parameters.html): Learn about the Apache Airflow parameters support on Amazon MWAA Serverless.
- [Supported Airflow macros and Jinja paramters](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/supported-jinja-parameters.html): Learn about the Apache Airflow parameters support on Amazon MWAA Serverless.


## [Getting started](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/get-started.html)

- [Create an S3 bucket](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/mwaas-s3-bucket.html): Learn how to create an Amazon S3 bucket to store your workflow files.
- [Execution roles](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/get-started-execution-role.html): This topic describes how to use and configure the execution role for your workflow to allow Amazon MWAA Serverless to access other AWS resources used by your workflow.


## [Workflows](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/workflows.html)

- [Convert Python DAG to YAML definition](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/workflows-migrate.html): Learn how to covert a Python DAG to YAML based workflow definition that is ready for MWAA Serverless.
- [Tag a workflow](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/workflows-tags.html): How to tag Amazon MWAA Serverless resources.


## [Security](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon MWAA Serverless.

### [Identity and access management](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security-iam.html)

How to authenticate requests and manage access your Amazon MWAA Serverless resources.

- [How Amazon MWAA Serverless works with IAM](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon MWAA Serverless, learn what IAM features are available to use with Amazon MWAA Serverless.
- [Identity-based policy examples](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon MWAA Serverless resources.
- [Using service-linked roles](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon MWAA Serverless access to resources in your AWS account.
- [AWS managed policy](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/mwaa-serverless-aws-managed-policy.html): AWS managed policies for Amazon MWAA Serverless
- [Troubleshooting](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon MWAA Serverless and IAM.
- [Compliance validation](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon MWAA Serverless features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/infrastructure-security.html): Learn how Amazon MWAA Serverless isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Best practices](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security-best-practices.html): This topic describes the security best practices we recommend when using Amazon MWAA Serverless to ensure your data is secure.


## [Monitoring](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/monitoring.html)

- [Observability with CloudWatch](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/observe-with-cloudwatch.html): This topic describes how customers can leverage CloudWatch to implement Observability in $MWAAS;.
- [Logging API calls with CloudTrail](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/log-apis-with-cloudtrail.html): This topic describes the security best practices we recommend when using Amazon MWAA Serverless to ensure your data is secure.


## [Networking](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/networking.html)

- [Create a VPC network](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/networking-vpc.html): This guide describes the different options to create a Amazon VPC network.
- [Security in your VPC](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/networking-security.html): This page describes the Amazon VPC components that are used to secure your Amazon MWAA Serverless workflow and the configurations needed for these components.
- [AWS PrivateLink](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/networking-privatelink.html): You can use an AWS PrivateLink to create a private connection between your VPC and Amazon MWAA Serverless.
