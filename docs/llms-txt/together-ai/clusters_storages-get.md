# Source: https://docs.together.ai/reference/clusters_storages-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a shared volumes

> Retrieve information about a specific shared volume.



## OpenAPI

````yaml GET /compute/clusters/storage/volumes/{volume_id}
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
  /compute/clusters/storage/volumes/{volume_id}:
    get:
      tags:
        - SharedVolumeService
      summary: Get shared volume by volume Id.
      description: Retrieve information about a specific shared volume.
      operationId: SharedVolumeService_Get
      parameters:
        - name: volume_id
          in: path
          required: true
          schema:
            description: The ID of the volume to retrieve
            type: string
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

            volume = client.beta.clusters.storage.retrieve("volume_id")
            print(volume)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: >
            import Together from "together-ai";

            const client = new Together();


            const volume = await
            client.beta.clusters.storage.retrieve("volume_id");

            console.log(volume);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: >
            import Together from "together-ai";

            const client = new Together();


            const volume = await
            client.beta.clusters.storage.retrieve("volume_id");

            console.log(volume);
        - lang: Shell
          label: cURL
          source: |
            curl -X GET \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/compute/clusters/storage/volumes/${VOLUME_ID}
components:
  schemas:
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