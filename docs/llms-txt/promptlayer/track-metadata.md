# Source: https://docs.promptlayer.com/reference/track-metadata.md

# Track Metadata

Associate a metadata dictionary with a request. This can be used for things like session\_ids, user\_ids, location, etc.

## Example Code

```python  theme={null}
import requests
response = requests.post(
  "https://api.promptlayer.com/rest/track-metadata",
  json={
      "api_key": "<YOUR_API_KEY>",
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
                - api_key
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt