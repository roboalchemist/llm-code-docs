# Source: https://docs.agent.ai/api-reference/advanced/convert-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Convert file

> Convert a file to a different format.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/convert_file
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
  /action/convert_file:
    post:
      tags:
        - Advanced
      summary: Convert file
      description: Convert a file to a different format.
      operationId: convertFile
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                input_file:
                  type: string
                  description: Input file URL
                  example: https://www.irs.gov/pub/irs-pdf/fw4.pdf
                convert_to_extension:
                  type: string
                  description: Desired output file extension (e.g., pdf, txt, png).
                  example: txt
              required:
                - input_file
                - convert_to_extension
      responses:
        '200':
          description: Converted file(s)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
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