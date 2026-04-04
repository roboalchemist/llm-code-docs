# Source: https://docs.aws.amazon.com/finspace/latest/userguide/llms.txt

# Amazon FinSpace User Guide

> Provides a conceptual overview of Amazon FinSpace, and detailed information about how to configure FinSpace catalog, load data, organize and prepare data, and perform analysis.

- [What is Amazon FinSpace?](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)
- [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html)
- [Service quotas](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-quotas.html)
- [Document history](https://docs.aws.amazon.com/finspace/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/finspace/latest/userguide/glossary.html)

## [Managed kdb Insights](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb.html)

- [Permissions required for Managed kdb](https://docs.aws.amazon.com/finspace/latest/userguide/permissions-managed-kdb.html): You must have certain IAM permissions to use Managed kdb.

### [Managed kdb environments](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-environment.html)

The Managed kdb Insights environment provides a logical container where you can launch and run clusters, and store data from kdb that can be used by the clusters.

- [Managing kdb environments](https://docs.aws.amazon.com/finspace/latest/userguide/using-kdb-environment.html): The following sections provide a detailed overview of the operations that you can perform by using a Managed kdb Insights environment.
- [Managing environment network settings](https://docs.aws.amazon.com/finspace/latest/userguide/manage-environment-network.html): For each Managed kdb Insights environment, you can configure a network connection to allow the Managed kdb clusters running in your environment infrastructure account to access resources in your internal network.

### [Tutorial: Configuring and validating outbound network connectivity](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-outbound-ntw-tgw.html)

How to create and outbound network and validate it by using a transit gateway.

- [Step 1: Configuring a network connection](https://docs.aws.amazon.com/finspace/latest/userguide/step1-config-ntw.html)
- [Step 2: Adding DNS details](https://docs.aws.amazon.com/finspace/latest/userguide/step2-dns-details.html): The Network tab on the Kdb environments details page allows you to add custom DNS server name and IP address.
- [Step 3: Setting up a transit gateway VPC attachment](https://docs.aws.amazon.com/finspace/latest/userguide/step3-setup-tgw-attachment.html)
- [Step 4: Configuring routes](https://docs.aws.amazon.com/finspace/latest/userguide/step4-config-routing-tgw.html): With a VPC, you must create routes to send traffic to the transit gateway.
- [Step 5: Configuring security group inbound rules](https://docs.aws.amazon.com/finspace/latest/userguide/step5-config-inbound-rule.html): After you set up routing, you need to add inbound rule for the default security group to allow inbound traffic.
- [Step 6: Validating network connectivity](https://docs.aws.amazon.com/finspace/latest/userguide/step6-validate-ntw.html): After youâve successfully created an outbound network connectivity between FinSpace VPC and your VPC using transit gateway, you can validate the network configuration.
- [Step 7: Validating connection using the DNS](https://docs.aws.amazon.com/finspace/latest/userguide/step7-validate-connection-dns-server.html): As an example, create a private hosted zone in your account that has an A record rule for example.com and Private IP DNS name of customerEc2Instance.

### [Managed kdb databases](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-db.html)

A Managed kdb Insights database acts as a highly available and scalable repository to store your kdb data files so that they can be used with one or more historical database (HDB) clusters in FinSpace kdb.

- [Managing kdb databases](https://docs.aws.amazon.com/finspace/latest/userguide/using-kdb-db.html): The following sections provide a detailed overview of the operations that you can perform by using a Managed kdb database.

### [Dataviews for querying data](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-dataviews.html)

Learn all about Amazon FinSpace managed kdb dataviews.

- [Managing kdb dataviews](https://docs.aws.amazon.com/finspace/latest/userguide/managing-kdb-dataviews.html): Learn how you can create, delete, view, and update a Amazon FinSpace managed kdb dataview.

### [Database maintenance](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-databases-dbmaint.html)

Learn how you can use the database maintenance feature in FinSpace.

- [Setting up for database maintenance](https://docs.aws.amazon.com/finspace/latest/userguide/dbmaint-writable-database-dataviews.html): Learn how you can create writeable database for maintenance operation in FinSpace.
- [Performing database maintenance](https://docs.aws.amazon.com/finspace/latest/userguide/dbmaint-long-running-dbmaint.html): Learn how you can perform database maintenance operations in FinSpace

### [Managed kdb scaling groups](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-scaling-groups.html)

Learn all about Amazon FinSpace managed kdb scaling groups in detail.

### [Managing kdb scaling groups](https://docs.aws.amazon.com/finspace/latest/userguide/managing-scaling-groups.html)

Learn how to use and managed Amazon FinSpace managed kdb scaling groups.

- [Creating a Managed kdb scaling group](https://docs.aws.amazon.com/finspace/latest/userguide/create-scaling-groups.html): Learn how to create Managing kdb scaling groups in Amazon FinSpace.
- [Viewing a Managing kdb scaling group](https://docs.aws.amazon.com/finspace/latest/userguide/view-kdb-scaling-groups.html): Learn how to view existing Amazon FinSpace Managed kdb scaling groups.
- [Deleting a Managing kdb scaling group](https://docs.aws.amazon.com/finspace/latest/userguide/delete-kdb-scaling-groups.html): Learn how to delete the Amazon FinSpace Managed kdb scaling groups.

### [Managed kdb volumes](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-volumes.html)

Learn all about Amazon FinSpace managed kdb volumes.

### [Managing kdb volumes](https://docs.aws.amazon.com/finspace/latest/userguide/managing-kdb-volumes.html)

Learn how you can use the Amazon FinSpace managed kdb volumes.

- [Creating a Managed kdb volume](https://docs.aws.amazon.com/finspace/latest/userguide/create-volumes.html): Learn how to create Managed kdb volume in Amazon FinSpace.
- [Viewing a Managed kdb volume](https://docs.aws.amazon.com/finspace/latest/userguide/view-volumes.html): Learn how to view Managed kdb volume after you create them in Amazon FinSpace.
- [Updating a Managed kdb volume](https://docs.aws.amazon.com/finspace/latest/userguide/update-volumes.html): Learn how to update the Managed kdb volumes after you create them in Amazon FinSpace.
- [Deleting a Managed kdb volume](https://docs.aws.amazon.com/finspace/latest/userguide/delete-volumes.html): Learn how to delete the Managed kdb volumes.

### [Managed kdb clusters](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-clusters.html)

A FinSpace Managed kdb Insights cluster is a set of compute resources that run kdb processes in a FinSpace Managed kdb environment.

- [Scaling groups cluster vs dedicated cluster](https://docs.aws.amazon.com/finspace/latest/userguide/kdb-clusters-running-clusters-comparison.html): The original Amazon FinSpace Managed kdb cluster launch configuration is now referred to as a dedicated cluster.
- [Cluster types](https://docs.aws.amazon.com/finspace/latest/userguide/kdb-cluster-types.html): Amazon FinSpace supports a variety of kdb clusters that you can use for different uses cases such as to implement a standard kdb tick architecture.

### [Managing kdb clusters](https://docs.aws.amazon.com/finspace/latest/userguide/managing-kdb-clusters.html)

The following sections provide a detailed overview of the operations that you can perform by using Managed kdb clusters.

- [Activating your kdb license](https://docs.aws.amazon.com/finspace/latest/userguide/kdb-licensing.html): To run Managed kdb Insights clusters, you must first have an existing kdb Insights license from KX.
- [Cluster software bundles](https://docs.aws.amazon.com/finspace/latest/userguide/kdb-software-bundles.html): When you launch a cluster, you can choose the software versions that will run on your cluster.
- [Maintaining a Managed kdb Insights cluster](https://docs.aws.amazon.com/finspace/latest/userguide/maintaining-kdb-clusters.html): Maintaining a kdb cluster involves updates to the cluster's underlying operating system or to the container hosting the Managed kdb Insights software.

### [Creating a cluster](https://docs.aws.amazon.com/finspace/latest/userguide/create-kdb-clusters.html)

Learn how to create kdb clusters by using console in Amazon FinSpace.

- [Opening the cluster wizard](https://docs.aws.amazon.com/finspace/latest/userguide/create-cluster-tab.html)
- [Step 1: Add cluster details](https://docs.aws.amazon.com/finspace/latest/userguide/create-cluster-step1.html): Specify details for each of the following sections on Add cluster details page.
- [Step 2: Add code](https://docs.aws.amazon.com/finspace/latest/userguide/create-cluster-step2.html): You can load q code onto your kdb cluster so that you can run it when the cluster is running.
- [Step 3: Configure VPC settings](https://docs.aws.amazon.com/finspace/latest/userguide/create-cluster-step3.html): You connect to your cluster using q IPC through an AWS PrivateLink VPC endpoint.
- [Step 4: Configure data and storage](https://docs.aws.amazon.com/finspace/latest/userguide/create-cluster-step4.html): Choose data and storage configurations that will be used for the cluster.
- [Step 5: Review and create](https://docs.aws.amazon.com/finspace/latest/userguide/create-cluster-step5.html)
- [Viewing a cluster](https://docs.aws.amazon.com/finspace/latest/userguide/view-kdb-clusters.html)
- [Updating code configurations](https://docs.aws.amazon.com/finspace/latest/userguide/update-cluster-code.html): Learn how to update code configurations on a running cluster without creating a new one.
- [Updating a cluster database](https://docs.aws.amazon.com/finspace/latest/userguide/update-kdb-clusters-databases.html): You can update the databases mounted on a kdb cluster using the console.
- [Deleting a cluster](https://docs.aws.amazon.com/finspace/latest/userguide/delete-kdb-clusters.html)

### [Using Managed kdb clusters](https://docs.aws.amazon.com/finspace/latest/userguide/using-kdb-clusters.html)

After you successfully create clusters in your kdb environment, you can use the clusters to do the following:

- [Managing kdb users](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-users.html): The following sections provide a detailed overview of the operations that you can perform by using Managed kdb Insights users.
- [Interacting with a kdb cluster](https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-clusters.html): To run commands on a Managed kdb Insights cluster, you must establish a q connection to a cluster endpoint or individual node in a cluster.

### [Running code on a Managed kdb Insights cluster](https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-loading-code.html)

Learn how to load code on to a cluster using the q API operations.

- [.z namespace override](https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-z-namespace.html): KX uses the .z namespace that contains environment variables and functions, and hooks for callbacks.
- [Supported system commands](https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-system-commands.html): Optimizing FinSpace Workflows with System Commands: A Comprehensive Guide.
- [FinSpace q API reference](https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-q-apis.html): FinSpace provides a set of q APIs that you can use to interact with resources in your Managed kdb environment.
- [Logging and monitoring](https://docs.aws.amazon.com/finspace/latest/userguide/kdb-cluster-logging-monitoring.html): Amazon FinSpace provides a variety of Amazon CloudWatch metrics that you can monitor to determine the health and performance of your FinSpace resources and instances.


## [Dataset browser (deprecated)](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-dataset-browser.html)

- [Core concepts and terms](https://docs.aws.amazon.com/finspace/latest/userguide/concepts-terms.html)

### [Getting started](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-getting-started.html)

### [Setting up the environment](https://docs.aws.amazon.com/finspace/latest/userguide/setting-up-for-amazon-finspace.html)

- [Sign up for AWS](https://docs.aws.amazon.com/finspace/latest/userguide/sign-up-for-aws.html)
- [Create an environment](https://docs.aws.amazon.com/finspace/latest/userguide/create-an-amazon-finspace-environment.html)
- [Sample data bundles](https://docs.aws.amazon.com/finspace/latest/userguide/sample-data-bundle.html)
- [Signing in to the application](https://docs.aws.amazon.com/finspace/latest/userguide/signing-into-amazon-finspace.html)
- [Using the homepage](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-homepage.html)
- [Search and browse](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-search-browse.html)

### [Understanding datasets](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-config-catalog.html)

- [Configuring categories](https://docs.aws.amazon.com/finspace/latest/userguide/categories.html)
- [Configuring controlled vocabularies](https://docs.aws.amazon.com/finspace/latest/userguide/controlled-vocabularies.html)
- [Configuring attribute sets](https://docs.aws.amazon.com/finspace/latest/userguide/attribute-sets.html)
- [Tutorial: Configuring a business data catalog](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-build-business-catalog.html)
- [Loading and analyzing data](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-load-data-analyze-finspace.html)

### [Add and manage data](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-add-data.html)

- [Loading data](https://docs.aws.amazon.com/finspace/latest/userguide/load-data-into-finspace.html)
- [Supported data types and file formats](https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html)

### [Working with datasets](https://docs.aws.amazon.com/finspace/latest/userguide/working-with-datasets.html)

- [Dataset details page](https://docs.aws.amazon.com/finspace/latest/userguide/dataset-details-page.html)
- [Creating a dataset](https://docs.aws.amazon.com/finspace/latest/userguide/creating-dataset.html)
- [Creating changesets in a dataset](https://docs.aws.amazon.com/finspace/latest/userguide/creating-changeset-in-a-dataset.html)
- [Corrections to a dataset](https://docs.aws.amazon.com/finspace/latest/userguide/corrections-to-a-dataset.html)
- [Removing a dataset](https://docs.aws.amazon.com/finspace/latest/userguide/deleting-a-dataset.html)

### [Data connectors](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-data-connector.html)

- [Tutorial: Creating a connector for GSFCD](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-creating-connector-gsm.html)
- [Connector details](https://docs.aws.amazon.com/finspace/latest/userguide/connector-summary.html)
- [Using external datasets](https://docs.aws.amazon.com/finspace/latest/userguide/dc-external-dataset.html)

### [Data views for querying data](https://docs.aws.amazon.com/finspace/latest/userguide/data-views.html)

- [Data view concepts](https://docs.aws.amazon.com/finspace/latest/userguide/data-view-concepts.html)
- [Create data view](https://docs.aws.amazon.com/finspace/latest/userguide/create-data-view.html)

### [Data views sharing](https://docs.aws.amazon.com/finspace/latest/userguide/data-sharing-lake-formation.html)

- [Tutorial: Sharing data views using AWS Lake Formation](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-data-sharing.html)

### [Prepare and analyze data](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-prepare-data.html)

### [Working with notebooks](https://docs.aws.amazon.com/finspace/latest/userguide/working-with-amazon-finSpace-notebooks.html)

- [Opening the notebook environment](https://docs.aws.amazon.com/finspace/latest/userguide/opening-the-notebook-environment.html)
- [Working in the notebook environment](https://docs.aws.amazon.com/finspace/latest/userguide/working-in-the-notebook-environment.html)
- [Access datasets from a notebook](https://docs.aws.amazon.com/finspace/latest/userguide/access-datasets-notebook.html)
- [Example notebooks](https://docs.aws.amazon.com/finspace/latest/userguide/example-notebook.html)
- [Working with Spark clusters](https://docs.aws.amazon.com/finspace/latest/userguide/working-with-Spark-clusters.html)
- [Importing library](https://docs.aws.amazon.com/finspace/latest/userguide/import-library.html)
- [Accessing Amazon S3 Bucket](https://docs.aws.amazon.com/finspace/latest/userguide/access-s3-buckets.html)

### [Spark time series analytics](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-time-series-library.html)

- [Collect time bars operations](https://docs.aws.amazon.com/finspace/latest/userguide/time-series-collect.title.html)
- [Summarize bars operations](https://docs.aws.amazon.com/finspace/latest/userguide/time-series-summarize-bars.title.html)
- [Fill and filter operations](https://docs.aws.amazon.com/finspace/latest/userguide/time-series-fill-filter.title.html)
- [Analyze operations](https://docs.aws.amazon.com/finspace/latest/userguide/time-series-analyze.title.html)
- [Using the library](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-using-the-library.title.html)


## [Administration](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-administration.html)

- [Regions and IP ranges](https://docs.aws.amazon.com/finspace/latest/userguide/regions-ip-ranges.html): AWS cloud-computing resources are housed in highly available facilities in different areas of the world (for example, North America, Europe, and Asia).
- [Supported browsers](https://docs.aws.amazon.com/finspace/latest/userguide/supported-browsers.html)


## [Security](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-security.html)

### [Identity and access management in FinSpace](https://docs.aws.amazon.com/finspace/latest/userguide/identity-management.html)

This section explains the identity management and authentication for Amazon FinSpace Managed kdb and Dataset browser.

### [Setting up SAML based single sign-on](https://docs.aws.amazon.com/finspace/latest/userguide/saml-sso.html)

- [Tutorial: Setup an Identity Provider](https://docs.aws.amazon.com/finspace/latest/userguide/setup-idp-finspace.html)
- [Tutorial: Creating an environment with Okta SSO](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-idp-okta-sso.html)
- [Tutorial: Creating an environment with IAM Identity Center](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-idp-aws-sso.html)
- [Tutorial: Creating an environment with AD FS](https://docs.aws.amazon.com/finspace/latest/userguide/tutorial-idp-ADFS-sso.html)

### [Managing user access](https://docs.aws.amazon.com/finspace/latest/userguide/managing-user-access.html)

Amazon FinSpace administrators or superusers can use the following topics to manage user access.

- [Managing user access with email and password](https://docs.aws.amazon.com/finspace/latest/userguide/managing-user-email-pwd.html)
- [Managing user access with SSO](https://docs.aws.amazon.com/finspace/latest/userguide/managing-user-sso.html)
- [Managing user permissions with permission groups](https://docs.aws.amazon.com/finspace/latest/userguide/managing-user-permissions.html)
- [Temporary credentials](https://docs.aws.amazon.com/finspace/latest/userguide/temporary-credentials.html): Amazon FinSpace has an internal application authorization model that controls access to the functions in FinSpace and the FinSpace API operations.
- [AWS managed policies](https://docs.aws.amazon.com/finspace/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for FinSpace and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/finspace/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give FinSpace access to resources in your AWS account.

### [Data protection](https://docs.aws.amazon.com/finspace/latest/userguide/data-protection.html)

The AWS shared responsibility model applies to data protection in Amazon FinSpace.

- [Data encryption in Amazon FinSpace](https://docs.aws.amazon.com/finspace/latest/userguide/data-encryption.html): Amazon FinSpace uses the following data encryption features
- [Inter-network traffic privacy in Dataset browser](https://docs.aws.amazon.com/finspace/latest/userguide/inter-network-traffic-privacy.html): Take following network considerations into account when using the Amazon FinSpace web application

### [Connecting Amazon FinSpace to your network](https://docs.aws.amazon.com/finspace/latest/userguide/cno-vpc.html)

- [Managing the VPC connection](https://docs.aws.amazon.com/finspace/latest/userguide/manage-vpc.html)
- [Validating your VPC connection](https://docs.aws.amazon.com/finspace/latest/userguide/vpc-validation.html)
- [Monitoring IP traffic](https://docs.aws.amazon.com/finspace/latest/userguide/monitoring-ip-traffic.html): You can use the transit gateway flow logs to monitor traffic coming from FinSpace.
- [Resilience](https://docs.aws.amazon.com/finspace/latest/userguide/resilience.html): The AWS global infrastructure is built around AWS Regions and Availability Zones.
- [Infrastructure security](https://docs.aws.amazon.com/finspace/latest/userguide/infrastructure-security.html): As a managed service, Amazon FinSpace is protected by AWS global network security.
- [Security best practices](https://docs.aws.amazon.com/finspace/latest/userguide/security-best-practices.html): Amazon FinSpace provides a number of security features to consider as you develop and implement your own security policies.
- [Querying AWS CloudTrail logs](https://docs.aws.amazon.com/finspace/latest/userguide/logging-cloudtrail-events.html)
- [Generating audit report](https://docs.aws.amazon.com/finspace/latest/userguide/audit-report.html)
