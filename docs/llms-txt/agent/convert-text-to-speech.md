# Source: https://docs.agent.ai/api-reference/use-ai/convert-text-to-speech.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Convert text to speech

> Convert text to a generated audio voice file.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/output_audio
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
  /action/output_audio:
    post:
      tags:
        - Use AI
      summary: Convert text to speech
      description: Convert text to a generated audio voice file.
      operationId: outputAudio
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                text_to_speech:
                  type: string
                  description: Text to convert to speech.
              required:
                - output_variable_name
      responses:
        '200':
          description: Generated audio output
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response: >-
                  https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/4oi2001mommncnj6.mp3
        '400':
          description: Generated audio output
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 400
                error: Input text_to_speech is not provided.
                response: null
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