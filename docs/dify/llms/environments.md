# Source: https://docs.dify.ai/en/self-host/configuration/environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Environments

<Info>
  This document may be outdated. Please refer to the latest configuration files:

  * [docker-compose.yaml](https://github.com/langgenius/dify/blob/5f8d20b5b2bb51f19547467167b18d9c0f6ffbb8/docker/docker-compose.yaml)

  * [.env.example](https://github.com/langgenius/dify/blob/5f8d20b5b2bb51f19547467167b18d9c0f6ffbb8/docker/.env.example)
</Info>

## Common Variables

### CONSOLE\_API\_URL

The backend URL for the console API. This is used to construct the authorization callback. If left empty, it defaults to the same domain as the application. Example: `https://api.console.dify.ai`

### CONSOLE\_WEB\_URL

The front-end URL of the console web interface. This is used to construct front-end addresses and for CORS configuration. If left empty, it defaults to the same domain as the application. Example: `https://console.dify.ai`

### SERVICE\_API\_URL

The Service API URL, used to display Service API Base URL in the front-end. If left empty, it defaults to the same domain as the application. Example: `https://api.dify.ai`

### TRIGGER\_URL

The base URL prefix used for the webhook callback URLs in both webhook triggers and plugin triggers.

Ensure it points to a public domain or IP address accessible to external systems.

### APP\_API\_URL

The WebApp API backend URL, used to specify the backend URL for the front-end API. If left empty, it defaults to the same domain as the application. Example: `https://app.dify.ai`

### APP\_WEB\_URL

The WebApp URL, used to display File preview or download Url to the front-end or as Multi-model inputs; If left empty, it defaults to the same domain as the application. Example: `https://udify.app/`

### FILES\_URL

The prefix for file preview or download URLs, used to display these URLs in the front-end and provide them as input for multi-modal models. To prevent forgery, image preview URLs are signed and expire after 5 minutes.

***

## Server

### MODE

Startup mode: This is only available when launched using docker. It is not applicable when running from source code.

* api: Start API Server.
* worker: Start asynchronous queue worker.

### DEBUG

Debug mode: Disabled by default. It's recommended to enable this setting during local development to prevent issues caused by monkey patching.

### FLASK\_DEBUG

Flask debug mode: When enabled, it outputs trace information in the API responses, facilitating easier debugging.

### SECRET\_KEY

A secret key used for securely signing session cookies and encrypting sensitive information in the database.

This variable must be set before the first launch.

Run `openssl rand -base64 42` to generate a strong key for it.

### DEPLOY\_ENV

Deployment environment:

* PRODUCTION (default): Production environment.
* TESTING: Testing environment. There will be a distinct color label on the front-end page, indicating that this environment is a testing environment.

### LOG\_LEVEL

The log output level. Default is INFO. For production environments, it's recommended to set this to ERROR.

### MIGRATION\_ENABLED

When set to true, database migrations are automatically executed on container startup. This is only available when launched using docker and does not apply when running from source code.

For source code launches, you need to manually run `flask db upgrade` in the api directory.

### CHECK\_UPDATE\_URL

Controls the version checking policy. If set to false, the system will not call `https://updates.dify.ai` to check for updates.

Currently, the version check interface based on CloudFlare Worker is not directly accessible in China. Setting this variable to an empty value will disable this API call.

### TEXT\_GENERATION\_TIMEOUT\_MS

Default value: 60000 (milliseconds). Specifies the timeout for text generation and workflow processes. This setting prevents system-wide service disruptions caused by individual processes exceeding their allocated time.

### OPENAI\_API\_BASE

Used to change the OpenAI base address, default is [https://api.openai.com/v1](https://api.openai.com/v1).

When OpenAI cannot be accessed in China, replace it with a domestic mirror address, or when a local model provides OpenAI compatible API, it can be replaced.

### Container Startup Related Configuration

Only effective when starting with docker image or docker-compose.

* DIFY\_BIND\_ADDRESS: API service binding address, default: 0.0.0.0, i.e., all addresses can be accessed.

* DIFY\_PORT: API service binding port number, default to 5001.

* SERVER\_WORKER\_AMOUNT: The number of API server workers, i.e., the number of gevent workers. Formula: `number of cpu cores x 2 + 1`

  Reference: [https://docs.gunicorn.org/en/stable/design.html#how-many-workers](https://docs.gunicorn.org/en/stable/design.html#how-many-workers)

* SERVER\_WORKER\_CLASS: Defaults to gevent. If using windows, it can be switched to sync or solo.

* GUNICORN\_TIMEOUT: Request handling timeout. Default is 200. Recommended value is 360 to support longer SSE (Server-Sent Events) connection times.

* CELERY\_WORKER\_CLASS: Similar to `SERVER_WORKER_CLASS`. Default is gevent. If using windows, it can be switched to sync or solo.

* CELERY\_WORKER\_AMOUNT: The number of Celery workers. The default is 1, and can be set as needed.

* COMPOSE\_PROFILES: Selectively start service groups. The default value is `${VECTOR_STORE:-weaviate},${DB_TYPE:-postgresql}`, which is automatically derived from `VECTOR_STORE` and `DB_TYPE`.

### Database Configuration

The database uses PostgreSQL. Please use the public schema.

* DB\_TYPE: Database type.

  Available values include：

  * `postgresql`(default)
  * `mysql` (MySQL-compatible databases like TiDB can also use this value)
  * `oceanbase`
  * `seekdb`

* DB\_USERNAME: username

* DB\_PASSWORD: password

* DB\_HOST: database host

* DB\_PORT: database port number, default is 5432

* DB\_DATABASE: database name

* SQLALCHEMY\_POOL\_SIZE: The size of the database connection pool. The default is 30 connections, which can be appropriately increased.

* SQLALCHEMY\_POOL\_RECYCLE: Database connection pool recycling time, the default is 3600 seconds.

* SQLALCHEMY\_ECHO: Whether to print SQL, default is false.

### Redis Configuration

This Redis configuration is used for caching and for pub/sub during conversation.

* REDIS\_HOST: Redis host
* REDIS\_PORT: Redis port, default is 6379
* REDIS\_DB: Redis Database, default is 0. Please use a different Database from Session Redis and Celery Broker.
* REDIS\_USERNAME: Redis username, default is empty
* REDIS\_PASSWORD: Redis password, default is empty. It is strongly recommended to set a password.
* REDIS\_USE\_SSL: Whether to use SSL protocol for connection, default is false
* REDIS\_USE\_SENTINEL: Use Redis Sentinel to connect to Redis servers
* REDIS\_SENTINELS: Sentinel nodes, format: `<sentinel1_ip>:<sentinel1_port>,<sentinel2_ip>:<sentinel2_port>,<sentinel3_ip>:<sentinel3_port>`
* REDIS\_SENTINEL\_SERVICE\_NAME: Sentinel service name, same as Master Name
* REDIS\_SENTINEL\_USERNAME: Username for Sentinel
* REDIS\_SENTINEL\_PASSWORD: Password for Sentinel
* REDIS\_SENTINEL\_SOCKET\_TIMEOUT: Sentinel timeout, default value: 0.1, unit: seconds

### Celery Configuration

* CELERY\_BROKER\_URL

  Format as follows(direct connection mode):

  ```
  redis://<redis_username>:<redis_password>@<redis_host>:<redis_port>/<redis_database>
  ```

  Example: `redis://:difyai123456@redis:6379/1`

  Sentinel mode:

  ```
  sentinel://<sentinel_username>:<sentinel_password>@<sentinel_host>:<sentinel_port>/<redis_database>
  ```

  Example: `sentinel://localhost:26379/1;sentinel://localhost:26380/1;sentinel://localhost:26381/1`

* BROKER\_USE\_SSL: If set to true, use SSL protocol for connection, default is false

* CELERY\_USE\_SENTINEL: If set to true, Sentinel mode will be enabled, default is false

* CELERY\_SENTINEL\_MASTER\_NAME: The service name of Sentinel, i.e., Master Name

* CELERY\_SENTINEL\_SOCKET\_TIMEOUT: Timeout for connecting to Sentinel, default value: 0.1, unit: seconds

### CORS Configuration

Used to set the front-end cross-domain access policy.

* CONSOLE\_CORS\_ALLOW\_ORIGINS\
  Console CORS cross-domain policy, default is `*`, that is, all domains can access.

* WEB\_API\_CORS\_ALLOW\_ORIGINS\
  WebAPP CORS cross-domain policy, default is `*`, that is, all domains can access.

* COOKIE\_DOMAIN\
  When the frontend and backend run on different subdomains, set `COOKIE_DOMAIN` to the site's top-level domain (e.g., `example.com`).\
  The frontend and backend must be under the same top-level domain to share authentication cookies.

* NEXT\_PUBLIC\_COOKIE\_DOMAIN\
  When the frontend and backend run on different subdomains, set `NEXT_PUBLIC_COOKIE_DOMAIN` to `1`.\
  The frontend and backend must be under the same top-level domain to share authentication cookies.

### File Storage Configuration

Used to store uploaded data set files, team/tenant encryption keys, and other files.

* STORAGE\_TYPE

  Type of storage facility

  * local (default): Local file storage, if this option is selected, the following `STORAGE_LOCAL_PATH` configuration needs to be set.

  * s3: S3 object storage, if this option is selected, the following S3\_ prefixed configurations need to be set.

  * azure-blob: Azure Blob object storage, if this option is selected, the following AZURE\_BLOB\_ prefixed configurations need to be set.

  * aliyun-oss: Alibaba Cloud OSS object storage, if this option is selected, the following ALIYUN\_OSS\_ prefixed configurations need to be set.

  * huawei-obs: Huawei OBS object storage, if this option is selected, the following HUAWEI\_OBS\_ prefixed configurations need to be set.

  * volcengine-tos: Volcengine TOS object storage, if this option is selected, the following VOLCENGINE\_TOS\_ prefixed configurations need to be set.

  * tencent-cos: Tencent Cloud COS object storage, if this option is selected, the following TENCENT\_COS\_ prefixed configurations need to be set.

* STORAGE\_LOCAL\_PATH

  Default is storage, that is, it is stored in the storage directory of the current directory.

  If you are deploying with docker or docker-compose, be sure to mount the `/app/api/storage` directory in both containers to the same local directory, otherwise, you may encounter file not found errors.

* S3\_ENDPOINT: S3 endpoint address

* S3\_BUCKET\_NAME: S3 bucket name

* S3\_ACCESS\_KEY: S3 Access Key

* S3\_SECRET\_KEY: S3 Secret Key

* S3\_REGION: S3 region information, such as: us-east-1

* AZURE\_BLOB\_ACCOUNT\_NAME: your-account-name eg, 'difyai'

* AZURE\_BLOB\_ACCOUNT\_KEY: your-account-key eg, 'difyai'

* AZURE\_BLOB\_CONTAINER\_NAME: your-container-name eg, 'difyai-container'

* AZURE\_BLOB\_ACCOUNT\_URL: '[https://your\_account\_name.blob.core.windows.net](https://your_account_name.blob.core.windows.net)'

* ALIYUN\_OSS\_BUCKET\_NAME: your-bucket-name eg, 'difyai'

* ALIYUN\_OSS\_ACCESS\_KEY: your-access-key eg, 'difyai'

* ALIYUN\_OSS\_SECRET\_KEY: your-secret-key eg, 'difyai'

* ALIYUN\_OSS\_ENDPOINT: [https://oss-ap-southeast-1-internal.aliyuncs.com](https://oss-ap-southeast-1-internal.aliyuncs.com) # reference: [https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints)

* ALIYUN\_OSS\_REGION: ap-southeast-1 # reference: [https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints)

* ALIYUN\_OSS\_AUTH\_VERSION: v4

* ALIYUN\_OSS\_PATH: your-path # Don't start with '/'. OSS doesn't support leading slash in object names. reference: [https://www.alibabacloud.com/help/en/oss/support/0016-00000005](https://www.alibabacloud.com/help/en/oss/support/0016-00000005)

* HUAWEI\_OBS\_BUCKET\_NAME: your-bucket-name eg, 'difyai'

* HUAWEI\_OBS\_SECRET\_KEY: your-secret-key eg, 'difyai'

* HUAWEI\_OBS\_ACCESS\_KEY: your-access-key eg, 'difyai'

* HUAWEI\_OBS\_SERVER: your-server-url # reference: [https://support.huaweicloud.com/sdk-python-devg-obs/obs\_22\_0500.html](https://support.huaweicloud.com/sdk-python-devg-obs/obs_22_0500.html)

* VOLCENGINE\_TOS\_BUCKET\_NAME: your-bucket-name eg, 'difyai'

* VOLCENGINE\_TOS\_SECRET\_KEY: your-secret-key eg, 'difyai'

* VOLCENGINE\_TOS\_ACCESS\_KEY: your-access-key eg, 'difyai'

* VOLCENGINE\_TOS\_REGION: your-region eg, 'cn-guangzhou' # reference: [https://www.volcengine.com/docs/6349/107356](https://www.volcengine.com/docs/6349/107356)

* VOLCENGINE\_TOS\_ENDPOINT: your-endpoint eg, 'tos-cn-guangzhou.volces.com' # reference: [https://www.volcengine.com/docs/6349/107356](https://www.volcengine.com/docs/6349/107356)

* TENCENT\_COS\_BUCKET\_NAME: your-bucket-name eg, 'difyai'

* TENCENT\_COS\_SECRET\_KEY: your-secret-key eg, 'difyai'

* TENCENT\_COS\_SECRET\_ID: your-secret-id eg, 'difyai'

* TENCENT\_COS\_REGION: your-region eg, 'ap-guangzhou' # reference: [https://cloud.tencent.com/document/product/436/6224](https://cloud.tencent.com/document/product/436/6224)

* TENCENT\_COS\_SCHEME: specify http/https protocol to access COS

### Vector Database Configuration

* VECTOR\_STORE\
  Available values include:
  * `weaviate`
  * `oceanbase`
  * `seekdb`
  * `qdrant`
  * `milvus`
  * `myscale`
  * `relyt`
  * `pgvector`
  * `pgvecto-rs`
  * `chroma`
  * `opensearch`
  * `oracle`
  * `tencent`
  * `elasticsearch`
  * `elasticsearch-ja`
  * `analyticdb`
  * `couchbase`
  * `vikingdb`
  * `opengauss`
  * `tablestore`
  * `vastbase`
  * `tidb`
  * `baidu`
  * `lindorm`
  * `huawei_cloud`
  * `upstash`
  * `matrixone`
  * `clickzetta`
  * `alibabacloud_mysql`
  * `iris`

#### Weaviate Configuration

* WEAVIATE\_ENDPOINT

  Weaviate endpoint address, such as: `http://weaviate:8080`.

* WEAVIATE\_API\_KEY

  The api-key credential used to connect to Weaviate.

* WEAVIATE\_BATCH\_SIZE

  The number of index Objects created in batches in Weaviate, default is 100.

  Refer to this document: [https://weaviate.io/developers/weaviate/manage-data/import#how-to-set-batch-parameters](https://weaviate.io/developers/weaviate/manage-data/import#how-to-set-batch-parameters)

* WEAVIATE\_GRPC\_ENABLED

  Whether to use the gRPC method to interact with Weaviate, performance will greatly increase when enabled, may not be usable locally, default is true.

#### OceanBase/seekdb Configuration

* OCEANBASE\_VECTOR\_HOST

  The hostname or IP address of OceanBase or seekdb vector database.

* OCEANBASE\_VECTOR\_PORT

  The port of OceanBase or seekdb vector database.

* OCEANBASE\_VECTOR\_USER

  The username of OceanBase or seekdb vector database.

* OCEANBASE\_VECTOR\_PASSWORD

  The password of OceanBase or seekdb vector database user.

* OCEANBASE\_VECTOR\_DATABASE

  The database name of OceanBase or seekdb vector database.

* OCEANBASE\_CLUSTER\_NAME

  The cluster name of OceanBase or seekdb vector database, only available for Docker deployment.

* OCEANBASE\_MEMORY\_LIMIT

  The memory limit of OceanBase vector database, only available for Docker deployment.

* SEEKDB\_MEMORY\_LIMIT

  The memory limit of seekdb vector database, only available for Docker deployment.

#### Qdrant Configuration

* QDRANT\_URL

  Qdrant endpoint address, such as: `https://your-qdrant-cluster-url.qdrant.tech/`

* QDRANT\_API\_KEY

  The api-key credential used to connect to Qdrant.

#### Milvus Configuration

* MILVUS\_URI

  Milvus uri configuration. e.g. `http://host.docker.internal:19530`. For [Zilliz Cloud](https://docs.zilliz.com/docs/free-trials), adjust the uri and token to the Public Endpoint and API Key.

* MILVUS\_TOKEN

  Milvus token configuration, default is empty.

* MILVUS\_USER

  Milvus user configuration, default is empty.

* MILVUS\_PASSWORD

  Milvus password configuration, default is empty.

#### MyScale Configuration

* MYSCALE\_HOST

  MyScale host configuration.

* MYSCALE\_PORT

  MyScale port configuration.

* MYSCALE\_USER

  MyScale user configuration, default is `default`.

* MYSCALE\_PASSWORD

  MyScale password configuration, default is empty.

* MYSCALE\_DATABASE

  MyScale database configuration, default is `default`.

* MYSCALE\_FTS\_PARAMS

  MyScale text-search params, check [MyScale docs](https://myscale.com/docs/en/text-search/#understanding-fts-index-parameters) for multi-language support, default is empty.

#### Couchbase Configuration

* COUCHBASE\_CONNECTION\_STRING

  The connection string for the Couchbase cluster.

* COUCHBASE\_USER

  The username for the database user.

* COUCHBASE\_PASSWORD

  The password for the database user.

* COUCHBASE\_BUCKET\_NAME

  The name of the bucket to use.

* COUCHBASE\_SCOPE\_NAME

  The name of the scope to use.

#### AnalyticDB Configuration

* ANALYTICDB\_KEY\_ID

  The access key ID used for Aliyun OpenAPI authentication. Read the  [Analyticdb documentation](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/support/create-an-accesskey-pair) to create your AccessKey.

* ANALYTICDB\_KEY\_SECRET

  The access key secret used for Aliyun OpenAPI authentication.

* ANALYTICDB\_INSTANCE\_ID

  The unique identifier for your AnalyticDB instance, such as : `gp-xxxxxx`. Read the [Analyticdb documentation](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/getting-started/create-an-instance-1) to create your instance.

* ANALYTICDB\_REGION\_ID

  The region identifier where the AnalyticDB instance is located, such as: `cn-hangzhou`.

* ANALYTICDB\_ACCOUNT

  The account name used to connect to the AnalyticDB instance. Read the [Analyticdb documentation](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/getting-started/createa-a-privileged-account) to create an account.

* ANALYTICDB\_PASSWORD

  The password for the account used to connect to the AnalyticDB instance.

* ANALYTICDB\_NAMESPACE

  The namespace(schema) within the AnalyticDB instance that you wish to interact with, such as `dify`. If this namespace does not exist, it will be created automatically.

* ANALYTICDB\_NAMESPACE\_PASSWORD

  The password for the namespace(schema). If the namespace does not exist, it will be created with this password.

#### TiDB Configuration

* TIDB\_VECTOR\_HOST

  The hostname or IP address of the TiDB vector database. Default is `tidb`.

* TIDB\_VECTOR\_PORT

  The port of the TiDB vector database. Default is `4000`.

* TIDB\_VECTOR\_USER

  The username of the TiDB vector database.

* TIDB\_VECTOR\_PASSWORD

  The password of the TiDB vector database.

* TIDB\_VECTOR\_DATABASE

  The database name of the TiDB vector database. Default is `dify`.

#### MatrixOne Configuration

* MATRIXONE\_HOST

  The host of Matrixone database, default value is matrixone.

* MATRIXONE\_PORT

  The port of Matrixone database, default value is 6001.

* MATRIXONE\_USER

  The user of Matrixone database, default value is dump.

* MATRIXONE\_PASSWORD

  The password of Matrixone database, default value is 111.

* MATRIXONE\_DATABASE

  The database of Matrixone database, default value is dify.

#### Tencent Cloud VectorDB Configuration

* TENCENT\_VECTOR\_DB\_URL

  The access address for Tencent Cloud VectorDB can be obtained from [the console](https://console.cloud.tencent.com/vdb).

* TENCENT\_VECTOR\_DB\_API\_KEY

  The API key (password) for the VectorDB server is used for identity authentication. [Key Management](https://cloud.tencent.com/document/product/1709/95108).

* TENCENT\_VECTOR\_DB\_USERNAME

  The vector database account, default 'root'. [Account Management](https://cloud.tencent.com/document/product/1709/115833).

* TENCENT\_VECTOR\_DB\_TIMEOUT

  Set the default request timeout duration.

* TENCENT\_VECTOR\_DB\_DATABASE

  Set up a Database for storing data. [Create Database](https://cloud.tencent.com/document/product/1709/95822).

* TENCENT\_VECTOR\_DB\_SHARD

  Specify the number of shards.

* TENCENT\_VECTOR\_DB\_REPLICAS

  Specify the number of replicas.

* TENCENT\_VECTOR\_DB\_ENABLE\_HYBRID\_SEARCH

  Specify whether to enable HybridSearch. [Sparse Vector Documentation](https://cloud.tencent.com/document/product/1709/110110).

#### Lindorm Configuration

* LINDORM\_URL

  The URL of LINDORM search engine，you can get it from [the console](https://lindorm.console.aliyun.com/)

* LINDORM\_USERNAME

  The username of lindorm search engine

* LINDORM\_PASSWORD

  The password of lindorm search engine

#### OpenGauss Configuration

* OPENGAUSS\_HOST

  The hostname or IP address of the openGauss vector database.

* OPENGAUSS\_PORT

  The port of the openGauss vector database.

* OPENGAUSS\_USER

  The username of the openGauss vector database.

* OPENGAUSS\_PASSWORD

  The password of the openGauss vector database.

* OPENGAUSS\_DATABASE

  The database name of the openGauss vector database.

* OPENGAUSS\_MIN\_CONNECTION

  Min connection of the openGauss vector database.

* OPENGAUSS\_MAX\_CONNECTION

  Max connection of the openGauss vector database.

* OPENGAUSS\_ENABLE\_PQ

  Enabling PQ Acceleration for the openGauss vector database.

#### TableStore Configuration

* TABLESTORE\_ENDPOINT

  The endpoint address of the TableStore server (e.g. '[https://instance-name.cn-hangzhou.ots.aliyuncs.com](https://instance-name.cn-hangzhou.ots.aliyuncs.com)')

* TABLESTORE\_INSTANCE\_NAME

  The instance name to access TableStore server (e.g. 'instance-name')

* TABLESTORE\_ACCESS\_KEY\_ID

  The accessKey id for the instance name

* TABLESTORE\_ACCESS\_KEY\_SECRET

  The accessKey secret for the instance name

### Knowledge Configuration

* UPLOAD\_FILE\_SIZE\_LIMIT\
  The maximum allowed size (in megabytes) for an uploaded file. Default 15.

* UPLOAD\_FILE\_BATCH\_LIMIT\
  The maximum number of files that can be uploaded in a single batch. Default 5.

* SINGLE\_CHUNK\_ATTACHMENT\_LIMIT\
  The maximum number of files that can be attached to a single chunk. Default 10.

* IMAGE\_FILE\_BATCH\_LIMIT\
  The maximum number of image attachments that can be uploaded in a single batch. Default 10.

* ATTACHMENT\_IMAGE\_FILE\_SIZE\_LIMIT\
  The maximum allowed size (in megabytes) for an image attachment. Default 2.

* ATTACHMENT\_IMAGE\_DOWNLOAD\_TIMEOUT\
  The timeout (in seconds) for downloading an image attachment. Default 60.

* ETL\_TYPE\
  Available values include:

  * `dify`: Dify's proprietary file extraction scheme
  * `Unstructured`: Unstructured.io file extraction scheme

* UNSTRUCTURED\_API\_URL\
  Unstructured API path, needs to be configured when ETL\_TYPE is Unstructured.\
  For example: `http://unstructured:8000/general/v0/general`

* TOP\_K\_MAX\_VALUE\
  The maximum top-k value of RAG, default 10.

### Multi-modal Configuration

* MULTIMODAL\_SEND\_IMAGE\_FORMAT

  The format of the image sent when the multi-modal model is input, the default is `base64`, optional `url`. The delay of the call in `url` mode will be lower than that in `base64` mode. It is generally recommended to use the more compatible `base64` mode. If configured as `url`, you need to configure `FILES_URL` as an externally accessible address so that the multi-modal model can access the image.

* UPLOAD\_IMAGE\_FILE\_SIZE\_LIMIT: Upload image file size limit, default 10M.

### Sentry Configuration

Used for application monitoring and error log tracking.

* SENTRY\_DSN: Sentry DSN address, default is empty, when empty, all monitoring information is not reported to Sentry.
* SENTRY\_TRACES\_SAMPLE\_RATE: The reporting ratio of Sentry events, if it is 0.01, it is 1%.
* SENTRY\_PROFILES\_SAMPLE\_RATE: The reporting ratio of Sentry profiles, if it is 0.01, it is 1%.

### Notion Integration Configuration

Notion integration configuration variables can be obtained by applying for Notion integration: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)

* NOTION\_INTEGRATION\_TYPE: Configure as "public" or "internal". Since Notion's OAuth redirect URL only supports HTTPS, if deploying locally, please use Notion's internal integration.
* NOTION\_CLIENT\_SECRET: Notion OAuth client secret (used for public integration type)
* NOTION\_CLIENT\_ID: OAuth client ID (used for public integration type)
* NOTION\_INTERNAL\_SECRET: Notion internal integration secret. If the value of `NOTION_INTEGRATION_TYPE` is "internal", you need to configure this variable.

### Mail related configuration

* MAIL\_TYPE

  * resend
    * MAIL\_DEFAULT\_SEND\_FROM: The sender's email name, such as: no-reply [no-reply@dify.ai](mailto:no-reply@dify.ai), not mandatory.
    * RESEND\_API\_KEY: API-Key for the Resend email provider, can be obtained from API-Key.

  * smtp
    * SMTP\_SERVER: SMTP server address
    * SMTP\_PORT: SMTP server port number
    * SMTP\_USERNAME: SMTP username
    * SMTP\_PASSWORD: SMTP password
    * SMTP\_USE\_TLS: Whether to use TLS, default is false
    * MAIL\_DEFAULT\_SEND\_FROM: The sender's email name, such as: no-reply [no-reply@dify.ai](mailto:no-reply@dify.ai), not mandatory.

  * sendgrid
    * SENDGRID\_API\_KEY: API key for the SendGrid email provider.
    * MAIL\_DEFAULT\_SEND\_FROM: The sender's email address, e.g., [your\_email@sendgrid.com](mailto:your_email@sendgrid.com). This field is required for SendGrid authentication.

For more details about the SendGrid email provider, please refer to the [SendGrid documentation](https://sendgrid.com/docs/for-developers/sending-email/).

### ModelProvider & Tool Position Configuration

Used to specify the model providers and tools that can be used in the app. These settings allow you to customize which tools and model providers are available, as well as their order and inclusion/exclusion in the app's interface.

For a list of available [tools](https://github.com/langgenius/dify/blob/main/api/core/tools/provider/_position.yaml) and [model providers](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/model_providers/_position.yaml), please refer to the provided links.

* POSITION\_TOOL\_PINS

  Pin specific tools to the top of the list, ensuring they appear first in the interface. (Use comma-separated values with **no spaces** between items.)

  Example: `POSITION_TOOL_PINS=bing,google`

* POSITION\_TOOL\_INCLUDES

  Specify the tools to be included in the app. Only the tools listed here will be available for use. If not set, all tools will be included unless specified in POSITION\_TOOL\_EXCLUDES. (Use comma-separated values with **no spaces** between items.)

  Example: `POSITION_TOOL_INCLUDES=bing,google`

* POSITION\_TOOL\_EXCLUDES

  Exclude specific tools from being displayed or used in the app. Tools listed here will be omitted from the available options, except for pinned tools. (Use comma-separated values with **no spaces** between items.)

  Example: `POSITION_TOOL_EXCLUDES=yahoo,wolframalpha`

* POSITION\_PROVIDER\_PINS

  Pin specific model providers to the top of the list, ensuring they appear first in the interface. (Use comma-separated values with **no spaces** between items.)

  Example: `POSITION_PROVIDER_PINS=openai,openllm`

* POSITION\_PROVIDER\_INCLUDES

  Specify the model providers to be included in the app. Only the providers listed here will be available for use. If not set, all providers will be included unless specified in POSITION\_PROVIDER\_EXCLUDES. (Use comma-separated values with **no spaces** between items.)

  Example: `POSITION_PROVIDER_INCLUDES=cohere,upstage`

* POSITION\_PROVIDER\_EXCLUDES

  Exclude specific model providers from being displayed or used in the app. Providers listed here will be omitted from the available options, except for pinned providers. (Use comma-separated values with **no spaces** between items.)

  Example: `POSITION_PROVIDER_EXCLUDES=openrouter,ollama`

### Scheduled Tasks Configuration

Dify uses Celery Beat to execute various background scheduled tasks for system maintenance and data cleanup. The following environment variables configure scheduled task settings:

* CELERY\_BEAT\_SCHEDULER\_TIME

  Celery Beat scheduling time interval (in days) that controls the execution frequency of certain scheduled tasks. Default is 1 day.

* ENABLE\_CLEAN\_EMBEDDING\_CACHE\_TASK

  Whether to enable the embedding cache cleanup task. Default is false. When enabled, it cleans expired embedding caches at 2:00 AM daily to reduce storage usage.

* ENABLE\_CLEAN\_UNUSED\_DATASETS\_TASK

  Whether to enable the unused datasets cleanup task. Default is false. When enabled, it cleans long-unused datasets at 3:00 AM daily to free up storage space.

* ENABLE\_CLEAN\_MESSAGES

  Whether to enable the message cleanup task. Default is false. When enabled, it cleans expired conversation message records at 4:00 AM daily.

* ENABLE\_MAIL\_CLEAN\_DOCUMENT\_NOTIFY\_TASK

  Whether to enable the mail document cleanup notification task. Default is false. When enabled, it sends document cleanup notification emails at 10:00 AM every Monday.

* ENABLE\_DATASETS\_QUEUE\_MONITOR

  Whether to enable the datasets queue monitoring task. Default is false. When enabled, it monitors the dataset processing queue status and sends alerts when the queue backlog exceeds the threshold.

* QUEUE\_MONITOR\_INTERVAL

  Dataset queue monitoring interval (in minutes). Default is 30 minutes. Only effective when the queue monitoring task is enabled.

* ENABLE\_CHECK\_UPGRADABLE\_PLUGIN\_TASK

  Whether to enable the check upgradable plugin task. Default is true. When enabled, it checks for upgradable plugin versions every 15 minutes. Requires MARKETPLACE\_ENABLED to be enabled.

* MARKETPLACE\_ENABLED

  Whether to enable the marketplace functionality. Default is true. When disabled, plugin-related features including plugin upgrade checks will be unavailable.

* ENABLE\_CREATE\_TIDB\_SERVERLESS\_TASK

  Whether to enable the create TiDB Serverless task. Default is false. Used for TiDB cloud service integration, executes every hour.

* ENABLE\_UPDATE\_TIDB\_SERVERLESS\_STATUS\_TASK

  Whether to enable the update TiDB Serverless status task. Default is false. Used to update TiDB cloud service status, executes every 10 minutes.

* WORKFLOW\_LOG\_CLEANUP\_ENABLED

  Whether to enable automatic workflow log cleanup task. Default is false. When enabled, it cleans workflow execution logs that exceed the retention period at 2:00 AM daily.

* WORKFLOW\_LOG\_RETENTION\_DAYS

  Workflow log retention days. Default is 30 days. Only effective when the workflow log cleanup task is enabled.

* WORKFLOW\_LOG\_CLEANUP\_BATCH\_SIZE

  Workflow log cleanup batch size. Default is 100. Number of log entries processed per cleanup operation, can be adjusted based on system performance.

### Others

* INVITE\_EXPIRY\_HOURS: Member invitation link valid time (hours), Default: 72.
* HTTP\_REQUEST\_NODE\_MAX\_TEXT\_SIZE: The maximum text size of the HTTP request node in the workflow, default 1MB。
* HTTP\_REQUEST\_NODE\_MAX\_BINARY\_SIZE: The maximum binary size of HTTP request nodes in the workflow, default 10MB。

***

## Web Frontend

### SENTRY\_DSN

Sentry DSN address, default is empty, when empty, all monitoring information is not reported to Sentry.

## Deprecated

### CONSOLE\_URL

> ⚠️ Modified in 0.3.8, will be deprecated in 0.4.9, replaced by: `CONSOLE_API_URL` and `CONSOLE_WEB_URL`.

Console URL, used to concatenate the authorization callback, console front-end address, and CORS configuration use. If empty, it is the same domain. Example: `https://console.dify.ai`.

### API\_URL

> ⚠️ Modified in 0.3.8, will be deprecated in 0.4.9, replaced by `SERVICE_API_URL`.

API URL, used to display Service API Base URL to the front-end. If empty, it is the same domain. Example: `https://api.dify.ai`

### APP\_URL

> ⚠️ Modified in 0.3.8, will be deprecated in 0.4.9, replaced by `APP_API_URL` and `APP_WEB_URL`.

WebApp Url, used to display WebAPP API Base Url to the front-end. If empty, it is the same domain. Example: `https://udify.app/`

### Session Configuration

> ⚠️ This configuration is no longer valid since v0.3.24.

Only used by the API service for interface identity verification.

* SESSION\_TYPE: Session component type

  * redis (default): If you choose this, you need to set the environment variables starting with SESSION\_REDIS\_ below.
  * sqlalchemy: If you choose this, the current database connection will be used and the sessions table will be used to read and write session records.

* SESSION\_REDIS\_HOST: Redis host

* SESSION\_REDIS\_PORT: Redis port, default is 6379

* SESSION\_REDIS\_DB: Redis Database, default is 0. Please use a different Database from Redis and Celery Broker.

* SESSION\_REDIS\_USERNAME: Redis username, default is empty

* SESSION\_REDIS\_PASSWORD: Redis password, default is empty. It is strongly recommended to set a password.

* SESSION\_REDIS\_USE\_SSL: Whether to use SSL protocol for connection, default is false

### Cookie Policy Configuration

> ⚠️ This configuration is no longer valid since v0.3.24.

Used to set the browser policy for session cookies used for identity verification.

* COOKIE\_HTTPONLY: Cookie HttpOnly configuration, default is true.
* COOKIE\_SAMESITE: Cookie SameSite configuration, default is Lax.
* COOKIE\_SECURE: Cookie Secure configuration, default is false.

## Chunk Length Configuration

### INDEXING\_MAX\_SEGMENTATION\_TOKENS\_LENGTH

Configuration for document chunk length. It is used to control the size of text segments when processing long documents. Default: 500. Maximum: 4000.

**Larger Chunks**

* Retain more context within each chunk, ideal for tasks requiring a broader understanding of the text.
* Reduce the total number of chunks, lowering processing time and storage overhead.

**Smaller Chunks**

* Provide finer granularity, improving accuracy for tasks like extraction or summarization.
* Reduce the risk of exceeding model token limits, making it safer for models with stricter constraints.

**Configuration Recommendations**

* Choose larger chunks for context-heavy tasks like sentiment analysis or document summarization.
* Choose smaller chunks for fine-grained tasks such as keyword extraction or paragraph-level processing.


Built with [Mintlify](https://mintlify.com).