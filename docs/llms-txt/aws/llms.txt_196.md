# Source: https://docs.aws.amazon.com/clouddirectory/latest/developerguide/llms.txt

# Amazon Cloud Directory Developer Guide

> Amazon Cloud Directory is a specialized graph-based directory store that provides a foundational building block for developers.

- [What Is Amazon Cloud Directory?](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
- [Amazon Cloud Directory availability change](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/cloud-directory-availability-change.html)
- [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html)
- [Compliance](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/compliance.html)
- [Using the Cloud Directory APIs](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/using_api.html)
- [Limits](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html)
- [Cloud Directory Resources](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/resources.html)
- [Document History](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/document_history.html)
- [AWS Glossary](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/glossary.html)

## [Getting Started](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/getting_started.html)

- [Create a Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/getting_started_create_schema.html): Learn how to create a schema in Amazon Cloud Directory.
- [Create a Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/getting_started_create_directory.html): Creating an Amazon Cloud Directory.
- [Using Cloud Directory Interface VPC Endpoints](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/getting_started_using_vpc_endpoints.html): If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and Cloud Directory.


## [Key Cloud Directory Concepts](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts.html)

- [Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_schema.html): A schema is a collection of facets that define what objects can be created in a directory and how they are organized.
- [Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html): A directory is a schema-based data store that contains specific types of objects organized in a multi-hierarchical structure (see for more details).
- [Directory Structure](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html): Data in a directory is structured hierarchically in a tree pattern consisting of nodes, leaf nodes, and links between the nodes, as shown in the following illustration.


## [Schemas](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas.html)

- [Schema Lifecycle](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_lifecycle.html): Cloud Directory offers a schema lifecycle to help with the development of schemas.
- [Facets](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_whatarefacets.html): Facets are the most basic abstraction within a schema.
- [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html): Cloud Directory offers the updating of existing schema attributes and facets to help integrate your applications with AWS provided services.
- [Managed Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_managed.html): Cloud Directory makes it easy for you to rapidly develop applications by using a managed schema.
- [Sample Schemas](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_sampleschemastopic.html): Cloud Directory comes ready with sample schemas for Organizations, Persons, and Devices.
- [Custom Schemas](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_customschematopic.html): The first step in creating a custom schema is to define exactly what fields you must index.
- [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html): Amazon Cloud Directory facets contain attributes.
- [Attribute Rules](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributerules.html): Rules describe permissible values of an attribute type and constrain the values that are allowed for any particular attribute.
- [Format Specification](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_jsonformat.html): A Cloud Directory schema adds structure to the data in your data directories.


## [Directory Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects.html)

- [Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html): A link is a directed edge between two objects that define a relationship.
- [Range Filters](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_range_filters.html): Several Cloud Directory list APIs allow specifying a filter in the form of a range.
- [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html): Objects in a directory can be accessed either by path or by objectIdentifier.
- [Consistency Levels](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_consistency_levels.html): Amazon Cloud Directory is a distributed directory store.


## [Indexing and Search](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.html)

- [Index Lifecycle](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search_lifecycle.html): You can use the following API calls to help with the development lifecycle of indexes.
- [Facet-Based Indexing](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search_facet.html): With facet-based indexing and search, you can optimize your directory searches by searching only a subset of your directory.
- [Unique vs Nonunique Indexes](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search_unique.html): Unique indexes differ from nonunique indexes in enforcing uniqueness of the indexed attribute values for objects that are attached to the index.


## [How To...](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to.html)

### [Manage Your Directories](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_directory.html)

Learn how to extend the reach of your Cloud Directory.

- [Create Your Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_directory_create.html): Learn how to create an Amazon Cloud Directory.
- [Delete Your Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_directory_delete.html): Learn how to delete a directory in Amazon Cloud Directory.
- [Disable Your Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_directory_disable.html): Disabling an Amazon Cloud Directory.
- [Enable Your Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_directory_enable.html): Enabling an Amazon Cloud Directory.

### [Manage Your Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema.html)

Learn how to secure your Cloud Directory.

- [Create Your Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema_create.html): Learn how to create a schema in Amazon Cloud Directory.
- [Delete a Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema_delete.html): Learn how to delete a schema.
- [Download a Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema_download.html): Learn how to download a schema.
- [Publish a Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema_publish.html): Use the following procedure to publish a schema in Cloud Directory.
- [Update Your Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema_update.html): Learn how to update a schema.
- [Upgrade Your Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/how_to_manage_schema_upgrade.html): Learn how to upgrade your schema.


## [Security](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/iam_auth_access.html)

Create permissions that specify which actions a user or group in your AWS account can perform and on which Cloud Directory resources.

- [Overview of Managing Access](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/iam_auth_access_accesscontrol_overview.html): Every AWS resource is owned by an AWS account, and permissions to create or access the resources are governed by permissions policies.
- [Using Identity-Based Policies (IAM Policies)](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/iam_auth_access_accesscontrol_identitybased.html): This topic provides examples of identity-based policies in which an account administrator can attach permissions policies to IAM identities (that is, users, groups, and roles).
- [Amazon Cloud Directory API Permissions Reference](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/iam_auth_access_usingwith_iam_resourcepermissions.html): Create fine-grained permissions that specify which Amazon Cloud Directory resources users are allowed to perform actions on.
- [Logging and Monitoring](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/incident-response.html): Monitor your Amazon Cloud Directory by using AWS CloudTrail.
- [Compliance Validation](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/cd-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Cloud Directory features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/infrastructure-security.html): Learn how Amazon Cloud Directory isolates service traffic.
