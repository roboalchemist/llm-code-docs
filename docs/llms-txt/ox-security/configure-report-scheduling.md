# Source: https://docs.ox.security/generate-reports/reporting/configure-report-scheduling.md

# Configure Report Scheduling

You can schedule email exports of [reports](https://docs.ox.security/generate-reports/reporting)to ensure stakeholders receive regular updates. Recipients can include anyone in your organization, even if they are not OX users.

If a recipient is not an OX user, their email address must include the company domain.

When the export is sent to a recipient who is not an OX user, the report reflects the creator’s scope. If the export is sent to a scoped OX user, the recipient receives the report in their own scope.

You can set the frequency, time, and format of the exported report.

The following permissions are required to schedule report export:

* **Built-in reports:** OX Admin only.
* **Custom reports:** OX Admin or report owner.

**To schedule report exports:**

1. Go to **Reports**, select the three-dot icon next to the report for which you want to configure scheduled exports, and select **Scheduled Report Exports**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f1ea5e9321bb4f27e73274694e7cc74f6e04ffbe%2Freport_schedule.png?alt=media" alt="" width="539"><figcaption></figcaption></figure>

1. Set the following:

| Field                            | Description                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Recipients**                   | Email addresses of the recipients who will receive the scheduled report. Multiple addresses can be added, separated by commas. |
| **Frequency**                    | Defines how often the report is sent, daily, weekly, or monthly.                                                               |
| **Day of Week/On day**           | Selects the day when the report will be sent.                                                                                  |
| **At**                           | Specifies the exact time of day when the report will be sent. Times are displayed in your local timezone.                      |
| **Format**                       | Defines the export format of the report. You can choose between **PDF** and **CSV**.                                           |
| **Maximum items per each table** | Sets a limit on the number of items included per table in the exported report.                                                 |

1. Select **Save Schedule**.
2. The schedule is turned on by default. To turn it off, turn off **Activate Schedule**.
