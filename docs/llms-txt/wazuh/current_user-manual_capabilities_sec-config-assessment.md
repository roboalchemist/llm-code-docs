# Source: https://documentation.wazuh.com/current/user-manual/capabilities/sec-config-assessment/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="manual-sec-config-assessment"></a>

# Security Configuration Assessment

Security Configuration Assessment (SCA) is the process of verifying that all systems conform to a set of predefined rules regarding configuration settings and approved application usage. One of the most certain ways to secure endpoints is by reducing their vulnerability surface. This process is commonly known as hardening. Configuration assessment is an effective way to identify weaknesses in your endpoints and patch them to reduce your attack surface.

The Wazuh SCA module performs scans to detect misconfigurations and exposures on monitored endpoints and recommend remediation actions. Those scans assess the configuration of the endpoints using policy files that contain rules to be tested against the actual configuration of the endpoint. SCA policies can check for the existence of files, directories, registry keys and values, running processes, and recursively test for the existence of files inside directories.

For example, the SCA module could assess whether it is necessary to change password-related configuration, remove unnecessary software, disable unnecessary services, or audit the TCP/IP stack configuration.

Policies for the SCA module are written in YAML. This format was chosen because it is human-readable and easy to understand. You can easily write your own SCA policies or extend existing ones to fit your needs. Furthermore, Wazuh is distributed with a set of out-of-the-box policies mostly based on the CIS benchmarks, a well-established standard for endpoint hardening.

Further information is available in the following sections:

* [How SCA works](how-it-works.md)
  * [Overview of an SCA check](how-it-works.md#overview-of-an-sca-check)
  * [Scan Results](how-it-works.md#scan-results)
  * [Integrity mechanisms](how-it-works.md#integrity-mechanisms)
* [How to configure SCA](how-to-configure.md)
  * [Enabling and disabling policies](how-to-configure.md#enabling-and-disabling-policies)
  * [How to share policy files and configuration with the Wazuh agents](how-to-configure.md#how-to-share-policy-files-and-configuration-with-the-wazuh-agents)
* [Available SCA policies](available-sca-policies.md)
* [Creating custom SCA policies](creating-custom-policies.md)
  * [Variables](creating-custom-policies.md#variables)
  * [Checks](creating-custom-policies.md#checks)
* [Use cases](use-cases.md)
  * [Prerequisites](use-cases.md#prerequisites)
  * [Detecting keyword in a file](use-cases.md#detecting-keyword-in-a-file)
  * [Detecting a running process](use-cases.md#detecting-a-running-process)
