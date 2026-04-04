# Source: https://docs.aws.amazon.com/servicecatalog/latest/arguide/llms.txt

# AWS Service Catalog AppRegistry Administrator Guide

- [Troubleshooting in AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/servicecatalog/latest/arguide/history.html)

## [What is AppRegistry?](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html)

### [Key concepts](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html)

Learn about the key components of AppRegistry.

### [The awsApplication tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-user-tags.html)

The awsApplication tag is a tag that AppRegistry vends when you create an AppRegistry application.

- [Tutorial: Existing AppRegistry application resources and the awsApplication tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/existing-customer-usecases.html): If you have existing AppRegistry application, AWS recommends that you retroactively apply the awsApplication tag to all of the resources in the application, and also ensure any future resources added to the application have the awsApplication tag applied.
- [Tag-sync tasks](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html): An automatic tag-synchronization of application resources (a tag-sync task) is an application resource management strategy that works by automatically adding and removing from resources to manage their inclusion in an application.
- [Quotas](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-quotas.html): Learn about the default service quotas for AppRegistry.


## [Getting started](https://docs.aws.amazon.com/servicecatalog/latest/arguide/getting-started-ar.html)

- [Tutorial: Create your first application and attribute group](https://docs.aws.amazon.com/servicecatalog/latest/arguide/tutorial-appreg.html): Learn how to create applications and attribute groups in AppRegistry


## [Using AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/use-appregistry.html)

### [Managing applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-app.html)

Learn about how to manage applications.

- [Creating applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-apps.html): Learn about how to create applications in AWS Service Catalog AppRegistry.

### [Using Application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-app-details.html)

Learn about how to use application details.

- [Viewing Application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/view-app-details.html): Learn about how to view Application details.
- [Viewing applications in AWS Systems Manager Application Manager](https://docs.aws.amazon.com/servicecatalog/latest/arguide/view-app-manager.html): Learn about how to view applications in Application Manager.
- [Editing applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/edit-apps.html): Learn about how to edit applications in AWS Service Catalog AppRegistry.
- [Deleting applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/delete-app-details.html): Learn about how to delete applications in AWS Service Catalog AppRegistry.

### [Managing application resources](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resource.html)

Learn about how to manage application resources.

- [Associating and disassociating application resources](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resources.html): Learn about how to associate and disassociate application resources.
- [Controlling the resources associated to applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/control-tags.html): Learn about how to control resources associated to applications.
- [Supported resource types for AppRegistry applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/supported-resource-types.html): This topic includes a list of supported resource types by service for AppRegistry applications.

### [Managing attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attributes.html)

Learn about how to manage attribute groups.

- [Creating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-attr-groups.html): Learn about how to create attribute groups in AppRegistry.

### [Using Attribute group details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-attr-group-details.html)

Learn about using Attribute group details.

- [Viewing Attribute group details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/view-attr-group.html): Learn about how to view Attribute group details.
- [Viewing attribute group metadata](https://docs.aws.amazon.com/servicecatalog/latest/arguide/manage-metatdata.html): Learn about how to view an attribute group metadata.
- [Editing attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/edit-attr-group.html): Learn about how to edit attribute groups.
- [Deleting attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/delete-attr-group.html): Learn about how to delete attribute groups in AppRegistry.
- [Associating and disassociating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attr-groups.html): Learn about how to associate and disassociate attribute groups in AppRegistry.

### [Sharing resources with accounts in your organization](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html)

Learn about how to share resources.

- [Creating and managing resource shares in applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/share-apps.html): Learn about creating and managing resource shares in applications.
- [Creating and managing resource shares in attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/share-attr-groups.html): Learn about creating and managing resource shares in attribute groups.
- [Using AWS Resource Access Manager to share resources](https://docs.aws.amazon.com/servicecatalog/latest/arguide/share-ram.html): TBD
- [Managing tags](https://docs.aws.amazon.com/servicecatalog/latest/arguide/add-tags.html): Learn about how to create and manage tags.


## [Security](https://docs.aws.amazon.com/servicecatalog/latest/arguide/security-app-registry.html)

- [Data protection](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-data-protection.html): Learn about how data protection works in AppRegistry.

### [Identity and Access Management](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-iam.html)

Learn about IAM and AWS Service Catalog AppRegistry

- [Using service-linked roles for AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/slr-appregistry.html): Learn about how AppRegistry uses the service-linked role AWSServiceCatalogAppRegistryServiceRolePolicy.
- [Logging and Monitoring](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-logging-monitoring.html): Learn about logging and monitoring in AppRegistry.
- [Compliance Validation](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-compliance-validation.html): Learn about how third-party auditors assess security and compliance for Service Catalog
- [Resilience](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-resilience.html): Learn about AWS Regions and Availability Zones as well as self-service actions for AppRegistry.
- [Infrastructure Security](https://docs.aws.amazon.com/servicecatalog/latest/arguide/ar-infrastructure.html): Learn about how the AWS global network security procedures protect AppRegistry.
- [AWS managed polices](https://docs.aws.amazon.com/servicecatalog/latest/arguide/managed-policies.html): Learn about AWS managed policies in AppRegistry.
