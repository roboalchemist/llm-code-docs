# Source: https://docs.confluent.io/cloud/current/release-notes/index.md

<a id="cloud-release-notes"></a>

# Release Notes for Confluent Cloud

Confluent Cloud is regularly updated with improvements and new features. This page
highlights significant new and updated features in Confluent Cloud by release date.

 <style>


.rss-feed-box {
     background-color: #E8F4F8;
     border-radius: 8px;
     padding: 16px 20px;
     margin: 20px 0;
     display: flex;
     align-items: center;
     gap: 16px;
 }
 .rss-icon {
     width: 40px;
     height: 40px;
     background-color: #FF6B35;
     border-radius: 4px;
     display: flex;
     align-items: center;
     justify-content: center;
     flex-shrink: 0;
 }
 .rss-icon svg {
     width: 24px;
     height: 24px;
     fill: white;
 }
 .rss-content {
     flex: 1;
     color: #0074A1;
     font-size: 14px;
     line-height: 1.5;
 }
 .rss-content a {
     color: #0074A1;
     text-decoration: underline;
 }
 .rss-content a:hover {
     color: #005a7a;
 }
 .rss-feed-url-container {
     display: flex;
     align-items: center;
     gap: 8px;
     margin-top: 4px;
 }
 .rss-feed-url {
     font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
     font-size: 13px;
     color: #0074A1;
     word-break: break-all;
     flex: 1;
 }
 .copy-button {
     background-color: transparent;
     border: 1px solid #0074A1;
     border-radius: 4px;
     color: #0074A1;
     cursor: pointer;
     padding: 4px 8px;
     font-size: 12px;
     display: flex;
     align-items: center;
     gap: 4px;
     transition: all 0.2s ease;
     flex-shrink: 0;
 }
 .copy-button:hover {
     background-color: #0074A1;
     color: white;
 }
 .copy-button:active {
     transform: scale(0.95);
 }
 .copy-button.copied {
     background-color: #28a745;
     border-color: #28a745;
     color: white;
 }
 .copy-icon {
     width: 14px;
     height: 14px;
     fill: #0074A1 !important;
     stroke: #0074A1;
 }
 .copy-button:hover .copy-icon {
     fill: white !important;
     stroke: white;
 }
 .copy-button.copied .copy-icon {
     fill: white !important;
     stroke: white;
 }
 .external-link-icon {
     display: inline-block;
     width: 12px;
     height: 12px;
     margin-left: 4px;
     vertical-align: middle;
 }
 </style>

 <div class="rss-feed-box">
    <div class="rss-icon"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M200-120q-33 0-56.5-23.5T120-200q0-33 23.5-56.5T200-280q33 0 56.5 23.5T280-200q0 33-23.5 56.5T200-120Zm480 0q0-117-44-218.5T516-516q-76-76-177.5-120T120-680v-120q142 0 265 53t216 146q93 93 146 216t53 265H680Zm-240 0q0-67-25-124.5T346-346q-44-44-101.5-69T120-440v-120q92 0 171.5 34.5T431-431q60 60 94.5 139.5T560-120H440Z"/></svg></div>
    <div class="rss-content">
         To get the latest product updates delivered to you in an RSS feed, add the URL of this page to your <a href="https://en.wikipedia.org/wiki/News_aggregator" target="_blank" rel="noopener">feed reader<svg class="external-link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></a>, or add the feed's URL directly:
         <div class="rss-feed-url-container">
             <div class="rss-feed-url" id="rss-feed-url">https://docs.confluent.io/cloud/current/release-notes.xml</div>
             <button class="copy-button" onclick="copyRssUrl()" aria-label="Copy RSS feed URL"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M360-240q-33 0-56.5-23.5T280-320v-480q0-33 23.5-56.5T360-880h360q33 0 56.5 23.5T800-800v480q0 33-23.5 56.5T720-240H360Zm0-80h360v-480H360v480ZM200-80q-33 0-56.5-23.5T120-160v-560h80v560h440v80H200Zm160-240v-480 480Z"/></svg>
                 <span class="copy-text">Copy</span>
             </button>
         </div>
    </div>
  </div>

 <script>
 function copyRssUrl() {
     const url = 'https://docs.confluent.io/cloud/current/release-notes.xml';
     const button = event.currentTarget;
     const copyText = button.querySelector('.copy-text');

     // Use modern Clipboard API if available
     if (navigator.clipboard && navigator.clipboard.writeText) {
         navigator.clipboard.writeText(url).then(function() {
             button.classList.add('copied');
             copyText.textContent = 'Copied!';
             setTimeout(function() {
                 button.classList.remove('copied');
                 copyText.textContent = 'Copy';
             }, 2000);
         }).catch(function(err) {
             console.error('Failed to copy: ', err);
             fallbackCopy(url, button, copyText);
         });
     } else {
         fallbackCopy(url, button, copyText);
     }
 }

 function fallbackCopy(text, button, copyText) {
     // Fallback for older browsers
     const textArea = document.createElement('textarea');
     textArea.value = text;
     textArea.style.position = 'fixed';
     textArea.style.opacity = '0';
     document.body.appendChild(textArea);
     textArea.select();
     try {
         document.execCommand('copy');
         button.classList.add('copied');
         copyText.textContent = 'Copied!';
         setTimeout(function() {
             button.classList.remove('copied');
             copyText.textContent = 'Copy';
         }, 2000);
     } catch (err) {
         console.error('Fallback copy failed: ', err);
     }
     document.body.removeChild(textArea);
 }
 </script>

## 2026 Releases

### March 3, 2026

