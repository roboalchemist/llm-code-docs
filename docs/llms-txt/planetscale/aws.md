# Source: https://planetscale.com/docs/vitess/managed/aws.md

# PlanetScale Managed on AWS overview

> PlanetScale Managed on Amazon Web Services (AWS) is a single-tenant deployment of PlanetScale in your AWS organization within an isolated AWS Organizations member account.

## Overview

In this configuration, you can use the same API, CLI, and web interface that PlanetScale offers, with the benefit of running entirely in an AWS Organizations member account that you own and PlanetScale manages for you.

## Architecture

The PlanetScale data plane is deployed inside of a PlanetScale-controlled AWS Organizations member account in your AWS organization.
The Vitess cluster will run within this member account, orchestrated via Kubernetes.

We distribute components of the cluster across three AWS availability zones within your selected region to ensure high availability.
You can deploy PlanetScale Managed to any AWS region with at least three availability zones, including those not supported by the PlanetScale self-serve product.

Backups, part of the data plane, are stored in S3 inside the same member account.
PlanetScale Managed uses isolated Amazon Elastic Compute Cloud (Amazon EC2) instances as part of the deployment.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=dc1fa5d01017c5e105d9f2fb59aa5946" alt="Architecture diagram for PlanetScale Managed in AWS" data-og-width="1664" width="1664" data-og-height="1118" height="1118" data-path="docs/images/assets/docs/managed/aws/aws-arch-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=27ad4832e817b50d5b855fe9b7b8e8df 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b89cd6bb954ea158e4ecfb8f00ebf135 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=c03abc4f85055d93c4696c4b64a8beef 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=8b249ab8f8116bd35c59d9011a57e84e 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=62b371d1d5b163b0684c6b24a32baa22 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-arch-diagram.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=fca36834076de28e021bdf546e0fd490 2500w" />
</Frame>

Your database lives entirely inside a dedicated AWS Organizations member account within your AWS organization.
PlanetScale will not have access to other member accounts nor your organization-level settings within AWS.
Outside of your AWS organization, we run the PlanetScale control plane, which includes the PlanetScale API and web application, including the dashboard you see at `app.planetscale.com`.

The Vitess cluster running inside Kubernetes is composed of a number of Vitess Components.
All incoming queries are received by one of the **VTGates**, which then routes them to the appropriate **VTTablet**.
The VTGates, VTTablets, and MySQL instances are distributed across 3 availability zones.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ee039f8d95d7fea1226360744d2e0f94" alt="Diagram of Vitess cluster on AWS" data-og-width="2184" width="2184" data-og-height="1626" height="1626" data-path="docs/images/assets/docs/managed/aws/aws-vitess.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=96d2ad24d694a21b1d2d36bcf49b2a53 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9c6dc87d00e2d360b19ac3cd4ca60347 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=25b679054b4364a7e567227820821a89 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=6c5a37d48033097ec81c9d2db79ee0b6 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5f226e36dbcbe4ffabdaf9b704bd939e 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/aws-vitess.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=d3617b2d36b0c085b66ddc4e7f38e16b 2500w" />
</Frame>

Several additional required Vitess components are run in the Kubernetes cluster as well.
The topology server keeps track of cluster configuration.
**VTOrc** monitors cluster health and handles repairs, including managing automatic failover in case of an issue with a primary.
**vtctld** along with the client **vtctl** can be used to make changes to the cluster configuration and run workflows.

## Security and compliance

PlanetScale Managed is an excellent option for organizations with specific security and compliance requirements.

You own the AWS organization and member account that PlanetScale is deployed within an isolated architecture. This differs from when your PlanetScale database is deployed within our AWS organizations.

<Note>
  PlanetScale manages the entire member account and can NOT support customers running Terraform or other configuration management in the member account.
</Note>

### PCI compliance

Along with System and Organization Controls (SOC) 2 Type 2 and other [security and compliance](/docs/security) practices that PlanetScale has been issued and follows, PlanetScale Managed has been issued an Attestation of Compliance (AoC) and Report on Compliance (RoC), certifying our compliance with the PCI DSS 4.0 as a [Level 1 Service Provider](https://www.pcisecuritystandards.org/glossary/service-provider/). This enables PlanetScale Managed to be used via a shared responsibility model across merchants, acquirers, issuers, and other roles in storing and processing cardholder data.

<Note>
  If you have any questions or concerns related to the security and compliance of PlanetScale Managed, please [contact us](https://planetscale.com/contact), and we will be happy to discuss them further.
</Note>

### AWS PrivateLink

By default, all connections are encrypted, but public. Optionally, you also have the option to use private database connectivity through [AWS PrivateLink](/docs/vitess/managed/aws/privatelink).

### Fully private network isolation

You can also turn off public database access with a dual AWS PrivateLink setup. PlanetScale's control plane will talk to your member account over AWS PrivateLink, and your VPCs will also communicate with your database over AWS PrivateLink. Please get in touch with your PlanetScale Account Manager for more information on how to set up fully private network isolation.

### Third-account customer-controlled public key infrastructure

PlanetScale Managed on AWS supports public key infrastructure (PKI) services. PlanetScale Managed customers can provide PlanetScale the use of a set of customer-managed keys in a third AWS account inside your organization. This third account is controlled by you, the customer. PlanetScale has no administrative access. Your organization is the custodian for this key material. PlanetScale uses the customer-managed keys to encrypt EBS volumes, S3 buckets, and for envelope encryption of backups.

## Billing

With any of the PlanetScale Enterprise offerings, including PlanetScale Managed, you have the option to purchase PlanetScale through the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-luy3krhkpjne4). In addition to this, the resources you use on PlanetScale will qualify against your EDP commitment.

<Note>
  If you have any billing-related questions for PlanetScale Managed, please [contact us](https://planetscale.com/contact), and we will be happy to discuss them further.
</Note>

## Getting started with PlanetScale Managed in AWS

If you want to see what is involved in getting set up with PlanetScale Managed in AWS, you can see the [AWS set up documentation](/docs/vitess/managed/aws/getting-started).

If you are interested in exploring PlanetScale Managed further, please [contact us](https://planetscale.com/contact), and we can chat more about your requirements and see if PlanetScale Managed is a good fit for you.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt