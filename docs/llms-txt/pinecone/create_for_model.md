# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/create_for_model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an index with integrated embedding

> Create an index with integrated embedding.
With this type of index, you provide source text, and  Pinecone uses a [hosted embedding model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models)  to convert the text automatically during [upsert](https://docs.pinecone.io/reference/api/2025-10/data-plane/upsert_records)  and [search](https://docs.pinecone.io/reference/api/2025-10/data-plane/search_records).  
For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index#integrated-embedding).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/indexes/create-for-model \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "name": "integrated-dense-curl",
          "cloud": "aws",
          "region": "us-east-1",
          "embed": {
            "model": "llama-text-embed-v2",
            "metric": "cosine",
            "field_map": {
              "text": "chunk_text"
            },
            "write_parameters": {
              "input_type": "passage",
              "truncate": "END"
            },
            "read_parameters": {
              "input_type": "query",
              "truncate": "END"
            }
          }
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9dabb7cb-ec0a-4e2e-b79e-c7c997e592ce",
    "name": "integrated-dense-curl",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": false,
      "state": "Initializing"
    },
    "host": "integrated-dense-curl-govk0nt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws"
      }
    },
    "deletion_protection": "disabled",
    "tags": null,
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "chunk_text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "input_type": "query",
        "truncate": "END"
      }
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml post /indexes/create-for-model
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
  /indexes/create-for-model:
    post:
      tags:
        - Manage Indexes
      summary: Create an index with integrated embedding
      description: >-
        Create an index with integrated embedding.

        With this type of index, you provide source text, and  Pinecone uses a
        [hosted embedding
        model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) 
        to convert the text automatically during
        [upsert](https://docs.pinecone.io/reference/api/2025-10/data-plane/upsert_records) 
        and
        [search](https://docs.pinecone.io/reference/api/2025-10/data-plane/search_records).  

        For guidance and examples, see [Create an
        index](https://docs.pinecone.io/guides/index-data/create-an-index#integrated-embedding).
      operationId: create_index_for_model
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
      requestBody:
        description: >-
          The desired configuration for the index and associated embedding
          model.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateIndexForModelRequest'
            examples:
              index-for-model:
                summary: Creating a serverless index for the specified model
                value:
                  cloud: gcp
                  deletion_protection: enabled
                  embed:
                    field_map:
                      text: your-text-field
                    metric: cosine
                    model: multilingual-e5-large
                  name: multilingual-e5-large-index
                  region: us-east1
        required: true
      responses:
        '201':
          description: The index has successfully been created for the embedding model.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IndexModel'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                index-metric-validation-error:
                  summary: Validation error
                  value:
                    error:
                      code: INVALID_ARGUMENT
                      message: >-
                        Bad request. The request body included invalid request
                        parameters.
                    status: 400
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
          description: Unknown cloud or region when creating a serverless index.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                serverless-spec-cloud-not-found:
                  summary: Cannot create serverless index with invalid spec.
                  value:
                    error:
                      code: NOT_FOUND
                      message: 'Resource cloud: aws region: us-west1 not found.'
                    status: 404
        '409':
          description: Index of given name already exists.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                index-name-already-exists:
                  summary: Index name needs to be unique
                  value:
                    error:
                      code: ALREADY_EXISTS
                      message: Resource already exists.
                    status: 409
        '422':
          description: Unprocessable entity. The request body could not be deserialized.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                missing-field:
                  summary: Unprocessable entity
                  value:
                    error:
                      code: UNPROCESSABLE_ENTITY
                      message: >-
                        Failed to deserialize the JSON body into the target
                        type: missing field `metric` at line 1 column 16
                    status: 422
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
    CreateIndexForModelRequest:
      description: The desired configuration for the index and associated embedding model.
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
        deletion_protection:
          $ref: '#/components/schemas/DeletionProtection'
        tags:
          $ref: '#/components/schemas/IndexTags'
        schema:
          $ref: '#/components/schemas/MetadataSchema'
        read_capacity:
          $ref: '#/components/schemas/ReadCapacity'
        embed:
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
          description: >-
            Specify the integrated inference embedding configuration for the
            index.


            Once set the model cannot be changed, but you can later update the
            embedding configuration for an integrated inference index including
            field map, read parameters, or write parameters.


            Refer to the [model
            guide](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models)
            for available models and model details.
          type: object
          properties:
            model:
              example: multilingual-e5-large
              description: The name of the embedding model to use for the index.
              type: string
            metric:
              description: >-
                The distance metric to be used for similarity search. You can
                use 'euclidean', 'cosine', or 'dotproduct'. If not specified,
                the metric will be defaulted according to the model. Cannot be
                updated once set.

                Possible values: `cosine`, `euclidean`, or `dotproduct`.
              x-enum:
                - cosine
                - euclidean
                - dotproduct
              type: string
            field_map:
              example:
                text: your-text-field
              description: >-
                Identifies the name of the text field from your document model
                that will be embedded.
              type: object
            dimension:
              description: The dimension of embedding vectors produced for the index.
              type: integer
            read_parameters:
              description: The read parameters for the embedding model.
              type: object
            write_parameters:
              description: The write parameters for the embedding model.
              type: object
          required:
            - model
            - field_map
      required:
        - name
        - cloud
        - region
        - embed
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
    ReadCapacity:
      description: >-
        By default the index will be created with read capacity  mode
        `OnDemand`. If you prefer to allocate dedicated read  nodes for your
        workload, you must specify mode `Dedicated` and additional
        configurations for `node_type` and `scaling`.
      discriminator:
        propertyName: mode
        mapping:
          OnDemand: '#/components/schemas/ReadCapacityOnDemandSpec'
          Dedicated: '#/components/schemas/ReadCapacityDedicatedSpec'
      oneOf:
        - $ref: '#/components/schemas/ReadCapacityOnDemandSpec'
        - $ref: '#/components/schemas/ReadCapacityDedicatedSpec'
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
    ReadCapacityOnDemandSpec:
      example:
        mode: OnDemand
      title: On-demand
      type: object
      properties:
        mode:
          description: >-
            The mode of the index. Possible values: `OnDemand` or `Dedicated`.
            Defaults to `OnDemand`. If set to `Dedicated`,
            `dedicated.node_type`, and `dedicated.scaling` must be specified.
          type: string
      required:
        - mode
      additionalProperties: false
    ReadCapacityDedicatedSpec:
      example:
        dedicated:
          manual:
            replicas: 1
            shards: 1
          node_type: t1
          scaling: Manual
        mode: Dedicated
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
      required:
        - mode
        - dedicated
      additionalProperties: true
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````