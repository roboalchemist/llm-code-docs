# Source: https://upstash.com/docs/devops/developer-api/redis/update_regions.md

# Update Regions

> Update the regions of a database

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/update-regions/{id}
paths:
  path: /redis/update-regions/{id}
  method: post
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of your database
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              read_regions:
                allOf:
                  - type: array
                    items:
                      type: string
                      enum:
                        - us-east-1
                        - us-east-2
                        - us-west-1
                        - us-west-2
                        - ca-central-1
                        - eu-central-1
                        - eu-west-1
                        - eu-west-2
                        - sa-east-1
                        - ap-south-1
                        - ap-northeast-1
                        - ap-southeast-1
                        - ap-southeast-2
                    description: Array of Read Regions of the Database
                    example:
                      - us-west-1
                      - us-west-2
            required: true
            requiredProperties:
              - read_regions
        examples:
          example:
            value:
              read_regions:
                - us-west-1
                - us-west-2
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Regions updated successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/update_regions
components:
  schemas: {}

````