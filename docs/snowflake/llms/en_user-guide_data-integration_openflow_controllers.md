# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/controllers/index.md

# All controller services (alphabetical)

This topic provides a list of all openflow controller services in alphabetical order.
The list includes:

> * Type of controller service (Snowflake or not)
> * The name of each controller service
> * A summary of each controller service

## A

|  | Controller | Description |
| --- | --- | --- |
|  | [ADLSCredentialsControllerService](adlscredentialscontrollerservice.md) | Defines credentials for ADLS processors. |
|  | [ADLSCredentialsControllerServiceLookup](adlscredentialscontrollerservicelookup.md) | Provides an ADLSCredentialsService that can be used to dynamically select another ADLSCredentialsService. |
|  | [AmazonGlueEncodedSchemaReferenceReader](amazonglueencodedschemareferencereader.md) | Reads Schema Identifier according to AWS Glue Schema encoding as a header consisting of a two byte markers and a 16 byte UUID |
|  | [AmazonGlueSchemaRegistry](amazonglueschemaregistry.md) | Provides a Schema Registry that interacts with the AWS Glue Schema Registry so that those Schemas that are stored in the Glue Schema Registry can be used in NiFi. |
|  | [AmazonMSKConnectionService](amazonmskconnectionservice.md) | Provides and manages connections to AWS MSK Kafka Brokers for producer or consumer operations. |
|  | [AmazonMSKConnectionService](amazonmskconnectionservice.md) | Provides and manages connections to AWS MSK Kafka Brokers for producer or consumer operations. |
|  | [ApicurioSchemaRegistry](apicurioschemaregistry.md) | Provides a Schema Registry that interacts with the Apicurio Schema Registry so that those Schemas that are stored in the Apicurio Schema Registry can be used in NiFi. |
|  | [AvroReader](avroreader.md) | Parses Avro data and returns each Avro record as an separate Record object. |
|  | [AvroRecordSetWriter](avrorecordsetwriter.md) | Writes the contents of a RecordSet in Binary Avro format. |
|  | [AvroSchemaRegistry](avroschemaregistry.md) | Provides a service for registering and accessing schemas. |
|  | [AWSCredentialsProviderControllerService](awscredentialsprovidercontrollerservice.md) | Defines credentials for Amazon Web Services processors. |
|  | [AzureBlobStorageFileResourceService](azureblobstoragefileresourceservice.md) | Provides an Azure Blob Storage file resource for other components. |
|  | [AzureCosmosDBClientService](azurecosmosdbclientservice.md) | Provides a controller service that configures a connection to Cosmos DB (Core SQL API) and provides access to that connection to other Cosmos DB-related components. |
|  | [AzureDataLakeStorageFileResourceService](azuredatalakestoragefileresourceservice.md) | Provides an Azure Data Lake Storage (ADLS) file resource for other components. |
|  | [AzureEventHubRecordSink](azureeventhubrecordsink.md) | Format and send Records to Azure Event Hubs |
|  | [AzureStorageCredentialsControllerService_v12](azurestoragecredentialscontrollerservice_v12.md) | Provides credentials for Azure Storage processors using Azure Storage client library v12. |
|  | [AzureStorageCredentialsControllerServiceLookup_v12](azurestoragecredentialscontrollerservicelookup_v12.md) | Provides an AzureStorageCredentialsService_v12 that can be used to dynamically select another AzureStorageCredentialsService_v12. |

## C

|  | Controller | Description |
| --- | --- | --- |
|  | [CEFReader](cefreader.md) | Parses CEF (Common Event Format) events, returning each row as a record. |
|  | [ConfluentEncodedSchemaReferenceReader](confluentencodedschemareferencereader.md) | Reads Schema Identifier according to Confluent encoding as a header consisting of a byte marker and an integer represented as four bytes |
|  | [ConfluentEncodedSchemaReferenceWriter](confluentencodedschemareferencewriter.md) | Writes Schema Identifier according to Confluent encoding as a header consisting of a byte marker and an integer represented as four bytes |
|  | [ConfluentProtobufMessageNameResolver](confluentprotobufmessagenameresolver.md) | Resolves Protobuf message names from Confluent Schema Registry wire format by decoding message indexes and looking up the fully qualified name in the schema definition For Confluent wire format reference see: <https://docs>. |
|  | [ConfluentSchemaRegistry](confluentschemaregistry.md) | Provides a Schema Registry that interacts with the Confluent Schema Registry so that those Schemas that are stored in the Confluent Schema Registry can be used in NiFi. |
|  | [CSVReader](csvreader.md) | Parses CSV-formatted data, returning each row in the CSV file as a separate record. |
|  | [CSVRecordLookupService](csvrecordlookupservice.md) | A reloadable CSV file-based lookup service. |
|  | [CSVRecordSetWriter](csvrecordsetwriter.md) | Writes the contents of a RecordSet as CSV data. |

