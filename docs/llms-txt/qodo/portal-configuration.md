# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/portal-configuration.md

# Configure Using the Qodo Portal

The Configuration page in the Qodo portal allows you to easily manage **organization-wide** review settings.

This page is located in the left-hand navigation menu in the [Qodo portal.](https://app.qodo.ai/)

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FM20smydwbsZDYIFIrnm4%2FScreenshot%202026-03-05%20083954.png?alt=media&#x26;token=27ff7eb3-517b-495a-80ad-ee5df76b7096" alt="" width="563"><figcaption></figcaption></figure>

#### How these settings are applied

The Portal Configuration page is applied only when no configuration is defined in the repository wiki, the repository root, or the organization settings repository (`pr-agent-settings`).

For full details about configuration precedence, see the [Configuration Overview.](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/..#configuration-precedence)

### Review settings

This section controls how Qodo performs code reviews, generates PR summaries, and displays findings in pull requests.

#### Code review

| Setting                      | Description                                                | Options                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Code review trigger**      | Determines when Qodo runs an AI code review.               | <p><strong>Manual only</strong> – Reviews run only when triggered manually using <code>/agentic\_review</code><br><strong>Published PRs</strong> – Reviews run automatically when a PR is published<br><strong>Draft & Published PRs</strong> – Reviews run automatically for both draft and published PRs</p> |
| **Comment type**             | Controls how findings are posted in the pull request.      | <p><strong>Summary only</strong> – All findings appear in a single summary comment<br><strong>Inline only</strong> – Findings are posted directly on relevant lines of code<br><strong>Summary & Inline</strong> – A summary comment is posted and findings are also added inline</p>                          |
| **Inline comment threshold** | Determines which severity levels generate inline comments. | <p><strong>High</strong> – Only high-severity findings appear inline (all findings still appear in the summary)<br><strong>Medium</strong> –  Findings above medium appear inline<br><strong>Low</strong> – Findings above low severity appear inline</p>                                                      |

Severity definitions:

* **High** findings indicate issues that require action.
* **Medium** findings are generally recommendations.
* **Low** severity findings are informational.

### PR summary

| Setting                 | Description                                              | Options                                                                                                                                                                                                                                                         |
| ----------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PR summary trigger**  | Determines when Qodo generates an AI-powered PR summary. | <p><strong>Manual only</strong> – Generated using <code>/agentic\_describe</code><br><strong>Published PRs</strong> – Generated automatically when a PR is published<br><strong>Draft & Published PRs</strong> – Generated for both draft and published PRs</p> |
| **PR summary location** | Controls where the generated summary appears.            | <p><strong>Native git description</strong> – Replaces the native PR description for the Git provider<br><strong>Standalone comment</strong> – Posts the summary as a separate comment</p>                                                                       |

### Display preferences

These settings control how findings are displayed in the pull request.

| Setting               | Description                                                                                          | Options                                                                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Finding overflow**  | Determines how many findings appear before showing a “View all” option.                              | <p><strong>None</strong> (all collapsed)<br><strong>1, 3, or 5</strong> findings shown before “View all”<br><strong>All</strong> (all findings expanded)</p> |
| **Resolved overflow** | Determines how many resolved findings appear before showing a “View all” option.                     | <p><strong>None</strong> (all collapsed)<br><strong>1, 3, or 5</strong> findings shown before “View all”<br><strong>All</strong> (all findings expanded)</p> |
| **Finding expansion** | Controls which sections are expanded by default when opening a finding. Multiple selections allowed. | **Code**, **Description**, **Relevance, Evidence, Prompt**                                                                                                   |

### Custom instructions

Add custom free-text instructions to guide how Qodo behaves.

| Setting                 | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| **Issue finding agent** | Add custom prompts to guide issue detection and reporting behavior.   |
| **Compliance agent**    | Add custom prompts to guide compliance checks and policy enforcement. |

Once your selections are made, click **Save.**
