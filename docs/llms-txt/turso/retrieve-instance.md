# Source: https://docs.turso.tech/api-reference/databases/retrieve-instance.md

# Retrieve Database Instance

> Return the individual database instance by name.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName}
paths:
  path: >-
    /v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName}
  method: get
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
        databaseName:
          schema:
            - type: string
              required: true
              description: The name of the database.
        instanceName:
          schema:
            - type: string
              required: true
              description: The name of the instance (location code).
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              instance:
                allOf:
                  - $ref: '#/components/schemas/Instance'
        examples:
          example:
            value:
              instance:
                uuid: 0be90471-6906-11ee-8553-eaa7715aeaf2
                name: lhr
                type: primary
                region: lhr
                hostname: '[databaseName]-[organizationSlug].turso.io'
        description: Successful response
  deprecated: false
  type: path
components:
  schemas:
    Instance:
      type: object
      properties:
        uuid:
          type: string
          description: The instance universal unique identifier (UUID).
          example: 0be90471-6906-11ee-8553-eaa7715aeaf2
        name:
          type: string
          description: The name of the instance (location code).
          example: lhr
        type:
          type: string
          description: The type of database instance this, will be `primary` or `replica`.
          enum:
            - primary
            - replica
          example: primary
        region:
          type: string
          description: The location code for the region this instance is located.
          example: lhr
        hostname:
          type: string
          description: >-
            The DNS hostname used for client libSQL and HTTP connections
            (specific to this instance only).
          example: '[databaseName]-[organizationSlug].turso.io'

````