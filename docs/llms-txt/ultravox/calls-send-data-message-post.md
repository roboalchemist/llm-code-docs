# Source: https://docs.ultravox.ai/api-reference/calls/calls-send-data-message-post.md

# Send Data Message to Call

> Sends a data message to a live call

The request body for this API is determined by the type of message being sent. See [Data Messages](/apps/datamessages) for details.


## OpenAPI

````yaml post /api/calls/{call_id}/send_data_message
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/send_data_message:
    post:
      tags:
        - calls
      operationId: send_data_message_to_call
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendCallDataMessage'
        required: true
      responses:
        '204':
          description: No response body
      security:
        - apiKeyAuth: []
components:
  schemas:
    SendCallDataMessage:
      type: object
      description: A data message to send to a call.
      properties:
        type:
          type: string
          description: The type of the data message.
      required:
        - type
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt