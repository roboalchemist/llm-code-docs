# Source: https://docs.aws.amazon.com/sns/latest/api/llms.txt

# Amazon Simple Notification Service API Reference

> We also provide SDKs that enable you to access Amazon SNS from your preferred programming language. The SDKs contain functionality that automatically takes care of tasks such as: cryptographically signing your service requests, retrying requests, and handling error responses. For a list of available SDKs, go to Tools for Amazon Web Services.

- [Welcome](https://docs.aws.amazon.com/sns/latest/api/welcome.html)
- [API actions by category](https://docs.aws.amazon.com/sns/latest/api/actions-list.html)
- [Common Parameters](https://docs.aws.amazon.com/sns/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/sns/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/sns/latest/api/API_Operations.html)

- [AddPermission](https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html): Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.
- [CheckIfPhoneNumberIsOptedOut](https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html): Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your AWS account.
- [ConfirmSubscription](https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html): Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action.
- [CreatePlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html): Creates a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and mobile apps may register.
- [CreatePlatformEndpoint](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html): Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS.
- [CreateSMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_CreateSMSSandboxPhoneNumber.html): Adds a destination phone number to an AWS account in the SMS sandbox and sends a one-time password (OTP) to that phone number.
- [CreateTopic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html): Creates a topic to which notifications can be published.
- [DeleteEndpoint](https://docs.aws.amazon.com/sns/latest/api/API_DeleteEndpoint.html): Deletes the endpoint for a device and mobile app from Amazon SNS.
- [DeletePlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_DeletePlatformApplication.html): Deletes a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging).
- [DeleteSMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_DeleteSMSSandboxPhoneNumber.html): Deletes an AWS account's verified or pending phone number from the SMS sandbox.
- [DeleteTopic](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html): Deletes a topic and all its subscriptions.
- [GetDataProtectionPolicy](https://docs.aws.amazon.com/sns/latest/api/API_GetDataProtectionPolicy.html): Retrieves the specified inline DataProtectionPolicy document that is stored in the specified Amazon SNS topic.
- [GetEndpointAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html): Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS.
- [GetPlatformApplicationAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html): Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging).
- [GetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html): Returns the settings for sending SMS messages from your AWS account.
- [GetSMSSandboxAccountStatus](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSSandboxAccountStatus.html): Retrieves the SMS sandbox status for the calling AWS account in the target AWS Region.
- [GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html): Returns all of the properties of a subscription.
- [GetTopicAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html): Returns all of the properties of a topic.
- [ListEndpointsByPlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html): Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM (Firebase Cloud Messaging) and APNS.
- [ListOriginationNumbers](https://docs.aws.amazon.com/sns/latest/api/API_ListOriginationNumbers.html): Lists the calling AWS account's dedicated origination numbers and their metadata.
- [ListPhoneNumbersOptedOut](https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html): Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.
- [ListPlatformApplications](https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html): Lists the platform application objects for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging).
- [ListSMSSandboxPhoneNumbers](https://docs.aws.amazon.com/sns/latest/api/API_ListSMSSandboxPhoneNumbers.html): Lists the calling AWS account's current verified and pending destination phone numbers in the SMS sandbox.
- [ListSubscriptions](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html): Returns a list of the requester's subscriptions.
- [ListSubscriptionsByTopic](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html): Returns a list of the subscriptions to a specific topic.
- [ListTagsForResource](https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html): List all tags added to the specified Amazon SNS topic.
- [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html): Returns a list of the requester's topics.
- [OptInPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_OptInPhoneNumber.html): Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number.
- [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html): Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the TargetArn).
- [PublishBatch](https://docs.aws.amazon.com/sns/latest/api/API_PublishBatch.html): Publishes up to 10 messages to the specified topic in a single batch.
- [PutDataProtectionPolicy](https://docs.aws.amazon.com/sns/latest/api/API_PutDataProtectionPolicy.html): Adds or updates an inline policy document that is stored in the specified Amazon SNS topic.
- [RemovePermission](https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html): Removes a statement from a topic's access control policy.
- [SetEndpointAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html): Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS.
- [SetPlatformApplicationAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html): Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging).
- [SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html): Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.
- [SetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html): Allows a subscription owner to set an attribute of the subscription to a new value.
- [SetTopicAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html): Allows a topic owner to set an attribute of the topic to a new value.
- [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html): Subscribes an endpoint to an Amazon SNS topic.
- [TagResource](https://docs.aws.amazon.com/sns/latest/api/API_TagResource.html): Add tags to the specified Amazon SNS topic.
- [Unsubscribe](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html): Deletes a subscription.
- [UntagResource](https://docs.aws.amazon.com/sns/latest/api/API_UntagResource.html): Remove tags from the specified Amazon SNS topic.
- [VerifySMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_VerifySMSSandboxPhoneNumber.html): Verifies a destination phone number with a one-time password (OTP) for the calling AWS account.


## [Data Types](https://docs.aws.amazon.com/sns/latest/api/API_Types.html)

- [BatchResultErrorEntry](https://docs.aws.amazon.com/sns/latest/api/API_BatchResultErrorEntry.html): Gives a detailed description of failed messages in the batch.
- [Endpoint](https://docs.aws.amazon.com/sns/latest/api/API_Endpoint.html): The endpoint for mobile app and device.
- [MessageAttributeValue](https://docs.aws.amazon.com/sns/latest/api/API_MessageAttributeValue.html): The user-specified message attribute value.
- [PhoneNumberInformation](https://docs.aws.amazon.com/sns/latest/api/API_PhoneNumberInformation.html): A list of phone numbers and their metadata.
- [PlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_PlatformApplication.html): Platform application object.
- [PublishBatchRequestEntry](https://docs.aws.amazon.com/sns/latest/api/API_PublishBatchRequestEntry.html): Contains the details of a single Amazon SNS message along with an Id that identifies a message within the batch.
- [PublishBatchResultEntry](https://docs.aws.amazon.com/sns/latest/api/API_PublishBatchResultEntry.html): Encloses data related to a successful message in a batch request for topic.
- [SMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_SMSSandboxPhoneNumber.html): A verified or pending destination phone number in the SMS sandbox.
- [Subscription](https://docs.aws.amazon.com/sns/latest/api/API_Subscription.html): A wrapper type for the attributes of an Amazon SNS subscription.
- [Tag](https://docs.aws.amazon.com/sns/latest/api/API_Tag.html): The list of tags to be added to the specified topic.
- [Topic](https://docs.aws.amazon.com/sns/latest/api/API_Topic.html): A wrapper type for the topic's Amazon Resource Name (ARN).
