# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/index.md

# All processors (alphabetical)

This topic provides a list of all Snowflake openflow processors in alphabetical order.
The list includes:

> * The name of each processor
> * A summary of each processor

## A

|  | Processor | Description |
| --- | --- | --- |
|  | [AbortQueryJob](abortqueryjob.md) | Aborts a Query Job in Salesforce using the Bulk API 2. |
|  | [AttributesToCSV](attributestocsv.md) | Generates a CSV representation of the input FlowFile Attributes. |
|  | [AttributesToJSON](attributestojson.md) | Generates a JSON representation of the input FlowFile Attributes. |

## C

|  | Processor | Description |
| --- | --- | --- |
|  | [CalculateRecordStats](calculaterecordstats.md) | Counts the number of Records in a record set, optionally counting the number of elements per category, where the categories are defined by user-defined properties. |
|  | [CaptureChangeMySQL](capturechangemysql.md) | Reads CDC events from a MySQL database. |
|  | [CaptureChangePostgreSQL](capturechangepostgresql.md) | Reads CDC events from a PostgreSQL database. |
|  | [CaptureChangeSqlServer](capturechangesqlserver.md) | Reads CDC events from a SQL Server database. |
|  | [CaptureGoogleDriveChanges](capturegoogledrivechanges.md) | Captures changes to a Shared Google Drive and emits a FlowFile for each change that occurs. |
|  | [CaptureMicrosoft365GroupsChanges](capturemicrosoft365groupschanges.md) | Captures Microsoft365 groups changes and emits a FlowFile for each change that occurs. |
|  | [CaptureSharepointChanges](capturesharepointchanges.md) | Captures changes from a Sharepoint Document Library and emits a FlowFile for each change that occurs. |
|  | [CheckMetaAdsReportReadiness](checkmetaadsreportreadiness.md) | Processor checking if the Meta Ads report is ready for download. |
|  | [ChunkRecordText](chunkrecordtext.md) | Chunks text with options for recursively splitting by delimiters and max character length. |
|  | [ChunkText](chunktext.md) | Chunks text with options for recursively splitting by delimiters and max character length. |
|  | [CompressContent](compresscontent.md) | Compresses or decompresses the contents of FlowFiles using a user-specified compression algorithm and updates the mime. |
|  | [ConnectWebSocket](connectwebsocket.md) | Acts as a WebSocket client endpoint to interact with a remote WebSocket server. |
|  | [ConsumeAMQP](consumeamqp.md) | Consumes AMQP Messages from an AMQP Broker using the AMQP 0. |
|  | [ConsumeAzureEventHub](consumeazureeventhub.md) | Receives messages from Microsoft Azure Event Hubs with checkpointing to ensure consistent event processing. |
|  | [ConsumeBoxEnterpriseEvents](consumeboxenterpriseevents.md) | Consumes Enterprise Events from Box admin_logs_streaming Stream Type. |
|  | [ConsumeBoxEvents](consumeboxevents.md) | Consumes all events from Box. |
|  | [ConsumeElasticsearch](consumeelasticsearch.md) | A processor that repeatedly runs a paginated query against a field using a Range query to consume new Documents from an Elasticsearch index/query. |
|  | [ConsumeGCPubSub](consumegcpubsub.md) | Consumes messages from the configured Google Cloud PubSub subscription. |
|  | [ConsumeIMAP](consumeimap.md) | Consumes messages from Email Server using IMAP protocol. |
|  | [ConsumeJMS](consumejms.md) | Consumes JMS Message of type BytesMessage, TextMessage, ObjectMessage, MapMessage or StreamMessage transforming its content to a FlowFile and transitioning it to ‘success’ relationship. |
|  | [ConsumeKafka](consumekafka.md) | Consumes messages from Apache Kafka Consumer API. |
|  | [ConsumeKafka](consumekafka.md) | Consumes messages from Apache Kafka Consumer API. |
|  | [ConsumeKinesisStream](consumekinesisstream.md) | Reads data from the specified AWS Kinesis stream and outputs a FlowFile for every processed Record (raw) or a FlowFile for a batch of processed records if a Record Reader and Record Writer are configured. |
|  | [ConsumeMQTT](consumemqtt.md) | Subscribes to a topic and receives messages from an MQTT broker |
|  | [ConsumePOP3](consumepop3.md) | Consumes messages from Email Server using POP3 protocol. |
|  | [ConsumeSlack](consumeslack.md) | Retrieves messages from one or more configured Slack channels. |
|  | [ConsumeSlackConversation](consumeslackconversation.md) | Retrieves messages from Slack conversations available to the App. |
|  | [ConsumeSlackHistory](consumeslackhistory.md) | Fetches historical messages from all Slack channels available to the App. |
|  | [ConsumeSnowflakeStream](consumesnowflakestream.md) | Fetches data from a Snowflake stream and writes it to a FlowFile. |
|  | [ConsumeTwitter](consumetwitter.md) | Streams tweets from Twitter’s streaming API v2. |
|  | [ControlRate](controlrate.md) | Controls the rate at which data is transferred to follow-on processors. |
|  | [ConvertCharacterSet](convertcharacterset.md) | Converts a FlowFile’s content from one character set to another |
|  | [ConvertRecord](convertrecord.md) | Converts records from one data format to another using configured Record Reader and Record Write Controller Services. |
|  | [ConvertToJournalSchema](converttojournalschema.md) | Converts the incoming database schema into the appropriate schema for a Snowflake CDC Journal table. |
|  | [CopyAzureBlobStorage_v12](copyazureblobstorage_v12.md) | Copies a blob in Azure Blob Storage from one account/container to another. |
|  | [CopyS3Object](copys3object.md) | Copies a file from one bucket and key to another in AWS S3 |
|  | [CountText](counttext.md) | Counts various metrics on incoming text. |
|  | [CreateAmazonAdsReport](createamazonadsreport.md) | Processor which creates report configuration for Amazon Ads connector. |
|  | [CreateAzureOpenAiEmbeddings](createazureopenaiembeddings.md) | Uses Azure OpenAI to create embeddings for text. |
|  | [CreateBoxFileMetadataInstance](createboxfilemetadatainstance.md) | Creates a metadata instance for a Box file using a specified template with values from the flowFile content. |
|  | [CreateBoxMetadataTemplate](createboxmetadatatemplate.md) | Creates a Box metadata template using field specifications from the flowFile content. |
|  | [CreateCohereEmbeddings](createcohereembeddings.md) | Uses Cohere to create embeddings for text. |
|  | [CreateMetaAdsReport](createmetaadsreport.md) | Processor which creates report configuration for Meta Ads connector. |
|  | [CreateOpenAiEmbeddings](createopenaiembeddings.md) | Uses OpenAI to create embeddings for text. |
|  | [CreateSnowflakeEmbeddings](createsnowflakeembeddings.md) | Create vector embeddings using Snowflake Cortex Large Language Model functions |
|  | [CreateVertexAIEmbeddings](createvertexaiembeddings.md) | Uses VertexAI to create embeddings for text. |
|  | [CryptographicHashContent](cryptographichashcontent.md) | Calculates a cryptographic hash value for the flowfile content using the given algorithm and writes it to an output attribute. |

## D

