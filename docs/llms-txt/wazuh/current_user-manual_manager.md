# Source: https://documentation.wazuh.com/current/user-manual/manager/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Wazuh server

The Wazuh server is the Wazuh central component that analyzes data it receives from agents, external APIs, and network devices. It analyzes the received data by correlating and matching it against a predefined ruleset to generate alerts for security monitoring and management.

The Wazuh server comprises two main components; the [Wazuh manager](wazuh-manager.md) and [Filebeat](indexer-integration.md#indexer-integration-filebeat). The Wazuh manager is responsible for data analysis and alerting, while Filebeat forwards the analyzed data to the [Wazuh indexer](indexer-integration.md#indexer-integration-wazuh-indexer). Refer to the [Wazuh server installation](../../installation-guide/wazuh-server/index.md) documentation for information on how to install and set it up.

> ##### Contents
> 
> * [Wazuh manager](wazuh-manager.md)
>   * [Agent enrollment service](wazuh-manager.md#agent-enrollment-service)
>   * [Agent connection service](wazuh-manager.md#agent-connection-service)
>   * [Analysis engine](wazuh-manager.md#analysis-engine)
> * [Indexer integration](indexer-integration.md)
>   * [Wazuh indexer](indexer-integration.md#wazuh-indexer)
>   * [Third-party indexers](indexer-integration.md#third-party-indexers)
> * [Alert management](alert-management.md)
>   * [Alert threshold](alert-management.md#alert-threshold)
>   * [Forwarding alerts](alert-management.md#forwarding-alerts)
> * [Event logging](event-logging.md)
>   * [Log compression and rotation](event-logging.md#log-compression-and-rotation)
>   * [Archiving event logs](event-logging.md#archiving-event-logs)
> * [External API integration](integration-with-external-apis.md)
>   * [Configuration](integration-with-external-apis.md#configuration)
>   * [Slack](integration-with-external-apis.md#slack)
>   * [PagerDuty](integration-with-external-apis.md#pagerduty)
>   * [VirusTotal](integration-with-external-apis.md#virustotal)
>   * [Shuffle](integration-with-external-apis.md#shuffle)
>   * [Maltiverse](integration-with-external-apis.md#maltiverse)
>   * [Custom integration](integration-with-external-apis.md#custom-integration)
> * [Queuing mechanisms](wazuh-server-queue.md)
>   * [Wazuh agent communication queue (queue_rd)](wazuh-server-queue.md#wazuh-agent-communication-queue-queue-rd)
>   * [Wazuh analysis engine queue (queue_and)](wazuh-server-queue.md#wazuh-analysis-engine-queue-queue-and)
>   * [Wazuh agent queue (queue_ad)](wazuh-server-queue.md#wazuh-agent-queue-queue-ad)
>   * [Wazuh queue decoder and rules](wazuh-server-queue.md#wazuh-queue-decoder-and-rules)
