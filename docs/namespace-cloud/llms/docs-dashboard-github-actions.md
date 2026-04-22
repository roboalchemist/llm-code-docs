<!-- Source: https://namespace.so/docs/dashboard/github-actions -->

# GitHub Actions Overview

In the GitHub Actions Overview, you can see at a glance the performance and reliability of your CI Workflows.

## Workflows per repository

On the homepage of the overview, you'll find all of your workflows.
They are grouped by repository, and show the status of recent runs as well as the duration of these workflows over time.

![GitHub actions overview showing different jobs for a repository including runtime progression over time](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgithub-actions-overview.d072b780.png&w=1920&q=75)

## Workflow

On top of the Workflow page, a few graphs give a quick impression of the health of this workflow.

- The grid of checkmarks shows runs and whether they succeeded or not, this allows you to quickly spot flakiness or find what commit caused it to fail.
- The duration graph shows the duration of the last job, and the progression over time. This is useful to spot performance regressions and possible optimizations.
- The success rate is another important indicator of the healthiness of a workflow, showing you if reliability has changed.

Underneath you'll find a list of recent workflow runs, including currently running ones. Here you can quickly jump into a specific run.

![GitHub Workflow page showing different runs, success rate and duration over time](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgithub-actions-workflow.10274a1b.png&w=1920&q=75)

## Workflow Jobs

The Workflows Jobs page shows you information about the commit or action that triggered this job,
and it shows all individual jobs that ran.

In the trace, you can see how long each job took and which jobs depend on each other.
This allows you to quickly identify the critical paths where performance improvements will be most impactful.

![GitHub Workflow trace showing step duration and dependencies](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgithub-actions-trace.4dc41d5b.png&w=1920&q=75)

## Job view

The dedicated job view allows correlating job steps with performance metrics and comparing a job's performance to previous runs.
This visibility helps you identify performance bottlenecks and track improvements over time.

More information about how you can use this view to [Debug GitHub Actions](/docs/solutions/github-actions/debugging)

![Runner metrics](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnermetrics.faf03497.png&w=1200&q=75)

The **previous runs** panel allows you to compare the performance of the current run to the recent history of this job.

Unlike traditional GitHub Actions, Namespace provides direct access to logs from running containers within your workflows.

![Container Logs](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftestcontainerlogs.f785750e.png&w=1200&q=75)

**Metrics correlation**
Namespace also collects and retains step logs, too. When hovering over a step, you can easily correlate it with the associated instance metrics.

![Step metric correlation](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsteplogsmetrics.d4509a81.png&w=1200&q=75)

Last updated July 4, 2025
