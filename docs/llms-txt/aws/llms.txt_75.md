# Source: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/llms.txt

# Amazon Q Business User Guide

- [What is Amazon Q Business?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html)
- [Creating an Amazon Quick-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-quicksight.html)
- [Using a web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-web-experience.html)
- [Maintenance updates](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/maintenance.html)
- [Service quotas](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quotas-regions.html)
- [Document history](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/getting-started.html)

- [How Amazon Q Business works](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/how-it-works.html): Learn about Amazon Q Business, a service that helps you build interactive chat applications for end users using your enterprise data.
- [Key concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/concepts-terms.html): Learn about the key concepts and terms to help you understand Amazon Q Business.
- [Subscription tiers and index types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html): Learn about the user subscriptions tiers and index types of Amazon Q Businessâa service that helps you build generative AI-powered interactive chat application environments for end users using your enterprise data.
- [Supported document formats](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html): Learn about document types supported by Amazon Q Business.
- [Document attributes and types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html): Learn about the document attributes and document attribute types supported by Amazon Q Business.
- [Supported languages](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-languages.html): Learn about supported languages in Amazon Q Business.
- [Setting up](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/setting-up.html): Learn about the tasks that are required to begin using Amazon Q Business.

### [IAM roles](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html)

Learn about the required access permissions for Amazon Q Business.

- [Amazon Q Business application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam-role.html): Learn about the IAM roles needed for a Amazon Q Business application.

### [Amazon Q Business web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-experience-iam-role.html)

Learn about the IAM roles needed for a Amazon Q Business web experience.

- [IAM Identity Center web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-experience-iam-role-idc.html): Learn about the IAM roles needed for a Amazon Q Business application using IAM Identity Center for identity management.
- [IAM Federation web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-experience-iam-role-iam.html): Learn about the IAM roles needed for a Amazon Q Business web experience using IAM.
- [Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-q-apps-iam-permissions.html): Learn about the IAM roles needed for a Amazon Q Business web experience with Amazon Q Apps.
- [Data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles-ds.html): Learn about IAM roles needed for Amazon Q Business data source connectors.
- [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugin-iam-role.html): Learn about the IAM roles needed for a Amazon Q Business plugin.
- [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-iam-roles.html): Learn about the IAM roles needed for a Amazon Q Business application using custom document enrichment (CDE).
- [Amazon Kendra retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/kendra-retriever-iam-role.html): Learn about the IAM roles needed for a Amazon Q Business application using a Amazon Kendra retriever.


## [Creating an IAM Identity Center-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html)

- [Configuring an IAM Identity Center instance](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/idc-setup.html): Learn about setting up an IAM Identity Center instance for Amazon Q Business.
- [Creating an application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-app.html): Learn about creating an Amazon Q Business application environment.
- [Migrating an application to IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/migrate-application.html): Learn about the process for migrating an Amazon Q Business SAML 2.0 application to IAM Identity Center.
- [Using APIs to create an application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/making-sigv4-authenticated-api-calls.html): Learn how to make authenticated Amazon Q Business API calls using IAM Identity Center.

### [Managing resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/managing-resources.html)

Learn about the process for managing Amazon Q Business resources.

- [Managing applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-app-actions.html): Learn how to manage a Amazon Q Business application environment.
- [Managing web experiences](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-exp-actions.html): Learn about managing an Amazon Q Business web experience.
- [Managing subscriptions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions.html): Learn how to delete user subscriptions added to an Amazon Q Business application environment.
- [Tagging resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html): Learn how to assign tags to Amazon Q Business resources.


## [Creating an IAM federated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html)

- [Using Okta for IAM federation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam-okta.html): Learn about the process for creating the Amazon Q Business application environment using IAM Federation for end user management.
- [Using Microsoft Entra ID for IAM federation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam-entraid.html): Learn about the process for creating the Amazon Q Business application environment using IAM Federation with Microsoft Entra ID for end user management.
- [Connecting multiple Amazon Q Business applications to a single IdP](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/multiple-qbusiness-apps-idp.html): Learn about connecting multiple Amazon Q Business applications to an identity provider.
- [Using APIs to create an IAM federated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/making-sigv4-authenticated-api-calls-iam.html): Learn about making authenticated Amazon Q Business API calls using IAM federation.

### [Managing resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/managing-resources-iam.html)

Learn about the process for managing Amazon Q Business resources.

- [Managing applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-app-actions-iam.html): Learn how to manage a Amazon Q Business application environment.
- [Managing web experiences](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-exp-actions-iam.html): Learn about managing an Amazon Q Business web experience.
- [Managing subscriptions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions-iam.html): Learn how to manage user subscriptions added to an Amazon Q Business application environment.
- [Tagging resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging-iam.html): Learn about tagging Amazon Q Business resources.


## [Creating anonymous access application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-anonymous-application.html)

- [Using APIs to create an application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/making-sigv4-authenticated-api-calls-anonymous-applications.html): Learn how to make authenticated Amazon Q Business API calls for application environment supporting anonymous access

### [Managing resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/managing-anonymous-app-resources.html)

Learn about the process for managing resources for Amazon Q Business application environments that support anonymous access.

- [IAM policies](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/anonymous-application-iam-policies.html): Example IAM policies for Amazon Q Business application environment supporting anonymous access
- [Managing anonymous application environments](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-anonymous-app-actions.html): Learn how to manage a Amazon Q Business application environment.
- [Managing web experiences](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-exp-actions-anonymous.html): Learn about managing an Amazon Q Business web experience for anonymous access.


## [Enhancing an application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/enhancements.html)

### [Data sources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-sources.html)

Learn how about Amazon Q Business data source connectors.

- [Creating an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html): Learn about creating and selecting an index and retriever for an Amazon Q Business application environment.
- [Uploading files](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-docs.html): Learn how to upload documents directly into an Amazon Q Business application environment.

### [Adding data connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-connectors.html)

Learn how about Amazon Q Business data source connectors.

- [Concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html): Learn about key Amazon Q Business data source connector concepts.
- [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html): Learn about what each Amazon Q Business considers as a document.
- [Configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html): Learn about Amazon Q Business data source connector best practices.

### [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html)

Learn the data source connectors Amazon Q Business supports.

### [Legacy connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/legacy-connectors.html)

The following connectors remain supported for existing customers but are no longer available for new onboarding.

### [AEM (Cloud)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-connector.html)

Learn how to connect Amazon Q Business with AEM (Cloud).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-limitations.html): Describes the known limitations of the Amazon Q Business AEM (Cloud) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-overview.html): An overview of the AEM (Cloud) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-prereqs.html): Prerequisites for connecting Amazon Q Business with AEM (Cloud).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-console.html): Learn how to connect Amazon Q Business with AEM (Cloud) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-api.html): Learn how to connect Amazon Q Business with AEM (Cloud) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-user-management.html): Learn how Amazon Q Business crawls AEM (Cloud) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-field-mappings.html): Learn what entities and field mappings the Amazon Q Business AEM (Cloud) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-iam-role.html): Describes the IAM permissions needed for Amazon Q to connect to AEM (Cloud).
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-cloud-error-codes.html): Learn how to interpret error codes in the AEM (Cloud) connector.

### [AEM (Server)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-connector.html)

Learn how to connect Amazon Q Business with AEM (Server) .

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-limitations.html): Describes the known limitations of the Amazon Q Business AEM (Server) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-overview.html): An overview of the AEM (Server) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-prereqs.html): Prerequisites for connecting Amazon Q Business with AEM (Server) .
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-console.html): Learn how to connect Amazon Q Business with AEM (Server) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-api.html): Learn how to connect Amazon Q Business with AEM (Server) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-user-management.html): Learn how Amazon Q Business crawls AEM (Server) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-field-mappings.html): Learn what entities and field mappings the Amazon Q Business AEM (Server) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to AEM (Server) .
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-server-error-codes.html): Learn how to interpret error codes in the AEM (Server) connector.

### [Alfresco (Cloud)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-connector.html)

Learn how to connect Amazon Q Business with Alfresco (Cloud).

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-overview.html): An overview of the Alfresco (Cloud) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-prereqs.html): Prerequisites for connecting Amazon Q Business with Alfresco (Cloud).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-console.html): Learn how to connect Amazon Q Business with Alfresco (Cloud) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-api.html): Learn how to connect Amazon Q Business with Alfresco (Cloud) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-user-management.html): Learn how Amazon Q Business crawls Alfresco (Cloud) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Alfresco (Cloud) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Alfresco (Cloud).

### [Alfresco (Server)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-connector.html)

