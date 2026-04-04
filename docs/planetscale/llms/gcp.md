# Source: https://planetscale.com/docs/vitess/managed/gcp.md

# PlanetScale Managed on GCP overview

> PlanetScale Managed on Google Cloud Platform (GCP) is a single-tenant deployment of PlanetScale in your GCP organization within an isolated project.

## Overview

In this configuration, you can use the same API, CLI, and web interface that PlanetScale offers, with the benefit of running entirely in a GCP project that you own and PlanetScale manages for you.

## Architecture

As you can see in the architecture diagram below, the PlanetScale data plane is deployed inside of a PlanetScale-controlled project in your GCP organization.
The Vitess cluster will run within this project, orchestrated by Kubernetes.

We distribute components of the cluster across three GCP zones within a region to ensure high availability.
You can deploy PlanetScale Managed to any GCP region with at least three zones, including zones not supported by the PlanetScale self-serve product, so long as the region supports the required GCP services (including but not limited to Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Cloud Storage, Persistent Disk, Cloud Key Management Service (Cloud KMS), Cloud Logging).

Backups, part of the data plane, are stored in Cloud Storage inside the same project.
PlanetScale Managed uses isolated GCE instances as part of the deployment.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=a2db14dd5cef1e279da0be5e44839df8" alt="Architecture diagram for PlanetScale Managed in GCP" data-og-width="1664" width="1664" data-og-height="1118" height="1118" data-path="docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=0069c5641129d032f7530619cefb8f37 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b8197c865136ae812ff1d765215ef4f8 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9f14313dc14e9f2b0c42ee2951061ba9 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=4099f851877c7aff01e7f4a9e7a8e693 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=3e792a579cdccfb0bb33ca7d33e129b2 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-arch-diagram.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=f4fbd8cef20c375faa7872adfb5a8297 2500w" />
</Frame>

Your database lives entirely inside a dedicated project within GCP. PlanetScale will not have access to other projects nor your organization-level settings within GCP. Outside of your GCP organization, we run the PlanetScale control plane, which includes the PlanetScale API and web application, including the dashboard you see at `app.planetscale.com`.

The Vitess cluster running inside Kubernetes is composed of a number of Vitess Components.
All incoming queries are received by one of the **VTGates**, which then routes them to the appropriate **VTTablet**.
The VTGates, VTTablets, and MySQL instances are distributed across 3 availability zones.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=8c50c23071733bc6438efad7c983fced" alt="Diagram of Vitess cluster on GCP" data-og-width="2184" width="2184" data-og-height="1626" height="1626" data-path="docs/images/assets/docs/managed/gcp/gcp-vitess.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=76d49e0a03673caa209113739d8af319 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=63cf4ddd75ca92a065d4693cdb5e371b 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=f73f061fe6374be4a52281e4f7500914 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=329222cdd7cef430edfde0c4990db003 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=0460e9b1cf6392054c5d5e6e42b06485 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/gcp/gcp-vitess.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5d1b34dadcbdde55900d77e90327ad76 2500w" />
</Frame>

Several additional required Vitess components are run in the Kubernetes cluster as well.
The topology server keeps track of cluster configuration.
**VTOrc** monitors cluster health and handles repairs, including managing automatic failover in case of an issue with a primary.
**vtctld** along with the client **vtctl** can be used to make changes to the cluster configuration and run workflows.

## Security and compliance

PlanetScale Managed is an excellent option for organizations with specific security and compliance requirements.

You own the GCP organization and project that PlanetScale is deployed within an isolated architecture. This differs from when your PlanetScale database is deployed within our GCP organizations.

Along with System and Organization Controls (SOC) 2 Type 2 and PlanetScale [security and compliance](/docs/security) practices that PlanetScale has been issued and follows, we can also sign BAAs for [HIPAA compliance](https://planetscale.com/blog/planetscale-and-hipaa) on PlanetScale Managed.

<Note>
  PlanetScale manages the entire project and can NOT support customers running Terraform or other configuration management in the project.
</Note>

### GCP Private Service Connect

By default, all connections are encrypted, but public. Optionally, you also have the option to use private database connectivity through [GCP Private Service Connect](/docs/vitess/managed/gcp/private-service-connect), which is only available on single-tenancy deployment options, including PlanetScale Managed.

<Note>
  If you have any questions or concerns related to the security and compliance of PlanetScale Managed, please [contact us](https://planetscale.com/contact), and we will be happy to discuss them further.
</Note>

## Getting started with PlanetScale Managed in GCP

If you want to see what is involved in getting set up with PlanetScale Managed in GCP, you can see the [GCP set up documentation](/docs/vitess/managed/gcp/getting-started).

If you are interested in exploring PlanetScale Managed further, please [contact us](https://planetscale.com/contact), and we can chat more about your requirements and see if PlanetScale Managed is a good fit for you.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt