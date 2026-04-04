# Source: https://docs.lunary.ai/docs/api/models/update-a-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a model



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/models/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/models/{id}:
    patch:
      tags:
        - Models
      summary: Update a model
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ModelInput'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model'
components:
  schemas:
    ModelInput:
      type: object
      required:
        - name
        - pattern
        - unit
        - inputCost
        - outputCost
      properties:
        name:
          type: string
        pattern:
          type: string
        unit:
          type: string
          enum:
            - TOKENS
            - CHARACTERS
            - MILLISECONDS
        inputCost:
          type: number
        outputCost:
          type: number
        tokenizer:
          type: string
        startDate:
          type: string
          format: date-time
    Model:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        pattern:
          type: string
        unit:
          type: string
          enum:
            - TOKENS
            - CHARACTERS
            - MILLISECONDS
        inputCost:
          type: number
        outputCost:
          type: number
        tokenizer:
          type: string
        startDate:
          type: string
          format: date-time
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

````