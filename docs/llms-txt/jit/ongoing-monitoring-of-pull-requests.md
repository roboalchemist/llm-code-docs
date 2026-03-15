# Source: https://docs.jit.io/docs/ongoing-monitoring-of-pull-requests.md

# Change-Based Security Tests in Pull-Requests

## The developer creates the pull request

Code-layer security requirements run when a developer creates a pull request via CLI, IDE, or SCM (in this example — GitHub). In this scenario, the developer makes code changes that contain the Python code security vulnerability below.

```python
import subprocess
output = subprocess.check_output(f"nslookup2 {domain}", shell=True, encoding='UTF-8')
```

> 📘 Note
>
> In this scenario, branch protection rules are configured to prevent merging if the **Jit Security** check fails.

## Jit checks run

Jit listens to pull request and merge request events and runs security checks on the code changes during the PR/MR flow.

The [Python Code Scanning](https://docs.jit.io/docs/security-tools) check fails with findings. Branch protection rules require this check to pass before the pull request can be merged. As a result, the option to merge is disabled.

> ❗️ If a Jit check fails with errors after multiple re-run attempts, notify your security champion.
>
> If a Jit check continues to fail with errors, Jit users with administrator privileges (such as security champions) can bypass branch protection rules by running the command `#jit-bypass-commit`in a new comment to unlock the option to merge the PR. Note that this may allow vulnerabilities, that would otherwise have been detected, onto the target branch.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/418936a6253b5f7f35fba3f47d3b6b41fe48ac1cbf61529e410a289b5aabbbb8-failed_check.png",
        "cant_merge2.png",
        "Jit Security - Checks"
      ],
      "align": "center"
    }
  ]
}
[/block]

## The developer views the security finding

Jit displays any security requirement findings in the pull request conversation using a common, unified format. For each finding, Jit presents the following—

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/098423c2e11c4962493db6c233061effd1a941b448cd728f2ad7d8ce6ff538c8-code_review.png",
        "finding_perfect.png",
        "Jit Security Review with comments"
      ],
      "align": "center",
      "sizing": "100"
    }
  ]
}
[/block]

> 📘 Finding format
>
> `Sample of flagged code`
>
> **Summary:** A high-level overview of the security impact and affected components.
>
> **Findings:** A breakdown of detected issues, grouped by severity.
>
> **Advanced options:** Information on supported ignore actions and syntax.

## The developer addresses the finding

When the Jit Security check fails, developers are advised to address the finding in order to eliminate any security issues or risky misconfigurations. Here are the options

* The developer can fix the code with [Jit automated remediation](https://docs.jit.io/docs/automated-remediation).
* The developer can ignore the finding.

### The developer fixes the code with Jit automated remediation

In some cases, developers can fix the security issue or IaC misconfiguration instantly with automated remediation within the scope of the pull request. For further information, see  [Jit automated remediation](https://docs.jit.io/docs/automated-remediation).

### The developer ignores the finding

Developers have the option to circumvent branch protection rules if they have reason to believe the finding is a false positive or intend to resolve the issue at a later time. To ignore the finding, the developer can issue one of three commands inside a comment (see below).

> 📘 Supported ignore commands
>
> * **Ignore a specific finding**`@sera ignore <finding_id> reason:<reason>`\
>   Ignores a single finding instance. reason is optional, Valid values:  `accepted`, `false-positive`, `other`.
> * **Ignore all findings in the PR**`@sera ignore all reason:<reason>`\
>   Ignores all findings reported in the current PR.
> * **Ignore a finding type**`@sera ignore type:<finding_type>`\
>   Ignores all findings of the specified type (e.g. GHSA-xxxx-xxxx).
> * **Undo an ignore action**`@sera unignore <finding_id>`\
>   Reverts a previous ignore action and restores the finding(s).
>   ***
>   **Reason values:** `accepted`, `false-positive`, `other`.\
>   To add a free-text explanation, place it after a dash following the reason: `@sera ignore <finding_id> reason:false-positive - this is a test credential`.\
>   The text after the dash is for your notes only and does not affect how the ignore is processed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9abd67d1ce5d996c4cf5eaecd5a88a0e9a123a0347e4e8ab7f296dd4ebee43c6-Screenshot_2026-01-26_at_16.49.05.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

If Slack integration is configured, a Slack notification is sent to the security champion with a link to review the ignored pull request. At this point, the security champion may choose to DM the developer to discuss the issue. For instructions on integrating with Slack see [Integrating with Slack](https://docs.jit.io/docs/integrating-with-slack),

![](https://files.readme.io/a2c57e1-Screenshot_2022-08-09_8.52.16_AM.png)

## The developer merges the pull request

When all findings have either been fixed or dismissed, successful status checks enable the option to merge.

![Pull Request checks pass](https://files.readme.io/a657ce5-green_merge_wide.png "green_merge_wide.png")