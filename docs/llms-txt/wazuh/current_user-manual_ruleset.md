# Source: https://documentation.wazuh.com/current/user-manual/ruleset/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Data analysis

Wazuh provides security monitoring for various platforms, including endpoints, containers, and cloud environments. It collects log data from these platforms through multiple methods such as the Wazuh agent, agentless monitoring, syslog, and APIs. Once collected, the log data is processed by the Wazuh data analysis engine. This engine utilizes decoders to parse the log messages into useful fields and matches these fields against out-of-the-box or custom rules. The analyzed data is then utilized for threat detection, security configuration assessment, and other Wazuh capabilities.

The Wazuh data analysis engine is responsible for decoding logs, triggering rules, and generating alerts in Wazuh using the following scheme:

1. **Log collection**: Wazuh gathers logs from monitored endpoints, applications, and network devices. These logs come from various sources including operating system logs, syslog-enabled devices, cloud provider logs, and custom logs. See the [log data collection](../capabilities/log-data-collection/index.md) documentation for more information.
2. **Log decoding**: The Wazuh server analyzes the collected logs in real-time using decoders. Decoders are responsible for parsing and normalizing log data, converting raw log data into a unified and structured format, and extracting the most relevant fields that Wazuh can process effectively.
3. **Rule matching and alert visualization**: After decoding, the Wazuh server compares logs against its ruleset and triggers alerts when specific conditions are met. The alerts generated are recorded in `/var/ossec/logs/alerts/alerts.log` and `/var/ossec/logs/alerts/alerts.json` on the Wazuh server. Then, using Filebeat, the logs are forwarded and stored on the Wazuh indexer.  These alerts can then be accessed through the Wazuh dashboard **Security Events** tab, where users can conduct real-time log data queries, apply filters, and identify anomalies and potential security incidents within their environment.

While the Wazuh development team continuously contributes to improving the Wazuh ruleset, we also encourage contributions from the Wazuh community to ensure its continuous improvement. As users adopt diverse technologies tailored to their specific requirements, the constant development of new security-relevant devices and software programs worldwide becomes increasingly relevant. Wazuh recognizes this need for adaptability and offers a comprehensive range of rules and decoders within its data analysis engine. Moreover, Wazuh empowers users with the flexibility to develop custom rules and decoders in addition to over 3000 rules and decoders that come out-of-the-box. For more information about the out-of-the-box rules and decoders, refer to the [ruleset directory](https://github.com/wazuh/wazuh/tree/master/ruleset) on our GitHub repository.

## Directory layout

Below, we show the structure of the ruleset directory on the Wazuh server:

```none
/var/ossec/
        ââ etc/
        â   ââ decoders/
        |   |        ââ local_decoder.xml
        â   ââ rules/
        |         ââ local_rules.xml
        ââ ruleset/
                ââ decoders/
                ââ rules/
```

#### NOTE
You can find all the out-of-the-box rules and decoders inside the `/var/ossec/ruleset/ directory`. All files within this directory are overwritten or modified during the Wazuh upgrade process. Therefore, we do not recommend editing or adding your custom files here. Instead, we recommend making custom changes in the `/var/ossec/etc/` directory. Here, you can add your own decoders and rules files or use the default `/var/ossec/etc/decoders/local_decoder.xml` and `/var/ossec/etc/rules/local_rules.xml` files.

## GitHub repository

Visit the [Wazuh GitHub](https://github.com/wazuh/wazuh/tree/master/ruleset) repository to view the ruleset in detail.

In the repository, you will find:

- **New rules and decoders**

  We update and maintain the out-of-the-box rules and decoders to increase detection coverage and accuracy. These rules and decoders  assist in meeting regulatory compliance standards, threat detection, security configuration assessment, and mapping events and alerts to the MITRE ATT&CK framework more accurately.
- **Tools**

  We provide useful tools such as the [wazuh-logtest](../reference/tools/wazuh-logtest.md), which allows for testing rules and decoders before using them. This tool processes only one-liner (no line breaks) logs and is available in `/var/ossec/bin/wazuh-logtest` on the Wazuh server, along with various other binaries which help in managing the Wazuh server and agents. For more information you can take a look at [Wazuh tools](../reference/tools/index.md) documentation.

> ##### Content
> 
> * [Decoders](decoders/index.md)
>   * [JSON decoder](decoders/json-decoder.md)
>   * [Dynamic fields](decoders/dynamic-fields.md)
>   * [Sibling Decoders](decoders/sibling-decoders.md)
>   * [Custom decoders](decoders/custom.md)
> * [Rules](rules/index.md)
>   * [Default rules](rules/default.md)
>   * [Custom rules](rules/custom.md)
>   * [Rules classification](rules/rules-classification.md)
> * [Ruleset XML syntax](ruleset-xml-syntax/index.md)
>   * [Decoders Syntax](ruleset-xml-syntax/decoders.md)
>   * [Rules Syntax](ruleset-xml-syntax/rules.md)
>   * [Regular Expression Syntax](ruleset-xml-syntax/regex.md)
>   * [Perl-compatible Regular Expressions](ruleset-xml-syntax/pcre2.md)
> * [Testing decoders and rules](testing.md)
>   * [Configuration](testing.md#configuration)
>   * [Using the Wazuh dashboard and the command line tool](testing.md#using-the-wazuh-dashboard-and-the-command-line-tool)
>   * [Using the Wazuh server API](testing.md#using-the-wazuh-server-api)
> * [Using CDB lists](cdb-list.md)
>   * [Creating a CDB list](cdb-list.md#creating-a-cdb-list)
>   * [Adding the list in the Wazuh server configuration file](cdb-list.md#adding-the-list-in-the-wazuh-server-configuration-file)
>   * [Using the CDB list in the rules](cdb-list.md#using-the-cdb-list-in-the-rules)
> * [MITRE ATT&CK framework](mitre.md)
>   * [Intelligence](mitre.md#intelligence)
>   * [Framework](mitre.md#framework)
>   * [Dashboard](mitre.md#dashboard)
>   * [Events](mitre.md#events)
>   * [Customization](mitre.md#customization)
