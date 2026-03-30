# Source: https://www.elastic.co/docs/release-notes/beats

﻿---
title: Beats release notes
description: Review the changes, fixes, and more in each version of Beats. To check for security updates, go to Security announcements for the Elastic Stack. 
url: https://www.elastic.co/docs/release-notes/beats
products:
  - Beats
applies_to:
  - Elastic Stack: Generally available
---

# Beats release notes
Review the changes, fixes, and more in each version of Beats.
To check for security updates, go to [Security announcements for the Elastic Stack](https://discuss.elastic.co/c/announcements/security-announcements/31).
<admonition title="Related release notes">
  Elastic Agent integrates and manages Beats for data collection. For changes to Elastic Agent, refer to the [Elastic Agent release notes](https://www.elastic.co/docs/release-notes/elastic-agent).
</admonition>


## 9.3.1


### Features and enhancements

**Filebeat**
- Add support for managed identity authentication to the `azure-eventhub` input. [#48655](https://github.com/elastic/beats/pull/48655) [#48680](https://github.com/elastic/beats/issues/48680)
- Improve log path sanitization for request trace logging. [#48719](https://github.com/elastic/beats/pull/48719)
- Add descriptions and units to CEL input OpenTelemetry metrics. [#48684](https://github.com/elastic/beats/pull/48684)
- Don't print warning about small files on each file system scan. [#48704](https://github.com/elastic/beats/pull/48704) [#45642](https://github.com/elastic/beats/issues/45642)
- Allow the configuration of OTLP histogram aggregation through the `OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION` environment variable in CEL input. [#48731](https://github.com/elastic/beats/pull/48731) [#48730](https://github.com/elastic/beats/issues/48730)
- Tighten request trace logging destination path checks in CEL, Entity Analytics, HTTP Endpoint and HTTP JSON inputs. [#48863](https://github.com/elastic/beats/pull/48863)


### Fixes

**All**
- Updates the `translate_ldap_attribute` processor discovery to try both LDAP and LDAPS per host, starting with LDAPS. [#48818](https://github.com/elastic/beats/pull/48818)

**Elastic Agent**
- Fix a bug which could report an invalid number of active `otelconsumer` events. [#48720](https://github.com/elastic/beats/pull/48720) [#12515](https://github.com/elastic/elastic-agent/issues/12515)

**Filebeat**
- Enforce region configuration when `non_aws_bucket_name` is defined for the `awss3` input. [#48534](https://github.com/elastic/beats/pull/48534) [#47847](https://github.com/elastic/beats/issues/47847)
- Fix Log to Filestream state migration removing states from non-harvested files. [#48570](https://github.com/elastic/beats/pull/48570)
- Fix CEL input incorrectly counting degraded program runs as successful executions in OpenTelemetry metrics. [#48734](https://github.com/elastic/beats/pull/48734) [#48714](https://github.com/elastic/beats/issues/48714)
- Fix Active Directory Entity Analytics to resolve nested group membership and escape Base DN filter values. [#48815](https://github.com/elastic/beats/pull/48815)
- Fix Entity Analytics Okta OAuth2 token requests ignoring custom TLS/SSL configuration. [#48866](https://github.com/elastic/beats/pull/48866)
- Fix an issue where the `azure-blob-storage` input was failing with the Storage Blob Data Reader RBAC role. [#48886](https://github.com/elastic/beats/pull/48886) [#48890](https://github.com/elastic/beats/issues/48890)

**Filebeat, Metricbeat**
- Add 30s metric logging to Beat receivers. [#48541](https://github.com/elastic/beats/pull/48541)

**Heartbeat**
- Add a missing dependency for Synthetics on Wolfi Docker image. [#48569](https://github.com/elastic/beats/pull/48569)

**Libbeat**
- Add SSPI bind timeout and document Windows account requirements for the `translate_ldap_attribute` processor. [#48444](https://github.com/elastic/beats/pull/48444)
- Fix `otelconsumer` logging hundreds of errors per second when queue is full. [#48807](https://github.com/elastic/beats/pull/48807) [#48803](https://github.com/elastic/beats/issues/48803)

**Osquerybeat**
- Fix differential results using wrong data source for removed events. [#48438](https://github.com/elastic/beats/pull/48438) [#48427](https://github.com/elastic/beats/issues/48427)

**Packetbeat**
- Refactor the DHCPv4 parsers and fix parsing issues. The DHCP `router` field is now a list, as is specified in RFC2132. [#48414](https://github.com/elastic/beats/pull/48414)
- Fix procfs network parsers. [#48428](https://github.com/elastic/beats/pull/48428)
- Fix a panic in the Thrift struct parser triggered by malformed packets. [#48498](https://github.com/elastic/beats/pull/48498)
- Add array access checks to SIP parser. [#48514](https://github.com/elastic/beats/pull/48514)
- Fix potential array access panics and infinite loops in PostgreSQL parser. [#48528](https://github.com/elastic/beats/pull/48528)
- Clean up `int` overflows and array access issues in MySQL parsers. [#48543](https://github.com/elastic/beats/pull/48543)
- Add `int` overflow checks to the `http` parser. [#48563](https://github.com/elastic/beats/pull/48563)


## 9.3.0

_This release also includes: [Deprecations](/docs/release-notes/beats/deprecations#beats-9.3.0-deprecations)._

### Features and enhancements

**All**
- Introduce cloud connectors flow. [#47587](https://github.com/elastic/beats/pull/47587)
- Make beats receivers emit status for their subcomponents. [#48015](https://github.com/elastic/beats/pull/48015)
- Add GUID translation, base DN inference, and SSPI authentication to LDAP processor. [#47827](https://github.com/elastic/beats/pull/47827)
- Add `events.failure_store` metric to track events sent to Elasticsearch failure store. [#48068](https://github.com/elastic/beats/pull/48068) [#47164](https://github.com/elastic/beats/issues/47164)

**Filebeat**
- Add support for direct HTTP request rate limit setting in CEL input. [#46953](https://github.com/elastic/beats/pull/46953)
- Allow adding file owner and group to the events meta fields on Unix systems. [#47331](https://github.com/elastic/beats/pull/47331) [#43226](https://github.com/elastic/beats/issues/43226)
- Add AWS auth method for CEL and HTTP JSON inputs. [#47260](https://github.com/elastic/beats/pull/47260)
- Add client secret authentication method for Azure Event Hub and storage in Filebeat. [#47256](https://github.com/elastic/beats/pull/47256)
- Add client address and name to submitted Redis slowlogs. [#41507](https://github.com/elastic/beats/pull/41507)
- Log unpublished event count and exit publish loop on input context cancellation. [#47730](https://github.com/elastic/beats/pull/47730)
- Upgrade CEL mito library version to v1.24.0. [#47762](https://github.com/elastic/beats/pull/47762)
- Add OTEL metrics to CEL inputs. [#47014](https://github.com/elastic/beats/pull/47014)
- Improve input error reporting to Elastic Agent, specially when pipeline configurations are incorrect. [#47905](https://github.com/elastic/beats/pull/47905) [#45649](https://github.com/elastic/beats/issues/45649)
- Azure EventHub input v2 - Add support for AMQP over WebSocket and HTTPS proxy. [#47956](https://github.com/elastic/beats/pull/47956) [#47823](https://github.com/elastic/beats/issues/47823)
- The Journald input now supports setting a chroot to use when calling
  the journalctl binary, thus allowing the journald input to be used
  with the wolfi container variant and in environments where the
  hosts Journald is not compatible with the `journalctl` version
  shipped with the container.
  . [#48008](https://github.com/elastic/beats/pull/48008) [#47164](https://github.com/elastic/beats/issues/47164)
  Add support in the journald inpur for using chroot when calling
  `journalctl`. In a container environment this allows to mount the host
  file system into the container and use its `journalctl`, which
  prevents any sort of incompatibility between the `journalctl` in the
  container image and the host Journald. Allows using the journald input with Wolfi based Docker containers.
- GZIP support is GA and always enabled on filestream. [#47893](https://github.com/elastic/beats/pull/47893) [#47880](https://github.com/elastic/beats/issues/47880)
  Ingesting GZIP-compressed files is now GA. The `gzip_experimental` configuration option has been deprecated. Users should use `compression` instead. Refer to the [documentation](https://www.elastic.co/docs/reference/beats/filebeat/filebeat-input-filestream#reading-gzip-files) for more details.
- Filebeat deploy on kubernetes examples use `compression` instead of `gzip_experimental`. [#48079](https://github.com/elastic/beats/pull/48079) [#47882](https://github.com/elastic/beats/issues/47882)
- Add file-based auth provider for CEL and HTTP JSON inputs. [#47507](https://github.com/elastic/beats/pull/47507) [#47506](https://github.com/elastic/beats/issues/47506)
  The CEL and HTTP JSON inputs now support reading authentication tokens from
  files, enabling integration with various secret providers like Vault,
  Kubernetes secret projections, etc. Tokens are automatically refreshed based on
  a configurable interval without requiring restarts.

**Metricbeat**
- Change calculation of CPU/Memory for Kubernetes to allocatable values. [#47815](https://github.com/elastic/beats/pull/47815)
  Update kubernetes cpu and memory metrics to use allocatable values instead of capacity values.
- Add extra debug logging to simplify troubleshooting in prometheus module. [#47477](https://github.com/elastic/beats/pull/47477) [#15693](https://github.com/elastic/beats/issues/15693)
- Add resource pool id to vsphere cluster metricset. [#47883](https://github.com/elastic/beats/pull/47883)
- Add `last_terminated_exitcode` to `kubernetes.container.status`. [#47968](https://github.com/elastic/beats/pull/47968)
- Report memory pressure stall information (PSI) for cgroup v2. [#48054](https://github.com/elastic/beats/pull/48054)
  Add memory PSI metrics to system.process.cgroup, complementing existing CPU and IO pressure metrics for cgroupv2.

**Osquerybeat**
- Add browser_history table to Osquery extension for cross-platform browser history analysis. [#47117](https://github.com/elastic/beats/pull/47117)
- Add amcache hive support for osquery extension in Windows. [#46996](https://github.com/elastic/beats/pull/46996)
- Add status reporting for osquerybeat lifecycle and osqueryd management. [#47472](https://github.com/elastic/beats/pull/47472)
- Add osqueryd process health monitoring with metrics exposed via beats monitoring endpoint. [#47474](https://github.com/elastic/beats/pull/47474)
- Upgrade osquery version to 5.19.0. [#48040](https://github.com/elastic/beats/pull/48040)
- Add record filtering/scoping support to the osquery extension. [#47396](https://github.com/elastic/beats/pull/47396)
- Update documentation for the amcache tables in the osquery extension. [#47748](https://github.com/elastic/beats/pull/47748)
- Add marshalling support for embedded structs in the osquery extension. [#47746](https://github.com/elastic/beats/pull/47746)
- Update column definition encoding to support embedded structs. [#47758](https://github.com/elastic/beats/pull/47758)

**Packetbeat**
- Add status reporter interface to packetbeat. [#45732](https://github.com/elastic/beats/pull/45732)

**Winlogbeat**
- Add process.args_count to winlogbeat windows security ingest pipeline. [#47266](https://github.com/elastic/beats/pull/47266)


### Fixes

**All**
- Add msync syscall to seccomp whitelist for BadgerDB persistent cache. [#48229](https://github.com/elastic/beats/pull/48229)
- Fix windows install script to properly migrate legacy state data. [#48293](https://github.com/elastic/beats/pull/48293)
- Remove use of github.com/elastic/elastic-agent-client from OSS Beats. [#48353](https://github.com/elastic/beats/pull/48353)

**Filebeat**
- Fix an issue in the initialization of exporters for input metrics that could cause an unexpected number of exporter connections to be created. [#48321](https://github.com/elastic/beats/pull/48321)
- Prevent panic during startup if dissect processor has invalid field name in tokenizer. [#47839](https://github.com/elastic/beats/pull/47839)
- Fix AD Entity Analytics failing to fetch users when Base DN contains a group CN. [#48395](https://github.com/elastic/beats/pull/48395)
- Fix filebeat goroutine leak when using harvester_limit. [#48445](https://github.com/elastic/beats/pull/48445)

**Metricbeat**
- Improve defensive checks to prevent panics in meraki module. [#47950](https://github.com/elastic/beats/pull/47950)
- Remove GCP Billing timestamp functions. [#47963](https://github.com/elastic/beats/pull/47963)
- Harden Prometheus metrics parser against panics caused by malformed input data. [#47914](https://github.com/elastic/beats/pull/47914)
- Add bounds checking to Zookeeper server module to prevent index-out-of-range panics. [#47915](https://github.com/elastic/beats/pull/47915)
- Fix panic in graphite server metricset when metric has fewer parts than template expects. [#47916](https://github.com/elastic/beats/pull/47916)
- Skip regions with no permission to query for AWS CloudWatch metrics. [#48135](https://github.com/elastic/beats/pull/48135)
- Enforce configurable size limits on incoming requests for remote_write metricset (max_compressed_body_bytes, max_decoded_body_bytes). [#48218](https://github.com/elastic/beats/pull/48218)
- Autoops agent to shutdown when it cant recover from the http errors. [#48292](https://github.com/elastic/beats/pull/48292)
- Add missing vector metrics in Autoops agent. [#48365](https://github.com/elastic/beats/pull/48365)
- Stack Monitoring now trims trailing slashes from host URLs for simplicity. [#48430](https://github.com/elastic/beats/pull/48430) [#48426](https://github.com/elastic/beats/issues/48426)
- Flatten AutoOps Cluster Settings to avoid unnecessary nesting and information. [#48454](https://github.com/elastic/beats/pull/48454) [#48453](https://github.com/elastic/beats/issues/48453)

**Osquerybeat**
- Fix zero time encoding for Unix timestamps. [#47970](https://github.com/elastic/beats/pull/47970)

**Packetbeat**
- RPC fragment bounds checking and sanitization. [#47803](https://github.com/elastic/beats/pull/47803)
- Add check for incorrect length values in PostgreSQL datarow parser. [#47872](https://github.com/elastic/beats/pull/47872)
- Verify and cap memcache UDP fragment counts. [#47874](https://github.com/elastic/beats/pull/47874)
- Fix bounds checking in MongoDB protocol parser to prevent panics. [#47925](https://github.com/elastic/beats/pull/47925)


## 9.2.6


### Features and enhancements

**Filebeat**
- Add support for managed identity authentication to the `azure-eventhub` input. [#48655](https://github.com/elastic/beats/pull/48655) [#48680](https://github.com/elastic/beats/issues/48680)
- Improve log path sanitization for request trace logging. [#48719](https://github.com/elastic/beats/pull/48719)
- Don't print warning about small files on each file system scan. [#48704](https://github.com/elastic/beats/pull/48704) [#45642](https://github.com/elastic/beats/issues/45642)
- Tighten request trace logging destination path checks in CEL, Entity Analytics, HTTP Endpoint and HTTP JSON inputs. [#48863](https://github.com/elastic/beats/pull/48863)


### Fixes

**Filebeat**
- Enforce region configuration when `non_aws_bucket_name` is defined for the `awss3` input. [#48534](https://github.com/elastic/beats/pull/48534) [#47847](https://github.com/elastic/beats/issues/47847)
- Fix Log to Filestream state migration removing states from non-harvested files. [#48570](https://github.com/elastic/beats/pull/48570)
- Fix Active Directory Entity Analytics to resolve nested group membership and escape Base DN filter values. [#48395](https://github.com/elastic/beats/pull/48395)
- Fix Entity Analytics Okta OAuth2 token requests ignoring custom TLS/SSL configuration. [#48866](https://github.com/elastic/beats/pull/48866)
- Fix an issue where the `azure-blob-storage` input was failing with the Storage Blob Data Reader RBAC role. [#48886](https://github.com/elastic/beats/pull/48886) [#48890](https://github.com/elastic/beats/issues/48890)

**Heartbeat**
- Add a missing dependency for Synthetics on Wolfi Docker image. [#48569](https://github.com/elastic/beats/pull/48569)

**Osquerybeat**
- Fix differential results using wrong data source for removed events. [#48438](https://github.com/elastic/beats/pull/48438) [#48427](https://github.com/elastic/beats/issues/48427)

**Packetbeat**
- Clean up `int` overflows and array access issues in MySQL parsers. [#48543](https://github.com/elastic/beats/pull/48543)
- Add `int` overflow checks to the `http` parser. [#48563](https://github.com/elastic/beats/pull/48563)


## 9.2.5


### Fixes

**All**
- Fix windows install script to properly migrate legacy state data. [#48293](https://github.com/elastic/beats/pull/48293)
- Remove use of github.com/elastic/elastic-agent-client from OSS Beats. [#48353](https://github.com/elastic/beats/pull/48353)

**Filebeat**
- Fix AD Entity Analytics failing to fetch users when Base DN contains a group CN. [#48395](https://github.com/elastic/beats/pull/48395)
- Fix Filebeat goroutine leak when using harvester_limit. [#48445](https://github.com/elastic/beats/pull/48445)
- Update github.com/elastic/mito version to v1.24.1 to fix issue with rate limit calculation. [#48499](https://github.com/elastic/beats/pull/48499)

**Metricbeat**
- Enforce configurable size limits on incoming requests for remote_write metricset (max_compressed_body_bytes, max_decoded_body_bytes). [#48218](https://github.com/elastic/beats/pull/48218)
- Autoops agent to shutdown when it cant recover from the http errors. [#48292](https://github.com/elastic/beats/pull/48292)
- Add missing vector metrics in Autoops agent. [#48365](https://github.com/elastic/beats/pull/48365)
- Stack Monitoring now trims trailing slashes from host URLs for simplicity. [#48430](https://github.com/elastic/beats/pull/48430)
- Flatten AutoOps Cluster Settings to avoid unnecessary nesting and information. [#48454](https://github.com/elastic/beats/pull/48454)

**Packetbeat**
- Add check for incorrect length values in PostgreSQL datarow parser. [#47872](https://github.com/elastic/beats/pull/47872)
- Fix procfs network parsers. [#48428](https://github.com/elastic/beats/pull/48428)
- Fix Thrift struct parser oob bug. [#48498](https://github.com/elastic/beats/pull/48498)
- Clean up and add checks to SIP parser. [#48514](https://github.com/elastic/beats/pull/48514)
- Fix potential array access panics  infinite loops in PostgreSQL parser. [#48528](https://github.com/elastic/beats/pull/48528)


## 9.2.4


### Features and enhancements

**Filebeat**
- Add client secret authentication method for Azure Event Hub and storage in Filebeat. [#47256](https://github.com/elastic/beats/pull/47256)
- Add support for AMQP-over-WebSocket transport in the processor v2. [#47956](https://github.com/elastic/beats/pull/47956) [#47823](https://github.com/elastic/beats/issues/47823)

**Metricbeat**
- Add `last_terminated_exitcode` to `kubernetes.container.status`. [#47968](https://github.com/elastic/beats/pull/47968)


### Fixes

**All**
- Upgrade opentelemtry-collector-contrib to 0.141.0 and opentelemetry-collector to 1.47.0. [#48122](https://github.com/elastic/beats/pull/48122)
- Add msync syscall to seccomp whitelist for BadgerDB persistent cache. [#48229](https://github.com/elastic/beats/pull/48229)

**Metricbeat**
- Harden Prometheus metrics parser against panics caused by malformed input data. [#47914](https://github.com/elastic/beats/pull/47914)
- Add bounds checking to Zookeeper server module to prevent index-out-of-range panics. [#47915](https://github.com/elastic/beats/pull/47915)
- Fix panic in graphite server metricset when metric has fewer parts than template expects. [#47916](https://github.com/elastic/beats/pull/47916)
- Skip regions with no permission to query for AWS CloudWatch metrics. [#48135](https://github.com/elastic/beats/pull/48135)

**Packetbeat**
- Fix bounds checking in MongoDB protocol parser to prevent panics. [#47925](https://github.com/elastic/beats/pull/47925)


## 9.2.3


### Features and enhancements

**All**
- Make beats receivers emit status for their subcomponents. [#48015](https://github.com/elastic/beats/pull/48015)
- Add GUID translation, base DN inference, and SSPI authentication to LDAP processor. [#47827](https://github.com/elastic/beats/pull/47827)

**Filebeat**
- Log unpublished event count and exit publish loop on input context cancellation. [#47730](https://github.com/elastic/beats/pull/47730) [#47717](https://github.com/elastic/beats/issues/47717)
- Improving input error reporting to Elastic Agent, specially when pipeline configurations are incorrect. [#47905](https://github.com/elastic/beats/pull/47905) [#45649](https://github.com/elastic/beats/issues/45649)

**Metricbeat**
- K8s_container_allocatable. [#47815](https://github.com/elastic/beats/pull/47815) [#40701](https://github.com/elastic/beats/issues/40701)
  Updates kubernetes cpu and memory metrics to use allocatable values instead of capacity values.
- Add resource pool id to vsphere cluster metricset. [#47883](https://github.com/elastic/beats/pull/47883)

**Packetbeat**
- Ipfrag2. [#47970](https://github.com/elastic/beats/pull/47970)


### Fixes

**Filebeat**
- Prevent panic during startup if dissect processor has invalid field name in tokenizer. [#47839](https://github.com/elastic/beats/pull/47839)

**Metricbeat**
- Improve defensive checks to prevent panics in meraki module. [#47950](https://github.com/elastic/beats/pull/47950)
- Remove GCP Billing timestamp functions. [#47963](https://github.com/elastic/beats/pull/47963) [#47967](https://github.com/elastic/beats/issues/47967)

**Packetbeat**
- Rpc_fragment_sanitization. [#47803](https://github.com/elastic/beats/pull/47803)
- Verify and cap memcache udp fragment counts. [#47874](https://github.com/elastic/beats/pull/47874)


## 9.2.2

_This release also includes: [Breaking changes](/docs/release-notes/beats/breaking-changes#beats-9.2.2-breaking-changes)._

### Features and enhancements

**All**
- Include whether Beat is running from a FIPS distribution in User Agent. [#47409](https://github.com/elastic/beats/pull/47409)

**Filebeat**
- Add support for DPoP authentication for the CEL and HTTP JSON inputs. [#47441](https://github.com/elastic/beats/pull/47441)
- Improve logging of cache processor and add ignore failure option. [#47565](https://github.com/elastic/beats/pull/47565)


### Fixes

**All**
- Fix a fatal startup error in Beats Receivers caused by truncation of long UTF-8 hostnames. [#47713](https://github.com/elastic/beats/pull/47713)
- Not being able to start the add_docker_metadata processor is now consistently a non-fatal error when Docker is not available. [#47760](https://github.com/elastic/beats/pull/47760)

**Filebeat**
- [Filestream] Ensure harvester always restarts if the file has not been fully ingested. [#47107](https://github.com/elastic/beats/pull/47107) [#46923](https://github.com/elastic/beats/issues/46923)
- Handle and remove BOM during JSON parsing in Azure Blob Storage and GCS inputs. [#47508](https://github.com/elastic/beats/pull/47508)
- Fix an issue where Filebeat could hang during shutdown when using the filestream input. [#47518](https://github.com/elastic/beats/pull/47518)
- Fix double locking in `translate_ldap_attribute` processor and improve logging. [#47585](https://github.com/elastic/beats/pull/47585)
- Fix possible data corruption in TCP, Syslog and Unix inputs. [#47618](https://github.com/elastic/beats/pull/47618)
- Skip AWS S3 test events in Filebeat AWS S3 input. [#47635](https://github.com/elastic/beats/pull/47635)

**Metricbeat**
- [Cloud Connect] Use `cluster.metadata.display_name` as cluster name if set. [#47440](https://github.com/elastic/beats/pull/47440)


## 9.2.1


### Features and enhancements

**Filebeat**
- Add data stream identification to Fleet health status updates. [#47229](https://github.com/elastic/beats/pull/47229)

**Metricbeat**
- Enhance GCP Billing metricset with additional fields. [#47059](https://github.com/elastic/beats/pull/47059)


### Fixes

**All**
- Add `close` to conditional processors if underlying processors have a `close` method. [#46653](https://github.com/elastic/beats/pull/46653) [#46575](https://github.com/elastic/beats/issues/46575)
- Fix a bug where Kerberos authentication could be disabled when server supports multiple authentication types. [#47444](https://github.com/elastic/beats/pull/47444) [#47443](https://github.com/elastic/beats/pull/47443) [#47110](https://github.com/elastic/beats/issues/47110)

**Filebeat**
- Fix potential Filebeat panic during memory queue shutdown. [#47248](https://github.com/elastic/beats/pull/47248)


## 9.2.0

_This release also includes: [Breaking changes](/docs/release-notes/beats/breaking-changes#beats-9.2.0-breaking-changes)._

### Features and enhancements

**All**
- The following `output latency_delta` metrics are now included when `logging.metrics` is enabled: `output.latency_delta.{count, max, median, min, p99}`. This only includes data collected since the last internal metrics was logged. [#45749](https://github.com/elastic/beats/pull/45749)

**Auditbeat**
- Add new ETW FIM backend for Windows. [#45887](https://github.com/elastic/beats/pull/45887)

**Filebeat**
- TCP and UDP inputs now support multiple pipeline workers configured using `number_of_workers`. Increasing the number of workers improves performance when slow processors are used by decoupling reading from the network connection and publishing. [#45124](https://github.com/elastic/beats/pull/45124) [#43674](https://github.com/elastic/beats/issues/43674)
- Add beta support for GZIP file ingestion in filestream. [#45301](https://github.com/elastic/beats/pull/45301)
- Update the `parse_aws_vpc_flow_log` processor to support AWS VPC flow log versions 6–8. [#45746](https://github.com/elastic/beats/pull/45746)
- Add OAuth2 support for Okta provider in Entity Analytics input. [#45753](https://github.com/elastic/beats/pull/45753)
- Improve error reporting for schemeless URLs in HTTP JSON input. [#45953](https://github.com/elastic/beats/pull/45953)
- Add `remaining_executions` global to the CEL input evaluation context. [#46210](https://github.com/elastic/beats/pull/46210)
- Journald input now supports reading from multiple journals, including remote ones. [#46722](https://github.com/elastic/beats/pull/46722) [#46656](https://github.com/elastic/beats/issues/46656)

**Metricbeat**
- Improve the Prometheus helper to handle multiple content types including blank and invalid headers. [#47085](https://github.com/elastic/beats/pull/47085)

**Osquerybeat**
- Upgrade osquery version to 5.18.1. [#46624](https://github.com/elastic/beats/pull/46624)

**Packetbeat**
- Bump Windows Npcap version to v1.83. [#46809](https://github.com/elastic/beats/pull/46809)


### Fixes

**All**
- Make data updates in `add_host_metadata` processor synchronous. [#46546](https://github.com/elastic/beats/pull/46546)
- Prevent panic in Logstash output when trying to send events while shutting down. [#46960](https://github.com/elastic/beats/pull/46960) [#46889](https://github.com/elastic/beats/issues/46889)
- Prevent panic in the `replace` processor for non-string values. [#47009](https://github.com/elastic/beats/pull/47009) [#42308](https://github.com/elastic/beats/issues/42308)
- Ensure Autodiscover correctly updates Kubernetes metadata on node and pod label changes. [#47034](https://github.com/elastic/beats/pull/47034) [#46979](https://github.com/elastic/beats/issues/46979)
- Prevent a 3s startup delay when `add_cloud_metadata` is used with debug logs. [#47058](https://github.com/elastic/beats/pull/47058) [#44203](https://github.com/elastic/beats/issues/44203)
- Update `elastic-agent-system-metrics` to version v0.13.3.  [#47104](https://github.com/elastic/beats/pull/47104)
- Remove “Accurate CPU counts not available on platform” log spam at the debug level. [#47054](https://github.com/elastic/beats/issues/47054)
- Allow users to customize their data stream namespace to `generic`. [#47140](https://github.com/elastic/beats/pull/47140)

**Filebeat**
- Fix defer usage for stopped status reporting. [#46916](https://github.com/elastic/beats/pull/46916)

**Metricbeat**
- Fix missing AWS cloudwatch metrics with linked accounts and same dimensions. [#46978](https://github.com/elastic/beats/pull/46978) [#15362](https://github.com/elastic/integrations/issues/15362)
- Add a fix to handle blank `content-type` headers in HTTP responses for Prometheus. [#47027](https://github.com/elastic/beats/pull/47027)
- Add pagination support to the `device_health` metricset in the meraki module. [#46938](https://github.com/elastic/beats/pull/46938) [#15551](https://github.com/elastic/integrations/issues/15551)


## 9.1.10


### Features and enhancements

**Filebeat**
- Add client secret authentication method for Azure Event Hub and storage in Filebeat. [#47256](https://github.com/elastic/beats/pull/47256)
- Improve input error reporting to Elastic Agent, especially when pipeline configurations are incorrect. [#47905](https://github.com/elastic/beats/pull/47905) [#45649](https://github.com/elastic/beats/issues/45649)
- Support for AMQP-over-WebSocket transport in the azure-eventhub processor v2. [#47956](https://github.com/elastic/beats/pull/47956) [#47823](https://github.com/elastic/beats/issues/47823)

**Metricbeat**
- Add `last_terminated_exitcode` to `kubernetes.container.status`. [#47968](https://github.com/elastic/beats/pull/47968)


### Fixes

**All**
- Add msync syscall to seccomp whitelist for BadgerDB persistent cache. [#48229](https://github.com/elastic/beats/pull/48229)

**Metricbeat**
- Harden Prometheus metrics parser against panics caused by malformed input data. [#47914](https://github.com/elastic/beats/pull/47914)
- Add bounds checking to Zookeeper server module to prevent index-out-of-range panics. [#47915](https://github.com/elastic/beats/pull/47915)
- Fix panic in graphite server metricset when metric has fewer parts than template expects. [#47916](https://github.com/elastic/beats/pull/47916)
- Skip regions with no permission to query for AWS CloudWatch metrics. [#48135](https://github.com/elastic/beats/pull/48135)

**Packetbeat**
- Fix bounds checking in MongoDB protocol parser to prevent panics. [#47925](https://github.com/elastic/beats/pull/47925)


## 9.1.9

_This release also includes: [Breaking changes](/docs/release-notes/beats/breaking-changes#beats-9.1.9-breaking-changes)._

### Features and enhancements

**Filebeat**
- Log unpublished event count and exit publish loop on input context cancellation. [#47730](https://github.com/elastic/beats/pull/47730) [#47717](https://github.com/elastic/beats/issues/47717)

**Metricbeat**
- Add resource pool id to vsphere cluster metricset. [#47883](https://github.com/elastic/beats/pull/47883)

**Packetbeat**
- Ipfrag2. [#47970](https://github.com/elastic/beats/pull/47970)


### Fixes

**Filebeat**
- [Filestream] ensure harvester always restarts if the file has not been fully ingested. [#47107](https://github.com/elastic/beats/pull/47107) [#46923](https://github.com/elastic/beats/issues/46923)
- Prevent panic during startup if dissect processor has invalid field name in tokenizer. [#47839](https://github.com/elastic/beats/pull/47839)

**Metricbeat**
- Improve defensive checks to prevent panics in meraki module. [#47950](https://github.com/elastic/beats/pull/47950)
- Remove GCP Billing timestamp functions. [#47963](https://github.com/elastic/beats/pull/47963) [#47967](https://github.com/elastic/beats/issues/47967)

**Packetbeat**
- Rpc_fragment_sanitization. [#47803](https://github.com/elastic/beats/pull/47803)
- Verify and cap memcache udp fragment counts. [#47874](https://github.com/elastic/beats/pull/47874)


## 9.1.8


### Features and enhancements

**All**
- Include whether Beat is running from a FIPS distribution in User Agent. [#47409](https://github.com/elastic/beats/pull/47409)

**Filebeat**
- Improve logging of cache processor and add ignore failure option. [#47565](https://github.com/elastic/beats/pull/47565)


### Fixes

**All**
- Fix a fatal startup error in Beats Receivers caused by truncation of long UTF-8 hostnames. [#47713](https://github.com/elastic/beats/pull/47713)

**Filebeat**
- Handle and remove BOM during JSON parsing in Azure Blob Storage and GCS inputs. [#47508](https://github.com/elastic/beats/pull/47508)
- Fix an issue where Filebeat could hang during shutdown when using the filestream input. [#47518](https://github.com/elastic/beats/pull/47518)
- Fix double locking in `translate_ldap_attribute` processor and improve logging. [#47585](https://github.com/elastic/beats/pull/47585)
- Fix possible data corruption in TCP, Syslog and Unix inputs. [#47618](https://github.com/elastic/beats/pull/47618)
- Skip AWS S3 test events in Filebeat AWS S3 input. [#47635](https://github.com/elastic/beats/pull/47635)

**Metricbeat**
- [Cloud Connect] Use `cluster.metadata.display_name` as cluster name if set. [#47440](https://github.com/elastic/beats/pull/47440)


## 9.1.7


### Features and enhancements

**Filebeat**
- Add data stream identification to Fleet health status updates. [#47229](https://github.com/elastic/beats/pull/47229)

**Metricbeat**
- Enhance GCP Billing metricset with additional fields. [#47059](https://github.com/elastic/beats/pull/47059)


### Fixes

**All**
- Add `close` to conditional processors if underlying processors have `close` method. [#46653](https://github.com/elastic/beats/pull/46653) [#46575](https://github.com/elastic/beats/issues/46575)
- Fix a bug where Kerberos authentication could be disabled when server supports multiple authentication types. [#47443](https://github.com/elastic/beats/pull/47443) [#47110](https://github.com/elastic/beats/issues/47110)

**Filebeat**
- Fix potential Filebeat panic during memory queue shutdown. [#47248](https://github.com/elastic/beats/pull/47248)

**Metricbeat**
- Add pagination support to the device health metricset in the Meraki module. [#46938](https://github.com/elastic/beats/pull/46938)


## 9.1.6


### Features and enhancements

**Metricbeat**
- Improve the Prometheus helper to handle multiple content types including blank and invalid headers. [#47085](https://github.com/elastic/beats/pull/47085)


### Fixes

**All**
- Prevent panic in logstash output when trying to send events while shutting down. [#46960](https://github.com/elastic/beats/pull/46960)
- Prevent panic in replace processor for non-string values. [#47009](https://github.com/elastic/beats/pull/47009)
- Autodiscover now correctly updates Kubernetes metadata on node and pod label changes. [#47034](https://github.com/elastic/beats/pull/47034)
- Prevent 3s startup delay when add_cloud_metadata is used with debug logs. [#47058](https://github.com/elastic/beats/pull/47058)
- Update elastic-agent-system-metrics to v0.13.3. [#47104](https://github.com/elastic/beats/pull/47104)
  Removes Accurate CPU counts not available on platform log spam at the debug log level.
- Allows users to customize their data stream namespace to generic. [#47140](https://github.com/elastic/beats/pull/47140)

**Filebeat**
- Fix defer usage for stopped status reporting. [#46916](https://github.com/elastic/beats/pull/46916)

**Metricbeat**
- Fix missing AWS cloudwatch metrics with linked accounts and same dimensions. [#46978](https://github.com/elastic/beats/pull/46978)
- Add a fix to handle blank content-type headers in HTTP responses for Prometheus. [#47027](https://github.com/elastic/beats/pull/47027)


## 9.1.5

_This release also includes: [Breaking changes](/docs/release-notes/beats/breaking-changes#beats-9.1.5-breaking-changes)_

### Features and enhancements

**Filebeat**
- Hints based autodiscover now sets `close.on_state_change.removed: false` in the default configuration to avoid missing the last log lines from a container. [34789](https://github.com/elastic/beats/issues/34789) [46695](https://github.com/elastic/beats/pull/46695)

**Metricbeat**
- Log every 401 response from Kubernetes API Server. [42714](https://github.com/elastic/beats/pull/42714)
- Add new metrics to vSphere Virtual Machine dataset (CPU usage percentage, disk average usage, disk read/write rate, number of disk reads/writes, memory usage percentage). [44205](https://github.com/elastic/beats/pull/44205)
- Added checks for the Resty response object in all Meraki module API calls to ensure proper handling of nil responses. [44193](https://github.com/elastic/beats/pull/44193)
- Add latency config option to Azure Monitor module. [44366](https://github.com/elastic/beats/pull/44366)
- Increase default polling period for MongoDB module from 10s to 60s. [44781](https://github.com/elastic/beats/pull/44781)
- Upgrade github.com/microsoft/go-mssqldb version from v1.7.2 to v1.8.2. [44990](https://github.com/elastic/beats/pull/44990)
- Add NTP response validation for system/ntp module. [46184](https://github.com/elastic/beats/pull/46184)
- Add vertexai_logs metricset to GCP for prompt response collection from VertexAI service. [46383](https://github.com/elastic/beats/pull/46383)
- Add default timegrain to Azure Storage Account metricset. [46786](https://github.com/elastic/beats/pull/46786)


### Fixes

**Affecting all Beats**
- Fixed a panic in the Kafka output that could occur when shutting down while final events were being published. [46109](https://github.com/elastic/beats/issues/46109) [46446](https://github.com/elastic/beats/pull/46446)

**Filebeat**
- [Journald input] Fix reading all files in a folder and watching for new ones. [46657](https://github.com/elastic/beats/issues/46657) [46682](https://github.com/elastic/beats/pull/46682)
- The UDP input now fails if it cannot bind to the configured port and its status is set to failed when running under Elastic Agent. [37216](https://github.com/elastic/beats/issues/37216) [46302](https://github.com/elastic/beats/pull/46302)
- The Unix input now fails on errors listening to the socket and its status is set to failed when running under Elastic Agent. [46302](https://github.com/elastic/beats/pull/46302)
- In Filestream, setting `clean_inactive: 0` does not re-ingest all files on startup any more. [45601](https://github.com/elastic/beats/issues/45601) [46373](https://github.com/elastic/beats/pull/46373)
- Fix metrics from TCP & UDP inputs when the port number is > 32767 [46486](https://github.com/elastic/beats/pull/46486)
- [azure-eventhub] Fix handling of connection strings with entity path. [43715](https://github.com/elastic/beats/issues/43715) [43716](https://github.com/elastic/beats/pull/43716)

**Winlogbeat**
- Fix EventLog reset logic to not close renderers. [46376](https://github.com/elastic/beats/pull/46376) {issue}45750{45750}


## 9.1.4


### Features and enhancements

**Filebeat**
- Improve HTTP JSON health status logic for empty template results. [46332](https://github.com/elastic/beats/pull/46332)
- Improve CEL input documentation of authentication options. [46253](https://github.com/elastic/beats/pull/46253)
- Add status reporting support for Azure Event Hub v2 input. [44846](https://github.com/elastic/beats/pull/44846)
- Add documentation for device collection in Entity Analytics Active Directory Filebeat's input. [46363](https://github.com/elastic/beats/pull/46363)

**Metricbeat**
- Add support for Kafka 4.0 in the Kafka module. [44723](https://github.com/elastic/beats/pull/44723)


### Fixes

**Affecting all Beats**
- Fix a race condition during metrics initialization which could cause a panic. [45822](https://github.com/elastic/beats/issues/45822) [46054](https://github.com/elastic/beats/pull/46054)
- Fixed a panic when the beat restarts itself by adding 'eventfd2' to default seccomp policy [46372](https://github.com/elastic/beats/issues/46372)
- Update github.com/go-viper/mapstructure/v2 to v2.4.0 [46335](https://github.com/elastic/beats/pull/46335)
- Update Go version to 1.24.7 [46070](https://github.com/elastic/beats/pull/46070).
- Update github.com/docker/docker to v28.3.3 [46334](https://github.com/elastic/beats/pull/46334)

**Filebeat**
- Fix wrongly emitted missing input ID warning [42969](https://github.com/elastic/beats/issues/42969) [45747](https://github.com/elastic/beats/pull/45747)
- Fix race condition that could cause Filebeat to hang during shutdown after failing to startup [45034](https://github.com/elastic/beats/issues/45034) [46331](https://github.com/elastic/beats/pull/46331)
- Fixed hints autodiscover for Docker when the configuration is only `hints.enabled: true`. [45156](https://github.com/elastic/beats/issues/45156) [45864](https://github.com/elastic/beats/pull/45864)

**Metricbeat**
- Fix an issue where the conntrack metricset entries field reported a count inflated by a factor of the number of CPU cores. [46138](https://github.com/elastic/beats/issues/46138) [46140](https://github.com/elastic/beats/pull/46140)

**Winlogbeat**
- Fix forwarded event handling and add channel error resilience. [46190](https://github.com/elastic/beats/pull/46190)


## 9.1.3


### Features and enhancements

**Affecting all Beats**
- Update Go version to 1.24.5. [45403](https://github.com/elastic/beats/pull/45403)
- Improve trimming of BOM from UTF-8 data in the libbeat `reader/readfile.EncoderReader`. [45742](https://github.com/elastic/beats/pull/45742)

**Filebeat**
- Add mechanism to allow HTTP JSON templates to terminate without logging an error. [45664](https://github.com/elastic/beats/issues/45664) [45810](https://github.com/elastic/beats/pull/45810)
- Add status reporting support for AWS S3 input. [45748](https://github.com/elastic/beats/pull/45748)


### Fixes

**Affecting all Beats**
- Fixed case where Beats would silently fail due to invalid input configuration, now the error is correctly reported. [43118](https://github.com/elastic/beats/issues/43118) [45733](https://github.com/elastic/beats/pull/45733)

**Filebeat**
- Fix handling of unnecessary BOM in UTF-8 text received by o365audit input. [44327](https://github.com/elastic/beats/issues/44327) [45739](https://github.com/elastic/beats/pull/45739)
- Fix reading journald messages with more than 4kb. [45511](https://github.com/elastic/beats/issues/45511) [46017](https://github.com/elastic/beats/pull/46017)
- Restore the Streaming input on Windows. [46031](https://github.com/elastic/beats/pull/46031)
- Fix termination of input on API errors. [45999](https://github.com/elastic/beats/pull/45999)

**Metricbeat**
- Changed Kafka protocol version from 3.6.0 to 2.1.0 to fix compatibility with Kafka 2.x brokers. [45761](https://github.com/elastic/beats/pull/45761)
- Enhance behavior of `sanitizeError`: replace sensitive info even if it is escaped and add pattern-based sanitization. [45857](https://github.com/elastic/beats/pull/45857)


## 9.1.2


### Features and enhancements

**Filebeat**
- Add status reporting support for AWS CloudWatch input. [45679](https://github.com/elastic/beats/pull/45679)

**Winlogbeat**
- Render data values in XML renderer. [44132](https://github.com/elastic/beats/pull/44132)


### Fixes

**Filebeat**
- Fix error handling in ABS input when both root level `max_workers` and `batch_size` are empty. [45680](https://github.com/elastic/beats/issues/45680) [45743](https://github.com/elastic/beats/pull/45743)


## 9.1.1


### Features and enhancements

**Filebeat**
- Log CEL single object evaluation results as ECS compliant documents where possible. [45254](https://github.com/elastic/beats/issues/45254) [45399](https://github.com/elastic/beats/pull/45399)
- Enhanced HTTPJSON input error logging with structured error metadata conforming to Elastic Common Schema (ECS) conventions. [45653](https://github.com/elastic/beats/pull/45653)


### Fixes

**Filebeat**
- Fix a panic in the winlog input that prevented it from starting. [45693](https://github.com/elastic/beats/issues/45693) [45730](https://github.com/elastic/beats/pull/45730)

**Metricbeat**
- Improve error messages in AWS Health [45408](https://github.com/elastic/beats/pull/45408)
- Fix URL construction to handle query parameters properly in GET requests for Jolokia [45620](https://github.com/elastic/beats/pull/45620)


## 9.1.0


### Features and enhancements

**Affecting all Beats**
- Added the `now` processor, which will populate the specified target field with the current timestamp. [44795](https://github.com/elastic/beats/pull/44795)

**Filebeat**
- Refactor & cleanup with updates to default values and documentation. [41834](https://github.com/elastic/beats/pull/41834)
- Add support for SSL and Proxy configurations for websocket type in streaming input. [41934](https://github.com/elastic/beats/pull/41934)
- Filestream take over now supports taking over states from other Filestream inputs and dynamic loading of inputs (autodiscover and Elastic Agent). There is a new syntax for the configuration, but the previous one can still be used. [42472](https://github.com/elastic/beats/issues/42472) [42884](https://github.com/elastic/beats/issues/42884) [42624](https://github.com/elastic/beats/pull/42624)
- Refactor & cleanup with updates to default values and documentation. [41834](https://github.com/elastic/beats/pull/41834)
- Segregated `max_workers` from `batch_size` in the GCS input. [44311](https://github.com/elastic/beats/issues/44311) [44333](https://github.com/elastic/beats/pull/44333)
- Add milliseconds to document timestamp from awscloudwatch Filebeat input [44306](https://github.com/elastic/beats/pull/44306)
- Added support for specifying custom content-types and encodings in azureblobstorage input. [44330](https://github.com/elastic/beats/issues/44330) [44402](https://github.com/elastic/beats/pull/44402)
- Introduce lastSync start position to AWS CloudWatch input backed by state registry. [43251](https://github.com/elastic/beats/pull/43251)
- Add proxy support to GCP Pub/Sub input. [44892](https://github.com/elastic/beats/pull/44892)
- Segregated `max_workers` from `batch_size` in the azure-blob-storage input. [44491](https://github.com/elastic/beats/issues/44491) [44992](https://github.com/elastic/beats/pull/44992)
- Add support for relationship expansion to EntraID entity analytics provider. [43324](https://github.com/elastic/beats/issues/43324) [44761](https://github.com/elastic/beats/pull/44761)
- Update CEL mito extensions to v1.22.0. [45245](https://github.com/elastic/beats/pull/45245)
- Add support for generalized token authentication to CEL input. [45359](https://github.com/elastic/beats/pull/45359)

**Metricbeat**
- Add new metricset wmi for the windows module. [42017](https://github.com/elastic/beats/pull/42017)
- Changed the Elasticsearch module behavior to only pull settings from non-system indices. [43243](https://github.com/elastic/beats/pull/43243)
- Exclude dotted indices from settings pull in Elasticsearch module. [43306](https://github.com/elastic/beats/pull/43306)
- Add a `jetstream` metricset to the NATS module [43310](https://github.com/elastic/beats/pull/43310)
- Update NATS module compatibility. Oldest version supported is now 2.2.6 [43310](https://github.com/elastic/beats/pull/43310)
- Upgrade Prometheus Library to v0.300.1. [43540](https://github.com/elastic/beats/pull/43540)
- Add GCP Dataproc metadata collector in GCP module. [43518](https://github.com/elastic/beats/pull/43518)
- Updated list of supported vSphere versions in the documentation. [43642](https://github.com/elastic/beats/pull/43642)
- Add SSL support for sql module: drivers mysql, postgres, and mssql. [44748](https://github.com/elastic/beats/pull/44748)
- Add VPN metrics to meraki module [44851](https://github.com/elastic/beats/pull/44851)
- Add GCP cache for metadata collectors. [44432](https://github.com/elastic/beats/pull/44432)


### Fixes

**Auditbeat**
- Fix potential data loss in add_session_metadata. [42795](https://github.com/elastic/beats/pull/42795)
- auditbeat/fim: Fix FIM@ebpfevents for new kernels #44371. [44371](https://github.com/elastic/beats/pull/44371)

**Filebeat**
- Log bad handshake details when websocket connection fails [41300](https://github.com/elastic/beats/pull/41300)
- Fix aws region in aws-s3 input s3 polling mode.  [41572](https://github.com/elastic/beats/pull/41572)
- Fix a logging regression that ignored to_files and logged to stdout. [44573](https://github.com/elastic/beats/pull/44573)
- Fixed issue for "Root level readerConfig no longer respected" in azureblobstorage input. [44812](https://github.com/elastic/beats/issues/44812) [44873](https://github.com/elastic/beats/pull/44873)
- Fixed password authentication for ACL users in the Redis input of Filebeat. [44137](https://github.com/elastic/beats/pull/44137)
- The data and logs path has changed on Windows to `$env:ProgramFiles`. See the breaking changes page for more details.

**Heartbeat**
- Added maintenance windows support for Heartbeat. [41508](https://github.com/elastic/beats/pull/41508)


## 9.0.8

_This release also includes: [Breaking changes](/docs/release-notes/beats/breaking-changes#beats-9.0.8-breaking-changes)_

### Features and enhancements

**Metricbeat**
- Upgrade github.com/microsoft/go-mssqldb version from v1.7.2 to v1.8.2. [44990](https://github.com/elastic/beats/pull/44990)
- Add SSL support for SQL modules: drivers Mysql, PostgreSQL, and MSSQL. [44748](https://github.com/elastic/beats/pull/44748)
- Add NTP response validation for system/ntp module. [46184](https://github.com/elastic/beats/pull/46184)
- Add vertexai_logs metricset to GCP for prompt response collection from VertexAI service. [46383](https://github.com/elastic/beats/pull/46383)
- Add default timegrain to Azure Storage Account metricset. [46786](https://github.com/elastic/beats/pull/46786)


### Fixes

**Affecting all Beats**
- Update github.com/docker/docker to v28.3.3 [46334](https://github.com/elastic/beats/pull/46334)
- Fixed a panic in the Kafka output that could occur when shutting down while final events were being published. [46109](https://github.com/elastic/beats/issues/46109) [46446](https://github.com/elastic/beats/pull/46446)

**Filebeat**
- The UDP input now fails if it cannot bind to the configured port and its status is set to failed when running under Elastic Agent. [37216](https://github.com/elastic/beats/issues/37216) [46302](https://github.com/elastic/beats/pull/46302)
- The Unix input now fails on errors listening to the socket and its status is set to failed when running under Elastic Agent. [46302](https://github.com/elastic/beats/pull/46302)
- [Journald input] Fix reading all files in a folder and watching for new ones. [46657](https://github.com/elastic/beats/issues/46657) [46682](https://github.com/elastic/beats/pull/46682)
- [azure-eventhub] Fix handling of connection strings with entity path. [43715](https://github.com/elastic/beats/issues/43715) [43716](https://github.com/elastic/beats/pull/43716)

**Metricbeat**
- Do not log an error if metadata enrichment is disabled for K8's module. [46536](https://github.com/elastic/beats/pull/46536)
- Fix Azure Monitor wildcard metrics names timegrain issue by using the first, smallest timegrain; fix nil pointer issue. [46145](https://github.com/elastic/beats/pull/46145)

**Winlogbeat**
- Fix EventLog reset logic to not close renderers. [46376](https://github.com/elastic/beats/pull/46376) {issue}45750{45750}


## 9.0.7


### Features and enhancements

**Filebeat**
- Improve HTTP JSON health status logic for empty template results. [46332](https://github.com/elastic/beats/pull/46332)
- Improve CEL input documentation of authentication options. [46253](https://github.com/elastic/beats/pull/46253)
- Add documentation for device collection in Entity Analytics Active Directory Filebeat's input. [46363](https://github.com/elastic/beats/pull/46363)

**Metricbeat**
- Add support for Kafka 4.0 in the Kafka module. [44723](https://github.com/elastic/beats/pull/44723)


### Fixes

**Affecting all Beats**
- Fixed case where Beats would silently fail due to invalid input configuration, now the error is correctly reported. [43118](https://github.com/elastic/beats/issues/43118) [45733](https://github.com/elastic/beats/pull/45733)
- Fix a race condition during metrics initialization which could cause a panic. [45822](https://github.com/elastic/beats/issues/45822) [46054](https://github.com/elastic/beats/pull/46054)
- Update Go version to 1.24.7 [46070](https://github.com/elastic/beats/pull/46070).
- Fixed a panic when the beat restarts itself by adding 'eventfd2' to default seccomp policy [46372](https://github.com/elastic/beats/issues/46372)
- Update github.com/go-viper/mapstructure/v2 to v2.4.0 [46335](https://github.com/elastic/beats/pull/46335)

**Filebeat**
- Fix wrongly emitted missing input ID warning [42969](https://github.com/elastic/beats/issues/42969) [45747](https://github.com/elastic/beats/pull/45747)
- Fix race condition that could cause Filebeat to hang during shutdown after failing to startup [45034](https://github.com/elastic/beats/issues/45034) [46331](https://github.com/elastic/beats/pull/46331)

**Metricbeat**
- Fix an issue where the conntrack metricset entries field reported a count inflated by a factor of the number of CPU cores. [46138](https://github.com/elastic/beats/issues/46138) [46140](https://github.com/elastic/beats/pull/46140)

**Winlogbeat**
- Fix forwarded event handling and add channel error resilience. [46190](https://github.com/elastic/beats/pull/46190)


## 9.0.6


### Features and enhancements

**Affecting all Beats**
- Update Go version to 1.24.5. [45403](https://github.com/elastic/beats/pull/45403)

**Filebeat**
- Add mechanism to allow HTTP JSON templates to terminate without logging an error. [45664](https://github.com/elastic/beats/issues/45664) [45810](https://github.com/elastic/beats/pull/45810)

**Winlogbeat**
- Render data values in XML renderer. [44132](https://github.com/elastic/beats/pull/44132)


### Fixes

**Filebeat**
- Fix handling of unnecessary BOM in UTF-8 text received by o365audit input. [44327](https://github.com/elastic/beats/issues/44327) [45739](https://github.com/elastic/beats/pull/45739)
- Fix reading journald messages with more than 4kb. [45511](https://github.com/elastic/beats/issues/45511) [46017](https://github.com/elastic/beats/pull/46017)
- Restore the Streaming input on Windows. [46031](https://github.com/elastic/beats/pull/46031)
- Fix termination of input on API errors. [45999](https://github.com/elastic/beats/pull/45999)
- Fix filestream registry entries being prematurely removed, which could cause files to be re-ingested after Filebeat restarts. [46007](https://github.com/elastic/beats/issues/46007) [46032](https://github.com/elastic/beats/pull/46032)

**Metricbeat**
- Changed Kafka protocol version from 3.6.0 to 2.1.0 to fix compatibility with Kafka 2.x brokers. [45761](https://github.com/elastic/beats/pull/45761)
- Enhance behavior of `sanitizeError`: replace sensitive info even if it is escaped and add pattern-based sanitization. [45857](https://github.com/elastic/beats/pull/45857)


## 9.0.5


### Features and enhancements

**Filebeat**
- Enhanced HTTPJSON input error logging with structured error metadata conforming to Elastic Common Schema (ECS) conventions. [45653](https://github.com/elastic/beats/pull/45653)

**Metricbeat**
- Improve error messages in AWS Health. [45408](https://github.com/elastic/beats/pull/45408)


### Fixes

**Auditbeat**
- Auditd: Request status from a separate socket to avoid data congestion. [41207](https://github.com/elastic/beats/pull/41207)
- Fix potential data loss in `add_session_metadata`. [42795](https://github.com/elastic/beats/pull/42795)

**Metricbeat**
- Fix URL construction to handle query parameters properly in GET requests for Jolokia. [45620](https://github.com/elastic/beats/pull/45620)


## 9.0.4


### Features and enhancements

**Filebeat**
- Add Fleet status updating to GCS input. [44273](https://github.com/elastic/beats/issues/44273) [44508](https://github.com/elastic/beats/pull/44508)
- Add Fleet status update functionality to udp input. [44419](https://github.com/elastic/beats/issues/44419) [44785](https://github.com/elastic/beats/pull/44785)
- Add Fleet status update functionality to tcp input. [44420](https://github.com/elastic/beats/issues/44420) [44786](https://github.com/elastic/beats/pull/44786)
- Add Fleet status updating to Azure Blob Storage input. [44268](https://github.com/elastic/beats/issues/44268) [44945](https://github.com/elastic/beats/pull/44945)
- Add Fleet status updating to HTTP JSON input. [44282](https://github.com/elastic/beats/issues/44282) [44365](https://github.com/elastic/beats/pull/44365)
- Add input metrics to Azure Blob Storage input. [36641](https://github.com/elastic/beats/issues/36641) [43954](https://github.com/elastic/beats/pull/43954)
- Add support for websocket keep_alive heartbeat in the streaming input. [42277](https://github.com/elastic/beats/issues/42277) [44204](https://github.com/elastic/beats/pull/44204)
- Add missing "text/csv" content-type filter support in GCS input. [44922](https://github.com/elastic/beats/issues/44922) [44923](https://github.com/elastic/beats/pull/44923)

**Heartbeat**
- Upgrade Node version to latest LTS v20.19.3. [45087](https://github.com/elastic/beats/pull/45087)
- Add base64 encoding option to inline monitors. [45100](https://github.com/elastic/beats/pull/45100)

**Metricbeat**
- Upgrade github.com/microsoft/go-mssqldb version from v1.7.2 to v1.8.2. [44990](https://github.com/elastic/beats/pull/44990)


### Fixes

**Affecting all Beats**
- The Elasticsearch output now correctly applies exponential backoff when being throttled by 429s ("too many requests") from Elasticsarch. [36926](https://github.com/elastic/beats/issues/36926) [45073](https://github.com/elastic/beats/pull/45073)

**Winlogbeat**
- Fix EvtVarTypeAnsiString conversion. [44026](https://github.com/elastic/beats/pull/44026)


## 9.0.3


### Features and enhancements

**Affecting all Beats**
- Update to Go 1.24.4. [44696](https://github.com/elastic/beats/pull/44696)

**Filebeat**
- Fix handling of ADC (Application Default Credentials) metadata server credentials in HTTPJSON input. [44349](https://github.com/elastic/beats/issues/44349) [44436](https://github.com/elastic/beats/pull/44436)
- Fix handling of ADC (Application Default Credentials) metadata server credentials in CEL input. [44349](https://github.com/elastic/beats/issues/44349) [44571](https://github.com/elastic/beats/pull/44571)
- Filestream now logs at level warn the number of files that are too small to be ingested [44751](https://github.com/elastic/beats/pull/44751)

**Metricbeat**
- Add check for http error codes in the Metricbeat's Prometheus query submodule [44493](https://github.com/elastic/beats/pull/44493)
- Increase default polling period for MongoDB module from 10s to 60s [44781](https://github.com/elastic/beats/pull/44781)


### Fixes

**Affecting all Beats**
- Fix `dns` processor to handle IPv6 server addresses properly. [44526](https://github.com/elastic/beats/pull/44526)
- Fix an issue where the Kafka output could get stuck if a proxied connection to the Kafka cluster was reset. [44606](https://github.com/elastic/beats/issues/44606)
- Use Debian 11 to build linux/arm to match linux/amd64. Upgrades linux/arm64's statically linked glibc from 2.28 to 2.31. [44816](https://github.com/elastic/beats/issues/44816)

**Filebeat**
- Handle special values of accountExpires in the Activedirectory Entity Analytics provider. [43364](https://github.com/elastic/beats/pull/43364)
- Fix status reporting panic in GCP Pub/Sub input. [44624](https://github.com/elastic/beats/issues/44624) [44625](https://github.com/elastic/beats/pull/44625)
- If a Filestream input fails to be created, its ID is removed from the list of running input IDs [44697](https://github.com/elastic/beats/pull/44697)
- Fix timeout handling by Crowdstrike streaming input. [44720](https://github.com/elastic/beats/pull/44720)
- Ensure DEPROVISIONED Okta entities are published by Okta entityanalytics provider. [12658](https://github.com/elastic/beats/issues/12658) [44719](https://github.com/elastic/beats/pull/44719)
- Fix handling of cursors by the streaming input for Crowdstrike. [44364](https://github.com/elastic/beats/issues/44364) [44548](https://github.com/elastic/beats/pull/44548)
- Added missing "text/csv" content-type filter support in azureblobsortorage input. [44596](https://github.com/elastic/beats/issues/44596) [44824](https://github.com/elastic/beats/pull/44824)
- Fix unexpected EOF detection and improve memory usage. [44813](https://github.com/elastic/beats/pull/44813)

**Heartbeat**
- Add missing dependencies to ubi9-minimal distro. [44556](https://github.com/elastic/beats/pull/44556)

**Metricbeat**
- Fix panic in kafka consumergroup member assignment fetching when there are 0 members in consumer group. [44576](https://github.com/elastic/beats/pull/44576)
- Sanitize error messages in Fetch method of SQL module [44577](https://github.com/elastic/beats/pull/44577)
- Upgrade `go.mongodb.org/mongo-driver` from `v1.14.0` to `v1.17.4` to fix connection leaks in MongoDB module [44769](https://github.com/elastic/beats/pull/44769)


## 9.0.2


### Features and enhancements

**Affecting all Beats**
- Update Go version to v1.24.3. [44270](https://github.com/elastic/beats/pull/44270)

**Filebeat**
- Add support for collecting device entities in the Active Directory entity analytics provider. [44309](https://github.com/elastic/beats/pull/44309)
- The `add_cloudfoundry_metadata` processor now uses `xxhash` instead of `SHA1` for sanitizing persistent cache filenames. Existing users will experience a one-time cache invalidation as the cache store will be recreated with the new filename format. [43964](https://github.com/elastic/beats/pull/43964)

**Metricbeat**
- Add checks for the Resty response object in all Meraki module API calls to ensure proper handling of nil responses. [44193](https://github.com/elastic/beats/pull/44193)
- Add a latency configuration option to the Azure Monitor module. [44366](https://github.com/elastic/beats/pull/44366)

**Osquerybeat**
- Update osquery version to v5.15.0. [43426](https://github.com/elastic/beats/pull/43426)


### Fixes

**Affecting all Beats**
- Fix the 'add_cloud_metadata' processor to better support custom certificate bundles by improving how the AWS provider HTTP client is overridden. [44189](https://github.com/elastic/beats/pull/44189)

**Auditbeat**
- Fix a potential error in the system/package component that could occur during internal package database schema migration. [44294](https://github.com/elastic/beats/issues/44294) [44296](https://github.com/elastic/beats/pull/44296)

**Filebeat**
- Fix endpoint path typo in the Okta entity analytics provider. [44147](https://github.com/elastic/beats/pull/44147)
- Fix a WebSocket panic scenario that occured after exhausting the maximum number of retries. [44342](https://github.com/elastic/beats/pull/44342)

**Metricbeat**
- Add AWS OwningAccount support for cross-account monitoring. [40570](https://github.com/elastic/beats/issues/40570) [40691](https://github.com/elastic/beats/pull/40691)
- Use namespace for GetListMetrics calls in AWS when available. [41022](https://github.com/elastic/beats/pull/41022)
- Limit index stats collection to cluster-level summaries. [36019](https://github.com/elastic/beats/issues/36019) [42901](https://github.com/elastic/beats/pull/42901)
- Omit `tier_preference`, `creation_date` and `version` fields in output documents when not pulled from source indices. [43637](https://github.com/elastic/beats/pull/43637)
- Add support for `_nodes/stats` URIs compatible with legacy Elasticsearch versions. [44307](https://github.com/elastic/beats/pull/44307)


## 9.0.1


### Features and enhancements

- For all Beats: Publish `cloud.availability_zone` by `add_cloud_metadata` processor in Azure environments. [#42601](https://github.com/elastic/beats/issues/42601) [#43618](https://github.com/elastic/beats/pull/43618)
- Add pagination batch size support to Entity Analytics input's Okta provider in Filebeat. [#43655](https://github.com/elastic/beats/pull/43655)
- Update CEL mito extensions version to v1.19.0 in Filebeat. [#44098](https://github.com/elastic/beats/pull/44098)
- Upgrade node version to latest LTS v18.20.7 in Heartbeat. [#43511](https://github.com/elastic/beats/pull/43511)
- Add `enable_batch_api` option in Azure monitor to allow metrics collection of multiple resources using Azure batch API in Metricbeat. [#41790](https://github.com/elastic/beats/pull/41790)


### Fixes

- For all Beats: Handle permission errors while collecting data from Windows services and don't interrupt the overall collection by skipping affected services. [#40765](https://github.com/elastic/beats/issues/40765) [#43665](https://github.com/elastic/beats/pull/43665).
- Fixed WebSocket input panic on sudden network error or server crash in Filebeat. [#44063](https://github.com/elastic/beats/issues/44063) [44068](https://github.com/elastic/beats/pull/44068).
- [Filestream] Log the "reader closed" message on the debug level to avoid log spam in Filebeat. [#44051](https://github.com/elastic/beats/pull/44051)
- Fix links to CEL mito extension functions in input documentation in Filebeat. [#44098](https://github.com/elastic/beats/pull/44098)


## 9.0.0


### Features and enhancements

- Improves logging in system/socket in Auditbeat. [#41571](https://github.com/elastic/beats/pull/41571)
- Adds out of the box support for Amazon EventBridge notifications over SQS to S3 input in Filebeat. [#40006](https://github.com/elastic/beats/pull/40006)
- Update CEL mito extensions to v1.16.0 in Filebeat. [#41727](https://github.com/elastic/beats/pull/41727)
- Filebeat's registry is now added to the Elastic-Agent diagnostics bundle. [#33238](https://github.com/elastic/beats/issues/33238) and [#41795](https://github.com/elastic/beats/pull/41795)
- Adds `unifiedlogs` input for MacOS in Filebeat. [#41791](https://github.com/elastic/beats/pull/41791)
- Adds evaluation state dump debugging option to CEL input in Filebeat. [#41335](https://github.com/elastic/beats/pull/41335)
- Rate limiting operability improvements in the Okta provider of the Entity Analytics input in Filebeat. [#40106](https://github.com/elastic/beats/issues/40106) and [#41977](https://github.com/elastic/beats/pull/41977)
- Rate limiting fault tolerance improvements in the Okta provider of the Entity Analytics input in Filebeat. [#40106](https://github.com/elastic/beats/issues/40106) [#42094](https://github.com/elastic/beats/pull/42094)
- Introduces ignore older and start timestamp filters for AWS S3 input in Filebeat. [#41804](https://github.com/elastic/beats/pull/41804)
- Journald input now can report its status to Elastic-Agent in Filebeat. [#39791](https://github.com/elastic/beats/issues/39791) and [#42462](https://github.com/elastic/beats/pull/42462)
- Publish events progressively in the Okta provider of the Entity Analytics input in Filebeat. [#40106](https://github.com/elastic/beats/issues/40106) and [#42567](https://github.com/elastic/beats/pull/42567)
- Journald `include_matches.match` now accepts `+` to represent a logical disjunction (OR) in Filebeat. [#40185](https://github.com/elastic/beats/issues/40185) and #[42517](https://github.com/elastic/beats/pull/42517)
- The journald input is now generally available in Filebeat. [#42107](https://github.com/elastic/beats/pull/42107)
- Adds support for RFC7231 methods to HTTP monitors in Heartbeat. [#41975](https://github.com/elastic/beats/pull/41975)
- Adds `use_kubeadm` config option in kubernetes module in order to toggle kubeadm-config API requests in Metricbeat. [#40086](https://github.com/elastic/beats/pull/40086)
- Preserve queries for debugging when `merge_results: true` in SQL module in Metricbeat. [#42271](https://github.com/elastic/beats/pull/42271)
- Collect more fields from ES node/stats metrics and only those that are necessary in Metricbeat. [#42421](https://github.com/elastic/beats/pull/42421)
- Adds benchmark module in Metricbeat. [#41801](https://github.com/elastic/beats/pull/41801)
- Increase maximum query timeout to 24 hours in Osquerybeat. [42356](https://github.com/elastic/beats/pull/42356)
- Properly set events `UserData` when experimental API is used in Winlogbeat. [#41525](https://github.com/elastic/beats/pull/41525)
- Include XML is respected for experimental API in Winlogbeat. [#41525](https://github.com/elastic/beats/pull/41525)
- Forwarded events use renderedtext info for experimental API in Winlogbeat. [#41525](https://github.com/elastic/beats/pull/41525)
- Language setting is respected for experimental API in Winlogbeat. [#41525](https://github.com/elastic/beats/pull/41525)
- Language setting also added to decode XML wineventlog processor in Winlogbeat. [#41525](https://github.com/elastic/beats/pull/41525)
- Format embedded messages in the experimental API in Winlogbeat. [#41525](https://github.com/elastic/beats/pull/41525)
- Make the experimental API GA and rename it to winlogbeat-raw in Winlogbeat. [#39580](https://github.com/elastic/beats/issues/39580) and [#41770](https://github.com/elastic/beats/pull/41770)
- Removes 22 clause limitation in Winlogbeat. [#35047](https://github.com/elastic/beats/issues/35047) and [#42187](https://github.com/elastic/beats/pull/42187)
- Adds handling for recoverable publisher disabled errorsin Winlogbeat. [#35316](https://github.com/elastic/beats/issues/35316) and [#42187](https://github.com/elastic/beats/pull/42187)
- Removes Functionbeat binaries from CI pipelines. [#40745](https://github.com/elastic/beats/issues/40745) and [#41506](https://github.com/elastic/beats/pull/41506)
- Update Go version to 1.24.0. [#42705](https://github.com/elastic/beats/pull/42705)
- Add `etw` input fallback to attach an already existing session in Filebeat. [#42847](https://github.com/elastic/beats/pull/42847)
- Update CEL mito extensions to v1.17.0 in Filebeat. [#42851](https://github.com/elastic/beats/pull/42851)
- Winlog input  in Filebeat cam now report its status to Elastic Agent. [#43089](https://github.com/elastic/beats/pull/43089)
- Add configuration option to limit HTTP Endpoint body size in Filebeat. [#43171](https://github.com/elastic/beats/pull/43171)
- Add a new `match_by_parent_instance` option to `perfmon` module in Metricbeat. [#43002](https://github.com/elastic/beats/pull/43002)
- Add a warning log to `metricbeat.vsphere` in Metricbeat in case vSphere connection has been configured as insecure. [#43104](https://github.com/elastic/beats/pull/43104)


### Fixes

- hasher: Add a cached hasher for upcoming backend in Auditbeat. [#41952](https://github.com/elastic/beats/pull/41952)
- Split common tty definitions in Auditbeat. [#42004](https://github.com/elastic/beats/pull/42004)
- Redact authorization headers in HTTPJSON debug logs in Filebeat. [#41920](https://github.com/elastic/beats/pull/41920)
- Further rate limiting fix in the Okta provider of the Entity Analytics input in Filebeat. [#40106](https://github.com/elastic/beats/issues/40106) and [#41977](https://github.com/elastic/beats/pull/41977)
- The `_id` generation process for S3 events has been updated to incorporate the LastModified field. This enhancement ensures that the `_id` is unique in Filebeat. [#42078](https://github.com/elastic/beats/pull/42078)
- Fixes truncation of bodies in request tracing by limiting bodies to 10% of the maximum file size in Filebeat. [#42327](https://github.com/elastic/beats/pull/42327)
- [Journald] Fixes handling of `journalctl` restart. A known symptom was broken multiline messages when there was a restart of journalctl while aggregating the lines in Filebeat. [#41331](https://github.com/elastic/beats/issues/41331) and [#42595](https://github.com/elastic/beats/pull/42595)
- Fixwa bug where Metricbeat unintentionally triggers Windows ASR in Metricbeat. [#42177](https://github.com/elastic/beats/pull/42177)
- Removes `hostname` field from ZooKeeper's `mntr` data stream in Metricbeat. [41887](https://github.com/elastic/beats/pull/41887)
- Properly marshal nested structs in ECS fields, fixing issues with mixed cases in field names in Packetbeat. [42116](https://github.com/elastic/beats/pull/42116)
- Fixed race conditions in the global ratelimit processor that could drop events or apply rate limiting incorrectly in Filebeat. [42966](https://github.com/elastic/beats/pull/42966)
- Prevent computer details being returned for user queries by Activedirectory Entity Analytics provider in Filebeat. [#11818](https://github.com/elastic/beats/issues/11818) and [#42796](https://github.com/elastic/beats/pull/42796)
- Handle unexpected EOF error in aws-s3 input and enforce retrying using download failed error in Filebeat. [#42420](https://github.com/elastic/beats/pull/42420)
- Prevent azureblobstorage input from logging key details during blob fetch operations in Filebeat. [#43169](https://github.com/elastic/beats/pull/43169)
- Add AWS OwningAccount support for cross account monitoring in Metricbeat. [#40570](https://github.com/elastic/beats/issues/40570) and [#40691](https://github.com/elastic/beats/pull/40691)
- Fix logging argument number mismatch in Metricbeat(Redis). [#43072](https://github.com/elastic/beats/pull/43072)
- Reset EventLog if error EOF is encountered in Winlogbeat. [#42826](https://github.com/elastic/beats/pull/42826)
- Implement backoff on error retrial in Winlogbeat. [#42826](https://github.com/elastic/beats/pull/42826)
- Fix boolean key in security pipelines and sync pipelines with integration in Winlogbeat. [#43027](https://github.com/elastic/beats/pull/43027)