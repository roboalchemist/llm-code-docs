# Source: https://docs.together.ai/reference/clusters-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Cluster

> Create an Instant Cluster on Together's high-performance GPU clusters.
With features like on-demand scaling, long-lived resizable high-bandwidth shared DC-local storage,
Kubernetes and Slurm cluster flavors, a REST API, and Terraform support,
you can run workloads flexibly without complex infrastructure management.




## OpenAPI

````yaml POST /compute/clusters
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
  /compute/clusters:
    post:
      tags:
        - GPUClusterService
      summary: Create GPU Cluster
      description: >
        Create an Instant Cluster on Together's high-performance GPU clusters.

        With features like on-demand scaling, long-lived resizable
        high-bandwidth shared DC-local storage,

        Kubernetes and Slurm cluster flavors, a REST API, and Terraform support,

        you can run workloads flexibly without complex infrastructure
        management.
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
                $ref: '#/components/schemas/GPUClusterInfo'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together

            client = Together()

            response = client.beta.clusters.create(
              cluster_name="my-gpu-cluster",
              region="us-central-8",
              gpu_type="H100_SXM",
              num_gpus=8,
              driver_version="CUDA_12_6_560",
              billint_type="ON_DEMAND",
            )

            print(response.cluster_id)
        - lang: TypeScript
          label: Together AI SDK (v2)
          source: |
            import Together from "together-ai";

            const client = new Together();

            const response = await client.beta.clusters.create({
              cluster_name: "my-gpu-cluster",
              region: "us-central-8",
              gpu_type: "H100_SXM",
              num_gpus: 8,
              driver_version: "CUDA_12_6_560",
              billint_type: "ON_DEMAND",
            });

            console.log(response.cluster_id)
        - lang: JavaScript
          label: Together AI SDK (v2)
          source: |
            import Together from "together-ai";

            const client = new Together();

            const response = await client.beta.clusters.create({
              cluster_name: "my-gpu-cluster",
              region: "us-central-8",
              gpu_type: "H100_SXM",
              num_gpus: 8,
              driver_version: "CUDA_12_6_560",
              billint_type: "ON_DEMAND",
            });

            console.log(response.cluster_id)
        - lang: Shell
          label: CLI
          source: |
            curl -X POST \
                  -H "Authorization Bearer $TOGETHER_API_KEY" \
                  --data '{ "region": "us-west-2", "gpu_type": "H100_SXM", "num_gpus": 8, "cluster_name": "my-gpu-cluster", "driver_version": "CUDA_12_6_560" }' \
                  https://api.together.ai/v1/compute/clusters
components:
  schemas:
    GPUClusterCreateRequest:
      description: GPU Cluster create request
      required:
        - region
        - gpu_type
        - num_gpus
        - cluster_name
        - driver_version
        - billing_type
      type: object
      properties:
        cluster_type:
          description: Type of cluster to create.
          type: string
          enum:
            - KUBERNETES
            - SLURM
        region:
          description: >-
            Region to create the GPU cluster in. Usable regions can be found
            from `client.clusters.list_regions()`
          type: string
        gpu_type:
          description: Type of GPU to use in the cluster
          type: string
          enum:
            - H100_SXM
            - H200_SXM
            - RTX_6000_PCI
            - L40_PCIE
            - B200_SXM
            - H100_SXM_INF
        num_gpus:
          description: >-
            Number of GPUs to allocate in the cluster. This must be multiple of
            8. For example, 8, 16 or 24
          type: integer
        cluster_name:
          description: Name of the GPU cluster.
          type: string
        duration_days:
          x-stainless-terraform-configurability: computed
          description: Duration in days to keep the cluster running.
          type: integer
        driver_version:
          description: NVIDIA driver version to use in the cluster.
          type: string
          enum:
            - CUDA_12_5_555
            - CUDA_12_6_560
            - CUDA_12_6_565
            - CUDA_12_8_570
        shared_volume:
          $ref: '#/components/schemas/GPUClustersSharedVolumeCreateRequest'
          x-stainless-terraform-configurability: computed
          description: >-
            Inline configuration to create a shared volume with the cluster
            creation.
        volume_id:
          description: ID of an existing volume to use with the cluster creation.
          type: string
        billing_type:
          description: >
            RESERVED billing types allow you to specify the duration of the
            cluster reservation via the duration_days field.

            ON_DEMAND billing types will give you ownership of the cluster until
            you delete it.
          x-stainless-terraform-configurability: computed
          type: string
          enum:
            - RESERVED
            - ON_DEMAND
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
    GPUClustersSharedVolumeCreateRequest:
      type: object
      required:
        - volume_name
        - size_tib
        - region
      properties:
        volume_name:
          description: Customizable name of the volume to create.
          type: string
        size_tib:
          description: Volume size in whole tebibytes (TiB).
          type: integer
        region:
          type: string
          description: >-
            Region name. Usable regions can be found from
            `client.clusters.list_regions()`
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