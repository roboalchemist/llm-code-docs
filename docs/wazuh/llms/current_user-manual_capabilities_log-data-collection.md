# Source: https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="manual-log-analysis"></a>

# Log data collection

Log data collection involves gathering and consolidating logs from different log sources within a network. Log data collection helps security teams to meet regulatory compliance, detect and remediate threats, and identify application errors and other security issues.

Wazuh collects, analyzes, and stores logs from endpoints, network devices, and applications. The Wazuh agent, running on a monitored endpoint, collects and forwards system and application logs to the Wazuh server for analysis. Additionally, you can send log messages to the Wazuh server via syslog, or third-party API integrations.

> ##### Contents
> 
> * [How it works](how-it-works.md)
> * [Configuration for monitoring log files](monitoring-log-files.md)
>   * [Monitoring basic log files](monitoring-log-files.md#monitoring-basic-log-files)
>   * [Monitoring date-based log files](monitoring-log-files.md#monitoring-date-based-log-files)
>   * [Monitoring log files using wildcard patterns](monitoring-log-files.md#monitoring-log-files-using-wildcard-patterns)
>   * [Monitoring log files with environment variables](monitoring-log-files.md#monitoring-log-files-with-environment-variables)
> * [Configuring syslog on the Wazuh server](syslog.md)
> * [Journald log collection](journald.md)
>   * [How this works](journald.md#how-this-works)
>   * [Configuration](journald.md#configuration)
>   * [Use cases](journald.md#use-cases)
> * [Using multiple socket outputs](multiple-socket-outputs.md)
> * [Configuring log collection for different operating systems](configuration.md)
>   * [Windows](configuration.md#windows)
>   * [Linux](configuration.md#linux)
>   * [macOS](configuration.md#macos)
> * [Log data analysis](log-data-analysis.md)
>   * [Pre-decoding](log-data-analysis.md#pre-decoding)
>   * [Decoding](log-data-analysis.md#decoding)
>   * [Rule matching](log-data-analysis.md#rule-matching)
> * [Use cases](use-cases.md)
>   * [Forwarding Linux logs using rsyslog](use-cases.md#forwarding-linux-logs-using-rsyslog)
>   * [Detecting the installation of applications on Windows](use-cases.md#detecting-the-installation-of-applications-on-windows)
>   * [Monitoring PowerShell activity](use-cases.md#monitoring-powershell-activity)
