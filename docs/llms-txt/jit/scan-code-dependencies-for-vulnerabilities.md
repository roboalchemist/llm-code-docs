# Source: https://docs.jit.io/docs/scan-code-dependencies-for-vulnerabilities.md

# Software Composition Analysis (SCA)

## Jit Software Composition Analysis (SCA): Key things to know

* **Brief description:** Jit SCA scans your open source code and dependencies for known vulnerabilities — including insecure open source components being committed in the PR and zero day vulnerabilities discovered in components that have already been deployed in your environment.
* **Scanning process:** Scanning takes place periodically across your entire codebase (or selected repositories), and during every code change introduced by your developers.
* **How to get started:** Jit SCA is automatically activated when you onboard Jit, which scans your selected repos/projects and records security findings in the [Findings Page](https://docs.jit.io/v5.0/docs/jit-findings), while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* **Based on OSV Scanner:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For SCA, we use OSV Scanner to run the analyses, which are used by thousands of engineering teams.
* **Vulnerability database**: Jit SCA inventories open source components across your codebase and cross references them with the [OSV Advisories Database](https://osv.dev/list), which includes CVEs documented in multiple databases including GitHub Security Advisories, the National Vulnerability Database (NVD), and other community sources.
* **Test Jit SCA:** Test Jit SCA by creating a pull request in GitHub or merge request in GitLab with these deliberately insecure code snippets in [Node](https://docs.jit.io/docs/code-samples#scan-code-dependencies-for-vulnerabilities-node) and [Python](https://docs.jit.io/docs/code-samples#scan-code-dependencies-for-vulnerabilities-python). Jit provides security feedback before the code is merged.

## Language and package manager support

| Language   | Package manager | Tool                                                 | Detection | Fix guidelines |
| :--------- | :-------------- | :--------------------------------------------------- | :-------- | :------------- |
| JavaScript | npm             | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | Yes            |
| JavaScript | pnpm            | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | Yes            |
| Python     | pip             | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | Yes            |
| Python     | Poetry          | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | Yes            |
| PHP        | Composer        | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | Yes            |
| Go         | dep, go mod     | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | -              |
| C#         | Nuget           | [Trivy](https://github.com/aquasecurity/trivy)       | Yes       | Yes            |
| Java       | Maven           | [OSV-scanner](https://github.com/google/osv-scanner) | Yes       | Yes            |
| Java       | Gradle          | Jit Gradle Scanner                                   | Yes       | Yes            |

> 📘 Monorepo support
>
> Additional configuration steps are required to enable dependency scanning via npm-audit within monorepos. For complete instructions, see [Monorepo Support](https://docs.jit.io/docs/monorepo-support).

## User experience

### Security Team UX in the Jit web app

**Detect existing open source vulnerabilities and "zero day" vulnerabilities**\
Jit SCA continuously scans your codebase to highlight open source vulnerabilities (categorized as "CVEs"), including zero day vulnerabilities — which are newly disclosed vulnerabilities that are already deployed in your environment.

* Navigate to the Findings page filter by "**Finding type**" : "**SCA**".

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7189c7fc5a4adea4826ca5f8c84ad3185125b25503e05c6c6cf205b41d9952bf-Screenshot_2026-01-19_at_15.06.28.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* In many environments, there can be thousands of open source vulnerabilities. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).

**Investigating, triaging, and remediating open source security issues**

Open up an open source security issue in order to:

* See helpful information like its location, resources to learn about the issue, and its Knowledge Graph, which shows the runtime context of the issue.
* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.
* Create a fix PR from within Jit to address the issue immediately.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8f7690a441db171806c96ed45f3b7ec580f57ca317a7e82a6d69e00ea5a97a01-Screenshot_2026-01-19_at_15.08.14.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Opening a fix PR will automatically take you to GitHub with Jit's suggested code fix to resolve the issue.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a8e106dc182b7d6337d29ed00cdf6cd88be77d03009889ed5bba7debf335c251-Screenshot_2026-01-19_at_15.09.29.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Developer UX

**Detect and resolve insecure open source components within the coding environment**

* Developers using Jit never need to leave their coding environment to detect and resolve open source code vulnerabilities.
* For every code repository where Jit SCA is enabled, every code change will automatically be scanned for vulnerable open source components.
* For code changes that include an insecure open source component, developers can view the vulnerability information and upgrade the open source component without having to create another PR.
* The upgrade can be made by simply hitting "Commit suggestion". This helps developers catch insecure open source components before deploying new code to production.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d3e5ea4-image_25.png",
        "",
        "Inline Remediation in a Pull-Request"
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

> 📘 Missing `name` property in NPM issues
>
> If the name property is missing in the Package JSON file, in the Package Lock JSON file the name in the Name properties field is opt by default.