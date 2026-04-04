# Network configuration and endpoints

Source: https://docs.sandboxes.cloud/docs/network-setup.md

This page talks about how to let components in the sandbox communicate with each other and how to access services running in the sandbox from outside via `endpoints`, specifically:

* [How services communicate with each other within sandbox](#how-services-communicate-with-each-other-within-sandbox)
  * [Direct access via hostname and port](#direct-access-via-hostname-and-port)
  * [Hostname Aliases](#hostname-aliases)
  * [Via in-sandbox port-forwarding (from workspace only)](#via-in-sandbox-port-forwarding-from-workspace-only)
* [How to expose services running in the sandbox for external access](#how-to-expose-services-running-in-the-sandbox-for-external-access)
  * [Setup endpoints](#setup-endpoints)
  * [From local via SSH tunneling or port-forwarding](#from-local-via-ssh-tunneling-or-port-forwarding)
* [Extend DNS Resolver](#extend-dns-resolver)

## How services communicate with each other within sandbox

As mentioned before, in each Crafting sandbox, there is an overlay network Crafting sets up for services to communicate with each other. There are multiple ways for one service to reach another within a sandbox.

### Direct access via hostname and port

The `workspaces`, `dependencies`, and `containers` can address each other by their `names` as the network `hostname`, and use the `ports` they define in the configuration.

<Image align="center" className="border" border={true} src="https://files.readme.io/07ed40b-image.png" />

For example, in the workspace defined above, other service can reach it by `spring:8080` using HTTP protocol. For all the built-in dependencies, they open the default ports, and details can be found at [https://sandboxes.cloud/dependencies](https://sandboxes.cloud/dependencies)

Note that the port defined in  `workspaces`, `dependencies`, and `containers` will NOT be directly exposed to Internet for security reasons, so you can't access them directly from your local machine. See [below](#how-to-expose-services-running-in-the-sandbox-for-external-access) for how to access that.

#### Hostname Aliases

A workload (a `workspace`, `dependency` or `container`) can be assigned extra hostnames as aliases in addition to its name, for example:

```yaml YAML
workspaces:
- name: work
  hostnames:
  - work.local
  - api-work
dependencies:
- name: mysql
  service_type: mysql
  hostnames:
  - db
containers:
- name: logger
  image: ...
  hostnames:
  - log-service
  - logd
```

In this example, the workspace `work` can also be accessed via hostnames `work.local` or `api-work` etc. Same for dependencies and containers. Note: the same hostname alias can't be assigned to more than one workloads.

#### Via in-sandbox port-forwarding (from workspace only)

Based on our practice for local development, sometimes we configure our services in dev mode to hit a port on localhost for reaching a dependency, e.g. hitting `localhost:6379` to reach the `redis` local server. Crafting makes it easy to replicate the same practice by allowing workspace port forwarding.

<Image align="center" className="border" border={true} src="https://files.readme.io/b73753f-image.png" />

For example, as shown above, the this workspace sets up two port forwardings for port 3306 and port 6379, to `mysql` and `redis`, respectively. That way, the service running on the workspace can just hit `localhost:3306`, which will be equivalent as hitting `mysql:3306`.

Setting up port forwardings on a workspace is also helpful for hybrid development by providing information on outbound connections. See [Port-forwarding for hybrid development](https://docs.sandboxes.cloud/docs/port-forwarding) for details.

### How to expose services running in the sandbox for external access

For security reasons, the port defined in  `workspaces`, `dependencies`, and `containers` will NOT be directly exposed to Internet. To access the services running in the sandbox from external, e.g. local laptop, there are following ways.

#### Setup endpoints

We can define `endpoints` in the sandbox to manage access from external. Each endpoint is corresponding to an external facing URL, which can be addressed from Internet. To add an endpoint, from the editing view of a [Standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox), click `Add Component` as shown below and choose `endpoints`.

<Image align="center" className="border" border={true} src="https://files.readme.io/581ee14-image.png" />

An endpoint can map traffic hitting the external URL to internal ports by a set of pre-defined rules. From web console, we can define a direct mapping for a TCP endpoint or a set of  routing rules for an HTTP endpoint.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/c6b6d92-image.png" />

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/71e2e47-image.png" />

In the above examples, the Internet facing URL `tcp://mysql--mysandbox-myorg.sandboxes.run:443` goes to the `mysql` service's default port (3306), and `https://app--mysandbox-myorg.sandboxes.run/` goes to the `frontend` service's `app` port (defined as 3000).

For security reasons, all `endpoints` exposed by Crafting sandbox need to have TLS layer, e.g. https for HTTP protocol and tcp+tls for TCP protocol.

As shown above, for HTTP endpoints, we can add authentication to make sure only users in the same organization can access the endpoint. For APIs, sometimes it might be unnecessary if the API itself has an app level authentication mechanism already there.

An HTTP endpoint can support routing different paths to different backend services, (i.e., `workspaces`, `containers`, `dependencies`). It also supports more advanced routing rules. Please see [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition#endpoints) for details.

#### From local via SSH tunneling or port-forwarding

There are other special ways to access services in the sandbox, which is using CLI `cs`. Using the same mechanism of how `cs ssh` works. We can set up SSH tunnel from a local machine.

In addition, after `cs portforward`, the local port on the local machine, e.g. `localhost:6379` will be mapped to the target port defined in the workspace's `port forwardings`, you can use your debugging tools to easily access the in-sandbox service that way from your local machine. See [Port-forwarding for hybrid development](https://docs.sandboxes.cloud/docs/port-forwarding).

We recommend define `endpoints` properly as shown above, which supports generic use cases such as mobile testing, end-to-end testing, and demoing.

### Extend DNS Resolver

Specifically, inside a workspace, the DNS resolver can be extended to resolve explicitly specified hosts entries, and/or hook up a second-level DNS resolver.

#### Static Hosts Entries

The built-in DNS resolver is aware of hosts files from the following locations:

* `/etc/hosts`
* `/etc/sandbox.d/dns/*.hosts`

All these files follow the same format as `/etc/hosts`, and only IPv4 is supported (all IPv6 entries are discarded).

#### Chained DNS Resolver

To hook up a chained, second-level DNS resolver, add a config file (must have suffix `.conf`) in `/etc/sandbox.d/dns` with content like:

```json
{"domains":[".foo.com.", ".foo.org."],"servers":["10.2.3.4:53"]}
{"domains":[".bar"],"servers":["10.7.8.9:53"]}
```

There are a few requirements about the content:

* Each line must be a single complete JSON document (the content is invalid if a JSON expands multiple lines);
* Each domain must have prefixing and trailing dots.

Note: it's possible to specify a domain like `"."` for using a second-level resolver to resolve all unresolved names, however it may introduce latency or instability in the case when the second-level resolver fails.
