# Source: https://docs.jit.io/docs/scan-iac-for-static-misconfigurations.md

# Infrastructure-as-Code Security Scanning

## Jit IaC Security Scanning: What to know

* **Brief description:** Scan IaC files to surface cloud security misconfigurations like overly permissive IAM policies, publicly available resources, unencrypted connections, and many more.
* **Scanning process:** Scanning takes place periodically across your entire codebase (or selected repositories) and documents findings in the [Findings Page](https://docs.jit.io/v5.0/docs/jit-findings). Additionally, Jit automatically scans every code change containing Helm charts or manifest files to provide immediate security feedback within GitHub or GitLab.
* **How to get started:** Jit IaC Security Scanning can be enabled by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **Scan your Infrastructure-as-code (IaC) for misconfigurations**. Hit **Activate**, which will kick off the scanning processes described above.
* **Based on KICS:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For IaC Security Scanning, Jit supports [KICS](https://kics.io/index.html), which contains hundreds of detection rules and is maintained by Checkmarx.
* **IaC language support**: Jit IaC Security Scanning can detect security misconfigurations in Terraform, Serverless Framework, Pulumi, CloudFormation, and AWS CDK outputs.
* **Test Jit IaC Security Scanning:** Find our deliberately insecure code snippets in Terraform [here](https://docs.jit.io/docs/code-samples#scan-iac-for-static-misconfigurations-terraform). Copy and paste the code into a GitHub pull request or GitLab merge request to test the experience. Jit detects the security misconfigurations before the code is committed.

***

## User Experience

### Security Team UX in the Jit Web App

**Detect existing IaC security vulnerabilities**\
Jit IaC Security Scanning continuously scans your codebase to highlight cloud security misconfigurations, which are documented in the Backlog page.

* Navigate to the Backlog page and create a **Vulnerability Type** filter, select **Cloud Infrastructure Misconfiguration**.
* Select an IaC security misconfiguration to bring up helpful information like its location and runtime context.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/926a1eecb39f39ca59cf9a9b0f8f96065c1dc7595724cac2bf115f7997597439-Screenshot_2025-01-10_at_2.52.34_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Prioritize and triage IaC security issues**

* In many environments, there can be thousands of code vulnerabilities. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).
* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.

**Remediate IaC security issues**

* Jit provides hundreds of out-of-the-box IaC security remediations, which can be applied in a click within the GitHub pull request or GitLab merge request. See below for details.

<br />

### UX for developers

Developers never need to leave their coding environment to identify and resolve IaC security issues before production.

* When Jit IaC Scanning is enabled for a given GitHub repository or GitLab project, it will automatically scan every code change that contains IaC files and provide immediate security feedback within the developer environment.
* Jit IaC Scanning supports auto remediation for many IaC security issues. Suggested code fixes are provided within the code change, and can be applied with a click without creating a new pull request/merge request.
* Remediation in a Pull Request whereby the suggested code is displayed in the PR itself, and the developer can accept it by clicking **Commit suggestion**. Learn more about Jit's [Automated Remediation](https://docs.jit.io/docs/automated-remediation).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3badc8e855fb3cfb1b1893a1e823455496da161fe0a4dba944bd6caa05e02c66-Screenshot_2025-01-10_at_2.58.40_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]