# Source: https://docs.promptlayer.com/reference/prompt-labels-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Prompt Template Label

Create a release label for a prompt template version.


## OpenAPI

````yaml POST /prompts/{prompt_id}/label
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompts/{prompt_id}/label:
    post:
      tags:
        - prompts
        - labels
      summary: Create a new label for a prompt
      operationId: create_prompt_label
      parameters:
        - name: prompt_id
          in: path
          required: true
          schema:
            type: integer
            title: prompt_id
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt_version_number:
                  type: integer
                name:
                  type: string
              required:
                - prompt_version_number
                - name
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  created_at:
                    type: string
                    format: date-time
                  id:
                    type: integer
                  name:
                    type: string
                  prompt_id:
                    type: integer
                  prompt_version_id:
                    type: integer
                required:
                  - created_at
                  - id
                  - name
                  - prompt_id
                  - prompt_version_id

````