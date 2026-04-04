# Source: https://docs.jit.io/docs/scan-code-for-hard-coded-secrets.md

# Secrets Detection

## Key things to know about Jit Secrets Detection

* **Brief description:** Scan your codebase for hardcoded secrets like cloud tokens, API keys, and passwords.
* **Scanning process:** Scanning takes place periodically across your entire codebase (or selected repositories), and during every code change introduced by your developers.
* **How to get started:** Jit Secrets Detection is automatically activated when you onboard Jit, which scans your selected repos/projects and records security findings in the [Findings Page](https://docs.jit.io/v5.0/docs/jit-findings), while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* **Based on GitLeaks and Trufflehog:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For Secrets Detection, we provide the option to use GitLeaks or Trufflehog — automatically orchestrating these scanners so you don't have to configure or run them yourself.
* **Test Jit Secrets Detection:** Test Jit Secrets Detection by creating a pull request in GitHub or merge request in GitLab with this deliberately insecure [code snippet](https://docs.jit.io/docs/code-samples#scan-code-for-hard-coded-secrets-multi-languages). Jit provides security feedback before the code is merged.
* **Language agnostic**: Jit Secrets Detection can detect hardcoded secrets in any programming language.

## User Experience

### UX for Security Teams

Security Teams can view hardcoded secrets across the entire codebase — unified alongside all other product security issues.

**Prioritizing the riskiest hardcoded secrets**

* Navigate to the Findings page filter by "**Finding type**" : "**Secret Detection**"

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/77aa516ec7eb7117f2f0475c3933bb1ecbc897a35f684bbbbbc23a98156bbafd-Screenshot_2026-01-19_at_17.22.34.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* In many environments, there can be thousands of hardcoded secrets. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).

**Investigating, triaging, and remediating hardcoded secrets**

Open up a hardcoded secret in order to:

* See helpful information like its location, resources to learn about the issue, and its Knowledge Graph, which shows the runtime context of the issue.
* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.
* Create a fix PR from within Jit to address the issue immediately.

### UX for developers

Developers never need to leave their coding environment to identify and resolve hardcoded secrets in their code.

* When Secrets Detection is enabled for a given GitHub repository or GitLab project, it will automatically scan every code change and provide immediate code security feedback within the developer environment.
* The issue can be resolved without having to create a new Pull Request.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cb7ff507184622578887fb5e7ec55ecd89be8c3c81e5fb3131d09edb6ba1154d-3fa2374-Screen_Shot_2022-07-15_at_8.52.19.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

<br />

## Orchestrate Gitleaks or TruffleHog

By default, Jit scans for secrets using Gitleaks. Alternatively, you can enable TruffleHog.

### Configure via the Plan page

Jit manages the secrets scanning tool selection through the Plan UI.

**New setup**\
1\.	Go to Plan.\
2\.	Click **Scan code for hard-coded secrets**.\
3\.	When enabling the control, choose the scanning tool:\
•	**Gitleaks**\
•	**TruffleHog**

**Existing setup**\
If **Scan code for hard-coded secrets** is already enabled:\
1\.	Go to Plan.\
2\.	Click **Scan code for hard-coded secrets**.\
3\.      Click **Configure**.\
4\.	Update your tool selection if needed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/338d8465df5dc57c297bd4c36df610689e322176b50e40d69f3a9715dcf55279-Screenshot_2026-01-19_at_17.24.40.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

> 📘 Additional information
>
> * By default, TruffleHog creates findings for all detected secrets and tags them with `Verified` or `Unverified`. If you use the `verified` toggle, Trufflehog will **not** create findings for **unverified** secrets.