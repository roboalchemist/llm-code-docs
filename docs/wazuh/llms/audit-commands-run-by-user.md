# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/audit-commands-run-by-user.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Monitoring execution of malicious commands

Auditd is an auditing utility native to Linux systems. Itâs used for accounting actions and changes in a Linux endpoint.

In this use case, you configure Auditd on an Ubuntu endpoint to account for all commands executed by a given user. This includes commands run by a user in `sudo` mode or after changing to the root user. You configure a custom Wazuh rule to alert for suspicious commands.

Consider reading the [Monitoring system calls](../user-manual/capabilities/system-calls-monitoring/index.md) section to get a broader picture of the ways to take advantage of it.

## Infrastructure

| Endpoint     | Description                                                                                                                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ubuntu 22.04 | On this endpoint, you configure Auditd to monitor the execution of malicious commands. Then, make use of the Wazuh CDB list lookup capability to create a list of potential malicious commands that can be run on it. |

## Configuration

### Ubuntu endpoint

Perform the following steps to install Auditd and create the necessary audit rules to query all commands run by a privileged user.

1. Install, start and enable Auditd if itâs not present on the endpoint:
   ```console
   $ sudo apt -y install auditd
   $ sudo systemctl start auditd
   $ sudo systemctl enable auditd
   ```
2. As the root user, execute the following commands to append audit rules to `/etc/audit/audit.rules` file:
   ```console
   # echo "-a exit,always -F auid=1000 -F egid!=994 -F auid!=-1 -F arch=b32 -S execve -k audit-wazuh-c" >> /etc/audit/audit.rules
   # echo "-a exit,always -F auid=1000 -F egid!=994 -F auid!=-1 -F arch=b64 -S execve -k audit-wazuh-c" >> /etc/audit/audit.rules
   ```
3. Reload the rules and confirm that they are in place:
   ```console
   # sudo auditctl -R /etc/audit/audit.rules
   # sudo auditctl -l
   ```

   ```none
   -a always,exit -F arch=b32 -S execve -F auid=1000 -F egid!=994 -F auid!=-1 -F key=audit-wazuh-c
   -a always,exit -F arch=b64 -S execve -F auid=1000 -F egid!=994 -F auid!=-1 -F key=audit-wazuh-c
   ```
4. Add the following configuration to the Wazuh agent `/var/ossec/etc/ossec.conf` file. This allows the Wazuh agent to read the auditd logs file:
   ```xml
   <localfile>
     <log_format>audit</log_format>
     <location>/var/log/audit/audit.log</location>
   </localfile>
   ```
5. Restart the Wazuh agent:
   ```console
   $ sudo systemctl restart wazuh-agent
   ```

### Wazuh server

Perform the following steps to create a CDB list of malicious programs and rules to detect the execution of the programs in the list.

1. Look over the key-value pairs in the lookup file `/var/ossec/etc/lists/audit-keys`.
   ```none
   audit-wazuh-w:write
   audit-wazuh-r:read
   audit-wazuh-a:attribute
   audit-wazuh-x:execute
   audit-wazuh-c:command
   ```

   This CDB list contains keys and values separated by colons.

   #### NOTE
   Wazuh allows you to maintain flat file CDB lists which must be `key` only or `key:value` pairs. These are compiled into a special binary format to facilitate high-performance lookups in Wazuh rules. Such lists must be created as files, added to the Wazuh configuration, and then compiled. After that, rules can be built to look up decoded fields in those CDB lists as part of their match criteria. For example, in addition to the text file `/var/ossec/etc/lists/audit-keys`, there is also a binary `/var/ossec/etc/lists/audit-keys.cdb` file that Wazuh uses for actual lookups.
2. Create a CDB list `/var/ossec/etc/lists/suspicious-programs` and fill its content with the following:
   ```none
   ncat:yellow
   nc:red
   tcpdump:orange
   ```
3. Add the list  to the `<ruleset>` section of the Wazuh server `/var/ossec/etc/ossec.conf` file:
   ```xml
   <list>etc/lists/suspicious-programs</list>
   ```
4. Create a high severity rule to fire when a "red" program is executed. Add this new rule to the `/var/ossec/etc/rules/local_rules.xml` file on the Wazuh server.
   ```xml
   <group name="audit">
     <rule id="100210" level="12">
         <if_sid>80792</if_sid>
     <list field="audit.command" lookup="match_key_value" check_value="red">etc/lists/suspicious-programs</list>
       <description>Audit: Highly Suspicious Command executed: $(audit.exe)</description>
         <group>audit_command,</group>
     </rule>
   </group>
   ```
5. Restart the Wazuh manager:
   ```console
   $ sudo systemctl restart wazuh-manager
   ```

## Attack emulation

1. On the Ubuntu endpoint, install and run a "**red**" program `netcat`:
   ```console
   $ sudo apt -y install netcat
   # nc -v
   ```

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, go to the **Threat Hunting** module and add the filters in the search bar to query the alerts.

- `data.audit.command:nc`

  <a id="wazuh_image-0"></a>
  ![](images/poc/audit-commands-alerts.png)
