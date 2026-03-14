# Source: https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="manual-file-integrity"></a>

# File integrity monitoring

File Integrity Monitoring (FIM) is a security process used to monitor the integrity of system and application files. FIM is an important security defense layer for any organization monitoring sensitive assets. It provides protection for sensitive data, application, and device files by monitoring, routinely scanning, and verifying their integrity. It helps organizations detect changes to critical files on their systems which reduces the risk of data being stolen or compromised. This process can save time and money in lost productivity, lost revenue, reputation damage, and legal and regulatory compliance penalties.

Wazuh has a built-in capability for file integrity monitoring. The Wazuh FIM module monitors files and directories and triggers an alert when a user or process creates, modifies, and deletes monitored files. It runs a baseline scan, storing the cryptographic checksum and other attributes of the monitored files. When a user or process changes a file, the module compares its checksum and attributes to the baseline. It triggers an alert if it finds a mismatch. The FIM module performs real-time and scheduled scans depending on the FIM configuration for agents and manager.

Some benefits of the Wazuh FIM capability include change management, threat detection and response, and regulatory compliance as follows.

<h2>Change management</h2>

The Wazuh FIM capability is an essential tool for verifying that the change management processes are working correctly. This Wazuh capability allows you to examine files to see if they change, how and when they change, and who or what changes them. The Wazuh FIM module compares the baseline information against the information of the latest version of the file. This comparison provides visibility into alterations and updates of critical files. For example, you can use this to detect incorrect updates to applications or unauthorized changes made to configuration files.

<h2>Threat detection and response</h2>

You can combine FIM with other Wazuh capabilities for threat detection and response. The FIM capability monitors file integrity, detects permission changes, and monitors user and file activities. It provides detailed alerts for quick responses to detected threats.

<h2>Regulatory compliance</h2>

The FIM capability helps organizations meet regulatory requirements for data security, privacy, and data retention. Monitoring critical files for changes is an important requirement for regulations such as PCI DSS, HIPAA, and GDPR.

> ##### Contents
> 
> * [How it works](how-it-works.md)
> * [How to configure the FIM module](how-to-configure-fim.md)
> * [Interpreting the FIM module analysis](interpreting-fim-module-analysis.md)
>   * [Inventory](interpreting-fim-module-analysis.md#inventory)
>   * [Dashboard](interpreting-fim-module-analysis.md#dashboard)
>   * [Events](interpreting-fim-module-analysis.md#events)
> * [Basic settings](basic-settings.md)
>   * [Real-time monitoring](basic-settings.md#real-time-monitoring)
>   * [Record file attributes](basic-settings.md#record-file-attributes)
>   * [Scheduled scans](basic-settings.md#scheduled-scans)
>   * [Report changes in file values](basic-settings.md#report-changes-in-file-values)
>   * [Adding exclusions](basic-settings.md#adding-exclusions)
> * [Creating custom FIM rules](creating-custom-fim-rules.md)
>   * [Mapping FIM fields to Wazuh alerts](creating-custom-fim-rules.md#mapping-fim-fields-to-wazuh-alerts)
>   * [Custom FIM rules examples](creating-custom-fim-rules.md#custom-fim-rules-examples)
> * [Advanced settings](advanced-settings.md)
>   * [Who-data monitoring](advanced-settings.md#who-data-monitoring)
>   * [Windows installation directory monitoring](advanced-settings.md#windows-installation-directory-monitoring)
>   * [Recursion level](advanced-settings.md#recursion-level)
>   * [Process priority](advanced-settings.md#process-priority)
>   * [Database storage](advanced-settings.md#database-storage)
>   * [Synchronization](advanced-settings.md#synchronization)
> * [Use cases](use-cases/index.md)
>   * [Detecting malware persistence technique](use-cases/detecting-malware-persistence-technique.md)
>   * [Detecting account manipulation](use-cases/detecting-account-manipulation.md)
>   * [Monitoring files at specific intervals](use-cases/monitoring-files-at-specific-intervals.md)
>   * [Reporting file changes](use-cases/reporting-file-changes.md)
>   * [Monitoring configuration changes](use-cases/monitoring-configuration-changes.md)
> * [Windows Registry monitoring](windows-registry-monitoring.md)
>   * [How it works](windows-registry-monitoring.md#how-it-works)
>   * [Configuration](windows-registry-monitoring.md#configuration)
>   * [Use case: Detect malware persistence in Windows Registry](windows-registry-monitoring.md#use-case-detect-malware-persistence-in-windows-registry)
