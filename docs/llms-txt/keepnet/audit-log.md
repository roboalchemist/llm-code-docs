# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/audit-log.md

# Audit Log

This document provides details of the **Audit** **Log** functionality and how it can be used as an analytical tool to assist in your security efforts.

Auditability and accountability are crucial aspects of a cyber security solution. The **Audit** **Log** records all of the activities of **system users** and **services**. This valuable information indicating access to the system and operations performed can also be integrated with SIEM solutions via API or Web Interface.

{% hint style="warning" %}
No record on the platform can be changed or deleted by any user, regardless of role or authority.
{% endhint %}

## Audit Log Components

Go to the **Company > Audit Log** section on the left sidebar menu of the platform dashboard to view the components described below.

The components of the **Audit** **Log** page are:

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>Log Date</td><td>Date the activity occurred</td></tr><tr><td>User Name</td><td>Name of the system user or service performed the activity</td></tr><tr><td>Entity Name</td><td>The product or component where the activity occurred</td></tr><tr><td>Operation</td><td>Type of activity performed (create, delete, update, etc.)</td></tr><tr><td>Changed Set</td><td>Indication of the previous state of a deleted or updated record</td></tr><tr><td>New Value</td><td>Detailed information of a newly created record</td></tr><tr><td>IP</td><td>IP address of the user performing the activity</td></tr><tr><td>Browser User Agent</td><td>Browser information of the user performing the activity</td></tr></tbody></table>

## How to Get Audit Logs via REST API

Audit Logs can be easily obtained using API endpoints. [REST API ](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/rest-api)keys must be created prior to use with the platform.

* Log into the [Swagger](https://api.keepnetlabs.com/docs/index.html) interface
* Authenticate User ID in the Swagger interface with the Client ID and Client Secret Keys you created on the platform.
* You can now obtain Audit Logs on the platform using the endpoint below.

<mark style="color:green;">**POST**</mark> **​/api/audit-logs/search**

{% hint style="warning" %}
The most up-to-date version of the body content that should be sent during the API request is available in the Swagger interface.
{% endhint %}

Audit logs can also be transferred to your SIEM products. The API documentation used during the log transfer to some SIEM products is given below.

* [HTTP Event Collector REST API endpoints](https://docs.splunk.com/Documentation/Splunk/8.2.4/Data/HECRESTendpoints) (Splunk)
* [QRadar API Reference Guide](ftp://public.dhe.ibm.com/software/security/products/qradar/documents/7.3.0/en/b_qradar_api.pdf)

{% hint style="warning" %}
If the SIEM product you are using does not support event log transfer via API, you can download/transfer the logs through the platform's API to a file and then read the event logs from that file with your SIEM product or use the Web Interface to integrate it if the platform supports your SIEM product.
{% endhint %}

## How to Get Audit Logs via SIEM Web Integration

Audit Logs can be easily transferred in real-time by integrating your SIEM product with the platform. You can see which SIEM products are currently supported by the platform while setting up the SIEM integration.

Please see the [SIEM Integration](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/siem-integrations) document for more information.

## Audit Log Use Cases

### Use Case 1: Keeping a record of all actions taken on the platform

Some organizations bound by legislation or internal policies may be required to keep a record of every action on the platform in a separate environment.

The procedures below will allow you to record and preserve these activity entries.

* Go to the Swagger interface.
* Select a REST API from under the **AuditLog** header.
* All actions performed on the platform can be listed using a REST API and can be transferred to a different environment, if needed. (For example, the data could be downloaded to a file, which could then be saved or transferred to another platform and hosted there.)

### Use Case 2: Tracking the actions of [Incident Responder ](https://keepnetlabs.com/products/incident-responder)analysts

You can review all actions taken by analysts on the Incident Responder by following the steps below.

For example, to review the actions taken by a user named Harold Finch:

* You must first have a valid access token in order to perform an API request.
* Under the AuditLog header, use the REST API address /api/audit-log/search.
  * Use the filter in the username column to search for Harold Finch.

{% hint style="warning" %}
These values ​​may change as new parameters are added. Please always check the latest API values ​​on the Swagger documentation.
{% endhint %}

## Video Tutorial

This tutorial provides details of the **Audit** **Log** functionality and how it can be used as an analytical tool to assist in your security efforts.

{% embed url="<https://youtu.be/rUTkkHBck7Y>" %}

## FAQ

### Q: Can I delete or edit Audit Log records?

A: No. Audit Log records on the platform cannot be changed or deleted.

### Q: Which actions on the platform can I review in the Audit Log section?

A: You can review all **create**, **delete** and **update** entries.

### Q: What information can I obtain from the Audit Log records?

A: The Audit Log entries contain all of the information listed in the Audit Log Components table above.

### Q: What does the service user mean?

A: An entry identified as a service user indicates actions taken by a service application of the platform. For example, notifications made through the Phishing Reporter plug-in.

### Q: Are Audit Log records deleted periodically?

A: No. Audit Log records are never deleted.
