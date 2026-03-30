# Source: https://docs.together.ai/reference/clusters_storages-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a shared volume

> Instant Clusters supports long-lived, resizable in-DC shared storage with user data persistence.
You can dynamically create and attach volumes to your cluster at cluster creation time, and resize as your data grows.
All shared storage is backed by multi-NIC bare metal paths, ensuring high-throughput and low-latency performance for shared storage.




## OpenAPI

````yaml POST /compute/clusters/storage/volumes
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
  /compute/clusters/storage/volumes:
    post:
      tags:
        - SharedVolumeService
      summary: Create a shared volume.
      description: >
        Instant Clusters supports long-lived, resizable in-DC shared storage
        with user data persistence.

        You can dynamically create and attach volumes to your cluster at cluster
        creation time, and resize as your data grows.

        All shared storage is backed by multi-NIC bare metal paths, ensuring
        high-throughput and low-latency performance for shared storage.
      operationId: SharedVolumeService_Create
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GPUClustersSharedVolumeCreateRequest'
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GPUClustersSharedVolume'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together
            client = Together()

            volume = client.beta.clusters.storage.create(
              volume_name="my-shared-volume",
              size_tib=2,
              region="us-west-2"
            )
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const volume = await client.beta.clusters.storage.create({
              volume_name: "my-shared-volume",
              size_tib: 2,
              region: "us-west-2"
            });
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const volume = await client.beta.clusters.storage.create({
              volume_name: "my-shared-volume",
              size_tib: 2,
              region: "us-west-2"
            });
        - lang: Shell
          label: cURL
          source: |
            curl -X POST \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  --data '{ "volume_name": "my-shared-volume", "size_tib": 2, "region": "us-west-2" }' \
                  https://api.together.ai/v1/compute/clusters/storage/volumes
components:
  schemas:
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
    GPUClustersSharedVolume:
      type: object
      required:
        - volume_id
        - volume_name
        - size_tib
        - status
      properties:
        volume_id:
          description: ID of the volume.
          type: string
        volume_name:
          description: Provided name of the volume.
          type: string
        size_tib:
          description: Size of the volume in whole tebibytes (TiB).
          type: integer
        status:
          description: Deployment status of the volume.
          type: string
          enum:
            - available
            - bound
            - provisioning
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).