# Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/delete-an-auto-monitor-setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an auto monitor setup

> Delete an auto monitor setup by ID



## OpenAPI

````yaml delete /v2/auto-monitor-setups/{setup_id}
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/auto-monitor-setups/{setup_id}:
    delete:
      tags:
        - auto-monitor-setups
      summary: Delete an auto monitor setup
      description: Delete an auto monitor setup by ID
      parameters:
        - description: Auto monitor setup ID
          in: path
          name: setup_id
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No content
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
components:
  schemas:
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object

````