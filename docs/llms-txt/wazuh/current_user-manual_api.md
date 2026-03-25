# Source: https://documentation.wazuh.com/current/user-manual/api/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Wazuh server API

The Wazuh server API is an open source RESTful API that allows interaction with the Wazuh manager from a web browser, a command-line tool such as cURL, or any script or program capable of making web requests. The Wazuh dashboard relies on the Wazuh server API to remotely manage the Wazuh server infrastructure. You can utilize the Wazuh server API to perform common tasks such as adding agents, restarting the manager(s) or agent(s), or looking up details about File Integrity Monitoring (FIM).

Here is a list of the Wazuh server API capabilities:

- Wazuh agent management
- Wazuh manager control and overview
- Cluster control and overview
- File integrity monitoring control and search
- MITRE ATT&CK overview
- Ruleset information
- Testing and verification of rules and decoders
- Syscollector information
- Role-Based Access Control (RBAC)
- API management (HTTPS, configuration)
- Users management
- Statistical information
- Error handling
- Query remote configuration

Refer to the [Wazuh server API reference](reference.md) for details about all the Wazuh server API endpoints. Also consider [use cases](use-cases.md) for example usage of the Wazuh server API.

> ##### Contents
> 
> * [Getting started](getting-started.md)
>   * [Starting and stopping the Wazuh server API](getting-started.md#starting-and-stopping-the-wazuh-server-api)
>   * [Using the Wazuh server API via the Wazuh dashboard](getting-started.md#using-the-wazuh-server-api-via-the-wazuh-dashboard)
>   * [Logging into the Wazuh server API via command line](getting-started.md#logging-into-the-wazuh-server-api-via-command-line)
>   * [Logging into the Wazuh server API via scripts](getting-started.md#logging-into-the-wazuh-server-api-via-scripts)
>   * [Understanding the Wazuh server API request and response](getting-started.md#understanding-the-wazuh-server-api-request-and-response)
>   * [Practical examples of Wazuh server API usage](getting-started.md#practical-examples-of-wazuh-server-api-usage)
> * [Configuration](configuration.md)
>   * [Wazuh server API configuration file](configuration.md#wazuh-server-api-configuration-file)
>   * [API configuration options](configuration.md#api-configuration-options)
>   * [Wazuh server API security configuration](configuration.md#wazuh-server-api-security-configuration)
>   * [Configuration endpoints](configuration.md#configuration-endpoints)
>   * [SSL certificate](configuration.md#ssl-certificate)
> * [Securing the Wazuh server API](securing-api.md)
>   * [Recommended changes to secure the Wazuh server API](securing-api.md#recommended-changes-to-secure-the-wazuh-server-api)
> * [Role-Based Access Control](rbac/index.md)
>   * [How it works](rbac/how-it-works.md)
>   * [Authorization Context](rbac/auth-context.md)
>   * [RBAC Reference](rbac/reference.md)
> * [Filtering data using Wazuh Query Language (WQL)](queries.md)
>   * [Examples](queries.md#examples)
> * [Wazuh server API use cases](use-cases.md)
>   * [Using the Wazuh dashboard](use-cases.md#using-the-wazuh-dashboard)
>   * [Using an authenticated terminal](use-cases.md#using-an-authenticated-terminal)
> * [Reference](reference.md)
