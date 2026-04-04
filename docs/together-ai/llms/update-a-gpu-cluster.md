# Source: https://docs.together.ai/api-reference/gpuclusterservice/update-a-gpu-cluster.md

# Update a GPU Cluster.



## OpenAPI

````yaml tcloud.yaml put /api/v1/gpu_cluster
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
  /api/v1/gpu_cluster:
    put:
      tags:
        - GPUClusterService
      summary: Update a GPU Cluster.
      operationId: GPUClusterService_Update
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GPUClusterUpdateRequest'
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GPUClusterUpdateResponse'
components:
  schemas:
    GPUClusterUpdateRequest:
      type: object
      properties:
        cluster_id:
          type: string
        cluster_type:
          enum:
            - UNKNOWN_TYPE
            - KUBERNETES
            - SLURM
          type: string
          format: enum
        num_gpus:
          type: integer
          format: uint32
    GPUClusterUpdateResponse:
      type: object
      properties:
        cluster_id:
          type: string
        status:
          enum:
            - UNKNOWN_STATUS
            - PENDING
            - QUEUED
            - WAITING_CONTROL_PLANE
            - WAITING_DATA_PLANE
            - READY
            - FAILED
          type: string
          format: enum
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt