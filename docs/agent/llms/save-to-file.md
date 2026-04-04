# Source: https://docs.agent.ai/api-reference/create-output/save-to-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save To File

> Save text content as a downloadable file.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/create_file
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
  /action/create_file:
    post:
      tags:
        - Create Output
      summary: Save To File
      description: Save text content as a downloadable file.
      operationId: createFile
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                file_type:
                  type: string
                  description: Enter the output file type (i.e. PDF).
                  enum:
                    - pdf
                    - docx
                    - html
                    - md
                    - odt
                    - tex
                    - azw3
                    - epub
                    - png
                  default: pdf
                  example: pdf
                body:
                  type: string
                  description: >-
                    Provide the content to be saved in the file, including text,
                    bullet points, or other structured information.
                  example: >-
                    # Sample Document


                    This is a sample document content that will be saved to a
                    file.
                output_variable_name:
                  type: string
                  description: Provide a variable name to store the file URL to.
                  pattern: ^[a-zA-Z0-9_]+$
                  example: saved_file
              required:
                - file_type
                - body
                - output_variable_name
      responses:
        '200':
          description: File saved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  saved_file: https://s3.example.com/asset-uploads/document.pdf
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: 27e26f0a-03fc-41c2-8449-79257ca914c7
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