## D

|  | Controller | Description |
| --- | --- | --- |
|  | [DatabaseLookup](databaselookup.md) | A Lookup Service that allows for enrichment with a database using a user-specified SQL statement. |
|  | [DatabaseRecordLookupService](databaserecordlookupservice.md) | A relational-database-based lookup service. |
|  | [DatabaseRecordSink](databaserecordsink.md) | Provides a service to write records using a configured database connection. |
|  | [DBCPConnectionPool](dbcpconnectionpool.md) | Provides Database Connection Pooling Service. |
|  | [DBCPConnectionPoolLookup](dbcpconnectionpoollookup.md) | Provides a DBCPService that can be used to dynamically select another DBCPService. |
|  | [DeveloperBoxClientService](developerboxclientservice.md) | Provides Box client objects through which Box API calls can be used. |
|  | [DistributedMapCacheLookupService](distributedmapcachelookupservice.md) | Allows to choose a distributed map cache client to retrieve the value associated to a key. |

## E

|  | Controller | Description |
| --- | --- | --- |
|  | [ElasticSearchClientServiceImpl](elasticsearchclientserviceimpl.md) | A controller service for accessing an Elasticsearch client, using the Elasticsearch (low-level) REST Client. |
|  | [ElasticSearchLookupService](elasticsearchlookupservice.md) | Lookup a record from Elasticsearch Server associated with the specified document ID. |
|  | [ElasticSearchStringLookupService](elasticsearchstringlookupservice.md) | Lookup a string value from Elasticsearch Server associated with the specified document ID. |
|  | [EmailRecordSink](emailrecordsink.md) | Provides a RecordSinkService that can be used to send records in email using the specified writer for formatting. |
|  | [EmbeddedHazelcastCacheManager](embeddedhazelcastcachemanager.md) | A service that runs embedded Hazelcast and provides cache instances backed by that. |
|  | [ExcelReader](excelreader.md) | Parses a Microsoft Excel document returning each row in each sheet as a separate record. |
|  | [ExternalHazelcastCacheManager](externalhazelcastcachemanager.md) | A service that provides cache instances backed by Hazelcast running outside of NiFi. |

## F

|  | Controller | Description |
| --- | --- | --- |
|  | [FreeFormTextRecordSetWriter](freeformtextrecordsetwriter.md) | Writes the contents of a RecordSet as free-form text. |

## G

|  | Controller | Description |
| --- | --- | --- |
|  | [GCPCredentialsControllerService](gcpcredentialscontrollerservice.md) | Defines credentials for Google Cloud Platform processors. |
|  | [GCSFileResourceService](gcsfileresourceservice.md) | Provides a Google Compute Storage (GCS) file resource for other components. |
|  | [GrokReader](grokreader.md) | Provides a mechanism for reading unstructured text data, such as log files, and structuring the data so that it can be processed. |

## H

|  | Controller | Description |
| --- | --- | --- |
|  | [HazelcastMapCacheClient](hazelcastmapcacheclient.md) | An implementation of DistributedMapCacheClient that uses Hazelcast as the backing cache. |
|  | [HikariCPConnectionPool](hikaricpconnectionpool.md) | Provides Database Connection Pooling Service based on HikariCP. |
|  | [HttpRecordSink](httprecordsink.md) | Format and send Records to a configured uri using HTTP post. |

## I

|  | Controller | Description |
| --- | --- | --- |
|  | [IPLookupService](iplookupservice.md) | A lookup service that provides several types of enrichment information for IP addresses. |

## J

