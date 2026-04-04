# Triage and remediate findings

Source: https://semgrep.dev/docs/semgrep-code/triage-remediation

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Scan and triage- SAST (Code)- Triage and remediation**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)Triage and remediate findings

This article shows you how to manage and triage identified by Semgrep Code using Semgrep AppSec Platform. The specific actions available to you when managing your findings include:

- **Fixing the issue detected.** This is Semgrep&#x27;s primary goal. If the rule produces a **true positive** finding, such as a security issue, developers must change or address the code so that the rule no longer matches it.
- **Triaging the finding.** Deprioritize a finding if it&#x27;s not helpful or important through triage. Triage actions include ignoring and reopening a previously ignored finding. Triaging a finding to **ignore** is one method to handle **false positives** without changing a rule or your code.
- **Removing the rule or code that generated the finding.** There are cases where Semgrep scans a file it should ignore or scans the file with an irrelevant rule. You can [disable the rule](/docs/semgrep-code/policies#disable-rules) from the **Policies** page or [add the file to the ignore list](/docs/ignoring-files-folders-code).

### Semgrep Assistant[​](#semgrep-assistant)
If you have Semgrep Assistant enabled, you receive AI-powered security recommendations to help you review, triage, and remediate your Semgrep findings:

- [Remediation advice](/docs/semgrep-assistant/overview#remediation) shown in Semgrep AppSec Platform, including:

[Guidance](/docs/semgrep-assistant/overview#guidance) with step-by-step instructions on how to remediate the finding identified by Semgrep Code in every pull request or merge request comment Semgrep pushes
- [Autofixes](/docs/semgrep-assistant/overview#autofix), or suggested code fixes

- [Component tagging](/docs/semgrep-assistant/overview#component-tags) to help identify high-priority issues

Semgrep Assistant can also [auto-triage findings](/docs/semgrep-assistant/overview#auto-triage), suggest whether a finding can safely be ignored, and [filter out potential false positives](/docs/semgrep-assistant/overview#noise-filtering-beta) to help increase developer velocity.

## Triage statuses[​](#triage-statuses)
**Triage** is the prioritization of a finding based on policies or criteria set by your team or organization, such as severity, coding standards, business goals, and product goals.

Semgrep AppSec Platform uses the logic specified in the table below to automatically mark findings as either fixed or removed when they are no longer present in the code. Additionally, Semgrep can automatically mark findings as **provisionally ignored** based on AI analysis, validation results, and reachability analysis.

You can manually **Ignore** findings or set them as **To fix** or **Reviewing** in Semgrep AppSec Platform directly through **triage** or **bulk triage** actions.

The triage statuses are as follows:

StatusDescription**Open**Findings are open by default. A finding is open if it was present the last time Semgrep scanned the code and has not been ignored. An open finding represents a match between the code and a rule enabled in the repository. Open findings require action, such as rewriting the code to eliminate the detected vulnerability.**Reviewing**Indicates that the finding requires investigation to determine what the next steps in the triage process should be.**Provisionally ignored**Findings that Semgrep Assistant has flagged as false positives. You can change the status to **Ignored** if you agree with Assistant&#x27;s assement. Otherwise, you can change the status to **To fix** if you disagree.**To fix**Findings that you have decided to fix. Commonly used to indicate that these findings are tracked in Jira or assigned to developers for further work.**Fixed**Fixed findings were detected in a previous scan but are no longer detected in the most recent scan of that same branch due to changes in the code.**Ignored**Findings marked as ignored are present in the code but have been labeled unimportant. Ignore false positives or deprioritized issues. Mark findings as [ignored through Semgrep AppSec Platform](/docs/semgrep-code/triage-remediation) or by adding a [nosemgrep code comment](/docs/ignoring-files-folders-code#reference-summary). You can also provide a reason for ignoring a finding: **False positive**, **Acceptable risk**, **No time to fix**.**Closed**Vulnerabilities that are no longer detected after a scan. This can be due to changes in the underlying rule or the code.
### Removed findings[​](#removed-findings)
Findings can also be **removed**. Semgrep considers a finding removed if it is not found in the most recent scan of the branch where Semgrep initially detected it due to any of the following conditions:

- The rule that detected the finding isn&#x27;t enabled in the policy anymore.
- The rule that detected the finding was updated in a way that it no longer detects the finding.
- The file path where the finding appeared is no longer found. The file path was deleted, renamed, added to a `.semgrepignore` file, added to a `.gitignore` file, or added to the list of ignored paths in Semgrep AppSec Platform.
- For GitHub organization accounts: the pull request or merge request where the finding was detected has been closed without merging.

Your removed findings do not count toward the fix rate or the number of findings. The removed findings also do not appear in Semgrep AppSec Platform.

### Triage behavior across refs and branches[​](#triage-behavior-across-refs-and-branches)

- When you triage a finding as ignored, reviewing, fixing, or reopened, Semgrep always triages across other branches and [Git references](https://git-scm.com/book/en/v2/Git-Internals-Git-References) (refs).
- At scan time, there&#x27;s automatic triaging that occurs in specific cases, and the behavior changes depending on the type of scan:

**Full scans**: if the current branch includes a finding that was

Previously introduced in another branch ***and***
- Triaged to a specific state
**Then** the finding in the current branch is triaged to that same state.

- **Diff-aware scan**: findings introduced in a diff-aware scan are **not** automatically triaged at scan time, even if there are other instances of that finding on branches that have been triaged.

## Triage and remediation[​](#triage-and-remediation)
The following sections show you how to manage your findings by:

- Fixing the underlying code
- Disabling a rule or a ruleset
- Ignoring a finding
- Reopening a finding

Note that some actions, such as ignoring and reopening findings, require different steps based on whether you have chosen **Group by Rule** or **No Grouping** when viewing your results on the **Findings** page.

### Fix a finding[​](#fix-a-finding)
To **fix a finding**, update or refactor the code so that the Semgrep rule pattern no longer matches it.

## Review provisionally ignored findings[​](#review-provisionally-ignored-findings)
If you have Semgrep Assistant enabled, review the findings that have been **provisionally ignored**. These are findings that Semgrep Assistant has flagged as false positives. For each finding, you can change the status to **Ignored** if you agree with Assistant&#x27;s assement. Otherwise, you can change the status to **To fix** if you disagree.

Findings with a status of **provisionally ignored** block pull requests and merge requests if the matching rule is included in a blocking policy.

### Ignore findings[​](#ignore-findings)
To handle **false positives** without changing the rule or your code, set the finding&#x27;s triage status to **ignore**.

Ignore findings in Group by Rule** viewTo **ignore findings** in the **Group by Rule** view:

- Go to [**Code &gt; All**](https://semgrep.dev/orgs/-/findings?tab=open), and ensure that your filters are set to display all **Open** findings.
- Perform one of these steps:

To select all findings for the same rule, select the first checkbox on the finding&#x27;s card, then click **Triage &gt; Ignored** .
- To select individual findings reported by a rule, fill in the checkboxes of the finding, and then click **Triage &gt; Ignored**.

- Select **Ignore reason**, and optionally, provide **Comments** to describe why the finding was ignored.
- Click **Submit**.

Ignore findings in ** No grouping** viewTo **ignore individual finding** in the **No grouping** view, follow these steps:

- Go to [Code &gt; All](https://semgrep.dev/orgs/-/findings?tab=open), and ensure that your filters are set to display all **Open** findings.
- Select the checkbox next to a finding you want to ignore, and click **Triage &gt; Ignored**.
- Select **Ignore reason**, and optionally, provide **Comments** to describe why the finding was ignored.
- Click **Submit**.
To **ignore multiple findings** in the **No grouping** view, follow these steps:

- Go to [Code &gt; All](https://semgrep.dev/orgs/-/findings?tab=open), and ensure that your filters are set to display all **Open** findings.
- Perform one of these steps:

Select all findings on the page displayed by clicking on the header row checkbox that states **X matching findings**. You can navigate to succeeding pages and add other results to the current selection.
- Select all findings of interest by clicking on their checkboxes.

- Click **Triage &gt; Ignored**.
- Select **Ignore reason**, and optionally, provide **Comments** to describe why the findings were ignored.
- Click **Submit**.

### Reopen findings[​](#reopen-findings)
You can **reopen** a finding at any time, whether you previously marked it as **ignored** or Semgrep automatically marked it as **provisionally ignored**.

Reopen findings in **Group by Rule** viewTo **reopen findings** in the **Group by Rule** view, follow these steps:

- Go to [Code &gt; All](https://semgrep.dev/orgs/-/findings?tab=open), and ensure that your filters are set to display all **Ignored**, **Provisionally Ignored**, or **Fixed** findings.
- Perform one of these steps:

To select all findings for the same rule, select the first checkbox on the finding&#x27;s card, then click **Triage &gt; Open** .
- To select individual findings reported by a rule, fill in the checkboxes of the finding, and then click **Triage &gt; Open**.

- Optional: Write a reason to describe why the finding was reopened.
- Click **Submit**.

Reopen findings in **No grouping** viewTo **reopen individual findings** in the No grouping view, follow these steps:

- Go to [Code &gt; All](https://semgrep.dev/orgs/-/findings?tab=open), and ensure that your filters are set to display all **Ignored**, **Provisionally Ignored**, or **Fixed** findings.
- Select the checkbox next to a finding you want to reopen. Click **Triage &gt; Open**.
- Optional: Write a reason to describe why the finding was reopened.
- Click **Submit**.
To **reopen multiple findings** in the **No grouping** view, follow these steps:

- Go to [Code &gt; All](https://semgrep.dev/orgs/-/findings?tab=open), and ensure that your filters are set to display all **Ignored**, **Provisionally Ignored**, or **Fixed** findings.
- Perform one of these steps:

Select all findings on the page displayed by clicking on the header row checkbox that states **X matching findings**. You can navigate to succeeding pages and add other results to the current selection.
- Select all findings of interest by clicking on their checkboxes.

- Click **Triage &gt; Open**.
- Optional: Write a reason to describe why the finding was reopened.
- Click **Submit**.

### Turn off a ruleset or a rule[​](#turn-off-a-ruleset-or-a-rule)
You can turn off a specific rule or ruleset to prevent Semgrep Code from using it when scanning your codebase.

infoWhen you turn off a rule, existing findings from that rule remain open until you re-scan your code.

Disable rules and rulesetsTo disable a **rule**:

- Go to the [**Policies** page](https://semgrep.dev/orgs/-/policies) and select either:

The top **Number Matching Rules** checkbox to select all rules.
- Individual checkboxes next to a rule to turn off rules one by one.

- Click **(Number) Change modes**, then click **Disabled**.
You can also set the state in the **Mode** column to **Disabled** for individual rules.

To turn off a **ruleset** using the Policies page:

- Go to the [**Policies** page](https://semgrep.dev/orgs/-/policies), .
- Use the **Ruleset** filter&#x27;s drop-down box to find and click the ruleset to remove.
- Click ** **Matching rules**.
- Click **Change modes &gt; Disabled**.

## Triage findings through PR and MR comments[​](#triage-findings-through-pr-and-mr-comments)
You can triage your Semgrep AppSec Platform findings displayed as comments in PRs and MRs by replying with another comment.

Before proceeding, ensure that you have:

- One or more repositories hosted by a [Semgrep-supported source code manager (SCM)](/docs/getting-started/scm-support).
- Configured [PR or MR comments](/docs/category/pr-or-mr-comments) for your SCM.

To triage a finding:

- Find an open comment created by Semgrep in your pull request or merge request.
- In a subsequent comment, reply with the action you want to take. You must provide a reason to help the reader understand why the finding has been triaged as ignored:

CommentDescription`/fp &lt;COMMENT&gt;`Triage a finding as **Ignored** with the triage reason **false positive**. Provide a `&lt;COMMENT&gt;` with information about the triage decision.`/ar &lt;COMMENT&gt;`Triage a finding as **Ignored** with the triage reason **acceptable risk**. Provide a `&lt;COMMENT&gt;` with information about the triage decision.`/other &lt;COMMENT&gt;`Triage a finding as **Ignored** without specifying the reason; the triage reason value is set to **No triage reason**. Provide a `&lt;COMMENT&gt;` with information about the triage decision.`/open &lt;REASON&gt;`Reopen a finding that has been triaged as **Ignored**. Optionally, provide a `&lt;COMMENT&gt;` with information about the decision to reopen the finding.
Semgrep attempts to reply to your comment if it successfully triages the finding.

Triaging a finding as **Ignored** through a comment changes the status of the finding to **Ignored** in Semgrep AppSec Platform. However, the pull request or merge request conversation itself is **not** automatically resolved by this process.

Legacy commandsSemgrep supports older versions of this feature that used the following commands:

- `/semgrep ignore &lt;REASON&gt;` - triage a finding as **Ignored**.
- `/semgrep open &lt;REASON&gt;` - reopen a finding that has been triaged as **Ignored**.

## Triage findings in bulk through the Semgrep API[​](#triage-findings-in-bulk-through-the-semgrep-api)
Semgrep provides an API endpoint you can use to triage findings in bulk, either by passing a list of `issue_ids` or filter query parameters to select findings. You must also specify an `issue_type`, such as `sast` or `sca`, and either `new_triage_state` or `new_note`.

The available `new_triage_state` values you can set are:

- `open`
- `reviewing`
- `fixing`
- `ignored`
- `fixed`

If specifying a `new_triage_reason`, you must also use `new_triage_state=ignored`.

noteWhen retrieving findings through the API, you may also see the `provisionally_ignored` status. This status is automatically set by Semgrep and cannot be manually assigned through the bulk triage API.

Refer to [** Bulk triage API documentation](https://semgrep.dev/api/v1/docs/#tag/TriageService) for complete details.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

**Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-code/triage-remediation.md)Last updated on **Dec 10, 2025**