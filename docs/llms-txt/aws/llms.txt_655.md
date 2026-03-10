# Source: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/llms.txt

# AWS Private CA Connector for Active Directory API Reference

> AWS Private CA Connector for Active Directory creates a connector between AWS Private CA and Active Directory (AD) that enables you to provision security certificates for AD signed by a private CA that you own. For more information, see AWS Private CA Connector for Active Directory.

- [Welcome](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Operations.html)

- [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html): Creates a connector between AWS Private CA and an Active Directory.
- [CreateDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html): Creates a directory registration that authorizes communication between AWS Private CA and an Active Directory
- [CreateServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateServicePrincipalName.html): Creates a service principal name (SPN) for the service account in Active Directory.
- [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html): Creates an Active Directory compatible certificate template.
- [CreateTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html): Create a group access control entry.
- [DeleteConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteConnector.html): Deletes a connector for Active Directory.
- [DeleteDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration.html): Deletes a directory registration.
- [DeleteServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteServicePrincipalName.html): Deletes the service principal name (SPN) used by a connector to authenticate with your Active Directory.
- [DeleteTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteTemplate.html): Deletes a template.
- [DeleteTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteTemplateGroupAccessControlEntry.html): Deletes a group access control entry.
- [GetConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetConnector.html): Lists information about your connector.
- [GetDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetDirectoryRegistration.html): A structure that contains information about your directory registration.
- [GetServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetServicePrincipalName.html): Lists the service principal name that the connector uses to authenticate with Active Directory.
- [GetTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetTemplate.html): Retrieves a certificate template that the connector uses to issue certificates from a private CA.
- [GetTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetTemplateGroupAccessControlEntry.html): Retrieves the group access control entries for a template.
- [ListConnectors](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors.html): Lists the connectors that you created by using the action.
- [ListDirectoryRegistrations](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListDirectoryRegistrations.html): Lists the directory registrations that you created by using the action.
- [ListServicePrincipalNames](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListServicePrincipalNames.html): Lists the service principal names that the connector uses to authenticate with Active Directory.
- [ListTagsForResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTagsForResource.html): Lists the tags, if any, that are associated with your resource.
- [ListTemplateGroupAccessControlEntries](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTemplateGroupAccessControlEntries.html): Lists group access control entries you created.
- [ListTemplates](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTemplates.html): Lists the templates, if any, that are associated with a connector.
- [TagResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TagResource.html): Adds one or more tags to your resource.
- [UntagResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UntagResource.html): Removes one or more tags from your resource.
- [UpdateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UpdateTemplate.html): Update template configuration to define the information included in certificates.
- [UpdateTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UpdateTemplateGroupAccessControlEntry.html): Update a group access control entry you created using CreateTemplateGroupAccessControlEntry.


## [Data Types](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Types.html)

- [AccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessControlEntry.html): An access control entry allows or denies Active Directory groups based on their security identifiers (SIDs) from enrolling and/or autoenrolling with the template.
- [AccessControlEntrySummary](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessControlEntrySummary.html): Summary of group access control entries that allow or deny Active Directory groups based on their security identifiers (SIDs) from enrolling and/or autofenrolling with the template.
- [AccessRights](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessRights.html): Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.
- [ApplicationPolicies](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ApplicationPolicies.html): Application policies describe what the certificate can be used for.
- [ApplicationPolicy](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ApplicationPolicy.html): Application policies describe what the certificate can be used for.
- [CertificateValidity](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CertificateValidity.html): Information describing the end of the validity period of the certificate.
- [Connector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Connector.html): AWS Private CA Connector for Active Directory is a service that links your Active Directory with AWS Private CA.
- [ConnectorSummary](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ConnectorSummary.html): Summary description of the AWS Private CA AD connectors belonging to an AWS account.
- [DirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DirectoryRegistration.html): The directory registration represents the authorization of the connector service with a directory.
- [DirectoryRegistrationSummary](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DirectoryRegistrationSummary.html): The directory registration represents the authorization of the connector service with the Active Directory.
- [EnrollmentFlagsV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_EnrollmentFlagsV2.html): Template configurations for v2 template schema.
- [EnrollmentFlagsV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_EnrollmentFlagsV3.html): Template configurations for v3 template schema.
- [EnrollmentFlagsV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_EnrollmentFlagsV4.html): Template configurations for v4 template schema.
- [ExtensionsV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ExtensionsV2.html): Certificate extensions for v2 template schema
- [ExtensionsV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ExtensionsV3.html): Certificate extensions for v3 template schema
- [ExtensionsV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ExtensionsV4.html): Certificate extensions for v4 template schema
- [GeneralFlagsV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GeneralFlagsV2.html): General flags for v2 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.
- [GeneralFlagsV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GeneralFlagsV3.html): General flags for v3 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.
- [GeneralFlagsV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GeneralFlagsV4.html): General flags for v4 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.
- [KeyUsage](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_KeyUsage.html): The key usage extension defines the purpose (e.g., encipherment, signature) of the key contained in the certificate.
- [KeyUsageFlags](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_KeyUsageFlags.html): The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.
- [KeyUsageProperty](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_KeyUsageProperty.html): The key usage property defines the purpose of the private key contained in the certificate.
- [KeyUsagePropertyFlags](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_KeyUsagePropertyFlags.html): Specifies key usage.
- [PrivateKeyAttributesV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyAttributesV2.html): Defines the attributes of the private key.
- [PrivateKeyAttributesV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyAttributesV3.html): Defines the attributes of the private key.
- [PrivateKeyAttributesV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyAttributesV4.html): Defines the attributes of the private key.
- [PrivateKeyFlagsV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyFlagsV2.html): Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key.
- [PrivateKeyFlagsV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyFlagsV3.html): Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.
- [PrivateKeyFlagsV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyFlagsV4.html): Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.
- [ServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ServicePrincipalName.html): The service principal name that the connector uses to authenticate with Active Directory.
- [ServicePrincipalNameSummary](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ServicePrincipalNameSummary.html): The service principal name that the connector uses to authenticate with Active Directory.
- [SubjectNameFlagsV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_SubjectNameFlagsV2.html): Information to include in the subject name and alternate subject name of the certificate.
- [SubjectNameFlagsV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_SubjectNameFlagsV3.html): Information to include in the subject name and alternate subject name of the certificate.
- [SubjectNameFlagsV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_SubjectNameFlagsV4.html): Information to include in the subject name and alternate subject name of the certificate.
- [Template](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Template.html): An Active Directory compatible certificate template.
- [TemplateDefinition](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateDefinition.html): Template configuration to define the information included in certificates.
- [TemplateRevision](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateRevision.html): The revision version of the template.
- [TemplateSummary](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateSummary.html): An Active Directory compatible certificate template.
- [TemplateV2](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateV2.html): v2 template schema that uses Legacy Cryptographic Providers.
- [TemplateV3](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateV3.html): v3 template schema that uses Key Storage Providers.
- [TemplateV4](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateV4.html): v4 template schema that can use either Legacy Cryptographic Providers or Key Storage Providers.
- [ValidityPeriod](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ValidityPeriod.html): Information describing the end of the validity period of the certificate.
- [VpcInformation](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_VpcInformation.html): Information about your VPC and security groups used with the connector.
