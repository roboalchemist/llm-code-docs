# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/monitoring-docker.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Monitoring Docker events

Docker automates the deployment of different applications inside software containers. The Wazuh module for Docker identifies security incidents across containers and alerts in real-time. In this use case, you configure Wazuh to monitor Docker events on an Ubuntu endpoint hosting Docker containers.

See the [Monitoring container activity](../user-manual/capabilities/container-security/monitoring-docker.md) section of the documentation to learn more about monitoring Docker and the `docker-listener` module.

## Infrastructure

| Endpoint     | Description                                                     |
|--------------|-----------------------------------------------------------------|
| Ubuntu 22.04 | This is the Docker host where you create and delete containers. |

## Configuration

Perform the following steps to install Docker on the Ubuntu endpoint and configure Wazuh to monitor Docker events.

1. Install Python and pip:
   ```console
   # sudo apt install python3 python3-pip
   ```
2. Upgrade pip:
   ```console
   # pip3 install --upgrade pip
   ```
3. Install Docker and Python Docker Library:

   Python 3.8â3.10

   Python 3.11â3.12
   ```console
   $ curl -sSL https://get.docker.com/ | sh
   $ sudo pip3 install docker==7.1.0 urllib3==1.26.20 requests==2.32.2
   ```

   ```console
   $ curl -sSL https://get.docker.com/ | sh
   $ sudo pip3 install docker==7.1.0 urllib3==1.26.20 requests==2.32.2 --break-system-packages
   ```

   #### NOTE
   This command modifies the default externally managed Python environment. See the [PEP 668](https://peps.python.org/pep-0668/) description for more information.

   To prevent the modification, you can run `pip3 install --upgrade pip` within a virtual environment. You must update the docker `/var/ossec/wodles/docker/DockerListener` script shebang with your virtual environment interpreter. For example: `#!</path/to/your/virtual/environment>/bin/python3`.
4. Edit the Wazuh agent configuration file `/var/ossec/etc/ossec.conf` and add this block to enable the `docker-listener` module:
   ```xml
   <ossec_config>
     <wodle name="docker-listener">
       <interval>10m</interval>
       <attempts>5</attempts>
       <run_on_start>yes</run_on_start>
       <disabled>no</disabled>
     </wodle>
   </ossec_config>
   ```
5. Restart the Wazuh agent to apply the changes:
   ```console
   $ sudo systemctl restart wazuh-agent
   ```

## Test the configuration

Perform several Docker activities like pulling a Docker image, starting an instance, running some other Docker commands, and then deleting the container.

1. Pull an image, such as the NGINX image, and run a container:
   ```console
   $ sudo docker pull nginx
   $ sudo docker run -d -P --name nginx_container nginx
   $ sudo docker exec -it nginx_container cat /etc/passwd
   $ sudo docker exec -it nginx_container /bin/bash
   $ exit
   ```
2. Stop and remove the container:
   ```console
   $ sudo docker stop nginx_container
   $ sudo docker rm nginx_container
   ```

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, go to **Docker**.

> <a id="wazuh_image-0"></a>
> ![](images/poc/docker-alerts.png)

## Troubleshooting

- **Error log**:
  ```none
  wazuh-modulesd:docker-listener: ERROR: /usr/bin/env: âpythonâ: No such file or directory
  ```

  **Location**: Wazuh agent log - `/var/ossec/logs/ossec.log`

  **Resolution**: You can create a symbolic link to solve this:
  ```console
  $ sudo ln -s /usr/bin/python3 /usr/bin/python
  ```
