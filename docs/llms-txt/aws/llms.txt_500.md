# Source: https://docs.aws.amazon.com/kendra/latest/dg/llms.txt

# Amazon Kendra Developer Guide

> Provides a conceptual overview of Amazon Kendra. Learn about Amazon Kendra features and get started indexing your documents using the console, CLI, and API.

- [What is Amazon Kendra?](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html)
- [IAM access roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html)
- [Adjusting capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html)
- [Enriching your documents during ingestion](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html)
- [Tuning search relevance](https://docs.aws.amazon.com/kendra/latest/dg/tuning.html)
- [Gaining insights with search analytics](https://docs.aws.amazon.com/kendra/latest/dg/search-analytics.html)
- [Quotas](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html)
- [API reference](https://docs.aws.amazon.com/kendra/latest/dg/api-ref.html)
- [Document history](https://docs.aws.amazon.com/kendra/latest/dg/doc-history.html)

## [How Amazon Kendra works](https://docs.aws.amazon.com/kendra/latest/dg/how-it-works.html)

### [Indexes in Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index.html)

An index holds the contents of your documents and is structured in a way to make the documents searchable.

- [Index types in Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-types.html): Amazon Kendra has three index types: GenAI Enterprise Edition index, Enterprise Edition index, and Developer Edition index.
- [Adding documents to an index in Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-adding-docs.html): The way you add documents to an index depends on how you store your documents.
- [Using Amazon Kendra reserved or common document fields](https://docs.aws.amazon.com/kendra/latest/dg/index-reserved-fields-hiw.html): With the UpdateIndex API operation, you can create reserved or common fields.
- [Retrieving responses from indexes in Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/index-searching.html): After you create an index, you can start searching your documents.
- [Documents](https://docs.aws.amazon.com/kendra/latest/dg/hiw-documents.html): This section explains how Amazon Kendra indexes the many document formats it supports and the different fields/attributes of documents.
- [Data sources](https://docs.aws.amazon.com/kendra/latest/dg/hiw-data-source.html): A data source is a data repository or location that Amazon Kendra connects to and indexes your documents or content.
- [Queries](https://docs.aws.amazon.com/kendra/latest/dg/hiw-query.html): To get answers, users query an index.
- [Tags](https://docs.aws.amazon.com/kendra/latest/dg/tagging.html): Manage your indices, data sources, and FAQs by assigning tags or labels.


## [Setting up Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/setup.html)

- [Setting up the AWS CLI](https://docs.aws.amazon.com/kendra/latest/dg/aws-kendra-set-up-aws-cli.html): Set up the AWS CLI to manage Amazon Kendra.
- [Setting up the AWS SDKs](https://docs.aws.amazon.com/kendra/latest/dg/aws-kendra-set-up-sdks.html): Download and install the AWS SDKs that you want to use.


## [Deploying Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/deploying.html)

- [Deploying a search application with no code](https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html): How build and deploy a fully functional search application in a few clicks using Amazon Kendra Experience Builder.


## [Getting started](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/kendra/latest/dg/gs-prerequisites.html): The following steps are prequisites for the getting started exercises.
- [Getting started with the Amazon Kendra console](https://docs.aws.amazon.com/kendra/latest/dg/gs-console.html): The following procedures show how to create and test an Amazon Kendra index by using the AWS console.
- [Getting started (AWS CLI)](https://docs.aws.amazon.com/kendra/latest/dg/gs-cli.html): The following procedure shows how to create an Amazon Kendra index using the AWS CLI.
- [Getting started (SDK for Python (Boto3))](https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html): The following program is an example of using Amazon Kendra in a Python program.
- [Getting started (SDK for Java)](https://docs.aws.amazon.com/kendra/latest/dg/gs-java.html): The following program is an example of using Amazon Kendra in a Java program.
- [Getting started with S3 (console)](https://docs.aws.amazon.com/kendra/latest/dg/getting-started-s3.html): Getting started with an Amazon S3 data source for Amazon Kendra.
- [Getting started with MySQL (console)](https://docs.aws.amazon.com/kendra/latest/dg/getting-started-mysql.html): Getting started with a MySQL database data source for Amazon Kendra.

### [Getting started with an IAM Identity Center identity source (console)](https://docs.aws.amazon.com/kendra/latest/dg/getting-started-aws-sso.html)

Getting started with an IAM Identity Center identity source (Console) for Amazon Kendra.

- [Changing your IAM Identity Center identity source](https://docs.aws.amazon.com/kendra/latest/dg/changing-aws-sso-source.html)


## [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html)

- [Adding documents directly to an index with batch upload](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-documents.html): You can add documents directly to an index using the BatchPutDocument API.
- [Adding frequently asked questions (FAQs) to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html)
- [Creating custom document fields](https://docs.aws.amazon.com/kendra/latest/dg/custom-attributes.html)

### [Controlling user access to documents with tokens](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control.html)

How to set up token-based user access control in Amazon Kendra.

- [Using OpenID](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control-tokens-openid.html): Hoow to use OpenID for access control when you create an Amazon Kendra index.
- [Using a JSON Web Token (JWT) with a shared secret](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control-tokens-jwtshared.html): How to use JWT with a shared secret for access control when you create an Amazon Kendra index.
- [Using a JSON Web Token (JWT) with a public key](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control-tokens-jwtpublic.html): How to use JWT with a public key for access control when you create an Amazon Kendra index.
- [Using JSON](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control-tokens-json.html): How to use JSON for access control when you create an Amazon Kendra index.


## [Creating a data source connector](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html)

### [Data source connectors](https://docs.aws.amazon.com/kendra/latest/dg/data-sources.html)

This section shows you how to connect Amazon Kendra to supported databases and data source repositories using Amazon Kendra in the AWS Management Console and the Amazon Kendra APIs.

- [Data source template schemas](https://docs.aws.amazon.com/kendra/latest/dg/ds-schemas.html): The following are template schemas for data sources where templates are supported.
- [Adobe Experience Manager](https://docs.aws.amazon.com/kendra/latest/dg/data-source-aem.html): How to use an Adobe Experience Manager data source connector in Amazon Kendra to index your documents.
- [Alfresco](https://docs.aws.amazon.com/kendra/latest/dg/data-source-alfresco.html): How to use an Alfresco data source connector in Amazon Kendra to index your documents.
- [Aurora (MySQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-aurora-mysql.html): How to use a Aurora (MySQL) data source connector in Amazon Kendra to index your documents.
- [Aurora (PostgreSQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-aurora-postgresql.html): How to use a Aurora (PostgreSQL) data source connector in Amazon Kendra to index your documents.
- [Amazon FSx (Windows)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-fsx.html): How to use an Amazon FSx (Windows) data source connector in Amazon Kendra to index your documents.
- [Amazon FSx (NetApp ONTAP)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-fsx-ontap.html): How to use an Amazon FSx (NetApp ONTAP) data source connector in Amazon Kendra to index your documents.
- [Amazon RDS/Aurora](https://docs.aws.amazon.com/kendra/latest/dg/data-source-database.html): How to use a database data source connector in Amazon Kendra to index your documents.
- [Amazon RDS (Microsoft SQL Server)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-ms-sql-server.html): How to use a Amazon RDS (Microsoft SQL Server) data source connector in Amazon Kendra to index your documents.
- [Amazon RDS (MySQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-mysql.html): How to use a Amazon RDS (MySQL) data source connector in Amazon Kendra to index your documents.
- [Amazon RDS (Oracle)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-oracle.html): How to use a Amazon RDS (Oracle) data source connector in Amazon Kendra to index your documents.
- [Amazon RDS (PostgreSQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-postgresql.html): How to use a Amazon RDS (PostgreSQL) data source connector in Amazon Kendra to index your documents.

### [Amazon S3](https://docs.aws.amazon.com/kendra/latest/dg/data-source-s3.html)

How to use an Amazon S3 data source connector in Amazon Kendra to index your documents.

- [Creating an Amazon S3 data source](https://docs.aws.amazon.com/kendra/latest/dg/create-ds-s3.html): The following examples demonstrate creating an Amazon S3 data source.
- [Amazon S3 document metadata](https://docs.aws.amazon.com/kendra/latest/dg/s3-metadata.html): You can add metadata, additional information about a document, to documents in an Amazon S3 bucket using a metadata file.
- [Access control for Amazon S3 data sources](https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html): You can control access to documents in an Amazon S3 data source using a configuration file.
- [Using Amazon VPC with Amazon S3](https://docs.aws.amazon.com/kendra/latest/dg/s3-vpc-example-1.html): This topic provides a step-by-step example that shows how to connect to an Amazon S3 bucket by using an Amazon S3 connector through Amazon VPC.

### [Amazon Kendra Web Crawler](https://docs.aws.amazon.com/kendra/latest/dg/data-source-web-crawler.html)

How to use a web crawler data source connector in Amazon Kendra to index your documents.

- [Amazon Kendra Web Crawler connector v1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-web-crawler.html): You can use Amazon Kendra Web Crawler to crawl and index web pages.
- [Amazon Kendra Web Crawler connector v2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-web-crawler.html): You can use Amazon Kendra Web Crawler to crawl and index web pages.
- [Configuring the robots.txt file for Amazon Kendra Web Crawler](https://docs.aws.amazon.com/kendra/latest/dg/stop-web-crawler.html): How to configure a robots.txt file for Amazon Kendra Web Crawler.
- [Box](https://docs.aws.amazon.com/kendra/latest/dg/data-source-box.html): How to use a Box data source connector in Amazon Kendra to index your documents.

### [Confluence](https://docs.aws.amazon.com/kendra/latest/dg/data-source-confluence.html)

How to use a Confluence data source connector in Amazon Kendra to index your documents.

- [Confluence connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-confluence.html): Confluence is a collaborative work-management tool designed for sharing, storing, and working on project planning, software development, and product management.
- [Confluence connector V1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-confluence.html): Confluence is a collaborative work-management tool designed for sharing, storing, and working on project planning, software development, and product management.

### [Custom data source connector](https://docs.aws.amazon.com/kendra/latest/dg/data-source-custom.html)

How to use your own custom data source connector in Amazon Kendra to index your documents.

- [Custom data source (Java)](https://docs.aws.amazon.com/kendra/latest/dg/custom-java-sample.html): The following code provides a sample implementation of a custom data source using Java.
- [Dropbox](https://docs.aws.amazon.com/kendra/latest/dg/data-source-dropbox.html): How to use a Dropbox data source connector in Amazon Kendra to index your documents.
- [Drupal](https://docs.aws.amazon.com/kendra/latest/dg/data-source-drupal.html): How to use a Drupal data source connector in Amazon Kendra to index your documents.
- [GitHub](https://docs.aws.amazon.com/kendra/latest/dg/data-source-github.html): How to use a GitHub data source connector in Amazon Kendra to index your documents.
- [Gmail](https://docs.aws.amazon.com/kendra/latest/dg/data-source-gmail.html): How to use a Gmail data source connector in Amazon Kendra to index your documents.

### [Google Drive](https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html)

How to use a Google Drive data source connector in Amazon Kendra to index your documents.

- [Google Drive connector V1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-google-drive.html): Google Drive is a cloud-based file storage service.
- [Google Drive connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-google-drive.html): Google Drive is a cloud-based file storage service.
- [IBM DB2](https://docs.aws.amazon.com/kendra/latest/dg/data-source-ibm-db2.html): How to use a IBM DB2 data source connector in Amazon Kendra to index your documents.
- [Jira](https://docs.aws.amazon.com/kendra/latest/dg/data-source-jira.html): How to use a Jira data source connector in Amazon Kendra to index your documents.
- [Microsoft Exchange](https://docs.aws.amazon.com/kendra/latest/dg/data-source-exchange.html): How to use a Microsoft Exchange data source connector in Amazon Kendra to index your documents.

### [Microsoft OneDrive](https://docs.aws.amazon.com/kendra/latest/dg/data-source-onedrive.html)

How to use a Microsoft OneDrive data source connector in Amazon Kendra to index your documents.

- [Microsoft OneDrive connector V1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-onedrive.html): Microsoft OneDrive is a cloud-based storage service that you can use to store, share, and host your content.
- [Microsoft OneDrive connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-onedrive.html): How to use a Microsoft OneDrive data source connector in Amazon Kendra to index your documents.

### [Microsoft SharePoint](https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html)

How to use a SharePoint data source connector in Amazon Kendra to index your documents.

- [SharePoint connector V1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-sharepoint.html): SharePoint is a collaborative website building service that you can use to customize web content and create pages, sites, document libraries, and lists.
- [SharePoint connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-sharepoint.html): SharePoint is a collaborative website building service that you can use to customize web content and create pages, sites, document libraries, and lists.
- [Microsoft SQL Server](https://docs.aws.amazon.com/kendra/latest/dg/data-source-ms-sql-server.html): How to use a Microsoft SQL Server data source connector in Amazon Kendra to index your documents.
- [Microsoft Teams](https://docs.aws.amazon.com/kendra/latest/dg/data-source-teams.html): How to use a Microsoft Teams data source connector in Amazon Kendra to index your documents.
- [Microsoft Yammer](https://docs.aws.amazon.com/kendra/latest/dg/data-source-yammer.html): How to use a Microsoft Yammer data source connector in Amazon Kendra to index your documents.
- [MySQL](https://docs.aws.amazon.com/kendra/latest/dg/data-source-mysql.html): How to use a MySQL data source connector in Amazon Kendra to index your documents.
- [Oracle Database](https://docs.aws.amazon.com/kendra/latest/dg/data-source-oracle-database.html): How to use a Oracle Database data source connector in Amazon Kendra to index your documents.
- [PostgreSQL](https://docs.aws.amazon.com/kendra/latest/dg/data-source-postgresql.html): How to use a PostgreSQL data source connector in Amazon Kendra to index your documents.
- [Quip](https://docs.aws.amazon.com/kendra/latest/dg/data-source-quip.html): How to use a Quip data source connector in Amazon Kendra to index your documents.

### [Salesforce](https://docs.aws.amazon.com/kendra/latest/dg/data-source-salesforce.html)

How to use a Salesforce data source connector in Amazon Kendra to index your documents.

- [Salesforce connector V1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-salesforce.html): Salesforce is a customer relationship management (CRM) tool for managing support, sales, and marketing teams.
- [Salesforce connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-salesforce.html): Salesforce is a customer relationship management (CRM) tool for managing support, sales, and marketing teams.

### [ServiceNow](https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html)

How to use a ServiceNow data source connector in Amazon Kendra to index your documents.

- [ServiceNow connector V1.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v1-servicenow.html): ServiceNow provides a cloud-based service management system to create and manage organization-level workflows, such as IT services, ticketing systems, and support.
- [ServiceNow connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-servicenow.html): ServiceNow provides a cloud-based service management system to create and manage organization-level workflows, such as IT services, ticketing systems, and support.
- [Specifying documents with a query](https://docs.aws.amazon.com/kendra/latest/dg/servicenow-query.html): Learn how to create a ServiceNow query to select documents for Amazon Kendra to index.
- [Slack](https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html): How to use a Slack data source connector in Amazon Kendra to index your documents.
- [Zendesk](https://docs.aws.amazon.com/kendra/latest/dg/data-source-zendesk.html): How to use a Zendesk data source connector in Amazon Kendra to index your documents.
- [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html): Amazon Kendra data source connectors can map document or content fields from your data source to fields in your Amazon Kendra index.
- [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html): You can index documents in multiple languages.

### [Configuring Amazon Kendra to use an Amazon VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html)

Amazon Kendra can connect to a virtual private cloud (VPC) that you created with Amazon Virtual Private Cloud to index content stored in data sources running in your private cloud.

- [Configuring Amazon VPC](https://docs.aws.amazon.com/kendra/latest/dg/connector-vpc-steps.html): To configure Amazon VPC for use with your Amazon Kendra connectors, take the following steps.
- [Connecting to Amazon VPC](https://docs.aws.amazon.com/kendra/latest/dg/connector-vpc-setup.html): When you add a new data source in Amazon Kendra, you can use the Amazon VPC feature if the selected data source connector supports this feature.
- [Connecting to a database](https://docs.aws.amazon.com/kendra/latest/dg/vpc-example.html): The following example shows how to connect a MySQL database running in a virtual private cloud (VPC) .
- [Troubleshooting VPC connection issues](https://docs.aws.amazon.com/kendra/latest/dg/vpc-connector-troubleshoot.html): If you encounter any issues with your virtual private cloud (VPC) connection, check that your IAM permissions, security group settings, and the subnet's route tables are configured correctly.


## [Deleting an index, data source, or batch uploaded documents](https://docs.aws.amazon.com/kendra/latest/dg/delete-index-datasource-batchdocs.html)

- [Deleting an index](https://docs.aws.amazon.com/kendra/latest/dg/delete-index.html): How to delete an Amazon Kendra index.
- [Deleting a data source](https://docs.aws.amazon.com/kendra/latest/dg/delete-data-source.html): How to delete a data source from an Amazon Kendra index.
- [Deleting batch uploaded documents](https://docs.aws.amazon.com/kendra/latest/dg/delete-batch-documents.html): How to delete documents you batch uploaded to an Amazon Kendra index.


## [Searching an index](https://docs.aws.amazon.com/kendra/latest/dg/searching.html)

- [Querying an index](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html): How to query an index in Amazon Kendra.
- [Retrieving passages](https://docs.aws.amazon.com/kendra/latest/dg/searching-retrieve.html): How to use Amazon Kendra retriever for retrieval augmented generation (RAG) systems.
- [Browsing an index](https://docs.aws.amazon.com/kendra/latest/dg/browsing.html): How to browse your indexed documents in Amazon Kendra.
- [Featuring search results](https://docs.aws.amazon.com/kendra/latest/dg/featured-results.html): How to feature search results for certain queries in Amazon Kendra.
- [Tabular search for HTML](https://docs.aws.amazon.com/kendra/latest/dg/searching-tables.html): How to query an index with tables in Amazon Kendra.
- [Query suggestions](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html): How to suggest queries in Amazon Kendra and autocomplete the search.
- [Query spell checker](https://docs.aws.amazon.com/kendra/latest/dg/query-spell-check.html): How to use query spell corrections in Amazon Kendra.
- [Filtering and facet search](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html): How to filter and facet search in Amazon Kendra.
- [Filtering on user context](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html): How to filter search results in Amazon Kendra based on user or their group access to documents.
- [Query responses and response types](https://docs.aws.amazon.com/kendra/latest/dg/query-responses-types.html): Search results in Amazon Kendra.
- [Tuning and sorting responses](https://docs.aws.amazon.com/kendra/latest/dg/tuning-sorting-responses.html): Relevance tuning and sorting search results in Amazon Kendra.
- [Collapsing/expanding query results](https://docs.aws.amazon.com/kendra/latest/dg/expand-collapse-query-results.html): Collapsing and expanding query resuls in Amazon Kendra.


## [Submitting feedback for incremental learning](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html)

- [Using the Amazon Kendra JavaScript library to submit feedback](https://docs.aws.amazon.com/kendra/latest/dg/feedback-javascript.html): Amazon Kendra provides a JavaScript library that you can use to add click feedback to your search results page.
- [Using the Amazon Kendra API to submit feedback](https://docs.aws.amazon.com/kendra/latest/dg/feedback-api.html): To use the Amazon Kendra API to submit query feedback, use the SubmitFeedback API.


## [Adding custom synonyms to an index](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms.html)

- [Creating a thesaurus file](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-creating-thesaurus-file.html): Learn how to create a thesaurus file containing synonyms.
- [Adding a thesaurus to an index](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-adding-thesaurus-file.html): Learn how to add a thesaurus containing synonyms to an index.
- [Updating a thesaurus](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-update.html): Learn how to edit thesaurus details and reload the thesaurus file.
- [Deleting a thesaurus](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-delete.html): Learn how to delete a thesaurus.
- [Highlights in search results](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-enabling-synonyms-in-results.html): Amazon Kendra's highlights in the search results.


## [Tutorial: Building an intelligent search solution](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata.html)

- [Step 1: Adding documents](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata-add-documents.html): Add documents to Amazon S3 for this tutorial.
- [Step 2: Detecting entities](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata-entities-analysis.html): Run an entities analysis job on Amazon Comprehend for this tutorial.
- [Step 3: Formatting the metadata](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata-format-output.html): Format the Amazon Comprehend entities analysis output as Amazon Kendra metadata for this tutorial.
- [Step 4: Creating an index and ingesting the metadata](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata-create-index-ingest.html): Creating an Amazon Kendra index and ingesting the metadata for this tutorial.
- [Step 5: Querying the index](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata-query-kendra.html): Querying the Amazon Kendra index with example queries for this tutorial.
- [Step 6: Cleaning up](https://docs.aws.amazon.com/kendra/latest/dg/tutorial-search-metadata-cleanup.html): Cleanup steps for this tutorial.


## [Monitoring and logging](https://docs.aws.amazon.com/kendra/latest/dg/monitoring.html)

- [Monitoring indexes](https://docs.aws.amazon.com/kendra/latest/dg/monitoring-runsync.html): Use the Amazon Kendra console to monitor the state of indexes and data sources.
- [Monitoring Amazon Kendra API calls with CloudTrail](https://docs.aws.amazon.com/kendra/latest/dg/cloudtrail.html): Amazon Kendra is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Kendra.
- [Monitoring Amazon Kendra Intelligent Ranking API calls with CloudTrail](https://docs.aws.amazon.com/kendra/latest/dg/cloudtrail-intelligent-ranking.html): Amazon Kendra Intelligent Ranking is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Kendra Intelligent Ranking.
- [Monitoring Amazon Kendra with CloudWatch](https://docs.aws.amazon.com/kendra/latest/dg/cloudwatch-metrics.html): To track the health of your indexes, use Amazon CloudWatch.
- [Monitoring Amazon Kendra with CloudWatch Logs](https://docs.aws.amazon.com/kendra/latest/dg/cloudwatch-logs.html): Amazon Kendra uses Amazon CloudWatch Logs to give you insight into the operation of your data sources.


## [Security](https://docs.aws.amazon.com/kendra/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/kendra/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Kendra.

- [Encryption at rest](https://docs.aws.amazon.com/kendra/latest/dg/encryption-at-rest.html): Amazon Kendra encrypts your data at rest with your choice of an encryption key.
- [Encryption in transit](https://docs.aws.amazon.com/kendra/latest/dg/encryption-in-transit.html): Amazon Kendra uses the HTTPS protocol to communicate with your client application.
- [Key management](https://docs.aws.amazon.com/kendra/latest/dg/key-management.html): Amazon Kendra encrypts the contents of your index using one of three types of keys.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/kendra/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Kendra or Amazon Kendra Intelligent Ranking without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.

### [Identity and access management](https://docs.aws.amazon.com/kendra/latest/dg/security-iam.html)

How to authenticate requests and manage access your Amazon Kendra resources.

- [How Amazon Kendra works with IAM](https://docs.aws.amazon.com/kendra/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Kendra, you should understand what IAM features are available to use with Amazon Kendra.
- [Identity-based policy examples](https://docs.aws.amazon.com/kendra/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Kendra resources.
- [AWS managed policies](https://docs.aws.amazon.com/kendra/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Kendra and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/kendra/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Kendra and IAM.
- [Security best practices](https://docs.aws.amazon.com/kendra/latest/dg/security-best-practices.html): Amazon Kendra provides a number of security features to consider as you develop and implement your own security policies.
- [Logging and monitoring in Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/incident-response.html): Monitoring is an important part of maintaining the reliability, availability, and performance of your Amazon Kendra applications.
- [Compliance validation](https://docs.aws.amazon.com/kendra/latest/dg/kendra-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/kendra/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Kendra features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/kendra/latest/dg/infrastructure-security.html): Learn how Amazon Kendra isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/kendra/latest/dg/configuration-and-vulnerability-analysis.html): AWS handles basic security tasks like guest operating system (OS) and database patching, firewall configuration, and disaster recovery.


## [Troubleshooting](https://docs.aws.amazon.com/kendra/latest/dg/troubleshooting.html)

- [Troubleshooting data sources](https://docs.aws.amazon.com/kendra/latest/dg/troubleshooting-data-sources.html): Help solve common issues when configuring and using Amazon Kendra data source connectors.
- [Troubleshooting document search results](https://docs.aws.amazon.com/kendra/latest/dg/troubleshooting-search-results.html): This section can help you fix issues in your Amazon Kendra search results.
- [Troubleshooting general issues](https://docs.aws.amazon.com/kendra/latest/dg/troubleshooting-general.html): Amazon Kendra uses CloudWatch metrics and logs to provide insight into synchronizing your data sources.


## [Amazon Kendra Intelligent Ranking](https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html)

- [Intelligent Ranking for self-managed OpenSearch](https://docs.aws.amazon.com/kendra/latest/dg/opensearch-rerank.html): How to set up and use the Amazon Kendra Intelligent Ranking plugin for OpenSearch (self managed).
- [Semantically ranking a search service's results](https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html): How to use Amazon Kendra to semantically re-rank a search service's results.
