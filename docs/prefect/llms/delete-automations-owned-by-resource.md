# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/automations/delete-automations-owned-by-resource.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Automations Owned By Resource



## OpenAPI

````yaml delete /automations/owned-by/{resource_id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /automations/owned-by/{resource_id}:
    delete:
      tags:
        - Automations
      summary: Delete Automations Owned By Resource
      operationId: >-
        delete_automations_owned_by_resource_automations_owned_by__resource_id__delete
      parameters:
        - name: resource_id
          in: path
          required: true
          schema:
            type: string
            title: Resource Id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '202':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).