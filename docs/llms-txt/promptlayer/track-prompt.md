# Source: https://docs.promptlayer.com/reference/track-prompt.md

# Track Prompt

Associate a prompt template with a request.

## Example Code

```python  theme={null}
import requests
response = requests.post(
  "https://api.promptlayer.com/rest/track-prompt",
  json={
      "api_key": "<YOUR_API_KEY>",
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                api_key:
                  type: string
                  description: Your PromptLayer API Key.
                  minLength: 1
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
                - api_key
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt