# Source: https://northflank.com/docs/v1/application/network/add-security-policies-for-ports.md

# Add security policies for ports

You can configure security policies for a service's port. Port security policies apply to all public DNS entries and paths assigned to the port.

To configure a port-wide security policy, expand the custom domains & security rules menu for a port and add a new IP policy, credentials, or select an organisation for SSO access control.

## Set IP policies

IP policies allow you to either block IP addresses from accessing a port, or to only allow certain IP addresses and exclude all others. You can use this feature to, for example:

- Block the IP ranges of certain countries to meet legal requirements

- Block the IP addresses of malicious actors

- Allow only the IP addresses of your employees or clients to help secure a website or data

- Allow only the IP address for a required external service

You can set IP policies for a specific port from the security rules section of the ports & DNS page of combined and deployment services.

![Configuring IP policies for a port for a deployment service in the Northflank application](https://assets.northflank.com/documentation/v1/application/network/set-ip-policies/ip-policy.png)

You can enter specific IP addresses or use [CIDR blocks](https://www.ripe.net/about-us/press-centre/understanding-ip-addressing) to allow or deny ranges of IP addresses. For example, `192.168.0.0/24` would apply your policy to IP addresses in the range `192.168.0.0` - `192.168.0.255`.

Allowing an IP address, or a range of addresses, will block all other IP addresses.

Denying an IP address will always take precedence over allowing an IP address, so it isn't possible to deny a range of IP addresses and allow specific ones within that range. You can, however, allow a range of IP addresses and deny specific IP addresses within the range.

You can apply rules to one or multiple ports, and apply different policies to different ports on the same service.

## Require credentials

Basic authentication is a simple method to prevent unwanted access to a website or endpoint. If you have added basic authentication to a port users will need to enter a valid username and password in the browser prompt to access your service, or send an [authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) with their HTTP requests.

You can add basic access authentication to a specific port from the security rules section of the ports & DNS page of deployment and combined services.

You can add multiple username and password combinations to the same port.

![Configuring basic authentication on a port for a deployment service in the Northflank application](https://assets.northflank.com/documentation/v1/application/network/configure-basic-authentication/basic-authentication.png)

## Use SSO provider

You can require users to authenticate via your SSO provider before they can access your Northflank service.

> [!note] Requirements
> You will need the following to get started:

- A team that's part of an [organisation](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation)
- [Single sign-on](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation#configure-single-sign-on-sso) configured for your organisation
- [Directory sync](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation#sync-your-directory) enabled

You can require SSO authentication for a port on a service by expanding the custom domains & security rules option.

Select your organisation's ID and choose the directory groups you want to be able to access the service via the port.

You can enforce internal traffic through the SSO authentication flow, which means that requests made using [private networking](configure-ports#private-ports) will need to authenticate. This applies to other services, as well as any users using [port forwarding](https://northflank.com/docs/v1/api/forwarding) with the Northflank CLI.

You can allow internal traffic to skip the SSO authentication flow for requests using a [public DNS](configure-ports#public-ports), which includes traffic from the same project or projects with ingress permissions from [multi-project networking](enable-multi-project-networking).

These enforce/allow options are mutually exclusive. The default behaviour allows private networking to skip authentication, but requires authentication for all traffic accessing the port via public endpoints.

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Domain registrar guides: Follow walkthroughs to add and verify domains on Cloudflare, NS1, OVH, and Namecheap.](/v1/application/domains/domains-on-northflank#custom-domains-and-subdomains)