Learn how to connect Amazon Q Business with Alfresco (Server).

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-overview.html): An overview of the Alfresco (Server) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-prereqs.html): Prerequisites for connecting Amazon Q Business with Alfresco (Server).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-console.html): Learn how to connect Amazon Q Business with Alfresco (Server) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-api.html): Learn how to connect Amazon Q Business with Alfresco (Server) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-user-management.html): Learn how Amazon Q Business crawls Alfresco (Server) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Alfresco (Server) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-server-iam-role.html): Describes the IAM permissions needed for Amazon Q to connect to Alfresco (Server).

### [Aurora (MySQL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-connector.html)

Learn how to connect Amazon Q Business with Aurora (MySQL).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-limitations.html): Describes the known limitations of the Amazon Q Business Aurora (MySQL) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-overview.html): An overview of the Aurora (MySQL) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-prereqs.html): Prerequisites for connecting Amazon Q Business with Aurora (MySQL).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-console.html): Learn how to connect Amazon Q Business with Aurora (MySQL) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-api.html): Learn how to connect Amazon Q Business with Aurora (MySQL) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-user-management.html): Learn how Amazon Q Business crawls Aurora (MySQL) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Aurora (MySQL) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-mysql-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Aurora (MySQL).

### [Aurora (PostgreSQL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-connector.html)

Learn how to connect Amazon Q Business with Aurora (PostgreSQL).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-limitations.html): Describes the known limitations of the Amazon Q Business Aurora (PostgreSQL) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-overview.html): An overview of the Aurora (PostgreSQL) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-prereqs.html): Prerequisites for connecting Amazon Q Business with Aurora (PostgreSQL).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-console.html): Learn how to connect Amazon Q Business with Aurora (PostgreSQL) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-api.html): Learn how to connect Amazon Q Business with Aurora (PostgreSQL) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-user-management.html): Learn how Amazon Q Business crawls Aurora (PostgreSQL) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Aurora (PostgreSQL) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aurora-postgresql-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Aurora (PostgreSQL).

### [Drupal](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-connector.html)

Learn how to connect Amazon Q Business with Drupal.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-overview.html): An overview of the Drupal connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-prereqs.html): Prerequisites for connecting Amazon Q Business with Drupal.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-console.html): Learn how to connect Amazon Q Business with Drupal using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-api.html): Learn how to connect Amazon Q Business with Drupal using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-user-management.html): Learn how Amazon Q Business crawls Drupal ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-field-mappings.html): Learn what entities and field mappings the Drupal connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Drupal.
- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-limitations.html): Describes the known limitations of the Amazon Q Business Drupal connector.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-error-codes.html): Learn how to interpret error codes in the Drupal connector.

### [IBM DB2](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-connector.html)

Learn how to connect Amazon Q Business with IBM DB2.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-limitations.html): Describes the known limitations of the IBM DB2 connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-overview.html): An overview of the IBM DB2 connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-prereqs.html): Prerequisites for connecting Amazon Q Business with IBM DB2.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-console.html): Learn how to connect Amazon Q Business with IBM DB2 using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-api.html): Learn how to connect Amazon Q Business with IBM DB2 using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-user-management.html): Learn how Amazon Q Business crawls IBM DB2 ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-field-mappings.html): Learn what entities and field mappings the IBM DB2 connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ibm-db2-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to IBM DB2.

### [Microsoft SQL Server](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-connector.html)

Learn how to connect Amazon Q Business with Microsoft SQL Server.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-limitations.html): Describes the known limitations of the Amazon Q Business Microsoft SQL Server connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-overview.html): An overview of the Microsoft SQL Server connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-prereqs.html): Prerequisites for connecting Amazon Q Business with Microsoft SQL Server.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-console.html): Learn how to connect Amazon Q Business with Microsoft SQL Server using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-api.html): Learn how to connect Amazon Q Business with Microsoft SQL Server using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-user-management.html): Learn how Amazon Q Business crawls Microsoft SQL Server ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Microsoft SQL Server connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/ms-sql-server-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Microsoft SQL Server.

### [Microsoft Yammer](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-connector.html)

Learn how to connect Amazon Q Business with Microsoft Yammer.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-limitations.html): Describes the known limitations of the Microsoft Yammer connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-overview.html): An overview of the Microsoft Yammer connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-prereqs.html): Prerequisites for connecting Amazon Q Business with Microsoft Yammer.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-console.html): Learn how to connect Amazon Q Business with Microsoft Yammer using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-api.html): Learn how to connect Amazon Q Business with Microsoft Yammer using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-user-management.html): Learn how Amazon Q Business crawls Microsoft Yammer ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-field-mappings.html): Learn what entities and field mappings the Microsoft Yammer connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Microsoft Yammer.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/yammer-error-codes.html): Learn how to interpret error codes in the Microsoft Yammer connector.

### [MySQL](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-connector.html)

Learn how to connect Amazon Q Business with MySQL.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-limitations.html): Describes the known limitations of the Amazon Q Business MySQL connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-overview.html): An overview of the MySQL connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-prereqs.html): Prerequisites for connecting Amazon Q Business with MySQL.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-console.html): Learn how to connect Amazon Q Business with MySQL using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-api.html): Learn how to connect Amazon Q Business with MySQL using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-user-management.html): Learn how Amazon Q Business crawls MySQL ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-field-mappings.html): Learn what entities and field mappings the Amazon Q Business MySQL connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to MySQL.

### [Oracle Database](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-connector.html)

Learn how to connect Amazon Q Business with Oracle Database.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-limitations.html): Describes the known limitations of the Amazon Q Business Oracle Database connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-overview.html): An overview of the Oracle Database connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-prereqs.html): Prerequisites for connecting Amazon Q Business with Oracle Database.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-console.html): Learn how to connect Amazon Q Business with Oracle Database using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-api.html): Learn how to connect Amazon Q Business with Oracle Database using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-user-management.html): Learn how Amazon Q Business crawls Oracle Database ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Oracle Database connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/oracle-database-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Oracle Database.

### [PostgreSQL](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-connector.html)

Learn how to connect Amazon Q Business with PostgreSQL.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-limitations.html): Describes the known limitations of the Amazon Q Business PostgreSQL connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-overview.html): An overview of the PostgreSQL connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-prereqs.html): Prerequisites for connecting Amazon Q Business with PostgreSQL.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-console.html): Learn how to connect Amazon Q Business with PostgreSQL using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-api.html): Learn how to connect Amazon Q Business with PostgreSQL using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-user-management.html): Learn how Amazon Q Business crawls PostgreSQL ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-field-mappings.html): Learn what entities and field mappings the Amazon Q Business PostgreSQL connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/postgresql-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to PostgreSQL.

### [Quip](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-connector.html)

Learn how to connect Amazon Q Business with Quip.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-limitations.html): Describes the known limitations of the Quip connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-overview.html): An overview of the Quip connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-prereqs.html): Prerequisites for connecting Amazon Q Business with Quip.
- [Setting up Quip](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-credentials.html): Learn how to configure Quip for Amazon Q.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-console.html): Learn how to connect Amazon Q Business with Quip using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-api.html): Learn how to connect Amazon Q Business with Quip using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-user-management.html): Learn how Amazon Q Business crawls Quip ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-field-mappings.html): Learn what entities and field mappings the Quip connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Quip.

### [Amazon RDS (Microsoft SQL Server)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-connector.html)

Learn how to connect Amazon Q Business with Amazon RDS (Microsoft SQL Server).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-limitations.html): Describes the known limitations of the Amazon Q Business Amazon RDS (Microsoft SQL Server) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-overview.html): An overview of the Amazon RDS (Microsoft SQL Server) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-prereqs.html): Prerequisites for connecting Amazon Q Business with Amazon RDS (Microsoft SQL Server).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-console.html): Learn how to connect Amazon Q with Amazon RDS (Microsoft SQL Server) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-api.html): Learn how to connect Amazon Q Business with Amazon RDS (Microsoft SQL Server) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-user-management.html): Learn how Amazon Q Business crawls Amazon RDS (Microsoft SQL Server) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Amazon RDS (Microsoft SQL Server) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-ms-sql-server-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Amazon RDS (Microsoft SQL Server).

### [Amazon RDS (MySQL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-connector.html)

Learn how to connect Amazon Q Business with Amazon RDS (MySQL).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-limitations.html): Describes the known limitations of the Amazon Q Amazon RDS (MySQL) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-overview.html): An overview of the Amazon RDS (MySQL) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-prereqs.html): Prerequisites for connecting Amazon Q Business with Amazon RDS (MySQL).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-console.html): Learn how to connect Amazon Q Business with Amazon RDS (MySQL) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-api.html): Learn how to connect Amazon Q Business with Amazon RDS (MySQL) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-user-management.html): Learn how Amazon Q Business crawls Amazon RDS (MySQL) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Amazon RDS (MySQL) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-my-sql-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Amazon RDS (MySQL).

