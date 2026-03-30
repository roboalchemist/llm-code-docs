# Source: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/llms.txt

# License Manager Linux Subscriptions API Reference

> With AWS License Manager, you can discover and track your commercial Linux subscriptions on running Amazon EC2 instances.

- [Welcome](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Operations.html)

- [DeregisterSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_DeregisterSubscriptionProvider.html): Remove a third-party subscription provider from the Bring Your Own License (BYOL) subscriptions registered to your account.
- [GetRegisteredSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_GetRegisteredSubscriptionProvider.html): Get details for a Bring Your Own License (BYOL) subscription that's registered to your account.
- [GetServiceSettings](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_GetServiceSettings.html): Lists the Linux subscriptions service settings for your account.
- [ListLinuxSubscriptionInstances](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListLinuxSubscriptionInstances.html): Lists the running Amazon EC2 instances that were discovered with commercial Linux subscriptions.
- [ListLinuxSubscriptions](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListLinuxSubscriptions.html): Lists the Linux subscriptions that have been discovered.
- [ListRegisteredSubscriptionProviders](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListRegisteredSubscriptionProviders.html): List Bring Your Own License (BYOL) subscription registration resources for your account.
- [ListTagsForResource](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListTagsForResource.html): List the metadata tags that are assigned to the specified AWS resource.
- [RegisterSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_RegisterSubscriptionProvider.html): Register the supported third-party subscription provider for your Bring Your Own License (BYOL) subscription.
- [TagResource](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_TagResource.html): Add metadata tags to the specified AWS resource.
- [UntagResource](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_UntagResource.html): Remove one or more metadata tag from the specified AWS resource.
- [UpdateServiceSettings](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_UpdateServiceSettings.html): Updates the service settings for Linux subscriptions.


## [Data Types](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Types.html)

- [Filter](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Filter.html): A filter object that is used to return more specific results from a describe operation.
- [Instance](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Instance.html): Details discovered information about a running instance using Linux subscriptions.
- [LinuxSubscriptionsDiscoverySettings](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_LinuxSubscriptionsDiscoverySettings.html): Lists the settings defined for discovering Linux subscriptions.
- [RegisteredSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_RegisteredSubscriptionProvider.html): A third-party provider for operating system (OS) platform software and license subscriptions, such as Red Hat.
- [Subscription](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Subscription.html): An object which details a discovered Linux subscription.
