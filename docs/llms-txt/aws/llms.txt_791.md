# Source: https://docs.aws.amazon.com/singlesignon/latest/developerguide/llms.txt

# IAM Identity Center SCIM Implementation Developer Guide

- [What is the IAM Identity Center SCIM implementation?](https://docs.aws.amazon.com/singlesignon/latest/developerguide/what-is-scim.html)
- [Making API Requests](https://docs.aws.amazon.com/singlesignon/latest/developerguide/making-api-requests.html)
- [Limitations](https://docs.aws.amazon.com/singlesignon/latest/developerguide/limitations.html)
- [Document History](https://docs.aws.amazon.com/singlesignon/latest/developerguide/document-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/singlesignon/latest/developerguide/glossary.html)

## [Supported API operations](https://docs.aws.amazon.com/singlesignon/latest/developerguide/supported-apis.html)

- [CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/creategroup.html): Groups can be created through a POST request to the /Groups endpoint with the body containing the information of the group.
- [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/createuser.html): You can create new users from a POST request using the IAM Identity Center SCIM implementation /Users endpoint.
- [DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/deletegroup.html): The DELETE request is also available for the /Groups endpoint to delete existing groups using the value of the id.
- [DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/deleteuser.html): A user can be deleted by making a DELETE request to the /Users endpoint with an existing user ID.
- [GetGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/getgroup.html): Information about an existing group can be retrieved by making a request to the /Groups endpoint with the group ID.
- [GetSchema](https://docs.aws.amazon.com/singlesignon/latest/developerguide/getschema.html): Information about supported SCIM schemas can be retrieved by making a request to the /Schemas endpoint.
- [GetUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/getuser.html): Existing users can be retrieved by making a GET request to the IAM Identity Center SCIM implementation /Users endpoint with a user ID.
- [ListGroups](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listgroups.html): You can use the /Groups endpoint to filter queries on a list of existing groups by making a GET request with additional filter information.
- [ListResourceTypes](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listresourcetypes.html): Information about supported resource types can be retrieved by making a request to the /ResourceTypes endpoint.
- [ListSchemas](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listschemas.html): Information about supported SCIM schemas can be retrieved by making a request to the /Schemas endpoint.
- [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listusers.html): This endpoint provides the ability to perform filter queries on an existing list of users through a GET request to /Users by inserting additional filters.
- [PatchGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/patchgroup.html): Existing groups can be updated by calling upon the PATCH operation to replace specific attribute values.
- [PatchUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/patchuser.html): The /Users endpoint allows a PATCH request to be made for partial changes to an existing user.
- [PutUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/putuser.html): An existing user can be overwritten by making a PUT request to the /Users endpoint with the user ID.
- [ServiceProviderConfig](https://docs.aws.amazon.com/singlesignon/latest/developerguide/serviceproviderconfig.html): You can use the /ServiceProviderConfig endpoint for GET requests to view additional information about the IAM Identity Center SCIM implementation.
