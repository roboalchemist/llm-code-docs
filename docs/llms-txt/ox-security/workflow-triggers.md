# Source: https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-triggers.md

# Workflow Triggers

Triggers define when a workflow should start. A trigger is an event or detection that activates the automation logic. For example, a trigger can be a newly discovered vulnerability, a failed security scan, or a change in source control posture.

Triggers are tied to security policies. A policy violation activates the workflow.

## Regular scan commonly used triggers

These triggers activate when a policy violation is detected during a regular scan.\
They cover different policy types across code, dependencies, infrastructure, and security tools.

| Trigger Name                           | Description                                                                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Any Policy                             | Activates when any policy violation is detected, regardless of type.                                                |
| Any Git Posture Policy                 | Activates when a Git posture-related issue is detected, such as exposed secrets or unsafe branch protection rules.  |
| Any Code Security Policy               | Activates when a code security issue is detected, including SAST findings or unapproved SaaS usage.                 |
| Any Secret/PII Scan Policy             | Activates when secrets or personally identifiable information (PII) are detected in code or history.                |
| Any Open Source Security Policy        | Activates when an open source vulnerability or license risk is detected.                                            |
| Any SBOM Policy                        | Activates when a Software Bill of Materials (SBOM) issue is detected, such as unapproved or malicious dependencies. |
| Any Infrastructure as Code Scan Policy | Activates when a misconfiguration or issue is detected in Infrastructure as Code (IaC) files.                       |
| Any CI/CD Posture Policy               | Activates when an insecure practice is detected in CI/CD pipelines.                                                 |
| Any Security Tool Coverage Policy      | Activates when issues are detected by an integrated security tool, or when coverage gaps are identified.            |
| Any Container Security Policy          | Activates when a vulnerability, secret, or misconfiguration is detected in a container image.                       |
| Any Dynamic App Security Policy        | Activates when an application fails a dynamic security test, such as DAST.                                          |
| Any Artifact Integrity Policy          | Activates when an artifact fails integrity checks, such as mismatched signatures.                                   |
| Any Cloud Context Policy               | Activates when a cloud security issue is detected in the environment or configuration.                              |
| Any Manual Upload Policy               | Activates when issues are detected in manually uploaded files or scan results.                                      |

## Regular Scan Git Posture Triggers

These triggers activate when insecure repository configurations or risky Git practices are detected.\
They help enforce branch protection, code review requirements, access controls, and repository hygiene.

| Trigger Name                                                              | Description                                                                         |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Any Git Posture Policy                                                    | Activates when any Git posture-related issue is detected.                           |
| Unreviewed Code Change                                                    | Activates when code is committed without a required review.                         |
| Veteran Developer Review Required                                         | Activates when a review from a veteran or senior developer is required but missing. |
| Branch Protection Not Enforced                                            | Activates when branch protection rules are not applied.                             |
| Branch Protection Code Review Can Be Ignored by Developer                 | Activates when a developer can bypass required code reviews.                        |
| Branch Protection Code Review Can Be Ignored by Outside Collaborator      | Activates when an external collaborator can bypass required code reviews.           |
| Branch Protection Push Restriction Can Be Ignored by Developer            | Activates when a developer can bypass push restrictions on a protected branch.      |
| Branch Protection Push Restriction Can Be Ignored by Outside Collaborator | Activates when an external collaborator can bypass push restrictions.               |
| Protected Branch Can Be Deleted by a Non-Admin                            | Activates when non-admin users can delete protected branches.                       |
| Branch Protection Allows Unsigned Commits                                 | Activates when unsigned commits are allowed on a protected branch.                  |
| Private Repo Forking Is Enabled                                           | Activates when private repositories allow forking.                                  |
| Private Repo Fork Detected                                                | Activates when a fork of a private repository is detected.                          |
| Public Repo Detected                                                      | Activates when a repository is public.                                              |
| Org Owner With No Admin Activity                                          | Activates when an organization owner has not performed any admin activity.          |
| Too Many Org Owners                                                       | Activates when the number of organization owners exceeds the recommended limit.     |
| Single Owner in Org                                                       | Activates when an organization has only one owner.                                  |
| Repo Admin With No Admin Activity                                         | Activates when a repository admin has not performed any admin activity.             |
| Too Many Repo Admins                                                      | Activates when the number of repository admins exceeds the recommended limit.       |
| Repo Wiki Publicly Editable                                               | Activates when a repository wiki can be edited by the public.                       |
| Developer Did Not Write Code in Repo                                      | Activates when a developer is listed but has no code contributions.                 |
| Outside Collaborator Is a Repo Admin                                      | Activates when an outside collaborator has repository admin permissions.            |
| Outside Collaborator Is a Repo Maintainer                                 | Activates when an outside collaborator has repository maintainer permissions.       |
| Outside Collaborator With No Activity                                     | Activates when an outside collaborator has no recorded activity.                    |
| Outside Collaborator Not Using 2FA                                        | Activates when an outside collaborator does not use two-factor authentication.      |
| Missing 2FA in Organization                                               | Activates when the organization does not enforce two-factor authentication.         |
| Bot User Is an Org Owner                                                  | Activates when a bot user has organization owner permissions.                       |
| Bot User Is a Repo Admin                                                  | Activates when a bot user has repository admin permissions.                         |
| License File Missing in Repo                                              | Activates when a repository does not include a license file.                        |
| Security Policy File Missing in Repo                                      | Activates when a repository does not include a security policy file.                |
| CODEOWNERS File Missing in Repo                                           | Activates when a repository does not include a CODEOWNERS file.                     |
| Unarchived Stale Repo                                                     | Activates when a stale repository remains unarchived.                               |

