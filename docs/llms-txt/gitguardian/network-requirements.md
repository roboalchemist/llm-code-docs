# Source: https://docs.gitguardian.com/self-hosting/network-requirements.md

# Network requirements

> Network requirements for GitGuardian self-hosted, including inbound/outbound rules, domain allowlists, and firewall configuration.

Depending on the installation method, you'll have some network requirements,
even for Airgap environments.

:::tip IPv6 support
GitGuardian self-hosted supports IPv4, IPv6, and dual-stack networking. For details, see [IPv6 networking](./management/infrastructure-management/ipv6-networking).
:::

## Services and components

GitGuardian uses different components for its functioning:

- **Nginx:** Web Server,
- **Celery:** queue and task manager,
- **Django:** framework used for the application,
- **PostgreSQL:** database,
- **Redis:** cache manager,
- **Replicated:** management console (KOTS admin and Replicated SDK).

![Services and components](/img/self-hosting/components_map.png)

After installing the GitGuardian application, you will see different pods
created on your Kubernetes cluster.

For detailed insights into deployment/pod names, types, and their usage, visit
the [GitGuardian Application Topology](./troubleshoot/topology) page.

## External access

Below domains to whitelist and ports to open are specific to the installation, upgrade, and usage of the application and its management.

Ensure the relevant rules are correctly applied to your firewall.

### Inbound rules

For you to communicate with GitGuardian application, certain inbound ports must be open.

| Protocol | Port | Source  | Destination   | Description                  |
| -------- | ---- | ------- | ------------- | ---------------------------- |
| TCP      | 443  | 0.0.0.0 | All K8S nodes | GitGuardian HTTPS entrypoint |
| TCP      | 8800 | 0.0.0.0 | All K8S nodes | KOTS Admin Console           |

> Note: The KOTS Admin Console is not applicable when using the Helm installation method.

The source is based on the customer's service access policy.
For example, the KOTS Admin Console might be limited to select internal IPs to prevent public access.

**We recommend dropping all incoming traffic except the ports listed above**.

### Outbound rules

For the GitGuardian application to communicate with external services, certain outbound ports must be open.

If you are using an HTTP proxy, you may also need to [configure your proxy](./management/infrastructure-management/proxy-server) to allow traffic to the following domains.

| Protocol | Port | Source        | Destination                      | Description                       |
| -------- | ---- | ------------- | -------------------------------- | --------------------------------- |
| TCP      | 443  | All K8S nodes | \*.replicated.com                | Replicated Registry and Proxy     |
| TCP      | 443  | All K8S nodes | replicated.app                   | Replicated API                    |
| TCP      | 443  | All K8S nodes | \*.docker.io                     | Docker hub Registry (auth & pull) |
| TCP      | 443  | All K8S nodes | production.cloudflare.docker.com | Docker hub Registry               |

> Note: The Docker hub registry is not applicable when using the Helm installation method.

#### Embedded cluster legacy (kURL) (instances installed in 2024 or before)

If you're using the Embedded installation method, there are some additional ports to open.

| Protocol | Port | Source        | Destination              | Description                      |
| -------- | ---- | ------------- | ------------------------ | -------------------------------- |
| TCP      | 443  | All K8S nodes | k8s.kurl.sh              | Replicated K8S kurl installer    |
| TCP      | 443  | All K8S nodes | s3.kurl.sh, kurl.sh      | Replicated kurl installer        |
| TCP      | 443  | All K8S nodes | kurl-sh.s3.amazonaws.com | Replicated kurl installer assets |

Replicated maintains a current list of IP addresses associated with these domains.

