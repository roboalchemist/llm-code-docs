# Source: https://infisical.com/docs/documentation/platform/access-controls/additional-privileges.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Additional Privileges

> Learn how to add specific privileges on top of predefined roles.

Even though Infisical supports full-fledged [role-base access controls](./role-based-access-controls) with ability to set predefined permissions for user and machine identities, it is sometimes desired to set additional privileges for specific user or machine identities on top of their roles.

Infisical **Additional Privileges** functionality enables specific permissions with access to sensitive secrets/folders by identities within certain projects. It is possible to set up additional privileges through Web UI or API.

To provision specific privileges through Web UI:

1. Click on the `Edit` button next to the set of roles for user or identities.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/edit-role.png" alt="Edit User Role" />

2. Click `Add Additional Privileges` in the corresponding section of the permission management modal.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/add-additional-privileges.png" alt="Add Specific Privilege" />

3. Fill out the necessary parameters in the privilege entry that appears. It is possible to specify the `Environment` and `Secret Path` to which you want to enable access.
   It is also possible to define the range of permissions (`View`, `Create`, `Modify`, `Delete`) as well as how long the access should last (e.g., permanent or timed).
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/additional-privileges.png" alt="Additional privileges" />

4. Click the `Save` button to enable the additional privilege.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/confirm-additional-privileges.png" alt="Confirm Specific Privilege" />
