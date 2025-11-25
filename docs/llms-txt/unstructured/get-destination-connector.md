# Source: https://docs.unstructured.io/api-reference/destinations/get-destination-connector.md

# Get destination connector

> Retrieve detailed information for a specific destination connector by its ID.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/destinations/{destination_id}
paths:
  path: /api/v1/destinations/{destination_id}
  method: get
  servers:
    - url: https://platform.unstructuredapp.io/
      description: Unstructured Platform API
  request:
    security:
      - title: HTTPBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        destination_id:
          schema:
            - type: string
              required: true
              title: Destination Id
              format: uuid
      query: {}
      header:
        unstructured-api-key:
          schema:
            - type: string
              required: false
              title: Unstructured-Api-Key
            - type: 'null'
              required: false
              title: Unstructured-Api-Key
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
                    title: Id
              name:
                allOf:
                  - type: string
                    title: Name
              type:
                allOf:
                  - $ref: '#/components/schemas/DestinationConnectorType'
              config:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AstraDBConnectorConfig'
                      - $ref: '#/components/schemas/AzureAISearchConnectorConfig'
                      - $ref: >-
                          #/components/schemas/CouchbaseDestinationConnectorConfig
                      - $ref: '#/components/schemas/DatabricksVolumesConnectorConfig'
                      - $ref: >-
                          #/components/schemas/DatabricksVDTDestinationConnectorConfig
                      - $ref: '#/components/schemas/DeltaTableConnectorConfig'
                      - $ref: '#/components/schemas/ElasticsearchConnectorConfig'
                      - $ref: '#/components/schemas/GCSDestinationConnectorConfig'
                      - $ref: >-
                          #/components/schemas/KafkaCloudDestinationConnectorConfig
                      - $ref: '#/components/schemas/MilvusDestinationConnectorConfig'
                      - $ref: '#/components/schemas/MongoDBConnectorConfig'
                      - $ref: '#/components/schemas/Neo4jDestinationConnectorConfig'
                      - $ref: >-
                          #/components/schemas/OneDriveDestinationConnectorConfig
                      - $ref: >-
                          #/components/schemas/PineconeDestinationConnectorConfig
                      - $ref: >-
                          #/components/schemas/PostgresDestinationConnectorConfig
                      - $ref: '#/components/schemas/RedisDestinationConnectorConfig'
                      - $ref: >-
                          #/components/schemas/QdrantCloudDestinationConnectorConfig
                      - $ref: '#/components/schemas/S3DestinationConnectorConfig'
                      - $ref: >-
                          #/components/schemas/SnowflakeDestinationConnectorConfig
                      - $ref: >-
                          #/components/schemas/WeaviateDestinationConnectorConfig
                      - $ref: >-
                          #/components/schemas/IBMWatsonxS3DestinationConnectorConfig
                      - additionalProperties: true
                        type: object
                    title: Config
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              updated_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Updated At
            title: DestinationConnectorInformation
            refIdentifier: '#/components/schemas/DestinationConnectorInformation'
            requiredProperties:
              - id
              - name
              - type
              - config
              - created_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              type: astradb
              config:
                collection_name: <string>
                keyspace: <string>
                batch_size: 123
                api_endpoint: <string>
                token: <string>
              created_at: '2023-11-07T05:31:56Z'
              updated_at: '2023-11-07T05:31:56Z'
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    AstraDBConnectorConfig:
      properties:
        collection_name:
          type: string
          title: Collection Name
        keyspace:
          anyOf:
            - type: string
            - type: 'null'
          title: Keyspace
        batch_size:
          type: integer
          title: Batch Size
        api_endpoint:
          type: string
          title: Api Endpoint
        token:
          type: string
          title: Token
      type: object
      required:
        - collection_name
        - batch_size
        - api_endpoint
        - token
      title: AstraDBConnectorConfig
    AzureAISearchConnectorConfig:
      properties:
        endpoint:
          type: string
          title: Endpoint
        index:
          type: string
          title: Index
        key:
          type: string
          title: Key
      type: object
      required:
        - endpoint
        - index
        - key
      title: AzureAISearchConnectorConfig
    CouchbaseDestinationConnectorConfig:
      properties:
        bucket:
          type: string
          title: Bucket
        connection_string:
          type: string
          title: Connection String
        scope:
          anyOf:
            - type: string
            - type: 'null'
          title: Scope
        collection:
          anyOf:
            - type: string
            - type: 'null'
          title: Collection
        batch_size:
          type: integer
          title: Batch Size
        username:
          type: string
          title: Username
        password:
          type: string
          title: Password
      type: object
      required:
        - bucket
        - connection_string
        - batch_size
        - username
        - password
      title: CouchbaseDestinationConnectorConfig
    DatabricksVDTDestinationConnectorConfig:
      properties:
        server_hostname:
          type: string
          title: Server Hostname
        http_path:
          type: string
          title: Http Path
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        client_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Id
        client_secret:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Secret
        catalog:
          type: string
          title: Catalog
        database:
          type: string
          title: Database
          default: default
        table_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Table Name
        schema:
          type: string
          title: Schema
          default: default
        volume:
          type: string
          title: Volume
        volume_path:
          anyOf:
            - type: string
            - type: 'null'
          title: Volume Path
      type: object
      required:
        - server_hostname
        - http_path
        - catalog
        - volume
      title: DatabricksVDTDestinationConnectorConfig
    DatabricksVolumesConnectorConfig:
      properties:
        host:
          type: string
          title: Host
        catalog:
          type: string
          title: Catalog
        schema:
          type: string
          title: Schema
          default: default
        volume:
          type: string
          title: Volume
        volume_path:
          type: string
          title: Volume Path
        client_secret:
          type: string
          title: Client Secret
        client_id:
          type: string
          title: Client Id
      type: object
      required:
        - host
        - catalog
        - volume
        - volume_path
        - client_secret
        - client_id
      title: DatabricksVolumesConnectorConfig
    DeltaTableConnectorConfig:
      properties:
        aws_access_key_id:
          type: string
          title: Aws Access Key Id
        aws_secret_access_key:
          type: string
          title: Aws Secret Access Key
        aws_region:
          type: string
          title: Aws Region
        table_uri:
          type: string
          title: Table Uri
      type: object
      required:
        - aws_access_key_id
        - aws_secret_access_key
        - aws_region
        - table_uri
      title: DeltaTableConnectorConfig
    DestinationConnectorType:
      type: string
      enum:
        - astradb
        - azure_ai_search
        - couchbase
        - databricks_volumes
        - databricks_volume_delta_tables
        - delta_table
        - elasticsearch
        - gcs
        - kafka-cloud
        - milvus
        - mongodb
        - motherduck
        - neo4j
        - onedrive
        - pinecone
        - postgres
        - redis
        - qdrant-cloud
        - s3
        - snowflake
        - weaviate-cloud
        - ibm_watsonx_s3
      title: DestinationConnectorType
    ElasticsearchConnectorConfig:
      properties:
        hosts:
          items:
            type: string
          type: array
          title: Hosts
        index_name:
          type: string
          title: Index Name
        es_api_key:
          type: string
          title: Es Api Key
      type: object
      required:
        - hosts
        - index_name
        - es_api_key
      title: ElasticsearchConnectorConfig
    GCSDestinationConnectorConfig:
      properties:
        remote_url:
          type: string
          title: Remote Url
        service_account_key:
          type: string
          title: Service Account Key
      type: object
      required:
        - remote_url
        - service_account_key
      title: GCSDestinationConnectorConfig
    IBMWatsonxS3DestinationConnectorConfig:
      properties:
        iam_api_key:
          type: string
          title: Iam Api Key
        access_key_id:
          type: string
          title: Access Key Id
        secret_access_key:
          type: string
          title: Secret Access Key
        iceberg_endpoint:
          type: string
          title: Iceberg Endpoint
        object_storage_endpoint:
          type: string
          title: Object Storage Endpoint
        object_storage_region:
          type: string
          title: Object Storage Region
        catalog:
          type: string
          title: Catalog
        max_retries_connection:
          type: integer
          title: Max Retries Connection
        namespace:
          type: string
          title: Namespace
        table:
          type: string
          title: Table
        max_retries:
          type: integer
          title: Max Retries
        record_id_key:
          type: string
          title: Record Id Key
      type: object
      required:
        - iam_api_key
        - access_key_id
        - secret_access_key
        - iceberg_endpoint
        - object_storage_endpoint
        - object_storage_region
        - catalog
        - max_retries_connection
        - namespace
        - table
        - max_retries
        - record_id_key
      title: IBMWatsonxS3DestinationConnectorConfig
    KafkaCloudDestinationConnectorConfig:
      properties:
        bootstrap_servers:
          type: string
          title: Bootstrap Servers
        port:
          type: integer
          title: Port
        group_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Group Id
        topic:
          type: string
          title: Topic
        kafka_api_key:
          type: string
          title: Kafka Api Key
        secret:
          type: string
          title: Secret
        batch_size:
          type: integer
          title: Batch Size
      type: object
      required:
        - bootstrap_servers
        - port
        - topic
        - kafka_api_key
        - secret
        - batch_size
      title: KafkaCloudDestinationConnectorConfig
    MilvusDestinationConnectorConfig:
      properties:
        uri:
          type: string
          title: Uri
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        db_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Db Name
        collection_name:
          type: string
          title: Collection Name
        record_id_key:
          type: string
          title: Record Id Key
      type: object
      required:
        - uri
        - collection_name
        - record_id_key
      title: MilvusDestinationConnectorConfig
    MongoDBConnectorConfig:
      properties:
        database:
          type: string
          title: Database
        collection:
          type: string
          title: Collection
        uri:
          type: string
          title: Uri
      type: object
      required:
        - database
        - collection
        - uri
      title: MongoDBConnectorConfig
    Neo4jDestinationConnectorConfig:
      properties:
        uri:
          type: string
          title: Uri
        database:
          type: string
          title: Database
        username:
          type: string
          title: Username
        password:
          type: string
          title: Password
        batch_size:
          type: integer
          title: Batch Size
      type: object
      required:
        - uri
        - database
        - username
        - password
        - batch_size
      title: Neo4jDestinationConnectorConfig
    OneDriveDestinationConnectorConfig:
      properties:
        client_id:
          type: string
          title: Client Id
        user_pname:
          type: string
          title: User Pname
        tenant:
          type: string
          title: Tenant
        authority_url:
          type: string
          title: Authority Url
        client_cred:
          type: string
          title: Client Cred
        remote_url:
          type: string
          title: Remote Url
      type: object
      required:
        - client_id
        - user_pname
        - tenant
        - authority_url
        - client_cred
        - remote_url
      title: OneDriveDestinationConnectorConfig
    PineconeDestinationConnectorConfig:
      properties:
        index_name:
          type: string
          title: Index Name
        api_key:
          type: string
          title: Api Key
        namespace:
          type: string
          title: Namespace
        batch_size:
          type: integer
          title: Batch Size
      type: object
      required:
        - index_name
        - api_key
        - namespace
        - batch_size
      title: PineconeDestinationConnectorConfig
    PostgresDestinationConnectorConfig:
      properties:
        host:
          type: string
          title: Host
        database:
          type: string
          title: Database
        port:
          type: integer
          title: Port
        username:
          type: string
          title: Username
        password:
          type: string
          title: Password
        table_name:
          type: string
          title: Table Name
        batch_size:
          type: integer
          title: Batch Size
      type: object
      required:
        - host
        - database
        - port
        - username
        - password
        - table_name
        - batch_size
      title: PostgresDestinationConnectorConfig
    QdrantCloudDestinationConnectorConfig:
      properties:
        url:
          type: string
          title: Url
        api_key:
          type: string
          title: Api Key
        collection_name:
          type: string
          title: Collection Name
        batch_size:
          type: integer
          title: Batch Size
      type: object
      required:
        - url
        - api_key
        - collection_name
        - batch_size
      title: QdrantCloudDestinationConnectorConfig
    RedisDestinationConnectorConfig:
      properties:
        host:
          type: string
          title: Host
        port:
          type: integer
          title: Port
        username:
          anyOf:
            - type: string
            - type: 'null'
          title: Username
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Uri
        database:
          type: integer
          title: Database
        ssl:
          type: boolean
          title: Ssl
        batch_size:
          type: integer
          title: Batch Size
      type: object
      required:
        - host
        - port
        - database
        - ssl
        - batch_size
      title: RedisDestinationConnectorConfig
    S3DestinationConnectorConfig:
      properties:
        remote_url:
          type: string
          title: Remote Url
        anonymous:
          type: boolean
          title: Anonymous
        key:
          anyOf:
            - type: string
            - type: 'null'
          title: Key
        secret:
          anyOf:
            - type: string
            - type: 'null'
          title: Secret
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        endpoint_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Endpoint Url
      type: object
      required:
        - remote_url
        - anonymous
      title: S3DestinationConnectorConfig
    SnowflakeDestinationConnectorConfig:
      properties:
        account:
          type: string
          title: Account
        role:
          type: string
          title: Role
        user:
          type: string
          title: User
        password:
          type: string
          title: Password
        host:
          type: string
          title: Host
        port:
          type: integer
          minimum: 1
          title: Port
          default: 443
        database:
          type: string
          title: Database
        schema:
          type: string
          title: Schema
        table_name:
          type: string
          title: Table Name
          default: elements
        batch_size:
          type: integer
          minimum: 1
          title: Batch Size
          default: 50
        record_id_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Record Id Key
          default: record_id
      type: object
      required:
        - account
        - role
        - user
        - password
        - host
        - database
        - schema
      title: SnowflakeDestinationConnectorConfig
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    WeaviateDestinationConnectorConfig:
      properties:
        cluster_url:
          type: string
          title: Cluster Url
        api_key:
          type: string
          title: Api Key
        collection:
          anyOf:
            - type: string
            - type: 'null'
          title: Collection
      type: object
      required:
        - cluster_url
        - api_key
      title: WeaviateDestinationConnectorConfig

````