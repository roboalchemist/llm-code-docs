# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/poc-file-integrity-monitoring.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# File integrity monitoring

File Integrity Monitoring (FIM) helps in auditing sensitive files and meeting regulatory compliance requirements. Wazuh has an inbuilt [FIM](../user-manual/capabilities/file-integrity/index.md) module that monitors file system changes to detect the creation, modification, and deletion of files.

This use case uses the Wazuh FIM module to detect changes in monitored directories on Ubuntu and Windows endpoints. The Wazuh FIM module enriches alert data by fetching information about the user and process that made the changes using [who-data audit](../user-manual/capabilities/file-integrity/advanced-settings.md#who-data-monitoring).

## Infrastructure

| Endpoint     | Description                                                                                                |
|--------------|------------------------------------------------------------------------------------------------------------|
| Ubuntu 22.04 | The Wazuh FIM module monitors a directory on this endpoint to detect file creation, changes, and deletion. |
| Windows 11   | The Wazuh FIM module monitors a directory on this endpoint to detect file creation, changes, and deletion. |

## Configuration

### Ubuntu endpoint

Perform the following steps to configure the Wazuh agent to monitor filesystem changes in the `/root` directory.

1. Edit the Wazuh agent `/var/ossec/etc/ossec.conf` configuration file. Add the directories for monitoring within the `<syscheck>` block. For this use case, you configure Wazuh to monitor the `/root` directory. To get additional information about the user and process that made the changes, enable [who-data audit](../user-manual/capabilities/file-integrity/advanced-settings.md#who-data-monitoring-linux):
   ```xml
   <directories check_all="yes" report_changes="yes" realtime="yes">/root</directories>
   ```

   #### NOTE
   You can also configure any path of your choice in the `<directories>` block.
2. Restart the Wazuh agent to apply the configuration changes:
   ```console
   $ sudo systemctl restart wazuh-agent
   ```

### Windows endpoint

Take the following steps to configure the Wazuh agent to monitor filesystem changes in the `C:\Users\Administrator\Desktop` directory.

1. Edit the `C:\Program Files (x86)\ossec-agent\ossec.conf` configuration file on the monitored Windows endpoint. Add the directories for monitoring within the `<syscheck>` block. For this use case, you  configure Wazuh to monitor the `C:\Users\Administrator\Desktop` directory. To get additional information about the user and process that made the changes, enable [who-data audit](../user-manual/capabilities/file-integrity/advanced-settings.md#who-data-monitoring-windows):
   ```xml
   <directories check_all="yes" report_changes="yes" realtime="yes">C:\Users\<USER_NAME>\Desktop</directories>
   ```

   #### NOTE
   You can also configure any path of your choice in the `<directories>` block.
2. Restart the Wazuh agent using Powershell with administrator privileges to apply the changes:
   ```powershell
   > Restart-Service -Name wazuh
   ```

As an alternative to local configurations on the Wazuh agents, you can [centrally configure groups of agents](../user-manual/reference/centralized-configuration.md).

## Test the configuration

1. Create a text file in the monitored directory then wait for 5 seconds.
2. Add content to the text file and save it. Wait for 5 seconds.
3. Delete the text file from the monitored directory.

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, go to the **File Integrity Monitoring** module and add the filters in the search bar to query the alerts:

- Ubuntu - `rule.id: is one of 550,553,554`

  <a id="wazuh_image-0"></a>
  ![](images/poc/fim-alerts-ubuntu.png)
- Windows - `rule.id: is one of 550,553,554`

  <a id="wazuh_image-1"></a>
  ![](images/poc/fim-alerts-windows.png)
