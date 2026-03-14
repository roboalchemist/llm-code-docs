# Source: https://documentation.wazuh.com/current/upgrade-guide/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Upgrade guide

This guide includes instructions on how to upgrade the Wazuh central components (server, indexer, and dashboard) and the Wazuh agent.

## Wazuh components compatibility

All central Wazuh components must have identical version numbers, including the patch level, for proper operation. Additionally, the Wazuh manager must always be the same version or newer than the Wazuh agents.

Note that Wazuh indexer 4.14.3 is specifically compatible with Filebeat-OSS 7.10.2.

## Upgrade the Wazuh central components

The [Wazuh central components](upgrading-central-components.md) section includes instructions on how to upgrade the Wazuh server, the Wazuh indexer, and the Wazuh dashboard. These instructions apply to both all-in-one deployments and multi-node cluster deployments.

## Upgrade the Wazuh agents

You can upgrade the Wazuh agents either remotely or locally. For remote upgrades, you can use either the Wazuh manager (`agent_upgrade` tool ) or the Wazuh API (via the Wazuh dashboard or a command-line tool). For details, refer to the [remote agent upgrade](../user-manual/agent/agent-management/remote-upgrading/upgrading-agent.md) section.

To perform the upgrade locally, select your operating system and follow the instructions.

<div class="link-boxes-group layout-6">
  <div class="link-boxes-item">
    <a class="link-boxes-link" href="./wazuh-agent/linux.md">
      <p class="link-boxes-label">Linux</p>![image](images/installation/linux.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/windows.md">
    <p class="link-boxes-label">Windows</p>![image](images/installation/windows-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/macos.md">
    <p class="link-boxes-label">macOS</p>![image](images/installation/macOS-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/solaris.md">
    <p class="link-boxes-label">Solaris</p>![image](images/installation/solaris.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/aix.md">
    <p class="link-boxes-label">AIX</p>![image](images/installation/AIX.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="./wazuh-agent/hp-ux.md">
    <p class="link-boxes-label">HP-UX</p>![image](images/installation/hpux.png)    </a>
  </div>
</div>
