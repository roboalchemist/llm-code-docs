# Source: https://northflank.com/docs/v1/application/domains/use-path-based-routing.md

# Use path-based routing

You can configure subdomains to route ingress traffic to different services and ports based on the path. You can route paths on a subdomain to multiple ports on the same service, ports on different services, as well as services in different projects.

When you add a new subdomain it will have the base path (`/`) added by default. You can [link the subdomain to a service's port](link-a-domain-to-a-port) with no extra configuration required.

If you add multiple paths for a subdomain you may need to [set their priority](#configure-a-path) to ensure the correct routing is used.

> [!note] 
> [Click here](https://app.northflank.com/s/account/domains) to view your account domains page.

## Add a path

You can configure as many paths for a subdomain as you need.

> [!note] Requirements
> You will need the following to get started:

- a [verified subdomain](./add-a-domain-to-your-account#add-a-subdomain) added to your Northflank team

Navigate to your domains page and select  add path on the entry for the subdomain you want to add path routing to.

Click  add path in the paths section of your subdomain settings to add a new path.

Enter the URI as either plain text or regex and select the [routing mode](#routing-modes).

You can [further configure](#configure-a-path) the path by expanding advanced options. Advanced options can be edited after creating a path, but not the path URI or routing mode.

![Configuring paths for a subdomain in the Northflank application](https://assets.northflank.com/documentation/v1/application/domains/use-path-based-routing/edit-subdomain-paths.png)

## Routing modes

When you add a path you will need to select a routing mode to determine how Northflank should handle requests. You can enter a path as either plain text or as a regular expression. Paths take precedence based on their [priority](#configure-a-path).

### Exact

Will route requests only to the given path, and not any subpaths. For example, a path with the URI `/path` and the routing mode set to `exact` will route requests to `/path` to the assigned port, but not `/path/subpath`.

Requests to paths that include `/path` as a prefix will be routed to another path that matches, if any exists.

### Prefix

Will route any paths beginning with the given URI to the assigned port. For example `/path` and `/path/subpath` will route to the assigned port, but not `/acme/subpath`.

### RegEx

Will route paths that match the regex supplied as the URI. For example, `/path|/acme` will route requests to `/path` or `/acme` to the assigned port, but not `/path/subpath` or `/blog`.

You can configure more settings for each path in advanced options.

## Set path priority

Paths will be matched based on their priority in descending order. A higher priority means the path will overrule any other matching paths of lower priority. By default, the base path will be added with priority `0` and other paths with priority `1`.

For example, in the configuration below, any paths starting with `/api/v1/` will be routed according to the rules set for that path. Any requests to the path `/api` without the subpath `/v1` will be routed according to the configuration for `/api`, and all other requests will be routed according to `/`.

If, however, we changed the priority of `/` to `3`, all requests would be routed according to the rules for `/`, including requests to the paths `/api` and `/api/v1`.

| Path | Mode | Priority |
| --- | --- | --- |
| `/` | `prefix` | `0` |
| `/api` | `prefix` | `1` |
| `/api/v1/` | `prefix` | `2` |

## Ignore the URI case

By default, paths are case-sensitive. This means a request to the route `/API` will not match a path added as `/api` unless ignore URI case is selected.

This is not relevant if you add a path in RegEx mode which matches both cases.

## Set path timeout

You can configure a custom HTTP request timeout for each path. The timeout can be set in seconds (`s`) or milliseconds (`ms`), for example `250ms` or `1s`.

If the service does not respond before the timeout is reached a `408 Request Timeout` will be returned to the request origin.

## Rewrite a path

You can rewrite paths before the request is forwarded to the assigned port.

URI rewrite will replace the requested path with the new URI provided in the rewrite setting. For example, the rewrite `/api` for the prefix path `/api/v1` would rewrite a request to `/api/v1/health` as `/api/health`.

Regex rewrite can replace any specific parts of the path which matches the given regex. For example the regex `^/acme/([^/]+)(/.*)$` with rewrite `/api/\1/\2` would alter the path `/acme/v1/health` to `/api/v1/health`.

## Modify request headers

You can set and add HTTP headers for requests and responses to the path. You can also remove headers by key.

- Set will overwrite the headers specified by key with the given values

- Add will append the given values to the headers specified by key

- Remove will delete the specified headers by key

## Configure the CORS policy

You can configure the [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) policy for the path. You can enable the policy to apply it to any specified origins

### Allow origins

You can set the allowed origins for CORS requests by selecting the matching mode and specifying the origin. The matching modes are the same as [routing modes](#routing-modes) for paths.

You can include apex domains as the origin (for example prefix mode with `https://example.com`), wildcards (for example exact mode with `*`), or use RegEx to specify allowed domains and paths.

### Allow methods

You can specify what [methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) are allowed in the CORS request. Allowing credentials will allow cookies and credentials to be sent with the request. You cannot send credentials if the origin is a wildcard (`*`).

### Allow headers

You can specify what headers should be forwarded in the CORS request, otherwise only the default headers will be included.

### Max age

Specify how long the results of a preflight request can be cached.

## Create retry policies

You can configure retry policies for paths, including whether to allow retries, how many retries to allow, and the time to wait between attempts.

You can select the specific HTTP or GRPC responses to retry on.

## Assign a path to a port

You can assign which service and port a path will route to after it has been added to the subdomain.

### In the subdomain settings

Select a service from the dropdown menu, then select an existing port from the service. Update path and Northflank will begin routing requests for the path to the selected port. If the service has no ports, or the expected port is not listed, you can click the button  to view the service and update the ports.

### In a service

Open the ports & DNS page for a service and expand the custom domains and security rules for the port you want to use. Add custom domain and select the subdomain with the path you want to route to the port. Save the changes and Northflank will begin routing requests for the path to the selected port.

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Domain registrar guides: Follow walkthroughs to add and verify domains on Cloudflare, NS1, OVH, and Namecheap.](/v1/application/domains/domains-on-northflank#custom-domains-and-subdomains)
