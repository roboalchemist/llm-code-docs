# Source: https://documentation.wazuh.com/current/user-manual/indexer-api/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Wazuh indexer API

The Wazuh indexer API is an open source RESTful API that allows interaction with the Wazuh indexer from the Wazuh dashboard, a command-line tool such as cURL, or any script or program capable of making web requests. The Wazuh indexer API provides endpoints for managing and querying data within the Wazuh indexer. Using this API, users can perform various operations, such as searching logs, managing indexes, and handling data related to security alerts and compliance reports. The Wazuh indexer API is designed to support automation and scalability, offering a flexible approach to accessing and analyzing data for security insights, obtaining operational metrics, and reporting.

Here is a list of some of the Wazuh indexer API capabilities:

- Index management
- User management
- Managing and searching through indexes
- Log ingestion
- Manage notifications
- Manage nodes in a single or multi-node cluster
- Snapshot and repository management
- Statistical information collection
- Error handling
- Configuration management
- Index lifecycle management

Refer to the [Wazuh indexer API reference](reference.md) for details about all the Wazuh indexer API endpoints. Take a look at the [Wazuh indexer API use cases](use-case.md) for practical examples of how the Wazuh indexer API can be utilized.

> ##### Contents
> 
> * [Getting started](getting-started.md)
>   * [Starting and stopping the Wazuh indexer API](getting-started.md#starting-and-stopping-the-wazuh-indexer-api)
>   * [Logging into the Wazuh indexer API](getting-started.md#logging-into-the-wazuh-indexer-api)
>     * [HTTP basic authentication](getting-started.md#http-basic-authentication)
>     * [JSON Web Token (JWT)](getting-started.md#json-web-token-jwt)
>   * [Using the Wazuh indexer API via the Wazuh dashboard](getting-started.md#using-the-wazuh-indexer-api-via-the-wazuh-dashboard)
>   * [Using the Wazuh indexer API via the command line](getting-started.md#using-the-wazuh-indexer-api-via-the-command-line)
>   * [Using the Wazuh indexer API via a script](getting-started.md#using-the-wazuh-indexer-api-via-a-script)
>     * [Using Python](getting-started.md#using-python)
>     * [Using Bash](getting-started.md#using-bash)
>   * [Understanding the Wazuh indexer API request and response](getting-started.md#understanding-the-wazuh-indexer-api-request-and-response)
>   * [Practical examples of Wazuh indexer API methods](getting-started.md#practical-examples-of-wazuh-indexer-api-methods)
>     * [GET](getting-started.md#get)
>     * [PUT](getting-started.md#put)
>     * [DELETE](getting-started.md#delete)
>   * [Practical examples of Wazuh indexer API access tools](getting-started.md#practical-examples-of-wazuh-indexer-api-access-tools)
>     * [cURL](getting-started.md#curl)
>     * [Python](getting-started.md#python)
>     * [Bash](getting-started.md#bash)
> * [Configuration](configuration.md)
>   * [Wazuh indexer API configuration file](configuration.md#wazuh-indexer-api-configuration-file)
>   * [Wazuh indexer API configuration options](configuration.md#wazuh-indexer-api-configuration-options)
>     * [network](configuration.md#network)
>     * [http](configuration.md#http)
>     * [http.cors](configuration.md#http-cors)
>     * [logger](configuration.md#logger)
>     * [path](configuration.md#path)
>     * [search](configuration.md#search)
> * [Securing the Wazuh indexer API](securing-indexer-api.md)
>   * [Recommended changes to secure the Wazuh indexer API](securing-indexer-api.md#recommended-changes-to-secure-the-wazuh-indexer-api)
>     * [Change the default password for the administrative users](securing-indexer-api.md#change-the-default-password-for-the-administrative-users)
>     * [Restrict network access](securing-indexer-api.md#restrict-network-access)
>     * [Limit API exposure](securing-indexer-api.md#limit-api-exposure)
>     * [Enforce rate limiting](securing-indexer-api.md#enforce-rate-limiting)
> * [Use cases](use-case.md)
>   * [Exploring alerts](use-case.md#exploring-alerts)
>   * [Getting information about the Wazuh indexer configuration](use-case.md#getting-information-about-the-wazuh-indexer-configuration)
>   * [Run a report on cluster health and statistics](use-case.md#run-a-report-on-cluster-health-and-statistics)
>   * [Query vulnerability data](use-case.md#query-vulnerability-data)
>   * [Threat hunting](use-case.md#threat-hunting)
>   * [Conclusion](use-case.md#conclusion)
> * [Reference](reference.md)
