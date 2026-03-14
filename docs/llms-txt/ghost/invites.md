# Source: https://docs.ghost.org/admin-api/users/invites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Invites

The invites resource provides an endpoint for inviting staff users to the Ghost instance. To invite a user you must specify the ID of the role they should receive (fetch roles, detailed above, to find the role IDs for your site), and the email address that the invite link should be sent to.

<RequestExample>
  ```json  theme={"dark"}
  // POST /admin/invites/
  {
      "invites": [
          {
              "role_id": "64498c2a7c11e805e0b4ad4b",
              "email": "person@example.com"
          },
          ...
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).