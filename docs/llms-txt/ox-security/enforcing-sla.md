# Source: https://docs.ox.security/exclusions-and-sla/scope-policy-and-sla-compliance/enforcing-sla.md

# Enforcing SLA

Security’s Service Level Agreement (SLA) capability is designed to help organizations maintain security standards by setting and enforcing time-based commitments for resolving security issues.

In many cases, organizations commit to their clients that certain types of security issues, especially those with high severity, are resolved within a defined period. OX Security’s SLA management capability enables teams to efficiently track and meet these commitments. It provides a structured way to monitor resolution timelines and automate actions when deadlines are not met.

## Automated OX SLA Management

OX Security’s automated SLA management eliminates the inefficiencies and risks associated with manual SLA tracking.

By centralizing SLA tracking, OX provides real-time visibility and automation, freeing teams from manual work and helping them address issues faster and more efficiently.

## OX SLA Use Cases

By default OX SLA capability is disabled. You need [to enable it](#enabling-sla-and-setting-conditions) and then you can use is as follows:

* [Configure SLA conditions](#configuring-sla-conditions)
* [Monitor SLA compliance](#monitoring-sla-compliance)
* [Change SLA settings for specific issues](#changing-sla-settings-for-specific-issues)
* [Monitor issues SLA trends](#monitoring-issue-sla-trends)
* [Schedule automated actions](#automated-actions)

### Configuring SLA conditions

You can define SLA conditions based on issue severity.

For instance, set an SLA for Critical issues to be resolved within one day.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a8d46c29a96f8d01327df32b5ee7ccfb742ee821%2Fsevirity%20based%20SLA_new1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Monitoring SLA compliance

You can track SLA compliance in real time across all workloads. This helps teams stay informed of SLA adherence and address breaches quickly.

For example, in the Dashboard you can see the total number of SLA in the overdue status.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-55dcc742794b0746aa5dbaa3b4ba61bd589809fc%2FSLA_dashboard.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

While in the Issues page, you can view the status of SLA adherence for each security issue and filter the page info for specific info, such as finding all the issues whose SLA is overdue for 1 day, or all the issues whose SLA will be due in 5 days.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bca49161b6c05f5487616beccdda2c85d9c15d8e%2FSLA_issues_correct.png?alt=media" alt=""><figcaption></figcaption></figure>

### Changing SLA settings for specific issues

SLA definitions are set globally based on issue severity, but you can manually adjust these settings for specific issues you select. This provides greater control over SLA management.

For example, all issues with Critical severity are assigned a 7-day SLA. However, some critical issues may be more complex and require additional time to resolve. In such cases, the AppSec manager can select specific critical issues and extend their SLA.

If, after a few days, the AppSec manager sees that the selected issues can be resolved along with others, they can reset the SLA settings for those issues, returning them to the original global settings.

Alternatively, the AppSec manager may identify certain issues that do not require an SLA and choose to cancel the SLA for those issues.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bdab7fa90f165c175dc61c29890ac015d8ba29f1%2FSLA_actions.png?alt=media" alt=""><figcaption></figcaption></figure>

### Monitoring issue SLA trends

Issues SLA compliance trends provide insights into how well the team is meeting its service level commitments. These reports can be customized to show performance across different business units and teams, helping leadership make informed decisions about resource allocation.

You can find issues SLA trends as part of Executive Reports.

For example, create a monthly report that shows issue resolving trend and issues SLA trend within the defined timeframe. The report can be shared with management to highlight areas for improvement or present successful performance.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-651721fd62c95377b467f9ef353dd4c2b37af9e6%2FSLA_in_ExecutiveReports.png?alt=media" alt=""><figcaption></figcaption></figure>

### Automated actions

OX Security can automatically trigger actions such as Slack alerts or ticket creation when SLA deadlines are breached.

For example, you can define that when the policies with severity level equal or greater than Critical are SLA overdue by 1 day, then a Slack notification is sent.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dafe099d411d15a5fdb8a6ea0f389afb82d367b2%2FSLA_WF.png?alt=media" alt="" width="144"><figcaption></figcaption></figure>

Another scenario is when for example Critical issue severity is set for all the issues in the system to 7 days, but the appsec admin thinks that for open source policies they need 15 days. In that case they can define that for each new Open Source Security policy Critical issue the SLA definition will be automatically changed to 15 days.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7cc27d107617e8ca9ffc5cbccbcb643427e7af7e%2FSLA_WF_change.png?alt=media" alt="" width="186"><figcaption></figcaption></figure>

## Enabling SLA and Setting Conditions

Before using SLA, you need to enable it.

1. In the OX app, go to **Settings > SLA**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8896bc45ad69023123715e487fdea12fc8972704%2Fsevirity%20based%20SLA.png?alt=media" alt="" width="552"><figcaption></figcaption></figure>

1. Set the following:

| Parameter                                             | Description                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SLA**                                               | Enables the capability.                                                                                                                                                                                                                                                                                                                                                    |
| **Severity levels (Appoxalypse, Critical and so on)** | Set the SLA period for each severity level.                                                                                                                                                                                                                                                                                                                                |
| **SLA Approaching Overdue Warning Period (in days):** | <p>Sets the number of days for the SLA Approaching Overdue status.<br><br>When this period expires, the issue is considered to have breached the SLA.<br><br>For example, if the value is set to 5 days, and there are 3 days left until the SLA breach, the following SLA status appears in the issue's info: -3d. This means that this issue's SLA is due in 3 days.</p> |
| **Start SLA from a specific date**                    | <p>Enable this option to set the date from which SLA counting begins.</p><p>Changing this date resets the SLA counting for your organization.</p>                                                                                                                                                                                                                          |

1. Select **SAVE**.
