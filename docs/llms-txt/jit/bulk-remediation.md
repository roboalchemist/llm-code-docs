# Source: https://docs.jit.io/docs/bulk-remediation.md

# Bulk Remediation

> ⚠️  Deprecated feature
>
> The Bulk Remediation (Actions) page has been removed for most customers and is being fully phased out. This documentation is kept temporarily for reference and will be removed.

## Overview

The Actions page enables you to quickly and easily remediate security issues and misconfigurations present in the [Findings Page](https://docs.jit.io/docs/jit-findings). Each Action is an aggregation of one or more issues of a common type that can be fixed as a group with automated remediation.

![](https://files.readme.io/b3d3a46-Screenshot_2022-12-10_6.50.15_PM.png)

## Supported remediation actions

Jit currently supports remediation for the following security requirements:

| Security requirement                                                                   | Jit remediation method |
| :------------------------------------------------------------------------------------- | :--------------------- |
| [Scan IaC for Static Misconfigurations](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations)     | Create a fix PR.       |
| [Require Branch Protection for SCM](https://docs.jit.io/docs/require-branch-protection-for-scm#remediation) | Run a script to fix.   |

## Actions

Each Action contains the following information:

* The action that fixes the issue.
* An explanation of *why*  it is important to fix the issue.
* The total number of occurrences of the issue.
* The severity.
* The last time the issue was detected.
* The specific issue type.
* Status: Whether the Action is *New* or *In Progress*. The *In Progress* status indicates that a user has opened a fix PR or ignored an issue, but some issues remain unresolved. An issue is considered resolved when it has been ignored or when its fix has been merged.

![](https://files.readme.io/8e99963-image.png)

**To fix issues in an Action —**

1. Select the Action to expand it.
2. Use the checkboxes to select one or more issues from the list.
3. Select **Fix (Open PR)**. Jit confirms the successful creation of a PR that, once merged, fixes the issue.
4. Navigate to the PR using the **View Fix PR** link and merge the changes. Jit security checks run a second time, confirming that the vulnerability or misconfiguration is no longer present.

> 📘 Note
>
> This final step can be performed by anyone on your team who has access to the repository.

**To ignore issues in an Action—**

1. Select the Action item to expand it.
2. Use the checkboxes to select one or more issues from the list.
3. Select **Ignore**. When viewed from the [Findings page](https://docs.jit.io/docs/jit-findings), the selected issues are listed as ignored findings.

### Creating tickets

To create tickets for findings, you must first integrate Jit with your ticket management system. For instructions, see [Integrating with Third-Party Products and Services](https://docs.jit.io/docs/integrating-with-third-party-products-and-services).

**To create a ticket management system issue for issues in an Action—**

1. Select the Action item to expand it.
2. Use the checkboxes to select one or more issues from the list.
3. Use the dropdown to select **Open a unified Jira issue**, **Open a Shortcut story**, or **Open a Linear issue**, depending on your ticket management system.

### Action sharing

Jit enables you to share Actions with other users via a notification in Slack. If you have not already configured Slack integration, please see [Integrating with Slack](https://docs.jit.io/docs/integrating-with-slack).

**To share an Action with another user—**

1. Select the Action's share icon. Dialog displays.
2. Enter the name(s) of the Jit users you wish to share this Action with.
3. Select **Send**. The selected user(s) receive a notification in Slack.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bbf5818-actionbuttonannote.png",
        null,
        "Step 1."
      ],
      "align": "center",
      "caption": "Step 1."
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ae78205-shareactiondialog.png",
        null,
        "Step 2."
      ],
      "align": "center",
      "caption": "Step 2."
    }
  ]
}
[/block]