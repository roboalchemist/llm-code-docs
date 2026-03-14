# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/detect-brute-force-attack.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Detecting a brute-force attack

Brute-forcing is a common attack vector that threat actors use to gain unauthorized access to endpoints and services. Services like SSH on Linux endpoints and RDP on Windows endpoints are usually prone to brute-force attacks. Wazuh identifies brute-force attacks by correlating multiple authentication failure events.

The section on [Blocking attacks with Active Response](../user-manual/capabilities/active-response/ar-use-cases/blocking-ssh-brute-force.md) describes how to configure an active response to block the IP address of an attacker. In this use case, we show how Wazuh detects brute-force attacks on RHEL and Windows endpoints.

## Infrastructure

| Endpoint     | Description                                                                                                             |
|--------------|-------------------------------------------------------------------------------------------------------------------------|
| Ubuntu 22.04 | Attacker endpoint that performs brute-force attacks. Itâs required to have an SSH client installed on this endpoint.    |
| RHEL 9.0     | Victim endpoint of SSH brute-force attacks. Itâs required to have an SSH server installed and enabled on this endpoint. |
| Windows 11   | Victim endpoint of RDP brute-force attacks. Itâs required to enable RDP on this endpoint.                               |

## Configuration

Perform the following steps to configure the Ubuntu endpoint. This allows performing authentication failure attempts on the monitored RHEL and Windows endpoints.

1. On the attacker endpoint, install Hydra and use it to execute the brute-force attack:
   ```console
   $ sudo apt update
   $ sudo apt install -y hydra
   ```

## Attack emulation

1. Create a text file with 10 random passwords.
2. Run Hydra from the attacker endpoint to execute brute-force attacks against the  RHEL endpoint. To do this, replace `<RHEL_IP>` with the IP address of the RHEL endpoint and run the command below:
   ```console
   $ sudo hydra -l badguy -P <PASSWD_LIST.txt> <RHEL_IP> ssh
   ```
3. Run Hydra from the attacker endpoint to execute brute-force attacks against the  Windows endpoint. To do this, replace `<WINDOWS_IP>` with the IP address of the Windows endpoint and run the command below:
   ```console
   $ sudo hydra -l badguy -P <PASSWD_LIST.txt> rdp://<WINDOWS_IP>
   ```

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, go to the **Threat Hunting** module and add the filters in the search bar to query the alerts.

- Linux - `rule.id:(5551 OR 5712)`. Other related rules are `5710`, `5711`, `5716`, `5720`, `5503`, `5504`.

  <a id="wazuh_image-0"></a>
  ![](images/poc/brute-force-attack-alerts-ubuntu.png)
- Windows - `rule.id:(60122 OR 60204)`

  <a id="wazuh_image-1"></a>
  ![](images/poc/brute-force-attack-alerts-windows.png)
