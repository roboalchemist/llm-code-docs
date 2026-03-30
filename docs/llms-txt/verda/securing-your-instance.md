# Source: https://docs.verda.com/cpu-and-gpu-instances/securing-your-instance.md

# Securing Your Instance

Depending on your setup, adding basic security to your GPU instance can be an important first step.

We will install and configure `fail2ban` & `ufw`. This guide assumes you are logged in as a non-root user. If logged in as root, you do not need to prepend the commands with `sudo`.

```bash
sudo apt update
sudo apt install fail2ban
sudo systemctl start fail2ban
sudo systemctl enable fail2ban
sudo apt install ufw
sudo ufw allow ssh
sudo ufw enable
```

* Fail2ban will block IP addresses that continuously attempt to connect to your machine in the hopes of finding a weak password, for example.
* Ufw is a firewall management tool that will block access to all ports unless otherwise specified.

{% hint style="warning" %}
`ufw` with default settings [will not block traffic to Docker](https://docs.docker.com/network/packet-filtering-firewalls/#docker-and-ufw). In case you plan to run Docker containers on your instance, please make sure to configure your firewall rules appropriately.
{% endhint %}

That's all! Your VPS is now equipped with a firewall and basic protection against automated machines trying to break in. Check your firewall status and fail2ban status with respective commands:

```bash
sudo ufw status
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

You might be surprised how many bad actors are trying to obtain access to your server!

## Connecting to JupyterLab securely

If you want to run a service like Jupyter Notebook, you will need to forward a port from your local computer over the SSH for that. The default port for Jupyter Notebook is `8888`

To have the port forward, please add the forwarding options to the SSH command:

```bash
ssh -L 8888:localhost:8888 root@IP_OF_YOUR_INSTANCE
```
