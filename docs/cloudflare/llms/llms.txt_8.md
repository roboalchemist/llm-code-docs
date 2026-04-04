# Source: https://developers.cloudflare.com/load-balancing/llms.txt

# Load Balancing

Maximize application performance and availability

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/load-balancing/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Load Balancing llms-full.txt](https://developers.cloudflare.com/load-balancing/llms-full.txt) for the complete Load Balancing documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Load Balancing](https://developers.cloudflare.com/load-balancing/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/load-balancing/get-started/index.md)
- [Enable](https://developers.cloudflare.com/load-balancing/get-started/enable-load-balancing/index.md): Learn how to enable load balancing.
- [Learning path](https://developers.cloudflare.com/load-balancing/get-started/learning-path/index.md): This guide provides an in-depth walkthrough for how to plan for and set up a load balancer. For a quicker explanation, refer to the [quickstart](/load-balancing/get-started/quickstart/).
- [Quickstart](https://developers.cloudflare.com/load-balancing/get-started/quickstart/index.md)

## Load balancers

- [Load balancers](https://developers.cloudflare.com/load-balancing/load-balancers/index.md)
- [Common configurations](https://developers.cloudflare.com/load-balancing/load-balancers/common-configurations/index.md)
- [Manage load balancers](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/index.md): Learn how to set up and maintain load balancers.
- [DNS records](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/index.md)

## Pools

- [Pools](https://developers.cloudflare.com/load-balancing/pools/index.md)
- [Use Pages as an origin for Load Balancing](https://developers.cloudflare.com/load-balancing/pools/cloudflare-pages-origin/index.md): This tutorial is intended as an introductory example of how you can leverage Cloudflare's global traffic management.
- [Manage pools](https://developers.cloudflare.com/load-balancing/pools/create-pool/index.md): Learn how to set up and maintain pools.

## Monitors

- [Monitors](https://developers.cloudflare.com/load-balancing/monitors/index.md)
- [Manage monitors](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/index.md): Learn how to set up and maintain monitors for your load balancer.
- [Monitor Groups](https://developers.cloudflare.com/load-balancing/monitors/monitor-groups/index.md)

## Private Network Load Balancing

- [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/index.md): Use Private Network Load Balancing to load balance traffic between servers within a data center or between private applications, and eliminate the need for hardware appliances.
- [Set up Private Network Load Balancing with Cloudflare WAN](https://developers.cloudflare.com/load-balancing/private-network/cloudflare-wan/index.md)
- [Set up Private Network Load Balancing for Public traffic to Tunnel](https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/index.md)
- [Set up Private Network Load Balancing with Client-to-Tunnel](https://developers.cloudflare.com/load-balancing/private-network/warp-to-tunnel/index.md)

## Additional configuration

- [Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/index.md)
- [Additional DNS records](https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/index.md)
- [Cloudflare Tunnel (published applications)](https://developers.cloudflare.com/load-balancing/additional-options/cloudflare-tunnel/index.md)
- [DNS persistence](https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/index.md)
- [Load Balancing with the China Network](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/index.md)
- [Custom load balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/index.md)
- [Actions](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/index.md)
- [Create custom rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/index.md)
- [Expressions](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/index.md)
- [Supported fields and operators](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/index.md)
- [Load shedding](https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/index.md): Use load shedding to prevent an at-risk endpoint from becoming unhealthy and starting the failover process.
- [Override HTTP Host headers](https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/index.md)
- [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/index.md)
- [Perform planned maintenance](https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/index.md): When you change application settings or add new assets, you will likely want to make these changes on one endpoint at a time. Going endpoint by endpoint reduces the risk of changes and ensures a more consistent user experience.
- [Spectrum](https://developers.cloudflare.com/load-balancing/additional-options/spectrum/index.md)

## Reference architecture

- [Reference architecture](https://developers.cloudflare.com/load-balancing/reference-architecture-external-link/index.md)

## API reference

- [API reference](https://developers.cloudflare.com/load-balancing/api-reference/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/load-balancing/changelog/index.md)

## reference

- [Limitations](https://developers.cloudflare.com/load-balancing/reference/limitations/index.md)
- [Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/index.md): Use load balancing analytics to evaluate traffic flow, assess the health of endpoints, and review health changes over time.
- [Health monitor notifications](https://developers.cloudflare.com/load-balancing/reference/migration-guides/health-monitor-notifications/index.md)
- [Migrate to new GraphQL nodes](https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/index.md)
- [Regions API](https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/index.md)

## troubleshooting

- [Common error codes](https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/index.md)
- [FAQs](https://developers.cloudflare.com/load-balancing/troubleshooting/load-balancing-faq/index.md)

## understand-basics

- [Adaptive routing](https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/index.md)
- [How endpoints and pools become unhealthy](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/index.md)
- [Load Balancing components](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-components/index.md)
- [Proxy status](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/index.md)
- [Session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/index.md)
- [Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/index.md)
- [Hash](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/index.md)
- [Least Outstanding Requests](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/least-outstanding-requests-pools/index.md)
- [Random](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/random-origin-steering/index.md)
- [Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/index.md)
- [Dynamic](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/index.md)
- [Geo](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/index.md)
- [Least Outstanding Requests](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/index.md)
- [Proximity](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/index.md)
- [Standard](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/index.md)