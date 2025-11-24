# Source: https://docs.agent.ai/api-reference/get-data/web-page-screenshot.md

# Web Page Screenshot

> Capture a visual screenshot of a specified web page for documentation or analysis.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/grab_web_screenshot
paths:
  path: /action/grab_web_screenshot
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - type: string
                    format: url
                    description: URL of the web page to capture.
                    example: https://agent.ai
              ttl_for_screenshot:
                allOf:
                  - type: integer
                    format: int64
                    enum:
                      - 3600
                      - 86400
                      - 604800
                      - 18144000
                    default: 86400
                    description: Cache expiration time for the screenshot in seconds.
            required: true
            requiredProperties:
              - url
        examples:
          example:
            value:
              url: https://agent.ai
              ttl_for_screenshot: 86400
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_0
                    type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - &ref_1
                    type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response: >-
                https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/31d8f9c8-27ce-42bf-a38c-ce02784ab98c.png
        description: Screenshot of the web page
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              response:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 500
              response: null
              error: Error uploading screenshot to S3
        description: Screenshot of the web page
  deprecated: false
  type: path
components:
  schemas: {}

````