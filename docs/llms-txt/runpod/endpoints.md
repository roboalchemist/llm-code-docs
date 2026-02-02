# Source: https://docs.runpod.io/sdks/python/endpoints.md

# Source: https://docs.runpod.io/sdks/javascript/endpoints.md

# Source: https://docs.runpod.io/sdks/go/endpoints.md

# Source: https://docs.runpod.io/api-reference/endpoints/POST/endpoints.md

# Source: https://docs.runpod.io/api-reference/endpoints/GET/endpoints.md

# Source: https://docs.runpod.io/api-reference/billing/GET/billing/endpoints.md

<!-- Documentation Index: See llms.txt -->
<!-- See llms.txt for complete documentation index -->
<!-- Use this for finding documentation -->

# Serverless billing history

> Retrieve billing information about your Serverless endpoints.


## OpenAPI

````yaml GET /billing/endpoints
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
  /billing/endpoints:
    get:
      tags:
        - billing
      summary: Serverless billing history
      description: Retrieve billing information about your Serverless endpoints.
      operationId: EndpointBilling
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
        - name: dataCenterId
          in: query
          schema:
            type: array
            example:
              - EU-RO-1
              - CA-MTL-1
            default:
              - EU-RO-1
              - CA-MTL-1
              - EU-SE-1
              - US-IL-1
              - EUR-IS-1
              - EU-CZ-1
              - US-TX-3
              - EUR-IS-2
              - US-KS-2
              - US-GA-2
              - US-WA-1
              - US-TX-1
              - CA-MTL-3
              - EU-NL-1
              - US-TX-4
              - US-CA-2
              - US-NC-1
              - OC-AU-1
              - US-DE-1
              - EUR-IS-3
              - CA-MTL-2
              - AP-JP-1
              - EUR-NO-1
              - EU-FR-1
              - US-KS-3
              - US-GA-1
            items:
              type: string
              enum:
                - EU-RO-1
                - CA-MTL-1
                - EU-SE-1
                - US-IL-1
                - EUR-IS-1
                - EU-CZ-1
                - US-TX-3
                - EUR-IS-2
                - US-KS-2
                - US-GA-2
                - US-WA-1
                - US-TX-1
                - CA-MTL-3
                - EU-NL-1
                - US-TX-4
                - US-CA-2
                - US-NC-1
                - OC-AU-1
                - US-DE-1
                - EUR-IS-3
                - CA-MTL-2
                - AP-JP-1
                - EUR-NO-1
                - EU-FR-1
                - US-KS-3
                - US-GA-1
            description: >-
              Filter to endpoints located in any of the provided Runpod data
              centers. The data center IDs are listed in the response of the
              /pods endpoint.
        - name: endpointId
          in: query
          schema:
            type: string
            example: jpnw0v75y3qoql
            description: Filter to a specific endpoint.
        - name: endTime
          in: query
          schema:
            type: string
            format: date-time
            example: '2023-01-31T23:59:59Z'
            description: The end date of the billing period to retrieve.
        - name: gpuTypeId
          in: query
          schema:
            type: array
            items:
              type: string
              enum:
                - NVIDIA GeForce RTX 4090
                - NVIDIA A40
                - NVIDIA RTX A5000
                - NVIDIA GeForce RTX 5090
                - NVIDIA H100 80GB HBM3
                - NVIDIA GeForce RTX 3090
                - NVIDIA RTX A4500
                - NVIDIA L40S
                - NVIDIA H200
                - NVIDIA L4
                - NVIDIA RTX 6000 Ada Generation
                - NVIDIA A100-SXM4-80GB
                - NVIDIA RTX 4000 Ada Generation
                - NVIDIA RTX A6000
                - NVIDIA A100 80GB PCIe
                - NVIDIA RTX 2000 Ada Generation
                - NVIDIA RTX A4000
                - NVIDIA RTX PRO 6000 Blackwell Server Edition
                - NVIDIA H100 PCIe
                - NVIDIA H100 NVL
                - NVIDIA L40
                - NVIDIA B200
                - NVIDIA GeForce RTX 3080 Ti
                - NVIDIA RTX PRO 6000 Blackwell Workstation Edition
                - NVIDIA GeForce RTX 3080
                - NVIDIA GeForce RTX 3070
                - AMD Instinct MI300X OAM
                - NVIDIA GeForce RTX 4080 SUPER
                - Tesla V100-PCIE-16GB
                - Tesla V100-SXM2-32GB
                - NVIDIA RTX 5000 Ada Generation
                - NVIDIA GeForce RTX 4070 Ti
                - NVIDIA RTX 4000 SFF Ada Generation
                - NVIDIA GeForce RTX 3090 Ti
                - NVIDIA RTX A2000
                - NVIDIA GeForce RTX 4080
                - NVIDIA A30
                - NVIDIA GeForce RTX 5080
                - Tesla V100-FHHL-16GB
                - NVIDIA H200 NVL
                - Tesla V100-SXM2-16GB
                - NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition
                - NVIDIA A5000 Ada
                - Tesla V100-PCIE-32GB
                - NVIDIA  RTX A4500
                - NVIDIA  A30
                - NVIDIA GeForce RTX 3080TI
                - Tesla T4
                - NVIDIA RTX A30
            example: NVIDIA GeForce RTX 4090
            description: Filter to endpoints with the provided GPU type attached.
        - name: grouping
          in: query
          schema:
            type: string
            enum:
              - endpointId
              - podId
              - gpuTypeId
            default: endpointId
            description: Group the billing records by the provided field.
        - name: imageName
          in: query
          schema:
            type: string
            example: runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04
            description: Filter to endpoints created with the provided image.
        - name: startTime
          in: query
          schema:
            type: string
            format: date-time
            example: '2023-01-01T00:00:00Z'
            description: The start date of the billing period to retrieve.
        - name: templateId
          in: query
          schema:
            type: string
            example: 30zmvf89kd
            description: Filter to endpoints created from the provided template.
      responses:
        '200':
          description: Successful operation.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BillingRecords'
components:
  schemas:
    BillingRecords:
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
          endpointId:
            type: string
            description: If grouping by endpoint ID, the endpoint ID of the group.
          gpuTypeId:
            type: string
            description: If grouping by GPU type ID, the GPU type ID of the group.
          podId:
            type: string
            description: If grouping by Pod ID, the Pod ID of the group.
          time:
            type: string
            format: date-time
            description: The start of the period for which the billing record applies.
            example: '2023-01-01T00:00:00Z'
          timeBilledMs:
            type: integer
            description: >-
              The total time billed for the billing period, in milliseconds.
              Does not apply to all resource types.
            example: 3600000
  securitySchemes:
    ApiKey:
      type: http
      scheme: bearer
      bearerFormat: Bearer

````