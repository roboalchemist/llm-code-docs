# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/describe_index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Describe an index

> Get a description of an index.

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl "https://api.pinecone.io/indexes/$INDEX_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" 
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  // EXAMPLE RESPONSE 1: Serverless index (on-demand)
  {
    "name": "example-serverless-ondemand-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-serverless-ondemand-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "OnDemand",
          "status": {
            "state": "Ready",
            "current_shards": null,
            "current_replicas": null
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag1": "value1",
      "tag2": "value2"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "END"
      },
      "vector_type": "dense"
    }
  }

  // EXAMPLE RESPONSE 2: Serverless index (dedicated)
  {
    "name": "example-serverless-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-serverless-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0",
      "tag1": "value1"
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml get /indexes/{index_name}
openapi: 3.0.3
info:
  title: Pinecone Control Plane API
  description: >-
    Pinecone is a vector database that makes it easy to search and retrieve
    billions of high-dimensional vectors.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://api.pinecone.io
    description: Production API endpoints
security:
  - ApiKeyAuth: []
tags:
  - name: Manage Indexes
    description: Actions that manage indexes
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /indexes/{index_name}:
    get:
      tags:
        - Manage Indexes
      summary: Describe an index
      description: Get a description of an index.
      operationId: describe_index
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: path
          name: index_name
          description: The name of the index to be described.
          required: true
          schema:
            type: string
          example: test-index
          style: simple
      responses:
        '200':
          description: Configuration information and deployment status of the index.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IndexModel'
              examples:
                movie-recommendations-serverless:
                  summary: A serverless index
                  value:
                    dimension: 1536
                    host: movie-recommendations-c01b5b5.svc.us-east1-gcp.pinecone.io
                    metric: cosine
                    name: movie-recommendations
                    spec:
                      serverless:
                        cloud: aws
                        read_capacity:
                          mode: OnDemand
                          status:
                            state: Ready
                        region: us-east-1
                        schema:
                          fields:
                            genre:
                              filterable: true
                            title:
                              filterable: true
                    status:
                      ready: false
                      state: Initializing
                    vector_type: dense
                movie-recommendations-pod:
                  summary: A pod-based index
                  value:
                    dimension: 1536
                    host: movie-recommendations-c01b5b5.svc.us-east1-gcp.pinecone.io
                    metric: cosine
                    name: movie-recommendations
                    spec:
                      pod:
                        environment: us-east-1-aws
                        metadata_config:
                          indexed:
                            - genre
                            - title
                            - imdb_rating
                        pod_type: p1.x1
                        pods: 1
                        replicas: 1
                        shards: 1
                    status:
                      ready: false
                      state: Initializing
                    vector_type: dense
          links:
            UpsertVector:
              operationId: upsert
              server:
                url: $response.body#/host
            UpdateVector:
              operationId: update
              server:
                url: $response.body#/host
            QueryVector:
              operationId: query
              server:
                url: $response.body#/host
            FetchVector:
              operationId: fetch
              server:
                url: $response.body#/host
            DeleteOneVector:
              operationId: delete1
              server:
                url: $response.body#/host
            DeleteVector:
              operationId: delete
              server:
                url: $response.body#/host
        '401':
          description: 'Unauthorized. Possible causes: Invalid API key.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Unauthorized
                  value:
                    error:
                      code: UNAUTHENTICATED
                      message: Invalid API key.
                    status: 401
        '404':
          description: Index not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                index-not-found:
                  summary: Index not found
                  value:
                    error:
                      code: NOT_FOUND
                      message: Index example-index not found.
                    status: 404
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                internal-server-error:
                  summary: Internal server error
                  value:
                    error:
                      code: UNKNOWN
                      message: Internal server error
                    status: 500
components:
  schemas:
    IndexModel:
      description: >-
        The IndexModel describes the configuration and status of a Pinecone
        index.
      type: object
      properties:
        name:
          example: example-index
          description: >
            The name of the index. Resource name must be 1-45 characters long,
            start and end with an alphanumeric character, and consist only of
            lower case alphanumeric characters or '-'.
          type: string
          minLength: 1
          maxLength: 45
        dimension:
          example: 1536
          description: The dimensions of the vectors to be inserted in the index.
          type: integer
          format: int32
          minimum: 1
          maximum: 20000
        metric:
          description: >-
            The distance metric to be used for similarity search. You can use
            'euclidean', 'cosine', or 'dotproduct'. If the 'vector_type' is
            'sparse', the metric must be 'dotproduct'. If the `vector_type` is
            `dense`, the metric defaults to 'cosine'.

            Possible values: `cosine`, `euclidean`, or `dotproduct`.
          x-enum:
            - cosine
            - euclidean
            - dotproduct
          type: string
        host:
          example: semantic-search-c01b5b5.svc.us-west1-gcp.pinecone.io
          description: The URL address where the index is hosted.
          type: string
        private_host:
          example: semantic-search-c01b5b5.svc.private.us-west1-gcp.pinecone.io
          description: The private endpoint URL of an index.
          type: string
        deletion_protection:
          $ref: '#/components/schemas/DeletionProtection'
        tags:
          $ref: '#/components/schemas/IndexTags'
        embed:
          $ref: '#/components/schemas/ModelIndexEmbed'
        spec:
          example:
            pod:
              environment: us-east-1-aws
              metadata_config:
                indexed:
                  - genre
                  - title
                  - imdb_rating
              pod_type: p1.x1
              pods: 1
              replicas: 1
              shards: 1
          description: The spec object defines how the index should be deployed.
          type: object
          oneOf:
            - title: Serverless
              type: object
              properties:
                serverless:
                  $ref: '#/components/schemas/ServerlessSpecResponse'
              required:
                - serverless
              additionalProperties: false
            - title: Pod-based
              type: object
              properties:
                pod:
                  $ref: '#/components/schemas/PodSpec'
              required:
                - pod
              additionalProperties: false
            - title: BYOC
              type: object
              properties:
                byoc:
                  $ref: '#/components/schemas/ByocSpecResponse'
              required:
                - byoc
              additionalProperties: false
        status:
          example:
            ready: true
            state: ScalingUpPodSize
          description: The current status of the index
          type: object
          properties:
            ready:
              description: Whether the index is ready for use
              type: boolean
            state:
              description: >-
                The state of the index.

                Possible values: `Initializing`, `InitializationFailed`,
                `ScalingUp`, `ScalingDown`, `ScalingUpPodSize`,
                `ScalingDownPodSize`, `Terminating`, `Ready`, or `Disabled`.
              x-enum:
                - Initializing
                - InitializationFailed
                - ScalingUp
                - ScalingDown
                - ScalingUpPodSize
                - ScalingDownPodSize
                - Terminating
                - Ready
                - Disabled
              type: string
          required:
            - ready
            - state
        vector_type:
          description: >-
            The index vector type. You can use 'dense' or 'sparse'. If 'dense',
            the vector dimension must be specified.  If 'sparse', the vector
            dimension should not be specified.
          default: dense
          type: string
      required:
        - name
        - metric
        - status
        - spec
        - host
        - vector_type
    ErrorResponse:
      example:
        error:
          code: QUOTA_EXCEEDED
          message: >-
            The index exceeds the project quota of 5 pods by 2 pods. Upgrade
            your account or change the project settings to increase the quota.
        status: 429
      description: The response shape used for all error responses.
      type: object
      properties:
        status:
          example: 500
          description: The HTTP status code of the error.
          type: integer
        error:
          example:
            code: INVALID_ARGUMENT
            message: >-
              Index name must contain only lowercase alphanumeric characters or
              hyphens, and must not begin or end with a hyphen.
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              description: >-
                The error code.

                Possible values: `OK`, `UNKNOWN`, `INVALID_ARGUMENT`,
                `DEADLINE_EXCEEDED`, `QUOTA_EXCEEDED`, `NOT_FOUND`,
                `ALREADY_EXISTS`, `PERMISSION_DENIED`, `UNAUTHENTICATED`,
                `RESOURCE_EXHAUSTED`, `FAILED_PRECONDITION`, `ABORTED`,
                `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`,
                `DATA_LOSS`, `FORBIDDEN`, `UNPROCESSABLE_ENTITY`, or
                `PAYMENT_REQUIRED`.
              x-enum:
                - OK
                - UNKNOWN
                - INVALID_ARGUMENT
                - DEADLINE_EXCEEDED
                - QUOTA_EXCEEDED
                - NOT_FOUND
                - ALREADY_EXISTS
                - PERMISSION_DENIED
                - UNAUTHENTICATED
                - RESOURCE_EXHAUSTED
                - FAILED_PRECONDITION
                - ABORTED
                - OUT_OF_RANGE
                - UNIMPLEMENTED
                - INTERNAL
                - UNAVAILABLE
                - DATA_LOSS
                - FORBIDDEN
                - UNPROCESSABLE_ENTITY
                - PAYMENT_REQUIRED
              type: string
            message:
              example: >-
                Index name must contain only lowercase alphanumeric characters
                or hyphens, and must not begin or end with a hyphen.
              description: A human-readable description of the error
              type: string
            details:
              description: >-
                Additional information about the error. This field is not
                guaranteed to be present.
              type: object
          required:
            - code
            - message
      required:
        - status
        - error
    DeletionProtection:
      description: >-
        Whether [deletion
        protection](http://docs.pinecone.io/guides/manage-data/manage-indexes#configure-deletion-protection)
        is enabled/disabled for the index.

        Possible values: `disabled` or `enabled`.
      default: disabled
      x-enum:
        - disabled
        - enabled
      type: string
    IndexTags:
      example:
        tag0: val0
        tag1: val1
      description: >-
        Custom user tags added to an index. Keys must be 80 characters or less.
        Values must be 120 characters or less. Keys must be alphanumeric, '_',
        or '-'.  Values must be alphanumeric, ';', '@', '_', '-', '.', '+', or '
        '. To unset a key, set the value to be an empty string.
      type: object
      additionalProperties:
        type: string
    ModelIndexEmbed:
      example:
        field_map:
          text: your-text-field
        metric: cosine
        model: multilingual-e5-large
        read_parameters:
          input_type: query
          truncate: NONE
        write_parameters:
          input_type: passage
      description: The embedding model and document fields mapped to embedding inputs.
      type: object
      properties:
        model:
          example: multilingual-e5-large
          description: The name of the embedding model used to create the index.
          type: string
        metric:
          description: >-
            The distance metric to be used for similarity search. You can use
            'euclidean', 'cosine', or 'dotproduct'. If not specified, the metric
            will be defaulted according to the model. Cannot be updated once
            set.

            Possible values: `cosine`, `euclidean`, or `dotproduct`.
          x-enum:
            - cosine
            - euclidean
            - dotproduct
          type: string
        dimension:
          example: 1536
          description: The dimensions of the vectors to be inserted in the index.
          type: integer
          format: int32
          minimum: 1
          maximum: 20000
        vector_type:
          description: >-
            The index vector type. You can use 'dense' or 'sparse'. If 'dense',
            the vector dimension must be specified.  If 'sparse', the vector
            dimension should not be specified.
          default: dense
          type: string
        field_map:
          example:
            text: your-text-field
          description: >-
            Identifies the name of the text field from your document model that
            is embedded.
          type: object
        read_parameters:
          description: The read parameters for the embedding model.
          type: object
        write_parameters:
          description: The write parameters for the embedding model.
          type: object
      required:
        - model
    ServerlessSpecResponse:
      description: Configuration of a serverless index.
      type: object
      properties:
        cloud:
          example: aws
          description: |-
            The public cloud where you would like your index hosted.
            Possible values: `gcp`, `aws`, or `azure`.
          x-enum:
            - gcp
            - aws
            - azure
          type: string
        region:
          example: us-east-1
          description: The region where you would like your index to be created.
          type: string
        read_capacity:
          $ref: '#/components/schemas/ReadCapacityResponse'
        source_collection:
          example: movie-embeddings
          description: The name of the collection to be used as the source for the index.
          type: string
        schema:
          $ref: '#/components/schemas/MetadataSchema'
      required:
        - cloud
        - region
        - read_capacity
    PodSpec:
      example:
        environment: us-east1-gcp
        metadata_config:
          indexed:
            - genre
            - title
            - imdb_rating
        pod_type: p1.x1
        pods: 1
        replicas: 1
        shards: 1
        source_collection: movie-embeddings
      title: Pod-based
      description: Configuration needed to deploy a pod-based index.
      type: object
      properties:
        environment:
          example: us-east1-gcp
          description: The environment where the index is hosted.
          type: string
        replicas:
          description: >-
            The number of replicas. Replicas duplicate your index. They provide
            higher availability and throughput. Replicas can be scaled up or
            down as your needs change.
          default: 1
          type: integer
          format: int32
          minimum: 1
        shards:
          description: >-
            The number of shards. Shards split your data across multiple pods so
            you can fit more data into an index.
          default: 1
          type: integer
          format: int32
          minimum: 1
        pod_type:
          description: >-
            The type of pod to use. One of `s1`, `p1`, or `p2` appended with `.`
            and one of `x1`, `x2`, `x4`, or `x8`.
          default: p1.x1
          type: string
        pods:
          example: 1
          description: >-
            The number of pods to be used in the index. This should be equal to
            `shards` x `replicas`.'
          default: 1
          type: integer
          minimum: 1
        metadata_config:
          example:
            indexed:
              - genre
              - title
              - imdb_rating
          description: >-
            Configuration for the behavior of Pinecone's internal metadata
            index. By default, all metadata is indexed; when `metadata_config`
            is present, only specified metadata fields are indexed. These
            configurations are only valid for use with pod-based indexes.
          type: object
          properties:
            indexed:
              description: >-
                By default, all metadata is indexed; to change this behavior,
                use this property to specify an array of metadata fields that
                should be indexed.
              type: array
              items:
                type: string
        source_collection:
          example: movie-embeddings
          description: The name of the collection to be used as the source for the index.
          type: string
      required:
        - environment
        - pod_type
    ByocSpecResponse:
      title: BYOC
      description: Configuration of a BYOC index.
      type: object
      properties:
        environment:
          example: aws-us-east-1-b921
          description: The environment where the index is hosted.
          type: string
        read_capacity:
          $ref: '#/components/schemas/ReadCapacityResponse'
        schema:
          $ref: '#/components/schemas/MetadataSchema'
      required:
        - environment
        - read_capacity
    ReadCapacityResponse:
      description: Response containing read capacity configuration
      discriminator:
        propertyName: mode
        mapping:
          OnDemand: '#/components/schemas/ReadCapacityOnDemandSpecResponse'
          Dedicated: '#/components/schemas/ReadCapacityDedicatedSpecResponse'
      oneOf:
        - $ref: '#/components/schemas/ReadCapacityOnDemandSpecResponse'
        - $ref: '#/components/schemas/ReadCapacityDedicatedSpecResponse'
    MetadataSchema:
      example:
        fields:
          description:
            filterable: true
          genre:
            filterable: true
          year:
            filterable: true
      description: >-
        Schema for the behavior of Pinecone's internal metadata index. By
        default, all metadata is indexed; when `schema` is present, only fields
        which are present in the `fields` object with a `filterable: true` are
        indexed. Note that `filterable: false` is not currently supported.
      type: object
      properties:
        fields:
          description: >-
            A map of metadata field names to their configuration. The field name
            must be a valid metadata field name. The field name must be unique.
          type: object
          additionalProperties:
            type: object
            properties:
              filterable:
                description: >-
                  Whether the field is filterable. If true, the field is indexed
                  and can be used in filters. Only true values are allowed.
                type: boolean
      required:
        - fields
    ReadCapacityOnDemandSpecResponse:
      example:
        mode: OnDemand
        status:
          state: Ready
      title: On-demand
      type: object
      properties:
        mode:
          description: >-
            The mode of the index. Possible values: `OnDemand` or `Dedicated`.
            Defaults to `OnDemand`. If set to `Dedicated`,
            `dedicated.node_type`, and `dedicated.scaling` must be specified.
          type: string
        status:
          $ref: '#/components/schemas/ReadCapacityStatus'
      required:
        - mode
        - status
      additionalProperties: false
    ReadCapacityDedicatedSpecResponse:
      example:
        dedicated:
          manual:
            replicas: 2
            shards: 2
          node_type: t1
          scaling: Manual
        mode: Dedicated
        status:
          current_replicas: 2
          current_shards: 2
          state: Ready
      title: Dedicated
      type: object
      properties:
        mode:
          description: >-
            The mode of the index. Possible values: `OnDemand` or `Dedicated`.
            Defaults to `OnDemand`. If set to `Dedicated`,
            `dedicated.node_type`, and `dedicated.scaling` must be specified.
          type: string
        dedicated:
          $ref: '#/components/schemas/ReadCapacityDedicatedConfig'
        status:
          $ref: '#/components/schemas/ReadCapacityStatus'
      required:
        - mode
        - dedicated
        - status
      additionalProperties: false
    ReadCapacityStatus:
      description: >-
        The current status of factors affecting the read capacity of a
        serverless index
      type: object
      properties:
        state:
          description: >-
            The `state` describes the overall status of factors relating to the
            read capacity of an index. 


            Available values:

            - `Ready` is the state most of the time

            - `Scaling` if the number of replicas or shards has been recently
            updated by calling the [configure index
            endpoint](https://docs.pinecone.io/reference/api/2025-10/control-plane/configure_index)

            - `Migrating` if the index is being migrated to a new `node_type`

            - `Error` if there is an error with the read capacity configuration.
            In that case, see `error_message` for more details.
          type: string
        current_replicas:
          description: >-
            The number of replicas. Each replica has dedicated  compute
            resources and data storage. Increasing this number  will increase
            the total throughput of the index.
          type: integer
          format: int32
        current_shards:
          description: >-
            The number of shards. Each shard has dedicated storage.  Increasing
            shards alleiviates index fullness. 
          type: integer
          format: int32
        error_message:
          description: >-
            An optional error message indicating any issues with your read
            capacity configuration
          type: string
      required:
        - state
    ReadCapacityDedicatedConfig:
      description: >-
        Configuration for dedicated read capacity. See  [this
        guide](https://docs.pinecone.io/guides/index-data/dedicated-read-nodes)
        for more details on  how to configure dedicated read capacity.
      type: object
      properties:
        node_type:
          description: >-
            The type of machines to use. Available options: `b1` and `t1`. `t1`
            includes increased processing power and memory.
          type: string
        scaling:
          description: The type of scaling strategy to use.
          type: string
        manual:
          $ref: '#/components/schemas/ScalingConfigManual'
    ScalingConfigManual:
      description: The config to use for manual read capacity scaling.
      type: object
      properties:
        replicas:
          description: >-
            The number of replicas to use. Replicas duplicate the compute
            resources and data of an index, allowing higher query throughput and
            availability. Setting replicas to 0 disables the index but can be
            used to reduce costs while usage is paused.
          type: integer
          format: int32
          minimum: 0
        shards:
          description: >-
            The number of shards to use. Shards determine the storage capacity
            of an index, with each shard providing 250 GB of storage.
          type: integer
          format: int32
          minimum: 1
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````