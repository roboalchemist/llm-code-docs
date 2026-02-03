# Source: https://docs.agent.ai/api-reference/advanced/convert-file-options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Convert file options

> Gets the full set of options that a file extension can be converted to.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/convert_file_options
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
  /action/convert_file_options:
    post:
      tags:
        - Advanced
      summary: Convert file options
      description: Gets the full set of options that a file extension can be converted to.
      operationId: convertFileOptions
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                extension:
                  type: string
                  description: File extension
                  example: txt
              required:
                - extension
      responses:
        '200':
          description: Convert file options
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  - doc
                  - docx
                  - html
                  - md
                  - odt
                  - pdf
                  - rtf
                  - tex
                  - azw3
                  - epub
                  - lrf
                  - mobi
                  - oeb
                  - pdb
                  - jpg
                  - png
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