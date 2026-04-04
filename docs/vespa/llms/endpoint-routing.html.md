# Source: https://docs.vespa.ai/en/operations/endpoint-routing.html.md

# Routing and endpoints

 

Vespa Cloud supports multiple methods of routing requests to an application. This guide describes how these routing methods work, failover, and how to configure them.

By default, each deployment of a Vespa Cloud application will have a zone endpoint. In addition to the default zone endpoint, one can configure global endpoints.

All endpoints for an application are available under the _endpoints_ tab of each deployment in the console.

## Endpoint format

Vespa Cloud endpoints are on the format: `{random}.{random}.{scope}.vespa-app.cloud`.

## Endpoint scopes

### Zone endpoint

This is the default endpoint for a deployment. Requests through a zone endpoint are sent directly to the zone.

Zone endpoints are created implicitly, one per container cluster declared in [services.xml](/en/reference/applications/services/container.html). Zone endpoints are not configurable.

Zone endpoints have the suffix `z.vespa-app.cloud`

### Global endpoint

A global endpoint is an endpoint that can route requests to multiple zones. It can be configured in [deployment.xml](/en/reference/applications/deployment.html#endpoints-global). Similar to how a [CDN](https://en.wikipedia.org/wiki/Content_delivery_network) works, requests through this endpoint will be routed to the nearest zone based on geo proximity, i.e. the zone that is nearest to the client.

Global endpoints have the suffix `g.vespa-app.cloud`

 **Important:** Global endpoints do not support feeding. Feeding must be done through zone endpoints.

## Routing control

Vespa Cloud has two mechanisms for manually controlling routing of requests to a zone:

- Removing the `<region>` element from the relevant `<endpoint>` elements in [deployment.xml](../reference/applications/deployment.html) and deploying a new version of your application. 
- Changing the status through the console.

This section describes the latter mechanism. Navigate to the relevant deployment of your application in the console. Hovering over the _GLOBAL ROUTING_ badge will display the current status and when it was last changed.

### Change status

In case of a production emergency, a zone can be manually set out to prevent it from receiving requests:

1. Hover over the _GLOBAL ROUTING_ badge for the problematic deployment and click _Deactivate_. 
2. Inspection of the status will now show the status set to _OUT_. To set the zone back in and have it continue receiving requests: Hover over the _GLOBAL ROUTING_ badge again and click _Activate_. 

### Behaviour

Changing the routing status is independent of the endpoint scope used. You're technically overriding the routing status the deployment reports to the Vespa Cloud routing infrastructure. This means that a change to routing status affects both _zonal endpoints_ and _global endpoints_.

Deactivating a deployment disables routing of requests to that deployment through global endpoints until the deployment is activated again. As routing through these endpoints is DNS-based, it may take up between 5 and 15 minutes for all traffic to shift to other deployments.

If all deployments of an endpoint are deactivated, requests are distributed as if all deployments were active. This is because attempting to route traffic according to the original configuration is preferable to discarding all requests.

## AWS clients

While Vespa Cloud is hosted in AWS, clients that talk to Vespa Cloud from AWS nodes will be treated as any other client from the Internet. This means clients in AWS will generate regular Internet egress traffic even though they are talking to a service in AWS in the same zone.

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Endpoint format](#)
- [Endpoint scopes](#)
- [Zone endpoint](#zone-endpoint)
- [Global endpoint](#global-endpoint)
- [Routing control](#routing-control)
- [Change status](#)
- [Behaviour](#)
- [AWS clients](#aws-clients)

