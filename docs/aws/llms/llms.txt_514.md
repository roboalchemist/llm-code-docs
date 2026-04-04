# Source: https://docs.aws.amazon.com/lake-formation/latest/dg/llms.txt

# AWS Lake Formation Developer Guide

> Provides a conceptual overview of AWS Lake Formation, a tutorial for setting up a data lake, and an API reference for developers.

- [Logging AWS Lake Formation API calls using AWS CloudTrail](https://docs.aws.amazon.com/lake-formation/latest/dg/logging-using-cloudtrail.html)
- [Supported Regions](https://docs.aws.amazon.com/lake-formation/latest/dg/supported-regions.html)
- [Document History](https://docs.aws.amazon.com/lake-formation/latest/dg/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/lake-formation/latest/dg/glossary.html)

## [What is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)

### [How it works](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html)

Learn how Lake Formation permissions work.

- [Metadata permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/metadata-permissions.html): Learn about how metadata access control works in AWS Lake Formation.
- [Storage access management](https://docs.aws.amazon.com/lake-formation/latest/dg/storage-permissions.html): Learn about how AWS Lake Formation provides access to Amazon S3 data.
- [Cross-account data sharing in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-data-sharing-lf.html): Learn about how AWS Lake Formation provides access to data in another account.
- [Lake Formation components](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works-components.html): Create and manage data lakes using the components available with Lake Formation, including the console, AWS CLI, and API operations.
- [Lake Formation terminology](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works-terminology.html): Learn about the some important terms that you will encounter in this guide.
- [AWS service integrations with Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/service-integrations.html): You can use Lake Formation to manage database, table, and column-level access permissions on data stored in Amazon S3.
- [Additional Lake Formation resources](https://docs.aws.amazon.com/lake-formation/latest/dg/additional-resources.html): Additional resources to help you understand and work with Lake Formation.


## [Getting started](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html)

- [Set up AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html): The following sections provide information on setting up Lake Formation for the first time.
- [Upgrading AWS Glue data permissions to the Lake Formation model](https://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html): Upgrade AWS Glue data permissions to the Lake Formation model.
- [Setting up Amazon VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/lake-formation/latest/dg/privatelink.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS Lake Formation without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [Tutorials](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-tutorials.html)

- [Creating a data lake from an AWS CloudTrail source](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-cloudtrail-tutorial.html): A step-by-step tutorial for creating and loading a data lake from an AWS CloudTrail source using Lake Formation.
- [Creating a data lake from a JDBC source](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-tutorial-jdbc.html): A step-by-step tutorial for creating and loading a data lake from a JDBC source using Lake Formation.
- [Setting up permissions for open table formats in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/otf-tutorial.html): A step-by-step tutorial for setting up Lake Formation permissions for open table formats: Iceberg, Hudi, and Delta Lake tables.
- [Managing a data lake using tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-dl-tutorial.html): A step-by-step tutorial for managing a data lake using tag-based access control in Lake Formation.
- [Securing data lakes with row-level access control](https://docs.aws.amazon.com/lake-formation/latest/dg/cbac-tutorial.html): A step-by-step tutorial for securing your data lakes using fine-grained access controls.
- [Securely share your data using Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/share-dl-tbac-tutorial.html): A step-by-step tutorial for sharing data within a data lake securely in Lake Formation.
- [Sharing Data Catalog resources with external AWS accounts using fine-grained access control](https://docs.aws.amazon.com/lake-formation/latest/dg/share-dl-fgac-tutorial.html): A step-by-step tutorial for sharing data within a data lake securely in Lake Formation by using fine-grained access control.


## [Onboarding to Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/onboarding-lf-permissions.html)

### [Overview of Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html)

There are two main types of permissions in AWS Lake Formation:

- [Methods for fine-grained access control](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-fine-grained.html): With a data lake, the goal is to have fine-grained access control to data.
- [Metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-metadata.html): For access control for Data Catalog resources, the following discussion assumes fine-grained access control with Lake Formation permissions and coarse-grained access control with IAM policies.
- [Underlying data access control](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-underlying-data.html): When an integrated AWS service requests access to data in an Amazon S3 location that is access-controlled by AWS Lake Formation, Lake Formation supplies temporary credentials to access the data.
- [Lake Formation personas and IAM permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/permissions-reference.html): Use this reference of AWS Lake Formation personas and their suggested IAM permissions.
- [Changing the default settings for your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html): Change the default settings for your data lake in Lake Formation.
- [Implicit Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/implicit-permissions.html): Manage implicit permissions for data lake administrators, database creators, table creators, and data lake users in Lake Formation.
- [Lake Formation permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html): Grant Lake Formation permissions to control access to Data Catalog resources and Amazon S3 locations.

### [Integrating IAM Identity Center](https://docs.aws.amazon.com/lake-formation/latest/dg/identity-center-integration.html)

Provides information about how to integrate AWS Lake Formation with IAM Identity Center.

- [Prerequisites for IAM Identity Center integration with Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/prerequisites-identity-center.html): Learn about the permissions required for integrating IAM Identity Center with Lake Formation.
- [Connecting Lake Formation with IAM Identity Center](https://docs.aws.amazon.com/lake-formation/latest/dg/connect-lf-identity-center.html): Learn how to connect Lake Formation with IAM Identity Center.
- [Updating IAM Identity Center integration](https://docs.aws.amazon.com/lake-formation/latest/dg/update-lf-identity-center-connection.html): Updating an existing IAM Identity Center integration with Lake Formation.
- [Deleting a Lake Formation connection with IAM Identity Center](https://docs.aws.amazon.com/lake-formation/latest/dg/delete-lf-identity-center-connection.html): Deleting an existing IAM Identity Center integration with Lake Formation.
- [Granting permissions to users and groups](https://docs.aws.amazon.com/lake-formation/latest/dg/grant-permissions-sso.html): Grant Lake Formation permissions to users and groups on Data Catalog resources.
- [Including IAM Identity Center user context in CloudTrail logs](https://docs.aws.amazon.com/lake-formation/latest/dg/identity-center-ct-logs.html): Set up required to include IAM Identity Center user context in CloudTrail logs.

### [Adding an Amazon S3 location to your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html)

Learn about registering an Amazon Simple Storage Service location with AWS Lake Formation.

### [Requirements for roles used to register locations](https://docs.aws.amazon.com/lake-formation/latest/dg/registration-role.html)

Use either the Lake Formation service-linked role or a custom role to register an Amazon S3 location.

- [Using service-linked roles](https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-roles.html): Use service-linked roles in Lake Formation to provide permissions to call other AWS services on your behalf.
- [Registering an Amazon S3 location](https://docs.aws.amazon.com/lake-formation/latest/dg/register-location.html): Register an Amazon Simple Storage Service path for management by AWS Lake Formation.
- [Registering an encrypted Amazon S3 location](https://docs.aws.amazon.com/lake-formation/latest/dg/register-encrypted.html): Register an encrypted Amazon Simple Storage Service path for management by AWS Lake Formation.
- [Registering an Amazon S3 location in another AWS account](https://docs.aws.amazon.com/lake-formation/latest/dg/register-cross-account.html): Register a location in another AWS account so that AWS Lake Formation can manage it.
- [Registering an encrypted Amazon S3 location across AWS accounts](https://docs.aws.amazon.com/lake-formation/latest/dg/register-cross-encrypted.html): Register an encrypted Amazon Simple Storage Service location when either the location or the encryption key is in another AWS account.
- [Deregistering an Amazon S3 location](https://docs.aws.amazon.com/lake-formation/latest/dg/unregister-location.html): Use the AWS management console to deregister an Amazon S3 location that is registered with Lake Formation.

### [Hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-mode.html)

Hybrid access mode provides the flexibility to selectively enable Lake Formation permissions for databases, tables, amd views in your AWS Glue Data Catalog.â¨ With the Hybrid access mode, you now have an incremental path that allows you to set Lake Formation permissions for a specific set of users without interrupting the permission policies of other existing users or workloads.

- [How hybrid access mode works](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-workflow.html): how Lake Formation authorization works in hybrid access mode.

### [Setting up hybrid access mode - common scenarios](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-setup.html)

Describes how to set up permissions in hybrid access mode.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-prerequisites.html): The following are the prerequisites for setting up hybrid access mode:
- [Converting an AWS Glue resource to a hybrid resource](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-mode-new.html): Describes the steps to convert a AWS Glue resource to a hybrid resource.
- [Converting a Lake Formation resource to a hybrid resource](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-mode-update.html): Describes how to enable hybrid access mode for Data Catalog resources registered with Lake Formation.
- [Sharing an AWS Glue resource using hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-mode-cross-account.html): Describes how to share Data Catalog resources in hybrid access mode.
- [Sharing a Lake Formation resource using hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-mode-cross-account-IAM.html): Describes how to share Data Catalog resources registered with Lake Formation in hybrid access mode.
- [Removing principals and resources from hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/delete-hybrid-access.html): Describes how to remove principals from hybrid access mode.
- [Viewing principals and resources in hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/view-hybrid-access.html): Describes how to view the principals and resources in hybrid access mode.
- [Additional resources](https://docs.aws.amazon.com/lake-formation/latest/dg/additional-resources-hybrid.html): Provides additional resources to set up hybrid access mode.

### [Creating objects in the AWS Glue Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/populating-catalog.html)

Create federated catalogs, metadata databases, tables, views, and resource links in the Data Catalog for use by AWS Lake Formation.

- [Creating a catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-catalog.html): Create a catalog in the Data Catalog to contain metadata databases and tables.
- [Creating a database](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-database.html): Create a database in the Data Catalog to contain metadata tables.

### [Creating tables](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-tables.html)

Create tables in the Data Catalog to access underlying data in the data lake and manage that data with Lake Formation permissions.

- [Creating Iceberg tables](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-iceberg-tables.html): Use the Lake Formation console, AWS CLI, or AWS API to create Apache Iceberg tables in the AWS Glue Data Catalog.
- [Optimizing Iceberg tables](https://docs.aws.amazon.com/lake-formation/latest/dg/data-compaction.html): Lake Formation supports multiple table optimization options to enhance the management and performance of Apache Iceberg tables used by the AWS analytical engines and ETL jobs.
- [Searching for tables](https://docs.aws.amazon.com/lake-formation/latest/dg/searching-for-tables.html): Use the Lake Formation console to search for tables by name, location, containing database, and more.
- [Sharing Data Catalog tables and databases across accounts](https://docs.aws.amazon.com/lake-formation/latest/dg/sharing-catalog-resources.html): Share Data Catalog databases and tables across accounts in AWS Lake Formation to enable users to run queries and jobs that can join and query tables across multiple accounts.

### [Building Data Catalog views](https://docs.aws.amazon.com/lake-formation/latest/dg/working-with-views.html)

Create views in the AWS Glue Data Catalog that can be queried from multiple engines.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/views-prereqs.html)
- [Creating views using DDL statements](https://docs.aws.amazon.com/lake-formation/latest/dg/create-views.html): You can create AWS Glue Data Catalog views using SQL editors for Athena, Amazon Redshift, and using the AWS Glue APIs/AWS CLI.

### [Creating views using AWS Glue APIs](https://docs.aws.amazon.com/lake-formation/latest/dg/views-api-usage.html)

You can use AWS Glue CreateTable, and UpdateTable APIs to create and update views in the Data Catalog.

- [Creating a connection to validate the view creation status](https://docs.aws.amazon.com/lake-formation/latest/dg/views-api-usage-connection.html): To create or update a AWS Glue Data Catalog view using the CreateTable or UpdateTable operations, you must create a new type of AWS Glue connection for validation, and provide it to the supported analytics engine.
- [Validating the view generation status](https://docs.aws.amazon.com/lake-formation/latest/dg/views-api-usage-get-table.html): When you run the CreateTable or UpdateTable operations, the Status field for the GetTable API output shows the details of the view creation status.
- [Asynchronous states and operations](https://docs.aws.amazon.com/lake-formation/latest/dg/views-api-usage-async-states.html): When you run a glue:CreateTable request, the asynchronous creation of the Data Catalog view begins.
- [View creation failure scenarios during asynchronous operations](https://docs.aws.amazon.com/lake-formation/latest/dg/views-api-usage-errors.html): The following examples are representative of the types of errors that may result from CreateTable or UpdateTable view API calls.
- [Granting permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/grant-perms-views.html): After creating views in the AWS Glue Data Catalog, you can grant data lake permissions on views to principals across AWS accounts, organizations and organizational units.
- [Materialized views](https://docs.aws.amazon.com/lake-formation/latest/dg/materialized-views.html): Create materialized views in the AWS Glue Data Catalog that store precomputed query results in Apache Iceberg format.

### [Importing data using workflows](https://docs.aws.amazon.com/lake-formation/latest/dg/workflows.html)

Configure a blueprint to create a workflow in AWS Lake Formation.

- [Blueprints and workflows](https://docs.aws.amazon.com/lake-formation/latest/dg/workflows-about.html): A workflow encapsulates a complex multi-job extract, transform, and load (ETL) activity.
- [Creating a workflow](https://docs.aws.amazon.com/lake-formation/latest/dg/workflows-creating.html): Before you start, ensure that you have granted the required data permissions and data location permissions to the role LakeFormationWorkflowRole.
- [Running a workflow](https://docs.aws.amazon.com/lake-formation/latest/dg/workflows-running.html): You can run a workflow using the Lake Formation console, the AWS Glue console, or the AWS Glue Command Line Interface (AWS CLI), or API.


## [Bringing your data into the Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/bring-your-data-overview.html)

### [Catalog federation](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation.html)

Learn about catalog federation in AWS Glue for accessing Iceberg tables, cataloged in remote catalogs and stored in Amazon S3, using AWS analytics engines.

- [Federate to Snowflake](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation-snowflake.html): Learn how to federate Data Catalog to Snowflake using OAuth2 credentials to access Snowflake Horizon and Polaris catalogs.
- [Federate to Databricks](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation-databricks.html): Learn how to federate Data Catalog to Databricks Unity Catalog using OAuth2 credentials to access Iceberg tables.

### [Bringing Amazon Redshift data into the Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-namespaces-datacatalog.html)

Learn to manage analytic data in Amazon Redshift data warehouses in the AWS Glue Data Catalog, and unify Amazon S3 data lakes and Amazon Redshift data warehouses.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/redshift-ns-prereqs.html)
- [Creating Amazon Redshift federated catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/create-ns-catalog.html): This topic describes the steps you need to follow to accept a cluster or namespace invitation, create a federated multi-level catalog, and grant permissions to other principals.
- [Viewing catalog objects](https://docs.aws.amazon.com/lake-formation/latest/dg/view-ns-catalog-resources.html): Learn to view catalog objects in the federated catalog.
- [Updating a federated catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/update-fed-catalog-steps.html): You can update a Amazon Redshift federated catalog in the Data Catalog using the Lake Formation console, the AWS CLI or the UpdateCatalog API operation.
- [Accessing a shared federated catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-resource-link.html): Create resource links in the Data Catalog to enable access to shared data in the data lake.
- [Deleting a federated catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/delete-rs-fed-catalog.html): You can delete the federated catalogs that you created in the AWS Glue Data Catalog using the glue:DeleteCatalog operation or the AWS Lake Formation console.
- [Querying federated catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/query-redshift-fed-catalog.html): After you grant permissions to other principals, they can sign in and start querying the tables in the federated catalogs by logging into the SQL tools using Amazon Redshift, Amazon EMR, Amazon Athena, and AWS Glue ETL.
- [Additional resources](https://docs.aws.amazon.com/lake-formation/latest/dg/additional-resources-byod.html): Provides additional resources to unify access to data in both data warehouses and data lakes.

### [Federating into external data sources](https://docs.aws.amazon.com/lake-formation/latest/dg/federated-catalog-data-connection.html)

Learn to connect the AWS Glue Data Catalog to external data sources using AWS Glue data source connectors.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/connect-data-source-prerequisites.html)
- [Creating a federated catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/create-fed-catalog-data-source.html): To connect the AWS Glue Data Catalog to external data sources, you need to use AWS Glue connections that enable communication with the external data sources.
- [Viewing catalog objects](https://docs.aws.amazon.com/lake-formation/latest/dg/view-fed-glue-connection-catalog.html): Learn how to view the objects in a federated catalog.
- [Deleting a federated catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/delete-glue-fed-catalog.html): You can delete the federated catalogs that you created in the AWS Glue Data Catalog using the glue:DeleteCatalog operation or the AWS Lake Formation console.
- [Querying federated catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/query-glue-fed-catalog.html): After you grant permissions to other principals, they can sign in and start querying the tables in the federated catalogs using Athena.
- [Additional resources](https://docs.aws.amazon.com/lake-formation/latest/dg/additional-resources-fed-connection.html): Provides additional resources to securely access data stored outside of Amazon S3 data lakes.

### [Creating an Amazon S3 tables catalog in the Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/create-s3-tables-catalog.html)

Learn to integrate and catalog Amazon S3 tables as AWS Glue Data Catalog objects.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/s3tables-catalog-prerequisites.html): Following are the prerequisites to enable Amazon S3 table integration with AWS Glue Data Catalog and AWS Lake Formation.
- [Enabling Amazon S3 Tables integration](https://docs.aws.amazon.com/lake-formation/latest/dg/enable-s3-tables-catalog-integration.html): Learn to integrate Amazon S3 Tables with Lake Formation and Data Catalog.
- [Creating databases and tables](https://docs.aws.amazon.com/lake-formation/latest/dg/create-databases-tables-s3-catalog.html): You can create databases to organize your Apache Iceberg tables, and tables to define the schema and location of your data in the S3 tables catalog.
- [Registering an Amazon S3 table bucket in another AWS account](https://docs.aws.amazon.com/lake-formation/latest/dg/register-cross-account-s3-table-bucket.html): Learn to establish cross-account data lake governance using AWS Lake Formation while maintaining secure access to S3 table buckets across AWS accounts.

### [Granting permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/s3-tables-grant-permissions.html)

After integrating your S3 tables with AWS Lake Formation, you can grant permissions on the S3 tables catalog and the catalog objects (table buckets, databases, tables) to other IAM roles and users in your account.

- [Accessing shared Amazon S3 tables](https://docs.aws.amazon.com/lake-formation/latest/dg/s3-tables-cross-account-sharing.html): After you grant cross-account permissions on a database or table in the S3 tables catalog, to access the resources, you need to create resource links to the shared databases and tables.
- [Creating an Amazon Redshift managed catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/create-rms-catalog.html): Learn to create an Amazon Redshift managed catalog for Amazon Redshift tables in the AWS Glue Data Catalog.

### [Managing permissions for data in an Amazon Redshift datashare](https://docs.aws.amazon.com/lake-formation/latest/dg/data-sharing-redshift.html)

Learn to securely manage data in a datashare from Amazon Redshift using AWS Lake Formation.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/redshift-ds-prereqs.html)
- [Setting up permissions for Amazon Redshift datashares](https://docs.aws.amazon.com/lake-formation/latest/dg/setup-ds-perms.html): This topic describes the steps you need to follow to accept a datashare invitation, create a federated database, and grant permissions.
- [Querying federated databases](https://docs.aws.amazon.com/lake-formation/latest/dg/qerying-fed-db.html): After you grant permissions, users can sign in and start querying the federated database using Amazon Redshift.

### [Managing permissions on datasets that use external metastores](https://docs.aws.amazon.com/lake-formation/latest/dg/data-sharing-hms.html)

Learn to connect the Data Catalog to external metastores that store metadata for your Amazon S3 data, and securely manage data access permissions using AWS Lake Formation.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/hms-prerequisites.html)
- [Connecting the Data Catalog to an external Hive metastore](https://docs.aws.amazon.com/lake-formation/latest/dg/hms-setup.html): To connect the AWS Glue Data Catalog to a Hive metastore, you need to deploy an AWS SAM application called GlueDataCatalogFederation-HiveMetastore.
- [Additional resources](https://docs.aws.amazon.com/lake-formation/latest/dg/additional-resources-hms.html): The following blog post contains detailed instructions to set up Lake Formation permissions on a Hive metastore database and tables, and query them using Athena.


## [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html)

### [Granting data location permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-location-permissions.html)

Grant data location permissions in AWS Lake Formation to enable principals to create and alter Data Catalog resources that point to designated registered Amazon S3 locations.

- [Granting data location permissions (same account)](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-location-permissions-local.html): Follow these steps to grant data location permissions to principals in your AWS account.
- [Granting data location permissions (external account)](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-location-permissions-external.html): Follow these steps to grant data location permissions to an external AWS account or organization.
- [Granting permissions on a data location shared with your account](https://docs.aws.amazon.com/lake-formation/latest/dg/regranting-locations.html): After a Data Catalog resource is shared with your AWS account, as a data lake administrator, you can grant permissions on the resource to other principals in your account.

### [Granting data permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)

Grant Data permissions to principals so that the principals can create and manage Data Catalog resources, and can access underlying data.

- [IAM permissions required to grant Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/required-permissions-for-grant.html): All principals, including the data lake administrator, need the following AWS Identity and Access Management (IAM) permissions to grant or revoke AWS Lake Formation Data Catalog permissions or data location permissions with the Lake Formation API or the AWS CLI:

### [Using the named resources method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-cat-perms-named-resource.html)

Use the named Data Catalog resource method to grant Lake Formation permissions on specific Data Catalog catalogs, databases, and tables.

- [Granting catalog permissions using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-multi-catalog-permissions.html): Use the named resource method to grant Lake Formation permissions on Data Catalog catalogs using the Lake Formation console and AWS CLI.
- [Granting database permissions using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-database-permissions.html): Use the named resource method to grant Lake Formation permissions on Data Catalog databases using the Lake Formation console and AWS CLI.
- [Granting table permissions using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-table-permissions.html): Use the named resource method to grant Lake Formation permissions on Data Catalog tables.
- [Granting permissions on views using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-view-permissions.html): The following steps explain how to grant permissions on views by using the named resource method and the Grant permissions page.

### [Tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/tag-based-access-control.html)

With LF-TBAC, LF-Tags are assigned to Data Catalog resources and granted to principals.

### [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html)

Create, maintain, and assign LF-Tags to control access to Data Catalog catalogs, databases, tables, and columns.

- [Adding LF-Tag creators](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-adding-tag-creator.html): Create, maintain, and assign LF-Tags to control access to Data Catalog objects.
- [Creating LF-Tags](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-creating-tags.html): Create LF-Tags to secure Data Catalog metadata with the Lake Formation tag-based access control method.
- [Updating LF-Tags](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-updating-tags.html): Update a LF-Tag by adding or deleting values for the key.
- [Deleting LF-Tags](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-deleting-tags.html): Delete LF-Tags that are no longer in use.
- [Listing LF-Tags](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-listing-tags.html): List LF-Tags to view the LF-Tags that you have permissions on.
- [Assigning LF-Tags to Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-assigning-tags.html): Assign LF-Tags to Data Catalog resources to control access to those resources.
- [Viewing LF-Tags assigned to a resource](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-view-resource-tags.html): You can view the LF-Tags that are assigned to a Data Catalog resource.
- [Viewing the resources that a LF-Tag is assigned to](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-view-tag-resources.html): Use the Lake Formation console to view the Data Catalog resources that a particular LF-Tag key is assigned to.

### [Managing LF-Tag expressions for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tag-expressions.html)

Create and maintain LF-Tag expressions to control access to Data Catalog resources.

- [Creating LF-Tag expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-creating-tag-expressions.html): Create LF-Tag expressions to secure Data Catalog metadata with the Lake Formation tag-based access control method.
- [Updating LF-Tag expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-updating-expressions.html): Update an LF-Tag expressions by updating the description, expression body, and permissions granted on the expression.
- [Deleting LF-Tag expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-deleting-expressions.html): Delete LF-Tag expressions that are no longer in use.
- [Listing LF-Tag expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-listing-expressions.html): List LF-Tag expressions to view the LF-Tag expressions that you have permissions on.

### [Managing LF-Tag value permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-granting-tags.html)

Grant permissions on LF-Tags so that principals can update, delete, view, and assign them to Data Catalog resources.

- [Listing LF-Tag permissions using the console](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-listing-tag-perms-console.html): You can use the Lake Formation console to view the permissions granted on LF-Tags.
- [Granting LF-Tag permissions using the console](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-granting-tags-console.html): The following steps explain how to grant permissions on LF-Tags by using the Grant LF-Tag permissions page on the Lake Formation console.
- [Managing LF-Tag permissions using the AWS CLI](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-granting-revoking-tags-cli.html): You can grant, revoke, and list permissions on LF-Tags by using the AWS Command Line Interface (AWS CLI).
- [Granting data lake permissions using the LF-TBAC method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-perms-TBAC.html): Use the Lake Formation tag-based access control (LF-TBAC) method to grant Lake Formation permissions on Data Catalog databases, tables, and columns.

### [Attribute-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/attribute-based-access-control.html)

Learn to grant fine-grained access permissions using attribute based access control.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/abac-prerequisites.html): To grant permissions using attribute-based access control (ABAC), you must complete the following prerequisites:
- [Granting permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/abac-granting-permissions.html): This topic describes the steps you need to follow to grant attribute-based access permissions on Data Catalog resources.
- [Permissions example scenario](https://docs.aws.amazon.com/lake-formation/latest/dg/security-permissions-example-scenario.html): Example of how to secure access control to data with permissions in Lake Formation.

### [Data filtering and cell-level security](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)

For data in your data lake, AWS Lake Formation supports column-level security, row-level security, and cell-level security.

- [PartiQL support in row filter expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/partiql-support.html): You can construct row filter expressions using a subset of PartiQL data types, operators, and aggregations.
- [Permissions required for querying tables with cell-level filtering](https://docs.aws.amazon.com/lake-formation/latest/dg/row-filtering-prereqs.html): The following AWS Identity and Access Management (IAM) permissions are required to run queries against tables with cell-level filtering.

### [Managing data filters](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-filters.html)

Use data filters to implement column-level, row-level, and cell-level security.

- [Creating a data filter](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-data-filters.html): You can create one or more data filters for each Data Catalog table.
- [Granting data filter permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-filter-perms.html): Grant permissions on data filters so that principals can view and apply them when granting Lake Formation permissions on tables.
- [Granting data permissions provided by data filters](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-data-perms-for-filters.html): Describes how to grant permissions to principals to access the data that data filters provide.
- [Viewing data filters](https://docs.aws.amazon.com/lake-formation/latest/dg/view-data-filters.html): You can use the Lake Formation console, AWS CLI, or the Lake Formation API to view data filters.
- [Listing data filter permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/listing-filter-perms.html): You can use the Lake Formation console to view the permissions granted on data filters.
- [Viewing Database and Table Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/viewing-permissions.html): View the Lake Formation permissions granted on a Data Catalog database or table.
- [Revoking permissions using the console](https://docs.aws.amazon.com/lake-formation/latest/dg/revoking-permssions-console-all.html): Use the Lake Formation console to revoke Data Catalog permissions, policy tag permissions, data filter permissions, and location permissions.

### [Cross-account data sharing](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html)

Learn about cross-account data sharing in Lake Formation.

- [Prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-prereqs.html): Before your AWS account can share Data Catalog resources (catalogs, databases and tables) with another account or principals in another account, and before you can access the resources shared with your account, the following prerequisites must be met.
- [Updating cross-account data sharing version settings](https://docs.aws.amazon.com/lake-formation/latest/dg/optimize-ram.html): From time to time, AWS Lake Formation updates the cross-account data sharing settings to distinguish the changes made to the AWS RAM usage and to support updates made to the cross-account data sharing feature.

### [Sharing Data Catalog tables and databases across AWS accounts or IAM principals from external accounts](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-data-share-steps.html)

This section includes instructions on how to grant cross-account permissions on Data Catalog resources to an external AWS account, IAM principal, AWS organization, or organizational unit.

- [Data sharing using tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-TBAC.html): AWS Lake Formation tag-based access control (LF-TBAC) is an authorization strategy that defines permissions based on attributes.
- [Cross-account data sharing using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-named-resource.html): You can grant permissions to directly to principals in the another AWS account, or to external AWS accounts or AWS Organizations.
- [Granting permissions on a database or table shared with your account](https://docs.aws.amazon.com/lake-formation/latest/dg/regranting-shared-resources.html): As a data lake administrator, you can grant permissions on Data Catalog resources shared with your AWS account to other principals in your account.
- [Granting resource link permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-link-permissions.html): Follow these steps to grant AWS Lake Formation permissions on one or more resource links to a principal in your AWS account.
- [Accessing the underlying data of a shared table](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-read-data.html): Assume that AWS account A shares a Data Catalog table with account Bâfor example, by granting SELECT with the grant option on the table to account B.
- [Cross-account CloudTrail logging](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-logging.html): Lake Formation provides a centralized audit trail of all cross-account access to data in your data lake.
- [Managing cross-account permissions using both AWS Glue and Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-cross-account.html): It's possible to grant cross-account access to Data Catalog resources and underlying data by using either AWS Glue or AWS Lake Formation.
- [Viewing all cross-account grants using the GetResourceShares API operation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-getresourcepolicies.html): If your enterprise grants cross-account permissions using both an AWS Glue Data Catalog resource policy and Lake Formation grants, the only way to view all cross-account grants in one place is to use the glue:GetResourceShares API operation.

### [Accessing and viewing shared Data Catalog tables and databases](https://docs.aws.amazon.com/lake-formation/latest/dg/viewing-shared-resources.html)

View shared tables or databases using the AWS Lake Formation console or the AWS Resource Access Manager console.

- [Accepting an AWS RAM resource share invitation](https://docs.aws.amazon.com/lake-formation/latest/dg/accepting-ram-invite.html): If a Data Catalog resource is shared with your AWS account and your account is not in the same AWS organization as the sharing account, you do not have access to the shared resource until you accept a resource share invitation from AWS Resource Access Manager (AWS RAM).
- [Viewing shared Data Catalog tables and databases](https://docs.aws.amazon.com/lake-formation/latest/dg/viewing-available-shared-resources.html): You can view resources that are shared with your account by using the Lake Formation console or AWS CLI.

### [Creating resource links](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-resource-links.html)

Create resource links in the Data Catalog to enable cross-account access to data in the data lake.

- [How resource links work](https://docs.aws.amazon.com/lake-formation/latest/dg/resource-links-about.html): Learn about resource links in AWS Lake Formation.
- [Creating a resource link to a shared table](https://docs.aws.amazon.com/lake-formation/latest/dg/create-resource-link-table.html): Create a resource link in AWS Lake Formation to assign a new name to a shared table, or to be able to access a shared table from any AWS Region in cross-account queries with integrated services such as Amazon Athena.
- [Creating a resource link to a shared database](https://docs.aws.amazon.com/lake-formation/latest/dg/create-resource-link-database.html): Create a resource link to a shared database in AWS Lake Formation to view the shared Data Catalog tables in the database and reference the database in extract, transform, and load (ETL) scripts.
- [Resource link handling in AWS Glue APIs](https://docs.aws.amazon.com/lake-formation/latest/dg/resource-links-glue-apis.html): Learn how the various AWS Glue APIs handle resource links to databases and tables.

### [Accessing tables across Regions](https://docs.aws.amazon.com/lake-formation/latest/dg/data-access-across-region.html)

Lake Formation supports querying Data Catalog tables across AWS Regions.

- [Setting up cross-Region table access](https://docs.aws.amazon.com/lake-formation/latest/dg/setup-cross-region-access.html): To access data from a different Region, you need to first set up the Data Catalog databases and tables in the Region where you register your Amazon S3 data location.


## [Security](https://docs.aws.amazon.com/lake-formation/latest/dg/security.html)

### [Data Protection](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-protection.html)

Learn how AWS Lake Formation protects your data.

- [Encryption at Rest](https://docs.aws.amazon.com/lake-formation/latest/dg/encryption-at-rest.html): Lake Formation supports encrypted data in your Amazon S3 data lake and in the AWS Glue Data Catalog.
- [Infrastructure Security](https://docs.aws.amazon.com/lake-formation/latest/dg/infrastructure-security.html): Learn how AWS Lake Formation isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Security event logging in AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/security-event-logging.html): Learn about event logging in Lake Formation


## [Integrating with Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/Integrating-with-LakeFormation.html)

### [Using Lake Formation application integration](https://docs.aws.amazon.com/lake-formation/latest/dg/using-cred-vending.html)

Lake Formation allows third-party services to integrate with Lake Formation and get temporary access to Amazon S3 data on behalf of their users by using GetTemporaryGlueTableCredentials and GetTemporaryGluePartitionCredentials operations.

- [How Lake Formation application integration works](https://docs.aws.amazon.com/lake-formation/latest/dg/how-vending-works.html): This section describes how to use application integration API operations to integrate a third-party application (query engine) with Lake Formation.
- [Roles and responsibilities in Lake Formation application integration](https://docs.aws.amazon.com/lake-formation/latest/dg/roles-and-responsibilities.html): Learn about the role and responsibilities for the Lake Formation application integration process.
- [Lake Formation workflow for application integration API operations](https://docs.aws.amazon.com/lake-formation/latest/dg/api-overview.html): The following is the work flow for application integration API operations:
- [Registering a third-party query engine](https://docs.aws.amazon.com/lake-formation/latest/dg/register-query-engine.html): Before a third-party query engine can use the application integration API operations, you need to explicitly enable permissions for the query engine to call the API operations on your behalf.
- [Enabling permissions for a third-party query engine to call application integration API operations](https://docs.aws.amazon.com/lake-formation/latest/dg/permitting-third-party-call.html): Follow these steps to allow a third-party query engine to call application integration API operations through the AWS Lake Formation console, the AWS CLI or API/SDK.
- [Application integration for full table access](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html): How to integrate applications for full table access.


## [Working with other AWS services](https://docs.aws.amazon.com/lake-formation/latest/dg/working-with-services.html)

- [Amazon Athena](https://docs.aws.amazon.com/lake-formation/latest/dg/athena-lf.html): Amazon Athena is a server-less query service that helps you analyze structured, semi-structured, and unstructured data stored in Amazon S3.
- [Amazon Redshift Spectrum](https://docs.aws.amazon.com/lake-formation/latest/dg/RSPC-lf.html): Amazon Redshift Spectrum lets you to query and retrieve data in Amazon S3 data lakes without loading data into Amazon Redshift cluster nodes.
- [AWS Glue](https://docs.aws.amazon.com/lake-formation/latest/dg/glue-features-lf.html): Data engineers and DevOps professionals use AWS Glue with Extract, Transform and Load (ETL) with Apache Spark to perform transformations on their data sets in Amazon S3 and load the transformed data into data lakes and data warehouses for analytics, machine learning, and application development.
- [Amazon EMR](https://docs.aws.amazon.com/lake-formation/latest/dg/emr-integ-lf.html): Amazon EMR is a flexible AWS managed cluster platform on which you can run any custom code on supported big data frameworks like Hadoop Map-Reduce, Spark, Hive, Presto, etc.
- [Quick](https://docs.aws.amazon.com/lake-formation/latest/dg/qs-integ-lf.html): Quick supports exploring datasets managed by Lake Formation permissions in Amazon S3 using Athena.
- [AWS CloudTrail Lake](https://docs.aws.amazon.com/lake-formation/latest/dg/cloudtrail-lake-integ-lf.html): AWS CloudTrail Lake supports exploring event data stores using Amazon Athena with fine-grained permissions in AWS Lake Formation.


## [Lake Formation best practices, considerations, and limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-limitations.html)

- [Cross-account data sharing best practices and considerations](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-notes.html): Lake Formation cross-account capabilities allow users to securely share distributed data lakes across multiple AWS accounts, AWS organizations or directly with IAM principals in another account providing fine-grained access to the Data Catalog metadata and underlying data.
- [Service-linked role limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-role-limitations.html): A service-linked role is a special type of IAM role that's linked directly to AWS Lake Formation.
- [Cross-Region data access limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/x-region-considerations.html): Lake Formation supports querying Data Catalog tables across AWS Regions.
- [Data Catalog views considerations and limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/views-notes.html): The following considerations and limitations apply to Data Catalog views.
- [Data filtering limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering-notes.html): When you grant Lake Formation permissions on a Data Catalog table, you can include data filtering specifications to restrict access to certain data in query results and engines integrated with Lake Formation.
- [Hybrid access mode considerations and limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/notes-hybrid.html): Hybrid access mode provides the flexibility to selectively enable Lake Formation permissions for databases and tables in your AWS Glue Data Catalog.â¨ With the Hybrid access mode, you now have an incremental path that allows you to set Lake Formation permissions for a specific set of users without interrupting the permission policies of other existing users or workloads.
- [Limitations for bringing Amazon Redshift data warehouse data into the AWS Glue Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/notes-ns-catalog.html): You can catalog, and manage access to analytic data in Amazon Redshift data warehouses using the AWS Glue Data Catalog.
- [S3 Tables catalog integration limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/notes-s3-catalog.html): Amazon S3 Tables integrates with AWS Glue Data Catalog (Data Catalog) and registers the catalog as a Lake Formation data location.
- [Hive metadata store data sharing considerations and limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/notes-hms.html): With AWS Glue Data Catalog metadata federation (Data Catalog federation), you can connect the Data Catalog to external metastores that store metadata for your Amazon S3 data, and securely manage data access permissions using AWS Lake Formation.
- [Amazon Redshift data sharing limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/notes-rs-datashare.html): AWS Lake Formation allows you to securely manage data in a datashare from Amazon Redshift.
- [IAM Identity Center integration limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/identity-center-lf-notes.html): With AWS IAM Identity Center, you can connect to identity providers (IdPs) and centrally manage access for users and groups across AWS analytics services.
- [Lake Formation tag-based access control best practices and considerations](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-tag-considerations.html): You can create, maintain, and assign LF-Tags to control access to Data Catalog databases, tables, and columns.
- [Attribute-based access control considerations, limitations, and supported regions](https://docs.aws.amazon.com/lake-formation/latest/dg/abac-considerations.html): The following considerations and limitations apply to Attribute based access control (ABAC).


## [Troubleshooting Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/troubleshooting.html)

- [Known issues for AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/limitations.html): Review these known issues for AWS Lake Formation.
- [Updated error message](https://docs.aws.amazon.com/lake-formation/latest/dg/error-message-update.html): AWS Lake Formation has updated the resource specific exceptions to general EntityNotFound error message for the following API operations to meet security and compliance objectives.


## [Lake Formation API](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api.html)

- [Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-permissions.html): This section describes operations and data types having to do with granting and revoking permissions in AWS Lake Formation.
- [Data Lake Settings](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-settings.html): This section describes data types and operations for managing Data Lake settings.
- [IAM Identity Center integration](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-Identity-center-integ.html): This section describes data types and operations for managing Lake Formation integration with IAM Identity Center.
- [Hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-hybrid-access-mode.html): This section describes operations and data types required to set up hybrid access mode in AWS Lake Formation.
- [Credential vending](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html): This section describes the credential vending API in the AWS Lake Formation service.
- [Tagging](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-tagging-api.html): This section describes the tagging API in the AWS Lake Formation service.
- [Data filter APIs](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-data-filter.html): This section describes Data Filter APIs.
- [Common data types](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html): This section describes miscellaneous common data types.
