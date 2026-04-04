# Source: https://docs.fireworks.ai/api-reference-dlde/list-batch-jobs.md

# List Batch Jobs

## OpenAPI

````yaml get /v1/accounts/{account_id}/batchJobs
paths:
  path: /v1/accounts/{account_id}/batchJobs
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
      query:
        pageSize:
          schema:
            - type: integer
              required: false
              description: >-
                The maximum number of batch jobs to return. The maximum
                page_size is 200,

                values above 200 will be coerced to 200.

                If unspecified, the default is 50.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                A page token, received from a previous ListBatchJobs call.
                Provide this

                to retrieve the subsequent page. When paginating, all other
                parameters

                provided to ListBatchJobs must match the call that provided the
                page

                token.
        filter:
          schema:
            - type: string
              required: false
              description: >-
                Only batch jobs satisfying the provided filter (if specified)
                will be

                returned. See https://google.aip.dev/160 for the filter grammar.
        orderBy:
          schema:
            - type: string
              required: false
              description: >-
                A comma-separated list of fields to order by. e.g. "foo,bar"

                The default sort order is ascending. To specify a descending
                order for a

                field, append a " desc" suffix. e.g. "foo desc,bar"

                Subfields are specified with a "." character. e.g. "foo.bar"

                If not specified, the default order is by "create_time desc".
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
              batchJobs:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayBatchJob'
              nextPageToken:
                allOf:
                  - type: string
                    description: >-
                      A token, which can be sent as `page_token` to retrieve the
                      next page.

                      If this field is omitted, there are no subsequent pages.
              totalSize:
                allOf:
                  - type: integer
                    format: int32
                    description: The total number of batch jobs.
            refIdentifier: '#/components/schemas/gatewayListBatchJobsResponse'
        examples:
          example:
            value:
              batchJobs:
                - name: <string>
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
              nextPageToken: <string>
              totalSize: 123
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
    gatewayBatchJob:
      type: object
      properties:
        name:
          type: string
          title: |-
            The resource name of the batch job.
            e.g. accounts/my-account/clusters/my-cluster/batchJobs/123456789
          readOnly: true
        displayName:
          type: string
          description: |-
            Human-readable display name of the batch job. e.g. "My Batch Job"
            Must be fewer than 64 characters long.
        createTime:
          type: string
          format: date-time
          description: The creation time of the batch job.
          readOnly: true
        startTime:
          type: string
          format: date-time
          description: The time when the batch job started running.
          readOnly: true
        endTime:
          type: string
          format: date-time
          description: The time when the batch job completed, failed, or was cancelled.
          readOnly: true
        createdBy:
          type: string
          description: The email address of the user who created this batch job.
          readOnly: true
        nodePoolId:
          type: string
          title: >-
            The ID of the node pool that this batch job should use. e.g.
            my-node-pool
        environmentId:
          type: string
          description: >-
            The ID of the environment that this batch job should use. e.g.
            my-env

            If specified, image_ref must not be specified.
        snapshotId:
          type: string
          description: >-
            The ID of the snapshot used by this batch job.

            If specified, environment_id must be specified and image_ref must
            not be

            specified.
        numRanks:
          type: integer
          format: int32
          description: |-
            For GPU node pools: one GPU per rank w/ host packing,
            for CPU node pools: one host per rank.
        envVars:
          type: object
          additionalProperties:
            type: string
          description: Environment variables to be passed during this job's execution.
        role:
          type: string
          description: |-
            The ARN of the AWS IAM role that the batch job should assume.
            If not specified, the connection will fall back to the node
            pool's node_role.
        pythonExecutor:
          $ref: '#/components/schemas/gatewayPythonExecutor'
        notebookExecutor:
          $ref: '#/components/schemas/gatewayNotebookExecutor'
        shellExecutor:
          $ref: '#/components/schemas/gatewayShellExecutor'
        imageRef:
          type: string
          description: >-
            The container image used by this job. If specified, environment_id
            and

            snapshot_id must not be specified.
        annotations:
          type: object
          additionalProperties:
            type: string
          description: >-
            Arbitrary, user-specified metadata.

            Keys and values must adhere to Kubernetes constraints:
            https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set

            Additionally, the "fireworks.ai/" prefix is reserved.
        state:
          $ref: '#/components/schemas/gatewayBatchJobState'
          description: The current state of the batch job.
          readOnly: true
        status:
          type: string
          description: Detailed information about the current status of the batch job.
          readOnly: true
        shared:
          type: boolean
          description: >-
            Whether the batch job is shared with all users in the account.

            This allows all users to update, delete, clone, and create
            environments

            using the batch job.
        updateTime:
          type: string
          format: date-time
          description: The update time for the batch job.
          readOnly: true
      title: 'Next ID: 22'
      required:
        - nodePoolId
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