|  | Processor | Description |
| --- | --- | --- |
|  | [DebugFlow](debugflow.md) | The DebugFlow processor aids testing and debugging the FlowFile framework by allowing various responses to be explicitly triggered in response to the receipt of a FlowFile or a timer event without a FlowFile if using timer or cron based scheduling. |
|  | [DecryptContentAge](decryptcontentage.md) | Decrypt content using the age-encryption. |
|  | [DecryptContentPGP](decryptcontentpgp.md) | Decrypt contents of OpenPGP messages. |
|  | [DeduplicateRecord](deduplicaterecord.md) | This processor de-duplicates individual records within a record set. |
|  | [DeleteAzureBlobStorage_v12](deleteazureblobstorage_v12.md) | Deletes the specified blob from Azure Blob Storage. |
|  | [DeleteAzureDataLakeStorage](deleteazuredatalakestorage.md) | Deletes the provided file from Azure Data Lake Storage |
|  | [DeleteBoxFileMetadataInstance](deleteboxfilemetadatainstance.md) | Deletes a metadata instance from a Box file using the specified template key |
|  | [DeleteByQueryElasticsearch](deletebyqueryelasticsearch.md) | Delete from an Elasticsearch index using a query. |
|  | [DeleteDBFSResource](deletedbfsresource.md) | Delete a DBFS files and directories. |
|  | [DeleteDynamoDB](deletedynamodb.md) | Deletes a document from DynamoDB based on hash and range key. |
|  | [DeleteFile](deletefile.md) | Deletes a file from the filesystem. |
|  | [DeleteGCSObject](deletegcsobject.md) | Deletes objects from a Google Cloud Bucket. |
|  | [DeleteGridFS](deletegridfs.md) | Deletes a file from GridFS using a file name or a query. |
|  | [DeleteMilvus](deletemilvus.md) | Deletes vectors from Milvus database from a collection by ID. |
|  | [DeleteMongo](deletemongo.md) | Executes a delete query against a MongoDB collection. |
|  | [DeletePinecone](deletepinecone.md) | Deletes vectors from a Pinecone index. |
|  | [DeleteQueryJob](deletequeryjob.md) | Deletes a Query Job in Salesforce using the Bulk API 2. |
|  | [DeleteS3Object](deletes3object.md) | Deletes a file from an Amazon S3 Bucket. |
|  | [DeleteSFTP](deletesftp.md) | Deletes a file residing on an SFTP server. |
|  | [DeleteSQS](deletesqs.md) | Deletes a message from an Amazon Simple Queuing Service Queue |
|  | [DeleteUnityCatalogResource](deleteunitycatalogresource.md) | Delete a Unity Catalog file or directory. |
|  | [DescribeDataShare](describedatashare.md) | Describe the specified data share metadata in Salesforce Data Cloud. |
|  | [DescribeSFDCObject](describesfdcobject.md) | Describe the specified object metadata in Salesforce. |
|  | [DetectDuplicate](detectduplicate.md) | Caches a value, computed from FlowFile attributes, for each incoming FlowFile and determines if the cached value has already been seen. |
|  | [DistributeLoad](distributeload.md) | Distributes FlowFiles to downstream processors based on a Distribution Strategy. |
|  | [DuplicateFlowFile](duplicateflowfile.md) | Intended for load testing, this processor will create the configured number of copies of each incoming FlowFile. |

## E

