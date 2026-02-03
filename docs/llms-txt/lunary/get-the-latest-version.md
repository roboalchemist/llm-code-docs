# Source: https://docs.lunary.ai/docs/api/templates/get-the-latest-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the latest version

> This is the most common endpoint you'll use when working with prompt templates.

This route is used by the Lunary SDKs to fetch the latest version of a template before making an LLM call.

This route differs from all the next ones in that:
- it requires only the `slug` parameter to reference a template
- it doesn't require using a Private Key to authenticate the request (Public Key is enough)




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/template-versions/latest
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/template-versions/latest:
    get:
      tags:
        - Templates
      summary: Get the latest version
      description: >
        This is the most common endpoint you'll use when working with prompt
        templates.


        This route is used by the Lunary SDKs to fetch the latest version of a
        template before making an LLM call.


        This route differs from all the next ones in that:

        - it requires only the `slug` parameter to reference a template

        - it doesn't require using a Private Key to authenticate the request
        (Public Key is enough)
      parameters:
        - in: query
          name: slug
          required: true
          schema:
            type: string
          description: Slug of the template
      responses:
        '200':
          description: Latest version of the template
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TemplateVersion'
        '404':
          description: Template not found
components:
  schemas:
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