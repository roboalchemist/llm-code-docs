# Source: https://docs.baseten.co/reference/training-api/search-training-jobs.md

# Search training jobs

> Search training jobs for the organization.

## OpenAPI

````yaml post /v1/training_jobs/search
paths:
  path: /v1/training_jobs/search
  method: post
  servers:
    - url: https://api.baseten.co
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: >-
                You must specify the scheme 'Api-Key' in the Authorization
                header. For example, `Authorization: Api-Key <Your_Api_Key>`
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              project_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    default: null
                    description: Filter the training jobs by project ID.
                    examples:
                      - n4q95w5
                    title: Project Id
              job_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    default: null
                    description: Filter the training jobs by job ID.
                    examples:
                      - p7qr9qv
                    title: Job Id
              statuses:
                allOf:
                  - anyOf:
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
                allOf:
                  - default:
                      - field: created_at
                        order: desc
                    description: >-
                      Order the training jobs by a field. Currently supports
                      created_at
                    items:
                      $ref: '#/components/schemas/OrderByV1'
                    title: Order By
                    type: array
            required: true
            title: SearchTrainingJobsRequestV1
            description: A request to search training jobs.
            refIdentifier: '#/components/schemas/SearchTrainingJobsRequestV1'
        examples:
          example:
            value:
              project_id: n4q95w5
              job_id: p7qr9qv
              statuses:
                - TRAINING_JOB_RUNNING
                - TRAINING_JOB_COMPLETED
              order_by:
                - field: created_at
                  order: desc
    codeSamples:
      - lang: bash
        source: |-
          curl --request POST \
          --url https://api.baseten.co/v1/training_jobs/search \
          --header "Authorization: Api-Key $BASETEN_API_KEY" \
          --data '{
            "project_id": "n4q95w5",
            "job_id": "p7qr9qv",
            "statuses": [
              "TRAINING_JOB_RUNNING",
              "TRAINING_JOB_COMPLETED"
            ],
            "order_by": null
          }'
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/training_jobs/search"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'project_id': 'n4q95w5', 'job_id': 'p7qr9qv', 'statuses': ['TRAINING_JOB_RUNNING', 'TRAINING_JOB_COMPLETED'], 'order_by': None}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              training_jobs:
                allOf:
                  - description: List of training jobs.
                    items:
                      $ref: '#/components/schemas/TrainingJobV1'
                    title: Training Jobs
                    type: array
            title: SearchTrainingJobsResponseV1
            description: A response to search training jobs.
            refIdentifier: '#/components/schemas/SearchTrainingJobsResponseV1'
            requiredProperties:
              - training_jobs
        examples:
          example:
            value:
              training_jobs:
                - id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  current_status: <string>
                  error_message: <string>
                  instance_type:
                    id: <string>
                    name: <string>
                    memory_limit_mib: 123
                    millicpu_limit: 123
                    gpu_count: 123
                    gpu_type: <string>
                    gpu_memory_limit_mib: 123
                  updated_at: '2023-11-07T05:31:56Z'
                  training_project_id: <string>
                  training_project:
                    id: <string>
                    name: <string>
                  name: gpt-oss-job
        description: A response to search training jobs.
  deprecated: false
  type: path
components:
  schemas:
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

````