- Confluent Intelligence now supports Anthropic and Fireworks AI as remote model providers.
  For more information, see [Run an AI Model with Confluent Cloud](../ai/ai-model-inference.md#flink-sql-ai-model).

March 2, 2026

- Cloud Console enables you to view and manage notifications at the resource level.
  For more information, see [Manage notifications for a resource](../monitoring/configure-notifications.md#ccloud-notifications-resource-level).
- Confluent Cloud for Apache FlinkÂ® updates the default watermark strategy
  (`SOURCE_WATERMARK()`) to use a fixed out-of-orderness tolerance of 180
  milliseconds. The new strategy produces watermarks immediately without
  requiring a minimum number of records per partition. The idle timeout for
  progressive idleness detection now starts at 10 seconds instead of 15
  seconds. Additionally, when a partition becomes idle, it forwards its latest
  event time so that idle partitions no longer block query results.
  If your data has out-of-orderness that exceeds 180ms, define a
  custom watermark strategy. For more information, see
  [SOURCE_WATERMARK](../flink/reference/functions/datetime-functions.md#flink-sql-source-watermark-function).

### February 26, 2026

- Confluent Intelligence now supports cector search with Azure Cosmos DB. You can use
  Flink SQL to perform vector similarity searches on Cosmos DB vector
  databases for real-time retrieval-augmented generation (RAG) use cases. For
  more information, see [Vector Search with External Databases](../ai/external-tables/vector-search.md#flink-sql-vector-search).

### February 25, 2026

- mTLS authentication is now generally available on AWS Enterprise and Freight clusters.
  For details, see [Configure Mutual TLS (mTLS) Authentication](../security/authenticate/workload-identities/identity-providers/mtls/configure.md#configure-mtls).
- The `query` configuration property is now available for the
  following Confluent Cloud JDBC source connectors. Use this property to
  execute custom SQL queries for joining tables or selecting specific data subsets.
  - [Microsoft SQL Server Source  (JDBC)](../connectors/cc-microsoft-sql-server-source.md#cc-microsoft-sql-server-source)
  - [MySQL Source  (JDBC)](../connectors/cc-mysql-source.md#cc-mysql-source)
  - [Oracle Database Source (JDBC)](../connectors/cc-oracle-db-source.md#cc-oracle-db-source)
  - [PostgreSQL Source  (JDBC)](../connectors/cc-postgresql-source.md#cc-postgresql-source)

### February 23, 2026

- The
  [Streams Rebalance Protocol (KIP-1071)](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1071%3A+Streams+Rebalance+Protocol)
  is now generally available for Kafka Streams applications with Enterprise
  and Dedicated clusters. This broker-driven rebalancing system reduces
  coordination overhead and improves failure detection, leading to more stable
  and responsive stream processing workloads. Kafka Streams client version 4.2 or
  later is required to use this feature. For more information, see
  [Streams Rebalance Protocol](../kafka-streams/upgrade-guide.md#streams-upgrade-guide-streams-rebalance-protocol).

### February 20, 2026

- Queues for Kafka provides queue semantics and elastic consumer scaling natively to Kafka through
  share groups and share consumers. This feature enables organizations to consolidate their messaging
  infrastructure while gaining elastic consumer scaling and per-message processing controls.
  [Share groups](../client-apps/share-consumers.md#kafka-sharegroup) and share consumers complement Kafkaâs traditional consumer API and consumer groups.

  Confluent Cloud supports all client and group level configs from [KIP-932](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka)
  and introduces a new share partition lag metric in the metrics API.

  #### NOTE
  Share groups and share consumers are only available on Dedicated and Enterprise clusters.

  To use share groups, your Java client must be compatible with Apache KafkaÂ® 4.2 or later.
  For more information, see [Client versions and support](/platform/current/clients/overview.html#client-versions-and-support.html).
- Added compressed documentation index for use in AI coding agents. This index provides a persistent context
  to AI coding agents by mapping documentation topics to their source files. For more information, see [Compressed documentation index for coding agents](../get-started/docs-ai.md#compressed-index).

### February 13, 2026

- Confluent Cloud now supports ingress gateways for private connections with your
  virtual private clouds (VPCs) in AWS. With a gateway, you can connect your VPC
  to multiple Confluent Cloud environments through AWS PrivateLink. To establish a
  connection, you register an interface VPC endpoint with a gateway access
  point. For more information, see [Use AWS PrivateLink for Serverless Products on Confluent Cloud](../networking/aws-platt.md#cloud-networking-privatelink-aws-esku).

  Gateways and access points are now the supported resources for private
  connections between AWS and Confluent Cloud. They replace PrivateLink Attachment (PLATT) resources
  and PLATT connections. Support for PLATT will end
  in a future release.

### February 11, 2026

- The fully-managed Elasticsearch Sink V2 connector for Confluent Cloud is now generally available for
  your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud. The connector writes data from a topic in Kafka to an Elasticsearch index.
  To explore a full range of features and get started with the connector, see [Elasticsearch Sink V2 connector](../connectors/cc-elasticsearch-sink-v2/cc-elasticsearch-sink-v2.md#cc-elasticsearch-sink-v2).

### February 4, 2026

- Expanded the [Operator role](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) to include the ability to describe access granted to resources through RBAC.
- The fully-managed [Google BigQuery Sink V2 Connector for Confluent Cloud](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-storage-api-sink) supports a hexadecimal converter
  for `_CHANGE_SEQUENCE_NUMBER` values. The  converter automatically transforms decimal values
  to hexadecimal format, which BigQuery requires to ensure correct record ordering and compatibility with BigQuery specifications.

### February 2, 2026

- Confluent Cloud for Apache FlinkÂ® introduces finer-grained permissions for Flink: The FlinkDeveloper
  role now can be bound to a compute pool, which enables granting access to
  an individual compute pool and all statements running in the pool.
  Also, Flink introduces a complementary role, FlinkFunctionDeveloper, to enable
  access to user-defined function (UDF) artifacts and external connectivity.
  For more information, see [FlinkDeveloper](../security/access-control/rbac/predefined-rbac-roles.md#flinkdeveloper-role) and
  [FlinkFunctionDeveloper](../security/access-control/rbac/predefined-rbac-roles.md#flinkfunctiondeveloper-role).

### January 30, 2026

- Confluent documentation now offers both HTML and Markdown versions of all content. LLMs and AI-powered IDEs can parse Markdown content more efficiently than traditional HTML content. By offering Markdown alongside HTML, Confluent documentation provides content optimized for both humans and AI tools.
  - AI agents can request the Markdown version of any document directly.
  - LLMs can scrape Confluent documentation much more efficiently, leading to better-ranked and more accurate results.

![image](images/docs-markdown.png)
- Limited Availability (LA) of mTLS now includes the AWS Freight cluster type. To sign up to try mTLS on Enterprise and Freight clusters, sign up with the [mTLS form](https://events.confluent.io/mtls-auth-limited-availability).
- [HTTP Source V2 Connector for Confluent Cloud](../connectors/cc-http-source-v2.md#cc-http-source-v2) now supports [Cursor pagination mode with absolute URL](../connectors/cc-http-source-v2.md#cc-http-source-v2-absolute-url-cursor-pagination), that
  allows using the absolute URL for subsequent requests.

### January 28, 2026

- The [ResourceOwner](../security/access-control/rbac/predefined-rbac-roles.md#resourceowner-role) role now includes permissions to create, describe, update, and delete API keys associated with the service accounts owned by the ResourceOwner. For more information about this RBAC role, see the [support advisory](https://support.confluent.io/hc/en-us/articles/45142562011924-ResourceOwner-role-can-now-create-and-manage-API-keys-tied-to-the-service-account).

### January 27, 2026

- Exactly once semantics (EOS) is now generally available for fully-managed [IBM MQ Sink connector](../connectors/cc-ibm-mq-sink.md#cc-ibm-mq-sink) on Confluent Cloud.
  For more information, see [Exactly once semantics](../connectors/cc-ibm-mq-sink.md#cc-ibmmq-sink-eos).

### January 23, 2026

- Confluent Cloud for Apache FlinkÂ® now supports multi-way join optimization for queries joining
  three or more tables on a common key. By using the `MULTI_JOIN` hint,
  the optimizer can reduce state by eliminating intermediate join results.
  For more information, see [Multi-way join optimization](../flink/reference/queries/joins.md#flink-sql-multi-way-joins).
- Confluent Cloud for Apache Flink now supports soft and hard limits on the amount of state that a
  Flink application can accumulate. You receive warnings proactively if a Flink
  application is within 80% of reaching its soft or hard limits. If a Flink
  application hits the soft limit, the statement is stopped, and you can decide
  whether you want to allow the application to keep running or resubmit the
  application with [State TTL](../flink/how-to-guides/resolve-common-query-problems.md#flink-sql-warning-high-state-no-ttl) to
  reduce the amount of state. For more information, see
  [Limits on state size](../flink/concepts/statements.md#flink-sql-statements-state-size-limits).

### January 22, 2026

- Size limits for tag definitions, tags, and business metadata are in effect. No action is needed for resources created prior to January 22, 2026.
  If newly created resources exceed the limits, the Confluent Cloud Console, Confluent CLI, or API will display a warning message indicating that the given resource exceeds the limit, and the resource will not be created.
  To learn more and view the size limits, see [Size limits for tags and metadata](../stream-governance/stream-catalog.md#size-limits-for-tags-and-metadata).

### January 21, 2026

- Secret manager integration with Confluent Cloud is now available as an Early Access feature.
  This feature enables Confluent Cloud to fetch sensitive configuration values such as secrets for
  your connectors at runtime, removing the need to persist secrets within Confluentâs
  boundary. Currently, the secret manager supports Azure Key Vault integration only. To explore
  its full range of features and get started, see [Create a secret manager integration in Confluent Cloud](../connectors/secret-manager-integration.md#cloud-secret-manager-quickstart).
- Tableflow is now generally available on Azure. You can now use Tableflow
  to expose Apache KafkaÂ® topics as Apache Icebergâ¢ and Delta Lake tables stored in Azure
  Data Lake Storage Gen2. On Azure, Tableflow can utilize private endpoints to
  connect to Azure Storage Accounts that donât allow connections from the public
  internet. For more information, see
  [Use Azure Private Networking with Tableflow](../topics/tableflow/operate/tableflow-private-networking-azure.md#tableflow-private-networking-azure).

### January 20, 2026

- **Changelog mode** is now available in SQL workspaces. You can now switch
  between table or changelog mode when viewing the results of a statement.
  For more information, see
  [Changelog entries](../flink/concepts/dynamic-tables.md#flink-sql-dynamic-tables-changelog-entries).

### January 15, 2026

- The fully-managed Amazon DocumentDB Sink connector for Confluent Cloud is now generally available
  for your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud. Configure it to map and persist events
  from Apache KafkaÂ® topics directly to a DocumentDB database collection. To explore its full range of
  features and get started, see [Amazon DocumentDB Sink Connector for Confluent Cloud](../connectors/cc-amazon-document-db-sink/cc-document-db-sink.md#cc-document-db-sink).
- Provider Integration support for AWS MemoryDB and AWS ElastiCache is now
  enabled for the following Confluent Cloud fully-managed connectors:
  - [Redis Kafka Sink connector](../connectors/cc-redis-kafka-db-sink.md#cc-redis-kafka-sink-setup-connection)
  - [Redis Kafka Source connector](../connectors/cc-redis-kafka-source.md#cc-redis-kafka-source-setup-connection)
- Confluent Cloud for Apache FlinkÂ® now supports Python User-Defined Functions (UDFs) as an Early
  Access feature. You can implement UDFs in Python and use them in Flink SQL
  statements by registering them with the [CREATE FUNCTION](../flink/reference/statements/create-function.md#flink-sql-create-function)
  statement. For more information, see
  [Create a User-Defined Function](../flink/how-to-guides/create-udf.md#flink-sql-create-udf).

### January 9, 2026

- Custom Single Message Transforms (SMT) is now generally available for your Apache KafkaÂ® clusters on Microsoft Azure.
  You can now bring your own SMTs to Confluent Cloud and use them with fully-managed connectors. For more information,
  see [Custom SMT for Confluent Cloud](../connectors/configure-custom-single-message-transforms/quick-start-custom-smt.md#cc-custom-single-message-transforms).

### January 7, 2026

- The fully-managed IBM MQ Sink connector is now generally available for your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud.
  Configure it to send messages from Kafka to an IBM MQ cluster. To explore its full range of
  features and get started, see [IBM MQ Sink Connector for Confluent Cloud](../connectors/cc-ibm-mq-sink.md#cc-ibm-mq-sink).
- Connections are now generally available in Confluent Cloud for Apache FlinkÂ®. You can use
  this feature to create secure connections to external services and data
  sources. Use the [CREATE CONNECTION](../flink/reference/statements/create-connection.md#flink-sql-create-connection)
  statement to register a connection for use in your Flink statements. For more
  information, see [Manage Connections in Confluent Cloud for Apache Flink](../flink/operate-and-deploy/manage-connections.md#flink-sql-manage-connections).
- Support for Mutual TLS (mTLS) security protocol with Enterprise clusters is now available in all AWS regions as Limited
  Availability release. For more information, see [Configure Mutual TLS Authentication on Confluent Cloud](../security/authenticate/workload-identities/identity-providers/mtls/configure.md#configure-mtls).

  To sign up to try mTLS on Enterprise clusters, use this form:
  [Sign up form for Limited Availability with mTLS Enterprise clusters](https://events.confluent.io/mtls-auth-limited-availability)
- New Confluent versions of Kafka Clients powered by librdkafka 2.13.0 are now available, including Python, JavaScript, .NET, Go, and C++.
  Included in this release are:
  - Python async and improved developer experience: Asyncio support is now GA with better context managers (`with`) and shutdown behavior
    (`close()`), richer message objects, deterministic partitioners, and type hints. Addressed issues addressed in the Python repo,
    significantly improving the developer experience around async and longârunning workloads.
  - Security, stability and performance: Updated support for [KIPâ482](https://cwiki.apache.org/confluence/display/KAFKA/KIP-482%3A+The+Kafka+Protocol+should+Support+Optional+Tagged+Fields)   by upgrading key admin APIs by improving compatibility and futureâproofing
    admin operations. Fixes addressing SSL, threadâsafety, memoryâsafety, and OAuth token refresh handling, including targeted performance
    improvements in .NET, Go, and JavaScript to keep highâthroughput workloads stable.
  - Schema Registry: Crossâlanguage upgrades for Avro schema references and associations, stricter validation flags, and multiple fixes for wrapped
    unions, bytes serialization, and caching. These improvements make Schema Registry usage smoother and more predictable across Python, .NET, Go,
    and JavaScript clients.
  - For more information, see [librdkafka 2.13 changelog](https://github.com/confluentinc/librdkafka/blob/master/CHANGELOG.md#librdkafka-v2130)
    and the Kafka [client guides](../client-apps/overview.md#java-client-guides).

### January 6, 2026

- Metrics API: Resource names now included in responses.

  Confluent Cloud now supports humanâreadable resource names in Metrics API responses for the following resource types:
  - Kafka clusters
  - Connect clusters
  - ksqlDB applications
  - Schema Registry clusters
  - Compute pools
  - Flink statements

  Previously, the Metrics API returned only resource IDs. Now, responses include both the resource ID and
  the resource name, so you can more easily find and understand metrics in your troubleshooting workflows.

## 2025 Releases

### December 30, 2025

- Confluent Cloud for Apache FlinkÂ® now supports soft and hard limits on the amount of state that a
  Flink application can accumulate. You receive warnings proactively if a Flink
  application is within 80% of reaching its soft or hard limits. If a Flink
  application hits the soft limit, the statement is stopped, and you can decide
  whether you want to allow the application to keep running or resubmit the
  application with [State TTL](../flink/how-to-guides/resolve-common-query-problems.md#flink-sql-warning-high-state-no-ttl) to
  reduce the amount of state. For more information, see
  [Limits on state size](../flink/concepts/statements.md#flink-sql-statements-state-size-limits).

### December 19, 2025

- Confluent Cloud now supports Fetch from Follower on AWS for Enterprise
  clusters with Private Network Interface (PNI) networking, adding to the existing support
  for Dedicated with VPC Peering and Freight with Private Network Interface
  (PNI) networking.

  The feature allows consumers to read from zone-local replicas to reduce
  cross-availability zone egress costs.

  For more information, see [Optimize Egress Costs with Follower Fetching on Confluent Cloud in AWS](../networking/fetch-from-follower.md#fetch-from-follower-aws).
- Enterprise and Freight clusters now support applying throughput limits
  to specific principals by configuring Client Quotas to service accounts or identity
  pools. For more information see [Multi-Tenancy and Client Quotas on Confluent Cloud](../clusters/client-quotas.md#client-quotas).
- Topic and Subject Resource level roles (for example ResourceOwner) can now view and attach metadata such as Tags, Description and Business Metadata.
  To learn more, see [Access control (RBAC) for Stream Catalog](../stream-governance/stream-catalog.md#stream-catalog-rbac).

### December 17, 2025

- Enterprise clusters with a 32 eCKU maximum limit is Generally Available in
  all three cloud providers. To scale Enterprise clusters up to a maximum of
  32 eCKU on AWS, your cluster networking must use Private Network Interface (PNI). For more
  information, see [Cluster provisioning and scaling](../clusters/cluster-types.md#cluster-scale-overview).
- You can reduce the maximum capacity on your elastic cluster by configuring a lower
  maximum eCKU than the default. Use this feature with caution. Maximum eCKU limits
  the clusterâs capacity, which can lead to throttling or workload impact when the
  reduced capacity limit is reached. For more information, see
  [Update Kafka clusters](../clusters/create-cluster.md#cloud-cluster-update-api).
- The following Single Message Transforms (SMTs) for fully-managed connectors are generally available:
  - [AdjustPrecisionAndScale](../connectors/transforms/adjustprecisionandscale.md#adjustprecisionscale)
  - [BytesToString](../connectors/transforms/bytestostring.md#bytestostring)
  - [ExtractNestedField](../connectors/transforms/extractnestedfield.md#extractnestedfield)
  - [ExtractXPath](../connectors/transforms/extractxpath.md#extractxpath)
  - [SetMaximumPrecision](../connectors/transforms/setmaximumprecision.md#setmaximumprecision) (Only available for fully-managed Source connectors)
  - [TimestampNow](../connectors/transforms/timestampnow.md#timestampnow)
  - [TimestampNowField](../connectors/transforms/timestampnowfield.md#timestampnowfield)

### December 16, 2025

- Confluent Cloud Console meets the Web Content Accessibility Guidelines (WCAG)
  2.2 standards. Read the revised
  [Accessibility Conformance Report](https://confluent.safebase.us/?itemUid=566fae90-6fe1-4c5c-bf54-eaa2b9bae1dd&source=search)
  published to the [Confluent Trust Center](https://confluent.safebase.us/) with a publish date of November 2025.

### December 15, 2025

- Confluent Cloud now supports Google Cloud Private Service Connect connections for self-managed services.
  This feature uses Egress Private Service Connect (PSC) Endpoints to enable fully-managed
  connectors in Confluent Cloud to securely access your internal services using Google Cloud Private Service Connect.
  For more information, see [Egress Private Service Connect Endpoints Setup Guide: Self-Managed Services on Google Cloud for Confluent Cloud](../connectors/networking/gcp-eap-self-managed.md#cc-gcp-eap-self-managed).
- Cross-cloud Cluster Linking on private networking is now generally available.
  You can link clusters on private networks across different cloud providers.
  For more information, see [Manage Private Networking for Cluster Linking on Confluent Cloud](../multi-cloud/cluster-linking/private-networking.md#cloud-cluster-link-private-networking) and
  [billing details for cross-cloud Cluster Linking on private networks](../billing/overview.md#cloud-cluster-linking-billing-dimensions-cross-cloud-private-networking).
- Confluent Cloud for Apache Flink now enforces strict type conversion rules when deserializing JSON data.
  If an incoming JSON type cannot be safely converted to the target SQL type defined
  in your table schema, the statement fails with a deserialization error. For the
  complete conversion matrix, see [JSON deserialization conversion behavior](../flink/reference/serialization.md#flink-sql-serialization-json-conversion-behavior).

### December 12, 2025

- You can now use [Client-Side Payload Encryption (CSPE)](../security/encrypt/cspe.md#use-client-side-payload-encryption)
  to make your data more secure on fully-managed connectors. For more information on CSPE setup
  in supported source and sink connectors, see [Manage CSPE for fully-managed connectors](../connectors/csfle.md#connect-csfle).

  This feature complements the existing Client-Side
  Field Level Encryption (CSFLE), allowing you to send all sensitive data to Confluent while maintaining full control
  over data access.
- Google Cloud private networking support is now available for the fully-managed Neo4j Sink connector
  in Confluent Cloud. To configure a Neo4j Sink connector with an Egress Private Service Connect on Google Cloud, see
  [Egress Private Service Connect Endpoint Setup: Neo4j on Google Cloud for Confluent Cloud](../connectors/cc-neo4j-sink/cc-neo4j-sink-eap-gcp.md#cc-neo4j-sink-eap-gcp).
- Google Cloud Functions (GCF) Gen 2 Sink connector enhancements:
  * You can now configure a custom URL for your Google Cloud Function, eliminating the need to
    use the default format (`https://<region-name>-<project-id>.cloudfunctions.net/<function-name>`)
  * The connector now adopts robust mTLS/SSL security standards. This allows you to
    configure essential parameters (such as keystore and truststore) to enforce TLS v1.3 for highly
    secure data transfer.

  For more information, see [Google Cloud Functions Gen 2 Sink Connector for Confluent Cloud](../connectors/cc-google-cloud-functions-gen2-sink.md#cc-google-cloud-functions-gen2-sink).

### December 10, 2025

- Exactly once semantics (EOS) is now available as an Early Access feature on Confluent Cloud for the following connectors:
  * [IBM MQ Source Connector](../connectors/cc-ibmmq-source.md#eos-ibmmq)
  * [PostgreSQL CDC Source V2 (Debezium) Connector](../connectors/cc-postgresql-cdc-source-v2-debezium/cc-postgresql-cdc-source-v2-debezium.md#eos-postgres-v2)
- [Client-side field level encryption (CSFLE)](../connectors/csfle.md#connect-csfle) is now extended to support the
  following fully-managed connectors for Confluent Cloud:
  * [Azure Data Lake Storage Gen2 Sink connector](../connectors/cc-azure-datalakeGen2-storage-sink.md#cc-azure-datalakegen2storage-sink)
  * [Azure Service Bus Source connector](../connectors/cc-azure-service-bus-source.md#cc-azure-service-bus-source)
  * [Microsoft SQL Server Source (JDBC) connector](../connectors/cc-microsoft-sql-server-source.md#cc-microsoft-sql-server-source)
  * [SFTP Source connector](../connectors/cc-sftp-source.md#cc-sftp-source)
- Confluent Cloud custom connectors are now supported with Egress PrivateLink on AWS
  in Limited Availability. If you would like to participate in the Limited
  Availability Program, contact Confluent Support.

  With this launch, you can bring custom-built connectors and run them within
  Confluent Cloud PrivateLink environments with private connectivity to external target systems.

  Dedicated and Enterprise clusters can use Egress PrivateLink
  to access external systems for custom connectors.

  Initial availability is in the AWS regions; other AWS region enablement is
  planned as a followâon.
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2
  * eu-central-1
  * ap-southeast-1
  * ap-southeast-2
  * ap-south-1
  * eu-west-2
  * ca-central-1

### December 5, 2025

- Support for Mutual TLS (mTLS) security protocol with Enterprise clusters is now a Limited
  Availability release for the following regions:
  - ap-southeast-4 â Australia (Melbourne).
  - ap-southeast-5 â Malaysia.
  - eu-south-1 â Italy (Milan).
  - eu-west-3 â France (Paris).
  - me-south-1 â Bahrain.
  - ap-east-1 â Hong Kong SAR.
  - ap-south-2 â India (Hyderabad).
  - eu-south-2 â Spain (Madrid).
  - me-central-1 â Middle East (UAE)
  - ap-northeast-2 â South Korea (Seoul).
  - ap-northeast-3 â Japan (Osaka).
  - ca-central-1 â Canada (Central/Montreal area).
  - eu-central-2 â Switzerland (Zurich).

  For more information, see [Configure Mutual TLS Authentication on Confluent Cloud](../security/authenticate/workload-identities/identity-providers/mtls/configure.md#configure-mtls).

### December 4, 2025

- Confluent Cloud now supports `iam.max_certificate_pools.per_certificate_authority` and `iam.max_identity_pools.per_identity_provider` resource scopes for service quota notifications and the [Quotas API](../quotas/quotas.md#cc-quotas).
- [ExtractTimeStamp](../connectors/transforms/extracttimestamp.md#extracttimestamp) SMT is now generally available for fully-managed HTTP V2 Sink, MongoDB Sink, and JDBC Sink connectors.
- [ChangeTopicCase](../connectors/transforms/changetopiccase.md#changetopiccase) SMT is now generally available for fully-managed JDBC Source, CDC Source, and MongoDB Source connectors.

### December 2, 2025

- Confluent Hub has been relaunched as [Confluent Marketplace](https://www.confluent.io/hub), a centralized destination for partners and community developers to share their contributions to the Confluent Cloud ecosystem. The developer experience is now simplified, and access to Developer Tools requires a login. To get started, visit the new [Confluent Marketplace](https://www.confluent.io/hub/dev-tools).

### November 22, 2025

- Confluent Cloud for Apache Flink now supports infinite scrolling UI for Flink statements. The
  Confluent Cloud Console now handles environments with large numbers of statements
  directly from the backend, instead of relying on client-side logic. This
  improvement enhances the user experience by providing faster page-load times
  and more robust filtering and sorting capabilities for listing Flink
  statements.

### November 21, 2025

- Cluster Linking can now link external Apache KafkaÂ® or Amazon MSK clusters to Confluent Cloud clusters over a private network. This supports a variety of use cases,
  including high availability data replication, disaster recovery, or data migration. Cluster Linking preserves offsets from your external sources
  to destination Confluent Cloud clusters, and provides an efficient, secure, and seamless experience. To learn more and get started quickly with the tutorial example,
  see [Link external clusters to |ccloud| over a private network](../multi-cloud/cluster-linking/private-networking.md#cloud-link-external-clusters-on-private-networking).
- The following Confluent Cloud connectors are now generally available for your Apache KafkaÂ® clusters
  on Amazon Web Services (AWS), Microsoft Azure (Azure), or Google Cloud:
  - The fully-managed InfluxDB 3 Sink connector for Confluent Cloud writes data from an Apache KafkaÂ® topic to an InfluxDB table.
    To explore a full range of features and get started with the connector, see
    [InfluxDB 3 Sink Connector for Confluent Cloud](../connectors/cc-influx-db3-sink.md#cc-influxdb3-sink).
  - The fully-managed Neo4j Sink connector for Confluent Cloud moves data moves data from Apache KafkaÂ® to Neo4j and
    Aura databases. To explore a full range of features and get started with the connector,
    see [Neo4j Sink connector for Confluent Cloud](../connectors/cc-neo4j-sink/cc-neo4j-sink.md#cc-neo4j-sink).
- The following connectors now support partitioning data using the `DefaultPartitioner` class.
  This option is available in addition to the `FieldPartitioner` and  `TimeBasedPartitioner` fields.
  - [Amazon S3 Sink](../connectors/cc-s3-sink/cc-s3-sink.md#cc-s3-connect-sink)
  - [Azure Blob Storage Sink](../connectors/cc-azure-blob-sink/cc-azure-blob-sink.md#cc-azure-blob-sink)
  - [Google Cloud Storage Sink](../connectors/cc-gcs-sink.md#cc-gcs-connect-sink)
- Azure Provider Integration support is now enabled for the following Confluent Cloud fully-managed connectors:
  - [Azure Blob Storage Sink connector](../connectors/cc-azure-blob-sink/cc-azure-blob-sink.md#cc-azure-blob-sink-setup-connection)
  - [Microsoft SQL Server CDC Source V2 (Debezium) connector](../connectors/cc-microsoft-sql-server-source-cdc-v2-debezium/cc-microsoft-sql-server-source-cdc-v2-debezium.md#cc-microsoft-sql-server-cdc-source-v2-debezium-setup-connection)

### November 20, 2025

- AWS Egress PrivateLink Endpoints are available for Confluent Cloud for Apache Flink in all
  regions where Flink is supported. Your Confluent Cloud Enterprise clusters can now
  access supported AWS services and other endpoint services powered by AWS
  PrivateLink, for example, [external tables](../ai/external-tables/overview.md#ai-external-tables-overview)
  and AWS S3. For more information, see [Enable private networking with AWS Egress PrivateLink Endpoints](../flink/operate-and-deploy/private-networking.md#flink-sql-enable-private-networking-egress).
- External table access in Confluent Cloud for Apache Flink is now generally available. You can use
  Flink SQL statements to search over external tables from Confluent Cloud. For more
  information, see:
  - [Key search with external sources](../ai/external-tables/key-search.md#flink-sql-key-search)
  - [Text search with external sources](../ai/external-tables/text-search.md#flink-sql-text-search)
  - [Vector search with external sources](../ai/external-tables/vector-search.md#flink-sql-vector-search)

  Egress and ingress data transfers from Flink are offered at no cost until
  3/31/2026.

### November 14, 2025

- The `io.confluent.kafka.server/max_pending_rebalance_time_milliseconds` metric is now available in
  the Metrics API. This metric can be used to understand how long consumer group rebalancing events
  take, as well as the frequency of those events in a given time range. For more information,
  see [Monitor Consumer Lag in Confluent Cloud](https://docs.confluent.io/cloud/current/monitoring/monitor-lag.html#monitor-ak-consumer-lag-in-ccloud).

### November 13, 2025

- Confluent Cloud Gateway is now generally available. You can use Confluent Gateway
  to secure and manage your Kafka clusters in Confluent Cloud. For more information, see
  [Gateway in Confluent Cloud](../cp-component/gateway/overview.md#gateway-overview).

  The first release of Confluent Cloud Gateway, 1.1.0, offers the following features:
  * Enables disaster recovery solutions and client migrations without client
    changes and client restarts.
  * Facilitates secure external partner access with public endpoints for private
    Kafka clusters exposure, authentication swapping, and advanced traffic
    controls.
  * Supports customizable routing and streaming domains.
  * Supports multiple combinations of authentication swapping with secure
    credential storage and retrieval.
  * Confluent Gateway now supports two license modes:
    * Trial mode (default) - No license required, and Confluent Gateway starts
      automatically in the trial mode.
    * Enterprise mode for Confluent Gateway - A valid Confluent Cloud Gateway license is
      required to have access to the full functionality of Confluent Gateway.

  The Confluent Gateway documentation is available at [Confluent Cloud Gateway Overview](../cp-component/gateway/overview.md#gateway-overview).

  Gateway deployment, route, and domain configuration samples are available on
  GitHub: [Confluent Gateway GitHub repository](https://github.com/confluentinc/gateway-images/tree/master/examples).

### November 12, 2025

- The `/discovery` endpoint for the Metrics API is now available. Use the `/discovery` endpoint
  to configure your monitoring tool to dynamically discover and scrape metrics from all authorized
  Confluent Cloud resources. This is especially useful when you want to monitor resources that are frequently
  created and deleted such as connectors. With the `/discovery` endpoint, you no longer need to update
  your Metrics API request to monitor such resources. For more information, see [Discovery endpoint](../monitoring/metrics-api.md#discovery-endpoint).
- Google Cloud Provider Integration support is now enabled for the following Confluent Cloud fully-managed connectors:
  - [Google Cloud Pub/Sub Source connector](../connectors/cc-google-pubsub-source.md#cc-google-pubsub-source-setup-connection)
  - [Google Cloud Storage (GCS) Source connector](../connectors/cc-gcs-source.md#cc-gcs-source-setup-connection)
- Early Access for Client-Side Payload Encryption (CSPE) in Confluent Cloud. With CSPE you can encrypt the entire payload,
  providing additional flexibility for comprehensive data protection. This feature complements our existing Client-Side
  Field Level Encryption (CSFLE), allowing you to send all sensitive data to Confluent while maintaining full control
  over data access. For more information, see
  [Protect Sensitive Data Using Client-Side Payload Encryption on Confluent Cloud](https://docs.confluent.io/cloud/current/security/encrypt/cspe.html).

### November 7, 2025

- The fully-managed [Oracle XStream CDC Source Connector for Confluent Cloud](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source.md#cc-oracle-xstream-cdc-source-configure-connector) now supports
  [ad-hoc blocking snapshot](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source-features.md#xstream-signals-actions) and
  [two-way TLS (mutual TLS) with client wallets](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source.md#connect-oracle-xstream-cdc-source-security).

### November 6, 2025

- [HTTP Source V2 Connector for Confluent Cloud](../connectors/cc-http-source-v2.md#cc-http-source-v2) now supports [Chaining offset with Timestamp mode](../connectors/cc-http-source-v2.md#cc-chaining-pagination-timestamp-mode), that
  combines chaining-based pagination with timestamp-based filtering.

### November 3, 2025

- Confluent Cloud for Apache Flink is now available in 13 new regions:
  - AWS
    - af-south-1
    - ap-southeast-3
    - eu-south-1
    - eu-west-3
    - me-central-1
  - Azure
    - japaneast
    - newzealandnorth
    - norwayeast
    - switzerlandnorth
  - Google Cloud
    - asia-northeast1
    - europe-north1
    - europe-west8
    - southamerica-east1

  For more information, see [Supported Cloud Regions](../flink/reference/cloud-regions.md#flink-cloud-regions).

### October 29, 2025

- The Real-Time Context Engine with Confluent Intelligence is available for early
  access. You can now enable AI agents to understand and act on live business
  context, directly from governed Apache KafkaÂ® topics. AI agents can now conduct
  low-latency queries on real-time Kafka topics because the Context Engine
  exposes topics as tools by using a fully managed MCP server. This gives AI
  agents, LLMs, and apps secure access to the freshest data without
  duplication, ETL, or spinning up infrastructure. For more information, see
  [Real-Time Context Engine](../ai/real-time-context-engine.md#real-time-context-engine).
- Streaming Agents are available as an Open Preview feature with Confluent Intelligence.
  You can now create Streaming Agents by using components like models, prompts,
  tools, and configuration like `max_iterations` for the agent. You can use
  Streaming Agents for more complex tasks requiring multiple iterations for
  reasoning and accurate results. Also, you can now define tools as resources
  in Flink, and these tools can be UDFs or MCP server tools. For
  more information, see
  [Streaming Agents in Confluent Cloud](../ai/streaming-agents/overview.md#ai-streaming-agents-overview).
- Tableflow is now available for early access in Azure regions eastus2 and
  westeurope. You can now expose your Kafka topics in near real-time as
  Apache Icebergâ¢ tables in Azure storage. For more information, see
  [Tableflow in Confluent Cloud](../topics/tableflow/overview.md#cloud-tableflow).

### October 27, 2025

- Tableflow now supports Dead-Letter Queue (DLQ) functionality. You can now
  configure Tableflow tables to send records that fail to materialize to a
  DLQ topic by using the Flink
  [error-handling.mode](../flink/reference/statements/create-table.md#flink-sql-create-table-with-error-handling-mode) and [error-handling.log.target](../flink/reference/statements/create-table.md#flink-sql-create-table-with-error-handling-log-target) table properties
  or Tableflow configurations. For more information, see
  [Tableflow Error-handling Mode](../topics/tableflow/operate/configure-tableflow.md#tableflow-configure-error-handling-mode).
- Confluent Cloud introduces the Unified Stream Manager (USM), which allows you to connect your self-managed Confluent Platform clusters to Confluent Cloud.
  USM provides a single pane of glass for unified governance, observability, and data lineage within your data
  streaming platform, no matter where your clusters reside. This feature introduces the USM Agent, a new component
  that facilitates a secure, private connection from your Confluent Platform environment to Confluent Cloud.

  It includes the following benefits:
  + Apply consistent data policies and quality rules across all your cloud and on-premises clusters from a single interface.
  + View the health and performance of all your Kafka topics, connectors, and clusters in a unified dashboard, and connect
    to existing monitoring tools such as Prometheus.
  + Manage your self-hosted Confluent Platform resources from the Confluent Cloud Console to simplify hybrid operations and streamline migrations.

  To get started, see [Unified Stream Manager in Confluent Cloud](../usm/overview.md#cloud-usm-overview).

### October 24, 2025

- The following cluster load metrics are now available on the `/export` endpoint of the Metrics API:
  - `cluster_load_percent`
  - `cluster_load_percent_average`
  - `cluster_load_percent_max`
  - `dedicated_cku_count`

  For the full list of metrics available and exportable, see the
  [metrics reference](https://api.telemetry.confluent.cloud/docs/descriptors/datasets/cloud).
- Azure private networking support is now available for the fully-managed ClickHouse Sink connector
  in Confluent Cloud. To configure a ClickHouse Sink connector with an Azure Egress Private Link Endpoint, see
  [Egress Private Link Endpoint Setup](../connectors/cc-clickhouse-sink-connector/cc-clickhouse-eap-azure.md#cc-clickhouse-sink-eap-azure).
- The fully-managed Snowflake Sink connector for Confluent Cloud now supports
  [OAuth 2.0-based database authentication](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-db-sink-oauth-setup).
- SSL/TLS support has been enhanced for the MySQL CDC Source V2 (Debezium) and
  PostgreSQL CDC Source V2 (Debezium) connectors, enabling stricter authentication modes for greater security:
  * The [MySQL CDC Source V2 (Debezium) connector](../connectors/cc-mysql-source-cdc-v2-debezium/cc-mysql-source-cdc-v2-debezium.md#cc-mysql-cdc-source-v2-debezium-setup-connection)
    now supports the `verify_ca` and `verify_identity` SSL modes.
  * The [PostgreSQL CDC Source V2 (Debezium) connector](../connectors/cc-postgresql-cdc-source-v2-debezium/cc-postgresql-cdc-source-v2-debezium.md#cc-postgresql-source-cdc-v2-debezium-setup-connection)
    now supports the `verify-ca` and `verify-full` SSL modes.
- [FromXML](../connectors/transforms/fromxml.md#fromxml) SMT is now generally available for HTTP V2 Source, HTTP V2 Sink, and IBM MQ Source connectors.

### October 22, 2025

- Confluent Cloud for Apache Flink enables creating tables that generate custom sample data. Now
  you can create *faker tables* that enable you to create custom data
  generators directly within your Flink stream-processing workflows. This
  capability enables you to generate a continuous stream of realistic test data
  without additional infrastructure or costs, streamlining development and
  testing processes. For more information, see [Generate Custom Sample Data with Confluent Cloud for Apache Flink](../flink/how-to-guides/custom-sample-data.md#flink-sql-custom-sample-data).

### October 21, 2025

- Delta Lake support for Tableflow is generally available. You can now use
  Tableflow to materialize Apache KafkaÂ® topics as Delta Lake tables in your own
  storage. For more information, see
  [Quick Start with Delta Lake Tables](../topics/tableflow/get-started/quick-start-delta-lake.md#cloud-tableflow-quick-start-delta-lake).

### October 20, 2025

An improved interface that provides a more centralized and streamlined for managing data-at-rest
encryption keys (BYOK). This new experience delivers improved transparency, better control, and greater operational efficiency.

- Centralized Hub: A new dedicated location to onboard, view, and manage all data-at-rest
  encryption keys.
- Key Identification: Easily assign a friendly, human-readable alias to keys.
- Usage Details: View total key usage and organizational limits, for example the 20 key per org limit.
- Operational Status: A new status field that shows the keyâs operational state: Ready, Pending, or Validation
  Failed.
- Associated Clusters: View the clusters actively using a specific key, with the operational status visible
  directly in the cluster settings page.
- Quick Troubleshooting: View the key policy directly in the Cloud Console, for example if key permissions are accidentally removed.
- Direct Deletion: Delete keys directly from the management interface, eliminating the need to navigate through
  the previous, multi-step cluster creation workflow.
- Simplified Search: Use filters to quickly locate specific keys based on criteria like alias, status, CSP,
  region, key ID, and associated cluster.

For more information, see the [Global Key Management](../security/encrypt/byok/overview.md#byok-global-key-management).

### October 17, 2025

- Google Cloud Provider Integration for Confluent Cloud and fully-managed connectors is
  now generally available:
  - For provider integration setup, see [Integrate with Google Cloud in Confluent Cloud](../integrations/provider-integrations/create-provider-integration-gc.md#create-provider-integration-gc).
  - For connector configuration, see [Manage Google Cloud Provider Integration for Fully-Managed Connectors](../connectors/provider-integration.md#connector-gcp-pi).
- Google Cloud Provider Integration support is now enabled for the following Confluent Cloud fully-managed connectors:
  - [Google BigQuery Sink V2 connector](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-storage-sink-setup-connection)
  - [Google Cloud Storage Sink connector](../connectors/cc-gcs-sink.md#cc-gcs-storage-sink-sink-setup-connection)
  - [PostgreSQL CDC Source V2 (Debezium) connector](../connectors/cc-postgresql-cdc-source-v2-debezium/cc-postgresql-cdc-source-v2-debezium.md#cc-postgresql-source-cdc-v2-debezium-setup-connection)
- Azure Provider Integration for Confluent Cloud and fully-managed connectors is
  now generally available:
  - For provider integration setup, see [Integrate with Azure in Confluent Cloud](../integrations/provider-integrations/create-provider-integration-azure.md#create-provider-integration-azure).
  - For connector configuration, see [Manage Azure Provider Integration for Fully-Managed Connectors](../connectors/provider-integration.md#connector-az-pi).
- Azure Provider Integration support is now enabled for the following Confluent Cloud fully-managed connectors:
  - [Azure Cosmos DB Sink V2 connector](../connectors/cc-azure-cosmos-sink-v2.md#cc-azure-cosmos-v2-sink-setup-connection)
  - [Azure Data Lake Storage Gen2 Sink connector](../connectors/cc-azure-datalakeGen2-storage-sink.md#cc-azure-datalakegen2-sink-setup-connection)
  - [Azure Cosmos DB Source V2 connector](../connectors/cc-azure-cosmos-source-v2.md#cc-cosmosdb-source-v2-setup-connection)
  - [Azure Event Hubs Source connector](../connectors/cc-azure-event-hubs-source.md#cc-azure-event-hubs-source-setup-connection)

### October 15, 2025

- Support for self-managed encryption keys (BYOK) with Tableflow is now available
  on AWS Dedicated clusters. You can now use your own encryption keys to encrypt
  Tableflow data, ensuring consistent encryption across your Kafka data and
  Tableflow tables. For more information,
  see [Use self-managed encryption keys with Tableflow](../security/encrypt/byok/tableflow-byok.md#tableflow-byok-integration).

### October 14, 2025

- AI-assisted troubleshooting is now available as a Preview feature for fully-managed connectors,
  which provides auto-generated summaries of connector issues in the Confluent Cloud Console.
  For more information, see [AI-Assisted Troubleshooting for Confluent Cloud Connectors](../connectors/reference/cflt-troubleshoot-assistant.md#cloud-ai-assist).
- The Confluent Cloud Translate API is now generally available. You can now translate a self-managed connector configuration
  to a fully-managed connector configuration using this API.
  For more information, see [Migrate a connector configuration](../connectors/connect-api-section.md#connector-migration-api).

<!-- - The :ref:`KeyToValue <keytovalue>` SMT for fully-managed connectors is generally available. -->
- Confluent Marketplace has been redesigned to make finding and deploying connectors faster and more intuitive. Key improvements include
  a redesigned interface and a new search experience that delivers more precise results. To get started, visit the new
  [Confluent Marketplace](https://www.confluent.io/hub/).

### October 13, 2025

- Confluent Cloud now supports Azure User Assigned Managed Identity (UAMI) for OAuth
  authentication. UAMI eliminates the need to manage static client IDs and
  secrets by leveraging Azureâs built-in identity management to automatically
  retrieve authentication tokens. This feature is available for Confluent Cloud and
  Confluent Platform 8.1 and later. For more information, see [Configure Azure User Assigned Managed Identity OAuth for Confluent Cloud](../security/authenticate/workload-identities/identity-providers/oauth/clients/uami.md#oauth-uami-share).

### October 10, 2025

- The new table filtering and column mapping configuration properties, including `table.include.list`,
  `table.exclude.list`,  `timestamp.columns.mapping`, and `incrementing.column.mapping`
  are now available in the following Confluent Cloud JDBC source connectors. The legacy properties,
  such as `timestamp.column.name` and `incrementing.column.name`, are now deprecated. Confluent
  recommends using the new column mapping properties for all new implementations.
  - [Microsoft SQL Server Source  (JDBC)](../connectors/cc-microsoft-sql-server-source.md#cc-microsoft-sql-server-source)
  - [MySQL Source  (JDBC)](../connectors/cc-mysql-source.md#cc-mysql-source)
  - [Oracle Database Source (JDBC)](../connectors/cc-oracle-db-source.md#cc-oracle-db-source)
  - [PostgreSQL Source  (JDBC)](../connectors/cc-postgresql-source.md#cc-postgresql-source)

### October 9, 2025

- Client-side field level encryption (CSFLE) now supports using multiple key vaults for
  high availability. You can configure multiple KEK registrations that reference the same
  encryption key material across regions or providers and implement client/proxy-driven
  failover if one key vault becomes unavailable. This feature supports cross-region
  disaster recovery scenarios and integration with on-premises Hardware Security Modules
  (HSMs) that distribute keys to multiple cloud key vaults. For more information, see the
  use of `encrypt.alternate.kms.key.ids` under `kmsProps` in
  [KEK Parameters](../security/encrypt/csfle/manage-keys.md#kek-parameters-csfle).
- Partial success response for the `/export` endpoint on the Metrics API is available as a
  Limited Availability feature in Confluent Cloud. For more information, see
  [How does the Metrics API handle requests that include inaccessible resources?](../monitoring/monitor-faq.md#metrics-api-faq-error-handling-change).
- Google Cloud VPC Service Controls (VPC-SC) is now supported for Confluent Cloud clusters using
  self-managed encryption keys. VPC-SC provides an additional security layer by
  restricting access to Google Cloud services such as Cloud Storage and Cloud KMS within a
  service perimeter. For configuration details, see [Manage key policies with Google Cloud VPC Service Controls (advanced)](../security/encrypt/byok/key-policy/manage-key-policies-gcp.md#byok-gcp-vpc-sc).

### October 7, 2025

- Autopilot scaling decisions for Confluent Cloud for Apache Flink are now available in the event logging.
  You can now view the scaling decisions for your Flink statements in the Confluent Cloud Console.
  For more information, see [Event Logging for Statements](../flink/operate-and-deploy/monitor-statements.md#flink-sql-monitor-statements-event-logging)
- Confluent for VS Code supports the full development workflow for Flink
  user defined functions (UDFs). Now you can:
  - Start Flink UDF projects from built-in templates.
  - Develop, build and test artifacts and UDFs locally.
  - Upload artifacts to Confluent Cloud.
  - Register artifacts as UDFs.
  - Author, submit, and view results of Flink SQL, referencing UDFs with the
    help of IntelliSense.

  To get the Confluent for VS Code extension, visit:
  - [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=confluentinc.vscode-confluent):
    For VS Code and VS Code Insiders
  - [OpenVSX Registry](https://open-vsx.org/extension/confluentinc/vscode-confluent):
    For Cursor and other VS Code-derived IDEs

### October 6, 2025

- Improvements to the Kafka Streams monitoring features in Confluent Cloud Console are
  generally available. You can now monitor metrics for your Kafka Streams
  applications, like application state, end-to-end latency, and process ratio.
  For more information, see [Monitor Kafka Streams Applications in Confluent Cloud](../kafka-streams/monitor-kafka-streams-apps.md#client-kafka-streams-monitor-apps).

### October 5, 2025

- The Schema Registry C++ client (`libschemaregistry`) for Confluent Cloud is generally
  available. It supports Avro, Protobuf, and JSON Schema, plus Data Contracts
  and client-side field-level encryption (CSFLE). For details and examples, see
  [Schema Registry C++ Client (libschemaregistry)](../sr/develop/cpp-clients.md#cpp-sr-client-libschemaregistry).

### October 2, 2025

- Upsert tables for Tableflow are generally available. Now you can insert,
  update, and delete individual rows in your analytics-ready tables, unlocking
  powerful new workflows for change data capture (CDC), append-mostly, and
  row-level data management. For more information see
  [Upsert Mode](../topics/tableflow/concepts/write-modes.md#cloud-tableflow-write-modes-upsert).
- Connection resources for AI/ML workloads can be created and managed directly
  by using Flink SQL. You can now use the CREATE CONNECTION statement in
  Flink SQL for creating connections to external databases and AI models. For
  more information, see [Create a Connection Resource](../flink/reference/statements/create-connection.md#flink-sql-create-connection).
- Fixed a bug where some users were unexpectedly logged out of the Confluent Cloud Console.

### October 1, 2025

- The Early Access program for UDF logging in Confluent Cloud for Apache Flink has ended. Log
  messages from user-defined functions (UDFs) now appear automatically in the
  Confluent Cloud Consoleâs
  [statement logging](../flink/operate-and-deploy/monitor-statements.md#flink-sql-monitor-statements-event-logging) page.
  For more information, see
  [Log Debug Messages in UDFs](../flink/how-to-guides/enable-udf-logging.md#flink-sql-enable-udf-logging).

### September 29, 2025

- The following Confluent Cloud connectors are now generally available for your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud.
  * The fully-managed Redis Kafka Sink connector for Confluent Cloud maps and writes records
    from Apache KafkaÂ® topics directly to a Redis database. To explore a full range of features
    and get started with the connector, see [Redis Kafka Sink connector](../connectors/cc-redis-kafka-db-sink.md#cc-redis-kafka-sink) for Confluent Cloud.
  * The fully-managed Redis Kafka Source connector for Confluent Cloud moves data from
    a Redis database into an Apache KafkaÂ® cluster in Confluent Cloud. To explore a full
    range of features and get started with the connector, see [Redis Kafka Source connector](../connectors/cc-redis-kafka-source.md#cc-redis-kafka-source) for Confluent Cloud.
- The [MongoDB Atlas Sink connector](../connectors/cc-mongo-db-sink/cc-mongo-db-sink.md#cc-mongo-db-sink) for Confluent Cloud now supports X.509 certificate-based database authentication.
- The [OpenSearch Sink connector](../connectors/cc-opensearch-sink.md#cc-opensearch-sink) for Confluent Cloud supports upsert functionality for ingested data.
- The [HTTP V2 Sink connector](../connectors/cc-http-sink-v2.md#cc-http-sink-v2) for Confluent Cloud includes the following enhancements:
  * The connector now enables upsert operations.
  * The connector now adds support for the **String** data format.
  * The connector now allows `DELETE` as a valid HTTP API request method.
- [Client-side field level encryption (CSFLE)](../connectors/csfle.md#connect-csfle) is now extended to support the
  fully-managed Salesforce CDC connector for Confluent Cloud.
- Support for Multiple Platform Events is now available in the
  [Salesforce Platform Event Source Connector](../connectors/cc-salesforce-platform-event-source.md#cc-salesforce-platform-event-source).
- Support for enhanced replay ID handling is now available in the [Salesforce Platform Event Source Connector](../connectors/cc-salesforce-platform-event-source.md#cc-salesforce-platform-event-source)
  and [Salesforce Change Data Capture (CDC) Source connector](../connectors/cc-salesforce-source-cdc.md#cc-salesforce-source-cdc).
  The connector now uses the `invalid.replay.id.behaviour` property to determine fallback behavior
  for invalid or expired event IDs.
- Confluent Cloud network for Confluent Cloud for Apache Flink is now available on Azure for all types of networks,
  including Peering clusters. For more information, see
  [Flink Private Networking](../flink/operate-and-deploy/private-networking.md#flink-sql-enable-private-networking).
- [Schema Registry Private Networking](../sr/fundamentals/sr-private-link.md#sr-ccloud-private-link) now
  supports Azure CCN Peering networks.

### September 26, 2025

- The `heartbeat.action.query` configuration is now available in the following connectors,
  which allows users to specify a custom SQL DML statement that executes on the source
  database to advance connector offsets during periods of low activity.
  - [Microsoft SQL Server CDC Source V2 (Debezium)](../connectors/cc-microsoft-sql-server-source-cdc-v2-debezium/cc-microsoft-sql-server-source-cdc-v2-debezium.md#cc-microsoft-sql-server-source-cdc-v2-debezium-configure-connector)
  - [PostgreSQL CDC Source V2 (Debezium)](../connectors/cc-postgresql-cdc-source-v2-debezium/cc-postgresql-cdc-source-v2-debezium.md#cc-postgresql-cdc-source-v2-debezium-configure-connector)
- Support for enhanced log stream capacity is now available in the
  [Amazon CloudWatch Logs Source connector](../connectors/cc-amazon-cloudwatch-logs-source.md#cc-amazon-cloudwatch-logs-source),
  enabling it to handle more than 50 log streams.
- The [legacy to Google BigQuery Sink V2 migration](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-sink-legacy-v2-migration) process
  has been enhanced to offer higher throughput, improved reliability, and better schema evolution support.

### September 25, 2025

- Confluent Cloud now maps PrivateLink endpoints to target clusters on the server side.
  This simplifies the client configuration and enables a more seamless client
  failover experience. This means Kafka clients that connect to AWS Enterprise
  clusters over AWS PrivateLink no longer require the `logicalCluster` OAuth extension
  parameter. For details, see [OAuth Configuration Reference](../security/authenticate/workload-identities/identity-providers/oauth/clients/configuration-reference.md#oauth-configuration-reference).

### September 24, 2025

- Permanent and in-line UDFs with the Table API on Confluent Cloud for Apache Flink are available
  as an Open Preview feature. For more information, see
  [Create a User-Defined Function](../flink/how-to-guides/create-udf.md#flink-sql-create-udf).

### September 19, 2025

- Support for self-managed encryption keys (including BYOK encryption) for Confluent Cloud
  Enterprise Kafka clusters and Dedicated Kafka clusters on Google Cloud is now generally available.
  For details, see [Encryption of data at rest on Kafka clusters](../security/encrypt/byok/overview.md#encryption-data-at-rest-clusters) and [Use Self-Managed Encryption Keys in Confluent Cloud on Google Cloud](../security/encrypt/byok/byok-gcp.md#byok-encrypted-clusters-gcp).

### September 18, 2025

- OAuth Auto Pool Mapping for Kafka clients and Kafka REST API is now generally
  available. This capability simplifies Kafka client configurations by reducing
  the complexity of managing multiple identity pools. You can use this
  functionality to:
  * Automatically map client tokens to all matching identity pools.
  * Grant clients the combined permissions from all matching pools.
  * Eliminate the need to specify identity pool IDs in configurations.

  For more information, see [Use auto pool mapping with OAuth identity pools](../security/authenticate/workload-identities/identity-providers/oauth/identity-pools.md#oauth-auto-pool-mapping).

### September 16, 2025

- Confluent Cloud for Apache Flink now shows state size metrics in the **Flink Statements** page
  of the Confluent Cloud Console. You can now view the state size per statement
  directly for a deeper understanding of resource usage. Integrated visual
  charts show how state size changes over time, offering a comprehensive way to
  monitor and analyze data-processing performance. State size is exposed as a
  metric in the Metrics API, enabling you to integrate it into your own
  observability tooling. For more information, see
  [Monitor and Manage SQL Statements](../flink/operate-and-deploy/monitor-statements.md#flink-sql-monitor-statements-with-cloud-console)
  and [Use Query Profiler](../flink/how-to-guides/profile-query.md#flink-sql-profile-query).

### September 15, 2025

- Private networking with Confluent Cloud for Apache Flink is now available in the following Google Cloud
  regions:
  - asia-south2
  - asia-southeast2
  - australia-southeast1

  Confluent Cloud for Apache Flink now supports public and private networking in all Confluent Cloud
  regions. For more information, see [Private Networking with Confluent Cloud for Apache Flink](../flink/concepts/flink-private-networking.md#flink-sql-private-networking).

### September 12, 2025

- Custom Connector Runtime Versioning for Confluent Cloud is now generally available.
  You can now configure the Kafka and Java runtime versions for your custom connector within
  your Confluent Cloud environments. For more information, see [Confluent Cloud API and Confluent CLI for Custom Connectors](../connectors/bring-your-connector/custom-connector-cli.md#cc-bring-your-connector-cli).

### September 9, 2025

- Confluent Cloud now offers the ability to [Infer a schema from messages](../sr/schemas-manage.md#cloud-schema-derive-from-messages), automating schema creation with a single click
  for new or existing schemaless topics with JSON messages. Avro, Protobuf, or JSON schemas can be auto-generated from sample JSON messages.
- You can now [specify a schema context to use with schema validation](../sr/broker-side-schema-validation.md#cloud-schema-validation-with-schema-context).
  The specified context will be used to search for the subject name and perform schema validation.

### September 8, 2025

- Cloud Console has an improved page for working with environments. A new environment
  overview brings all your environment details together, including clusters, compute pools, and
  network configurations. Manage tags and metadata directly from the environments page. See at
  a glance the type of Governance package available in the environment. For more information,
  see [Environments on Confluent Cloud](../security/access-control/hierarchy/cloud-environments.md#cloud-environments)

### September 5, 2025

- Event logging for statements is generally available in Confluent Cloud for Apache Flink. You can now
  view the event logs for your Flink statements in the Confluent Cloud Console. For more
  information, see [Event Logging for Statements](../flink/operate-and-deploy/monitor-statements.md#flink-sql-monitor-statements-event-logging)

### September 4, 2025

- The fully-managed [Snowflake Sink connector](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink) for Confluent Cloud now supports ingesting data into a
  Snowflake-managed [Apache Iceberg table](https://docs.snowflake.com/en/user-guide/tables-iceberg).
- Share consumers and share groups are now available as a preview feature for Java clients
  ([Queues for Kafka (KIP-932)](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka)).
  This feature introduces a concurrent processing model, allowing multiple consumers within a share group to process
  messages from the same topic partition simultaneously. This is an alternative to the traditional consumer group model,
  which assigns each partition to a single consumer. For more information, see the [documentation](../client-apps/share-consumers.md#kafka-sharegroup) and
  [Whatâs New in Apache KafkaÂ® 4.1 YouTube video](https://www.youtube.com/watch?v=cr9cDJGjm2E).

### August 29, 2025

- The [Oracle XStream CDC Source Connector for Confluent Cloud](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source.md#cc-oracle-xstream-cdc-source-configure-connector) now supports capturing change data from the following Oracle database environments:
  - The connector now supports [Amazon RDS for Oracle](../connectors/cc-oracle-xstream-cdc-source/prereqs-validation.md#connect-oracle-xstream-cdc-source-prereqs-check-amazon-rds), with the following specific configurations - Oracle Database 19c, a non-CDB architecture and non-custom deployment type.
  - The connector supports capturing changes from databases encrypted with Oracle [Transparent Data Encryption (TDE)](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source.md#cc-oracle-xstream-cdc-source-tde).
  - The connector supports [Oracle Exadata](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source.md#cc-oracle-xstream-cdc-source-supported-versions) with TDE (Transparent Data Encryption) enabled.
- Improved carry-over offsets for Confluent Cloud for Apache Flink are now generally available,
  enabling orchestrated updates of statement logic. You can now use carry-over
  offsets to start a new statement from the offsets of an existing statement.
  For more information, see [Carry Over Offsets](../flink/operate-and-deploy/carry-over-offsets.md#flink-sql-carry-over-offsets).

### August 27, 2025

- Enterprise clusters limit increase for connection attempts and total connections. Enterprise
  clusters get a maximum of 5,000 connection attempts and 180,000 total connections per cluster. For more information,
  see [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).

### August 22, 2025

- Configuring Custom SMT (Single Message Transforms) through the Confluent Cloud Console is now generally available
  for your Apache KafkaÂ® clusters on AWS. You can now bring your own SMTs to Confluent Cloud and use them with fully-managed connectors.
  For more information, see [Custom SMT for Confluent Cloud](../connectors/configure-custom-single-message-transforms/quick-start-custom-smt.md#cc-custom-single-message-transforms).

### August 19, 2025

- **Streaming Agents** with Confluent Cloud for Apache Flink are available for preview. You can
  now use the [AI_TOOL_INVOKE](../flink/reference/functions/model-inference-functions.md#flink-sql-ai-tool-invoke-function) function to invoke tools
  in your AI workflows. For more information,
  see [Invoke Tools in AI Workflows](../ai/builtin-functions/invoke-tool-ai-workflow.md#ai-invoke-tool-in-workflow).
- **Searches over external tables** are available for preview. You can now
  use the following search functions to query your data in external tables:
  - [Key Search](../ai/external-tables/key-search.md#flink-sql-key-search)
  - [Text Search](../ai/external-tables/text-search.md#flink-sql-text-search)
  - [Vector Search](../ai/external-tables/vector-search.md#flink-sql-vector-search)

  For more information, see [Searches over External Tables](../ai/external-tables/overview.md#ai-external-tables-overview).
- The [CREATE CONNECTION](../flink/reference/statements/create-connection.md#flink-sql-create-connection) statement in Confluent Cloud for Apache Flink
  is available for preview. You can now use Flink SQL to declare secure
  connections to external services for use in your Flink statements. For more
  information, see [Manage Connections](../flink/operate-and-deploy/manage-connections.md#flink-sql-manage-connections).
- [AI_COMPLETE](../flink/reference/functions/model-inference-functions.md#flink-sql-ai-complete-function) as a native Flink function
  is available for preview. You can now generate text completions,
  summaries, or answers based on streaming data.
- [AI_EMBEDDING](../flink/reference/functions/model-inference-functions.md#flink-sql-ai-embedding-function) as a native Flink
  function is available for preview. You can now generate embeddings for
  your streaming text data.
- [ML_DETECT_ANOMALIES](../flink/reference/functions/model-inference-functions.md#flink-sql-ml-anomaly-detect-function) and
  [AI_FORECAST](../flink/reference/functions/model-inference-functions.md#flink-sql-ml-forecast-function) as native Flink functions
  are now generally available. For more information, see
  [Built-in AI/ML Functions](../ai/builtin-functions/overview.md#ai-builtin-functions-overview).

### August 15, 2025

- The minimum number of CSUs for new ksqlDB clusters is now 4.

### August 14, 2025

- The fully-managed MongoDB Atlas [Source](../connectors/cc-mongo-db-source.md#cc-mongo-db-source) and [Sink](../connectors/cc-mongo-db-sink/cc-mongo-db-sink.md#cc-mongo-db-sink)
  connectors now support self-managed MongoDB instances, enabling customers to seamlessly
  connect to both self-managed and fully-managed deployments.
- Support for external key managers (EKM) for Confluent Cloud Dedicated clusters is now
  generally available on AWS using your external key manager with AWS KMS
  External Key Store (XKS). For details, see
  [Key creation and management](../security/encrypt/byok/byok-aws.md#byok-requirements-aws-key-management).
- Confluent Cloud now provides version 3.1.0 of the fully-managed Snowflake [Sink](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink) connector
  along with a critical data loss fix (SNOW-2034182). This release introduces support for the
  `snowflake.streaming.metadata.connectorPushTime` property, enabling users to [estimate ingestion latency](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-kafka#estimating-ingestion-latency).

### August 7, 2025

- Schema Registry Private Link now supports Google Cloud in a subset of regions.

  For more information, see [Schema Registry Private Networking](../sr/fundamentals/sr-private-link.md#sr-ccloud-private-link).

### August 5, 2025

- User-defined functions (UDFs) with Confluent Cloud for Apache Flink are now generally available
  in the following AWS and Azure regions:
  - AWS
    - ap-east-1
    - eu-north-1
    - me-south-1
  - Azure
    - spaincentral
    - uaenorth
    - uksouth
    - westus3

  For more information, see [User-defined Functions in Confluent Cloud for Apache Flink](../flink/concepts/user-defined-functions.md#flink-sql-udfs).

### August 4, 2025

- The fully-managed Azure Data Lake Storage Gen2 (ADLS Gen2) Sink connector
  now supports [WORM-enabled containers](../connectors/cc-azure-datalakeGen2-storage-sink.md#cc-azure-datalakegen2storage-sink).

### August 1, 2025

- Private Network Interface (PNI) Support for Enterprise Clusters on AWS

  You can now connect to Confluent Cloud Enterprise clusters on AWS using
  PNI, offering a secure and cost-effective private networking option in
  addition to AWS PrivateLink. This release delivers the following enhancements:
  * Expanded private access: PNI for Enterprise provides the same
    security assurances as PrivateLink, with the added benefit of the cost
    efficiency similar to VPC peering.
  * Dual networking: Enterprise clusters (on AWS only) now support
    dual connectivity via both PrivateLink and PNI, enabling seamless
    transitions between the two networking types without requiring cluster
    redeployment.
  * Flexible transitions: Switching an Enterprise cluster between
    PrivateLink and PNI (or vice versa) is fully supported and does not
    require downtimes or redeployment.
  * Multiple PNI gateways: Each Confluent Cloud environment can attach up to two PNI
    gateways per AWS region, accommodating complex networking topologies and
    high availability requirements.
  * Endpoint visibility: For Enterprise clusters in AWS, all
    available endpoints (PrivateLink and PNI) are displayed to facilitate
    integration and management.
  * Endpoint selection for the Confluent Cloud Console functionality: For
    Enterprise clusters in AWS, users must select which endpoint to use
    to unlock full Confluent Cloud Console functionality.
  * Consistent developer experience: Connecting through PNI offers private
    IP-based access, supporting multiple clusters in an Environment and a Region
    (including planned support for additional services) via a single PNI
    gateway.

  For more information about using PNI with Enterprise clusters,
  including setup, requirements, and considerations, see [Private Network
  Interface (PNI) Support for Enterprise Clusters on AWS](../networking/aws-pni.md#cloud-networking-pni-aws).

### July 31, 2025

- Confluent Cloud network with Schema Registry and Confluent Cloud for Apache Flink is now available on Azure for Private Link
  CCN.

  For more information, see
  [Schema Registry Private Networking](../sr/fundamentals/sr-private-link.md#sr-ccloud-private-link) and
  [Flink Private Networking](../flink/concepts/flink-private-networking.md#flink-sql-private-networking).

### July 30, 2025

- API key secrets created on or after July 30, 2025 have a `cflt` prefix. API key
  secrets created before this date do not have the `cflt` prefix, but all API key
  secrets continue to work normally for authentication. For more information, see
  [API key format](../security/authenticate/workload-identities/service-accounts/api-keys/overview.md#api-key-format).

### July 29, 2025

- Data stream in the Dark

  Dark Mode is now generally available in Confluent Cloud. This update gives you more
  flexibility and comfort while using the platformâwhether youâre working late,
  reducing screen brightness, or simply prefer a darker interface. Confluent Cloud
  automatically matches your system preferences, or you can set your preferred
  mode [manually](../faq.md#dark-mode-faq)âitâs entirely up to you.

  This feature has been popularly requested, especially from developers and
  power users who spend long hours in front of their screens. Dark Mode can help
  reduce eye strain in low-light environments and offers improved accessibility
  for users with certain visual sensitivities. Most importantly, itâs about
  delivering a better, more comfortable user experienceâwhere the interface
  works with you, not against you.

  Beyond the visual benefits, this is part of a larger effort to make Confluent Cloud Console
  more user-friendly and responsive to the needs of the community. You may have
  already noticed a refreshed color theme rolled out earlier this year as a first
  step toward supporting Dark Mode. That change laid the foundation for a more
  flexible, modern interface, and todayâs release brings it full circle.

  Dark Mode is available nowâno setup required unless [you want to customize it](../faq.md#dark-mode-faq).
  Just another way Confluent is making Confluent Cloud work better for you.
  ![Dark mode dark in |ccloud|](images/dark-mode-dark.png)![Dark mode light in |ccloud|](images/dark-mode-light.png)
- The fully-managed [PostgreSQL CDC Source V2 (Debezium) connector](../connectors/cc-postgresql-cdc-source-v2-debezium/cc-postgresql-cdc-source-v2-debezium.md#cc-prostgresql-cdc-source-v2-config-properties)
  now includes the `publish.via.partition.root` configurable property, which helps create the publication in the
  source database.

### July 25, 2025

- You can now view logs for managed connectors and custom SMTs with various search
  criteria using the Confluent CLI. For more information, see [View Connector Events for Confluent Cloud](../connectors/logging-cloud-connectors.md#ccloud-connector-logging).

### July 24, 2025

- Dark mode is available in Cloud Console for some customers during Early
  Access release. For more information, see [Does Cloud Console have dark mode?](../faq.md#dark-mode-faq).

### July 22, 2025

- Custom Connector Plugin Versioning for Confluent Cloud is now generally available.
  You can now manage different versions of your custom connector plugins within
  your Confluent Cloud environments, upload new versions, and update running connectors
  seamlessly while maintaining message offset continuity. For more information,
  see [Confluent Cloud API and Confluent CLI for Custom Connectors](../connectors/bring-your-connector/custom-connector-cli.md#cc-bring-your-connector-cli).
- Custom error handling rules for Confluent Cloud for Apache Flink are now generally available.
  Flink now supports custom error handling for deserialization errors. You can
  choose to fail, ignore, or log problematic records. When set to `log`,
  errors are sent to a Dead Letter Queue (DLQ) table. For more information, see
  [error-handling.mode](../flink/reference/statements/create-table.md#flink-sql-create-table-with-error-handling-mode).
- Query Profiler for Confluent Cloud for Apache Flink is now generally available. You can now view
  detailed information about the execution of your Flink statements, including
  the time taken for each stage, the number of records processed, and the
  amount of data transferred. For more information, see
  [Query Profiler for Confluent Cloud](../flink/operate-and-deploy/query-profiler.md#flink-sql-query-profiler).

### July 21, 2025

- Tableflow integration with Unity Catalog is available for Open Preview.
  Tableflowâs Unity Catalog integration enables you to publish materialized
  tables to Unity Catalog, making them accessible as external Delta Lake tables
  in Databricks. For more information, see
  [Integrate Tableflow with Unity Catalog in Confluent Cloud](../topics/tableflow/how-to-guides/catalog-integration/integrate-with-unity-catalog.md#cloud-tableflow-integrate-with-unity-catalog).

### July 18, 2025

- [Filter (Confluent)](../connectors/transforms/filter-confluent.md#confluent-filter) has now been extended to all Confluent Cloud fully-managed connectors.
- New SMTs for fully-managed connectors are generally available:
  - [HeaderToValue](../connectors/transforms/headertovalue.md#headertovalue)
  - [Flatten (Confluent)](../connectors/transforms/flatten-confluent.md#flatten-confluent)

### July 11, 2025

- Custom Single Message Transforms (SMT) for Confluent Cloud is now generally available
  for your Apache KafkaÂ® clusters on AWS. You can now bring your own SMTs to Confluent Cloud and use them with fully-managed connectors.
  For more information, see [Custom SMT for Confluent Cloud](../connectors/configure-custom-single-message-transforms/quick-start-custom-smt.md#cc-custom-single-message-transforms).

### July 9, 2025

- CEL filters for [SSO group mappings](../security/authenticate/user-identities/user-idps/sso/group-mapping/overview.md#group-mapping) now support the `startsWith`
  and `endsWith` operators. For more information, see [Supported CEL filter operators](../security/authenticate/user-identities/user-idps/sso/group-mapping/manage-group-mappings.md#supported-cel-operators-group-mapping).
- The [maximum number of identity pools per OAuth identity provider](../quotas/service-quotas.md#service-quotas-oauth-identity-providers)
  has been increased from `300` to `1000`.

### July 7, 2025

- Access Transparency is now in Limited Availability for Dedicated Kafka clusters.
  This feature provides visibility into when Confluent personnel access your
  Dedicated Kafka clusters for support, maintenance, or operational purposes, helping
  you meet compliance and governance requirements. For details, see
  [Access Transparency on Confluent Cloud](../monitoring/audit-logging/access-transparency-overview.md#access-transparency-overview).

### July 3, 2025

- The fully-managed MariaDB CDC Source (Debezium) connector for Confluent Cloud is now generally available
  for your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud. The connector obtain a snapshot of the existing
  data in a MariaDB database, then monitor and record all subsequent row-level changes. To explore a
  full range of features and get started with the connector, see [MariaDB CDC Source (Debezium) connector for Confluent Cloud](../connectors/cc-mariadb-cdc-source-debezium.md#cc-mariadb-source-cdc-debezium-configure-connector).
- New features for [Oracle XStream CDC Source connector](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source-features.md#xstream-features)
  for Confluent Cloud are generally available:
  * The connector now captures changes from tables that contain [large object (LOB)](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source-features.md#xstream-lob-handling) data types.
  * The connector now supports [Client-side field level encryption (CSFLE)](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source-features.md#xstream-csfle-support)
    to protect sensitive data.
  * A diagnostics script, [orclcdc_diag.sql](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source-troubleshoot.md#cc-oracle-xstream-cdc-source-troubleshooting) is available
    to help troubleshooting by collecting key diagnostic information about the
    Oracle database and XStream configuration.
- [Custom Connectors](../connectors/bring-your-connector/overview.md#cc-bring-your-connector) are now supported on Google Cloud Platform. You
  can now create and manage them directly within specified [GCP regions](../connectors/bring-your-connector/custom-connector-fands.md#cc-byoc-gcp-regions)
  supported by Confluent Cloud.
- Provider Integration support for AWS Identity and Access Management (IAM) role-based authorization
  in [Amazon Redshift Sink connector](../connectors/cc-amazon-redshift-sink.md#cc-amazon-redshift-sink)
  is now available. For more information, see [Manage Provider Integration for Fully-Managed Connectors in Confluent Cloud](../connectors/provider-integration.md#cloud-pi-quickstart).
- The fully-managed [Snowflake Sink connector](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink) for Confluent Cloud now supports HTTPS proxy support.
  This feature enables you to use an [HTTPS proxy](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink-proxy-support) to connect to Snowflake.

### July 2, 2025

- The following connectors now support partitioning data using the `FieldPartitioner` class. This option
  is available in addition to the default `TimeBasedPartitioner`.
  * [Amazon S3 Sink](../connectors/cc-s3-sink/cc-s3-sink.md#cc-s3-connect-sink)
  * [Azure Blob Storage Sink](../connectors/cc-azure-blob-sink/cc-azure-blob-sink.md#cc-azure-blob-sink)
  * [Google Cloud Storage Sink](../connectors/cc-gcs-sink.md#cc-gcs-connect-sink)

### June 30, 2025

- General release (GA) of [Schema Registry PrivateLink on Azure](../sr/fundamentals/sr-private-link.md#sr-ccloud-private-link) in the [listed regions](../sr/fundamentals/sr-private-link.md#sr-private-link-azure-regions).
  This feature enables you to connect to Schema Registry using a private endpoint within your Virtual Private Cloud (VPC)
  without egressing to the public internet, enhancing security of your data streams.

  This GA launch uses Private Link Attachments (PLATTs) for private connectivity to Schema Registry. For existing Dedicated SKU (DSKU) Kafka customers,
  youâll need to create a PLATT in the same region as your Kafka cluster to get a private endpoint for Schema Registry. For Enterprise SKU (ESKU) customers,
  the existing PLATT used for ESKU will be reused.
- The fully-managed ClickHouse sink connector for Confluent Cloud is now generally available for
  your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud. The connector maps and persists events from Apache KafkaÂ® topics directly to a
  ClickHouse database collection. To explore a full range of features and get started with the connector,
  see [ClickHouse Sink connector for Confluent Cloud](../connectors/cc-clickhouse-sink-connector/cc-clickhouse-sink.md#cc-clickhouse-sink).
- Private networking with Confluent Cloud for Apache Flink is now available in the following Google Cloud
  regions:
  - asia-south1
  - asia-southeast1
  - europe-west1
  - europe-west2
  - europe-west3
  - europe-west4
  - northamerica-northeast1
  - northamerica-northeast2
  - us-central1
  - us-east1
  - us-east4
  - us-west1
  - us-west2
  - us-west4

  For more information, see [Private Networking with Confluent Cloud for Apache Flink](../flink/concepts/flink-private-networking.md#flink-sql-private-networking).
- Confluent Cloud for Apache Flink is now available in the following regions:
  - AWS
    - ap-east-1
    - eu-north-1
    - me-south-1
  - Azure
    - spaincentral
    - uaenorth
    - uksouth
    - westus3

  Public and private networking are available for all new regions. For more
  information, see [Supported Cloud Regions for Confluent Cloud for Apache Flink](../flink/reference/cloud-regions.md#flink-cloud-regions).

### June 26th, 2025

- Statement-level CFU consumption metrics are now available in Confluent Cloud for Apache Flink and
  the Metrics API. The statement CFU metrics give you insights into the
  resources consumed by individual Flink statements running inside your compute
  pools.

  The statement CFU consumption metrics are available to view in the statements
  summary table and in the statement side panel.

  For more information, see [Statement CFU Metrics](../flink/concepts/statement-cfu-metrics.md#flink-statement-cfu).

### June 25, 2025

- The following Confluent Cloud connectors are now generally available for your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud.
  - The fully-managed Couchbase Sink connector maps and persists events from Apache KafkaÂ® topics directly to a
    Couchbase database collection. To explore a full range of features and get started with the connector,
    see [Couchbase Sink connector for Confluent Cloud](../connectors/cc-couchbase-db-sink/cc-couchbase-db-sink.md#cc-couchbase-sink).
  - The fully-managed Couchbase Source connector moves data from a Couchbase server into Apache KafkaÂ® topics
    in Confluent Cloud. To explore a full range of features and get started with the
    connector, see [Couchbase Source connector for Confluent Cloud](../connectors/cc-couchbase-db-source/cc-couchbase-db-source.md#cc-couchbase-source).

### June 24, 2025

- HTTP URLs for CRLs are now supported for Confluent Cloud mTLS authentication. For details, see
  [Configure Mutual TLS (mTLS) Authentication](../security/authenticate/workload-identities/identity-providers/mtls/configure.md#configure-mtls).
- New features for [Google BigQuery Sink V2 connector](../connectors/cc-gcp-bigquery-storage-sink.md#cloud-bigquery-v2-features) for Confluent Cloud are generally available.
  - The connector now supports the `sanitize.field.names.in.array` configuration,
    which enables sanitization of field names inside array-type objects during data ingestion.
    This ensures that nested fields within arrays follow BigQuery column naming rules.
    * If the connector ingests records with unsanitized field names inside arrays and
      `auto.update.schemas` is enabled, enabling this configuration will automatically
      update the table schema to include the sanitized field names.
    * If `auto.update.schemas` is disabled, the connector will move records containing
      sanitized fields that do not match the existing schema to the Dead Letter Queue (DLQ),
      if configured.
  - `_CHANGE_SEQUENCE_NUMBER` pseudo column support in CDC mode is now available.
    Contact Confluent [Support](https://support.confluent.io/) to enable the
    feature in your connector.
- You can now retrieve the Flink statement status from the Metrics API. This
  metric monitors and returns the status of a statement within the system.

  For more information, see
  [Query for the statement status of a Flink SQL statement](../monitoring/metrics-api.md#metrics-api-statement-status).

### June 17, 2025

- [Simplified Schema Registry Private Networking with CCN Support for AWS](../sr/fundamentals/sr-private-link.md#sr-ccloud-private-link) is now available on Confluent Cloud.

  Simplified private networking for Confluent Cloud Schema Registry with CCN (Confluent Cloud network) support significantly streamlines the setup process for private access to Schema Registry.
  Configuring a CCN for Dedicated Kafka clusters on AWS automatically provides a unique private endpoint for Schema Registry, with no additional setup required.
  Similarly, if you already have a private network connection setup for Dedicated Kafka clusters (via PrivateLink, VPC Peering, or Transit Gateway), you automatically have Schema Registry private endpoints.

  Key benefits are:
  - Simplified Setup: No extra network configuration is required if youâre already using Dedicated Kafka clusters with private networking.
  - Enhanced Security: Maintain private access to Schema Registry within your AWS environment.
  - Broad Compatibility: Supports all types of CCNs (PrivateLink, VPC Peering, and Transit Gateway).
  - Confluent Platform to Confluent Cloud Schema Linking: Can be used for [Schema Linking](../sr/schema-linking.md#schema-linking) between Confluent Platform and Confluent Cloud.
  - Comprehensive Support: Available via UI, CLI, and Terraform.
  - Wide Regional Availability:  Supported across 16 AWS regions.

### June 12, 2025

- Confluent Cloud for Apache Flink is now available in the following Google Cloud regions:
  - asia-southeast2
  - europe-west4
  - northamerica-northeast1
  - northamerica-northeast2
  - us-west2
- The limit for Flink compute pools per environment has increased from 10 to 50.

### June 5, 2025

- The logging UI has been completely redesigned and improved to simplify debugging for Confluent Cloud
  connectors. For more information, see [View Connector Events for Confluent Cloud](../connectors/logging-cloud-connectors.md#ccloud-connector-logging).
- [Client-side field level encryption (CSFLE)](../connectors/csfle.md#connect-csfle) is now extended to support the
  following fully-managed connectors for Confluent Cloud:
  * [Azure Cosmos DB Source V2 connector](../connectors/cc-azure-cosmos-source-v2.md#cc-azure-cosmos-source-v2)
  * [Azure Cosmos DB Sink V2 connector](../connectors/cc-azure-cosmos-sink-v2.md#cc-azure-cosmos-v2-sink)

### May 30, 2025

- Aliases and versions support for AWS Lambda functions is now available. For more information, see [AWS Lambda Sink Connector for Confluent Cloud](../connectors/cc-aws-lambda-sink.md#cc-aws-lambda-sink).

### May 19, 2025

- Enhanced Debezium Envelope Detection for Confluent Cloud for Apache Flink and Tableflow: Effective
  for schemas created after May 19, 2025 at 09:00 UTC that are recognized as
  incorporating a Debezium envelope, the default inference for the following
  Confluent Cloud for Apache Flink and Tableflow table properties has been updated:
  * `value-format`: The default inference has changed from `*-registry` to
    `*-debezium-registry`.
  * `changelog.mode`:
    * The default has changed from `append` to `retract`.
    * Exception: If the Kafka `cleanup.policy` is set to `compact`, the
      `changelog.mode` is set to `upsert`.

  A schema is considered to be incorporating a Debezium envelope if the data
  structure contains the fields `after`, `before`, and `op`.

  This enhancement provides automatic detection and proper handling of Debezium
  CDC (Change Data Capture) streams without requiring manual configuration. For
  more information about working with Debezium formats, see
  [Inferred tables](../flink/reference/statements/create-table.md#flink-sql-create-table-inferred-tables).

### May 18, 2025

- Snapshot queries in Confluent Cloud for Apache Flink are enabled for Early Access. For more
  information, see [Snapshot Queries in Confluent Cloud for Apache Flink](../flink/concepts/snapshot-queries.md#flink-sql-snapshot-queries).

### May 13, 2025

- [User-defined functions (UDFs)](../flink/concepts/user-defined-functions.md#flink-sql-udfs) with Confluent Cloud for Apache Flink are
  now generally available in the following Azure regions:
  - australiaeast
  - brazilsouth
  - centralindia
  - centralus
  - eastus
  - eastus2
  - francecentral
  - northeurope
  - southcentralus
  - southeastasia
  - westeurope
  - westus2

### May 12, 2025

- Provider Integration support for AWS Identity and Access Management (IAM) role-based authorization
  in [Amazon DynamoDB Sink connector](../connectors/cc-amazon-dynamo-db-sink.md#cc-amazon-dynamodb-sink)
  is now available. For more information, see [Manage Provider Integration for Fully-Managed Connectors in Confluent Cloud](../connectors/provider-integration.md#cloud-pi-quickstart).

### May 8, 2025

- [Provider Integration support](../connectors/provider-integration.md#supported-fm-pi) for AWS Identity and Access Management (IAM) role-based authorization
  has now been extended to the following Confluent Cloud fully-managed connectors:
  - [Amazon CloudWatch Logs Source connector](../connectors/cc-amazon-cloudwatch-logs-source.md#cc-amazon-cloudwatch-logs-source)
  - [Amazon Kinesis Source connector](../connectors/cc-kinesis-source.md#cc-kinesis-source)
  - [Amazon SQS Source connector](../connectors/cc-amazon-sqs-source.md#cc-amazon-sqs-source)
  - [MySQL CDC Source V2 connector](../connectors/cc-mysql-source-cdc-v2-debezium/cc-mysql-source-cdc-v2-debezium.md#cc-mysql-source-cdc-v2-debezium-configure-connector)

### May 7, 2025

- The following Confluent Cloud connectors are now generally available for your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud.
  - The fully-managed Azure Cosmos DB Sink V2 connector polls data from Apache KafkaÂ® and writes to a
    Microsoft Azure Cosmos DB database. To explore a full range of features and get started with the connector,
    see [Azure Cosmos DB Sink V2 connector for Confluent Cloud](../connectors/cc-azure-cosmos-sink-v2.md#cc-azure-cosmos-v2-sink).
  - The fully-managed Azure Cosmos DB Source V2 connector reads records from an Azure Cosmos DB database and writes
    data to Apache KafkaÂ® topics in Confluent Cloud. To explore a full range of features and get started with the
    connector, see [Azure Cosmos DB Source V2 connector for Confluent Cloud](../connectors/cc-azure-cosmos-source-v2.md#cc-azure-cosmos-source-v2).

### May 6, 2025

- Confluent Cloud for Apache Flink now includes a **Patch Method** on the Statements endpoint. This
  method enables you to update the configuration of a Flink SQL statement
  without needing to pass in the entire statement object. For more information,
  see [Patch a Statement](/cloud/current/api.html#tag/Statements-(sqlv1)/operation/patchSqlv1Statement).

### April 30, 2025

- Confluent Cloud for Apache Flink now includes the **Statement Advisor** feature, which analyzes
  Flink SQL statements when you submit them without blocking query execution
  and provides real-time warnings for queries that might lead to potential
  issues, like operational problems, high costs, or unexpected results. Key
  scenarios that trigger warnings include:
  - Mismatched primary keys and derived upsert keys.
  - High state usage without a configured state Time-to-Live (TTL).
  - Incorrect `GROUP BY` clauses in window aggregations.

  For more details on the warnings and how to resolve them,
  see [Resolve Statement Issues](../flink/how-to-guides/resolve-common-query-problems.md#flink-sql-statement-problems).

### April 28, 2025

- Confluent Cloud now supports the new [Consumer Rebalance Protocol (KIP-848)](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol)
  for use by consumers whose client libraries support the Kafka 4.0 version. For
  more information about using the protocol in your consumers, see the following:
  - For general information about the consumer rebalance protocol, see [Kafka Consumer Design: Consumers, Consumer Groups, and Offsets](https://docs.confluent.io/kafka/design/consumer-design.html).
  - For detailed information about consumers and consumer groups that use the
    new protocol, see [Kafka Consumer for Confluent Cloud](../client-apps/consumer.md#kafka-consumer-cc).
  - Cloud Console displays the consumer group protocol type from the consumer group list
    on **Consumer lag**. For more information, see [Monitor Consumer Group Rebalancing](../monitoring/monitor-lag.md#console-lag-monitoring).

### April 24, 2025

- [Client-side field level encryption (CSFLE)](../connectors/csfle.md#supported-source-csfle) is now extended to support the
  following fully-managed connectors for Confluent Cloud:
  * Azure Blob Storage Source connector
  * Google BigQuery Sink V2 connector
  * Google Cloud Functions Gen 2 Sink connector
  * MongoDB Atlas Sink connector

### April 22, 2025

- The fully-managed Oracle XStream CDC Source connector for Confluent Cloud is now generally available for
  your Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud. The connector captures all changes made to rows in
  an Oracle database and represents the changes as change event records in Apache KafkaÂ® topics.

  To explore a full range of features and get started with the connector,
  see [Oracle XStream CDC Source connector for Confluent Cloud](../connectors/cc-oracle-xstream-cdc-source/cc-oracle-xstream-cdc-source-features.md#cc-oracle-xstream-cdc-source).

### April 11, 2025

- The [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) role no longer has permissions to pause and
  resume connectors. Administrators can now grant the read-only Operator
  role to users who you want to be able to view metadata and monitor resources
  without the right to modify resources. The [ConnectManager](../security/access-control/rbac/predefined-rbac-roles.md#connectmanager-role)
  role can be used to grant users the ability to monitor, pause, and resume connectors in your
  clusters. For details, see [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) and
  [ConnectManager](../security/access-control/rbac/predefined-rbac-roles.md#connectmanager-role).
- Provider Integration support for AWS Identity and Access Management (IAM) role-based authorization in [Amazon S3 Source connector](../connectors/cc-s3-source.md#cc-s3-connect-source)
  and [AWS Lambda Sink connector](../connectors/cc-aws-lambda-sink.md#cc-aws-lambda-sink) is now available. For more information,
  see [Manage Provider Integration for Fully-Managed Connectors in Confluent Cloud](../connectors/provider-integration.md#cloud-pi-quickstart).
- Added the ability to configure common configuration properties for fully-managed connectors.
  These properties will help customers customize configurations and plan the migration from self-managed
  to fully-managed connectors. To explore a full list of supported configurations, for example, those
  for the Google BigQuery Sink V2 connector,
  see [Additional Configurations](https://docs.confluent.io/cloud/current/connectors/cc-gcp-bigquery-storage-sink.html#additional-configs).

### April 9, 2025

- TLS 1.3 has been progressively enabled across Confluent Cloud and is now used by
  default for all Confluent Cloud services, except for Kafka clusters. You can enable
  TLS 1.3 on Dedicated clusters, with support for other Confluent Cloud cluster types
  coming soon. For details, see [Manage Data in Transit with TLS](../security/encrypt/tls.md#manage-data-in-transit-with-tls).

### April 8, 2025

- Confluent Cloud for Apache Flink is now available with public and private networking in the Azure
  regions `canadacentral`, `eastasia`, and `germanywestcentral`.

### April 2, 2025

- Schema generation from Cloud Console is now available. For more information, see [Produce new messages to topics](../topics/messages.md#ccloud-msgs-produce-new).
- Azure: Support for self-managed encryption keys (aka BYOK) for Confluent Cloud Enterprise
  clusters is now available. For details, see [Encryption of data at rest on Kafka clusters](../security/encrypt/byok/overview.md#encryption-data-at-rest-clusters)
  and [Use Self-Managed Encryption Keys in Confluent Cloud on Azure](../security/encrypt/byok/byok-azure.md#byok-encrypted-clusters-azure).
- The fully-managed Snowflake Source connector captures a snapshot of the existing data in specified Snowflake tables and then monitor and record all subsequent row-level changes to that data. To explore a full range of features and get started with the connector, see [Snowflake Source Connector for Confluent Cloud](../connectors/cc-snowflake-source/cc-snowflake-source.md#cc-snowflake-source).
- Clustering support in [BigQuery V2 Sink Connector](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-storage-api-sink) is now available.

### March 31, 2025

- OAuth Auto Pool Mapping for Kafka Clients is now available as a Limited Availability
  feature. This capability simplifies Kafka client configurations, reducing the
  complexity of managing multiple identity pools. Use this functionality to:
  * Automatically map client tokens to all matching identity pools.
  * Grant clients the combined permissions from all matching pools.
  * Eliminate the need to specify identity pool IDs in configurations.

  For details and to sign up, see [Use auto pool mapping with OAuth identity pools](../security/authenticate/workload-identities/identity-providers/oauth/identity-pools.md#oauth-auto-pool-mapping).
- The Enterprise type clusters are generally available on Google Cloud.

  Enterprise clusters are designed for production-ready functionality that
  requires private endpoint networking capabilities.

  Enterprise clusters are available over Google Cloud Private Service Connect
  connections in the following Google Cloud regions:
  - us-central1 (Iowa)
  - us-east4 (N. Virginia)
  - europe-west1 (Belgium)
  - us-west4 (Las Vegas)
  - us-east1 (S. Carolina)
  - asia-southeast1 (Singapore)
  - us-west2 (Los Angeles)
  - us-west1 (Oregon)
  - europe-west2 (London)
  - asia-south1 (Mumbai)

  For details about Enterprise clusters, see [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).

  As part of this release, you can now create PrivateLink Attachments in the
  supported Google Cloud regions. For details about PrivateLink Attachment on Google Cloud, see
  [Use Google Cloud Private Service Connect for Serverless Products on Confluent Cloud](../networking/gcp-platt.md#cloud-networking-privatelink-gc-esku).
- Cluster Linking now supports Enterprise clusters and cross-cloud linking.
  - For details on supported cluster combinations, see this high level table in the Cluster Linking
    overview: [Supported cluster types](../multi-cloud/cluster-linking/index.md#cloud-cluster-linking-supported-types) and the detailed breakdown in the
    [private networking](../multi-cloud/cluster-linking/private-networking.md#cloud-cluster-link-private-networking) section:
    [Supported cluster combinations](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-private-net-supported-combos).
  - This broadened support for cluster types streamlines Cluster Linking deployment for private networking on Azure and AWS,
    as described in [How to use cluster links with private networking](../multi-cloud/cluster-linking/private-networking.md#cloud-cluster-link-how-to-use-for-private-networking).
  - To learn more about these enhancements and new supported cluster combinations for Cluster Linking, see the
    [Confluent Q1 2025 blog post on new features and updates](https://www.confluent.io/blog/latest-confluent-cloud/#additional-feature-q1).
- Confluent Cloud for Apache Flink now supports existing Confluent Cloud network to access private networking on
  AWS: this simplifies using Flink with Dedicated clusters using
  private networking (PrivateLink, VPC Peering and Transit Gateway). You no
  longer need to create any additional networking infrastructure (PLATT).
  Instead, you can access the Flink service by using use the same network
  connection established to connect to your Dedicated cluster. Also,
  this capability enables a specific DNS endpoint for every network, allowing
  various types of architectures. Existing users of private networking will
  see a new prompt in Confluent Cloud Console to choose the endpoint. For more
  information, see [Private Networking with Confluent Cloud for Apache Flink](../flink/concepts/flink-private-networking.md#flink-sql-private-networking).
- IP Filtering support for Flink: you can now control access to a Flink public
  by using [IP Filtering](../security/access-control/ip-filtering/manage-ip-filters.md#flink-operation-group-api-operations), which
  provides more flexibility to access Flink resources (statements and
  workspaces).
  - Flexibility: going forward, access to Flink resources (statements and
    workspaces) is allowed from a public endpoint by default, and you can
    restrict access based on your needs.
  - Backward compatibility: A default âdeny all public IPsâ rule has been
    applied to environments with an existing PrivateLink Attachment (PLATT) to maintain the same
    behavior that previously blocked public access once a PLATT was created in
    an environment. You can modify and open up this rule as you see fit to
    allow public access again.
- Confluent Cloud for Apache Flink is now available with public and private networking in the AWS
  region `ap-northeast-1`.

### March 28, 2025

- Dead Letter Queue (DLQ) support for handling Lambda invocation failures in the
  fully-managed [AWS Lambda Sink connector](../connectors/cc-aws-lambda-sink.md#cc-aws-lambda-sink) for Confluent Cloud is now available.
- [Client-side field level encryption (CSFLE)](../connectors/csfle.md#connect-csfle) is now extended to support the
  following fully-managed connectors for Confluent Cloud: Microsoft SQL Server CDC Source V2 (Debezium) and
  MySQL CDC Source V2 (Debezium).

### March 27, 2025

- General release (GA) of [Schema Registry PrivateLink](../sr/fundamentals/sr-private-link.md#sr-ccloud-private-link). This feature enables client applications
  in the virtual private cloud (VPC) to securely access Schema Registry without egressing to the public internet
  from your VPC. Schema Registry PrivateLink is currently available in [select regions on AWS](../sr/fundamentals/sr-private-link.md#sr-private-link-aws-regions).
- The Stream Governance UI on the Confluent Cloud Console has also been revamped for better user experience.

### March 25, 2025

- The following SQL functions have been enhanced in Confluent Cloud for Apache Flink:
  - **TO_TIMESTAMP_LTZ** function now offers overloaded functionality, supporting
    both numeric-based conversions (epoch seconds/milliseconds) and string-based
    conversions with format and timezone parameters. For more information, see
    [TO_TIMESTAMP_LTZ](../flink/reference/functions/datetime-functions.md#flink-sql-to-timestamp-ltz-function).
  - **JSON_OBJECT** and **JSON_ARRAY** functions now support nested JSON structures,
    allowing output from other JSON construction function calls to be inserted
    directly rather than as strings. This enables creating complex nested JSON
    structures with better readability and maintainability. For more information,
    see [JSON_OBJECT](../flink/reference/functions/json-functions.md#flink-sql-json-object-function) and [JSON_ARRAY](../flink/reference/functions/json-functions.md#flink-sql-json-array-function).

### March 24, 2025

- New ConnectManager role

  On **April 11, 2025**, Confluent removes permissions to pause and resume connectors
  from the [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) role. This change restores to administrators
  a read-only Operator role that can view metadata and monitor resources without the right
  to modify resources. Starting immediately, you can grant users the [ConnectManager](../security/access-control/rbac/predefined-rbac-roles.md#connectmanager-role)
  role to monitor, pause, and resume connectors in your clusters. For details, see
  [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) and [ConnectManager](../security/access-control/rbac/predefined-rbac-roles.md#connectmanager-role).
- New Google Cloud regions for Flink

  Confluent Cloud for Apache Flink is now available in Google Cloud regions us-west1 (Oregon) and europe-west2
  (London).

### March 19, 2025

- Tableflow for Apache Icebergâ¢ is now generally available in Confluent Cloud with AWS.
  This feature enables managing streaming data in Apache KafkaÂ® as tables in your data
  lake without the need for complex infrastructure management.

  Key features
  : - **GA status:** Iceberg as a destination format is now generally available.
    - **Cluster support:** Works with all cluster types in AWS, including
      Freight clusters.
    - **Networking:** Supports all networking types, with private networks using
      âBring Your Own Storageâ.
    - **Storage options:** You can store data in your own S3 bucket or use
      Confluent Managed Storage.
    - **Schema Registry formats:** Supports all Schema Registry formats (JSON Schema, Avro,
      Protobuf) and data not serialized with Schema Registry clients.
    - **Schema evolution:** Supports automatic schema evolution, including adding
      and widening columns.
    - **Table registration:** Automatically registers tables as external tables in
      AWS Glue, Snowflake Open Catalog, and Apache Polaris catalogs.
    - **Table maintenance:** Handles table maintenance such as compaction
      automatically.
    - **CLI and Terraform provider:** Launch includes support for Confluent CLI
      and Confluent Terraform provider.
    - **Metrics:** Offers a comprehensive suite of metrics including bytes and rows
      written, compaction metrics, latest offsets, and more.

  For more information, see [Tableflow in Confluent Cloud](../topics/tableflow/overview.md#cloud-tableflow).

### March 17, 2025

- [IP Filtering](../security/access-control/ip-filtering/overview.md#ip-filtering) adds support for schema management operations.
  You can enhance the security of your Confluent Cloud resources by allowing access only
  from trusted network locations, either at the organization level or at the
  environment level. You can use the predefined No Public Networks group to block
  all public network locations.
- **Confluent Cloud now supports Jio Cloud**

  Confluent announces the general availability of Confluent Cloud in the Jio India West
  region, marking the exciting beginning of a multi-year strategic partnership
  with Jio Platforms Limited. With Confluent Cloud on Jio Cloud, Indian businesses have
  the tools to unlock valuable insights, improve operational efficiency, and
  deliver superior customer experiences . This offering is available
  immediately to all Jio Cloud customers. For more information, see [Jio Cloud](../clusters/regions.md#jio-regions)
  and [How do I sign up for Confluent Cloud in Jio regions?](../faq.md#jio-regions-faq).
- **Confluent Cloud networking**

  Support for `/27` CIDR blocks is now generally available in Confluent Cloud. You can
  use `/27` CIDR blocks with your VPC Peering and Transit Gateway on AWS for
  more efficient IP address allocation.

  To learn more, see the [Confluent Cloud network CIDR blocks and block size for peering and Transit Gateway](../networking/ccloud-network/aws.md#cidr-block-size) section in
  [Create Confluent Cloud Network on AWS](../networking/ccloud-network/aws.md#create-ccloud-network-aws).

### March 14, 2025

- **ConnectManager Role**

  A new RBAC role, [ConnectManager](../security/access-control/rbac/predefined-rbac-roles.md#connectmanager-role), grants permissions
  to describe, pause, read, restart, and resume managed connectors.

### March 12, 2025

- **Topic Message Viewer Enhancements**

  We are thrilled to introduce significant updates to Topic Message Viewer in Confluent Cloud, a key tool for developers
  and operators. For more information, see [Use Message Browser in Confluent Cloud](../topics/messages.md#ccloud-topic-message-browser).

  This release includes the following enhancements:
  - **Default Page for Topics**: The message viewer is now the default view when opening any topic in Confluent Cloud.
  - **Histogram Visualization**: Message counts over time can now be visualized in a histogram. You can easily hover
    or scrub across the chart to filter by the selected time range.
  - **Increased Performance**: You can now seamlessly stream, visualize, search, and filter up to 1,000,000
    messagesâa substantial increase from the previous limit of 1,000 messages. The search and filter operations
    are performed in memory, ensuring a superior user experience.
  - **Improved Timestamp Formats**: Timestamps display in both ISO and UNIX epoch formats.
  - **New User-interface Controls**: The interface has been completely redesigned for a modern look and feel.

### March 11, 2025

- Delegated workload identity management for service accounts, OAuth identity
  pools, and certificate identity pools is now generally available for Confluent Cloud.
  Use the [ResourceOwner](../security/access-control/rbac/predefined-rbac-roles.md#resourceowner-role) and
  [Assigner](../security/access-control/rbac/predefined-rbac-roles.md#assigner-role) roles to delegate management of
  workload identities to developers and other users. With these changes,
  the following roles can now *create* workload identities:
  * [EnvironmentAdmin](../security/access-control/rbac/predefined-rbac-roles.md#environmentadmin-role)
  * [CloudClusterAdmin](../security/access-control/rbac/predefined-rbac-roles.md#cloudclusteradmin-role)
  * [KsqlAdmin](../security/access-control/rbac/predefined-rbac-roles.md#ksqladmin-role)
  * [ResourceOwner](../security/access-control/rbac/predefined-rbac-roles.md#resourceowner-role)

  CLI commands that create workload identities with the `--resource-owner`
  require require CLI version 4.18.0 or later.

  For details, see [Manage Workload Identities](../security/authenticate/workload-identities/manage-workload-identities.md#manage-workload-identities).
- A configurable property, `use.integer.for.int8.int16`, for mapping INT8 and INT16 data types to
  INTEGER in [Google BigQuery Sink V2 connector](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-storage-sink-config-properties) is now available.

### March 10, 2025

- Confluent Cloud now supports limiting user invitations to only verified organizations
  with trusted domains. For details, see [Manage Trusted Domains on Confluent Cloud](../security/authenticate/user-identities/user-idps/sso/trusted-domains.md#manage-trusted-domains).
- Confluent Cloud for Apache Flink now provides comprehensive support for Debezium CDC streams,
  making it easier to work with change data when building real-time
  applications that react to database changes.

  To enable Debezium format for your tables, use the ALTER TABLE command:
  ```sql
  -- Convert from regular Avro format to Avro Debezium format
  ALTER TABLE my_table SET (
    'value.format' = 'avro-debezium-registry',
    'changelog.mode' = 'retract'  -- Choose the appropriate mode for your use case
  );
  ```

  Note: Select the most appropriate changelog mode for your specific use case:
  - Use âretractâ when changes to the same row are represented as paired operations
  - Use âupsertâ when tracking state changes using a primary key (derived from Kafka message key)
  - Use âappendâ when each record should be treated as an independent operation

### February 19, 2025

- Cluster Linking is now generally available on Azure Private Networking (including Azure Private Link and VNet Peering)
  in a subset of Azure regions: centralus, eastus, eastus2, westus2, westus3.
  To learn more, see [Cluster Linking between Confluent Cloud clusters using Azure, AWS, or Google Cloud private networking](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-azure-privatelink) and [Supported cluster combinations](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-private-net-supported-combos).

### February 17, 2025

- The fully-managed ServiceNow Source V2 connector is now generally available for your Apache KafkaÂ®
  clusters on AWS, Azure, and Google Cloud. The connector allows you to fetch records from up to five
  ServiceNow tables simultaneously and add the records in Kafka topics in real time.

  To explore a full range of features and get started with the
  connector, see [ServiceNow Source V2 Connector for Confluent Cloud](../connectors/cc-servicenow-source-v2.md#cc-servicenow-source-v2).

### February 12, 2025

- Confluent Cloud now features a new default user interface theme designed to enhance
  user experience. Key improvements include:
  - Improved accessibility
  - Enhanced text contrast
  - Refined interactive states and elements
  - Upgraded data visualizations

  This new theme is active for all users. Log in to your Confluent Cloud account to
  experience the refreshed interface.
- New features for Flink SQL Workspaces in Confluent Cloud for Apache Flink are generally
  available.
  - Pre-submission error highlighting: The SQL editor now highlights any errors
    in your SQL before you submit a statement. The precise cause of an error is
    underlined with red squiggly lines to help you quickly determine what needs
    to be fixed.
  - Tabbed workspaces: Previously, only a single SQL Workspace could be open at
    a given time. Now, each Workspace is its own in-browser tab that maintains
    state across tab visits, enabling you to run many more statements with less
    effort.
  - Time-series visualization: The output of certain SQL statements can be
    rendered seamlessly as time-series charts. Whenever a statementâs output has
    at least one time column, and at least one numeric column, it is charted
    automatically in a time series when you toggle to chart mode. You can
    further customize charts by user interactions: you can choose a different
    x-axis column, add multiple series, change the chartâs time granularity, and
    filter the overall time range. For more information, see [View Time
    Series Data](../flink/how-to-guides/view-time-series-data.md#flink-sql-view-time-series).

### February 7, 2025

- Private networking with Confluent Cloud for Apache Flink is now generally available in all supported
  Azure regions. For more information, see [Azure supported regions](../flink/reference/cloud-regions.md#flink-cloud-regions-azure).

### February 3, 2025

* Freight clusters

  Freight clusters, a new type of Confluent Cloud cluster, are generally available on
  AWS. Freight clusters are designed for high throughput workloads with
  relaxed latency requirements. With this new cluster type, you get:
  * A managed streaming service that is up to 80% cheaper than self-managed open
    source Apache KafkaÂ®
  * Autoscaling capabilities up to 152 eCKU
  * TCO-optimizing features including zone alignment and the [Fetch from
    Follower](../networking/fetch-from-follower.md#fetch-from-follower-aws) feature

  Freight clusters are supported by the new Private Network Interface networking type.

  For more information, check out the [release blog](https://www.confluent.io/blog/freight-clusters-are-generally-available/)
  and the [Freight Cluster documentation](../clusters/cluster-types.md#freight-cluster).

<br/>
* Confluent Private Network Interface

  Confluent Cloud now supports Private Network Interface (PNI) which enables you to attach an
  Elastic Network Interface (ENI) from your AWS account to a network service
  in the Confluent AWS account. Currently it allows you to access Freight
  clusters through the ENI that resides in your AWS account.

  For more details, see [Private Network Interface on Confluent Cloud](../networking/aws-pni.md#cloud-networking-pni-aws).

### January 29, 2025

- Support for self-managed encryption keys for Confluent Cloud Enterprise Kafka clusters
  on AWS is now available. For details, see [Encryption of data at rest on Kafka clusters](../security/encrypt/byok/overview.md#encryption-data-at-rest-clusters) and
  [Use Self-Managed Encryption Keys in Confluent Cloud on AWS](../security/encrypt/byok/byok-aws.md#byok-encrypted-clusters-aws).

### January 27, 2025

- Support for external key managers (EKM) for Confluent Cloud Dedicated clusters is now
  generally available for Google Cloud using your external key manager and Google Cloud External
  Key Manager (Cloud EKM). For details, see [Key creation and management](../security/encrypt/byok/byok-gcp.md#byok-requirements-gcp-key-management).

### January 23, 2025

- Confluent Cloud supports outbound Google Cloud Private Service Connect connections using
  Egress Private Service Connect Endpoints. Egress Private Service Connect
  Endpoints enable fully managed Confluent connectors to access services from Google Cloud
  Private Service Connect service providers, such as Google, MongoDB, Snowflake, and
  others.

  With this capability, Confluent Cloud now supports private outbound connections for
  Dedicated clusters across all three cloud providers, AWS, Azure, and Google Cloud.

  For details, see [Google Cloud Egress Private Service Connect Endpoints for
  Dedicated Clusters](../networking/gcp-egress-psc.md#cloud-networking-gcp-psc-egress).
- Confluent Cloud supports resolving private DNS names from a DNS resolver within your
  own Google Cloud VPC via DNS forwarding. This feature enables fully-managed connectors
  to access endpoints using private DNS zones.

  In addition to Google Cloud Peering, DNS forwarding is supported for AWS VPC peering,
  AWS Transit Gateway connection, or Azure VNet peering in Confluent Cloud.

  For details, see [DNS forwarding for Google Cloud Peering](../networking/peering/gcp-peering.md#dns-forwarding-gcp-peering).

### January 22, 2025

- Confluent Cloud for Apache Flink is now available with public and private networking in the Azure
  region `southcentralus`.

### January 15, 2025

- Just-in-time user provisioning (JIT) for Confluent Cloud is now generally available
  for Azure Marketplace organizations. For more information,
  see [JIT user provisioning](../security/authenticate/user-identities/user-idps/sso/jit-user-provisioning.md#jit-user-provisioning).

### January 9, 2025

- The new support policy for fully-managed connectors in Confluent Cloud is now generally available.
  The policy outlines the lifecycle phases for fully-managed connectors, including details on deprecated
  connectors, end of life (EOL) timeframes, and migration recommendations by Confluent. To know more,
  see [Support policy for Confluent Cloud connectors](../connectors/overview.md#support-lifecyle-connectors).

  For information on how to upgrade to the most up-to-date, secure, and efficient version of the
  fully-managed connector, see [Deprecated connectors and migration path](../connectors/overview.md#deprecated-connectors).

## 2024 Releases

### December 20, 2024

The following features are now available in Confluent Cloud for Apache Flink:

- **DROP TABLE Support:** You can now completely [remove tables](../flink/reference/statements/drop-table.md#flink-sql-drop-table)
  and their underlying Kafka topics in Confluent Cloud for Apache Flink. For tables using
  TopicNameStrategy,  this removes both the Kafka topic and associated schemas.
  With RecordNameStrategy or TopicRecordNameStrategy, it safely removes only the
  Kafka topic while preserving shared schemas. This enables complete lifecycle
  management of Flink tables through SQL.
- **Support for TopicNameStrategy and RecordNameStrategy:** You can now work with Kafka
  topics using RecordNameStrategy or TopicRecordNameStrategy as subject naming strategies.
  Users can now configure their tables with various formats (`avro-registry`, `json-registry`,
  or `proto-registry`) and handle [multiple event types](../flink/how-to-guides/multiple-event-types.md#flink-sql-multiple-event-types)
  in a single table.
- **Enhanced EXPLAIN Statement Features:** The [EXPLAIN](../flink/reference/statements/explain.md#flink-sql-explain) statement now
  provides deeper query insights and optimization guidance, including:
  - Detailed visibility into upsert and primary keys for each operator
  - Support for EXPLAIN on CREATE TABLE AS SELECT statements
  - Enhanced physical execution plan details
  - Comprehensive changelog mode information
  - Advanced optimization recommendations for data movement, skew handling, and sink configuration

### December 19, 2024

Azure private networking with Confluent Cloud for Apache Flink is now available as a Limited
Availability feature in the following regions: `AustraliaEast`, `WestUS2`.

The [AccountAdmin](../security/access-control/rbac/predefined-rbac-roles.md#accountadmin-role) role can now perform operations
(Create, Alter, Delete, and Describe) on identity pools and group mappings.
Also, the [ResourceOwner](../security/access-control/rbac/predefined-rbac-roles.md#resourceowner-role) role can now be assigned
for specific identity pools and group mappings.

### December 18, 2024

User-defined functions (UDFs) in Confluent Cloud for Apache Flink are now generally available. UDFs
enable running custom logic that you canât express in the system-provided
Flink SQL [queries](../flink/reference/queries/overview.md#flink-sql-queries) or with the
[Table API](../flink/reference/table-api.md#flink-table-api).

You can implement user-defined functions in Java, and you can use third-party
libraries within a UDF. Confluent Cloud for Apache Flink supports scalar functions (UDFs), which map
scalar values to a new scalar value, and table functions (UDTFs), which map
multiple scalar values to multiple output rows.

For more information, see
[Create a User-Defined Function](../flink/how-to-guides/create-udf.md#flink-sql-create-udf).

### December 16, 2024

Confluent JavaScript Client for Apache KafkaÂ® is now generally available.

This client provides developers a way to program Kafka clients in JavaScript or
TypeScript in Node.js environments, all while being officially maintained by
Confluent and supported by Confluent Global Technical Support.

With this client, developers get:

* The option to use either a callback API or a promised API, similar to
  existing JavaScript clients that are available today
* A supported Schema Registry client, with OAuth capabilities
* Client-side field level encryption (CSFLE)

For more information, check out the [release blog](https://www.confluent.io/blog/introducing-confluent-kafka-javascript/), the
[JavaScript Client documentation](https://docs.confluent.io/kafka-clients/javascript/current/overview.html),
and [the library on Github](https://github.com/confluentinc/confluent-kafka-javascript).

### November 22, 2024

The following features are now available in Confluent Cloud for Apache Flink:

- **Move statements between compute pools:** Compute pools are crucial for
  managing both budget and workload isolation. To give you more control and
  flexibility, you can now move statements between pools, which can be
  particularly useful if youâre close to maxing out the resources in one pool.
- **Change security principal:** If you have statements in production that were
  created with a user account, now you can switch these statements to a service
  account, which provides better security and stability, ensuring that your
  statements arenât affected by changes in user status or authorization.

### November 20, 2024

Confluent Cloud for Apache Flink is now available in the AWS region `ca-central-1` and Azure
`brazilsouth`, `francecentral`, and `northeurope`. For more information,
see [Supported Cloud Regions for Confluent Cloud for Apache Flink](../flink/reference/cloud-regions.md#flink-cloud-regions).

### November 18, 2024

The following features have been added to Confluent Cloud for Apache Flink:

- View Support: Introduces [CREATE VIEW](../flink/reference/statements/create-view.md#flink-sql-create-view),
  ALTER VIEW, and DROP VIEW statements for creating and managing virtual
  tables. Views can simplify complex queries, and provide a consistent
  interface to the underlying tables while abstracting away implementation
  details, significantly simplifying query management and promoting code
  reuse across your Flink SQL applications.
- The [kafka.producer.compression.type table option](../flink/reference/statements/create-table.md#flink-sql-create-table-with-kafka-producer-compression-type)
  is now supported on Flink tables for configuring the compression type for
  producers. This allows optimizing network and storage usage by compressing
  records before sending to Kafka.
- The [kafka.consumer.isolation-level property](../flink/reference/statements/create-table.md#flink-sql-create-table-with-kafka-consumer-isolation-level)
  is now available on Flink tables to control which transactional messages are
  read by Flink. This enables trade-offs between latency and consistency,
  allowing consumption of in-progress transactions if needed. For more
  information, see [delivery guarantees and latency](../flink/concepts/delivery-guarantees.md#flink-sql-delivery-guarantees-latency).
- When using private networking, cross-environment queries are now supported,
  bringing parity with statements created on public networking: a statement in
  an environment accessed by a PrivateLink Attachment can now use three-part-name references,
  for example, `SELECT * from mycatalog.mydatabase.mytable`, to access tables
  in other environments.

### November 7, 2024

The following features have been added to Confluent Cloud for Apache Flink:

- **Carry-over-offset between statements:** This feature improves CI/CD for
  stateless statements by enabling a new statement to process data where a
  previous one stopped, which avoids unnecessary re-processing and minimizes
  catch-up time when updating query logic. For more information, see
  [Schema and Statement Evolution](../flink/concepts/schema-statement-evolution.md#flink-sql-schema-and-statement-evolution).

New performance metrics and observability improvements are available in
Confluent Cloud Console:

- **Watermarks:** Now you have visibility on watermarks, a critical feature that
  shows how âfreshâ your data is. Viewing watermarks is an essential tool for
  debugging Flink statements.
- **Per-table metrics:** Flink metrics like watermarks and number of messages
  are now emitted per table, which enables more fine-grained observability.
  These metrics are available in the Cloud Console and the
  [Metrics API](https://api.telemetry.confluent.cloud/docs/descriptors/datasets/cloud).
- **Enhanced Statement details:** The upgraded statement details panel in
  Cloud Console offers granular metrics at the topic/table level,
  giving you a transparent view of how messages are being read from sources and
  written to sinks.
- **Stability indicators:** Now you can see when back pressure is increasing on
  your queries, alerting you to potential performance issues.

For more information, see
[Monitor and Manage Flink Statements](../flink/operate-and-deploy/monitor-statements.md#flink-sql-monitor-statements-with-cloud-console).

### October 28, 2024

Confluent Cloud Enterprise clusters now support connecting to external data systems,
such as Azure services, AWS services, MongoDB, Snowflake, and others through AWS
PrivateLink or Azure Private Link with fully managed connectors.

For details, see [AWS Egress PrivateLink Endpoints for Serverless Products](../networking/aws-egress-privatelink-esku.md#cloud-networking-privatelink-aws-egress-esku).

For details, see [Azure Egress Private Link Endpoints for Serverless
Products](../networking/azure-egress-privatelink-esku.md#cloud-networking-privatelink-azure-egress-esku).

### October 21, 2024

Mutual TLS (mTLS) authentication for Confluent Cloud Dedicated clusters is promoted to
General Availability (GA). For details, see [mTLS for Confluent Cloud](../security/authenticate/workload-identities/identity-providers/mtls/overview.md#mtls-overview).

The following features are now available in Confluent Cloud for Apache Flink:

- Resume a stopped statement: Ensures that statements can continue after
  resolving upstream issues or during operational pauses.
- Support for SESSION Windows: SESSION windows group elements by sessions of
  activity. Unlike TUMBLE and HOP windows, session windows donât overlap and
  donât have a fixed start and end time. Instead, they group events
  automatically based on their time. For more information see:
  [SESSION Windows](../flink/reference/queries/window-tvf.md#flink-sql-window-tvfs-session).
- Schema context support: Confluent Cloud for Apache Flink now fully supports Schema context from
  Schema Registry. It automatically detects and uses the appropriate schema context for
  your Flink tables, minimizing manual intervention.
- Support for state TTL per table: This feature gives you precise control over
  state retention at the individual operator level. For more information, see:
  [Dynamic Table Options](../flink/reference/statements/hints.md#flink-sql-hints).

### October 15, 2024

You can now use IBM MQâs HA/DR support by adding multiple hosts in the `mq.connection.list`. For more details, see [IBM MQ Connection](https://docs.confluent.io/cloud/current/connectors/cc-ibmmq-source.html#ibm-mq-connection).

### October 14, 2024

You can now use [Client-side field level encryption (CSFLE)](../security/encrypt/csfle/overview.md#client-side-field-level-encryption)
to make your data more secure on fully-managed connectors. For more information on CSFLE setup in supported source and sink connectors,
see [Manage CSFLE for connectors](../connectors/csfle.md#connect-csfle).

### October 9, 2024

Confluent Cloud for Apache Flink is now available in the AWS regions `ap-northeast-2` and
`sa-east-1`.

### October 7, 2024

[Client-side field level encryption (CSFLE)](../security/encrypt/csfle/overview.md#client-side-field-level-encryption),
is promoted to General Availability (GA). CSFLE provides an additional layer of security
on Confluent Cloud for protection of sensitive data, safeguarding data in motion throughout
its lifecycle across producers and consumers.

For details, see [Protect Sensitive Data Using Client-Side Field Level Encryption on Confluent Cloud](../security/encrypt/csfle/overview.md#csfle-overview).

Confluent Cloud Provider Integration is promoted to General Availability (GA). You can now configure AWS Identity
and Access Management (IAM) roles in Confluent through Confluent Cloud Console, Confluent CLI, Confluent APIs, or Confluent Terraform Provider.
These IAM roles can then be used to configure and authorize fully-managed connectors, allowing you to create
a secure access connection between AWS source or sink resources and Confluent Cloud for data ingestion or
transfer.

For more information, see [Manage Provider Integration for Fully-Managed Connectors in Confluent Cloud](../connectors/provider-integration.md#cloud-pi-quickstart).

### October 3, 2024

You can now use Confluent Cloud Console to reset offsets for generic consumer groups. For more
information, see [Reset Consumer Offsets in Confluent Cloud](../client-apps/offsets-consumer.md#offset-consumer-manage).

### October 1, 2024

Mutual TLS (mTLS) support for Confluent Cloud is now available as a Limited Availability
feature for select Confluent customers. To request early access before General
Availability, please contact Confluent Support.

mTLS can be used for client certificate authentication and to provide granular
access control to Confluent Cloud Dedicated clusters.

For details, see [mTLS for Confluent Cloud](../security/authenticate/workload-identities/identity-providers/mtls/overview.md#mtls-overview).

### September 30, 2024

ksqlDB version 7.7.0-318 was released to Confluent Cloud.

### September 16, 2024

Confluent Cloud for Apache Flink is now available in the Azure `centralus` and Azure
`australiaeast` regions.

The following features have been added to Confluent Cloud for Apache Flink:

- **Flexible schemas**
  - [Schema-less topics:](../flink/how-to-guides/process-schemaless-events.md#flink-sql-schemaless-events) Flink now
    supports events backed by Kafka topics in which the bytestream isnât
    serialized with Schema Registry serializers, but instead plain Avro, JSON or
    Protobuf. You can submit the schema to Schema Registry and query the table
    immediately.
  - [Support for schema references:](../flink/how-to-guides/multiple-event-types.md#flink-sql-multiple-event-types) Flink
    now supports schema reference for Avro, Protobuf, and JSON. This is the
    preferred method to use multiple event types in the same table (topic).
- **SQL improvements**
  - [CREATE TABLE AS (CTAS) statement:](../flink/reference/statements/create-table.md#flink-sql-ctas) Now you can
    create and populate tables with the results of a query by using a single
    statement.
  - [EXPLAIN:](../flink/reference/statements/explain.md#flink-sql-explain) You can view and analyze the query
    plans of Flink SQL statements.
  - [Support for dynamic table hints:](../flink/reference/statements/hints.md#flink-sql-hints) You can specify
    table options on a per-statement basis for options like `scan.startup.mode`.
  - Windows Aggregate can now be used with retract streams.
- **Table API** for Java and Python is available in Open Preview. Get started
  with the [Java Table API Quick Start](../flink/get-started/quick-start-java-table-api.md#flink-java-table-api-quick-start)
  and [Python Table API Quick Start](../flink/get-started/quick-start-python-table-api.md#flink-python-table-api-quick-start)
  guides.
- **AI model inference** is available in Open Preview. Confluent Cloud for Apache Flink supports AI
  model inference and enables using models as resources in Flink SQL, similar
  to tables and functions. Models running on the following solutions are
  supported: AWS Bedrock, AWS Sagemaker, Azure OpenAI, Azure ML, Google AI,
  OpenAI, and Vertex AI. For more information, see
  [Run an AI Model](../ai/ai-model-inference.md#flink-sql-ai-model).

### September 11, 2024

Added capability to Confluent Cloud Console to produce messages with an associated schema.
For more information, see [Use Message Browser in Confluent Cloud](../topics/messages.md#ccloud-topic-message-browser) and this blog post:
[Producing Messages With a Schema in Confluent Cloud Console](https://www.confluent.io/blog/producing-messages-with-a-schema-in-confluent-cloud-console/).

### September 6, 2024

- Oracle Database versions 11g, 12c and 18c are deprecated. Confluent will end
  support for these versions on June 30, 2025. For more details, see
  [Oracle CDC Source Connector for Confluent Cloud Overview and Features](../connectors/cc-oracle-cdc-source/cc-oracle-cdc-source-features.md#cc-oracle-cdc-source).
- The following connectors are now generally available for your Apache KafkaÂ® clusters
  on AWS, Azure, and Google Cloud.
  - The fully-managed HTTP Source V2 connector integrates Apache KafkaÂ® with an API
    using HTTP or HTTPS and allows you to configure one or more APIs seamlessly
    with an OpenAPI/Swagger specification file. To explore a full range of
    features and get started with the connector, see [HTTP Source V2 Connector for Confluent Cloud](../connectors/cc-http-source-v2.md#cc-http-source-v2).
  - The fully-managed HTTP Sink V2 connector integrates Apache KafkaÂ® with an API
    using HTTP or HTTPS and allows you to configure up to 15 APIs seamlessly
    with an OpenAPI specification file. To explore a full range of features and
    get started with the connector, see [HTTP Sink V2 Connector for Confluent Cloud](../connectors/cc-http-sink-v2.md#cc-http-sink-v2).

### September 4, 2024

The default service quota for API keys per service account
(resource-scoped to Kafka cluster) has been increased from `10` to `100`.
For details, see [Service Quotas for API keys](../quotas/service-quotas.md#service-quotas-api-keys).

### August 23, 2024

Flink Private Networking on AWS has reached General Availability (GA) after a successful Limited Availability phase
with several customers onboarded. This release allows customers to connect to Flink over Private Link (PL) to access
Enterprise and Dedicated clusters using various AWS connectivity options such as Private Link, Transit Gateway, or
VPC Peering. Customers can now connect to Flink over PL to access Enterprise and Dedicated clusters using any type of
connectivity in AWS. Flink queries can process, join, and move data across various Dedicated clusters, enabling
customers to gain insights and create rich transformations on their private data.

### August 20, 2024

The Schema Registry cluster management (SRCM) v2 regions API and v2 clusters API is deprecated and will no longer be supported after February 2025.
Related Confluent CLI commands and Confluent Terraform Provider resources and data sources that rely on this API will
also no longer be supported.

For information on how to upgrade to SRCM API v3, Confluent CLI and Terraform upgrades, along with details on the v2
deprecation timeframes, see [Upgrade to SRCM v3 clusters and regions APIs (Deprecation of SRCM v2)](../stream-governance/packages.md#update-srcm-api-to-v3).

### August 19, 2024

Early Access to the Confluent Cloud Provider Integration is now available. You can use Provider Integration APIs
to manage provider integration configurations by mapping AWS Identity and Access Management (IAM) roles in Confluent.
Using the integration, you can create a secure access connection between source or sink resources on AWS
and Confluent Cloud for data ingestion or transfer.

For more information, see [Manage Provider Integration for Fully-Managed Connectors in Confluent Cloud](../connectors/provider-integration.md#cloud-pi-quickstart).

### August 15, 2024

[Confluent Terraform Provider v2.0.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs) (**Guides** > **Confluent Provider 2.0.0: Upgrade Guide**)
is now generally available. Version 2 supports the Always-On Governance feature
of Confluent Cloud, providing compatibility with the latest version of the Confluent Cloud
Stream Governance APIs.

- View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md).
- Learn about
  [upgrading to version 2](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)

### August 6, 2024

In continuing our efforts to provide robust security controls, changes were
made to the [Azure VNET peering configuration steps](../networking/peering/azure-peering.md#cloud-networking-peering-azure-connection) (at step 4.4).

### July 25, 2024

- Five additional Confluent Cloud metrics are now available to query directly using the
  Metrics API. For more information, see [Monitor Dedicated Clusters in Confluent Cloud](../monitoring/cluster-load-metric.md#monitor-dedicated-clusters) and [Dedicated Cluster Performance and Expansion in Confluent Cloud](../monitoring/monitor-performance.md#cloud-cluster-monitor-performance).
  - `cluster_load_percent_avg`
  - `cluster_load_percent_max`
  - `dedicated_cku_count`
  - `hot_partition_ingress`
  - `hot_partition_egress`
- Enterprise clusters are now available in the swedencentral (GÃ¤vle) region in Azure.

### July 19, 2024

The fully-managed Google Cloud Functions Gen 2 Sink connector for Confluent Cloud integrates
Apache KafkaÂ® with Google Cloud Functions. For basic information about functions,
see [Google Cloud Functions](https://cloud.google.com/functions/docs/console-quickstart). The connector consumes records
from Kafka topic(s) and executes a Google Cloud Function. The connector supports both Gen 1 and Gen 2 functions.

For more information, see [Google Cloud Functions Gen 2 Sink Connector for Confluent Cloud](../connectors/cc-google-cloud-functions-gen2-sink.md#cc-google-cloud-functions-gen2-sink).

### July 17, 2024

ksqlDB version 7.7.0-223 was released to Confluent Cloud.

### July 11, 2024

Confluent Cloud for Apache Flink now supports AWS PrivateLink Attachment on Enterprise clusters and is generally
available for production use. Flink can securely read and write data stored in
Confluent Cloud clusters that are located in private networking, with no data flowing
to the public internet.

For more information, see [Private Networking with Confluent Cloud for Apache Flink](../flink/concepts/flink-private-networking.md#flink-sql-private-networking).

---

[Client-side field level encryption (CSFLE)](../security/encrypt/csfle/overview.md#client-side-field-level-encryption),
in Limited Availability, adds support for:

* [Confluent .NET Client](https://github.com/confluentinc/confluent-kafka-dotnet)
* [Confluent Go Client](https://github.com/confluentinc/confluent-kafka-go)

For details, see [CSFLE requirements](../security/encrypt/csfle/client-side.md#csfle-requirements).

### July 8, 2024

Mutual TLS (mTLS) support for Confluent Cloud is now available as an Early Access feature.
You can use mTLS for client certificate authentication and granular access control
to Confluent Cloud Dedicated clusters.

For details, see [mTLS for Confluent Cloud](../security/authenticate/workload-identities/identity-providers/mtls/overview.md#mtls-overview).

---

The fully managed DynamoDB CDC Source connector is now available for your
Apache KafkaÂ® clusters on AWS. The connector supports the following three modes:

- `SNAPSHOT`: Only allows a one-time scan of the existing data in the source
  table(s) simultaneously.
- `CDC`: Only allows CDC with DynamoDB stream(s) without an initial snapshot
  for all streams simultaneously.
- `SNAPSHOT_CDC` (default): Allows an initial snapshot of all configured
  tables; once the snapshot is complete, starts CDC streaming using DynamoDB
  streams.

For more details, see [Amazon DynamoDB CDC Source Connector for Confluent Cloud](../connectors/cc-amazon-dynamodb-cdc-source.md#cc-amazon-dynamodb-cdc-source).

### July 3, 2024

Managing SSO access to the Confluent Support Portal is now in General Availability.
For more information, see [Manage Trusted Domains on Confluent Cloud](../security/authenticate/user-identities/user-idps/sso/trusted-domains.md#manage-trusted-domains).

### June 24, 2024

- Support for Avro unions in Confluent Cloud for Apache Flink has been added. Avro unions are used
  to define multiple event types in one topic. Previously, you could not read
  or write to tables that were backed by a schema using Avro unions. When Avro
  unions are used, the schema is inferred as a ROW type, similar to how the
  the feature is supported for JSON and Protobuf.
- The [JSON_QUERY](../flink/reference/functions/json-functions.md#flink-sql-json-query-function) function now supports returning
  arrays. JSON_QUERY is one of the Flink JSON functions that returns objects,
  arrays, and other non-scalar types. You can now specify the JSON_QUERY return
  type to be ARRAY<STRING>, instead of STRING.
- The Kafka Connect Google BigQuery Sink V2 connector for Confluent Cloud now
  supports upsert and delete functionality for ingested data. With the upsert
  feature, you can insert new data, or update existing data with matching keys.
  The upsert and delete functionality adds the option to insert new data, update existing
  matching key data, or remove data with matching keys for tombstone records.
  For more details, see
  [Google BigQuery Sink V2 Connector for Confluent Cloud](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-storage-api-sink).

### June 17, 2024

API key management in the Confluent Cloud Console is simplified and improved. In the
**API keys** section, you can create API keys using resource scopes for
clusters (Kafka, Schema Registry, and ksqlDB), Flink regions, and cloud resource management.
For more information, see [Resource scopes](../security/authenticate/workload-identities/service-accounts/api-keys/overview.md#cloud-api-key-resource-scopes) and [Manage API Keys in Confluent Cloud](../security/authenticate/workload-identities/service-accounts/api-keys/manage-api-keys.md#manage-api-keys).

### June 11, 2024

Custom offset management for fully-managed connectors is
generally available. Use custom offsets to manage the offsets
of supported connectors. This includes use cases
like migrating from self-managed connectors to fully-managed
connectors. For more information, see [Manage Offsets for Fully-Managed Connectors in Confluent Cloud](../connectors/offsets.md#connect-custom-offsets).

### June 10, 2024

Terraform support for the `freight` Kafka cluster type in the
[confluent_kafka_cluster resource](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_cluster) is available in Early Access.

### June 6, 2024

ksqlDB version 7.7.0-184 was released to Confluent Cloud.

### June 3, 2024

A bug was fixed that occurred during creation of a Flink API key. Previously,
only 10 service accounts were shown in the dropdown when you selected a
service account. Now you can now see all service accounts in the dropdown.

### May 30, 2024

The minimum value for `max.compaction.lag.ms` has changed from 7 days (`604800000`) to 6 hours
(`21600000`). For more information, see [max.compaction.lag.ms](../topics/manage.md#topics-max-compaction-lag-ms).

### May 29, 2024

On **June 6, 2024**, the Letâs Encrypt R3 intermediate certificate expires. If you
pinned to this expiring intermediate certificate, you should remove any intermediate
certificate and replace it with the root certificate. For more information, see:

* [Manage TLS certificates](../client-apps/client-configs.md#manage-tls-certificates)
* [New Intermediate TLS Certificates rollout starting June 6th](https://support.confluent.io/hc/en-us/articles/26845972991380-New-Intermediate-TLS-Certificates-rollout-starting-June-6th)

### May 24, 2024

The default service quota for [SSO group mappings per organization](../quotas/service-quotas.md#ccloud-resource-limits-organization)
has been increased from `12` to `100`.

The new [Gateway scope](../quotas/service-quotas.md#ccloud-resource-limits-gateway) service quota limits
for gateways connecting to Confluent Cloud using a Private Link connection are now available.
The new service quota limits include âAccess points per gatewayâ (default is `10`)
and âDNS records per gatewayâ (default is `20`).

Principals that have the FlinkDeveloper role can now delete Flink statements.

### May 23, 2024

The default retention for Flink statements in terminal states (COMPLETED, FAILED, STOPPED)
has now been changed from 7 days to 30 days.

### May 22, 2024

Users are no longer required to specify the principal manually when submitting
Flink statements to the Statements API by using the Flink API key. The principal
field is now optional and auto-assigned, so the system infers the principal
associated with the Flink API key and assigns it automatically to the request.
This behavior is the same for all types of supported authorization.

### May 22, 2024

The fully-managed Amazon S3 Source connector now supports CSV and Parquet
input data formats. For more details, see [Amazon S3 Source Connector for Confluent Cloud](../connectors/cc-s3-source.md#cc-s3-connect-source).

### May 17, 2024

The default service quota for [RBAC role bindings in a Dedicated Kafka cluster](../quotas/service-quotas.md#ccloud-resource-limits-kafka-cluster)
has been increased from `5000` to `25000`.

### May 15, 2024

Three additional Flink compute pool metrics (`current_cfus`, `cfu_limit`,
and `cfu_minutes_consumed`) are now available to query directly by using the
Metrics API and Datadog.

### May 10, 2024

- You can now run a Flink SQL statement without stopping the currently
  running statement explicitly. Previously, an editor cell was completely
  locked while a statement was running. To run the next statement in the same
  cell, the running statement had to be stopped explicitly. This behavior has
  been improved so an editor cell is locked only while the statement is
  starting. As soon as the statement is running, the editor is unlocked and
  editable, and you can submit the next statement immediately.
- Improved Flink compute pool deletion behavior so actively running statements
  stop automatically when a compute pool is deleted.
- Statement sets are now supported within SQL editor cells in workspaces.
- Improved synchronization between Flink statement status in an editor cell and the
  Flink statementâs details panel to prevent out-of-sync issues.
- The catalog browser in workspaces is now horizontally resizable, making long
  topic names more accessible.

### May 9, 2024

Confluent Cloud now supports outbound Azure Private Link connections using Egress Access
Points. Egress Access Points enable fully managed Confluent connectors to access
services from Azure Private Link Service providers such as Microsoft, MongoDB,
Snowflake, and others.

Egress Access Points are currently supported for Dedicated Clusters with Azure
Private Link or AWS PrivateLink networking.

For details, see [Azure Egress Access Points for Dedicated Clusters](../networking/azure-egress-privatelink.md#cloud-networking-privatelink-azure-egress).

### April 29, 2024

Confluent Cloud for Apache Flink is now available in AWS (ap-south-1), Azure (centralindia)
and Google Cloud (asia-south1, asia-south2).

### April 17, 2024

Enterprise Kafka clusters now support one eCKU as a minimum instead of two. For more
information, see [eCKU/CKU comparison](../clusters/cluster-types.md#e-cku-details).

### April 11, 2024

Client-side field level encryption (CSFLE) is now available in Limited Availability
as a fully supported feature recommended for production use. CSFLE provides an
additional layer of security on Confluent Cloud for protection of sensitive data,
safeguarding data in motion throughout its lifecycle across producers and
consumers. For more information, see [Protect Sensitive Data Using Client-Side Field Level Encryption on Confluent Cloud](../security/encrypt/csfle/overview.md#client-side-field-level-encryption).

To be considered for access before General Availability, contact
[Confluent Support](https://support.confluent.io).

---

Enterprise clusters are available in the following Microsoft Azure regions:

- australiaeast
- brazilsouth
- canadacentral
- centralus
- eastasia
- eastus
- eastus2
- germanywestcentral
- northeurope
- southeastasia
- uksouth
- westeurope

For details about Enterprise clusters, see [Cluster types](../clusters/cluster-types.md#enterprise-cluster).

### April 10, 2024

Default user permissions now apply to all SSO user accounts in new SSO-enabled
organizations. A new default group mapping binds all SSO user accounts to the
DataDiscovery and FlinkDeveloper roles, providing permissions to access Confluent Cloud
resources, including Flink and Data Portal. Existing SSO-enabled organizations
can opt-in. For more information, see [Default user permissions](../security/authenticate/user-identities/user-accounts/manage-sso-user-accounts.md#default-user-permissions).

The fully-managed OpenSearch Sink connector is now generally available for your
Apache KafkaÂ® clusters on AWS, Azure, and Google Cloud. The connector provides a simple and
secure way to stream data from Confluent Cloud to OpenSearch and supports both AWS and
OSS OpenSearch. For more details, see [OpenSearch Sink Connector for Confluent Cloud](../connectors/cc-opensearch-sink.md#cc-opensearch-sink).

### April 5, 2024

Service quota default for [User accounts (active and invited) per organization](../quotas/service-quotas.md#ccloud-resource-limits-organization)
is now `1,000` (increased from `500`).

[OAuth 2.0 authentication using Confluent Security Token Service (STS) access
tokens](../security/authenticate/workload-identities/identity-providers/oauth/access-rest-apis-sts.md#use-confluent-sts-with-ccloud-apis) (`confluent-sts-access-token`) for
authorization to access Confluent Cloud resources is now available for all control plane
Confluent Cloud APIs. Support is added for `notifications/v1`, `sd/v1`, `service-quota`,
`srcm/v2`, `billing/v1`, `cdx/v1`, `partner/v2`, `byok/v1`, `metrics`,
`flink`, and `kafka-quota/v1`. For more information, see the [API Reference for Confluent Cloud](../api.md#cloud-apis).

### April 3, 2024

Service quotas for RBAC role bindings have been updated:

- [Organization scope](../quotas/service-quotas.md#ccloud-resource-limits-organization) includes a
  new quota, RBAC role bindings (total), and the updated quota, RBAC role bindings
  (with Kafka permissions), no longer limiting role bindings without Kafka permissions.
- **Schema Registry Cluster scope** has been removed, and the RBAC role bindings
  are incorporated in the new quota for RBAC role bindings (total) at the
  Organization scope.
- [Kafka Cluster scope](../quotas/service-quotas.md#ccloud-resource-limits-kafka-cluster) includes
  an updated quota, RBAC role bindings (with Kafka permissions), which no longer
  limits role bindings without Kafka permissions.
- All RBAC role binding quotas now provide usage data.

### March 29, 2024

Confluent Cloud now supports outbound AWS PrivateLink connections using Egress Access
Points. Egress Access Points enable fully managed Confluent connectors to access
services from AWS PrivateLink Service providers such as AWS, MongoDB,
Snowflake, and others.

Egress Access Points are currently supported for Dedicated Clusters with AWS
PrivateLink networking.

For details, see [AWS Egress Access Points for Dedicated Clusters](../networking/aws-egress-privatelink.md#cloud-networking-privatelink-aws-egress).

### March 28, 2024

Managing SSO access to the Confluent Support Portal is now in Early Access.
For more information, see [Manage Trusted Domains on Confluent Cloud](../security/authenticate/user-identities/user-idps/sso/trusted-domains.md#manage-trusted-domains).

### March 25, 2024

The throughput cluster limits and capacity guidelines for Dedicated and Enterprise Kafka clusters have
changed.

- For Enterprise clusters, capacity guidance for ingress is 60 megabytes per second (MBps) per CKU with an upper limit of 300 megabytes
  and egress is 180 MBps per CKU with a 900 megabyte limit. Per partitions limits for Enterprise are now 6 MBps
  for ingress and 18 MBps for egress.
- For Dedicated clusters, capacity guidance for ingress is 60 MBps per CKU with an upper limit of 9,120 megabytes
  and egress is 180 MBps per CKU with a 27,360 megabyte limit. Per partitions limits for Dedicated are now 12 MBps
  for ingress and 36 MBps for egress.

For more information, see [eCKU/CKU comparison](../clusters/cluster-types.md#enterprise-cku-guidance), [Fixed limits and recommended guidelines](../clusters/cluster-types.md#cku-details), and [Dimensions with recommended guidelines](../clusters/cluster-types.md#guideline).

### March 19, 2024

Confluent Cloud for Apache Flink is promoted to General Availability.

[Auditable event methods for Apache Flink](../monitoring/audit-logging/event-methods/flink.md#event-methods-flink) and
[Auditable event methods for Flink authentication and authorization](../monitoring/audit-logging/event-methods/flink-authn-authz.md#flink-authentication-authorization-auditable-events)
are promoted to General Availability. These auditable event methods are triggered
by operations on Flink authentication, authorization, regions, compute pools,
workspaces, and statements.

### March 5, 2024

Stream Lineage for Flink is now available providing complete end-to-end visibility
for Flink SQL statements.

### March 4, 2024

A new predefined RBAC role, [BillingAdmin](../security/access-control/rbac/predefined-rbac-roles.md#billingadmin-role), is now generally
available. This role allows users to view and manage billing information for an
organization. For more information, see [BillingAdmin](../security/access-control/rbac/predefined-rbac-roles.md#billingadmin-role).

[IP Filtering](../security/access-control/ip-filtering/overview.md#ip-filtering) is now generally available for production use.
Use IP Filtering to enhance the security of your Confluent Cloud resources by restricting
access to trusted network locations. This extra layer of access control protects
against compromised credentials being used to manage Confluent Cloud from unauthorized
IP addresses.

### February 29, 2024

RBAC role bindings usage data is now available for the following scopes:
[Organization](../quotas/service-quotas.md#ccloud-resource-limits-organization) and
[Kafka cluster](../quotas/service-quotas.md#ccloud-resource-limits-kafka-cluster). For details about
using the Quotas API to view your usage data, see
[Service Quotas API for Confluent Cloud resources](../quotas/quotas.md#cc-quotas).

### February 22, 2024

Confluent Cloud for Apache Flink is now available for preview in Google Cloud (asia-southeast1,
australia-southeast1, europe-west1, europe-west3, us-central1, us-east1,
us-east4, and us-west4).

### February 21, 2024

Confluent Cloud now supports resolving private DNS names from a DNS resolver
within your own VPC or VNet via DNS forwarding. This feature enables fully
managed connectors to access endpoints using private DNS zones.

DNS forwarding is supported for AWS VPC peering, AWS Transit Gateway
connection, or Azure VNet peering in Confluent Cloud.

For details, see [DNS forwarding for AWS Peering](../networking/peering/aws-peering.md#dns-forwarding-aws-peering), [DNS forwarding for AWS Transit Gateway](../networking/aws-transit-gateway.md#dns-forwarding-aws-tgw), and [DNS for Azure Peering](../networking/peering/azure-peering.md#dns-forwarding-azure-peering).

### February 16, 2024

Early Access is now available for the [confluent-kafka-javascript client](https://github.com/confluentinc/confluent-kafka-javascript), a
librdkafka-based client with APIs that are compatible with the KafkaJS and
node-rdkafka libraries. For early access, only basic produce and consume
functionality is available, along with the ability to create and delete topics.
For more information, see the [Introduction to
Confluent-Kafka-JavaScript](https://github.com/confluentinc/confluent-kafka-javascript/blob/dev_early_access_development_branch/INTRODUCTION.md).
For migrating existing code, see the [KafkaJS Migration Guide](https://github.com/confluentinc/confluent-kafka-javascript/blob/dev_early_access_development_branch/MIGRATION.md#kafkajs).

### January 12, 2024

- Terraform support for Flink SQL statements is now available. Refer to
  [this tutorial](../flink/operate-and-deploy/deploy-flink-sql-statement.md#flink-deploy-sql-statement) for a complete end-to-end
  CI/CD example of deploying a Flink SQL statement on Confluent Cloud for Apache Flink.
- Flink is now available in preview in Azure (eastus, eastus2, westeurope,
  southeastasia, westus2) and 4 additional AWS regions (us-west-2,
  ap-southeast-1, eu-west-2, ap-southeast-2).
- Several Flink [metrics](../monitoring/metrics-api.md#metrics-api-records-a-flink-sql-statement-has-received)
  are now available to query directly via the Metrics API, Confluent Cloud Console,
  and Datadog.

### January 10, 2024

The connection count guideline for Dedicated Kafka clusters has been raised from 12,000 per CKU to 18,000 per CKU.
For more information, see [Fixed limits and recommended guidelines](../clusters/cluster-types.md#cku-details) and [Dimensions with recommended guidelines](../clusters/cluster-types.md#guideline).

## 2023 Releases

### December 15, 2023

- Networking-related commands are now available in the Confluent Cloud CLI. Refer to
  the topics under [Manage Networking on Confluent Cloud](../networking/overview.md#cloud-networking) for the CLI commands to perform
  specific networking tasks.
- [Fully-managed Snowflake Sink connector](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink) version
  2.1.2 is now available. Version 2.1.2 supports Snowflake schematization
  (`snowflake.enable.schematization`). When set to `TRUE` the connector
  provides schema detection and evolution when using [Snowpipe Streaming for
  Kafka](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-kafka).

### December 14, 2023

[Self-managed encryption keys on Azure](../security/encrypt/byok/byok-azure.md#byok-encrypted-clusters-azure) now
include support for FIPS 140-2 Level 2 compliance on Confluent Cloud Dedicated clusters
when using HSM-protected keys with Azure Key Vault.

### December 13, 2023

Service quota on RBAC role bindings for a Schema Registry cluster updated:

- Schema Registry cluster scope added, with the RBAC role bindings quota for each
  Schema Registry cluster now independent of the âorganizations + environmentsâ RBAC role bindings quota.
- RBAC role bindings now enforced per Schema Registry cluster with default quota of 5000.

### December 6, 2023

[IP Filtering](../security/access-control/ip-filtering/overview.md#ip-filtering) is available for production use in Limited
Availability. Use IP Filtering to enhance the security of your Confluent Cloud resources
by restricting access to trusted network locations. This extra layer of access control
protects against compromised credentials being used to manage Confluent Cloud from unauthorized
IP addresses. To get access before General Availability, contact
[Confluent Support](https://support.confluent.io).

### December 4, 2023

[Just-in-time (JIT) user provisioning](../security/authenticate/user-identities/user-idps/sso/jit-user-provisioning.md#jit-user-provisioning) and
[group mapping](../security/authenticate/user-identities/user-idps/sso/group-mapping/overview.md#group-mapping) are promoted to General Availability.
JIT user provisioning automatically creates Confluent Cloud user accounts,
then uses group mapping to grant Confluent Cloud RBAC permissions based on group
memberships in your SSO identity provider.

### December 1, 2023

- You can now create [custom connectors](../connectors/bring-your-connector/overview.md#cc-bring-your-connector) in any
  [AWS region](../clusters/regions.md#providers-regions) supported by Confluent Cloud.
- Confluent Cloud Console topic message search improvements. Use message browser to view messages
  from all partitions, even if you are not actively producing to a given partition. For more
  information, see [Use Message Browser in Confluent Cloud](../topics/messages.md#ccloud-topic-message-browser).

### November 17, 2023

The fully-managed BigQuery Sink V2 connector is available for your Apache KafkaÂ®
clusters on Google Cloud. The connector supports the Google Cloud [BigQuery Storage Write API](https://cloud.google.com/bigquery/docs/write-api) for data ingestion. Using
the BigQuery Storage Write API may provide a [cost-benefit](https://cloud.google.com/bigquery/pricing?hl=en#data_ingestion_pricing) for
your BigQuery project. For more information, see [Google BigQuery Sink V2 Connector for Confluent Cloud](../connectors/cc-gcp-bigquery-storage-sink.md#cc-gcp-bigquery-storage-api-sink).

### October 12, 2023

Enterprise clusters are now available in the ap-south-1 (Mumbai) region in AWS.

### October 6, 2023

- The new resource metadata access option is generally available.

  The resource metadata access option enables you to connect to the Kafka
  clusters with private networking to view resources. Without the need to set up
  a proxy or reverse SSH channel, the following features are enabled when you
  turn on the option in your private network:
  - Topics metadata views, specifically names, and configuration
  - Stream Lineage
  - Metrics and consumer lag information for topics

  You can toggle the option at the cluster level or at the organization level as
  the OrganizationAdmin role.

  For details, see [Enable or disable the Resource metadata access option](../networking/ccloud-console-access.md#ccloud-console-with-resource-management-access).

### September 26, 2023

A new Kafka cluster type, Enterprise, is generally available on AWS. Enterprise clusters are designed for
production-ready functionality that requires private endpoint networking capabilities.

Enterprise clusters are available over AWS PrivateLink connections in the following regions in AWS, with
rollouts to additional regions shortly following:

- us-east-1 (N. Virginia)
- us-east-2 (Ohio)
- us-west-2 (Oregon)
- eu-west-1 (Ireland)
- eu-central-1 (Frankfurt)
- ap-southeast-2 (Sydney)
- ap-southeast-1 (Singapore)
- af-south-1 (Cape Town)

For details about the Enterprise cluster, see [Cluster types](../clusters/cluster-types.md#enterprise-cluster).

Flink SQL is available for Open Preview. For more information, see
[Stream Processing with Confluent Cloud for Apache Flink](../flink/overview.md#ccloud-flink).

### September 11, 2023

- [Auditable event methods for custom connector plugins](../monitoring/audit-logging/event-methods/custom-connector-plugin.md#event-methods-custom-connector-plugin) is
  promoted to General Availability. The auditable event methods track operations
  on custom connector plugins used with custom connectors.

### September 8, 2023

- Support for `/27` CIDR blocks in AWS Transit Gateway Confluent Cloud networks is
  in Limited Availability to a subset of  Confluent customers.

  You can create Confluent Cloud networks with AWS Transit Gateway in the Confluent Cloud
  console, REST API, or [Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/1.21.0). To
  learn more, see the [Confluent Cloud network CIDR blocks and block size for peering and Transit Gateway](../networking/ccloud-network/aws.md#cidr-block-size) section in
  [Create Confluent Cloud Network on AWS](../networking/ccloud-network/aws.md#create-ccloud-network-aws).

### August 1, 2023

- Two new RBAC roles, AccountAdmin and ResourceKeyAdmin, are promoted to General
  Availability.
  - [AccountAdmin](../security/access-control/rbac/predefined-rbac-roles.md#accountadmin-role) - Manage user and service accounts across the
    organization.
  - [ResourceKeyAdmin](../security/access-control/rbac/predefined-rbac-roles.md#resourcekeyadmin-role) - Manage API keys for resources (Kafka, Schema Registry, and
    ksqlDB) across the organization. No Cloud API key management.
- [Just-in-time (JIT) user provisioning](../security/authenticate/user-identities/user-idps/sso/jit-user-provisioning.md#jit-user-provisioning) automatically
  creates Confluent Cloud user accounts, then uses [group mapping](../security/authenticate/user-identities/user-idps/sso/group-mapping/overview.md#group-mapping)
  to grant Confluent Cloud RBAC permissions based on group memberships in your SSO identity
  provider. Both features are now available for **Early Access**. To be considered
  for access before General Availability, contact Confluent Support.

### July 27, 2023

- Use OAuth to authenticate a cluster link with source Confluent Cloud, Confluent Platform, or Apache KafkaÂ® clusters,
  as described under [OAuth](../multi-cloud/cluster-linking/security-cloud.md#cloud-cluster-linking-oauth) in the Cluster Linking documentation.

### July 14, 2023

- Use the [Custom Connector](../connectors/bring-your-connector/overview.md#cc-bring-your-connector) Logs UI to view
  detailed log messages for custom connectors. To learn more, see
  [View from logs tab](../connectors/bring-your-connector/custom-connector-manage.md#cc-byoc-view-the-log-stack-trace).
- Cluster links can now be created in bidirectional mode for Disaster Recovery.
  To learn more, see [Bidirectional mode](../multi-cloud/cluster-linking/cluster-links-cc.md#bidirectional-mode-cluster-linking) in the Confluent Cloud Cluster Linking configuration documentation.
- Cluster Linking mirror topics can now begin replication from the latest
  message, thereby leaving behind historical events, or from a specific timestamp using
  the cluster link configuration `mirror.start.offset.spec`.
  To learn more, see [mirror.start.offset.spec](../multi-cloud/cluster-linking/cluster-links-cc.md#mirror-start-offset-spec).

### July 12, 2023

Use the Confluent Security Token Service (Confluent STS) to provide trusted
users or services with temporary security credentials that can access
Confluent Cloud resources without requiring them to have a Confluent Cloud account.
Documentation is now available at [Use Confluent Security Token Service (STS) tokens on Confluent Cloud](../security/authenticate/workload-identities/identity-providers/oauth/access-rest-apis-sts.md#use-confluent-sts-with-ccloud-apis).

### July 7, 2023

Two new RBAC roles, AccountAdmin and ResourceKeyAdmin, are now in Limited
Availability to a subset of Confluent customers.

* [AccountAdmin](../security/access-control/rbac/predefined-rbac-roles.md#accountadmin-role) - Manage user and service accounts across the
  organization.
* [ResourceKeyAdmin](../security/access-control/rbac/predefined-rbac-roles.md#resourcekeyadmin-role) - Manage API keys for resources (Kafka, Schema Registry, and
  ksqlDB) across the organization. No Cloud API key management.

To be considered for access before General Availability, contact Confluent Support.

### June 22, 2023

Cluster Linking is now available between Private Confluent Cloud [Dedicated
clusters](../clusters/cluster-types.md#dedicated-cluster) in AWS PrivateLink.

To learn more, see [(Legacy) Cluster Linking between AWS PrivateLink Confluent Cloud clusters](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-aws-privatelink).

### June 22, 2023

[ksqlDB 0.29.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0290-2023-06-22) is now available in Confluent Cloud.

- New functions: `LOG`, `POWER`, `CBRT`, `TRUNC`, `CORRELATION`
- UDAFs with multiple/variadic args and support for four- and five-column arguments to UDAFs
- Variadic `TOPK` that can select other columns
- Improved syntax error messages
- Support for JSON arrays

### June 5, 2023

The managed Snowflake Sink connector with support for the [Snowpipe Streaming
API](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-kafka)
is available for public preview. For more information, see
[Snowflake Sink Connector for Confluent Cloud](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink).

### May 16, 2023

The managed AlloyDB Sink connector is available for your Kafka clusters on Google Cloud.
The AlloyDB Sink connector is a fully-managed PostgreSQL-compatible database service. For
more information, see [AlloyDB Sink Connector for Confluent Cloud](../connectors/cc-alloydb-sink.md#cc-alloydb-sink).

### May 12, 2023

[Custom Connector](../connectors/bring-your-connector/overview.md#cc-bring-your-connector) support is available in
Confluent Cloud for certain AWS regions. Custom Connectors offer a fully-managed
Connect infrastructure service in Confluent Cloud. Users can upload a
Kafka Connect-based plugin to Confluent Cloud and create connectors based on that
plugin. While customers manage the connectors, Confluent manages the underlying
Connect infrastructure in Confluent Cloud.

### May 10, 2023

[Stream Sharing](../stream-sharing/index.md#cloud-data-sharing) is now GA. Use Stream Sharing to exchange data between multiple organizations at the
topic level. For more information, see [Share Data with Stream Sharing from Confluent Cloud](../stream-sharing/index.md#cloud-data-sharing).

### April 28, 2023

[Costs API](https://docs.confluent.io/cloud/current/api.html#tag/Costs-(billingv1)) is now GA. Use the Cost API to access your costs for a specific range of dates.
For more information, see [View or download invoices](../billing/overview.md#view-invoice).

### April 27, 2023

Cluster Linking is now available from any Private Confluent Cloud [Dedicated](../clusters/cluster-types.md#dedicated-cluster) cluster to a Public-Dedicated Confluent Cloud cluster.
To learn more, see [Private to public Cluster Linking](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-private-to-public).

### April 24, 2023

Single Sign-on (SSO) adds support for SAML metadata files. You can now upload a
SAML metadata file obtained from your identity provider to quickly enable SSO
or update settings while eliminating the risks of manual entry. For more
information, see [Use the SAML metadata file for SSO configuration](../security/authenticate/user-identities/user-idps/sso/enable-sso.md#saml-metadata-for-sso-configuration).

### April 21, 2023

The Cluster Linking metric `io.confluent.kafka.server/cluster_active_link_count`, which indicates the number of active links on a cluster, is DEPRECATED and will be removed in a future release.
To learn more, see [Monitor Metrics for Cluster Linking on Confluent Cloud](../multi-cloud/cluster-linking/metrics-cc.md#metrics-cc).

### April 12, 2023

Audit log support for Notifications Service is now generally available. The
auditable event methods track operations on notification types, integrations,
and subscriptions. To learn more, see [Notifications Service Auditable Event Methods on Confluent Cloud](../monitoring/audit-logging/event-methods/notification-service.md#organization-notification-service).

### April 3, 2023

Error reporting is available for the [Google Cloud BigQuery Sink [Deprecated] Connector for Confluent Cloud](../connectors/cc-gcp-bigquery-sink.md#cc-gcp-bigquery-sink). For additional
details, see [KIP-610](https://cwiki.apache.org/confluence/display/KAFKA/KIP-610%3A+Error+Reporting+in+Sink+Connectors).

### March 31, 2023

Support for `/27` CIDR blocks in VPC Peering Confluent Cloud networks on AWS
is a fully supported offering in Limited Availability to a subset of
Confluent customers. To learn more, see the [Confluent Cloud network CIDR blocks and block size for peering and Transit Gateway](../networking/ccloud-network/aws.md#cidr-block-size) section
in [Create Confluent Cloud Network on AWS](../networking/ccloud-network/aws.md#create-ccloud-network-aws).

### March 29, 2023

Support for Resource ID (`resourceId`) in access control lists (ACLs) is currently
rolling out to Confluent Cloud organizations. The non-breaking changes enable resource
IDs (`resourceId`) for Kafka ACLs in Confluent Cloud. For more information,
see [ACL operation details](../security/access-control/acls/operations.md#acl-operation-details).

### March 27, 2023

Authentication protections have been added to Confluent Cloud to prevent
unauthorized access to local user accounts. For more information, see
[Security Protections for Authentication on Confluent Cloud](../security/authenticate/user-identities/user-accounts/authentication-protections.md#authentication-protections).

### March 24, 2023

OAuth authentication support for Confluent Cloud APIs is promoted to General Availability (GA).
This release includes the following enhancements:

- Support for OAuth on APIs for managing Confluent Cloud (an authentication
  alternative to Cloud API keys)
- Introduction of a new Secure Token Service (STS) that enables exchanging a
  third-party token for a Confluent STS token.

To learn more, see [Authentication](https://docs.confluent.io/cloud/current/api.html#section/Authentication)
in the Confluent Cloud APIs documentation.

### March 10, 2023

Audit log support for authentication and authorization of Schema Registry and Stream
Catalog actions are now available. To learn more, see
[Schema Registry Authentication and Authorization Auditable Event Methods on Confluent Cloud](../monitoring/audit-logging/event-methods/sr-authn-authz.md#sr-authentication-authorization-auditable-events).

### March 9, 2023

Static egress IP addresses for Azure are generally available (GA). Static egress
IP addresses are now supported on all three major cloud platforms. Static egress
IP addresses are public IP addresses associated with Confluent Cloud that are used to
communicate with external resources (such as data sources and sinks for managed
connectors) over the public internet. To learn more, see
[Use Public Egress IP Addresses on Confluent Cloud for Connectors and Cluster Linking](../networking/static-egress-ip-addresses.md#static-egress-ip-addresses) and [Public Egress IP Addresses for Confluent Cloud Connectors](../connectors/static-egress-ip.md#cc-static-egress-ips).

### February 28, 2023

Private DNS resolution is promoted to General Availability for:

- [Azure Private Link](../networking/private-links/azure-privatelink.md#dns-resolution-options-azure)
- [Google Cloud Private Service Connect](../networking/private-links/gcp-private-service-connect.md#dns-resolution-options-gcp)

Enable private DNS resolution to fully resolve Confluent endpoints within your
private DNS zone without requiring external resolution to the Confluent Global
DNS Resolver (GLB).

### February 24, 2023

[Keys (byok/v1) API](https://docs.confluent.io/cloud/current/api.html#tag/Keys-(byokv1))
is available in [Open Preview](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)
for Confluent Cloud on AWS and Azure. Use the Keys API to include self-managed encryption keys (aka BYOK)
as part of your cluster creation workflow (including the ability to build policy profiles).

---

Confluent Cloud Console now uses the [Kafka REST API](/cloud/current/api.html#tag/Cluster-(v3)) and
the [Metrics API](https://api.telemetry.confluent.cloud/docs) instead of the legacy API.
While most of Confluent Cloud remains unchanged, Consumer Lag in Cloud Console will no longer
display offset information, instead focusing only on the lag to make it more actionable for
developers and operators. This change rolls out across organizations over the next few weeks.

### February 23, 2023

[Self-managed Encryption Keys for Azure](../security/encrypt/byok/byok-azure.md#byok-encrypted-clusters-azure) support
is promoted to General Availability (GA). You can now use your own encryption keys in
Azure Key Vault to encrypt data at rest on Confluent Cloud Dedicated Clusters in Azure.

### February 15, 2023

[Stream Catalog RBAC](../stream-governance/stream-catalog.md#stream-catalog-rbac) is now General Available (GA).
As part of this, we have released two new roles [DataSteward](../security/access-control/rbac/predefined-rbac-roles.md#datasteward-role) and [DataDiscovery](../security/access-control/rbac/predefined-rbac-roles.md#datadiscovery-role)
which allow management of access to metadata associated with entities such as topics and schemas.
As RBAC will be enforced on the ability to attach tags, business metadata, and searching using Stream Catalog APIs,
cluster and resource level roles such as CloudClusterAdmin, Operator (Resource level), ResourceOwner, DeveloperRead
and DeveloperWrite roles will not be allowed to attach tags, business metadata and search using via UI or Stream Catalog APIs.

### January 30, 2023

[Private DNS resolution](../networking/private-links/aws-privatelink.md#dns-resolution-options) for AWS PrivateLink is
promoted to General Availability. You can fully resolve Confluent endpoints
within your private DNS zone without requiring external resolution to the
Confluent Global DNS Resolver (GLB).

### January 27, 2023

Stream Designer now enables users and organizations to easily manage the entire lifecycle
of pipelines by using the Confluent CLI and the
Pipelines REST API.

## 2022 Releases

### December 19, 2022

[OAuth for Confluent Cloud](../security/authenticate/workload-identities/identity-providers/oauth/overview.md#oauth-overview) is now extended to support:

- [OAuth for Schema Registry clients](../security/authenticate/workload-identities/identity-providers/oauth/clients/java-clients.md#configure-sr-java-clients-for-oauth)
- [Manual refresh of JWKS URI](../security/authenticate/workload-identities/identity-providers/oauth/jwks-manual-refresh.md#manual-refresh-jwks-uri)
- Stream Governance APIs, including:
  - [OAuth for Schema Registry API](../sr/sr-rest-apis.md#sr-api-oauth)
  - [OAuth for Stream Catalog API](../stream-governance/stream-catalog-rest-apis.md#dg-tags-api-oauth)

### December 16, 2022

OAuth for Kafka REST APIs is now promoted to General Availability (GA). You
can now authenticate using an OAuth/OIDC identity provider to access Kafka
REST APIs. To learn more, see [Access Kafka REST APIs with an OAuth-OIDC identity provider on Confluent Cloud](../security/authenticate/workload-identities/identity-providers/oauth/access-rest-apis.md#access-kafka-apis-with-identity-provider).

---

Cluster Linking between two AWS Transit Gateway Confluent Cloud clusters in different regions is now promoted to
General Availability (GA). You can peer AWS Transit Gateways to create connectivity and use Cluster Linking
for fully-managed multi-region replication. To learn more, see [(Legacy) Cluster Linking between AWS Transit Gateway attached Confluent Cloud clusters](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-aws-tgw).

### December 13, 2022

[OAuth for Kafka](../security/authenticate/workload-identities/identity-providers/oauth/overview.md#oauth-overview) is now promoted to General
Availability (GA). Create OAuth/OIDC identity providers and use
Confluent OAuth with Kafka clients.

### December 9, 2022

- Confluent Cloud now supports role-based access control (RBAC) for Schema Registry and Schema Linking. To learn more, see the following sections:
  - [Access control (RBAC) for Confluent Cloud Schema Registry](../sr/schemas-manage.md#cloud-sr-rbac)
  - [Role-Based Access Control (RBAC) for Schema Linking](../sr/schema-linking.md#cloud-schema-linking-rbac)
  - [RBAC by component](../security/access-control/rbac/manage-role-bindings.md#cloud-rbac-resources-per-components)
- Cloud Client Quotas are now promoted to General Availability (GA) for Confluent Cloud Dedicated
  Clusters. Create Client Quotas using the Confluent Cloud Console, REST API, or
  [Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/1.21.0).

### December 8, 2022

Self-service [AWS Transit Gateway](../networking/aws-transit-gateway.md#aws-transit-gateway) is now promoted
to General Availability (GA) for Confluent Cloud networks using the Confluent Cloud Console,
REST API, or [Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/1.21.0).

### December 7, 2022

[Service quotas for RBAC role bindings](../quotas/service-quotas.md#ccloud-resource-limits) have been
added or updated to enable increases in quotas:

- Organization scope: RBAC role bindings (organization plus environments)
- Environment scope: RBAC role bindings (organization plus environments)
- Kafka cluster scope: RBAC role bindings

---

Audit log support for role-based access control (RBAC) operations and action are now available.
To learn more, see [Audit log support for |rbac-long|](../monitoring/audit-logging/event-methods/rbac.md#rbac-auditable-events).

### December 6, 2022

As a feature of , the Confluent CLI AsyncAPI tool adds the
ability to [Use AsyncAPI to Describe Topics and Schemas on Confluent Cloud Clusters](../stream-governance/async-api.md#stream-gov-async-api).

### November 28, 2022

Support for  business and topic metadata is available in the Confluent Cloud Console
and REST API. To learn more, see these topics:

- [Business metadata](../stream-governance/stream-catalog.md#data-discovery-business-metadata)
- [Example: Apply business metadata to a topic](../stream-governance/stream-catalog.md#data-discovery-topics-metadata)
- [Business metadata API examples](../stream-governance/stream-catalog-rest-apis.md#dg-business-metadata-api-examples)

### November 17, 2022

Support for the following auditable event methods have been added to
[Confluent Cloud audit logs](../monitoring/audit-logging/index.md#audit-logs-in-ccloud):

- [Kafka cluster management](../monitoring/audit-logging/event-methods/kafka-management.md#kafka-management-auditable-events)
- [OAuth/OIDC identity provider and identity pool](../monitoring/audit-logging/event-methods/identity-provider.md#org-events-identity-provider)

### November 4, 2022

To make the ksqlDB editor more accessible, you can press `Alt+Tab` in the
editor window to create a tab on a Mac.

### October 11, 2022

The [Message Browser](../topics/messages.md#ccloud-topic-message-browser) now supports Avro messages deserialization.

To learn more about schema formats, see [Formats, Serializers, and Deserializers](/platform/current/schema-registry/serdes-develop/index.html).

### October 3, 2022

- Promoted to General Availability (GA):
  - Confluent Stream Designer, a high-productivity,
    easy to use, visual designer for building, testing, running, and monitoring
    data pipelines.
  - Pipeline auditable events for Stream Designer,
    include the actions, or operations, on a data pipeline that generate auditable
    event messages when using Stream Designer.
- [Cluster Linking for Transit Gateway clusters](../multi-cloud/cluster-linking/private-networking.md#cluster-linking-aws-tgw) launched in Limited Availability.
- Notifications for account, billing, and service events can now be managed using a REST API in addition to the Cloud Console.
  You can integrate Microsoft Teams, Slack, a generic webhook or email for notifications using the API, and create
  new notification subscriptions. For more information, see [Notifications for Confluent Cloud](../monitoring/configure-notifications.md#ccloud-notifications).

### September 29, 2022

[REST APIs for Invitation](https://docs.confluent.io/cloud/current/api.html#tag/Invitations-(iamv2))
are promoted to General Availability:

- Provides programmatic management of user invitation operations, including
  creating, listing, describing, and deleting Invitations.

### August 31, 2022

[Google Cloud Private Service Connect](../networking/private-links/gcp-private-service-connect.md#private-service-connect-gc) for
Dedicated clusters on Confluent Cloud is promoted to General Availability.

### August 11, 2022

[OAuth for Confluent Cloud](../security/authenticate/workload-identities/identity-providers/oauth/overview.md#oauth-overview) is a fully supported offering
in Limited Availability to a subset of Confluent Cloud customers.

### August 2, 2022

[ksqlDB 0.28.2](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0282-2022-08-02) is now available in Confluent Cloud.
: - Enable the new EMIT FINAL implementation.
  - Support pausing and resuming persistent queries.
  - Add additional UDFs for trigonometry.

### July 21, 2022

[ksqlDB 0.27.1](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0271-2022-07-21) is now available in Confluent Cloud.
: - Handle multi-schema Protobuf/Avro topics.
  - Add ASSERT SCHEMA and ASSERT TOPIC statements to assert the existence of resources.
  - Add PROTOBUF_NOSR format for Protobuf messages without Schema Registry.
  - Enable aggregation without a GROUP BY clause.
  - Improve null handling.

### July 15, 2022

[Google Cloud Private Service Connect](../networking/private-links/gcp-private-service-connect.md#private-service-connect-gc) for
Dedicated clusters on Confluent Cloud is available in an **Early Access Program** to
a limited set of early adopters.

### June 30, 2022

Cluster Linking now supports adding a prefix to the names of mirror topics. To learn more, see,
[Prefixing Mirror Topics and Consumer Group Names](https://docs.confluent.io/cloud/current/multi-cloud/cluster-linking/mirror-topics-cc.html#prefixing-mirror-topics-and-consumer-group-names).

[Confluent Terraform Provider v1.0.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now generally available.

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md).

### June 28, 2022

[Confluent Terraform Provider v0.13.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Added support for the `kafka_api_key`, `kafka_api_secret`, `kafka_rest_endpoint`
  attributes in a provider block to make the `rest_endpoint` attribute and credentials
  block optional for `confluent_kafka_acl` and `confluent_kafka_topic` resources
  ([#37](https://github.com/confluentinc/terraform-provider-confluent/issues/37),
  [#54](https://github.com/confluentinc/terraform-provider-confluent/issues/54)).
- Added disable_wait_for_ready attribute to disable readiness check for confluent_api_key resource
  [#25](https://github.com/confluentinc/terraform-provider-confluent/issues/25),
  [#51](https://github.com/confluentinc/terraform-provider-confluent/issues/51)).
- Added support for pausing / resuming a connector by adding status attribute for
  `confluent_connector` resource.

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md).

### June 27, 2022

[Confluent Terraform Provider v0.12.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Reverted resource versioning changes introduced in `0.11.0`. For example,
  the `confluent_environment_v2` resource was renamed to `confluent_environment`.
  User feedback on versioned resources made it clear that the pain of manually
  updating the TF state file outweighs the potential benefits of deprecation
  flexibility that versioned resources could have provided. In order to avoid
  forcing users to edit their TF state files (either manually or by running
  commands like `terraform state mv`) in the future, TF state migrations will
  be handled within the Confluent Terraform Provider whenever possible.

Follow [Confluent Provider 0.12.0: Upgrade Guide](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/upgrade-guide-0.12.0)
to update your TF state and TF configuration files accordingly. Direct updates
from both `0.10.0` and `0.11.0` to `0.12.0` are supported.

### June 23, 2022

Added the `SignIn` event to organization auditable log events. For details,
see [Sign-in attempt](../monitoring/audit-logging/event-methods/organization-events.md#organization-sign-in-attempt).

### June 15, 2022

[Confluent Terraform Provider v0.11.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Renamed all resources and data sources to contain a version postfix that
  matches their API group version
  ([full list](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/upgrade-guide-0.11.0)).
- Renamed the `http_endpoint` attribute to `rest_endpoint` for the
  `confluent_kafka_cluster`, `confluent_kafka_topic`, `confluent_kafka_acl`
  resources and data sources to match the **Cluster settings** tab in
  Confluent Cloud Console, where the corresponding attribute is named the REST endpoint.
- Renamed the `api_key` and `api_secret` attributes of the provider block to
  `cloud_api_key` and `cloud_api_secret`, respectively.

### June 9, 2022

Updated the RBAC limitations about API keys for ksqlDB and Schema Registry clusters.

### June 8, 2022

[Confluent Terraform Provider v0.10.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Added new [confluent_private_link_access data source](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_private_link_access).
- Added new [confluent_peering data source](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_peering).
- Added new [confluent_role_binding data source](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_role_binding).
- Adjusted waiting time for `confluent_role_binding` resource by to avoid sync issues.
- Added more granular examples: [kafka-ops-env-admin-product-team](https://github.com/confluentinc/terraform-provider-confluent-internal/tree/master/examples/configurations/kafka-ops-env-admin-product-team) and [kafka-ops-kafka-admin-product-team](https://github.com/confluentinc/terraform-provider-confluent-internal/tree/master/examples/configurations/kafka-ops-kafka-admin-product-team).
- Added client validation for topic name for `confluent_kafka_topic`.
- Resolved 4 Dependabot alerts.
- Updated SDK for API Key Mgmt API to display more descriptive errors for `confluent_api_key`.
- Fixed importing error for `confluent_connector`.
- Fixed provisioning error for `confluent_connector` ([#43](https://github.com/confluentinc/terraform-provider-confluent/issues/43)).
- Updated docs and examples.

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md).

### May 25, 2022

[Confluent Terraform Provider v0.9.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Added new [confluent_network data source](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_network) ([#39](https://github.com/confluentinc/terraform-provider-confluent/issues/39)).
- Added `dns_domain` and `zonal_subdomains` computed attributes for `confluent_network` resource ([#40](https://github.com/confluentinc/terraform-provider-confluent/issues/40)).
- Decreased the creation time of `confluent_role_binding` resource by 4.5x ([#24](https://github.com/confluentinc/terraform-provider-confluent/issues/24)).

Bug fixes:

- Fixed provisioning error for `confluent_connector` resource ([#43](https://github.com/confluentinc/terraform-provider-confluent/issues/43)).

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md).

### May 24, 2022

Notifications for account, billing, and service events can now be managed using the Cloud Console.
Additionally, you can integrate Microsoft Teams, Slack, or a generic webhook for notifications
using the console. For more information, see [Notifications for Confluent Cloud](../monitoring/configure-notifications.md#ccloud-notifications).

### May 13, 2022

[Confluent Terraform Provider v0.8.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Added new `confluent_connector` resource ([#6](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/6)).
- Added new `confluent_organization` data source ([#20](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/20)).
- Implemented import for `confluent_api_key` resource ([#17](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/17)).

Bug fixes:

- Updated input validation for `confluent_private_link_access` and `confluent_kafka_cluster` resources ([#18](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/18)).
- Fixed minor documentation issues ([#15](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/15)).

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md).

### May 6, 2022

[Network service quotas](../quotas/service-quotas.md#ccloud-resource-limits-network) for the following
resources have increased:

- Kafka clusters: 10 (previously 5)
- Kafka cluster CKUs: 72 (previously 24)

### May 4, 2022

[REST APIs for Cloud and Kafka API keys](https://docs.confluent.io/cloud/current/api.html#tag/API-Keys-(iamv2))
are promoted to General Availability:

- Provides programmatic management of critical API key operations, including
  creating, listing, describing, updating, and deleting API keys.
- Enables organizations to build end-to-end provisioning flow using the
  [Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
  or other automation tools.

---

The [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) RBAC role has been updated with the following restrictions:

- No access to ksqlDB clusters and cannot see any information related to the ksqlDB clusters.
- No access to the Schema Registry and cannot see any information related to the Schema Registry.

### May 3, 2022

[Confluent Terraform Provider v0.7.0](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
is now available in public preview. It contains the following changes:

- Added new resources and corresponding docs:
  - `confluent_api_key` ([#4](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/4), [#17](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/17), [#25](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/25), [#41](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/41), [#66](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/66))
  - `confluent_network` ([#45](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/45))
  - `confluent_peering`
  - `confluent_private_link_access` ([#45](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/45))
- Added new data sources and corresponding docs:
  - `confluent_user` ([#61](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/61))
- Completely rewrote the [Sample Project guide](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/sample-project)
  that references 9 TF sample configurations for end-to-end workflows.
- Updated `confluent_kafka_cluster` and `confluent_environment` data sources
  to accept `display_name` as an input.
- Improved logging to simplify debugging process:
  - Started using the `tflog` [package](https://github.com/hashicorp/terraform-plugin-log/tree/main/tflog):
    now you can [enable detailed logs](https://www.terraform.io/internals/debugging)
    and use `grep` and a corresponding âlogging keyâ to find all entries related to
    a particular resource, for example, `grep "environment_id=env-9761j7" log.txt`.
  - Revised and structured logging messages to output non-sensitive attributes
    instead of unreadable references.
- Added support for [self-managed encryption keys (also known as bring-your-own-key
  (BYOK) encryption)](https://docs.confluent.io/cloud/current/clusters/byok/index.html).
  They are only available for Dedicated Kafka clusters on AWS and GCP.

Bug fixes:

- Fixed pagination issue for data sources ([#54](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/54), [#68](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/68)).
- Fixed a bug where you could âsuccessfullyâ import a non-existent resource ([#58](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/58)).
- Fixed a null pointer exception ([#53](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/53), [#55](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/55), [#67](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/67)).
- Added other minor fixes ([#57](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/57)).

Breaking changes:

- All resources and data sources have been renamed in the new
  [Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs).
  The prefix has been changed from `confluentcloud` to `confluent`. For example,
  the `confluentcloud_environment` resource was updated to `confluent_environment`.
  Follow the [Confluent Provider 0.7.0: Upgrade Guide](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/upgrade-guide-0.7.0) to update your TF state file.
- Changed `kafka_cluster` attribute type from `string` to `block` for
  `confluent_kafka_acl` and `confluent_kafka_topic` resources and data sources.
- Made `host` attribute required for `confluent_kafka_acl` resource.

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluent/blob/master/CHANGELOG.md#070-may-3-2022).

### May 3, 2022

New user session timeouts when using the Confluent Cloud Console are now promoted to
General Availability:

- Users remain signed in to the Confluent Cloud Console until no activity is detected
  for 30 minutes.
- Users remain signed in to the Confluent Cloud Console for a maximum of eight hours
  without refreshing user credentials. Users must sign in at least once every
  eight hours.

For details, see [What user session timeouts does Cloud Console require?](../faq.md#user-session-timeouts).

### April 28, 2022

[ksqlDB 0.26.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0260-2022-04-28) is now available in Confluent Cloud.
: - Add support for Stream-to-Stream and Table-to-Table right joins.
  - MIN/MAX aggregates can now be used for Time/TS/Date types.

### April 28, 2022

REST APIs for Dedicated clusters and private networking are now Generally Available,
and include the following features:

- Adds REST APIs for:
  - [Networks (networking/v1)](https://docs.confluent.io/cloud/current/api.html#tag/Networks-(networkingv1)).
  - [Clusters (cmk/v2)](https://docs.confluent.io/cloud/current/api.html#tag/Clusters-(cmkv2)).
    for Dedicated clusters in private networks.
- Adds [Confluent Cloud networks](../networking/overview.md#ccloud-network-overview)
  - Confluent Cloud networks are now first-class citizens, with independent lifecycle
    management of private dedicated clusters and networks.
  - Supports self-service provisioning of multiple Dedicated clusters,
    reducing manual effort and improving network resource utilization.
    For example, you can reuse `/16` CIDR blocks across multiple clusters
    for VPC peering.
  - Users can select zones for the Confluent Cloud network. A Confluent Cloud network is always
    multi-zone and all multi-zone clusters in it are added to the same zones.
- Adds [NetworkAdmin RBAC role](../security/access-control/rbac/predefined-rbac-roles.md#networkadmin-role) targeting network
  lifecycle management, enabling the separation of concerns between
  infrastructure and application development teams in an organization.
- Adds [audit log support for network-related auditable events](../monitoring/audit-logging/event-methods/organization-events.md#organization-events).

### April 7, 2022

[ksqlDB 0.25.1](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0251-2022-04-07) is now available in Confluent Cloud.
: - Improvements to aggregate functions to support complex types, like
    structs, arrays, and maps.
  - Support for push query continuation tokens in the Java API.
  - Better error handling for nested functions.
  - In the Java API and migrations tool, support for custom request headers
    and connector IF NOT EXISTS clauses.

### April 1, 2022

The Service Level Agreement (SLA) for Confluent Cloud now specifies a 99.99% uptime SLA
for Standard and Dedicated Kafka clusters with Multi-Zone configurations.
For details, see [Confluent Cloud SLA](https://www.confluent.io/confluent-cloud-uptime-sla).

The uptime SLAs for Single-Zone clusters remain the same; 99.5% for Basic
and 99.95% for Standard and Dedicated.

### March 30, 2022

ksqlDB Connector Management is now available in Confluent Cloud. For more details,
see [Manage Connectors With ksqlDB on Confluent Cloud](../ksqldb/ksqldb-connector-management.md#cloud-ksql-connector-management).

### March 29, 2022

New organization audit log events for management operations are promoted to
General Availability. For more details, see [Organization Auditable Event Methods on Confluent Cloud](../monitoring/audit-logging/event-methods/organization-events.md#organization-events).

### March 24, 2022

Consumer lag is now available as a metric in the Confluent Cloud Metrics API.
For more details see [Monitor Kafka Consumer Lag in Confluent Cloud](../monitoring/monitor-lag.md#cloud-monitoring-lag).

### March 22, 2022

Granular role-based access control (RBAC) for Kafka resources is promoted to General
Availability. For details, see [Role-based Access Control (RBAC) on Confluent Cloud](../security/access-control/rbac/overview.md#cloud-rbac).

Highlights:

- Adds roles for DeveloperRead (Read access), DeveloperWrite (Write access),
  DeveloperManage (Create, Delete, Change configurations), ResourceOwner (full
  access, including granting permissions) for Kafka resources to enable using
  RBAC for managing access to topics, consumer groups, and transactionalIDs.
- Adds the Operator role that enables Describe-only access at the Organization,
  Environment, and Cluster level. For details, see [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role).
- Restrict user and service accounts using RBAC and ACLs.
- User and service accounts can be granted multiple roles.
- Adds the MetricsViewer role that grants access only to metrics for specified
  user and service accounts. This role cannot access data in Kafka clusters.
- Granular RBAC for Kafka resources is only available in Standard and Dedicated
  clusters. This functionality is not available on Basic clusters.
  - Note that administrator roles are enforced on Basic clusters as usual.
- Stream Lineage views can be accessed by administrator and operator
  roles (OrganizationAdmin, EnvironmentAdmin, CloudClusterAdmin, MetricsViewer,
  and Operator). Developers cannot access.

Gaps:

- User and service accounts with DeveloperRead, DeveloperWrite, DeveloperManage,
  and ResourceOwner roles on resources within a Kafka cluster can see all of the
  metrics within that cluster. We are actively working to block this access.
- Any user with access to a resource in a cluster can see all of the consumers and
  producers of a cluster, regardless of which topic on the cluster the consumer consumes
  from. Engineering is actively working to block this access.
- Some users might receive email notifications related to Connector create operations,
  even if they are not directly related to or involved in these operations. If a user
  receives a notification email message, they cannot access the connector unless they
  are assigned the required roles. Engineering is working to resolve this issue.

### March 9, 2022

Cluster links can now be viewed on the Confluent Cloud Console in your web browser. Log on to [Confluent Cloud](https://confluent.cloud/login),
navigate to **Environments**, then click the **Cluster links** tab (next to **Environments** on the Home page).
To learn more, see [Go exploring](../multi-cloud/cluster-linking/quickstart.md#cluster-links-on-the-cloud-console) in the Quick Start Tutorial.

[Confluent Cloud Terraform Provider v0.5.0](https://registry.terraform.io/providers/confluentinc/confluentcloud/latest) is now available in public preview. It contains the following changes:

- Added support for Kafka topic configuration updates ([#11](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/11)).
- Added support for `display_name` input for `confluentcloud_environment` and `confluentcloud_service_account` data sources ([#42](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/42), [#46](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/46)).
- Fixed *Provider produced inconsistent result after apply error* when creating a lot of Kafka topics ([#40](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/40)).
- Fixed delete operation for `confluentcloud_kafka_topic` resource to avoid *400 Bad Request: Topic âfoobarâ is marked for deletion* error when recreating a lot of Kafka topics ([#50](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/50)).
- Added support for old environment IDs ([#43](https://github.com/confluentinc/terraform-provider-confluentcloud/issues/43)).

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluentcloud/blob/master/CHANGELOG.md#050-march-9-2022).

### February 22, 2022

New metrics to track all bytes sent and received over the network by Confluent Cloud are now
available in the Confluent Cloud Metrics API. These metrics have a `principal_id` label to attribute usage to
a user or service account. For more details see [Confluent Cloud Metrics](../monitoring/metrics-api.md#metrics-api).

### February 11, 2022

[ksqlDB 0.24.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0240-2022-02-11) is now available in Confluent Cloud.
: - Expose Kafka message headers to ksqlDB
  - Add utility functions for working with JSON data
  - Add ability to use an existing Schema Registry schema when creating streams and tables

### January 28, 2022

[Confluent Cloud Terraform Provider v0.4.0](https://registry.terraform.io/providers/confluentinc/confluentcloud/latest) is now available in public preview. It contains the following changes:
: - Added data sources for: `confluentcloud_environment`, `confluentcloud_kafka_cluster`, `confluentcloud_kafka_topic`, and `confluentcloud_service_account`
  - Improved readability of error messages by adding details to them
  - Resolved potential HTTP 429 errors by adding automatic retries with exponential backoff for HTTP requests
  - Added graceful handling for resources created via Terraform but deleted via Confluent Cloud Console, Confluent CLI, or Confluent Cloud APIs.
  - Fixed minor bugs and docs issues.

Breaking Changes:
: - Removed friction around manual look-up of IntegerID for Service Accounts by removing the need to use a service_account_int_id TF variable. If you are using the `confluentcloud_kafka_acl` resource you might see an input validation error after running terraform plan, which can be resolved by following [this guide](https://registry.terraform.io/providers/confluentinc/confluentcloud/latest/docs/guides/upgrade-guide-0.4.0). Updated âSample projectâ guide to reflect this change.
  - Simplified `confluentcloud_role_binding` resource creation by adding a new rbac_crn attribute for confluentcloud_kafka_cluster resource. Updated the `confluentcloud_role_binding` resource examples to reflect this simplified approach.

View the [full changelog on Github](https://github.com/confluentinc/terraform-provider-confluentcloud/blob/master/CHANGELOG.md#040-january-28-2022).

### January 19, 2022

ksqlDB now supports 1 CSU and 2 CSU deployments. For more information, see [Announcing the Confluent Q1 â22 Launch](https://www.confluent.io/blog/real-time-data-integrations-at-scale-with-confluent-q1-22-launch/#single-csu-pricing).

### January 11, 2022

[Confluent Cloud Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluentcloud/latest) is now available in public preview. You can manage the following Confluent Cloud resources:
: - Environments
  - Kafka Clusters
  - Kafka Topics
  - Kafka ACLs
  - RBAC Rolebindings
  - Service Accounts

## 2021 Releases

### December 14, 2021

[ksqlDB 0.23.1](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0231-2021-12-14) is now available in Confluent Cloud.
: - Add support for TIMESTAMP type in the WITH/TIMESTAMP property
  - Enable ROWPARTITION and ROWOFFSET pseudo columns
  - Enable GRACE period with new stream-stream joins semantics

<a id="cloud-shrink-note"></a>

### November 16, 2021

[ksqlDB 0.22.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0220-2021-11-03) is now available in Confluent Cloud.
: - Add SOURCE keyword for CREATE STREAM and CREATE TABLE statements
  - Improve pull query performance for primary key range scans
  - Improve push query performance

### October 7, 2021

For Dedicated clusters:

- New [Cluster Shrink capabilities](../clusters/resize.md#cloud-cluster-shrink) and the related [Cluster Load
  metric](../monitoring/cluster-load-metric.md#cloud-cluster-load-metric) are being incrementally released to customers using Dedicated
  Kafka clusters starting today.
  The roll out is gradual to help ensure a consistent experience across cloud providers and regions.

  These features are expected to be available for all customers using Dedicated clusters by mid-November.
  For more information on using the Cluster Load metric, see [Dedicated Cluster Performance and Expansion in Confluent Cloud](../monitoring/monitor-performance.md#cloud-cluster-monitor-performance).

### September 16, 2021

[ksqlDB 0.21.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0210-2021-09-15) is now available in Confluent Cloud.
: - Support for expressions in foreign-key table-table joins
  - BYTES data type to represent byte arrays
  - ARRAY_CONCAT function added

### September 14, 2021

[Stream Governance](../stream-governance/index.md#cloud-dg) is now available on Confluent Cloud including:

- [Stream Catalog on Confluent Cloud: User Guide to Manage Tags and Metadata](../stream-governance/stream-catalog.md#cloud-stream-catalog)
- [Track Data with Stream Lineage on Confluent Cloud](../stream-governance/stream-lineage.md#cloud-stream-lineage)
- [Stream quality](../stream-governance/index.md#cloud-stream-quality)

[Schema Linking](../sr/schema-linking.md#schema-linking) is introduced in preview.

Fully-managed Confluent Cloud Azure Cognitive Search Sink GA
: This feature is launched for your Kafka clusters on Azure. For more information,
  see [Azure Cognitive Search Sink Connector for Confluent Cloud](../connectors/cc-azure-cognitive-search-sink.md#cc-azure-cognitive-search-sink).

### September 9, 2021

Fully-managed Confluent Cloud Azure Synapse Analytics Search Sink GA
: This feature is launched for your Kafka clusters on Azure. For more information,
  see [Azure Synapse Analytics Sink Connector for Confluent Cloud](../connectors/cc-azure-synapse-analytics-sink.md#cc-azure-synapse-analytics-sink).

### September 8, 2021

Fully-managed Confluent Cloud Salesforce Platform Events Sink GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Salesforce Platform Event Sink Connector for Confluent Cloud](../connectors/cc-salesforce-platform-event-sink.md#cc-salesforce-platform-event-sink).

### September 7, 2021

Fully-managed Confluent Cloud Salesforce SObject Sink GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Salesforce SObject Sink Connector for Confluent Cloud](../connectors/cc-salesforce-SObjects-sink.md#cc-salesforce-sobjects-sink).

### August 17, 2021

Multi-tenant cluster provisioning APIs, Admin REST APIs for Apache KafkaÂ®, and Cluster Linking APIs are Generally Available. For more information, see [API Reference Documentation](../api.md#cloud-apis).

[ksqlDB Pull Queries](/platform/current/ksqldb/pull-queries-in-ccloud.html) are now Generally Available.

Fully-managed Confluent Cloud Azure Service Bus Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Azure Service Bus Source Connector for Confluent Cloud](../connectors/cc-azure-service-bus-source.md#cc-azure-service-bus-source).

Fully-managed Confluent Cloud ServiceNow Sink GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [ServiceNow Sink Connector for Confluent Cloud](../connectors/cc-servicenow-sink.md#cc-servicenow-sink).

Fully-managed Confluent Cloud ServiceNow Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [ServiceNow Source [Legacy] Connector for Confluent Cloud](../connectors/cc-servicenow-source.md#cc-servicenow-source).

Infinite Storage is now available on Google Cloud clusters. CKUs are no longer tied to storage on Google Cloud clusters.

Cluster Linking for Confluent Cloud is Generally Available on all dedicated, internet networked clusters across all cloud providers. Note: Cluster Linking REST APIs to create and update cluster links are available on all [Dedicated Confluent Cloud clusters](../clusters/cluster-types.md#dedicated-cluster) with Internet networking created after August 16, 2021. These APIs are being rolled out to all previously created clusters. To request a Dedicated cluster update sooner, send an email to [clusterlinking@confluent.io](mailto:clusterlinking@confluent.io). To learn more, see the [Cluster Linking on Confluent Cloud Overview page](../multi-cloud/cluster-linking/index.md#cloud-cluster-linking).

max.message.bytes can now be configured up to 20 MB on dedicated clusters (previously the limit was 8 MB). See the [Confluent Cloud Broker and Topic Configuration Settings](https://docs.confluent.io/cloud/current/clusters/broker-config.html) for more details.

Additionally, check out the [August Confluent Cloud](https://www.confluent.io/blog/confluent-newest-features-in-q3-2021/) blog post to learn about the latest Confluent Cloud features.

### August 16, 2021

Fully-managed Confluent Cloud Salesforce Platform Events Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Salesforce Platform Event Source Connector for Confluent Cloud](../connectors/cc-salesforce-platform-event-source.md#cc-salesforce-platform-event-source).

### August 9, 2021

Fully-managed Confluent Cloud Azure Cosmos DB Sink GA
: This feature is launched for your Kafka clusters on Azure. For more information,
  see [Azure Cosmos DB Sink Connector for Confluent Cloud](../connectors/cc-azure-cosmos-sink.md#cc-azure-cosmos-sink).

### July 28, 2021

Cluster management APIs for Standard and Basic clusters are now available.
For more information, see [Clusters-(cmkv2)](https://docs.confluent.io/cloud/current/api.html#tag/Clusters-(cmkv2)).

### July 26, 2021

[ksqlDB 0.20.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0200-2021-07-26) is now available in Confluent Cloud.
: - DATE and TIME SQL types added
  - LEAST and GREATEST UDFs added
  - DATEADD and DATESUB functions added
  - FROM_DAYS and update UNIX_DATE functions added
  - PARSE_DATE and FORMAT_DATE functions added
  - PARSE_TIME and FORMAT_TIME functions added
  - TIMEADD and TIMESUB functions added

### July 19, 2021

[ksqlDB 0.19.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0190-2021-06-08) is now available in Confluent Cloud.
: - Foreign-key joins are now supported.
  - NULLIF function added.

### July 12, 2021

For customers with at least one [Standard](../clusters/cluster-types.md#standard-cluster) or [Dedicated](../clusters/cluster-types.md#dedicated-cluster) Kafka cluster, [Audit logs](../monitoring/audit-logging/cloud-audit-log-concepts.md#cloud-audit-logs) now include authorization event checks that occur in the control plane.

### June 10, 2021

Fully-managed Confluent Cloud Datadog Metrics Sink GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Datadog Metrics Sink for Confluent Cloud](../connectors/cc-datadog-metrics-sink.md#cc-datadog-metrics-sink).

### June 2, 2021

Infinite Storage for Standard and Dedicated clusters on Google Cloud
All new and existing Standard and Dedicated clusters on Google Cloud now support Infinite Storage. This means there is no maximum size limit for the amount of data that can be stored on the cluster. There is no price change for clusters with Infinite Storage.

For more information, see [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).

### May 26, 2021

[ksqlDB 0.18.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0180-2021-05-26) is now available in Confluent Cloud.

### May 6, 2021

[Audit logs](../monitoring/audit-logging/cloud-audit-log-concepts.md#cloud-audit-logs) are now GA
: Authentication events and authorization check events that occur on [Standard](../clusters/cluster-types.md#standard-cluster) and [Dedicated](../clusters/cluster-types.md#dedicated-cluster) Kafka cluster types are logged and available for consumption.

[Confluent Cloud Cluster Role Based Access Control (RBAC)](../security/access-control/rbac/overview.md#cloud-rbac) is now GA
: Customers can gate access to management operations at the Organization, Environment, and Cluster level. Existing users and service accounts with Confluent Cloud API keys are granted the OrganizationAdmin role in all existing organizations.

### April 26, 2021

[ksqlDB 0.17.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0170-2021-04-26) is now available in Confluent Cloud
: - Added support for [lambda functions](/platform/current/ksqldb/concepts/lambda-functions.html)
  - Added [migration tooling](/platform/current/ksqldb/operate-and-deploy/migrations-tool.html) for applying changes to running workloads
  - Non-aggregate [CTAS tables](/platform/current/ksqldb/developer-guide/ksqldb-reference/create-table-as-select.html) now support pull queries

### April 22, 2021

Fully-managed Confluent Cloud MongoDB Atlas Sink GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [MongoDB Atlas Sink Connector for Confluent Cloud](../connectors/cc-mongo-db-sink/cc-mongo-db-sink.md#cc-mongo-db-sink).

Fully-managed Confluent Cloud MongoDB Atlas Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Get Started with the MongoDB Atlas Source Connector for Confluent Cloud](../connectors/cc-mongo-db-source.md#cc-mongo-db-source).

### April 6, 2021

Azure Private Link support for Confluent Cloud Dedicated clusters is now GA
: Customers can provision new Confluent Cloud Dedicated clusters with Azure Private Link
  and establish secure connectivity to Confluent Cloud from their Azure VNet.
  <br/>
  For more information, see [Confluent Cloud Azure Private Link](https://docs.confluent.io/cloud/current/networking/index.html#az-private-link)

Import Routes with VPC Peering to Confluent Cloud Dedicated clusters on Google Cloud (Preview)
: Import route option is now supported with VPC Peering to Confluent Cloud Dedicated
  clusters on Google Cloud to enable connectivity from customer premise through customer
  VPC and support advanced network topologies to connect to Confluent Cloud.
  <br/>
  For more information, see [Confluent Cloud VPC Peering on Google Cloud](https://docs.confluent.io/cloud/current/networking/gcp-peering.html#import-custom-routes-preview)

### March 18, 2021

Fully-managed Confluent Cloud Microsoft SQL Server Sink (JDBC) GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Microsoft SQL Server Sink (JDBC) Connector for Confluent Cloud](../connectors/cc-microsoft-sql-server-sink.md#cc-microsoft-sql-server-sink).

Fully-managed Confluent Cloud MySQL Sink (JDBC) GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [MySQL Sink (JDBC) Connector for Confluent Cloud](../connectors/cc-mysql-sink.md#cc-mysql-sink).

Fully-managed Confluent Cloud PostgreSQL Sink (JDBC) GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [PostgreSQL Sink (JDBC) Connector for Confluent Cloud](../connectors/cc-postgresql-sink.md#cc-postgresql-sink).

### February 24, 2021

Fully-managed Confluent Cloud Microsoft SQL Server CDC Source (Debezium) GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Microsoft SQL Server CDC Source (Debezium) [Deprecated] Connector for Confluent Cloud](../connectors/cc-microsoft-sql-server-source-cdc-debezium.md#cc-microsoft-sql-server-source-cdc-debezium).

Fully-managed Confluent Cloud MySQL CDC Source (Debezium) GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [MySQL CDC Source (Debezium) [Deprecated] Connector for Confluent Cloud](../connectors/cc-mysql-source-cdc-debezium.md#cc-mysql-source-cdc-debezium).

Fully-managed Confluent Cloud PostgreSQL CDC Source (Debezium) GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [PostgreSQL CDC Source Connector (Debezium) [Deprecated] for Confluent Cloud](../connectors/cc-postgresql-cdc-source-debezium.md#cc-postgresql-cdc-source-debezium).

Fully-managed Confluent Cloud Salesforce CDC Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see [Salesforce CDC Source Connector for Confluent Cloud](../connectors/cc-salesforce-source-cdc.md#cc-salesforce-source-cdc).

### February 2021

Dedicated clusters are now available for all Confluent Cloud users
: Previously, [Dedicated clusters](../clusters/cluster-types.md#dedicated-cluster) were only available for customers who
  signed up through a cloud provider Marketplace integration, and customers with commits.

Fully-managed Confluent Cloud AWS Lambda Sink GA
: This feature is launched for your Kafka clusters on AWS. For more information, see
  [AWS Lambda Sink Connector for Confluent Cloud](../connectors/cc-aws-lambda-sink.md#cc-aws-lambda-sink).

Metrics API Version 2 is now GA
: Version 2 of the Metrics API adds metrics for Kafka Connect, ksqlDB, and Schema Registry.
  For more information, see [Confluent Cloud Metrics](../monitoring/metrics-api.md#metrics-api).

[ksqlDB 0.15.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0150-2021-01-20) is now available in Confluent Cloud
: - Array and Struct types can now be used as row keys.
  - PARTITION BY now supports partitioning on multiple columns.
  - Row keys now support all data formats (e.g., JSON, DELIMITED, etc.)
  - This ksqlDB release includes [breaking changes](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#breaking-changes).
    Note that these breaking changes only apply to newly created persistent queries. Existing
    persistent queries are not affected:
    - Persistent queries that use multiple grouping columns now use a different row key format.
    - Stream-table key-to-key joins on mismatched key formats now result in repartition.

### January 28, 2021

Microsoft Azure marketplace enhanced integration is in GA for customers
: The change allows customers to use their Azure AD account to login (SSO) to
  Confluent Cloud, and thereâs no need for a separate sign up.

Self-serve provisioning UI and CLI for ksqlDB applications
: New self-serve provisioning UI and CLI for ksqlDB apps that enables
  providing your own API Key. You can specify the access for your ksqlDB
  application:
  <br/>
  - With Global access, you donât need to configure ACLs at all,
    and you can begin writing queries immediately.
  - With Granular access, you can configure ACLS in the UI.

Fully-managed Confluent Cloud Azure Functions Sink GA
: This feature is launched for your Kafka clusters on Azure. For more information,
  see [Azure Functions Sink Connector for Confluent Cloud](../connectors/cc-azure-functions-sink.md#cc-azure-functions-sink).

Fully-managed Confluent Cloud Google Functions Sink GA
: This feature is launched for your Kafka clusters on Google Cloud. For more information,
  see [Google Cloud Functions Sink [Deprecated] Connector for Confluent Cloud](../connectors/cc-google-functions-sink.md#cc-google-functions-sink).

Manage lifecycle for your fully-managed connectors using an API
: You can now manage the lifecycle for your fully-managed connectors by API.
  For more information, see the [Confluent Cloud Connector API docs](https://api.confluent.cloud/docs#tag/Connectors-(v1)).

Fully-managed Confluent Cloud MongoDB Atlas Source Connector now supports BSON
: The fully-managed Confluent Cloud MongoDB Atlas Source Connector now supports BSON
  as an input message format, along with Avro, JSON, JSON_SR (JSON schema),
  and Protobuf. The connector also now supports an option to fetch a document
  change only and an option to fetch a full document when a subset of records
  is updated. For more information, see [Get Started with the MongoDB Atlas Source Connector for Confluent Cloud](../connectors/cc-mongo-db-source.md#cc-mongo-db-source).

Fully-managed Confluent Cloud MongoDB Atlas Sink Connector now supports BSON
: The fully-managed Confluent Cloud MongoDB Atlas Sink Connector now supports BSON as
  an input message format, along with Avro, JSON, JSON_SR (JSON schema), and
  Protobuf. For more information, see [MongoDB Atlas Sink Connector for Confluent Cloud](../connectors/cc-mongo-db-sink/cc-mongo-db-sink.md#cc-mongo-db-sink).

## 2020 Releases

### December 16, 2020

ksqlDB [version 0.14.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0140-2020-10-28) now available in Confluent Cloud
: ksqlDB version 0.14.0 provides more advanced pull query expressions
  (`WHERE k IN (...)`), incremental schema evolution (ALTER), variable
  substitution (`${foo}`), and more key formats.

### December 1, 2020

Infinite Storage for Standard and Dedicated clusters on AWS
: All new and existing Standard and Dedicated clusters on AWS now support Infinite Storage. This means there is no maximum size
  limit for the amount of data that can be stored on the cluster. There is no price change for clusters with Infinite Storage.
  <br/>
  For more information, see [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).

### November 20, 2020

Fully-managed Confluent Cloud Elasticsearch Service Sink GA
: This feature is launched for your Kafka clusters on AWS, Azure, or Google Cloud. For more information, see [Elasticsearch Service Sink Connector for Confluent Cloud](../connectors/cc-elasticsearch-service-sink.md#cc-elasticsearch-service-sink).

Fully-managed Confluent Cloud Azure Data Lake Storage Gen2 Sink GA
: This feature is launched for your Kafka clusters on Azure. For more information, see [Azure Data Lake Storage Gen2 Sink Connector for Confluent Cloud](../connectors/cc-azure-datalakeGen2-storage-sink.md#cc-azure-datalakegen2storage-sink).

Fully-managed Confluent Cloud Google Cloud Functions Sink Preview
: This feature is launched for your Kafka clusters on Google Cloud. For more information, see [Google Cloud Functions Sink [Deprecated] Connector for Confluent Cloud](../connectors/cc-google-functions-sink.md#cc-google-functions-sink).

### October 23, 2020

ksqlDB [version 0.13.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0130-2020-10-23) now available in Confluent Cloud
: [Pull queries](/platform/current/ksqldb/concepts/queries.html#pull)
  are now available [as a preview feature](https://docs.confluent.io/current/ksqldb/pull-queries-in-ccloud.html#pull-queries-preview-with-ccloud-ksqldb) for all Confluent Cloud ksqlDB users.

### September 28, 2020

ksqlDB version 0.12.0 now available in Confluent Cloud
: For more information, see the
  [0.12.0 changelog](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0120-2020-09-01).

### September 25, 2020

Fully-managed Confluent Cloud Amazon Redshift Sink GA
: This feature is launched for your Kafka clusters in AWS. For more information, see [Amazon Redshift Sink Connector for Confluent Cloud](../connectors/cc-amazon-redshift-sink.md#cc-amazon-redshift-sink).

Fully-managed Confluent Cloud Microsoft SQL Server Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [Microsoft SQL Server Source (JDBC) Connector for Confluent Cloud](../connectors/cc-microsoft-sql-server-source.md#cc-microsoft-sql-server-source).

Fully-managed Confluent Cloud Oracle DB Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [Oracle Database Source (JDBC) Connector for Confluent Cloud](../connectors/cc-oracle-db-source.md#cc-oracle-db-source).

Fully-managed Confluent Cloud Snowflake Sink GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [Oracle Database Source (JDBC) Connector for Confluent Cloud](../connectors/cc-oracle-db-source.md#cc-oracle-db-source).

Fully-managed Confluent Cloud Azure Functions Sink Preview
: This feature is launched for your Kafka clusters in AWS. For more information, see [Azure Functions Sink Connector for Confluent Cloud](../connectors/cc-azure-functions-sink.md#cc-azure-functions-sink).

Fully-managed Confluent Cloud MySQL Sink Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [MySQL Sink (JDBC) Connector for Confluent Cloud](../connectors/cc-mysql-sink.md#cc-mysql-sink).

### September 11, 2020

MySQL Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [MySQL Source (JDBC) Connector for Confluent Cloud](../connectors/cc-mysql-source.md#cc-mysql-source).

PostgreSQL Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [PostgreSQL Source (JDBC) Connector for Confluent Cloud](../connectors/cc-postgresql-source.md#cc-postgresql-source).

Fully-managed Confluent Cloud AWS Lambda Sink Preview
: This feature is launched for your Kafka clusters in AWS. For more information, see [AWS Lambda Sink Connector for Confluent Cloud](../connectors/cc-aws-lambda-sink.md#cc-aws-lambda-sink).

Fully-managed Confluent Cloud Salesforce CDC Source Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information, see [Salesforce CDC Source Connector for Confluent Cloud](../connectors/cc-salesforce-source-cdc.md#cc-salesforce-source-cdc).

### September 3, 2020

Updated Schemas UI + Schema Registry settings
: Customers can now see the list of schemas stored in Schema Registry, irrespective of the subject naming
  strategy applied, on the Schemas section in the Cloud Console. Additionally, **Schemas Registry Allowed Usage**,
  **Schemas Registry API access**, and **Schemas Registry compatibility configuration**
  are moved to the **Settings** section in the **Environment** the Schema Registry was created.

Fully-managed Confluent Cloud Microsoft SQL Server Sink Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [Microsoft SQL Server Sink (JDBC) Connector for Confluent Cloud](../connectors/cc-microsoft-sql-server-sink.md#cc-microsoft-sql-server-sink).

Fully-managed Confluent Cloud PostgreSQL Sink Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [PostgreSQL Sink (JDBC) Connector for Confluent Cloud](../connectors/cc-postgresql-sink.md#cc-postgresql-sink).

Fully-managed Confluent Cloud MySQL CDC Source (Debezium) Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [MySQL CDC Source (Debezium) [Deprecated] Connector for Confluent Cloud](../connectors/cc-mysql-source-cdc-debezium.md#cc-mysql-source-cdc-debezium).

Fully-managed Confluent Cloud Microsoft SQL Server CDC Source (Debezium) Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [Microsoft SQL Server CDC Source (Debezium) [Deprecated] Connector for Confluent Cloud](../connectors/cc-microsoft-sql-server-source-cdc-debezium.md#cc-microsoft-sql-server-source-cdc-debezium).

Fully-managed Confluent Cloud PostgreSQL CDC Source Connector (Debezium) Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [PostgreSQL CDC Source Connector (Debezium) [Deprecated] for Confluent Cloud](../connectors/cc-postgresql-cdc-source-debezium.md#cc-postgresql-cdc-source-debezium).

### September 1, 2020

Improvements to Confluent Cloud ksqlDB handling of authorization by using bearer tokens.

### August 13, 2020

Early access for Custom Dedicated Cluster settings
: You can now modify the following Dedicated cluster settings in this limited Early Access: auto
  topic creation, allowed cipher suites, and default topic partitions and retention.  For more
  information, see [Change cluster settings for Dedicated clusters](../clusters/broker-config.md#custom-settings-dedicated).

### August 3, 2020

Azure VPC Peering self-serve provisioning via the Confluent Cloud Console
: Customers with annual commitments on usage-based billing plans can now provision new dedicated
  clusters on Azure with VPC Peering. For more information, see [Use Azure VNet Peering with Confluent Cloud](../networking/peering/azure-peering.md#cloud-networking-azure).

ksqlDB version 0.11.0 now available in Confluent Cloud.
: For more information, see the
  [0.11.0 changelog](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#0110-2020-08-03).

### July 31, 2020

Fully-managed Confluent Cloud Datagen Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more
  information,  see  [Datagen Source Connector for Confluent Cloud](../connectors/cc-datagen-source.md#cc-datagen-source).

Feature enhancements for Fully-managed connectors
: - Protobuf and JSON Schema support for Confluent Cloud connectors.
  - Compression support for the Amazon S3 sink connector. For more information, see [Amazon S3 Sink Connector for Confluent Cloud](../connectors/cc-s3-sink/cc-s3-sink.md#cc-s3-connect-sink).

### July 15, 2020

AWS Marketplace Commits and Pay-as-you-go
: Amazon Web Services customers can now sign up for a self-serve Pay-as-you-go account or Confluent Cloud annual
  commitments through the AWS Marketplace. With Confluent Cloud annual commitments you can use your AWS
  commit towards usage-based consumption of Confluent Cloud. For more information, see:
  <br/>
  - [Get Started with Confluent Cloud on the AWS Marketplace with Pay As You Go](../billing/ccloud-aws-payg.md#ccloud-aws-market)
  - [Get Started with Confluent Cloud on the AWS Marketplace with Commitments](../billing/ccloud-aws-ubb.md#ccloud-aws-market-ubb)

### July 14, 2020

Support for Bring Your Own Key (BYOK) on AWS dedicated clusters
: - New dedicated clusters only.
  - Supports AWS Key Management Service (KMS) only.
  - Support for automatic key rotation. No support for manual key rotation.
  <br/>
  For more information, see [Protect Data at Rest Using Self-Managed Encryption Keys on Confluent Cloud](../security/encrypt/byok/overview.md#byok-encrypted-clusters).

### June 25, 2020

Fully-managed Confluent Cloud Azure Event Hubs Source GA
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [Azure Event Hubs Source Connector for Confluent Cloud](../connectors/cc-azure-event-hubs-source.md#cc-azure-event-hubs-source).

Fully-managed Confluent Cloud Snowflake Sink Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [Snowflake Sink Connector for Confluent Cloud](../connectors/cc-snowflake-sink/cc-snowflake-sink.md#cc-snowflake-sink).

Fully-managed Confluent Cloud Elasticsearch Sink Preview
: This feature is launched for your Kafka clusters in AWS, Azure, or Google Cloud. For more information,
  see  [Elasticsearch Service Sink Connector for Confluent Cloud](../connectors/cc-elasticsearch-service-sink.md#cc-elasticsearch-service-sink).

Fully-managed Confluent Cloud Amazon S3 Sink Improvements
: Additional properties to support building a time-based directory structure for data stored in S3.
  For more information, see  [Amazon S3 Sink Connector for Confluent Cloud](../connectors/cc-s3-sink/cc-s3-sink.md#cc-s3-connect-sink).

Hard-delete schemas in Schema Registry
: The Schema Registry API now supports permanent schema deletes with `?permanent=true` on the HTTP DELETE
  call.

Support for schema references for Avro and JSON Schema in Schema Registry
: Avro and JSON Schema can now make references to external schemas and evolve those independently
  (Protobuf already supports references). Schema references are a means of modularizing a schema
  and its dependencies.

Functionality from ksqlDB [0.9.0 and 0.10.0](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md) is now available in Confluent Cloud
: - Support for multi-way joins.
  - [New syntax for specifying row keys](https://github.com/confluentinc/ksql/blob/master/CHANGELOG.md#explicit-keys).
  - Many new builtin functions.

### June 18, 2020

Annual Commitment Users on Google Cloud Can Provision Dedicated Clusters with VPC Peering
: Customers with annual commitments on usage-based billing plans can now provision new dedicated
  clusters on Google Cloud with VPC Peering through the Cloud Console. For more information, see
  [Use Google Cloud VPC Network Peering with Confluent Cloud](../networking/peering/gcp-peering.md#cloud-networking-gcp).

### June 10, 2020

Data flow
: Data flow is now GA. This feature provides a visual representation of the data flow paths (edges)
  between producers, topics, and consumers within a cluster.

Google Cloud Marketplace Commits
: Google Cloud customers can now sign up for Confluent Cloud annual commitments using the Google Cloud marketplace and
  utilize their Google Cloud commit towards usage-based consumption of Confluent Cloud. For more information, see
  [Get Started with Confluent Cloud on the Google Cloud Marketplace with Commitments](../billing/ccloud-gcp-ubb.md#ccloud-gcp-market-ubb).

### June 5, 2020

Fully-managed Confluent Cloud Kinesis Source GA
: This feature is launched for your Kafka clusters in AWS. For more information, see
  [Amazon Kinesis Source Connector for Confluent Cloud](../connectors/cc-kinesis-source.md#cc-kinesis-source).

Annual Commitment Users on AWS Can Provision Dedicated Clusters with VPC Peering
: Customers with annual commitments on usage-based billing plans can now provision new dedicated
  clusters on Amazon Web Services with VPC Peering through the Cloud Console. For more information,
  see [Use AWS VPC Peering with Confluent Cloud](../networking/peering/aws-peering.md#cloud-networking-peering-aws).

### May 27, 2020

Fully-managed Confluent Cloud Google BigQuery Sink GA
: This feature is launched for your Kafka clusters in Google Cloud. For more information, see [Google Cloud BigQuery Sink [Deprecated] Connector for Confluent Cloud](../connectors/cc-gcp-bigquery-sink.md#cc-gcp-bigquery-sink).

Fully-managed Confluent Cloud Google Cloud Pub/Sub Source GA
: This feature is launched for your Kafka clusters in Amazon Web Services, Google Cloud, and Microsoft Azure. For more information, see [Google Cloud Pub/Sub Source Connector for Confluent Cloud](../connectors/cc-google-pubsub-source.md#cc-google-pubsub-source).

Fully-managed Confluent Cloud MongoDB Source Preview
: This feature is launched for your Kafka clusters in Amazon Web Services, Google Cloud, and Microsoft Azure. For more information, see [Get Started with the MongoDB Atlas Source Connector for Confluent Cloud](../connectors/cc-mongo-db-source.md#cc-mongo-db-source).

Fully-managed Confluent Cloud MongoDB Sink Preview
: This feature is launched for your Kafka clusters in Amazon Web Services, Google Cloud, and Microsoft Azure. For more information, see [MongoDB Atlas Sink Connector for Confluent Cloud](../connectors/cc-mongo-db-sink/cc-mongo-db-sink.md#cc-mongo-db-sink).

Confluent Cloud Metrics API
: Confluent Cloud Metrics API now serves metrics for records sent and received for clusters, topics, and partitions along with cluster level partition count. For more information, see [Confluent Cloud Metrics](../monitoring/metrics-api.md#metrics-api).

### May 14, 2020

Cluster Level Metrics in the Cloud Console
: View your time-series graphs of your Apache KafkaÂ® cluster usage. This includes your ingress, egress,
  storage, and partition count to allow you to monitor your usage over time.

Annual Commitment Users Can Expand Dedicated Clusters
: Customers with annual commitments on usage-based billing plans can now expand their dedicated
  clusters through the Cloud Console. For more information, see [Expand a Dedicated Kafka Cluster](../clusters/resize.md#cloud-cluster-expand).

### April 23, 2020

Usage-based billing with commits
: Usage-based billing with commits is now available for customers on the Azure Marketplace. You can
  now commit a spend, get a discount, and transact through the Azure Marketplace to get started with
  Confluent Cloud. For more information, see [Get Started with Confluent Cloud on the Azure Marketplace with Commitments](../billing/ccloud-azure-ubb.md#ccloud-azure-market-ubb).

Support for Protocol Buffers and JSON Schema in Confluent Cloud
: Support for Protocol Buffers and JSON Schema has been added in Schema Registry and throughout
  Confluent Cloud, including ksqlDB, Kafka Streams and Kafka Clients. For more information, see [Avro, JSON, and Protobuf Supported Formats and Extensibility](/platform/current/schema-registry/index.html#avro-json-proto-exten).

Confluent Cloud CLI General Availability
: The Confluent Cloud CLI has been promoted to general availability with features that now enable use in
  a scripted environment:
  <br/>
  - Machine readable JSON or YAML output through the `-o` flag on commands with return values.
  - Long-lived authentication through `ccloud login --save`.
  <br/>
  For more information, see [Confluent Cloud command reference](https://docs.confluent.io/confluent-cli/current/command-reference/overview.html).

Fully-managed Confluent Cloud Google Cloud Spanner Sink Preview
: This feature is launched for your Kafka clusters in Google Cloud. For more information, see
  [Google Cloud Spanner Sink Connector for Confluent Cloud](../connectors/cc-gcp-spanner-sink.md#cc-gcp-spanner-sink).

Fully-managed Confluent Cloud Google Cloud Dataproc Sink Preview
: This feature is launched for your Kafka clusters in Google Cloud. For more information, see
  [Google Cloud Dataproc Sink Connector [Deprecated] for Confluent Cloud](../connectors/cc-gcp-dataproc-sink.md#cc-gcp-dataproc-sink).

Fully-managed Confluent Cloud Azure Event Hubs Source Preview
: This feature is launched for your Kafka clusters in Amazon Web Services, Google Cloud, and Microsoft Azure. For
  more information, see [Azure Event Hubs Source Connector for Confluent Cloud](../connectors/cc-azure-event-hubs-source.md#cc-azure-event-hubs-source).

Fully-managed Confluent Cloud Azure Data Lake Storage Gen2 Sink Preview
: This feature is launched for your Kafka clusters in Microsoft Azure. For more information, see
  [Azure Data Lake Storage Gen2 Sink Connector for Confluent Cloud](../connectors/cc-azure-datalakeGen2-storage-sink.md#cc-azure-datalakegen2storage-sink).

Fully-managed Confluent Cloud Amazon Redshift Sink Preview
: This feature is launched for your Kafka clusters in Amazon Web Services. For more information, see
  [Amazon Redshift Sink Connector for Confluent Cloud](../connectors/cc-amazon-redshift-sink.md#cc-amazon-redshift-sink).

### April 6, 2020

Confluent Cloud Cluster Tiers: Basic, Standard, Dedicated
: Confluent Cloud now offers three cluster tiers: Basic, Standard, and Dedicated.
  <br/>
  - Basic clusters are billed for ingress, egress, and storage.
  - Standard clusters are billed an hourly base price of $1.50 USD per hour, in addition to
    usage-based charges.
  - Dedicated clusters are available for customers with annual commitments, which you can purchase
    from Confluent. Existing standard clusters will remain unchanged through March 31, 2021, after
    which any existing single-zone clusters will be migrated to basic, and multi-zone clusters will
    be migrated to standard.
  <br/>
  For more information, see [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).

Annual Commitment Users Can Provision Dedicated Clusters
: Customers with annual commitments on usage-based billing plans can now provision new dedicated
  clusters with internet endpoints through the Confluent Cloud Console. For more information, see
  [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).

Confluent Cloud ksqlDB Production Availability
: Confluent Cloud ksqlDB is now production available for all users on usage-based billing plans.

### March 31, 2020

Confluent Cloud Metrics API GA
: The Confluent Cloud Metrics API is now GA with new metrics for connection counts and request rates. It
  is enabled for all newly provisioned clusters and is rolling out to existing clusters in AWS,
  Google Cloud, and Azure at this time. For more information, see [Confluent Cloud Metrics](../monitoring/metrics-api.md#metrics-api).

Confluent Cloud Azure Blob Storage Sink GA
: Fully-managed Confluent Cloud Azure Blob Storage Sink is now GA. For more information, see
  [Azure Blob Storage Sink Connector for Confluent Cloud](../connectors/cc-azure-blob-sink/cc-azure-blob-sink.md#cc-azure-blob-sink).

### February 18, 2020

Consumption-based Self-serve Confluent Cloud on the Azure Marketplace
: With this release, you can now find consumption-based self-serve Confluent Cloud offering on the Azure
  Marketplace. You can sign up to use Confluent Cloud by utilizing your Azure spend. For more information,
  see [Get Started with Confluent Cloud on the Azure Marketplace with Pay As You Go](../billing/ccloud-azure-payg.md#ccloud-azure-market) and the [blog post](https://confluent.io/blog/confluent-cloud-managed-kafka-service-azure-marketplace).

### January 24, 2020

Fully-managed Confluent Cloud Oracle Database Source Preview
: This feature is launched for your Apache KafkaÂ® clusters in Amazon Web Services, Google Cloud, and Microsoft Azure. For
  more information, see [Oracle Database Source (JDBC) Connector for Confluent Cloud](../connectors/cc-oracle-db-source.md#cc-oracle-db-source).

Fully-managed Confluent Cloud Microsoft SQL Server Source Preview
: This feature is launched for your Kafka clusters in AWS, Google Cloud, and Azure. For more information,
  see [Microsoft SQL Server Source (JDBC) Connector for Confluent Cloud](../connectors/cc-microsoft-sql-server-source.md#cc-microsoft-sql-server-source).

Fully-managed Confluent Cloud Google Cloud Pub/Sub Source Preview
: This feature is launched for your Kafka clusters in AWS, Google Cloud, and Azure. For more information,
  see [Google Cloud Pub/Sub Source Connector for Confluent Cloud](../connectors/cc-google-pubsub-source.md#cc-google-pubsub-source).

### January 2, 2020

Fully-managed Confluent Cloud GCS Connector (Sink) GA
: For more information, see [Google Cloud Storage Sink Connector for Confluent Cloud](../connectors/cc-gcs-sink.md#cc-gcs-connect-sink).

## 2019 Releases

### December 20, 2019

SAML/SSO Production Availability
: - This feature enables customers to utilize their Identity provider to centrally
    manage user login information.
  - This feature supports all the Identity Providers with SAML 2.0 including: Okta, Ping, OneLogin,
    Microsoft Active Directory
  - This feature is available on AWS, Google Cloud, and Azure.
  - For more information, see the [documentation](../security/authenticate/user-identities/user-idps/sso/overview.md#sso-saml).

Confluent Cloud Metrics API Preview
: This feature is available for Apache KafkaÂ® clusters in AWS, Google Cloud, and Azure. For more
  information, see [Confluent Cloud Metrics](../monitoring/metrics-api.md#metrics-api).

### December 12, 2019

Fully-managed Confluent Cloud PostgreSQL Source Preview
: This feature is launched for your Apache KafkaÂ® clusters in AWS, Google Cloud, and Azure. For more information,
  see [PostgreSQL Source (JDBC) Connector for Confluent Cloud](../connectors/cc-postgresql-source.md#cc-postgresql-source).

Fully-managed Confluent Cloud MySQL Source Preview
: This feature is launched for your Kafka clusters in AWS, Google Cloud, and Azure. For more information,
  see [MySQL Source (JDBC) Connector for Confluent Cloud](../connectors/cc-mysql-source.md#cc-mysql-source).

Fully-managed Confluent Cloud Kinesis Source Preview
: This feature is launched for your Kafka clusters in AWS. For more information, see [Amazon Kinesis Source Connector for Confluent Cloud](../connectors/cc-kinesis-source.md#cc-kinesis-source).

Other improvements
: - The Kafka cluster ID is now shown in the **Cluster Settings** page. This makes it easier for you
    to connect clients to your clusters.
  - The Clients tab in **CLI & Client Configuration** page now shows client configurations for 12
    different clients, with links to example code for each type of client.

### November 15, 2019

Fully-managed Confluent Cloud Google BigQuery Connector (Sink) Preview
: For more information, see [Google Cloud BigQuery Sink [Deprecated] Connector for Confluent Cloud](../connectors/cc-gcp-bigquery-sink.md#cc-gcp-bigquery-sink).

Connector improvements
: - Avro format support has been added to Confluent Cloud [Google Cloud Storage Connector](../connectors/cc-gcs-sink.md#cc-gcs-connect-sink) and
    [Azure Blob Storage Connector](../connectors/cc-azure-blob-sink/cc-azure-blob-sink.md#cc-azure-blob-sink).
  - You can increase connect tasks to get a better performance and handle more partitions.

Support plan update
: * Support plan downgrades now have certain restrictions in place. When you purchase a support plan, you will retain the support plan and be charged for it for the current and potentially next billing cycle. For more information, see [Support](../billing/overview.md#cloud-support-plans)
  * A Confluent Community [self-serve offering](https://console.cloud.google.com/marketplace/details/endpoints/payg-prod.gcpmarketplace.confluent.cloud) is now available from the Google Cloud marketplace. Google Cloud customers can now use their Google Cloud committed expenditure for Confluent Cloud standard clusters. See the [Google Cloud Marketplace offering for details](https://console.cloud.google.com/marketplace/details/endpoints/payg-prod.gcpmarketplace.confluent.cloud).

### October 31, 2019

Higher availability with multi-zone clusters
: You can now choose between single or multiple availability zones when creating new Confluent Cloud clusters. If you
  select multiple availability zones, data in the cluster will be spread across multiple cloud availability zones.
  This provides higher availability in the case of a zonal outage. Prices may differ between single and multiple
  availability zone configurations. For more details about cloud provider availability zones:
  <br/>
  - AWS: [https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones)
  - Google Cloud: [https://cloud.google.com/docs/geography-and-regions](https://cloud.google.com/docs/geography-and-regions)
  - Azure: [https://docs.microsoft.com/en-us/azure/availability-zones/az-overview](https://docs.microsoft.com/en-us/azure/availability-zones/az-overview)

Use all UI features with VPC-peered clusters
: You can now use the Confluent Cloud Console for ksqlDB stream processing, topic management, and consumer lag monitoring on
  VPC peered clusters. You must configure your network to route and proxy the necessary requests between the UI and
  your cluster. For more details about setting this up, see [Manage Networking on Confluent Cloud](../networking/overview.md#cloud-networking).

Fully-managed Confluent Cloud Azure Blob Storage Connector (Sink) Preview
: Fully-managed Confluent Cloud Azure Blob Storage Connector (Sink) available in Preview. For more information, see
  [Azure Blob Storage Sink Connector for Confluent Cloud](../connectors/cc-azure-blob-sink/cc-azure-blob-sink.md#cc-azure-blob-sink).

Use Confluent Cloud in more regions
: Confluent Cloud is now available in:
  <br/>
  - Azure useast2 (Virginia)
  - Google Cloud asia-southeast1 (Singapore)

### September 27, 2019

Confluent Cloud Schema Registry General Availability
: Now available on Microsoft Azure and in multiple geographical regions (US, Europe, and APAC).

### August 30, 2019

Microsoft Azure General Availability
: Confluent Cloud is now generally available on Microsoft Azure in:
  <br/>
  - Azure southeastasia (Singapore)
  - Azure westus2 (Washington)
  - Azure westeurope (Netherlands)

Fully-managed Confluent Cloud S3 Connector (Sink) Production Availability.
: For more information, see [Amazon S3 Sink Connector for Confluent Cloud](../connectors/cc-s3-sink/cc-s3-sink.md#cc-s3-connect-sink).

Fully-managed Confluent Cloud GCS Connector (Sink) Preview
: For more information, see [Google Cloud Storage Sink Connector for Confluent Cloud](../connectors/cc-gcs-sink.md#cc-gcs-connect-sink).

Use Confluent Cloud in more regions
: Confluent Cloud is now available in:
  <br/>
  - AWS ap-northeast-1 (Tokyo)
  - AWS ap-south-1 (Mumbai)
  - AWS ap-southeast-1 (Singapore)
  - Google Cloud asia-northeast1 (Tokyo)
  - Google Cloud asia-southeast1 (Singapore)
  - Google Cloud europe-west4 (Netherlands)

### August 16, 2019

Support
: You can now purchase support for Confluent Cloud through the global menu in the web interface. For plan details and pricing, see [Confluent Cloud Support](https://www.confluent.io/confluent-cloud/support/).

Service Level Agreement (SLA)
: With this release, the SLA for Confluent Cloud is updated. An uptime SLA is now available for new clusters created in some regions; the SLA is displayed in the cluster creation and cluster details UI if it is available. See [Confluent Cloud SLA for details](https://www.confluent.io/confluent-cloud-uptime-sla).

Schema Registry
: Confluent Cloud Schema Registry is now generally available on Google Cloud (GCP) and in multiple geographical regions (US, Europe, and APAC). To get started, see [Quick Start for Schema Management on Confluent Cloud](../get-started/schema-registry.md#cloud-sr-config).

### August 1, 2019

VPC peering to multiple customer VPCs
: You can now peer one Dedicated cluster with up to five VPCs within the same region and cloud provider. This lets you connect applications across multiple networks using Confluent Cloud.

AWS Transit Gateway
: You can now link a Dedicated cluster running in AWS to an [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/). Transit Gateway allows transitive routing and supports a variety of AWS networking services, which makes it possible to connect clients in many networks, both in the cloud and on-premises, to Confluent Cloud.

### June 25, 2019

Apache KafkaÂ® 2.3 released.
: All Confluent Cloud clusters have been automatically upgraded. For more information, see [https://www.apache.org/dist/kafka/2.3.0/RELEASE_NOTES.html](https://www.apache.org/dist/kafka/2.3.0/RELEASE_NOTES.html).

### May 29, 2019

CLI update
: The Confluent Cloud CLI now supports [ACLs and service accounts](../security/authenticate/user-identities/user-accounts/overview.md#user-accounts).

### May 13, 2019

Capacity increase
: All Confluent Cloud self-serve clusters can now support peak throughput up to 100 MBps write and 100 MBps read, and can store up to 5 TB of data.

ksqlDB Preview
: Fully managed [KSQL is available in Preview](../ksqldb/overview.md#ksql-optin-ccloud-preview).

### May 7, 2019

S3 Connector Preview
: Fully managed [AWS S3 Sink Connector is available in Preview](../connectors/cc-s3-sink/cc-s3-sink.md#cc-s3-connect-sink).

### May 1, 2019

Consumption-based pricing
: Confluent Cloud now offers [consumption-based pricing](../billing/overview.md#cloud-billing).

Name change
: Confluent Cloud Professional is now simply called Confluent Cloud. For more information, see [https://www.confluent.io/blog/introducing-cloud-native-experience-for-apache-kafka-in-confluent-cloud](https://www.confluent.io/blog/introducing-cloud-native-experience-for-apache-kafka-in-confluent-cloud).

### April 5, 2019

Schema edit UI
: View and edit schemas in the [Topic Management UI](../sr/schemas-manage.md#cloud-schemas-manage).

### March 26, 2019

Apache KafkaÂ® 2.2 released.
: All Confluent Cloud clusters have been automatically upgraded. For more information, see [https://www.apache.org/dist/kafka/2.2.0/RELEASE_NOTES.html](https://www.apache.org/dist/kafka/2.2.0/RELEASE_NOTES.html).

### March 13, 2019

Schema Registry Preview
: Schema Registry [is now available in Preview](../sr/schemas-manage.md#sr-prv).

### February 27, 2019

Topic management UI
: You can now see the actual topics, configurations, and events on your cluster from the Cloud Console interface.  For details, see [Manage Topics in Confluent Cloud](../topics/overview.md#cloud-topics).

Consumer lag
: You can now see how your consumer groups are managing with the traffic on your cluster from the Cloud Console interface. For details, see [Monitor Kafka Consumer Lag in Confluent Cloud](../monitoring/monitor-lag.md#cloud-monitoring-lag).

#### IMPORTANT
These features are not yet available for customers using VPC peering.

### January 22, 2019

UI navigation update
: The UI has been updated to show you more information with fewer clicks, and to logically group common actions. Many administrative actions and support links are always available by clicking on your name in the upper-right corner. These options were previously available in the navigation bar and in the cluster management UI. The [Quick Start for Confluent Cloud](../get-started/index.md#cloud-quickstart) and related documentation is updated to reflect these changes.

Environment overview
: Now you can see provisioned capacity and usage data for all your clusters on the new **Environment Overview** page. Usage data was previously available in a dedicated Activity page for each cluster.

Parameter changes
: In the past, Confluent Cloud allowed users to configure a wide range of topic level configuration parameters. However, some of these parameters arenât necessary when using a fully managed service. Confluent Cloud now ignores these parameters. Existing users should see no change, as it has been verified that these parameters were never used in practice. For consistency, some configuration parameters in the describe topics/configuration APIs are now read-only.

- Azure users can now use self-managed encryption keys (BYOK) for Confluent Cloud Enterprise Kafka clusters.
  For more information, see [Encryption of data at rest on Kafka clusters](../security/encrypt/byok/overview.md#encryption-data-at-rest-clusters) and
  [Use Self-Managed Encryption Keys in Confluent Cloud on Azure](../security/encrypt/byok/byok-azure.md#byok-encrypted-clusters-azure).
