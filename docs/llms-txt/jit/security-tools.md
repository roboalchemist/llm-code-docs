# Source: https://docs.jit.io/docs/security-tools.md

# Jit Scanner Summary

Jit unifies and enhances the leading open source scanners for all product security scanning technologies. Jit users do not need to configure or deploy the supported scanners – they are built-in to the platform and supported out-of-the-box.

By integrating the following open source security scanners into our platform, Jit provides the following benefits:

* Automate configuration, deployment, and execution for all scanners
* Automated scanner upgrading
* Added custom rules to surface additional vulnerabilities, while tweaking noisy rules to reduce false positives
* Contextual prioritization to surface the code security flaws and cloud misconfigurations that introduce real risk
* A unique developer UX and auto remediation to simplify code security for developers
* Unification of all findings into a single, prioritized backlog with metrics to monitor security posture

<br />

## Jit-supported scanners

[block:parameters]
{
  "data": {
    "h-0": "Jit Security Control",
    "h-1": "OSS Security Tool",
    "h-2": "Layer",
    "h-3": "Supports",
    "h-4": "OSS Tool Documentation",
    "0-0": "[Scan your code for vulnerabilities (SAST)](https://docs.jit.io/docs/scan-code-for-vulnerabilities)",
    "0-1": "Semgrep",
    "0-2": "Application Security",
    "0-3": "Javascript, Typescript, Python, Go, Java, Scala, Kotlin, Swift, Rust, C#, PHP, C, C++, Ruby",
    "0-4": "[repo](https://github.com/returntocorp/semgrep)",
    "1-0": "[Scan your code for vulnerabilities (SAST)](https://docs.jit.io/docs/scan-code-for-vulnerabilities)",
    "1-1": "Gosec",
    "1-2": "Application Security",
    "1-3": "Go",
    "1-4": "[repo](https://github.com/securego/gosec)",
    "2-0": "[Scan code for hard-coded secrets](https://docs.jit.io/docs/scan-code-for-hard-coded-secrets)",
    "2-1": "Gitleaks",
    "2-2": "Application Security",
    "2-3": "Text files",
    "2-4": "[repo](https://github.com/zricethezav/gitleaks)",
    "3-0": "[Scan code for hard-coded secrets](https://docs.jit.io/docs/scan-code-for-hard-coded-secrets)",
    "3-1": "TruffleHog",
    "3-2": "Application Security",
    "3-3": "Text files",
    "3-4": "[repo](https://github.com/trufflesecurity/trufflehog)",
    "4-0": "[Scan your code dependencies for vulnerabilities (SCA)](https://docs.jit.io/docs/scan-code-dependencies-for-vulnerabilities)",
    "4-1": "OSV-Scanner",
    "4-2": "Application Security",
    "4-3": "Python, PHP, Java, Go, Javascript, Typescript",
    "4-4": "[repo](https://github.com/google/osv-scanner)",
    "5-0": "[Scan your Dockerfiles for vulnerabilities](https://docs.jit.io/docs/scan-dockerfiles)",
    "5-1": "Trivy",
    "5-2": "Application Security",
    "5-3": "Dockerfile",
    "5-4": "[repo](https://github.com/aquasecurity/trivy)",
    "6-0": "[Scan your infrastructure-as-code (IaC) for misconfigurations](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations)",
    "6-1": "KICS",
    "6-2": "Cloud Security",
    "6-3": "Terraform, Serverless Framework, Pulumi, CloudFormation, AWS CDK",
    "6-4": "[repo](https://github.com/Checkmarx/kics)",
    "7-0": "[Scan Kubernetes configuration files](https://docs.jit.io/docs/scan-kubernetes-iac-for-misconfigurations)",
    "7-1": "Kubescape",
    "7-2": "Cloud Security",
    "7-3": "K8s manifest files, Helm charts",
    "7-4": "[repo](https://github.com/kubescape/kubescape)",
    "8-0": "[Scan infrastructure for runtime misconfigurations](https://docs.jit.io/docs/scan-runtime-infra)",
    "8-1": "Prowler",
    "8-2": "Cloud Security",
    "8-3": "AWS, GCP, Azure",
    "8-4": "[repo](https://github.com/prowler-cloud/prowler)",
    "9-0": "[Import AWS Security Hub Findings](https://docs.jit.io/docs/import-aws-security-hub-findings)",
    "9-1": "AWS Security Hub",
    "9-2": "Cloud Security",
    "9-3": "AWS",
    "9-4": "[documentation](https://docs.aws.amazon.com/securityhub/?id=docs_gateway)",
    "10-0": "[Verify that the users of your AWS accounts have enabled MFA](https://docs.jit.io/docs/require-mfa-for-cloud-providers)",
    "10-1": "AWS MFA Checker",
    "10-2": "Cloud Security",
    "10-3": "AWS",
    "10-4": "[Jit tool](https://docs.jit.io/docs/require-mfa-for-cloud-providers)",
    "11-0": "[Scan your API for vulnerabilities (DAST)](https://docs.jit.io/docs/ensure-your-api-is-secure)  \n[Scan your web application for vulnerabilities (DAST)](https://docs.jit.io/docs/run-a-web-application-scanner)",
    "11-1": "ZAP",
    "11-2": "DAST",
    "11-3": "APIs, Web applications",
    "11-4": "[repo](https://github.com/zaproxy)",
    "12-0": "[Detect GitHub misconfigurations](https://docs.jit.io/docs/github-misconfiguration-detection)",
    "12-1": "Legitify",
    "12-2": "CI/CD Security",
    "12-3": "GitHub",
    "12-4": "[repo](https://github.com/Legit-Labs/legitify)",
    "13-0": "[Verify that MFA for your GitHub organization is enabled](https://docs.jit.io/docs/require-mfa-for-scm)",
    "13-1": "GitHub MFA Checker",
    "13-2": "CI/CD Security",
    "13-3": "GitHub",
    "13-4": "[Jit tool](https://docs.jit.io/docs/require-mfa-for-scm)",
    "14-0": "[Verify that Github Branch Protection is properly configured](https://docs.jit.io/docs/require-branch-protection-for-scm)",
    "14-1": "GitHub BP Checker",
    "14-2": "CI/CD Security",
    "14-3": "GitHub",
    "14-4": "[Jit tool](https://docs.jit.io/docs/require-branch-protection-for-scm)"
  },
  "cols": 5,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]