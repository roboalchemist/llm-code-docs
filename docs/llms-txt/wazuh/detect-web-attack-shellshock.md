# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/detect-web-attack-shellshock.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Detecting a Shellshock attack

Wazuh is capable of detecting a Shellshock attack by analyzing web server logs collected from a monitored endpoint. In this use case, you set up an Apache web server on the Ubuntu endpoint and simulate a shellshock attack.

## Infrastructure

| Endpoint     | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| Ubuntu 22.04 | Victim endpoint running an Apache 2.4.54 web server.                              |
| RHEL 9.0     | This attacker endpoint sends a malicious HTTP request to the victimâs web server. |

## Configuration

### Ubuntu endpoint

Perform the following steps to install an Apache web server and monitor its logs with the Wazuh agent.

1. Update local packages and install the Apache web server:
   ```console
   $ sudo apt update
   $ sudo apt install apache2
   ```
2. If a firewall is enabled, modify it to allow external access to web ports. Skip this step if the firewall is disabled:
   ```console
   $ sudo ufw app list
   $ sudo ufw allow 'Apache'
   $ sudo ufw status
   ```
3. Check that the Apache web server is running:
   ```console
   $ sudo systemctl status apache2
   ```
4. Add the following lines to the Wazuh agent `/var/ossec/etc/ossec.conf` configuration file. This sets the Wazuh agent to monitor the access logs of your Apache server:
   ```xml
   <localfile>
       <log_format>syslog</log_format>
       <location>/var/log/apache2/access.log</location>
   </localfile>
   ```
5. Restart the Wazuh agent to apply the configuration changes:
   ```console
   $ sudo systemctl restart wazuh-agent
   ```

## Attack emulation

1. Replace `<WEBSERVER_IP_ADDRESS>` with the Ubuntu IP address and execute the following command from the attacker endpoint:
   ```console
   $ sudo curl -H "User-Agent: () { :; }; /bin/cat /etc/passwd" <WEBSERVER_IP_ADDRESS>
   ```

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, go to the **Threat Hunting** module and add the filters in the search bar to query the alerts.

- `rule.description:Shellshock attack detected`
- If you have Suricata monitoring the endpoint traffic, you can also query `rule.description:*CVE-2014-6271*` for the related Suricata alerts.

  <a id="wazuh_image-0"></a>
  ![](images/poc/shellshock-alerts.png)
