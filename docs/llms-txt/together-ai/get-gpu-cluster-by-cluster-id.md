# Source: https://docs.together.ai/api-reference/gpuclusterservice/get-gpu-cluster-by-cluster-id.md

# Get GPU cluster by cluster ID



## OpenAPI

````yaml tcloud.yaml get /api/v1/gpu_cluster/{cluster_id}
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
    get:
      tags:
        - GPUClusterService
      summary: Get GPU cluster by cluster ID
      operationId: GPUClusterService_Get
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
                $ref: '#/components/schemas/GPUClusterInfo'
components:
  schemas:
    GPUClusterInfo:
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
        region:
          type: string
        gpu_type:
          enum:
            - UNKNOWN_GPU_TYPE
            - H100_SXM
            - H200_SXM
            - RTX_6000_PCI
          type: string
          format: enum
        cluster_name:
          type: string
        duration_hours:
          type: integer
          format: uint32
        driver_version:
          enum:
            - UNKNOWN_DRIVER
            - CUDA_12_5_555
            - CUDA_12_6_560
            - CUDA_12_6_565
            - CUDA_12_8_570
          type: string
          format: enum
        volumes:
          type: array
          items:
            $ref: '#/components/schemas/GPUClusterVolume'
        status:
          type: string
        control_plane_nodes:
          type: array
          items:
            $ref: '#/components/schemas/GPUClusterControlPlaneNode'
        gpu_worker_nodes:
          type: array
          items:
            $ref: '#/components/schemas/GPUClusterGPUWorkerNode'
        kube_config:
          type: string
        num_gpus:
          type: integer
          format: int32
    GPUClusterVolume:
      type: object
      properties:
        volume_id:
          type: string
        volume_name:
          type: string
        size_tib:
          type: integer
          format: uint32
        status:
          type: string
    GPUClusterControlPlaneNode:
      type: object
      properties:
        node_id:
          type: string
        node_name:
          type: string
        status:
          type: string
        host_name:
          type: string
        num_cpu_cores:
          type: integer
          format: uint32
        memory_gib:
          type: number
          format: float
        network:
          type: string
    GPUClusterGPUWorkerNode:
      type: object
      properties:
        node_id:
          type: string
        node_name:
          type: string
        status:
          type: string
        host_name:
          type: string
        num_cpu_cores:
          type: integer
          format: uint32
        num_gpus:
          type: integer
          format: uint32
        memory_gib:
          type: number
          format: float
        networks:
          type: array
          items:
            type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt