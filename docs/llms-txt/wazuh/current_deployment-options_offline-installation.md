# Source: https://documentation.wazuh.com/current/deployment-options/offline-installation/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Offline installation guide

You can install Wazuh even without an Internet connection. Installing the solution offline involves first downloading the Wazuh central components on a system with Internet access, then transferring and installing them on the offline system. Wazuh supports both all-in-one and distributed deployments. The Wazuh server, indexer, and dashboard can run on the same host in an all-in-one setup, or be installed on separate hosts for a distributed deployment. It supports 64-bit architectures, including x86_64/AMD64 and AARCH64/ARM64.

For more information about the hardware requirements and the recommended operating systems, check the [Requirements](../../quickstart.md#installation-requirements) section.

#### NOTE
You need root user privileges to run all the commands described below.

## Prerequisites

- `curl`, `tar`, and `setcap` need to be installed in the target system where the offline installation will be carried out. `gnupg` might need to be installed as well for some Debian-based systems.
- In some systems, the command `cp` is an alias for `cp -i` â you can check this by running `alias cp`. If this is your case, use `unalias cp` to avoid being asked for confirmation to overwrite files.

## Download the packages and configuration files

From a Linux system with Internet access, run the script below to download all files needed for offline installation. Choose the package format (RPM or DEB) and architecture (x86_64/AMD64 or AARCH64/ARM64).

1. Run the command on any Linux system with Internet access to download and prepare the Wazuh offline installer script
   ```console
   # curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh

   # chmod 744 wazuh-install.sh
   ```
2. Download packages by architecture and format

   RPM

   DEB

   **x86_64 / AMD64**
   ```console
   # ./wazuh-install.sh -dw rpm -da x86_64
   ```

   **AARCH64 / ARM64**
   ```console
   # ./wazuh-install.sh -dw rpm -da aarch64
   ```

   **x86_64 / AMD64**
   ```console
   # ./wazuh-install.sh -dw deb -da amd64
   ```

   **AARCH64 / ARM64**
   ```console
   # ./wazuh-install.sh -dw deb -da arm64
   ```
3. Download the certificates configuration file.
   ```console
   # curl -sO https://packages.wazuh.com/4.14/config.yml
   ```
4. Edit `config.yml` to prepare the certificates creation.
   - If you are performing an all-in-one deployment, replace `"<indexer-node-ip>"`, `"<wazuh-manager-ip>"`, and `"<dashboard-node-ip>"` with `127.0.0.1`.
   - If you are performing a distributed deployment, replace the node names and IP values with the corresponding names and IP addresses. You need to do this for all the Wazuh server, Wazuh indexer, and Wazuh dashboard nodes. Add as many node fields as needed.
5. Run the `./wazuh-install.sh -g` command to create the certificates. For a multi-node cluster, these certificates need to be later deployed to all Wazuh instances in your cluster.
   ```console
   # ./wazuh-install.sh -g
   ```
6. Copy or move the following files to a directory on the host(s) from where the offline installation will be carried out. You can use `scp` for this.
   - `wazuh-install.sh`
   - `wazuh-offline.tar.gz`
   - `wazuh-install-files.tar`

## Next steps

Once the Wazuh files are ready and copied to the specified hosts, it is necessary to install the Wazuh components.

Please make sure that a copy of the `wazuh-install-files.tar` and `wazuh-offline.tar.gz` files, created during the initial configuration step, is placed in your working directory.

* [Install Wazuh components using the assisted method](installation-assistant.md)
* [Install Wazuh components step by step](step-by-step.md)
