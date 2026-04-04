# Source: https://docs.datafold.com/datafold-deployment/datafold-deployment-options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Options

> Datafold is a web-based application with multiple deployment options, including multi-tenant SaaS and dedicated cloud (either customer- or Datafold-hosted).

## SaaS / Multi-Tenant

Our standard multi-tenant deployment is a cost-efficient option for most teams and is available in two AWS regions:

| Region Name      | Region      | Sign-Up Page                                                               |
| :--------------- | :---------- | :------------------------------------------------------------------------- |
| US West (Oregon) | `us-west-2` | [https://app.datafold.com/org-signup](https://app.datafold.com/org-signup) |
| Europe (Ireland) | `eu-west-1` | [https://eu.datafold.com/org-signup](https://eu.datafold.com/org-signup)   |

For additional security, we provide the following options:

1. [IP Whitelisting](/security/securing-connections#ip-whitelisting): only allow access to specific IP addresses
2. [AWS PrivateLink](/security/securing-connections#private-link): set up a limited network point to access your RDS in the same region
3. [VPC Peering](/security/securing-connections#vpc-peering-saas): securely join two networks together
4. [SSH Tunnel](/security/securing-connections#ssh-tunnel): set up a secure tunnel between your network and Datafold with the SSH server on your side
5. [IPSec Tunnel](/security/securing-connections#ipsec-tunnel): an IPSec tunnel setup

## Dedicated Cloud

We also offer a single-tenant deployment of the Datafold application in a dedicated Virtual Private Cloud (VPC). The options are (from least to most complex):

1. **Datafold-hosted, Datafold-managed**: the Cloud account belongs to Datafold and we manage the Datafold application for you.
2. **Customer-hosted, Datafold-managed**: the Cloud account belongs to you, but we manage the Datafold application for you.
3. **Customer-hosted, Customer-managed**: the Cloud account belongs to you and you manage the Datafold application. Datafold does not have access.

Dedicated Cloud can be deployed to all major cloud providers:

* [AWS](/datafold-deployment/dedicated-cloud/aws)
* [GCP](/datafold-deployment/dedicated-cloud/gcp)
* [Azure](/datafold-deployment/dedicated-cloud/azure)

<Tip>
  **VPC vs. VNet**

  We use the term VPC across all major cloud providers. However, Azure refers to this concept as a Virtual Network (VNet).
</Tip>

### Datafold Dedicated Cloud FAQ

<AccordionGroup>
  <Accordion title="What is the benefit of a Dedicated Cloud deployment?">
    Dedicated Cloud deployment may be the preferred deployment method by customers with special privacy and security concerns and in highly regulated domains. In a Dedicated Cloud deployment, the entire Datafold stack runs on dedicated cloud infrastructure and network, which usually means it is:

    1. Not accessible to public Internet (sits behind customer's VPN)
    2. Uses internal network to communicate with customer's databases and other resources – none of the data is sent using public networks
  </Accordion>

  <Accordion title="How does a Customer-hosted Dedicated Cloud deployment work?">
    Datafold is deployed to customer's cloud infrastructure but is fully managed by Datafold. The only DevOps involvement needed from the customer's side is to set up a cloud project and role (steps #1 and #2 below).

    1. Customer creates a Datafold-specific namespace in their cloud account (subaccount in AWS / project in GCP / subscription or resource group in Azure)
    2. Customer creates a Datafold-specific IAM resource with permissions to deploy the Datafold-specific namespace
    3. Datafold Infrastructure team provisions the Datafold stack on the customer's infrastructure using fully-automated procedure with Terraform
    4. Customer and Datafold Infrastructure teams collaborate to implement the security and networking requirements, see [all available options](#additional-security-dedicated-cloud)

    See cloud-specific instructions here:

    * [AWS](/datafold-deployment/dedicated-cloud/aws)
    * [GCP](/datafold-deployment/dedicated-cloud/gcp)
    * [Azure](/datafold-deployment/dedicated-cloud/azure)

    After the initial deployment, the Datafold team uses the same procedure to roll out software updates and perform maintenance to keep the uptime SLA.
  </Accordion>

  <Accordion title="How does a Datafold-hosted Dedicated Cloud deployment work?">
    Datafold is deployed in the customer's region of choice on AWS, GCP, or Azure that is owned and managed by Datafold. We collaborate to implement the security and networking requirements ensuring that traffic either does not cross the public internet or, if it does, does so securely. All available options are listed below.
  </Accordion>

  <Accordion title="How does a Customer-hosted, Customer-managed deployment work?">
    This deployment method follows the same process as the standard customer-hosted deployment (see above), but with a key difference: the customer is responsible for managing both the infrastructure and the application. Datafold engineers do not have any access to the deployment in this case.

    We offer open-source projects that facilitate this deployment, with examples for every major cloud provider. You can find these projects on GitHub:

    * [AWS](https://github.com/datafold/terraform-aws-datafold)
    * [GCP](https://github.com/datafold/terraform-google-datafold)
    * [Azure](https://github.com/datafold/terraform-azure-datafold)

    Each of these projects uses a Helm chart for deploying the application. The Helm chart is also available on GitHub:

    * [Helm Chart](https://github.com/datafold/helm-charts)

    By providing these open-source projects, Datafold enables you to integrate the deployment into your own infrastructure, including existing clusters. This allows your infrastructure team to manage the deployment effectively.

    <Tip>
      **Deployment Secrets:** Datafold provides the necessary secrets for downloading images as part of the license agreement. Without this agreement, the deployment will not complete successfully.
    </Tip>
  </Accordion>

  <Accordion title="What additional security and networking options are available?">
    Because the Datafold application is deployed in a dedicated VPC, your databases/integrations are not directly accessible when they are not exposed to the public Internet. The following solutions enable secure connections to your databases/integrations without exposing them to the public Internet:

    <Tabs>
      <Tab title="AWS">
        1. [PrivateLink](/security/securing-connections?current-cloud=aws#private-link "PrivateLink")
        2. [VPC Peering](/security/securing-connections#vpc-peering-dedicated-cloud "VPC Peering")
        3. [SSH Tunnel](/security/securing-connections#ssh-tunnel "SSH Tunnel")
        4. [IPSec Tunnel](/security/securing-connections#ipsec-tunnel "IPSec Tunnel")
      </Tab>

      <Tab title="GCP">
        1. [Private Service Connect](/security/securing-connections?current-cloud=gcp#private-link "Private Service Connect")
        2. [VPC Peering](/security/securing-connections#vpc-peering-dedicated-cloud "VPC Peering")
        3. [SSH Tunnel](/security/securing-connections#ssh-tunnel "SSH Tunnel")
      </Tab>

      <Tab title="Azure">
        1. [Private Link](/security/securing-connections?current-cloud=azure#private-link "Private Link")
        2. [VNet Peering](/security/securing-connections#vpc-peering-dedicated-cloud "VNet Peering")
        3. [SSH Tunnel](/security/securing-connections#ssh-tunnel "SSH Tunnel")
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Can Datafold be deployed and managed by the customer's internal team?">
    Please inquire with [sales@datafold.com](mailto:sales@datafold.com) about customer-managed deployment options.
  </Accordion>
</AccordionGroup>