|  | Controller | Description |
| --- | --- | --- |
|  | [JettyWebSocketClient](jettywebsocketclient.md) | Implementation of WebSocketClientService. |
|  | [JettyWebSocketServer](jettywebsocketserver.md) | Implementation of WebSocketServerService. |
|  | [JMSConnectionFactoryProvider](jmsconnectionfactoryprovider.md) | Provides a generic service to create vendor specific javax. |
|  | [JndiJmsConnectionFactoryProvider](jndijmsconnectionfactoryprovider.md) | Provides a service to lookup an existing JMS ConnectionFactory using the Java Naming and Directory Interface (JNDI). |
|  | [JsonConfigBasedBoxClientService](jsonconfigbasedboxclientservice.md) | Provides Box client objects through which Box API calls can be used. |
|  | [JsonPathReader](jsonpathreader.md) | Parses JSON records and evaluates user-defined JSON Path ‘s against each JSON object. |
|  | [JsonRecordSetWriter](jsonrecordsetwriter.md) | Writes the results of a RecordSet as either a JSON Array or one JSON object per line. |
|  | [JsonTableColumnFilter](jsontablecolumnfilter.md) | Provides a table column filter based on a JSON configuration. |
|  | [JsonTreeReader](jsontreereader.md) | Parses JSON into individual Record objects. |
|  | [JWTBearerOAuth2AccessTokenProvider](jwtbeareroauth2accesstokenprovider.md) | Provides OAuth 2. |

## K

|  | Controller | Description |
| --- | --- | --- |
|  | [Kafka3ConnectionService](kafka3connectionservice.md) | Provides and manages connections to Kafka Brokers for producer or consumer operations. |
|  | [Kafka3ConnectionService](kafka3connectionservice.md) | Provides and manages connections to Kafka Brokers for producer or consumer operations. |

## L

