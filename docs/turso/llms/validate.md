# Source: https://docs.turso.tech/api-reference/tokens/validate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate API Token

> Validates an API token belonging to a user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v1/auth/validate' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.apiTokens.validate("...");
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/auth/validate
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
  /v1/auth/validate:
    get:
      summary: Validate API Token
      description: Validates an API token belonging to a user.
      operationId: validateAPIToken
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  exp:
                    type: integer
                    description: >-
                      The time of expiration for the provided token in unix
                      epoch seconds, or `-1` if there is no expiration.
                    example: 999

````