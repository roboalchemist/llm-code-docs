# Source: https://buildkite.com/docs/pipelines/insights/waterfall.md

# Waterfall view

Waterfall view allows you to see build data as a waterfall chart, providing enhanced visibility into your build's job processes, durations and dependencies.

To access waterfall view:

1. Navigate to any build page.
1. Select **View**.
1. Select **Waterfall** from the dropdown menu.

<img alt="Image of an example waterfall chart" src="/docs/assets/waterfall-view-DLHVAw8m.png" />

Waterfall view only displays data for finished steps. If a finished step has jobs that are canceled, timed out, expired or skipped, the row will render as blank for those jobs. Wait, block, and input steps are not included in the chart.

Most rows will show bars with three colored sections:

1. Gray: time the job spent waiting for an agent to be assigned.
1. Yellow: time elapsed since the agent was assigned, up until the time the agent started running the job.
1. Green or Red: time the agent spent running the job. Displayed as green for a **passed** job or red for a **failed** job.

You can hover over a bar to view these durations. Time is rounded to the nearest second.

<img alt="Image of a waterfall popover, displaying the job&#39;s waiting, dispatching and running durations" src="/docs/assets/waterfall-view-popover-CTueA5EV.png" />

Group, matrix and parallel steps are shown with nested rows underneath a 'parent' row. A parent row displays a solid bar representing the total duration of its child rows. The bar is green if all child rows passed, and red if any of them failed.

<img alt="Image showing an example of a parent row and its children in a waterfall chart" src="/docs/assets/waterfall-view-parent-row-RT2CpAmu.png" />

> 📘 Build time discrepancies in the waterfall view
> Although canceled jobs appear as a blank line in the waterfall view, their duration still contributes to the total build time. For example, if a job ran for 20 minutes and was then canceled, that job will appear as a blank line in the waterfall view, but contributes 20 minutes to the total build time.
