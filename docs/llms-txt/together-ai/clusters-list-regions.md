# Source: https://docs.together.ai/reference/clusters-list-regions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List compute region capabilities



## OpenAPI

````yaml GET /compute/regions
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
  /compute/regions:
    get:
      tags:
        - RegionService
      summary: List regions and corresponding supported driver versions
      operationId: RegionService_List
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RegionListResponse'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together
            client = Together()

            regions = client.beta.clusters.list_regions()
            print(regions)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const regions = await client.beta.clusters.list_regions();
            console.log(regions);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const regions = await client.beta.clusters.list_regions();
            console.log(regions);
        - lang: Shell
          label: cURL
          source: |
            curl -X GET \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/compute/regions
components:
  schemas:
    RegionListResponse:
      type: object
      required:
        - regions
      properties:
        regions:
          type: array
          items:
            type: object
            required:
              - name
              - availability_zones
              - driver_versions
            properties:
              name:
                description: Identifiable name of the region.
                type: string
              driver_versions:
                description: >-
                  List of supported identifiable driver versions available in
                  the region.
                type: array
                items:
                  type: string
              supported_instance_types:
                description: List of supported identifiable gpus available in the region.
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