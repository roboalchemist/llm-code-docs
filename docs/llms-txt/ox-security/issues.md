# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/issues.md

# Active Issues

{% hint style="success" %}
**At a glance:** Review a summary list of all issues identified during the scan and apply detailed filters to highlight those most relevant to your organization. Then, dig into detailed data for each issue, including recommendations for remediation.
{% endhint %}

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-382ccaa217a20e8a4ce76cd895ba63332c528669%2Fissues.png?alt=media" alt=""><figcaption></figcaption></figure>

## Summary table

The **Issues** page summary table shows each issue's severity, category, application, owner, date of discovery, and count. You can sort the table by any of its columns, perform detailed issue filtering, and choose from an extensive list of actions for handling each issue.

### Filter issues

The filter pane on the left side of the **Issues** page provides extensive options for filtering issues. You can filter by one or more criteria simultaneously and save your filter combinations to use again later. After you apply a filter, the summary table will display only those issues that meet the filter criteria.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8fbd38e431955653204c66b0c0d0b0a5034c9516%2Fissue_filters.png?alt=media" alt="" width="165"><figcaption></figcaption></figure></div>

See the **Reference** section below for a list of all [**Issues** page filters](#issues-page-filters).

## Issue details

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-46f9543759b320c8b451d436c71382655e887521%2Fissue_details.png?alt=media" alt=""><figcaption></figcaption></figure>

The issue details pane provides extensive information about the app, including recommendations for remediation, attack path, a list of reachable vulnerabilities, and more. Switch among tabs to navigate the types of detailed information available.

## Issue actions

The buttons in the issue details pane give you extensive options for issue treatment. These actions include:

* Adding a comment
* Starting ChatGPT with pre-filled prompts for obtaining more information about the issue
* Applying an automatic fix for the issue (when available)
* Viewing a code fix (when available)
* Opening a pull request applying the code fix
* Sending an alert to one or more of your organization's Slack channels
* Creating a Jira ticket or linking to an existing ticket
* Excluding the issue
  * This moves the issue to the [**Exclusions**](https://docs.ox.security/exclusions-and-sla/scope-policy-and-sla-compliance/exclusions) page and prevents it from being reported in future scans.
* Making the app in which the issue was found irrelevant
  * When the app is made irrelevant, all of that app's issues will be removed from the summary table.
* Disabling the policy that the issue violated
  * Disabling a policy prevents all issues related to that policy from being reported in future scans.
* Viewing and editing the policy that the issue violated (in a new browser tab)
* Changing the issue's severity
* Reporting the issue to OX as a false positive, with the option to exclude the issue

### Bulk issue actions

Certain issue actions can be applied to multiple issues simultaneously by selecting the relevant issues in the summary table and using the buttons at the top of the table:

* Excluding the issues
* Changing the issues' severity
* Creating a new Jira ticket
* Adding, editing, or deleting a comment

## Export

You can export several reports from the **Issues** page in various formats:

* All issues
  * Aggregated (CSV or PDF)
  * Non-aggregated (CSV)
* Filtered issues
  * Aggregated (CSV or PDF)
  * Non-aggregated (CSV)

## Reference

<details>

<summary>Issues page filters</summary>

![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fbfd9d4a9b6a17c9128e0733624c19dfb9875e78%2Fissue_filters_full.png?alt=media)

</details>
