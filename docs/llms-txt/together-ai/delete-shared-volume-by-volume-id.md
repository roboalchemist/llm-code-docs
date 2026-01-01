# Source: https://docs.together.ai/api-reference/sharedvolumeservice/delete-shared-volume-by-volume-id.md

# Delete shared volume by volume id.



## OpenAPI

````yaml tcloud.yaml delete /api/v1/shared_volume/{volume_id}
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
    delete:
      tags:
        - SharedVolumeService
      summary: Delete shared volume by volume id.
      operationId: SharedVolumeService_Delete
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
                $ref: '#/components/schemas/SharedVolumeDeleteResponse'
components:
  schemas:
    SharedVolumeDeleteResponse:
      type: object
      properties:
        success:
          type: boolean
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt