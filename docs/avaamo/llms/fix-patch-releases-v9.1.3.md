# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/fix-patch-releases-v9.1.3.md

# Fix patch releases (v9.1.3)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.1.3. The following are some of the key fixes included in this release:

1. [Language selection for file ingestion in DataSync](#language-selection-for-file-ingestion-in-datasync)
2. [Control masking with safelist patterns](#control-masking-with-safelist-patterns)
3. [Export agents with optional LLaMB skill data](#export-agents-with-optional-llamb-skill-data)
4. [Email notifications for failed jobs](#email-notifications-for-failed-jobs)

### Language selection for file ingestion in DataSync

In this release, we are introducing a new **Language selection** option for file-based content ingestion in DataSync. You can view this option during file ingestion. This enhancement improves content-processing accuracy, ensures better handling of non-English documents, and helps the system generate more reliable responses from ingested data.

You can select the language in the [Upload Files](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/files/step-2-configure-content-source-and-ingest-content/upload-files) step. Click the dropdown to display the languages configured for the agent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQbO3aeyx3LBgiYijYl8u%2FScreenshot%202025-12-12%20at%202.04.04%E2%80%AFPM.png?alt=media&#x26;token=7f2c92db-625c-4740-aba5-ae6610055767" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notes:** The language selection option is disabled when the Auto-detect toggle is enabled
{% endhint %}

You can verify the configured language after the file or document is ingested. Navigate to the individual document’s **Actions** section, click the **three-dot menu**, and select **Edit** to view the language of the ingested document content.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzxWlQVgAP4hJBY9ywUtb%2FScreenshot%2017-12-2025%20at%2012.48.png?alt=media&#x26;token=ad53fb20-4456-4cc6-9b0a-e6c1cfdc019a" alt=""><figcaption></figcaption></figure>

Refer [Files](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/files), for more information.

### Control masking with safelist patterns

In this release, we introduce `Safelist masking patterns`, which let you prevent specific words or word groups from being masked.&#x20;

For example, if you configure the system to mask all numbers in queries, responses, or both, specific terms such as RoBE-19 that contain numerals can be excluded from masking.

This enhancement provides greater control and flexibility in data masking, ensuring that essential terms remain readable while sensitive information remains protected.

To add safelist masking patterns, contact `Avaamo Support` with the list of words or patterns you want to exempt from masking.

### Export agents with optional LLaMB skill data

In this release, we introduce a new checkbox in the agent export flow that lets users include or exclude LLaMB skills in the export. By default, all applicable skills are included. Users can clear the checkbox to exclude LLaMB skills from the exported agent.

{% hint style="info" %}
**Note:** This feature is enabled by default; the checkbox is selected.
{% endhint %}

This enhancement includes two scenarios:

* **Fresh export:** See the screenshot below, where LLaMB skills are excluded by clearing the checkbox.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FsKtU1ROu8J57n1KxwVQq%2FScreenshot%202025-12-16%20at%202.04.05%E2%80%AFPM.png?alt=media&#x26;token=b995c828-979c-46ea-8894-546399ad59bb" alt=""><figcaption></figcaption></figure>

* **Repeated export:** See the screenshot below, where LLaMB skills are excluded by clearing the checkbox.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCmEumrHWyg4eY7prlPuH%2FScreenshot%202025-12-16%20at%202.11.16%E2%80%AFPM.png?alt=media&#x26;token=bd4c4ac2-f180-4434-b381-7cf1be61bf67" alt=""><figcaption></figcaption></figure>

This improvement provides greater control and improves export performance, especially for agents with large skill datasets.

Refer to [Export and import agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents), for more information.

### Email notifications for failed jobs

In this release, we introduce the **Email Notifiers** to configure email notifications for failed jobs. You can now add email addresses to receive alerts whenever a job fails for any reason.

For example, if an auto-sync is scheduled to run at a specific time and the job fails, the configured email recipients are immediately notified. This alert helps teams detect failures early, respond quickly, and minimize data sync disruptions.

**To configure email notifications:**

1. Navigate to the required job.
2. Click the three-dot menu next to the job name and select **Email Notifiers**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2kDrqglgtcmbhHI8DcLR%2FScreenshot%202025-12-16%20at%203.39.20%E2%80%AFPM.png?alt=media&#x26;token=28997ca7-ad81-4ef9-9ce3-7f7f52c8f341" alt=""><figcaption></figcaption></figure>

3. Add up to **five email addresses**, using **+ Add** to include them one by one. Click **Save** to apply the configuration.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjxsWs3oIBf8vpY9enx4i%2FScreenshot%202025-12-16%20at%203.41.08%E2%80%AFPM.png?alt=media&#x26;token=cb46fb32-5d8f-425a-afbc-e739673cbcdb" alt=""><figcaption></figcaption></figure>

Refer [Email Notifiers](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/email-notifiers), for more information.