## Regular scan code security triggers

These triggers activate when issues are detected in source code during static analysis.\
They help identify insecure coding practices, logic flaws, and maintainability risks.

| Trigger name             | Description                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| Any code security policy | Activates when any code security issue is detected.                                                                     |
| SAST issue               | Activates when a static application security testing (SAST) tool identifies a vulnerability in code.                    |
| Code smell issue         | Activates when a code smell or maintainability problem is detected, such as unused variables or overly complex methods. |

## Regular scan secret/PII scan triggers

These triggers activate when secrets or personally identifiable information (PII) are detected in code, logs, or version history.\
They help prevent sensitive data from being exposed in repositories.

| Trigger name               | Description                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Any secret/PII scan policy | Activates when any secret or PII-related issue is detected.                                         |
| Secret in code             | Activates when a secret, such as an API key, password, or token, is found in source code.           |
| Secret in Git history      | Activates when a secret is found in the Git commit history.                                         |
| Secret logging in code     | Activates when a secret is written to logs by the code.                                             |
| PII embedded in code       | Activates when personal data, such as names, emails, or identifiers, is hardcoded into source code. |
| PII logging in code        | Activates when personal data is written to logs by the code.                                        |
| PII in Git history         | Activates when personal data is found in the Git commit history.                                    |

## Regular scan open source security triggers

These triggers activate when vulnerabilities or risks are detected in open source components.\
They help manage CVEs in dependencies, images, and manifests across different environments.

| Trigger name                                         | Description                                                                                         |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Any open source security policy                      | Activates when any open source security issue is detected.                                          |
| Vulnerable dependency (CVE) in code                  | Activates when a code dependency contains a known vulnerability (CVE).                              |
| Vulnerable base image (CVE) in Dockerfile            | Activates when a base image defined in a Dockerfile contains a known vulnerability.                 |
| Vulnerable public image (CVE) in Docker Compose      | Activates when a public image referenced in a Docker Compose file contains a known vulnerability.   |
| Vulnerable public image (CVE) in Kubernetes manifest | Activates when a public image used in a Kubernetes manifest contains a known vulnerability.         |
| Vulnerable public image (CVE) in Helm chart          | Activates when a public image referenced in a Helm chart contains a known vulnerability.            |
| Vulnerable public image (CVE) in Terraform           | Activates when a public image referenced in Terraform configuration contains a known vulnerability. |
| Vulnerable public image (CVE) in CI/CD deployment    | Activates when a public image used in a CI/CD deployment contains a known vulnerability.            |

## Regular scan SBOM triggers

These triggers activate when issues are detected in the software bill of materials (SBOM).\
They help identify risks in dependencies, licenses, and package sources.

