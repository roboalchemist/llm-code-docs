# Source: https://docs.together.ai/api-reference/sharedvolumeservice/list-all-shared-volumes.md

# List all shared volumes.



## OpenAPI

````yaml tcloud.yaml get /api/v1/shared_volumes
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
  /api/v1/shared_volumes:
    get:
      tags:
        - SharedVolumeService
      summary: List all shared volumes.
      operationId: SharedVolumeService_List
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SharedVolumes'
components:
  schemas:
    SharedVolumes:
      type: object
      properties:
        volumes:
          type: array
          items:
            $ref: '#/components/schemas/SharedVolumeInfo'
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