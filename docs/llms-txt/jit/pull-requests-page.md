# Source: https://docs.jit.io/docs/pull-requests-page.md

# Pull Requests

## Overview

The Pull Requests page enables you to track pull requests (PRs) of interest and get a high-level summary of the pull requests activity in your organization over a certain period of time (default is two weeks). The Pull Requests page provides the following benefits:

1. At-a-glance identification of ongoing issues with PRs.
2. Compliance verification (SOC2, Iso, etc).

Additionally, this view helps you identify PRs with security vulnerabilities that are either taking too long to fix, or are being hastily merged back into code without sufficient attention.

![](https://files.readme.io/dc5a3ae-Untitled.png)

## Pull Request Statistics

The following statistics display at the top of the page:

![](https://files.readme.io/2977581-Untitled.png)

* **Failed PRs** ⁠— The number of pull requests that contain security findings, and the relative change in this value compared to a point in time exactly two weeks in the past. Mouse over to view the percentage of open PRs that contain security findings, and the number of repositories (compared to the total scanned) that contain security findings.
* **Passed PRs** ⁠— The number of pull requests that do not contain security findings, and the relative change in this value compared to a point in time exactly two weeks in the past. Mouse over to view the percentage of open PRs that do not contain security findings.

## Pull Requests of Interest

This page also lists PRs that you should be aware of, organized into the following categories:

![](https://files.readme.io/be7d246-Untitled.png)

* **Merged with Security Findings** — This list contains PRs that were merged to your main branch with security findings.
* **Merged with Ignored Findings** — This list contains PRs that were merged to your main branch with ignored security findings.
* **Open with Findings** — This list contains PRs that are currently open with security findings. PRs that have been open with findings for more than three days are marked as *stale*.
* **Merged with Fixed Findings** — This list contains PRs that were merged to your main branch with fixed security findings.

Each category displays at-a-glance statistics, including the total number of PRs and the relative change in this value compared to a point in time exactly two weeks in the past.

### Viewing pull requests of interest

Select a PR category to view its associated PRs in a vertical list on the left side of the page. To view the PR in the SCM, select the PR name.