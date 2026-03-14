# Source: https://documentation.wazuh.com/current/getting-started/use-cases/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Use cases

The Wazuh platform helps organizations and individuals protect their data assets through threat prevention, detection, and response. Besides, Wazuh is also employed to meet regulatory compliance requirements, such as PCI DSS or HIPAA, and configuration standards like CIS hardening guides.

Moreover, Wazuh is also a solution for users of IaaS (Amazon AWS, Azure, or Google Cloud) to monitor virtual machines and cloud instances. This is done at a system level utilizing the [Wazuh security agent](../components/wazuh-agent.md) and at an infrastructure level pulling data directly from the cloud provider API.

Additionally, Wazuh is employed to protect containerized environments by providing cloud-native runtime security. This feature is based on an integration with the Docker engine API and the Kubernetes API. The Wazuh security agent can run on the Docker host providing a complete set of threat detection and response capabilities.

Below you can find examples of some of the most common use cases of the Wazuh platform.

| Endpoint security                                       | Threat intelligence                                   | Security operations                               | Cloud security                                      |
|---------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------|-----------------------------------------------------|
| [Configuration assessment](configuration-assessment.md) | [Threat hunting](threat-hunting.md)                   | [Incident response](incident-response.md)         | [Container security](container-security.md)         |
| [Malware detection](malware-detection.md)               | [Log data analysis](log-analysis.md)                  | [Regulatory compliance](regulatory-compliance.md) | [Posture management](posture-management.md)         |
| [File integrity monitoring](file-integrity.md)          | [Vulnerability detection](vulnerability-detection.md) | [IT hygiene](it-hygiene.md)                       | [Workload protection](cloud-workload-protection.md) |
