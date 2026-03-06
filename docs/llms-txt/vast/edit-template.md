# Source: https://docs.vast.ai/api-reference/templates/edit-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# edit template

> Edits an existing template in place.

Templates are mutable. Use PUT with the template's `hash_id` to update it. You only need to include the fields you want to change - unchanged fields retain their existing values.

Note: The template's `hash_id` will change after editing (since it's content-based), but the numeric `id` stays the same.

For detailed usage, see [Creating and Using Templates with API](/api-reference/creating-and-using-templates-with-api).

CLI Usage: `vastai update template <hash_id> [options]`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/template/
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
    put:
      tags:
        - Templates
      summary: edit template
      description: >-
        Edits an existing template in place.


        Templates are mutable. Use PUT with the template's `hash_id` to update
        it. You only need to include the fields you want to change - unchanged
        fields retain their existing values.


        Note: The template's `hash_id` will change after editing (since it's
        content-based), but the numeric `id` stays the same.


        For detailed usage, see [Creating and Using Templates with
        API](/api-reference/creating-and-using-templates-with-api).


        CLI Usage: `vastai update template <hash_id> [options]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - hash_id
              properties:
                hash_id:
                  type: string
                  description: >-
                    Hash ID of the template to edit. Required for identifying
                    which template to update.
                name:
                  type: string
                  description: Name of the template
                image:
                  type: string
                  description: Docker image path
                desc:
                  type: string
                  description: Short description of the template
                recommended_disk_space:
                  type: number
                  description: Recommended disk space in GB
              additionalProperties: true
            example:
              hash_id: 5915f1dc1ce881defb572015eb9d8178
              desc: Updated description
              recommended_disk_space: 16
      responses:
        '200':
          description: Template updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  template:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: Template numeric ID (unchanged after edit)
                      hash_id:
                        type: string
                        description: Updated template hash ID (changes based on content)
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