# Source: https://docs.portainer.io/2.33-lts/faqs/troubleshooting/logs-errors-and-debugging/why-do-i-see-a-lot-of-tls-handshake-errors-in-my-portainer-and-or-agent-logs.md

# Source: https://docs.portainer.io/sts/faqs/troubleshooting/logs-errors-and-debugging/why-do-i-see-a-lot-of-tls-handshake-errors-in-my-portainer-and-or-agent-logs.md

# Source: https://docs.portainer.io/faqs/troubleshooting/logs-errors-and-debugging/why-do-i-see-a-lot-of-tls-handshake-errors-in-my-portainer-and-or-agent-logs.md

# Why do I see a lot of TLS handshake errors in my Portainer and/or Agent logs?

This can occur when either the Portainer Server or your Portainer Agents are exposed to the public internet, and are being subjected to port scanners.

We highly recommend restricting access to your Portainer deployments to only the IPs that are required for access by using a firewall or other ACL mechanism to limit access.
