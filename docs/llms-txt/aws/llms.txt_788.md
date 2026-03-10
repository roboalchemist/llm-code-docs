# Source: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/llms.txt

# Identity Store API Reference

> Identity Store API Reference.

- [Welcome](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/CommonErrors.html)
- [Document History](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/document_history.html)

## [Actions](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Operations.html)

- [CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroup.html): Creates a group within the specified identity store.
- [CreateGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroupMembership.html): Creates a relationship between a member and a group.
- [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html): Creates a user within the specified identity store.
- [DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroup.html): Delete a group within an identity store given GroupId.
- [DeleteGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroupMembership.html): Delete a membership within a group given MembershipId.
- [DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteUser.html): Deletes a user within an identity store given UserId.
- [DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html): Retrieves the group metadata and attributes from GroupId in an identity store.
- [DescribeGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroupMembership.html): Retrieves membership metadata and attributes from MembershipId in an identity store.
- [DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html): Retrieves the user metadata and attributes from the UserId in an identity store.
- [GetGroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupId.html): Retrieves GroupId in an identity store.
- [GetGroupMembershipId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupMembershipId.html): Retrieves the MembershipId in an identity store.
- [GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html): Retrieves the UserId in an identity store.
- [IsMemberInGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html): Checks the user's membership in all requested groups and returns if the member exists in all queried groups.
- [ListGroupMemberships](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMemberships.html): For the specified group in the specified identity store, returns the list of all GroupMembership objects and returns results in paginated form.
- [ListGroupMembershipsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html): For the specified member in the specified identity store, returns the list of all GroupMembership objects and returns results in paginated form.
- [ListGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html): Lists all groups in the identity store.
- [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html): Lists all users in the identity store.
- [UpdateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateGroup.html): Updates the specified group metadata and attributes in the specified identity store.
- [UpdateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateUser.html): Updates the specified user metadata and attributes in the specified identity store.


## [Data Types](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Types.html)

- [Address](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Address.html): The address associated with the specified user.
- [AlternateIdentifier](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_AlternateIdentifier.html): A unique identifier for a user or group that is not the primary identifier.
- [AttributeOperation](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_AttributeOperation.html): An operation that applies to the requested group.
- [Email](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Email.html): The email address associated with the user.
- [ExternalId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ExternalId.html): The identifier issued to this resource by an external identity provider.
- [Filter](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Filter.html): A query filter used by ListUsers and ListGroups.
- [Group](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html): A group object that contains the metadata and attributes for a specified group.
- [GroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GroupMembership.html): Contains the identifiers for a group, a group member, and a GroupMembership object in the identity store.
- [GroupMembershipExistenceResult](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GroupMembershipExistenceResult.html): Indicates whether a resource is a member of a group in the identity store.
- [MemberId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_MemberId.html): An object containing the identifier of a group member.
- [Name](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Name.html): The full name of the user.
- [PhoneNumber](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_PhoneNumber.html): The phone number associated with the user.
- [Photo](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Photo.html): Contains information about a user's photo.
- [Role](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Role.html): The role associated with the user.
- [UniqueAttribute](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UniqueAttribute.html): An entity attribute that's unique to a specific entity.
- [User](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html): A user object that contains the metadata and attributes for a specified user.
