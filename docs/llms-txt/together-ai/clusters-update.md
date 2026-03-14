# Source: https://docs.together.ai/reference/clusters-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update or Scale GPU Cluster

> Update the configuration of an existing GPU cluster.



## OpenAPI

````yaml PUT /compute/clusters/{cluster_id}
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
  /compute/clusters/{cluster_id}:
    put:
      tags:
        - GPUClusterService
      summary: Update a GPU Cluster.
      description: Update the configuration of an existing GPU cluster.
      operationId: GPUClusterService_Update
      parameters:
        - name: cluster_id
          in: path
          required: true
          schema:
            description: The ID of the cluster to update
            type: string
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
                $ref: '#/components/schemas/GPUClusterInfo'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: >
            from together import Together

            client = Together()


            cluster = client.beta.clusters.update("cluster_id",
            cluster_type="KUBERNETES", num_gpus=24)

            print(cluster)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const cluster = await client.beta.clusters.update({
              cluster_id: "cluster_id",
              cluster_type: "kubernetes",
              num_gpus: 24,
            })
            console.log(cluster)
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const cluster = await client.beta.clusters.update({
              cluster_id: "cluster_id",
              cluster_type: "kubernetes",
              num_gpus: 24,
            })
            console.log(cluster)
        - lang: Shell
          label: cURL
          source: |
            curl -X PUT \
                  -H "Authorization Bearer $TOGETHER_API_KEY" \
                  --data '{ "cluster_id": "cluster id", "cluster_type": "kubernetes", "num_gpus": 24 }' \
                  https://api.together.ai/v1/compute/clusters
components:
  schemas:
    GPUClusterUpdateRequest:
      type: object
      properties:
        cluster_type:
          description: Type of cluster to update.
          enum:
            - KUBERNETES
            - SLURM
        num_gpus:
          description: >-
            Number of GPUs to allocate in the cluster. This must be multiple of
            8. For example, 8, 16 or 24
          type: integer
    GPUClusterInfo:
      type: object
      required:
        - cluster_id
        - cluster_type
        - region
        - gpu_type
        - cluster_name
        - duration_hours
        - driver_version
        - volumes
        - status
        - control_plane_nodes
        - gpu_worker_nodes
        - kube_config
        - num_gpus
      properties:
        cluster_id:
          type: string
        cluster_type:
          description: Type of cluster.
          enum:
            - KUBERNETES
            - SLURM
        region:
          type: string
        gpu_type:
          enum:
            - H100_SXM
            - H200_SXM
            - RTX_6000_PCI
            - L40_PCIE
            - B200_SXM
            - H100_SXM_INF
        cluster_name:
          type: string
        duration_hours:
          type: integer
        driver_version:
          enum:
            - CUDA_12_5_555
            - CUDA_12_6_560
            - CUDA_12_6_565
            - CUDA_12_8_570
        volumes:
          type: array
          items:
            $ref: '#/components/schemas/GPUClusterVolume'
        status:
          description: Current status of the GPU cluster.
          enum:
            - WaitingForControlPlaneNodes
            - WaitingForDataPlaneNodes
            - WaitingForSubnet
            - WaitingForSharedVolume
            - InstallingDrivers
            - RunningAcceptanceTests
            - Paused
            - OnDemandComputePaused
            - Ready
            - Degraded
            - Deleting
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
    GPUClusterVolume:
      type: object
      required:
        - volume_id
        - volume_name
        - size_tib
        - status
      properties:
        volume_id:
          type: string
        volume_name:
          type: string
        size_tib:
          type: integer
        status:
          type: string
    GPUClusterControlPlaneNode:
      type: object
      required:
        - node_id
        - node_name
        - status
        - host_name
        - num_cpu_cores
        - memory_gib
        - network
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
        memory_gib:
          type: number
        network:
          type: string
    GPUClusterGPUWorkerNode:
      type: object
      required:
        - node_id
        - node_name
        - status
        - host_name
        - num_cpu_cores
        - num_gpus
        - memory_gib
        - networks
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
        num_gpus:
          type: integer
        memory_gib:
          type: number
        networks:
          type: array
          items:
            type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).