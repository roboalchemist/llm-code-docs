# Source: https://docs.datadoghq.com/security/guide/byoti_guide.md

---
title: Bring Your Own Threat Intelligence
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Security Guides > Bring Your Own Threat Intelligence
---

# Bring Your Own Threat Intelligence

Datadog Security supports enriching and searching [traces](https://app.datadoghq.com/security/appsec/traces) with [threat intelligence](https://docs.datadoghq.com/security/threat_intelligence) indicators of compromise stored in Datadog reference tables. [Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables) allow you to combine metadata with information already in Datadog.

## Storing indicators of compromise in reference tables{% #storing-indicators-of-compromise-in-reference-tables %}

Threat intelligence is supported in the CSV format and requires the following columns:

**CSV Structure**

| field           | data | description                                                                                                                                                               | required | example                                                                   |
| --------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------- |
| ip_address      | text | The primary key for the reference table in the IPv4 dot notation format.                                                                                                  | true     | 192.0.2.1                                                                 |
| additional_data | json | Additional data to enrich the trace.                                                                                                                                      | false    | `{"ref":"hxxp://example.org"}`                                            |
| category        | text | The threat intel [category](https://docs.datadoghq.com/security/threat_intelligence#threat-intelligence-categories). This is used by some out of the box detection rules. | true     | `residential_proxy`                                                       |
| intention       | text | The threat intel [intent](https://docs.datadoghq.com/security/threat_intelligence#threat-intelligence-intents). This is used by some out of the box detection rules.      | true     | malicious                                                                 |
| source          | json | Fields representing where the threat intelligence originates, such as your team and your team's wiki.                                                                     | true     | `{"name":"internal_security_team", "url":"https://teamwiki.example.org"}` |

The full list of supported categories and intents is available at [Threat Intelligence Facets](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-facets).

{% alert level="info" %}
JSON in a CSV requires double quoting. The following is an example CSV.
{% /alert %}

```
ip_address,additional_data,category,intention,source
192.0.2.1,"{""ref"":""hxxp://example.org""}",scanner,suspicious,"{""name"":""internal_security_team"", ""url"":""https://teamwiki.example.org""}"
192.0.2.2,"{""ref"":""hxxp://example.org""}",scanner,suspicious,"{""name"":""internal_security_team"", ""url"":""https://teamwiki.example.org""}"
192.0.2.3,"{""ref"":""hxxp://example.org""}",scanner,suspicious,"{""name"":""internal_security_team"", ""url"":""https://teamwiki.example.org""}"
```

## Uploading and enabling your own threat intel{% #uploading-and-enabling-your-own-threat-intel %}

Datadog supports creating reference tables through a manual upload, or by periodically retrieving the data from [Amazon S3, Azure storage, or Google Cloud storage](https://docs.datadoghq.com/integrations/guide/reference-tables/?tab=manualupload#create-a-reference-table).

{% alert level="info" %}
\**Usage notes:**

- If a primary key is duplicated, it is skipped and an error message about the key is displayed.
- Signals are not enriched. Enrichment only applies to traces.
- Datadog does not enrich local or private IPs.
- Only new traces (after the reference table is enabled or updated) are enriched. Old traces are not retroactively enriched.
- Enrichment happens for traces that match the IPs (supported in SIEM and App and API Protection) and domains (supported in SIEM) in the reference table.
- Manual file uploads don't auto-update. Updates occur only from cloud storage.

{% /alert %}

On a new [references table](https://app.datadoghq.com/reference-tables/create) page:

1. Name the table. The table name is referenced in AAP's **Threat Intel** config.

1. Upload a local CSV or import a CSV from a cloud storage bucket. The file is normalized and validated.

1. Preview the table schema and choose the IP address as the Primary Key.

   {% image
      source="https://datadog-docs.imgix.net/images/security/application_security/threats/threat_intel/threat_intel_ref_table.944825895f91cd787b5eecc8e64c96eb.png?auto=format"
      alt="New reference table" /%}

1. Save the table.

1. In [Threat Intel](https://app.datadoghq.com/security/configuration/threat-intel), locate the new table, and then select the toggle to enable it.

### Using cloud storage{% #using-cloud-storage %}

When the reference table is created from cloud storage, it is refreshed periodically. The entire table is *replaced*. Data is not merged.

See the related reference table documentation for:

- [Amazon S3](https://docs.datadoghq.com/integrations/guide/reference-tables/?tab=amazons3#create-a-reference-table)
- [Azure storage](https://docs.datadoghq.com/integrations/guide/reference-tables/?tab=azurestorage#create-a-reference-table)
- [Google Cloud storage](https://docs.datadoghq.com/integrations/guide/reference-tables/?tab=googlecloudstorage#create-a-reference-table)

### Troubleshooting cloud imports{% #troubleshooting-cloud-imports %}

If the reference tables are not refreshing, select the **View Change Events** link from the settings on the reference table detail page.

**View Change Events** opens a page in **Event Management** showing potential error events for the ingestion. You can also filter in **Event Management** using the reference table name.

{% alert level="info" %}
In Datadog Event Management, it can look like the data is fetched from the cloud, but it can take a few more minutes to propagate those changes to Threat Intellegence.
{% /alert %}

Other useful cloud import details to remember:

- The expected latency before updated enrichments are available when a source is uploaded or updated is 10 to 30 minutes.
- How to know when the updates are applied: The changes are visible in the reference table or in the spans. Select the **View Change Events** link from settings on the reference table detail page to see the related events.
- The update replaces the *entire table* with the new data.
- In case of a duplicated primary key, the rows with the duplicated key are not written, and an error is shown in the reference table detail page.

## Filter traces by joining the list with a Reference Table{% #filter-traces-by-joining-the-list-with-a-reference-table %}

You can filter AAP traces in Datadog by joining a trace table with a Reference Table.

To join a Reference Table with a trace query, you combine rows from the Datadog trace table and a Reference Table based on a related column between them. The traces query returns only those traces where there is a match in both tables.

Using a join with a Reference Table enables you to evaluate impact before enrichment by searching for historical matches with existing traces.

You can use any fields, not just IP addresses. For example, by associating security traces with specific URLs from a reference table, you can identify which parts of your application are being targeted by attacks. This can help pinpoint vulnerabilities or high-risk areas within the application.

Examples:

- Investigation and incident response. You can upload and join using IPs or other fields from attacks and see the traffic related to that incident.
- By using security traces with the IP addresses from a Reference Table, such as associating IP addresses with geographic locations or organizational details, security teams can gain better context around attack attempts. This can help in understanding the origin and potential motivation behind the attacks.

To join a trace with a Reference Table:

1. Upload the Reference Table you want to use as described in Uploading and enabling your own threat intel.
1. To join a trace with a Reference Table, in [Traces](https://app.datadoghq.com/security/appsec/traces), select **Add**, and then select **Join with Reference Table**.
1. In **Inner join with reference table**, select the Reference Table to use.
1. In **where field**, select the Datadog traces field to use for the join.
1. In **column**, select the Reference Table field to use for the join.

## Enriching traces for detection rules{% #enriching-traces-for-detection-rules %}

Enriching traces includes the threat intelligence attributes in AAP traces when the indicator of compromise matches the value of the `http.client_ip` key in the AAP trace. This enables searching for traces with threat intelligence matches using existing facets and using threat intelligence with detection rules.