### [Amazon RDS (Oracle)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-connector.html)

Learn how to connect Amazon Q Business with Amazon RDS (Oracle).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-limitations.html): Describes the known limitations of the Amazon Q Business Amazon RDS (Oracle) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-overview.html): An overview of the Amazon RDS (Oracle) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-prereqs.html): Prerequisites for connecting Amazon Q Business with Amazon RDS (Oracle).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-console.html): Learn how to connect Amazon Q Business with Amazon RDS (Oracle) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-api.html): Learn how to connect Amazon Q Business with Amazon RDS (Oracle) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-user-management.html): Learn how Amazon Q Business crawls Amazon RDS (Oracle) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Amazon RDS (Oracle) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-oracle-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Amazon RDS (Oracle).

### [Amazon RDS (PostgreSQL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-connector.html)

Learn how to connect Amazon Q Business with Amazon RDS (PostgreSQL).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-limitations.html): Describes the known limitations of the Amazon RDS (PostgreSQL) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-overview.html): An overview of the Amazon RDS (PostgreSQL) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-prereqs.html): Prerequisites for connecting Amazon Q Business with Amazon RDS (PostgreSQL).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-console.html): Learn how to connect Amazon Q Business with Amazon RDS (PostgreSQL) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-api.html): Learn how to connect Amazon Q Business with Amazon RDS (PostgreSQL) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-user-management.html): Learn how Amazon Q Business crawls Amazon RDS (PostgreSQL) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-field-mappings.html): Learn what entities and field mappings the Amazon RDS (PostgreSQL) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/rds-postgresql-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Amazon RDS (PostgreSQL).

### [Amazon Q custom connector](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-connector.html)

Use a custom data source when you have a repository that Amazon Q Business doesnât yet provide a data source connector for.

- [Creating an Amazon Q custom connector](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-connector-hiw.html): To use a custom data source, create an application environment that is responsible for updating your Amazon Q index.
- [Required attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-required-attributes.html): When you submit a document to Amazon Q using the BatchPutDocument API operation, you must provide the following two attributes for each document:
- [Viewing metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-metrics.html): After a sync job is finished, you can use the DataSourceSyncJobMetrics API operation to get the metrics associated with the sync job.

### [Amazon Q Web Crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-webcrawler.html)

Learn how to connect Amazon Q Business with Web Crawler.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/webcrawler-overview.html): An overview of the Web Crawler connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/webcrawler-prereqs.html): Prerequisites for connecting Amazon Q Business with Web Crawler.
- [Retrieving XPaths](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/webcrawler-retrieving-credentials.html): Learn how to retrieve XPaths for the Web Crawler connector.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/webcrawler-console.html): Learn how to connect Amazon Q Business with Web Crawler using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-api.html): Learn how to connect Amazon Q Business with Web Crawler using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-cfn.html): Learn how to connect Amazon Q Business with Web Crawler using AWS CloudFormation.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-field-mappings.html): Learn what entities and field mappings the Web Crawler connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/webcrawler-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Web Crawler.
- [Configuring a robots.txt file](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/stop-web-crawler.html): Learn how to configure a robots.txt file for Amazon Q Business Web Crawler.

### [Asana (Preview)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-connector.html)

Learn how to connect Amazon Q Business with Asana.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-limitations.html): Describes the known limitations of the Amazon Q Business Asana connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-overview.html): An overview of the Asana connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-prereqs.html): Prerequisites for connecting Amazon Q Business with Asana.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-console.html): Learn how to connect Amazon Q Business with Asana using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-api.html): Learn how to connect Amazon Q Business with Asana using API.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Asana connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Asana.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-error-codes.html): Learn how to interpret error codes in the Amazon Q Asana connector.

### [Box](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-connector.html)

Learn how to connect Amazon Q Business with Box.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-limitations.html): Describes the known limitations of the Amazon Q Box connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-overview.html): An overview of the Box connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-prereqs.html): Prerequisites for connecting Amazon Q Business with Box.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-console.html): Learn how to connect Amazon Q Business with Box using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-api.html): Learn how to connect Amazon Q Business with Box using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-user-management.html): Learn how Amazon Q Business crawls Box ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-field-mappings.html): Learn what entities and field mappings the Box connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/box-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Box.

### [Confluence (Cloud)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-connector.html)

Learn how to connect Amazon Q Business with Confluence (Cloud).

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-overview.html): An overview of the Confluence (Cloud) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-prereqs.html): Prerequisites for connecting Amazon Q Business with Confluence (Cloud).

### [Setting up Confluence (Cloud)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-credentials.html)

Learn how to configure Confluence (Cloud) for Amazon Q Business.

- [Basic authentication](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-credentials-basic.html): You can connect Amazon Q to Confluence (Cloud) using basic authentication credentials.
- [OAuth 2.0 authentication](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-credentials-oauth.html): You can connect Amazon Q to Confluence (Cloud) using OAuth 2.0 authentication credentials.
- [How Amazon Q works with Confluence (Cloud) access and refresh tokens](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-credentials-notes.html): The following are important points to note about using Confluence (Cloud) access and refresh tokens with Amazon Q:
- [Checking Confluence (Cloud) connectivity](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-connection-check.html): Before you sync your Confluence (Cloud) data source connector after configuring it, we recommend you check the connection between Amazon Q Business and Confluence (Cloud).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-console.html): Learn how to connect Amazon Q Business with Confluence (Cloud) using the console.
- [Connecting Amazon Q Business to Confluence (Cloud) using APIs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-api.html): You use the CreateDataSource action to connect a data source to your Amazon Q application.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-cfn.html): Learn how to connect Amazon Q Business with Confluence (Cloud) using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-user-management.html): Learn how Amazon Q Business crawls Confluence (Cloud) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Confluence (Cloud) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-iam-role.html): Describes the IAM permissions needed for Amazon Q to connect to Confluence (Cloud).
- [Error codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-error-codes.html): Learn how to interpret error codes in the Confluence (Cloud) connector.

### [Confluence (Server/Data Center)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-connector.html)

Atlassian Confluence is a collaborative work-management tool designed for sharing, storing, and working on project planning, software development, and product management.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-limitations.html): Describes the known limitations of the Amazon Q Business Confluence (Server/Data Center) connector.
- [Confluence (Server/Data Center) connector overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html): The following table gives an overview of the Amazon Q Business Confluence (Server/Data Center) connector and its supported features.
- [Prerequisites for connecting Amazon Q to Confluence (Server/Data Center)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-prereqs.html): Before you begin, make sure that you have completed the following prerequisites.
- [Checking Confluence (Server/Data Center) connectivity](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-connection-check.html): Before you sync your Confluence (Server/Data Center) data source connector after configuring it, we recommend you check the connection between Amazon Q Business and Confluence (Server/Data Center).
- [Connecting Amazon Q Business to Confluence (Server/Data Center) using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-console.html): On the Confluence page, enter the following information:
- [Connecting Amazon Q Business to Confluence (Server/Data Center) using APIs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-api.html): You use the CreateDataSource action to connect a data source to your Amazon Q application.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-cfn.html): Learn how to connect Amazon Q Business with Confluence (Server/Data Center) using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-user-management.html): Learn how Amazon Q Business crawls Confluence (Server/Data Center) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Confluence (Server/Data Center) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-iam-role.html): Describes the IAM permissions needed for Amazon Q to connect to Confluence (Server/Data Center).
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-error-codes.html): Learn how to interpret error codes in the Confluence (Server/Data Center) connector.

### [Dropbox](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-connector.html)

Learn how to connect Amazon Q Business with Dropbox.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-limitations.html): Describes the known limitations of the Amazon Q Dropbox connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-overview.html): An overview of the Dropbox connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-prereqs.html): Prerequisites for connecting Amazon Q Business with Dropbox.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-console.html): Learn how to connect Amazon Q Business with Dropbox using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbix-api.html): Learn how to connect Amazon Q Business with Dropbox using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-user-management.html): Learn how Amazon Q Business crawls Dropbox ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-field-mappings.html): Learn what entities and field mappings the Dropbox connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Dropbox.

### [Amazon FSx (Windows)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-windows-connector.html)

Learn how to connect Amazon Q Business with Amazon FSx (Windows).

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-windows-overview.html): An overview of the Amazon FSx (Windows) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-windows-prereqs.html): Prerequisites for connecting Amazon Q Business with Amazon FSx (Windows).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-windows-console.html): Learn how to connect Amazon Q Business with Amazon FSx (Windows) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-api.html): Learn how to connect Amazon Q Business with Amazon FSx (Windows) using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-user-management.html): Learn how Amazon Q Business crawls Amazon FSx (Windows) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-field-mappings.html): Learn what entities and field mappings the Amazon FSx (Windows) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/fsx-windows-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Amazon FSx (Windows).

