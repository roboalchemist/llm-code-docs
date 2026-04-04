# Source: https://fly.io/docs/networking/egress-ips/

Title: Egress IP addresses

URL Source: https://fly.io/docs/networking/egress-ips/

Markdown Content:
[Docs](https://fly.io/docs/)[Networking](https://fly.io/docs/networking)Egress IP addresses![Image 1: Illustration by Annie Ruygt of two happy Machines sitting on clouds](https://fly.io/static/images/Egress-IP.png)
[](https://fly.io/docs/networking/egress-ips/#overview)Overview
---------------------------------------------------------------

*   By default, outbound (egress) IPs from Fly Machines are **unstable** and may change. 
*   You can allocate **static egress IPs** for an app (both IPv4 and IPv6) via `fly ips allocate-egress`. 
*   App-scoped static egress IPs are per-region: you need one for each region where you have machines. 
*   Static egress IPs come with trade-offs: they cost more, and limit how many machines you can run at once. 
*   Legacy machine-scoped static egress IPs are still available, but are no longer recommended due to their limitations and quirks. 

* * *

[](https://fly.io/docs/networking/egress-ips/#why-egress-ips-matter)Why Egress IPs Matter
-----------------------------------------------------------------------------------------

Some external services—APIs, databases, payment providers—require allowlisting source IPs. Without static egress IPs, outbound IPs from Fly machines may change due to machine lifecycle or infrastructure changes.

*   Machines often egress over IPv6 when the destination has an AAAA record and the application prefers it. For example, `curl` will try IPv6 first if available, then fall back to IPv4 if needed. Fly doesn’t force IPv6, but many apps will use it when it’s available. 
*   IPv4 traffic is NAT’d and may vary. This means the source IP address is rewritten by the host, and which IP you get can change depending on where the machine runs or is restarted. 
*   You need static egress if you’re allowlisting IPs with third-party services. 

* * *

[](https://fly.io/docs/networking/egress-ips/#static-egress-ips-app-scoped)Static Egress IPs (App-Scoped)
---------------------------------------------------------------------------------------------------------

App-scoped static egress IPs can be shared between multiple machines in a region belonging to the same app, and will not be deleted when machines are recreated. They are recommended over our legacy machine-scoped static egress IPs.

### [](https://fly.io/docs/networking/egress-ips/#allocate-an-app-scoped-static-egress-ip)Allocate an App-scoped Static Egress IP

```
fly ips allocate-egress --app <app-name> -r <region>
```

This allocates a pair of static egress addresses, IPv4 and IPv6, for your app in a region.

If your app has Machines in multiple regions, you must allocate at least 1 app-scoped static egress IP address **per region**. Machines can only use static egress IPs that were allocated in their own region.

You can allocate multiple pairs of IPv4 and IPv6 static egress addresses in the same region. Machines will randomly choose a pair from all static egress IPs available in the region.

### [](https://fly.io/docs/networking/egress-ips/#view-and-manage)View and Manage

```
fly ips list
fly ips release-egress <ip-address>
```

App-scoped egress IPs are only released when you explicitly run `fly ips release-egress`. They persist across Machine destruction and deployments.

### [](https://fly.io/docs/networking/egress-ips/#billing)Billing

Each app-scoped IPv4 static egress address costs $3.60/mo, billed hourly. IPv6 addresses are allocated alongside IPv4 and are not billed separately.

### [](https://fly.io/docs/networking/egress-ips/#caveats)Caveats

*   Each static egress IP can support up to 64 Machines. If you need more than 64 Machines in one region, you will need to allocate multiple static egress IPs. 
*   When using app-scoped static egress IPs, a Machine can make up to 1024 concurrent connections to _each_ destination IP address. There is no limit on the _total_ number of concurrent connections. 

We do not expect this to be a concern for most apps. However, feel free to talk to us if this limits your use case!

*   When you have multiple static egress IPs assigned in one region, there is currently no way to specify exactly which IP each machine will use. 
*   There may be delays when egress IPs are applied to Machines: 
*   Right after allocating a new egress IP, it will be applied to all existing Machines in the region after a short delay. Allocating multiple pairs of static egress IPs will not help in this case. 
*   When creating a new Machine in an app that already has an egress IP assigned, there may be a delay before the Machine can use the egress IP. This delay may be more noticeable with more Machines or during bluegreen deployments. Allocating multiple pairs of static egress IPs can help alleviate this issue. 
*   `flyctl` surfaces warnings when these limits are approached during Machine creation, deployments, and IP management. 

### [](https://fly.io/docs/networking/egress-ips/#interaction-with-machine-scoped-egress-ips)Interaction with Machine-Scoped Egress IPs

App-scoped and machine-scoped egress IPs are not intended to be used together.

If a Machine has a machine-scoped egress IP, it takes precedence over any app-scoped egress IP in the same region. This behavior may change in the future.

* * *

[](https://fly.io/docs/networking/egress-ips/#static-egress-ips-machine-scoped)Static Egress IPs (Machine-Scoped)
-----------------------------------------------------------------------------------------------------------------

Machine-scoped static egress IPs are considered a legacy feature and may be removed in the future. This section is kept for reference purposes only. New apps should use [app-scoped static egress IPs](https://fly.io/docs/networking/egress-ips/#static-egress-ips-app-scoped).

### [](https://fly.io/docs/networking/egress-ips/#allocate-a-static-egress-ip)Allocate a Static Egress IP

```
fly machine egress-ip allocate <machine-id> --app <app-name>
```

*   This assigns a stable IPv4 + IPv6 pair to the specified machine. 

### [](https://fly.io/docs/networking/egress-ips/#view-and-manage-2)View and Manage

```
fly machine egress-ip list --app <app-name>
fly machine egress-ip release <machine-id> --app <app-name>
```

### [](https://fly.io/docs/networking/egress-ips/#caveats-2)Caveats

Because legacy static egress IPs are **per-machine**, not per-app:

*   IPs are released when a machine is destroyed. 
*   IPs don’t automatically transfer across deploys. 
*   Bluegreen deployments will replace machines—and their IPs. 
*   Deployment-time jobs may bypass egress routing. 
*   Extra latency and connectivity issues are possible in some regions. 

Machine-scoped static egress IPs are billed per hour per machine.

* * *

[](https://fly.io/docs/networking/egress-ips/#the-proxy-pattern-for-machine-scoped-static-egress-ips)The Proxy Pattern (for Machine-Scoped Static Egress IPs)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

This section only applies to existing apps using machine-scoped static egress IPs. New apps should use [app-scoped static egress IPs](https://fly.io/docs/networking/egress-ips/#static-egress-ips-app-scoped) instead.

To avoid assigning static IPs to every machine, route traffic through a shared proxy app.

### [](https://fly.io/docs/networking/egress-ips/#how-it-works)How It Works

1.   Deploy a small Fly app (e.g. `egress-proxy`) with static egress IPs. 
2.   Run a forward HTTP/HTTPS proxy on it. 
3.   Set `http_proxy` / `https_proxy` env vars in consuming apps. 
4.   Outbound traffic from those apps will route through the proxy. 

### [](https://fly.io/docs/networking/egress-ips/#benefits)Benefits

*   Fewer IPs to manage. 
*   Primary app machines can be ephemeral. 
*   Centralize allowlisting. 

### [](https://fly.io/docs/networking/egress-ips/#downsides)Downsides

*   Primarily supports HTTP/S traffic. Other protocols (like raw TCP or Postgres) may be possible with extra work, such as using SOCKS5 proxies, `haproxy` in TCP mode, or `socat`, but those setups are more complex and outside the scope of this guide. 
*   Adds some latency (~100ms typical). 
*   Requires maintaining a separate proxy app. 

* * *

[](https://fly.io/docs/networking/egress-ips/#best-practices)Best Practices
---------------------------------------------------------------------------

*   Use static egress only when required. 
*   Test connectivity after assigning egress IPs. 
*   Monitor for failures during deploy-time migrations.