|  | Processor | Description |
| --- | --- | --- |
|  | [EncodeContent](encodecontent.md) | Encode or decode the contents of a FlowFile using Base64, Base32, or hex encoding schemes |
|  | [EncryptContentAge](encryptcontentage.md) | Encrypt content using the age-encryption. |
|  | [EncryptContentPGP](encryptcontentpgp.md) | Encrypt contents using OpenPGP. |
|  | [EnforceOrder](enforceorder.md) | Enforces expected ordering of FlowFiles that belong to the same data group within a single node. |
|  | [EnrichAttributes](enrichattributes.md) | Looks up a value using the configured Lookup Service and adds the results to the FlowFile as one or more attributes. |
|  | [EnrichCdcStream](enrichcdcstream.md) | Enriches incoming FlowFiles that come from CaptureChangePostgreSQL, etc. |
|  | [EvaluateJsonPath](evaluatejsonpath.md) | Evaluates one or more JsonPath expressions against the content of a FlowFile. |
|  | [EvaluateRagAnswerCorrectness](evaluateraganswercorrectness.md) | Evaluates the correctness of generated answers in a Retrieval-Augmented Generation (RAG) context by computing metrics such as F1 score, cosine similarity, and answer correctness. |
|  | [EvaluateRagFaithfulness](evaluateragfaithfulness.md) | Evaluates the faithfulness of generated answers in a Retrieval-Augmented Generation (RAG) system by analyzing responses using an LLM (e. |
|  | [EvaluateRagRetrieval](evaluateragretrieval.md) | Calculates retrieval metrics (Precision@N, Recall@N, FScore@N, MAP@N, MRR) for a RAG system using an LLM as a judge. |
|  | [EvaluateXPath](evaluatexpath.md) | Evaluates one or more XPaths against the content of a FlowFile. |
|  | [EvaluateXQuery](evaluatexquery.md) | Evaluates one or more XQueries against the content of a FlowFile. |
|  | [ExecuteGroovyScript](executegroovyscript.md) | Experimental Extended Groovy script processor. |
|  | [ExecuteProcess](executeprocess.md) | Runs an operating system command specified by the user and writes the output of that command to a FlowFile. |
|  | [ExecuteScript](executescript.md) | Experimental - Executes a script given the flow file and a process session. |
|  | [ExecuteSQL](executesql.md) | Executes provided SQL select query. |
|  | [ExecuteSQLRecord](executesqlrecord.md) | Executes provided SQL select query. |
|  | [ExecuteSQLStatement](executesqlstatement.md) | Executes a SQL DDL or DML Statement against a database. |
|  | [ExecuteStreamCommand](executestreamcommand.md) | The ExecuteStreamCommand processor provides a flexible way to integrate external commands and scripts into NiFi data flows. |
|  | [ExtractAvroMetadata](extractavrometadata.md) | Extracts metadata from the header of an Avro datafile. |
|  | [ExtractEmailAttachments](extractemailattachments.md) | Extract attachments from a mime formatted email file, splitting them into individual flowfiles. |
|  | [ExtractEmailHeaders](extractemailheaders.md) | Using the flowfile content as source of data, extract header from an RFC compliant email file adding the relevant attributes to the flowfile. |
|  | [ExtractGrok](extractgrok.md) | Evaluates one or more Grok Expressions against the content of a FlowFile, adding the results as attributes or replacing the content of the FlowFile with a JSON notation of the matched content |
|  | [ExtractRecordSchema](extractrecordschema.md) | Extracts the record schema from the FlowFile using the supplied Record Reader and writes it to the ‘avro. |
|  | [ExtractSchemaColumns](extractschemacolumns.md) | Extracts the record schema columns from the FlowFile using the supplied Record Reader and writes it to the ‘schema. |
|  | [ExtractStructuredBoxFileMetadata](extractstructuredboxfilemetadata.md) | Extracts metadata from a Box file using Box AI. |
|  | [ExtractText](extracttext.md) | Evaluates one or more Regular Expressions against the content of a FlowFile. |

## F

|  | Processor | Description |
| --- | --- | --- |
|  | [FetchAzureBlobStorage_v12](fetchazureblobstorage_v12.md) | Retrieves the specified blob from Azure Blob Storage and writes its content to the content of the FlowFile. |
|  | [FetchAzureDataLakeStorage](fetchazuredatalakestorage.md) | Fetch the specified file from Azure Data Lake Storage |
|  | [FetchBoxFile](fetchboxfile.md) | Fetches files from a Box Folder. |
|  | [FetchBoxFileInfo](fetchboxfileinfo.md) | Fetches metadata for files from Box and adds it to the FlowFile’s attributes. |
|  | [FetchBoxFileMetadataInstance](fetchboxfilemetadatainstance.md) | Retrieves specific metadata instance associated with a Box file using template key and scope. |
|  | [FetchBoxFileRepresentation](fetchboxfilerepresentation.md) | Fetches a Box file representation using a representation hint and writes it to the FlowFile content. |
|  | [FetchDatabaseMetadata](fetchdatabasemetadata.md) | Fetches complete database metadata for all tables and outputs them to a FlowFile. |
|  | [FetchDistributedMapCache](fetchdistributedmapcache.md) | Computes cache key(s) from FlowFile attributes, for each incoming FlowFile, and fetches the value(s) from the Distributed Map Cache associated with each key. |
|  | [FetchDropbox](fetchdropbox.md) | Fetches files from Dropbox. |
|  | [FetchFile](fetchfile.md) | Reads the contents of a file from disk and streams it into the contents of an incoming FlowFile. |
|  | [FetchFTP](fetchftp.md) | Fetches the content of a file from a remote FTP server and overwrites the contents of an incoming FlowFile with the content of the remote file. |
|  | [FetchGCSObject](fetchgcsobject.md) | Fetches a file from a Google Cloud Bucket. |
|  | [FetchGoogleDrive](fetchgoogledrive.md) | Fetches files from a Google Drive Folder. |
|  | [FetchGoogleDriveFileComments](fetchgoogledrivefilecomments.md) | Fetches comments and their replies for a Google Drive file. |
|  | [FetchGoogleDriveMetadata](fetchgoogledrivemetadata.md) | Fetches Google Drive file metadata. |
|  | [FetchGridFS](fetchgridfs.md) | Retrieves one or more files from a GridFS bucket by file name or by a user-defined query. |
|  | [FetchJiraFields](fetchjirafields.md) | Retrieves comprehensive metadata for all fields available in the Jira Cloud instance using the REST API v3 /field endpoint. |
|  | [FetchJiraIssues](fetchjiraissues.md) | Fetches issues from Jira Cloud using REST API v3 with configurable search options. |
|  | [FetchMicrosoftDataverseTable](fetchmicrosoftdataversetable.md) | Fetch records from Microsoft Dataverse Tables |
|  | [FetchS3Object](fetchs3object.md) | Retrieves the contents of an S3 Object and writes it to the content of a FlowFile |
|  | [FetchSFTP](fetchsftp.md) | Fetches the content of a file from a remote SFTP server and overwrites the contents of an incoming FlowFile with the content of the remote file. |
|  | [FetchSharepointFile](fetchsharepointfile.md) | Fetches the contents of a file from a Sharepoint Drive, optionally downloading a PDF or HTML version of the file when applicable. |
|  | [FetchSharepointMetadata](fetchsharepointmetadata.md) | For each drive item retrieves its metadata and permissions and writes them as FlowFile attributes. |
|  | [FetchSlackConversationInfo](fetchslackconversationinfo.md) | Fetches Slack conversation info and member emails |
|  | [FetchSlackFile](fetchslackfile.md) | Downloads a file shared on Slack. |
|  | [FetchSlackMessage](fetchslackmessage.md) | Fetches data about a single Slack message |
|  | [FetchSmb](fetchsmb.md) | Fetches files from a SMB Share. |
|  | [FetchSnowflakeTableProperties](fetchsnowflaketableproperties.md) | Reads properties from a table and stores them as flow file attributes. |
|  | [FetchSourceTableSchema](fetchsourcetableschema.md) | Fetches the table schema (i. |
|  | [FetchTableSnapshot](fetchtablesnapshot.md) | Fetches a snapshot of a table from a database. |
|  | [FilterAttribute](filterattribute.md) | Filters the attributes of a FlowFile by retaining specified attributes and removing the rest or by removing specified attributes and retaining the rest. |
|  | [FindConfluencePages](findconfluencepages.md) | Processor for finding Confluence pages using space name and page name. |
|  | [FindSharepointDriveItem](findsharepointdriveitem.md) | Finds a Sharepoint Drive Item by its Drive ID and Item path. |
|  | [FlattenJson](flattenjson.md) | Provides the user with the ability to take a nested JSON document and flatten it into a simple key/value pair document. |
|  | [ForkEnrichment](forkenrichment.md) | Used in conjunction with the JoinEnrichment processor, this processor is responsible for adding the attributes that are necessary for the JoinEnrichment processor to perform its function. |
|  | [ForkRecord](forkrecord.md) | This processor allows the user to fork a record into multiple records. |

## G

|  | Processor | Description |
| --- | --- | --- |
|  | [GenerateAnswersFromContext](generateanswersfromcontext.md) | Generates synthetic answers for each question present in the incoming records using a Large Language Model (LLM). |
|  | [GenerateAnswersFromGroundTruth](generateanswersfromgroundtruth.md) | Generates synthetic answers for each question in the incoming records using an LLM. |
|  | [GenerateFlowFile](generateflowfile.md) | This processor creates FlowFiles with random data or custom content. |
|  | [GenerateJSON](generatejson.md) | Produces a batch of JSON Objects with random field values based on a configurable JSON Schema. |
|  | [GenerateRecord](generaterecord.md) | This processor creates FlowFiles with records having random value for the specified fields. |
|  | [GenerateTableFetch](generatetablefetch.md) | Generates SQL select queries that fetch “pages” of rows from a table. |
|  | [GeoEnrichIP](geoenrichip.md) | Looks up geolocation information for an IP address and adds the geo information to FlowFile attributes. |
|  | [GeoEnrichIPRecord](geoenrichiprecord.md) | Looks up geolocation information for an IP address and adds the geo information to FlowFile attributes. |
|  | [GetAmazonAdsReport](getamazonadsreport.md) | Processor downloading report from Amazon Ads if ready. |
|  | [GetAwsPollyJobStatus](getawspollyjobstatus.md) | Retrieves the current status of an AWS Polly job. |
|  | [GetAwsTextractJobStatus](getawstextractjobstatus.md) | Retrieves the current status of an AWS Textract job. |
|  | [GetAwsTranscribeJobStatus](getawstranscribejobstatus.md) | Retrieves the current status of an AWS Transcribe job. |
|  | [GetAwsTranslateJobStatus](getawstranslatejobstatus.md) | Retrieves the current status of an AWS Translate job. |
|  | [GetAzureEventHub](getazureeventhub.md) | Receives messages from Microsoft Azure Event Hubs without reliable checkpoint tracking. |
|  | [GetAzureQueueStorage_v12](getazurequeuestorage_v12.md) | Retrieves the messages from an Azure Queue Storage. |
|  | [GetBoxFileCollaborators](getboxfilecollaborators.md) | Retrieves all collaborators on a Box file and adds the collaboration information to the FlowFile’s attributes. |
|  | [GetBoxGroupMembers](getboxgroupmembers.md) | Retrieves members for a Box Group and writes their details in FlowFile attributes. |
|  | [GetConfluenceAuditRecords](getconfluenceauditrecords.md) | Processor listing Confluence audit records. |
|  | [GetConfluenceGroupUsers](getconfluencegroupusers.md) | Processor that downloads information about users belonging to a given Confluence group |
|  | [GetConfluencePageContent](getconfluencepagecontent.md) | Processor downloading Confluence pages. |
|  | [GetConfluencePageIds](getconfluencepageids.md) | Downloads changed Confluence pages since the last sync and emits each as a FlowFile with metadata. |
|  | [GetConfluencePagePermissions](getconfluencepagepermissions.md) | Processor downloading Confluence page permissions. |
|  | [GetConfluenceSpaceIds](getconfluencespaceids.md) | Processor for retrieving Confluence space ids. |
|  | [GetConfluenceSpacePermissions](getconfluencespacepermissions.md) | Processor downloading Confluence space permissions. |
|  | [GetDataShareCredentials](getdatasharecredentials.md) | Describe the specified data share metadata in Salesforce Data Cloud. |
|  | [GetDataShareTables](getdatasharetables.md) | Describe the specified data share metadata in Salesforce Data Cloud. |
|  | [GetDBFSFile](getdbfsfile.md) | Read a DBFS file. |
|  | [GetDynamoDB](getdynamodb.md) | Retrieves a document from DynamoDB based on hash and range key. |
|  | [GetElasticsearch](getelasticsearch.md) | Elasticsearch get processor that uses the official Elastic REST client libraries to fetch a single document from Elasticsearch by _id. |
|  | [GetFile](getfile.md) | Creates FlowFiles from files in a directory. |
|  | [GetFileResource](getfileresource.md) | This processor creates FlowFiles with the content of the configured File Resource. |
|  | [GetFTP](getftp.md) | Fetches files from an FTP Server and creates FlowFiles from them |
|  | [GetGcpVisionAnnotateFilesOperationStatus](getgcpvisionannotatefilesoperationstatus.md) | Retrieves the current status of an Google Vision operation. |
|  | [GetGcpVisionAnnotateImagesOperationStatus](getgcpvisionannotateimagesoperationstatus.md) | Retrieves the current status of an Google Vision operation. |
|  | [GetGoogleAdsReport](getgoogleadsreport.md) | A processor which can interact with Google Ads Reporting API. |
|  | [GetGoogleGroupMembers](getgooglegroupmembers.md) | Retrieves the members of one or more Google Groups, specified as a comma-separated list of group IDs that is given as a FlowFile attribute. |
|  | [GetGoogleSheets](getgooglesheets.md) | Processor responsible for fetching data from Google Sheets. |
|  | [GetHubSpot](gethubspot.md) | Retrieves JSON data from a private HubSpot application. |
|  | [GetHubSpotObject](gethubspotobject.md) | Get a HubSpot object and its associations by ID or unique value. |
|  | [GetHubSpotSchema](gethubspotschema.md) | Retrieves schema information for HubSpot object types including field names, types, and labels. |
|  | [GetLinkedInAdsReport](getlinkedinadsreport.md) | Processor downloading metrics from the LinkedIn Reporting APIs. |
|  | [GetMicrosoft365GroupMembers](getmicrosoft365groupmembers.md) | Retrieves Microsoft365 group members and emits a FlowFile for each change that occurs. |
|  | [GetMongo](getmongo.md) | Creates FlowFiles from documents in MongoDB loaded by a user-specified query. |
|  | [GetMongoRecord](getmongorecord.md) | A record-based version of GetMongo that uses the Record writers to write the MongoDB result set. |
|  | [GetQueryJobResult](getqueryjobresult.md) | Gets the results of a Query Job in Salesforce using the Bulk API 2. |
|  | [GetQueryJobStatus](getqueryjobstatus.md) | Gets the status of a Query Job in Salesforce using the Bulk API 2. |
|  | [GetS3ObjectMetadata](gets3objectmetadata.md) | Check for the existence of an Object in S3 and fetch its Metadata without attempting to download it. |
|  | [GetS3ObjectTags](gets3objecttags.md) | Check for the existence of an Object in S3 and fetch its Tags without attempting to download it. |
|  | [GetSFTP](getsftp.md) | Fetches files from an SFTP Server and creates FlowFiles from them |
|  | [GetSharepointSiteGroupMembers](getsharepointsitegroupmembers.md) | Retrieves all members of a SharePoint site group. |
|  | [GetShopify](getshopify.md) | Retrieves objects from a custom Shopify store. |
|  | [GetSmbFile](getsmbfile.md) | Reads file from a samba network location to FlowFiles. |
|  | [GetSplunk](getsplunk.md) | Retrieves data from Splunk Enterprise. |
|  | [GetSQS](getsqs.md) | Fetches messages from an Amazon Simple Queuing Service Queue |
|  | [GetUnityCatalogFile](getunitycatalogfile.md) | Read a Unity Catalog file up to 5 GiB. |
|  | [GetUnityCatalogFileMetadata](getunitycatalogfilemetadata.md) | Checks for Unity Catalog file metadata. |
|  | [GetWorkdayReport](getworkdayreport.md) | A processor which can interact with a configurable Workday Report. |
|  | [GetZendesk](getzendesk.md) | Incrementally fetches data from Zendesk API. |

## H

|  | Processor | Description |
| --- | --- | --- |
|  | [HandleHttpRequest](handlehttprequest.md) | Starts an HTTP Server and listens for HTTP Requests. |
|  | [HandleHttpResponse](handlehttpresponse.md) | Sends an HTTP Response to the Requestor that generated a FlowFile. |

## I

|  | Processor | Description |
| --- | --- | --- |
|  | [IdentifyMimeType](identifymimetype.md) | Attempts to identify the MIME Type used for a FlowFile. |
|  | [InvokeHTTP](invokehttp.md) | An HTTP client processor which can interact with a configurable HTTP Endpoint. |
|  | [InvokeScriptedProcessor](invokescriptedprocessor.md) | Experimental - Invokes a script engine for a Processor defined in the given script. |
|  | [ISPEnrichIP](ispenrichip.md) | Looks up ISP information for an IP address and adds the information to FlowFile attributes. |

## J

|  | Processor | Description |
| --- | --- | --- |
|  | [JoinEnrichment](joinenrichment.md) | Joins together Records from two different FlowFiles where one FlowFile, the ‘original’ contains arbitrary records and the second FlowFile, the ‘enrichment’ contains additional data that should be used to enrich the first. |
|  | [JoltTransformJSON](jolttransformjson.md) | Applies a list of Jolt specifications to either the FlowFile JSON content or a specified FlowFile JSON attribute. |
|  | [JoltTransformRecord](jolttransformrecord.md) | Applies a JOLT specification to each record in the FlowFile payload. |
|  | [JSLTTransformJSON](jslttransformjson.md) | Applies a JSLT transformation to the FlowFile JSON payload. |
|  | [JsonQueryElasticsearch](jsonqueryelasticsearch.md) | A processor that allows the user to run a query (with aggregations) written with the Elasticsearch JSON DSL. |

## L

|  | Processor | Description |
| --- | --- | --- |
|  | [ListArchivedHubSpotData](listarchivedhubspotdata.md) | Lists archived data from HubSpot for the chosen object type and generates one FlowFile per listed object with the corresponding metadata as FlowFile attributes. |
|  | [ListAzureBlobStorage_v12](listazureblobstorage_v12.md) | Lists blobs in an Azure Blob Storage container. |
|  | [ListAzureDataLakeStorage](listazuredatalakestorage.md) | Lists directory in an Azure Data Lake Storage Gen 2 filesystem |
|  | [ListBoxFile](listboxfile.md) | Lists files in a Box folder. |
|  | [ListBoxFileInfo](listboxfileinfo.md) | Fetches file metadata for each file in a Box Folder. |
|  | [ListBoxFileMetadataInstances](listboxfilemetadatainstances.md) | Retrieves all metadata instances associated with a Box file. |
|  | [ListBoxFileMetadataTemplates](listboxfilemetadatatemplates.md) | Retrieves all metadata templates associated with a Box file. |
|  | [ListConfluenceGroups](listconfluencegroups.md) | Processor listing Confluence groups. |
|  | [ListDatabaseTables](listdatabasetables.md) | Generates a set of flow files, each containing attributes corresponding to metadata about a table from a database connection. |
|  | [ListDBFSDirectory](listdbfsdirectory.md) | List file names in a DBFS directory and output a new FlowFile with the filename. |
|  | [ListDropbox](listdropbox.md) | Retrieves a listing of files from Dropbox (shortcuts are ignored). |
|  | [ListenFTP](listenftp.md) | Starts an FTP server that listens on the specified port and transforms incoming files into FlowFiles. |
|  | [ListenHTTP](listenhttp.md) | Starts an HTTP Server and listens on a given base path to transform incoming requests into FlowFiles. |
|  | [ListenOTLP](listenotlp.md) | Collect OpenTelemetry messages over HTTP or gRPC. |
|  | [ListenSlack](listenslack.md) | Retrieves real-time messages or Slack commands from one or more Slack conversations. |
|  | [ListenSyslog](listensyslog.md) | Listens for Syslog messages being sent to a given port over TCP or UDP. |
|  | [ListenTCP](listentcp.md) | Listens for incoming TCP connections and reads data from each connection using a line separator as the message demarcator. |
|  | [ListenUDP](listenudp.md) | Listens for Datagram Packets on a given port. |
|  | [ListenUDPRecord](listenudprecord.md) | Listens for Datagram Packets on a given port and reads the content of each datagram using the configured Record Reader. |
|  | [ListenWebSocket](listenwebsocket.md) | Acts as a WebSocket server endpoint to accept client connections. |
|  | [ListFile](listfile.md) | Retrieves a listing of files from the input directory. |
|  | [ListFTP](listftp.md) | Performs a listing of the files residing on an FTP server. |
|  | [ListGCSBucket](listgcsbucket.md) | Retrieves a listing of objects from a GCS bucket. |
|  | [ListGoogleDrive](listgoogledrive.md) | Performs a listing of concrete files (shortcuts are ignored) in a Google Drive folder. |
|  | [ListGoogleDriveFileInfo](listgoogledrivefileinfo.md) | Lists all files and folders in a specified Google Drive. |
|  | [ListGoogleGroups](listgooglegroups.md) | Lists all of the groups for a given domain in Google Workspace. |
|  | [ListHubSpotObjects](listhubspotobjects.md) | Fetches data from HubSpot for specified object types, and generates one FlowFile per listed object with the corresponding metadata as FlowFile attributes. |
|  | [ListMicrosoftDataverseTables](listmicrosoftdataversetables.md) | List Tables from Microsoft Dataverse environments |
|  | [ListS3](lists3.md) | Retrieves a listing of objects from an S3 bucket. |
|  | [ListSFDCDataShares](listsfdcdatashares.md) | List the available data shares in the organization that are available to the identified user. |
|  | [ListSFDCObjects](listsfdcobjects.md) | List the available objects in the organization that are available to the identified user. |
|  | [ListSFTP](listsftp.md) | Performs a listing of the files residing on an SFTP server. |
|  | [ListSharepointDrives](listsharepointdrives.md) | Emits a FlowFile for each Drive present in the specified Sharepoint Site. |
|  | [ListSharepointSiteGroups](listsharepointsitegroups.md) | Lists all SharePoint site groups available on a specified SharePoint site. |
|  | [ListSmb](listsmb.md) | Lists concrete files shared via SMB protocol. |
|  | [ListTableNames](listtablenames.md) | Fetches all source table names and matches them with one of the possible configurations: - regexp expression e. |
|  | [ListUnityCatalogDirectory](listunitycatalogdirectory.md) | List file names in a Unity Catalog directory and output a new FlowFile with the filename. |
|  | [LogAttribute](logattribute.md) | Emits attributes of the FlowFile at the specified log level |
|  | [LogMessage](logmessage.md) | Emits a log message at the specified log level |
|  | [LookupAttribute](lookupattribute.md) | Lookup attributes from a lookup service |
|  | [LookupRecord](lookuprecord.md) | Extracts one or more fields from a Record and looks up a value for those fields in a LookupService. |

## M

|  | Processor | Description |
| --- | --- | --- |
|  | [MergeContent](mergecontent.md) | Merges a Group of FlowFiles together based on a user-defined strategy and packages them into a single FlowFile. |
|  | [MergeRecord](mergerecord.md) | This Processor merges together multiple record-oriented FlowFiles into a single FlowFile that contains all of the Records of the input FlowFiles. |
|  | [MergeSnowflakeJournalTable](mergesnowflakejournaltable.md) | Triggers a merge operation on changes from journal table to a destination table in Snowflake. |
|  | [ModifyBytes](modifybytes.md) | Discard byte range at the start and end or all content of a binary file. |
|  | [ModifyCompression](modifycompression.md) | Changes the compression algorithm used to compress the contents of a FlowFile by decompressing the contents of FlowFiles using a user-specified compression algorithm and recompressing the contents using the specified compression format properties. |
|  | [MonitorActivity](monitoractivity.md) | Monitors the flow for activity and sends out an indicator when the flow has not had any data for some specified amount of time and again when the flow’s activity is restored |
|  | [MoveAzureDataLakeStorage](moveazuredatalakestorage.md) | Moves content within an Azure Data Lake Storage Gen 2. |

## N

|  | Processor | Description |
| --- | --- | --- |
|  | [Notify](notify.md) | Caches a release signal identifier in the distributed cache, optionally along with the FlowFile’s attributes. |

## O

|  | Processor | Description |
| --- | --- | --- |
|  | [OpenAiTranscribeAudio](openaitranscribeaudio.md) | Transcribes audio into English text. |

## P

|  | Processor | Description |
| --- | --- | --- |
|  | [PackageFlowFile](packageflowfile.md) | This processor will package FlowFile attributes and content into an output FlowFile that can be exported from NiFi and imported back into NiFi, preserving the original attributes and content. |
|  | [PaginatedJsonQueryElasticsearch](paginatedjsonqueryelasticsearch.md) | A processor that allows the user to run a paginated query (with aggregations) written with the Elasticsearch JSON DSL. |
|  | [ParseEvtx](parseevtx.md) | Parses the contents of a Windows Event Log file (evtx) and writes the resulting XML to the FlowFile |
|  | [ParseExcelCellReference](parseexcelcellreference.md) | Processor responsible for parsing Excel cell reference formula. |
|  | [ParseSyslog](parsesyslog.md) | Attempts to parses the contents of a Syslog message in accordance to RFC5424 and RFC3164 formats and adds attributes to the FlowFile for each of the parts of the Syslog message. |
|  | [ParseSyslog5424](parsesyslog5424.md) | Attempts to parse the contents of a well formed Syslog message in accordance to RFC5424 format and adds attributes to the FlowFile for each of the parts of the Syslog message, including Structured Data. |
|  | [PartitionRecord](partitionrecord.md) | Splits, or partitions, record-oriented data based on the configured fields in the data. |
|  | [PerformSnowflakeCortexOCR](performsnowflakecortexocr.md) | Performs Optical Character Recognition (OCR) on PDF documents using Snowflake Cortex ML functions. |
|  | [PickTablesForReplication](picktablesforreplication.md) | Accepts a list of fully qualified table names and determines if a table: - is new (is not replicated, but was added in the source) - is existing (is replicated and exists in the source) - is stale (is replicated but no longer exists in the source) Configuration is passed as a FlowFile attribute. |
|  | [PromptAnthropicAI](promptanthropicai.md) | Sends a prompt to Anthropic, writing the response either as a FlowFile attribute or to the contents of the incoming FlowFile. |
|  | [PromptAzureOpenAI](promptazureopenai.md) | Sends a prompt to Azure’s OpenAI service, writing the response either as a FlowFile attribute or to the contents of the incoming FlowFile. |
|  | [PromptLLM](promptllm.md) | This processor sends a user defined prompt to a Large Language Model (LLM) to respond. |
|  | [PromptOpenAI](promptopenai.md) | Sends a prompt to OpenAI, writing the response either as a FlowFile attribute or to the contents of the incoming FlowFile. |
|  | [PromptSnowflakeCortex](promptsnowflakecortex.md) | Sends a prompt to Snowflake Cortex, writing the response either as a FlowFile attribute or to the contents of the incoming FlowFile. |
|  | [PromptVertexAI](promptvertexai.md) | Sends a prompt to VertexAI, writing the response either as a FlowFile attribute or to the contents of the incoming FlowFile. |
|  | [PublishAMQP](publishamqp.md) | Creates an AMQP Message from the contents of a FlowFile and sends the message to an AMQP Exchange. |
|  | [PublishGCPubSub](publishgcpubsub.md) | Publishes the content of the incoming flowfile to the configured Google Cloud PubSub topic. |
|  | [PublishJMS](publishjms.md) | Creates a JMS Message from the contents of a FlowFile and sends it to a JMS Destination (queue or topic) as JMS BytesMessage or TextMessage. |
|  | [PublishKafka](publishkafka.md) | Sends the contents of a FlowFile as either a message or as individual records to Apache Kafka using the Kafka Producer API. |
|  | [PublishKafka](publishkafka.md) | Sends the contents of a FlowFile as either a message or as individual records to Apache Kafka using the Kafka Producer API. |
|  | [PublishMQTT](publishmqtt.md) | Publishes a message to an MQTT topic |
|  | [PublishSlack](publishslack.md) | Posts a message to the specified Slack channel. |
|  | [PutAzureBlobStorage_v12](putazureblobstorage_v12.md) | Puts content into a blob on Azure Blob Storage. |
|  | [PutAzureCosmosDBRecord](putazurecosmosdbrecord.md) | This processor is a record-aware processor for inserting data into Cosmos DB with Core SQL API. |
|  | [PutAzureDataExplorer](putazuredataexplorer.md) | Acts as an Azure Data Explorer sink which sends FlowFiles to the provided endpoint. |
|  | [PutAzureDataLakeStorage](putazuredatalakestorage.md) | Writes the contents of a FlowFile as a file on Azure Data Lake Storage Gen 2 |
|  | [PutAzureEventHub](putazureeventhub.md) | Send FlowFile contents to Azure Event Hubs |
|  | [PutAzureQueueStorage_v12](putazurequeuestorage_v12.md) | Writes the content of the incoming FlowFiles to the configured Azure Queue Storage. |
|  | [PutBigQuery](putbigquery.md) | Writes the contents of a FlowFile to a Google BigQuery table. |
|  | [PutBoxFile](putboxfile.md) | Puts content to a Box folder. |
|  | [PutCloudWatchMetric](putcloudwatchmetric.md) | Publishes metrics to Amazon CloudWatch. |
|  | [PutDatabaseRecord](putdatabaserecord.md) | The PutDatabaseRecord processor uses a specified RecordReader to input (possibly multiple) records from an incoming flow file. |
|  | [PutDatabricksSQL](putdatabrickssql.md) | Submit a SQL Execution using Databricks REST API then write the JSON response to FlowFile Content. |
|  | [PutDBFSFile](putdbfsfile.md) | Write FlowFile content to DBFS. |
|  | [PutDistributedMapCache](putdistributedmapcache.md) | Gets the content of a FlowFile and puts it to a distributed map cache, using a cache key computed from FlowFile attributes. |
|  | [PutDropbox](putdropbox.md) | Puts content to a Dropbox folder. |
|  | [PutDynamoDB](putdynamodb.md) | Puts a document from DynamoDB based on hash and range key. |
|  | [PutDynamoDBRecord](putdynamodbrecord.md) | Inserts items into DynamoDB based on record-oriented data. |
|  | [PutElasticsearchJson](putelasticsearchjson.md) | An Elasticsearch put processor that uses the official Elastic REST client libraries. |
|  | [PutElasticsearchRecord](putelasticsearchrecord.md) | A record-aware Elasticsearch put processor that uses the official Elastic REST client libraries. |
|  | [PutEmail](putemail.md) | Sends an e-mail to configured recipients for each incoming FlowFile |
|  | [PutFile](putfile.md) | Writes the contents of a FlowFile to the local file system |
|  | [PutFTP](putftp.md) | Sends FlowFiles to an FTP Server |
|  | [PutGCSObject](putgcsobject.md) | Writes the contents of a FlowFile as an object in a Google Cloud Storage. |
|  | [PutGoogleDrive](putgoogledrive.md) | Writes the contents of a FlowFile as a file in Google Drive. |
|  | [PutGridFS](putgridfs.md) | Writes a file to a GridFS bucket. |
|  | [PutHubSpot](puthubspot.md) | Upsert a HubSpot object. |
|  | [PutIcebergTable](puticebergtable.md) | Store records in Iceberg using configurable Catalog for managing namespaces and tables. |
|  | [PutKinesisFirehose](putkinesisfirehose.md) | Sends the contents to a specified Amazon Kinesis Firehose. |
|  | [PutKinesisStream](putkinesisstream.md) | Sends the contents to a specified Amazon Kinesis. |
|  | [PutLambda](putlambda.md) | Sends the contents to a specified Amazon Lambda Function. |
|  | [PutMongo](putmongo.md) | Writes the contents of a FlowFile to MongoDB |
|  | [PutMongoBulkOperations](putmongobulkoperations.md) | Writes the contents of a FlowFile to MongoDB as bulk-update |
|  | [PutMongoRecord](putmongorecord.md) | This processor is a record-aware processor for inserting/upserting data into MongoDB. |
|  | [PutRecord](putrecord.md) | The PutRecord processor uses a specified RecordReader to input (possibly multiple) records from an incoming flow file, and sends them to a destination specified by a Record Destination Service (i. |
|  | [PutRedisHashRecord](putredishashrecord.md) | Puts record field data into Redis using a specified hash value, which is determined by a RecordPath to a field in each record containing the hash value. |
|  | [PutS3Object](puts3object.md) | Writes the contents of a FlowFile as an S3 Object to an Amazon S3 Bucket. |
|  | [PutSalesforceObject](putsalesforceobject.md) | Creates new records for the specified Salesforce sObject. |
|  | [PutSFTP](putsftp.md) | Sends FlowFiles to an SFTP Server |
|  | [PutSmbFile](putsmbfile.md) | Writes the contents of a FlowFile to a samba network location. |
|  | [PutSnowflakeInternalStageFile](putsnowflakeinternalstagefile.md) | Puts files into a Snowflake internal stage. |
|  | [PutSnowpipeStreaming](putsnowpipestreaming.md) | Streams records into a Snowflake table. |
|  | [PutSnowpipeStreaming2](putsnowpipestreaming2.md) | Send Records formatted as Newline Delimited JSON to Snowflake Database Pipes using Snowpipe Streaming Version 2. |
|  | [PutSNS](putsns.md) | Sends the content of a FlowFile as a notification to the Amazon Simple Notification Service |
|  | [PutSplunk](putsplunk.md) | Sends logs to Splunk Enterprise over TCP, TCP + TLS/SSL, or UDP. |
|  | [PutSplunkHTTP](putsplunkhttp.md) | Sends flow file content to the specified Splunk server over HTTP or HTTPS. |
|  | [PutSQL](putsql.md) | Executes a SQL UPDATE or INSERT command. |
|  | [PutSQS](putsqs.md) | Publishes a message to an Amazon Simple Queuing Service Queue |
|  | [PutSyslog](putsyslog.md) | Sends Syslog messages to a given host and port over TCP or UDP. |
|  | [PutTCP](puttcp.md) | Sends serialized FlowFiles or Records over TCP to a configurable destination with optional support for TLS |
|  | [PutUDP](putudp.md) | The PutUDP processor receives a FlowFile and packages the FlowFile content into a single UDP datagram packet which is then transmitted to the configured UDP server. |
|  | [PutUnityCatalogFile](putunitycatalogfile.md) | Write FlowFile content with max size of 5 GiB to Unity Catalog. |
|  | [PutVectaraDocument](putvectaradocument.md) | Generate and upload a JSON document to Vectara’s upload endpoint. |
|  | [PutVectaraFile](putvectarafile.md) | Upload a FlowFile content to Vectara’s index endpoint. |
|  | [PutWebSocket](putwebsocket.md) | Sends messages to a WebSocket remote endpoint using a WebSocket session that is established by either ListenWebSocket or ConnectWebSocket. |
|  | [PutZendeskTicket](putzendeskticket.md) | Create Zendesk tickets using the Zendesk API. |

## Q

|  | Processor | Description |
| --- | --- | --- |
|  | [QueryAzureDataExplorer](queryazuredataexplorer.md) | Query Azure Data Explorer and stream JSON results to output FlowFiles |
|  | [QueryDatabaseTable](querydatabasetable.md) | Generates a SQL select query, or uses a provided statement, and executes it to fetch all rows whose values in the specified Maximum Value column(s) are larger than the previously-seen maxima. |
|  | [QueryDatabaseTableRecord](querydatabasetablerecord.md) | Generates a SQL select query, or uses a provided statement, and executes it to fetch all rows whose values in the specified Maximum Value column(s) are larger than the previously-seen maxima. |
|  | [QueryMilvus](querymilvus.md) | Queries a given collection in a Milvus database using vectors. |
|  | [QueryPinecone](querypinecone.md) | Queries Pinecone for vectors that are similar to the input vector, or retrieves a vector by ID. |
|  | [QueryRecord](queryrecord.md) | Evaluates one or more SQL queries against the contents of a FlowFile. |
|  | [QuerySalesforceObject](querysalesforceobject.md) | Retrieves records from a Salesforce sObject. |
|  | [QuerySplunkIndexingStatus](querysplunkindexingstatus.md) | Queries Splunk server in order to acquire the status of indexing acknowledgement. |

## R

|  | Processor | Description |
| --- | --- | --- |
|  | [RemoveRecordField](removerecordfield.md) | Modifies the contents of a FlowFile that contains Record-oriented data (i. |
|  | [RenameRecordField](renamerecordfield.md) | Renames one or more fields in each Record of a FlowFile. |
|  | [ReplaceText](replacetext.md) | Updates the content of a FlowFile by searching for some textual value in the FlowFile content (via Regular Expression/regex, or literal value) and replacing the section of the content that matches with some alternate value. |
|  | [ReplaceTextWithMapping](replacetextwithmapping.md) | Updates the content of a FlowFile by evaluating a Regular Expression against it and replacing the section of the content that matches the Regular Expression with some alternate value provided in a mapping file. |
|  | [RetryFlowFile](retryflowfile.md) | FlowFiles passed to this Processor have a ‘Retry Attribute’ value checked against a configured ‘Maximum Retries’ value. |
|  | [RouteOnAttribute](routeonattribute.md) | Routes FlowFiles based on their Attributes using the Attribute Expression Language |
|  | [RouteOnContent](routeoncontent.md) | Applies Regular Expressions to the content of a FlowFile and routes a copy of the FlowFile to each destination whose Regular Expression matches. |
|  | [RouteText](routetext.md) | Routes textual data based on a set of user-defined rules. |
|  | [RunDatabricksJob](rundatabricksjob.md) | Triggers a pre-defined Databricks job to run with custom parameters. |
|  | [RunMongoAggregation](runmongoaggregation.md) | A processor that runs an aggregation query whenever a flowfile is received. |

## S

|  | Processor | Description |
| --- | --- | --- |
|  | [SampleRecord](samplerecord.md) | Samples the records of a FlowFile based on a specified sampling strategy (such as Reservoir Sampling). |
|  | [ScanAttribute](scanattribute.md) | Scans the specified attributes of FlowFiles, checking to see if any of their values are present within the specified dictionary of terms |
|  | [ScanContent](scancontent.md) | Scans the content of FlowFiles for terms that are found in a user-supplied dictionary. |
|  | [ScriptedFilterRecord](scriptedfilterrecord.md) | This processor provides the ability to filter records out from FlowFiles using the user-provided script. |
|  | [ScriptedPartitionRecord](scriptedpartitionrecord.md) | Receives Record-oriented data (i. |
|  | [ScriptedTransformRecord](scriptedtransformrecord.md) | Provides the ability to evaluate a simple script against each record in an incoming FlowFile. |
|  | [ScriptedValidateRecord](scriptedvalidaterecord.md) | This processor provides the ability to validate records in FlowFiles using the user-provided script. |
|  | [SearchElasticsearch](searchelasticsearch.md) | A processor that allows the user to repeatedly run a paginated query (with aggregations) written with the Elasticsearch JSON DSL. |
|  | [SegmentContent](segmentcontent.md) | Segments a FlowFile into multiple smaller segments on byte boundaries. |
|  | [SignContentPGP](signcontentpgp.md) | Sign content using OpenPGP Private Keys |
|  | [SnowflakeDetectDuplicate](snowflakedetectduplicate.md) | Checks if a FlowFile ‘s hash (provided as a FlowFile attribute) is already in a Snowflake table, and routes the FlowFile to’ duplicate ‘if found,’distinct ‘if not found, or’ failure’ on errors. |
|  | [SplitAvro](splitavro.md) | Splits a binary encoded Avro datafile into smaller files based on the configured Output Size. |
|  | [SplitContent](splitcontent.md) | Splits incoming FlowFiles by a specified byte sequence |
|  | [SplitExcel](splitexcel.md) | This processor splits a multi sheet Microsoft Excel spreadsheet into multiple Microsoft Excel spreadsheets where each sheet from the original file is converted to an individual spreadsheet in its own flow file. |
|  | [SplitJson](splitjson.md) | Splits a JSON File into multiple, separate FlowFiles for an array element specified by a JsonPath expression. |
|  | [SplitRecord](splitrecord.md) | Splits up an input FlowFile that is in a record-oriented data format into multiple smaller FlowFiles |
|  | [SplitText](splittext.md) | Splits a text file into multiple smaller text files on line boundaries limited by maximum number of lines or total size of fragment. |
|  | [SplitXml](splitxml.md) | Splits an XML File into multiple separate FlowFiles, each comprising a child or descendant of the original root element |
|  | [StartAwsPollyJob](startawspollyjob.md) | Trigger a AWS Polly job. |
|  | [StartAwsTextractJob](startawstextractjob.md) | Trigger a AWS Textract job. |
|  | [StartAwsTranscribeJob](startawstranscribejob.md) | Trigger a AWS Transcribe job. |
|  | [StartAwsTranslateJob](startawstranslatejob.md) | Trigger a AWS Translate job. |
|  | [StartGcpVisionAnnotateFilesOperation](startgcpvisionannotatefilesoperation.md) | Trigger a Vision operation on file input. |
|  | [StartGcpVisionAnnotateImagesOperation](startgcpvisionannotateimagesoperation.md) | Trigger a Vision operation on image input. |
|  | [SubmitQueryJob](submitqueryjob.md) | Submits a Query Job to Salesforce using the Bulk API 2. |
|  | [SummarizeText](summarizetext.md) | This processor uses a Large Language Model (LLM) to summarize the content of a FlowFile. |

## T

|  | Processor | Description |
| --- | --- | --- |
|  | [TagS3Object](tags3object.md) | Adds or updates a tag on an Amazon S3 Object. |
|  | [TailFile](tailfile.md) | “Tails” a file, or a list of files, ingesting data from the file as it is written to the file. |
|  | [TransformXml](transformxml.md) | Applies the provided XSLT file to the FlowFile XML payload. |

## U

|  | Processor | Description |
| --- | --- | --- |
|  | [UnpackContent](unpackcontent.md) | Unpacks the content of FlowFiles that have been packaged with one of several different Packaging Formats, emitting one to many FlowFiles for each input FlowFile. |
|  | [UpdateAttribute](updateattribute.md) | Updates the Attributes for a FlowFile by using the Attribute Expression Language and/or deletes the attributes based on a regular expression |
|  | [UpdateBoxFileMetadataInstance](updateboxfilemetadatainstance.md) | Updates metadata template values for a Box file using the record in the given flowFile. |
|  | [UpdateBulkJobState](updatebulkjobstate.md) | Updates the status of a Salesforce Bulk Job in the shared state service for a specific object type |
|  | [UpdateByQueryElasticsearch](updatebyqueryelasticsearch.md) | Update documents in an Elasticsearch index using a query. |
|  | [UpdateCounter](updatecounter.md) | This processor allows users to set specific counters and key points in their flow. |
|  | [UpdateDatabaseTable](updatedatabasetable.md) | This processor uses a JDBC connection and incoming records to generate any database table changes needed to support the incoming records. |
|  | [UpdateRecord](updaterecord.md) | Updates the contents of a FlowFile that contains Record-oriented data (i. |
|  | [UpdateSnowflakeDatabase](updatesnowflakedatabase.md) | Updates the definition of a Snowflake table based on the schema provided in the incoming FlowFile. |
|  | [UpdateSnowflakeIcebergDatabase](updatesnowflakeicebergdatabase.md) | Updates the definition of a Snowflake Iceberg table. |
|  | [UpdateSnowflakeSchema](updatesnowflakeschema.md) | Creates Snowflake database schema if it does not exist. |
|  | [UpdateSnowflakeStream](updatesnowflakestream.md) | Manages Snowflake streams by creating, dropping, or replacing them based on the configured operation. |
|  | [UpdateSnowflakeTable](updatesnowflaketable.md) | Updates the definition of a Snowflake table based on the schema provided in the incoming FlowFile. |
|  | [UpdateSnowflakeView](updatesnowflakeview.md) | Creates or replaces Snowflake views based on column mappings provided in the incoming FlowFile. |
|  | [UpdateTableState](updatetablestate.md) | Updates the state of a table in the Table State Service |
|  | [UpsertMilvus](upsertmilvus.md) | Upserts vectors into Milvus database for a given collection |
|  | [UpsertPinecone](upsertpinecone.md) | Publishes vectors, including metadata, and optionally text, to a Pinecone index. |
|  | [UpsertSFDCObjects](upsertsfdcobjects.md) | Upserts the records from the incoming FlowFile into Salesforce |

## V

|  | Processor | Description |
| --- | --- | --- |
|  | [ValidateCsv](validatecsv.md) | Validates the contents of FlowFiles or a FlowFile attribute value against a user-specified CSV schema. |
|  | [ValidateJson](validatejson.md) | Validates the contents of FlowFiles against a configurable JSON Schema. |
|  | [ValidateRecord](validaterecord.md) | Validates the Records of an incoming FlowFile against a given schema. |
|  | [ValidateXml](validatexml.md) | Validates XML contained in a FlowFile. |
|  | [VerifyContentMAC](verifycontentmac.md) | Calculates a Message Authentication Code using the provided Secret Key and compares it with the provided MAC property |
|  | [VerifyContentPGP](verifycontentpgp.md) | Verify signatures using OpenPGP Public Keys |

## W

|  | Processor | Description |
| --- | --- | --- |
|  | [Wait](wait.md) | Routes incoming FlowFiles to the ‘wait’ relationship until a matching release signal is stored in the distributed cache from a corresponding Notify processor. |
|  | [WaitForTableState](waitfortablestate.md) | Blocks incoming FlowFiles until the corresponding table state is not equal to accepted state. |
