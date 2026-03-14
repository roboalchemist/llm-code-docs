# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/detect-web-attack-sql-injection.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Detecting an SQL injection attack

You can use Wazuh to detect SQL injection attacks from web server logs that contain patterns like `select`, `union`, and other common SQL injection patterns.

SQL injection is an attack in which a threat actor inserts malicious code into strings transmitted to a database server for parsing and execution. A successful SQL injection attack gives unauthorized access to confidential information contained in the database.

In this use case, you simulate an SQL injection attack against an Ubuntu endpoint and detect it with Wazuh.

## Infrastructure

| Endpoint     | Description                                               |
|--------------|-----------------------------------------------------------|
| Ubuntu 22.04 | Victim endpoint running an Apache 2.4.54 web server.      |
| RHEL 9.0     | Attacker endpoint that launches the SQL injection attack. |

## Configuration

### Ubuntu endpoint

Perform the following steps to install Apache and configure the Wazuh agent to monitor the Apache logs.

1. Update the local packages and install the Apache web server:
   ```console
   $ sudo apt update
   $ sudo apt install apache2
   ```
2. If the firewall is enabled, modify it to allow external access to web ports. Skip this step if the firewall is disabled.
   ```console
   $ sudo ufw app list
   $ sudo ufw allow 'Apache'
   $ sudo ufw status
   ```
3. Check the status of the Apache service to verify that the web server is running:
   ```console
   $ sudo systemctl status apache2
   ```
4. Use the `curl` command or open `http://<UBUNTU_IP>` in a browser to view the Apache landing page and verify the installation:
   ```console
   $ curl http://<UBUNTU_IP>
   ```
5. Add the following lines to the Wazuh agent `/var/ossec/etc/ossec.conf` file. This allows the Wazuh agent to monitor the access logs of your Apache server:
   ```xml
   <ossec_config>
     <localfile>
       <log_format>apache</log_format>
       <location>/var/log/apache2/access.log</location>
     </localfile>
   </ossec_config>
   ```
6. Restart the Wazuh agent to apply the configuration changes:
   ```console
   $ sudo systemctl restart wazuh-agent
   ```

## Attack emulation

Replace `<UBUNTU_IP>` with the appropriate IP address and execute the following command from the attacker endpoint:

```console
$ curl -XGET "http://<UBUNTU_IP>/users/?id=SELECT+*+FROM+users";
```

The expected result here is an alert with rule ID 31103 but a successful SQL injection attempt generates an alert with rule ID 31106.

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, go to the Threat Hunting module and add the filters in the search bar to query the alerts.

- `rule.id:31103`

  <a id="wazuh_image-0"></a>
  ![](images/poc/SQL-injection-rule-31103.png)
- `rule.id:31106`

  <a id="wazuh_image-1"></a>
  ![](images/poc/SQL-injection-rule-31106.png)
