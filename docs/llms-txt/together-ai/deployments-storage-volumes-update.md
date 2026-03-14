# Source: https://docs.together.ai/reference/deployments-storage-volumes-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Storage Volume

> Update an existing volume's configuration or contents



## OpenAPI

````yaml PATCH /deployments/storage/volumes/{id}
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
    patch:
      tags:
        - Volumes
      summary: Update a volume
      description: Update an existing volume's configuration or contents
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Volume ID or name.
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateVolumeRequest'
        description: Updated volume configuration
        required: true
      responses:
        '200':
          description: Volume updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VolumeResponseItem'
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                type: object
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
    UpdateVolumeRequest:
      properties:
        content:
          allOf:
            - $ref: '#/components/schemas/VolumeContent'
          description: >-
            Content specifies the new content that will be preloaded to this
            volume
        name:
          description: Name is the new unique identifier for the volume within the project
          type: string
        type:
          allOf:
            - $ref: '#/components/schemas/VolumeType'
          description: Type is the new volume type (currently only "readOnly" is supported)
      type: object
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