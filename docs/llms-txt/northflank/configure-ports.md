# Source: https://northflank.com/docs/v1/application/network/configure-ports.md

# Configure ports

You can expose as many ports per deployment, public and private, as you require, and link each public port with a [subdomain](https://northflank.com/docs/v1/application/domains/link-a-domain-to-a-port).

You can add ports required by your application manually, or Northflank can automatically detect ports exposed by your Dockerfile.

Ports can be added while creating your deployment, or afterwards from the ports & DNS page on deployment and combined services. Updating ports on your deployments will not require a restart.

| Protocol | Uses | Can be made public? |
| --- | --- | --- |
| HTTP(S)/1.1 | Common web servers, websockets | Yes |
| HTTP(S)/2 | Modern web servers, [gRPC](https://grpc.io/), websockets | Yes |
| TCP | Common applications | No |
| UDP | Real-time communication, media and game servers, VoIP, DNS | No |

You can use any port from 1 to 65535 (ports for web servers are often 80, 443, 3000, 8000, and 8080).

![Configuring ports for a deployment service in the Northflank application](https://assets.northflank.com/documentation/v1/application/network/configure-ports/public-private-ports.png)

## Public ports

Public ports allow your application to receive and send traffic from clients on the internet. Only HTTP and HTTP/2 ports can be publicly exposed.

Public ports are automatically assigned a Northflank domain name, secured with an automatically-generated TLS certificate. They take the format:

`[port-name]--[service-name]--[random-string].code.run`

Public ports can be also linked to [your own subdomain](https://northflank.com/docs/v1/application/domains/link-a-domain-to-a-port).

Your application can be configured to listen on any port for HTTP/S traffic. Northflank will expose your HTTP ports publicly on ports 80 and 443 and route traffic to your configured port. HTTP (port 80) traffic will be automatically redirected to HTTPS (port 443).

For example:

| Application port | Port configuration on Northflank | Ports exposed by Northflank |
| --- | --- | --- |
| 80 | 80, HTTP, publicly exposed | 80, 443 |
| 3000 | 3000, HTTP, publicly exposed | 80, 443 |

## Private ports

You can create a private port for any protocol supported on Northflank.

Applications in your project will be able to access the private ports simply by referring to the service name and port in the following format:

`[service-name]:[port-number]`

Internal traffic in your project is managed with round-robin load-balancing between replicas.

You can forward private ports using the Northflank [CLI, API, or JavaScript client](https://northflank.com/docs/v1/api/forwarding).

If required, internal traffic between your containers can be encrypted with mTLS. Contact [[support@northflank.com](mailto:support@northflank.com)](mailto:support@northflank.com) to discuss your requirements.

## Detect ports

When you create a new deployment Northflank will scan the image manifest and attempt to identify and add the ports exposed by the image. You can also detect ports from the ports & DNS page on a service. You should always verify that the ports are correct for your deployment.

You can expose ports in your Dockerfile in the following ways:

```Dockerfile
# HTTP port (public by default)
EXPOSE 3000
# TCP port (private)
EXPOSE 2121/tcp
# UDP port (private)
EXPOSE 7171/udp
```

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Set IP policies: Allow or deny access to services based on IP addresses.](/v1/application/network/add-security-policies-for-ports#set-ip-policies)
- [Configure basic authentication: Require users to enter a username and password to access your site.](/v1/application/network/add-security-policies-for-ports#require-credentials)
