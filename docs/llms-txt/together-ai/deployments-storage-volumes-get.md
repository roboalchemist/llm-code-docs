# Source: https://docs.together.ai/reference/deployments-storage-volumes-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Storage Volume

> Retrieve details of a specific volume by its ID or name



## OpenAPI

````yaml GET /deployments/storage/volumes/{id}
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /deployments/storage/volumes/{id}:
    get:
      tags:
        - Volumes
      summary: Get a volume by ID or name
      description: Retrieve details of a specific volume by its ID or name
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Volume ID or name
            type: string
      responses:
        '200':
          description: Volume details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VolumeResponseItem'
        '404':
          description: Volume not found
          content:
            application/json:
              schema:
                type: object
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
components:
  schemas:
    VolumeResponseItem:
      properties:
        content:
          allOf:
            - $ref: '#/components/schemas/VolumeContent'
          description: Content specifies the content that will be preloaded to this volume
        created_at:
          description: CreatedAt is the ISO8601 timestamp when this volume was created
          type: string
        id:
          description: ID is the unique identifier for this volume
          type: string
        name:
          description: Name is the name of the volume
          type: string
        object:
          description: The object type, which is always `volume`.
          const: volume
        type:
          allOf:
            - $ref: '#/components/schemas/VolumeType'
          description: Type is the volume type (e.g., "readOnly")
        updated_at:
          description: UpdatedAt is the ISO8601 timestamp when this volume was last updated
          type: string
      type: object
    VolumeContent:
      properties:
        source_prefix:
          description: >-
            SourcePrefix is the file path prefix for the content to be preloaded
            into the volume
          example: models/
          type: string
        type:
          description: >-
            Type is the content type (currently only "files" is supported which
            allows preloading files uploaded via Files API into the volume)
          enum:
            - files
          example: files
          type: string
      type: object
    VolumeType:
      enum:
        - readOnly
      type: string
      x-enum-varnames:
        - VolumeTypeReadOnly
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).