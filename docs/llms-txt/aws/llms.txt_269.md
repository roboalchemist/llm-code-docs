# Source: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/llms.txt

# AWS Data Pipeline Developer Guide

> Automate the movement and transformation of data with AWS Data Pipeline.

- [Setting Up](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-get-setup.html)
- [Getting Started with AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-getting-started.html)
- [Limits](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-limits.html)
- [AWS Data Pipeline Resources](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/RelatedResources.html)
- [Document History](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/DocHistory.html)

## [What is AWS Data Pipeline?](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html)

- [Migrating workloads from AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/migration.html): AWS launched the AWS Data Pipeline service in 2012.
- [Related services](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/datapipeline-related-services.html): AWS Data Pipeline works with the following services to store data.

### [Supported Instance Types for Pipeline Work Activities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-supported-instance-types.html)

When AWS Data Pipeline runs a pipeline, it compiles the pipeline components to create a set of actionable Amazon EC2 instances.

- [Default Amazon EC2 Instances by AWS Region](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-ec2-default-instance-types.html): If you do not specify an instance type in your pipeline definition, AWS Data Pipeline launches an instance by default.
- [Additional Supported Amazon EC2 Instances](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-ec2-supported-instance-types.html): In addition to the default instances that are created if you don't specify an instance type in your pipeline definition, the following instances are supported.
- [Supported Amazon EC2 Instances for Amazon EMR Clusters](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-emr-supported-instance-types.html): This table lists the Amazon EC2 instances that AWS Data Pipeline supports and can create for Amazon EMR clusters, if specified.


## [AWS Data Pipeline Concepts](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts.html)

- [Pipeline Definition](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-how-pipeline-definition.html): Communicate your business logic to AWS Data Pipeline with a pipeline definition that includes details of your data sources and activities.
- [Pipeline Components, Instances, and Attempts](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-how-tasks-scheduled.html): Associate three types of items with a scheduled pipeline: pipeline components, instances, and attempts.
- [Task Runners](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-how-remote-taskrunner-client.html): Poll the AWS Data Pipeline for tasks and then perform those tasks with a task runner application.
- [Data Nodes](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-datanodes.html): Define the location and type of data that a pipeline activity uses as input or output in a data node.
- [Databases](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-databases.html): Describes the supported databases available for AWS Data Pipeline.
- [Activities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-activities.html): Supported activities are available for AWS Data Pipeline.
- [Preconditions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-preconditions.html): Supported preconditions are available for AWS Data Pipeline, which check conditions that must be true before an activity can run.
- [Resources](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-resources.html): Different computational resources can perform the work that a pipeline activity specifies for AWS Data Pipeline.
- [Actions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-actions.html): A pipeline component can take alarm or terminate action when certain events occur for AWS Data Pipeline.


## [Working with pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-managing-pipeline.html)

### [Creating a pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-creating-pipelines.html)

Create pipelines by using the command line interface, or the API.

### [Create a pipeline from Data Pipeline templates using the CLI](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-cli-templates.html)

Create pipelines using the templates provided by the AWS Data Pipeline console.

