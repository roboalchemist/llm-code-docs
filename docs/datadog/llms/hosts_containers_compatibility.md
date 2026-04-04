# Source: https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/hosts_containers_compatibility.md

---
title: Cloud Security Vulnerabilities Hosts and Containers Compatibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Vulnerabilities >
  Cloud Security Vulnerabilities Hosts and Containers Compatibility
---

# Cloud Security Vulnerabilities Hosts and Containers Compatibility

## Operating systems{% #operating-systems %}

Cloud Security Vulnerabilities supports vulnerability scanning for hosts and containers running the following operating system versions:

| Operating System         | Supported Versions                                  | Package Managers / Source | Agentless support | Agent support |
| ------------------------ | --------------------------------------------------- | ------------------------- | ----------------- | ------------- |
| Alpine Linux             | 2.2-2.7, 3.0-3.19 (edge is not supported)           | apk                       | yes               | yes           |
| Wolfi Linux              | N/A                                                 | apk                       | yes               | yes           |
| Chainguard               | N/A                                                 | apk                       | yes               | yes           |
| Red Hat Enterprise Linux | 6, 7, 8, 9                                          | dnf/yum/rpm               | yes               | yes           |
| CentOS                   | 6, 7, 8                                             | dnf/yum/rpm               | yes               | yes           |
| AlmaLinux                | 8, 9                                                | dnf/yum/rpm               | yes               | yes           |
| Rocky Linux              | 8, 9                                                | dnf/yum/rpm               | yes               | yes           |
| Oracle Linux             | 5, 6, 7, 8                                          | dnf/yum/rpm               | yes               | yes           |
| CBL-Mariner              | 1.0, 2.0                                            | dnf/yum/rpm               | yes               | yes           |
| Amazon Linux             | 1, 2, 2023                                          | dnf/yum/rpm               | yes               | yes           |
| openSUSE Leap            | 42, 15                                              | zypper/rpm                | yes               | yes           |
| SUSE Enterprise Linux    | 11, 12, 15                                          | zypper/rpm                | yes               | yes           |
| Photon OS                | 1.0, 2.0, 3.0, 4.0                                  | tndf/yum/rpm              | yes               | yes           |
| Debian GNU/Linux         | 7, 8, 9, 10, 11, 12 (unstable/sid is not supported) | apt/dpkg                  | yes               | yes           |
| Ubuntu                   | All versions supported by Canonical                 | apt/dpkg                  | yes               | yes           |
| Windows                  | Windows Server 2016/2019/2022, Windows 10 and later | Windows OS                | yes               | yes           |

{% alert level="info" %}
Datadog supports official OS packages from vendors listed above. Third-party or self-compiled packages are not supported.
{% /alert %}

{% collapsible-section %}
#### Windows limitations

- Datadog detects vulnerabilities in Windows by identifying the Windows version and installed security knowledge base (KB) updates to address vulnerabilities associated with that version. However, some KB updates are cumulative and contain other KB updates, which might cause Datadog to misidentify which updates have been installed.

- Datadog can't track vulnerability fixes that Windows applies outside of KB updates.

- Datadog can't track vulnerabilities associated with third-party software.

{% /collapsible-section %}

## Application libraries{% #application-libraries %}

Cloud Security Vulnerabilities supports vulnerability scanning for the following application languages and libraries on containers and Lambda instances:

| Language | Supported Package Manager | Supported Files                                                      | Agentless support | Agent support |
| -------- | ------------------------- | -------------------------------------------------------------------- | ----------------- | ------------- |
| Ruby     | bundler                   | Gemfile.lock, gemspec                                                | yes               | yes           |
| .NET     | nuget                     | packages.lock.json, packages.config, .deps.json, *packages.props     | yes               | yes           |
| Go       | mod                       | Binaries built by Go, go.mod                                         | yes               | yes           |
| Java     | Gradle, Maven             | pom.xml, *gradle.lockfile, JAR/WAR/PAR/EAR (with pom.properties)     | yes               | yes           |
| Node.js  | npm, pnpm, yarn           | package-lock.json, yarn.lock, pnpm-lock.yaml, package.json           | yes               | yes           |
| PHP      | composer                  | composer.lock                                                        | yes               | yes           |
| Python   | pip, poetry               | pipfile.lock, poetry.lock, egg package, wheel package, conda package | yes               | yes           |

**Note**: Agent-based vulnerability management in application libraries is available in Agent versions [7.64 or newer](https://github.com/DataDog/datadog-agent/releases).
