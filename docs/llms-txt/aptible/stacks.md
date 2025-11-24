# Source: https://www.aptible.com/docs/core-concepts/architecture/stacks.md

# Stacks

> Learn about using Stacks to deploy resources to various regions

<Frame>
    <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=bd666044298866ac13ce9444a542ae26" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/1-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b654c604d06eb46f4fad6372356809c4 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b9e8eda1d05bc5143683c02b7792b094 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=913f3637810b30c9f38a0c6bb6fd6c9d 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8887aa785d1d9de12f03583f6a229acd 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=0eaa88875de391bcf75443f4bab6bd8a 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-app-ui.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=dac0bde86f760bfd5eb0de390edae025 2500w" />
</Frame>

# Overview

Stacks are fundamental to the network-level isolation of your resources. Each Stack is hosted in a specific region and is comprised of [environments](/core-concepts/architecture/environments). Aptible offers two types of Stacks: [Shared Stacks](/core-concepts/architecture/stacks#shared-stacks) (non-isolated) and [Dedicated Stacks](/core-concepts/architecture/stacks#dedicated-stacks) (isolated).

Resources in different Stacks can only connect with each other with a [network integration.](/core-concepts/integrations/network-integrations) For example: Databases and Internal Endpoints deployed in a given Stack are not accessible from Apps deployed in other Stacks.

<Note> The underlying virtualized infrastructure (EC2 instances, private network, etc.), which provides network-level isolation of resources.</Note>

# Shared Stacks (Non-Isolated)

Stacks shared across many customers are called Shared Stacks. Use Shared Stacks for development, testing, and staging [Environments](/core-concepts/architecture/environments).

<Warning> You can not host sensitive or regulated data with shared stacks.</Warning>

# Dedicated Stacks (Isolated)

<Info> Dedicated Stacks are only available on [Production and Enterprise plans.](https://www.aptible.com/pricing)</Info>

Dedicated stacks are built for production [environments](/core-concepts/architecture/environments), are dedicated to a single customer, and provide four significant benefits:

* **Tenancy** - Dedicated stacks are isolated from other Aptible customers, and you can also use multiple Dedicated Stacks to architect the [isolation](/core-concepts/architecture/overview#what-kinds-of-isolation-can-aptible-provide) you require within your organization.
* **Availability** - Aptible's [Service Level Agreement](https://www.aptible.com/legal/service-level-agreement/) applies only to Environments hosted on a Dedicated stack.
* **Regulatory** - Aptible will sign a HIPAA Business Associate Agreement (BAA) to cover information processing in Environments hosted on a Dedicated stack.
* **Connectivity** - [Integrations](/core-concepts/integrations/network-integrations), such as VPN and VPC Peering connections, are available only to Dedicated stacks.
* **Security** - Dedicated stacks automatically come with a [suite of security features](https://www.aptible.com/secured-by-aptible), including encryption, DDoS protection, host hardening, [intrusion detection](/core-concepts/security-compliance/hids), and [vulnerability scanning ](/core-concepts/security-compliance/security-scans)— alleviating the need to worry about security best practices.

## Supported Regions

<Frame>
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3ddaf8e8bbed083fb7f4dd7088a1e46b" alt="" data-og-width="1500" width="1500" data-og-height="1000" height="1000" data-path="images/regions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=18a083533a8c131372569164792ec6f3 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4ae05f8f10f53d997e31920e3d3fe5d6 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f57d1fc8ec956ddf123dbfe01d7ca7b9 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9863c8e3596c86b32f1d1af2eca3ad8d 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6959ace0c6b15d247faf328b2089b18a 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/regions.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3715b235f41e0196fb2448f8dcf75aa7 2500w" />
</Frame>

| Region                                    | Available on Shared Stacks | Available on Dedicated Stacks |
| ----------------------------------------- | -------------------------- | ----------------------------- |
| us-east-1 / US East (N. Virginia)         | ✔️                         | ✔️                            |
| us-east-2 / US East (Ohio)                |                            | ✔️                            |
| us-west-1 / US West (N. California)       | ✔️                         | ✔️                            |
| us-west-2 / US West (Oregon)              |                            | ✔️                            |
| eu-central-1 / Europe (Frankfurt)         | ✔️                         | ✔️                            |
| sa-east-1 / South America (São Paulo)     |                            | ✔️                            |
| eu-west-1 / Europe (Ireland)              |                            | ✔️                            |
| eu-west-2 / Europe (London)               |                            | ✔️                            |
| eu-west-3 / Europe (Paris)                |                            | ✔️                            |
| ca-central-1 / Canada (Central)           | ✔️                         | ✔️                            |
| ap-south-1 / Asia Pacific (Mumbai)        | ✔️                         | ✔️                            |
| ap-southeast-2 / Asia Pacific (Sydney)    | ✔️                         | ✔️                            |
| ap-northeast-1 / Asia Pacific (Tokyo)     |                            | ✔️                            |
| ap-southeast-1 / Asia Pacific (Singapore) |                            | ✔️                            |

<Tip> A Stack's Region will affect the latency of customer connections based on proximity. For [VPC Peering](/core-concepts/integrations/network-integrations), deploy the Aptible Stack in the same region as the AWS VPC for both latency and DNS concerns.</Tip>

# FAQ

<AccordionGroup>
  <Accordion title="How do I create or deprovision a dedicated stack?">
    ### Read the guide

    <Card title="How to create and deprovison dedicated stacks" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/create-dedicated-stack" />
  </Accordion>

  <Accordion title="Does Aptible support multi-region setups for business continuity?">
    Yes, this is touched on in our [Business Continuity Guide](https://www.aptible.com/docs/business-continuity). For more information about setup, contact Aptible Support.
  </Accordion>

  <Accordion title="How much do Dedicated Stacks cost?">
    See our pricing page for more information: [https://www.aptible.com/pricing](https://www.aptible.com/pricing)
  </Accordion>

  <Accordion title="Can Dedicated Stacks be renamed?">
    Dedicated Stacks cannot be renamed once created. To update the name of a Dedicated Stack, you create a new Dedicated Stack and migrate your resources to this new Stack. Please note: this does incur downtime.
  </Accordion>

  <Accordion title="Can my resources be migrated from a Shared Stack to a Dedicated Stack">
    Yes, contact Aptible Support to request resources be migrated.
  </Accordion>
</AccordionGroup>