- [Getting started using ShellCommandActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-gettingstartedshell.html): Run a shell command script using an AWS Data Pipeline template.
- [Run AWS CLI command](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-runawscli.html): Run an AWS CLI using an AWS Data Pipeline template.
- [Export DynamoDB table to S3](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-exportddbtos3.html): Export data from a DynamoDB table to an Amazon S3 bucket using an AWS Data Pipeline template.
- [Import DynamoDB backup data from S3](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-exports3toddb.html): Export data from an Amazon S3 bucket to a DynamoDB table using an AWS Data Pipeline template.
- [Run job on an Amazon EMR cluster](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-emr.html): Export data from an Amazon S3 bucket to a DynamoDB table using an AWS Data Pipeline template.
- [Full copy of Amazon RDS MySQL Table to Amazon S3](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-copyrdstos3.html): Copy data from an Amazon RDS instance to an Amazon S3 bucket using an AWS Data Pipeline template.
- [Incremental copy of Amazon RDS MySQL table to Amazon S3](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-incrementalcopyrdstos3.html): Copy data from an Amazon RDS instance to an Amazon S3 bucket using an AWS Data Pipeline template.
- [Load S3 data into Amazon RDS MySQL table](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-copys3tords.html): Copy data from an Amazon S3 bucket to an Amazon RDS instance using an AWS Data Pipeline template.
- [Amazon RDS to Amazon Redshift templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-redshift.html): Copy data between Amazon Redshift and Amazon S3 using an AWS Data Pipeline template.
- [Full copy of Amazon RDS MySQL table to Amazon Redshift](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-redshiftrdsfull.html): Copy data between Amazon RDS and Amazon Redshift using an AWS Data Pipeline template.
- [Incremental copy of an Amazon RDS MySQL table to Amazon Redshift](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-redshiftrdsincremental.html): Copy data incrementally between Amazon RDS and Amazon Redshift using an AWS Data Pipeline template.
- [Load data from Amazon S3 into Amazon Redshift](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-s3redshift.html): Copy data between Amazon S3 and Amazon Redshift using an AWS Data Pipeline template.
- [Creating a pipeline Using parametrized templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-custom-templates.html): Learn how to customize an AWS Data Pipeline pipeline definition using a parametrized template.

### [Viewing Your Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-list-pipelines.html)

View your pipelines.

- [Interpreting Pipeline Status Codes](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-interpret-status.html): Describes the pipeline status codes used to indicate the condition of a pipeline and its components.
- [Interpreting Pipeline and Component Health State](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-interpret-health-status.html): Describes the health states of a pipeline.
- [Viewing Your Pipeline Definitions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-view-definition.html): View a pipeline definition using the command line interface.
- [Viewing Pipeline Instance Details](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-details-console.html): View the details and monitor the progress of your pipeline runs.
- [Viewing Pipeline Logs](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-viewing-logs.html): View the logs for your pipeline.
- [Editing Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-modify-console.html): Edit certain details of your pipeline after you have activated it.
- [Cloning Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-clone-cli.html): Clone a pipeline to make a copy of a pipeline that allows you to specify a name for the new pipeline.
- [Tagging Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-adding-tags.html): Tag a pipeline to help you categorize your pipeline.
- [Deactivating Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-deactivate-pipeline.html): Deactivate a pipeline to make changes.
- [Deleting Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-delete-console.html): Delete a pipeline when you no longer need it.
- [Staging Data and Tables with Activities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-staging.html): Stage input and output data in your pipelines to make it easier to use certain activities.
- [Using Resources in Multiple Regions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-region.html): Use resources to run pipelines in different regions by configuring AWS Data Pipeline.
- [Cascading failures and reruns](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-cascade-failandrerun.html): Configure the way pipeline objects behave when a dependency fails or is canceled by a user.
- [Pipeline definition file syntax](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-writing-pipeline-definition.html): Describes the syntax of the pipeline definition file for working manually.

### [Working with the API](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-program-pipeline.html)

Use one of the AWS SDKs to write applications that interact with AWS Data Pipeline.

- [Making an HTTP Request to AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-make-http-request.html): Make HTTP requests using the POST method to perform AWS Data Pipeline operations.


## [Security](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/security.html)

