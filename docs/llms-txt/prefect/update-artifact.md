# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/artifacts/update-artifact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Artifact

> Update an artifact in the database.



## OpenAPI

````yaml patch /artifacts/{id}
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
    patch:
      tags:
        - Artifacts
      summary: Update Artifact
      description: Update an artifact in the database.
      operationId: update_artifact_artifacts__id__patch
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The ID of the artifact to update.
            title: Id
          description: The ID of the artifact to update.
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
              $ref: '#/components/schemas/ArtifactUpdate'
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    ArtifactUpdate:
      properties:
        data:
          anyOf:
            - additionalProperties: true
              type: object
            - {}
            - type: 'null'
          title: Data
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        metadata_:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Metadata
      additionalProperties: false
      type: object
      title: ArtifactUpdate
      description: Data used by the Prefect REST API to update an artifact.
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