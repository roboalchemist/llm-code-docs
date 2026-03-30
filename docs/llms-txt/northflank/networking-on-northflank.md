# Source: https://northflank.com/docs/v1/application/network/networking-on-northflank.md

# Networking on Northflank

Northflank allows flexible and secure private and public networking for services, jobs, databases and other addons. HTTP, HTTP/2, Websockets, gRPC, TCP and UDP are all supported networking protocols.

Networking settings are accessed on the ports & DNS page on deployment and combined services, and on the settings page in the network section for databases and other addons.

## Public networking

HTTP, HTTP/2, Websockets and gRPC can be exposed publicly via a load-balancer served with an auto-generated TLS certificate with either `code.run` endpoints or your own domains. HTTPS requests are terminated at the edge load-balancer and the request is then routed internally via Northflank’s network.

You can choose to [publicly expose databases](https://northflank.com/docs/v1/application/databases-and-persistence/access-a-database#expose-a-database-publicly) and other addons via a load-balanced TCP endpoint. Northflank will enforce and generate TLS certificates which will be automatically configured in the database and connection details.

Northflank will expose your HTTP ports publicly on ports 80 and 443 and route traffic to your configured ports. HTTP (port 80) traffic is automatically redirected to HTTPS (port 443).

- [Expose ports in your application: Expose ports in your application to make it available for networking.](/v1/application/network/expose-your-application)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Domains on Northflank: Manage your domains on Northflank, quickly and easily assigning them to your deployments.](/v1/application/domains/domains-on-northflank)
- [Expose a database with TLS: Secure internal database connections or expose it publicly with TLS.](/v1/application/databases-and-persistence/access-a-database)

## Network security

You can configure security policies for individual ports, with allow/deny lists based on IP address, basic auth for endpoints, and SSO for organisations. You can also create granular security policies by subdomain path, for even greater control.

- [Set IP policies: Allow or deny access to services based on IP addresses.](/v1/application/network/add-security-policies-for-ports#set-ip-policies)
- [Configure basic authentication: Require users to enter a username and password to access your site.](/v1/application/network/add-security-policies-for-ports#require-credentials)
- [Use SSO access control: Use your organisation's SSO provider to authenticate access to your services.](/v1/application/network/add-security-policies-for-ports#use-sso-provider)
- [Configure security policies by path: Set security policies to restrict access to your endpoints based on port and subdomain path.](/v1/application/network/create-path-based-security-policies)

## Private networking

Ports serving all protocols can be configured for private networking. Services, jobs and databases with private ports will only be accessible by other resources inside the same project.

Deployments and databases can be forwarded for secure, local access, without the need to publicly expose them to the internet.

You can enable multi-project networking to securely access resources from another Northflank project, and enable Tailscale in your projects to access resources in your Tailscale VPN.

- [Add private ports: Configure ports to allow your services to communicate securely within your project.](/v1/application/network/configure-ports#private-ports)
- [Forward deployments and databases: Forward deployments and databases to your local machine for development.](/v1/api/forwarding)
- [Multi-project networking: Configure projects to securely allow ingress network traffic from other projects.](/v1/application/network/enable-multi-project-networking)
- [Use Tailscale: Allow secure access to Tailscale devices to resources within your project.](/v1/application/network/use-tailscale)

## Load-balancing strategies

Northflank uses scalable and highly performant load balancers to securely distribute external traffic to services in your projects.

When you create a service you can select the load-balancing strategy to use, the default selects the instance with the least current traffic.

- [Select a load-balancing strategy: Choose the load-balancing strategy for your services.](/v1/application/network/load-balancing)

## Headers

You can access the source IP of a request from the [X-Forwarded-For header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For), which is attached to all HTTP/S requests by the Northflank load balancer.

Request and response headers can also be managed by configuring path-based routing for your subdomains.

- [Use path-based routing: Route incoming traffic to different services and ports for paths on a subdomain.](/v1/application/domains/use-path-based-routing)
