# Source: https://docs.datadoghq.com/agent/supported_platforms.md

---
title: Supported Platforms
description: >-
  Complete list of operating systems and platforms supported by the Datadog
  Agent including Linux, Windows, macOS, and cloud environments.
breadcrumbs: Docs > Agent > Supported Platforms
---

# Supported Platforms

The Datadog Agent is supported on a range of widely used operating systems and platforms. If your operating system is not listed below, [a source installation](https://docs.datadoghq.com/agent/supported_platforms/source/) might work for you.

{% tab title="Linux" %}
## 64-BIT X86

| Operating system                                                                                                                                      | OS versions  | Agent 5 versions | Agent 6 versions | Agent 7 versions |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------- | ---------------- | ---------------- |
| [Amazon Linux](https://docs.datadoghq.com/agent/basic_agent_usage/amazonlinux/)                                                                       | 2            | yes              | yes              | yes              |
| 2022                                                                                                                                                  | \>= 6.40.0   | \>= 7.40.0       |
| 2023                                                                                                                                                  | \>= 6.40.0   | \>= 7.40.0       |
| [Debian](https://docs.datadoghq.com/agent/basic_agent_usage/deb/) (systemd)                                                                           | 7.0 (wheezy) | yes              | <= 6.35.2        | <= 7.35.2        |
| \>= 8.0 (jessie)                                                                                                                                      | yes          | yes              | yes              |
| Debian (SysVinit)                                                                                                                                     | 7.0 (wheezy) | 6.6.0 - 6.35.2   | <= 7.35.2        |
| \>= 8.0 (jessie)                                                                                                                                      | yes          | yes              |
| [Ubuntu](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)                                                                                  | 12.04        | yes              |
| \>= 14.04                                                                                                                                             | yes          | yes              | yes              |
| [RedHat/CentOS/](https://docs.datadoghq.com/agent/basic_agent_usage/redhat/)[Oracle Linux](https://docs.datadoghq.com/agent/basic_agent_usage/oracle) | 5.0          | yes              |
| \>= 6.0                                                                                                                                               | yes          | <= 6.51.1        | <= 7.51.1        |
| \>= 7.0                                                                                                                                               | yes          | yes              |
| [AlmaLinux /Rocky](https://docs.datadoghq.com/agent/basic_agent_usage/redhat/)                                                                        | \>= 8.0      | \>= 6.33.0       | \>= 7.33.0       |
| [SUSE Enterprise Linux (systemd)](https://docs.datadoghq.com/agent/basic_agent_usage/suse/)                                                           | 11 SP4       | yes              | <= 6.32.4        | <= 7.32.4        |
| \>= 12.0                                                                                                                                              | yes          | yes              | yes              |
| SUSE Enterprise Linux (SysVinit)                                                                                                                      | 11 SP4       | 6.16.0 - 6.33.0  | 7.16.0 - 7.33.0  |
| [OpenSUSE (systemd)](https://docs.datadoghq.com/agent/basic_agent_usage/suse/)                                                                        | \>= 15.0     | yes              | yes              | yes              |
| [Fedora](https://docs.datadoghq.com/agent/basic_agent_usage/fedora/)                                                                                  | \>= 26       | yes              | yes              | yes              |

A check mark (
{% icon name="icon-check-bold" /%}
 ) indicates support for all minor and patch versions.

## 64-BIT ARM V8

| Operating system                                                                                                                                        | OS versions       | Agent 6 versions | Agent 7 versions |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- | ---------------- |
| [Amazon Linux](https://docs.datadoghq.com/agent/basic_agent_usage/amazonlinux/)                                                                         | 2                 | \>= 6.16.0       | \>= 7.16.0       |
| 2022                                                                                                                                                    | \>= 6.40.0        | \>= 7.40.0       |
| 2023                                                                                                                                                    | \>= 6.40.0        | \>= 7.40.0       |
| [Debian](https://docs.datadoghq.com/agent/basic_agent_usage/deb/) (systemd)                                                                             | \>= 9.0 (stretch) | \>= 6.16.0       | \>= 7.16.0       |
| [Ubuntu](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)                                                                                    | \>= 16.04         | \>= 6.16.0       | \>= 7.16.0       |
| [RedHat /CentOS/](https://docs.datadoghq.com/agent/basic_agent_usage/redhat/)[Oracle Linux](https://docs.datadoghq.com/agent/basic_agent_usage/oracle/) | \>= 8.0           | \>= 6.16.0       | \>= 7.16.0       |
| [AlmaLinux /Rocky](https://docs.datadoghq.com/agent/basic_agent_usage/redhat/)                                                                          | \>= 8.0           | \>= 6.33.0       | \>= 7.33.0       |
| [Fedora](https://docs.datadoghq.com/agent/basic_agent_usage/fedora/)                                                                                    | \>= 27            | \>= 6.16.0       | \>= 7.16.0       |

{% /tab %}

{% tab title="Windows" %}

| Operating system                                                              | OS versions | Agent 5 versions | Agent 6 versions | Agent 7 versions | Notes                                                                                                             |
| ----------------------------------------------------------------------------- | ----------- | ---------------- | ---------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| [Windows Server](https://docs.datadoghq.com/agent/basic_agent_usage/windows/) | 2008 R2     | yes              | <= 6.45.1        | <= 7.45.1        | Server 2008 R2 is affected by a [known issue with clock drift and Go](https://github.com/golang/go/issues/24489). |
| 2012/R2                                                                       | <= 6.46.0   | <= 7.46.0        |
| 2016, 2019, 2022, 2025                                                        | yes         | yes              |
| Windows                                                                       | 7           | yes              |
| 8.1                                                                           | <= 6.46.0   | <= 7.46.0        |
| 10                                                                            | yes         | yes              |
| 11                                                                            | yes         | yes              |

A check mark (
{% icon name="icon-check-bold" /%}
 ) indicates support for all minor and patch versions.

To install a specific version of the Windows Agent, see the [installer list](https://ddagent-windows-stable.s3.amazonaws.com/installers_v2.json).
{% /tab %}

{% tab title="macOS" %}
## 64-BIT X86

| macOS version | Agent 5         | Agent 6   | Agent 7 |
| ------------- | --------------- | --------- | ------- |
| 10.10 - 10.11 | <= 5.11.3       |
| 10.12         | <= 6.34.0       | <= 7.34.0 |
| 10.13         | <= 6.38.2       | <= 7.38.2 |
| 10.14         | 7.39.0 - 7.61.0 |
| \>= 11.0      | \>= 7.39.0      |

## Apple ARM64{% #apple-arm64 %}

| macOS version | Agent 7     |
| ------------- | ----------- |
| \>= 11.0      | \>= 7.70.0* |

\*Earlier versions for 64-BIT X86 may be used on Apple ARM64 through [Rosetta 2](https://support.apple.com/en-us/102527) emulation.
{% /tab %}

{% tab title="Cloud and containers" %}
## 64-BIT X86 support

| Agent | [Docker](https://docs.datadoghq.com/agent/docker/) | [Kubernetes](https://docs.datadoghq.com/agent/basic_agent_usage/kubernetes/) | [Azure Stack HCI OS](https://docs.datadoghq.com/agent/basic_agent_usage/windows/) |
| ----- | -------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 5     | \>= 1.14                                           | 1.3 - 1.8                                                                    |
| 6     | \>= 1.14                                           | \>= 1.3                                                                      | All versions                                                                      |
| 7     | \>= 1.14                                           | \>= 1.3                                                                      | All versions                                                                      |

## 64-BIT ARM V8 support

Agent 6 and 7 support the following 64-BIT ARM V8 platforms:

| Platform                                                                     | Supported versions | 64-BIT ARM V8 support | 64-BIT X86 support |
| ---------------------------------------------------------------------------- | ------------------ | --------------------- | ------------------ |
| [Docker](https://docs.datadoghq.com/agent/docker/)                           | \>= 1.14           | yes                   | yes                |
| [Kubernetes](https://docs.datadoghq.com/agent/basic_agent_usage/kubernetes/) | \>= 1.3            | yes                   | yes                |

{% /tab %}

{% tab title="Unix" %}
The UNIX Agent supports the following [AIX](https://docs.datadoghq.com/agent/basic_agent_usage/aix/) versions:

- 6.1 TL9 SP6
- 7.1 TL5 SP3
- 7.2 TL3 SP0
- 7.3 TL3 SP0

Note: The Datadog UNIX Agent is developed for specific system architectures, and is not the same as the Windows, Linux, and MacOS Agents.
{% /tab %}

## Further reading{% #further-reading %}

- [The Datadog Agent](https://docs.datadoghq.com/agent/)
