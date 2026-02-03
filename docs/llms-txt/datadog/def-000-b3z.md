# Source: https://docs.datadoghq.com/security/default_rules/def-000-b3z.md

---
title: >-
  Blob Service storage logging should be enabled for 'Read', 'Write', and
  'Delete' requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Blob Service storage logging should be
  enabled for 'Read', 'Write', and 'Delete' requests
---

# Blob Service storage logging should be enabled for 'Read', 'Write', and 'Delete' requests
 
## Description{% #description %}

Storage Logging operates on the server-side, logging details of both successful and failed requests in the storage account, including timing, authentication, concurrency information, and the sizes of the request and response messages. The logs provide insights into all read, write, and delete operations against the blobs. Additionally, Storage Analytics logs capture detailed information about requests to a storage service to monitor every individual request for increased security or diagnostics. However, due to its potential impact on costs, Storage Analytics logging is not automatically enabled and requires careful consideration of usage and projected costs before activation.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Open Azure portal at [https://portal.azure.com/](https://portal.azure.com/)
1. Navigate to your existing blob storage account.
1. Inside your blob storage account, select **Settings**, then choose **Diagnostic settings**.
1. Click on **Add diagnostic setting**.
1. Under the **Blob Service** section, ensure **Read**, **Write**, and **Delete** boxes are checked.
1. You can choose to save them to a **Storage Account**, stream them to an **Event Hub**, or send them to **Log Analytics**.
1. Click **Save** at the top of the page.
