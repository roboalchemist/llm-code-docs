# Source: https://docs.ox.security/automate-with-ox-workflows/ox-automations/ox-onboarding.md

# Before You Begin Setting Up Workflows

Before you begin creating workflows in OX, make sure your environment is fully connected, cleaned up, and aligned with your actual development practices.

Workflows are only as reliable as the data they depend on, for example, visibility of applications, repositories, and issues.

Confirm that your environment is complete, accurate, and prioritized before enabling automation. If something is missing or misconfigured, automation will not behave as expected.

Once you have completed this checklist and are confident that OX reflects your actual infrastructure, you are ready to begin configuring workflows.

## Step 1. Connect All Relevant Systems

Start by connecting your source control, ticketing tools, and registries. Simply connecting isn’t enough, you must confirm that what OX shows matches your real environment.

* Verify that all repositories are connected and visible.
* Check that critical applications are present, not just default or random selections.
* Confirm that tickets can be created in the correct project space in Jira or your issue tracker.

## Step 2. Verify Applications

Go to the Applications page and review the repositories grouped under each application.

* Confirm that your business-critical applications are present.
* Remove or clean up old, irrelevant applications.
* Ensure no high-priority projects are missing.

Applications may disappear or shift due to naming patterns or tagging logic, for example, a repo named `internal-service` might be filtered out.

Verify that application visibility reflects your real-world priorities.

## Step 3. Uncover Hidden Gaps

This stage often reveals problems teams didn’t know existed.

* Entire teams (e.g., offshore development centers) may not have been connected. Adding them can expose previously invisible issues.
* Legacy files or outdated services may surface, sometimes with security issues from years ago.
* Cleaning up may take multiple rounds, especially when onboarding teams from different business units.

## Step 4. Handle False Positives Early

Flagging false positives early is essential. They influence how workflows behave later.

* Use the false positive flag where necessary.
* Reach out to the OX research team for review; sometimes a suspected false positive is actually valid under best practices.
* Remember that flagged results may be updated only for your environment or applied globally, depending on the case.

## Step 5. Align Ticketing

Ensure your ticketing system is connected and configured correctly.

* Verify the connection points to the right Jira project space or equivalent tracker.
* Review repository mapping and permissions; misconfiguration is common.
* Confirm that OX can assign, update, and track tickets without manual intervention.

## Step 6. Finalize Setup Before Workflows

Before creating workflows, double-check that OX has an accurate and complete view of your environment:

* Review filters, naming conventions, and business priority tagging.
* Confirm that applications contain actual code. Repositories with only graphics or binaries will not generate issues.
* Remember, only administrators can configure workflows. If something is missing from the application or repository list, it cannot trigger a workflow.
* Assign business priorities to applications. This directly influences workflow conditions such as SLA, severity, and blocking behavior.
* Understand that production-facing repos should be treated differently from sandbox or test code. For example, an API issue in production must escalate faster than the same issue in a staging repo.

## Pre-Workflow Checklist

Use this checklist to verify that your environment is correctly prepared before you start configuring workflows.

Go through each area, confirm the items are complete, and mark the Status column so your team has a clear record of readiness.

| Area                  | What to Check                                                                                           | Status (✔/✘) |
| --------------------- | ------------------------------------------------------------------------------------------------------- | ------------ |
| **Source Control**    | All repositories connected; critical repos selected; no missing or wrongly mapped projects.             |              |
| **Applications**      | Applications grouped correctly; irrelevant ones removed; all high-priority apps visible.                |              |
| **Business Priority** | Priorities set correctly in the Applications page; staging/test repos not tagged as production.         |              |
| **Legacy Code**       | Old, irrelevant, or unused code excluded; false positives flagged and reviewed with the research team.  |              |
| **Ticketing System**  | Jira/issue tracker connected; repository mapping and permissions correct; tickets route to right space. |              |
| **Workflow Control**  | Only admins edit workflows; verify repo visibility; repos with no code excluded; new repos selected.    |              |
