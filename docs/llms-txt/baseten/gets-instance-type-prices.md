# Source: https://docs.baseten.co/reference/management-api/instance-types/gets-instance-type-prices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Instance type prices



## OpenAPI

````yaml get /v1/instance_type_prices
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/instance_type_prices:
    get:
      summary: Gets prices for available instance types.
      responses:
        '200':
          description: A list of instance types.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InstanceTypePricesV1'
components:
  schemas:
    InstanceTypePricesV1:
      description: A list of instance types.
      properties:
        instance_types:
          items:
            $ref: '#/components/schemas/InstanceTypeWithPriceV1'
          title: Instance Types
          type: array
      required:
        - instance_types
      title: InstanceTypePricesV1
      type: object
    InstanceTypeWithPriceV1:
      properties:
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type properties.
        price:
          description: Usage price in USD / minute.
          title: Price
          type: number
      required:
        - instance_type
        - price
      title: InstanceTypeWithPriceV1
      type: object
    InstanceTypeV1:
      description: An instance type.
      properties:
        id:
          description: Identifier string for the instance type
          title: Id
          type: string
        name:
          description: Display name of the instance type
          title: Name
          type: string
        memory_limit_mib:
          description: Memory limit of the instance type in Mebibytes
          title: Memory Limit Mib
          type: integer
        millicpu_limit:
          description: CPU limit of the instance type in millicpu
          title: Millicpu Limit
          type: integer
        gpu_count:
          description: Number of GPUs on the instance type
          title: Gpu Count
          type: integer
        gpu_type:
          anyOf:
            - type: string
            - type: 'null'
          description: Type of GPU on the instance type
          title: Gpu Type
        gpu_memory_limit_mib:
          anyOf:
            - type: integer
            - type: 'null'
          description: Memory limit of the GPU on the instance type in Mebibytes
          title: Gpu Memory Limit Mib
      required:
        - id
        - name
        - memory_limit_mib
        - millicpu_limit
        - gpu_count
        - gpu_type
        - gpu_memory_limit_mib
      title: InstanceTypeV1
      type: object
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````