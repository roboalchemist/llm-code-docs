# Source: https://docs.runpod.io/api-reference/pods/POST/pods.md

# Source: https://docs.runpod.io/api-reference/pods/GET/pods.md

# Source: https://docs.runpod.io/api-reference/billing/GET/billing/pods.md

# Source: https://docs.runpod.io/api-reference/pods/POST/pods.md

# Source: https://docs.runpod.io/api-reference/pods/GET/pods.md

# Source: https://docs.runpod.io/api-reference/billing/GET/billing/pods.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Pod billing history

> Retrieve billing information about your Pods.



## OpenAPI

````yaml GET /billing/pods
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
  /billing/pods:
    get:
      tags:
        - billing
      summary: Pod billing history
      description: Retrieve billing information about your Pods.
      operationId: PodBilling
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
        - name: gpuTypeId
          in: query
          schema:
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
            description: Filter to Pods with the provided GPU type attached.
        - name: grouping
          in: query
          schema:
            type: string
            enum:
              - podId
              - gpuTypeId
            default: gpuTypeId
            description: Group the billing records by the provided field.
        - name: podId
          in: query
          schema:
            type: string
            example: xedezhzb9la3ye
            description: Filter to a specific Pod.
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