# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions.md

# Source: https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/common-actions.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/common-actions.md

# Common actions

## Auto sync

The `Auto sync` feature allows you to synchronize articles automatically at regular time intervals. Once configured, the system checks for updates made to the articles during that interval and automatically updates them in the existing job. This ensures that the ingested articles remain up to date, so the responses generated include the most recent information.

{% hint style="info" %}
**Note:** This option is available only for `SharePoint`, `ServiceNow`, and `Website` connectors.
{% endhint %}

**Setting up Auto sync**

1. Navigate to the list of jobs and select the job you created.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fh9jSNIG2cESw160u9uVL%2FScreenshot%202025-10-03%20at%203.09.06%E2%80%AFPM.png?alt=media&#x26;token=c6664871-c0a9-49a9-b72d-338862075f58" alt=""><figcaption></figcaption></figure>

3. Access the extended menu by clicking the three dots next to the job name. Select the `Auto Sync` option.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtqzDHaETzLq18JtG5r0J%2FScreenshot%202025-10-03%20at%203.06.57%E2%80%AFPM.png?alt=media&#x26;token=73ef7be0-4195-4dcf-97c0-8e23297220ea" alt=""><figcaption></figcaption></figure>

4. On the configuration page that opens, enter the required details. Click **Submit** to enable Auto sync for the selected job.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8OsHtTpFWSYwj0STiMx3%2FScreenshot%202025-10-03%20at%203.13.27%E2%80%AFPM.png?alt=media&#x26;token=daa99430-67cd-4f18-a7a3-1dd17b776241" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="148.15234375">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Timezone</strong></td><td>Select the time zone from the available options in the dropdown list.</td></tr><tr><td><strong>Start time</strong></td><td>Select the date and time when Auto sync should start.</td></tr><tr><td><strong>Repeat</strong></td><td>Select the repeating pattern for Auto sync. Options include <code>Daily</code>, <code>Weekly</code>, <code>Monthly</code>, or <code>Minutely</code>.</td></tr><tr><td><strong>Repeat on</strong></td><td>Select the specific day(s) of the week when Auto sync should run.</td></tr><tr><td><strong>Ends</strong></td><td>Configure when Auto sync should stop. <br>Options include: <br>1) Specify an end date, or <br>2) End after a certain number of occurrences.</td></tr></tbody></table>

## Manual Sync

This option allows you to manually sync all ingested articles immediately after updating them. Even if Auto sync is set up, you can manually sync articles at any time. This gives users the flexibility to update and sync content to the created job whenever needed.

{% hint style="info" %}
**Note:** This option is available only for `SharePoint`, `ServiceNow`, and `Website` connectors.
{% endhint %}

**Setting up Manual sync**

1. Navigate to the list of jobs and select the job you created.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fh9jSNIG2cESw160u9uVL%2FScreenshot%202025-10-03%20at%203.09.06%E2%80%AFPM.png?alt=media&#x26;token=c6664871-c0a9-49a9-b72d-338862075f58" alt=""><figcaption></figcaption></figure>

3. Access the extended menu by clicking the three dots next to the job name. Select the `Sync Now` option.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtqzDHaETzLq18JtG5r0J%2FScreenshot%202025-10-03%20at%203.06.57%E2%80%AFPM.png?alt=media&#x26;token=73ef7be0-4195-4dcf-97c0-8e23297220ea" alt=""><figcaption></figcaption></figure>

4. It synchronizes all updated content from your database to the created job immediately.

## View job details

You can view the details of a job after it is created.

Access the extended menu by clicking the three dots next to the job name. Select the `View job details` option. You can view the following details.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJxrJlTnuwvUKr6aAvjqH%2FScreenshot%2023-10-2025%20at%2011.40.png?alt=media&#x26;token=1a58169c-44be-4830-bff1-ea1e19e05609" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="188.0078125">Option</th><th>Description</th><th>Content Sources</th></tr></thead><tbody><tr><td><strong>Job ID</strong></td><td>A unique identifier assigned to the job for tracking and reference purposes.</td><td>SharePoint, ServiceNow, Website, Files</td></tr><tr><td><strong>Initiated by</strong></td><td>The name or ID of the user who started the job.</td><td>SharePoint, ServiceNow, Website, Files</td></tr><tr><td><strong>Initiated at</strong></td><td>The date and time when the job was started.</td><td>SharePoint, ServiceNow, Website, Files</td></tr><tr><td><strong>Client ID</strong></td><td>Unique identifier of the client, provided by Admin</td><td>SharePoint</td></tr><tr><td><strong>Client Secret</strong></td><td>Password provided by Admin</td><td>SharePoint</td></tr><tr><td><strong>Tenant</strong></td><td>Name of the tenant, provided by Admin</td><td>SharePoint</td></tr><tr><td><strong>Tenant ID</strong></td><td>Unique identifier of the tenant, provided by Admin</td><td>SharePoint</td></tr><tr><td><strong>User Name</strong></td><td>The user name of the ServiceNow, provided by the Admin</td><td>ServiceNow</td></tr><tr><td><strong>Password</strong></td><td>Password of the ServiceNow, provided by the Admin</td><td>ServiceNow</td></tr><tr><td><strong>Source URL</strong></td><td>URL of the ServiceNow, provided by the Admin</td><td>ServiceNow</td></tr><tr><td><strong>ServiceNow Query URL</strong></td><td>Query URL that contains information about articles/documents ingested</td><td>ServiceNow</td></tr></tbody></table>

## Delete job

