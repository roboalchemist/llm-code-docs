# Source: https://documentation.wazuh.com/current/deployment-options/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="deployment"></a>

# Installation alternatives

You can install Wazuh using other deployment options. These are complementary to the installation methods you can find in the  [Installation guide](../installation-guide/index.md) and the [Quickstart](../quickstart.md).

## Installing the Wazuh central components

All the alternatives include instructions on how to install the [Wazuh central components](../getting-started/components/index.md). After these are installed, you then need to deploy agents to your endpoints.

<h3>Ready-to-use machines</h3>
- [Virtual machine (VM)](virtual-machine/virtual-machine.md): Wazuh provides a pre-built virtual machine image (OVA) that you can directly import using VirtualBox or other OVA compatible virtualization systems.
- [Amazon Machine Images (AMI)](amazon-machine-images/amazon-machine-images.md): This is a pre-built Amazon Machine Image (AMI) you can directly launch on an AWS cloud instance.

<h3>Containers</h3>
- [Deployment on Docker](docker/index.md): Docker is a set of platform-as-a-service (PaaS) products that deliver software in packages called containers. Using Docker, you can install and configure the Wazuh deployment as a single-host architecture.
- [Deployment on Kubernetes](deploying-with-kubernetes/index.md): Kubernetes is an open-source system for automating deployment, scaling, and managing containerized applications. This deployment type uses Wazuh images from Docker and allows you to build the Wazuh environment.

<h3>Offline</h3>
- [Offline installation guide](offline-installation/index.md): Installing the solution offline involves downloading the Wazuh components to later install them on a system with no internet connection.

<h3>From sources</h3>
- [Installing the Wazuh server from sources](wazuh-from-sources/index.md): Installing Wazuh from sources means installing the Wazuh manager without using a package manager. You compile the source code and copy the binaries to your computer instead.

#### NOTE
To integrate Wazuh with Elastic or Splunk, refer to our [Integrations guide: Elastic, OpenSearch, Splunk, Amazon Security Lake](../integrations-guide/index.md).

## Installing the Wazuh agent

The [Wazuh agent](../installation-guide/wazuh-agent/index.md) is a single and lightweight monitoring software. It is a multi-platform component that can be deployed to laptops, desktops, servers, cloud instances, containers, or virtual machines. It provides visibility into the endpoint security by collecting critical system and application records, inventory data, and detecting potential anomalies.

If the Wazuh central components are already installed in your environment, select your operating system below and follow the installation steps to deploy the agent on the endpoints.

<div class="link-boxes-group layout-6">
  <div class="link-boxes-item">
    <a class="link-boxes-link" href="../installation-guide/wazuh-agent/wazuh-agent-package-linux.md">
      <p class="link-boxes-label">Linux</p>![image](images/installation/linux.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="../installation-guide/wazuh-agent/wazuh-agent-package-windows.md">
    <p class="link-boxes-label">Windows</p>![image](images/installation/windows-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="../installation-guide/wazuh-agent/wazuh-agent-package-macos.md">
    <p class="link-boxes-label">macOS</p>![image](images/installation/macOS-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="../installation-guide/wazuh-agent/wazuh-agent-package-solaris.md">
    <p class="link-boxes-label">Solaris</p>![image](images/installation/solaris.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="../installation-guide/wazuh-agent/wazuh-agent-package-aix.md">
    <p class="link-boxes-label">AIX</p>![image](images/installation/AIX.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="../installation-guide/wazuh-agent/wazuh-agent-package-hpux.md">
    <p class="link-boxes-label">HP-UX</p>![image](images/installation/hpux.png)    </a>
  </div>
</div><h3>From sources</h3>
- [Installing the Wazuh agent from sources](wazuh-from-sources/wazuh-agent/index.md): Installing Wazuh from sources means installing the Wazuh agent without using a package manager. You compile the source code and copy the binaries to your computer instead.

## Orchestration tools

These alternatives guide you to install the Wazuh central components along with the single universal agent.

- [Deployment with Ansible](deploying-with-ansible/index.md): Ansible is an open source platform designed for automating tasks. Its deployment tool is used to deploy the Wazuh infrastructure on AWS. The Wazuh environment consists of the Wazuh central components and a Wazuh agent.
- [Deployment with Puppet](deploying-with-puppet/index.md): Puppet is an open-source software tool that gives you an automatic way to inspect, deliver, operate, and future-proof all of your software, no matter where it is executed. It is very simple to use and allows you to install and configure Wazuh easily.
