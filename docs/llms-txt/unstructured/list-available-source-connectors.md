# Source: https://docs.unstructured.io/api-reference/sources/list-available-source-connectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List available source connectors

> Retrieve a list of available source connectors.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/sources/
openapi: 3.1.0
info:
  title: Platform API
  version: 3.1.0
servers:
  - url: https://platform.unstructuredapp.io/
    description: Unstructured Platform API
    x-speakeasy-server-id: platform-api
security: []
paths:
  /api/v1/sources/:
    get:
      tags:
        - sources
      summary: List available source connectors
      description: Retrieve a list of available source connectors.
      operationId: list_sources
      parameters:
        - name: source_type
          in: query
          required: false
          schema:
            anyOf:
              - $ref: '#/components/schemas/SourceConnectorType'
              - type: 'null'
            title: Source Type
        - name: unstructured-api-key
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Unstructured-Api-Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SourceConnectorInformation'
                title: Response List Sources
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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
        - opensearch
        - outlook
        - postgres
        - s3
        - salesforce
        - sharepoint
        - slack
        - snowflake
        - teradata
        - jira
        - zendesk
      title: SourceConnectorType
    SourceConnectorInformation:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        type:
          anyOf:
            - $ref: '#/components/schemas/SourceConnectorType'
            - type: string
          title: Type
        config:
          anyOf:
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
            - $ref: '#/components/schemas/OpenSearchConnectorConfig'
            - $ref: '#/components/schemas/OutlookSourceConnectorConfig'
            - $ref: '#/components/schemas/PostgresSourceConnectorConfig'
            - $ref: '#/components/schemas/S3SourceConnectorConfig'
            - $ref: '#/components/schemas/SalesforceSourceConnectorConfig'
            - $ref: '#/components/schemas/SharePointSourceConnectorConfig'
            - $ref: '#/components/schemas/SnowflakeSourceConnectorConfig'
            - $ref: '#/components/schemas/TeradataSourceConnectorConfig'
            - $ref: '#/components/schemas/JiraSourceConnectorConfig'
            - $ref: '#/components/schemas/ZendeskSourceConnectorConfig'
            - additionalProperties: true
              type: object
          title: Config
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated At
      type: object
      required:
        - id
        - name
        - type
        - config
        - created_at
      title: SourceConnectorInformation
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
    OpenSearchConnectorConfig:
      properties:
        hosts:
          items:
            type: string
          type: array
          minItems: 1
          title: Hosts
          description: List of OpenSearch hosts to connect to
        index_name:
          type: string
          title: Index Name
          description: Name of the OpenSearch index to read from or write to
        username:
          anyOf:
            - type: string
            - type: 'null'
          title: Username
          description: Username for basic authentication
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
          description: Password for basic authentication
        aws_access_key_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Aws Access Key Id
          description: >-
            AWS access key ID for IAM authentication. When provided with
            aws_secret_access_key, IAM authentication is used instead of basic
            auth. Region and service type are auto-detected from the host URL.
        aws_secret_access_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Aws Secret Access Key
          description: >-
            AWS secret access key for IAM authentication. Required when
            aws_access_key_id is provided.
        aws_session_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Aws Session Token
          description: >-
            AWS session token for temporary credentials (optional). Only used
            when aws_access_key_id and aws_secret_access_key are provided.
        use_ssl:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Use Ssl
          description: Whether to use SSL for the connection
          default: true
      type: object
      required:
        - hosts
        - index_name
      title: OpenSearchConnectorConfig
      description: >-
        OpenSearch connector configuration.


        OpenSearch is a fork of Elasticsearch with similar functionality.

        Supports two authentication methods:

        1. Basic auth: username + password

        2. AWS IAM auth: aws_access_key_id + aws_secret_access_key (+ optional
        aws_session_token)


        For AWS OpenSearch Service or OpenSearch Serverless, region and service
        type

        are auto-detected from the host URL.
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
    TeradataSourceConnectorConfig:
      properties:
        host:
          type: string
          title: Host
        user:
          type: string
          title: User
        password:
          type: string
          title: Password
        database:
          anyOf:
            - type: string
            - type: 'null'
          title: Database
        dbs_port:
          type: integer
          minimum: 1
          title: Dbs Port
          default: 1025
        id_column:
          type: string
          title: Id Column
          default: id
        table_name:
          type: string
          title: Table Name
        batch_size:
          type: integer
          minimum: 1
          title: Batch Size
          default: 100
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
        - user
        - password
        - table_name
      title: TeradataSourceConnectorConfig
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
    EncryptionType:
      type: string
      enum:
        - rsa
        - rsa_aes
      title: EncryptionType

````