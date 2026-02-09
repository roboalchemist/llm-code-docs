# Source: https://docs.turso.tech/api-reference/organizations/members/remove.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Member

> Remove a user from the organization by username.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE https://api.turso.tech/v1/organizations/{organizationSlug}/members/{username} \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const member = await turso.organizations.removeMember("mycompany", "iku");
  ```
</RequestExample>


## OpenAPI

````yaml DELETE /v1/organizations/{organizationSlug}/members/{username}
openapi: 3.0.1
info:
  title: Turso Platform API
  description: API description here
  license:
    name: MIT
  version: 0.1.0
servers:
  - url: https://api.turso.tech
    description: Turso's Platform API
security: []
paths:
  /v1/organizations/{organizationSlug}/members/{username}:
    delete:
      summary: Remove Member
      description: Remove a user from the organization by username.
      operationId: removeOrganizationMember
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/username'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  member: f7e1a190-3daf-4f9d-a74e-c843e6c24598
        '404':
          description: Member not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: user [username] is not a member of org [organizationSlug]
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
    username:
      name: username
      in: path
      required: true
      schema:
        type: string
      description: The username of a Turso user or organization member.

````