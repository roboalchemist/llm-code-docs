# Source: https://docs.unstructured.io/api-reference/sources/update-source-connector.md

# Update source connector

> Update the configuration of an existing source connector.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json put /api/v1/sources/{source_id}
paths:
  path: /api/v1/sources/{source_id}
  method: put
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
        source_id:
          schema:
            - type: string
              required: true
              title: Source Id
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              config:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AzureSourceConnectorConfigInput'
                      - $ref: '#/components/schemas/BoxSourceConnectorConfigInput'
                      - $ref: >-
                          #/components/schemas/ConfluenceSourceConnectorConfigInput
                      - $ref: >-
                          #/components/schemas/CouchbaseSourceConnectorConfigInput
                      - $ref: >-
                          #/components/schemas/DatabricksVolumesConnectorConfigInput
                      - $ref: '#/components/schemas/DropboxSourceConnectorConfigInput'
                      - $ref: '#/components/schemas/ElasticsearchConnectorConfigInput'
                      - $ref: '#/components/schemas/GCSSourceConnectorConfigInput'
                      - $ref: >-
                          #/components/schemas/GoogleDriveSourceConnectorConfigInput
                      - $ref: >-
                          #/components/schemas/KafkaCloudSourceConnectorConfigInput
                      - $ref: '#/components/schemas/MongoDBConnectorConfigInput'
                      - $ref: >-
                          #/components/schemas/OneDriveSourceConnectorConfigInput
                      - $ref: '#/components/schemas/OutlookSourceConnectorConfigInput'
                      - $ref: >-
                          #/components/schemas/PostgresSourceConnectorConfigInput
                      - $ref: '#/components/schemas/S3SourceConnectorConfigInput'
                      - $ref: >-
                          #/components/schemas/SalesforceSourceConnectorConfigInput
                      - $ref: >-
                          #/components/schemas/SharePointSourceConnectorConfigInput
                      - $ref: >-
                          #/components/schemas/SnowflakeSourceConnectorConfigInput
                      - $ref: '#/components/schemas/JiraSourceConnectorConfigInput'
                      - $ref: '#/components/schemas/ZendeskSourceConnectorConfigInput'
                      - additionalProperties: true
                        type: object
                    title: Config
            required: true
            title: UpdateSourceConnector
            refIdentifier: '#/components/schemas/UpdateSourceConnector'
            requiredProperties:
              - config
        examples:
          example:
            value:
              config:
                remote_url: <string>
                account_name: <string>
                account_key: <string>
                connection_string: <string>
                sas_token: <string>
                recursive: true
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
                  - $ref: '#/components/schemas/SourceConnectorType'
              config:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AzureSourceConnectorConfig'
                      - $ref: '#/components/schemas/BoxSourceConnectorConfig'
                      - $ref: '#/components/schemas/ConfluenceSourceConnectorConfig'
                      - $ref: '#/components/schemas/CouchbaseSourceConnectorConfig'
                      - $ref: '#/components/schemas/DatabricksVolumesConnectorConfig'
                      - $ref: '#/components/schemas/DropboxSourceConnectorConfig'
                      - $ref: '#/components/schemas/ElasticsearchConnectorConfig'
                      - $ref: '#/components/schemas/GCSSourceConnectorConfig'
                      - $ref: '#/components/schemas/GoogleDriveSourceConnectorConfig'
                      - $ref: '#/components/schemas/KafkaCloudSourceConnectorConfig'
                      - $ref: '#/components/schemas/MongoDBConnectorConfig'
                      - $ref: '#/components/schemas/OneDriveSourceConnectorConfig'
                      - $ref: '#/components/schemas/OutlookSourceConnectorConfig'
                      - $ref: '#/components/schemas/PostgresSourceConnectorConfig'
                      - $ref: '#/components/schemas/S3SourceConnectorConfig'
                      - $ref: '#/components/schemas/SalesforceSourceConnectorConfig'
                      - $ref: '#/components/schemas/SharePointSourceConnectorConfig'
                      - $ref: '#/components/schemas/SnowflakeSourceConnectorConfig'
                      - $ref: '#/components/schemas/JiraSourceConnectorConfig'
                      - $ref: '#/components/schemas/ZendeskSourceConnectorConfig'
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
            title: SourceConnectorInformation
            refIdentifier: '#/components/schemas/SourceConnectorInformation'
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
              type: azure
              config:
                remote_url: <string>
                account_name: <string>
                account_key: <string>
                connection_string: <string>
                sas_token: <string>
                recursive: true
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
    AzureSourceConnectorConfig:
      properties:
        remote_url:
          type: string
          title: Remote Url
        account_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Name
        account_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Key
        connection_string:
          anyOf:
            - type: string
            - type: 'null'
          title: Connection String
        sas_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Sas Token
        recursive:
          type: boolean
          title: Recursive
      type: object
      required:
        - remote_url
        - recursive
      title: AzureSourceConnectorConfig
    AzureSourceConnectorConfigInput:
      properties:
        remote_url:
          type: string
          pattern: ^(az:\/\/|abfs:\/\/)
          title: Remote Url
        account_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Name
        account_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Key
        connection_string:
          anyOf:
            - type: string
            - type: 'null'
          title: Connection String
        sas_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Sas Token
        recursive:
          type: boolean
          title: Recursive
          default: true
      type: object
      required:
        - remote_url
      title: AzureSourceConnectorConfigInput
    BoxSourceConnectorConfig:
      properties:
        box_app_config:
          type: string
          title: Box App Config
        recursive:
          type: boolean
          title: Recursive
      type: object
      required:
        - box_app_config
        - recursive
      title: BoxSourceConnectorConfig
    BoxSourceConnectorConfigInput:
      properties:
        box_app_config:
          type: string
          title: Box App Config
        remote_url:
          type: string
          pattern: ^box:\/\/
          title: Remote Url
        recursive:
          type: boolean
          title: Recursive
          default: true
      type: object
      required:
        - box_app_config
        - remote_url
      title: BoxSourceConnectorConfigInput
    ConfluenceSourceConnectorConfig:
      properties:
        url:
          type: string
          title: Url
        username:
          type: string
          title: Username
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        api_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Api Token
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        cloud:
          type: boolean
          title: Cloud
        extract_images:
          type: boolean
          title: Extract Images
          default: false
        extract_files:
          type: boolean
          title: Extract Files
          default: false
        max_num_of_spaces:
          type: integer
          title: Max Num Of Spaces
        max_num_of_docs_from_each_space:
          type: integer
          title: Max Num Of Docs From Each Space
        spaces:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Spaces
      type: object
      required:
        - url
        - username
        - cloud
        - max_num_of_spaces
        - max_num_of_docs_from_each_space
        - spaces
      title: ConfluenceSourceConnectorConfig
    ConfluenceSourceConnectorConfigInput:
      properties:
        url:
          type: string
          title: Url
        username:
          type: string
          title: Username
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        api_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Api Token
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        cloud:
          type: boolean
          title: Cloud
          default: false
        extract_images:
          type: boolean
          title: Extract Images
          default: false
        extract_files:
          type: boolean
          title: Extract Files
          default: false
        max_num_of_spaces:
          type: integer
          minimum: 1
          title: Max Num Of Spaces
          default: 500
        max_num_of_docs_from_each_space:
          type: integer
          minimum: 1
          title: Max Num Of Docs From Each Space
          default: 150
        spaces:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Spaces
      type: object
      required:
        - url
        - username
      title: ConfluenceSourceConnectorConfigInput
    CouchbaseSourceConnectorConfig:
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
        collection_id:
          type: string
          title: Collection Id
      type: object
      required:
        - bucket
        - connection_string
        - batch_size
        - username
        - password
        - collection_id
      title: CouchbaseSourceConnectorConfig
    CouchbaseSourceConnectorConfigInput:
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
        collection_id:
          type: string
          title: Collection Id
      type: object
      required:
        - bucket
        - connection_string
        - batch_size
        - username
        - password
        - collection_id
      title: CouchbaseSourceConnectorConfigInput
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
    DatabricksVolumesConnectorConfigInput:
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
      title: DatabricksVolumesConnectorConfigInput
    DropboxSourceConnectorConfig:
      properties:
        token:
          type: string
          title: Token
        remote_url:
          type: string
          title: Remote Url
        recursive:
          type: boolean
          title: Recursive
      type: object
      required:
        - token
        - remote_url
        - recursive
      title: DropboxSourceConnectorConfig
    DropboxSourceConnectorConfigInput:
      properties:
        token:
          type: string
          title: Token
        remote_url:
          type: string
          pattern: ^dropbox:\/\/
          title: Remote Url
        recursive:
          type: boolean
          title: Recursive
          default: true
      type: object
      required:
        - token
        - remote_url
      title: DropboxSourceConnectorConfigInput
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
    ElasticsearchConnectorConfigInput:
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
      title: ElasticsearchConnectorConfigInput
    EncryptionType:
      type: string
      enum:
        - rsa
        - rsa_aes
      title: EncryptionType
    GCSSourceConnectorConfig:
      properties:
        remote_url:
          type: string
          title: Remote Url
        service_account_key:
          type: string
          title: Service Account Key
        recursive:
          type: boolean
          title: Recursive
      type: object
      required:
        - remote_url
        - service_account_key
        - recursive
      title: GCSSourceConnectorConfig
    GCSSourceConnectorConfigInput:
      properties:
        remote_url:
          type: string
          pattern: ^(gs|gcs):\/\/
          title: Remote Url
        service_account_key:
          type: string
          title: Service Account Key
        recursive:
          type: boolean
          title: Recursive
          default: true
      type: object
      required:
        - remote_url
        - service_account_key
      title: GCSSourceConnectorConfigInput
    GoogleDriveSourceConnectorConfig:
      properties:
        drive_id:
          type: string
          title: Drive Id
        service_account_key:
          anyOf:
            - $ref: '#/components/schemas/SecretReference'
            - type: string
          title: Service Account Key
        extensions:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Extensions
        recursive:
          type: boolean
          title: Recursive
      type: object
      required:
        - drive_id
        - service_account_key
        - recursive
      title: GoogleDriveSourceConnectorConfig
    GoogleDriveSourceConnectorConfigInput:
      properties:
        drive_id:
          type: string
          title: Drive Id
        service_account_key:
          anyOf:
            - $ref: '#/components/schemas/SecretReference'
            - type: string
          title: Service Account Key
        extensions:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Extensions
        recursive:
          type: boolean
          title: Recursive
          default: true
      type: object
      required:
        - drive_id
        - service_account_key
      title: GoogleDriveSourceConnectorConfigInput
    JiraSourceConnectorConfig:
      properties:
        url:
          type: string
          title: Url
        username:
          type: string
          title: Username
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        cloud:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Cloud
          default: false
        projects:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Projects
        boards:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Boards
        issues:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Issues
        status_filters:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Status Filters
        download_attachments:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Download Attachments
          default: false
      type: object
      required:
        - url
        - username
      title: JiraSourceConnectorConfig
    JiraSourceConnectorConfigInput:
      properties:
        url:
          type: string
          title: Url
        username:
          type: string
          title: Username
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        token:
          anyOf:
            - type: string
            - type: 'null'
          title: Token
        cloud:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Cloud
          default: false
        projects:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Projects
        boards:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Boards
        issues:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Issues
        status_filters:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Status Filters
        download_attachments:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Download Attachments
          default: false
      type: object
      required:
        - url
        - username
      title: JiraSourceConnectorConfigInput
    KafkaCloudSourceConnectorConfig:
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
        num_messages_to_consume:
          type: integer
          title: Num Messages To Consume
      type: object
      required:
        - bootstrap_servers
        - port
        - topic
        - kafka_api_key
        - secret
        - num_messages_to_consume
      title: KafkaCloudSourceConnectorConfig
    KafkaCloudSourceConnectorConfigInput:
      properties:
        bootstrap_servers:
          type: string
          title: Bootstrap Servers
        port:
          type: integer
          minimum: 1
          title: Port
          default: 9092
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
        num_messages_to_consume:
          type: integer
          minimum: 1
          title: Num Messages To Consume
          default: 100
      type: object
      required:
        - bootstrap_servers
        - topic
        - kafka_api_key
        - secret
      title: KafkaCloudSourceConnectorConfigInput
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
    MongoDBConnectorConfigInput:
      properties:
        database:
          type: string
          title: Database
        collection:
          type: string
          title: Collection
        uri:
          type: string
          pattern: >-
            ^mongodb(?:\+srv)?:\/\/(?:([^:@/\s]+)(?::([^@/\s]*))?@)?([^/\s:,]+)(?::(\d+))?(?:,([^/\s:,]+)(?::(\d+))?)*(?:\/([^/\s?]*))?(?:\?([^/\s]*))?$
          title: Uri
      type: object
      required:
        - database
        - collection
        - uri
      title: MongoDBConnectorConfigInput
    OneDriveSourceConnectorConfig:
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
        recursive:
          type: boolean
          title: Recursive
        path:
          type: string
          title: Path
      type: object
      required:
        - client_id
        - user_pname
        - tenant
        - authority_url
        - client_cred
        - recursive
        - path
      title: OneDriveSourceConnectorConfig
    OneDriveSourceConnectorConfigInput:
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
        recursive:
          type: boolean
          title: Recursive
          default: false
        path:
          type: string
          title: Path
      type: object
      required:
        - client_id
        - user_pname
        - tenant
        - authority_url
        - client_cred
        - path
      title: OneDriveSourceConnectorConfigInput
    OutlookSourceConnectorConfig:
      properties:
        authority_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Authority Url
        tenant:
          anyOf:
            - type: string
            - type: 'null'
          title: Tenant
        client_id:
          type: string
          title: Client Id
        client_cred:
          type: string
          title: Client Cred
        outlook_folders:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Outlook Folders
        recursive:
          type: boolean
          title: Recursive
        user_email:
          type: string
          title: User Email
      type: object
      required:
        - client_id
        - client_cred
        - recursive
        - user_email
      title: OutlookSourceConnectorConfig
    OutlookSourceConnectorConfigInput:
      properties:
        authority_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Authority Url
        tenant:
          anyOf:
            - type: string
            - type: 'null'
          title: Tenant
        client_id:
          type: string
          title: Client Id
        client_cred:
          type: string
          title: Client Cred
        outlook_folders:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Outlook Folders
        recursive:
          type: boolean
          title: Recursive
          default: false
        user_email:
          type: string
          title: User Email
      type: object
      required:
        - client_id
        - client_cred
        - user_email
      title: OutlookSourceConnectorConfigInput
    PostgresSourceConnectorConfig:
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
        id_column:
          type: string
          title: Id Column
        fields:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Fields
      type: object
      required:
        - host
        - database
        - port
        - username
        - password
        - table_name
        - batch_size
        - id_column
      title: PostgresSourceConnectorConfig
    PostgresSourceConnectorConfigInput:
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
        id_column:
          type: string
          title: Id Column
          default: id
        fields:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Fields
      type: object
      required:
        - host
        - database
        - port
        - username
        - password
        - table_name
        - batch_size
      title: PostgresSourceConnectorConfigInput
    S3SourceConnectorConfig:
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
        recursive:
          type: boolean
          title: Recursive
      type: object
      required:
        - remote_url
        - anonymous
        - recursive
      title: S3SourceConnectorConfig
    S3SourceConnectorConfigInput:
      properties:
        remote_url:
          type: string
          pattern: ^s3:\/\/
          title: Remote Url
        anonymous:
          type: boolean
          title: Anonymous
          default: false
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
        recursive:
          type: boolean
          title: Recursive
          default: true
      type: object
      required:
        - remote_url
      title: S3SourceConnectorConfigInput
    SalesforceSourceConnectorConfig:
      properties:
        username:
          type: string
          title: Username
        consumer_key:
          type: string
          title: Consumer Key
        private_key:
          type: string
          title: Private Key
        categories:
          items:
            type: string
          type: array
          title: Categories
      type: object
      required:
        - username
        - consumer_key
        - private_key
        - categories
      title: SalesforceSourceConnectorConfig
    SalesforceSourceConnectorConfigInput:
      properties:
        username:
          type: string
          title: Username
        consumer_key:
          type: string
          title: Consumer Key
        private_key:
          type: string
          title: Private Key
        categories:
          items:
            type: string
          type: array
          title: Categories
      type: object
      required:
        - username
        - consumer_key
        - private_key
        - categories
      title: SalesforceSourceConnectorConfigInput
    SecretReference:
      properties:
        id:
          type: string
          title: Id
        type:
          $ref: '#/components/schemas/EncryptionType'
          default: rsa
      type: object
      required:
        - id
      title: SecretReference
    SharePointSourceConnectorConfig:
      properties:
        site:
          type: string
          title: Site
        tenant:
          type: string
          title: Tenant
        authority_url:
          type: string
          title: Authority Url
          default: https://login.microsoftonline.com
        user_pname:
          type: string
          title: User Pname
        client_id:
          type: string
          title: Client Id
        client_cred:
          type: string
          title: Client Cred
        recursive:
          type: boolean
          title: Recursive
        path:
          anyOf:
            - type: string
            - type: 'null'
          title: Path
      type: object
      required:
        - site
        - tenant
        - user_pname
        - client_id
        - client_cred
        - recursive
      title: SharePointSourceConnectorConfig
    SharePointSourceConnectorConfigInput:
      properties:
        site:
          type: string
          pattern: >-
            ^https:\/\/([a-zA-Z0-9-]+)(-admin)?\.sharepoint\.com(\/sites\/[a-zA-Z0-9-_]+)?$
          title: Site
        tenant:
          type: string
          title: Tenant
        authority_url:
          type: string
          title: Authority Url
          default: https://login.microsoftonline.com
        user_pname:
          type: string
          title: User Pname
        client_id:
          type: string
          title: Client Id
        client_cred:
          type: string
          title: Client Cred
        recursive:
          type: boolean
          title: Recursive
          default: false
        path:
          anyOf:
            - type: string
            - type: 'null'
          title: Path
      type: object
      required:
        - site
        - tenant
        - user_pname
        - client_id
        - client_cred
      title: SharePointSourceConnectorConfigInput
    SnowflakeSourceConnectorConfig:
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
        batch_size:
          type: integer
          minimum: 1
          title: Batch Size
          default: 100
        id_column:
          type: string
          title: Id Column
        fields:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Fields
      type: object
      required:
        - account
        - role
        - user
        - password
        - host
        - database
        - schema
        - table_name
        - id_column
      title: SnowflakeSourceConnectorConfig
    SnowflakeSourceConnectorConfigInput:
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
        batch_size:
          type: integer
          minimum: 1
          title: Batch Size
          default: 100
        id_column:
          type: string
          title: Id Column
        fields:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Fields
      type: object
      required:
        - account
        - role
        - user
        - password
        - host
        - database
        - schema
        - table_name
        - id_column
      title: SnowflakeSourceConnectorConfigInput
    SourceConnectorType:
      type: string
      enum:
        - azure
        - box
        - confluence
        - couchbase
        - databricks_volumes
        - dropbox
        - elasticsearch
        - gcs
        - google_drive
        - kafka-cloud
        - mongodb
        - onedrive
        - outlook
        - postgres
        - s3
        - salesforce
        - sharepoint
        - slack
        - snowflake
        - jira
        - zendesk
      title: SourceConnectorType
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
    ZendeskSourceConnectorConfig:
      properties:
        subdomain:
          type: string
          title: Subdomain
        email:
          type: string
          title: Email
        api_token:
          type: string
          title: Api Token
        item_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Item Type
          default: tickets
        batch_size:
          anyOf:
            - type: integer
            - type: 'null'
          title: Batch Size
          default: 2
      type: object
      required:
        - subdomain
        - email
        - api_token
      title: ZendeskSourceConnectorConfig
    ZendeskSourceConnectorConfigInput:
      properties:
        subdomain:
          type: string
          title: Subdomain
        email:
          type: string
          title: Email
        api_token:
          type: string
          title: Api Token
        item_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Item Type
          default: tickets
        batch_size:
          anyOf:
            - type: integer
            - type: 'null'
          title: Batch Size
          default: 2
      type: object
      required:
        - subdomain
        - email
        - api_token
      title: ZendeskSourceConnectorConfigInput

````