### [GitHub (Cloud)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-connector.html)

Learn how to connect Amazon Q Business with GitHub (Cloud).

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-overview.html): An overview of the GitHub (Cloud) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-prereqs.html): Prerequisites for connecting Amazon Q Business with GitHub (Cloud).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-console.html): Learn how to connect Amazon Q Business with GitHub (Cloud) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-api.html): Learn how to connect Amazon Q Business with GitHub (Cloud) using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-cfn.html): Learn how to connect Amazon Q Business with GitHub (Cloud) using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-user-management.html): Learn how Amazon Q Business crawls GitHub Cloud ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-field-mappings.html): Learn what entities and field mappings the Amazon Q Business GitHub (Cloud) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to GitHub (Cloud).

### [GitHub (Server)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-connector.html)

Learn how to connect Amazon Q Business with GitHub (Server).

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-overview.html): An overview of the GitHub (Server) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-prereqs.html): Prerequisites for connecting Amazon Q Business with GitHub (Server).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-console.html): Learn how to connect Amazon Q Business with GitHub (Server) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-api.html): Learn how to connect Amazon Q Business with GitHub (Server) using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-cfn.html): Learn how to connect Amazon Q Business with GitHub (Server) using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-user-management.html): Learn how Amazon Q Business crawls GitHub Server ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-field-mappings.html): Learn what entities and field mappings the Amazon Q Business GitHub (Server) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-server-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to GitHub (Server).

### [Gmail](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-connector.html)

Learn how to connect Amazon Q Business with Gmail.

- [Connector versions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-versions.html): Choose between two Gmail connector versions.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-overview.html): An overview of the Gmail connector.

### [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-prereqs.html)

Prerequisites for connecting Amazon Q Business with Gmail.

- [Setting up Google Workspace authentication](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-prereqs-google.html): Complete these steps in your Google Workspace environment to prepare for the Amazon Q Business connection:
- [Using the latest connector (Console)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-console-new.html): Learn how to connect Amazon Q Business with Gmail using the latest connector through the console.
- [Using the legacy connector (Console)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-console-original.html): Learn how to connect Amazon Q Business with Gmail using the legacy connector through the console.
- [Using the new connector (API)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-new-api.html): Use the API to connect Amazon Q Business with Gmail using the new connector programmatically.
- [Using the original connector (API)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-original-api.html): Use the API to connect Amazon Q Business with Gmail using the original connector programmatically.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-user-management.html): Understand how Amazon Q Business crawls Gmail ACL information.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-field-mappings.html): Understand the entities and field mappings that the Gmail connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Gmail.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-error-codes.html): Learn how to interpret error codes in the Gmail connector.

### [Google Calendar (Preview)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-connector.html)

Learn how to connect Amazon Q Business with Google Calendar.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-limitations.html): Describes the known limitations of the Amazon Q Business Google Calendar connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-overview.html): An overview of the Google Calendar connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-prereqs.html): Prerequisites for connecting Amazon Q Business with Google Calendar.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-console.html): Learn how to connect Amazon Q Business with Google Calendar using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-api.html): Learn how to connect Amazon Q Business with Google Calendar using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-user-management.html): Learn how Amazon Q Business crawls Google Calendar ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-calendar-field-mappings.html): Learn what entities and field mappings the Google Calendar connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Google Calendar.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-error-codes.html): Learn how to interpret error codes in the Google Calendar connector.

### [Google Drive](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-connector.html)

Learn how to connect Amazon Q Business with Google Drive using either the enhanced new or connector.

### [Google Drive New](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-connector-primary.html)

Learn how to connect Amazon Q Business with Google Drive using the enhanced new connector.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-limitations-primary.html): Describes the known limitations of the Amazon Q Business Google Drive connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-overview-primary.html): An overview of the Google Drive connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-prereqs-gd2.html): Prerequisites for connecting Amazon Q Business with Google Drive.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-console-v2.html): Learn how to connect Amazon Q Business with Google Drive new using the console.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Google Drive new.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-acl-crawling.html): Learn how Amazon Q Business crawls Google Drive ACL using the new connector.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-api.html): Learn how to connect Amazon Q Business with GoogleDrive New using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-cfn.html): Learn how to connect Amazon Q Business with Google Drive New using AWS CloudFormation.

### [Google Drive (Original)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-connector-primary1.html)

Learn how to connect Amazon Q Business with Google Drive using the original connector.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-overview-primary.html): An overview of the Google Drive connector .
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-prereqs.html): Prerequisites for connecting Amazon Q Business with Google Drive.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-console.html): Learn how to connect Amazon Q Business with Google Drive using the console.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Google Drive .
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-error-codes.html): Learn how to interpret error codes in the Amazon Q Google Drive connector .
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/v1-c1-user-management.html): Learn how Amazon Q Business crawls Google Drive ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-field-mappings.html): Learn what entities and field mappings the Google Drive connector supports.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-api.html): Learn how to connect Amazon Q Business with GoogleDrive using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-cfn.html): Learn how to connect Amazon Q Business with Google Drive using AWS CloudFormation.

### [Jira](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-connector.html)

Learn how to connect Amazon Q Business with Jira.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-limitations.html): Describes the known limitations of the Amazon Q Jira connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-overview.html): An overview of the Jira connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-prereqs.html): Prerequisites for connecting Amazon Q Business with Jira.

### [Setting up Jira](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-credentials.html)

Learn how to configure Jira for Amazon Q Business.

- [Basic authentication](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-credentials-basic.html): You can connect Amazon Q to Jira using basic authentication credentials.
- [OAuth 2.0 authentication](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-credentials-oauth.html): You can connect Amazon Q to Jira using OAuth 2.0 authentication credentials.
- [How Amazon Q works with Jira access and refresh tokens](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-credentials-notes.html): The following are important points to note about using Jira access and refresh tokens with Amazon Q:
- [Checking Jira connectivity](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-connection-check.html): Before you sync your Jira data source connector after configuring it, we recommend you check the connection between Amazon Q Business and Jira.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-console.html): Learn how to connect Amazon Q Business with Jira using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-api.html): Learn how to connect Amazon Q Business with Jira using API.
- [Using CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-cfn.html): Learn how to connect Amazon Q Business with Jira using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-user-management.html): Learn how Amazon Q Business crawls Jira ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-field-mappings.html): Learn what entities and field mappings the Jira connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Jira.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-error-codes.html): Learn how to interpret error codes in the Jira connector.

### [Microsoft Exchange](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-connector.html)

Use Amazon Q Business to connect with Microsoft Exchange.

- [Connector versions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-versions.html): Choose between two Microsoft Exchange connector versions.
- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-limitations.html): Describes the known limitations of the Amazon Q Microsoft Exchange connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-overview.html): An overview of the Microsoft Exchange connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-prereqs.html): Complete these steps before connecting your Exchange environment to Amazon Q Business.
- [Using the latest connector (Console)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-console-new.html): Learn how to connect Amazon Q Business with Microsoft Exchange using the latest connector.
- [Using the legacy connector (Console)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-console-original.html): Learn how to connect Amazon Q Business with Microsoft Exchange using the legacy connector with full configuration options.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-api.html): Use the API to connect Amazon Q Business with Microsoft Exchange programmatically.
- [Using the API (New connector)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-new-api.html): Use the API to connect Amazon Q Business with Microsoft Exchange programmatically using the new connector version.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-user-management.html): Understand how Amazon Q Business crawls Exchange ACL information.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-field-mappings.html): Understand the entities and field mappings that the Microsoft Exchange connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Microsoft Exchange.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-error-codes.html): Learn how to interpret error codes in the Microsoft Exchange connector.

### [Microsoft OneDrive](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-connector.html)

Learn how to connect Amazon Q Business with Microsoft OneDrive using either the new connector or original connector.

### [Microsoft OneDrive New](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-connector.html)

Learn how to connect Amazon Q Business with Microsoft OneDrive using the new connector.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-overview.html): The following table gives an overview of the Amazon Q Business Microsoft OneDrive new connector and its supported features.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-prereqs.html): Before you begin, make sure that you have completed the following prerequisites.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-console.html): The following procedure outlines how to connect Amazon Q Business to Microsoft OneDrive using the new connector with the AWS Management Console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-v2-api.html): Learn how to connect Amazon Q Business with Microsoft OneDrive using API.
- [Using AWS CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-v2-cfn.html): Learn how to connect Amazon Q Business with Microsoft OneDrive using AWS CloudFormation with the new connector.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-acl-crawling.html): Learn how Amazon Q Business crawls Microsoft OneDrive ACL using the new connector.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-iam-role.html): If you use the AWS CLI or an AWS SDK, you must create an AWS Identity and Access Management (IAM) policy before you create an Amazon Q resource.

