# Source: https://docs.together.ai/reference/clusters-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Cluster

> Delete a GPU cluster by cluster ID.



## OpenAPI

````yaml DELETE /compute/clusters/{cluster_id}
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
    delete:
      tags:
        - GPUClusterService
      summary: Delete GPU cluster by cluster ID
      description: Delete a GPU cluster by cluster ID.
      operationId: GPUClusterService_Delete
      parameters:
        - name: cluster_id
          in: path
          required: true
          schema:
            description: The ID of the cluster to delete
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                  - cluster_id
                properties:
                  cluster_id:
                    type: string
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together
            client = Together()

            cluster = client.beta.clusters.delete("cluster_id")
            print(cluster)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const cluster = await client.beta.clusters.delete("cluster_id");
            console.log(cluster);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const cluster = await client.beta.clusters.delete("cluster_id");
            console.log(cluster);
        - lang: Shell
          label: cURL
          source: |
            curl -X DELETE \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/compute/clusters/${CLUSTER_ID}
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).