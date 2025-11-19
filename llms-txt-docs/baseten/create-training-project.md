# Source: https://docs.baseten.co/reference/training-api/create-training-project.md

# Create training project

> Upserts a training project with the specified metadata.

## OpenAPI

````yaml post /v1/training_projects
paths:
  path: /v1/training_projects
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
              training_project:
                allOf:
                  - $ref: '#/components/schemas/UpsertTrainingProjectV1'
                    description: The training project to upsert.
            required: true
            title: UpsertTrainingProjectRequestV1
            description: A request to upsert a training project.
            refIdentifier: '#/components/schemas/UpsertTrainingProjectRequestV1'
            requiredProperties:
              - training_project
        examples:
          example:
            value:
              training_project:
                name: My Training Project
    codeSamples:
      - lang: bash
        source: |-
          curl --request POST \
          --url https://api.baseten.co/v1/training_projects \
          --header "Authorization: Api-Key $BASETEN_API_KEY" \
          --data '{
            "training_project": {
              "name": "My Training Project"
            }
          }'
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/training_projects"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'training_project': {'name': 'My Training Project'}}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              training_project:
                allOf:
                  - $ref: '#/components/schemas/TrainingProjectV1'
                    description: The upserted training project.
            title: UpsertTrainingProjectResponseV1
            description: A response to upserting a training project.
            refIdentifier: '#/components/schemas/UpsertTrainingProjectResponseV1'
            requiredProperties:
              - training_project
        examples:
          example:
            value:
              training_project:
                id: <string>
                name: <string>
                created_at: '2023-11-07T05:31:56Z'
                updated_at: '2023-11-07T05:31:56Z'
                latest_job:
                  id: <string>
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
        description: A response to upserting a training project.
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
    UpsertTrainingProjectV1:
      description: Fields that can be upserted on a training project.
      properties:
        name:
          description: Name of the training project.
          examples:
            - My Training Project
          title: Name
          type: string
      required:
        - name
      title: UpsertTrainingProjectV1
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
    TrainingProjectV1:
      properties:
        id:
          description: Unique identifier of the training project
          title: Id
          type: string
        name:
          description: Name of the training project.
          title: Name
          type: string
        created_at:
          description: Time the training project was created in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        updated_at:
          description: Time the training project was updated in ISO 8601 format.
          format: date-time
          title: Updated At
          type: string
        latest_job:
          anyOf:
            - $ref: '#/components/schemas/TrainingJobV1'
            - type: 'null'
          description: Most recently created training job for the training project.
      required:
        - id
        - name
        - created_at
        - updated_at
        - latest_job
      title: TrainingProjectV1
      type: object

````