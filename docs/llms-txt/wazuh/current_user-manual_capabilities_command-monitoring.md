# Source: https://documentation.wazuh.com/current/user-manual/capabilities/command-monitoring/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="manual-command-monitoring"></a>

# Command monitoring

Wazuh command monitoring capability allows you to monitor the output of specific commands and treat the output as log content. Command monitoring can be used to monitor a variety of things, such as disk space utilization, load average, a change in network listeners, and running processes to ensure all important processes are running.

Command monitoring can be used to detect a variety of anomalies and threats. For example, you could use it to monitor for a change in the output of the `netstat` command, which would indicate that a new network listener has been added or removed. You could also use it to monitor for the presence of specific strings in the output of the `ps` command, which could indicate that a malicious process is running.

> ##### Contents
> 
> * [How it works](how-it-works.md)
> * [Configuration](configuration.md)
>   * [Modules](configuration.md#modules)
>   * [Configuration files](configuration.md#configuration-files)
> * [Command output analysis](command-output-analysis.md)
>   * [Decoding and rule matching](command-output-analysis.md#decoding-and-rule-matching)
>   * [Viewing the raw logs](command-output-analysis.md#viewing-the-raw-logs)
>   * [Creating a custom ruleset](command-output-analysis.md#creating-a-custom-ruleset)
> * [Use cases](use-cases/index.md)
>   * [Monitoring running processes](use-cases/monitoring-running-processes.md)
>   * [Disk space utilization](use-cases/disk-space-utilization.md)
>   * [Check if the output changed](use-cases/check-if-the-output-changed.md)
>   * [Detect USB Storage](use-cases/detect-usb-storage.md)
>   * [Load average](use-cases/load-average.md)
