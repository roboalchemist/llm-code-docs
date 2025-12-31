# Source: https://docs.baseten.co/reference/training-api/get-training-job-metrics.md

# Get training job metrics

> Get the metrics for a training job.

## OpenAPI

````yaml post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
paths:
  path: /v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              end_epoch_millis:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Epoch millis timestamp to end fetching metrics
                    title: End Epoch Millis
              start_epoch_millis:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Epoch millis timestamp to start fetching metrics.
                    title: Start Epoch Millis
            required: true
            title: GetTrainingJobMetricsRequestV1
            description: >-
              A request to fetch metrics. Allows the user to request metrics
              over a period of time.
            refIdentifier: '#/components/schemas/GetTrainingJobMetricsRequestV1'
        examples:
          example:
            value:
              end_epoch_millis: 123
              start_epoch_millis: 123
    codeSamples:
      - lang: bash
        source: >-
          curl --request POST \

          --url
          https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY" \

          --data '{
            "end_epoch_millis": null,
            "start_epoch_millis": null
          }'
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'end_epoch_millis': None, 'start_epoch_millis': None}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              gpu_memory_usage_bytes:
                allOf:
                  - additionalProperties:
                      items:
                        $ref: '#/components/schemas/TrainingJobMetricV1'
                      type: array
                    description: >-
                      A map of GPU rank to memory usage for the training job.
                      For multinode jobs, this is the memory usage of the leader
                      unless specified otherwise.
                    title: Gpu Memory Usage Bytes
                    type: object
              gpu_utilization:
                allOf:
                  - additionalProperties:
                      items:
                        $ref: '#/components/schemas/TrainingJobMetricV1'
                      type: array
                    description: >-
                      A map of GPU rank to fractional GPU utilization. For
                      multinode jobs, this is the GPU utilization of the leader
                      unless specified otherwise.
                    title: Gpu Utilization
                    type: object
              cpu_usage:
                allOf:
                  - description: >-
                      The CPU usage measured in cores. For multinode jobs, this
                      is the CPU usage of the leader unless specified otherwise.
                    items:
                      $ref: '#/components/schemas/TrainingJobMetricV1'
                    title: Cpu Usage
                    type: array
              cpu_memory_usage_bytes:
                allOf:
                  - description: >-
                      The CPU memory usage for the training job. For multinode
                      jobs, this is the CPU memory usage of the leader unless
                      specified otherwise.
                    items:
                      $ref: '#/components/schemas/TrainingJobMetricV1'
                    title: Cpu Memory Usage Bytes
                    type: array
              ephemeral_storage:
                allOf:
                  - $ref: '#/components/schemas/StorageMetricsV1'
                    description: >-
                      The storage usage for the ephemeral storage. For multinode
                      jobs, this is the ephemeral storage usage of the leader
                      unless specified otherwise.
              training_job:
                allOf:
                  - $ref: '#/components/schemas/TrainingJobV1'
                    description: The training job.
              cache:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/StorageMetricsV1'
                      - type: 'null'
                    description: The storage usage for the read-write cache.
              per_node_metrics:
                allOf:
                  - description: The metrics for each node in the training job.
                    items:
                      $ref: '#/components/schemas/TrainingJobNodeMetricsV1'
                    title: Per Node Metrics
                    type: array
            title: GetTrainingJobMetricsResponseV1
            description: >-
              A response to fetch training job metrics. The outer list for each
              metric represents that metric across time.
            refIdentifier: '#/components/schemas/GetTrainingJobMetricsResponseV1'
            requiredProperties:
              - gpu_memory_usage_bytes
              - gpu_utilization
              - cpu_usage
              - cpu_memory_usage_bytes
              - ephemeral_storage
              - training_job
              - cache
              - per_node_metrics
        examples:
          example:
            value:
              gpu_memory_usage_bytes: {}
              gpu_utilization: {}
              cpu_usage:
                - value: 123
                  timestamp: '2023-11-07T05:31:56Z'
              cpu_memory_usage_bytes:
                - value: 123
                  timestamp: '2023-11-07T05:31:56Z'
              ephemeral_storage:
                usage_bytes:
                  - value: 123
                    timestamp: '2023-11-07T05:31:56Z'
                utilization:
                  - value: 123
                    timestamp: '2023-11-07T05:31:56Z'
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
              cache:
                usage_bytes:
                  - value: 123
                    timestamp: '2023-11-07T05:31:56Z'
                utilization:
                  - value: 123
                    timestamp: '2023-11-07T05:31:56Z'
              per_node_metrics:
                - node_id: <string>
                  metrics:
                    gpu_memory_usage_bytes: {}
                    gpu_utilization: {}
                    cpu_usage:
                      - value: 123
                        timestamp: '2023-11-07T05:31:56Z'
                    cpu_memory_usage_bytes:
                      - value: 123
                        timestamp: '2023-11-07T05:31:56Z'
                    ephemeral_storage:
                      usage_bytes:
                        - value: 123
                          timestamp: '2023-11-07T05:31:56Z'
                      utilization:
                        - value: 123
                          timestamp: '2023-11-07T05:31:56Z'
        description: >-
          A response to fetch training job metrics. The outer list for each
          metric represents that metric across time.
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
    StorageMetricsV1:
      description: A metric for a training job.
      properties:
        usage_bytes:
          description: The number of bytes used on the storage entity.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Usage Bytes
          type: array
        utilization:
          description: The utilization of the storage entity as a decimal percentage.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Utilization
          type: array
      required:
        - usage_bytes
        - utilization
      title: StorageMetricsV1
      type: object
    TrainingJobMetricV1:
      description: A metric for a training job.
      properties:
        value:
          description: The value of the metric.
          title: Value
          type: number
        timestamp:
          description: The timestamp of the metric in ISO 8601 format.
          format: date-time
          title: Timestamp
          type: string
      required:
        - value
        - timestamp
      title: TrainingJobMetricV1
      type: object
    TrainingJobMetricsV1:
      properties:
        gpu_memory_usage_bytes:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: >-
            A map of GPU rank to memory usage for the training job. For
            multinode jobs, this is the memory usage of the leader unless
            specified otherwise.
          title: Gpu Memory Usage Bytes
          type: object
        gpu_utilization:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: >-
            A map of GPU rank to fractional GPU utilization. For multinode jobs,
            this is the GPU utilization of the leader unless specified
            otherwise.
          title: Gpu Utilization
          type: object
        cpu_usage:
          description: >-
            The CPU usage measured in cores. For multinode jobs, this is the CPU
            usage of the leader unless specified otherwise.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Usage
          type: array
        cpu_memory_usage_bytes:
          description: >-
            The CPU memory usage for the training job. For multinode jobs, this
            is the CPU memory usage of the leader unless specified otherwise.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Memory Usage Bytes
          type: array
        ephemeral_storage:
          $ref: '#/components/schemas/StorageMetricsV1'
          description: >-
            The storage usage for the ephemeral storage. For multinode jobs,
            this is the ephemeral storage usage of the leader unless specified
            otherwise.
      required:
        - gpu_memory_usage_bytes
        - gpu_utilization
        - cpu_usage
        - cpu_memory_usage_bytes
        - ephemeral_storage
      title: TrainingJobMetricsV1
      type: object
    TrainingJobNodeMetricsV1:
      description: A set of metrics for a training job node.
      properties:
        node_id:
          description: The name of the node.
          title: Node Id
          type: string
        metrics:
          $ref: '#/components/schemas/TrainingJobMetricsV1'
          description: The metrics for the node.
      required:
        - node_id
        - metrics
      title: TrainingJobNodeMetricsV1
      type: object

````