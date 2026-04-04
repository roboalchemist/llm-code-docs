# Source: https://docs.turso.tech/cli/auth/api-tokens/revoke.md

# Source: https://docs.turso.tech/api-reference/tokens/revoke.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke API Token

> Revokes the provided API token belonging to a user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/auth/api-tokens/{tokenName}' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.apiTokens.revoke("my-token");
  ```
</RequestExample>


## OpenAPI

````yaml DELETE /v1/auth/api-tokens/{tokenName}
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
  /v1/auth/api-tokens/{tokenName}:
    delete:
      summary: Revoke API Token
      description: Revokes the provided API token belonging to a user.
      operationId: revokeAPIToken
      parameters:
        - $ref: '#/components/parameters/tokenName'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                properties:
                  token:
                    type: string
                    description: The revoked token name.
                    example: ...
components:
  parameters:
    tokenName:
      name: tokenName
      in: path
      required: true
      schema:
        type: string
      description: The name of the api token.

````