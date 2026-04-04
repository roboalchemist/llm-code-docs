# Source: https://docs.datadoghq.com/getting_started/code_security.md

# Source: https://docs.datadoghq.com/developers/ide_plugins/idea/code_security.md

# Source: https://docs.datadoghq.com/security/code_security.md

---
title: Code Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Code Security
---

# Code Security

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Code Security scans your first-party code and open source libraries used in your applications in both your repositories and running services, providing end-to-end visibility from development to production. It encompasses the following capabilities:

- [Static Code Analysis (SAST)](https://docs.datadoghq.com/security/code_security/static_analysis/) for identifying security and quality issues in your first-party code
- [Software Composition Analysis (SCA)](https://docs.datadoghq.com/security/code_security/software_composition_analysis/) for identifying open source dependencies in both your repositories and your services
- [Runtime Code Analysis (IAST)](https://docs.datadoghq.com/security/code_security/iast/) for identifying vulnerabilities in the first-party code within your services
- [Secret Scanning](https://docs.datadoghq.com/security/code_security/secret_scanning/) for identifying and validating leaked secrets (in Preview)
- [Infrastructure as Code (IaC) Security](https://docs.datadoghq.com/security/code_security/iac_security) for identifying security misconfigurations in Terraform files stored in your repositories
- Supply Chain Security for preventing malicious packages from entering your development environment and code repositories

Code Security helps teams implement DevSecOps throughout the organization:

- **Developers:** early vulnerability detection, code quality improvements, faster development as developers spend less time debugging and patching.
- **Security Administrators:** enhanced security posture, improved patch management in response to early vulnerability alerts, and compliance monitoring.
- **Site Reliability Engineers (SREs):** automated security checks throughout CI/CD workflow, security compliance, and system resilience. SAST reduces manual overhead for SREs and ensures that each release is thoroughly tested for vulnerabilities.

The following vulnerability management capabilities are available across Code Security:

- [Developer tool integrations](https://docs.datadoghq.com/security/code_security/dev_tool_int/) to flag vulnerabilities in IDE and pull request comments, and block vulnerabilities from being merged to your production codebase
- [Ticketing integrations](https://docs.datadoghq.com/security/ticketing_integrations) with Jira and Datadog Case Management, with bidirectional syncing
- [Notifications](https://docs.datadoghq.com/security/notifications/)
- [Automation pipelines](https://docs.datadoghq.com/security/automation_pipelines/) for automatically muting vulnerabilities and assigning due dates by severity

## Static Code Analysis (SAST){% #static-code-analysis-sast %}

Static Code Analysis (SAST) analyzes pre-production code to identify security and quality issues. You can embed best security and development practices throughout the software development lifecycle with:

- IDE integration to flag violations in real time with deterministic suggested fixes
- In-line pull request comments with deterministic suggested fixes and incremental/diff-aware scanning
- Ability to open a pull request to fix a violation directly from Datadog

Scans can run via your CI/CD pipelines or directly in Datadog with hosted scanning.See [Static Code Analysis Setup](https://docs.datadoghq.com/security/code_security/static_analysis/setup/) to get started.

Static Code Analysis can also scan your pull requests at scale to detect and prevent malicious code changes. This allows Datadog to not only check for known code vulnerabilities, but also detect potentially malicious intent in PRs submitted to default branches of your repositories. [Request access to the Preview](https://www.datadoghq.com/product-preview/malicious-pr-protection/).

## Software Composition Analysis{% #software-composition-analysis %}

Software Composition Analysis (SCA) analyzes open source libraries in both your repositories and running services. You can track and manage dependencies across the software development lifecycle with:

- IDE integration to flag vulnerabilities affecting libraries running on your services
- Ability to open a pull request to fix a library vulnerability directly from Datadog
- Runtime-informed prioritization of vulnerabilities with the Datadog severity score

SCA supports both static and runtime dependency detection.For static scanning, you can scan via your CI/CD pipelines or directly via Datadog with hosted scanning. See [static setup](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static/) to get started.For runtime vulnerability detection, you can easily enable SCA on your services instrumented with Datadog APM. See [runtime setup](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_runtime/) to get started.

## Runtime Code Analysis (IAST){% #runtime-code-analysis-iast %}

Runtime Code Analysis (IAST) identifies code-level vulnerabilities in your running services. It relies on inspection of legitimate application traffic as opposed to external testing that often requires extra configuration or periodic scheduling. IAST provides an up-to-date view of your attack surface area by:

- Monitoring your code's interactions with other components of your stack (such as libraries and infrastructure)
- Providing 100% coverage of the OWASP Top 10
- Runtime-informed prioritization of vulnerabilities with the Datadog severity score

You can enable IAST on your services instrumented with Datadog APM. See [IAST setup](https://docs.datadoghq.com/security/code_security/iast/) to get started.

## Secret Scanning{% #secret-scanning %}

Secret Scanning identifies and validates leaked secrets in your codebase. [Request access to the Preview](https://www.datadoghq.com/product-preview/secret-scanning/).

## Supply Chain Security{% #supply-chain-security %}

Prevent malicious packages from entering your development environments with Datadog Supply Chain Security Firewall, supported for GitHub. [Request access to the Preview](https://docs.google.com/forms/d/1Xqh5h1n3-jC7au2t30fdTq732dkTJqt_cb7C7T-AkPc).

## Further Reading{% #further-reading %}

- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
- [Detect and block exposed credentials with Datadog Secret Scanning](https://www.datadoghq.com/blog/code-security-secret-scanning)
- [Secure your code at scale with AI-driven vulnerability management](https://www.datadoghq.com/blog/code-security-ai-capabilities)
- [Identify common security risks in MCP servers](https://www.datadoghq.com/blog/monitor-mcp-servers/)
- [Using LLMs to filter out false positives from static code analysis](https://www.datadoghq.com/blog/using-llms-to-filter-out-false-positives/)
