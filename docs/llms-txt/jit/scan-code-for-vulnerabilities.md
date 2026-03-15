# Source: https://docs.jit.io/docs/scan-code-for-vulnerabilities.md

# Static Application Security Testing (SAST)

## Jit Static Application Security Testing (SAST): Key things to know

* **Brief description:** Jit SAST scans your custom code for security flaws that could lead to vulnerabilities if deployed, depending on the runtime context of the code.
* **Scanning process:** Scanning takes place periodically across your entire codebase (or selected repositories), and during every code change introduced by your developers.
* **How to get started:** Jit SAST is automatically activated when you onboard Jit, which scans your selected repos/projects and records security findings in the [Findings Page](https://docs.jit.io/v5.0/docs/jit-findings), while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* **Based on Semgrep:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For SAST, we use Semgrep and GoSec to run the analyses, which are used by thousands of engineering teams. We've added custom Semgrep rules and tweaked noisy rules to improve scanning efficacy and reduce false positives. Learn more about Semgrep [here](https://github.com/semgrep/semgrep).
* **Test Jit SAST:** Test Jit SAST by creating a pull request in GitHub or merge request in GitLab with these deliberately insecure code snippets in [Python](https://docs.jit.io/docs/code-samples#scan-code-for-vulnerabilities-go), [Javascript](https://docs.jit.io/docs/code-samples#scan-code-for-vulnerabilities-javascript), and [Go](https://docs.jit.io/docs/code-samples#scan-code-for-vulnerabilities-go). Jit provides security feedback before the code is merged.

## User Experience

### Security Team UX in the Jit Web App

**Detect existing code security vulnerabilities**\
Jit SAST continuously scans your codebase to highlight code security vulnerabilities (categorized as "CWEs").

* Navigate to the Findings page filter by "**Finding type**" : "**SAST**".

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ac02b453af13b998b423ab17469ee2066b08f1c23f8cdbcfb59903e9c48c1452-Screenshot_2026-01-19_at_15.03.12.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* In many environments, there can be thousands of code vulnerabilities. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).

**Investigating and triaging code security issues**

Open up a code security issue in order to:

* See helpful information like its location, resources to learn about the issue, and its Knowledge Graph, which shows the runtime context of the issue.
* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.

**Remediate SAST-detected issues**

* Create a fix PR from within Jit to address the issue immediately.

<br />

### UX for developers

Developers never need to leave their coding environment to identify and resolve SAST-detected security issues.

* When Jit SAST is enabled for a given GitHub repository or GitLab project, it will automatically scan every code change and provide immediate code security feedback within the developer environment.
* Jit SAST supports auto remediation for many vulnerabilities. Suggested code fixes are provided within the code change, and can be applied with a click without creating a new pull request/merge request.
* Remediation in a Pull Request whereby the suggested code is displayed in the PR itself, and the developer can accept it by clicking **Commit suggestion**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/beba71d-image_28.png",
        "",
        "Inline Remediation in a Pull Request"
      ],
      "align": "center",
      "border": true,
      "caption": "Inline Remediation in a Pull Request."
    }
  ]
}
[/block]

## Language Support

| Language   | Tool                                               | Detection | Remediation |
| :--------- | :------------------------------------------------- | :-------- | :---------- |
| JavaScript | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| TypeScript | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| Python     | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| Go         | [Gosec](https://github.com/securego/gosec)         | Yes       | -           |
| Java       | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| Scala      | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| Kotlin     | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| PHP        | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | -           |
| C#         | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| Swift      | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | Yes         |
| Rust       | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | -           |
| C          | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | -           |
| C++        | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | -           |
| Ruby       | [Semgrep](https://github.com/returntocorp/semgrep) | Yes       | -           |