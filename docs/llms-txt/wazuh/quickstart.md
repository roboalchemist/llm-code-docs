# Source: https://documentation.wazuh.com/current/quickstart.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Quickstart

Wazuh is a security platform that provides unified XDR and SIEM protection for endpoints and cloud workloads. The solution is composed of a single universal agent and three central components: the Wazuh server, the Wazuh indexer, and the Wazuh dashboard. For more information, check the [Getting Started](getting-started/index.md) documentation.

Wazuh is free and open source. Its components abide by the [GNU General Public License, version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html), and the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) (ALv2).

This quickstart shows you how to install the Wazuh central components, on the same host, using our installation assistant. You can check our [Installation guide](installation-guide/index.md) for more details and other installation options.

Below you can find a section about the requirements needed to install Wazuh. It will help you learn about the hardware requirements and the supported operating systems for your Wazuh installation.

<a id="installation-requirements"></a>

## Requirements

### Hardware

Hardware requirements highly depend on the number of protected endpoints and cloud workloads. This number can help estimate how much data will be analyzed and how many security alerts will be stored and indexed.

Following this quickstart implies deploying the Wazuh server, the Wazuh indexer, and the Wazuh dashboard on the same host. This is usually enough for monitoring up to 100 endpoints and for 90 days of queryable/indexed alert data. The table below shows the recommended hardware for a quickstart deployment:

| **Agents**   | **CPU**   | **RAM**   | **Storage (90 days)**   |
|--------------|-----------|-----------|-------------------------|
| **1â25**     | 4 vCPU    | 8 GiB     | 50 GB                   |
| **25â50**    | 8 vCPU    | 8 GiB     | 100 GB                  |
| **50â100**   | 8 vCPU    | 8 GiB     | 200 GB                  |

For larger environments we recommend a distributed deployment. Multi-node cluster configuration is available for the Wazuh server and for the Wazuh indexer, providing high availability and load balancing.

### Operating system

The Wazuh central components require a 64-bit Intel, AMD, or ARM Linux processor (x86_64/AMD64 or AARCH64/ARM64 architecture) to run. Wazuh recommends any of the following operating system versions:

<!-- Copyright (C) 2015, Wazuh, Inc. -->
- Amazon Linux 2, Amazon Linux 2023
- CentOS Stream 10
- Red Hat Enterprise Linux 7, 8, 9, 10
- Ubuntu 16.04, 18.04, 20.04, 22.04, 24.04

<!-- End of include file -->

<a id="quickstart-installing-wazuh"></a>

## Installing Wazuh

1. Download and run the Wazuh installation assistant.
   ```console
   $ curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
   ```

   Once the assistant finishes the installation, the output shows the access credentials and a message that confirms that the installation was successful.
   ```none
   INFO: --- Summary ---
   INFO: You can access the web interface https://<WAZUH_DASHBOARD_IP_ADDRESS>
       User: admin
       Password: <ADMIN_PASSWORD>
   INFO: Installation finished.
   ```

   You now have installed and configured Wazuh.
2. Access the Wazuh web interface with `https://<WAZUH_DASHBOARD_IP_ADDRESS>` and your credentials:
   - **Username**: `admin`
   - **Password**: `<ADMIN_PASSWORD>`

When you access the Wazuh dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. This is expected and the user has the option to accept the certificate as an exception or, alternatively, configure the system to use a certificate from a trusted authority.

#### NOTE
You can find the passwords for all the Wazuh indexer and Wazuh API users in the `wazuh-passwords.txt` file inside `wazuh-install-files.tar`. To print them, run the following command:

> ```console
> $ sudo tar -O -xvf wazuh-install-files.tar wazuh-install-files/wazuh-passwords.txt
> ```

If you want to uninstall the Wazuh central components, run the Wazuh installation assistant using the option `-u` or `â-uninstall`.

<!-- Copyright (C) 2015, Wazuh, Inc. -->

#### NOTE
**Recommended Action**: Disable Wazuh Updates.

We recommend disabling the Wazuh package repositories after installation to prevent accidental upgrades that could break the environment.

Execute the following command to disable the Wazuh repository:

YUM

APT (Debian/Ubuntu)

```console
# sed -i "s/^enabled=1/enabled=0/" /etc/yum.repos.d/wazuh.repo
```

```console
# sed -i "s/^deb /#deb /" /etc/apt/sources.list.d/wazuh.list
# apt update
```

<!-- End of include file -->

## Next steps

Now that your Wazuh installation is ready, you can start deploying the Wazuh agent. This can be used to protect laptops, desktops, servers, cloud instances, containers, or virtual machines. The agent is lightweight and multi-purpose, providing a variety of security capabilities.

Instructions on how to deploy the Wazuh agent can be found in the Wazuh web user interface, or in our [documentation](installation-guide/wazuh-agent/index.md).

<div class="link-boxes-group layout-6">
  <div class="link-boxes-item">
    <a class="link-boxes-link" href="installation-guide/wazuh-agent/wazuh-agent-package-linux.md">
      <p class="link-boxes-label">Linux</p>![image](images/installation/linux.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="installation-guide/wazuh-agent/wazuh-agent-package-windows.md">
    <p class="link-boxes-label">Windows</p>![image](images/installation/windows-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="installation-guide/wazuh-agent/wazuh-agent-package-macos.md">
    <p class="link-boxes-label">macOS</p>![image](images/installation/macOS-logo.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="installation-guide/wazuh-agent/wazuh-agent-package-solaris.md">
    <p class="link-boxes-label">Solaris</p>![image](images/installation/solaris.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="installation-guide/wazuh-agent/wazuh-agent-package-aix.md">
    <p class="link-boxes-label">AIX</p>![image](images/installation/AIX.png)  </a>
</div>
<div class="link-boxes-item">
  <a class="link-boxes-link" href="installation-guide/wazuh-agent/wazuh-agent-package-hpux.md">
    <p class="link-boxes-label">HP-UX</p>![image](images/installation/hpux.png)    </a>
  </div>
</div>
