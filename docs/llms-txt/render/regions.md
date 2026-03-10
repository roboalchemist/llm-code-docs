# Source: https://render.com/docs/regions.md

# Regions — Deploy your apps and datastores close to your users.

You can deploy Render services to any of the following regions to minimize latency for your users:

- Oregon, USA
- Ohio, USA
- Virginia, USA
- Frankfurt, Germany
- Singapore

We'll continue to add regions over time. If you're interested in a particular region, vote for it at [feedback.render.com](https://feedback.render.com).

## Choosing a region

> You don't choose a region for [static sites](static-sites), which are backed by a global CDN.

You choose a region for your service or datastore during the creation flow in the [Render Dashboard](https://dashboard.render.com):

[image: Selecting a region for a service]

The dashboard indicates the regions where you already have services (if any). To deploy elsewhere, click *Deploy in a new region*.

## Changing a service's region

Render doesn't currently support changing the region for an existing service or database. Instead, create a new service or database in the desired region, then migrate your configuration and data as needed.

## Private networking

Each region provides a separate [private network](private-network) for your services. This means that services in _different_ regions can't communicate directly over a private network.

To communicate between services across regions, you need to properly secure that communication for traversal over the public internet.