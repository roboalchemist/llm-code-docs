# Source: https://typescript-eslint.io/maintenance/issues

On this page# IssuesThis document serves as a guide for how you might manage our [GitHub Issues](https://docs.github.com/issues), also known as issue triaging.
Use your best judgement when triaging issues, and most of all remember to be **encouraging, friendly, and kind** when responding to users.
Many users are new to open source and/or typed linting.
It&#x27;s imperative we give them a positive, uplifting experience.
tipIf you&#x27;re ever unsure on any part of issue management, don&#x27;t hesitate to loop in a maintainer that has more context to help!
## Governance[​](#governance)
Per the scales from [Contribution Tiers > Pointing](/maintenance/contributor-tiers#pointing):
- Straightforward: at reviewer discretion, may be marked as approved by any committer or maintainer.
This includes docs enhancements, bug fixes, and feature additions.
- Non-straightforward: may be marked as approved with either two committer approvals or one maintainer approval.
These include significant internal refactors and non-breaking public API changes.
- "Unusual"-categorized: require a public discussion followed by two maintainer approvals.
These include significant refactors with cross-project and public API ramifications.
## Issue Flow[​](#issue-flow)
noteWe include a set of common responses to issues in [`.github/replies.yml`](https://github.com/typescript-eslint/typescript-eslint/blob/main/.github/replies.yml), intended to be used with the [Refined Saved Replies](https://github.com/JoshuaKGoldberg/refined-saved-replies) extension.
Don&#x27;t treat these as exact responses you must use: they&#x27;re just a starting copy+paste helper.
Please do adopt your specific responses to your personal tone and to match the thread for non-straightforward issues.
[Issues pending triage](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aopen+is%3Aissue+label%3Atriage) are searchable with the `triage` label.
That label is added automatically when a new issue is created.
Most issues go through the following review flow when created or updated:
- A maintainer ensures the issue is valid:
If the poster didn&#x27;t fill out an appropriate template with enough information:
Add the `please fill out the template` and `awaiting response` labels, and remove the `triage` label
- Ask the poster for more information using a *Needs More Info* response
- If it&#x27;s a duplicate of an issue that already exists:
Add the `duplicate` label and remove the `triage` label
- If it&#x27;s an obvious duplicate, post a *Clearly Duplicate Issue* response linking to the existing issue
- If it&#x27;s not an obvious duplicate, link to the existing issue and explain why
- Close the issue as *not planned*
- If the code is working as intended:
Add the `working as intended` label and remove the `bug` and `triage` labels
- If the behavior is due to the user doing something wrong, such as an incorrect config:
Add the `fix: user error` label
- [This issue search has some examples of closing comments](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aissue+sort%3Aupdated-desc+label%3A%22fix%3A+user+error%22+is%3Aclosed)
- If the behavior is otherwise expected, [this issue search has some examples of closing comments](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aissue+sort%3Aupdated-desc+label%3A%22working+as+intended%22+-label%3A%22fix%3A+user+error%22+is%3Aclosed+)
- You needn&#x27;t go into too much detail in your comment - just enough to explain it
- Close the issue as *not planned*
- If issue contains an enhancement-like request that is unlikely to be implemented on the typescript-eslint side:
Add the `wontfix` label and remove `triage` label
- [Issue search with some examples of closing comments](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aissue+sort%3Aupdated-desc+label%3Awontfix+is%3Aclosed)
- If there&#x27;re any alternatives or approaches to meet the request, it would be nice to suggest them
- Close the issue as *not planned*
- If the issue requires further discussion or community engagement evaluation:
Add the `evaluating community engagement` label and remove the `triage` label
- If the report is valid:
Remove the `triage` label
- Add the `team assigned` label if you think only a member of the team should tackle it, or `accepting prs` if anybody could
- If you know the rough steps for a fix, consider writing a comment with links to codebase to help someone put together a fix
- If you think that the fix is relatively straightforward, consider also adding the `good first issue` label
Whenever an issue is waiting for the reporter to provide more information, it should be given the `awaiting response` label.
When more information is provided:
- If you have time to go through the triage flow again, do so
- If you don&#x27;t have time, add the `triage` label and remove the `awaiting response` label
tipIf your link is both a "permalink" (includes a commit hash instead of a branch name) and has a line number/line range then GitHub will embed the code in your comment.
When viewing a file in GitHub pressing `y` will update the URL to a "permalink" with the current commit hash, then you can select the relevant lines and paste that URL into the comment.
### Looking for Duplicates[​](#looking-for-duplicates)
It&#x27;s worth noting that, occasionally, a user will intentionally raise a duplicate issue because they feel the original issue was closed when it shouldn&#x27;t have been.
If this is the case, you should read the original issue to gather context, understand the reason for it being closed, and determine if the new issue raises any new or relevant point that requires addressing.
### Determining Whether Code is Working As Intended[​](#determining-whether-code-is-working-as-intended)
As you become more familiar with the codebase and how everything works, this will be easier to do intuitively, but to begin with, this will likely involve investigating the documentation, code, and tests to determine if it&#x27;s a bug or working as intended.
In general, if there is a passing test or documented example that is the same as or similar to the repro code — that indicates it&#x27;s working as intended.
If you can&#x27;t find anything that matches, use your best judgement based on the spirit of the code.
### Community Engagement Evaluation[​](#community-engagement-evaluation)
In most cases, maintainers have a pretty good idea of how people write code and what most users of the typescript-eslint tooling want.
However, there are cases when maintainers can&#x27;t confidently choose the most reasonable approach to solving a particular problem:
- The issue subject relates to a library/framework that the maintainers are not familiar with. Therefore, they don&#x27;t know the idiomatic patterns associated with it.
- There is a new syntax or a new feature - sometimes it&#x27;s hard to guess how people might use that feature.
- The issue was about to be closed, but someone made a compelling argument. This requires further discussion to find a viewpoint that most people agree on.
3-6 months after the issue is labeled `evaluating community engagement`, the engagement of community is evaluated:
- If the community was active and common ground was found, the issue is labeled as `accepting prs` or `team assigned`
- Otherwise, the issue is closed as *not planned* with the `wontfix` label
For requests that can be implemented outside of typescript-eslint, be sure to mention any relevant APIs such as [Custom Rules](/developers/custom-rules) that can be used.
## Skipping Steps[​](#skipping-steps)
As you become more familiar with the codebase and how it&#x27;s supposed to behave you&#x27;ll be able to skip steps or do things out of order as you see fit.
For example, you may be able to identify if a bug report is "working as intended", or you might recognize an issue as a duplicate without having a completely filled-out issue.
In such cases you can forgo the back-and-forth and just skip to the closing steps.
## Specific Issue Types[​](#specific-issue-types)
### 🐛 Bug Reports[​](#-bug-reports)
#### 🐞 "Simple" Bugs[​](#-simple-bugs)
A simple bug is a bug that can be reproduced in a single TS file plus an ESLint config (and possibly a TSConfig) - i.e. an issue reproducible on [our playground](/play).
The vast majority of bug reports fall into this category.
If you cannot reproduce the issue as described using the issue&#x27;s provided playground reproduction, it has not provided enough information.
Consider using a specific response like the *Needs Playground Reproduction* response.
#### 🦟 "Complex" Bugs[​](#-complex-bugs)
A complex bug is a bug that requires multiple files to reproduce.
This is the rarer case, but does happen when people are using library types or if there are issues when types are imported.
These bugs should be reported with a link to a GitHub repository that can be checked out to reproduce the issue.
If you cannot reproduce the issue as described using repository&#x27;s README.md and issue description, it has not provided enough information.
Consider using a specific response like the *Needs Full Reproduction* response.
### 🏗 Feature Requests[​](#-feature-requests)
For any feature request, make sure the requested support is either:
- Very useful for at least one commonly used way to run TypeScript (e.g. tsc-built CLI package; bundler-managed web app)
- Relevant for *most* projects that would be using typescript-eslint
We avoid features that:
- Are only relevant for a minority of users, as they aren&#x27;t likely worth the maintenance burden
- Aren&#x27;t TypeScript-specific (e.g. should be in ESLint core instead)
- Are only relevant with specific userland frameworks or libraries, such as Jest or React
- Are for "formatting" functionality (we [strongly recommend users use a separate dedicated formatter](/users/what-about-formatting))
#### ✨ Rule Enhancements[​](#-rule-enhancements)
We&#x27;re generally accepting of rule enhancements that meet the above feature request criteria.
If a rule enhancement would substantially change the target area of the rule, consider whether it should instead be a new rule.
Common signs of this are the rule&#x27;s original name now being inaccurate, or some options being relevant just for the old functionality.
Enhancements that can cause new reports to be reported are considered breaking changes.
We have two common strategies for them:
- Treat the enhancement as a breaking change, and block merging it until the next major version
- Add an option to disable the new logic: which is a breaking change if opt-in, and a non-breaking change if opt-out
- Add an option to enable the new logic: which is a breaking change if opt-out, and a non-breaking change if opt-in
See [Can we standardize logical direction of rule options?](https://github.com/typescript-eslint/typescript-eslint/discussions/6101) for context on naming options.
For enhancements meant to limit which kinds of nodes the rule targets, mark the issue as blocked on [RFC: Common format to specify a type or value as a rule option](https://github.com/typescript-eslint/typescript-eslint/discussions/6017).
#### 🚀 New Rules[​](#-new-rules)
We&#x27;re generally accepting of new rules that meet the above feature request criteria.
The biggest exception is rules that can roughly be implemented with [`@typescript-eslint/no-restricted-types`](/rules/no-restricted-types) and/or [`no-restricted-syntax`](https://eslint.org/docs/latest/rules/no-restricted-syntax).
## Pruning Old Issues[​](#pruning-old-issues)
Every so often, we like to [search for open issues `awaiting response`](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aopen+is%3Aissue+label%3A%22awaiting+response%22) to find ones that might have been forgotten.
Our flow for issues that have been waiting for >=1 month is:
- Ping the author with a message like the *Checking In* template
- Add the `stale` label to the issue
- Wait 2 weeks
- If they still haven&#x27;t responded, close the issue with a message like the *Pruning Stale Issue* template
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/maintenance/Issues.mdx)- [Governance](#governance)- [Issue Flow](#issue-flow)[Looking for Duplicates](#looking-for-duplicates)- [Determining Whether Code is Working As Intended](#determining-whether-code-is-working-as-intended)- [Community Engagement Evaluation](#community-engagement-evaluation)- [Skipping Steps](#skipping-steps)- [Specific Issue Types](#specific-issue-types)[🐛 Bug Reports](#-bug-reports)[🐞 "Simple" Bugs](#-simple-bugs)- [🦟 "Complex" Bugs](#-complex-bugs)- [🏗 Feature Requests](#-feature-requests)[✨ Rule Enhancements](#-rule-enhancements)- [🚀 New Rules](#-new-rules)- [Pruning Old Issues](#pruning-old-issues)