# Source: https://documentation.wazuh.com/current/installation-guide/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="installation-guide"></a>

# Installation guide

Wazuh is a security platform that provides unified XDR and SIEM protection for endpoints and cloud workloads. The solution is composed of the [Wazuh agent](../getting-started/components/wazuh-agent.md) and three central components: the [Wazuh server](../getting-started/components/wazuh-server.md), the [Wazuh indexer](../getting-started/components/wazuh-indexer.md), and the [Wazuh dashboard](../getting-started/components/wazuh-dashboard.md). For more information, check the [Getting Started](../getting-started/index.md) documentation.

Wazuh is free and open source. Its components abide by the [GNU General Public License, version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html), and the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) (ALv2).

In this installation guide, you will learn how to install Wazuh in your infrastructure. We also offer [Wazuh Cloud](https://wazuh.com/cloud/), our software as a service (SaaS) solution. Wazuh Cloud is ready to use, with no additional hardware or software required, reducing the cost and complexity. Check the [Wazuh Cloud service](../cloud-service/index.md) documentation for more information and take advantage of the [Wazuh Cloud trial](https://console.cloud.wazuh.com/sign-up?landing=trial) to explore this service.

## Installing the Wazuh central components

You can install the Wazuh indexer, Wazuh server, and Wazuh dashboard on a single host or distribute them in cluster configurations. Each Wazuh central component supports two installation methods and both methods provide instructions to install the central components on a single host or on separate hosts.

You can check our [Quickstart](../quickstart.md) documentation to perform an all-in-one installation. This is the fastest way to get the Wazuh central components up and running.

For more deployment flexibility and customization, install the Wazuh central components by starting with the [Wazuh indexer](wazuh-indexer/index.md) deployment. This deployment method supports both an all-in-one installation and installing components on separate hosts.

Follow this installation workflow:

<div class="link-boxes-group layout-3" data-step="0">
  <div class="steps-line">
    <div class="steps-number future-step">1</div>
    <div class="steps-number future-step">2</div>
    <div class="steps-number future-step">3</div>
  </div>
  <div class="link-boxes-item future-step">
    <a class="link-boxes-link" href="wazuh-indexer/index.md">
      <p class="link-boxes-label">Install the Wazuh indexer</p>![image](images/installation/Indexer-noBG.png)  </a>
</div>

<div class="link-boxes-item future-step">
  <a class="link-boxes-link" href="wazuh-server/index.md">
    <p class="link-boxes-label">Install the Wazuh server</p>![image](images/installation/Server-noBG.png)  </a>
</div>

<div class="link-boxes-item future-step">
  <a class="link-boxes-link" href="wazuh-dashboard/index.md">
    <p class="link-boxes-label">Install the Wazuh dashboard</p>![image](images/installation/Dashboard-noBG.png)    </a>
  </div>
</div>

<a id="installing-the-wazuh-agent"></a>

## Installing the Wazuh agent

The Wazuh agent is a single, lightweight monitoring software. It is a multi-platform component that you can deploy to laptops, desktops, servers, cloud instances, containers, or virtual machines. It provides visibility into the monitored endpoint by collecting critical system and application records, inventory data, and detecting potential anomalies.

Select your endpoint operating system below and follow the installation steps to deploy the Wazuh agent.

<div class="link-boxes-group layout-6">
  <div class="link-boxes-item">
    <a class="link-boxes-link" href="./wazuh-agent/wazuh-agent-package-linux.md">
      <p class="link-boxes-label">Linux</p>![image](images/installation/linux.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/wazuh-agent-package-windows.md">
    <p class="link-boxes-label">Windows</p>![image](images/installation/windows-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/wazuh-agent-package-macos.md">
    <p class="link-boxes-label">macOS</p>![image](images/installation/macOS-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/wazuh-agent-package-solaris.md">
    <p class="link-boxes-label">Solaris</p>![image](images/installation/solaris.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/wazuh-agent-package-aix.md">
    <p class="link-boxes-label">AIX</p>![image](images/installation/AIX.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/wazuh-agent-package-hpux.md">
    <p class="link-boxes-label">HP-UX</p>![image](images/installation/hpux.png)    </a>
  </div>
</div>

## Packages list

The [Packages list](packages-list.md) section contains all the packages required for installing Wazuh.

## Uninstalling Wazuh

In the [Uninstalling Wazuh](uninstalling-wazuh/index.md) section, you will find instructions on how to uninstall the Wazuh central components and the Wazuh agent.

## Installation alternatives

Wazuh provides other [installation alternatives](../deployment-options/index.md) as well. These are complementary to the installation methods of this installation guide. You will find instructions on how to deploy Wazuh using ready-to-use machines, containers, and orchestration tools. There is also information on how to install the solution offline, from sources, and with alternative components.

* [Wazuh indexer](wazuh-indexer/index.md)
* [Wazuh server](wazuh-server/index.md)
* [Wazuh dashboard](wazuh-dashboard/index.md)
* [Wazuh agent](wazuh-agent/index.md)
* [Packages list](packages-list.md)
* [Uninstalling Wazuh](uninstalling-wazuh/index.md)
