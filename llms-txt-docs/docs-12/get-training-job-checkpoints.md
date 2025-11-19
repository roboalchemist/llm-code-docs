# Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoints.md

# List training job checkpoints

> Get the checkpoints for a training job.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints
paths:
  path: >-
    /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints
  method: get
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
      path:
        training_project_id:
          schema:
            - type: string
              required: true
        training_job_id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: bash
        source: >
          curl --request GET \

          --url
          https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "GET",
              url,
              headers=headers,
              json={}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              training_job:
                allOf:
                  - $ref: '#/components/schemas/TrainingJobV1'
                    description: The training job.
              checkpoints:
                allOf:
                  - description: The checkpoints for the training job.
                    items:
                      $ref: '#/components/schemas/TrainingJobCheckpointV1'
                    title: Checkpoints
                    type: array
            title: GetTrainingJobCheckpointsResponseV1
            description: A response to fetch checkpoints for a training job.
            refIdentifier: '#/components/schemas/GetTrainingJobCheckpointsResponseV1'
            requiredProperties:
              - training_job
              - checkpoints
        examples:
          example:
            value:
              training_job:
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
              checkpoints:
                - training_job_id: <string>
                  checkpoint_id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  checkpoint_type: <string>
                  base_model: <string>
                  lora_adapter_config: {}
                  size_bytes: 123
        description: A response to fetch checkpoints for a training job.
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
    TrainingJobCheckpointV1:
      description: A checkpoint for a training job.
      properties:
        training_job_id:
          description: The ID of the training job.
          title: Training Job Id
          type: string
        checkpoint_id:
          description: The ID of the checkpoint.
          title: Checkpoint Id
          type: string
        created_at:
          description: The timestamp of the checkpoint in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        checkpoint_type:
          description: The type of checkpoint.
          title: Checkpoint Type
          type: string
        base_model:
          anyOf:
            - type: string
            - type: 'null'
          description: The base model of the checkpoint.
          title: Base Model
        lora_adapter_config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          description: The adapter config of the checkpoint.
          title: Lora Adapter Config
        size_bytes:
          description: The size of the checkpoint in bytes.
          title: Size Bytes
          type: integer
      required:
        - training_job_id
        - checkpoint_id
        - created_at
        - checkpoint_type
        - base_model
        - lora_adapter_config
        - size_bytes
      title: TrainingJobCheckpointV1
      type: object

````