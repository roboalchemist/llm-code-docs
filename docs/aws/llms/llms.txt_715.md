# Source: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/llms.txt

# IAM Roles Anywhere API Reference

> AWS Identity and Access Management Roles Anywhere provides a secure way for your workloads such as servers, containers, and applications that run outside of AWS to obtain temporary AWS credentials. Your workloads can use the same IAM policies and roles you have for native AWS applications to access AWS resources. Using IAM Roles Anywhere eliminates the need to manage long-term credentials for workloads running outside of AWS.

- [Welcome](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_Operations.html)

- [CreateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateProfile.html): Creates a profile, a list of the roles that Roles Anywhere service is trusted to assume.
- [CreateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateTrustAnchor.html): Creates a trust anchor to establish trust between IAM Roles Anywhere and your certificate authority (CA).
- [DeleteAttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteAttributeMapping.html): Delete an entry from the attribute mapping rules enforced by a given profile.
- [DeleteCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteCrl.html): Deletes a certificate revocation list (CRL).
- [DeleteProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteProfile.html): Deletes a profile.
- [DeleteTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteTrustAnchor.html): Deletes a trust anchor.
- [DisableCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableCrl.html): Disables a certificate revocation list (CRL).
- [DisableProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableProfile.html): Disables a profile.
- [DisableTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableTrustAnchor.html): Disables a trust anchor.
- [EnableCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableCrl.html): Enables a certificate revocation list (CRL).
- [EnableProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableProfile.html): Enables temporary credential requests for a profile.
- [EnableTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableTrustAnchor.html): Enables a trust anchor.
- [GetCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetCrl.html): Gets a certificate revocation list (CRL).
- [GetProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetProfile.html): Gets a profile.
- [GetSubject](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetSubject.html): Gets a subject, which associates a certificate identity with authentication attempts.
- [GetTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetTrustAnchor.html): Gets a trust anchor.
- [ImportCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ImportCrl.html): Imports the certificate revocation list (CRL).
- [ListCrls](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListCrls.html): Lists all certificate revocation lists (CRL) in the authenticated account and AWS Region.
- [ListProfiles](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListProfiles.html): Lists all profiles in the authenticated account and AWS Region.
- [ListSubjects](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListSubjects.html): Lists the subjects in the authenticated account and AWS Region.
- [ListTagsForResource](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListTagsForResource.html): Lists the tags attached to the resource.
- [ListTrustAnchors](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListTrustAnchors.html): Lists the trust anchors in the authenticated account and AWS Region.
- [PutAttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_PutAttributeMapping.html): Put an entry in the attribute mapping rules that will be enforced by a given profile.
- [PutNotificationSettings](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_PutNotificationSettings.html): Attaches a list of notification settings to a trust anchor.
- [ResetNotificationSettings](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ResetNotificationSettings.html): Resets the custom notification setting to IAM Roles Anywhere default setting.
- [TagResource](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_TagResource.html): Attaches tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UntagResource.html): Removes tags from the resource.
- [UpdateCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateCrl.html): Updates the certificate revocation list (CRL).
- [UpdateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateProfile.html): Updates a profile, a list of the roles that IAM Roles Anywhere service is trusted to assume.
- [UpdateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateTrustAnchor.html): Updates a trust anchor.


## [Data Types](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_Types.html)

- [AttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_AttributeMapping.html): A mapping applied to the authenticating end-entity certificate.
- [CredentialSummary](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CredentialSummary.html): A record of a presented X509 credential from a temporary credential request.
- [CrlDetail](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CrlDetail.html): The state of the certificate revocation list (CRL) after a read or write operation.
- [InstanceProperty](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_InstanceProperty.html): A key-value pair you set that identifies a property of the authenticating instance.
- [MappingRule](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_MappingRule.html): A single mapping entry for each supported specifier or sub-field.
- [NotificationSetting](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_NotificationSetting.html): Customizable notification settings that will be applied to notification events.
- [NotificationSettingDetail](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_NotificationSettingDetail.html): The state of a notification setting.
- [NotificationSettingKey](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_NotificationSettingKey.html): A notification setting key to reset.
- [ProfileDetail](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ProfileDetail.html): The state of the profile after a read or write operation.
- [Source](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_Source.html): The trust anchor type and its related certificate data.
- [SourceData](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_SourceData.html): The data field of the trust anchor depending on its type.
- [SubjectDetail](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_SubjectDetail.html): The state of the subject after a read or write operation.
- [SubjectSummary](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_SubjectSummary.html): A summary representation of subjects.
- [Tag](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_Tag.html): A label that consists of a key and value you define.
- [TrustAnchorDetail](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_TrustAnchorDetail.html): The state of the trust anchor after a read or write operation.
