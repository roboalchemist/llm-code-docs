# Source: https://www.aptible.com/docs/reference/pricing.md

# Pricing

> Learn about Aptible's pricing

# Aptible Hosted Pricing

The Aptible Hosted option allows organizations to provision infrastructure fully hosted by Aptible. This is ideal for organizations that prefer not to manage their own infrastructure and/or are looking to quickly get started. With this offering, the Aptible platform fee and infrastructure costs are wrapped into a simple, usage-based pricing model.

<CardGroup cols={3}>
  <Card title="Get started in minutes" icon="sparkles" iconType="duotone">
    Instantly deploy apps & databases
  </Card>

  <Card title="Simple pricing, fully on-demand" icon="play-pause" iconType="duotone">
    Pay-as-you-go, no contract required
  </Card>

  <Card title="Fast track compliance" icon="shield-halved" iconType="duotone">
    Infrastructure for ready for HIPAA, SOC 2, HITRUST & more
  </Card>
</CardGroup>

### On-Demand Pricing

|                            | Cost                                                    | Docs                                                                                       |
| -------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Compute**                |                                                         |                                                                                            |
| General Purpose Containers | \$0.08/GB RAM/hour                                      | [→](/core-concepts/scaling/container-profiles)                                             |
| CPU-Optimized Containers   | \$0.10/GB RAM/hour                                      | [→](/core-concepts/scaling/container-profiles)                                             |
| RAM-Optimized Containers   | \$0.05/GB RAM/hour                                      | [→](/core-concepts/scaling/container-profiles)                                             |
| **Databases**              |                                                         |                                                                                            |
| Database Storage (Disk)    | \$0.20/GB/month                                         | [→](/core-concepts/scaling/database-scaling)                                               |
| Database IOPS              | \$0.01/IOPS after the first 3,000 IOPs/month (included) | [→](/core-concepts/scaling/database-scaling)                                               |
| Database Backups           | \$0.02/GB/month                                         | [→](/core-concepts/managed-databases/managing-databases/database-backups)                  |
| **Isolation**              |                                                         |                                                                                            |
| Shared Stack               | Free                                                    | [→](/core-concepts/architecture/stacks)                                                    |
| Dedicated Stack            | \$499/Stack/month                                       | [→](/core-concepts/architecture/stacks)                                                    |
| **Connectivity**           |                                                         | [→]()                                                                                      |
| Endpoints (Load Balancers) | \$0.06/endpoint/hour                                    | [→](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#types-of-app-endpoints)  |
| Shared HTTP(S) Endpoints   | \$0.04/endpoint/hour                                    | [→](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/shared-endpoints) |
| VPN                        | \$99/VPN peer/month                                     | [→](/core-concepts/integrations/network-integrations)                                      |
| **Security & Compliance**  |                                                         |                                                                                            |
| HIDS Reporting             | [Contact us]()                                          | [→](/core-concepts/security-compliance/hids)                                               |

### Enterprise and Volume Pricing

Aptible offers discounts for Enterprise and volume agreements. All agreements require a 12-month commitment. [Contact us to request a quote.](https://app.aptible.com/contact)

# Self Hosted Pricing

<Info>
  This offering is currently in limited release. [Request early access here](https://app.aptible.com/signup?cta=early-access).
</Info>

The Self Hosted offering allows companies to host the Aptible platform directly within their own AWS accounts. This is ideal for organizations that already existing AWS usage or organizations interested in host their own infrastructure. With this offering, you pay Aptible a platform fee, and your infrastructure costs are paid directly to AWS.

<CardGroup cols={3}>
  <Card title="Unified Infrastructure" icon="badge-check" iconType="duotone">
    Manage your AWS infrastructure in your own account
  </Card>

  <Card title="Infrastructure costs paid directly to AWS" icon="aws" iconType="duotone">
    Leverage AWS discount and credit programs
  </Card>

  <Card title="Full access to AWS tools" icon="unlock" iconType="duotone">
    Unlock full access to tools and services within AWS marketplace
  </Card>
</CardGroup>

### On-Demand and Enterprise Pricing

All pricing for our Self Hosted offering is custom. This allows us to tailor agreements designed for organizations of all sizes.

# Support Plans

All Aptible customers receive access to email support with our Customer Reliability team. Our support plans give you additional access to things like increased targetted response times, 24x7 urgent support, Slack support, and a designated technical resources from the Aptible team.

<CardGroup cols={3}>
  <Card title="Standard" icon="signal-fair">
    **\$0/mo**

    Standard support with our technical experts. Recommended for the average production workload.
  </Card>

  <Card title="Premium" icon="signal-good">
    **\$499/mo**

    Faster response times with our technical experts. Recommended for average production workloads, with escalation ability.
  </Card>

  <Card title="Enterprise" icon="signal-strong">
    **Custom**

    Dedicated team of technical experts. Recommended for critical production workloads that require 24x7 support. Includes a Technical Account Manager and Slack support.
  </Card>
</CardGroup>

|                                | Standard        | Premium                                       | Enterprise                                    |
| ------------------------------ | --------------- | --------------------------------------------- | --------------------------------------------- |
| Get Started                    | Included        | [Contact us](https://app.aptible.com/contact) | [Contact us](https://app.aptible.com/contact) |
| **Target Response Time**       |                 |                                               |                                               |
| Low Priority                   | 2 Business Days | 2 Business Days                               | 2 Business Days                               |
| Normal Priority                | 1 Business Day  | 1 Business Day                                | 1 Business Day                                |
| High Priority                  | 1 Business Day  | 3 Business Hours                              | 3 Business Hours                              |
| Urgent Priority                | 1 Business Day  | 3 Business Hours                              | 1 Calendar Hour                               |
| **Support Options**            |                 |                                               |                                               |
| Email and Zendesk Support      | ✔️              | ✔️                                            | ✔️                                            |
| Slack Support (for Low/Normal) | -               | -                                             | ✔️                                            |
| 24/7 Support (for Urgent)      | -               | -                                             | ✔️                                            |
| Production Readiness Reviews   | -               | -                                             | ✔️                                            |
| Architectural Reviews          | -               | -                                             | ✔️                                            |
| Technical Account Manager      | -               | -                                             | ✔️                                            |

<Note>
  Aptible is committed to best-in-class uptime for all customers regardless of support plan. Aptible will make reasonable efforts to ensure your services running in Dedicated Environments are available with a Monthly Uptime Percentage of at least 99.95%. This means that we guarantee our customers will experience no more than 21.56 min/month of Unavailability.\
  Unavailability, for app services and databases, is when our customer's service or database is not running or not reachable due to Aptible's fault. Details on our commitment to uptime and company level SLAs can be found [here](https://www.aptible.com/legal/service-level-agreement). The following Support plans and their associated target response times are for roadblocks that customers may run into while Aptible Services are up and running as expected.
</Note>

# Trials

Aptible offers a 30-day free trial for Aptible-hosted resources upon sign-up if you sign up with a business email.

<Tip>
  Didn't receive a trial by default? [Contact us!](https://www.aptible.com/contact)
</Tip>

### Trial Usage Limits

All accounts on a trial have the following usage limits in place:

* **Scaling Limits**: 3GB of Compute, 20GB of Storage, 1 Endpoint
* **Stacks Limits:** Deploy to Shared Stacks in US East

Ready to scale beyond the trial? [Upgrade your plan to the Development or Production plan here](https://app.aptible.com/plans) in the Plans page to scale unlimitedly.

# FAQ

<AccordionGroup>
  <Accordion title="What’s the difference between the Aptible Hosted and Self Hosted options?">
    Hundreds of the fastest growing startups and scaling companies have used **Aptible’s hosted platform** for a decade. In this option, Aptible hosts and manages your resources, abstracting away all the complexity of interacting with an underlying cloud provider and ensuring resources are provisioned properly.

    Aptible also manages **existing resources hosted in your own cloud account**. This means that you integrate Aptible with your cloud accounts and Aptible helps your platform engineering team create a platform on top of the infrastructure you already have. In this option, you control and pay for your own cloud accounts, while Aptible helps you analyze and standardize your cloud resources.
  </Accordion>

  <Accordion title="How can I upgrade my support plan?">
    [Contact us](https://app.aptible.com/contact) to ugprade your support plan.
  </Accordion>

  <Accordion title="How do I manage billing details such as payment information or invoices?">
    See our [Billing & Payments](/core-concepts/billing-payments) page for more information.
  </Accordion>

  <Accordion title="Does Aptible offer a startup program?">
    Yes, see our [Startup Program page for more information](https://www.aptible.com/startup).
  </Accordion>
</AccordionGroup>
