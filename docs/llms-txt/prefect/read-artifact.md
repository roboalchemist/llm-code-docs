# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/artifacts/read-artifact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Artifact

> Retrieve an artifact from the database.



## OpenAPI

````yaml get /artifacts/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /artifacts/{id}:
    get:
      tags:
        - Artifacts
      summary: Read Artifact
      description: Retrieve an artifact from the database.
      operationId: read_artifact_artifacts__id__get
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The ID of the artifact to retrieve.
            title: Id
          description: The ID of the artifact to retrieve.
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
              schema:
                $ref: '#/components/schemas/Artifact'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Artifact:
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
        key:
          anyOf:
            - type: string
            - type: 'null'
          title: Key
          description: An optional unique reference key for this artifact.
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
          description: >-
            An identifier that describes the shape of the data field. e.g.
            'result', 'table', 'markdown'
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A markdown-enabled description of the artifact.
        data:
          anyOf:
            - additionalProperties: true
              type: object
            - {}
            - type: 'null'
          title: Data
          description: >-
            Data associated with the artifact, e.g. a result.; structure depends
            on the artifact type.
        metadata_:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Metadata
          description: >-
            User-defined artifact metadata. Content must be string key and value
            pairs.
        flow_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Flow Run Id
          description: The flow run associated with the artifact.
        task_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Task Run Id
          description: The task run associated with the artifact.
      type: object
      required: []
      title: Artifact
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