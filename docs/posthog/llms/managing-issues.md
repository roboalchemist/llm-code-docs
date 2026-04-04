# Source: https://posthog.com/docs/error-tracking/managing-issues.md

# Manage and resolve issues - Docs

Error tracking gives you multiple ways to help you manage issues and work towards resolution.

## Update issue status

You can update the status of an issue from the issue page under **Status** or issue list.

All issues are marked **Active** by default. You can update the status to reflect the current state of the issue:

-   **Active** - The default status for new issues. Use this for issues that need attention.
-   **Resolved** - Mark issues that are fixed. If the issue reoccurs, it's automatically reopened.
-   **Suppressed** - Mark issues you choose not to action. Typically used for noisy or unhelpful issues. Note that suppressing an issue will drop any associated exceptions.

You can also filter issues by status in the issue list:

![Error tracking filter by issue status](https://res.cloudinary.com/dmukukwp6/image/upload/filter_by_status_light_1f57d7d0b1.png)![Error tracking filter by issue status](https://res.cloudinary.com/dmukukwp6/image/upload/filter_by_status_dark_f48d183989.png)

A common workflow is to look for all issues that are **Active** assigned to you or your team, and triage them to be fixed or suppressed.

## View stack traces and event properties

Each issue contains detailed information about the exceptions that triggered it.

Click the **Stacktrace** tab to see exactly where the error occurred. [Stack traces](/docs/error-tracking/stack-traces.md) help you pinpoint the line of code and the sequence of function calls leading up to the exception.

![Error tracking stack traces](https://res.cloudinary.com/dmukukwp6/image/upload/issues_stacktrace_light_8e0c699ca2.png)![Error tracking stack traces](https://res.cloudinary.com/dmukukwp6/image/upload/issues_stacktrace_dark_0b00f2d4fd.png)

Under the **Properties** tab, you can view additional metadata about the exception event.

![Error tracking event properties](https://res.cloudinary.com/dmukukwp6/image/upload/issues_properties_light_6fa900f42e.png)![Error tracking event properties](https://res.cloudinary.com/dmukukwp6/image/upload/issues_properties_dark_e973d3dfb2.png)

## Watch session replays

Error tracking works with [session replays](/docs/session-replay.md) to help you understand the context of an issue. This is useful for reproducing and debugging issues.

You can view a session replay for an exception by:

-   Selecting an exception in the exception list and clicking the **Session** tab at the top of the page.
-   Clicking the **View recording** button besides each exception.

![An issue's session replay](https://res.cloudinary.com/dmukukwp6/image/upload/session_replay_error_light_5f25f72344.png)![An issue's session replay](https://res.cloudinary.com/dmukukwp6/image/upload/issue_exception_with_filter_dark_bf74dca1d9.png)

## Discover errors from logs

Error tracking issues can also be discovered from the [Logs](https://app.posthog.com/logs) viewer. When [logs are linked to sessions](/docs/logs/link-session-replay.md), related errors can be viewed in the **Related errors** tab of any log entry. This is useful for investigating backend issues where both logs and errors were captured during the same session.

## Assign issues to teammates

Issues can be [assigned to a teammate](/docs/error-tracking/assigning-issues.md) from the list or issue page. To do this, select the **assignee** option and search for the teammate you want to assign it to, and select them. You can click this dropdown again to remove the assignee.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better