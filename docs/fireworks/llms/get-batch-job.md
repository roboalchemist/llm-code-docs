# Source: https://docs.fireworks.ai/api-reference-dlde/get-batch-job.md

# Get Batch Job

## OpenAPI

````yaml get /v1/accounts/{account_id}/batchJobs/{batch_job_id}
paths:
  path: /v1/accounts/{account_id}/batchJobs/{batch_job_id}
  method: get
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
        batch_job_id:
          schema:
            - type: string
              required: true
              description: The Batch Job Id
      query:
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    title: >-
                      The resource name of the batch job.

                      e.g.
                      accounts/my-account/clusters/my-cluster/batchJobs/123456789
                    readOnly: true
              displayName:
                allOf:
                  - type: string
                    description: >-
                      Human-readable display name of the batch job. e.g. "My
                      Batch Job"

                      Must be fewer than 64 characters long.
              createTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The creation time of the batch job.
                    readOnly: true
              startTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The time when the batch job started running.
                    readOnly: true
              endTime:
                allOf:
                  - type: string
                    format: date-time
                    description: >-
                      The time when the batch job completed, failed, or was
                      cancelled.
                    readOnly: true
              createdBy:
                allOf:
                  - type: string
                    description: The email address of the user who created this batch job.
                    readOnly: true
              nodePoolId:
                allOf:
                  - type: string
                    title: >-
                      The ID of the node pool that this batch job should use.
                      e.g. my-node-pool
              environmentId:
                allOf:
                  - type: string
                    description: >-
                      The ID of the environment that this batch job should use.
                      e.g. my-env

                      If specified, image_ref must not be specified.
              snapshotId:
                allOf:
                  - type: string
                    description: >-
                      The ID of the snapshot used by this batch job.

                      If specified, environment_id must be specified and
                      image_ref must not be

                      specified.
              numRanks:
                allOf:
                  - type: integer
                    format: int32
                    description: |-
                      For GPU node pools: one GPU per rank w/ host packing,
                      for CPU node pools: one host per rank.
              envVars:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    description: >-
                      Environment variables to be passed during this job's
                      execution.
              role:
                allOf:
                  - type: string
                    description: >-
                      The ARN of the AWS IAM role that the batch job should
                      assume.

                      If not specified, the connection will fall back to the
                      node

                      pool's node_role.
              pythonExecutor:
                allOf:
                  - $ref: '#/components/schemas/gatewayPythonExecutor'
              notebookExecutor:
                allOf:
                  - $ref: '#/components/schemas/gatewayNotebookExecutor'
              shellExecutor:
                allOf:
                  - $ref: '#/components/schemas/gatewayShellExecutor'
              imageRef:
                allOf:
                  - type: string
                    description: >-
                      The container image used by this job. If specified,
                      environment_id and

                      snapshot_id must not be specified.
              annotations:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    description: >-
                      Arbitrary, user-specified metadata.

                      Keys and values must adhere to Kubernetes constraints:
                      https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set

                      Additionally, the "fireworks.ai/" prefix is reserved.
              state:
                allOf:
                  - $ref: '#/components/schemas/gatewayBatchJobState'
                    description: The current state of the batch job.
                    readOnly: true
              status:
                allOf:
                  - type: string
                    description: >-
                      Detailed information about the current status of the batch
                      job.
                    readOnly: true
              shared:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the batch job is shared with all users in the
                      account.

                      This allows all users to update, delete, clone, and create
                      environments

                      using the batch job.
              updateTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The update time for the batch job.
                    readOnly: true
            title: 'Next ID: 22'
            refIdentifier: '#/components/schemas/gatewayBatchJob'
            requiredProperties:
              - nodePoolId
        examples:
          example:
            value:
              name: <string>
              displayName: <string>
              createTime: '2023-11-07T05:31:56Z'
              startTime: '2023-11-07T05:31:56Z'
              endTime: '2023-11-07T05:31:56Z'
              createdBy: <string>
              nodePoolId: <string>
              environmentId: <string>
              snapshotId: <string>
              numRanks: 123
              envVars: {}
              role: <string>
              pythonExecutor:
                targetType: TARGET_TYPE_UNSPECIFIED
                target: <string>
                args:
                  - <string>
              notebookExecutor:
                notebookFilename: <string>
              shellExecutor:
                command: <string>
              imageRef: <string>
              annotations: {}
              state: STATE_UNSPECIFIED
              status: <string>
              shared: true
              updateTime: '2023-11-07T05:31:56Z'
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    PythonExecutorTargetType:
      type: string
      enum:
        - TARGET_TYPE_UNSPECIFIED
        - MODULE
        - FILENAME
      default: TARGET_TYPE_UNSPECIFIED
      description: |2-
         - MODULE: Runs a python module, i.e. passed as -m argument.
         - FILENAME: Runs a python file.
    gatewayBatchJobState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - CREATING
        - QUEUED
        - PENDING
        - RUNNING
        - COMPLETED
        - FAILED
        - CANCELLING
        - CANCELLED
        - DELETING
      default: STATE_UNSPECIFIED
      description: |-
        - CREATING: The batch job is being created.
         - QUEUED: The batch job is in the queue and waiting to be scheduled.
        Currently unused.
         - PENDING: The batch job scheduled and is waiting for resource allocation.
         - RUNNING: The batch job is running.
         - COMPLETED: The batch job has finished successfully.
         - FAILED: The batch job has failed.
         - CANCELLING: The batch job is being cancelled.
         - CANCELLED: The batch job was cancelled.
         - DELETING: The batch job is being deleted.
      title: 'Next ID: 10'
    gatewayNotebookExecutor:
      type: object
      properties:
        notebookFilename:
          type: string
          description: Path to a notebook file to be executed.
      description: Execute a notebook file.
      required:
        - notebookFilename
    gatewayPythonExecutor:
      type: object
      properties:
        targetType:
          $ref: '#/components/schemas/PythonExecutorTargetType'
          description: The type of Python target to run.
        target:
          type: string
          description: A Python module or filename depending on TargetType.
        args:
          type: array
          items:
            type: string
          description: Command line arguments to pass to the Python process.
      description: Execute a Python process.
      required:
        - targetType
        - target
    gatewayShellExecutor:
      type: object
      properties:
        command:
          type: string
          title: Command we want to run for the shell script
      description: Execute a shell script.
      required:
        - command

````