# Source: https://docs.together.ai/reference/deployments-storage-volumes-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Storage Volumes

> Retrieve all volumes in your project



## OpenAPI

````yaml GET /deployments/storage/volumes
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
  /deployments/storage/volumes:
    get:
      tags:
        - DeploymentsVolumes
      summary: Get the list of project volumes
      description: Retrieve all volumes in your project
      responses:
        '200':
          description: List of volumes
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListVolumesResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together
            client = Together()

            volumes = client.beta.jig.storage.volumes.list()
            print(volumes)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const volumes = await client.beta.jig.storage.volumes.list();
            console.log(volumes);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const volumes = await client.beta.jig.storage.volumes.list();
            console.log(volumes);
        - lang: Shell
          label: cURL
          source: |
            curl -X GET \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/deployments/storage/volumes
components:
  schemas:
    ListVolumesResponse:
      properties:
        data:
          description: Data is the array of volume items
          items:
            $ref: '#/components/schemas/VolumeResponseItem'
          type: array
        object:
          description: The object type, which is always `list`.
          const: list
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