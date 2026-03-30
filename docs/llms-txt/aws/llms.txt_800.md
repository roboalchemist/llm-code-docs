# Source: https://docs.aws.amazon.com/social-messaging/latest/APIReference/llms.txt

# AWS End User Messaging Social API Reference

> AWS End User Messaging Social, also referred to as Social messaging, is a messaging service that enables application developers to incorporate WhatsApp into their existing workflows. The AWS End User Messaging Social API provides information about the AWS End User Messaging Social API resources, including supported HTTP methods, parameters, and schemas.

- [Welcome](https://docs.aws.amazon.com/social-messaging/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/social-messaging/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/social-messaging/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_Operations.html)

- [AssociateWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_AssociateWhatsAppBusinessAccount.html): This is only used through the AWS console during sign-up to associate your WhatsApp Business Account to your AWS account.
- [CreateWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplate.html): Creates a new WhatsApp message template from a custom definition.
- [CreateWhatsAppMessageTemplateFromLibrary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplateFromLibrary.html): Creates a new WhatsApp message template using a template from Meta's template library.
- [CreateWhatsAppMessageTemplateMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplateMedia.html): Uploads media for use in a WhatsApp message template.
- [DeleteWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppMessageMedia.html): Delete a media object from the WhatsApp service.
- [DeleteWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppMessageTemplate.html): Deletes a WhatsApp message template.
- [DisassociateWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DisassociateWhatsAppBusinessAccount.html): Disassociate a WhatsApp Business Account (WABA) from your AWS account.
- [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html): Get the details of your linked WhatsApp Business Account.
- [GetLinkedWhatsAppBusinessAccountPhoneNumber](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccountPhoneNumber.html): Retrieve the WABA account id and phone number details of a WhatsApp business account phone number.
- [GetWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageMedia.html): Get a media file from the WhatsApp service.
- [GetWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageTemplate.html): Retrieves a specific WhatsApp message template.
- [ListLinkedWhatsAppBusinessAccounts](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html): List all WhatsApp Business Accounts linked to your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListTagsForResource.html): List all tags associated with a resource, such as a phone number or WABA.
- [ListWhatsAppMessageTemplates](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppMessageTemplates.html): Lists WhatsApp message templates for a specific WhatsApp Business Account.
- [ListWhatsAppTemplateLibrary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppTemplateLibrary.html): Lists templates available in Meta's template library for WhatsApp messaging.
- [PostWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html): Upload a media file to the WhatsApp service.
- [PutWhatsAppBusinessAccountEventDestinations](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PutWhatsAppBusinessAccountEventDestinations.html): Add an event destination to log event data from WhatsApp for a WhatsApp Business Account (WABA).
- [SendWhatsAppMessage](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html): Send a WhatsApp message.
- [TagResource](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_TagResource.html): Adds or overwrites only the specified tags for the specified resource.
- [UntagResource](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UntagResource.html): Removes the specified tags from a resource.
- [UpdateWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppMessageTemplate.html): Updates an existing WhatsApp message template.


## [Data Types](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_Types.html)

- [LibraryTemplateBodyInputs](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LibraryTemplateBodyInputs.html): Configuration options for customizing the body content of a template from Meta's library.
- [LibraryTemplateButtonInput](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LibraryTemplateButtonInput.html): Configuration options for customizing buttons in a template from Meta's library.
- [LibraryTemplateButtonList](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LibraryTemplateButtonList.html): Defines a button in a template from Meta's library.
- [LinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LinkedWhatsAppBusinessAccount.html): The details of your linked WhatsApp Business Account.
- [LinkedWhatsAppBusinessAccountIdMetaData](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LinkedWhatsAppBusinessAccountIdMetaData.html): Contains your WhatsApp registration status and details of any unregistered WhatsApp phone number.
- [LinkedWhatsAppBusinessAccountSummary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LinkedWhatsAppBusinessAccountSummary.html): The details of a linked WhatsApp Business Account.
- [MetaLibraryTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaLibraryTemplate.html): Represents a template from Meta's library with customization options.
- [MetaLibraryTemplateDefinition](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaLibraryTemplateDefinition.html): Defines the complete structure and content of a template in Meta's library.
- [S3File](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_S3File.html): Contains information for the S3 bucket that contains media files.
- [S3PresignedUrl](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_S3PresignedUrl.html): You can use presigned URLs to grant time-limited access to objects in Amazon S3 without updating your bucket policy.
- [Tag](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_Tag.html): The tag for a resource.
- [TemplateSummary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_TemplateSummary.html): Provides a summary of a WhatsApp message template's key attributes.
- [WabaPhoneNumberSetupFinalization](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WabaPhoneNumberSetupFinalization.html): The registration details for a linked phone number.
- [WabaSetupFinalization](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WabaSetupFinalization.html): The registration details for a linked WhatsApp Business Account.
- [WhatsAppBusinessAccountEventDestination](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppBusinessAccountEventDestination.html): Contains information on the event destination.
- [WhatsAppPhoneNumberDetail](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppPhoneNumberDetail.html): The details of your WhatsApp phone number.
- [WhatsAppPhoneNumberSummary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppPhoneNumberSummary.html): The details of a linked phone number.
- [WhatsAppSetupFinalization](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppSetupFinalization.html): The details of linking a WhatsApp Business Account to your AWS account.
- [WhatsAppSignupCallback](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppSignupCallback.html): Contains the accessToken provided by Meta during signup.
- [WhatsAppSignupCallbackResult](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppSignupCallbackResult.html): Contains the results of WhatsAppSignupCallback.
