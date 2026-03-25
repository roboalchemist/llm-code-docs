# Source: https://docs.jit.io/docs/scan-dockerfiles.md

# Dockerfile Security Scanning

## Key things to know about Jit Dockerfile Security Scanning

* **Brief description:** Scan your codebase for a wide variety of security issues within your dockerfiles, like overly permissive containers, insecure base images, exposed ports, and many more.
* **Scanning process:** Scanning takes place periodically across your entire codebase (or selected repositories), and during every code change introduced by your developers.
* **How to get started:** Jit IaC Security Scanning can be enabled by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **Scan your Dockerfiles for vulnerabilities**. Hit **Activate**, which will kick off the scanning processes described above.
* **Based on Trivy:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For Dockerfile scanning, Jit leverages [Trivy](https://trivy.dev/latest/) — automatically deploying and running the scanner so you don't have to manage it yourself.

<br />

## User Experience

### UX for Security Teams

Security Teams can view Dockerfile security issues across the entire codebase — unified alongside all other product security issues.

**Detecting and investigating Dockerfile security issues**

* Go to the Jit [Findings Page](https://dash.readme.com/project/jitsecurity/v5.0/docs/jit-findings)  and create a **Vulnerability Type** filter and select **Container Vulnerabilities**.
* Open a security issue to bring up helpful information like its location and Knowledge Graph, which describes the runtime context of the issue.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bd6dcd1f463b4cfb223b645bbee9a3f3a3d180f83253b553fe39fa01bdc98002-Screenshot_2025-01-10_at_3.33.24_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Prioritizing the riskiest Dockerfile security issues**

* In many environments, there can be thousands of Dockerfile security issues. Rather than manually trying to determine which vulnerabilities introduce the most risk, Jit assigns each issue a Priority Score based on the issue's runtime context — making it easy to focus on the top risks.
* Learn more about Jit's contextual prioritization on the Context Engine [page](https://docs.jit.io/docs/contextual-prioritization-context-engine).

**Triaging and remediating Dockerfile security issues**

* Create a ticket through Jira, Slack, Linear and other notification endpoints (see ticketing and triage information [here](https://docs.jit.io/docs/integrating-with-third-party-products-and-services)). Or, you can open a fix PR to patch the security issue with an updated OSS version.
* Create a fix PR from within Jit to auto remediate the issue immediately with one-click code suggestions.

<br />

### UX for developers

Developers never need to leave their coding environment to identify and resolve Dockerfile security issues.

* When Dockerfile Security Scanning is enabled for a given GitHub repository or GitLab project, it will automatically scan every code change and provide immediate code security feedback within the developer environment.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/555db8e040e0ce0272de68a7dd106abb5528dcf30f12214b4b6006ec3952d488-Screenshot_2025-01-10_at_3.40.41_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* Jit returns all of the information needed to resolve the issue within the PR or MR, including auto remediation to resolve the security issue with a click.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/254d3bbb08b9bbfa1c5cf5f4cfbcf8708b0935a958e740f0ea8402cd59969b63-Screenshot_2025-01-10_at_3.40.55_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]