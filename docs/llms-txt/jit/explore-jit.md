# Source: https://docs.jit.io/docs/explore-jit.md

# Explore Jit Features

Below are some of the core features of Jit's platform. See the [Jit Product Demo Hub](https://www.jit.io/aspm-platform/demo-hub) to view demo videos for some of these features.

## Developer UX: Empower developers to secure everything they code

Learn how Jit makes it easy for developers to quickly resolve code security issues before production.

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FAcYN_qjZDM4%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAcYN_qjZDM4&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FAcYN_qjZDM4%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=AcYN_qjZDM4",
  "title": "Simplify Security for Developers with Jit",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/AcYN_qjZDM4/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=AcYN_qjZDM4",
  "typeOfEmbed": "youtube"
}
[/block]

To try the developer user experience yourself, create a pull request in GitHub or merge request in GitLab with our deliberately [insecure code snippets](https://docs.jit.io/docs/code-samples). Jit provides feedback before the code is merged.

To scan code via pre commit hooks in VS Code, learn how to set up the [VS Code integration](https://docs.jit.io/docs/jit-ide-extension-for-visual-studio).

***

## Manage risk across your applications and infrastructure

The Findings page is where you review, search, and manage all security findings detected across your environment. It helps you quickly understand what needs attention, prioritize risks, and track remediation status.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/96a50c31b8fad4fafbac6e99b6868472c4b4e4335a6c939c82a1ee5730cc8d47-findings_page.png",
        "",
        "Example of the Findings page showing the search field, filters, and findings list."
      ],
      "align": "center",
      "border": true,
      "caption": "Example of the Findings page showing the search field, filters, and findings list."
    }
  ]
}
[/block]

Learn more about the Findings page [here](https://dash.readme.com/project/jitsecurity/v5.0/docs/jit-findings).

***

## Prioritize the top product security risks in your environment

After scanning your codebase and cloud environment for security issues, Jit automatically prioritizes the top product security risks based on runtime and business context – like whether they’re exposed to the internet or call a sensitive database.

This information is synthesized into a Priority Score for each security issue detected by Jit.

> 📘 Integrate Jit with AWS to enable Context Engine
>
> To configure Context Engine, [integrate Jit with AWS](https://docs.jit.io/docs/integrating-with-aws)  to provide visibility into your cloud environment. Additionally, [contact Jit](https://www.jit.io/contact) so we can open the feature for you account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cac0f04670cba906584e67c2d6e94845fc3a26724e7d923fa66090942b644d8d-findings_page.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

By opening up a security issue within the Findings page, you can visualize how the issue is deployed in runtime with Jit’s Finding Graph.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8a40ddd46f131c94f97f1bbe4987ce605fd75f97e3696e4593029d33ed13da87-Screenshot_2026-01-19_at_14.12.02.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

This visualization describes how the security finding is deployed. Labels are attached to the relevant resources to describe the prioritization factors, like whether the issue is deployed to production, calls a database, is exposed to the internet, and so on.

***

## Integrate Jit with a notification endpoint

Follow the links below to begin triaging security issues in Jit to your endpoint notification system.

* [Jira](https://docs.jit.io/docs/integrating-with-jira)
* [Slack](https://docs.jit.io/docs/integrating-with-slack)
* [Linear](https://docs.jit.io/docs/integrating-with-linear)
* [Shortcut](https://docs.jit.io/docs/integrating-with-shortcut)
* [Monday.com](https://docs.jit.io/docs/integrating-with-monday)

***

## Expand your product security coverage

Jit unifies the following product security scanners onto one platform – making tens of scanners feel like one.

**Scan your customer code for security flaws** with Static Application Security Testing (SAST). Jit SAST scans all common code languages. Learn more about Jit SAST [here](https://docs.jit.io/docs/scan-code-for-vulnerabilities).

* Jit SAST is automatically activated when you onboard Jit, which scans your selected repos/projects and records security findings in the Findings page, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* Test Jit SAST by creating a pull request in GitHub or merge request in GitLab with these deliberately insecure code snippets in [Python](https://docs.jit.io/docs/code-samples#scan-code-for-vulnerabilities-python), [Javascript](https://docs.jit.io/docs/code-samples#scan-code-for-vulnerabilities-javascript), and [Go](https://docs.jit.io/docs/code-samples#scan-code-for-vulnerabilities-go). Jit provides security feedback before the code is merged.

<br />

**Scan your open source components and dependencies for known vulnerabilities** using Software Composition Analysis (SCA). Jit SCA scans all common code languages. Learn more about SCA [here](https://docs.jit.io/docs/scan-code-dependencies-for-vulnerabilities).

* Jit SCA is automatically activated when you onboard Jit, which scans your selected repos/projects and records security findings in the Findings page, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* Test Jit SCA by creating a pull request in GitHub or merge request in GitLab with these deliberately insecure code snippets in [Node](https://docs.jit.io/docs/code-samples#scan-code-dependencies-for-vulnerabilities-node) and [Python](https://docs.jit.io/docs/code-samples#scan-code-dependencies-for-vulnerabilities-python). Jit provides security feedback before the code is merged.

<br />

**Scan your codebase for copyleft open source licenses** like GPL with Open Source License Detection. Jit Open Source License Detection scans all common languages. Learn more about Jit Open Source License Detection [here](https://docs.jit.io/docs/scan-for-denied-licenses).

* Activate Open Source License Detection by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan your code for license violations”.
* Activation will scan your repos/projects for copyleft open source licenses, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.

<br />

**Scan your codebase for hard coded secrets** with Secrets Detection. Jit Secrets Detection scans all coding languages. Learn more about Jit Secrets Detection [here](https://docs.jit.io/docs/scan-code-for-hard-coded-secrets).

* Jit Secrets Detection is automatically activated when you onboard Jit, which scans your selected repos/projects and records security findings in the Findings page, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* Test Jit Secrets Detection by creating a pull request in GitHub or merge request in GitLab with this deliberately [insecure snippet](https://docs.jit.io/docs/code-samples#scan-code-for-hard-coded-secrets-multi-languages). Jit provides security feedback before the code is merged.

<br />

**Create a continuously updated inventory of your codebase** with Software Bill of Materials (SBOM). Jit SBOM scans all common coding languages. Learn more about Jit SBOM [here](https://docs.jit.io/docs/sbom).

* Activate SBOM by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Generate a Software Bill of Materials (SBOM)”.
* After activation, wait a few minutes and navigate to **My Environment** → **SBOM** in the left menu to see your SBOM.

**Scan your IaC files for infrastructure security misconfigurations** with IaC scanning. Jit IaC Scanning supports Terraform, Pulumi, serverless manifest files, CloudFormation, AWS CDK files. Learn more about Jit IaC Scanning [here](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations).

* Activate IaC scanning by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan your Infrastructure as Code (IaC) for misconfigurations”.
* Activation will scan your selected repos/projects and record security findings in the Findings page, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.
* Test Jit IaC Scanning by creating a pull request in GitHub or merge request in GitLab with this deliberately [insecure terraform snippet](https://docs.jit.io/docs/code-samples#code-sample-ec2-instance-has-public-ip). Jit provides security feedback before the code is merged.

<br />

**Scan Kubernetes manifest files for security misconfigurations** with Kubernetes Scanning. Learn more about Jit Kubernetes Scanning [here](https://docs.jit.io/docs/scan-kubernetes-iac-for-misconfigurations).

* Activate Jit Kubernetes Scanning scanning by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan your Infrastructure as Code (IaC) for misconfigurations”.
* Activation will scan your selected repos/projects and record security findings in the Findings page, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.

<br />

**Scan your dockerfiles for code security flaws and misconfigurations** with Dockerfile Scanning (container scanning on build or in your registry coming soon). Learn more about Jit Dockerfile Scanning [here](https://docs.jit.io/docs/scan-dockerfiles).

* Activate Jit Dockerfile Scanning by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan your Infrastructure as Code (IaC) for misconfigurations”.
* Activation will scan your selected repos/projects and record security findings in the Findings page, while implementing continuous scanning for every code change in GitHub, GitLab, or your IDE.

<br />

**Scan your cloud infrastructure in runtime for infrastructure security misconfigurations** using Cloud Security Posture Management (CSPM). Learn more about Jit CSPM [here](https://docs.jit.io/docs/scan-runtime-infra).

* Activate Jit CSPM by integrating Jit with AWS, Azure or GCP. Then, activate Jit CSPM by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan infrastructure for runtime misconfigurations”. This will scan your cloud infrastructure daily.
* See the integration pages for [AWS](https://docs.jit.io/docs/integrating-with-aws), [Azure](https://docs.jit.io/docs/integrating-with-azure), and [GCP](https://docs.jit.io/docs/integrating-with-gcp).
* Security findings are recorded in the Findings page.

<br />

**Scan your web applications in runtime** using Dynamic Application Security Testing (DAST). Learn more about Jit DAST for web apps [here](https://docs.jit.io/docs/scan-your-web-application-for-vulnerabilities-dast-copy).

* Activate Jit DAST by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan your web application for vulnerabilities”. This will open the configuration wizard to configure periodic scans.
* Security findings are recorded in the Findings page.

<br />

**Scan your APIs for vulnerabilities** using Dynamic Application Security Testing (DAST). Learn more about Jit DAST for APIs [here](https://docs.jit.io/docs/ensure-your-api-is-secure).

* Activate Jit DAST by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Scan your API for vulnerabilities”. This will open the configuration wizard to configure periodic scans.
* Security findings are recorded in the Findings page.

<br />

**Scan your GitHub environment for security misconfigurations** with Jit CI/CD Security. Learn more about Jit CI/CD Security [here](https://docs.jit.io/docs/github-misconfiguration-detection).

* Activate Jit CI/CD Security by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Detect GitHub misconfigurations”.
* Ensure branch protection is enabled and that MFA is enabled for your GitHub organization by going to the left menu in the Jit app and navigating to **ASPM** → **Security Plans** → **Jit Max Security Plan** and activate “Verify that Github Branch Protection is properly configured” or “Verify that MFA for your GitHub organization is enabled”.
* Activation will periodically scan your GitHub environment and record security findings in the Findings page.