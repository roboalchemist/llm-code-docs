# Source: https://docs.lunary.ai/docs/api/templates/list-all-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all templates

> List all the prompt templates in your project, along with their versions.
Useful for usecases where you might want to pre-load all the templates in your application.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/templates
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/templates:
    get:
      tags:
        - Templates
      summary: List all templates
      description: >
        List all the prompt templates in your project, along with their
        versions.

        Useful for usecases where you might want to pre-load all the templates
        in your application.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Template'
components:
  schemas:
    Template:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        slug:
          type: string
        mode:
          type: string
          enum:
            - text
            - openai
        createdAt:
          type: string
          format: date-time
        group:
          type: string
        projectId:
          type: string
        versions:
          type: array
          items:
            $ref: '#/components/schemas/TemplateVersion'
    TemplateVersion:
      type: object
      properties:
        id:
          type: string
        templateId:
          type: string
        content:
          type: array
          items:
            type: object
            properties:
              role:
                type: string
              content:
                type: string
        extra:
          type: object
        testValues:
          type: object
        isDraft:
          type: boolean
        notes:
          type: string
        createdAt:
          type: string
          format: date-time
        version:
          type: number

````