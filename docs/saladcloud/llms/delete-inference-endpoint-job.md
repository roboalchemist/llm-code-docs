# Source: https://docs.salad.com/reference/saladcloud-api/inference-endpoints/delete-inference-endpoint-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel an Inference Endpoint Job

> Cancels an inference endpoint job.

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml delete /organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs/{inference_endpoint_job_id}
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
  /organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs/{inference_endpoint_job_id}:
    summary: Jobs in an inference endpoint
    description: Operations for jobs in an inference endpoint
    parameters:
      - $ref: '#/components/parameters/organization_name'
      - $ref: '#/components/parameters/inference_endpoint_name'
      - $ref: '#/components/parameters/inference_endpoint_job_id'
    delete:
      tags:
        - inference_endpoints
      summary: Cancel an Inference Endpoint Job
      description: Cancels an inference endpoint job.
      operationId: delete_inference_endpoint_job
      responses:
        '202':
          $ref: '#/components/responses/202'
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
    inference_endpoint_name:
      name: inference_endpoint_name
      in: path
      description: The inference endpoint name.
      required: true
      schema:
        $ref: '#/components/schemas/InferenceEndpointName'
    inference_endpoint_job_id:
      name: inference_endpoint_job_id
      description: The inference endpoint job identifier.
      in: path
      required: true
      schema:
        $ref: '#/components/schemas/InferenceEndpointJobId'
  responses:
    '202':
      description: Accepted
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
    InferenceEndpointName:
      description: The inference endpoint name.
      type: string
      examples:
        - transcribe
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Inference Endpoint Name
    InferenceEndpointJobId:
      description: The inference endpoint job identifier.
      type: string
      format: uuid
      examples:
        - 2fc459a1-1c09-4a34-ade7-54d03fc51d6a
      title: Inference Endpoint Job ID
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````