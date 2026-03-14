# Source: https://documentation.wazuh.com/current/migration-guide/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Backup guide

In this section you can find instructions on how to create and restore a backup of your Wazuh installation.

To do this backup, copy the key files to a designated folder while preserving file permissions, ownership, and directory structure. This ensures you can later restore your Wazuh data, certificates, and configurations by transferring the files back to their original locations. This method is particularly useful when migrating your Wazuh installation to a new system.

* [Creating a backup](creating/index.md)
  * [Wazuh central components](creating/wazuh-central-components.md)
  * [Wazuh agent](creating/wazuh-agent.md)
* [Restoring Wazuh from backup](restoring/index.md)
  * [Wazuh central components](restoring/wazuh-central-components.md)
  * [Wazuh agent](restoring/wazuh-agent.md)