- For the range of IP addresses for `k8s.kurl.sh`, see [replicatedhq/ips](https://github.com/replicatedhq/ips/blob/main/ip_addresses.json#L34-L39) in GitHub.
- The range of IP addresses for `s3.kurl.sh` is the same as for the `kurl.sh` domain. For the range of IP addresses for `kurl.sh`, see [replicatedhq/ips](https://github.com/replicatedhq/ips/blob/main/ip_addresses.json#L28-L31) in GitHub.
- The kurl installer assets (tar.gz packages) are downloaded from Amazon S3 during installations with kURL. For information about dynamically scraping the IP ranges to allowlist for accessing these packages, see [AWS IP address ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#aws-ip-download) in the AWS documentation.

:::note
Depending on your integrations and settings, additional domains or IP ranges may need to be whitelisted and/or allowed in your HTTP proxy if you are using one.

Here is a list of features that will make outbound requests:

- [Honeytoken](../honeytoken/self-hosted#network-requirements)
- Secret validity checkers
- VCS Integrations (GitHub, GitHub Enterprise Server, GitLab, Bitbucket...)
- Messaging Integrations (Slack, Microsoft Teams...)
- Documentation Integrations (Confluence...)
- External notifiers (Slack, Jira...)
- Custom webhook notifier
- Email notifications (either SMTP or Sendgrid)

:::

## Nginx reverse proxy example for embedded installation

If you want to set up a reverse proxy in front of your embedded installation,
you need to configure and forward the SNI header properly.

Here is an example configuration for an Nginx virtual host.
`external_gitguardian_hostname` is the hostname to use in a browser to access
the dashboard, and `internal_gitguardian_hostname` is the hostname used to reach
the GitGuardian instance internally from the reverse proxy.
This is also the hostname set up in the KOTS Admin Console.

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name external_gitguardian_hostname;

    ssl_certificate           /path/to/fullchain.pem;
    ssl_certificate_key       /path/to/privkey.pem;

    set $target_host internal_gitguardian_hostname;

    location / {
      proxy_set_header        Host $target_host;
      proxy_set_header        X-Real-IP $remote_addr;
      proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header        X-Forwarded-Proto $scheme;

      proxy_pass          https://$target_host;
      proxy_read_timeout  60;
      proxy_ssl_name $target_host;
      proxy_ssl_server_name on;
      proxy_ssl_protocols TLSv1.2 TLSv1.3;
      proxy_ssl_session_reuse off;
    }
}
```

## Architecture examples

Here are some architecture examples that can help you install and configure your
GitGuardian environment.

### Internal network

![Internal network graph](/img/self-hosting/network_flows_internal_network.png)

If you have an internal network behind a firewall, you can easily connect to an
internal VCS (eg: self-hosted GitLab).

However, **if you want to connect to github.com, therefore requiring internet
access, you will need to open wide incoming access to the HTTPS port of your
GitGuardian instance**.

:::note
It is possible to restrict traffic to github.com IP addresses, but
[this is not recommended by GitHub](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/about-githubs-ip-addresses).
You can use a Web Application Firewall (WAF) or a proxy to monitor closely the
incoming traffic on the GitGuardian instance.
:::

In this scenario, the GitGuardian instance needs an open 443 egress port to get
updates.

### Internal network with DMZ

![DMZ network graph](/img/self-hosting/network_flows_dmz.png)

If in addition to an internal network, you have a DMZ and you want to integrate
with github.com, you can put **the GitGuardian instance in the DMZ**. This makes
it easier to access github.com but you will need to expose your internal VCS
outside of your internal network so that the GitGuardian instance can access it.

In this scenario, GitGuardian needs an open 443 egress port to get updates.

### Isolated network

GitGuardian offers a fully offline solution, ensuring that your data remains within your environment at all times.

![Isolated network graph](/img/self-hosting/network_flows_isolated_network.png)

In this scenario, **the GitGuardian instance is completely isolated from the
Internet**. It is offline and airgapped. This means no github.com monitoring is
possible. This also means you don't need an open 443 egress port to get updates.

For more details on installing GitGuardian in an airgap environment, refer to our [installation guide](./installation/airgap-installation-existing-cluster-helm).

:::info
This Airgap functionality is not available by default. Please contact your **[sales representative](mailto:support@gitguardian.com)** if you want to enable it.
:::
