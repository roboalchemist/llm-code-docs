# Source: https://www.elastic.co/docs/release-notes/security

﻿---
title: Elastic Security release notes
description: Review the changes, fixes, and more in each version of Elastic Security. To check for security updates, go to Security announcements for the Elastic stack...
url: https://www.elastic.co/docs/release-notes/security
products:
  - Elastic Security
---

# Elastic Security release notes
Review the changes, fixes, and more in each version of Elastic Security.
To check for security updates, go to [Security announcements for the Elastic stack](https://discuss.elastic.co/c/announcements/security-announcements/31).
<tip>
  Elastic Security runs on Kibana, so we recommend also reviewing the [Kibana release notes](https://www.elastic.co/docs/release-notes/kibana) for relevant updates.
</tip>


## 9.3.1


### Features and enhancements

- Allows user and host details flyouts to open while observed data is loading [#252657](https://github.com/elastic/kibana/pull/252657).
- Adds a new **Overview** tab to the rule details page [#251662](https://github.com/elastic/kibana/pull/251662).
- Adds a `region` field to the Amazon Bedrock connector [#252960](https://github.com/elastic/kibana/pull/252960), [#252956](https://github.com/elastic/kibana/pull/252956).
- Improves Automatic Migration performance by reducing the number of Elasticsearch calls when updating field mappings [#252431](https://github.com/elastic/kibana/pull/252431).
- Updates the `fast-xml-parser` package dependency to version 5.3.4 [#251644](https://github.com/elastic/kibana/pull/251644).


### Fixes

- Improves the performance of bulk rule deletion [#253116](https://github.com/elastic/kibana/pull/253116).
- Fixes an Automatic Migration issue where failed rules appeared in non-failed status filters [#252263](https://github.com/elastic/kibana/pull/252263).
- Fixes accessibility issues in the Security AI Assistant confirm delete modal [#251962](https://github.com/elastic/kibana/pull/251962).
- Replaces a deprecated icon in the UI [#251930](https://github.com/elastic/kibana/pull/251930).
- Adds optional field indicators to the OpenAI connector configuration [#251857](https://github.com/elastic/kibana/pull/251857).
- Fixes an accessibility issue with a missing label in the Security AI Assistant flyout [#251656](https://github.com/elastic/kibana/pull/251656).
- Fixes the `spaceId` handling in Agent Builder security tools [#251513](https://github.com/elastic/kibana/pull/251513).
- Fixes an issue where detection rules APIs didn't properly validate endpoint response actions [#251352](https://github.com/elastic/kibana/pull/251352).
- Fixes an issue in the Security AI Assistant where the **Add connector** button was incorrectly grayed out for users with permission to create connectors [#250921](https://github.com/elastic/kibana/pull/250921).
- Fixes an issue where the privileged user monitoring table didn't refresh alert data when the time range changed [#250618](https://github.com/elastic/kibana/pull/250618).
- Fixes a DNS parsing bug in Linux versions of Elastic Defend that could result in crashes.
- Fixes a bug in version 9.3.0 of Elastic Defend that resulted in the Windows Security Center status page showing an error.


## 9.3.0


### Features and enhancements

- Adds a new **Workflows** action to detection rules, allowing you to trigger workflows when a detection rule generates an alert. Refer to [Workflows](https://www.elastic.co/docs/explore-analyze/workflows) and [Alert triggers](https://www.elastic.co/docs/explore-analyze/workflows/triggers/alert-triggers) for more details.
- Adds a new **Rules, Alerts, and Exceptions** feature privilege that controls access to detection rules, alerts, and rule exceptions [#239634](https://github.com/elastic/kibana/pull/239634).
- Updates MITRE ATT&CK mappings to `v18.1` [#246770](https://github.com/elastic/kibana/pull/246770).
- Adds the gap auto-fill scheduler UI and API for detection rules [#244719](https://github.com/elastic/kibana/pull/244719).
- Adds a **Gap fill status** column and filter to the Rules table on the **Rule Monitoring** tab [#242595](https://github.com/elastic/kibana/pull/242595).
- Enables the **Value report** page in Elastic Stack [#243511](https://github.com/elastic/kibana/pull/243511).
- Makes the Attack Discovery and Attack Discovery Schedules APIs generally available [#246788](https://github.com/elastic/kibana/pull/246788).
- Improves Attack Discovery prompts [#241346](https://github.com/elastic/kibana/pull/241346).
- Allows you to migrate QRadar rules to Elastic using Automatic Migration [#244924](https://github.com/elastic/kibana/pull/244924).
- Allows you to opt in to the new Agent Builder chat experience [#246089](https://github.com/elastic/kibana/pull/246089), [#243574](https://github.com/elastic/kibana/pull/243574), [#245259](https://github.com/elastic/kibana/pull/245259), [#242598](https://github.com/elastic/kibana/pull/242598), [#245205](https://github.com/elastic/kibana/pull/245205), [#246193](https://github.com/elastic/kibana/pull/246193), [#246403](https://github.com/elastic/kibana/pull/246403).
- Improves the alert details flyout by saving the selected threat intelligence time to local storage [#243571](https://github.com/elastic/kibana/pull/243571).
- Improves the alert details flyout by saving the selected prevalence time to local storage [#243543](https://github.com/elastic/kibana/pull/243543).
- Displays Session View in full height [#245888](https://github.com/elastic/kibana/pull/245888).
- Displays the visual event analyzer in full height [#245857](https://github.com/elastic/kibana/pull/245857).
- Persists the visual event analyzer's data view selection in local storage [#245002](https://github.com/elastic/kibana/pull/245002).
- Updates graph visualization to use Elastic Common Schema (ECS) entity fields for actor and target identification [#243711](https://github.com/elastic/kibana/pull/243711).
- Improves the graph investigation feature by introducing new popover components for displaying additional node details [#236906](https://github.com/elastic/kibana/pull/236906).
- Prepares the monitoring entity source CRUD APIs for general availability of privileged user monitoring [#246978](https://github.com/elastic/kibana/pull/246978).
- Introduces the **Entity summary** section in the entity details flyout [#245532](https://github.com/elastic/kibana/pull/245532).
- Adds Cloud Connector usage statistics collection for the CSPM and Asset Discovery integrations [#236992](https://github.com/elastic/kibana/pull/236992),[#240272](https://github.com/elastic/kibana/pull/240272).
- Improves the reliability of Cloud Security Posture (CSP) data by automatically upgrading outdated Misconfiguration and Vulnerabilities data views to the correct versions [#238547](https://github.com/elastic/kibana/pull/238547).
- Fixes Cloud Security Posture regressions to ensure AWS, GCP, and Azure cloud providers are all supported [#242592](https://github.com/elastic/kibana/pull/242592).
- Upgrades the Osquery schema to v5.19.0 and the ECS schema to v9.2.0 [#246005](https://github.com/elastic/kibana/pull/246005).
- Adds a file download relative URI to response actions that provide file output [#237713](https://github.com/elastic/kibana/pull/237713).
- Adds a free-text input option to the `runscript` response action for providing input to the selected script [#239436](https://github.com/elastic/kibana/pull/239436).
- Displays `runscript` response action output for Microsoft Defender for Endpoint for files up to 4.5 KB [#242441](https://github.com/elastic/kibana/pull/242441).
- Adds a server configuration setting that allows you to turn off automatic installation of the Endpoint Security (Elastic Defend) rule when creating an Elastic Defend integration policy [#246418](https://github.com/elastic/kibana/pull/246418).
- Adds UI and API support for process descendants in trusted applications [#236318](https://github.com/elastic/kibana/pull/236318).
- Adds an `actions` command to Elastic Defend to list all queued response actions or cancel an action by ID.
- Adds the `thumbprint_sha256` field to `code_signature` for process and library events in Elastic Defend on Windows.
- Adds the `desktop_name` field to Elastic Defend on Windows process events to assist with the detection of malicious hidden desktop activity.
- Improves Elastic Defend by integrating two new Event Tracing for Windows (ETW) providers (`Microsoft-Windows-WebIO` and `Microsoft-Windows-WinINet`) to detect malicious HTTP activity.
- Moves the Elastic Defend response actions internal state location. If an unsuccessful Elastic Defend upgrade is rolled back to the previous version, existing pending actions are aborted early.
- Adds service-less (no systemd) install mode for Elastic Defend on Linux. Enable by setting the `ELASTIC_ENDPOINT_NO_SYSTEM_SERVICES=1` environment variable during install.
- Adds the `memory-dump` response action to Elastic Defend on Windows.
- Hardens Elastic Defend on Windows against Bind Filter rebinding attacks.
- Adds a new event capture mode, Quark, to Elastic Defend on Linux.
- Adds DNS events for Elastic Defend on Linux (only supported by eBPF-based event collection).
- Removes the 100 MB file size limit for the Elastic Defend `get-file` response action.
- Adds `entropy` and `header_bytes` fields to Linux file events in Elastic Defend.
- Adds a trusted ancestor feature to Elastic Defend. When enabled, allows a trusted process to also be marked as a trusted ancestor, so all child processes are automatically trusted and skipped by other endpoint subsystems. Configure using the `advanced.trusted_ancestors` policy setting.
- Adds the `size` field to Elastic Defend file events on Linux.
- Optimizes the Elastic Defend kernel driver to collect file and registry access events more efficiently, improving overall system responsiveness and reducing CPU usage.
- Adds script content collection to Elastic Defend on macOS. Use the `advanced.events.script_capture` setting to enable this feature and `advanced.events.script_max_size` to control the maximum size of collected content.
- Improves responsiveness on systems running Elastic Defend.
- Adds an Elastic Defend advanced configuration option to use multiple streams for `get-file` uploads.
- Adds an Elastic Defend advanced configuration option to process multiple `get-file` action uploads in parallel.
- Improves Elastic Defend Tamper Protection error logging to include current policy information when uninstall or upgrade fails due to an invalid uninstall token.
- Reduces the number of I/O operations performed by Elastic Defend for file event enrichment. This reduction is more pronounced when Ransomware Protection is not in use.
- Enables Elastic Defend to save response action upload progress and continue after restart.
- Improves the Elastic Defend startup log to explain unsigned policy details.
- Reduces the performance impact of file copy and move operations involving Windows Offloaded Data Transfer while Elastic Defend is installed.
- Adds an Elastic Defend policy advanced setting to maintain a minimum amount of free disk space.
- Reduces Elastic Defend CPU usage when suppressing activity from trusted applications on Windows. This might be especially noticeable in applications that are JIT-heavy like PowerShell and .NET.
- Improves Elastic Defend visibility into image load events in mixed-architecture scenarios, such as during .NET library loading when the library and main executable might use different architectures. This only applies to Windows 10, version 1709 and later.
- Refactors Elastic Defend Windows file scanning behavior to reduce the risk of file sharing conflicts with other applications and improve the reliability of malware-on-write and event enrichments that rely on file contents such as code signatures and imphashes.
- Improves the accuracy of thread CPU usage reported in Elastic Defend metrics documents.
- Further reduces Elastic Defend behavioral protection CPU usage for trusted applications.


### Fixes

- Fixes an issue where the rule settings pop-up remained open after clicking **Save** when enabling or disabling auto gap fill [#247678](https://github.com/elastic/kibana/pull/247678).
- Fixes the **Get started** page visibility for users with read-only privileges for rules [#247355](https://github.com/elastic/kibana/pull/247355).
- Fixes a display issue with filters on the **MITRE ATT&CK® coverage** page [#246794](https://github.com/elastic/kibana/pull/246794).
- Limits the retrieval of gap summaries to 100 `rule_id`s [#245924](https://github.com/elastic/kibana/pull/245924).
- Fixes threshold rule logic when no "group by" fields are defined [#241022](https://github.com/elastic/kibana/pull/241022).
- Fixes an issue where alerts generated by threshold rules had non-functional source event links [#238707](https://github.com/elastic/kibana/pull/238707).
- Fixes multiple issues searching installed rules by allowing partial matches on rule name and improving special character support [#237496](https://github.com/elastic/kibana/pull/237496).
- Updates the icon that is shown when alert suppression is not available because of insufficient license [#247964](https://github.com/elastic/kibana/pull/247964).
- Truncates long text in the **Value** column in the value list modal [#246679](https://github.com/elastic/kibana/pull/246679).
- Ignores `resource_already_exists_exception` for value list creation hook [#243642](https://github.com/elastic/kibana/pull/243642).
- Fixes an infinite loop bug related to bootstrapping value list resources [#241052](https://github.com/elastic/kibana/pull/241052).
- Fixes an issue where rule exception operators could not be cleared when editing a rule exception [#236051](https://github.com/elastic/kibana/pull/236051).
- Fixes an issue where the Security AI Assistant chat completion API didn't use an associated conversation's system prompt [#248020](https://github.com/elastic/kibana/pull/248020).
- Updates the configuration validation logic for the Google Gemini connector [#245647](https://github.com/elastic/kibana/pull/245647).
- Fixes an issue with the Security AI Assistant **Regenerate** button [#241240](https://github.com/elastic/kibana/pull/241240).
- Fixes Security AI Assistant index entry form field suggestions for nested and multi-fields [#239453](https://github.com/elastic/kibana/pull/239453).
- Prioritizes connector `defaultModel` over stored conversation model [#237947](https://github.com/elastic/kibana/pull/237947).
- Fixes an issue where attack discovery schedules couldn't be created with Case as the connector type [#239748](https://github.com/elastic/kibana/pull/239748).
- Clears the rule selection on the **Translated rules** page after successfully updating an index pattern [#239245](https://github.com/elastic/kibana/pull/239245).
- Fixes an issue where users couldn't change the migration when translating rules [#238679](https://github.com/elastic/kibana/pull/238679).
- Fixes an issue where the `createdBy` field in the notes filter didn't use exact matching [#247351](https://github.com/elastic/kibana/pull/247351).
- Changes the placement of **Migrations** and **Inventory** items in the Elastic Security navigation menu [#247002](https://github.com/elastic/kibana/pull/247002).
- Fixes an issue where Timeline actions appeared in the Alerts table bulk actions menu without proper privileges [#246150](https://github.com/elastic/kibana/pull/246150).
- Fixes an issue where the visual event analyzer preview didn't use the same data view that was selected in the analyzer [#246081](https://github.com/elastic/kibana/pull/246081).
- Fixes an issue where the visual event analyzer rendered before the data view was ready [#245712](https://github.com/elastic/kibana/pull/245712).
- Fixes an issue where the **Threat intelligence** section in the alert details flyout didn't display multiple values [#245449](https://github.com/elastic/kibana/pull/245449).
- Fixes an issue where clicking a rule link from an alert flyout inside a saved Timeline also opened the Timeline [#242313](https://github.com/elastic/kibana/pull/242313).
- Fixes a UI issue when displaying ES|QL queries in Timeline full screen mode [#242027](https://github.com/elastic/kibana/pull/242027).
- Allows saving a Timeline with an adhoc data view [#240537](https://github.com/elastic/kibana/pull/240537).
- Fixes an issue where the onboarding integrations list wasn't fetched for all pages [#239709](https://github.com/elastic/kibana/pull/239709).
- Fixes an issue where the names of the `Security solution default` and `Security solution alerts` data views were displayed incorrectly [#238354](https://github.com/elastic/kibana/pull/238354).
- Fixes an issue where the graph visualization didn't render when switching tabs or refreshing the page [#238038](https://github.com/elastic/kibana/pull/238038).
- Fixes controls on the **Alerts** page [#236756](https://github.com/elastic/kibana/pull/236756).
- Adds support for multiple values in the Indicator details flyout's **Table** tab [#236110](https://github.com/elastic/kibana/pull/236110).
- Fixes a pagination issue with the data table on the **Indicators** page [#241108](https://github.com/elastic/kibana/pull/241108).
- Fixes alert grouping in the alerts table [#237911](https://github.com/elastic/kibana/pull/237911).
- Fixes an issue where the "Top <_n_>" popover stayed open after opening the create case flyout [#242045](https://github.com/elastic/kibana/pull/242045).
- Fixes an issue where entity user and host names were not escaped in URLs, which resulted in invalid URLs [#247707](https://github.com/elastic/kibana/pull/247707).
- Fixes an issue where special characters in ES|QL queries for risk scoring were not handled correctly [#247060](https://github.com/elastic/kibana/pull/247060).
- Fixes an issue where the **Entity summary** section in the entity details flyout showed incorrect vulnerabilities data [#246889](https://github.com/elastic/kibana/pull/246889).
- Updates Active Directory matchers to use SID-based privileged groups for privileged user monitoring [#246763](https://github.com/elastic/kibana/pull/246763).
- Fixes an issue where the **Integrations** section on the privileged user monitoring **Manage data sources** page always showed a "no data stream" warning [#246180](https://github.com/elastic/kibana/pull/246180).
- Fixed the entity risk engine custom filters so that user-supplied KQL syntax isn't double-negated [#242171](https://github.com/elastic/kibana/pull/242171).
- Fixes the entity flyout **Risk contributions** tab link [#241153](https://github.com/elastic/kibana/pull/241153).
- Fixes an issue where the entity popover showed a missing `EngineMetadata.type` error [#239661](https://github.com/elastic/kibana/pull/239661).
- Fixes an issue where the CSPM and Asset Discovery integrations failed to collect data when using agent-based deployment [#241390](https://github.com/elastic/kibana/pull/241390).
- Standardizes how to log errors [#245030](https://github.com/elastic/kibana/pull/245030).
- Adds encoding for CloudFormation URL parameters [#242365](https://github.com/elastic/kibana/pull/242365).
- Fixes a react-query key collision that occurred when two different integration lookups shared the same key [#240517](https://github.com/elastic/kibana/pull/240517).
- Sanitizes lookup names for index creation [#240228](https://github.com/elastic/kibana/pull/240228).
- Introduces a check for Fleet `read` permissions before loading in the integrations data source component [#239122](https://github.com/elastic/kibana/pull/239122).
- Fixes an issue causing "missing authentication credentials" warnings in `TelemetryConfigWatcher` and `PolicyWatcher`, reducing unnecessary warning log entries in the `securitySolution` plugin [#237796](https://github.com/elastic/kibana/pull/237796).
- Fixes an issue where the response actions API (for Elastic Defend agent types) didn't send actions to more than 10 agents [#243387](https://github.com/elastic/kibana/pull/243387).
- Updates response action response codes [#240420](https://github.com/elastic/kibana/pull/240420).
- Fixes endpoint artifacts spaces migration to ensure all artifacts are processed [#238740](https://github.com/elastic/kibana/pull/238740).
- Updates the datafeed of the `packetbeat_dns_tunneling` Elastic Security machine learning job to include runtime mappings [#249317](https://github.com/elastic/kibana/pull/249317).
- Fixes an issue where Elastic Defend on Windows could log a warning about "Quarantine directory failed validation due to ACL or file attribute change" for empty removable media drives such as optical drives.
- Fixes an issue in Elastic Defend that could result in delayed or missing malware-on-write alerts.
- Fixes an issue where Elastic Defend upgrades and uninstallations could fail on busy systems.
- Fixes an issue in Elastic Defend on Windows where Mark of the Web parsing incorrectly handled file origin information ending with a `\0`.
- Prevents unnecessary policy reloads in Elastic Defend when only the overall config version changes.
- Fixes a bug where Elastic Defend for Linux could fail to bootstrap with Elastic Agent.
- Fixes an issue that could prevent Elastic Defend from properly handling upgrades when Tamper Protection is enabled.
- Fixes an issue in Elastic Defend that could cause `get-file` and `execute` response actions to start failing after many are issued with a single running instance of Elastic Defend.
- Improves Elastic Defend detection of file rename operations that occur on Windows over SMB.
- Fixes a bug in Elastic Defend on Linux where the legacy network event source (debugfs/kprobes) would miss network events for non-blocking connect calls.
- Fixes multiple Elastic Defend issues in malware protection for Linux where a deadlock could sometimes occur when containers and autofs were both active.
- For Elastic Defend on Linux, reduces the occurrence of policy failures related to malware protection system deadlock avoidance.
- Improves Elastic Defend on Linux to better handle fanotify events from different mount namespaces.
- Fixes a bug in Elastic Defend Linux event collection where some long-running processes were not enriched.


## 9.2.6


### Features and enhancements

- Adds a new **Overview** tab to the rule details page [#251662](https://github.com/elastic/kibana/pull/251662).
- Adds a `region` field to the Amazon Bedrock connector [#252960](https://github.com/elastic/kibana/pull/252960), [#252956](https://github.com/elastic/kibana/pull/252956).
- Improves Automatic Migration performance by reducing the number of Elasticsearch calls when updating field mappings [#252431](https://github.com/elastic/kibana/pull/252431).
- Updates the `fast-xml-parser` package dependency to version 5.3.4 [#251644](https://github.com/elastic/kibana/pull/251644).


### Fixes

- Improves the performance of bulk rule deletion [#253116](https://github.com/elastic/kibana/pull/253116).
- Fixes accessibility issues in the Security AI Assistant confirm delete modal [#251962](https://github.com/elastic/kibana/pull/251962).
- Adds optional field indicators to the OpenAI connector configuration [#251857](https://github.com/elastic/kibana/pull/251857).
- Fixes an accessibility issue with a missing label in the Security AI Assistant flyout [#251656](https://github.com/elastic/kibana/pull/251656).
- Fixes an issue where detection rules APIs didn't properly validate endpoint response actions [#251352](https://github.com/elastic/kibana/pull/251352).
- Fixes an issue where the `os_types` field was not saved when creating an exception list [#250279](https://github.com/elastic/kibana/pull/250279).
- Fixes a DNS parsing bug in Linux versions of Elastic Defend that could result in crashes.


## 9.2.5


### Features and enhancements

- Further reduces Elastic Defend behavioral protection CPU usage for trusted applications.


### Fixes

- Improves the stability of the **Add Elastic rules** page on deployments with low RAM configurations [#248259](https://github.com/elastic/kibana/pull/248259).
- Fixes an issue in Elastic Defend on Windows that could reduce the detection efficacy of malware-on-write.
- Fixes an issue where Elastic Defend on Windows could log a warning about "Quarantine directory failed validation due to ACL or file attribute change" for empty removable media drives such as optical drives.
- Fixes an issue in Elastic Defend that could cause the system to lock up for up to several minutes during Elastic Endpoint uninstallation or upgrade.


## 9.2.4


### Features and enhancements

- Updates MITRE ATT&CK mappings to `v18.1` [#246770](https://github.com/elastic/kibana/pull/246770).
- Adds a server configuration setting that allows you to disable the automatic installation of the Endpoint Security (Elastic Defend) rule when creating an Elastic Defend integration policy [#246418](https://github.com/elastic/kibana/pull/246418).
- Persists the visual event analyzer's data view selection in local storage [#245002](https://github.com/elastic/kibana/pull/245002).
- Improves responsiveness on systems running Elastic Defend.
- Optimizes the Elastic Defend kernel driver to collect file and registry access events more efficiently, improving overall system responsiveness and reducing CPU usage.


### Fixes

- Fixes an issue where the Security AI Assistant chat completion API didn't use an associated conversation's system prompt [#248020](https://github.com/elastic/kibana/pull/248020).
- Fixes an issue where entity user and host names were not escaped in URLs, which resulted in invalid URLs [#247707](https://github.com/elastic/kibana/pull/247707).
- Fixes an issue where the `createdBy` field in the notes filter didn't use exact matching [#247351](https://github.com/elastic/kibana/pull/247351).
- Fixes an issue where special characters in ES|QL queries for risk scoring were not handled correctly [#247060](https://github.com/elastic/kibana/pull/247060).
- Fixes a display issue with filters on the **MITRE ATT&CK® coverage** page [#246794](https://github.com/elastic/kibana/pull/246794).
- Fixes an issue where the **Integrations** section on the privileged user monitoring **Manage data sources** page always showed a "no data stream" warning [#246180](https://github.com/elastic/kibana/pull/246180).
- Fixes an issue where Timeline actions appeared in the Alerts table bulk actions menu without proper privileges [#246150](https://github.com/elastic/kibana/pull/246150).
- Fixes an issue where the visual event analyzer preview didn't use the same data view that was selected in the analyzer [#246081](https://github.com/elastic/kibana/pull/246081).
- Fixes an issue where the visual event analyzer rendered before the data view was ready [#245712](https://github.com/elastic/kibana/pull/245712).
- Fixes an issue where the **Threat intelligence** section in the alert details flyout didn't display multiple values [#245449](https://github.com/elastic/kibana/pull/245449).
- Fixes an issue in Elastic Defend Windows on-write malware scanning that could cause sharing violations when other applications attempted to open files.
- Fixes an issue where Elastic Defend upgrades and uninstallations could fail on busy systems.
- Fixes an issue in Elastic Defend on Windows where Mark of the Web parsing incorrectly handled file origin information ending with a `\0`.
- For Elastic Defend on Linux, reduces the occurrence of policy failures related to malware protection system deadlock avoidance.
- Fixes an issue in Elastic Defend that could result in delayed or missing malware-on-write alerts.
- Fixes a bug in Elastic Defend on Windows that could sometimes result in `KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL` or `PAGE_FAULT_IN_NONPAGED_AREA` bugchecks when [Offloaded Data Transfer (ODX)](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/offloaded-data-transfer) was used to copy files.  This regression was introduced in Elastic Defend versions 8.19.8, 9.1.8, and 9.2.2.


## 9.2.3


### Features and enhancements

- Shows session view in full height [#245888](https://github.com/elastic/kibana/pull/245888).
- Shows analyzer in full height [#245857](https://github.com/elastic/kibana/pull/245857).
- Hardens Elastic Defend on Windows against Bind Filter rebinding attacks.
- Adds `process.group_leader.pid` and `process.session_leader.pid` to Elastic Defend MacOS process exec events.
- Improves general system responsiveness while Elastic Defend is installed.
- Reduces the number of I/O operations performed by Elastic Defend for file event enrichment.  This reduction is more pronounced when Ransomware Protection is not in use.


### Fixes

- Standardizes how to log errors [#245030](https://github.com/elastic/kibana/pull/245030).
- Fixes a bug for Elastic Defend on Linux, where the legacy network event source (debugfs/kprobes) would miss network events for non-blocking connect calls.


## 9.2.2


### Features and enhancements

- Improves the alert details flyout by saving the selected threat intelligence time to local storage [#243571](https://github.com/elastic/kibana/pull/243571).
- Improves the alert details flyout by saving the selected prevalence time to local storage [#243543](https://github.com/elastic/kibana/pull/243543).


### Fixes

- Fixes response actions API (for Elastic Defend agent types) not sending action to more than 10 agents [#243387](https://github.com/elastic/kibana/pull/243387).
- Fixes an issue where clicking a rule link from an alert flyout inside a saved Timeline would also open the Timeline [#242313](https://github.com/elastic/kibana/pull/242313).
- Fixes an issue where the "Top <_n_>" popover stayed open after opening the create case flyout. It now closes automatically when the flyout opens [#242045](https://github.com/elastic/kibana/pull/242045).
- Fixes a UI issue when displaying ES|QL queries in Timeline full screen mode [#242027](https://github.com/elastic/kibana/pull/242027).
- Allows saving a Timeline with an adhoc data view [#240537](https://github.com/elastic/kibana/pull/240537).
- Fixes an issue where alerts generated by threshold rules had non-functional source event links [#238707](https://github.com/elastic/kibana/pull/238707).
- Ignores `resource_already_exists_exception` for value list creation hook [#243642](https://github.com/elastic/kibana/pull/243642).
- Adds support for multiple values in the Indicator details flyout's **Table** tab [#236110](https://github.com/elastic/kibana/pull/236110).
- Prevents unnecessary policy reloads in Elastic Defend when only the overall config version changes.
- Fixes a bug where Elastic Defend for Linux could fail to bootstrap with Elastic Agent.
- Generates already mounted events for device control.


## 9.2.1


### Features and enhancements

- Improves the startup log in Elastic Defend to explain the details of unsigned policy.
- Improves the accuracy of thread CPU usage reported in Elastic Defend metrics documents.


### Fixes

- Fixes an issue where the CSPM and Asset Discovery integrations failed to collect data when using agent-based deployment [#241390](https://github.com/elastic/kibana/pull/241390).
- Fixes a react-query key collision that occurred when two different integration lookups shared the same key, which could cause errors when navigating between pages [#240517](https://github.com/elastic/kibana/pull/240517).
- Fixes multiple issues searching installed rules by allowing partial matches on rule name and improving special character support [#237496](https://github.com/elastic/kibana/pull/237496).
- Fixes an Elastic Defend bug in Linux event collection where some long-running processes were not enriched.
- Fixes multiple Elastic Defend issues in malware protection for Linux where a deadlock could sometimes occur when containers and autofs were both active.
- Fixes an Elastic Defend issue that could cause the `get-file` and `execute` response actions to fail after many were issued with a single running instance of Elastic Defend
- Improves Elastic Defend detection of file rename operations on Windows when performed over Server Message Block (SMB).
- Fixes an Elastic Defend issue on Windows where the `code_signature.thumbprint_sha256` field was missing under process and DLL events for certain event types.


## 9.2.0


### Features and enhancements

- Adds the Security Entity Analytics risk score reset feature [#237829](https://github.com/elastic/kibana/pull/237829).
- Introduces a Security risk scoring AI Assistant tool [#233647](https://github.com/elastic/kibana/pull/233647).
- Uses ES|QL for calculating entity risk scores [#237871](https://github.com/elastic/kibana/pull/237871).
- Enables privileged user monitoring and the Entity analytics navigation item by default [#237436](https://github.com/elastic/kibana/pull/237436).
- Enables discovering privileged users from the Entity Analytics Okta integration [#237129](https://github.com/elastic/kibana/pull/237129).
- Adds the data view picker to the **Privileged user monitoring** dashboard page [#233264](https://github.com/elastic/kibana/pull/233264).
- Implements minor UI changes on **Privileged user monitoring** dashboard page [#231921](https://github.com/elastic/kibana/pull/231921).
- Populates the `entity.attributes.Privileged` field in the entity store for users [#237038](https://github.com/elastic/kibana/pull/237038).
- Adds public APIs for attack discovery and attack discovery schedules [#236736](https://github.com/elastic/kibana/pull/236736).
- Displays total execution time for automatic migrations [#236147](https://github.com/elastic/kibana/pull/236147).
- Adds **Update missing index pattern** option to the automatic migration **Translated rules** page [#233258](https://github.com/elastic/kibana/pull/233258).
- Introduces new API endpoints for automatic migration of dashboards [#229112](https://github.com/elastic/kibana/pull/229112).
- Adds a new deployment method, "cloud connector", for the CSPM and Asset Discovery integrations [#235442](https://github.com/elastic/kibana/pull/235442), [#230137](https://github.com/elastic/kibana/pull/230137).
- Implements CDR Data View versioning and migration logic [#238547](https://github.com/elastic/kibana/pull/238547).
- Makes automatic troubleshooting generally available [#234853](https://github.com/elastic/kibana/pull/234853).
- Updates the automatic troubleshooting feature to detect warnings and failures in Elastic Defend policy responses and suggest possible remediations [#231908](https://github.com/elastic/kibana/pull/231908).
- Adds an advanced setting that keeps the alert suppression window active after you close an alert, preventing new alerts during that period [#231079](https://github.com/elastic/kibana/pull/231079).
- Adds `DOES NOT MATCH` capability to indicator match rules [#227084](https://github.com/elastic/kibana/pull/227084).
- Adds the `customized_fields` and `has_base_version` fields to the `rule_source` object schema [#234793](https://github.com/elastic/kibana/pull/234793).
- Enables the auto-extract observables toggle in the alerts table for both row and bulk actions when adding alerts to a case [#235433](https://github.com/elastic/kibana/pull/235433).
- Enables the new data view picker [#234101](https://github.com/elastic/kibana/pull/234101).
- Adds a `managed` property to data views, marking Kibana-managed data views with a **Managed** tag [#223451](https://github.com/elastic/kibana/pull/223451).
- Adds support for specifying a reason when closing an alert [#226590](https://github.com/elastic/kibana/pull/226590).
- Adds a source event ID link to the alert flyout's **Highlighted fields** section, allowing you to quickly preview the event that triggered the alert [#224451](https://github.com/elastic/kibana/pull/224451).
- Updates the indicator details flyout's UI to be more consistent with the alert details flyout's UI [#230593](https://github.com/elastic/kibana/pull/230593).
- Restricts **Value report** page access to `admin` and `soc_manager` roles in the Security Analytics Complete Serverless feature tier [#234377](https://github.com/elastic/kibana/pull/234377).
- Implements the **Value report** page for the Elastic AI SOC Engine (EASE) Serverless project type [#228877](https://github.com/elastic/kibana/pull/228877).
- Adds conversation sharing functionality to the Security AI Assistant, allowing you to share conversations with team members [#230614](https://github.com/elastic/kibana/pull/230614).
- Adds a non-CVE reference link list to the vulnerability details flyout [#225601](https://github.com/elastic/kibana/pull/225601).
- Adds support for using the `runscript` response action on SentinelOne-enrolled hosts [#234492](https://github.com/elastic/kibana/pull/234492).
- Adds support for using the `cancel` response action on MDE-enrolled hosts [#230399](https://github.com/elastic/kibana/pull/230399).
- Adds support for trusted applications advanced mode [#230111](https://github.com/elastic/kibana/pull/230111).
- Introduces the Elastic Defend **Endpoint Exceptions** sub-feature privilege [#233433](https://github.com/elastic/kibana/pull/233433).
- Adds an Elastic Defend advanced policy setting that allows you to disable the firewall anti-tamper plugin or move it into detect-only mode [#236431](https://github.com/elastic/kibana/pull/236431).
- Adds two new Elastic Defend advanced policy settings that allow you to opt out of collecting ransomware diagnostics on macOS [#235193](https://github.com/elastic/kibana/pull/235193).
- Adds an Elastic Defend advanced policy setting to disable the filtering of file-backed volumes and CD-ROMs in the `device_control` plugin [#236620](https://github.com/elastic/kibana/pull/236620).
- Adds an Elastic Defend option to remediate orphaned state by attempting to start Elastic Agent service.
- Adds a new device data stream to the Elastic Defend integration.
- Adds two new dashboards to the Elastic Defend integration.
- Adds more Elastic Defend options to the Logstash output, allowing for finer control.
- Increases the throughput of Elastic Defend's Logstash connections by increasing the maximum size it can upload at once.
- Adds Elastic Defend support for device control on macOS and Windows.
- Adds architecture of PE file in Windows malware alerts to Elastic Defend.
- Adds the `Endpoint.state.orphaned` indicator to Elastic Defend policy response.
- Adds Elastic Defend support for cluster migration.
- Adds firewall anti-tamper plug-in to protect Elastic Endpoint processes against network blocking through Windows Firewall.
- Includes `origin_url`, `origin_referrer_url`, and `Ext.windows.zone_identifier` fields to Elastic Defend by default to Windows image load and process events, if the information can be retrieved.
- Improves Elastic Defend by integrating a new Event Tracing for Windows (ETW) provider (Microsoft-Windows-Ldap-Client) to create new event types that prebuilt endpoint rules can use to detect malicious LDAP activity.
- Improves reporting reliability and accuracy of Elastic Defend's Elasticsearch connection.
- Enriches Elastic Defend macOS network connect events with `network.direction`. Possible values are `ingress` and `egress`.
- Improves Elastic Defend malware scan queue efficiency by not blocking scan requests when an oplock for the file being scanned cannot be acquired.
- Adds an Elastic Defend advanced policy setting `windows.advanced.events.security.event_disabled` that lets users disable security event collection per event ID.
- Shortens the time it takes Elastic Defend to recover from a `DEGRADED` status caused by communication issues with Elastic Agent.
- Improves the `verify` command to ensure Elastic Endpoint service is running, otherwise Elastic Agent has to fix it automatically.
- Adds experimental Elastic Defend support for Windows on ARM. This is pre-release software under active development, and should not be run on any production systems. We welcome feedback in our [community Slack](https://ela.st/slack).
- Improves the reliability of Elastic Defend Kafka connections.


### Fixes

- Fixes an issue where the names of the `Security solution default` and `Security solution alerts` data views were displayed incorrectly [#238354](https://github.com/elastic/kibana/pull/238354).
- Fixes an issue where the navigation manu overlapped expandable flyouts [#236655](https://github.com/elastic/kibana/pull/236655).
- Ensures the data view picker icon is always vertically centered [#236379](https://github.com/elastic/kibana/pull/236379).
- Integrates data view logic into host KPIs charts [#236084](https://github.com/elastic/kibana/pull/236084).
- Fixes integrations RAG in automatic migration rule translations [#234211](https://github.com/elastic/kibana/pull/234211).
- Removes the feature flag for privileged user monitoring [#233960](https://github.com/elastic/kibana/pull/233960).
- Returns a 500 response code if there is an error during privileged user monitoring engine initialization [#234368](https://github.com/elastic/kibana/pull/234368).
- Ensures that privileged user `@timestamp` and `event.ingested` fields are updated when a privileged user is updated [#233735](https://github.com/elastic/kibana/pull/233735).
- Fixes a bug in privileged user monitoring index synchronization where stale users weren't removed after index pattern changes [#229789](https://github.com/elastic/kibana/pull/229789).
- Updates the privileged user monitoring UI to replace hard-coded CSS values with the EUI theme [#225307](https://github.com/elastic/kibana/pull/225307).
- Fixes incorrect threat enrichment for partially matched `AND` conditions in indicator match rules [#230773](https://github.com/elastic/kibana/pull/230773).
- Adds a validation error to prevent users from setting a custom action interval shorter than the rule's check interval [#229976](https://github.com/elastic/kibana/pull/229976).
- Fixes accessibility issues on the **Benchmarks** page [#229521](https://github.com/elastic/kibana/pull/229521).
- Simplifies the Cloud Security Posture Misconfigurations data view by removing redundancy in the index pattern definition [#227995](https://github.com/elastic/kibana/pull/227995).
- Fixes an issue causing "missing authentication credentials" warnings in `TelemetryConfigWatcher` and `PolicyWatcher`, reducing unnecessary warning log entries in the `securitySolution` plugin.
- Fixes an Elastic Defend issue on Linux by preventing unnecessary locking within Malware Protections to avoid invalid watchdog firings.
- Fixes issues that could sometimes cause crashes of the Elastic Defend user-mode process on busy Windows systems.
- Adds support in Elastic Defend for installing eBPF event probes on Linux endpoints when cgroup2 is mounted in a non-standard location or not mounted at all.
- Adds support in Elastic Defend for installing eBPF probes on Linux endpoints when taskstats is compiled out of the kernel.
- Fixes an issue in Elastic Defend where Linux network events could have source and destination bytes swapped.
- Fixes a bug where Linux capabilities were included in Elastic Endpoint network events despite being disabled.
- Fixes an issue where Elastic Defend would incorrectly calculate throughput capacity when sending documents to output. This may have limited event throughput on extremely busy endpoints.
- Improves the reliability of local Elastic Defend administrative shell commands. In rare cases, a command could fail to execute due to issues with interprocess communication.
- Fixes an issue in Elastic Defend where host isolation could auto-release incorrectly. Host isolation now only releases when Elastic Endpoint becomes orphaned. Intermittent Elastic Agent connectivity changes no longer alter the host isolation state.
- Fixes a bug in Elastic Defend where Linux endpoints would report `process.executable` as a relative, instead of absolute, path.
- Fixes an issue which could cause Elastic Defend to improperly report success when self-healing rollback attempted to terminate a process with an active debugger on Windows.
- Fixes an issue in Elastic Defend installation logging where only the first character of install paths (usually 'C') was logged.
- Fixes an issue to improve reliability of health status reporting between Elastic Endpoint and Elastic Agent.
- Fixes a race condition in Elastic Defend that occasionally resulted in corrupted process command lines on Windows. This could cause incorrect values for `process.command_line`, `process.args_count`, and `process.args`, leading to false positives.
- Fixes an issue in Elastic Defend that could result in a crash if a specified Logstash output configuration contained a certificate that couldn't be parsed.
- Fixes CVE-2025-37735 ([ESA-2025-23](https://discuss.elastic.co/t/elastic-defend-8-19-6-9-1-6-and-9-2-0-security-update-esa-2025-23/383272)) in Elastic Defend on Windows which could allow a low-privilege attacker to delete arbitrary files on the system and potentially escalate privileges to SYSTEM. Windows 11 24H2 includes changes which make this issue harder to exploit.


## 9.1.10


### Features and enhancements

- Updates MITRE ATT&CK mappings to `v18.1` [#246770](https://github.com/elastic/kibana/pull/246770).


### Fixes

- Fixes an issue where the Security AI Assistant chat completion API didn't use an associated conversation's system prompt [#248020](https://github.com/elastic/kibana/pull/248020).
- Fixes an issue where entity user and host names were not escaped in URLs, which resulted in invalid URLs [#247707](https://github.com/elastic/kibana/pull/247707).
- Fixes an issue where the `createdBy` field in the notes filter didn't use exact matching [#247351](https://github.com/elastic/kibana/pull/247351).
- Fixes a display issue with filters on the **MITRE ATT&CK® coverage** page [#246794](https://github.com/elastic/kibana/pull/246794).
- Fixes an issue where Timeline actions appeared in the Alerts table bulk actions menu without proper privileges [#246150](https://github.com/elastic/kibana/pull/246150).
- Limits the detection rule execution gaps API for retrieving gap summaries to 100 `rule_id`s per request [#245924](https://github.com/elastic/kibana/pull/245924).
- Fixes an issue where the **Threat intelligence** section in the alert details flyout didn't display multiple values [#245449](https://github.com/elastic/kibana/pull/245449).
- Fixes an issue where Elastic Defend upgrades and uninstallations could fail on busy systems.
- Fixes an issue in Elastic Defend on Windows where Mark of the Web parsing incorrectly handled file origin information ending with a `\0`.
- For Elastic Defend on Linux, reduces the occurrence of policy failures related to malware protection system deadlock avoidance.
- Fixes a bug in Elastic Defend on Windows that could sometimes result in `KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL` or `PAGE_FAULT_IN_NONPAGED_AREA` bugchecks when [Offloaded Data Transfer (ODX)](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/offloaded-data-transfer) was used to copy files.  This regression was introduced in Elastic Defend versions 8.19.8, 9.1.8, and 9.2.2.


## 9.1.9


### Features and enhancements

- Shows session view in full height [#245888](https://github.com/elastic/kibana/pull/245888).
- Shows analyzer in full height [#245857](https://github.com/elastic/kibana/pull/245857).
- Hardens Elastic Defend on Windows against Bind Filter rebinding attacks.
- Improves general system responsiveness while Elastic Defend is installed.


### Fixes

- Standardizes how to log errors [#245030](https://github.com/elastic/kibana/pull/245030).
- Fixes an issue that could prevent Elastic Defend from properly handling upgrades when Tamper Protection is enabled.
- Elastic Defend no longer reloads its policy if nothing has functionally changed from the previous policy.
- For Linux Elastic Defend, fixes a bug where the legacy network event source (debugfs/kprobes) would miss network events for non-blocking connect calls.


## 9.1.8


### Features and enhancements

- Improves the alert details flyout by saving the selected threat intelligence time to local storage [#243571](https://github.com/elastic/kibana/pull/243571).
- Ignores `resource_already_exists_exception` for value list creation hook [#243642](https://github.com/elastic/kibana/pull/243642).


### Fixes

- Fixes an issue where the "Top <_n_>" popover stayed open after opening the create case flyout. It now closes automatically when the new case flyout opens [#242045](https://github.com/elastic/kibana/pull/242045).
- Fixes a UI issue when displaying ES|QL queries in Timeline full screen mode [#242027](https://github.com/elastic/kibana/pull/242027).
- Prevents unnecessary policy reloads in Elastic Defend when only the overall config version changes.
- Fixes a bug where Elastic Defend for Linux could fail to bootstrap with Elastic Agent.


## 9.1.7


### Features and enhancements

- Improves the reliability of Cloud Security Posture (CSP) data by automatically upgrading outdated Misconfiguration and Vulnerabilities data views to the correct versions [#238547](https://github.com/elastic/kibana/pull/238547).
- Adds more Elastic Defend options to the Logstash output, allowing for finer control.
- Improves the accuracy of thread CPU usage reported in Elastic Defend metrics documents.


### Fixes

- Fixes entity flyout **Risk contributions** tab link [#241153](https://github.com/elastic/kibana/pull/241153).
- Fixes a pagination issue with the data table on the **Indicators** page [#241108](https://github.com/elastic/kibana/pull/241108).
- Fixes a react-query key collision that occurred when two different integration lookups shared the same key, which could cause errors when navigating between pages [#240517](https://github.com/elastic/kibana/pull/240517).
- Fixes multiple issues searching installed rules by allowing partial matches on rule name and improving special character support [#237496](https://github.com/elastic/kibana/pull/237496).
- Fixes an issue where rule exception operators could not be cleared when editing a rule exception [#236051](https://github.com/elastic/kibana/pull/236051).
- Fixes an Elastic Defend issue on Linux by preventing unnecessary locking within malware protection to avoid invalid watchdog firings.
- Fixes issues that could sometimes cause crashes of the Elastic Defend user-mode process on busy Windows systems.
- Fixes multiple Elastic Defend issues in malware protection for Linux where a deadlock could sometimes occur when containers and autofs were both active.
- Fixes CVE-2025-37735 ([ESA-2025-23](https://discuss.elastic.co/t/elastic-defend-8-19-6-9-1-6-and-9-2-0-security-update-esa-2025-23/383272)) in Elastic Defend on Windows which could allow a low-privilege attacker to delete arbitrary files on the system and potentially escalate privileges to SYSTEM. Windows 11 24H2 includes changes which make this issue harder to exploit.
- Fixes an Elastic Defend bug in Linux event collection where some long-running processes were not enriched.
- Fixes an Elastic Defend issue that could cause the `get-file` and `execute` response actions to fail after many were issued with a single running instance of Elastic Defend.


## 9.1.6


### Features and enhancements

- Adds the `customized_fields` and `has_base_version` fields to the `rule_source` object schema  [#234793](https://github.com/elastic/kibana/pull/234793).
- Implements CDR Data View versioning and migration logic [#238547](https://github.com/elastic/kibana/pull/238547).


### Fixes

- Fixes Elastic Endpoint artifacts spaces migration to ensure all artifacts are processed [#238740](https://github.com/elastic/kibana/pull/238740).
- Fixes an issue causing "missing authentication credentials" warnings in `TelemetryConfigWatcher` and `PolicyWatcher`, reducing unnecessary warning log entries in the `securitySolution` plugin [#237796](https://github.com/elastic/kibana/pull/237796).
- Prioritizes connector `defaultModel` over stored conversation model [#237947](https://github.com/elastic/kibana/pull/237947).


## 9.1.5


### Features and enhancements

- Adds an Elastic Defend option to remediate orphaned state by attempting to start Elastic Agent service.
- Increases the throughput of Elastic Defend Logstash connections by increasing the maximum size it can upload at once.
- Improves reliability and accuracy of reporting of the Elastic Defend's Elasticsearch connection.


### Fixes

- Fixes browser fields caching to use the `dataView` ID instead of the index pattern [#234381](https://github.com/elastic/kibana/pull/234381).
- Removes `null` in confirmation dialog when bulk editing index patterns for rules [#236572](https://github.com/elastic/kibana/pull/236572).
- Fixes the URL passed to detection rule actions using the `{{context.results_link}}` placeholder [#236067](https://github.com/elastic/kibana/pull/236067).
- Fixes system prompt updates from the Conversations tab in AI Assistant [#234812](https://github.com/elastic/kibana/pull/234812).
- Fixes an issue in the Highlighted fields table in the alert details flyout [#234222](https://github.com/elastic/kibana/pull/234222).
- Fixes an issue in rule exceptions to include the `matches` operator only for supported fields [#233127](https://github.com/elastic/kibana/pull/233127).
- Adds support in Elastic Defend for installing eBPF event probes on Linux endpoints when cgroup2 is mounted in a non-standard location or not mounted at all.
- Adds support in Elastic Defend for installing eBPF probes on Linux endpoints when taskstats is compiled out of the kernel.
- Fixes an issue in Elastic Defend where Linux network events could have source and destination bytes swapped.
- Removes `.process.thread.capabilities.permitted` and `.process.thread.capabilities.effective` from Linux network events in Elastic Defend.
- Fixes an issue in Elastic Defend where host isolation could auto-release incorrectly. Host isolation now only releases when Elastic Endpoint becomes orphaned. Intermittent Elastic Agent connectivity changes no longer alter the host isolation state.
- Fixes an issue where Elastic Defend would incorrectly calculate throughput capacity when sending documents to output.  This may have limited event throughput on extremely busy endpoints.
- Fixes an issue in Elastic Defend installation logging where only the first character of install paths (usually 'C') would be logged.


## 9.1.4


### Features and enhancements

- Adds more Linux diagnostic process `ptrace` events.


### Fixes

- Fixes filtering on the **Alerts** page by checking for an empty dataView [#235144](https://github.com/elastic/kibana/pull/235144).
- Fixes a bug where the toggle column functionality only functioned on the **Alerts** page [#234278](https://github.com/elastic/kibana/pull/234278).
- Fixes a bug where Linux capabilities were included in Elastic Endpoint network events despite being disabled.
- Makes the delivery of Elastic Endpoint command line commands more robust. In rare cases, commands could previously fail due to interprocess communication issues.


## 9.1.3


### Fixes

- Fixes a bug that prevented the vulnerability findings contextual flyout from showing details [#231778](https://github.com/elastic/kibana/pull/231778).
- Fixes an issue preventing the creation of Knowledge Base Index Entries in deployments with a large number of indices/mappings [#231376](https://github.com/elastic/kibana/pull/231376).
- Fixes a bug where Linux endpoints would report `process.executable` as a relative, instead of absolute, path.


## 9.1.2


### Features and enhancements

- Adds Automatic Import documentation links for users in log description and the error message so that users have better access to the data types that are valid [#229375](https://github.com/elastic/kibana/pull/229375).
- To help identify which parts of `elastic-endpoint.exe` are using a significant amount of CPU, Elastic Defend on Windows can now include CPU profiling data in diagnostics. To request CPU profiling data using the command line, refer to [Elastic Agent command reference](/docs/reference/fleet/agent-command-reference#_options). To request CPU profiling data using Kibana, check the **Collect additional CPU metrics** box when requesting Elastic Agent diagnostics.
- Improves Elastic Defend malware scan queue efficiency on Windows by not blocking scan requests when an oplock for the file being scanned cannot be acquired.
- Allows Elastic Defend to automatically recover in some situations when it loses connectivity with Elastic Agent.


### Fixes

- Fixes privileged user monitoring index sync in non-default Kibana spaces [#230420](https://github.com/elastic/kibana/pull/230420).
- Only creates a privileged user monitoring default index source if one doesn't currently exist [#229693](https://github.com/elastic/kibana/pull/229693).
- Fixes a race condition in Elastic Defend that may occasionally result in corrupted process command lines on Windows. When this occurs, `process.command_line`, `process.args_count` and `process.args` may be incorrect, leading to false positives.
- Due to an issue in macOS, Elastic Defend would sometimes send network events without `user.name` populated. Elastic Defend will now identify these events and populate `user.name` if necessary.


## 9.1.1


### Features and enhancements

- Improves the reliability of Elastic Defend Kafka connections.


### Fixes

- Fixes a bug by moving the `scheduleNow` call to the privileged monitoring engine initialization step, ensuring the task is only scheduled after the engine is fully created and ready [#230263](https://github.com/elastic/kibana/pull/230263).
- Fixes a bug where the base version API route cache was not properly invalidated after rule import [#228475](https://github.com/elastic/kibana/pull/228475).
- Fixes an issue in Elastic Defend performance metrics that resulted in `endpoint_uptime_percent` always being 0 for behavioral rules.


## 9.1.0


### Features and enhancements

- Adds an option to update the `kibana.alert.workflow_status` field for alerts associated with attack discoveries [#225029](https://github.com/elastic/kibana/pull/225029).
- The rule execution gaps functionality is now generally available [#224657](https://github.com/elastic/kibana/pull/224657).
- Adds the Security Entity Analytics privileged user monitoring feature [#224638](https://github.com/elastic/kibana/pull/224638).
- Adds the ability to bulk fill gaps [#224585](https://github.com/elastic/kibana/pull/224585).
- Automatic migration is now generally available [#224544](https://github.com/elastic/kibana/pull/224544).
- Adds a name field to the automatic migration UI [#223860](https://github.com/elastic/kibana/pull/223860).
- Adds the ability to bulk set up and delete alert suppression [#223090](https://github.com/elastic/kibana/pull/223090).
- Adds a human-readable incremental ID to cases, making referencing cases easier [#222874](https://github.com/elastic/kibana/pull/222874).
- Adds the ability to change rule migration execution settings when re-processing a migration [#222542](https://github.com/elastic/kibana/pull/222542).
- Adds `runscript` response action support for Microsoft Defender for Endpoint–enrolled hosts [#222377](https://github.com/elastic/kibana/pull/222377).
- Updates automatic migration API schema [#219597](https://github.com/elastic/kibana/pull/219597).
- Adds `siemV3` role migration to support the new Security **Global Artifact Management** privilege [#219566](https://github.com/elastic/kibana/pull/219566).
- Adds automatic saving of attack discoveries, with search and filter capabilities [#218906](https://github.com/elastic/kibana/pull/218906).
- Adds the ability to edit highlighted fields in the alert details flyout [#216740](https://github.com/elastic/kibana/pull/216740).
- Adds API endpoints for the Entity Analytics privileged user monitoring feature [#215663](https://github.com/elastic/kibana/pull/215663).
- Adds the onboarding flow for the Asset Inventory feature [#212315](https://github.com/elastic/kibana/pull/212315).
- Adds the XSOAR connector [#212049](https://github.com/elastic/kibana/pull/212049).
- Adds a custom script selector for choosing scripts to execute when using the `runscript` response action [#204965](https://github.com/elastic/kibana/pull/204965).
- Updates Elastic Security Labs Knowledge Base content [#227125](https://github.com/elastic/kibana/pull/227125).
- Bumps default Gemini model [#225917](https://github.com/elastic/kibana/pull/225917).
- Groups vulnerabilities by resource and cloud account using IDs instead of names [#225492](https://github.com/elastic/kibana/pull/225492).
- Adds prompt tiles to the Security AI Assistant [#224981](https://github.com/elastic/kibana/pull/224981).
- Adds support for collapsible sections in integrations READMEs [#223916](https://github.com/elastic/kibana/pull/223916).
- Adds advanced policy settings in Elastic Defend to enable collection of file origin information for File, Process, and DLL (ImageLoad) events [#223882](https://github.com/elastic/kibana/pull/223882), [#222030](https://github.com/elastic/kibana/pull/222030).
- Adds the `ecs@mappings` component to the transform destination index template [#223878](https://github.com/elastic/kibana/pull/223878).
- Adds the ability to revert a customized prebuilt rule to its original version [#223301](https://github.com/elastic/kibana/pull/223301).
- Displays which fields are customized for prebuilt rules [#225939](https://github.com/elastic/kibana/pull/225939).
- Adds an Elastic Defend advanced policy setting that allows you to enable or disable the Microsoft-Windows-Security-Auditing ETW provider for security events collection [#222197](https://github.com/elastic/kibana/pull/222197).
- Updates the risk severity color map to match the new design [#222061](https://github.com/elastic/kibana/pull/222061).
- Updates the asset criticality status color map to match the new design [#222024](https://github.com/elastic/kibana/pull/222024).
- Updates the highlighted fields button styling in the alert details flyout [#221862](https://github.com/elastic/kibana/pull/221862).
- Adds support for content connectors in Elastic Security and Observability [#221856](https://github.com/elastic/kibana/pull/221856).
- Expands CVE ID search to all search parameters, not only names [#221099](https://github.com/elastic/kibana/pull/221099).
- Improves alert searching and filtering by including additional ECS data stream fields [#220447](https://github.com/elastic/kibana/pull/220447).
- Updates default model IDs for Amazon Bedrock and OpenAI connectors [#220146](https://github.com/elastic/kibana/pull/220146).
- Adds support for PKI (certificate-based) authentication for the OpenAI **Other** connector providers [#219984](https://github.com/elastic/kibana/pull/219984).
- Adds pinning and settings to the **Table** tab in the alert and event details flyouts [#218686](https://github.com/elastic/kibana/pull/218686).
- Updates the data view selector in the event analyzer [#218183](https://github.com/elastic/kibana/pull/218183).
- Updates the data view selector in the global header [#216685](https://github.com/elastic/kibana/pull/216685).
- Updates UI handling for multiple CVEs and package fields [#216411](https://github.com/elastic/kibana/pull/216411).
- Adds the Security AI prompts integration [#216106](https://github.com/elastic/kibana/pull/216106).
- Adds support for grouping multi-value fields in Cloud Security [#215913](https://github.com/elastic/kibana/pull/215913).
- Limits unassigned notes to a maximum of 100 per document instead of globally [#214922](https://github.com/elastic/kibana/pull/214922).
- Updates the Detection rule monitoring dashboard to include rule gaps histogram [#214694](https://github.com/elastic/kibana/pull/214694).
- Adds support for multiple CVEs and improves vulnerability data grid, flyout, and contextual flyout UI [#213039](https://github.com/elastic/kibana/pull/213039).
- Adds support for the `MV_EXPAND` command for the ES|QL rule type [#212675](https://github.com/elastic/kibana/pull/212675).
- Adds support for partial results for the ES|QL rule type [#223198](https://github.com/elastic/kibana/pull/223198).
- Updates the data view selector in Timelines [#210585](https://github.com/elastic/kibana/pull/210585).
- Adds `unassigned` as an asset criticality level for bulk uploads [#208884](https://github.com/elastic/kibana/pull/208884).
- Enables `isolate` and `release` response actions from the event details flyout [#206857](https://github.com/elastic/kibana/pull/206857).
- Standardizes action triggers in alerts KPI visualizations [#206340](https://github.com/elastic/kibana/pull/206340).
- Introduces space-awareness capabilities for Elastic Defend and other Elastic Security-specific Fleet features.
- Adds Elastic Defend process event monitoring for `ptrace` and `memfd` activity on Linux (kernel 5.10+) using eBPF.
- Adds support for DNS events on macOS. Events can be controlled from the Elastic Defend policy using the **DNS events** checkbox.
- Adds TCC (Transparency Consent and Control) events to Elastic Defend on macOS. Events are generated every time the TCC database is altered.
- Adds `parent.command_line` to Elastic Defend process events on macOS to keep in line with Linux and Windows.
- Reduces Elastic Defend CPU usage for ETW events, API events, and behavioral protections. In some cases, this may be a significant reduction.
- Elastic Defend: Changes the security events source from the Event Log provider to Event Tracing for Windows (Microsoft-Windows-Security Auditing) provider and enriches the events with additional data.
- Adds Elastic Defend support for Elliptic Curve certificates and TLS output settings, including `supported_protocols`, `cipher_suites`, and `curve_types`.
- Reduces Elastic Defend CPU and memory usage for behavioral protections.
- Reduces Elastic Defend CPU when processing events from the System process, such as IIS network events.
- Improves Elastic Defend logging of fatal exceptions.
- Improves Elastic Defend call site analysis logic.


### Fixes

- Fixes a bug where data wasn't fetched by the vulnerability expandable flyout in preview mode [#227262](https://github.com/elastic/kibana/pull/227262).
- Fixes a bug where Timelines and investigations did not consistently use the default Security data view [#226314](https://github.com/elastic/kibana/pull/226314).
- Fixes a bug where opening an alert deeplink didn't correctly load filters on the **Alerts** page [#225650](https://github.com/elastic/kibana/pull/225650).
- Updates entity links to open in a flyout instead of leaving the current page [#225381](https://github.com/elastic/kibana/pull/225381).
- Adds a title to the rule gap histogram in the Detection rule monitoring dashboard [#225274](https://github.com/elastic/kibana/pull/225274).
- Fixes URL query handling for the asset inventory flyout [#225199](https://github.com/elastic/kibana/pull/225199).
- Fixes a bug where pressing Escape with an alert details flyout open from a Timeline closed the Timeline instead of the flyout [#224352](https://github.com/elastic/kibana/pull/224352).
- Fixes a bug where comma-separated `process.args` values didn't wrap properly in the alert details flyout's **Overview** tab [#223544](https://github.com/elastic/kibana/pull/223544).
- Fixes wrapping for threat indicator match event renderer [#223164](https://github.com/elastic/kibana/pull/223164).
- Fixes a z-index issue in the ES|QL query editor within Timeline [#222841](https://github.com/elastic/kibana/pull/222841).
- Fixes incorrect content displaying after tab switching in the integrations section on the **Get started** page [#222271](https://github.com/elastic/kibana/pull/222271).
- Fixes the exception flyout to show the correct "Edit rule exception" title and button label when editing an exception item [#222248](https://github.com/elastic/kibana/pull/222248).
- Retrieves active integrations from the installed integrations API [#218988](https://github.com/elastic/kibana/pull/218988).
- Updates tooltips in the gap fills table [#218926](https://github.com/elastic/kibana/pull/218926).
- Fixes AI Assistant prompt updates so UI changes reflect only successful updates [#217058](https://github.com/elastic/kibana/pull/217058).
- Fixes error callout placement on the **Engine Status** tab of the **Entity Store** page [#216228](https://github.com/elastic/kibana/pull/216228).
- Fixes alert severity ordering to display from highest severity to lowest [#215813](https://github.com/elastic/kibana/pull/215813).
- Generalizes and consolidates custom Fleet onboarding logic [#215561](https://github.com/elastic/kibana/pull/215561).
- Fixes an alert grouping re-render issue that caused infinite rendering loops when selecting a group [#215086](https://github.com/elastic/kibana/pull/215086).
- Fixes a bug in the alert details flyout's **Table** tab where fields displayed duplicate hover actions [#212316](https://github.com/elastic/kibana/pull/212316).
- Refactors conversation pagination for the Security AI Assistant [#211831](https://github.com/elastic/kibana/pull/211831).
- Fixes a bug in Elastic Defend where the `fqdn` feature flag wasn't being persisted across system or endpoint restarts.
- Fixes a crash in the Elastic Defend scan response action and suppresses the end-user popup when running background malware scans.
- Fixes an unbounded kernel non-paged memory growth issue in the Elastic Defend kernel driver during extremely high event load situations on Windows. Systems affected by this issue would slow down or become unresponsive until the triggering event load (such as network activity) subsided [#88](https://github.com/elastic/endpoint/issues/88).
- Fixes a memory growth bug in Elastic Defend on Linux when both **Collect session data** and **Capture terminal output** are enabled.
- Fixes a bug in Elastic Defend where Linux network events would have source and destination byte counts swapped.
- Fixes an issue where Elastic Defend may incorrectly set the artifact channel in policy responses, and adds `manifest_type` to policy responses.


## 9.0.8


### Features and enhancements

- Adds an Elastic Defend option to remediate orphaned state by attempting to start Elastic Agent service.


### Fixes

- Removes `null` in confirmation dialog when bulk editing index patterns for rules [#236572](https://github.com/elastic/kibana/pull/236572).
- Fixes the URL passed to detection rule actions using the `{{context.results_link}}` placeholder [#236067](https://github.com/elastic/kibana/pull/236067).
- Adds support in Elastic Defend for installing eBPF probes on Linux endpoints when taskstats is compiled out of the kernel.
- Fixes an issue in Elastic Defend where Linux network events could have source and destination bytes swapped.
- Removes `.process.thread.capabilities.permitted` and `.process.thread.capabilities.effective` from Linux network events in Elastic Defend.
- Fixes an issue in Elastic Defend where host isolation could auto-release incorrectly. Host isolation now only releases when Elastic Endpoint becomes orphaned. Intermittent Elastic Agent connectivity changes no longer alter the host isolation state.
- Improves the reliability of local Elastic Defend administrative shell commands. In rare cases, a command could fail to execute due to issue with interprocess communication.
- Fixes an issue where Elastic Defend would incorrectly calculate throughput capacity when sending documents to output.  This may have limited event throughput on extremely busy endpoints.
- Fixes an issue in Elastic Defend installation logging where only the first character of install paths (usually 'C') would be logged.


## 9.0.7


### Fixes

- Prevents users without appropriate privileges from deleting notes [#233948](https://github.com/elastic/kibana/pull/233948).
- Fixes a bug that prevented the **MITRE ATT&CK** section from appearing in the alert details flyout [#233805](https://github.com/elastic/kibana/pull/233805).
- Updates Kibana MITRE ATT&CK data to v17.1 [#231375](https://github.com/elastic/kibana/pull/231375).
- Fixes a bug where Linux capabilities were included in Elastic Endpoint network events despite being disabled.
- Makes the delivery of Elastic Endpoint command line commands more robust. In rare cases, commands could previously fail due to interprocess communication issues.


## 9.0.6


### Features and enhancements

- Improves the reliability of Elastic Defend's connection to its kernel driver. This should reduce the instances of temporary `DEGRADED` policy statuses at boot due to `connect_kernel` failures.
- Improves Elastic Defend malware scan queue efficiency by not blocking scan requests when an oplock for the file being scanned cannot be acquired.
- To help identify which parts of `elastic-endpoint.exe` are using a significant amount of CPU, Elastic Defend on Windows can now include CPU profiling data in diagnostics. To request CPU profiling data using the command line, refer to [Elastic Agent command reference](/docs/reference/fleet/agent-command-reference#_options). To request CPU profiling data using Kibana, check the **Collect additional CPU metrics** box when requesting Elastic Agent diagnostics.
- Enriches Elastic Defend macOS network connect events with `network.direction`. Possible values are `ingress` and `egress`.


### Fixes

- Prevents the ES|QL form from locking in read-only mode in the rule upgrade flyout [#231699](https://github.com/elastic/kibana/pull/231699).
- Fixes a bug in Elastic Defend where the `fqdn` feature flag was not being persisted across system/endpoint restarts.
- Fix a race condition in Elastic Defend that occasionally resulted in corrupted process command lines on Windows. This could cause incorrect values for `process.command_line`, `process.args_count` and `process.args`, leading to false positives.
- Fixes a bug in Elastic Defend where Linux endpoints would report `process.executable` as a relative, instead of absolute, path.


## 9.0.5


### Features and enhancements

- Adds the `detection_rule_upgrade_status` object to snapshot telemetry schema [#223086](https://github.com/elastic/kibana/pull/223086).
- Reduces Elastic Defend CPU when processing events from the System process on Windows.
- Allows Elastic Defend to automatically recover in some situations when it loses connectivity with Elastic Agent.
- Shortens the time it takes Elastic Defend to recover from a `DEGRADED` status caused by communication issues with Elastic Agent.
- Due to an issue in macOS, Elastic Defend would sometimes send network events without `user.name` populated. Elastic Defend will now identify these events and populate `user.name` if necessary.
- Reduces Elastic Defend CPU usage for ETW events, API events, and Behavioral Protections. In some cases, this may be a significant reduction.


### Fixes

- Fixes a bug where Security AI Assistant settings landed on the wrong page for users on the Basic license  [#229163](https://github.com/elastic/kibana/pull/229163).
- Fixes an issue in Elastic Defend performance metrics that resulted in `endpoint_uptime_percent` always being 0 for behavioral rules.
- Fixes an issue in Elastic Defend that could result in a crash if a Logstash output configuration is specified containing a certificate that cannot not be parsed.


## 9.0.4


### Features and enhancements

- Adds the `elastic_customized_total`, `elastic_noncustomized_total`, and `is_customized` fields to snapshot telemetry schema [#222370](https://github.com/elastic/kibana/pull/222370).
- Improves logging of fatal exceptions in Elastic Defend.


### Fixes

- Fixes differences between risk scoring preview and persisted risk scores [#226456](https://github.com/elastic/kibana/pull/226456).
- Updates a placeholder and validation message in the **Related Integrations** section of the rule upgrade flyout [#225775](https://github.com/elastic/kibana/pull/225775).
- Excludes machine learning rules from installation and upgrade checks for users with Basic or Essentials licenses [#224676](https://github.com/elastic/kibana/pull/224676).
- Allows using days as a time unit in rule schedules, fixing an issue where durations normalized to days were incorrectly displayed as 0 seconds [#224083](https://github.com/elastic/kibana/pull/224083).
- Fixes a bug where unmodified prebuilt rules installed before v8.18 didn't appear in the **Upgrade** table when the **Unmodified** filter was selected [#227859](https://github.com/elastic/kibana/pull/227859).
- Improves UI copy for the "bulk update with conflicts" modal [#227803](https://github.com/elastic/kibana/pull/227803).
- Strips `originId` from connectors before rule import to ensure correct ID regeneration and prevent errors when migrating connector references on rules [#223454](https://github.com/elastic/kibana/pull/223454).
- Fixes an issue that prevented the AI Assistant Knowledge Base settings UI from displaying [#225033](https://github.com/elastic/kibana/pull/225033).
- Fixes a bug in Elastic Defend where Linux network events would fail to load if IPv6 is not supported by the system.
- Fixes an issue in Elastic Defend that may result in bugchecks (BSODs) on Windows systems with a very high volume of network connections.
- Fixes an issue where Elastic Defend may incorrectly set the artifact channel in policy responses, and adds `manifest_type` to policy responses.


## 9.0.3


### Features and enhancements

- Adds `dns` event collection for macOS for Elastic Defend [#223566](https://github.com/elastic/kibana/pull/223566).
- Adds pricing information about Elastic Managed LLM in AI Assistant and Attack Discovery tours and callouts [#221566](https://github.com/elastic/kibana/pull/221566).
- Adds support for DNS events on macOS. Events can be controlled from the policy using the **DNS events** checkbox.


### Fixes

- Fixes a bug where OSS models didn’t work when streaming was ON [#224129](https://github.com/elastic/kibana/pull/224129).
- Fixes a bug where cell actions didn’t work when opening a Timeline from specific rules [#223306](https://github.com/elastic/kibana/pull/223306).
- Fixes an issue where the entity risk score feature stopped persisting risk score documents [#221937](https://github.com/elastic/kibana/pull/221937).
- Fixes a bug where the **Rules**, **Alerts**, and **Fleet** pages would stall in air-gapped environments by ensuring API requests are sent even when offline [#220510](https://github.com/elastic/kibana/pull/220510).
- Ensures the Amazon Bedrock connector respects the action proxy configuration [#224130](https://github.com/elastic/kibana/pull/224130).
- Ensures the OpenAI connector respects the action proxy configuration for all sub-actions [#219617](https://github.com/elastic/kibana/pull/219617).


## 9.0.2


### Features and enhancements

There are no new features or enhancements.

### Fixes

- Fixes a bug that caused an error message to appear when you changed entity asset criticality from the entity flyout [#219858](https://github.com/elastic/kibana/pull/219858)
- Removes the technical preview badge from the alert suppression fields for event correlation rules
- Fixes a bug in Elastic Defend 8.16.0 where Elastic Endpoint would incorrectly report some files as being `.NET`


## 9.0.1


### Features and enhancements

There are no new features or enhancements.

### Fixes

- Fixes a bug that caused installed prebuilt detection rules to upgrade to their latest available versions when you installed a new Elastic Defend integration or Elastic Agent policy [#217959](https://github.com/elastic/kibana/pull/217959)
- Prevents ES|QL rules from timing out if the rule query takes longer than five minutes to complete [#216667](https://github.com/elastic/kibana/pull/216667)
- Fixes a bug that prevented you form scrolling in modals [#218697](https://github.com/elastic/kibana/pull/218697)


## 9.0.0

<::::{NOTE}>
  All features introduced in 8.18.0 are also available in 9.0.0.
</::::{NOTE}>


### Features and enhancements

- Enables Automatic Import to accept CEL log samples [#206491](https://github.com/elastic/kibana/pull/206491)
- Enhances Automatic Import by including setup and troubleshooting documentation for each input type that's selected in the readme [#206477](https://github.com/elastic/kibana/pull/206477)
- Adds the ability to continue to the Entity Analytics dashboard when there is no data [#201363](https://github.com/elastic/kibana/pull/201363)
- Modifies the privilege-checking behavior during rule execution. Now, only read privileges of extant indices are checked during rule execution [#177658](https://github.com/elastic/kibana/pull/177658)


### Fixes

- Fixes a bug that caused the Entity Analytics Dashboard refresh button to break risk score tables [#215472](https://github.com/elastic/kibana/pull/215472)
- Fixes AI Assistant `apiConfig` set by Security getting started page [#213971](https://github.com/elastic/kibana/pull/213971)
- Limits the length of `transformID` to 36 characters [#213405](https://github.com/elastic/kibana/pull/213405)
- Ensures that table actions use standard colors [#207743](https://github.com/elastic/kibana/pull/207743)
- Fixes a bug with the **Save and continue** button on a Fleet form [#211563](https://github.com/elastic/kibana/pull/211563)