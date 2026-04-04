# Source: https://docs.lunary.ai/docs/api/models/create-a-new-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new model



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/models
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/models:
    post:
      tags:
        - Models
      summary: Create a new model
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