### [Microsoft OneDrive Original](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-original-connector.html)

Learn how to connect Amazon Q Business with Microsoft OneDrive using the original connector.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-original-overview.html): The following table gives an overview of the Amazon Q Business Microsoft OneDrive original connector and its supported features.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-original-prereqs.html): Before you begin, make sure that you have completed the following prerequisites.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-original-console.html): The following procedure outlines how to connect Amazon Q Business to Microsoft OneDrive using the original connector with the AWS Management Console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-v1-api.html): Learn how to connect Amazon Q Business with Microsoft OneDrive using API
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-legacy-acl-crawling.html): Learn how Amazon Q Business crawls Microsoft OneDrive ACL using the legacy connector.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-legacy-field-mappings.html): Learn what entities and field mappings the Microsoft OneDrive legacy connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-original-iam-role.html): If you use the AWS CLI or an AWS SDK, you must create an AWS Identity and Access Management (IAM) policy before you create an Amazon Q resource.
- [Error codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-original-error-codes.html): The following table provides information about error codes you may see for the Microsoft OneDrive original connector and suggested resolutions.

### [Microsoft SharePoint (Online)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-connector.html)

Learn how to connect Amazon Q Business with SharePoint (Online).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-limitations.html): Describes the known limitations of the Amazon Q Business SharePoint (Online) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-overview.html): An overview of the SharePoint (Online) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-prereqs.html): Prerequisites for connecting Amazon Q Business with SharePoint (Online).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-console.html): Learn how to connect Amazon Q Business with SharePoint (Online) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-api.html): Learn how to connect Amazon Q Business with SharePoint (Online) using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-cfn.html): Learn how to connect Amazon Q Business with SharePoint (Online) using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-user-management.html): Learn how Amazon Q Business crawls SharePoint (Online) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-field-mappings.html): Learn what entities and field mappings the Amazon Q Business SharePoint (Online) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-iam-role.html): Describes the IAM permissions needed for Amazon Q to connect to SharePoint (Online).
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-error-codes.html): Learn how to interpret error codes in the SharePoint (Online) connector.

### [Microsoft SharePoint Server 2016](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-connector.html)

Learn how to connect Amazon Q Business with SharePoint Server 2016.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-limitations.html): Describes the known limitations of the Amazon Q Business SharePoint Server 2016 connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-overview.html): An overview of the SharePoint Server 2016 connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-prereqs.html): Prerequisites for connecting Amazon Q Business with SharePoint Server 2016.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-console.html): Learn how to connect Amazon Q Business with SharePoint Server 2016 using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-api.html): Learn how to connect Amazon Q Business with SharePoint Server 2016 using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-cfn.html): Learn how to connect Amazon Q Business with SharePoint Server 2016 using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-user-management.html): Learn how Amazon Q Business crawls SharePoint Server 2016 ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-field-mappings.html): Learn what entities and field mappings the Amazon Q Business SharePoint Server 2016 connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to SharePoint Server 2016.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-error-codes.html): Learn how to interpret error codes in the SharePoint Server 2016 connector.

### [Microsoft SharePoint Server 2019](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-connector.html)

Learn how to connect Amazon Q Business with SharePoint Server 2019.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-limitations.html): Describes the known limitations of the Amazon Q Business SharePoint Server 2019 connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-overview.html): An overview of the SharePoint Server 2019 connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-prereqs.html): Prerequisites for connecting Amazon Q Business with SharePoint Server 2019.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-console.html): Learn how to connect Amazon Q Business with SharePoint Server 2019 using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-api.html): Learn how to connect Amazon Q Business with SharePoint Server 2019 using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-cfn.html): Learn how to connect Amazon Q Business with SharePoint Server 2019 using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-user-management.html): Learn how Amazon Q Business crawls SharePoint Server 2019 ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-field-mappings.html): Learn what entities and field mappings the Amazon Q Business SharePoint Server 2019 connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to SharePoint Server 2019.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-error-codes.html): Learn how to interpret error codes in the SharePoint Server 2019 connector.

### [Microsoft SharePoint Server (Subscription Edition)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-connector.html)

Learn how to connect Amazon Q Business with SharePoint Server (Subscription Edition).

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-limitations.html): Describes the known limitations of the Amazon Q Business SharePoint Server (Subscription Edition) connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-overview.html): An overview of the SharePoint Server (Subscription Edition) connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-prereqs.html): Prerequisites for connecting Amazon Q Business with SharePoint Server (Subscription Edition).
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-console.html): Learn how to connect Amazon Q Business with SharePoint Server (Subscription Edition) using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-api.html): Learn how to connect Amazon Q Business with SharePoint Server (Subscription Edition) using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-cfn.html): Learn how to connect Amazon Q Business with SharePoint Server (Subscription Edition) using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-user-management.html): Learn how Amazon Q Business crawls SharePoint Server (Subscription Edition) ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-field-mappings.html): Learn what entities and field mappings the Amazon Q Business SharePoint Server (Subscription Edition) connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to SharePoint Server (Subscription Edition).
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-error-codes.html): Learn how to interpret error codes in the SharePoint Server (Subscription Edition) connector.

### [Microsoft Teams](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-connector.html)

Learn how to connect Amazon Q Business with Microsoft Teams.

- [Connector versions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-versions.html): Choose between two Microsoft Teams connector versions.
- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-limitations.html): Describes the known limitations of the Amazon Q Microsoft Teams connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-overview.html): An overview of the Microsoft Teams connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-prereqs.html): Complete these steps before connecting your Teams environment to Amazon Q Business.
- [Using the latest connector (Console)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-console-new.html): Connect Amazon Q Business with Microsoft Teams using the latest connector.
- [Using the legacy connector (Console)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-console-original.html): Connect Amazon Q Business with Microsoft Teams using the legacy connector with full configuration options.

### [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-api.html)

Connect Amazon Q Business with Microsoft Teams using API.

- [Using the API (new connector)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-new-api.html): Connect Amazon Q Business with Microsoft Teams using API for the new connector version.
- [Using the API (Original connector)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-original-api.html): Learn how to connect Amazon Q Business with Microsoft Teams using API for the original connector version.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-cfn.html): Connect Amazon Q Business with Microsoft Teams using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-user-management.html): How Amazon Q Business crawls Microsoft Teams ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-field-mappings.html): Entities and field mappings the Microsoft Teams connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Microsoft Teams.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-troubleshooting.html): Troubleshoot your Microsoft Teams connector.

### [Amazon S3](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-connector.html)

Learn how to connect Amazon Q Business with Amazon S3 using either the new enhanced connector or the old connector.

### [Amazon S3 (New)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-connector.html)

Learn how to connect Amazon Q Business with Amazon S3 using the enhanced connector.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-overview.html): The following table gives an overview of the Amazon Q Business Amazon S3 connector and its supported features.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-prereqs.html): Before you begin, make sure that you have completed the following prerequisites.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-console.html): The following procedure outlines how to connect Amazon Q Business to Amazon S3 using the AWS Management Console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-api.html): Learn how to connect Amazon Q Business with Amazon S3 using the new API.
- [Using AWS CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-cfn.html): Learn how to connect Amazon Q Business with Amazon S3 using AWS CloudFormation with the new connector.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-iam-role.html): Whether you use the AWS Management Console or the CreateDataSource API, you must provide an IAM role that allows Amazon Q Business to access your Amazon S3 bucket.

### [Clickable Link Feature](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-clickable-links-shared.html)

Learn about the Clickable URL Feature in Amazon Q Business.

- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v2-clickable-links-troubleshooting.html): Resolve common issues when using clickable links for source references.
- [Adding metadata](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-metadata-v2.html): Learn how you can add metadata for documents in an Amazon Q Business Amazon S3 connector.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-user-management-2.html): Learn how Amazon Q Business crawls Amazon S3 ACL.

### [Amazon S3](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v1-connector.html)

Learn how to connect Amazon Q Business with Amazon S3 using the old connector.

- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v1-overview.html): The following table gives an overview of the Amazon Q Business Amazon S3 connector and its supported features.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v1-prereqs.html): Before you begin, make sure that you have completed the following prerequisites.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-console.html): Learn how to connect Amazon Q Business with Amazon S3 using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-api.html): Learn how to connect Amazon Q Business with Amazon S3 using API.
- [Using AWS CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-cfn.html): Learn how to connect Amazon Q Business with Amazon S3 using AWS CloudFormation.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v1-iam-role.html): Whether you use the AWS Management Console or the CreateDataSource API, you must provide an IAM role that allows Amazon Q Business to access your Amazon S3 bucket.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-field-mappings.html): Learn what entities and field mappings the Amazon S3 connector supports.

