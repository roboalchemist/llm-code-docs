# Source: https://docs.promptlayer.com/reference/track-prompt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track Prompt

Associate a prompt template with a request.

## Example Code

```python  theme={null}
import requests
response = requests.post(
  "https://api.promptlayer.com/rest/track-prompt",
  headers={"X-API-KEY": "<YOUR_API_KEY>"},
  json={
      "prompt_name": "<PROMPT_NAME>",
      "prompt_input_variables": {"variable1": "value1", "variable2": "value2"},
      "request_id": "<REQUEST_ID>",
      "version": "<VERSION>"
  },
)
```


## OpenAPI

````yaml POST /rest/track-prompt
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /rest/track-prompt:
    post:
      tags:
        - prompt
      summary: Track Prompt
      operationId: trackPrompt
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: Your PromptLayer API Key.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt_name:
                  type: string
                  description: The name of the prompt template.
                  minLength: 1
                prompt_input_variables:
                  type: object
                  description: Input variables for the prompt template.
                  additionalProperties:
                    type: string
                  optional: true
                request_id:
                  type: integer
                  description: The unique identifier for the request.
                version:
                  type: integer
                  description: >-
                    The version of the prompt template. Both version and label
                    cannot be specified. Only one or none.
                  optional: true
                label:
                  type: string
                  description: >-
                    The label of the prompt template version. Both version and
                    label cannot be specified. Only one or none.
                  minLength: 1
                  maxLength: 512
                  optional: true
              required:
                - prompt_name
                - request_id
      responses:
        '200':
          description: Prompt tracked successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message
        '400':
          description: Bad Request
        '401':
          description: Unauthorized

````