| Trigger name                                           | Description                                                                                              |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Any SBOM policy                                        | Activates when any SBOM-related issue is detected.                                                       |
| Typosquatting dependency in code                       | Activates when a dependency name closely resembles a popular package, suggesting a typosquatting attack. |
| Malicious dependency in code                           | Activates when a dependency is identified as malicious.                                                  |
| Dependency confusion: organization scope in code       | Activates when a dependency in organization scope is at risk of dependency confusion.                    |
| Dependency confusion: private package in code          | Activates when a private package is at risk of dependency confusion.                                     |
| Unapproved license used by direct dependency in code   | Activates when a direct dependency uses a license that is not approved.                                  |
| Unapproved license used in forked open source          | Activates when a forked open source project includes an unapproved license.                              |
| Unapproved license detected by 3rd party security app  | Activates when a third-party security application detects an unapproved license.                         |
| Deprecated direct dependency in code                   | Activates when a direct dependency is marked as deprecated.                                              |
| Outdated direct dependency in code                     | Activates when a direct dependency is outdated and no longer maintained.                                 |
| Unpopular direct dependency in code                    | Activates when a direct dependency is rarely used across the ecosystem, increasing risk of poor support. |
| Unused direct dependency in code                       | Activates when a direct dependency is included but not used in the codebase.                             |
| Unapproved license used by indirect dependency in code | Activates when an indirect (transitive) dependency uses a license that is not approved.                  |
| Deprecated indirect dependency in code                 | Activates when an indirect dependency is marked as deprecated.                                           |
| Outdated indirect dependency in code                   | Activates when an indirect dependency is outdated and no longer maintained.                              |
| Unpopular indirect dependency in code                  | Activates when an indirect dependency is rarely used across the ecosystem.                               |
| Untrusted source for dependency in code                | Activates when a dependency originates from an untrusted or unverified source.                           |

## Regular scan CI/CD posture triggers

These triggers activate when risks or misconfigurations are detected in CI/CD pipelines and workflows.\
They help secure automation processes, prevent misuse of secrets, and ensure least-privilege practices.

| Trigger name                                 | Description                                                                       |
| -------------------------------------------- | --------------------------------------------------------------------------------- |
| Any CI/CD posture policy                     | Activates when any CI/CD-related posture issue is detected.                       |
| CI/CD workflow security issue                | Activates when a generic CI/CD workflow security issue is identified.             |
| Secret echoed in workflow console            | Activates when a secret is printed to the CI/CD logs.                             |
| Deprecated command in workflow               | Activates when a workflow uses a deprecated command.                              |
| CI/CD context values in workflow             | Activates when context values in workflows expose sensitive information.          |
| CI/CD bot can approve code review            | Activates when a CI/CD automation bot has permission to approve code reviews.     |
| Incorrect storage of secret in GitHub Action | Activates when secrets are improperly stored in GitHub Actions workflows.         |
| Excessive permissions in workflow file       | Activates when a workflow file is configured with unnecessary privileges.         |
| Excessive permissions in workflow setting    | Activates when workflow configuration grants excessive permissions.               |
| Unpinned (SHA) third-party actions in GitHub | Activates when GitHub Actions are used without pinning to a secure commit SHA.    |
| Unauthorized serverless function deployment  | Activates when a serverless function is deployed without authorization.           |
| Unauthorized CI/CD used                      | Activates when an unapproved CI/CD platform is used in the organization.          |
| Malicious webhook                            | Activates when a webhook is flagged as malicious.                                 |
| Suspicious webhook                           | Activates when webhook activity is suspicious but not yet confirmed as malicious. |
| Webhook with unknown reputation              | Activates when a webhook source cannot be verified.                               |
| Anomaly in webhook usage                     | Activates when unusual or abnormal webhook behavior is detected.                  |
| Webhook without SSL/TLS                      | Activates when a webhook is not protected with SSL/TLS encryption.                |
| Webhook without secret key                   | Activates when a webhook does not use a secret key for validation.                |

## Regular scan security tool coverage triggers

These triggers activate when gaps are detected in the use of security tools.\
They help identify missing, disabled, or unsupported tools across CI/CD pipelines.

| Trigger name                                   | Description                                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Any security tool coverage policy              | Activates when any issue related to security tool coverage is detected.                     |
| SAST missing in CI/CD pipeline                 | Activates when static application security testing (SAST) is not included in a pipeline.    |
| SAST disabled                                  | Activates when SAST is present but turned off.                                              |
| SAST unsupported language                      | Activates when SAST cannot analyze code due to an unsupported language.                     |
| Open source security missing in CI/CD pipeline | Activates when open source security scanning is not included in a pipeline.                 |
| Open source security disabled                  | Activates when open source security scanning is present but turned off.                     |
| Open source security unsupported language      | Activates when open source security scanning cannot analyze due to an unsupported language. |
| Secrets detection missing in CI/CD pipeline    | Activates when secret scanning is not included in a pipeline.                               |

