# Source: https://northflank.com/docs/v1/application/network/create-path-based-security-policies.md

# Create path-based security policies

You can configure security policies by path for each port on a service. Security policies consist of rules, which are a group of paths and a group of security policies. This allows you to use the same security policy for multiple paths, and create different security policies for different paths.

## Allow internal traffic to skip security policies

By default, all requests to the service's port using the [public endpoints](configure-ports#public-ports) will trigger the security policies. Only traffic using the [internal, private DNS](configure-ports#private-ports) will be able to access the service without passing the security policies.

You can allow your team's resources to skip the security policies for requests using a public DNS, which includes traffic from the same project or from resources in projects with ingress permissions from [multi-project networking](enable-multi-project-networking).

## Create a security policy

To configure security policies, expand the custom domains & security rules menu for a port and enable security policies. You can enable or disable all security policies for a port using this toggle.

### Create a rule

You can add rule to create a new rule, and enable or disable individual rules with their respective protected toggles. You can add multiple rules to a port. Each rule consists of one or more paths, and one or more security policies.

### Add a path

You must add at least one path to your rule. If you add multiple paths, the policies will apply to all matching paths in the rule. Paths consist of a URI (for example `/login`), the routing mode, and the priority.

#### Routing mode

- Exact will route only the specific path, and not subpaths

- Prefix will route the given path and all subpaths

- RegEx will route paths that match the given regular expression

#### Priority

Rules will match paths based on their priority in descending order. The rule with the highest priority that contains the matching path will override any other rules that match this path with a lower priority.

### Add a policy

You can add one or more security policies to a rule. This allows you to include, for example, IP allow lists as well as IP block lists, or combine an IP allow list with basic authentication.

You can add policies to an `AND` group or an `OR` group.

- `&& AND` requires users to pass all security policies in this group

- `|| OR` requires users to pass at least one security policies in this group

You can include policies from both groups. For example, you could add multiple credential policies in the `OR` group to allow for multiple basic auth username and password combinations, and an IP address policy and a HTTP header policy in the `AND` group. This would require users to match only one of the credential policies, but also the other security policies.

## Set IP policies

IP address policies allow you to either deny IP addresses from accessing a service, or to only allow certain IP addresses and exclude all others.

You can use this feature to, for example:

- Block the IP ranges of certain countries to meet legal requirements

- Block the IP addresses of malicious actors

- Allow only the IP addresses of your employees and clients

- Allow only the IP address for a required external service

You can enter specific IP addresses or use [CIDR blocks](https://www.ripe.net/about-us/press-centre/understanding-ip-addressing) to allow or deny ranges of IP addresses. For example, `192.168.0.0/24` would apply your policy to IP addresses in the range `192.168.0.0` - `192.168.0.255`.

Allowing an IP address, or a range of addresses, will block all other IP addresses.

Denying an IP address will always take precedence over allowing an IP address, so it isn't possible to deny a range of IP addresses and allow specific ones within that range. You can, however, allow a range of IP addresses and deny specific IP addresses within the range.

You can add multiple IP address policies using the `&& AND` group.

## Require credentials

The credentials policy includes methods to require a username/password combination before accessing the service.

### Basic authentication

Basic authentication is a simple method to prevent unwanted access to a website or endpoint. Users will need to enter a valid username and password in the browser prompt to access your service, or send an [authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) with their HTTP requests.

You can add multiple username and password combinations to the same rule by adding policies to the `|| OR` group.

## Allow based on HTTP header

You can allow access to a service based on [HTTP header](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header) content.

Northflank will check for the presence of a key/value pair in the header of a HTTP request, and allow or deny access based on whether it matches the key/value in the security policy. The value for the specified key can be evaluated against the exact string given, or as a regular expression.

This can be used to restrict access to requests based on a manually-set key/value pair, or by detecting a header like `Origin` to only allow requests from specified sources.

## Use SSO provider

You can require users to authenticate via your SSO provider before they can access your Northflank service.

> [!note] Requirements
> You will need the following to get started:

- A team that's part of an [organisation](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation)
- [Single sign-on](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation#configure-single-sign-on-sso) configured for your organisation
- [Directory sync](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation#sync-your-directory) enabled

Select your organisation's ID and choose the directory groups you want to grant access to.

You can enforce internal traffic through the SSO authentication flow, which means that requests made using [private networking](configure-ports#private-ports) will need to authenticate. This applies to other services, as well as any users using [port forwarding](https://northflank.com/docs/v1/api/forwarding) with the Northflank CLI. This cannot be enabled at the same time as [allowing internal traffic to skip security policies](#allow-internal-traffic-to-skip-security-policies).

You can also choose to set the authentication cookie on the root domain. This means that if you also require SSO authentication to access different subdomains or paths that the user only has to authenticate once.

Only one SSO authorisation can be added per `AND`/`OR` group.

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Domain registrar guides: Follow walkthroughs to add and verify domains on Cloudflare, NS1, OVH, and Namecheap.](/v1/application/domains/domains-on-northflank#custom-domains-and-subdomains)
