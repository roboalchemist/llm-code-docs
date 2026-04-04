# Source: https://docs.aws.amazon.com/mwaa/latest/userguide/llms.txt

# Amazon Managed Workflows for Apache Airflow User Guide

> Learn about how to use Amazon Managed Workflows for Apache Airflow to create environments that let you easily configure, deploy, and manage your Apache Airflow workflows.

- [What Is Amazon MWAA?](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)
- [Quick start](https://docs.aws.amazon.com/mwaa/latest/userguide/quick-start.html)
- [Versions](https://docs.aws.amazon.com/mwaa/latest/userguide/airflow-versions.html)
- [Endpoints and quotas](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-quotas.html)
- [FAQs](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-faqs.html)
- [Amazon MWAA User Guide history](https://docs.aws.amazon.com/mwaa/latest/userguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html)

- [Create a bucket](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html): This guide describes the steps to create an Amazon S3 bucket to store your Apache Airflow Directed Acyclic Graphs (DAGs), custom plugins, and Python dependencies for Apache Airflow.
- [Create the VPC network](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-create.html): This guide describes the different options to create the Amazon VPC network for an Amazon Managed Workflows for Apache Airflow environment.
- [Create an environment](https://docs.aws.amazon.com/mwaa/latest/userguide/create-environment.html): This topic describes the steps to create an Amazon Managed Workflows for Apache Airflow environment.


## [Managing access](https://docs.aws.amazon.com/mwaa/latest/userguide/manage-access.html)

- [Accessing an Amazon MWAA environment](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html): This topic describes the access policies you can attach to your Apache Airflow development team and Apache Airflow users for your Amazon Managed Workflows for Apache Airflow environment.
- [Service-linked role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-slr.html): How to use service-linked roles to give Amazon MWAA access to resources in your AWS account.
- [Execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html): This topic describes how to use and configure the execution role for your environment to allow Amazon MWAA to access other AWS resources used by your environment.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mwaa/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Apache Airflow access modes](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html): This guide describes the access modes available for the Apache Airflow webserver on your Amazon Managed Workflows for Apache Airflow environment, and the additional resources you'll need to configure in your Amazon VPC if you choose the private network option.


## [Accessing Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/access-airflow-ui.html)

- [Create a webserver access token](https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-web.html): This page describes how to create a web serer access token and make Amazon MWAA API calls directly in your command shell.
- [Setting up a custom domain](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-custom-domain.html): Learn how to configure a custom domain name for your Amazon MWAA-managed Apache Airflow webserver.
- [Apache Airflow CLI token](https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-cli.html): Learn how to generate a CLI token and make Amazon MWAA API calls directly in your command shell.
- [Using the Apache Airflow REST API](https://docs.aws.amazon.com/mwaa/latest/userguide/access-mwaa-apache-airflow-rest-api.html): This Amazon MWAA documentation page describes how to authenticate with an access toke, then call the Apache Airflow REST API using a Python script.
- [Apache Airflow CLI command reference](https://docs.aws.amazon.com/mwaa/latest/userguide/airflow-cli-command-reference.html): This topic describes the supported and unsupported Apache Airflow CLI commands on Amazon Managed Workflows for Apache Airflow.


## [Managing connections](https://docs.aws.amazon.com/mwaa/latest/userguide/manage-connections.html)

- [Apache Airflow packages](https://docs.aws.amazon.com/mwaa/latest/userguide/connections-packages.html): This page lists the Apache Airflow provider packages used for connections that are installed by Amazon Managed Workflows for Apache Airflow to all Apache Airflow environments.
- [Connection types](https://docs.aws.amazon.com/mwaa/latest/userguide/manage-connection-types.html): Apache Airflow stores connections as a connection URI string.
- [Configuring Secrets Manager](https://docs.aws.amazon.com/mwaa/latest/userguide/connections-secrets-manager.html): Describes how to use AWS Secrets Manager to securely store secrets for Apache Airflow variables and an Apache Airflow connection on Amazon Managed Workflows for Apache Airflow.


## [Managing environments](https://docs.aws.amazon.com/mwaa/latest/userguide/using-mwaa.html)

- [Configuring the environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html): This topic describes each Amazon MWAA environment class, and how to update the environment class on the Amazon Managed Workflows for Apache Airflow console.
- [Configuring worker auto scaling](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-autoscaling.html): This topic describes how you can configure automatic scaling by specifying the maximum number of Apache Airflow workers that run on your environment using the Amazon MWAA console.
- [Configuring webserver auto scaling](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-web-server-autoscaling.html): This page describes how you can configure webserver auto scaling by specifying the maximum number of Apache Airflow webservers that run on your environment using the Amazon MWAA console.
- [Using configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html): This topic describes the Apache Airflow configuration options available in the dropdown list on the Amazon Managed Workflows for Apache Airflow console, and how to use these options to override Apache Airflow configuration settings in your environment.
- [Update an environment](https://docs.aws.amazon.com/mwaa/latest/userguide/update-environment.html): This topic describes the steps to update an Amazon Managed Workflows for Apache Airflow environment.
- [Changing the version](https://docs.aws.amazon.com/mwaa/latest/userguide/upgrading-environment.html): Describes the process for upgrading and downgrading an Amazon MWAA environment to a new or previous Apache Airflow minor version.
- [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html): Describes how to customize your Amazon Managed Workflows for Apache Airflow environment using a shell script that runs when your environment starts.


## [Working with DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags.html)

- [Adding or updating DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html): This topic describes the steps to add or update Apache Airflow DAGs on your Amazon Managed Workflows for Apache Airflow environment using the DAGs folder in your Amazon S3 bucket.
- [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html): This page describes the steps to install Apache Airflow custom plugins on your Amazon Managed Workflows for Apache Airflow environment.
- [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html): This topic describes the steps to install Apache Airflow Python dependencies on your Amazon Managed Workflows for Apache Airflow environment using a requirements.txt file in your Amazon S3 bucket.
- [Deleting files on Amazon S3](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-delete.html): This page describes how versioning works in an Amazon S3 bucket for an Amazon Managed Workflows for Apache Airflow environment, and the steps to delete a DAG, plugins.zip or requirements.txt file.


## [Networking](https://docs.aws.amazon.com/mwaa/latest/userguide/networking.html)

- [About networking](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html): This page describes the Amazon VPC infrastructure with public routing or private routing that's needed to support an Amazon Managed Workflows for Apache Airflow environment.
- [Security in your VPC](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html): This page describes the Amazon VPC components used to secure your Amazon Managed Workflows for Apache Airflow environment and the configurations needed for these components.
- [Managing access to VPC endpoints](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-vpe-access.html): This page describes how to access the VPC endpoint for an Apache Airflow webserver with the private network access mode on Amazon Managed Workflows for Apache Airflow.
- [VPC service endpoints in private Amazon VPCs](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-vpe-create-access.html): This page describes the VPC endpoints required for the AWS services used by Amazon MWAA, the VPC endpoints required for Apache Airflow, and how to create and attach the VPC endpoints to an existing Amazon VPC with private routing.
- [Managing your own Amazon VPC endpoints](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-endpoint-management.html): Learn how to manage your own Amazon VPC endpoints when you create an Amazon MWAA environment.


## [Tutorials](https://docs.aws.amazon.com/mwaa/latest/userguide/tutorials.html)

- [Tutorial: AWS Client VPN](https://docs.aws.amazon.com/mwaa/latest/userguide/tutorials-private-network-vpn-client.html): This tutorial walks you through the steps to create a VPN tunnel from your computer to the Apache Airflow webserver for your Amazon Managed Workflows for Apache Airflow environment.
- [Tutorial: Linux Bastion Host](https://docs.aws.amazon.com/mwaa/latest/userguide/tutorials-private-network-bastion.html): This tutorial walks you through the steps to create an SSH tunnel from your computer to the to the Apache Airflow webserver for your Amazon Managed Workflows for Apache Airflow environment.
- [Tutorial: Restricting users to a subset of DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/limit-access-to-dags.html): Amazon MWAA manages access to your environment by mapping your IAM principals to one or more of Apache Airflow's default roles.
- [Tutorial: Automate managing your own environment endpoints](https://docs.aws.amazon.com/mwaa/latest/userguide/tutorials-customer-managed-endpoints.html): Describes how to create, and manage your own Amazon VPC endpoints using an EventBridge rule and a Lambda function.


## [Code examples](https://docs.aws.amazon.com/mwaa/latest/userguide/sample-code.html)

- [Import variables DAG](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-variables-import.html): The following sample code imports variables using the CLI on Amazon Managed Workflows for Apache Airflow
- [Using the SSHOperator](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-ssh.html): Use this code example to learn how to use the SSHOperator in a DAG and create an SSH connection to a remote instance in Amazon Managed Workflows for Apache Airflow.
- [Apache Airflow Snowflake connection in Secrets Manager](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-sm-snowflake.html): The following sample calls AWS Secrets Manager to get a secret key for an Apache Airflow Snowflake connection on Amazon Managed Workflows for Apache Airflow.
- [Using a DAG to write custom metrics](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-custom-metrics.html): Use the provided code example for a DAG that runs a PythonOperator to retrieve OS-level metrics for an Amazon MWAA environment, then publishes custom metrics to CloudWatch.
- [Aurora PostgreSQL database cleanup](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-database-cleanup.html): The following sample code periodically clears out entries from the dedicated Aurora PostgreSQL database for your Amazon Managed Workflows for Apache Airflow environment.
- [Exporting environment metadata to Amazon S3](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-dag-run-info-to-csv.html): Use this code example for querying the Aurora PostgreSQL database for information about DAG runs, and writing the data to a CSV file stored on Amazon S3.
- [Using an Apache Airflow variable in Secrets Manager](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-secrets-manager-var.html): The following sample calls AWS Secrets Manager to get a secret key for an Apache Airflow variable on Amazon Managed Workflows for Apache Airflow.
- [Using an Apache Airflow connection in Secrets Manager](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-secrets-manager.html): The following sample calls AWS Secrets Manager to get a secret key for an Apache Airflow connection on Amazon Managed Workflows for Apache Airflow.
- [Custom plugin with Oracle](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-oracle.html): The following sample walks you through the steps to create a custom plugin using Oracle for an Amazon Managed Workflows for Apache Airflow environment.
- [Changing a DAG's timezone](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-plugins-timezone.html): Use this code example to learn how you to use the Pendulum Python library to create timezone-aware DAGs, and how to create a custom plugin to change the timezone for Apache Airflow logs delivered to CloudWatch.
- [Refreshing an AWS CodeArtifact token at runtime](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-code-artifact.html): The following sample walks you through the steps to create a DAG that uses the token in your CodeArtifact repository, rather than in a requirements.txt on Amazon Managed Workflows for Apache Airflow.
- [Custom plugin with Apache Hive and Hadoop](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-hive.html): The following sample walks you through the steps to create a custom plugin using Apache Hive and Hadoop on an Amazon Managed Workflows for Apache Airflow environment.
- [Custom plugin to patch PythonVirtualenvOperator](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-virtualenv.html): The following sample explains how to patch the Apache Airflow PythonVirtualenvOperator with a custom plugin on Amazon Managed Workflows for Apache Airflow.
- [Invoking DAGs with Lambda](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-lambda.html): Use this code example to invoke a DAG in an Amazon MWAA environment using a Lambda function.
- [Invoking DAGs in different environments](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-invoke-dag.html): Use this code example to write a DAG that retrieves a new Apache Airflow CLI token, then invokes a DAG in another Amazon MWAA environment.
- [Amazon RDS server](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-sql-server.html): The following sample code uses DAGs on an Amazon Managed Workflows for Apache Airflow environment to connect to and execute queries on an RDS for SQL Server server.
- [Amazon EKS (eksctl)](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-eks-example.html): The following sample demonstrates how to use Amazon Managed Workflows for Apache Airflow with Amazon EKS.
- [Using the ECSOperator](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-ecs-operator.html): Describes sample code for using the ECSOperator to connect to an Amazon Elastic Container Service (Amazon ECS) container from Amazon MWAA.
- [Using dbt with Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-dbt.html): Demonstrates integrating dbt libraries with an Amazon MWAA environment using BashOperator.


## [Best practices](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices.html)

- [Performance tuning for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices-tuning.html): This topic describes how to tune the performance of an Amazon Managed Workflows for Apache Airflow environment using Apache Airflow configuration options.
- [Managing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices-dependencies.html): This topic describes how to install and manage Python dependencies in a requirements.txt file for an Amazon Managed Workflows for Apache Airflow environment.


## [Monitoring and metrics](https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html)

- [Overview](https://docs.aws.amazon.com/mwaa/latest/userguide/monitoring-overview.html): This page describes the services used to access and use the monitoring dashboards for an Amazon Managed Workflows for Apache Airflow environment.
- [Accessing audit logs](https://docs.aws.amazon.com/mwaa/latest/userguide/monitoring-cloudtrail.html): Learn about how to use AWS CloudTrail to monitor an Amazon Managed Workflows for Apache Airflow environment.
- [Accessing Airflow logs](https://docs.aws.amazon.com/mwaa/latest/userguide/monitoring-airflow.html): Learn about how to enable and use Amazon CloudWatch to monitor Apache Airflow on an Amazon Managed Workflows for Apache Airflow environment.
- [Monitoring dashboards and alarms](https://docs.aws.amazon.com/mwaa/latest/userguide/monitoring-dashboard.html): This page describes how to create a health status dashboard for the Apache Airflow metrics in CloudWatch for an Amazon MWAA environment.
- [Apache Airflow environment metrics](https://docs.aws.amazon.com/mwaa/latest/userguide/access-metrics-cw.html): This page describes the Apache Airflow v2 and Apache Airflow v3 metrics published to Amazon CloudWatch for an Amazon Managed Workflows for Apache Airflow environment, and how to access metrics in the Amazon CloudWatch console.
- [Container, queue, and database metrics](https://docs.aws.amazon.com/mwaa/latest/userguide/accessing-metrics-cw-container-queue-db.html): Describes Amazon ECS container, Amazon SQS queue, and Amazon RDS database metrics published by Amazon MWAA.


## [Security](https://docs.aws.amazon.com/mwaa/latest/userguide/security.html)

### [Data Protection](https://docs.aws.amazon.com/mwaa/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Managed Workflows for Apache Airflow.

- [Encryption](https://docs.aws.amazon.com/mwaa/latest/userguide/encryption.html): Describes how Amazon MWAA protects your data at rest, and in transit.
- [Using customer-managed keys](https://docs.aws.amazon.com/mwaa/latest/userguide/custom-keys-certs.html): You can optionally provide a Customer-managed key for data encryption on your environment.

### [AWS Identity and Access Management](https://docs.aws.amazon.com/mwaa/latest/userguide/security-iam.html)

This topic describes how Amazon Managed Workflows for Apache Airflow uses AWS Identity and Access Management (IAM).

- [Troubleshooting Amazon Managed Workflows for Apache Airflow identity and access](https://docs.aws.amazon.com/mwaa/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you can encounter when working with Amazon MWAA and IAM.

### [How Amazon MWAA works with IAM](https://docs.aws.amazon.com/mwaa/latest/userguide/security_iam_service-with-iam.html)

Amazon MWAA uses IAM identity-based policies to grant permissions to Amazon MWAA actions and resources.

- [Identity-based policy examples](https://docs.aws.amazon.com/mwaa/latest/userguide/security_iam_id-based-policy-examples.html): To access the Amazon MWAA policies, refer to .
- [Compliance Validation](https://docs.aws.amazon.com/mwaa/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mwaa/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon MWAA features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/mwaa/latest/userguide/infrastructure-security.html): Learn how Amazon Managed Workflows for Apache Airflow isolates service traffic.
- [Configuration and Vulnerability Analysis](https://docs.aws.amazon.com/mwaa/latest/userguide/configuration-vulnerability-analysis.html): Learn about configuration and IT controls on Amazon Managed Workflows for Apache Airflow.
- [Best practices](https://docs.aws.amazon.com/mwaa/latest/userguide/security-best-practices.html): This topic describes the security best practices we recommend when using Amazon Managed Workflows for Apache Airflow to ensure your data is secure.


## [Troubleshooting](https://docs.aws.amazon.com/mwaa/latest/userguide/troubleshooting.html)

- [Apache Airflow v2 and v3](https://docs.aws.amazon.com/mwaa/latest/userguide/t-apache-airflow-202.html): Describes common errors and resolutions to Apache Airflow v2 and v3 Python dependencies, custom plugins, DAGs, Operators, Connections, tasks, and webserver errors on an Amazon Managed Workflows for Apache Airflow environment.
- [Amazon MWAA Create/Update](https://docs.aws.amazon.com/mwaa/latest/userguide/t-create-update-environment.html): The topics on this page contain errors and resolutions to creating and updating an Amazon Managed Workflows for Apache Airflow environment.
- [CloudWatch Logs and CloudTrail](https://docs.aws.amazon.com/mwaa/latest/userguide/t-cloudwatch-cloudtrail-logs.html): Use the following topics to resolve issues related to Amazon CloudWatch Logs and AWS CloudTrail for an Amazon Managed Workflows for Apache Airflow environment.
