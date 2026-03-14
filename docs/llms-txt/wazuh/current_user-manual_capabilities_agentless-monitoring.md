# Source: https://documentation.wazuh.com/current/user-manual/capabilities/agentless-monitoring/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="manual-agentless"></a>

# Agentless monitoring

The Wazuh server analyzes the data it receives from the Wazuh agents to monitor, detect, and trigger alerts for security events and incidents on endpoints. However, some endpoints may have limitations that prevent the installation of the Wazuh agent. Wazuh solves this problem by using the agentless monitoring capability.

Agentless monitoring refers to a type of endpoint monitoring that does not require the installation of an agent or software. This approach uses existing protocols to access and gather information from the monitored endpoint.

The Wazuh agentless monitoring capability uses the SSH (Secure Shell) protocol to collect and transfer events from endpoints to the Wazuh server. The supported platforms include routers, firewalls, switches, and Linux/BSD systems. It allows endpoints with software installation restrictions to meet security and compliance requirements.

> ##### Contents
> 
> * [How it works](how-it-works.md)
>   * [Monitor files, directories, or configuration of an endpoint](how-it-works.md#monitor-files-directories-or-configuration-of-an-endpoint)
>   * [Run commands on an endpoint](how-it-works.md#run-commands-on-an-endpoint)
> * [Connection](connection.md)
>   * [Add an endpoint](connection.md#add-an-endpoint)
>   * [List connected endpoints](connection.md#list-connected-endpoints)
>   * [Remove agentless configuration](connection.md#remove-agentless-configuration)
> * [Configuration](agentless-configuration.md)
>   * [Supported attributes](agentless-configuration.md#supported-attributes)
>   * [Monitoring files, directories, or configuration settings on an endpoint](agentless-configuration.md#monitoring-files-directories-or-configuration-settings-on-an-endpoint)
>   * [Running commands on an endpoint](agentless-configuration.md#running-commands-on-an-endpoint)
>   * [Checking the agentless monitoring setup](agentless-configuration.md#checking-the-agentless-monitoring-setup)
> * [Visualization](visualization.md)
> * [Use cases](use-cases.md)
>   * [Monitoring the output of a command on an endpoint](use-cases.md#monitoring-the-output-of-a-command-on-an-endpoint)
>   * [Monitor files and directories on an endpoint](use-cases.md#monitor-files-and-directories-on-an-endpoint)
