# Source: https://docs.salad.com/reference/saladcloud-api/inference-endpoints/list-inference-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Inference Endpoints

> Lists inference endpoints.

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml get /organizations/{organization_name}/inference-endpoints
openapi: 3.1.0
info:
  title: SaladCloud API
  description: >-
    The SaladCloud REST API. Please refer to the [SaladCloud API
    Documentation](https://docs.salad.com/api-reference) for more details.
  termsOfService: https://salad.com/terms
  contact:
    name: SaladCloud Support
    url: https://salad.com
    email: cloud@salad.com
  license:
    name: MIT License
    identifier: MIT
  version: 0.9.0-alpha.16
servers:
  - url: https://api.salad.com/api/public
security:
  - ApiKeyAuth: []
tags:
  - name: container_groups
    description: Container Groups
  - name: inference_endpoints
    description: Inference Endpoints
  - name: organization_data
    description: Auxiliary organization data and info
  - name: queues
    description: Job Queues
  - name: quotas
    description: quotas
  - name: system_logs
    description: System Logs
  - name: webhook_secret_key
    description: Webhook Secret Key
  - name: logs
    description: Platform and Application Log Entries
paths:
  /organizations/{organization_name}/inference-endpoints:
    summary: Inference Endpoints
    description: Operations for inference endpoints
    parameters:
      - $ref: '#/components/parameters/organization_name'
    get:
      tags:
        - inference_endpoints
      summary: List Inference Endpoints
      description: Lists inference endpoints.
      operationId: list_inference_endpoints
      parameters:
        - $ref: '#/components/parameters/Page'
        - $ref: '#/components/parameters/PageSize'
      responses:
        '200':
          $ref: '#/components/responses/ListInferenceEndpoints'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '403':
          $ref: '#/components/responses/403'
        '404':
          $ref: '#/components/responses/404'
        '429':
          $ref: '#/components/responses/429'
        default:
          $ref: '#/components/responses/UnknownError'
components:
  parameters:
    organization_name:
      name: organization_name
      in: path
      description: >-
        Your organization name. This identifies the billing context for the API
        operation and represents a security boundary for SaladCloud resources.
        The organization must be created before using the API, and you must be a
        member of the organization.
      required: true
      schema:
        $ref: '#/components/schemas/OrganizationName'
    Page:
      in: query
      name: page
      description: The page number.
      schema:
        $ref: '#/components/schemas/Page'
    PageSize:
      in: query
      name: page_size
      description: The maximum number of items per page.
      schema:
        $ref: '#/components/schemas/PageSize'
  responses:
    '400':
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '401':
      description: Unauthorized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '403':
      description: Forbidden
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '404':
      description: Not Found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '429':
      description: Too Many Requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    ListInferenceEndpoints:
      description: OK
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/InferenceEndpointCollection'
    UnknownError:
      description: Unknown Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
  schemas:
    OrganizationName:
      description: The organization name.
      type: string
      examples:
        - acme-corp
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Organization Name
    Page:
      description: The page number.
      type: integer
      format: int32
      examples:
        - 1
      maximum: 2147483647
      minimum: 1
    PageSize:
      description: The maximum number of items per page.
      type: integer
      format: int32
      examples:
        - 1
      maximum: 100
      minimum: 1
    InferenceEndpointCollection:
      description: Represents a page from the collection of inference endpoints.
      type: object
      properties:
        items:
          description: The list of inference endpoints.
          type: array
          items:
            $ref: '#/components/schemas/InferenceEndpoint'
          maxItems: 100
          minItems: 0
        page:
          $ref: '#/components/schemas/Page'
        page_size:
          $ref: '#/components/schemas/PageSize'
        total_size:
          $ref: '#/components/schemas/TotalSize'
      required:
        - items
        - page
        - page_size
        - total_size
    ProblemDetails:
      description: Represents an API error
      type: object
      properties:
        type:
          description: The URI reference that identifies the error type.
          type: string
          format: url
          default: about:blank
          examples:
            - https://example.com/errors/invalid-request
          maxLength: 2048
          minLength: 1
        title:
          description: The short, human-readable summary of the error type.
          type: string
          examples:
            - Not Found
          maxLength: 2000
          minLength: 1
        status:
          description: >-
            The HTTP status code generated by the origin server for this
            occurrence of the error.
          type: integer
          format: int32
          examples:
            - 404
          maximum: 599
          minimum: 100
        detail:
          description: >-
            The human-readable explanation specific to this occurrence of the
            error.
          type: string
          examples:
            - The container group could not be found.
          maxLength: 2000
          minLength: 1
        instance:
          description: >-
            The URI reference that identifies the specific occurrence of the
            error.
          type: string
          format: url
          examples:
            - https://example.com/error-instances/12345
          maxLength: 2048
          minLength: 1
    InferenceEndpoint:
      description: Represents an inference endpoint
      type: object
      properties:
        id:
          $ref: '#/components/schemas/InferenceEndpointId'
        name:
          $ref: '#/components/schemas/InferenceEndpointName'
        organization_name:
          $ref: '#/components/schemas/OrganizationName'
        display_name:
          $ref: '#/components/schemas/DisplayName'
        description:
          $ref: '#/components/schemas/Description'
        readme:
          description: >-
            A markdown file containing a detailed description of the inference
            endpoint
          type: string
          maxLength: 100000
          minLength: 1
          pattern: ^.*$
        price_description:
          description: A description of the price
          type: string
          maxLength: 100
          minLength: 1
          pattern: ^.*$
        icon_url:
          description: The URL of the icon image
          type: string
          format: url
          maxLength: 2048
          minLength: 1
          pattern: ^.*$
        input_schema:
          description: The input schema
          type: string
          maxLength: 100000
          minLength: 1
          pattern: ^.*$
        output_schema:
          description: The output schema
          type: string
          maxLength: 100000
          minLength: 1
          pattern: ^.*$
      required:
        - description
        - display_name
        - icon_url
        - id
        - input_schema
        - name
        - organization_name
        - output_schema
        - price_description
        - readme
    TotalSize:
      description: The total number of items in the collection.
      type: integer
      format: int32
      examples:
        - 100
      maximum: 2147483647
      minimum: 0
    InferenceEndpointId:
      description: The inference endpoint identifier.
      type: string
      format: uuid
      examples:
        - cb3a4591-efc3-46c0-b06a-3d820c0ec100
      title: Inference Endpoint ID
    InferenceEndpointName:
      description: The inference endpoint name.
      type: string
      examples:
        - transcribe
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Inference Endpoint Name
    DisplayName:
      description: The display-friendly name of the resource.
      type: string
      examples:
        - Name
      maxLength: 63
      minLength: 2
      pattern: ^[ ,-.0-9A-Za-z]+$
    Description:
      description: The detailed description of the resource.
      type: string
      examples:
        - ''
      maxLength: 1000
      minLength: 0
      pattern: ^.*$
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````