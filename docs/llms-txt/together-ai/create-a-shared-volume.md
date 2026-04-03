# Source: https://docs.together.ai/api-reference/sharedvolumeservice/create-a-shared-volume.md

# Create a shared volume.



## OpenAPI

````yaml tcloud.yaml post /api/v1/shared_volume
openapi: 3.0.3
info:
  title: ''
  version: 0.0.1
servers: []
security:
  - bearerAuth: []
tags:
  - name: GPUClusterService
  - name: RegionService
  - name: SharedVolumeService
paths:
  /api/v1/shared_volume:
    post:
      tags:
        - SharedVolumeService
      summary: Create a shared volume.
      operationId: SharedVolumeService_Create
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SharedVolumeCreateRequest'
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SharedVolumeCreateResponse'
components:
  schemas:
    SharedVolumeCreateRequest:
      type: object
      properties:
        volume_name:
          type: string
        size_tib:
          type: integer
          description: Volume size in whole tebibytes (TiB).
          format: uint32
        region:
          type: string
    SharedVolumeCreateResponse:
      type: object
      properties:
        volume_id:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt