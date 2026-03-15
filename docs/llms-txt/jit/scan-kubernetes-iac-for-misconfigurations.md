# Source: https://docs.jit.io/docs/scan-kubernetes-iac-for-misconfigurations.md

# Kubernetes Security Scanning

## Jit Kubernetes Security Scanning: Key things to know

* **Brief description:** Jit Kubernetes Security Scanning analyzes Helm charts and manifest files for security misconfigurations, such as unsecured APIs, over-privileged containers, misconfigured resource limits and many more.
* **Scanning process:** Scanning takes place periodically across your entire codebase (or selected repositories) and documents findings in the [Findings Page](https://docs.jit.io/v5.0/docs/jit-findings). Additionally, Jit automatically scans every code change containing Helm charts or manifest files to provide immediate security feedback within GitHub or GitLab.
* **How to get started:** Jit Kubernetes Security Scanning can be enabled by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **Scan Kubernetes configuration files**. Hit **Activate**, which will kick off the scanning processes described above.
* **Based on Kubescape:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For Kubernetes Security Scanning, we use [Kubescape](https://github.com/kubescape/kubescape), which was created by [ARMO](https://www.armosec.io/) and is a [Cloud Native Computing Foundation (CNCF) sandbox project](https://www.cncf.io/sandbox-projects/).
* **Ecosystem support**: Scan Kubernetes manifest files (YAML) or Helm charts for security misconfigurations, without requiring an active cluster.

<br />

## User Experience

### Security Team UX in the Jit Web App

**Detect existing code security vulnerabilities**\
Jit Kubernetes Scanning continuously scans your codebase to highlight Kubernetes security misconfigurations.

* To list all Kubernetes security misconfigurations within your environment, navigate to the Backlog page and create a **Vulnerability type** filter, then select **Kubernetes IaC Misconfiguration**. Add additional filters like **Location** to narrow the findings.
* Open an issue to see helpful information like its location, resources to learn about the issue, and its Knowledge Graph, which shows the runtime context of the issue.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/54c55e4a2fe7b470229e99b8f3027292d98f9700beca88581ed93c99deb5edae-Screenshot_2025-01-10_at_2.30.06_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Investigating and prioritizing Kubernetes security misconfigurations**

* In many environments, there can be thousands of code vulnerabilities. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).

**Triage and remediate Kubernetes security misconfigurations**

* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.
* Create a fix PR from within Jit to address the issue immediately.

<br />

### UX for developers

Developers never need to leave their coding environment to identify and resolve Kubernetes security misconfigurations:

* When Jit Kubernetes Security Scanning is enabled for a given GitHub repository or GitLab project, it will automatically scan every code change and provide immediate code security feedback within the developer environment.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1d07af1faf7b73e8444abe962e266440240d6d0962d67d2dea8740c6409bfd5d-Screenshot_2025-01-10_at_2.24.05_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* Jit provides runtime context for detected security misconfigurations to help developers understand the actual impact of the issue.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f7888ee77037a9e245c2143401f5eef45bc23e3f2648e1ffd27c3bfe9f422825-Screenshot_2025-01-10_at_2.23.32_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]