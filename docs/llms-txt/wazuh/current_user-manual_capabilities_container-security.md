# Source: https://documentation.wazuh.com/current/user-manual/capabilities/container-security/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Container security

Container security involves implementing measures and practices to ensure the protection and availability of containers and the applications they contain, thereby safeguarding their integrity and confidentiality. Wazuh provides several capabilities and features to help organizations secure their container environments, including centralized logging, real-time monitoring, vulnerability scanning, and incident response automation.

Wazuh enables users to effectively monitor container platforms like [Docker](monitoring-docker.md), providing comprehensive visibility into container resources, including [monitoring container health](https://wazuh.com/blog/docker-container-security-monitoring-with-wazuh/). Additionally, Wazuh offers the capability to [audit Kubernetes](https://wazuh.com/blog/auditing-kubernetes-with-wazuh/) infrastructure, ensuring a holistic approach to container security and monitoring.

* [Using Wazuh to monitor Docker](monitoring-docker.md)
  * [Enable the Wazuh Docker listener](monitoring-docker.md#enable-the-wazuh-docker-listener)
  * [Wazuh Docker dashboard](monitoring-docker.md#wazuh-docker-dashboard)
  * [Wazuh Docker listener configuration options](monitoring-docker.md#wazuh-docker-listener-configuration-options)
  * [Example configuration](monitoring-docker.md#example-configuration)
* [Use cases](use-cases.md)
  * [Requirements](use-cases.md#requirements)
  * [Monitoring user interaction with Docker resources](use-cases.md#monitoring-user-interaction-with-docker-resources)
  * [Monitoring container runtime](use-cases.md#monitoring-container-runtime)
