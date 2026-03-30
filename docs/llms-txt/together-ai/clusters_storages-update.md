# Source: https://docs.together.ai/reference/clusters_storages-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a shared volume

> Update the configuration of an existing shared volume.




## OpenAPI

````yaml PUT /compute/clusters/storage/volumes
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
    put:
      tags:
        - SharedVolumeService
      summary: Update a shared volume.
      description: |
        Update the configuration of an existing shared volume.
      operationId: SharedVolumeService_Update
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GPUClustersSharedVolumeUpdateRequest'
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

            volume = client.beta.clusters.storage.update(
              volume_id="12345-67890-12345-67890",
              size_tib=3
            )
            print(volume)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const volume = await client.beta.clusters.storage.update({
              volume_id: "12345-67890-12345-67890",
              size_tib: 3
            });
            console.log(volume);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const volume = await client.beta.clusters.storage.update({
              volume_id: "12345-67890-12345-67890",
              size_tib: 3
            });
            console.log(volume);
        - lang: Shell
          label: cURL
          source: |
            curl -X PUT \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  --data '{ "volume_id": "12345-67890-12345-67890", "size_tib": 3}' \
                  https://api.together.ai/v1/compute/clusters/storage/volumes
components:
  schemas:
    GPUClustersSharedVolumeUpdateRequest:
      type: object
      properties:
        volume_id:
          description: ID of the volume to update.
          type: string
        size_tib:
          description: Size of the volume in whole tebibytes (TiB).
          type: integer
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