# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flows/create-flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Flow

> Creates a new flow from the provided schema. If a flow with the
same name already exists, the existing flow is returned.

For more information, see https://docs.prefect.io/v3/concepts/flows.



## OpenAPI

````yaml post /flows/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flows/:
    post:
      tags:
        - Flows
      summary: Create Flow
      description: |-
        Creates a new flow from the provided schema. If a flow with the
        same name already exists, the existing flow is returned.

        For more information, see https://docs.prefect.io/v3/concepts/flows.
      operationId: create_flow_flows__post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FlowCreate'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Flow'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    FlowCreate:
      properties:
        name:
          type: string
          pattern: ^[^/%&><]+$
          title: Name
          description: The name of the flow
          examples:
            - my-flow
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of flow tags
          examples:
            - - tag-1
              - tag-2
        labels:
          anyOf:
            - additionalProperties:
                anyOf:
                  - type: boolean
                  - type: integer
                  - type: number
                  - type: string
              type: object
            - type: 'null'
          title: Labels
          description: >-
            A dictionary of key-value labels. Values can be strings, numbers, or
            booleans.
          examples:
            - key: value1
              key2: 42
      additionalProperties: false
      type: object
      required:
        - name
      title: FlowCreate
      description: Data used by the Prefect REST API to create a flow.
    Flow:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        name:
          type: string
          pattern: ^[^/%&><]+$
          title: Name
          description: The name of the flow
          examples:
            - my-flow
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of flow tags
          examples:
            - - tag-1
              - tag-2
        labels:
          anyOf:
            - additionalProperties:
                anyOf:
                  - type: boolean
                  - type: integer
                  - type: number
                  - type: string
              type: object
            - type: 'null'
          title: Labels
          description: >-
            A dictionary of key-value labels. Values can be strings, numbers, or
            booleans.
          examples:
            - key: value1
              key2: 42
      type: object
      required:
        - name
        - id
        - created
        - updated
      title: Flow
      description: An ORM representation of flow data.
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