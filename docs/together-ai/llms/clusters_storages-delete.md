# Source: https://docs.together.ai/reference/clusters_storages-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a shared volume

> Delete a shared volume. Note that if this volume is attached to a cluster, deleting will fail.




## OpenAPI

````yaml DELETE /compute/clusters/storage/volumes/{volume_id}
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
    delete:
      tags:
        - SharedVolumeService
      summary: Delete shared volume by volume id.
      description: >
        Delete a shared volume. Note that if this volume is attached to a
        cluster, deleting will fail.
      operationId: SharedVolumeService_Delete
      parameters:
        - name: volume_id
          in: path
          required: true
          schema:
            description: The ID of the volume to delete
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GPUClustersSharedVolumeDeleteResponse'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together
            client = Together()

            volume = client.beta.clusters.storage.delete("volume_id")
            print(volume)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: >
            import Together from "together-ai";

            const client = new Together();


            const volume = await
            client.beta.clusters.storage.delete("volume_id");

            console.log(volume);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: >
            import Together from "together-ai";

            const client = new Together();


            const volume = await
            client.beta.clusters.storage.delete("volume_id");

            console.log(volume);
        - lang: Shell
          label: cURL
          source: |
            curl -X DELETE \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/compute/clusters/storage/volumes/${VOLUME_ID}
components:
  schemas:
    GPUClustersSharedVolumeDeleteResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).