### [Clickable Link Feature](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v1-clickable-links-shared.html)

Learn about the Clickable URL Feature in Amazon Q Business for the legacy connector.

- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-v1-clickable-links-troubleshooting.html): Resolve common issues when using clickable links for source references.
- [Adding metadata](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-metadata.html): Learn how you can add metadata for documents in an Amazon Q Business Amazon S3 connector.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-user-management.html): Learn how Amazon Q Business crawls Amazon S3 ACL.
- [Error codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-error-codes.html): Learn how to interpret error codes in the Amazon S3 connector.

### [Salesforce Online](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-connector.html)

Learn how to connect Amazon Q Business with Salesforce Online.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-limitations.html): Describes the known limitations of the Salesforce Online connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html): An overview of the Salesforce Online connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-prereqs.html): Prerequisites for connecting Amazon Q Business with Salesforce Online.
- [Setting up Salesforce Online](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-credentials.html): Learn how to configure Salesforce Online for Amazon Q Business.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-console.html): Learn how to connect Amazon Q Business with Salesforce Online using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-api.html): Learn how to connect Amazon Q Business with Salesforce using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-user-management.html): Learn how Amazon Q Business crawls Salesforce ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-field-mappings.html): Learn what entities and field mappings the Salesforce Online connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Salesforce Online.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-error-codes.html): Learn how to interpret error codes in the Amazon Q Salesforce Online connector.

### [ServiceNow Online](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-connector.html)

Learn how to connect Amazon Q Business with ServiceNow Online.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-limitations.html): Describes the known limitations of the Amazon Q Business ServiceNow Online connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-overview.html): An overview of the ServiceNow Online connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-prereqs.html): Prerequisites for connecting Amazon Q Business with ServiceNow Online.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-console.html): Learn how to connect Amazon Q Business with ServiceNow Online using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-api.html): Learn how to connect Amazon Q Business with ServiceNow using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-cfn.html): Learn how to connect Amazon Q Business with ServiceNow using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-user-management.html): Learn how Amazon Q Business crawls ServiceNow ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-field-mappings.html): Learn what entities and field mappings the ServiceNow Online connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to ServiceNow Online.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-error-codes.html): Learn how to interpret error codes in the ServiceNow Online connector.

### [Slack](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-connector.html)

Learn how to connect Amazon Q Business with Slack.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-limitations.html): Describes the known limitations of the Amazon Q Business Slack connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-overview.html): An overview of the Slack connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-prereqs.html): Prerequisites for connecting Amazon Q Business with Slack.
- [Setting up Slack](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-credentials.html): Learn how to configure Slack for Amazon Q.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-console.html): Learn how to connect Amazon Q Business with Slack using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-api.html): Learn how to connect Amazon Q Business with Slack using API.
- [Using the CloudFormation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-cfn.html): Learn how to connect Amazon Q Business with Slack using AWS CloudFormation.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-user-management.html): Learn how Amazon Q Business crawls Slack ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Slack connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Slack.

### [Smartsheet](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-connector.html)

Learn how to connect Amazon Q Business with Smartsheet.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-limitations.html): Describes the known limitations of the Amazon Q Business Smartsheet connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-prereqs.html): Prerequisites for connecting Amazon Q Business with Smartsheet.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-console.html): Learn how to connect Amazon Q Business with Smartsheet using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-api.html): Learn how to connect Amazon Q Business with Smartsheet using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-user-management.html): Learn how Amazon Q Business crawls Smartsheet ACL.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Smartsheet.

### [Zendesk](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-connector.html)

Learn how to connect Amazon Q Business with Zendesk.

- [Known limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-limitations.html): Describes the known limitations of the Zendesk connector.
- [Overview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-overview.html): An overview of the Zendesk connector.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-prereqs.html): Prerequisites for connecting Amazon Q Business with Zendesk.
- [Setting up Zendesk](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-credentials.html): Learn how to configure Zendesk for Amazon Q Business.
- [Using the console](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-console.html): Learn how to connect Amazon Q Business with Zendesk using the console.
- [Using the API](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-api.html): Learn how to connect Amazon Q Business with Zendesk using API.
- [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-user-management.html): Learn how Amazon Q Business crawls Zendesk ACL.
- [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-field-mappings.html): Learn what entities and field mappings the Amazon Q Business Â Zendesk connector supports.
- [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-iam-role.html): Describes the IAM permissions needed for Amazon Q Business to connect to Zendesk.
- [Error Codes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-error-codes.html): Learn how to interpret error codes in the Zendesk connector.

### [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html)

Learn about how the Amazon Q Business User Store works.

- [Principal mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/principal-mapping.html): Learn about how the Amazon Q Business data source connector principal mapping works.
- [How the User Store works](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/principal-store-hiw.html): Each document in any data source has access control list (ACL) information inherently attached to it as metadata.

### [Using Amazon VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-vpc.html)

Learn about using VPC with an Amazon Q Business data source connector.

- [Configuring Amazon VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-vpc-steps.html): Learn how to configure a VPC for an Amazon Q Business data source connector.
- [Connecting to Amazon VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-vpc-setup.html): Learn how to connect a Amazon Q Business data source connector to a VPC.
- [Using Amazon VPC with Amazon S3](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-vpc-example-1.html): Learn how to connect an Amazon Q Business Amazon S3 data source connector to a VPC.
- [Troubleshooting data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/troubleshooting-data-sources.html): This section can help you fix issues with Amazon Q Business data source connectors.

### [Managing resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/managing-resources-data-sources.html)

Learn about the process for managing Amazon Q Business resources.

- [Managing Amazon Q Business indices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-native-retriever-actions.html): Learn about managing native indices for an Amazon Q Business application environment.
- [Managing Amazon Kendra indices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-kendra-retriever-actions.html): Learn how to manage a Amazon Kendra index for an Amazon Q Business application environment.
- [Managing data sources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-datasource-actions.html): To manage data source connectors, you can perform the following actions:
- [Deleting uploaded documents](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/delete-doc-upload.html): Learn how to manage documents uploaded directly into an Amazon Q Business application environment.
- [Tagging resources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging-ds.html): Learn about tagging Amazon Q Business resources.

### [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html)

Learn about Amazon Q Business enterprise controls and guardrails.

- [Key terms](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-concepts.html): Learn about key concept for Amazon Q Business guardrails.
- [Using global controls](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html): Learn about Amazon Q Business guardrails global controls.
- [Using topic-level controls](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-topic-controls.html): Learn about customizing Amazon Q Business guardrails topic controls.
- [Managing admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-management.html): Learn about managing Amazon Q Business admin controls and guardrails.

### [Response customization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/response-customization.html)

Learn how to customize response generation in Amazon Q Business.

- [Response customization settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/response-customization-components.html): Learn about the settings available for response customization in Amazon Q Business.
- [Managing response configurations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/response-customization-configurations.html): Learn how to create and manage response configurations in Amazon Q Business.

### [Data accessors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors.html)

Learn how to securely share your enterprise data with verified independent software vendors (ISVs) using Amazon Q Business.

- [Verified data accessors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors-list.html): See a list of verified software providers who are data accessors.
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors-prerequisites.html): See a list of verified software providers who are data accessors.
- [Add data accessor](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors-granting-permissions.html): After setting up your application environment and connecting your data source(s), Amazon Q Business begins indexing your enterprise data.
- [Completing the process](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors-external-setup.html): After you grant a software provider (ISV) data accessor permissions, you'll need to provide AWS or the ISV with the following configuration parameters.
- [Removing access](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors-removing-access.html): You can remove a data accessor's permissions to your Amazon Q index using the Amazon Q Business console or the Amazon Q Business API using the AWS SDK, REST API, or AWS CLI.

### [Amazon Q embedded](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/embed-amazon-q-business.html)

Learn how to embed the Amazon Q Business assistant within trusted websites.

- [Add your website as an allowed URL](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/add-website-as-allowed-url.html): Learn how to configure the allowed website(s) for your existing Amazon Q Business web experience.
- [Add Amazon Q embedded to your website](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/embed-web-experience.html): Learn how to embed your Amazon Q Business web experience on your website.
- [Remove your website as an allowed URL](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/remove-website-as-allowed-url.html): Learn how to remove the allowed website(s) for your existing Amazon Q Business web experience.

### [Integrations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/integrations.html)

