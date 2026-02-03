# Source: https://braintrust.dev/docs/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Security

Braintrust implements industry-leading security practices and maintains compliance with key standards to protect your data and ensure the highest levels of security for the platform.

<Tip>
  The [Trust center](https://trust.braintrust.dev/) is the central resource for information about Braintrust's security practices, certifications, and policies. It provides up-to-date details for customers and partners.
</Tip>

## Deployment options

In addition to the managed cloud service, Braintrust offers a [hybrid deployment model](/admin/self-hosting). This allows customers to keep data secure within their own environment while taking advantage of Braintrust's newest UI and platform features.

## Authentication

The Braintrust UI supports end-user authentication through enterprise identity providers (Google, Okta, Microsoft), SSO/SAML integration with major providers (Okta Workforce, Microsoft Entra ID, Google Workspace), and OpenID Connect (OIDC) for custom providers. Users receive credentials directly in their browser that securely communicate with your data plane.

For programmatic access, API keys are displayed only once upon creation and stored as cryptographic hashes, never in plaintext. Each key inherits the user's permissions and can be scoped to specific projects. Best practices: rotate keys periodically, revoke compromised keys immediately, store keys in environment variables or secret management systems (never in code), apply principle of least privilege, and monitor API key usage through activity logs. See [API keys](/admin/authentication) to create and manage keys.

For [Model Context Protocol (MCP)](/integrations/developer-tools/mcp) servers, authentication uses OAuth 2.0 with PKCE (Proof Key for Code Exchange). MCP clients authenticate via standard OAuth flow and receive access tokens with refresh capabilities for secure, long-lived sessions. Tokens inherit your user account permissions, providing access only to resources you can normally access.

## Authorization

Braintrust uses role-based access control (RBAC) with built-in permission groups (Owners, Engineers, Viewers) and support for custom groups with fine-grained permissions. Permissions can be set at organization, project, or individual object (experiment, dataset, prompt) levels, enabling project-level isolation and object-level access control for sensitive resources. See [Access control](/admin/access-control) for configuration details.

## Data encryption

All data is encrypted at rest and in transit. LLM provider API keys and secrets are encrypted using AES-256 with unique 256-bit keys and nonces. For [self-hosted deployments](/admin/self-hosting), you control encryption keys through your cloud provider's key management system (AWS KMS, Google Cloud KMS, Azure Key Vault).

## Network security

The data plane runs in an isolated VPC with no access to internal infrastructure (hosted) or in your own VPC (self-hosted). [Custom code functions](#code-execution) can execute in quarantined VPCs on AWS deployments. Self-hosted deployments support firewall and VPN deployment for additional security. SDKs and browser UI communicate directly with your data plane via CORS — no customer data flows through Braintrust's control plane. Self-hosted deployments can access private network resources like internal LLM models, proprietary tools, and private databases. See [Architecture](/admin/architecture) for details.

## Code execution

Braintrust provides several [function types](/deploy/functions) to enable features like Python and TypeScript scorers, hosted tools, and replay-able eval functions. These functions are implemented using different execution mechanisms:

* **Prompts** - [Mustache or Nunjucks](/evaluate/write-prompts#use-templating)-templated text messages filled dynamically
* **Inline code** - TypeScript or Python code snippets
* **Bundled code** - Packaged TypeScript or Python applications
* **HTTP endpoints** - External functions called over HTTP
* **Global functions** - Pre-installed functions from the open source [autoevals](https://github.com/braintrustdata/autoevals) library

Prompts, HTTP endpoints, and global functions have straightforward security models: prompts are template expansions, HTTP endpoints communicate with your external services, and global functions run pre-vetted code from the autoevals library.

For inline and bundled code, the security model varies by deployment type:

* For Braintrust-hosted deployments and self-hosted deployments on AWS, inline and bundled code functions run in an isolated VPC specifically for function execution. This environment has no access to your internal infrastructure (databases, application servers), can make outbound internet requests (for API calls, package downloads), provides organization-level separation when multiple orgs share the same stack, and runs functions in ephemeral AWS Lambda environments.
* For self-hosted deployments on GCP and Azure, custom code runs in the same process as the data plane without isolation.

## Data residency and retention

[Self-hosted deployments](/admin/self-hosting) keep all sensitive data (experiment logs, traces, datasets, prompts) within your cloud account and region for regulatory compliance. Configure [automated retention policies](/admin/automations/data-management#configure-retention) to delete logs, experiments, or datasets after specified periods (e.g., 7 days for development, 90 days for production, 180 days for experiments). For hybrid deployments v1.1.21+, data is soft-deleted with a 24-hour grace period before permanent removal. [Export to S3](/admin/automations/data-management#export-to-s3) periodically with JSON Lines or Parquet formats, or export on-demand via API in JSON/Parquet for entire projects or organizations.

## Compliance

### SOC 2 Type II

Braintrust is SOC 2 Type II compliant. This independent audit confirms that our controls related to security, availability, and confidentiality are operating effectively over time. Associated documentation and reports are available on the [Trust Center](https://trust.braintrust.dev/) after signing a mutual NDA.

### HIPAA

Braintrust supports HIPAA compliance requirements and maintains the necessary administrative, physical, and technical safeguards for handling protected health information (PHI). For organizations subject to HIPAA regulations, Braintrust can execute Business Associate Agreements (BAAs).

To discuss your specific HIPAA compliance needs, [contact Braintrust](https://www.braintrust.dev/contact).

### GDPR

For GDPR compliance requirements, Braintrust can execute Data Processing Agreements (DPAs) to satisfy certain data processing obligations. However, for full GDPR compliance, organizations should use Braintrust's [hybrid deployment model](https://www.braintrust.dev/blog/hybrid-deployment) with self-hosting in the EU.

To discuss your specific GDPR requirements, [contact Braintrust](https://www.braintrust.dev/contact).
