# Source: https://docs.aws.amazon.com/cognitosync/latest/APIReference/llms.txt

# Amazon Cognito Sync API Reference

> Amazon Cognito Sync provides an AWS service and client library that enable cross-device syncing of application-related user data. High-level client libraries are available for both iOS and Android. You can use these libraries to persist data locally so that it's available even if the device is offline. Developer credentials don't need to be stored on the mobile device to access the service. You can use Amazon Cognito to obtain a normalized user ID and credentials. User data is persisted in a dataset that can store up to 1 MB of key-value pairs, and you can have up to 20 datasets per user identity.

- [Welcome](https://docs.aws.amazon.com/cognitosync/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cognitosync/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cognitosync/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Operations.html)

- [BulkPublish](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_BulkPublish.html): Initiates a bulk publish of all existing datasets for an Identity Pool to the configured stream.
- [DeleteDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DeleteDataset.html): Deletes the specific dataset.
- [DescribeDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeDataset.html): Gets meta data about a dataset by identity and dataset name.
- [DescribeIdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityPoolUsage.html): Gets usage details (for example, data storage) about a particular identity pool.
- [DescribeIdentityUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityUsage.html): Gets usage information for an identity, including number of datasets and data usage.
- [GetBulkPublishDetails](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetBulkPublishDetails.html): Get the status of the last BulkPublish operation for an identity pool.
- [GetCognitoEvents](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetCognitoEvents.html): Gets the events and the corresponding Lambda functions associated with an identity pool.
- [GetIdentityPoolConfiguration](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetIdentityPoolConfiguration.html): Gets the configuration settings of an identity pool.
- [ListDatasets](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListDatasets.html): Lists datasets for an identity.
- [ListIdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListIdentityPoolUsage.html): Gets a list of identity pools registered with Cognito.
- [ListRecords](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListRecords.html): Gets paginated records, optionally changed after a particular sync count for a dataset and identity.
- [RegisterDevice](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_RegisterDevice.html): Registers a device to receive push sync notifications.
- [SetCognitoEvents](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_SetCognitoEvents.html): Sets the AWS Lambda function for a given event type for an identity pool.
- [SetIdentityPoolConfiguration](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_SetIdentityPoolConfiguration.html): Sets the necessary configuration for push sync.
- [SubscribeToDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_SubscribeToDataset.html): Subscribes to receive notifications when a dataset is modified by another device.
- [UnsubscribeFromDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_UnsubscribeFromDataset.html): Unsubscribes from receiving notifications when a dataset is modified by another device.
- [UpdateRecords](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_UpdateRecords.html): Posts updates to records and adds and deletes records for a dataset and user.


## [Data Types](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Types.html)

- [CognitoStreams](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_CognitoStreams.html): Configuration options for configure Cognito streams.
- [Dataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Dataset.html): A collection of data for an identity pool.
- [IdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_IdentityPoolUsage.html): Usage information for the identity pool.
- [IdentityUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_IdentityUsage.html): Usage information for the identity.
- [PushSync](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_PushSync.html): Configuration options to be applied to the identity pool.
- [Record](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Record.html): The basic data structure of a dataset.
- [RecordPatch](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_RecordPatch.html): An update operation for a record.
