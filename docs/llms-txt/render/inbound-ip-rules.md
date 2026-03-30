# Source: https://render.com/docs/inbound-ip-rules.md

# Inbound IP Rules — Allow incoming connections only from specified IP ranges.

You can configure which IP addresses can connect to your Render services over the public internet:

[image: Setting inbound IP rules in the Render Dashboard]

By setting these inbound IP rules, you can grant access only to IP ranges you trust.

*All workspaces* can set inbound IP rules for:

- Individual [Render Postgres](postgresql-creating-connecting#restricting-external-access) and [Key Value](key-value#enabling-external-connections) datastores

*Enterprise orgs* can also set rules for:

- Individual web services and static sites
- An entire [environment](projects)
- An entire workspace

After you set IP rules, Render only allows inbound service connections from the IP ranges you specify. Disallowed IPs are automatically blocked with a `403 Forbidden` response.

Requests are blocked at the edge and do not reach your service. For web services, blocked requests _do_ still appear in [HTTP request logs](logging#http-request-logs).

> *Inbound IP rules apply only to connections from the public internet.*
>
> These rules do not apply to inter-service communication over your [private network](private-network). For private network controls, see [Blocking cross-environment traffic](projects#blocking-cross-environment-traffic).

## Setup

### Render Postgres / Key Value

All workspaces can set inbound IP rules for Render Postgres and Key Value. See the documentation for each type of managed datastore:

- [Render Postgres](postgresql-creating-connecting#restricting-external-access)
- [Render Key Value](key-value#enabling-external-connections)

### All other resource types

> *Setting IP rules for any resource besides a [managed datastore](#render-postgres-key-value) requires an Enterprise org.*

Follow these steps to set inbound IP rules for a web service, static site, environment, or workspace.

1. In the [Render Dashboard](https://dashboard.render.com), open the settings page for the service or environment you want to configure.
   - For workspace-level rules, click *Network Access* in the left pane of your workspace home.
2. Scroll down to the *Networking* section and find *Inbound IP Restrictions*:

   [image: Editing inbound IP rules in the Render Dashboard]

   If you haven't made any changes yet, you'll see a single default rule: `0.0.0.0/0` (allow all IPs).

3. Click an existing rule to edit it, or click *+ Add source* to create a new rule. You can also click the trash icon next to a rule to delete it.

   - Learn more about [rule format](#rule-format) below.

> *If you delete all rules, Render blocks _all_ inbound traffic to the affected service(s)!*

4. Click *Save* to apply your changes.

You're all set! Your new rules take effect within a few seconds.

## Rule format

Inbound IP rules are allowlists of IP ranges you specify using [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation). Render allows connections from the IP ranges you specify and blocks connections from all other IPs.

> *Only IPv4 CIDR ranges are supported.*

Here are some example ranges:

| Rule | Meaning |
| --- | --- |
| `0.0.0.0/0` | Allow any IP address. This is the default rule for services besides [Render Key Value instances.](key-value#enabling-external-connections) |
| `203.0.113.0/24` | Allow IP addresses `203.0.113.0` through `203.0.113.255`. This might represent a company's office network or a trusted third-party service. |
| `198.51.100.16/29` | Allow IP addresses `198.51.100.16` through `198.51.100.23`. This smaller range of 8 addresses might represent a specific subnet of an office network. |
| `203.0.113.42/32` | Allow _only_ the IP address `203.0.113.42`. The `/32` suffix limits the rule to the single defined IP address. This is useful for allowing only your own development machine. |

## Combining IP rules

> *This section applies only to Enterprise orgs.*

When a service is subject to IP rules at multiple levels (workspace, environment, and/or service), an inbound IP must be allowed by _each level's_ rules to successfully connect:

<img src="../assets/images/docs/inbound-ip-combining.svg" width="650" alt="IP rules flowchart" />

If an IP is allowed at the service level but disallowed at the environment level (or vice versa), the connection is blocked.

When you view a service's inbound IP rules, you can see each level of rules that apply to it:

[image: Viewing all IP rules for a service]

## FAQ

###### Can I set IP rules for a private service / background worker / cron job?

No. These service types never receive traffic from the public internet.

###### How do I allow connections from all IP addresses?

Include the value `0.0.0.0/0` (CIDR notation for "any IPv4 address") in your inbound IP rules.

This is the default rule for services besides [Render Key Value instances.](key-value#enabling-external-connections)

###### What happens if I delete all rules for a given resource?

If you delete all inbound IP rules for a given service, environment, or workspace, Render blocks _all_ inbound traffic to the affected service(s).

###### Why don't I see inbound IP rule settings for my web service?

Inbound IP rules require an [Enterprise org](enterprise-orgs) for everything besides [managed datastores.](#render-postgres-key-value)