|  | Controller | Description |
| --- | --- | --- |
|  | [LoggingRecordSink](loggingrecordsink.md) | Provides a RecordSinkService that can be used to log records to the application log (nifi-app. |

## M

|  | Controller | Description |
| --- | --- | --- |
|  | [MapCacheClientService](mapcacheclientservice.md) | Provides the ability to communicate with a MapCacheServer. |
|  | [MapCacheServer](mapcacheserver.md) | Provides a map (key/value) cache that can be accessed over a socket. |
|  | [MicrosoftClientCertificateOAuth2TokenProvider](microsoftclientcertificateoauth2tokenprovider.md) | Provides OAuth2 access tokens for the Microsoft Graph API using client_credentials with a client certificate. |
|  | [MicrosoftGraphAuthenticationProvider](microsoftgraphauthenticationprovider.md) | Provides authentication for the Microsoft Graph API, which can be used for interacting with Microsoft 365 services. |
|  | [MongoDBControllerService](mongodbcontrollerservice.md) | Provides a controller service that configures a connection to MongoDB and provides access to that connection to other Mongo-related components. |
|  | [MongoDBLookupService](mongodblookupservice.md) | Provides a lookup service based around MongoDB. |

## P

|  | Controller | Description |
| --- | --- | --- |
|  | [ParquetIcebergWriter](parqueticebergwriter.md) | Provides record serialization for Apache Iceberg using Apache Parquet formatting |
|  | [PEMEncodedSSLContextProvider](pemencodedsslcontextprovider.md) | SSLContext Provider configurable using PEM Private Key and Certificate files. |
|  | [PolarisIcebergCatalog](polarisicebergcatalog.md) | Provides Apache Iceberg integration with Apache Polaris Catalog access over REST HTTP |
|  | [PropertiesFileLookupService](propertiesfilelookupservice.md) | A reloadable properties file-based lookup service |
|  | [ProtobufReader](protobufreader.md) | Parses a Protocol Buffers message from binary format. |

## R

|  | Controller | Description |
| --- | --- | --- |
|  | [ReaderLookup](readerlookup.md) | Provides a RecordReaderFactory that can be used to dynamically select another RecordReaderFactory. |
|  | [RecordSetWriterLookup](recordsetwriterlookup.md) | Provides a RecordSetWriterFactory that can be used to dynamically select another RecordSetWriterFactory. |
|  | [RecordSinkServiceLookup](recordsinkservicelookup.md) | Provides a RecordSinkService that can be used to dynamically select another RecordSinkService. |
|  | [RedisConnectionPoolService](redisconnectionpoolservice.md) | A service that provides connections to Redis. |
|  | [RedisDistributedMapCacheClientService](redisdistributedmapcacheclientservice.md) | An implementation of DistributedMapCacheClient that uses Redis as the backing cache. |
|  | [RemoveFieldRecordReader](removefieldrecordreader.md) | A wrapper for a RecordReaderFactory that supports filtering out specified fields from NiFi Records. |
|  | [RestLookupService](restlookupservice.md) | Use a REST service to look up values. |

## S

|  | Controller | Description |
| --- | --- | --- |
|  | [S3FileResourceService](s3fileresourceservice.md) | Provides an Amazon Web Services (AWS) S3 file resource for other components. |
|  | [SalesforceDataCloudOAuthTokenProvider](salesforcedatacloudoauthtokenprovider.md) | Retrieves an OAuth2 access token from Salesforce using the configured OAuth2 Access Token Provider and exchanges the token for a Data Cloud API token. |
|  | [ScriptedLookupService](scriptedlookupservice.md) | Allows the user to provide a scripted LookupService instance in order to enrich records from an incoming flow file. |
|  | [ScriptedReader](scriptedreader.md) | Allows the user to provide a scripted RecordReaderFactory instance in order to read/parse/generate records from an incoming flow file. |
|  | [ScriptedRecordSetWriter](scriptedrecordsetwriter.md) | Allows the user to provide a scripted RecordSetWriterFactory instance in order to write records to an outgoing flow file. |
|  | [ScriptedRecordSink](scriptedrecordsink.md) | Allows the user to provide a scripted RecordSinkService instance in order to transmit records to the desired target. |
|  | [SetCacheClientService](setcacheclientservice.md) | Provides the ability to communicate with a SetCacheServer. |
|  | [SetCacheServer](setcacheserver.md) | Provides a set (collection of unique values) cache that can be accessed over a socket. |
|  | [SimpleCsvFileLookupService](simplecsvfilelookupservice.md) | A reloadable CSV file-based lookup service. |
|  | [SimpleDatabaseLookupService](simpledatabaselookupservice.md) | A relational-database-based lookup service. |
|  | [SimpleKeyValueLookupService](simplekeyvaluelookupservice.md) | Allows users to add key/value pairs as User-defined Properties. |
|  | [SimpleRedisDistributedMapCacheClientService](simpleredisdistributedmapcacheclientservice.md) | An implementation of DistributedMapCacheClient that uses Redis as the backing cache. |
|  | [SimpleScriptedLookupService](simplescriptedlookupservice.md) | Allows the user to provide a scripted LookupService instance in order to enrich records from an incoming flow file. |
|  | [SlackRecordSink](slackrecordsink.md) | Format and send Records to a configured Channel using the Slack Post Message API. |
|  | [SmbjClientProviderService](smbjclientproviderservice.md) | Provides access to SMB Sessions with shared authentication credentials. |
|  | [SnowflakeConnectionService](snowflakeconnectionservice.md) | Provides pooled database connections to Snowflake services |
|  | [SnowflakeDatabaseDialectService](snowflakedatabasedialectservice.md) | Database Dialect Service supporting Snowflake. |
|  | [SnowflakeSignJWTService](snowflakesignjwtservice.md) | Provides OAuth2 access token using a JWT signed with a secret stored in Snowflake. |
|  | [SnowflakeTableSchemaRegistry](snowflaketableschemaregistry.md) | Uses Snowflake tables as the source of schema — utilises Snowpipe Streaming REST API. |
|  | [StandardAnthropicLLMService](standardanthropicllmservice.md) | A Controller Service that provides integration with Anthropic’s Claude AI models through their Messages API. |
|  | [StandardAtlassianRequestRateManager](standardatlassianrequestratemanager.md) | Provides rate limiting coordination for Atlassian API calls across processors to prevent cascading rate limit issues. |
|  | [StandardAzureCredentialsControllerService](standardazurecredentialscontrollerservice.md) | Provide credentials to use with an Azure client. |
|  | [StandardConfluenceClientService](standardconfluenceclientservice.md) | Provides connection service to Confluence APIs |
|  | [StandardDatabricksWorkspaceClientService](standarddatabricksworkspaceclientservice.md) | Databricks client. |
|  | [StandardDropboxCredentialService](standarddropboxcredentialservice.md) | Defines credentials for Dropbox processors. |
|  | [StandardFileResourceService](standardfileresourceservice.md) | Provides a file resource for other components. |
|  | [StandardHashiCorpVaultClientService](standardhashicorpvaultclientservice.md) | A controller service for interacting with HashiCorp Vault. |
|  | [StandardHttpContextMap](standardhttpcontextmap.md) | Provides the ability to store and retrieve HTTP requests and responses external to a Processor, so that multiple Processors can interact with the same HTTP request. |
|  | [StandardHubSpotClientService](standardhubspotclientservice.md) | HubSpot Controller Service to integrate with HubSpot HTTP api. |
|  | [StandardJsonSchemaRegistry](standardjsonschemaregistry.md) | Provides a service for registering and accessing JSON schemas. |
|  | [StandardKustoIngestService](standardkustoingestservice.md) | Sends batches of flowfile content or stream flowfile content to an Azure ADX cluster. |
|  | [StandardKustoQueryService](standardkustoqueryservice.md) | Standard implementation of Kusto Query Service for Azure Data Explorer |
|  | [StandardMilvusConnectionService](standardmilvusconnectionservice.md) | Provides connection service to a Milvus instance |
|  | [StandardOauth2AccessTokenProvider](standardoauth2accesstokenprovider.md) | Provides OAuth 2. |
|  | [StandardOCRService](standardocrservice.md) | Provides integration to Openflow OCR Service |
|  | [StandardOpenAILLMService](standardopenaillmservice.md) | A Controller Service that provides integration with OpenAI’s Chat Completion API. |
|  | [StandardPGPPrivateKeyService](standardpgpprivatekeyservice.md) | PGP Private Key Service provides Private Keys loaded from files or properties |
|  | [StandardPGPPublicKeyService](standardpgppublickeyservice.md) | PGP Public Key Service providing Public Keys loaded from files |
|  | [StandardPrivateKeyService](standardprivatekeyservice.md) | Private Key Service provides access to a Private Key loaded from configured sources |
|  | [StandardProtobufReader](standardprotobufreader.md) | Parses Protocol Buffers messages from binary format into NiFi Records. |
|  | [StandardProxyConfigurationService](standardproxyconfigurationservice.md) | Provides a set of configurations for different NiFi components to use a proxy server. |
|  | [StandardRestrictedSSLContextService](standardrestrictedsslcontextservice.md) | Restricted implementation of the SSLContextService. |
|  | [StandardS3EncryptionService](standards3encryptionservice.md) | Adds configurable encryption to S3 Put and S3 Fetch operations. |
|  | [StandardSalesforceBulkJobsStateService](standardsalesforcebulkjobsstateservice.md) | Stores Salesforce Bulk Jobs state per object type at cluster scope |
|  | [StandardSalesforceClientService](standardsalesforceclientservice.md) | Provides connection service to Salesforce APIs |
|  | [StandardSalesforceDataCloudClientService](standardsalesforcedatacloudclientservice.md) | Provides connection service to Salesforce Data Cloud APIs |
|  | [StandardSlackRateLimiterService](standardslackratelimiterservice.md) | Provides rate limiting coordination for Slack API calls across processors to prevent cascading rate limit issues |
|  | [StandardSSLContextService](standardsslcontextservice.md) | Standard implementation of the SSLContextService. |
|  | [StandardTableStateService](standardtablestateservice.md) | A controller Service that provides and manages table state. |
|  | [StandardVectaraClientService](standardvectaraclientservice.md) | Vectara Controller Service to integrate with Vectara HTTP Api. |
|  | [StandardWebClientServiceProvider](standardwebclientserviceprovider.md) | Web Client Service Provider with support for configuring standard HTTP connection properties |
|  | [StateManagedCdcSchemaRegistry](statemanagedcdcschemaregistry.md) | Uses the in-built NiFi State Management to store the hashes of table schemas. |
|  | [Syslog5424Reader](syslog5424reader.md) | Provides a mechanism for reading RFC 5424 compliant Syslog data, such as log files, and structuring the data so that it can be processed. |
|  | [SyslogReader](syslogreader.md) | Attempts to parses the contents of a Syslog message in accordance to RFC5424 and RFC3164. |

## U

|  | Controller | Description |
| --- | --- | --- |
|  | [UDPEventRecordSink](udpeventrecordsink.md) | Format and send Records as UDP Datagram Packets to a configurable destination |

## V

|  | Controller | Description |
| --- | --- | --- |
|  | [VolatileSchemaCache](volatileschemacache.md) | Provides a Schema Cache that evicts elements based on a Least-Recently-Used algorithm. |

## W

|  | Controller | Description |
| --- | --- | --- |
|  | [WindowsEventLogReader](windowseventlogreader.md) | Reads Windows Event Log data as XML content having been generated by ConsumeWindowsEventLog, ParseEvtx, etc. |

## X

|  | Controller | Description |
| --- | --- | --- |
|  | [XMLFileLookupService](xmlfilelookupservice.md) | A reloadable XML file-based lookup service. |
|  | [XMLReader](xmlreader.md) | Reads XML content and creates Record objects. |
|  | [XMLRecordSetWriter](xmlrecordsetwriter.md) | Writes a RecordSet to XML. |

## Y

|  | Controller | Description |
| --- | --- | --- |
|  | [YamlTreeReader](yamltreereader.md) | Parses YAML into individual Record objects. |
