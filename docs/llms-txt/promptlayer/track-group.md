# Source: https://docs.promptlayer.com/reference/track-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track Group

Associate a group with a request.

## Example Code

```python  theme={null}
pl_group_id = promptlayer_client.group.create()

import requests
response = requests.post(
  "https://api.promptlayer.com/rest/track-group",
  headers={"X-API-KEY": "<YOUR_API_KEY>"},
  json={
      "request_id": "<REQUEST_ID>",
      "group_id": pl_group_id,
  },
)
```


## OpenAPI

````yaml POST /rest/track-group
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /rest/track-group:
    post:
      tags:
        - group
      summary: Track Group
      operationId: trackGroup
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
                request_id:
                  type: integer
                  description: The unique identifier for the request.
                group_id:
                  type: integer
                  description: >-
                    The unique identifier for the group to be associated with
                    the request.
              required:
                - request_id
                - group_id
      responses:
        '200':
          description: Group tracked successfully
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