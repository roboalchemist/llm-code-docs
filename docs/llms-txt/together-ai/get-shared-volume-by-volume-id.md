# Source: https://docs.together.ai/api-reference/sharedvolumeservice/get-shared-volume-by-volume-id.md

# Get shared volume by volume Id.



## OpenAPI

````yaml tcloud.yaml get /api/v1/shared_volume/{volume_id}
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
  /api/v1/shared_volume/{volume_id}:
    get:
      tags:
        - SharedVolumeService
      summary: Get shared volume by volume Id.
      operationId: SharedVolumeService_Get
      parameters:
        - name: volume_id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SharedVolumeInfo'
components:
  schemas:
    SharedVolumeInfo:
      type: object
      properties:
        volume_id:
          type: string
        volume_name:
          type: string
        size_tib:
          type: integer
          format: uint32
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt