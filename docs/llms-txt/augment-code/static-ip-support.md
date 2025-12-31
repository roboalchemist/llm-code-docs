# Source: https://docs.augmentcode.com/setup-augment/static-ip-support.md

# Allow Augment traffic from static IPs

> Locate Augment static IP addresses and configure firewalls, allowlists, and network policies for Augment Agent and its integrations.

Augment routes all outbound integration and remote-agent traffic through region specific static IP addresses. Add these IPs to your firewalls and allowlists when you need predictable source addresses for compliance or access control.

## When static IP support helps

**You likely need static IPs when**

* Your GitHub organization enforces IP allowlists.
* Internal APIs, artifact registries, or databases sit behind IP restricted networks.
* Corporate firewalls require a known source IP before allowing outbound agent traffic.
* You are connecting Augment remote agents to private cloud or on-prem systems.
* Compliance policies mandate tracking specific egress addresses.

**You probably do not need static IPs when**

* Integrated services such as GitHub, Linear, Slack, and others are accessible without IP restrictions.
* You only use Augment with SaaS tools that do not enforce IP allowlists.
* Your network does not block traffic based on source IP.

## Get the IP addresses for your region

<Callout type="info">
  Always perform the lookup from a network that mirrors the environment enforcing the allowlist so you can detect DNS filtering or caching differences.
</Callout>

### US region

```bash  theme={null}
dig +short us-static.augmentcode.com
```

### EU region

```bash  theme={null}
dig +short eu-static.augmentcode.com
```

The DNS record returns the exact set of IP addresses Augment uses for outbound traffic in that region. Addresses are stable, and repeated lookups should return the same list. Rerun the lookup periodically or set up monitoring so you are alerted if Augment adds new addresses.

## Add the IPs to common services

### GitHub Enterprise with IP restrictions

1. Run the lookup for your region.
2. In GitHub, open **Settings** -> **Security** -> **IP allow list**.
3. Add each Augment IP address with a clear description such as `Augment Agent`.

### Private artifact registries

Add the IP addresses to the allowlist for the registry host. For example, with a private npm registry include the addresses in the service configuration before agents pull packages.

### Corporate firewalls

1. Allow inbound traffic to your services from the Augment IP addresses.
2. Note the rules in your change management system for auditing.
3. Monitor firewall logs for denied connections from Augment IPs.

### API gateways

```yaml  theme={null}
apiVersion: networking.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-augment
spec:
  rules:
  - from:
    - source:
        ipBlocks:
        - "203.0.113.10/32"  # Replace with the Augment IPs you looked up
        - "203.0.113.11/32"
```

### Databases with IP allowlists

```sql  theme={null}
-- PostgreSQL pg_hba.conf example
host    all    augment_user    203.0.113.10/32    md5
host    all    augment_user    203.0.113.11/32    md5
```

## Implementation checklist

* Use the DNS entry for the region where your Augment deployment runs (`us-static` or `eu-static`).
* Document which services rely on Augment IPs and who owns the configuration.
* Limit access to only the systems Augment needs, following least privilege.
* Review and confirm allowlist entries during regular security audits.
* Configure alerts for DNS changes or repeated blocked traffic from Augment IPs.

## Troubleshooting

**If integrations stop working**

1. Rerun `dig +short <region>-static.augmentcode.com` and confirm the addresses match your allowlists.
2. Review firewall or service logs for blocked requests from Augment IPs.
3. Update the allowlist if any addresses changed or were missed.

**If DNS queries fail**

```bash  theme={null}
nslookup us-static.augmentcode.com
dig us-static.augmentcode.com A
dig us-static.augmentcode.com +noall +answer
```

Ensure local DNS resolvers can reach the Augment records and that caching layers are not serving stale results.

## Need help?

Contact Augment Support with your region, the affected integrations, and relevant firewall or allowlist details so the team can help you validate the configuration.
