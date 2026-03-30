# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/deployments/pause-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Pause Deployment

> Set a deployment schedule to inactive. Any auto-scheduled runs still in a Scheduled
state will be deleted.



## OpenAPI

````yaml post /deployments/{id}/pause_deployment
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /deployments/{id}/pause_deployment:
    post:
      tags:
        - Deployments
      summary: Pause Deployment
      description: >-
        Set a deployment schedule to inactive. Any auto-scheduled runs still in
        a Scheduled

        state will be deleted.
      operationId: pause_deployment_deployments__id__pause_deployment_post
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The deployment id
            title: Id
          description: The deployment id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
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