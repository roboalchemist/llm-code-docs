# Source: https://docs.datadoghq.com/account_management/audit_trail/forwarding_audit_events.md

---
title: Forwarding Audit Events to Custom Destinations
description: >-
  Forward audit events from Datadog to custom destinations like Splunk,
  Elasticsearch, and HTTP endpoints for compliance and security monitoring.
breadcrumbs: >-
  Docs > Account Management > Datadog Audit Trail > Forwarding Audit Events to
  Custom Destinations
---

# Forwarding Audit Events to Custom Destinations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="danger" %}
Audit Event Forwarding is in Preview.
{% /alert %}

## Overview{% #overview %}

Audit Event Forwarding allows you to send audit events from Datadog to custom destinations like Splunk, Elasticsearch, and HTTP endpoints. Audit events are forwarded in JSON format. You can add up to three destinations for each Datadog org.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/audit_logs/audit_events_forwarding.e0020de4485e16c36afb054c1d721704.png?auto=format"
   alt="The Custom Destinations section showing an active Login-Event-to-SIEM destination with 10.4 MB of estimated audit events volume in the last 24 hours and @action:login as query to filter." /%}

**Note**: Only Datadog users with the `audit_trail_write` permission can create, edit, or delete custom destinations for forwarding audit events.

## Set up audit event forwarding to custom destinations{% #set-up-audit-event-forwarding-to-custom-destinations %}

1. Add webhook IPs from the [IP ranges list](https://ip-ranges.datadoghq.com/) to the allowlist if necessary.
1. Navigate to [Audit Trail Settings](https://app.datadoghq.com/organization-settings/audit-trail-settings).
1. Click **Add Destination** in the **Audit Event Forwarding** section.
1. Enter the query to filter your audit events for forwarding. For example, add `@action:login` as the query to filter if you only want to forward login events to your SIEM or custom destination. See [Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/) for more information.
1. Select the **Destination Type**.

{% tab title="HTTP" %}
Enter a name for the destination.In the **Define endpoint** field, enter the endpoint to which you want to send the logs. The endpoint must start with `https://`.
- For example, if you want to send logs to Sumo Logic, follow their [Configure HTTP Source for Logs and Metrics documentation](https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/logs-metrics/) to get the HTTP Source Address URL to send data to their collector. Enter the HTTP Source Address URL in the **Define endpoint** field.
In the **Configure Authentication** section, select one of the following authentication types and provide the relevant details:
- Basic Authentication: Provide the username and password for the account to which you want to send logs.
- Request Header: Provide the header name and value. For example, if you use the Authorization header and the username for the account to which you want to send logs is `myaccount` and the password is `mypassword`:
  - Enter `Authorization` for the **Header Name**.
  - The header value is in the format of `Basic username:password`, where `username:password` is encoded in base64. For this example, the header value is `Basic bXlhY2NvdW50Om15cGFzc3dvcmQ=`.
Click **Save**.
{% /tab %}

{% tab title="Splunk" %}
Enter a name for the destination.In the **Configure Destination** section, enter the endpoint to which you want to send the logs. The endpoint must start with `https://`. For example, enter `https://<your_account>.splunkcloud.com:8088`. **Note**: `/services/collector/event` is automatically appended to the endpoint.In the **Configure Authentication** section, enter the Splunk HEC token. See [Set up and use HTTP Event Collector](https://docs.splunk.com/Documentation/Splunk/9.0.1/Data/UsetheHTTPEventCollector) for more information about the Splunk HEC token.Click **Save**.
**Note**: The [indexer acknowledgment](https://docs.splunk.com/Documentation/Splunk/9.0.3/Data/AboutHECIDXAck) needs to be disabled.
{% /tab %}

{% tab title="Elasticsearch" %}
Enter a name for the destination.In the **Configure Destination** section, enter the following details:
1. The endpoint to which you want to send the logs. The endpoint must start with `https://`. An example endpoint for Elasticsearch: `https://<your_account>.us-central1.gcp.cloud.es.io`.
1. The name of the destination index where you want to send the logs.
1. Optionally, select the index rotation for how often you want to create a new index: `No Rotation`, `Every Hour`, `Every Day`, `Every Week`, or `Every Month`. The default is `No Rotation`.
In the **Configure Authentication** section, enter the username and password for your Elasticsearch account.Click **Save**.
{% /tab %}

{% tab title="Microsoft Sentinel" %}

{% alert level="info" %}
Log forwarding to Microsoft Sentinel is in Preview.
{% /alert %}
Enter a name for the destination.Authentication for the Microsoft Sentinel Forwarder requires configuring an App Registration through the Datadog Azure Integration.In the **Configure Destination** section, enter the following details:
| Setting                     | Description                                                                                                                                                                                                                                   | Example                                                 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Logs Ingestion Endpoint** | Enter the endpoint on the Data Collection Endpoint (DCE) where logs are sent. This is labeled "Logs Ingestion" on the DCE Overview page.                                                                                                      | `https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com` |
| **Immutable ID**            | Specify the immutable ID of the Data Collection Rule (DCR) where logging routes are defined, as found on the DCR Overview page as "Immutable Id". **Note**: Ensure the Monitoring Metrics Publisher role is assigned in the DCR IAM settings. | `dcr-000a00a000a00000a000000aa000a0aa`                  |
| **Stream Declaration Name** | Provide the name of the target Stream Declaration found in the Resource JSON of the DCR under `streamDeclarations`.                                                                                                                           | `Custom-MyTable`                                        |

{% /tab %}

## Further Reading{% #further-reading %}

- [Learn more about Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/)
