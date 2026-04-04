# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/auto-sync.md

# Auto sync

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
