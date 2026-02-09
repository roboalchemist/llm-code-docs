# Source: https://docs.vespa.ai/en/learn/tenant-apps-instances.html.md

# Tenants, Applications and Instances

 

When registering for Vespa Cloud, a _tenant_ is created. Tenant is the billable unit, and most often represents an organization. A tenant has one or more _applications_ with one or more _instances_:

 ![A tenant can have multiple applications with multiple instances each](/assets/img/tenants-apps-instances.svg)

Instances are used for different use cases, and are deployed to a set of [zones](../operations/zones.html) - example:

 ![An application can be deployed to multiple zones](/assets/img/instances-zones.svg)

The _Application_ has a "default" instance serving queries from two _production_ zones. It has an "integration" instance with another dataset, used for other applications to interface a production-like, stable interface. Finally, a developer has deployed the "bob" instance to a _dev_ zone to further develop plugin code.

Deployments to production zones are specified in [deployment.xml](../reference/applications/deployment.html). Deployments to the manual _dev_ zones are normally done directly from a developer computer for rapid code and config development. Read more in [Automated deployments](../operations/automated-deployments.html).

The service configuration is specified in [services.xml](../reference/applications/services/services.html) and is composed of individually sized _clusters_. A cluster is deployed to a set of _nodes_ with _resources_ specified.

## Lifecycle

The tenant name cannot be changed - create a new tenant, or contact Vespa Support.

Tenants in trial are auto-expired once trial is completed. Move to a paid plan to keep applications and data.

It is not possible to auto-migrate applications and data between tenants. To move an application to a new tenant, re-deploy the application with the new tenant name, see [cloning applications and data](../cloud/cloning-applications-and-data).

 Copyright © 2026 - [Cookie Preferences](#)