You can delete the job after it is created. If you no longer need the job, or it is duplicated by another job, you can delete it, which removes all articles ingested under this job ID.

Access the extended menu by clicking the three dots next to the job name. Select the `Delete job` option.&#x20;

Click `Delete` in the confirmation window to proceed and remove the job.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F10X0BreuUW49yjbqLSWh%2FScreenshot%202025-10-03%20at%205.48.46%E2%80%AFPM.png?alt=media&#x26;token=d2fd1a64-67a9-4d77-adcd-4b7baff3c472" alt=""><figcaption></figcaption></figure>

## Email Notifiers

You can configure email notifications to alert stakeholders whenever a job fails. This helps teams monitor job health, quickly identify failures, and take timely corrective action.

When email notifiers are configured, the system sends a notification to the specified email addresses if a job fails. For example, if an [auto-sync](#auto-sync) job scheduled to run at a specific time fails, the configured recipients receive an immediate alert.

**To configure email notifications:**

1. Navigate to the required job.
2. Click the three-dot menu next to the job name and select `Email Notifiers`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2kDrqglgtcmbhHI8DcLR%2FScreenshot%202025-12-16%20at%203.39.20%E2%80%AFPM.png?alt=media&#x26;token=28997ca7-ad81-4ef9-9ce3-7f7f52c8f341" alt=""><figcaption></figcaption></figure>

3. Add up to five email addresses, using `+ Add` to include them one by one. Click `Save` to apply the configuration.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjxsWs3oIBf8vpY9enx4i%2FScreenshot%202025-12-16%20at%203.41.08%E2%80%AFPM.png?alt=media&#x26;token=cb46fb32-5d8f-425a-afbc-e739673cbcdb" alt=""><figcaption></figcaption></figure>

## View the version of the job

You can view different versions of a job by clicking the dropdown option located at the top-right corner of the job.

{% hint style="warning" %}
**Note:** This option is available only for `SharePoint`, `ServiceNow`, and `Website` connectors.
{% endhint %}

This feature is handy if you have used `Auto sync` or `Sync Now`. It lets you view the history of article synchronizations for the job. By comparing different versions, you can identify what content has been updated, added, or changed over time. This helps ensure that you always have a clear record of changes and can track updates efficiently.

To view different versions of a job:

1. Navigate to the `Jobs` list and select the job you want to review.
2. Locate the dropdown menu at the top-right corner of the page. Click the dropdown and select a version from the list. The selected job version, along with its ingested articles or documents, is displayed.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fgq47ckL3FwVCQOiJcVSq%2FScreenshot%202025-10-23%20at%2011.37.42%E2%80%AFAM.png?alt=media&#x26;token=744dc8b9-8f31-4667-883d-4794da33e665" alt=""><figcaption></figcaption></figure>

## Advanced Attributes Handler

If you missed configuring attributes during ingestion, or if you want to update attributes for already ingested documents or articles, you can use the `Advanced Attribute Handler`. This feature allows you to apply or modify document attributes using custom JavaScript logic during a sync run.

This approach allows you to safely validate attribute logic before applying it across documents during a sync operation.

**To configure the advanced attribute handler**

1. Navigate to the required DataSync job.
2. Click the three-dot menu next to the job name and select `Advanced Attribute Handler`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMiQJ5vNgK6hDQYS7ucNO%2FScreenshot%202026-01-29%20at%205.10.53%E2%80%AFPM.png?alt=media&#x26;token=0f70520f-085d-44b1-8652-3f655cdaaca8" alt=""><figcaption></figcaption></figure>

3. A side panel opens with the configuration options. Toggle the `Enabled` switch to enable the attribute handler.

{% hint style="info" %}
**Note**:&#x20;

1. The configured JavaScript is saved as part of the post-processing configuration and is applied **only when a Sync Now or Auto Sync operation is triggered**.&#x20;
2. Disabling the attribute handler prevents the script from running during subsequent syncs.
   {% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FprEToJbyD8H3grVAHf4O%2FScreenshot%202026-01-29%20at%205.11.01%E2%80%AFPM.png?alt=media&#x26;token=14cb23a3-a405-4a43-b831-2e4fc2701a44" alt=""><figcaption></figcaption></figure>

4. Under `Configure attribute handler`, provide the JavaScript code that returns the updated attributes you want to apply to the documents.
5. In the `Test` option in the attribute handler panel. Update the test JavaScript input with actual sample data.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fi6uvg6vdGq5QDJMA5dL4%2FScreenshot%202026-01-29%20at%205.11.16%E2%80%AFPM.png?alt=media&#x26;token=b5be0b22-f953-47b0-ba97-0e44a3467b71" alt=""><figcaption></figcaption></figure>

6. Click **Test** to validate the script execution. Review the output to confirm that the attributes are updated correctly for the selected document or article.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FOWZZOLqYuQtbT7xhqcPx%2FScreenshot%202026-01-29%20at%205.11.24%E2%80%AFPM.png?alt=media&#x26;token=765643f1-0475-4fd9-9a63-51bd05d33c39" alt=""><figcaption></figcaption></figure>

7. Once you have configured and tested the attribute handler, choose one of the following actions:

* **Cancel** – Discard the changes if you do not want to apply the attribute configuration.
* **Save** – Save the configuration. The attribute handler will be applied the next time [AutoSync](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/auto-sync) or [SyncNow](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/sync-now) is triggered.
* **Save & Apply** – Save the configuration and immediately run a `manual sync` to apply the attribute handler to the selected documents.
