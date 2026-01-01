# Source: https://docs.together.ai/api-reference/gpuclusterservice/delete-gpu-cluster-by-cluster-id.md

# Delete GPU cluster by cluster ID



## OpenAPI

````yaml tcloud.yaml delete /api/v1/gpu_cluster/{cluster_id}
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
  /api/v1/gpu_cluster/{cluster_id}:
    delete:
      tags:
        - GPUClusterService
      summary: Delete GPU cluster by cluster ID
      operationId: GPUClusterService_Delete
      parameters:
        - name: cluster_id
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
                $ref: '#/components/schemas/GPUCLusterDeleteResponse'
components:
  schemas:
    GPUCLusterDeleteResponse:
      type: object
      properties:
        cluster_id:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt