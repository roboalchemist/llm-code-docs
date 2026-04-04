# Source: https://docs.datadoghq.com/api/latest/observability-pipelines/

# Observability Pipelines
Observability Pipelines allows you to collect and process logs within your own infrastructure, and then route them to downstream integrations.
## [List pipelines](https://docs.datadoghq.com/api/latest/observability-pipelines/#list-pipelines)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/observability-pipelines/#list-pipelines-v2)


**Note** : This endpoint is in Preview. Fill out this [form](https://www.datadoghq.com/product-preview/observability-pipelines-api-and-terraform-support/) to request access.
GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.ap2.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.datadoghq.eu/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.ddog-gov.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.us3.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines
### Overview
Retrieve a list of pipelines. This endpoint requires the `observability_pipelines_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
### Response
  * [200](https://docs.datadoghq.com/api/latest/observability-pipelines/#ListPipelines-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/observability-pipelines/#ListPipelines-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/observability-pipelines/#ListPipelines-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/observability-pipelines/#ListPipelines-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Represents the response payload containing a list of pipelines and associated metadata.
Expand All
Field
Type
Description
_required_]
[object]
The `schema` `data`.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
id [_required_]
string
Unique identifier for the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
object
Metadata about the response.
totalCount
int64
The total number of pipelines.
```
{
  "data": [
    {
      "attributes": {
        "config": {
          "destinations": [
            {
              "id": "datadog-logs-destination",
              "inputs": [
                "filter-processor"
              ],
              "type": "datadog_logs"
            }
          ],
          "processors": [
            {
              "display_name": "my component",
              "enabled": true,
              "id": "grouped-processors",
              "include": "service:my-service",
              "inputs": [
                "datadog-agent-source"
              ],
              "processors": [
                []
              ]
            }
          ],
          "sources": [
            {
              "group_id": "consumer-group-0",
              "id": "kafka-source",
              "librdkafka_options": [
                {
                  "name": "fetch.message.max.bytes",
                  "value": "1048576"
                }
              ],
              "sasl": {
                "mechanism": "string"
              },
              "tls": {
                "ca_file": "string",
                "crt_file": "/path/to/cert.crt",
                "key_file": "string"
              },
              "topics": [
                "topic1",
                "topic2"
              ],
              "type": "kafka"
            }
          ]
        },
        "name": "Main Observability Pipeline"
      },
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "type": "pipelines"
    }
  ],
  "meta": {
    "totalCount": 42
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=typescript)


#####  List pipelines
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List pipelines
```
"""
List pipelines returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi

configuration = Configuration()
configuration.unstable_operations["list_pipelines"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.list_pipelines()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List pipelines
```
# List pipelines returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_pipelines".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ObservabilityPipelinesAPI.new
p api_instance.list_pipelines()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List pipelines
```
// List pipelines returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ListPipelines", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewObservabilityPipelinesApi(apiClient)
	resp, r, err := api.ListPipelines(ctx, *datadogV2.NewListPipelinesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObservabilityPipelinesApi.ListPipelines`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ObservabilityPipelinesApi.ListPipelines`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List pipelines
```
// List pipelines returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ObservabilityPipelinesApi;
import com.datadog.api.client.v2.model.ListPipelinesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listPipelines", true);
    ObservabilityPipelinesApi apiInstance = new ObservabilityPipelinesApi(defaultClient);

    try {
      ListPipelinesResponse result = apiInstance.listPipelines();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservabilityPipelinesApi#listPipelines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List pipelines
```
// List pipelines returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_observability_pipelines::ListPipelinesOptionalParams;
use datadog_api_client::datadogV2::api_observability_pipelines::ObservabilityPipelinesAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListPipelines", true);
    let api = ObservabilityPipelinesAPI::with_config(configuration);
    let resp = api
        .list_pipelines(ListPipelinesOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List pipelines
```
/**
 * List pipelines returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listPipelines"] = true;
const apiInstance = new v2.ObservabilityPipelinesApi(configuration);

apiInstance
  .listPipelines()
  .then((data: v2.ListPipelinesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a new pipeline](https://docs.datadoghq.com/api/latest/observability-pipelines/#create-a-new-pipeline)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/observability-pipelines/#create-a-new-pipeline-v2)


**Note** : This endpoint is in Preview. Fill out this [form](https://www.datadoghq.com/product-preview/observability-pipelines-api-and-terraform-support/) to request access.
POST https://api.ap1.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.ap2.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.datadoghq.eu/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.ddog-gov.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.us3.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelineshttps://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines
### Overview
Create a new pipeline. This endpoint requires the `observability_pipelines_deploy` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Expand All
Field
Type
Description
_required_]
object
Contains the the pipeline configuration.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
```
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "my-processor-group"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "enabled": true,
            "id": "my-processor-group",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              {
                "enabled": true,
                "id": "filter-processor",
                "include": "status:error",
                "type": "filter"
              }
            ]
          }
        ],
        "sources": [
          {
            "id": "datadog-agent-source",
            "type": "datadog_agent"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "type": "pipelines"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/observability-pipelines/#CreatePipeline-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/observability-pipelines/#CreatePipeline-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/observability-pipelines/#CreatePipeline-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/observability-pipelines/#CreatePipeline-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/observability-pipelines/#CreatePipeline-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Top-level schema representing a pipeline.
Expand All
Field
Type
Description
_required_]
object
Contains the pipeline’s ID, type, and configuration attributes.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
id [_required_]
string
Unique identifier for the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
```
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "filter-processor"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "display_name": "my component",
            "enabled": true,
            "id": "grouped-processors",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              []
            ]
          }
        ],
        "sources": [
          {
            "group_id": "consumer-group-0",
            "id": "kafka-source",
            "librdkafka_options": [
              {
                "name": "fetch.message.max.bytes",
                "value": "1048576"
              }
            ],
            "sasl": {
              "mechanism": "string"
            },
            "tls": {
              "ca_file": "string",
              "crt_file": "/path/to/cert.crt",
              "key_file": "string"
            },
            "topics": [
              "topic1",
              "topic2"
            ],
            "type": "kafka"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "type": "pipelines"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=typescript)


#####  Create a new pipeline returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "my-processor-group"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "enabled": true,
            "id": "my-processor-group",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              {
                "enabled": true,
                "id": "filter-processor",
                "include": "status:error",
                "type": "filter"
              }
            ]
          }
        ],
        "sources": [
          {
            "id": "datadog-agent-source",
            "type": "datadog_agent"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "type": "pipelines"
  }
}
EOF  

                        
```

#####  Create a new pipeline returns "OK" response
```
// Create a new pipeline returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ObservabilityPipelineSpec{
		Data: datadogV2.ObservabilityPipelineSpecData{
			Attributes: datadogV2.ObservabilityPipelineDataAttributes{
				Config: datadogV2.ObservabilityPipelineConfig{
					Destinations: []datadogV2.ObservabilityPipelineConfigDestinationItem{
						datadogV2.ObservabilityPipelineConfigDestinationItem{
							ObservabilityPipelineDatadogLogsDestination: &datadogV2.ObservabilityPipelineDatadogLogsDestination{
								Id: "datadog-logs-destination",
								Inputs: []string{
									"my-processor-group",
								},
								Type: datadogV2.OBSERVABILITYPIPELINEDATADOGLOGSDESTINATIONTYPE_DATADOG_LOGS,
							}},
					},
					Processors: []datadogV2.ObservabilityPipelineConfigProcessorGroup{
						{
							Enabled: true,
							Id:      "my-processor-group",
							Include: "service:my-service",
							Inputs: []string{
								"datadog-agent-source",
							},
							Processors: []datadogV2.ObservabilityPipelineConfigProcessorItem{
								datadogV2.ObservabilityPipelineConfigProcessorItem{
									ObservabilityPipelineFilterProcessor: &datadogV2.ObservabilityPipelineFilterProcessor{
										Enabled: true,
										Id:      "filter-processor",
										Include: "status:error",
										Type:    datadogV2.OBSERVABILITYPIPELINEFILTERPROCESSORTYPE_FILTER,
									}},
							},
						},
					},
					Sources: []datadogV2.ObservabilityPipelineConfigSourceItem{
						datadogV2.ObservabilityPipelineConfigSourceItem{
							ObservabilityPipelineDatadogAgentSource: &datadogV2.ObservabilityPipelineDatadogAgentSource{
								Id:   "datadog-agent-source",
								Type: datadogV2.OBSERVABILITYPIPELINEDATADOGAGENTSOURCETYPE_DATADOG_AGENT,
							}},
					},
				},
				Name: "Main Observability Pipeline",
			},
			Type: "pipelines",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreatePipeline", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewObservabilityPipelinesApi(apiClient)
	resp, r, err := api.CreatePipeline(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObservabilityPipelinesApi.CreatePipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ObservabilityPipelinesApi.CreatePipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a new pipeline returns "OK" response
```
// Create a new pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ObservabilityPipelinesApi;
import com.datadog.api.client.v2.model.ObservabilityPipeline;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfig;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigDestinationItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigProcessorGroup;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigProcessorItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigSourceItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineDataAttributes;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogAgentSource;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogAgentSourceType;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogLogsDestination;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogLogsDestinationType;
import com.datadog.api.client.v2.model.ObservabilityPipelineFilterProcessor;
import com.datadog.api.client.v2.model.ObservabilityPipelineFilterProcessorType;
import com.datadog.api.client.v2.model.ObservabilityPipelineSpec;
import com.datadog.api.client.v2.model.ObservabilityPipelineSpecData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createPipeline", true);
    ObservabilityPipelinesApi apiInstance = new ObservabilityPipelinesApi(defaultClient);

    ObservabilityPipelineSpec body =
        new ObservabilityPipelineSpec()
            .data(
                new ObservabilityPipelineSpecData()
                    .attributes(
                        new ObservabilityPipelineDataAttributes()
                            .config(
                                new ObservabilityPipelineConfig()
                                    .destinations(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigDestinationItem(
                                                new ObservabilityPipelineDatadogLogsDestination()
                                                    .id("datadog-logs-destination")
                                                    .inputs(
                                                        Collections.singletonList(
                                                            "my-processor-group"))
                                                    .type(
                                                        ObservabilityPipelineDatadogLogsDestinationType
                                                            .DATADOG_LOGS))))
                                    .processors(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigProcessorGroup()
                                                .enabled(true)
                                                .id("my-processor-group")
                                                .include("service:my-service")
                                                .inputs(
                                                    Collections.singletonList(
                                                        "datadog-agent-source"))
                                                .processors(
                                                    Collections.singletonList(
                                                        new ObservabilityPipelineConfigProcessorItem(
                                                            new ObservabilityPipelineFilterProcessor()
                                                                .enabled(true)
                                                                .id("filter-processor")
                                                                .include("status:error")
                                                                .type(
                                                                    ObservabilityPipelineFilterProcessorType
                                                                        .FILTER))))))
                                    .sources(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigSourceItem(
                                                new ObservabilityPipelineDatadogAgentSource()
                                                    .id("datadog-agent-source")
                                                    .type(
                                                        ObservabilityPipelineDatadogAgentSourceType
                                                            .DATADOG_AGENT)))))
                            .name("Main Observability Pipeline"))
                    .type("pipelines"));

    try {
      ObservabilityPipeline result = apiInstance.createPipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservabilityPipelinesApi#createPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a new pipeline returns "OK" response
```
"""
Create a new pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
    ObservabilityPipelineConfigProcessorGroup,
)
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
    ObservabilityPipelineDatadogAgentSource,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source_type import (
    ObservabilityPipelineDatadogAgentSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
    ObservabilityPipelineDatadogLogsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
    ObservabilityPipelineDatadogLogsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData

body = ObservabilityPipelineSpec(
    data=ObservabilityPipelineSpecData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                destinations=[
                    ObservabilityPipelineDatadogLogsDestination(
                        id="datadog-logs-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineDatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processors=[
                    ObservabilityPipelineConfigProcessorGroup(
                        enabled=True,
                        id="my-processor-group",
                        include="service:my-service",
                        inputs=[
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineFilterProcessor(
                                enabled=True,
                                id="filter-processor",
                                include="status:error",
                                type=ObservabilityPipelineFilterProcessorType.FILTER,
                            ),
                        ],
                    ),
                ],
                sources=[
                    ObservabilityPipelineDatadogAgentSource(
                        id="datadog-agent-source",
                        type=ObservabilityPipelineDatadogAgentSourceType.DATADOG_AGENT,
                    ),
                ],
            ),
            name="Main Observability Pipeline",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.create_pipeline(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a new pipeline returns "OK" response
```
# Create a new pipeline returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_pipeline".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ObservabilityPipelinesAPI.new

body = DatadogAPIClient::V2::ObservabilityPipelineSpec.new({
  data: DatadogAPIClient::V2::ObservabilityPipelineSpecData.new({
    attributes: DatadogAPIClient::V2::ObservabilityPipelineDataAttributes.new({
      config: DatadogAPIClient::V2::ObservabilityPipelineConfig.new({
        destinations: [
          DatadogAPIClient::V2::ObservabilityPipelineDatadogLogsDestination.new({
            id: "datadog-logs-destination",
            inputs: [
              "my-processor-group",
            ],
            type: DatadogAPIClient::V2::ObservabilityPipelineDatadogLogsDestinationType::DATADOG_LOGS,
          }),
        ],
        processors: [
          DatadogAPIClient::V2::ObservabilityPipelineConfigProcessorGroup.new({
            enabled: true,
            id: "my-processor-group",
            include: "service:my-service",
            inputs: [
              "datadog-agent-source",
            ],
            processors: [
              DatadogAPIClient::V2::ObservabilityPipelineFilterProcessor.new({
                enabled: true,
                id: "filter-processor",
                include: "status:error",
                type: DatadogAPIClient::V2::ObservabilityPipelineFilterProcessorType::FILTER,
              }),
            ],
          }),
        ],
        sources: [
          DatadogAPIClient::V2::ObservabilityPipelineDatadogAgentSource.new({
            id: "datadog-agent-source",
            type: DatadogAPIClient::V2::ObservabilityPipelineDatadogAgentSourceType::DATADOG_AGENT,
          }),
        ],
      }),
      name: "Main Observability Pipeline",
    }),
    type: "pipelines",
  }),
})
p api_instance.create_pipeline(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a new pipeline returns "OK" response
```
// Create a new pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_observability_pipelines::ObservabilityPipelinesAPI;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfig;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigDestinationItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigProcessorGroup;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigProcessorItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigSourceItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDataAttributes;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogAgentSource;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogAgentSourceType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogLogsDestination;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogLogsDestinationType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineFilterProcessor;
use datadog_api_client::datadogV2::model::ObservabilityPipelineFilterProcessorType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineSpec;
use datadog_api_client::datadogV2::model::ObservabilityPipelineSpecData;

#[tokio::main]
async fn main() {
    let body =
        ObservabilityPipelineSpec::new(
            ObservabilityPipelineSpecData::new(
                ObservabilityPipelineDataAttributes::new(
                    ObservabilityPipelineConfig::new(
                        vec![
                            ObservabilityPipelineConfigDestinationItem::ObservabilityPipelineDatadogLogsDestination(
                                Box::new(
                                    ObservabilityPipelineDatadogLogsDestination::new(
                                        "datadog-logs-destination".to_string(),
                                        vec!["my-processor-group".to_string()],
                                        ObservabilityPipelineDatadogLogsDestinationType::DATADOG_LOGS,
                                    ),
                                ),
                            )
                        ],
                        vec![
                            ObservabilityPipelineConfigSourceItem::ObservabilityPipelineDatadogAgentSource(
                                Box::new(
                                    ObservabilityPipelineDatadogAgentSource::new(
                                        "datadog-agent-source".to_string(),
                                        ObservabilityPipelineDatadogAgentSourceType::DATADOG_AGENT,
                                    ),
                                ),
                            )
                        ],
                    ).processors(
                        vec![
                            ObservabilityPipelineConfigProcessorGroup::new(
                                true,
                                "my-processor-group".to_string(),
                                "service:my-service".to_string(),
                                vec!["datadog-agent-source".to_string()],
                                vec![
                                    ObservabilityPipelineConfigProcessorItem::ObservabilityPipelineFilterProcessor(
                                        Box::new(
                                            ObservabilityPipelineFilterProcessor::new(
                                                true,
                                                "filter-processor".to_string(),
                                                "status:error".to_string(),
                                                ObservabilityPipelineFilterProcessorType::FILTER,
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ],
                    ),
                    "Main Observability Pipeline".to_string(),
                ),
                "pipelines".to_string(),
            ),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreatePipeline", true);
    let api = ObservabilityPipelinesAPI::with_config(configuration);
    let resp = api.create_pipeline(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a new pipeline returns "OK" response
```
/**
 * Create a new pipeline returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createPipeline"] = true;
const apiInstance = new v2.ObservabilityPipelinesApi(configuration);

const params: v2.ObservabilityPipelinesApiCreatePipelineRequest = {
  body: {
    data: {
      attributes: {
        config: {
          destinations: [
            {
              id: "datadog-logs-destination",
              inputs: ["my-processor-group"],
              type: "datadog_logs",
            },
          ],
          processors: [
            {
              enabled: true,
              id: "my-processor-group",
              include: "service:my-service",
              inputs: ["datadog-agent-source"],
              processors: [
                {
                  enabled: true,
                  id: "filter-processor",
                  include: "status:error",
                  type: "filter",
                },
              ],
            },
          ],
          sources: [
            {
              id: "datadog-agent-source",
              type: "datadog_agent",
            },
          ],
        },
        name: "Main Observability Pipeline",
      },
      type: "pipelines",
    },
  },
};

apiInstance
  .createPipeline(params)
  .then((data: v2.ObservabilityPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a specific pipeline](https://docs.datadoghq.com/api/latest/observability-pipelines/#get-a-specific-pipeline)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/observability-pipelines/#get-a-specific-pipeline-v2)


**Note** : This endpoint is in Preview. Fill out this [form](https://www.datadoghq.com/product-preview/observability-pipelines-api-and-terraform-support/) to request access.
GET https://api.ap1.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.ap2.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.datadoghq.eu/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.ddog-gov.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.us3.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}
### Overview
Get a specific pipeline by its ID. This endpoint requires the `observability_pipelines_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
pipeline_id [_required_]
string
The ID of the pipeline to retrieve.
### Response
  * [200](https://docs.datadoghq.com/api/latest/observability-pipelines/#GetPipeline-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/observability-pipelines/#GetPipeline-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/observability-pipelines/#GetPipeline-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Top-level schema representing a pipeline.
Expand All
Field
Type
Description
_required_]
object
Contains the pipeline’s ID, type, and configuration attributes.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
id [_required_]
string
Unique identifier for the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
```
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "filter-processor"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "display_name": "my component",
            "enabled": true,
            "id": "grouped-processors",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              []
            ]
          }
        ],
        "sources": [
          {
            "group_id": "consumer-group-0",
            "id": "kafka-source",
            "librdkafka_options": [
              {
                "name": "fetch.message.max.bytes",
                "value": "1048576"
              }
            ],
            "sasl": {
              "mechanism": "string"
            },
            "tls": {
              "ca_file": "string",
              "crt_file": "/path/to/cert.crt",
              "key_file": "string"
            },
            "topics": [
              "topic1",
              "topic2"
            ],
            "type": "kafka"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "type": "pipelines"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=typescript)


#####  Get a specific pipeline
Copy
```
                  # Path parameters  
export pipeline_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a specific pipeline
```
"""
Get a specific pipeline returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = environ["PIPELINE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.get_pipeline(
        pipeline_id=PIPELINE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a specific pipeline
```
# Get a specific pipeline returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_pipeline".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ObservabilityPipelinesAPI.new

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = ENV["PIPELINE_DATA_ID"]
p api_instance.get_pipeline(PIPELINE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a specific pipeline
```
// Get a specific pipeline returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "pipeline" in the system
	PipelineDataID := os.Getenv("PIPELINE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetPipeline", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewObservabilityPipelinesApi(apiClient)
	resp, r, err := api.GetPipeline(ctx, PipelineDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObservabilityPipelinesApi.GetPipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ObservabilityPipelinesApi.GetPipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a specific pipeline
```
// Get a specific pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ObservabilityPipelinesApi;
import com.datadog.api.client.v2.model.ObservabilityPipeline;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getPipeline", true);
    ObservabilityPipelinesApi apiInstance = new ObservabilityPipelinesApi(defaultClient);

    // there is a valid "pipeline" in the system
    String PIPELINE_DATA_ID = System.getenv("PIPELINE_DATA_ID");

    try {
      ObservabilityPipeline result = apiInstance.getPipeline(PIPELINE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservabilityPipelinesApi#getPipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a specific pipeline
```
// Get a specific pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_observability_pipelines::ObservabilityPipelinesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "pipeline" in the system
    let pipeline_data_id = std::env::var("PIPELINE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetPipeline", true);
    let api = ObservabilityPipelinesAPI::with_config(configuration);
    let resp = api.get_pipeline(pipeline_data_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a specific pipeline
```
/**
 * Get a specific pipeline returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getPipeline"] = true;
const apiInstance = new v2.ObservabilityPipelinesApi(configuration);

// there is a valid "pipeline" in the system
const PIPELINE_DATA_ID = process.env.PIPELINE_DATA_ID as string;

const params: v2.ObservabilityPipelinesApiGetPipelineRequest = {
  pipelineId: PIPELINE_DATA_ID,
};

apiInstance
  .getPipeline(params)
  .then((data: v2.ObservabilityPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a pipeline](https://docs.datadoghq.com/api/latest/observability-pipelines/#update-a-pipeline)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/observability-pipelines/#update-a-pipeline-v2)


**Note** : This endpoint is in Preview. Fill out this [form](https://www.datadoghq.com/product-preview/observability-pipelines-api-and-terraform-support/) to request access.
PUT https://api.ap1.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.ap2.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.datadoghq.eu/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.ddog-gov.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.us3.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}
### Overview
Update a pipeline. This endpoint requires the `observability_pipelines_deploy` permission.
### Arguments
#### Path Parameters
Name
Type
Description
pipeline_id [_required_]
string
The ID of the pipeline to update.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Expand All
Field
Type
Description
_required_]
object
Contains the pipeline’s ID, type, and configuration attributes.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
id [_required_]
string
Unique identifier for the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
```
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "updated-datadog-logs-destination-id",
            "inputs": [
              "my-processor-group"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "enabled": true,
            "id": "my-processor-group",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              {
                "enabled": true,
                "id": "filter-processor",
                "include": "status:error",
                "type": "filter"
              }
            ]
          }
        ],
        "sources": [
          {
            "id": "datadog-agent-source",
            "type": "datadog_agent"
          }
        ]
      },
      "name": "Updated Pipeline Name"
    },
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "type": "pipelines"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/observability-pipelines/#UpdatePipeline-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/observability-pipelines/#UpdatePipeline-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/observability-pipelines/#UpdatePipeline-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/observability-pipelines/#UpdatePipeline-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/observability-pipelines/#UpdatePipeline-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/observability-pipelines/#UpdatePipeline-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Top-level schema representing a pipeline.
Expand All
Field
Type
Description
_required_]
object
Contains the pipeline’s ID, type, and configuration attributes.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
id [_required_]
string
Unique identifier for the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
```
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "filter-processor"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "display_name": "my component",
            "enabled": true,
            "id": "grouped-processors",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              []
            ]
          }
        ],
        "sources": [
          {
            "group_id": "consumer-group-0",
            "id": "kafka-source",
            "librdkafka_options": [
              {
                "name": "fetch.message.max.bytes",
                "value": "1048576"
              }
            ],
            "sasl": {
              "mechanism": "string"
            },
            "tls": {
              "ca_file": "string",
              "crt_file": "/path/to/cert.crt",
              "key_file": "string"
            },
            "topics": [
              "topic1",
              "topic2"
            ],
            "type": "kafka"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "type": "pipelines"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=typescript)


#####  Update a pipeline returns "OK" response
Copy
```
                          # Path parameters  
export pipeline_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/${pipeline_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "updated-datadog-logs-destination-id",
            "inputs": [
              "my-processor-group"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "enabled": true,
            "id": "my-processor-group",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              {
                "enabled": true,
                "id": "filter-processor",
                "include": "status:error",
                "type": "filter"
              }
            ]
          }
        ],
        "sources": [
          {
            "id": "datadog-agent-source",
            "type": "datadog_agent"
          }
        ]
      },
      "name": "Updated Pipeline Name"
    },
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "type": "pipelines"
  }
}
EOF  

                        
```

#####  Update a pipeline returns "OK" response
```
// Update a pipeline returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "pipeline" in the system
	PipelineDataID := os.Getenv("PIPELINE_DATA_ID")

	body := datadogV2.ObservabilityPipeline{
		Data: datadogV2.ObservabilityPipelineData{
			Attributes: datadogV2.ObservabilityPipelineDataAttributes{
				Config: datadogV2.ObservabilityPipelineConfig{
					Destinations: []datadogV2.ObservabilityPipelineConfigDestinationItem{
						datadogV2.ObservabilityPipelineConfigDestinationItem{
							ObservabilityPipelineDatadogLogsDestination: &datadogV2.ObservabilityPipelineDatadogLogsDestination{
								Id: "updated-datadog-logs-destination-id",
								Inputs: []string{
									"my-processor-group",
								},
								Type: datadogV2.OBSERVABILITYPIPELINEDATADOGLOGSDESTINATIONTYPE_DATADOG_LOGS,
							}},
					},
					Processors: []datadogV2.ObservabilityPipelineConfigProcessorGroup{
						{
							Enabled: true,
							Id:      "my-processor-group",
							Include: "service:my-service",
							Inputs: []string{
								"datadog-agent-source",
							},
							Processors: []datadogV2.ObservabilityPipelineConfigProcessorItem{
								datadogV2.ObservabilityPipelineConfigProcessorItem{
									ObservabilityPipelineFilterProcessor: &datadogV2.ObservabilityPipelineFilterProcessor{
										Enabled: true,
										Id:      "filter-processor",
										Include: "status:error",
										Type:    datadogV2.OBSERVABILITYPIPELINEFILTERPROCESSORTYPE_FILTER,
									}},
							},
						},
					},
					Sources: []datadogV2.ObservabilityPipelineConfigSourceItem{
						datadogV2.ObservabilityPipelineConfigSourceItem{
							ObservabilityPipelineDatadogAgentSource: &datadogV2.ObservabilityPipelineDatadogAgentSource{
								Id:   "datadog-agent-source",
								Type: datadogV2.OBSERVABILITYPIPELINEDATADOGAGENTSOURCETYPE_DATADOG_AGENT,
							}},
					},
				},
				Name: "Updated Pipeline Name",
			},
			Id:   PipelineDataID,
			Type: "pipelines",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdatePipeline", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewObservabilityPipelinesApi(apiClient)
	resp, r, err := api.UpdatePipeline(ctx, PipelineDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObservabilityPipelinesApi.UpdatePipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ObservabilityPipelinesApi.UpdatePipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a pipeline returns "OK" response
```
// Update a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ObservabilityPipelinesApi;
import com.datadog.api.client.v2.model.ObservabilityPipeline;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfig;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigDestinationItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigProcessorGroup;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigProcessorItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigSourceItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineData;
import com.datadog.api.client.v2.model.ObservabilityPipelineDataAttributes;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogAgentSource;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogAgentSourceType;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogLogsDestination;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogLogsDestinationType;
import com.datadog.api.client.v2.model.ObservabilityPipelineFilterProcessor;
import com.datadog.api.client.v2.model.ObservabilityPipelineFilterProcessorType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updatePipeline", true);
    ObservabilityPipelinesApi apiInstance = new ObservabilityPipelinesApi(defaultClient);

    // there is a valid "pipeline" in the system
    String PIPELINE_DATA_ID = System.getenv("PIPELINE_DATA_ID");

    ObservabilityPipeline body =
        new ObservabilityPipeline()
            .data(
                new ObservabilityPipelineData()
                    .attributes(
                        new ObservabilityPipelineDataAttributes()
                            .config(
                                new ObservabilityPipelineConfig()
                                    .destinations(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigDestinationItem(
                                                new ObservabilityPipelineDatadogLogsDestination()
                                                    .id("updated-datadog-logs-destination-id")
                                                    .inputs(
                                                        Collections.singletonList(
                                                            "my-processor-group"))
                                                    .type(
                                                        ObservabilityPipelineDatadogLogsDestinationType
                                                            .DATADOG_LOGS))))
                                    .processors(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigProcessorGroup()
                                                .enabled(true)
                                                .id("my-processor-group")
                                                .include("service:my-service")
                                                .inputs(
                                                    Collections.singletonList(
                                                        "datadog-agent-source"))
                                                .processors(
                                                    Collections.singletonList(
                                                        new ObservabilityPipelineConfigProcessorItem(
                                                            new ObservabilityPipelineFilterProcessor()
                                                                .enabled(true)
                                                                .id("filter-processor")
                                                                .include("status:error")
                                                                .type(
                                                                    ObservabilityPipelineFilterProcessorType
                                                                        .FILTER))))))
                                    .sources(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigSourceItem(
                                                new ObservabilityPipelineDatadogAgentSource()
                                                    .id("datadog-agent-source")
                                                    .type(
                                                        ObservabilityPipelineDatadogAgentSourceType
                                                            .DATADOG_AGENT)))))
                            .name("Updated Pipeline Name"))
                    .id(PIPELINE_DATA_ID)
                    .type("pipelines"));

    try {
      ObservabilityPipeline result = apiInstance.updatePipeline(PIPELINE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservabilityPipelinesApi#updatePipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a pipeline returns "OK" response
```
"""
Update a pipeline returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline import ObservabilityPipeline
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
    ObservabilityPipelineConfigProcessorGroup,
)
from datadog_api_client.v2.model.observability_pipeline_data import ObservabilityPipelineData
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
    ObservabilityPipelineDatadogAgentSource,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source_type import (
    ObservabilityPipelineDatadogAgentSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
    ObservabilityPipelineDatadogLogsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
    ObservabilityPipelineDatadogLogsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = environ["PIPELINE_DATA_ID"]

body = ObservabilityPipeline(
    data=ObservabilityPipelineData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                destinations=[
                    ObservabilityPipelineDatadogLogsDestination(
                        id="updated-datadog-logs-destination-id",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineDatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processors=[
                    ObservabilityPipelineConfigProcessorGroup(
                        enabled=True,
                        id="my-processor-group",
                        include="service:my-service",
                        inputs=[
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineFilterProcessor(
                                enabled=True,
                                id="filter-processor",
                                include="status:error",
                                type=ObservabilityPipelineFilterProcessorType.FILTER,
                            ),
                        ],
                    ),
                ],
                sources=[
                    ObservabilityPipelineDatadogAgentSource(
                        id="datadog-agent-source",
                        type=ObservabilityPipelineDatadogAgentSourceType.DATADOG_AGENT,
                    ),
                ],
            ),
            name="Updated Pipeline Name",
        ),
        id=PIPELINE_DATA_ID,
        type="pipelines",
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.update_pipeline(pipeline_id=PIPELINE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a pipeline returns "OK" response
```
# Update a pipeline returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_pipeline".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ObservabilityPipelinesAPI.new

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = ENV["PIPELINE_DATA_ID"]

body = DatadogAPIClient::V2::ObservabilityPipeline.new({
  data: DatadogAPIClient::V2::ObservabilityPipelineData.new({
    attributes: DatadogAPIClient::V2::ObservabilityPipelineDataAttributes.new({
      config: DatadogAPIClient::V2::ObservabilityPipelineConfig.new({
        destinations: [
          DatadogAPIClient::V2::ObservabilityPipelineDatadogLogsDestination.new({
            id: "updated-datadog-logs-destination-id",
            inputs: [
              "my-processor-group",
            ],
            type: DatadogAPIClient::V2::ObservabilityPipelineDatadogLogsDestinationType::DATADOG_LOGS,
          }),
        ],
        processors: [
          DatadogAPIClient::V2::ObservabilityPipelineConfigProcessorGroup.new({
            enabled: true,
            id: "my-processor-group",
            include: "service:my-service",
            inputs: [
              "datadog-agent-source",
            ],
            processors: [
              DatadogAPIClient::V2::ObservabilityPipelineFilterProcessor.new({
                enabled: true,
                id: "filter-processor",
                include: "status:error",
                type: DatadogAPIClient::V2::ObservabilityPipelineFilterProcessorType::FILTER,
              }),
            ],
          }),
        ],
        sources: [
          DatadogAPIClient::V2::ObservabilityPipelineDatadogAgentSource.new({
            id: "datadog-agent-source",
            type: DatadogAPIClient::V2::ObservabilityPipelineDatadogAgentSourceType::DATADOG_AGENT,
          }),
        ],
      }),
      name: "Updated Pipeline Name",
    }),
    id: PIPELINE_DATA_ID,
    type: "pipelines",
  }),
})
p api_instance.update_pipeline(PIPELINE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a pipeline returns "OK" response
```
// Update a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_observability_pipelines::ObservabilityPipelinesAPI;
use datadog_api_client::datadogV2::model::ObservabilityPipeline;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfig;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigDestinationItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigProcessorGroup;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigProcessorItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigSourceItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineData;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDataAttributes;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogAgentSource;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogAgentSourceType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogLogsDestination;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogLogsDestinationType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineFilterProcessor;
use datadog_api_client::datadogV2::model::ObservabilityPipelineFilterProcessorType;

#[tokio::main]
async fn main() {
    // there is a valid "pipeline" in the system
    let pipeline_data_id = std::env::var("PIPELINE_DATA_ID").unwrap();
    let body =
        ObservabilityPipeline::new(
            ObservabilityPipelineData::new(
                ObservabilityPipelineDataAttributes::new(
                    ObservabilityPipelineConfig::new(
                        vec![
                            ObservabilityPipelineConfigDestinationItem::ObservabilityPipelineDatadogLogsDestination(
                                Box::new(
                                    ObservabilityPipelineDatadogLogsDestination::new(
                                        "updated-datadog-logs-destination-id".to_string(),
                                        vec!["my-processor-group".to_string()],
                                        ObservabilityPipelineDatadogLogsDestinationType::DATADOG_LOGS,
                                    ),
                                ),
                            )
                        ],
                        vec![
                            ObservabilityPipelineConfigSourceItem::ObservabilityPipelineDatadogAgentSource(
                                Box::new(
                                    ObservabilityPipelineDatadogAgentSource::new(
                                        "datadog-agent-source".to_string(),
                                        ObservabilityPipelineDatadogAgentSourceType::DATADOG_AGENT,
                                    ),
                                ),
                            )
                        ],
                    ).processors(
                        vec![
                            ObservabilityPipelineConfigProcessorGroup::new(
                                true,
                                "my-processor-group".to_string(),
                                "service:my-service".to_string(),
                                vec!["datadog-agent-source".to_string()],
                                vec![
                                    ObservabilityPipelineConfigProcessorItem::ObservabilityPipelineFilterProcessor(
                                        Box::new(
                                            ObservabilityPipelineFilterProcessor::new(
                                                true,
                                                "filter-processor".to_string(),
                                                "status:error".to_string(),
                                                ObservabilityPipelineFilterProcessorType::FILTER,
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ],
                    ),
                    "Updated Pipeline Name".to_string(),
                ),
                pipeline_data_id.clone(),
                "pipelines".to_string(),
            ),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdatePipeline", true);
    let api = ObservabilityPipelinesAPI::with_config(configuration);
    let resp = api.update_pipeline(pipeline_data_id.clone(), body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a pipeline returns "OK" response
```
/**
 * Update a pipeline returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updatePipeline"] = true;
const apiInstance = new v2.ObservabilityPipelinesApi(configuration);

// there is a valid "pipeline" in the system
const PIPELINE_DATA_ID = process.env.PIPELINE_DATA_ID as string;

const params: v2.ObservabilityPipelinesApiUpdatePipelineRequest = {
  body: {
    data: {
      attributes: {
        config: {
          destinations: [
            {
              id: "updated-datadog-logs-destination-id",
              inputs: ["my-processor-group"],
              type: "datadog_logs",
            },
          ],
          processors: [
            {
              enabled: true,
              id: "my-processor-group",
              include: "service:my-service",
              inputs: ["datadog-agent-source"],
              processors: [
                {
                  enabled: true,
                  id: "filter-processor",
                  include: "status:error",
                  type: "filter",
                },
              ],
            },
          ],
          sources: [
            {
              id: "datadog-agent-source",
              type: "datadog_agent",
            },
          ],
        },
        name: "Updated Pipeline Name",
      },
      id: PIPELINE_DATA_ID,
      type: "pipelines",
    },
  },
  pipelineId: PIPELINE_DATA_ID,
};

apiInstance
  .updatePipeline(params)
  .then((data: v2.ObservabilityPipeline) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a pipeline](https://docs.datadoghq.com/api/latest/observability-pipelines/#delete-a-pipeline)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/observability-pipelines/#delete-a-pipeline-v2)


**Note** : This endpoint is in Preview. Fill out this [form](https://www.datadoghq.com/product-preview/observability-pipelines-api-and-terraform-support/) to request access.
DELETE https://api.ap1.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.ap2.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.datadoghq.eu/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.ddog-gov.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.us3.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}
### Overview
Delete a pipeline. This endpoint requires the `observability_pipelines_delete` permission.
### Arguments
#### Path Parameters
Name
Type
Description
pipeline_id [_required_]
string
The ID of the pipeline to delete.
### Response
  * [204](https://docs.datadoghq.com/api/latest/observability-pipelines/#DeletePipeline-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/observability-pipelines/#DeletePipeline-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/observability-pipelines/#DeletePipeline-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/observability-pipelines/#DeletePipeline-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/observability-pipelines/#DeletePipeline-429-v2)


OK
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=typescript)


#####  Delete a pipeline
Copy
```
                  # Path parameters  
export pipeline_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/${pipeline_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a pipeline
```
"""
Delete a pipeline returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = environ["PIPELINE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    api_instance.delete_pipeline(
        pipeline_id=PIPELINE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a pipeline
```
# Delete a pipeline returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_pipeline".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ObservabilityPipelinesAPI.new

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = ENV["PIPELINE_DATA_ID"]
api_instance.delete_pipeline(PIPELINE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a pipeline
```
// Delete a pipeline returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "pipeline" in the system
	PipelineDataID := os.Getenv("PIPELINE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeletePipeline", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewObservabilityPipelinesApi(apiClient)
	r, err := api.DeletePipeline(ctx, PipelineDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObservabilityPipelinesApi.DeletePipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a pipeline
```
// Delete a pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ObservabilityPipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deletePipeline", true);
    ObservabilityPipelinesApi apiInstance = new ObservabilityPipelinesApi(defaultClient);

    // there is a valid "pipeline" in the system
    String PIPELINE_DATA_ID = System.getenv("PIPELINE_DATA_ID");

    try {
      apiInstance.deletePipeline(PIPELINE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservabilityPipelinesApi#deletePipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a pipeline
```
// Delete a pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_observability_pipelines::ObservabilityPipelinesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "pipeline" in the system
    let pipeline_data_id = std::env::var("PIPELINE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeletePipeline", true);
    let api = ObservabilityPipelinesAPI::with_config(configuration);
    let resp = api.delete_pipeline(pipeline_data_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a pipeline
```
/**
 * Delete a pipeline returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deletePipeline"] = true;
const apiInstance = new v2.ObservabilityPipelinesApi(configuration);

// there is a valid "pipeline" in the system
const PIPELINE_DATA_ID = process.env.PIPELINE_DATA_ID as string;

const params: v2.ObservabilityPipelinesApiDeletePipelineRequest = {
  pipelineId: PIPELINE_DATA_ID,
};

apiInstance
  .deletePipeline(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Validate an observability pipeline](https://docs.datadoghq.com/api/latest/observability-pipelines/#validate-an-observability-pipeline)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/observability-pipelines/#validate-an-observability-pipeline-v2)


**Note** : This endpoint is in Preview. Fill out this [form](https://www.datadoghq.com/product-preview/observability-pipelines-api-and-terraform-support/) to request access.
POST https://api.ap1.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/validatehttps://api.ap2.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/validatehttps://api.datadoghq.eu/api/v2/remote_config/products/obs_pipelines/pipelines/validatehttps://api.ddog-gov.com/api/v2/remote_config/products/obs_pipelines/pipelines/validatehttps://api.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/validatehttps://api.us3.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/validatehttps://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/validate
### Overview
Validates a pipeline configuration without creating or updating any resources. Returns a list of validation errors, if any. This endpoint requires the `observability_pipelines_read` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Expand All
Field
Type
Description
_required_]
object
Contains the the pipeline configuration.
_required_]
object
Defines the pipeline’s name and its components (sources, processors, and destinations).
_required_]
object
Specifies the pipeline's configuration, including its sources, processors, and destinations.
_required_]
[ <oneOf>]
A list of destination components where processed logs are sent.
object
The `datadog_logs` destination forwards logs to Datadog Log Management.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `datadog_logs`. Allowed enum values: `datadog_logs`
default: `datadog_logs`
object
The `amazon_s3` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
S3 bucket name.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys.
region [_required_]
string
AWS region of the S3 bucket.
storage_class [_required_]
enum
S3 storage class. Allowed enum values: `STANDARD,REDUCED_REDUNDANCY,INTELLIGENT_TIERING,STANDARD_IA,EXPRESS_ONEZONE,ONEZONE_IA,GLACIER,GLACIER_IR,DEEP_ARCHIVE`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `google_cloud_storage` destination stores logs in a Google Cloud Storage (GCS) bucket. It requires a bucket name, GCP authentication, and metadata fields.
acl
enum
Access control list setting for objects written to the bucket. Allowed enum values: `private,project-private,public-read,authenticated-read,bucket-owner-read,bucket-owner-full-control`
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
bucket [_required_]
string
Name of the GCS bucket.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
key_prefix
string
Optional prefix for object keys within the GCS bucket.
[object]
Custom metadata to attach to each object uploaded to the GCS bucket.
name [_required_]
string
The metadata key.
value [_required_]
string
The metadata value.
storage_class [_required_]
enum
Storage class used for objects stored in GCS. Allowed enum values: `STANDARD,NEARLINE,COLDLINE,ARCHIVE`
type [_required_]
enum
The destination type. Always `google_cloud_storage`. Allowed enum values: `google_cloud_storage`
default: `google_cloud_storage`
object
The `splunk_hec` destination forwards logs to Splunk using the HTTP Event Collector (HEC).
auto_extract_timestamp
boolean
If `true`, Splunk tries to extract timestamps from incoming log events. If `false`, Splunk assigns the time the event was received.
encoding
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
index
string
Optional name of the Splunk index where logs are written.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
sourcetype
string
The Splunk sourcetype to assign to log events.
type [_required_]
enum
The destination type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `sumo_logic` destination forwards logs to Sumo Logic.
encoding
enum
The output encoding format. Allowed enum values: `json,raw_message,logfmt`
[object]
A list of custom headers to include in the request to Sumo Logic.
name [_required_]
string
The header field name.
value [_required_]
string
The header field value.
header_host_name
string
Optional override for the host name header.
header_source_category
string
Optional override for the source category header.
header_source_name
string
Optional override for the source name header.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `elasticsearch` destination writes logs to an Elasticsearch cluster.
api_version
enum
The Elasticsearch API version to use. Set to `auto` to auto-detect. Allowed enum values: `auto,v6,v7,v8`
bulk_index
string
The index to write logs to in Elasticsearch.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `elasticsearch`. Allowed enum values: `elasticsearch`
default: `elasticsearch`
object
The `rsyslog` destination forwards logs to an external `rsyslog` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` destination forwards logs to an external `syslog-ng` server over TCP or UDP using the syslog protocol.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
keepalive
int64
Optional socket keepalive duration in milliseconds.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `azure_storage` destination forwards logs to an Azure Blob Storage container.
blob_prefix
string
Optional prefix for blobs written to the container.
container_name [_required_]
string
The name of the Azure Blob Storage container to store logs in.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `azure_storage`. Allowed enum values: `azure_storage`
default: `azure_storage`
object
The `microsoft_sentinel` destination forwards logs to Microsoft Sentinel.
client_id [_required_]
string
Azure AD client ID used for authentication.
dcr_immutable_id [_required_]
string
The immutable ID of the Data Collection Rule (DCR).
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
table [_required_]
string
The name of the Log Analytics table where logs are sent.
tenant_id [_required_]
string
Azure AD tenant ID.
type [_required_]
enum
The destination type. The value should always be `microsoft_sentinel`. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
object
The `google_chronicle` destination sends logs to Google Chronicle.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
customer_id [_required_]
string
The Google Chronicle customer ID.
encoding
enum
The encoding format for the logs sent to Chronicle. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
log_type
string
The log type metadata associated with the Chronicle destination.
type [_required_]
enum
The destination type. The value should always be `google_chronicle`. Allowed enum values: `google_chronicle`
default: `google_chronicle`
object
The `new_relic` destination sends logs to the New Relic platform.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The New Relic region. Allowed enum values: `us,eu`
type [_required_]
enum
The destination type. The value should always be `new_relic`. Allowed enum values: `new_relic`
default: `new_relic`
object
The `sentinel_one` destination sends logs to SentinelOne.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
enum
The SentinelOne region to send logs to. Allowed enum values: `us,eu,ca,data_set_us`
type [_required_]
enum
The destination type. The value should always be `sentinel_one`. Allowed enum values: `sentinel_one`
default: `sentinel_one`
object
The `opensearch` destination writes logs to an OpenSearch cluster.
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `opensearch`. Allowed enum values: `opensearch`
default: `opensearch`
object
The `amazon_opensearch` destination writes logs to Amazon OpenSearch.
_required_]
object
Authentication settings for the Amazon OpenSearch destination. The `strategy` field determines whether basic or AWS-based authentication is used.
assume_role
string
The ARN of the role to assume (used with `aws` strategy).
aws_region
string
AWS region
external_id
string
External ID for the assumed role (used with `aws` strategy).
session_name
string
Session name for the assumed role (used with `aws` strategy).
strategy [_required_]
enum
The authentication strategy to use. Allowed enum values: `basic,aws`
bulk_index
string
The index to write logs to.
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
type [_required_]
enum
The destination type. The value should always be `amazon_opensearch`. Allowed enum values: `amazon_opensearch`
default: `amazon_opensearch`
object
The `socket` destination sends logs over TCP or UDP to a remote server.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
_required_]
<oneOf>
Framing method configuration.
object
Each log event is delimited by a newline character.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingNewlineDelimitedMethod` object. Allowed enum values: `newline_delimited`
object
Event data is not delimited at all.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object. Allowed enum values: `bytes`
object
Each log event is separated using the specified delimiter character.
delimiter [_required_]
string
A single ASCII character used as a delimiter.
method [_required_]
enum
The definition of `ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod` object. Allowed enum values: `character_delimited`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
mode [_required_]
enum
Protocol used to send logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
object
The `amazon_security_lake` destination sends your logs to Amazon Security Lake.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
bucket [_required_]
string
Name of the Amazon S3 bucket in Security Lake (3-63 characters).
custom_source_name [_required_]
string
Custom source name for the logs in Security Lake.
id [_required_]
string
Unique identifier for the destination component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
region [_required_]
string
AWS region of the S3 bucket.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. Always `amazon_security_lake`. Allowed enum values: `amazon_security_lake`
default: `amazon_security_lake`
object
The `crowdstrike_next_gen_siem` destination forwards logs to CrowdStrike Next Gen SIEM.
object
Compression configuration for log events.
algorithm [_required_]
enum
Compression algorithm for log events. Allowed enum values: `gzip,zlib`
level
int64
Compression level.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The destination type. The value should always be `crowdstrike_next_gen_siem`. Allowed enum values: `crowdstrike_next_gen_siem`
default: `crowdstrike_next_gen_siem`
object
The `google_pubsub` destination publishes logs to a Google Cloud Pub/Sub topic.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
encoding [_required_]
enum
Encoding format for log events. Allowed enum values: `json,raw_message`
id [_required_]
string
The unique identifier for this component.
inputs [_required_]
[string]
A list of component IDs whose output is used as the `input` for this component.
project [_required_]
string
The GCP project ID that owns the Pub/Sub topic.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topic [_required_]
string
The Pub/Sub topic name to publish logs to.
type [_required_]
enum
The destination type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
[object]
A list of processor groups that transform or enrich log data.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor group is enabled.
id [_required_]
string
The unique identifier for the processor group.
include [_required_]
string
Conditional expression for when this processor group should execute.
inputs [_required_]
[string]
A list of IDs for components whose output is used as the input for this processor group.
_required_]
[ <oneOf>]
Processors applied sequentially within this group. Events flow through each processor in order.
object
The `filter` processor allows conditional processing of logs based on a Datadog search query. Logs that match the `include` query are passed through; others are discarded.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
type [_required_]
enum
The processor type. The value should always be `filter`. Allowed enum values: `filter`
default: `filter`
object
The `parse_json` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
field [_required_]
string
The name of the log field that contains a JSON string.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `parse_json`. Allowed enum values: `parse_json`
default: `parse_json`
object
The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.
display_name
string
The display name for a component.
drop_events
boolean
If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
ignore_when_missing_partitions
boolean
If `true`, the processor skips quota checks when partition fields are missing from the logs.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
name [_required_]
string
Name of the quota.
overflow_action
enum
The action to take when the quota is exceeded. Options:
  * `drop`: Drop the event.
  * `no_action`: Let the event pass through.
  * `overflow_routing`: Route to an overflow destination. Allowed enum values: `drop,no_action,overflow_routing`


[object]
A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
_required_]
[object]
A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
_required_]
object
The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
enforce [_required_]
enum
Unit for quota enforcement in bytes for data size or events for count. Allowed enum values: `bytes,events`
limit [_required_]
int64
The limit for quota enforcement.
partition_fields
[string]
A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
type [_required_]
enum
The processor type. The value should always be `quota`. Allowed enum values: `quota`
default: `quota`
object
The `add_fields` processor adds static key-value fields to logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of static fields (key-value pairs) that is added to each log event processed by this component.
name [_required_]
string
The field name.
value [_required_]
string
The field value.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_fields`. Allowed enum values: `add_fields`
default: `add_fields`
object
The `remove_fields` processor deletes specified fields from logs.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of field names to be removed from each log event.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `remove_fields`. Allowed enum values: `remove_fields`
default: `remove_fields`
object
The `rename_fields` processor changes field names.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
_required_]
[object]
A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
destination [_required_]
string
The field name to assign the renamed value to.
preserve_source [_required_]
boolean
Indicates whether the original field, that is received from the source, should be kept (`true`) or removed (`false`) after renaming.
source [_required_]
string
The original field name in the log event that should be renamed.
id [_required_]
string
A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `rename_fields`. Allowed enum values: `rename_fields`
default: `rename_fields`
object
The `generate_datadog_metrics` processor creates custom metrics from logs and sends them to Datadog. Metrics can be counters, gauges, or distributions and optionally grouped by log fields.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include
string
A Datadog search query used to determine which logs this processor targets.
[object]
Configuration for generating individual metrics.
group_by
[string]
Optional fields used to group the metric series.
include [_required_]
string
Datadog filter query to match logs for metric generation.
metric_type [_required_]
enum
Type of metric to create. Allowed enum values: `count,gauge,distribution`
name [_required_]
string
Name of the custom metric to be created.
_required_]
<oneOf>
Specifies how the value of the generated metric is computed.
object
Strategy that increments a generated metric by one for each matching event.
strategy [_required_]
enum
Increments the metric by 1 for each matching event. Allowed enum values: `increment_by_one`
object
Strategy that increments a generated metric based on the value of a log field.
field [_required_]
string
Name of the log field containing the numeric value to increment the metric by.
strategy [_required_]
enum
Uses a numeric field in the log event as the metric increment. Allowed enum values: `increment_by_field`
type [_required_]
enum
The processor type. Always `generate_datadog_metrics`. Allowed enum values: `generate_datadog_metrics`
default: `generate_datadog_metrics`
object
The `sample` processor allows probabilistic sampling of logs at a fixed rate.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
percentage
double
The percentage of logs to sample.
rate
int64
Number of events to sample (1 in N).
type [_required_]
enum
The processor type. The value should always be `sample`. Allowed enum values: `sample`
default: `sample`
object
The `parse_grok` processor extracts structured fields from unstructured log messages using Grok patterns.
disable_library_rules
boolean
If set to `true`, disables the default Grok rules provided by Datadog.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
A unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
_required_]
[object]
A list of Grok parsing rules that define how to extract fields from the source field. Each rule must contain a name and a valid Grok pattern.
name [_required_]
string
The name of the rule.
rule [_required_]
string
The definition of the Grok rule.
source [_required_]
string
The name of the field in the log event to apply the Grok rules to.
[object]
A list of Grok helper rules that can be referenced by the parsing rules.
name [_required_]
string
The name of the Grok helper rule.
rule [_required_]
string
The definition of the Grok helper rule.
type [_required_]
enum
The processor type. The value should always be `parse_grok`. Allowed enum values: `parse_grok`
default: `parse_grok`
object
The `sensitive_data_scanner` processor detects and optionally redacts sensitive data in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of rules for identifying and acting on sensitive data patterns.
object
Configuration for keywords used to reinforce sensitive data pattern detection.
keywords [_required_]
[string]
A list of keywords to match near the sensitive pattern.
proximity [_required_]
int64
Maximum number of tokens between a keyword and a sensitive value match.
name [_required_]
string
A name identifying the rule.
_required_]
<oneOf>
Defines what action to take when sensitive data is matched.
object
Configuration for completely redacting matched sensitive data.
action [_required_]
enum
Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility. Allowed enum values: `redact`
_required_]
object
Configuration for fully redacting sensitive data.
replace [_required_]
string
The `ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions` `replace`.
object
Configuration for hashing matched sensitive values.
action [_required_]
enum
Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content. Allowed enum values: `hash`
options
object
The `ObservabilityPipelineSensitiveDataScannerProcessorActionHash` `options`.
object
Configuration for partially redacting matched sensitive data.
action [_required_]
enum
Action type that redacts part of the sensitive data while preserving a configurable number of characters, typically used for masking purposes (e.g., show last 4 digits of a credit card). Allowed enum values: `partial_redact`
_required_]
object
Controls how partial redaction is applied, including character count and direction.
characters [_required_]
int64
The `ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions` `characters`.
direction [_required_]
enum
Indicates whether to redact characters from the first or last part of the matched value. Allowed enum values: `first,last`
_required_]
<oneOf>
Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
object
Defines a custom regex-based pattern for identifying sensitive data in logs.
_required_]
object
Options for defining a custom regex pattern.
rule [_required_]
string
A regular expression used to detect sensitive values. Must be a valid regex.
type [_required_]
enum
Indicates a custom regular expression is used for matching. Allowed enum values: `custom`
object
Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.
_required_]
object
Options for selecting a predefined library pattern and enabling keyword support.
id [_required_]
string
Identifier for a predefined pattern from the sensitive data scanner pattern library.
use_recommended_keywords
boolean
Whether to augment the pattern with recommended keywords (optional).
type [_required_]
enum
Indicates that a predefined library pattern is used. Allowed enum values: `library`
_required_]
<oneOf>
Determines which parts of the log the pattern-matching rule should be applied to.
object
Includes only specific fields for sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Applies the rule only to included fields. Allowed enum values: `include`
object
Excludes specific fields from sensitive data scanning.
_required_]
object
Fields to which the scope rule applies.
fields [_required_]
[string]
The `ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions` `fields`.
target [_required_]
enum
Excludes specific fields from processing. Allowed enum values: `exclude`
object
Applies scanning across all available fields.
target [_required_]
enum
Applies the rule to all fields. Allowed enum values: `all`
tags [_required_]
[string]
Tags assigned to this rule for filtering and classification.
type [_required_]
enum
The processor type. The value should always be `sensitive_data_scanner`. Allowed enum values: `sensitive_data_scanner`
default: `sensitive_data_scanner`
object
The `ocsf_mapper` processor transforms logs into the OCSF schema using a predefined mapping configuration.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
A list of mapping rules to convert events to the OCSF format.
include [_required_]
string
A Datadog search query used to select the logs that this mapping should apply to.
_required_]
<oneOf>
Defines a single mapping rule for transforming logs into the OCSF schema.
Option 1
enum
Predefined library mappings for common log formats. Allowed enum values: `CloudTrail Account Change,GCP Cloud Audit CreateBucket,GCP Cloud Audit CreateSink,GCP Cloud Audit SetIamPolicy,GCP Cloud Audit UpdateSink,Github Audit Log API Activity,Google Workspace Admin Audit addPrivilege,Microsoft 365 Defender Incident,Microsoft 365 Defender UserLoggedIn,Okta System Log Authentication,Palo Alto Networks Firewall Traffic`
type [_required_]
enum
The processor type. The value should always be `ocsf_mapper`. Allowed enum values: `ocsf_mapper`
default: `ocsf_mapper`
object
The `add_env_vars` processor adds environment variable values to log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this processor in the pipeline.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
type [_required_]
enum
The processor type. The value should always be `add_env_vars`. Allowed enum values: `add_env_vars`
default: `add_env_vars`
_required_]
[object]
A list of environment variable mappings to apply to log fields.
field [_required_]
string
The target field in the log event.
name [_required_]
string
The name of the environment variable to read.
object
The `dedupe` processor removes duplicate fields in log events.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
fields [_required_]
[string]
A list of log field paths to check for duplicates.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
mode [_required_]
enum
The deduplication mode to apply to the fields. Allowed enum values: `match,ignore`
type [_required_]
enum
The processor type. The value should always be `dedupe`. Allowed enum values: `dedupe`
default: `dedupe`
object
The `enrichment_table` processor enriches logs using a static CSV file or GeoIP database.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
object
Defines a static enrichment table loaded from a CSV file.
_required_]
object
File encoding format.
delimiter [_required_]
string
The `encoding` `delimiter`.
includes_headers [_required_]
boolean
The `encoding` `includes_headers`.
type [_required_]
enum
Specifies the encoding format (e.g., CSV) used for enrichment tables. Allowed enum values: `csv`
_required_]
[object]
Key fields used to look up enrichment values.
column [_required_]
string
The `items` `column`.
comparison [_required_]
enum
Defines how to compare key fields for enrichment table lookups. Allowed enum values: `equals`
field [_required_]
string
The `items` `field`.
path [_required_]
string
Path to the CSV file.
_required_]
[object]
Schema defining column names and their types.
column [_required_]
string
The `items` `column`.
type [_required_]
enum
Declares allowed data types for enrichment table columns. Allowed enum values: `string,boolean,integer,float,date,timestamp`
object
Uses a GeoIP database to enrich logs based on an IP field.
key_field [_required_]
string
Path to the IP field in the log.
locale [_required_]
string
Locale used to resolve geographical names.
path [_required_]
string
Path to the GeoIP database file.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
target [_required_]
string
Path where enrichment results should be stored in the log.
type [_required_]
enum
The processor type. The value should always be `enrichment_table`. Allowed enum values: `enrichment_table`
default: `enrichment_table`
object
The `reduce` processor aggregates and merges logs based on matching keys and merge strategies.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by [_required_]
[string]
A list of fields used to group log events for merging.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
_required_]
[object]
List of merge strategies defining how values from grouped events should be combined.
path [_required_]
string
The field path in the log event.
strategy [_required_]
enum
The merge strategy to apply. Allowed enum values: `discard,retain,sum,max,min,array,concat,concat_newline,concat_raw,shortest_array,longest_array,flat_unique`
type [_required_]
enum
The processor type. The value should always be `reduce`. Allowed enum values: `reduce`
default: `reduce`
object
The `throttle` processor limits the number of events that pass through over a given time window.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
group_by
[string]
Optional list of fields used to group events before the threshold has been reached.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
threshold [_required_]
int64
the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
type [_required_]
enum
The processor type. The value should always be `throttle`. Allowed enum values: `throttle`
default: `throttle`
window [_required_]
double
The time window in seconds over which the threshold applies.
object
The `custom_processor` processor transforms events using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/) scripts with advanced filtering capabilities.
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this processor.
include [_required_]
string
A Datadog search query used to determine which logs this processor targets. This field should always be set to `*` for the custom_processor processor.
default: `*`
_required_]
[object]
Array of VRL remap rules.
drop_on_error [_required_]
boolean
Whether to drop events that caused errors during processing.
enabled
boolean
Whether this remap rule is enabled.
include [_required_]
string
A Datadog search query used to filter events for this specific remap rule.
name [_required_]
string
A descriptive name for this remap rule.
source [_required_]
string
The VRL script source code that defines the processing logic.
type [_required_]
enum
The processor type. The value should always be `custom_processor`. Allowed enum values: `custom_processor`
default: `custom_processor`
object
The `datadog_tags` processor includes or excludes specific Datadog tags in your logs.
action [_required_]
enum
The action to take on tags with matching keys. Allowed enum values: `include,exclude`
display_name
string
The display name for a component.
enabled [_required_]
boolean
Whether this processor is enabled.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
include [_required_]
string
A Datadog search query used to determine which logs this processor targets.
keys [_required_]
[string]
A list of tag keys.
mode [_required_]
enum
The processing mode. Allowed enum values: `filter`
type [_required_]
enum
The processor type. The value should always be `datadog_tags`. Allowed enum values: `datadog_tags`
default: `datadog_tags`
_required_]
[ <oneOf>]
A list of configured data sources for the pipeline.
object
The `kafka` source ingests data from Apache Kafka topics.
group_id [_required_]
string
Consumer group ID used by the Kafka client.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
[object]
Optional list of advanced Kafka client configuration options, defined as key-value pairs.
name [_required_]
string
The name of the `librdkafka` configuration option to set.
value [_required_]
string
The value assigned to the specified `librdkafka` configuration option.
object
Specifies the SASL mechanism for authenticating with a Kafka cluster.
mechanism
enum
SASL mechanism used for Kafka authentication. Allowed enum values: `PLAIN,SCRAM-SHA-256,SCRAM-SHA-512`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
topics [_required_]
[string]
A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
type [_required_]
enum
The source type. The value should always be `kafka`. Allowed enum values: `kafka`
default: `kafka`
object
The `datadog_agent` source collects logs from the Datadog Agent.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `datadog_agent`. Allowed enum values: `datadog_agent`
default: `datadog_agent`
object
The `splunk_tcp` source receives logs from a Splunk Universal Forwarder over TCP. TLS is supported for secure transmission.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_tcp`. Allowed enum values: `splunk_tcp`
default: `splunk_tcp`
object
The `splunk_hec` source implements the Splunk HTTP Event Collector (HEC) API.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `splunk_hec`. Allowed enum values: `splunk_hec`
default: `splunk_hec`
object
The `amazon_s3` source ingests logs from an Amazon S3 bucket. It supports AWS authentication and TLS encryption.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
region [_required_]
string
AWS region where the S3 bucket resides.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. Always `amazon_s3`. Allowed enum values: `amazon_s3`
default: `amazon_s3`
object
The `fluentd` source ingests logs from a Fluentd-compatible service.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluentd. Allowed enum values: `fluentd`
default: `fluentd`
object
The `fluent_bit` source ingests logs from Fluent Bit.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `fluent_bit`. Allowed enum values: `fluent_bit`
default: `fluent_bit`
object
The `http_server` source collects logs over HTTP POST from external services.
auth_strategy [_required_]
enum
HTTP authentication method. Allowed enum values: `none,plain`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
Unique ID for the HTTP server source.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_server`. Allowed enum values: `http_server`
default: `http_server`
object
The `sumo_logic` source receives logs from Sumo Logic collectors.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
type [_required_]
enum
The source type. The value should always be `sumo_logic`. Allowed enum values: `sumo_logic`
default: `sumo_logic`
object
The `rsyslog` source listens for logs over TCP or UDP from an `rsyslog` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `rsyslog`. Allowed enum values: `rsyslog`
default: `rsyslog`
object
The `syslog_ng` source listens for logs over TCP or UDP from a `syslog-ng` server using the syslog protocol.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used by the syslog source to receive messages. Allowed enum values: `tcp,udp`
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `syslog_ng`. Allowed enum values: `syslog_ng`
default: `syslog_ng`
object
The `amazon_data_firehose` source ingests logs from AWS Data Firehose.
object
AWS authentication credentials used for accessing AWS services such as S3. If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
assume_role
string
The Amazon Resource Name (ARN) of the role to assume.
external_id
string
A unique identifier for cross-account role assumption.
session_name
string
A session identifier used for logging and tracing the assumed role session.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `amazon_data_firehose`. Allowed enum values: `amazon_data_firehose`
default: `amazon_data_firehose`
object
The `google_pubsub` source ingests logs from a Google Cloud Pub/Sub subscription.
object
GCP credentials used to authenticate with Google Cloud Storage.
credentials_file [_required_]
string
Path to the GCP service account key file.
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
project [_required_]
string
The GCP project ID that owns the Pub/Sub subscription.
subscription [_required_]
string
The Pub/Sub subscription name from which messages are consumed.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `google_pubsub`. Allowed enum values: `google_pubsub`
default: `google_pubsub`
object
The `http_client` source scrapes logs from HTTP endpoints at regular intervals.
auth_strategy
enum
Optional authentication strategy for HTTP requests. Allowed enum values: `basic,bearer`
decoding [_required_]
enum
The decoding format used to interpret incoming logs. Allowed enum values: `bytes,gelf,json,syslog`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
scrape_interval_secs
int64
The interval (in seconds) between HTTP scrape requests.
scrape_timeout_secs
int64
The timeout (in seconds) for each scrape request.
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `http_client`. Allowed enum values: `http_client`
default: `http_client`
object
The `logstash` source ingests logs from a Logstash forwarder.
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
object
Configuration for enabling TLS encryption between the pipeline component and external services.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `logstash`. Allowed enum values: `logstash`
default: `logstash`
object
The `socket` source ingests logs over TCP or UDP.
_required_]
<oneOf>
Framing method configuration for the socket source.
object
Byte frames which are delimited by a newline character.
method [_required_]
enum
Byte frames which are delimited by a newline character. Allowed enum values: `newline_delimited`
object
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
method [_required_]
enum
Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments). Allowed enum values: `bytes`
object
Byte frames which are delimited by a chosen character.
delimiter [_required_]
string
A single ASCII character used to delimit events.
method [_required_]
enum
Byte frames which are delimited by a chosen character. Allowed enum values: `character_delimited`
object
Byte frames according to the octet counting format as per RFC6587.
method [_required_]
enum
Byte frames according to the octet counting format as per RFC6587. Allowed enum values: `octet_counting`
object
Byte frames which are chunked GELF messages.
method [_required_]
enum
Byte frames which are chunked GELF messages. Allowed enum values: `chunked_gelf`
id [_required_]
string
The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
mode [_required_]
enum
Protocol used to receive logs. Allowed enum values: `tcp,udp`
object
TLS configuration. Relevant only when `mode` is `tcp`.
ca_file
string
Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
crt_file [_required_]
string
Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
key_file
string
Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
type [_required_]
enum
The source type. The value should always be `socket`. Allowed enum values: `socket`
default: `socket`
name [_required_]
string
Name of the pipeline.
type [_required_]
string
The resource type identifier. For pipeline resources, this should always be set to `pipelines`.
default: `pipelines`
```
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "my-processor-group"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "enabled": true,
            "id": "my-processor-group",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              {
                "enabled": true,
                "id": "filter-processor",
                "include": "status:error",
                "type": "filter"
              }
            ]
          }
        ],
        "sources": [
          {
            "id": "datadog-agent-source",
            "type": "datadog_agent"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "type": "pipelines"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/observability-pipelines/#ValidatePipeline-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/observability-pipelines/#ValidatePipeline-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/observability-pipelines/#ValidatePipeline-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/observability-pipelines/#ValidatePipeline-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


Response containing validation errors.
Expand All
Field
Type
Description
[object]
The `ValidationResponse` `errors`.
_required_]
object
Describes additional metadata for validation errors, including field names and error messages.
field
string
The field name that caused the error.
id
string
The ID of the component in which the error occurred.
message [_required_]
string
The detailed error message.
title [_required_]
string
A short, human-readable summary of the error.
```
{
  "errors": [
    {
      "meta": {
        "field": "region",
        "id": "datadog-agent-source",
        "message": "Field 'region' is required"
      },
      "title": "Field 'region' is required"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/observability-pipelines/)
  * [Example](https://docs.datadoghq.com/api/latest/observability-pipelines/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/observability-pipelines/?code-lang=typescript)


#####  Validate an observability pipeline returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/remote_config/products/obs_pipelines/pipelines/validate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "config": {
        "destinations": [
          {
            "id": "datadog-logs-destination",
            "inputs": [
              "my-processor-group"
            ],
            "type": "datadog_logs"
          }
        ],
        "processors": [
          {
            "enabled": true,
            "id": "my-processor-group",
            "include": "service:my-service",
            "inputs": [
              "datadog-agent-source"
            ],
            "processors": [
              {
                "enabled": true,
                "id": "filter-processor",
                "include": "status:error",
                "type": "filter"
              }
            ]
          }
        ],
        "sources": [
          {
            "id": "datadog-agent-source",
            "type": "datadog_agent"
          }
        ]
      },
      "name": "Main Observability Pipeline"
    },
    "type": "pipelines"
  }
}
EOF  

                        
```

#####  Validate an observability pipeline returns "OK" response
```
// Validate an observability pipeline returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ObservabilityPipelineSpec{
		Data: datadogV2.ObservabilityPipelineSpecData{
			Attributes: datadogV2.ObservabilityPipelineDataAttributes{
				Config: datadogV2.ObservabilityPipelineConfig{
					Destinations: []datadogV2.ObservabilityPipelineConfigDestinationItem{
						datadogV2.ObservabilityPipelineConfigDestinationItem{
							ObservabilityPipelineDatadogLogsDestination: &datadogV2.ObservabilityPipelineDatadogLogsDestination{
								Id: "datadog-logs-destination",
								Inputs: []string{
									"my-processor-group",
								},
								Type: datadogV2.OBSERVABILITYPIPELINEDATADOGLOGSDESTINATIONTYPE_DATADOG_LOGS,
							}},
					},
					Processors: []datadogV2.ObservabilityPipelineConfigProcessorGroup{
						{
							Enabled: true,
							Id:      "my-processor-group",
							Include: "service:my-service",
							Inputs: []string{
								"datadog-agent-source",
							},
							Processors: []datadogV2.ObservabilityPipelineConfigProcessorItem{
								datadogV2.ObservabilityPipelineConfigProcessorItem{
									ObservabilityPipelineFilterProcessor: &datadogV2.ObservabilityPipelineFilterProcessor{
										Enabled: true,
										Id:      "filter-processor",
										Include: "status:error",
										Type:    datadogV2.OBSERVABILITYPIPELINEFILTERPROCESSORTYPE_FILTER,
									}},
							},
						},
					},
					Sources: []datadogV2.ObservabilityPipelineConfigSourceItem{
						datadogV2.ObservabilityPipelineConfigSourceItem{
							ObservabilityPipelineDatadogAgentSource: &datadogV2.ObservabilityPipelineDatadogAgentSource{
								Id:   "datadog-agent-source",
								Type: datadogV2.OBSERVABILITYPIPELINEDATADOGAGENTSOURCETYPE_DATADOG_AGENT,
							}},
					},
				},
				Name: "Main Observability Pipeline",
			},
			Type: "pipelines",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ValidatePipeline", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewObservabilityPipelinesApi(apiClient)
	resp, r, err := api.ValidatePipeline(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObservabilityPipelinesApi.ValidatePipeline`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ObservabilityPipelinesApi.ValidatePipeline`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Validate an observability pipeline returns "OK" response
```
// Validate an observability pipeline returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ObservabilityPipelinesApi;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfig;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigDestinationItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigProcessorGroup;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigProcessorItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineConfigSourceItem;
import com.datadog.api.client.v2.model.ObservabilityPipelineDataAttributes;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogAgentSource;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogAgentSourceType;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogLogsDestination;
import com.datadog.api.client.v2.model.ObservabilityPipelineDatadogLogsDestinationType;
import com.datadog.api.client.v2.model.ObservabilityPipelineFilterProcessor;
import com.datadog.api.client.v2.model.ObservabilityPipelineFilterProcessorType;
import com.datadog.api.client.v2.model.ObservabilityPipelineSpec;
import com.datadog.api.client.v2.model.ObservabilityPipelineSpecData;
import com.datadog.api.client.v2.model.ValidationResponse;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.validatePipeline", true);
    ObservabilityPipelinesApi apiInstance = new ObservabilityPipelinesApi(defaultClient);

    ObservabilityPipelineSpec body =
        new ObservabilityPipelineSpec()
            .data(
                new ObservabilityPipelineSpecData()
                    .attributes(
                        new ObservabilityPipelineDataAttributes()
                            .config(
                                new ObservabilityPipelineConfig()
                                    .destinations(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigDestinationItem(
                                                new ObservabilityPipelineDatadogLogsDestination()
                                                    .id("datadog-logs-destination")
                                                    .inputs(
                                                        Collections.singletonList(
                                                            "my-processor-group"))
                                                    .type(
                                                        ObservabilityPipelineDatadogLogsDestinationType
                                                            .DATADOG_LOGS))))
                                    .processors(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigProcessorGroup()
                                                .enabled(true)
                                                .id("my-processor-group")
                                                .include("service:my-service")
                                                .inputs(
                                                    Collections.singletonList(
                                                        "datadog-agent-source"))
                                                .processors(
                                                    Collections.singletonList(
                                                        new ObservabilityPipelineConfigProcessorItem(
                                                            new ObservabilityPipelineFilterProcessor()
                                                                .enabled(true)
                                                                .id("filter-processor")
                                                                .include("status:error")
                                                                .type(
                                                                    ObservabilityPipelineFilterProcessorType
                                                                        .FILTER))))))
                                    .sources(
                                        Collections.singletonList(
                                            new ObservabilityPipelineConfigSourceItem(
                                                new ObservabilityPipelineDatadogAgentSource()
                                                    .id("datadog-agent-source")
                                                    .type(
                                                        ObservabilityPipelineDatadogAgentSourceType
                                                            .DATADOG_AGENT)))))
                            .name("Main Observability Pipeline"))
                    .type("pipelines"));

    try {
      ValidationResponse result = apiInstance.validatePipeline(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservabilityPipelinesApi#validatePipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Validate an observability pipeline returns "OK" response
```
"""
Validate an observability pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
    ObservabilityPipelineConfigProcessorGroup,
)
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
    ObservabilityPipelineDatadogAgentSource,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source_type import (
    ObservabilityPipelineDatadogAgentSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
    ObservabilityPipelineDatadogLogsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
    ObservabilityPipelineDatadogLogsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData

body = ObservabilityPipelineSpec(
    data=ObservabilityPipelineSpecData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                destinations=[
                    ObservabilityPipelineDatadogLogsDestination(
                        id="datadog-logs-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineDatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processors=[
                    ObservabilityPipelineConfigProcessorGroup(
                        enabled=True,
                        id="my-processor-group",
                        include="service:my-service",
                        inputs=[
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineFilterProcessor(
                                enabled=True,
                                id="filter-processor",
                                include="status:error",
                                type=ObservabilityPipelineFilterProcessorType.FILTER,
                            ),
                        ],
                    ),
                ],
                sources=[
                    ObservabilityPipelineDatadogAgentSource(
                        id="datadog-agent-source",
                        type=ObservabilityPipelineDatadogAgentSourceType.DATADOG_AGENT,
                    ),
                ],
            ),
            name="Main Observability Pipeline",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
configuration.unstable_operations["validate_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Validate an observability pipeline returns "OK" response
```
# Validate an observability pipeline returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.validate_pipeline".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ObservabilityPipelinesAPI.new

body = DatadogAPIClient::V2::ObservabilityPipelineSpec.new({
  data: DatadogAPIClient::V2::ObservabilityPipelineSpecData.new({
    attributes: DatadogAPIClient::V2::ObservabilityPipelineDataAttributes.new({
      config: DatadogAPIClient::V2::ObservabilityPipelineConfig.new({
        destinations: [
          DatadogAPIClient::V2::ObservabilityPipelineDatadogLogsDestination.new({
            id: "datadog-logs-destination",
            inputs: [
              "my-processor-group",
            ],
            type: DatadogAPIClient::V2::ObservabilityPipelineDatadogLogsDestinationType::DATADOG_LOGS,
          }),
        ],
        processors: [
          DatadogAPIClient::V2::ObservabilityPipelineConfigProcessorGroup.new({
            enabled: true,
            id: "my-processor-group",
            include: "service:my-service",
            inputs: [
              "datadog-agent-source",
            ],
            processors: [
              DatadogAPIClient::V2::ObservabilityPipelineFilterProcessor.new({
                enabled: true,
                id: "filter-processor",
                include: "status:error",
                type: DatadogAPIClient::V2::ObservabilityPipelineFilterProcessorType::FILTER,
              }),
            ],
          }),
        ],
        sources: [
          DatadogAPIClient::V2::ObservabilityPipelineDatadogAgentSource.new({
            id: "datadog-agent-source",
            type: DatadogAPIClient::V2::ObservabilityPipelineDatadogAgentSourceType::DATADOG_AGENT,
          }),
        ],
      }),
      name: "Main Observability Pipeline",
    }),
    type: "pipelines",
  }),
})
p api_instance.validate_pipeline(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Validate an observability pipeline returns "OK" response
```
// Validate an observability pipeline returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_observability_pipelines::ObservabilityPipelinesAPI;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfig;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigDestinationItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigProcessorGroup;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigProcessorItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineConfigSourceItem;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDataAttributes;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogAgentSource;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogAgentSourceType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogLogsDestination;
use datadog_api_client::datadogV2::model::ObservabilityPipelineDatadogLogsDestinationType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineFilterProcessor;
use datadog_api_client::datadogV2::model::ObservabilityPipelineFilterProcessorType;
use datadog_api_client::datadogV2::model::ObservabilityPipelineSpec;
use datadog_api_client::datadogV2::model::ObservabilityPipelineSpecData;

#[tokio::main]
async fn main() {
    let body =
        ObservabilityPipelineSpec::new(
            ObservabilityPipelineSpecData::new(
                ObservabilityPipelineDataAttributes::new(
                    ObservabilityPipelineConfig::new(
                        vec![
                            ObservabilityPipelineConfigDestinationItem::ObservabilityPipelineDatadogLogsDestination(
                                Box::new(
                                    ObservabilityPipelineDatadogLogsDestination::new(
                                        "datadog-logs-destination".to_string(),
                                        vec!["my-processor-group".to_string()],
                                        ObservabilityPipelineDatadogLogsDestinationType::DATADOG_LOGS,
                                    ),
                                ),
                            )
                        ],
                        vec![
                            ObservabilityPipelineConfigSourceItem::ObservabilityPipelineDatadogAgentSource(
                                Box::new(
                                    ObservabilityPipelineDatadogAgentSource::new(
                                        "datadog-agent-source".to_string(),
                                        ObservabilityPipelineDatadogAgentSourceType::DATADOG_AGENT,
                                    ),
                                ),
                            )
                        ],
                    ).processors(
                        vec![
                            ObservabilityPipelineConfigProcessorGroup::new(
                                true,
                                "my-processor-group".to_string(),
                                "service:my-service".to_string(),
                                vec!["datadog-agent-source".to_string()],
                                vec![
                                    ObservabilityPipelineConfigProcessorItem::ObservabilityPipelineFilterProcessor(
                                        Box::new(
                                            ObservabilityPipelineFilterProcessor::new(
                                                true,
                                                "filter-processor".to_string(),
                                                "status:error".to_string(),
                                                ObservabilityPipelineFilterProcessorType::FILTER,
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ],
                    ),
                    "Main Observability Pipeline".to_string(),
                ),
                "pipelines".to_string(),
            ),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ValidatePipeline", true);
    let api = ObservabilityPipelinesAPI::with_config(configuration);
    let resp = api.validate_pipeline(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Validate an observability pipeline returns "OK" response
```
/**
 * Validate an observability pipeline returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.validatePipeline"] = true;
const apiInstance = new v2.ObservabilityPipelinesApi(configuration);

const params: v2.ObservabilityPipelinesApiValidatePipelineRequest = {
  body: {
    data: {
      attributes: {
        config: {
          destinations: [
            {
              id: "datadog-logs-destination",
              inputs: ["my-processor-group"],
              type: "datadog_logs",
            },
          ],
          processors: [
            {
              enabled: true,
              id: "my-processor-group",
              include: "service:my-service",
              inputs: ["datadog-agent-source"],
              processors: [
                {
                  enabled: true,
                  id: "filter-processor",
                  include: "status:error",
                  type: "filter",
                },
              ],
            },
          ],
          sources: [
            {
              id: "datadog-agent-source",
              type: "datadog_agent",
            },
          ],
        },
        name: "Main Observability Pipeline",
      },
      type: "pipelines",
    },
  },
};

apiInstance
  .validatePipeline(params)
  .then((data: v2.ValidationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## Can't find something?
Our friendly, knowledgeable solutions engineers are here to help!
[Contact Us](https://docs.datadoghq.com/help/)
[Free Trial](https://docs.datadoghq.com/api/latest/observability-pipelines/)
Download mobile app
[](https://apps.apple.com/app/datadog/id1391380318)[](https://play.google.com/store/apps/details?id=com.datadog.app)
Product
[Infrastructure Monitoring](https://www.datadoghq.com/product/infrastructure-monitoring/) [Network Monitoring](https://www.datadoghq.com/product/network-monitoring/) [Container Monitoring](https://www.datadoghq.com/product/container-monitoring/) [Serverless](https://www.datadoghq.com/product/serverless-monitoring/) [Cloud Cost Management](https://www.datadoghq.com/product/cloud-cost-management/) [Cloudcraft](https://www.datadoghq.com/product/cloudcraft/) [Kubernetes Autoscaling](https://www.datadoghq.com/product/kubernetes-autoscaling/) [Application Performance Monitoring](https://www.datadoghq.com/product/apm/) [Software Catalog](https://www.datadoghq.com/product/software-catalog/) [Universal Service Monitoring](https://www.datadoghq.com/product/universal-service-monitoring/) [Data Streams Monitoring](https://www.datadoghq.com/product/data-streams-monitoring/) [Jobs Monitoring](https://www.datadoghq.com/product/data-observability/jobs-monitoring/) [Quality Monitoring](https://www.datadoghq.com/product/data-observability/quality-monitoring/) [Database Monitoring](https://www.datadoghq.com/product/database-monitoring/) [Continuous Profiler](https://www.datadoghq.com/product/code-profiling/) [Dynamic Instrumentation](https://www.datadoghq.com/product/dynamic-instrumentation/) [Log Management](https://www.datadoghq.com/product/log-management/) [Sensitive Data Scanner](https://www.datadoghq.com/product/sensitive-data-scanner/) [Audit Trail](https://www.datadoghq.com/product/audit-trail/) [Observability Pipelines](https://www.datadoghq.com/product/observability-pipelines/) [Cloud Security](https://www.datadoghq.com/product/cloud-security/) [Cloud Security Posture Management](https://www.datadoghq.com/product/cloud-security/#posture-management) [Workload Protection](https://www.datadoghq.com/product/workload-protection/) [Cloud Infrastructure Entitlement Management](https://www.datadoghq.com/product/cloud-security/#entitlement-management) [Vulnerability Management](https://www.datadoghq.com/product/cloud-security/#vulnerability-management) [Compliance](https://www.datadoghq.com/product/cloud-security/#compliance) [App and API Protection](https://www.datadoghq.com/product/app-and-api-protection/) [Software Composition Analysis](https://www.datadoghq.com/product/software-composition-analysis/) [Code Security](https://www.datadoghq.com/product/code-security/) [Static Code Analysis (SAST)](https://www.datadoghq.com/product/sast/) [Runtime Code Analysis (IAST)](https://www.datadoghq.com/product/iast/) [IaC Security](https://www.datadoghq.com/product/iac-security) [Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) [Browser Real User Monitoring](https://www.datadoghq.com/product/real-user-monitoring/) [Mobile Real User Monitoring](https://www.datadoghq.com/product/real-user-monitoring/mobile-rum/) [Product Analytics](https://www.datadoghq.com/product/product-analytics/) [Session Replay](https://www.datadoghq.com/product/real-user-monitoring/session-replay/) [Synthetic Monitoring](https://www.datadoghq.com/product/synthetic-monitoring/) [Mobile App Testing](https://www.datadoghq.com/product/mobile-app-testing/)
[Continuous Testing](https://www.datadoghq.com/product/continuous-testing/) [Error Tracking](https://www.datadoghq.com/product/error-tracking/) [CloudPrem](https://www.datadoghq.com/product/cloudprem/) [Internal Developer Portal](https://www.datadoghq.com/product/internal-developer-portal/) [CI Visibility](https://www.datadoghq.com/product/ci-cd-monitoring/) [Test Optimization](https://www.datadoghq.com/product/test-optimization/) [Feature Flags](https://www.datadoghq.com/product/feature-flags/) [Code Coverage](https://www.datadoghq.com/product/code-coverage/) [Service Level Objectives](https://www.datadoghq.com/product/service-level-objectives/) [Incident Response](https://www.datadoghq.com/product/incident-response/) [Event Management](https://www.datadoghq.com/product/event-management/) [Case Management](https://www.datadoghq.com/product/case-management/) [Bits AI Agents](https://www.datadoghq.com/product/ai/bits-ai-agents/) [Bits AI SRE](https://www.datadoghq.com/product/ai/bits-ai-sre/) [Metrics](https://www.datadoghq.com/product/metrics/) [Watchdog](https://www.datadoghq.com/product/platform/watchdog/) [LLM Observability](https://www.datadoghq.com/product/llm-observability/) [AI Integrations](https://www.datadoghq.com/product/platform/integrations/#cat-aiml) [Workflow Automation](https://www.datadoghq.com/product/workflow-automation/) [App Builder](https://www.datadoghq.com/product/app-builder/) [CoScreen](https://www.datadoghq.com/product/coscreen/) [Teams](https://docs.datadoghq.com/account_management/teams/) [Dashboards](https://www.datadoghq.com/product/platform/dashboards/) [Notebooks](https://docs.datadoghq.com/notebooks/) [Mobile App](https://docs.datadoghq.com/service_management/mobile/?tab=ios) [Fleet Automation](https://www.datadoghq.com/product/fleet-automation/) [Access Control](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication) [OpenTelemetry](https://www.datadoghq.com/solutions/opentelemetry/) [Alerts](https://www.datadoghq.com/product/platform/alerts/) [integrations](https://www.datadoghq.com/product/platform/integrations/) [IDE Plugins](https://www.datadoghq.com/product/platform/ides/) [API](https://docs.datadoghq.com/api/) [Marketplace](https://www.datadoghq.com/marketplacepartners/) [Security Labs Research](https://securitylabs.datadoghq.com/) [Open Source Projects](https://opensource.datadoghq.com/) [Storage Management](https://www.datadoghq.com/product/storage-management/) [DORA Metrics](https://www.datadoghq.com/product/platform/dora-metrics/) [Secret Scanning](https://www.datadoghq.com/product/secret-scanning/)
resources
[Pricing](https://www.datadoghq.com/pricing/) [Documentation](https://docs.datadoghq.com/) [Support](https://www.datadoghq.com/support/) [Services & Enablement](https://www.datadoghq.com/support-services/) [Product Preview Program](https://www.datadoghq.com/product-preview/) [Certification](https://www.datadoghq.com/certification/overview/)
[Open Source](https://opensource.datadoghq.com/) [Events and Webinars](https://www.datadoghq.com/events-webinars/) [Security](https://www.datadoghq.com/security/) [Privacy Center](https://www.datadoghq.com/privacy/) [Knowledge Center](https://www.datadoghq.com/knowledge-center/) [Learning Resources](https://www.datadoghq.com/learn/)
About
[Contact Us](https://www.datadoghq.com/about/contact/) [Partners](https://www.datadoghq.com/partner/network/) [Press](https://www.datadoghq.com/about/latest-news/press-releases/) [Leadership](https://www.datadoghq.com/about/leadership/) [Careers](https://careers.datadoghq.com/) [Legal](https://www.datadoghq.com/legal/)
[Investor Relations](https://investors.datadoghq.com/) [Analyst Reports](https://www.datadoghq.com/about/analyst/) [ESG Report](https://www.datadoghq.com/esg-report/) [Vendor Help](https://www.datadoghq.com/vendor-help/) [Trust Hub](https://www.datadoghq.com/trust/)
Blog
[The Monitor](https://www.datadoghq.com/blog/) [Engineering](https://www.datadoghq.com/blog/engineering/)
[AI](https://www.datadoghq.com/blog/ai/) [Security Labs](https://securitylabs.datadoghq.com/)
Icon/world Created with Sketch. English 
[English ](https://docs.datadoghq.com/?lang_pref=en)[Français ](https://docs.datadoghq.com/fr/?lang_pref=fr)[日本語 ](https://docs.datadoghq.com/ja/?lang_pref=ja)[한국어 ](https://docs.datadoghq.com/ko/?lang_pref=ko)[Español](https://docs.datadoghq.com/es/?lang_pref=es)
[](https://twitter.com/datadoghq)[](https://www.instagram.com/datadoghq/)[](https://www.youtube.com/user/DatadogHQ)[](https://www.LinkedIn.com/company/datadog/)
© Datadog 2026 [Terms](https://www.datadoghq.com/legal/terms/) | [Privacy](https://www.datadoghq.com/legal/privacy/) | [Your Privacy Choices ![](https://imgix.datadoghq.com/img/icons/privacyoptions.svg?w=24&dpr=2)](https://docs.datadoghq.com/api/latest/observability-pipelines/)
###### Request a personalized demo
×
*
First Name*
*
Last Name*
*
Business Email*
*
Company*
*
Job Title*
*
Phone Number
*
How are you currently monitoring your infrastructure and applications?
By submitting this form, you agree to the [Privacy Policy](https://www.datadoghq.com/legal/privacy/) and [Cookie Policy.](https://www.datadoghq.com/legal/cookies/)
Request a Demo
##### Get Started with Datadog
