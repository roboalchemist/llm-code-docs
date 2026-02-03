# Source: https://docs.agent.ai/api-reference/get-data/web-page-screenshot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Page Screenshot

> Capture a visual screenshot of a specified web page for documentation or analysis.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/grab_web_screenshot
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/grab_web_screenshot:
    post:
      tags:
        - Get Data
      summary: Web Page Screenshot
      description: >-
        Capture a visual screenshot of a specified web page for documentation or
        analysis.
      operationId: grabWebScreenshot
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  format: url
                  description: URL of the web page to capture.
                  example: https://agent.ai
                ttl_for_screenshot:
                  type: integer
                  format: int64
                  enum:
                    - 3600
                    - 86400
                    - 604800
                    - 18144000
                  default: 86400
                  description: Cache expiration time for the screenshot in seconds.
              required:
                - url
      responses:
        '200':
          description: Screenshot of the web page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response: >-
                  https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/31d8f9c8-27ce-42bf-a38c-ce02784ab98c.png
        '500':
          description: Screenshot of the web page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 500
                response: null
                error: Error uploading screenshot to S3
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````