Learn about integrations that extend Amazon Q Business capabilities to third-party enterprise tools.

### [Browser extensions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html)

The Amazon Q Business browser extension enhances your users' web browsing experience.

- [Configuring](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/configuring-browser-extension.html): After installation and authentication, your users can access Amazon Q while browsing the web.
- [Disabling, removing and blocking](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/removing-browser-extension.html): To disable the browser extension to your existing web experience, Admin users can use the Amazon Q Business console or the Amazon Q Business API, AWS SDK, or AWS CLI.
- [Using](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-browser-extension.html): The browser extension is available to Amazon Q Business users on Google Chrome, Mozilla Firefox, and Microsoft Edge browsers.

### [Slack](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack.html)

Learn how to enhance your users' Slack experience with Amazon Q Business.

- [Configuring Slack Integration](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-configuration.html): Learn how to configure the Amazon Q Business integration for Slack.
- [Using Slack App](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-using.html): Learn how to use the Amazon Q Business Slack App and its features.

### [Microsoft Teams](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/msteams.html)

Learn how to enhance your users' Microsoft Teams experience with Amazon Q Business.

- [Configuring Teams Integration](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/msteams-configuration.html): Learn how to configure the Amazon Q Business integration for Microsoft Teams.
- [Using Teams App](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/msteams-using.html): Learn how to install, login, and use the Amazon Q Business App in your Microsoft Teams organization.

### [Microsoft Outlook](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/integration-msoutlook.html)

Amazon Q Business can enhance your users' Microsoft Outlook (Outlook) experience by increasing their email productivity, bringing Amazon Q's AI-powered assistance directly into their daily email workflows.

- [Configuring](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/configuring-integration-msoutlook.html)
- [Using](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-integration-msoutlook.html)

### [Microsoft Word](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/integration-msword.html)

Amazon Q Business can enhance your users' Microsoft Word (Word) experience by increasing their productivity, bringing Amazon Q's AI-powered assistance directly into their daily document workflows.

- [Configuring](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/configuring-integration-msword.html)
- [Using](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-integration-msword.html)
- [IAM Roles and Trust Policy](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam.html): Learn about the IAM roles and trust policies required for Amazon Q Business integrations.

### [Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)

Learn about how your web experience users can create their own lightweight, purpose-built Amazon Q Apps within a broader application environment.

- [Prerequisites for Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps-prerequisites.html): Before using Amazon Q Apps, make sure that you do the following:
- [Managing Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps-manage.html): You can enable or disable the ability for web experience users to create and run their own Amazon Q Apps.
- [Creating Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps-web-experience.html): After you enable Amazon Q Apps in the console, web experience users can then start creating, running, and publishing their own purpose-built Q Apps.
- [Sharing Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-private-sharing.html): Amazon Q Apps allows you to privately share your Q Apps with specific users within your Q Business application environment.
- [Custom labels for Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html): Learn how to customize the label categories available for Q Apps.
- [Verified Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/verfied-apps-management.html): Understanding and managing Verified Amazon Q Apps.

### [Amazon Q Apps data collection](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/q-apps-forms.html)

Learn how to use data collection features in Amazon Q Apps to gather information from users through forms.

- [Data collection concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-forms-data-collection-concepts.html): Understand key concepts and features related to data collection in Amazon Q Apps.
- [Creating a new Q App with a data collection form](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-forms-creating-app.html): Learn how to create a new Amazon Q App with a data collection form to gather information from users.
- [Starting a new data collection](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-forms-starting-new-data-collection.html): Learn how to start a new data collection using the web experience or Amazon Q Apps APIs.
- [Using plugins in Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-plugins.html): Learn how to add plugins to Amazon Q Apps.

### [Document enrichments](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-document-enrichment.html)

Learn about Amazon Q Business custom document enrichment.

- [Document enrichment limitations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-limitations.html): Learn about Amazon Q Business document enrichment limitations.
- [How document enrichment works](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-hiw.html): Learn how Amazon Q Business custom document enrichment works.
- [Using basic operations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-basic-operations.html): Learn about using Amazon Q Business custom document enrichment basic operations.
- [Using Lambda functions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html): Learn about Amazon Q Business custom document enrichment Lambda functions.

### [Extracting semantic meaning from visuals](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html)

Learn how to use Amazon Q Business to extract semantic meaning from images and other visuals in your documents.

- [Guidelines and requirements](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/semantic-meaning-guidelines-and-requirements.html): The following are guidelines and requirements for extracting content from images:
- [Extracting content from visuals with data connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/enable-semantic-meanining-data-source.html): Steps to enable semantic meaning extraction from images when you add or update a data source
- [Extracting semantic meaning from audio and video content](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Audio-video-extraction.html): Amazon Q Business extracts semantic information from audio and video files, making data sources queryable and enhancing information retrieval.
- [Extracting content from visuals in a file](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/enable-semantic-meanining-file-upload.html): Steps to enable semantic meaning extraction from images in a file.
- [Downloading images to add to responses (API operations)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/semantic-meaning-adding-img-response.html): Steps to download images to add to chat responses when using the Amazon Q Business Chat and ChatSync APIs.
- [Relevancy tuning](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/relevancy-tuning.html): Relevancy tuning allows you to tune query responses based on when the document was created or updated or the data source contain the documents.

### [Metadata boosting (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/metadata-boosting.html)

Learn about using metadata to boost Amazon Q Business chat results.

