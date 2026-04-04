# Source: https://docs.envzero.com/changelogs/2025/11/code-optimizer-beta.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔧 Now Available (Beta): Code Optimizer Helps You Improve Infrastructure Code Quality and Safety

> Code Optimizer is a new beta feature in env zero that scans your Infrastructure as Code and helps you catch issues early, before they cause problems in production. It detects risks, flags inconsistencies, and suggests code-level improvements you can review and apply.

**Code Optimizer** is a new beta feature in env zero that scans your Infrastructure as Code and helps you catch issues early, before they cause problems in production. It detects risks, flags inconsistencies, and suggests code-level improvements you can review and apply.

Instead of relying on manual reviews or post-incident cleanup, Code Optimizer offers a faster, more proactive path to better infrastructure code.

<Frame caption="Code Optimizer dashboard showing detected issues">
  <img src="https://mintcdn.com/envzero-b61043c8/r1hfz_udZgUmpFfC/images/changelogs/2025/11/code-optimizer-issues.png?fit=max&auto=format&n=r1hfz_udZgUmpFfC&q=85&s=5ccad0589b410b47f779b7c4c83929c9" alt="Code Optimizer provides detailed analysis and lists all detected issues with severity levels" width="1600" height="934" data-path="images/changelogs/2025/11/code-optimizer-issues.png" />
</Frame>

## What's included in the beta

* Run scans manually from development environments
* Detect potential issues like hardcoded values, overly permissive access, or weak defaults
* View which environments may be affected by an issue
* Generate pull requests with suggested code fixes
* Track, ignore, or resolve issues with built-in controls

<Frame caption="Issue details and affected environments">
  <img src="https://mintcdn.com/envzero-b61043c8/r1hfz_udZgUmpFfC/images/changelogs/2025/11/code-optimizer-issue-details.png?fit=max&auto=format&n=r1hfz_udZgUmpFfC&q=85&s=7e2e604b4a0a40a243fe83a54e4118a4" alt="Detailed view of an issue showing the resource, file, repository, severity, and relevant environments" width="534" height="758" data-path="images/changelogs/2025/11/code-optimizer-issue-details.png" />
</Frame>

## Powered by familiar tools, enriched with context

Code Optimizer runs scanning tools like Checkov and TFLint under the hood, but with full awareness of your environments, modules, and infrastructure history. That context makes findings more relevant and fixes easier to trust.

## Beta limitations

* Scanning and detection: GitHub, GitHub Enterprise, GitLab Enterprise, and Bitbucket Server are supported
* Code fix creation: GitHub and GitHub Enterprise are supported
* Environment mapping is based on code paths (not yet plan or state aware)

## What's coming next

* More VCS provider integrations
* Expanded scan coverage
* Future features like runtime insights and state validation

<Tip>
  Learn more in the [Code Optimizer documentation](/guides/policies-governance/code-optimizer/overview) or get the details on the [blog](https://www.env0.com/blog).
</Tip>

Built with [Mintlify](https://mintlify.com).
