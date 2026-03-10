# Source: https://docs.aws.amazon.com/emr/latest/ManagementGuide/llms.txt

# Amazon EMR Management Guide

> Learn to plan, configure, deploy, monitor, and secure big-data solutions in the cloud using Amazon EMR. Amazon EMR is the Amazon Web Services (AWS) managed framework for running Apache Hadoop, Spark, HBase, Presto, Flink and other big-data applications on dynamically scalable Amazon EC2 instances. Use this guide together with the Amazon EMR Release Guide, which covers application installation, configuration, and optimization.

- [Before you set up Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-setting-up.html)
- [Getting started tutorial](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
- [Managing Amazon EMR clusters with the console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/whats-new-in-console.html)
- [AWS Glossary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/glossary.html)
- [Document history](https://docs.aws.amazon.com/emr/latest/ManagementGuide/mgmt-dochistory.html)

## [What is Amazon EMR?](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)

- [Understanding how to create and work with Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html): Learn about distributed data processing among nodes in an Amazon EMR cluster.
- [Benefits of using Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview-benefits.html): Learn about the benefits of using Amazon EMR to process data using big data frameworks.
- [Architecture and service layers](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview-arch.html): Learn about architecture and service layers in Amazon EMR.


## [Amazon EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)

- [How it works](https://docs.aws.amazon.com/emr/latest/ManagementGuide/how-emr-studio-works.html): Overview of Amazon EMR Studio features

### [EMR Studio features, requirements, and limits](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-considerations.html)

Things to consider when working with Amazon EMR Studio, including considerations about regions and technical details, cluster requirements, and the benefits of using EMR Studio.

- [VPC and subnet best practices for EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-vpc-subnet-best-practices.html): Use the following best practices to set up an Amazon Virtual Private Cloud (Amazon VPC) with subnets for EMR Studio:
- [Cluster requirements](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-cluster-requirements.html): Amazon EMR Clusters Running on Amazon EC2

### [Configure EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-configure.html)

Set up an Amazon EMR Studio for your team: choose IAM or IAM Identity Center authentication for EMR Studio, create cluster templates with Service Catalog, define IAM roles, permissions policies, and security groups for the Studio, and assign users and groups.

- [Administrator permissions to create an EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-admin-permissions.html): Learn about the IAM permissions you need to create an Amazon EMR and assign users and groups to a Studio.

### [Set up an EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-set-up.html)

Complete the following steps to set up an EMR Studio.

- [Choose an authentication mode](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-authentication.html): Choose AWS Identity and Access Management or AWS IAM Identity Center authentication for Amazon EMR Studio to define how users should log in to an EMR Studio.
- [Create an EMR Studio service role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-service-role.html): Define an IAM service role for EMR Studio so that the Studio can interoperate with other AWS services such as Amazon S3.
- [Studio user permissions (EC2, EKS)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-user-permissions.html): Learn how to configure fine-grained user and group permissions for Amazon EMR Studio.
- [Create an EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-studio.html): Create an EMR Studio for your team with the Amazon EMR console or the AWS CLI.
- [Assign and manage users](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-manage-users.html): Assign a user or group to an Amazon EMR Studio, see existing Studio users, and update or delete a user from a Studio.
- [Monitor, update and delete Amazon EMR Studio resources](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-manage-studio.html): Manage an Amazon EMR Studio, and monitor Studio activity using AWS CloudTrail events and Spark user impersonation.
- [Encrypting workspace notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-workspace-storage-encryption.html): In EMR Studio, you can create and configure different workspaces to organize and run notebooks.
- [Control EMR Studio network traffic](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-security-groups.html): Set up security groups used by EMR Studio to control network traffic between Studio Workspaces and EMR clusters.
- [Create cluster templates](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-cluster-templates.html): Create AWS CloudFormation templates for Amazon EMR clusters with Service Catalog so your team can quickly create new EMR clusters in an EMR Studio Workspace.
- [Access and permissions for Git-based repositories](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-enable-git.html): Information about how EMR Studio users link Git-based repositories to Workspaces.
- [Optimize Spark jobs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-spark-optimization.html): Configure Spark jobs using EMR Studio so your team can optimize your Amazon EMR cluster.

### [Use an EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/use-an-emr-studio.html)

Log in to an Amazon EMR Studio and create a Workspace to run notebooks and debug applications.

### [Learn EMR Studio workspaces](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-configure-workspace.html)

Create and configure a Workspace for Amazon EMR Studio so that you can manage and run notebook files.

- [Create a Workspace](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-workspace.html): You can create EMR Studio Workspaces to run notebook code using the EMR Studio interface.
- [Launch a Workspace in EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-use-workspace.html): To start working with notebook files, launch a Workspace to access the notebook editor.
- [Understand the Workspace UI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-workspace-ui.html): The EMR Studio Workspace user interface is based on the JupyterLab interface with icon-denoted tabs on the left sidebar.
- [Explore notebook examples in an EMR Studio workspace](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-notebook-examples.html): Every EMR Studio Workspace includes a set of notebook examples that you can use to explore EMR Studio features.
- [Save Workspace content in EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-save-workspace.html): When you work in the notebook editor of a Workspace, EMR Studio saves the content of notebook cells and output for you in the Amazon S3 location associated with the Studio.
- [Delete a Workspace and notebook files in EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-delete-workspace.html): When you delete a notebook file from an EMR Studio Workspace, you delete the file from the File browser, and EMR Studio removes its backup copy in Amazon S3.
- [Workspace status](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-workspace-status.html): After you create an EMR Studio Workspace, it appears as a row in the Workspaces list in your Studio with its name, status, creation time, and last modified timestamp.
- [Resolve Workspace connectivity issues](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-workspace-stop-start.html): To resolve Workspace connectivity issues, you can stop and restart a Workspace.
- [Workspace collaboration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-workspace-collaboration.html): Use Workspace to write and run notebook code with other team members.
- [Run Workspace with a runtime role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-runtime.html): How to use a runtime role when you attach an EMR Studio Workspace to an EMR cluster.
- [Run Amazon EMR Studio Workspace Workspace notebooks programmatically](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-run-programmatically.html): Run Workspace notebooks with a script or on the AWS CLI.
- [Browse data with SQL Explorer for EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-sql-explorer.html): Use Amazon EMR Studio's SQL Explorer to browse data sources on your EMR cluster, write and run SQL queries, and download query results.
- [Attach a compute to a Workspace](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-use-clusters.html): Create EMR clusters for Amazon EMR Studio, and link clusters to a Workspace so you can run notebook code.
- [Link Git repositories](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-git-repo.html): Associate up to three Git-based repositories with an Amazon EMR Studio Workspace to save and share notebook files.
- [Athena integration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-athena.html): Use Amazon EMR Studio for SQL analytics on Amazon Athena from the same interface that you use for your Spark, Scala, and other workloads.
- [CodeWhisperer integration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-codewhisperer.html): Data analysts can get real-time code recommendations as they write code in JupyterLab notebooks in EMR Studio Workspaces.
- [Debug applications and jobs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html): Debug and troubleshoot applications from EMR Studio using on-cluster and persistent web application UIs such as the Spark History Server.
- [Install kernels and libraries](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-install-libraries-and-kernels.html): Install Jupyter Notebook kernels and Python libraries for EMR Studio.
- [Magic commands](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-magics.html): Use magic commands to analyze data and submit Spark jobs.
- [Use multi-language notebooks with Spark kernels](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-multi-language-kernels.html): Multi-language support for Spark kernels in Jupyter notebooks in EMR Studio.


## [EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html)

- [Notebooks in the console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-migration.html): Amazon EMR Notebooks has merged with Amazon EMR Studio Workspaces.
- [Considerations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-considerations.html)
- [Create a Notebook](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-create.html)
- [Working with EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)

### [Sample programmatic commands for EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html)

- [Notebook CLI command samples](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless-cli.html): This topic shows CLI command samples for an EMR notebook.
- [Boto3 SDK sample script](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless-python.html): This topic contains a sample command file.
- [Ruby sample script](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless-ruby.html): This topic contains a Ruby sample that demonstrate notebook functionality.
- [User impersonation for Spark](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-spark-monitor.html): EMR Notebooks allows you to configure user impersonation on a Spark cluster.
- [Security](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security.html): Several features are available to help you tailor the security posture of EMR Notebooks.
- [Installing and using kernels and libraries in EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-installing-libraries-and-kernels.html): Each EMR notebook comes with a set of pre-installed libraries and kernels.

### [Associating Git-based repositories with EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo.html)

You can associate Git-based repositories with your Amazon EMR notebooks to save your notebooks in a version controlled environment.

- [Prerequisites and considerations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-git-considerations.html): Consider the following best practices regarding commits, permissions, and hosting when planning to integrate a Git-based repository with EMR Notebooks.
- [Add a Git-based repository to Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo-add.html): Refer to the following sections for information on how to add a Git-based repository to an EMR notebook in the old console, or to an EMR Studio Workspace in the console.
- [Update or delete a Git-based repository from an EMR Studio Workspace](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo-delete.html): Refer to the following sections for information on how to delete a Git-based repository from an EMR notebook in the old console, or from an EMR Studio Workspace in the console.
- [Link or unlink a Git-based repository in EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo-link.html): Use the following steps to link or unlink a Git-based repository to an EMR notebook in the old console, or to an EMR Studio Workspace in the console.
- [Create a new Notebook with an associated Git repository in EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo-create-notebook.html)
- [Use Git repositories in an EMR Studio Notebook](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo-open.html)


## [Plan, configure and launch Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan.html)

- [Launch an Amazon EMR cluster quickly](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-launch-with-quick-options.html): Launch an Amazon EMR cluster in the Amazon EMR console.

### [Configure Amazon EMR cluster location and data storage](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cluster-location-data-storage.html)

This section describes how to configure the region for a cluster, the different file systems available when you use Amazon EMR and how to use them.

- [Choose an AWS Region for your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-region.html): Pick the AWS Region into which you will launch your Amazon EMR cluster.
- [Working with storage and file systems](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-file-systems.html): Lists the types of file system that are compatible with Amazon EMR.

### [Prepare input data for processing with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input.html)

Prepare input data for your cluster by ensuring it is a location that the cluster can access and in a format the cluster can process.

- [Types of input Amazon EMR can accept](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input-accept.html): Lists the types of input data that Amazon EMR can accept.

### [Different ways to get data into Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-get-data-in.html)

Describes several ways to get data onto a cluster using Amazon EMR.

### [Upload data to Amazon S3](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-upload-s3.html)

Describes the steps to upload data to an Amazon S3 bucket for use on your cluster.

- [Upload data to S3 Express One Zone](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-express-one-zone.html): Configure your Spark cluster to access data from a bucket that uses the S3 Express One Zone storage class for low latency and high performance cloud object storage.
- [Upload data with AWS DataSync](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-upload-datasync.html): Use AWS DataSync to upload data from on-premises storage systems like HDFS into Amazon S3 so that you can work with the data on an Amazon EMR cluster.
- [Import files with distributed cache with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input-distributed-cache.html): Import files from a distributed file system to the local file system using a Hadoop feature called DistributedCache.
- [Detecting and processing compressed files with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/HowtoProcessGzippedFiles.html): Describes how to process compressed files supported by Hadoop.
- [Import DynamoDB data into Hive with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input-dynamodb.html): Import and export data between Amazon DynamoDB and an Amazon EMR cluster using Hive.
- [Connect to data with AWS Direct Connect from Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input-directconnect.html): Connect to data through a private dedicated network connection with AWS Direct Connect.
- [Upload large amounts of data for Amazon EMR with AWS Snowball Edge](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input-snowball.html): Upload large amounts of data from physical storage devices into AWS with AWS Snowball Edge.

### [Configure a location for Amazon EMR cluster output](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-output.html)

Prepare an output location into which your Amazon Elastic MapReduce cluster writes files.

- [What formats can Amazon EMR return?](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-output-formats.html): Lists the output formats that an Amazon Elastic MapReduce cluster can return.
- [How to write data to an Amazon S3 bucket you don't own with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-s3-acls.html): Write data to an Amazon S3 bucket that you don't own by getting permission from the other AWS user and set read permissions on those files.
- [Ways to compress the output of your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-output-compression.html): Compress the output of your cluster by to improve the performance transferring large amounts of data.

### [Plan and configure primary nodes in your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha.html)

When you launch an Amazon EMR cluster, you can choose to have one or three primary nodes in your cluster.

- [Features that support high availability in an Amazon EMR cluster and how they work with open-source applications](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-applications.html): This topic provides information about the Hadoop high-availability features of HDFS NameNode and YARN ResourceManager in an Amazon EMR cluster, and how the high-availability features work with open source applications and other Amazon EMR features.
- [Launch an Amazon EMR Cluster with multiple primary nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-launch.html): This topic provides configuration details and examples for launching an Amazon EMR cluster with multiple primary nodes.
- [Amazon EMR integration with EC2 placement groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-placementgroup.html): When you launch an Amazon EMR multiple primary node cluster on Amazon EC2, you have the option to use placement group strategies to specify how you want the primary node instances deployed to protect against hardware failure.
- [Considerations and best practices for a cluster with multiple primary nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-considerations.html): Consider the following when you create an Amazon EMR cluster with multiple primary nodes:
- [EMR clusters on AWS Outposts](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-outposts.html): Beginning with Amazon EMR 5.28.0, you can create and run EMR clusters on AWS Outposts.
- [EMR clusters on AWS Local Zones](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-localzones.html): Beginning with Amazon EMR version 5.28.0, you can create and run Amazon EMR clusters on an AWS Local Zones subnet as a logical extension of an AWS Region that supports Local Zones.
- [Configure Docker for use with Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-docker.html): Amazon EMR 6.x supports Hadoop 3, which allows the YARN NodeManager to launch containers either directly on the Amazon EMR cluster or inside a Docker container.

### [Control Amazon EMR cluster termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html)

Understand and control how Amazon EMR terminates clusters and Amazon EC2 instances.

- [Configuring an Amazon EMR cluster to continue or terminate after step execution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-longrunning-transient.html): Choose whether to run your cluster as a transient process or to continue running until you deliberately shut it down.
- [Using an auto-termination policy](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-auto-termination-policy.html): Use an auto-termination policy to shut down an idle Amazon EMR cluster.
- [Using termination protection to protect your Amazon EMR clusters from accidental shut down](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html): Termination protection protects your clusters from accidental termination, which can be especially useful for long running clusters processing critical workloads.
- [Replacing unhealthy nodes with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-node-replacement.html): Amazon EMR periodically uses the NodeManager health checker service in Apache Hadoop to monitor the statuses of core nodes in your Amazon EMR on Amazon EC2 clusters.

### [Working with AMIs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ami.html)

Working with Amazon Linux Amazon Machine Images (AMIs) in Amazon EMR.

- [Using the default AMI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-default-ami.html): Each Amazon EMR release version uses a default Amazon Linux AMI for Amazon EMR unless you specify a custom AMI.
- [Using a custom AMI to provide more flexibility for Amazon EMR cluster configuration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html): Using a Custom Amazon Linux Amazon Machine Image (AMI) with Amazon EMR for advanced software configuration and root volume encryption.
- [Change the AL release](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami-change-al-release.html): When you launch a cluster using Amazon EMR 6.6.0 or higher, it automatically uses the latest Amazon Linux 2 release that has been validated for the default Amazon EMR AMI.
- [Customizing the EBS root volume](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami-root-volume-size.html): You can set your volume type and other attributes, depending on your use case and cost requirements.

### [Configure applications when you launch your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-software.html)

Configure the software to install when you launch your cluster.

- [Create bootstrap actions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-bootstrap.html): Create bootstrap actions to install additional software and to change the configuration of applications on the cluster.

### [Configure Amazon EMR cluster hardware and networking](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances.html)

Learn to plan and configure Amazon EMR cluster hardware and networking.

- [Understand node types](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html): Understand the difference between primary, core, and task nodes in an Amazon EMR cluster.

### [Configure Amazon EC2 instance types for use with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ec2-instances.html)

Configure Amazon EC2 instances for Amazon EMR.

### [Supported instance types with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-supported-instance-types.html)

View tables of the Amazon EC2 instance types that Amazon EMR supports, organized by AWS Region.

- [Instance purchasing options in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-purchasing-options.html): Understand the difference between the On-Demand and Spot Instance purchasing options for Amazon EC2 instances when you use Amazon EMR.

### [Instance storage options and behavior in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-storage.html)

Learn about Amazon EBS volume storage for HDFS data on Amazon EMR.

- [Comparing Amazon EBS volume types gp2 and gp3](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-storage-compare-volume-types.html): Here is a comparison of cost between gp2 and gp3 volumes in the US East (N.
- [Selecting IOPS and throughput when migrating to gp3 Amazon EBS volume types](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-storage-gp3-migration-selection.html): When provisioning a gp2 volume, you must figure out the size of the volume in order to get the proportional IOPS and throughput.

### [Configure networking in a VPC for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-vpc-subnet.html)

Select a subnet for your cluster to run your instances in a virtual private cloud (VPC) that's logically isolated to your AWS account.

- [Amazon VPC options when you launch a cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-clusters-in-a-vpc.html): Learn about Amazon Virtual Private Cloud options for Amazon EMR, such as public subnets, private subnets, and shared subnets.
- [Set up a VPC to host Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-vpc-host-job-flows.html): Learn how to create an Amazon Virtual Private Cloud with subnets for your Amazon EMR cluster.
- [Launch clusters into a VPC with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-vpc-launching-job-flows.html): Launch an Amazon EMR cluster in a subnet that belongs to your Amazon Virtual Private Cloud
- [Sample policies for private subnets that access Amazon S3](https://docs.aws.amazon.com/emr/latest/ManagementGuide/private-subnet-iampolicy.html): Learn about the minimum Amazon S3 policy that you need when you launch an Amazon EMR cluster in a private subnet.

### [Configure instance fleets or instance groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html)

Optimize and customize the way that Amazon EMR provisions Amazon EC2 instances for a cluster by using instance fleets and instance groups.

- [Planning and configuring instance fleets for your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html): Use the Amazon EMR console or the AWS CLI to create a cluster with an instance fleet configuration.
- [Reconfiguring instance fleets for your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/instance-fleet-reconfiguration.html): With Amazon EMR version 5.21.0 and later, you can reconfigure cluster applications and specify additional configuration classifications for each instance fleet in a running cluster.
- [Use capacity reservations with instance fleets in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/on-demand-capacity-reservations.html): Launch an Amazon EMR cluster using the On-Demand allocation strategy and capacity reservations.
- [Configure uniform instance groups for your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-uniform-instance-group.html): Create an Amazon EMR cluster with uniform instance groups to specify the configuration of the primary, core, and task nodes.
- [Availability Zone flexibility for launching instances](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-flexibility.html): How and why to express instance flexibility with Amazon EMR.
- [Guidelines and best practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html): Learn about the best practices to follow when you create an Amazon EMR cluster that uses instance fleets or instance groups.
- [Configure Amazon EMR cluster logging and debugging](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-debugging.html): Configure logging and debugging support for your cluster with the debugging tools that Amazon EMR offers.

### [Tag and categorize Amazon EMR cluster resources](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html)

Use tags to categorize the resources in your Amazon EMR cluster by assigning custom metadata.

- [Restrictions that apply to tagging resources in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-restrictions.html): Follow these basic restrictions when applying tags to your resources in Amazon EMR.
- [Tag Amazon EMR resources for billing](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-billing.html): Use tags on your resources for organizing your AWS bill to reflect your own cost structure.
- [Add tags to an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-add-new.html): Add tags to a cluster with the Amazon EMR console or CLI.
- [View tags on an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-view.html): Display all available tags on a cluster using the Amazon EMR console or CLI.
- [Remove tags from an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-delete.html): Remove tags from a cluster when you no longer need a tag using the Amazon EMR console or CLI.

### [Drivers and third-party application integration on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-third-party.html)

Run third-party big-data applications on Amazon Elastic MapReduce for a nominal additional hourly fee.

- [Use business intelligence tools with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-bi-tools.html): You can use popular business intelligence tools like Microsoft Excel, MicroStrategy, QlikView, and Tableau with Amazon EMR to explore and visualize your data.


## [Security](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-security.html)

### [Security configurations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-security-configurations.html)

Create Amazon EMR security configurations to configure data encryption, Kerberos authentication, and Amazon S3 authorization for EMRFS on your clusters.

- [Create a security configuration with the Amazon EMR console or with the AWS CLI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-create-security-configuration.html): Learn how to enable encryption, Kerberos authentication, and EMRFS authorization for Amazon S3 for an EMR cluster.
- [Specify a security configuration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-specify-security-configuration.html): Learn how to specify encryption settings for an EMR cluster with a security configuration.

### [Data protection](https://docs.aws.amazon.com/emr/latest/ManagementGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon EMR.

### [Encrypt data at rest and in transit with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-encryption.html)

Describes encryption options for data at rest and in transit with Amazon EMR.

- [Encryption options for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-encryption-options.html): With Amazon EMR releases 4.8.0 and higher, you can use a security configuration to specify settings for encrypting data at rest, data in transit, or both.
- [Encryption at rest using a customer KMS key for the EMR WAL service](https://docs.aws.amazon.com/emr/latest/ManagementGuide/encryption-at-rest-kms.html): EMR write-ahead logs (WAL) provides customer KMS key encryption-at-rest support.
- [Create keys and certificates for data encryption with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-encryption-enable.html): Describes encryption configuration Amazon EMR.
- [In-transit encryption support](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-encryption-support-matrix.html): You can configure an EMR cluster to run open-source frameworks such as Apache Spark, Apache Hive, and Presto. each of these open-source frameworks has a set of processes running on the EC2 instances of a cluster.

### [IAM with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html)

Learn to configure a user permissions for Amazon EMR to manage access to your clusters.

- [How Amazon EMR works with IAM](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon EMR, learn what IAM features are available to use with Amazon EMR.
- [Runtime roles for Amazon EMR steps](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-steps-runtime-roles.html): Control the resources that Amazon EMR and the applications it runs can access by assigning (IAM) service roles.

### [Configure service roles for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html)

Control the resources that Amazon EMR and the applications it runs can access by assigning IAM service roles.

### [Service roles used by Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-service-roles.html)

Amazon EMR uses IAM service roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources, and creating and running EMR Notebooks.

- [Amazon EMR role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role.html): The Amazon EMR role defines the allowable actions for Amazon EMR when it provisions resources and performs service-level tasks that aren't performed in the context of an Amazon EC2 instance running within a cluster.
- [EC2 instance profile](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html): The service role for cluster EC2 instances (also called the EC2 instance profile for Amazon EMR) is a special type of service role that is assigned to every EC2 instance in an Amazon EMR cluster when the instance launches.
- [Auto Scaling role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role-automatic-scaling.html): The Auto Scaling role for Amazon EMR performs a similar function as the service role, but allows additional actions for dynamically scaling environments.
- [EMR Notebooks role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-service-role.html): Each EMR notebook needs permissions to access other AWS resources and perform actions.

### [Using service-linked roles](https://docs.aws.amazon.com/emr/latest/ManagementGuide/using-service-linked-roles.html)

How to use service-linked roles to give Amazon EMR access to resources in your AWS account.

- [Cleanup role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/using-service-linked-roles-cleanup.html): How to use service-linked roles to clean up Amazon EMR resources in your AWS account.
- [WAL role](https://docs.aws.amazon.com/emr/latest/ManagementGuide/using-service-linked-roles-wal.html): How to use service-linked roles to let the Amazon EMR WAL access Amazon EMR resources in your AWS account.
- [Customize IAM roles with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles-custom.html): Create IAM roles to define the AWS resources that Amazon EMR and the applications it runs can access.
- [Configure IAM roles for EMRFS](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-emrfs-iam-roles.html)
- [Resource-based policies for AWS Glue](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles-glue.html): If you use AWS Glue in conjunction with Hive, Spark, or Presto in Amazon EMR, AWS Glue supports resource-based policies to control access to Data Catalog resources.
- [Use IAM roles with applications that call AWS services directly](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles-calling.html): Use IAM roles with SDKs for custom applications.
- [Allow users and groups to create and modify roles](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles-create-permissions.html): IAM principals (users and groups) who create, modify, and specify roles for a cluster, including default roles, must be allowed to perform the following actions.

### [Identity-based policy examples](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_iam_id-based-policy-examples.html)

By default, a users and roles don't have permission to create or modify Amazon EMR resources.

- [Policy best practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_iam_service-with-iam-policy-best-practices.html): Identity-based policies are very powerful.
- [Allow users to view their own permissions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_iam_id-based-policy-examples-view-own-permissions.html): This example shows how you might create a policy that allows a users to view the inline and managed policies that are attached to their user identity.

### [Managed policies](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-iam-policies.html)

Use managed policies for Amazon EMR to easily grant access privileges to users.

- [Full access (v2 scoped)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-policy-fullaccess-v2.html): The v2 scoped EMR default managed policies grant specific access privileges to users.
- [Full access (path to deprecation)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-policy-fullaccess.html): The AmazonElasticMapReduceFullAccess and AmazonEMRFullAccessPolicy_v2 AWS Identity and Access Management (IAM) managed policies grant all the required actions for Amazon EMR and other services.
- [Read-only (v2 scoped)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-policy-readonly-v2.html): To grant read-only privileges to Amazon EMR, attach the AmazonEMRReadOnlyAccessPolicy_v2 managed policy.
- [Read-only (path to deprecation)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-policy-readonly.html): The AmazonElasticMapReduceReadOnlyAccess managed policy is on the path to deprecation.
- [EMRDescribeClusterPolicyForEMRWAL](https://docs.aws.amazon.com/emr/latest/ManagementGuide/EMRDescribeClusterPolicyForEMRWAL.html): You can't attach EMRDescribeClusterPolicyForEMRWAL to your IAM entities.
- [Policy updates](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security-iam-awsmanpol-updates.html): View details about updates to AWS managed policies for Amazon EMR since this service began tracking these changes.
- [Policies for tag-based access control](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-fine-grained-cluster-access.html): Learn to implement fine-grained access control for Amazon EMR using cluster tags and a user policies.
- [Denying the ModifyInstanceGroup action in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cluster-deny-modifyinstancegroup.html): The ModifyInstanceGroups action in Amazon EMR does not require that you provide a cluster ID with the action.
- [Troubleshooting](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon EMR and IAM.
- [S3 Access Grants with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-access-grants.html): Access Grants from Amazon S3 are a scalable access control solution to manage access to your S3 data from Amazon EMR.

### [Authenticate to cluster nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-authenticate-cluster-connections.html)

SSH clients can use an Amazon EC2 key pair to authenticate to cluster instances.

- [Use an EC2 key pair for SSH credentials for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-ssh.html): Create SSH credentials for the primary node of the EMR cluster.

### [Use Kerberos authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html)

Amazon EMR releases 5.10.0 and higher support Kerberos.

- [Supported applications with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-principals.html): Within an EMR cluster, Kerberos principals are the big data application services and subsystems that run on all cluster nodes.
- [Architecture options](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-options.html): When you use Kerberos with Amazon EMR, you can choose from the architectures listed in this section.

### [Configuring Kerberos on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-configure.html)

This section provides configuration details and examples for setting up Kerberos with common architectures.

### [Security configuration and cluster settings](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-configure-settings.html)

When you create a Kerberized cluster, you specify the security configuration together with Kerberos attributes that are specific to the cluster.

- [Configuration examples](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-config-examples.html): The following examples demonstrate security configurations and cluster configurations for common scenarios.
- [Configuring an Amazon EMR cluster for Kerberos-authenticated HDFS users and SSH connections](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-configuration-users.html): Amazon EMR creates Kerberos-authenticated user clients for the applications that run on the clusterâfor example, the hadoop user, spark user, and others.
- [Connecting with SSH](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-connect-ssh.html): This section demonstrates the steps for a Kerberos-authenticated user to connect to the primary node of an EMR cluster.
- [Tutorial: Cluster-dedicated KDC](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-cluster-kdc.html): This topic guides you through creating a cluster with a cluster-dedicated key distribution center (KDC), manually adding Linux accounts to all cluster nodes, adding Kerberos principals to the KDC on the primary node, and ensuring that client computers have a Kerberos client installed.
- [Tutorial: Cross-realm trust](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos-cross-realm.html): When you set up a cross-realm trust, you allow principals (usually users) from a different Kerberos realm to authenticate to application components on the EMR cluster.

### [Use LDAP authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap.html)

With Amazon EMR releases 6.12.0 and higher, you can use the LDAP over SSL (LDAPS) protocol to launch a cluster that natively integrates with your corporate identity server.

- [Overview](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-overview.html): Lightweight Directory Access Protocol (LDAP) is a software protocol that network administrators use to manage and control access to data by authenticating users within a companyâs network.
- [LDAP components](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-components.html)
- [Considerations for LDAP for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-considerations.html): This topic lists supported applications, supported features and unsupported features.

### [Configure LDAP](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-setup.html)

This section covers how to configure Amazon EMR for use with LDAP authentication.

- [Secrets Manager permissions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-setup-asm.html): Amazon EMR uses an IAM service role to perform actions on your behalf to provision and manage clusters.
- [LDAP security configuration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-setup-security.html): Before you can launch an EMR cluster with LDAP integration, use the steps in to create an Amazon EMR security configuration for the cluster.
- [Launch a cluster that uses LDAP](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-setup-launch.html): Use the following steps to launch an EMR cluster with LDAP or Active Directory.
- [Examples](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-examples.html): Once you provision an EMR cluster that uses LDAP integration, you can provide your LDAP credentials to any supported application through its built-in username and password authentication mechanism.

### [Integrate Amazon EMR with Identity Center](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc.html)

Integrate EMR clusters with AWS Lake Formation.

### [Getting started](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-start.html)

Get set up to use the Identity Center

- [Use Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-lf.html): Integrate AWS Lake Formation with your AWS IAM Identity Center enabled EMR cluster.
- [Use S3 Access Grants](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-s3ag.html): Use S3 Access Grants with your AWS IAM Identity Center enabled EMR cluster.
- [User background sessions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/user-background-sessions.html): User background sessions
- [Considerations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-considerations.html): Considerations with IAM Identity Center and Amazon EMR.

### [Integrate Amazon EMR with Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lake-formation.html)

Integrate EMR clusters with AWS Lake Formation.

### [Fine-grained access with Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-fine-grained-access.html)

Fine-grained access with Lake Formation.

- [Enable Lake Formation with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-enable.html): Set up a Lake Formation security configuration and launch an Amazon EMR cluster with it.
- [Open-table format support](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-fgac1.html): Amazon EMR releases 6.15.0 and higher include support for fine-grained access control based on AWS Lake Formation with Hive tables, Apache Iceberg, Apache Hudi, and Delta Lake when you read and write data with Spark SQL.
- [Working with Glue Data Catalog views in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/SECTION-jobs-glue-data-catalog-views-ec2.html)
- [Considerations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-limitations-cont.html): What to consider when you use Amazon EMR with Lake Formation.
- [Spark native fine-grained access control alllowlisted PySpark API](https://docs.aws.amazon.com/emr/latest/ManagementGuide/clean-rooms-spark-fgac-pyspark-api-allowlist.html): Reference document and searchable list for supported PySpark function use within Amazon EMR Spark FGAC
- [Lake Formation full table access for Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-unfiltered-ec2-access.html): Learn how to use AWS Lake Formation with full table permissions in Amazon EMR releases 7.8.0 and higher without fine-grained access control limitations.

### [Integrate Amazon EMR with Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger.html)

Beginning with Amazon EMR 5.32.0, you can launch a cluster that natively integrates with Apache Ranger.

### [Ranger overview](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-overview.html)

Apache Ranger is a framework to enable, monitor, and manage comprehensive data security across the Hadoop platform.

- [Ranger architecture](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-architecture.html)
- [Amazon EMR components](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-components.html): Amazon EMR enables fine-grained access control with Apache Ranger through the following components.
- [Considerations for using Amazon EMR with Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-app-support.html)

### [Set up Amazon EMR for Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-begin.html)

Before you install Apache Ranger, review the information in this section to make sure that Amazon EMR is properly configured.

### [Set up a Ranger Admin server to integrate with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-admin.html)

For Amazon EMR integration, the Apache Ranger application plugins must communicate with the Admin server using TLS/SSL.

- [TLS certificates for Apache Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-admin-tls.html): Apache Ranger integration with Amazon EMR requires that traffic from Amazon EMR nodes to the Ranger Admin server is encrypted using TLS, and that Ranger plugins authenticate to the Apache Ranger server using two-way mutual TLS authentication.
- [Service definition installation for Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-admin-servicedef-install.html): A service definition is used by the Ranger Admin server to describe the attributes of policies for an application.
- [Network traffic rules for integrating with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-network.html): When Apache Ranger is integrated with your EMR cluster, the cluster needs to communicate with additional servers and AWS.

### [IAM roles for native integration with Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam.html)

The integration between Amazon EMR and Apache Ranger relies on three key roles that you should create before you launch your cluster:

- [EC2 instance profile for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam-ec2.html): Amazon EMR uses an IAM service role to perform actions on your behalf to provision and manage clusters.
- [IAM role for Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam-ranger.html): This role provides credentials for trusted execution engines, such as Apache Hive and Amazon EMR Record Server to access Amazon S3 data.
- [IAM role for other AWS services for Amazon EMR integration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam-other-AWS.html): This role provides users who are not trusted execution engines with credentials to interact with AWS services, if needed.
- [Validate your permissions for Amazon EMR integration with Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam-validate.html): See for instructions on validating permissions.
- [Create the EMR security configuration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-security-config.html): Creating an Amazon EMR Security Configuration for Apache Ranger
- [Store TLS certificates in AWS Secrets Manager](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-tls-certificates.html): The Ranger plugins installed on an Amazon EMR cluster and the Ranger Admin server must communicate over TLS to ensure that policy data and other information sent cannot be read if they are intercepted.
- [Start an EMR cluster with Apache Ranger](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-start-emr-cluster.html): Before you launch an Amazon EMR cluster with Apache Ranger, make sure each component meets the following minimum version requirement:
- [Configure Zeppelin](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-configure-zeppelin.html): Configure Apache Zeppelin for Apache Ranger on Amazon EMR so that you can use Zeppelin notebooks for interactive data exploration.
- [Known issues for Amazon EMR integration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-security-considerations.html): Known Issues

### [Apache Ranger plugins for Amazon EMR integration scenarios](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-plugins.html)

Apache Ranger plugins validate the access of a user against the authorization policies defined in the Apache Ranger policy admin server.

- [Apache Hive plugin for Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-hive.html): Apache Hive is a popular execution engine within the Hadoop ecosystem.
- [Apache Spark plugin for Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-spark.html): Amazon EMR has integrated EMR RecordServer to provide fine-grained access control for SparkSQL.
- [EMRFS S3 plugin for Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-emrfs.html): To make it easier to provide access controls against objects in S3 on a multi-tenant cluster, the EMRFS S3 plugin provides access controls to the data within S3 when accessing it through EMRFS.
- [Trino plugin for Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-trino.html): Trino (previously PrestoSQL) is a SQL query engine that you can use to run queries on data sources such as HDFS, object storage, relational databases, and NoSQL databases.

### [Apache Ranger troubleshooting](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-troubleshooting.html)

Here are some commonly diagnosed issues related to using Apache Ranger.

- [EMR cluster failed to provision](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-troubleshooting-cluster-failed.html): There are several reasons why an Amazon EMR cluster may fail to start.
- [Queries are unexpectedly failing for Ranger integration with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-troubleshooting-queries-failed.html): Check Apache Ranger plugin logs (Apache Hive, EMR RecordServer, EMR SecretAgent, etc., logs)

### [Control network traffic with security groups for your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-security-groups.html)

Learn to configure security groups for Amazon EMR, which control inbound and outbound access to cluster instances.

- [Working with Amazon EMR-managed security groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-man-sec-groups.html)
- [Working with additional security groups for an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-additional-sec-groups.html): Additional security groups allow users to apply customized inbound and outbound access rules to Amazon EMRâmanaged security groups.
- [Specifying security groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-sg-specify.html): You can specify security groups using the AWS Management Console, the AWS CLI, or the Amazon EMR API.
- [Security groups for EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html): When you create an EMR notebook, two security groups are used to control network traffic between the EMR notebook and the Amazon EMR cluster when you use the notebook editor.
- [Block public access](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html): Amazon EMR block public access (BPA) prevents you from launching a cluster in a public subnet if the cluster has a security configuration that allows inbound traffic from public IP addresses on a port.
- [Compliance validation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/emr/latest/ManagementGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EMR features for data resiliency.

### [Infrastructure security](https://docs.aws.amazon.com/emr/latest/ManagementGuide/infrastructure-security.html)

Learn how Amazon EMR isolates service traffic.

- [Connect to Amazon EMR using an interface VPC endpoint](https://docs.aws.amazon.com/emr/latest/ManagementGuide/interface-vpc-endpoint.html): Access Amazon EMR using an interface VPC endpoint.


## [Manage Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage.html)

### [Connect to an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node.html)

Connect to an Amazon EMR cluster.

- [Before you connect](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-ssh-prereqs.html): Set up inbound traffic authorization over SSH before you connect to your Amazon EMR cluster.

### [Connect to the Amazon EMR cluster primary node using SSH](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html)

Connect to the Amazon EMR primary node using SSH on Windows, Linux, Unix, or Mac OS X.

- [Amazon EMR service ports](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-service-ports.html)

### [View web interfaces hosted on Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-web-interfaces.html)

View websites hosted on Amazon EMR clusters.

- [Option 1: Set up an SSH tunnel to the Amazon EMR primary node using local port forwarding](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ssh-tunnel-local.html): Create an SSH connection with the Amazon EMR primary node using local port forwarding.
- [Option 2, part 1: Set up an SSH tunnel to the primary node using dynamic port forwarding](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ssh-tunnel.html): Create an SSH tunnel with the Amazon EMR primary node using dynamic port forwarding (SOCKS).
- [Option 2, part 2: Configure proxy settings to view websites hosted on the Amazon EMR cluster primary node](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html): Configure a SOCKS proxy add-on for your browser to dynamically load websites hosted on the Amazon EMR primary node.

### [Submit work to an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-work-with-steps.html)

Add steps to a cluster and submit Hadoop jobs to a cluster.

- [Add steps with the console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-add-steps-console.html): Use the following procedures to add steps to a cluster with the AWS Management Console.
- [Add steps with the CLI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/add-step-cli.html): The following procedures demonstrate how to add steps to a newly created cluster and to a running cluster with the AWS CLI.
- [Running multiple steps](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-concurrent-steps.html): Running multiple steps in parallel when you submit work to Amazon EMR requires preliminary decisions about resource planning and expectations regarding cluster behavior.
- [Viewing steps after submitting work to an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-view-steps.html): You can see up to 10,000 steps that Amazon EMR completed within the last seven days.
- [Cancel steps when you submit work to an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cancel-steps.html): You can cancel pending and running steps from the AWS Management Console, the AWS CLI, or the Amazon EMR, when you submit work to your cluster.

### [View and monitor an Amazon EMR cluster as it performs work](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view.html)

Monitor and view information about the cluster from the console, the CLI or programmatically.

- [View Amazon EMR cluster status and details](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-clusters.html): Monitor the status, view cluster details, and retrieve extended information about a cluster and its execution.
- [Enhanced step debugging with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-enhanced-step-debugging.html): If an Amazon EMR step fails and you submitted your work using the Step API operation with an AMI of version 5.x or later, Amazon EMR can identify and return the root cause of the step failure in some cases, along with the name of the relevant log file and a portion of the application stack trace via API.

### [View Amazon EMR application history](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cluster-application-history.html)

Monitor application execution for Spark and YARN.

- [View persistent application user interfaces in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html): Starting with Amazon EMR version 5.25.0, you can connect to the persistent Spark History Server application details hosted off-cluster using the cluster Summary page or the Application user interfaces tab in the console.
- [View a high-level application history in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-summary.html)
- [View Amazon EMR log files](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html): View the log files that report status on the cluster produced by Hadoop and Amazon EMR.
- [View cluster instances in Amazon EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_Tagging.html): View cluster instances and manage resource in Amazon EC2 by assigning metadata tags to the resources.

### [CloudWatch events and metrics from Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-cluster-cloudwatch.html)

Monitor and manage Amazon EMR cluster activity and health with Amazon CloudWatch Events and CloudWatch metrics.

- [Monitor metrics](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.html): Monitor the status of your Amazon EMR cluster with CloudWatch metrics.
- [Monitor events](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-cloudwatch-events.html): Track the status of your Amazon EMR cluster with CloudWatch events.

### [Respond to events](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-events-response.html)

Take action in response to Amazon EMR event messages from CloudWatch.

- [Create rules](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-events-cloudwatch-console.html): Amazon EMR automatically sends events to a CloudWatch event stream.
- [Set alarms](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_ViewingMetrics_Alarm.html): Amazon EMR pushes metrics to Amazon CloudWatch.
- [Respond to insufficient capacity events](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-events-response-insuff-capacity.html): How to respond to EMR cluster events that have event code "EC2 provisioning - Insufficient Instance Capacity"
- [Respond to instance fleet resize timeout events](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-events-response-timeout-events.html): How to respond to EMR cluster instance fleet resize timeout events"
- [View cluster application metrics using Ganglia with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/ViewingGangliaMetrics.html): Track the progress and health of your cluster with monitoring metrics from CloudWatch.
- [CloudTrail logs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/logging-using-cloudtrail.html): Learn about logging AWS EMR with AWS CloudTrail.
- [EMR Observability Best Practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-metrics-observability.html): EMR Observability encompasses a comprehensive monitoring and management approach for AWS EMR clusters.

### [Use Amazon EMR cluster scaling to adjust for changing workloads](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-scale-on-demand.html)

Use cluster scaling to adjust the number of Amazon EC2 instances available to an Amazon EMR cluster automatically or manually in response to workloads that have varying demands

### [Managed scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-scaling.html)

Enable Amazon EMR managed scaling to automatically increase or decrease the number of instances or units in your cluster based on workload.

- [Configure managed scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/managed-scaling-configure.html): Launch an EMR cluster that uses managed scaling with the AWS Management Console, the AWS SDK for Java, or the AWS Command Line Interface.
- [Advanced Scaling for EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/managed-scaling-allocation-strategy-optimized.html): Advanced scaling for further improving resource utilization for a cluster.
- [Node allocation strategies](https://docs.aws.amazon.com/emr/latest/ManagementGuide/managed-scaling-allocation-strategy.html): Understand node allocation strategies and common scaling scenarios for Amazon EMR managed scaling.
- [Managed scaling metrics](https://docs.aws.amazon.com/emr/latest/ManagementGuide/managed-scaling-metrics.html): Understand managed scaling metrics for Amazon EMR that indicate current or target cluster capacity and cluster application status.
- [Automatic scaling with a custom policy](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html): Use automatic scaling with Amazon EMR to programmatically scale core and task nodes based on a CloudWatch metric and a scaling policy.
- [Resize a running cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-resize.html): Increase or decrease the number of nodes in a running Amazon EMR cluster using either the console, CLI, or API.

### [Provisioning timeouts](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-provisioning-timeout.html)

When you use instance fleets, you can configure timeouts for provisioning capacity during cluster launch and cluster scaling operations.

- [Provisioning timeout for launch](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-provisioning-timeout-launch.html): Customize a provisioning timeout period for cluster launch in Amazon EMR.
- [Provisioning timeout for resize](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-provisioning-timeout-resize.html): Define a timeout period for provisioning Spot Instances for each fleet in your Amazon EMR cluster.

### [Cluster scale-down options for Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-scaledown-behavior.html)

Configure scale-down behavior for Amazon EMR clusters.

- [Configure Amazon EMR scale-down behavior](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-scaledown-configure.html)
- [Terminate an Amazon EMR cluster in the starting, running, or waiting states](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminateJobFlow.html): Terminate a cluster that is in the starting, running, or waiting states.
- [Clone a cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/clone-console.html): Clone a cluster, which makes a copy of the configuration of the original cluster to use as the basis for a new cluster using the Amazon EMR console.
- [Automate recurring Amazon EMR clusters with AWS Data Pipeline](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-recurring.html): Automate regular schedules for moving input data and launching clusters to process data with the AWS Data Pipeline service.


## [Amazon EMR tutorials](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-tutorials.html)

- [Amazon EMR on EC2 â Enhanced Monitoring with CloudWatch using custom metrics and logs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/enhanced-custom-metrics.html): Learn how to configure enhanced monitoring capabilities for Amazon EMR clusters using CloudWatch, including custom metrics collection and log aggregation.
- [Monitor Apache Spark applications on Amazon EMR with Amazon CloudWatch](https://docs.aws.amazon.com/emr/latest/ManagementGuide/enhanced-custom-metrics-applications.html): Learn how to configure enhanced monitoring capabilities for Amazon EMR clusters using CloudWatch, including custom metrics collection and log aggregation.
- [Monitor Amazon EMR application status with CloudWatch integration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/enhanced-custom-metrics-application-status.html): When you integrate CloudWatch with Amazon EMR, you can track critical statuses for applications like HiveServer2.
- [Debugging EMR steps Using YARN application IDs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/debug-emr-yarn.html): One effective way to debug steps that launch YARN-based applications (such as Spark steps) is to leverage the Yarn Application ID information available in the Amazon EMR console.

### [Observability and additional logging features](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-debugging-logging-observability.html)

Configure logging and debugging support for your cluster.

- [Customizing the log location for step log files](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-debugging-step-log-customization.html): Learn how to customize S3 logging behavior for steps on a per-step basis in Amazon EMR.
- [Publish Amazon EMR logs to CloudWatch Logs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-logging-cw.html): Learn how to configure Amazon EMR to send cluster logs directly to Amazon CloudWatch Logs.


## [Troubleshoot Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot.html)

- [Troubleshooting tools](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-tools.html): There are several tools that can help you troubleshoot unexpected behavior with your cluster.
- [View and restart processes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-process-restart-stop-view.html): How to view, restart, and stop Amazon EMR, Hadoop, and other big-data processes.

### [Common errors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-errors.html)

Troubleshoot some common errors in an EMR cluster.

### [Error codes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-errordetail.html)

Troubleshoot errors that return ErrorDetail data.

### [Bootstrap failures](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-errordetail-bootstrap.html)

Troubleshoot bootstrap errors that might cause your cluster to fail.

- [Primary with non zero code](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_PRIMARY_WITH_NON_ZERO_CODE.html)
- [BA download failed primary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_BA_DOWNLOAD_FAILED_PRIMARY.html)
- [File not found primary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_FILE_NOT_FOUND_PRIMARY.html)
- [Insufficient disk space primary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY.html)
- [Insufficient disk space worker](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_WORKER.html)
- [Hive metastore connection error primary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_PRIMARY.html)
- [Hive metastore connection error worker](https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER.html)

### [Internal errors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-errordetail-internal.html)

Troubleshoot internal errors that might cause your cluster to fail.

- [EC2 insufficient capacity AZ](https://docs.aws.amazon.com/emr/latest/ManagementGuide/INTERNAL_ERROR_EC2_INSUFFICIENT_CAPACITY_AZ.html)
- [Spot price increase primary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/INTERNAL_ERROR_SPOT_PRICE_INCREASE_PRIMARY.html)
- [Spot no capacity primary](https://docs.aws.amazon.com/emr/latest/ManagementGuide/INTERNAL_ERROR_SPOT_NO_CAPACITY_PRIMARY.html)

### [Validation failures](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-errordetail-validation.html)

Troubleshoot validation errors that might cause your cluster to fail.

- [Subnet not from one VPC](https://docs.aws.amazon.com/emr/latest/ManagementGuide/VALIDATION_ERROR_SUBNET_NOT_FROM_ONE_VPC.html)
- [Security group not from one VPC](https://docs.aws.amazon.com/emr/latest/ManagementGuide/VALIDATION_ERROR_SECURITY_GROUP_NOT_FROM_ONE_VPC.html)
- [Invalid SSH key name](https://docs.aws.amazon.com/emr/latest/ManagementGuide/VALIDATION_ERROR_INVALID_SSH_KEY_NAME.html)
- [Instance type not supported](https://docs.aws.amazon.com/emr/latest/ManagementGuide/VALIDATION_ERROR_INSTANCE_TYPE_NOT_SUPPORTED.html)

### [Resource errors during Amazon EMR cluster operations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-resource.html)

Troubleshoot some of the common errors caused by constrained resources on the cluster, including NO_SLAVE_LEFT and FAILED_BY_MASTER.

- [Amazon EMR cluster terminates with NO_SLAVE_LEFT and core nodes FAILED_BY_MASTER](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cluster-NO_SLAVE_LEFT-FAILED_BY_MASTER.html): Usually, this happens because termination protection is disabled, and all core nodes exceed disk storage capacity as specified by a maximum utilization threshold in the yarn-site configuration classification, which corresponds to the yarn-site.xml file.
- [Amazon EMR cluster error: Cannot replicate block, only managed to replicate to zero nodes.](https://docs.aws.amazon.com/emr/latest/ManagementGuide/enough-hdfs-space.html): The error, "Cannot replicate block, only managed to replicate to zero nodes." typically occurs when a cluster does not have enough HDFS storage.
- [Amazon EMR cluster error: EC2 QUOTA EXCEEDED](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-EC2.html): If you get an EC2 QUOTA EXCEEDED message, there may be several causes.
- [Amazon EMR cluster error: Too many fetch-failures](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-resource-1.html): The presence of "Too many fetch-failures" or "Error reading task output" error messages in step or task attempt logs indicates the running task is dependent on the output of another task.
- [Amazon EMR cluster error: File could only be replicated to 0 nodes instead of 1](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-resource-2.html): When a file is written to HDFS, it is replicated to multiple core nodes.
- [Amazon EMR cluster error: Deny-listed nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-resource-3.html): The NodeManager daemon is responsible for launching and managing containers on core and task nodes.
- [Throttling errors with an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-throttling-error.html): The errors "Throttled from Amazon EC2 while launching cluster" and "Failed to provision instances due to throttling from Amazon EC2" occur when Amazon EMR cannot complete a request because another service has throttled the activity.
- [Amazon EMR cluster error: Instance type not supported](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-INSTANCE_TYPE_NOT_SUPPORTED-error.html): If you create a cluster, and it fails with the error message "The requested instance type InstanceType is not supported in the requested Availability Zone," it means that you created the cluster and specified an instance type for one or more instance groups that is not supported by Amazon EMR in the Region and Availability Zone where the cluster was created.
- [Amazon EMR cluster error: EC2 is out of capacity](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-EC2_INSUFFICIENT_CAPACITY-error.html): An EC2 is out of capacity for InstanceType error occurs when you attempt to create a cluster, or add instances to a cluster, in an Availability Zone which has no more of the specified EC2 instance type.
- [Amazon EMR cluster error: HDFS replication factor error](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-hdfs-insufficient-replication.html): When you remove a core node from a core instance group or instance fleet, Amazon EMR might run into an HDFS replication error.
- [Amazon EMR cluster error: HDFS insufficient space error](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-hdfs-insufficient-space.html): An Hadoop Distributed File System (HDFS) insufficient space error can occur if you attempt to remove a core node, but Amazon EMR can't safely complete the operation because of insuficicent space left in the HDFS.
- [Cluster input and output errors during Amazon EMR operations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-errors-io.html): Troubleshoot common errors in cluster input and output operations.
- [Permissions errors during Amazon EMR cluster operations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-permissions.html): Troubleshoot some of the common errors when using permissions or credentials.
- [Hive cluster errors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-hive.html): Troubleshoot some of the common Hive cluster errors in the syslog file.
- [VPC errors during Amazon EMR cluster operations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-vpc.html): Troubleshoot some of the common errors in VPC configuration in Amazon Elastic MapReduce.
- [Streaming Amazon EMR cluster errors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-streaming.html): Troubleshoot some of the common errors to streaming clusters in Amazon Elastic MapReduce.
- [Amazon EMR: Custom JAR cluster errors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-custom-jar.html): Troubleshoot some of the common errors in custom JAR cluster operations.
- [Amazon EMR AWS GovCloud (US-West) errors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-error-govcloud.html): Troubleshoot some of the common errors that are specific to the AWS GovCloud (US-West) region.

### [Troubleshoot failed clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed.html)

Troubleshoot some of the common errors and causes of a failed cluster.

- [Step 1: Gather data about the issue with the Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed-1.html): Gather information about what went wrong with the failed Amazon EMR cluster and get the current status and configuration of the cluster.
- [Step 2: Check the environment](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed-2.html): Check the environment running Amazon EMR for issues with web services or open-source software.
- [Step 3: Look at the last state change](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed-3.html): Look at the last state change information to see what occurred the last time the cluster changed state.
- [Step 4: Examine the Amazon EMR log files](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed-4.html): Examine the log files in order to locate an error code or other indication of the issue on why the cluster failed.
- [Step 5: Test the Amazon EMR cluster step by step](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed-5-test-steps.html): Test the cluster step by step to by restarting the cluster and submit the steps to it one by one.

### [Troubleshoot a slow cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow.html)

Troubleshoot some of the common reasons that your cluster might run slowly.

- [Step 1: Gather data about the issue with the Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-1.html): Gather information about what went wrong and get the current status and configuration of the cluster.
- [Step 2: Check the EMR cluster environment](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-2.html): Check your environment to see if there are service outages or you have exceeded an AWS service limit.
- [Step 3: Examine the log files for the Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-3.html): Examine the log files to see if you can locate an error code for what went wrong with your cluster.
- [Step 4: Check Amazon EMR cluster and instance health](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-4.html): Check the cluster and the health of your instances.
- [Step 5: Check for suspended groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-5.html): Check for suspended groups where an instance group encounters too many errors while trying to launch nodes.
- [Step 6: Review configuration settings for the Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-6.html): Review the configuration settings for specific details on how the cluster is set up.
- [Step 7: Examine input data for the Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-slow-7.html): Examine your input data so that there is not an imbalanced distribution of work.
- [Troubleshoot common issues when using Amazon EMR with AWS Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-lf.html): This section walks you through the process of troubleshooting common issues when using Amazon EMR with AWS Lake Formation.


## [Write applications that launch and manage Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/making_api_requests.html)

- [End-to-end Amazon EMR Java source code sample](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-common-programming-sample.html): Use this end-to-end Java code example to install the AWS Toolkit for Eclipse and add steps to an Amazon EMR cluster.
- [Common concepts for Amazon EMR API calls](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-common-programming-concepts.html): Apply these common concepts for calling the Amazon EMR API.

### [Use SDKs to call Amazon EMR APIs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/call-emr-using-sdks.html)

Use the AWS SDKs to call Amazon EMR APIs to simplify the process of writing your application.

- [Using the AWS SDK for Java to create an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/calling-emr-with-java-sdk.html): Review this Java code example for how to use the AWS SDK for Java to create an Amazon EMR cluster.

### [Manage Amazon EMR Service Quotas](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-service-limits-manage.html)

This section describes EMR service quotas (formerly referred to as service limits), how to manage them in the AWS Management Console, and when it's better to use CloudWatch events instead of service quotas to monitor clusters and trigger actions.

- [What are Amazon EMR Service Quotas](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-service-limits-what-are.html): Your AWS account has default service quotas, also known as limits, for each AWS service.
- [How to manage Amazon EMR Service Quotas](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-service-limits-strategy.html): Service Quotas is an AWS feature that you can use to view and manage your Amazon EMR service quotas or limits from a central location, using the AWS Management Console, the API or the AWS CLI.
- [When to set up EMR events in CloudWatch](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-service-limits-cloudwatch-events.html): For some polling APIs, such as DescribeCluster, DescribeStep, and ListClusters, setting up a CloudWatch event can reduce the response time to changes and free up your service quotas.
