# Source: https://docs.vast.ai/api-reference/templates/delete-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# delete template

> Deletes an existing template.

Pass the template's numeric `id` (not `hash_id`) in the request body.

For detailed usage, see [Creating and Using Templates with API](/api-reference/creating-and-using-templates-with-api).

CLI Usage: `vastai delete template --template-id <id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/template/
openapi: 3.1.0
info:
  title: Vast.ai API
  description: >-
    Welcome to Vast.ai 's API documentation. Our API allows you to
    programmatically manage GPU instances, handle machine operations, and
    automate your AI/ML workflow. Whether you're running individual GPU
    instances or managing a fleet of machines, our API provides comprehensive
    control over all Vast.ai  platform features.
  version: 1.0.0
  contact:
    name: Vast.ai Support
    url: https://discord.gg/vast
servers:
  - url: https://console.vast.ai
    description: Production server
security:
  - BearerAuth: []
paths:
  /api/v0/template/:
    delete:
      tags:
        - Templates
      summary: delete template
      description: >-
        Deletes an existing template.


        Pass the template's numeric `id` (not `hash_id`) in the request body.


        For detailed usage, see [Creating and Using Templates with
        API](/api-reference/creating-and-using-templates-with-api).


        CLI Usage: `vastai delete template --template-id <id>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - template_id
              properties:
                template_id:
                  type: integer
                  description: Numeric ID of the template to delete (not hash_id)
            example:
              template_id: 334548
      responses:
        '200':
          description: Template deleted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
        '401':
          description: Unauthorized - invalid or missing API key
        '404':
          description: Template not found
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````