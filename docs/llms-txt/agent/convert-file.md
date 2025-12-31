# Source: https://docs.agent.ai/api-reference/advanced/convert-file.md

# Convert file

> Convert a file to a different format.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/convert_file
paths:
  path: /action/convert_file
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
              input_file:
                allOf:
                  - type: string
                    description: Input file URL
                    example: https://www.irs.gov/pub/irs-pdf/fw4.pdf
              convert_to_extension:
                allOf:
                  - type: string
                    description: Desired output file extension (e.g., pdf, txt, png).
                    example: txt
            required: true
            requiredProperties:
              - input_file
              - convert_to_extension
        examples:
          example:
            value:
              input_file: https://www.irs.gov/pub/irs-pdf/fw4.pdf
              convert_to_extension: txt
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                - contents: |-
                    Form

                    W-4

                    Department of the Treasury
                    Internal Revenue Service

                    Step 1:
                    Enter
                    Personal
                    Information

                    Employee’s Withholding Certificate

                    OMB No. 1545-0074...
                  url: >-
                    https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/wka0ndlr_fw4.txt
        description: Converted file(s)
  deprecated: false
  type: path
components:
  schemas: {}

````