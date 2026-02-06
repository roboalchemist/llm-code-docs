# Zenoh in action · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/overview/zenoh-in-action

# Source: https://zenoh.io/docs/overview/zenoh-in-action

# Zenoh in action
Let us now look into a sample scenario of Zenoh working.
Zenoh supports two paradigms of communication - publish-subscribe and queries.
- Pub/Sub in Zenoh
- Query in Zenoh

## Pub/Sub in Zenoh
This animation shows a basic pub/sub in action. The subscribers connected to the system receive the values sent by the publishers routed efficicently through the Zenoh network.
You can also observe the presence of a sleeping subscriber connected to the network. Once the subscriber awakes, the nearest Zenoh node will send the pending publications.

## Queries in Zenoh
This animation shows a simple query in action through Zenoh. You can see the presence of storages and queryables.
A queryable is any process that can reply to queries. A storage is a combination of a subscriber and a queryable.
In the following sections, we introduce the primitives and abstractions in Zenoh that enables this sample scenario.