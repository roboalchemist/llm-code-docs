# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/update_assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an assistant

> Update an existing assistant. You can modify the assistant's instructions.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#add-instructions-to-an-assistant).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X PATCH "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.1"}
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.1"},
    "status": "Ready",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-10-01T12:30:00Z",
    "updated_at": "2025-10-01T12:45:00Z"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_control_2025-10.oas.yaml patch /assistants/{assistant_name}
openapi: 3.0.3
info:
  title: Pinecone Assistant Control Plane API
  description: >-
    Pinecone Assistant Engine is a context engine to store and retrieve relevant
    knowledge  from millions of documents at scale. This API supports creating
    and managing assistants. 
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://api.pinecone.io/assistant
    description: Production API endpoints
security:
  - ApiKeyAuth: []
tags:
  - name: Manage Assistants
    description: Actions that manage Assistants
paths:
  /assistants/{assistant_name}:
    patch:
      tags:
        - Manage Assistants
      summary: Update an assistant
      description: >-
        Update an existing assistant. You can modify the assistant's
        instructions.


        For guidance and examples, see [Manage
        assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#add-instructions-to-an-assistant).
      operationId: update_assistant
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: path
          name: assistant_name
          description: The name of the assistant to update.
          required: true
          schema:
            type: string
          style: simple
      requestBody:
        description: The desired configuration updates for the assistant.
        content:
          application/json:
            schema:
              description: The configuration updates for the assistant.
              type: object
              properties:
                instructions:
                  nullable: true
                  description: >-
                    Description or directive for the assistant to apply to all
                    responses. Maximum 16 KB.
                  type: string
                metadata:
                  description: >-
                    Optional metadata associated with the assistant. Metadata is
                    a JSON object that can store custom organizational data,
                    tags, and attributes. Maximum size is 16KB.
                  nullable: true
                  type: object
        required: true
      responses:
        '200':
          description: Update request successful.
          content:
            application/json:
              schema:
                type: object
                properties:
                  assistant_name:
                    type: string
                  instructions:
                    description: >-
                      Description or directive for the assistant to apply to all
                      responses.
                    type: string
                  metadata:
                    description: >-
                      Optional metadata associated with the assistant. Metadata
                      is a JSON object that can store custom organizational
                      data, tags, and attributes.
                    type: object
        '400':
          description: Bad Request
        '401':
          description: Unauthorized
        '404':
          description: Assistant not found
        '500':
          description: Internal Server Error
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: Pinecone API Key

````