- [Data Protection](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Data Pipeline.

### [Identity and Access Management](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html)

Describes how to share your pipelines with other users and control the level of access they have.

- [IAM Policies for AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-resourcebased-access.html): Control which AWS Data Pipeline resources can be viewed, created, and modified by IAM users.
- [Example Policies for AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-example-tag-policies.html): Learn to create policy statements to control the permissions that IAM users have to AWS Data Pipeline.
- [IAM Roles](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html): Learn the roles required to grant permissions for actions and resource access to AWS Data Pipeline.
- [Logging and Monitoring](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-cloudtrail-logging.html): Learn about logging Your service name with AWS CloudTrail.
- [Incident Response](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/incident-response.html): Incident response for AWS Data Pipeline is an AWS responsibility.
- [Compliance Validation](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/compliance-validation.title.html): AWS Data Pipeline is not in scope of any AWS compliance programs.
- [Resilience](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Data Pipeline features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/infrastructure-security.html): Learn how AWS Data Pipeline isolates service traffic.
- [Configuration and Vulnerability Analysis in AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/configuration-and-vulnerability-analysis.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.


## [Tutorials](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/welcome.html)

### [Process Data Using Amazon EMR with Hadoop Streaming](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-launch-emr-jobflow.html)

Manage your Amazon EMR Hadoop streaming clusters using AWS Data Pipeline.

- [Before You Begin](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-emr-jobflow-prereq.html): Ensure that you have completed the following steps before you begin with AWS Data Pipeline.
- [Using the CLI](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-launch-emr-jobflow-cli.html): Manage your Amazon EMR clusters using the AWS Data Pipeline command line interface.

### [Copy CSV Data from Amazon S3 to Amazon S3](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-s3.html)

How to copy CSV data from one Amazon S3 bucket to another.

- [Before You Begin](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-s3-prereq.html): Complete the following prerequisites before you begin copying data in this AWS Data Pipelinetutorial.
- [Using the CLI](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-get-started-copy-data-cli.html): Create and use pipelines to copy data from one Amazon S3 bucket to another using the AWS Data Pipeline command line interface.

### [Export MySQL Data to Amazon S3](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-mysql.html)

Create a data pipeline to export data from a MySQL database table to an Amazon S3 bucket.

- [Before You Begin](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-mysql-prereq.html): Be sure you've completed the following steps.
- [Using the CLI](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copymysql-cli.html): Creating a pipeline to copy data from a MySQL table to a file in an Amazon S3 bucket using the command line interface.

### [Copy Data to Amazon Redshift](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift.html)

Create a pipeline to move data from Amazon S3 to Amazon Redshift using the AWS Data Pipeline console.

- [Before You Begin: Configure COPY Options](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-learn-copy-redshift.html): Review and configure the COPY command in Amazon Redshift and load sample data from Amazon S3.
- [Before You Begin: Set up Pipeline, Security, and Cluster](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-prereq.html)

### [Using the CLI](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-cli.html)

Copy data from Amazon S3 to Amazon Redshift using the AWS Data Pipeline command line interface.

### [Define a Pipeline in JSON Format](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-define-pipeline-cli.html)

Copy data from Amazon S3 to Amazon Redshift using the full pipeline definition JSON file.

- [Data Nodes](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-node-cli.html): View a pipeline example that uses an input data node, an output data node, and a database.
- [Resource](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-resource-cli.html): View an example of the computational resource that performs the copy operation.
- [Activity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-activity-cli.html): View the last section in the JSON file that is the definition of the activity representing the work to perform.
- [Upload and Activate the Pipeline Definition](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift-upload-cli.html): Upload and activate the pipeline definition file using the command line interface.


## [Pipeline Expressions and Functions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-expressions-functions.html)

- [Expressions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-expressions.html): Share a value across related object using expressions in AWS Data Pipeline.
- [Mathematical Functions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-reference-functions-math.html): Use mathematical functions in AWS Data Pipeline.
- [String Functions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-reference-functions-string.html): Use string value functions in AWS Data Pipeline.
- [Date and Time Functions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-reference-functions-datetime.html): Use date and time value functions in AWS Data Pipeline.
- [Special Characters](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-characters.html): Use special characters in AWS Data Pipeline.


## [Pipeline Object Reference](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-objects.html)

### [Data Nodes](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-datanodes.html)

Describes the data node objects that you can use in your pipeline definition file.

- [DynamoDBDataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-dynamodbdatanode.html): Defines a data node using DynamoDB, which is specified as an input to a HiveActivity or EMRActivity object.
- [MySqlDataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-mysqldatanode.html): Defines a data node using MySQL using the MySqlDataNode operation.
- [RedshiftDataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-redshiftdatanode.html): Defines a data node using Amazon Redshift using the RedshiftDataNode operation.
- [S3DataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-s3datanode.html): Defines a data node using Amazon S3 using the S3DataNode operation.
- [SqlDataNode](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-sqldatanode.html): Defines a data node using MySQL using the SqlDataNode operation.

### [Activities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-activities.html)

Describes the activity objects that you can use in your pipeline definition file.

- [CopyActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-copyactivity.html): Copies data from one location to another using the CopyActivity operation.
- [EmrActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emractivity.html): Runs an EMR cluster using the EmrActivity operation, which, in turn, uses the EmrCluster object.
- [HadoopActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-hadoopactivity.html): Runs an EMR cluster using the HadoopActivity operation.
- [HiveActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-hiveactivity.html): Runs a Hive query on an EMR cluster using the HiveActivity operation.
- [HiveCopyActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-hivecopyactivity.html): Runs a Hive query on an EMR cluster using the HiveCopyActivity operation.
- [PigActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-pigactivity.html): Provides native support for Pig scripts in AWS Data Pipeline without the requirement to use ShellCommandActivity or EmrActivity
- [RedshiftCopyActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-redshiftcopyactivity.html): Copies data directly from DynamoDB or Amazon S3 to Amazon Redshift.
- [ShellCommandActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-shellcommandactivity.html): Runs a command or script to run time-series or cron-like scheduled tasks.
- [SqlActivity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-sqlactivity.html): Runs a SQL query on a database with the SqlActivity operation.

### [Resources](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-resources.html)

Describes the resource objects that you can use in your pipeline definition file.

- [Ec2Resource](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-ec2resource.html): Describes an Amazon EC2 instance that performs the work defined by a pipeline activity.

### [EmrCluster](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emrcluster.html)

Represents the configuration of an Amazon EMR cluster.

### [Examples](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example.html)

The following are examples of this object type.

- [Launch an Amazon EMR cluster with hadoopVersion](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-launch.html)
- [Launch an Amazon EMR cluster with release label emr-4.x or greater](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-release-label.html)
- [Install additional software on your Amazon EMR cluster](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-install-software.html)
- [Disable server-side encryption on 3.x releases](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example1-disable-encryption.html)
- [Disable server-side encryption on 4.x releases](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example2-disable-encryption.html)
- [Configure Hadoop KMS ACLs and create encryption zones in HDFS](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-hadoop-kms.html)
- [Specify custom IAM roles](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-custom-iam-roles.html)
- [Use EmrCluster Resource in AWS SDK for Java](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-java.html)
- [Configure an Amazon EMR cluster in a private subnet](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-private-subnet.html)
- [Attach EBS volumes to cluster nodes](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/emrcluster-example-ebs.html)
- [HttpProxy](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-httpproxy.html): Configure an HttpProxy for use with a TaskRunner.

### [Preconditions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-preconditions.html)

Describes the precondition objects that you can use in your pipeline definition file.

- [DynamoDBDataExists](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-dynamodbdataexists.html): Describes a precondition to check that data exists in a DynamoDB table.
- [DynamoDBTableExists](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-dynamodbtableexists.html): Describes a precondition to check that the DynamoDB table exists.
- [Exists](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-exists.html): Checks whether a data node object exists; however, we recommend that you use system-managed preconditions instead.
- [S3KeyExists](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-S3KeyExists.html): Checks whether a key exists in an Amazon S3 data node.
- [S3PrefixNotEmpty](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-s3prefixnotempty.html): Describes a precondition to check that the Amazon S3 objects with the given prefix (represented as a URI) are present.
- [ShellCommandPrecondition](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-shellcommandprecondition.html): Describes a Unix/Linux shell command that can be run as a precondition.

### [Databases](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-databases.html)

Describes the database objects that you can use in your pipeline definition file.

- [JdbcDatabase](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-jdbcdatabase.html): Defines a JDBC database using the JdbcDatabase operation.
- [RdsDatabase](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-rdsdatabase.html): Defines an Amazon RDS database with the RdsDatabase operation.
- [RedshiftDatabase](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-redshiftdatabase.html): Defines an Amazon Redshift database with the RedshiftDatabase operation.

### [Data Formats](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-dataformats.html)

Describes the data format objects that you can use in your pipeline definition file.

- [CSV Data Format](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-csv.html): Describes a comma-delimited data format where the column separator is a comma and the record separator is a newline character.
- [Custom Data Format](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-custom.html): Describes a custom data format defined by a combination of a certain column separator, record separator, and escape character.
- [DynamoDBDataFormat](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-dynamodbdataformat.html): Applies a schema to an Amazon DynamoDB table to make it accessible by a Hive query.
- [DynamoDBExportDataFormat](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-dynamodbexportdataformat.html): Applies a schema to an Amazon DynamoDB table to make it accessible by a Hive query.
- [RegEx Data Format](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-regex.html): Describes a custom data format defined by a regular expression.
- [TSV Data Format](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-tsv.html): Describes a comma-delimited data format where the column separator is a tab character and the record separator is a newline character.

### [Actions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-actions.html)

Describes the action objects that you can use in your pipeline definition file.

- [SnsAlarm](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-snsalarm.html): Sends an Amazon SNS notification message when an activity fails or finishes successfully.
- [Terminate](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-terminate.html): Describes an action to trigger the cancellation of a pending or unfinished activity, resource, or data node.
- [Schedule](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-schedule.html): Defines the timing of a scheduled event, such as when an activity runs.

### [Utilities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-utilities.html)

The following utility objects configure other pipeline objects:

- [ShellScriptConfig](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-shellscriptconfig.html): Run a shell script at the specified URI to run pre- or post-activity.
- [EmrConfiguration](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emrconfiguration.html): The EmrConfiguration object is the configuration used for EMR clusters with releases 4.0.0 or greater.
- [Property](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-property.html): A single key-value property for use with an EmrConfiguration object.


## [Working with Task Runner](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-using-task-runner.html)

- [Task Runner on AWS Data Pipeline-Managed Resources](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-how-task-runner-dp-managed.html): Describes how Task Runner works with AWS Data Pipeline-managed resources.

### [Executing Work on Existing Resources Using Task Runner](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-how-task-runner-user-managed.html)

How to manually install and then run Task Runner on user-managed computational resources.

- [(Optional) Granting Task Runner Access to Amazon RDS](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-taskrunner-rdssecurity.html): Control access to your DB instances using database security groups by allowing Task Runner to access your Amazon RDS instances.
- [Task Runner Threads and Preconditions](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-taskrunner-threading.html): Describes Task Runner threading, precondition behavior, and the related settings.
- [Task Runner Configuration Options](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-taskrunner-config-options.html): Lists the configuration options available in Task Runner from the command line interface.
- [Using Task Runner with a Proxy](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-taskrunner-proxy.html): If you are using a proxy host, you can either specify its configuration when invoking Task Runner or set the environment variable, HTTPS_PROXY.
- [Task Runner and Custom AMIs](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-custom-ami.html): When you specify an Ec2Resource object for your pipeline, AWS Data Pipeline creates an EC2 instance for you, using an AMI that installs and configures Task Runner for you.


## [Troubleshooting](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-troubleshooting.html)

- [Locating Errors in Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-troubleshoot-locate-errors.html): Locate errors about failed or incomplete pipeline runs with the AWS Data Pipeline console.
- [Identifying the Amazon EMR Cluster that Serves Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-troubleshoot-emr.html): Identify the Amazon EMR cluster that serves your pipeline and use the Amazon EMR console to see more detailed error information.
- [Interpreting Pipeline Status Details](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-status.html): View pipeline status values and definitions in the AWS Data Pipeline console and command line interface.
- [Locating Error Logs](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-error-logs.html): Find the various logs that the AWS Data Pipeline writes, which you can use to determine the source of certain failures and errors.
- [Resolving Common Problems](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-check-when-run-fails.html): Find solutions for some common AWS Data Pipeline problems.
