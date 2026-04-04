# Source: https://electric-sql.com/use-cases/cloud-costs.md

---
url: /use-cases/cloud-costs.md
description: "Take the query workload off your database and the compute\_workload off\_your\_cloud."
---

## Radically reduce your cloud bill

Most software today is built on a 3-tier web-service architecture. Front-end apps talk to backend services to fetch data and run business logic.

This means business logic executes on the cloud, which leads to high volumes of requests and database queries. This costs money to serve, in the form of compute and database query costs. Plus querying data in the cloud leads to large egress costs.

## Sync-engine architecture

Sync-engine architecture replaces data fetching, querying and egress from the cloud with sync into a local data store, local queries and minimal egress.

This architecture changes the operational cost characteristics of your software:

* moving business logic onto the client device
* eliminating the request workload hitting the cloud
* minimising database query and egress costs
* avoiding SRE costs from high uptime

## How does Electric help?

Electric is a sync engine. You can use Electric to move to a sync engine architecture.

## Example

[Linear](https://linear.app), which is the world's most popular project management software, built their product on a sync-engine archicture. As a result, they've been able to run the whole of their European hosting on just two standard web servers. This has massively reduced their cloud bill.

## Next steps

Get in touch if you're interested in switching to a sync engine architecture to reduce your cloud costs.
