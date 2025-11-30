# Source: https://dagshub.com/docs/feature_guide/data_science_pull_requests/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/data_science_pull_requests.md "Edit this page")

# Data Science Pull Requests[¶](#data-science-pull-requests "Permanent link")

You [discovered the experiments](../experiment_tracking/) you wanted to work on, understood what you want to do to improve them, [reproduced the results](../../use_cases/reproduce_experiment_results/) and made some modifications that improve some key metrics. Now you want to ***contribute*** that work back to the project.

## TL;DR[¶](#tldr "Permanent link")

Data Science Pull Requests is a standard way for data scientists to review data science work, and accept code, data and experiment contributions to a project. If you have a DagsHub project you will see the data science pull request upon creating a pull request in a project.

## Overview[¶](#overview "Permanent link")

**Contributing** â€" The final step of the collaborative process, is arguably the most important one. Without it, the workflow is one-sided, a monologue, which means collaboration isn\'t really happening. Practically, contributing can be broken down into two tasks - reviewing and merging contributions.

Contributing data science work is hard â€" The goal of data science pull requests is to lower friction and make it as easy as possible for two reasons:

1.  If we have a standard way to discuss and review data science, that means we don\'t need to invent custom workflows from scratch for every project, and teams can move faster.
2.  A standard process for reviewing and contributing work promotes Open Source Data Science, [which doesn\'t really exist today](https://dagshub.com/blog/a-case-for-open-source-data-science/).

To see the Data Science Pull Requests in a project or create a new one, just click the pull request tab (1) on the project\'s homepage. Once you\'re in the pull requests tab, creating a new pull request is as simple as clicking the New Pull Request (2) button and choosing which branch you want to start the pull request from.

[![Pull Request Tab](../assets/data_science_pull_requests/pull-request-tab.png)](../assets/data_science_pull_requests/pull-request-tab.png)\
~Pull\ Request\ Tab~

## Data Science Review[¶](#data-science-review "Permanent link")

[![Tab Review](../assets/data_science_pull_requests/review-tabs.gif)](../assets/data_science_pull_requests/review-tabs.gif)\
~Data\ Science\ Pull\ Request\ Tabs\ â€"\ Ready\ for\ review~

Before accepting a pull request, you\'ll probably want to review the work done by the contributor or team member. DagsHub enables a standardized, automatic way to do that by providing a few useful features, dedicated to the data science workflow.

### Experiment Review[¶](#experiment-review "Permanent link")

Before diving into the details of the files and structural changes that are up for review, we usually want to take a look at the experiment parameters and results in a data science pull request.

It might be an updated metric, an ablation test to understand the effect of a parameter on performance or a \"simple\" parameter tuning. In any case, we want to **understand** why a pull request is interesting, and what are the proposed **data science** (as opposed to just code) changes.

With experiment review you can see all the familiar views in the [DagsHub Experiments tab](../experiment_tracking/), with a few important changes.

First, the base experiment â€" the one being compared to, is marked in blue for convenience. All the experiments that are being suggested as part of the pull request appear below it for ease of comparison.

[![Experiment Compare](../assets/data_science_pull_requests/pull-request-exp-compare.png)](../assets/data_science_pull_requests/pull-request-exp-compare.png)\
~Pull\ request\ experiment\ tab\ â€"\ Note\ the\ blue\ row\ which\ is\ the\ base\ experiment~

Second, upon going into a single experiment view, or the experiment comparison view, you will see a comment box, that lets you add comments in context â€" meaning after creating the comment, it will be added to the Conversation tab, with a link to the same view â€" making it easy for team members to understand what is being discussed.

[![Experiment Comments](../assets/data_science_pull_requests/experiment-comment.png)](../assets/data_science_pull_requests/experiment-comment.png)\
~Pull\ request\ experiment\ tab\ â€"\ Comment\ box\ for\ the\ Parallel\ Coordinate\ Plot~

### Code Review[¶](#code-review "Permanent link")

Code is still an important part of data science. In the Files Changed tab of the pull request, you can see the code files changed in your project, what was added or removed in a way that focuses you on what\'s important.

However, we know that some things matter especially to data scientists â€" like working with notebooks\...

#### Notebook Review[¶](#notebook-review "Permanent link")

\...So we also added notebook diffing as part of the review process. See what changed in your notebooks in an easy to understand way.

[![Notebook Diffing](../assets/dagshub_diffing/notebook-diff.png)](../assets/dagshub_diffing/notebook-diff.png)\
~Notebook\ diffing\ in\ data\ science\ pull\ requests~

### Data & Model Review[¶](#data-model-review "Permanent link")

Reviewing code changes is necessary, but not sufficient to understand a data science project. We need data and model changes in order to get the entire picture. In the Files Changed tab, in addition to code changes (tracked in Git), you will see changes to data, models and any other artifact tracked by DVC. This means that all changes can be viewed in one place.

[![Data Diffing](../assets/data_science_pull_requests/data-diff.png)](../assets/data_science_pull_requests/data-diff.png)\
~Data\ and\ model\ files\ changed~

## Next Steps[¶](#next-steps "Permanent link")

Congratulations! you\'ve successfully completed one data science workflow cycle. Perhaps it\'s time to [discover another experiment](../experiment_tracking/) or [explore a new project](https://dagshub.com/explore) to work on?

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).