# Source: https://www.elastic.co/docs/release-notes/elastic-agent

﻿---
title: Elastic Agent release notes
description: Review the changes, fixes, and more in each version of Elastic Agent. To check for security updates, go to Security announcements for the Elastic Stack...
url: https://www.elastic.co/docs/release-notes/elastic-agent
products:
  - Elastic Agent
applies_to:
  - Elastic Stack: Generally available
---

# Elastic Agent release notes
Review the changes, fixes, and more in each version of Elastic Agent.
To check for security updates, go to [Security announcements for the Elastic Stack](https://discuss.elastic.co/c/announcements/security-announcements/31).
<admonition title="Related release notes">
  Elastic Agent integrates and manages Beats for data collection, and Beats changes may impact Elastic Agent functionality. To check for Elastic Agent changes in Beats, go to [Beats release notes](https://www.elastic.co/docs/release-notes/beats).
</admonition>


## 9.3.1

_This release also includes: [Deprecations](/docs/release-notes/elastic-agent/deprecations#elastic-agent-9.3.1-deprecations)._

### Features and enhancements

- Support the `-—prefix` flag when installing from RPM. [#12263](https://github.com/elastic/elastic-agent/pull/12263) [#141](https://github.com/elastic/elastic-agent/issues/141)
- Add `agent.internal.runtime.dynamic_inputs` flag to control the runtime used by inputs using dynamic variables. [#12438](https://github.com/elastic/elastic-agent/pull/12438) [#11630](https://github.com/elastic/elastic-agent/issues/11630)
- Update OTel Collector components to v0.144.0. [#12449](https://github.com/elastic/elastic-agent/pull/12449)
- Add `statsd` receiver to EDOT Collector. [#12628](https://github.com/elastic/elastic-agent/pull/12628)
- Add `logdedup` processor to EDOT as an extended component. [#12654](https://github.com/elastic/elastic-agent/pull/12654) [#6869](https://github.com/elastic/ingest-dev/issues/6869)
- Include more standard metadata in monitoring events from the OTel Collector. [#12717](https://github.com/elastic/elastic-agent/pull/12717)


### Fixes

- Add a missing dependency for Synthetics on Wolfi Docker image. [#12453](https://github.com/elastic/elastic-agent/pull/12453)
- Fix becoming unhealthy when using the `warn` log level. [#12519](https://github.com/elastic/elastic-agent/pull/12519) [#12513](https://github.com/elastic/elastic-agent/issues/12513)
- Fix an issue where monitoring could reingest its own error logs in a feedback loop. [#12663](https://github.com/elastic/elastic-agent/pull/12663) [#12524](https://github.com/elastic/elastic-agent/issues/12524)
- Fix OTel Collector not receiving `service.telemetry` config from persisted file. [#12736](https://github.com/elastic/elastic-agent/pull/12736) [#12737](https://github.com/elastic/elastic-agent/issues/12737)


## 9.3.0build202602051825

<note>
  This is an independent Elastic Agent release. Independent Elastic Agent releases deliver critical fixes and updates for Elastic Agent and Elastic Defend independently of a full Elastic Stack release. Read more in [Elastic Agent release process](https://www.elastic.co/docs/reference/fleet/fleet-agent-release-process).
</note>


### Fixes

- Fixes a bug in version 9.3.0 of Elastic Defend that resulted in the Windows Security Center status page showing an error.
- Fixes a DNS parsing bug in Linux versions of Elastic Defend.


## 9.3.0

_This release also includes: [Breaking changes](/docs/release-notes/elastic-agent/breaking-changes#elastic-agent-9.3.0-breaking-changes) and [Known issues](https://www.elastic.co/docs/release-notes/elastic-agent/known-issues)._

### Features and enhancements

- Add support for logstash output to elastic agent standalone helm chart. [#10644](https://github.com/elastic/elastic-agent/pull/10644)
- Enable cpu and disk hostmetrics scrapers for Darwin configurations. [#11423](https://github.com/elastic/elastic-agent/pull/11423)
- Add support for downgrading a running Agents privileges from Fleet. [#10231](https://github.com/elastic/elastic-agent/pull/10231)
- Add awss3receiver to EDOT. [#10515](https://github.com/elastic/elastic-agent/pull/10515) [#604](https://github.com/elastic/obs-integration-team/issues/604)
- Add awslogsencodingextension to EDOT. [#11107](https://github.com/elastic/elastic-agent/pull/11107)
- Add opex to elastic-agent helm chart. This change adds the Opex-CCM support to the offical elastic-agent helm chart deployment. [#9363](https://github.com/elastic/elastic-agent/pull/9363)
- Add windowseventlogreceiver to EDOT. [#11418](https://github.com/elastic/elastic-agent/pull/11418)
- Allow setting component runtime per input type. [#11186](https://github.com/elastic/elastic-agent/pull/11186)
- Improve metrics monitoring coverage for OTel-based ingestion. [#11813](https://github.com/elastic/elastic-agent/pull/11813)
  Extend ingestion of OTel collector internal telemetry to give more detailed metrics, including support for both monitoring and non-monitoring components in the same collector.
- Allow manually initiating an upgrade rollback within a configurable window. [#11955](https://github.com/elastic/elastic-agent/pull/11955) [#6881](https://github.com/elastic/elastic-agent/issues/6881)
- Add SNMP receiver to EDOT Collector. [#12239](https://github.com/elastic/elastic-agent/pull/12239)
- Restore cloud-defend to the basic and complete Docker images. [#11795](https://github.com/elastic/elastic-agent/pull/11795)
- Make otel default runtime for system\metrics input. [#11613](https://github.com/elastic/elastic-agent/pull/11613)
- Update OTel Collector components to v0.141.0. [#11671](https://github.com/elastic/elastic-agent/pull/11671)
- Change default runtime for select metricbeat inputs. [#11754](https://github.com/elastic/elastic-agent/pull/11754)
  The following metricbeat inputs will use the otel runtime by default if the elasticsearch output is used:
  - activemq/metrics
- apache/metrics
- beat/metrics
- containerd/metrics
- docker/metrics
- elasticsearch/metrics
- etcd/metrics
- http/metrics
- jolokia/metrics
- kafka/metrics
- kibana/metrics
- linux/metrics
- logstash/metrics
- memcached/metrics
- mongodb/metrics
- mysql/metrics
- nats/metrics
- nginx/metrics
- rabbitmq/metrics
- sql/metrics
- stan/metrics
- statsd/metrics
- system/metrics
- vsphere/metrics
  This will result in a memory reduction since fewer agentbeat processes are started, because the otel runtime runs within the collector process.  If the policy is not compatible with the otel runtime, it will fall back to the process runtime.
- Improve input not supported error message to reference installation flavors. [#11825](https://github.com/elastic/elastic-agent/pull/11825)
- Add service.instance.id to k8s attributes in helm charts. [#11844](https://github.com/elastic/elastic-agent/pull/11844)
- Reduce installation size for all versions of the Elastic Agent. [#11821](https://github.com/elastic/elastic-agent/pull/11821)
  The Elastic Agent now ships with a single elastic-otel-collector binary that contains both the
  OTEL collector, beats receivers, and beat modules. This reduces the size of the Elastic Agent roughly
  ~200MB (amount depends on the platform). The elastic-agent.exe has also been greatly reduced from ~400M to ~75M.
- Add prometheusremotewrite receiver to EDOT. [#11937](https://github.com/elastic/elastic-agent/pull/11937)
- Replace elastic-agent/collector component name with elastic-otel-collector in self-monitoring. [#12364](https://github.com/elastic/elastic-agent/pull/12364)
  Make self-monitoring metrics consistently use the name of the new elastic-otel-collector binary executing the EDOT collector and beats receivers.
- Rotated container logs can be ingested using the helm-chart by setting `kubernetes.containers.logs.rotated_logs=true`. [#11783](https://github.com/elastic/elastic-agent/pull/11783) [#11559](https://github.com/elastic/elastic-agent/issues/11559)


### Fixes

- Report crashing otel process cleanly with proper status reporting. [#11448](https://github.com/elastic/elastic-agent/pull/11448)
- Fix kube-stack null template evaluation for Helm v4. [#11481](https://github.com/elastic/elastic-agent/pull/11481)
- Ensure the self-monitoring configuration accounts for the runtime components actually run in. [#11300](https://github.com/elastic/elastic-agent/pull/11300)
- Add environment.yaml file to diagnostics. [#11484](https://github.com/elastic/elastic-agent/pull/11484) [#10966](https://github.com/elastic/elastic-agent/issues/10966)
- Merge multiple agent keys when loading config. [#11619](https://github.com/elastic/elastic-agent/pull/11619) [#3717](https://github.com/elastic/elastic-agent/issues/3717)
- Hide healthcheckv2 from status output. [#11718](https://github.com/elastic/elastic-agent/pull/11718)
- Set path.home for beat receivers to components directory. [#11726](https://github.com/elastic/elastic-agent/pull/11726) [#48010](https://github.com/elastic/beats/issues/48010)
- Fix signature verification using the upgrade command with the --source-uri flag for fleet-managed agents. [#11826](https://github.com/elastic/elastic-agent/pull/11826) [#11152](https://github.com/elastic/elastic-agent/issues/11152)
- Handle curve_types to []curve_types conversion for elasticsearch config translation. [#11892](https://github.com/elastic/elastic-agent/pull/11892) [#11776](https://github.com/elastic/elastic-agent/issues/11776)
- Avoid uninstall and reinstalling service components on policy changes or reassignments. [#11740](https://github.com/elastic/elastic-agent/pull/11740)
- Fix reloading agent.logging.level for standalone Elastic Agent. [#11998](https://github.com/elastic/elastic-agent/pull/11998)
- Fix FLEET_TOKEN_POLICY_NAME environment variable for the container command to handle cases where there are more than 20 agent policies available. [#12073](https://github.com/elastic/elastic-agent/pull/12073) [#12069](https://github.com/elastic/elastic-agent/issues/12069)
- This updates the kube-stack otel gateway collector endpoint to be OTEL_K8S_POD_IP as the previous value was causing an undefined log warning. [#12205](https://github.com/elastic/elastic-agent/pull/12205)
- Emit the correct error message when the app lock cannot be acquired. [#12225](https://github.com/elastic/elastic-agent/pull/12225)
- Fix diagnostics socket path for read-only container filesystems. [#12312](https://github.com/elastic/elastic-agent/pull/12312) [#11572](https://github.com/elastic/elastic-agent/issues/11572)


## 9.2.6


### Features and enhancements

- Update OTel Collector components to v0.144.0. [#12735](https://github.com/elastic/elastic-agent/pull/12735)
- Add statsd receiver to EDOT Collector. [#12628](https://github.com/elastic/elastic-agent/pull/12628)


### Fixes

- Adds a missing dependency for Synthetics on wolfi docker image. [#12453](https://github.com/elastic/elastic-agent/pull/12453)


## 9.2.5


### Features and enhancements

- Support --prefix flag when installing from RPM. [#12263](https://github.com/elastic/elastic-agent/pull/12263)


### Fixes

- OSQuery - Add list capabilities to directories for interactive users. [#12189](https://github.com/elastic/elastic-agent/pull/12189)
  Fixing file permission issues for osquery extensions on Windows.
  It approches the problem by adding List Content permission to Logged in users so Directory permissions are not altered by UAC when traversing Agent directory structure.
  After this user wont be prompted with UAC and when opening e.g log files, instead user will run into access denied in editor of choice.
  Elevated editor must be used to open files that require elevated permissions.
- Update the kube-stack otel gateway collector endpoint to be OTEL_K8S_POD_IP as the previous value was causing an undefined log warning. [#12205](https://github.com/elastic/elastic-agent/pull/12205)
- Emit the correct error message when the app lock cannot be acquired. [#12225](https://github.com/elastic/elastic-agent/pull/12225)
- Fix elasticsearch retry behavior in OTEL runtime for reliable delivery. [#12455](https://github.com/elastic/elastic-agent/pull/12455)
  Elastic Agent running on the OTEL runtime now retries the same Elasticsearch response codes as standalone Beats, including 5xx errors. Previously, only 429 responses were retried, which could result in dropped events under certain failure conditions.


## 9.2.4


### Features and enhancements

- Update OTel Collector components to v0.141.0. [#11671](https://github.com/elastic/elastic-agent/pull/11671)
- Add service.instance.id to k8s attributes in helm charts. [#11844](https://github.com/elastic/elastic-agent/pull/11844)


### Fixes

- Fix signature verification using the upgrade command with the --source-uri flag for fleet-managed agents. [#11826](https://github.com/elastic/elastic-agent/pull/11826) [#11152](https://github.com/elastic/elastic-agent/issues/11152)
- Fix FLEET_TOKEN_POLICY_NAME environment variable for the container command to handle cases where there are more than 20 agent policies available. [#12073](https://github.com/elastic/elastic-agent/pull/12073) [#12069](https://github.com/elastic/elastic-agent/issues/12069)
- Handle string to []string conversion for elasticsearch config translation. [#11732](https://github.com/elastic/elastic-agent/pull/11732) [#11152](https://github.com/elastic/elastic-agent/issues/11152)


## 9.2.3


### Features and enhancements

- Enable cpu and disk hostmetrics scrapers for Darwin configurations. [#11423](https://github.com/elastic/elastic-agent/pull/11423)
- Add Windows Event Log Receiver to EDOT. [#11418](https://github.com/elastic/elastic-agent/pull/11418)
- Improve input not supported error message to reference installation flavors. [#11825](https://github.com/elastic/elastic-agent/pull/11825)


### Fixes

- Report crashing otel process cleanly with proper status reporting. [#11448](https://github.com/elastic/elastic-agent/pull/11448)
- Fix kube-stack null template evaluation for Helm v4. [#11481](https://github.com/elastic/elastic-agent/pull/11481)
- Add environment.yaml file to diagnostics. [#11484](https://github.com/elastic/elastic-agent/pull/11484) [#10966](https://github.com/elastic/elastic-agent/issues/10966)
- Merge multiple agent keys when loading config. [#11619](https://github.com/elastic/elastic-agent/pull/11619) [#3717](https://github.com/elastic/elastic-agent/issues/3717)
- Hide healthcheckv2 from status output. [#11718](https://github.com/elastic/elastic-agent/pull/11718)


## 9.2.2


### Fixes

- Redact secrets in slices. [#11271](https://github.com/elastic/elastic-agent/pull/11271)
  Redact secrets in conifg and component files found in the diagnostics archive that occur within slices.
- Fix filesource provider to work with kubernetes secret mounts. [#11050](https://github.com/elastic/elastic-agent/pull/11050)
- Ensure the monitoring input for the OTel collector can only run inside the collector. [#11204](https://github.com/elastic/elastic-agent/pull/11204)
- Fix a fatal startup error in Beats Receivers caused by truncation of long UTF-8 hostnames. [#11285](https://github.com/elastic/elastic-agent/pull/11285)
- Allow host to be a string for otel configuration translation. [#11394](https://github.com/elastic/elastic-agent/pull/11394) [#11352](https://github.com/elastic/elastic-agent/issues/11352)


## 9.2.1


### Features and enhancements

- Add sample config files for Windows ES and mOTLP ingestion. [#10728](https://github.com/elastic/elastic-agent/pull/10728) [#10540](https://github.com/elastic/elastic-agent/issues/10540)


### Fixes

- Reduce memory usage by executing Elastic Agent self-monitoring inputs as OpenTelemetry collector receivers by default. [#10594](https://github.com/elastic/elastic-agent/pull/10594)
  Self-monitoring inputs which were previously executed as Beat sub-processes are now executed as receivers in a single OpenTelemetry collector sub-process.
  For a Fleet managed Elastic Agent running the default System integration, steady state memory usage is reduced by 11.5% (79.1 MB) on Linux, 34.5% (185.77 MB) on Windows, and 23.0% (115.9 MB) on MacOS.
  This is the first phase of work reducing the Elastic Agents memory footprint, memory reductions will continue in future releases.
- Fix issue where switching to OTEL runtime would cause data to be re-ingested. [#10857](https://github.com/elastic/elastic-agent/pull/10857)
- Fix signal handling for the EDOT Collector. [#10908](https://github.com/elastic/elastic-agent/pull/10908)
- Reload agent binary source settings as configured in Fleet. [#10993](https://github.com/elastic/elastic-agent/pull/10993)


## 9.2.0build202510300150

<note>
  This is an independent Elastic Agent release. Independent Elastic Agent releases deliver critical fixes and updates for Elastic Agent and Elastic Defend independently of a full Elastic Stack release. Read more in [Elastic Agent release process](https://www.elastic.co/docs/reference/fleet/fleet-agent-release-process).
</note>


### Fixes

- Fix EDOT - mOTLP onboarding configuration. [#10822](https://github.com/elastic/elastic-agent/pull/10822)
- Fix quoting of boolean values in Helm charts. [#10681](https://github.com/elastic/elastic-agent/pull/10681)


## 9.2.0

_This release also includes: [Breaking changes](/docs/release-notes/elastic-agent/breaking-changes#elastic-agent-9.2.0-breaking-changes) and[Deprecations](/docs/release-notes/elastic-agent/deprecations#elastic-agent-9.2.0-deprecations)._

### Features and enhancements

- Add the tailsampling OpenTelemetry processor. [#9621](https://github.com/elastic/elastic-agent/pull/9621)
- Add_k8seventsreceiver. [#9826](https://github.com/elastic/elastic-agent/pull/9826) [#9791](https://github.com/elastic/elastic-agent/issues/9791)
  Adds k8seventsreceiver otel component.
- Edot-profilingmetrics. [#9887](https://github.com/elastic/elastic-agent/pull/9887)
- Edot-profilingreceiver. [#9888](https://github.com/elastic/elastic-agent/pull/9888)
  Add profilingreceiver to EDOT.
- Add agent_policy_id and policy_revision_idx to checkin requests. [#9931](https://github.com/elastic/elastic-agent/pull/9931) [#6446](https://github.com/elastic/elastic-agent/issues/6446)
  Add agent_policy_id and policy_revision_idx attributes to checkin requests.
  These attributes are used to inform fleet-server of the policy id and revision that the agent is currently running.
  Add a feature flag to disable sending acks for POLICY_CHANGE actions on a future release.
- (kube-stack) Add k8seventsreceiver in kube-stack configurations. [#10086](https://github.com/elastic/elastic-agent/pull/10086) [#9791](https://github.com/elastic/elastic-agent/issues/9791)
- Remove resource/k8s processor and use k8sattributes processor for mOTEL service attributes. [#10108](https://github.com/elastic/elastic-agent/pull/10108)
  This PR removes the `resource/k8s` processor in honour of the k8sattributes processor that
  provides native support for the Service attributes:
  [https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.127.0/processor/k8sattributesprocessor#configuring-recommended-resource-attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.127.0/processor/k8sattributesprocessor#configuring-recommended-resource-attributes)
  This change is aligned with the respective Semantic Conventions guidance:
  [https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-attributes/#service-attributes](https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-attributes/#service-attributes)
- Add Logstash exporter to be used with Beats OTel receivers. [#10137](https://github.com/elastic/elastic-agent/pull/10137)
- Add Windows Event Log receiver to EDOT Collector. [#10196](https://github.com/elastic/elastic-agent/pull/10196)
- Add logs_metrics_traces.yml sample in EDOT for Windows. [#10514](https://github.com/elastic/elastic-agent/pull/10514)
- Add Headers Setter extension to EDOT Collector. [#9903](https://github.com/elastic/elastic-agent/pull/9903) [#9889](https://github.com/elastic/elastic-agent/issues/9889)
- Include OTel Collector internal telemetry in Agent monitoring. [#9928](https://github.com/elastic/elastic-agent/pull/9928)
- Add debug exporter to AutoOps OTel config sample. [#10268](https://github.com/elastic/elastic-agent/pull/10268)
- Update OTel Collector components to v0.137.0. [#10391](https://github.com/elastic/elastic-agent/pull/10391)


### Fixes

- Add special case handling for profiling in EDOT. [#10143](https://github.com/elastic/elastic-agent/pull/10143)
- Inspect: Handle components with slashes in their name. [#10442](https://github.com/elastic/elastic-agent/pull/10442)
- Improve OTel batching and queueing for AutoOps data shipping. [#10492](https://github.com/elastic/elastic-agent/pull/10492)


## 9.1.10


### Features and enhancements

- Add debug exporter to AutoOps OTel config sample. [#10268](https://github.com/elastic/elastic-agent/pull/10268)
- Add service.instance.id to k8s attributes in helm charts. [#11844](https://github.com/elastic/elastic-agent/pull/11844)


### Fixes

- Fix signature verification using the upgrade command with the --source-uri flag for fleet-managed agents. [#11826](https://github.com/elastic/elastic-agent/pull/11826) [#11152](https://github.com/elastic/elastic-agent/issues/11152)
- Fix FLEET_TOKEN_POLICY_NAME environment variable for the container command to handle cases where there are more than 20 agent policies available. [#12073](https://github.com/elastic/elastic-agent/pull/12073) [#12069](https://github.com/elastic/elastic-agent/issues/12069)
- Handle string to []string conversion for elasticsearch config translation. [#11732](https://github.com/elastic/elastic-agent/pull/11732) [#11152](https://github.com/elastic/elastic-agent/issues/11152)


## 9.1.9


### Features and enhancements

- Enable cpu and disk hostmetrics scrapers for Darwin configurations. [#11423](https://github.com/elastic/elastic-agent/pull/11423)
- Improve input not supported error message to reference installation flavors. [#11825](https://github.com/elastic/elastic-agent/pull/11825) [#11746](https://github.com/elastic/elastic-agent/issues/11746)


### Fixes

- Fix kube-stack null template evaluation for Helm v4. [#11481](https://github.com/elastic/elastic-agent/pull/11481)
- Allow host to be a string for otel configuration translation. [#11394](https://github.com/elastic/elastic-agent/pull/11394) [#11352](https://github.com/elastic/elastic-agent/issues/11352)
- Add environment.yaml file to diagnostics. [#11484](https://github.com/elastic/elastic-agent/pull/11484) [#10966](https://github.com/elastic/elastic-agent/issues/10966)
- Merge multiple agent keys when loading config. [#11619](https://github.com/elastic/elastic-agent/pull/11619) [#3717](https://github.com/elastic/elastic-agent/issues/3717)


## 9.1.8


### Fixes

- Redact secrets in slices. [#11271](https://github.com/elastic/elastic-agent/pull/11271)
- Fix filesource provider to work with kubernetes secret mounts. [#11050](https://github.com/elastic/elastic-agent/pull/11050)
- Fix a fatal startup error in Beats Receivers caused by truncation of long UTF-8 hostnames. [#11285](https://github.com/elastic/elastic-agent/pull/11285)


## 9.1.7


### Features and enhancements

- Update OTel Collector components to v0.135.0. [#9858](https://github.com/elastic/elastic-agent/pull/9858)


### Fixes

- Fix quoting of boolean values in Helm charts. [#10681](https://github.com/elastic/elastic-agent/pull/10681)
- Fix signal handling for the EDOT Collector. [#10908](https://github.com/elastic/elastic-agent/pull/10908)
- Reload agent binary source settings as configured in Fleet. [#10993](https://github.com/elastic/elastic-agent/pull/10993)


## 9.1.6


### Features and enhancements

- Add logs_metrics_traces.yml sample in EDOT for Windows. [#10514](https://github.com/elastic/elastic-agent/pull/10514)
- Include OTel Collector internal telemetry in Agent monitoring. [#9928](https://github.com/elastic/elastic-agent/pull/9928)


### Fixes

- Improve logging to catch early errors on startup. [#10158](https://github.com/elastic/elastic-agent/pull/10158) [#9099](https://github.com/elastic/elastic-agent/issues/9099)
- Fix an incorrectly formatted log message when a provider fails. [#10217](https://github.com/elastic/elastic-agent/pull/10217)
- Fix troubleshooting docs URL for 9.x to prevent invalid version links. [#10218](https://github.com/elastic/elastic-agent/pull/10218)
- Inspect: Handle components with slashes in their name. [#10442](https://github.com/elastic/elastic-agent/pull/10442)
- Improve OTel batching and queueing for AutoOps data shipping. [#10492](https://github.com/elastic/elastic-agent/pull/10492)


## 9.1.5


### Features and enhancements

- Agent cleans up downloads directory and the new versioned home if upgrade fails. [#9386](https://github.com/elastic/elastic-agent/pull/9386) [#5235](https://github.com/elastic/elastic-agent/issues/5235)
- When there is a disk space error during an upgrade, agent responds with clean insufficient disk space error message. [#9392](https://github.com/elastic/elastic-agent/pull/9392) [#5235](https://github.com/elastic/elastic-agent/issues/5235)
- Add Headers Setter extension to EDOT Collector. [#9903](https://github.com/elastic/elastic-agent/pull/9903) [#9889](https://github.com/elastic/elastic-agent/issues/9889)
- Update OTel components to v0.132.0. [#10033](https://github.com/elastic/elastic-agent/pull/10033)


### Fixes

- Include aggregated agent status in HTTP liveness checks. [#9673](https://github.com/elastic/elastic-agent/pull/9673) [#9576](https://github.com/elastic/elastic-agent/issues/9576)
- Reduce-default-telemetry-frequency. [#9987](https://github.com/elastic/elastic-agent/pull/9987)
  Reduce the default telemetry frequency to 60 seconds. This change aims to lower infrastructure costs and reduce label churn in time-series storage. High-cardinality labels sampled too frequently inflate storage and index size, and increase query latency with limited added value. Environments that require higher resolution can change the `collection_interval` for `hostmetrics`, `kubeletstats` and `k8s_cluster` receivers to a lower value.
- Fix stuck upgrade state by clearing coordinator overridden state after failed upgrade. [#9992](https://github.com/elastic/elastic-agent/pull/9992)
- Include components units status in HTTP liveness checks. [#10060](https://github.com/elastic/elastic-agent/pull/10060) [#8047](https://github.com/elastic/elastic-agent/issues/8047)
- Add info about hostPID for Universal Profiling. [#10173](https://github.com/elastic/elastic-agent/pull/10173)


## 9.1.4


### Features and enhancements

- Add the dockerstats OpenTelemetry receiver. [#9364](https://github.com/elastic/elastic-agent/pull/9364)
- Bump kube-stack Helm Chart to 0.9.1 and enable the cluster collector. [#9535](https://github.com/elastic/elastic-agent/pull/9535)
- Enhanced loggers for easier debugging of upgrade related issues. [#9536](https://github.com/elastic/elastic-agent/issues/9536)


### Fixes

- Redact secrets from pre-config, computed-config, components-expected, and components-actual files in diagnostics archive. [#9560](https://github.com/elastic/elastic-agent/pull/9560)
- Retry service start command upon failure with 30-second delay. [#9313](https://github.com/elastic/elastic-agent/pull/9313)
- Fix reporting of scheduled upgrade details across restarts and cancels. [#9562](https://github.com/elastic/elastic-agent/pull/9562) [#8778](https://github.com/elastic/elastic-agent/issues/8778)
- Enable root user to re-enroll unprivileged agent for mac and linux. [#8544](https://github.com/elastic/elastic-agent/issues/8544)
- Fix missing liveness healthcheck during container enrollment. [#9612](https://github.com/elastic/elastic-agent/pull/9612) [#9611](https://github.com/elastic/elastic-agent/issues/9611)
- Enable admin user to re-enroll unprivileged agent for windows. [#9623](https://github.com/elastic/elastic-agent/pull/9623) [#8544](https://github.com/elastic/elastic-agent/issues/8544)
- Treat exit code 284 from Endpoint binary as non-fatal. [#9687](https://github.com/elastic/elastic-agent/pull/9687)
- Ensure failed upgrade actions are removed from queue and details are set. [#9634](https://github.com/elastic/elastic-agent/pull/9634) [#9629](https://github.com/elastic/elastic-agent/issues/9629)


## 9.1.3


### Features and enhancements

- Adjust the timeout for Elastic Defend check command. [#9329](https://github.com/elastic/elastic-agent/pull/9329) [#9521](https://github.com/elastic/elastic-agent/pull/9521) [#9522](https://github.com/elastic/elastic-agent/pull/9522) [#9545](https://github.com/elastic/elastic-agent/pull/9545) [#9213](https://github.com/elastic/elastic-agent/pull/9213)
- Update OTel components to v0.130.0. [#9329](https://github.com/elastic/elastic-agent/pull/9329) [#9521](https://github.com/elastic/elastic-agent/pull/9521) [#9522](https://github.com/elastic/elastic-agent/pull/9522) [#9545](https://github.com/elastic/elastic-agent/pull/9545) [#9362](https://github.com/elastic/elastic-agent/pull/9362)


### Fixes

- Upgrade to Go 1.24.6. [#9287](https://github.com/elastic/elastic-agent/pull/9287)
- On Windows, retry saving the Agent information file to disk. [#9224](https://github.com/elastic/elastic-agent/pull/9224) [#5862](https://github.com/elastic/elastic-agent/issues/5862)
  Saving the Agent information file involves renaming/moving a file to its final destination. However, on Windows, it is sometimes not possible to rename/move a file to its destination file because the destination file is locked by another process (e.g. antivirus software). For such situations, we now retry the save operation on Windows.
- Correct hints annotations parsing to resolve only `${kubernetes.*}` placeholders instead of resolving all `${...}` patterns. [#9307](https://github.com/elastic/elastic-agent/pull/9307)
- Treat exit code 28 from Endpoint binary as non-fatal. [#9320](https://github.com/elastic/elastic-agent/pull/9320)
- Fixed jitter backoff strategy reset. [#9342](https://github.com/elastic/elastic-agent/pull/9342) [#8864](https://github.com/elastic/elastic-agent/issues/8864)
- Fix Docker container failing to start with no matching vars: ${env.ELASTICSEARCH_API_KEY:} and similar errors by restoring support for `:` to set default values. [#9451](https://github.com/elastic/elastic-agent/pull/9451) [#9328](https://github.com/elastic/elastic-agent/issues/9328)
- Fix deb upgrade by stopping elastic-agent service before stopping endpoint. [#9462](https://github.com/elastic/elastic-agent/pull/9462)


## 9.1.2

_No new features, enhancements, or fixes._

## 9.1.1


### Features and enhancements

- Add k8s leader elector Otel extension. [#9261](https://github.com/elastic/elastic-agent/pull/9261) [#9262](https://github.com/elastic/elastic-agent/pull/9262) [#9065](https://github.com/elastic/elastic-agent/pull/9065)


### Fixes

- Dont overwrite elasticsearch output headers from enrollment --headers flag. [#9199](https://github.com/elastic/elastic-agent/pull/9199) [#9197](https://github.com/elastic/elastic-agent/issues/9197)


## 9.1.0

_This release also includes: [Deprecations](/docs/release-notes/elastic-agent/deprecations#elastic-agent-9.1.0-deprecations)._

### Features and enhancements

- Adds a new configuration setting, `agent.upgrade.rollback.window`. [#8065](https://github.com/elastic/elastic-agent/pull/8065) [#6881](https://github.com/elastic/elastic-agent/issues/6881)
  The value of the `agent.upgrade.rollback.window` setting determines the period after upgrading
  Elastic Agent when a rollback to the previous version can be triggered. This is an optional
  setting, with a default value of `168h` (7 days). The value can be any string that is parseable
  by [https://pkg.go.dev/time#ParseDuration](https://pkg.go.dev/time#ParseDuration).
- Remove resource/k8s processor and use k8sattributes processor for service attributes. [#8599](https://github.com/elastic/elastic-agent/pull/8599)
  This PR removes the `resource/k8s` processor in honour of the k8sattributes processor that
  provides native support for the Service attributes:
  [https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.127.0/processor/k8sattributesprocessor#configuring-recommended-resource-attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.127.0/processor/k8sattributesprocessor#configuring-recommended-resource-attributes)
  This change is aligned with the respective Semantic Conventions guidance:
  [https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-attributes/#service-attributes](https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-attributes/#service-attributes)
- Add elastic.agent.fips to local_metadata.  [#7112](https://github.com/elastic/elastic-agent/pull/7112)
  Add elastic.agent.fips (bool) attribute to local_metadata sent with enroll and checkin requests.
  The value of this attribute indicates if the agent is a FIPS-capable distribution.
- Validate pbkdf2 settings when in FIPS mode. [#7187](https://github.com/elastic/elastic-agent/pull/7187)
- FIPS-capable agent file vault. [#7360](https://github.com/elastic/elastic-agent/pull/7360)
  Change elastic file vault implementation to allow variable length salt sizes
  only in FIPS enabled agents.  Increase default salt size to 16 for FIPS
  compliance. Non-FIPS agents are unchanged.
- With this change FIPS-capable agents will only be able to upgrade to other FIPS-capable agents. This change also restricts non-fips to fips upgrades as well. [#7312](https://github.com/elastic/elastic-agent/pull/7312) [#4811](https://github.com/elastic/ingest-dev/issues/4811)
- Updated the error messages returned for fips upgrades. [#7453](https://github.com/elastic/elastic-agent/pull/7453)
- Retry enrollment requests on any error. [#8056](https://github.com/elastic/elastic-agent/pull/8056)
  If any error is encountered during an attempted enrollment, the elastic-agent
  will backoff and retry. Add a new --enroll-timeout flag and
  FLEET_ENROLL_TIMEOUT env var to set how long it tries for, default 10m. A
  negative value disables the timeout.
- Remove deprecated otel elasticsearch exporter config `*_dynamic_index` from code and samples. [#8592](https://github.com/elastic/elastic-agent/pull/8592)
- Include the forwardconnector as an EDOT collector commponent. [#8753](https://github.com/elastic/elastic-agent/pull/8753)
  [https://github.com/open-telemetry/opentelemetry-collector/tree/main/connector/forwardconnector](https://github.com/open-telemetry/opentelemetry-collector/tree/main/connector/forwardconnector)
- Update OTel components to v0.129.0.
- Update APM Config extension to v0.4.0.
- Update Elastic Trace processor to v0.7.0.
- Update Elastic APM connector to v0.4.0.
- Update API Key Auth extension to v0.2.0.
- Update Elastic Infra Metrics processor to v0.16.0.


### Fixes

- Upgrade to Go 1.24.3. [#8109](https://github.com/elastic/elastic-agent/pull/8109)
- Correctly handle sending signal to child process. [#7738](https://github.com/elastic/elastic-agent/pull/7738) [#6875](https://github.com/elastic/elastic-agent/issues/6875)
- Preserve agent run state on DEB and RPM upgrades. [#7999](https://github.com/elastic/elastic-agent/pull/7999) [#3832](https://github.com/elastic/elastic-agent/issues/3832)
- Use --header from enrollment when communicating with Fleet Server. [#8071](https://github.com/elastic/elastic-agent/pull/8071) [#6823](https://github.com/elastic/elastic-agent/issues/6823)
  The --header option for the enrollment command now adds the headers to the communication with Fleet Server. This
  allows a proxy that requires specific headers present for traffic to flow to be placed in front of a Fleet Server
  to be used and still allowing the Elastic Agent to enroll.
- Address a race condition that can occur in Agent diagnostics if log rotation runs while logs are being zipped.
- Use paths.TempDir for diagnostics actions. [#8472](https://github.com/elastic/elastic-agent/pull/8472)
- Use Debian 11 to build linux/arm to match linux/amd64. Upgrades linux/arm64s statically linked glibc from 2.28 to 2.31. [#8497](https://github.com/elastic/elastic-agent/pull/8497)
- Relax file ownership check to allow admin re-enrollment on Windows. [#8503](https://github.com/elastic/elastic-agent/pull/8503) [#7794](https://github.com/elastic/elastic-agent/issues/7794)
  On Windows, the agent previously enforced a strict file ownership (SID) check during re-enrollment, which prevented legitimate admin users from re-enrolling the agent if the owner did not match. This PR changes the Windows-specific logic to a no-op, allowing any admin to re-enroll the agent. This restores usability for admin users, but reintroduces the risk that privileged re-enrollment can break unprivileged installs. The Unix-specific ownership check remains unchanged.
- Remove incorrect logging that unprivileged installations are in beta. [#8715](https://github.com/elastic/elastic-agent/pull/8715) [#8689](https://github.com/elastic/elastic-agent/issues/8689)
  Unprivileged installations went GA in 8.15.0: [https://www.elastic.co/docs/reference/fleet/elastic-agent-unprivileged](https://www.elastic.co/docs/reference/fleet/elastic-agent-unprivileged)
- Ensure standalone Elastic Agent uses log level from configuration instead of persisted state. [#8784](https://github.com/elastic/elastic-agent/pull/8784) [#8137](https://github.com/elastic/elastic-agent/issues/8137)
- Resolve deadlocks in runtime checkin communication. [#8881](https://github.com/elastic/elastic-agent/pull/8881) [#7944](https://github.com/elastic/elastic-agent/issues/7944)
- Removed init.d support from RPM packages. [#8896](https://github.com/elastic/elastic-agent/pull/8896) [#8840](https://github.com/elastic/elastic-agent/issues/8840)


## 9.0.8


### Features and enhancements

- Agent cleans up downloads directory and the new versioned home if upgrade fails. [#9386](https://github.com/elastic/elastic-agent/pull/9386) [#5235](https://github.com/elastic/elastic-agent/issues/5235)
- When there is a disk space error during an upgrade, agent responds with clean insufficient disk space error message. [#9392](https://github.com/elastic/elastic-agent/pull/9392) [#5235](https://github.com/elastic/elastic-agent/issues/5235)


### Fixes

- Include aggregated agent status in HTTP liveness checks. [#9673](https://github.com/elastic/elastic-agent/pull/9673) [#9576](https://github.com/elastic/elastic-agent/issues/9576)
- Reduce-default-telemetry-frequency. [#9987](https://github.com/elastic/elastic-agent/pull/9987)
  Reduce the default telemetry frequency to 60 seconds. This change aims to lower infrastructure costs and reduce label churn in time-series storage. High-cardinality labels sampled too frequently inflate storage and index size, and increase query latency with limited added value. Environments that require higher resolution can change the `collection_interval` for `hostmetrics`, `kubeletstats` and `k8s_cluster` receivers to a lower value.
- Fix stuck upgrade state by clearing coordinator overridden state after failed upgrade. [#9992](https://github.com/elastic/elastic-agent/pull/9992)
- Include components units status in HTTP liveness checks. [#10060](https://github.com/elastic/elastic-agent/pull/10060) [#8047](https://github.com/elastic/elastic-agent/issues/8047)
- Add info about hostPID for Universal Profiling. [#10173](https://github.com/elastic/elastic-agent/pull/10173)


## 9.0.7


### Features and enhancements

- Bump kube-stack Helm Chart to 0.9.1 and enable the cluster collector. [#9535](https://github.com/elastic/elastic-agent/pull/9535)
- Enhanced loggers for easier debugging of upgrade related issues. [#9536](https://github.com/elastic/elastic-agent/issues/9536)


### Fixes

- Redact secrets from pre-config, computed-config, components-expected, and components-actual files in diagnostics archive. [#9560](https://github.com/elastic/elastic-agent/pull/9560)
- Retry service start command upon failure with 30-second delay. [#9313](https://github.com/elastic/elastic-agent/pull/9313)
- Fix reporting of scheduled upgrade details across restarts and cancels. [#9562](https://github.com/elastic/elastic-agent/pull/9562) [#8778](https://github.com/elastic/elastic-agent/issues/8778)
- Enable root user to re-enroll unprivileged agent for mac and linux. [#9603](https://github.com/elastic/elastic-agent/pull/9603) [#8544](https://github.com/elastic/elastic-agent/issues/8544)
- Fix missing liveness healthcheck during container enrollment. [#9612](https://github.com/elastic/elastic-agent/pull/9612) [#9611](https://github.com/elastic/elastic-agent/issues/9611)
- Enable admin user to re-enroll unprivileged agent for windows. [#9623](https://github.com/elastic/elastic-agent/pull/9623) [#8544](https://github.com/elastic/elastic-agent/issues/8544)
- Treat exit code 284 from Endpoint binary as non-fatal. [#9687](https://github.com/elastic/elastic-agent/pull/9687)
- Ensure failed upgrade actions are removed from queue and details are set. [#9634](https://github.com/elastic/elastic-agent/pull/9634) [#9629](https://github.com/elastic/elastic-agent/issues/9629)


## 9.0.6


### Features and enhancements

- Adjust the timeout for Elastic Defend check command. [#9523](https://github.com/elastic/elastic-agent/pull/9523) [#9524](https://github.com/elastic/elastic-agent/pull/9524) [#9542](https://github.com/elastic/elastic-agent/pull/9542) [#9213](https://github.com/elastic/elastic-agent/pull/9213)


### Fixes

- Upgrade to Go 1.24.6. [#9287](https://github.com/elastic/elastic-agent/pull/9287)
- On Windows, retry saving the Agent information file to disk. [#9224](https://github.com/elastic/elastic-agent/pull/9224) [#5862](https://github.com/elastic/elastic-agent/issues/5862)
  Saving the Agent information file involves renaming/moving a file to its final destination. However, on Windows, it is sometimes not possible to rename/move a file to its destination file because the destination file is locked by another process (e.g. antivirus software). For such situations, we now retry the save operation on Windows.
- Correct hints annotations parsing to resolve only `${kubernetes.*}` placeholders instead of resolving all `${...}` patterns. [#9307](https://github.com/elastic/elastic-agent/pull/9307)
- Treat exit code 28 from Endpoint binary as non-fatal. [#9320](https://github.com/elastic/elastic-agent/pull/9320)
- Fixed jitter backoff strategy reset. [#9342](https://github.com/elastic/elastic-agent/pull/9342) [#8864](https://github.com/elastic/elastic-agent/issues/8864)
- Fix Docker container failing to start with no matching vars: ${env.ELASTICSEARCH_API_KEY:} and similar errors by restoring support for `:` to set default values. [#9451](https://github.com/elastic/elastic-agent/pull/9451) [#9328](https://github.com/elastic/elastic-agent/issues/9328)
- Fix deb upgrade by stopping elastic-agent service before upgrading. [#9462](https://github.com/elastic/elastic-agent/pull/9462)


## 9.0.5

_No new features, enhancements, or fixes._

## 9.0.4


### Features and enhancements

- Add file logs only managed OTLP input kube-stack configuration. [#8785](https://github.com/elastic/elastic-agent/pull/8785)


### Fixes

- Remove incorrect logging that unprivileged installations are in beta. [#8715](https://github.com/elastic/elastic-agent/pull/8715) [#8689](https://github.com/elastic/elastic-agent/issues/8689)
  Unprivileged installations went GA in 8.15.0: [https://www.elastic.co/docs/reference/fleet/elastic-agent-unprivileged](https://www.elastic.co/docs/reference/fleet/elastic-agent-unprivileged)
- Ensure standalone Elastic Agent uses log level from configuration instead of persisted state. [#8784](https://github.com/elastic/elastic-agent/pull/8784) [#8137](https://github.com/elastic/elastic-agent/issues/8137)
- Resolve deadlocks in runtime checkin communication. [#8881](https://github.com/elastic/elastic-agent/pull/8881) [#7944](https://github.com/elastic/elastic-agent/issues/7944)
- Removed init.d support from RPM packages. [#8896](https://github.com/elastic/elastic-agent/pull/8896) [#8840](https://github.com/elastic/elastic-agent/issues/8840)


## 9.0.3


### Features and enhancements

- Add cumulativetodeltaprocessor to EDOT collector. [#8352](https://github.com/elastic/elastic-agent/pull/8352) [#8573](https://github.com/elastic/elastic-agent/pull/8573) [#8575](https://github.com/elastic/elastic-agent/pull/8575) [#8616](https://github.com/elastic/elastic-agent/pull/8616) [#8372](https://github.com/elastic/elastic-agent/pull/8372)


### Fixes

- Address a race condition that can occur in Agent diagnostics if log rotation runs while logs are being zipped. [#8215](https://github.com/elastic/elastic-agent/pull/8215)
- Use paths.TempDir for diagnostics actions. [#8472](https://github.com/elastic/elastic-agent/pull/8472)
- Relax file ownership check to allow admin re-enrollment on Windows. [#8503](https://github.com/elastic/elastic-agent/pull/8503) [#7794](https://github.com/elastic/elastic-agent/issues/7794)
  On Windows, the agent previously enforced a strict file ownership (SID) check during re-enrollment, which prevented legitimate admin users from re-enrolling the agent if the owner did not match. This PR changes the Windows-specific logic to a no-op, allowing any admin to re-enroll the agent. This restores usability for admin users, but reintroduces the risk that privileged re-enrollment can break unprivileged installs. The Unix-specific ownership check remains unchanged.


## 9.0.2


### Fixes

- Upgrade Go version to 1.24.3. [#8109](https://github.com/elastic/elastic-agent/pull/8109)
- Preserve agent run state on DEB and RPM upgrades. [#7999](https://github.com/elastic/elastic-agent/pull/7999) [#3832](https://github.com/elastic/elastic-agent/issues/3832)
  Improves the upgrade process for Elastic Agent installed using DEB or RPM packages by copying the run directory from the previous installation into the new versions folder


## 9.0.1

_This release also includes: [Breaking changes](/docs/release-notes/elastic-agent/breaking-changes#elastic-agent-9.0.1-breaking-changes)._

### Features and enhancements

- Add nopexporter to EDOT Collector. [#7788](https://github.com/elastic/elastic-agent/pull/7788)
- Set collectors fullnameOverride for edot kube-stack values. [#7754](https://github.com/elastic/elastic-agent/pull/7754) [#7381](https://github.com/elastic/elastic-agent/issues/7381)
- Update OTel components to v0.121.0. [#7686](https://github.com/elastic/elastic-agent/pull/7686)


### Fixes

- Fix Managed OTLP Helm config to use current image repo. [#7882](https://github.com/elastic/elastic-agent/pull/7882)


## 9.0.0

_This release also includes: [Breaking changes](/docs/release-notes/elastic-agent/breaking-changes#elastic-agent-9.0.0-breaking-changes)._

### Features and enhancements

- Adds the Azure Asset Inventory definition to Cloudbeat for Elastic Agent [#5323](https://github.com/elastic/elastic-agent/pull/5323)
- Adds Kubernetes deployment of the Elastic Distribution of OTel Collector named "gateway" to the Helm kube-stack deployment for Elastic Agent [#6444](https://github.com/elastic/elastic-agent/pull/6444)
- Adds the filesource provider to composable inputs. The provider watches for changes of the files and updates the values of the variables when the content of the file changes for Elastic Agent [#6587](https://github.com/elastic/elastic-agent/pull/6587) and [#6362](https://github.com/elastic/elastic-agent/issues/6362)
- Adds the jmxreceiver to the Elastic Distribution of OTel Collector for Elastic Agent [#6601](https://github.com/elastic/elastic-agent/pull/6601)
- Adds support for context variables in outputs as well as a default provider prefix for Elastic Agent [#6602](https://github.com/elastic/elastic-agent/pull/6602) and [#6376](https://github.com/elastic/elastic-agent/issues/6376)
- Adds the Nginx receiver and Redis receiver OTel components for Elastic Agent [#6627](https://github.com/elastic/elastic-agent/pull/6627)
- Adds --id (ELASTIC_AGENT_ID environment variable for container) and --replace-token (FLEET_REPLACE_TOKEN environment variable for container) enrollment options for Elastic Agent [#6498](https://github.com/elastic/elastic-agent/pull/6498)
- Updates Go version to 1.22.10 in Elastic Agent [#6236](https://github.com/elastic/elastic-agent/pull/6236)
- Adds the Filebeat receiver into Elastic Agent [#5833](https://github.com/elastic/elastic-agent/pull/5833)
- Updates OTel components to v0.119.0 in Elastic Agent [#6713](https://github.com/elastic/elastic-agent/pull/6713)


### Fixes

- Fixes logical race conditions in the kubernetes_secrets provider in Elastic Agent [#6623](https://github.com/elastic/elastic-agent/pull/6623)
- Resolves the proxy to inject into agent component configurations using the Go http package in Elastic Agent [#6675](https://github.com/elastic/elastic-agent/pull/6675) and [#6209](https://github.com/elastic/elastic-agent/issues/6209)