- [Boosting types (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/boosting-parameters.html): Learn about document attribute boosting types in Amazon Q Business.
- [Configuring document attributes for boosting (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/configuring-boosting.html): Learn about configuring document attribute boosting in Amazon Q Business.
- [Enabling document attributes for search (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/boosting-searchable-attributes.html): Learn how to enable document attributes for search in Amazon Q Business.
- [Metadata controls](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/mapping-doc-attributes.html): Learn about mapping document attributes to index fields in Amazon Q Business.


## [Customizing a web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience.html)

- [Text Elements](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience-text-elements.html): Learn how to customize text elements in your Amazon Q Business web experience using the AWS Management Console and AWS CLI.
- [Visual Themes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience-themes.html): Learn how to customize the visual theme of your Amazon Q Business web experience using the AWS Management Console and AWS CLI.
- [Reference Materials](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience-themes-reference-materials.html): Supported root CSS variables and color considerations for Amazon Q Business web experience customization.


## [Configuring actions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/actions.html)

### [Quick plugin](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quicksight-plugin.html)

Learn about configuring a Quick plugin for Amazon Q Business.

- [Configuring the plugin](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quicksight-plugin-configuring-application.html): Configure an Amazon Q Business application to get insights from Quick.
- [Getting data insights from Amazon Quick answers](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quicksight-plugin-getting-data-insights.html): Describes how users can access insights from QuickSight in Amazon Q Business.
- [Pausing integration with Quick](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quicksight-plugin-pausing-integration.html): Pause the integration with Quick.

### [Built-in plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/built-in-plugin.html)

Built-in plugins have already been built by Amazon Q Business for common use cases across Jira, Salesforce, ServiceNow, and Zendesk.

- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/basic-plugins-prereqs.html)
- [Asana](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/asana-actions.html): Learn about configuring an Amazon Q Business Asana plugin.
- [Atlassian Confluence](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-actions.html): Learn about configuring an Amazon Q Business Atlassian Confluence plugin.
- [Google Calendar](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-actions.html): Learn about configuring an Amazon Q Business Google Calendar plugin.
- [Jira Cloud](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-actions.html): Learn about creating an Amazon Q Business Jira plugin.
- [Microsoft Exchange](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-actions.html): Configure an Amazon Q Business Microsoft Exchange plugin.
- [Microsoft Teams](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-actions.html): Configure an Amazon Q Business Microsoft Teams plugin.
- [PagerDuty Advance](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/pagerduty-actions.html): Learn about configuring an Amazon Q Business PagerDuty Advance plugin.
- [Salesforce](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-actions.html): Learn about creating an Amazon Q Business Salesforce plugin.
- [ServiceNow](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-actions.html): Learn about configuring an Amazon Q Business ServiceNow plugin.
- [Smartsheet](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-actions.html): Learn about configuring an Amazon Q Business Smartsheet plugin.
- [Zendesk Suite](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-actions.html): Learn about creating an Amazon Q Business Zendesk Suite plugin.
- [Jira (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-plugin.html): Learn about creating an Amazon Q Business Jira plugin.
- [Salesforce (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-plugin.html): Learn about managing an Amazon Q Business Salesforce plugin.
- [ServiceNow (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-plugin.html): Learn about configuring an Amazon Q Business ServiceNow plugin.
- [Zendesk (Legacy)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-plugin.html): Learn about creating an Amazon Q Business Zendesk plugin.
- [Using built-in plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-plugins.html): Learn how to use Amazon Q plugins.

### [Custom plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-plugin.html)

You can use the Amazon Q Business console or APIs to create custom plugins for your Amazon Q application.

- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-plugin-prereqs.html): Before you configure your Amazon Q custom plugin, you must ensure you have the following:
- [Service access roles](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-plugin-iam-role.html): To connect Amazon Q Business to third party applications that require authentication, you need to give the Amazon Q role permissions to access your Secrets Manager secret.
- [Defining OpenAPI schemas](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins-api-schema.html): Learn how to write API schemas for custom plugins in Amazon Q Business.
- [Best practices for OpenAPI schema definition](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins-api-schema-best-practices.html): While application programming interfaces (APIs) have traditionally been used by developers to integrate with external applications, today APIs are increasingly being used by generative AI-powered assistants, such as Amazon Q Business custom plugins.
- [Creating a custom plugin](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-plugin-create.html)
- [Using a custom plugin](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-custom-plugin.html): Once a custom plugin is deployed, end users can launch it from the menu icon in the Amazon Q Business web experience.
- [Managing plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugin-management.html): Learn about managing Amazon Q Business plugins.


## [Amazon Q Business features](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/features.html)

- [Filtering using document attributes and metadata](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/metadata-filtering.html): Learn about using document attributes and metadata to filter Amazon Q Business chat results.
- [Source attribution with citations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/source-attribution-citations.html): Learn about using source attributions with citations in Amazon Q Business.
- [Upload files and chat](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-chat-files.html): Learn how to upload files to a chat in Amazon Q Business.
- [Personalizing chat responses](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html): Learn how to use end user information in IAM Identity Center to personalize Amazon Q Business chat responses.
- [Quick prompts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quick-prompts.html): Learn about quick prompts in Amazon Q Business.
- [Hallucination mitigation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/hallucination-reduction.html): Learn about hallucination mitigation in Amazon Q Business.
- [Agentic RAG](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/agentic-rag.html): Learn about agentic retrieval augmented generation (RAG) in Amazon Q Business.


## [Amazon Q index for ISVs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv.html)

- [Key concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-key-concepts.html)
- [Prerequisites](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-prerequisites.html)
- [ISV information](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-info-to-provide.html): Before an independent software provider or vendor (ISV) can become a verified data accessor, they must provide either an Auth code or Trusted token issuer (TTI) configuration information to the Amazon Q Business team.
- [Getting access](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-getting-access.html): There are two non-mutually exclusive ways to get access to a customer's Amazon Q index:
- [Creating an Amazon Q index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-creating-index.html): We recommend creating one Amazon Q Business application environment per customer for better security and data segregation.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-troubleshooting.html): If ISVs encounter issues with accessing the Amazon Q index, consider the following.


## [Security](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security.html)

### [Data protection](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Q Business.

- [Data encryption for Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-encryption.html): Amazon Q Business supports encryption at rest using a customer supplied symmetric AWS KMS key when provided, or uses an AWS-owned AWS KMS key if no customer managed key is provided.
- [Data encryption for Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-encryption-qapps.html): Q Apps stores the following data:
- [Key management](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/key-management.html): Amazon Q Business encrypts the contents of your index using the following types of keys:
- [Cross-region inference](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html): Learn how to use cross-region inference to increase throughput and resilience of your chat requests.
- [Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html): Amazon Q Business does not use customer data for service improvement or for improving underlying LLMs.
- [Amazon VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/vpc-interface-endpoints.html): Learn how to use AWS PrivateLink to create a private connection between your VPC and Amazon Q Business.

### [Identity and access management](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html)

Learn how to authenticate requests and manage access to your Amazon Q Business resources.

- [How Amazon Q Business works with IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Q, learn what IAM features are available to use with Amazon Q.
- [Identity-based policy examples](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Q resources.
- [AWS managed policies](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Q Business and recent changes to those policies.
- [AWS managed policies for Q App](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam-awsmanpol-qapps.html): Learn about AWS managed policies for Amazon Q Apps and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html): How to use service-linked roles to give Amazon Q Business access to resources in your AWS account.
- [Using service-linked roles for Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html): How to use service-linked roles to give Amazon Q Apps access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Q and IAM.
- [Compliance validation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Using ACL Analyzer](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/acl-analyzer.html): Learn how to use the ACL Analyzer tool to verify document access permissions in Amazon Q.
- [Resilience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Q Business features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/infrastructure-security.html): Learn how Amazon Q Business isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/configuration-and-vulnerability-analysis.html): AWS handles basic security tasks like guest operating system (OS) and database patching, firewall configuration, and disaster recovery.
- [Security best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-best-practices.html): Amazon Q Business provides several security features to consider as you develop and implement your own security policies.


## [Monitoring](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/monitoring-overview.html)

- [Amazon Q Business CloudTrail logs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/logging-using-cloudtrail.html): Learn about logging Amazon Q Business with AWS CloudTrail.
- [Amazon Q Apps CloudTrail logs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/logging-qapps-using-cloudtrail.html): Learn about logging Amazon Q Apps with AWS CloudTrail.

### [CloudWatch metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/monitoring-cloudwatch.html)

You can monitor Amazon Q Business and Amazon Q Apps with Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

- [Creating a CloudWatch alarm](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alarms.html): Learn how to create a CloudWatch alarm
- [Amazon Q Business chat metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-metrics-chat.html): Learn about the chat metrics that Amazon Q Business sends to CloudWatch in real time.
- [Amazon Q Business API operation metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-metrics-api.html): Learn about the API operation metrics that Amazon Q Business sends to CloudWatch in real time.
- [Amazon Q Business index metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-metrics-index.html): Learn about the index metrics that Amazon Q Business sends to CloudWatch in real time.
- [Amazon Q Apps metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-metrics.html): Learn about the metrics that Amazon Q Apps sends to CloudWatch in real time.

### [Amazon Q Business CloudWatch Logs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/monitoring-cloudwatch-logs.html)

You can use Amazon CloudWatch Logs to deliver user conversations and response feedback in Amazon Q Business for you to analyze.

- [Log examples](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-log-examples.html): The following are examples of Amazon Q Business chat message and feedback logs in CloudWatch Logs.
- [Permissions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-logs-permissions.html): Learn about the required permissions for enabling CloudWatch Logs for Amazon Q Business
- [Enabling logging](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-logs-enable-logging.html): Learn how to enable Amazon Q Business user conversation logging.
- [Log query examples](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-logs-common-queries.html): Learn how to interact with conversation logs using queries.

### [Analytics dashboards](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/analytics-dashboard.html)

Learn about the dashboards in the Amazon Q Business console.

- [Viewing the analytics dashboards](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/analytics-dashboard-view.html): View the Amazon Q Business Analytics dashboard or Amazon Q Apps Analytics dashboard in Amazon Q Business.
- [Amazon Q Business Analytics dashboard metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/analytics-dashboard-metrics.html): Learn about the metrics available in the Amazon Q Business Analytics dashboard.
- [Amazon Q Apps Analytics dashboard metrics](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/q-apps-analytics-dashboard-metrics.html): Learn about the metrics available in the Amazon Q Apps Analytics dashbaord.


## [API reference](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/api-ref.html)

- [Creating an application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/application-api.html): Learn what APIs to use to create an Amazon Q Business application.
- [Creating an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/index-api.html): Learn what APIs to use to create an Amazon Q Business index.
- [Creating a retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/retriever-api.html): Learn what APIs to use to create an Amazon Q Business retriever.
- [Connecting a data source](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/datasource-apis.html): Learn what APIs to use to connect an Amazon Q Business data source.
- [Upload documents directly](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/document-upload-api.html): Learn what APIs to use to upload documents directly to an Amazon Q Business application.
- [GetDocumentContent Output Schema](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/document-content-schema.html): Schema for extracted text content returned by the GetDocumentContent API when using EXTRACTED output format.
- [Creating a web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-experience-api.html): Learn what APIs to use to create an Amazon Q Business web experience.
- [Chat and conversation management](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/conversation-api.html): Learn what APIs to use to manage Amazon Q Business chats and conversations.
- [User and group management](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/user-group-management-api.html): Learn what APIs to use to use to manage users and groups in an Amazon Q Business application.
- [Subscription management](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/subscription-management-api.html): Learn what APIs to use to use to manage subscriptions in an Amazon Q Business application.
- [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugin-apis.html): Learn what APIs to use to connect an Amazon Q Business data source.
- [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-api.html): Learn what APIs to use to manage admin controls and guardrails for a Amazon Q Business application.
- [User feedback](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/feedback-api.html): Learn what APIs to use to capture user feedback to Amazon Q Business responses using APIs.
