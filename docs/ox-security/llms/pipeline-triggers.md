# Source: https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-triggers.md

# Pipeline Triggers

Triggers define when to activate a workflow upon a security policy violation.

## Commonly Used Triggers

These triggers are shortcuts to the most frequently applied workflow entry points.\
They cover broad policy types and let you build workflows quickly without selecting individual checks.

| Trigger Name                           | Description                                                                                                                                  |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Any Policy                             | Activates when any policy violation is detected, regardless of type. Useful for workflows that apply across the entire platform.             |
| Any Code Security Policy               | Activates when a code security issue is detected, such as a SAST issue, unapproved SaaS, or code smell.                                      |
| Any Secret/PII Scan Policy             | Activates when a secret or personally identifiable information (PII) is detected in code, logs, or Git history.                              |
| Any Open Source Security Policy        | Activates when a vulnerability or license risk is detected in an open source dependency, base image, or manifest.                            |
| Any SBOM Policy                        | Activates when an issue related to the Software Bill of Materials (SBOM) is detected, such as an unapproved license or malicious dependency. |
| Any Infrastructure as Code Scan Policy | Activates when a misconfiguration or risk is detected in Infrastructure as Code (IaC) templates like Terraform, Helm, or Kubernetes.         |
| Any CI/CD Posture Policy               | Activates when an insecure practice is detected in CI/CD pipelines, such as unpinned actions, secrets in logs, or excessive permissions.     |
| Any Container Security Policy          | Activates when a vulnerability, secret, or misconfiguration is detected in a container image.                                                |

## Code Security Triggers

These triggers activate when issues are detected directly in source code.\
They include static analysis results, use of unapproved services, and maintainability problems.

| Trigger Name             | Description                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Any Code Security Policy | Activates when any code security issue is detected, regardless of type.                                              |
| SAST Issue               | Activates when a static application security testing (SAST) issue is found in code.                                  |
| Unapproved SaaS in Code  | Activates when the code references a software-as-a-service (SaaS) provider that is not approved by the organization. |
| Code Smell Issue         | Activates when a maintainability problem or code smell is detected, such as duplicated logic or unused variables.    |

## Secret/PII Scan Triggers

These triggers activate when secrets or personally identifiable information (PII) are detected in code or repositories.\
They help prevent sensitive data from being exposed in source code, logs, or version history.

| Trigger Name               | Description                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Any Secret/PII Scan Policy | Activates when any secret or PII-related issue is detected.                                         |
| Secret in Code             | Activates when a secret, such as an API key, password, or token, is found in source code.           |
| Secret Logging in Code     | Activates when a secret is written to logs by the code.                                             |
| PII Embedded in Code       | Activates when personal data, such as names, emails, or identifiers, is hardcoded into source code. |
| PII Logging in Code        | Activates when personal data is written to logs by the code.                                        |
| PII in Git History         | Activates when personal data is found in the Git commit history.                                    |

## Open Source Security Triggers

These triggers activate when vulnerabilities or risks are found in open source dependencies, images, or manifests.\
They help track and respond to known CVEs in software supply chains.

| Trigger Name                                         | Description                                                                                    |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Any Open Source Security Policy                      | Activates when any open source security issue is detected.                                     |
| Vulnerable Dependency (CVE) in Code                  | Activates when a dependency with a known vulnerability (CVE) is detected in code.              |
| Vulnerable Base Image (CVE) in DockerFile            | Activates when a base image defined in a Dockerfile has a known vulnerability.                 |
| Vulnerable Public Image (CVE) in Docker Compose      | Activates when a Docker Compose configuration uses a public image with a known vulnerability.  |
| Vulnerable Public Image (CVE) in Kubernetes Manifest | Activates when a Kubernetes manifest references a public image with a known vulnerability.     |
| Vulnerable Public Image (CVE) in Helm Chart          | Activates when a Helm chart references a public image with a known vulnerability.              |
| Vulnerable Public Image (CVE) in Terraform           | Activates when a Terraform configuration references a public image with a known vulnerability. |
| Vulnerable Public Image (CVE) in CI/CD Deployment    | Activates when a CI/CD pipeline deploys a public image with a known vulnerability.             |

## SBOM Triggers

These triggers activate when issues are detected in the Software Bill of Materials (SBOM).\
They help enforce license compliance, detect malicious or confusing dependencies, and highlight outdated or deprecated components.

