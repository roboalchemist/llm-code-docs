# Source: https://docs.together.ai/api-reference/regionservice/list-regions-and-corresponding-supported-driver-versions.md

# List regions and corresponding supported driver versions



## OpenAPI

````yaml tcloud.yaml get /api/v1/regions
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
  /api/v1/regions:
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
components:
  schemas:
    RegionListResponse:
      type: object
      properties:
        regions:
          type: array
          items:
            $ref: '#/components/schemas/Region'
    Region:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        availability_zones:
          type: array
          items:
            type: string
        driver_versions:
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