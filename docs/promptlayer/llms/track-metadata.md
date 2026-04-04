# Source: https://docs.promptlayer.com/reference/track-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track Metadata

Associate a metadata dictionary with a request. This can be used for things like session\_ids, user\_ids, location, etc.

## Example Code

```python  theme={null}
import requests
response = requests.post(
  "https://api.promptlayer.com/rest/track-metadata",
  headers={"X-API-KEY": "<YOUR_API_KEY>"},
  json={
      "request_id": "<REQUEST_ID>",
      "metadata": {"session_id": "abc123", "user_id": "user123"}
  },
)
```


## OpenAPI

````yaml POST /rest/track-metadata
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /rest/track-metadata:
    post:
      tags:
        - metadata
      summary: Track Metadata
      operationId: trackMetadata
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
                  description: >-
                    The unique identifier for the request to which the metadata
                    is associated.
                metadata:
                  type: object
                  additionalProperties: true
                  description: >-
                    A dictionary of metadata items to associate with the
                    request. Can include session_ids, user_ids, location, etc.
              required:
                - request_id
                - metadata
      responses:
        '200':
          description: Metadata tracked successfully
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