| Trigger Name                                           | Description                                                                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Any SBOM Policy                                        | Activates when any SBOM-related issue is detected.                                                                           |
| Typosquatting Dependency in Code                       | Activates when a dependency is detected with a name similar to a trusted package, suggesting typo-squatting.                 |
| Malicious Dependency in Code                           | Activates when a dependency identified as malicious is detected.                                                             |
| Dependency Confusion: Organization Scope in Code       | Activates when a package with the same name exists in both public and private registries, and the public version is used.    |
| Dependency Confusion: Private Package in Code          | Activates when a package expected to be private is mistakenly pulled from a public registry.                                 |
| Unapproved License Used by Direct Dependency in Code   | Activates when a direct dependency uses a license that is not approved by the organization.                                  |
| Deprecated Direct Dependency in Code                   | Activates when a direct dependency is marked as deprecated.                                                                  |
| Outdated Direct Dependency in Code                     | Activates when a direct dependency version is outdated compared to the latest available version.                             |
| Unpopular Direct Dependency in Code                    | Activates when a direct dependency is rarely used or lacks community adoption, which may indicate security or support risks. |
| Unapproved License Used by Indirect Dependency in Code | Activates when an indirect dependency uses a license that is not approved by the organization.                               |
| Deprecated Indirect Dependency in Code                 | Activates when an indirect dependency is marked as deprecated.                                                               |
| Outdated Indirect Dependency in Code                   | Activates when an indirect dependency version is outdated compared to the latest available version.                          |
| Unpopular Indirect Dependency in Code                  | Activates when an indirect dependency is rarely used or lacks community adoption.                                            |

## Infrastructure as Code (IaC) Scan Triggers

These triggers activate when security issues or misconfigurations are detected in Infrastructure as Code.\
They help enforce best practices for Terraform, Helm, Kubernetes, and other IaC frameworks.

| Trigger Name                           | Description                                                                                                                                   |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Any Infrastructure as Code Scan Policy | Activates when any Infrastructure as Code (IaC) security issue is detected.                                                                   |
| IaC Issue                              | Activates when a misconfiguration or security issue is found in IaC files, such as Terraform templates, Kubernetes manifests, or Helm charts. |

## CI/CD Posture Triggers

These triggers activate when security issues are detected in continuous integration and continuous delivery (CI/CD) pipelines.\
They help enforce safe pipeline practices and prevent insecure configurations.

| Trigger Name                                 | Description                                                                                                           |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Any CI/CD Posture Policy                     | Activates when any CI/CD posture-related issue is detected.                                                           |
| CI/CD Workflow Security Issue                | Activates when a general security issue is detected in a CI/CD workflow.                                              |
| Secret Echoed in Workflow Console            | Activates when a secret is printed or echoed in a CI/CD workflow console.                                             |
| Deprecated Command in Workflow               | Activates when a workflow uses a command that is deprecated.                                                          |
| CI/CD Context Values in Workflow             | Activates when unsafe or incorrect context values are used in a workflow.                                             |
| Incorrect Storage of Secret in GitHub Action | Activates when a secret is stored incorrectly in a GitHub Action workflow.                                            |
| Excessive Permissions in Workflow File       | Activates when a workflow file is configured with more permissions than required.                                     |
| Unpinned (SHA) Third-Party Actions in GitHub | Activates when a GitHub Action references an unpinned third-party action without a SHA, increasing supply chain risk. |

## Container Security Triggers

These triggers activate when vulnerabilities, secrets, or misconfigurations are detected in container images.\
They help secure containerized applications across base images, user code, and registries.

| Trigger Name                                                           | Description                                                                                                  |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Any Container Security Policy                                          | Activates when any container security issue is detected.                                                     |
| Vulnerable Dependency (CVE) in Container from User Code                | Activates when a container includes a dependency with a known vulnerability (CVE) introduced by user code.   |
| Vulnerable Dependency (CVE) in Container from User Instruction         | Activates when a container includes a vulnerable dependency introduced by a Dockerfile or build instruction. |
| Vulnerable Dependency (CVE) in Container from Base Image               | Activates when a base image used in a container contains a known vulnerability.                              |
| Vulnerable Dependency (CVE) in Container from Operating System         | Activates when an operating system package in a container contains a known vulnerability.                    |
| Vulnerable Dependency (CVE) in Public Image Hosted in Private Registry | Activates when a public image stored in a private registry contains a known vulnerability.                   |
| Vulnerable Dependency (CVE) in Java Archive Package                    | Activates when a container includes a Java archive (JAR) package with a known vulnerability.                 |
| Secret in Container                                                    | Activates when a secret, such as an API key or password, is found inside a container.                        |
| PII in Container                                                       | Activates when personally identifiable information (PII) is found in a container.                            |
| Unapproved Dependency License in Container                             | Activates when a container includes a dependency with a license that is not approved.                        |
| Misconfiguration in Container                                          | Activates when a container image is misconfigured in a way that introduces security risk.                    |
