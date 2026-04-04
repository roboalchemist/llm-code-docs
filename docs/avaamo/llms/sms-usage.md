# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/sms-usage.md

# SMS Usage

The `SMS usage` page is valuable for users with the [SMS channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sms) enabled in their agents, providing a means to monitor and track `SMS usage` within their accounts. Navigate to `Profile Icon>Settings>Usage reports>SMS usage` to view.

You can also export the usage report from this page to analyze further. The page helps you to track the anticipated SMS billing associated with the company-level SMS configuration.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fl3VzlPfK4hla9hncdYku%2FScreenshot%202024-10-21%20at%202.20.13%E2%80%AFPM.png?alt=media&#x26;token=c4393e0b-349c-4d8e-9ebf-2a436f84a9a4" alt=""><figcaption></figcaption></figure>

### What is Segment?

Messages longer than 160 characters are automatically split into parts (called "segments") and then re-assembled when they are received. Message concatenation allows you to send long SMS messages, but this increases your per-message cost, as SMS are billed per segment.

### How to use this page?

{% hint style="info" %}
**Notes**:&#x20;

* The `SMS Usage` page is available only for users with the `Settings` role.
* All the data in the page is captured in the UTC timezone.
  {% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVZXAt7I0rzi6Sl9Ynd1C%2FScreenshot%202024-10-21%20at%202.23.30%E2%80%AFPM.png?alt=media&#x26;token=91fb05a7-d499-4fc6-9032-a3698d80db85" alt=""><figcaption></figcaption></figure>

* At the top, you can view the data for 6 months with segments and message count. Click `Export all` to export 6 months of data in a CSV format.
* Data for each month with segment and message summary is displayed. Click the month to view the complete history of SMS usage for each day of the month. The following information is displayed in the detailed view for each date:
  * **SMS Outbound Count (Messages)**:  Total number of messages sent by the Avaamo Conversational AI Platform.
  * &#x20;**SMS Outbound Usage (Segments)**: Total number of segments sent by the Avaamo Conversational AI Platform. Note that SMS are billed per segment. See [What is Segment?](#what-is-segment), for more information.&#x20;
  * **SMS Inbound Usage**: Total number of messages received by the Avaamo Conversational AI Platform.
* Click `Export` to export the specific month's data in a CSV format.
