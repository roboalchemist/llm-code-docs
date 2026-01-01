# Source: https://docs.together.ai/api-reference/gpuclusterservice/create-gpu-cluster.md

# Create GPU Cluster



## OpenAPI

````yaml tcloud.yaml post /api/v1/gpu_cluster
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
    post:
      tags:
        - GPUClusterService
      summary: Create GPU Cluster
      operationId: GPUClusterService_Create
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GPUClusterCreateRequest'
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GPUClusterCreateResponse'
components:
  schemas:
    GPUClusterCreateRequest:
      required:
        - region
        - gpu_type
        - num_gpus
        - cluster_name
        - duration_days
        - driver_version
        - billing_type
      type: object
      properties:
        cluster_type:
          enum:
            - UNKNOWN_TYPE
            - KUBERNETES
            - SLURM
          type: string
          description: GPU Cluster create request.
          format: enum
        region:
          type: string
          description: >-
            Region to create the GPU cluster in. Valid values are us-central-8
            and us-central-4.
        gpu_type:
          enum:
            - UNKNOWN_GPU_TYPE
            - H100_SXM
            - H200_SXM
            - RTX_6000_PCI
          type: string
          description: Type of GPU to use in the cluster
          format: enum
        num_gpus:
          type: integer
          description: >-
            Number of GPUs to allocate in the cluster. This must be multiple of
            8. For example, 8, 16 or 24
          format: int32
        cluster_name:
          type: string
          description: Name of the GPU cluster.
        duration_days:
          type: integer
          description: Duration in days to keep the cluster running.
          format: uint32
        driver_version:
          enum:
            - UNKNOWN_DRIVER
            - CUDA_12_5_555
            - CUDA_12_6_560
            - CUDA_12_6_565
            - CUDA_12_8_570
          type: string
          description: NVIDIA driver version to use in the cluster.
          format: enum
        shared_volume:
          $ref: '#/components/schemas/SharedVolumeCreateRequest'
        volume_id:
          type: string
        billing_type:
          enum:
            - UNSPECIFIED
            - RESERVED
            - ON_DEMAND
          type: string
          format: enum
      description: GPU Cluster create request
    GPUClusterCreateResponse:
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt