# Source: https://docs.runpod.io/api-reference/network-volumes/POST/networkvolumes.md

# Source: https://docs.runpod.io/api-reference/network-volumes/GET/networkvolumes.md

# Source: https://docs.runpod.io/api-reference/billing/GET/billing/networkvolumes.md

# Source: https://docs.runpod.io/api-reference/network-volumes/POST/networkvolumes.md

# Source: https://docs.runpod.io/api-reference/network-volumes/GET/networkvolumes.md

# Source: https://docs.runpod.io/api-reference/billing/GET/billing/networkvolumes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Volume billing history

> Retrieve billing information about your network volumes.



## OpenAPI

````yaml GET /billing/networkvolumes
openapi: 3.0.3
info:
  title: Runpod API
  description: Public Rest API for managing Runpod programmatically.
  version: 0.1.0
  contact:
    name: help
    url: https://contact.runpod.io/hc/requests/new
    email: help@runpod.io
servers:
  - url: https://rest.runpod.io/v1
security:
  - ApiKey: []
tags:
  - name: docs
    description: This documentation page.
  - name: pods
    description: Manage Pods.
  - name: endpoints
    description: Manage Serverless endpoints.
  - name: network volumes
    description: Manage Runpod network volumes.
  - name: templates
    description: Manage Pod and Serverless templates.
  - name: container registry auths
    description: >-
      Manage authentication for container registries such as dockerhub to use
      private images.
  - name: billing
    description: Retrieve billing history for your Runpod account.
externalDocs:
  description: Find out more about Runpod.
  url: https://runpod.io
paths:
  /billing/networkvolumes:
    get:
      tags:
        - billing
      summary: Network volume billing history
      description: Retrieve billing information about your network volumes.
      operationId: NetworkVolumeBilling
      parameters:
        - name: bucketSize
          in: query
          schema:
            type: string
            enum:
              - hour
              - day
              - week
              - month
              - year
            default: day
            description: >-
              The length of each billing time bucket. The billing time bucket is
              the time range over which each billing record is aggregated.
        - name: endTime
          in: query
          schema:
            type: string
            format: date-time
            example: '2023-01-31T23:59:59Z'
            description: The end date of the billing period to retrieve.
        - name: startTime
          in: query
          schema:
            type: string
            format: date-time
            example: '2023-01-01T00:00:00Z'
            description: The start date of the billing period to retrieve.
      responses:
        '200':
          description: Successful operation.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NetworkVolumeBillingRecords'
components:
  schemas:
    NetworkVolumeBillingRecords:
      type: array
      items:
        type: object
        properties:
          amount:
            type: number
            description: The amount charged for the group for the billing period, in USD.
            example: 100.5
          diskSpaceBilledGb:
            type: integer
            description: >-
              The amount of disk space billed for the billing period, in
              gigabytes (GB). Does not apply to all resource types.
            example: 50
          highPerformanceStorageAmount:
            type: number
            description: >-
              The amount charged for high performance storage for the billing
              period, in USD.
            example: 100.5
          highPerformanceStorageDiskSpaceBilledGb:
            type: integer
            description: >-
              The amount of high performance storage disk space billed for the
              billing period, in gigabytes (GB).
            example: 50
          time:
            type: string
            format: date-time
            description: The start of the period for which the billing record applies.
            example: '2023-01-01T00:00:00Z'
  securitySchemes:
    ApiKey:
      type: http
      scheme: bearer
      bearerFormat: Bearer

````