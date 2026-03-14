# Source: https://docs.kubearmor.io/kubearmor/readme.md

# KubeArmor

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e6d14fd78f87efa0b8803a3f6fdf04093d66d094%2Flogo.png?alt=media\&token=eda680df-7fab-4fd4-8788-6cddfd25b707)

[![Build Status](https://github.com/kubearmor/KubeArmor/actions/workflows/ci-test-ginkgo.yml/badge.svg)](https://github.com/kubearmor/KubeArmor/actions/workflows/ci-test-ginkgo.yml/) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5401/badge)](https://bestpractices.coreinfrastructure.org/projects/5401) [![CLOMonitor](https://img.shields.io/endpoint?url=https://clomonitor.io/api/projects/cncf/kubearmor/badge)](https://clomonitor.io/projects/cncf/kubearmor) [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/kubearmor/kubearmor/badge)](https://securityscorecards.dev/viewer/?uri=github.com/kubearmor/KubeArmor) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor.svg?type=shield\&issueType=license)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor?ref=badge_shield) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor.svg?type=shield\&issueType=security)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor?ref=badge_shield) [![Slack](https://img.shields.io/badge/Join%20Our%20Community-Slack-blue)](https://cloud-native.slack.com/archives/C02R319HVL3) [![Discussions](https://img.shields.io/badge/Got%20Questions%3F-Chat-Violet)](https://github.com/kubearmor/KubeArmor/discussions) [![Docker Downloads](https://img.shields.io/docker/pulls/kubearmor/kubearmor)](https://hub.docker.com/r/kubearmor/kubearmor) [![ArtifactHub](https://img.shields.io/badge/ArtifactHub-KubeArmor-blue?logo=artifacthub\&labelColor=grey\&color=green)](https://artifacthub.io/packages/search?kind=19)

KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operations) of pods, containers, and nodes (VMs) at the system level.

KubeArmor leverages [Linux security modules (LSMs)](https://en.wikipedia.org/wiki/Linux_Security_Modules) such as [AppArmor](https://en.wikipedia.org/wiki/AppArmor), [SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux), or [BPF-LSM](https://docs.kernel.org/bpf/prog_lsm.html) to enforce the user-specified policies. KubeArmor generates rich alerts/telemetry events with container/pod/namespace identities by leveraging eBPF.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><span data-gb-custom-inline data-tag="emoji" data-code="1f4aa">💪</span> <a href="use-cases/hardening_guide"><strong>Harden Infrastructure</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="26d3">⛓️</span> Protect critical paths such as cert bundles<br><span data-gb-custom-inline data-tag="emoji" data-code="1f4cb">📋</span> MITRE, STIGs, CIS based rules<br><span data-gb-custom-inline data-tag="emoji" data-code="1f6c5">🛅</span> Restrict access to raw DB table</p>          | <p><span data-gb-custom-inline data-tag="emoji" data-code="1f48d">💍</span> <a href="use-cases/least_permissive_access"><strong>Least Permissive Access</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="1f6a5">🚥</span> Process Whitelisting<br><span data-gb-custom-inline data-tag="emoji" data-code="1f6a5">🚥</span> Network Whitelisting<br><span data-gb-custom-inline data-tag="emoji" data-code="1f39b">🎛️</span> Control access to sensitive assets</p>                                       |
| <p><span data-gb-custom-inline data-tag="emoji" data-code="1f52d">🔭</span> <a href="use-cases/workload_visibility"><strong>Application Behavior</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="1f9ec">🧬</span> Process execs, File System accesses<br><span data-gb-custom-inline data-tag="emoji" data-code="1f9ed">🧭</span> Service binds, Ingress, Egress connections<br><span data-gb-custom-inline data-tag="emoji" data-code="1f52c">🔬</span> Sensitive system call profiling</p> | <p><span data-gb-custom-inline data-tag="emoji" data-code="2744">❄️</span> <a href="https://github.com/kubearmor/KubeArmor/blob/main/getting-started/deployment_models.md"><strong>Deployment Models</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="2638">☸️</span> Kubernetes Deployment<br><span data-gb-custom-inline data-tag="emoji" data-code="1f40b">🐋</span> Containerized Deployment<br><span data-gb-custom-inline data-tag="emoji" data-code="1f4bb">💻</span> VM/Bare-Metal Deployment</p> |

### Architecture Overview

![KubeArmor High Level Design](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-90da4830ad1a4916e7a413447a25e78ba3a7c18b%2Fkubearmor_overview.png?alt=media)

### Documentation :notebook:

* :point\_right: [Getting Started](https://docs.kubearmor.io/kubearmor/quick-links/deployment_guide)
* :dart: [Use Cases](https://docs.kubearmor.io/kubearmor/use-cases/hardening)
* :heavy\_check\_mark: [KubeArmor Support Matrix](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix)
* :chess\_pawn: [How is KubeArmor different?](https://docs.kubearmor.io/kubearmor/quick-links/differentiation)
* :scroll: Security Policy for Pods/Containers \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/security_policy_examples)]
* :scroll: Cluster level security Policy for Pods/Containers \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/cluster_security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/cluster_security_policy_examples)]
* :scroll: Security Policy for Hosts/Nodes \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/host_security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/host_security_policy_examples)]
* :scroll: Network Security Policy for Hosts/Nodes \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/network_security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/network_security_policy_examples)]\
  ... [detailed documentation](https://docs.kubearmor.io/kubearmor/)

#### Contributors :busts\_in\_silhouette

* :blue\_book: [Contribution Guide](https://docs.kubearmor.io/kubearmor/contribution/contribution_guide)
* :technologist: [Development Guide](https://docs.kubearmor.io/kubearmor/contribution/development_guide), [Testing Guide](https://docs.kubearmor.io/kubearmor/contribution/testing_guide)
* :raised\_hand: [Join KubeArmor Slack](https://cloud-native.slack.com/archives/C02R319HVL3)
* :question: [FAQs](https://docs.kubearmor.io/kubearmor/documentation/faq)

#### Biweekly Meeting

* :speaking\_head: [Zoom Link](http://zoom.kubearmor.io)
* :page\_facing\_up: Minutes: [Document](https://docs.google.com/document/d/1IqIIG9Vz-PYpbUwrH0u99KYEM1mtnYe6BHrson4NqEs/edit)
* :calendar: Calendar invite: [Google Calendar](http://www.google.com/calendar/event?action=TEMPLATE\&dates=20220210T150000Z%2F20220210T153000Z\&text=KubeArmor%20Community%20Call\&location=\&details=%3Ca%20href%3D%22https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1IqIIG9Vz-PYpbUwrH0u99KYEM1mtnYe6BHrson4NqEs%2Fedit%22%3EMinutes%20of%20Meeting%3C%2Fa%3E%0A%0A%3Ca%20href%3D%22%20http%3A%2F%2Fzoom.kubearmor.io%22%3EZoom%20Link%3C%2Fa%3E\&recur=RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TH\&ctz=Asia/Calcutta), [ICS file](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/resources/KubeArmorMeetup.ics)

### Notice/Credits :handshake:

* KubeArmor uses [Tracee](https://github.com/aquasecurity/tracee/)'s system call utility functions.

### CNCF

KubeArmor is [Sandbox Project](https://www.cncf.io/projects/kubearmor/) of the Cloud Native Computing Foundation. ![CNCF SandBox Project](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-4623d5e5b6d7d045cc7650c43a3701994357d19e%2Fcncf-sandbox.png?alt=media\&token=39d1b266-9f97-4c42-9ad8-bcb5b1abcdc8)

### ROADMAP

KubeArmor roadmap is tracked via [KubeArmor Projects](https://github.com/orgs/kubearmor/projects?query=is%3Aopen)
