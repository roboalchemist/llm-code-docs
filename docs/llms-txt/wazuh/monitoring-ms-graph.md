# Source: https://documentation.wazuh.com/current/cloud-security/azure/monitoring-ms-graph.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Monitoring Microsoft Graph services with Wazuh

The Microsoft Graph API is a comprehensive system that provides access to data across the full suite of Microsoft cloud services, including Microsoft 365, Azure, Dynamics 365, and other Microsoft cloud services. It is an endpoint for accessing structured data, insights, and rich relationships from the Microsoft Cloud ecosystem.

This section provides instructions for monitoring your organization's Microsoft Graph API resources and relationships using the Wazuh module for Microsoft Graph.

The Wazuh module for Microsoft Graph allows you to monitor the following:

- Microsoft Entra ID Protection
- Microsoft 365 Defender
- Microsoft Defender for Cloud Apps
- Microsoft Defender for Endpoint
- Microsoft Defender for Identity
- Microsoft Defender for Office 365
- Microsoft Purview eDiscovery
- Microsoft Purview Data Loss Prevention (DLP)

The data from these services is visualised using the Wazuh Microsoft API Dashboard

<a id="wazuh_image-0"></a>
![](images/cloud-security/ms-graph/ms-graph-dashboard.png)

While these are fundamental to the security resource, you can monitor many additional resources using the Microsoft Graph API. See the [Overview of Microsoft Graph](https://learn.microsoft.com/en-us/graph/overview?view=graph-rest-1.0) documentation to learn more.

#### NOTE
The security resource can be considered mature, as it has been tested with pre-made rules. However, your organization can ingest logs from other resources into your Wazuh deployment.

<a id="retrieving-content"></a>

## Retrieving content

To retrieve a set of logs from Microsoft Graph, make a `GET` request using the URL below:

```none
GET https://graph.microsoft.com/{version}/{resource}/{relationship}?{query-parameters}
```

A description of the current production version of the Microsoft Graph API can be found in the [Overview of Microsoft Graph](https://learn.microsoft.com/en-us/graph/overview?view=graph-rest-1.0).

Alternatively, the API can be tested directly in the [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer).

* [Microsoft Graph API setup](ms-graph-api-setup.md)
  * [Registering your app](ms-graph-api-setup.md#registering-your-app)
  * [Certificates & secrets](ms-graph-api-setup.md#certificates-secrets)
  * [API permissions](ms-graph-api-setup.md#api-permissions)
  * [Wazuh server or agent](ms-graph-api-setup.md#wazuh-server-or-agent)
  * [Use cases](ms-graph-api-setup.md#use-cases)
