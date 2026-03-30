# Source: https://docs.aws.amazon.com/datazone/latest/userguide/llms.txt

# Amazon DataZone User Guide

- [What is Amazon DataZone?](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html)
- [Amazon SageMaker and when to use Amazon SageMaker vs Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/sagemaker-datazone.html)
- [Terminology and concepts](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-concepts.html)
- [What is new?](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-new-in-datazone.html)
- [Supported Regions](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-supported-regions.html)
- [Built-in blueprints](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-blueprints.html)
- [Events and notifications](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-events-and-notifications.html)
- [Troubleshooting](https://docs.aws.amazon.com/datazone/latest/userguide/troubleshooting-datazone.html)
- [Quotas](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-limits.html)
- [Document history](https://docs.aws.amazon.com/datazone/latest/userguide/doc-history.html)

## [Setting up](https://docs.aws.amazon.com/datazone/latest/userguide/setting-up.html)

- [Sign up for an AWS account](https://docs.aws.amazon.com/datazone/latest/userguide/setting-up-aws-sign-up.html): If you do not have an AWS account, complete the following steps to create one.
- [Configure the IAM permissions required to use the management console](https://docs.aws.amazon.com/datazone/latest/userguide/create-iam-roles.html): In order to access and conï¬gure your Amazon DataZone domains, blueprints, and users, and to create the Amazon DataZone data portal, you must use the Amazon DataZone management console.
- [Configure the IAM permissions required to use the data portal](https://docs.aws.amazon.com/datazone/latest/userguide/data-portal-permissions.html): Amazon DataZone data portal (outside the AWS Management Console) is a browser-based web application where users can go to catalog, discover, govern, share, and analyze data in a self-service fashion.
- [Setting up AWS IAM Identity Center for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/sso-setup.html)


## [Getting started](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html)

- [Quickstart guide with sample AWS Glue data](https://docs.aws.amazon.com/datazone/latest/userguide/quickstart-glue.html): Complete the following quickstart steps to run through the complete data producer and data consumer workflows in Amazon DataZone with sample AWS Glue data.
- [Quickstart guide with sample Amazon Redshift data](https://docs.aws.amazon.com/datazone/latest/userguide/quickstart-rs.html): Complete the following quickstart steps to run through the complete data producer and data consumer workflows in Amazon DataZone with sample Amazon Redshift data.
- [Sample scripts for common tasks](https://docs.aws.amazon.com/datazone/latest/userguide/quickstart-apis.html): You can access Amazon DataZone via the management portal or the Amazon DataZone data portal, or programmatically by using the Amazon DataZone HTTPS API, which lets you issue HTTPS requests directly to the service.


## [Domains and user access](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-domains-users.html)

- [Create domains](https://docs.aws.amazon.com/datazone/latest/userguide/create-domain.html)
- [Edit domains](https://docs.aws.amazon.com/datazone/latest/userguide/edit-domain.html): In Amazon DataZone, a domain is an organizing entity for connecting together your assets, users, and their projects.
- [Delete domains](https://docs.aws.amazon.com/datazone/latest/userguide/delete-domain.html): In Amazon DataZone, a domain is an organizing entity for connecting together your assets, users, and their projects.
- [Enable IAM Identity Center for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/enable-IAM-identity-center-for-datazone.html)
- [Disable IAM Identity Center for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/disable-IAM-identity-center-for-datazone.html): Disabling AWS IAM Identity Center for an Amazon DataZone domain will remove access for all SSO users.
- [Manage users in the Amazon DataZone console](https://docs.aws.amazon.com/datazone/latest/userguide/user-management-console.html): Your users can access the Amazon DataZone data portal by using either their AWS credentials or single sign-on (SSO) credentials.
- [Manage user permissions in the data portal](https://docs.aws.amazon.com/datazone/latest/userguide/user-management-portal.html): You can use the Amazon DataZone management portal to configure authentication for IAM users and roles, SSO users and groups, and SAML users.
- [Restricting access to Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/user-management-portal-restricting-programmatic-access.html): Restricting programmatic access to Amazon DataZone - for IAM users or roles, making programmatic API calls, access can be restricted via IAM policies.
- [Upgrade Amazon DataZone domains to Amazon SageMaker unified domains](https://docs.aws.amazon.com/datazone/latest/userguide/upgrade-domain.html)


## [Domain units and authorization policies](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-domain-units.html)

- [Create domain units](https://docs.aws.amazon.com/datazone/latest/userguide/create-domain-unit.html): In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Edit domain units](https://docs.aws.amazon.com/datazone/latest/userguide/edit-domain-unit.html): In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Delete domain units](https://docs.aws.amazon.com/datazone/latest/userguide/delete-domain-unit.html): In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Manage domain unit owners](https://docs.aws.amazon.com/datazone/latest/userguide/add-domain-unit-owners.html): In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams.

### [Assign authorization policies to users and groups within a domain unit](https://docs.aws.amazon.com/datazone/latest/userguide/assign-authorization-policies-to-users-in-domain-unit.html)

In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams.

- [Project membership policy in the hierarchy of domain units in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/projectmembershippolicy.html): The project membership policy defines the individuals or groups that are eligible to be added as members to projects within a domain unit.
- [Assign authorization policies to projects within a domain unit](https://docs.aws.amazon.com/datazone/latest/userguide/assign-authorization-policies-to-projects-in-domain-unit.html): In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams.
- [Assign authorization policies within blueprint configurations](https://docs.aws.amazon.com/datazone/latest/userguide/assign-authorization-policies-in-blueprint-config.html): Another way to use the authorization mechanism in Amazon DataZone is to apply authorization policies to projects and domain unit owners within Amazon DataZone blueprint configurations.


## [Custom AWS service blueprints](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-custom-blueprint.html)

- [Enable a custom AWS service blueprint](https://docs.aws.amazon.com/datazone/latest/userguide/enable-custom-blueprint.html): Complete the following procedure to enable a custom AWS service blueprint in your domain.
- [Create an environment using a custom AWS service blueprint](https://docs.aws.amazon.com/datazone/latest/userguide/create-custom-environment.html): Complete the following procedure to create an environment using a custom AWS service blueprint.
- [Create actions in a custom AWS service environment](https://docs.aws.amazon.com/datazone/latest/userguide/configure-custom-environment-actions.html): Complete the following procedure to create actions in a custom AWS service environment.
- [Add project members to a custom AWS service environment](https://docs.aws.amazon.com/datazone/latest/userguide/add-project-members-to-custom-environment.html): Complete the following procedure to add project members to an AWS service environment.
- [Configure a data source in an AWS service environment](https://docs.aws.amazon.com/datazone/latest/userguide/configure-data-source-in-custom-environment.html): Complete the following procedure to configure a data source in an AWS service environment.
- [Configure a subscription target in an AWS service environment](https://docs.aws.amazon.com/datazone/latest/userguide/configure-subscription-target-in-custom-environment.html): Complete the following procedure to configure a subscription target in an AWS service environment.


## [Associated accounts](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-associated-accounts.html)

- [Add Amazon SageMaker as a trusted service in the associated AWS account](https://docs.aws.amazon.com/datazone/latest/userguide/add-sagemaker-as-trusted-service-associate.html): If you've enabled the Amazon SageMaker blueprint, you must also add SageMaker as one of the trusted services within Amazon DataZone.
- [Reject an account association request from an Amazon DataZone domain](https://docs.aws.amazon.com/datazone/latest/userguide/reject-invitation-to-associate.html): To reject an association request in the Amazon DataZone management console from an Amazon DataZone domain, you must assume an IAM role in the account with administrative permissions. to obtain the minimum permissions.
- [Remove an associated account in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/remove-associated-account.html): To remove an associated AWS account in the Amazon DataZone management console, you must assume an IAM role in the account with administrative permissions. to obtain the minimum permissions.


## [Data catalog](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-business-catalog.html)

- [Create a business glossary](https://docs.aws.amazon.com/datazone/latest/userguide/create-maintain-business-glossary.html): In Amazon DataZone, a business glossary is a collection of business terms (words) that may be associated with assets (data).
- [Edit a business glossary](https://docs.aws.amazon.com/datazone/latest/userguide/edit-business-glossary.html): In Amazon DataZone, a business glossary is a collection of business terms (words) that may be associated with assets (data).
- [Delete a business glossary](https://docs.aws.amazon.com/datazone/latest/userguide/delete-business-glossary.html): In Amazon DataZone, a business glossary is a collection of business terms (words) that may be associated with assets (data).
- [Create a term in a glossary](https://docs.aws.amazon.com/datazone/latest/userguide/create-maintain-term.html): In Amazon DataZone, a business glossary is a collection of business terms that may be associated with assets (data).
- [Edit a term in a glossary](https://docs.aws.amazon.com/datazone/latest/userguide/edit-term.html): In Amazon DataZone, a business glossary is a collection of business terms that may be associated with assets (data).
- [Delete a term in a glossary](https://docs.aws.amazon.com/datazone/latest/userguide/delete-term.html): In Amazon DataZone, a business glossary is a collection of business terms that may be associated with assets (data).
- [Create a metadata form](https://docs.aws.amazon.com/datazone/latest/userguide/create-metadata-form.html): In Amazon DataZone, metadata forms are simple forms to augment additional business context to the asset metadata in the catalog.
- [Edit a metadata form](https://docs.aws.amazon.com/datazone/latest/userguide/edit-metadata-form.html): In Amazon DataZone, metadata forms are simple forms to augment additional business context to the asset metadata in the catalog.
- [Delete a metadata form](https://docs.aws.amazon.com/datazone/latest/userguide/delete-metadata-form.html): In Amazon DataZone, metadata forms are simple forms to augment additional business context to the asset metadata in the catalog.
- [Create a field in a metadata form](https://docs.aws.amazon.com/datazone/latest/userguide/create-field-in-metadata-form.html): In Amazon DataZone, metadata forms are simple forms to augment additional business context to the asset metadata in the catalog.
- [Edit a field in a metadata form](https://docs.aws.amazon.com/datazone/latest/userguide/edit-field-in-metadata-form.html): In Amazon DataZone, metadata forms are simple forms to augment additional business context to the asset metadata in the catalog.
- [Delete a field in a metadata form](https://docs.aws.amazon.com/datazone/latest/userguide/delete-field-in-metadata-form.html): In Amazon DataZone, metadata forms are simple forms to augment additional business context to the asset metadata in the catalog.


## [Projects and environments](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-projects.html)

- [Create an environment profile](https://docs.aws.amazon.com/datazone/latest/userguide/create-environment-profile.html): In Amazon DataZone, an environment proï¬le is a template that you can use to create environments.
- [Edit an environment profile](https://docs.aws.amazon.com/datazone/latest/userguide/edit-environment-profile.html): In Amazon DataZone, an environment proï¬le is a template that you can use to create environments.
- [Delete an environment profile](https://docs.aws.amazon.com/datazone/latest/userguide/delete-environment-profile.html): In Amazon DataZone, an environment proï¬le is a template that you can use to create environments.
- [Create a new environment](https://docs.aws.amazon.com/datazone/latest/userguide/create-new-environment.html): In Amazon DataZone projects, environments are collections of configured resources (for example, an Amazon S3 bucket, an AWS Glue database, or an Amazon Athena workgroup), with a given set of IAM principals (environment user roles) with assigned owner or contributor permissions who can operate on those resources.
- [Edit an environment](https://docs.aws.amazon.com/datazone/latest/userguide/edit-environment.html): In Amazon DataZone projects, environments are collections of configured resources (for example, an Amazon S3 bucket, an AWS Glue database, or an Amazon Athena workgroup), with a given set of IAM principals (with assigned contributor permissions) who can operate on those resources.
- [Delete an environment](https://docs.aws.amazon.com/datazone/latest/userguide/delete-environment.html): In Amazon DataZone projects, environments are collections of configured resources (for example, an Amazon S3 bucket, an AWS Glue database, or an Amazon Athena workgroup), with a given set of IAM principals (with assigned contributor permissions) who can operate on those resources.
- [Create a new project](https://docs.aws.amazon.com/datazone/latest/userguide/create-new-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog.
- [Edit project](https://docs.aws.amazon.com/datazone/latest/userguide/edit-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog.
- [Move project to a different domain unit](https://docs.aws.amazon.com/datazone/latest/userguide/move-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog.
- [Delete project](https://docs.aws.amazon.com/datazone/latest/userguide/delete-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and/or consuming data assets in the Amazon DataZone catalog.
- [Leave project](https://docs.aws.amazon.com/datazone/latest/userguide/leave-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog.
- [Add members to a project](https://docs.aws.amazon.com/datazone/latest/userguide/add-members-to-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog.
- [Remove members from a project](https://docs.aws.amazon.com/datazone/latest/userguide/remove-members-from-project.html): In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog.


## [Data inventory and publishing](https://docs.aws.amazon.com/datazone/latest/userguide/publishing-data.html)

### [Configure Lake Formation permissions for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/lake-formation-permissions-for-datazone.html)

When you create an environment using the built-in data lake blueprint (DefaultDataLake), an AWS Glue database is added in Amazon DataZone as part of this environment's creation process.

- [Amazon DataZone integration with AWS Lake Formation hybrid mode](https://docs.aws.amazon.com/datazone/latest/userguide/hybrid-mode.html): Amazon DataZone is integrated with AWS Lake Formation hybrid mode.
- [Create custom asset types](https://docs.aws.amazon.com/datazone/latest/userguide/create-asset-types.html): In Amazon DataZone, assets represent specific types of data resources such as database tables, dashboards, or machine learning models.
- [Create and run a data source for the AWS Glue Data Catalog](https://docs.aws.amazon.com/datazone/latest/userguide/create-glue-data-source.html): In Amazon DataZone, you can create an AWS Glue Data Catalog data source in order to import technical metadata of database tables from AWS Glue.
- [Create and run a data source for Amazon Redshift](https://docs.aws.amazon.com/datazone/latest/userguide/create-redshift-data-source.html): In Amazon DataZone, you can create an Amazon Redshift data source in order to import technical metadata of database tables and views from the Amazon Redshift data warehouse.
- [Edit a data source](https://docs.aws.amazon.com/datazone/latest/userguide/edit-data-source.html): After you create an Amazon DataZone data source, you can modify it at any time to change the source details or the data selection criteria.
- [Delete a data source](https://docs.aws.amazon.com/datazone/latest/userguide/delete-data-source.html): After you create an Amazon DataZone data source, you can modify it at any time to change the source details or the data selection criteria.
- [Publish assets to the catalog from the project inventory](https://docs.aws.amazon.com/datazone/latest/userguide/publishing-data-asset.html): You can publish Amazon DataZone assets and their metadata from project inventories into the Amazon DataZone catalog.
- [Manage inventory and curate assets](https://docs.aws.amazon.com/datazone/latest/userguide/update-metadata.html): In order to use Amazon DataZone to catalog your data, you must first bring your data (assets) as inventory of your project in Amazon DataZone.
- [Manually create an asset](https://docs.aws.amazon.com/datazone/latest/userguide/create-data-asset-manually.html): In Amazon DataZone, an asset is an entity that presents a single physical data object (for example, a table, a dashboard, a file) or virtual data object (for example, a view).
- [Unpublish an asset from the catalog](https://docs.aws.amazon.com/datazone/latest/userguide/archive-data-asset.html): When you unpublish an Amazon DataZone asset from the catalog, it no longer appears in global search results.
- [Delete an asset](https://docs.aws.amazon.com/datazone/latest/userguide/delete-data-asset.html): When you no longer need an asset in Amazon DataZone, you can permanently delete it.
- [Manually start a data source run](https://docs.aws.amazon.com/datazone/latest/userguide/manually-start-data-source-run.html): When you run a data source, Amazon DataZone pulls all any new or modified metadata from the source and updates the associated assets in the inventory.
- [Asset versioning](https://docs.aws.amazon.com/datazone/latest/userguide/asset-versioning.html): Amazon DataZone increments the revision of an asset when you edit its business or technical metadata.
- [Data quality in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-data-quality.html): Data quality metrics in Amazon DataZone help you understand the different quality metrics such as completeness, timeliness, and accuracy of your data sources.
- [Using machine learning and generative AI in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/autodoc.html)
- [Data lineage in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-data-lineage.html): Data lineage in Amazon DataZone is an OpenLineage-compatible feature that can help you to capture and visualize lineage events, from OpenLineage-enabled systems or through APIs, to trace data origins, track transformations, and view cross-organizational data consumption.
- [Metadata enforcement rules for publishing](https://docs.aws.amazon.com/datazone/latest/userguide/metadata-rules-publishing.html): The metadata enforcement rules for publishing in Amazon DataZone strengthen data governance by enabling domain unit owners to establish clear metadata requirements for data producers, streamlining access requests and enhancing data governance.


## [Data products](https://docs.aws.amazon.com/datazone/latest/userguide/working-with-data-products.html)

- [Create new data products](https://docs.aws.amazon.com/datazone/latest/userguide/create-new-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Publish data products](https://docs.aws.amazon.com/datazone/latest/userguide/publish-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Edit data products](https://docs.aws.amazon.com/datazone/latest/userguide/edit-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Unpublish data products](https://docs.aws.amazon.com/datazone/latest/userguide/unpublish-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Delete data products](https://docs.aws.amazon.com/datazone/latest/userguide/delete-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Subscribe to a data product](https://docs.aws.amazon.com/datazone/latest/userguide/subscribe-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Review a subscription request and grant a subscription to a data product](https://docs.aws.amazon.com/datazone/latest/userguide/review-grant-subscription-to-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.
- [Republish data products](https://docs.aws.amazon.com/datazone/latest/userguide/republish-data-product.html): Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases.


## [Data discovery, subscription, and consumption](https://docs.aws.amazon.com/datazone/latest/userguide/discover-subscribe-consume-data.html)

- [Search for and view assets in the catalog](https://docs.aws.amazon.com/datazone/latest/userguide/search-for-data.html): Amazon DataZone provides a streamlined way to search for data.
- [Request subscription to assets](https://docs.aws.amazon.com/datazone/latest/userguide/subscribe-to-data-assets-managed-by-datazone.html): Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone catalog.
- [Approve or reject a subscription request](https://docs.aws.amazon.com/datazone/latest/userguide/approve-reject-subscription-request.html): Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone catalog.
- [Revoke an existing subscription](https://docs.aws.amazon.com/datazone/latest/userguide/revoke-subscription.html): Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone catalog.
- [Cancel a subscription request](https://docs.aws.amazon.com/datazone/latest/userguide/cancel-subscription-request.html): Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone catalog.
- [Unsubscribe from an asset](https://docs.aws.amazon.com/datazone/latest/userguide/unsubscribe-from-subscription.html): Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone catalog.
- [Using existing IAM roles to fulfill Amazon DataZone subscriptions](https://docs.aws.amazon.com/datazone/latest/userguide/use-your-own-role.html): In the current release, Amazon DataZone supports you using your existing IAM roles to get access to the data.
- [Grant access to managed AWS Glue Data Catalog assets](https://docs.aws.amazon.com/datazone/latest/userguide/grant-access-to-glue-asset.html): In Amazon DataZone, subscription requests and approved or granted subscriptions for read access to the assets are managed by asset owners.
- [Grant access to managed Amazon Redshift assets](https://docs.aws.amazon.com/datazone/latest/userguide/grant-access-to-redshift-asset.html): When a subscription to an Amazon Redshift table or view is approved, Amazon DataZone can automatically add the subscribed asset to all the data warehouse environments within the project, so that members of the project can query the data using the Amazon Redshift query editor link within their environments.
- [Grant access for approved subscriptions to unmanaged assets](https://docs.aws.amazon.com/datazone/latest/userguide/grant-access-to-unmanaged-asset.html): In Amazon DataZone, subscription requests and approved or granted subscriptions for read access to the assets are managed by asset owners.
- [Query data in Amazon Athena or Amazon Redshift](https://docs.aws.amazon.com/datazone/latest/userguide/query-athena-with-deep-link-in-project.html): In Amazon DataZone, once a subscriber has access to an asset in the catalog, they can consume it (query and analyze) using Amazon Athena or Amazon Redshift query editor v2.
- [Metadata enforcement rules for subscription requests](https://docs.aws.amazon.com/datazone/latest/userguide/metadata-rules.html): The metadata enforcement rules for subscription requests feature in Amazon DataZone strengthens data governance by enabling domain unit owners to establish clear metadata requirements for data consumers, streamlining access requests and enhancing data governance.
- [Analyze your subscribed data with external analytics applications via JDBC connection](https://docs.aws.amazon.com/datazone/latest/userguide/query-with-jdbc.html): Amazon DataZone enables data consumers to easily locate and subscribe to data from multiple sources within a single project and analyze this data using Amazon Athena, Amazon Redshift Query Editor, and Amazon SageMaker.


## [Fine-grained access control to data](https://docs.aws.amazon.com/datazone/latest/userguide/fine-grained-access-control.html)

- [Create row filters](https://docs.aws.amazon.com/datazone/latest/userguide/create-row-filter.html): Amazon DataZone allows you to create row filters that you can use when approving subscriptions to make sure that the subscriber can only access rows of data as defined in the row filters.
- [Create column filters](https://docs.aws.amazon.com/datazone/latest/userguide/create-column-filter.html): Amazon DataZone enables you to create column filters that you can use when approving subscriptions to make sure that the subscriber can only access columns of data as defined in the column filters.
- [Delete row or column filters](https://docs.aws.amazon.com/datazone/latest/userguide/delete-row-column-filter.html): To delete a row or a column filter, follow the steps below:
- [Edit row or column filters](https://docs.aws.amazon.com/datazone/latest/userguide/edit-row-column-filter.html): To edit a row or a column filter, follow the steps below:
- [Grant access with filters](https://docs.aws.amazon.com/datazone/latest/userguide/grant-access-with-filters.html): Amazon DataZone enables fine-grained access control by translating the defined row and column filters into appropriate grants for AWS Lake Formation and Amazon Redshift.


## [Security](https://docs.aws.amazon.com/datazone/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/datazone/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon DataZone.

- [Data encryption at rest for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/encryption-rest-datazone.html): Encryption of data at rest by default helps reduce the operational overhead and complexity involved in protecting sensitive data.
- [Using Interface VPC Endpoints for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-vpc.html): If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a connection between your Amazon VPC and Amazon DataZone.
- [Authorization in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/security-authorization.html): Learn about Authorization in Amazon DataZone

### [Controlling access](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam.html)

Control access to your Amazon DataZone resources by using AWS Identity and Access Management (IAM).

### [AWS managed policies](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol.html)

Learn about AWS managed policies for Amazon DataZone and recent changes to those policies.

- [AmazonDataZoneFullAccess](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneFullAccess.html): You can attach the AmazonDataZoneFullAccess policy to your IAM identities.
- [AmazonDataZoneFullUserAccess](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneFullUserAccess.html): This policy grants full access to Amazon DataZone, but it doesn't allow the management of domains, users, or associated accounts.
- [AmazonDataZoneEnvironmentRolePermissionsBoundary](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneEnvironmentRolePermissionsBoundary.html)
- [AmazonDataZoneRedshiftGlueProvisioningPolicy](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneRedshiftGlueProvisioningPolicy.html): The AmazonDataZoneRedshiftGlueProvisioningPolicy policy grants Amazon DataZone the permissions required to interoperate with AWS Glue and Amazon Redshift.
- [AmazonDataZoneGlueManageAccessRolePolicy](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneGlueManageAccessRolePolicy.html): This policy gives Amazon DataZone permissions to publish AWS Glue data to the catalog.
- [AmazonDataZoneRedshiftManageAccessRolePolicy](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneRedshiftManageAccessRolePolicy.html): This policy gives Amazon DataZone permissions to publish Amazon Redshift data to the catalog.
- [AmazonDataZoneDomainExecutionRolePolicy](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneDomainExecutionRolePolicy.html): This is the default policy for the Amazon DataZone DomainExecutionRole service role.
- [AmazonDataZoneSageMakerProvisioningRolePolicy](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneSageMakerProvisioningRolePolicy.html): The AmazonDataZoneSageMakerProvisioningRolePolicy policy grants Amazon DataZone the permissions required to interoperate with Amazon SageMaker.
- [AmazonDataZoneSageMakerManageAccessRolePolicy](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneSageMakerManageAccessRolePolicy.html): This policy gives Amazon DataZone permissions to publish Amazon SageMaker assets to the catalog.
- [AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary.html)
- [Policy updates](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-updates.html): View details about updates to AWS managed policies for Amazon DataZone since this service began tracking these changes.

### [IAM roles for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/iam-roles-datazone.html)

- [AmazonDataZoneProvisioningRole-<domainAccountId>](https://docs.aws.amazon.com/datazone/latest/userguide/bootstraprole.html): The AmazonDataZoneProvisioningRole-<domainAccountId> has the AmazonDataZoneRedshiftGlueProvisioningPolicy attached.
- [AmazonDataZoneDomainExecutionRole](https://docs.aws.amazon.com/datazone/latest/userguide/AmazonDataZoneDomainExecutionRole.html): The AmazonDataZoneDomainExecutionRole has the AWS managed policy AmazonDataZoneDomainExecutionRolePolicy attached.
- [AmazonDataZoneGlueAccess-<region>-<domainId>](https://docs.aws.amazon.com/datazone/latest/userguide/glue-manage-access-role.html): The AmazonDataZoneGlueAccess-<region>-<domainId> role has the AmazonDataZoneGlueManageAccessRolePolicy attached.
- [AmazonDataZoneRedshiftAccess-<region>-<domainId>](https://docs.aws.amazon.com/datazone/latest/userguide/redshift-manage-access-role.html): The AmazonDataZoneRedshiftAccess-<region>-<domainId> role has the AmazonDataZoneRedshiftManageAccessRolePolicy attached.
- [AmazonDataZoneS3Manage-<region>-<domainId>](https://docs.aws.amazon.com/datazone/latest/userguide/AmazonDataZoneS3Manage.html): The AmazonDataZoneS3Manage-<region>-<domainId> is used when Amazon DataZone calls AWS Lake Formation to register an Amazon Simple Storage Service (Amazon S3) location.
- [AmazonDataZoneSageMakerManageAccessRole-<region>-<domainId>](https://docs.aws.amazon.com/datazone/latest/userguide/AmazonDataZoneSageMakerManageAccessRole.html): The AmazonDataZoneSageMakerManageAccessRole role has the AmazonDataZoneSageMakerAccess, the AmazonDataZoneRedshiftManageAccessRolePolicy, and the AmazonDataZoneGlueManageAccessRolePolicy attached.
- [AmazonDataZoneSageMakerProvisioningRolePolicyRole-<domainAccountId>](https://docs.aws.amazon.com/datazone/latest/userguide/AmazonDataZoneSageMakerProvisioningRolePolicyRole.html): The AmazonDataZoneSageMakerProvisioningRolePolicyRole role has the AmazonDataZoneSageMakerProvisioningRolePolicy and the AmazonDataZoneRedshiftGlueProvisioningPolicy attached.
- [Temporary Credentials](https://docs.aws.amazon.com/datazone/latest/userguide/temporarycredentials.html): Some AWS services don't work when you sign in using temporary credentials.
- [Principal permissions](https://docs.aws.amazon.com/datazone/latest/userguide/Principalpermissions.html): When you use an IAM user or role to perform actions in AWS, you are considered a principal.
- [Compliance validation](https://docs.aws.amazon.com/datazone/latest/userguide/compliance-validation.html): Learn what AWS services are in the scope of a specific compliance program.
- [Security Best Practices](https://docs.aws.amazon.com/datazone/latest/userguide/security-best-practices.html): Amazon DataZone provides a number of security features to consider as you develop and implement your own security policies.
- [Resilience](https://docs.aws.amazon.com/datazone/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon DataZone features for data resiliency.
- [Infrastructure Security in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/infrastructure-security.html): Learn how Amazon DataZone isolates service traffic.
- [Cross-service confused deputy prevention in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/crossservicedeputy.html): Cross-service confused deputy prevention in Amazon DataZone
- [Configuration and vulnerability analysis in for Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/vulnerability-analysis-and-management.html): Learn what configuration and vulnerability analysis is for Amazon DataZone.
- [Domains to add to your allow list](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-networking.html): Learn about Amazon DataZone networking.


## [Monitoring](https://docs.aws.amazon.com/datazone/latest/userguide/monitoring-overview.html)

- [Monitoring events](https://docs.aws.amazon.com/datazone/latest/userguide/monitoring-events.html): You can monitor Amazon DataZone events in EventBridge, which delivers a stream of real-time data from your own applications, software-as-a-service (SaaS) applications, and AWS services.
- [CloudTrail logs](https://docs.aws.amazon.com/datazone/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon DataZone with AWS CloudTrail.
