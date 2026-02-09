# Source: https://docs.datadoghq.com/security/default_rules/def-000-ovj.md

---
title: >-
  Table Service storage logging should be enabled for 'Read', 'Write', and
  'Delete' requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Table Service storage logging should be
  enabled for 'Read', 'Write', and 'Delete' requests
---

# Table Service storage logging should be enabled for 'Read', 'Write', and 'Delete' requests
 
## Description{% #description %}

Storage Logging occurs server-side, recording details of both successful and failed requests in the storage account, and giving users insights into read, write, and delete operations against the tables. The logs contain detailed information about individual requests such as timing, authentication, concurrency information, and the sizes of request and response messages. Storage Analytics logs offer additional data about successful and failed requests to a storage service, aiding in monitoring each request for better security and diagnostics. However, due to its potential impact on storage costs, Storage Analytics logging is not automatically enabled and requires careful consideration of usage and projected costs before activation.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Open Azure portal at [https://portal.azure.com/](https://portal.azure.com/)
1. Navigate to your existing table storage account.
1. Inside your table storage account, select **Settings**, then choose **Diagnostic settings**.
1. Click on **Add diagnostic setting**.
1. Under the **Blob Service** section, ensure **Read**, **Write**, and **Delete** boxes are checked.
1. You can choose to save them to a **Storage Account**, stream them to an **Event Hub**, or send them to **Log Analytics**.
1. Click **Save** at the top of the page.
