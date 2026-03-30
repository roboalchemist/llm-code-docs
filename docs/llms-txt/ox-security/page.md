# Source: https://docs.ox.security/automate-with-ox-workflows/page.md

# Workflow Execution Logs

Workflow execution logs display the results of recent automatic and manual workflows based on the period selected in the page header.

From the menu pane, go to **Workflows > Workflows Execution Logs**.

Use this page to:

* Verify that scheduled workflows or scans ran successfully.
* Investigate a failed or skipped workflow.
* Monitor performance or frequency of automation runs.

## Prerequisites

Ensure that there is at least one regular workflow or pipeline workflow.

## Triggers, conditions and actions

For detailed information workflow triggers, conditions and actions, see these articles:

* [Workflow Triggers](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-triggers)
* [Workflow Conditions](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-conditions)
* [Workflow Actions](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-actions)

## Workflow execution statuses

The execution statuses are:

Success, Failed, Partial, Suppressed (temporarily disabled).

## Log details

The page includes the following elements:

* **Filters:** Single or multi-select filters including a filter by period. The filters only show options for workflows completed in the selected period.
* **Summary metrics:** Shows the total workflow count.
* **Execution list:** Displays details for each workflow run.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-096a300857934dfa4ecfa61e009ca30234945f8f%2Fox%20audit%20log%20page%20main%20screen.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="158" valign="top">Element</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Period filter<br>(in the header)</td><td valign="top">Filters the results to the selected period.</td></tr><tr><td valign="top">Total</td><td valign="top">Displays the total number of workflows based on the applied filters.</td></tr><tr><td valign="top">Search bar</td><td valign="top">Enter text to search for a specific term.</td></tr><tr><td valign="top">Filters</td><td valign="top"><p>Select one or multiple filters:</p><ul><li>Job Type</li><li>Action Name</li><li>Workflow Name: Examples: Default Workflow; Jira Ticket etc.</li><li>Execution Status: Examples: Suppressed, Success, Failed, Partial.</li></ul></td></tr><tr><td valign="top">Workflow details</td><td valign="top"><p>Use the tooltips to identify icons.<br></p><ul><li><strong>Trigger:</strong> Examples: Trigger, Manual Ex.</li><li><strong>Workflow Name</strong></li><li><strong>Action:</strong> Examples: Alert Pipeline, Slack Message to parameter @[email].</li><li><strong>Status:</strong> Examples: Suppressed, Success, Failed, Partial.</li><li><strong>Details:</strong> Description of success / failure.</li><li><strong>Issues:</strong> Shows the number of related issues. Click to view the issues.</li><li><strong>Execution Summary icon:</strong> Use the tooltip to see the description.</li><li><strong>App:</strong> The application name.</li><li><strong>Executed at:</strong> The time the workflow was executed.</li></ul></td></tr></tbody></table>