## Regular scan container security triggers

These triggers activate when vulnerabilities, misconfigurations, or risks are found in container images.\
They help ensure that containerized applications are secure before deployment.

| Trigger name                                                           | Description                                                                                           |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Any container security policy                                          | Activates when any container security issue is detected.                                              |
| Vulnerable dependency (CVE) in container from user code                | Activates when a CVE is detected in dependencies added by user code inside a container.               |
| Vulnerable dependency (CVE) in container from user instruction         | Activates when a CVE is detected in dependencies added through build instructions (e.g., Dockerfile). |
| Vulnerable dependency (CVE) in container from base image               | Activates when a CVE is detected in the base image used for building a container.                     |
| Vulnerable dependency (CVE) in container from operating system         | Activates when a CVE is detected in the operating system packages inside a container.                 |
| Vulnerable dependency (CVE) in public image hosted in private registry | Activates when a CVE is detected in a public image stored in a private registry.                      |
| Vulnerable dependency (CVE) in Java archive package                    | Activates when a CVE is detected in a Java archive (JAR) package within a container.                  |
| Secret in container                                                    | Activates when secrets are detected inside a container image.                                         |
| PII in container                                                       | Activates when personally identifiable information (PII) is detected inside a container image.        |
| Unapproved dependency license in container                             | Activates when a container contains a dependency with a disallowed license.                           |
| Misconfiguration in container                                          | Activates when a container configuration does not comply with security best practices.                |

## Regular scan dynamic app security triggers

These triggers activate when issues are detected by dynamic application security testing (DAST).\
They help identify vulnerabilities exposed during runtime.

| Trigger name                    | Description                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| Any dynamic app security policy | Activates when any DAST-related issue is detected.                                   |
| DAST issue                      | Activates when a vulnerability is detected during dynamic testing of an application. |

## Regular scan artifact integrity triggers

These triggers activate when artifacts used in builds or deployments come from untrusted or unverified sources.\
They help ensure supply chain integrity.

| Trigger name                                | Description                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------ |
| Any artifact integrity policy               | Activates when any artifact integrity issue is detected.                       |
| Registry artifact not from CI/CD            | Activates when an artifact originates outside of the CI/CD pipeline.           |
| Cloud artifact is not from trusted registry | Activates when an artifact is pulled from an unapproved or untrusted registry. |

## Regular scan cloud context triggers

These triggers activate when cloud-specific vulnerabilities or misconfigurations are detected.\
They help secure cloud environments, workloads, and services.

| Trigger name                                        | Description                                                                              |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Any cloud context policy                            | Activates when any cloud security issue is detected.                                     |
| CSPM issue                                          | Activates when a cloud security posture management (CSPM) tool finds a misconfiguration. |
| CSPM secret                                         | Activates when secrets are exposed in cloud CSPM scans.                                  |
| Runtime open source vulnerability                   | Activates when an open source vulnerability is detected in a cloud runtime environment.  |
| Runtime operating system vulnerability              | Activates when an OS vulnerability is detected in a cloud runtime.                       |
| Vulnerable dependency (CVE) in VM                   | Activates when a CVE is detected in a virtual machine.                                   |
| Vulnerable public image (CVE) in Kubernetes cluster | Activates when a vulnerable public image is deployed in a Kubernetes cluster.            |
| Vulnerable dependency (CVE) in cloud functions      | Activates when a CVE is detected in a cloud function dependency.                         |
| SAST in cloud functions                             | Activates when a static analysis finding is detected in cloud function code.             |
| Secrets in cloud functions                          | Activates when secrets are detected in cloud functions.                                  |
| SAST in runtime                                     | Activates when a static analysis finding is detected in runtime workloads.               |
| Secret in runtime                                   | Activates when secrets are detected in runtime workloads.                                |
| Vulnerability management                            | Activates when cloud vulnerability management identifies issues.                         |

## Regular scan manual upload triggers

These triggers activate when issues are added manually to the platform.\
They help track findings imported outside of automated scanning.

| Trigger name             | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Any manual upload policy | Activates when any issue from a manual upload is detected.   |
| Manual issues upload     | Activates when issues are uploaded manually into the system. |
