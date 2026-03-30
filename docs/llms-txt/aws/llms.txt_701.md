# Source: https://docs.aws.amazon.com/repostprivate/latest/APIReference/llms.txt

# AWS re:Post Private Welcome

> AWS re:Post Private is a private version of AWS re:Post for enterprises with Enterprise Support or Enterprise On-Ramp Support plans. It provides access to knowledge and experts to accelerate cloud adoption and increase developer productivity. With your organization-specific private re:Post, you can build an organization-specific developer community that drives efficiencies at scale and provides access to valuable knowledge resources. Additionally, re:Post Private centralizes trusted AWS technical content and offers private discussion forums to improve how your teams collaborate internally and with AWS to remove technical obstacles, accelerate innovation, and scale more efficiently in the cloud.

- [Welcome](https://docs.aws.amazon.com/repostprivate/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/repostprivate/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/repostprivate/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_Operations.html)

- [BatchAddChannelRoleToAccessors](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchAddChannelRoleToAccessors.html): Add role to multiple users or groups in a private re:Post channel.
- [BatchAddRole](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchAddRole.html): Add a role to multiple users or groups in a private re:Post.
- [BatchRemoveChannelRoleFromAccessors](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchRemoveChannelRoleFromAccessors.html): Remove a role from multiple users or groups in a private re:Post channel.
- [BatchRemoveRole](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchRemoveRole.html): Remove a role from multiple users or groups in a private re:Post.
- [CreateChannel](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_CreateChannel.html): Creates a channel in an AWS re:Post Private private re:Post.
- [CreateSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_CreateSpace.html): Creates an AWS re:Post Private private re:Post.
- [DeleteSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_DeleteSpace.html): Deletes an AWS re:Post Private private re:Post.
- [DeregisterAdmin](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_DeregisterAdmin.html): Removes the user or group from the list of administrators of the private re:Post.
- [GetChannel](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_GetChannel.html): Displays information about a channel in a private re:Post.
- [GetSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_GetSpace.html): Displays information about the AWS re:Post Private private re:Post.
- [ListChannels](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ListChannels.html): Returns the list of channel within a private re:Post with some information about each channel.
- [ListSpaces](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ListSpaces.html): Returns a list of AWS re:Post Private private re:Posts in the account with some information about each private re:Post.
- [ListTagsForResource](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ListTagsForResource.html): Returns the tags that are associated with the AWS re:Post Private resource specified by the resourceArn.
- [RegisterAdmin](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_RegisterAdmin.html): Adds a user or group to the list of administrators of the private re:Post.
- [SendInvites](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SendInvites.html): Sends an invitation email to selected users and groups.
- [TagResource](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_TagResource.html): Associates tags with an AWS re:Post Private resource.
- [UntagResource](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UntagResource.html): Removes the association of the tag with the AWS re:Post Private resource.
- [UpdateChannel](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UpdateChannel.html): Modifies an existing channel.
- [UpdateSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UpdateSpace.html): Modifies an existing AWS re:Post Private private re:Post.


## [Data Types](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_Types.html)

- [BatchError](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchError.html): An error that occurred during a batch operation.
- [ChannelData](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ChannelData.html): A structure that contains some information about a channel in a private re:Post.
- [SpaceData](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SpaceData.html): A structure that contains some information about a private re:Post in the account.
- [SupportedEmailDomainsParameters](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SupportedEmailDomainsParameters.html)
- [SupportedEmailDomainsStatus](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SupportedEmailDomainsStatus.html)
- [ValidationExceptionField](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ValidationExceptionField.html): Stores information about a field thatâs passed inside a request that resulted in an exception.
