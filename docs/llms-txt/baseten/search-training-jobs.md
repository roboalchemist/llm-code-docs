# Source: https://docs.baseten.co/reference/training-api/search-training-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Search training jobs

> Search training jobs for the organization.



## OpenAPI

````yaml post /v1/training_jobs/search
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
  /v1/training_jobs/search:
    post:
      summary: Search training jobs.
      description: Search training jobs for the organization.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SearchTrainingJobsRequestV1'
        required: true
      responses:
        '200':
          description: A response to search training jobs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SearchTrainingJobsResponseV1'
components:
  schemas:
    SearchTrainingJobsRequestV1:
      description: A request to search training jobs.
      properties:
        project_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Filter the training jobs by project ID.
          examples:
            - n4q95w5
          title: Project Id
        job_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Filter the training jobs by job ID.
          examples:
            - p7qr9qv
          title: Job Id
        statuses:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          default: null
          description: Filter the training jobs by status.
          examples:
            - - TRAINING_JOB_RUNNING
              - TRAINING_JOB_COMPLETED
          title: Statuses
        order_by:
          default:
            - field: created_at
              order: desc
          description: Order the training jobs by a field. Currently supports created_at
          items:
            $ref: '#/components/schemas/OrderByV1'
          title: Order By
          type: array
      title: SearchTrainingJobsRequestV1
      type: object
    SearchTrainingJobsResponseV1:
      description: A response to search training jobs.
      properties:
        training_jobs:
          description: List of training jobs.
          items:
            $ref: '#/components/schemas/TrainingJobV1'
          title: Training Jobs
          type: array
      required:
        - training_jobs
      title: SearchTrainingJobsResponseV1
      type: object
    OrderByV1:
      description: A request to order training jobs.
      properties:
        field:
          description: The field to order by.
          examples:
            - created_at
          title: Field
          type: string
        order:
          description: The direction to order by.
          examples:
            - asc
            - desc
          title: Order
          type: string
      required:
        - field
        - order
      title: OrderByV1
      type: object
    TrainingJobV1:
      properties:
        id:
          description: Unique identifier of the training job.
          title: Id
          type: string
        created_at:
          description: Time the job was created in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        current_status:
          description: Current status of the training job.
          title: Current Status
          type: string
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Error message if the training job failed.
          title: Error Message
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type of the training job.
        updated_at:
          description: Time the job was updated in ISO 8601 format.
          format: date-time
          title: Updated At
          type: string
        training_project_id:
          description: ID of the training project.
          title: Training Project Id
          type: string
        training_project:
          $ref: '#/components/schemas/TrainingProjectSummaryV1'
          description: Summary of the training project.
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the training job.
          examples:
            - gpt-oss-job
          title: Name
      required:
        - id
        - created_at
        - current_status
        - instance_type
        - updated_at
        - training_project_id
        - training_project
      title: TrainingJobV1
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
    TrainingProjectSummaryV1:
      description: A summary of a training project.
      properties:
        id:
          description: Unique identifier of the training project.
          title: Id
          type: string
        name:
          description: Name of the training project.
          title: Name
          type: string
      required:
        - id
        - name
      title: TrainingProjectSummaryV1
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