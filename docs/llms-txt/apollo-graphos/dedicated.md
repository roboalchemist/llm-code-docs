# Source: https://www.apollographql.com/docs/graphos/routing/cloud/dedicated.md

# Cloud Dedicated Overview

Apollo is discontinuing Serverless and Dedicated plans, which use cloud routers. Serverless plans end on February 1, 2026, and serverless cloud routers are not available after February 15, 2026. Dedicated plans end on March 15, 2026, and dedicated cloud routers are not available after March 15, 2026.

If you're currently on a Serverless or Dedicated plan, migrate your graphs to use self-hosted routers. [See the migration guide](https://www.apollographql.com/docs/graphos/routing/cloud/migrate-to-self-hosted) for step-by-step instructions.

GraphOS *Cloud Dedicated* is the Apollo offering that lets you run a cloud router on dedicated, pre-provisioned infrastructure that you control and scale. It gives you access to a fully managed and monitored fleet of GraphOS Routers.

The Cloud Dedicated approach lets you implement and scale your supergraph without managing any additional infrastructure. Tailored for teams handling production-grade workloads, Cloud Dedicated offers additional control over performance and security.

Go the [Cloud Dedicated quickstart](https://www.apollographql.com/docs/graphos/routing/cloud/dedicated-quickstart) to get started.

## Runs on Amazon Web Services (AWS)

Cloud Dedicated runs a fleet of GraphOS Routers in the AWS region of your choice. The following regions are currently available:

* us-east-1
* us-east-2
* us-west-2
* ap-southeast-1
* ap-southeast-2
* ap-northeast-1
* ca-central-1
* eu-central-1
* eu-west-1
* eu-west-2
* eu-north-1

Dedicated supports subgraphs running in any cloud region or provider. However, you may incur additional networking charges for subgraphs running outside your selected AWS region. AWS VPC Lattice is only supported for the regions listed above.

## Pricing

Cloud Dedicated pricing is based on the amount of *Graph Compute Units* (GCUs) needed to run your graph. A GCU is a unit of throughput capacity. You can scale GCUs via [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content) or the [GraphOS Platform API](https://www.apollographql.com/docs/graphos/reference/platform-api/).

To learn about GCU performance and scaling, consult the [Throughput guide](https://www.apollographql.com/docs/graphos/routing/cloud/throughput-guide).

## Private preview

Cloud Dedicated is a new product and is in [preview](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages/#preview) while it matures. It is only available to select customers on an invite-only basis. If you have feedback or are interested in joining the preview, get in touch.

Please note the following while Cloud Dedicated is in preview:

* 99.9% SLA for ingress traffic
* Limited to customers running subgraphs in AWS
* Month-to-month billing, pricing subject to change
* Limited scaling, up to 10 GCUs per variant
