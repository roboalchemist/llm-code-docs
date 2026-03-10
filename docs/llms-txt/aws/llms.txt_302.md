# Source: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/llms.txt

# AWS Directory Service Data API Reference

> AWS Directory Service Data is an extension of AWS Directory Service. This API reference provides detailed information about Directory Service Data operations and object types.

- [Welcome](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_Operations.html)

- [AddGroupMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_AddGroupMember.html): Adds an existing user, group, or computer as a group member.
- [CreateGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateGroup.html): Creates a new group.
- [CreateUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateUser.html): Creates a new user.
- [DeleteGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DeleteGroup.html): Deletes a group.
- [DeleteUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DeleteUser.html): Deletes a user.
- [DescribeGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeGroup.html): Returns information about a specific group.
- [DescribeUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeUser.html): Returns information about a specific user.
- [DisableUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DisableUser.html): Deactivates an active user account.
- [ListGroupMembers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupMembers.html): Returns member information for the specified group.
- [ListGroups](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroups.html): Returns group information for the specified directory.
- [ListGroupsForMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupsForMember.html): Returns group information for the specified member.
- [ListUsers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListUsers.html): Returns user information for the specified directory.
- [RemoveGroupMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_RemoveGroupMember.html): Removes a member from a group.
- [SearchGroups](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchGroups.html): Searches the specified directory for a group.
- [SearchUsers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchUsers.html): Searches the specified directory for a user.
- [UpdateGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateGroup.html): Updates group information.
- [UpdateUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateUser.html): Updates user information.


## [Data Types](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_Types.html)

- [AttributeValue](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_AttributeValue.html): The data type for an attribute.
- [Group](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_Group.html): A group object that contains identifying information and attributes for a specified group.
- [GroupSummary](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_GroupSummary.html): A structure containing a subset of fields of a group object from a directory.
- [Member](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_Member.html): A member object that contains identifying information for a specified member.
- [User](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_User.html): A user object that contains identifying information and attributes for a specified user.
- [UserSummary](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UserSummary.html): A structure containing a subset of the fields of a user object from a directory.
