# Source: https://docs.salad.com/reference/saladcloud-api/container-groups/get-container-group-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get System Logs

> Gets the System Logs

*Last Updated: July 1, 2025*

<Warning>
  This API endpoint is deprecated and will be removed in a future version of the SaladCloud API. The new [Query Log
  Entries](/reference/saladcloud-api/logs/query-log-entries) API endpoint replaces this endpoint, providing a powerful
  query interface for troubleshooting deployments and jobs.
</Warning>


## OpenAPI

````yaml api-specs/salad-cloud.yaml get /organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/system-logs
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
  /organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/system-logs:
    summary: System Logs
    description: Operations for System Logs
    parameters:
      - $ref: '#/components/parameters/organization_name'
      - $ref: '#/components/parameters/project_name'
      - $ref: '#/components/parameters/container_group_name'
    get:
      tags:
        - system_logs
      summary: Get System Logs
      description: Gets the System Logs
      operationId: get_system_logs
      responses:
        '200':
          $ref: '#/components/responses/ListSystemLogs'
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
    project_name:
      name: project_name
      in: path
      description: >-
        Your project name. This represents a collection of related SaladCloud
        resources. The project must be created before using the API.
      required: true
      schema:
        $ref: '#/components/schemas/ProjectName'
    container_group_name:
      in: path
      name: container_group_name
      description: The unique container group name
      required: true
      schema:
        $ref: '#/components/schemas/ContainerGroupName'
  responses:
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
    ListSystemLogs:
      description: OK
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/SystemLogList'
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
    ProjectName:
      description: The project name.
      type: string
      examples:
        - dev-env
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
    ContainerGroupName:
      description: The container group name.
      type: string
      examples:
        - mandlebrot
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Container Group Name
    SystemLogList:
      description: Represents a list of system logs
      type: object
      properties:
        items:
          description: A list of system logs
          type: array
          items:
            $ref: '#/components/schemas/SystemLog'
          maxItems: 50
          minItems: 0
      required:
        - items
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
    SystemLog:
      description: Represents a system log
      type: object
      properties:
        event_name:
          description: The name of the event
          type: string
          maxLength: 255
          minLength: 1
          pattern: ^.*$
        event_time:
          description: The UTC date & time when the log item was created
          type: string
          format: date-time
        instance_id:
          $ref: '#/components/schemas/ContainerGroupInstanceId'
        machine_id:
          $ref: '#/components/schemas/ContainerGroupMachineId'
        resource_cpu:
          description: The number of CPUs
          type:
            - integer
            - 'null'
          maximum: 16
          minimum: 1
        resource_gpu_class:
          description: The GPU class name
          type: string
        resource_memory:
          description: The memory amount in MB
          type:
            - integer
            - 'null'
          maximum: 61440
          minimum: 1024
        resource_storage_amount:
          description: The storage amount in bytes
          type:
            - integer
            - 'null'
          format: int64
          maximum: 268435456000
          minimum: 1073741824
        version:
          description: The version instance ID
          type: string
      required:
        - event_name
        - event_time
        - resource_cpu
        - resource_gpu_class
        - resource_memory
        - resource_storage_amount
        - version
    ContainerGroupInstanceId:
      description: The container group instance identifier.
      type: string
      format: uuid
      examples:
        - db3a4591-efc3-46c0-b06a-3d820c0ec100
      title: Container Group Instance ID
    ContainerGroupMachineId:
      description: The container group machine identifier.
      type: string
      format: uuid
      examples:
        - eb3a4591-efc3-46c0-b06a-3d820c0ec100
      title: Container Group Machine ID
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````