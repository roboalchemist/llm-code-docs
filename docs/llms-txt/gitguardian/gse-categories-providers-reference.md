# Source: https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/gse-categories-providers-reference.md

# Secret Enricher Categories Reference

> Reference of all Secret Enricher categories and providers used to classify generic secret incidents by service type.

# Secret Enricher Categories Reference

The "Secret Enricher" feature uses machine learning to analyze the context around generic secrets and automatically classify them into **categories** and identify specific **providers**. This classification helps you prioritize remediation efforts by understanding the potential impact and criticality of each incident.

When Secret Enricher successfully enriches a generic incident, the enriched secret name (like "Redis Identifiers" or "Stripe API Key") automatically replaces the generic detector name throughout the platform, giving you immediate, actionable context.

:::info
This feature is specifically designed for **generic incidents** that couldn't be matched to a specific detector. The GSE analyzes the surrounding context to provide enriched names, categories, and provider insights that help with prioritization and remediation.

Later on we will also enrich specific incidents to unveil more context.
:::

## How Secret Enricher Categories and Enriched Names Help with Remediation

The Secret Enricher transforms incident management through enriched names and categories:

- **Instant Identification**: Enriched names like "PostgreSQL Connection String" or "Stripe API Key" immediately tell you what leaked
- **Prioritize critical infrastructure**: Categories help you focus on Cloud providers, Databases, Payment systems first

## Categories Reference

### ð¤ AI
**What it includes:** API keys and tokens for artificial intelligence and machine learning services.

**Examples:** OpenAI, Anthropic, Hugging Face, Cohere, DeepSeek, Mistral AI, Azure OpenAI

**Why it matters:** AI services can be expensive to abuse and may contain sensitive data or model access. Leaked AI tokens could lead to:
- Unauthorized API usage and billing
- Access to proprietary models or training data
- Potential data exfiltration through AI services

### ð CDN
**What it includes:** Content Delivery Network services and edge computing platforms.

**Examples:** Cloudflare, Fastly, Amazon CloudFront, Akamai, Bunny.net

**Why it matters:** CDN credentials can impact website performance, security configurations, and content delivery. Compromise could lead to:
- Website defacement or content manipulation
- DDoS protection bypass
- SSL/TLS certificate compromise

### ð CI/CD
**What it includes:** Continuous Integration and Continuous Deployment pipeline credentials.

**Examples:** CircleCI, BuildKite, LaunchDarkly, Jenkins, GitLab CI

**Why it matters:** CI/CD credentials provide access to deployment pipelines and can impact entire development workflows. Compromise could lead to:
- Unauthorized code deployments
- Supply chain attacks
- Access to production environments
- Source code exposure

### âï¸ Cloud Provider
**What it includes:** Major cloud infrastructure provider credentials.

**Examples:** Amazon AWS, Microsoft Azure, Google Cloud, DigitalOcean, Terraform, OVH

**Why it matters:** Cloud provider credentials often have broad access to infrastructure resources. Compromise could lead to:
- Data breaches
- Resource manipulation or deletion
- Cryptocurrency mining
- Service disruption
- High billing costs

### ð Code Analysis
**What it includes:** Code quality, security scanning, and analysis platform credentials.

**Examples:** SonarQube, Code Climate, Codacy, Snyk, Sourcegraph

**Why it matters:** These tools often have access to source code and security findings. Compromise could lead to:
- Source code exposure
- Security vulnerability information disclosure
- Manipulation of security reports

### ð¤ Collaboration Tool
**What it includes:** Team collaboration, project management, and productivity platform credentials.

**Examples:** Asana, Trello, Notion, Contentful, Netlify, Atlassian

**Why it matters:** Collaboration tools contain business information and team communications. Compromise could lead to:
- Sensitive business information exposure
- Project manipulation
- Unauthorized access to team communications

### ð CRM
**What it includes:** Customer Relationship Management system credentials.

**Examples:** Salesforce, HubSpot, Freshdesk, Zendesk

**Why it matters:** CRM systems contain sensitive customer data and business information. Compromise could lead to:
- Customer data breaches
- Privacy regulation violations (GDPR, CCPA)
- Competitive intelligence exposure
- Customer relationship damage

### ðª Cryptos
**What it includes:** Cryptocurrency exchange and blockchain service credentials.

**Examples:** Coinbase, Bitfinex, Kraken, various blockchain APIs

**Why it matters:** Cryptocurrency credentials can provide direct access to financial assets. Compromise could lead to:
- Direct financial theft
- Unauthorized trading
- Wallet compromise

### ðï¸ Data Storage
**What it includes:** Database systems, cloud storage, and data management service credentials.

**Examples:** PostgreSQL, MySQL, MongoDB, Redis, Amazon S3, Supabase, PlanetScale

**Why it matters:** Data storage credentials provide access to potentially sensitive business and customer data. Compromise could lead to:
- Data breaches
- Data manipulation or deletion
- Privacy regulation violations
- Business disruption

### ð E-commerce
**What it includes:** Online commerce platform and marketplace credentials.

**Examples:** Shopify, Webflow, Etsy, various e-commerce APIs

**Why it matters:** E-commerce credentials can affect online sales and customer experience. Compromise could lead to:
- Customer data exposure
- Order manipulation
- Payment system compromise
- Revenue impact

### ð Identity Provider
**What it includes:** Authentication, authorization, and identity management service credentials.

**Examples:** Auth0, Okta, Microsoft Azure Active Directory, Ping Identity, Keycloak

**Why it matters:** Identity providers control access to multiple systems and user authentication. Compromise could lead to:
- Unauthorized access to connected systems
- User impersonation
- Single sign-on (SSO) bypass
- Privilege escalation

### ð¢ Internal
**What it includes:** Internal or proprietary system credentials.

**Examples:** Custom internal APIs, proprietary services, internal tools

**Why it matters:** Internal credentials provide access to organization-specific systems. Impact varies based on the specific system, but could lead to:
- Internal system compromise
- Proprietary information exposure
- Business process disruption

### ð¬ Messaging System
**What it includes:** Communication platforms, email services, and messaging APIs.

**Examples:** Slack, Twilio, SendGrid, Mailgun, Zoom, Discord, Microsoft Teams

**Why it matters:** Messaging systems handle communications and notifications. Compromise could lead to:
- Communication interception
- Spam or phishing campaigns
- Business communication disruption
- Social engineering attacks

### ð Monitoring
**What it includes:** Application performance monitoring, logging, and observability platform credentials.

**Examples:** Datadog, New Relic, Splunk, Grafana, GitGuardian, Lacework

**Why it matters:** Monitoring tools have access to system metrics, logs, and security information. Compromise could lead to:
- Sensitive system information exposure
- Security monitoring bypass
- Performance data manipulation
- Infrastructure intelligence gathering

### ð¦ Package Registry
**What it includes:** Software package repository and artifact storage credentials.

**Examples:** NPM, PyPI, RubyGems, NuGet, JFrog Artifactory, Docker registries

**Why it matters:** Package registry credentials can affect software supply chain security. Compromise could lead to:
- Malicious package publishing
- Supply chain attacks
- Dependency compromise
- Software integrity issues

### ð³ Payment System
**What it includes:** Payment processing, financial services, and fintech platform credentials.

**Examples:** Stripe, PayPal, Square, Plaid, Razorpay, GoCardless, Amazon MWS

**Why it matters:** Payment credentials provide access to financial transactions and customer payment data. Compromise could lead to:
- Financial fraud
- Payment data breaches
- PCI DSS compliance violations
- Direct financial loss

### ð Private Key
**What it includes:** Private keys, certificates, and cryptographic material.

**Examples:** SSL/TLS certificates, SSH keys, cryptographic signing keys

**Why it matters:** Private keys are fundamental to security infrastructure. Compromise could lead to:
- Encryption bypass
- Digital signature forgery
- SSL/TLS certificate compromise
- Authentication bypass

### ð Remote Access
**What it includes:** Remote access tools, VPN services, and secure connection credentials.

**Examples:** SSH, Tailscale, various VPN services, remote desktop tools

**Why it matters:** Remote access credentials provide direct system access. Compromise could lead to:
- Unauthorized system access
- Network lateral movement
- Remote system control
- Bypassing network security controls

### ð Secret Management
**What it includes:** Secret management platforms and credential storage services.

**Examples:** HashiCorp Vault, Doppler, 1Password, Delinea, AWS Secrets Manager

**Why it matters:** Secret management credentials provide access to other stored secrets and credentials. Compromise could lead to:
- Mass credential exposure
- Centralized secret compromise
- Cascading security failures

### ð± Social Network
**What it includes:** Social media platform and social networking service credentials.

**Examples:** LinkedIn, Twitter, Meta/Facebook, various social media APIs

**Why it matters:** Social network credentials can impact brand reputation and communications. Compromise could lead to:
- Brand reputation damage
- Unauthorized social media posting
- Social engineering attacks
- Customer communication disruption

### ð Version Control Platform
**What it includes:** Source code management and version control system credentials.

**Examples:** GitHub, GitLab, Bitbucket, various Git hosting services

**Why it matters:** Version control credentials provide access to source code and development history. Compromise could lead to:
- Source code theft
- Malicious code injection
- Development process disruption
- Intellectual property theft

### â Other
**What it includes:** Services that don't fit into other categories or are not yet classified.

**Examples:** Various APIs, specialized services, or unknown providers

## Using Enriched Names and Categories in Your Workflow

### 1. Set Up Custom Views
Create [saved views](../../platform/collaboration-and-sharing/saved-views) that focus on high-priority categories:
- **Critical Infrastructure:** Filter for "Secret Management", "Cloud provider", "Data storage", "Identity provider"
- **Financial Systems:** Filter for "Payment system", "Cryptos", "E-commerce"
- **Development Security:** Filter for "Version control platform", "CI/CD", "Package registry"

### 2. Apply Automated Severity Rules
Use Secret categories in your [automated severity scoring rules](../../internal-monitoring/remediate/prioritize-incidents#automated-severity-scoring):
- **Critical severity:** Incidents categorized as "Payment system", "Cloud provider", "Identity provider"
- **Critical or High severity:** Incidents categorized as "Data storage", "CI/CD", "Version control platform"
- **Medium severity:** Other categorized incidents

## Best Practices

1. **Don't ignore "Other" category** - Investigate these incidents to understand their actual impact
2. **Combine with other incident attributes** - Use Secret categories alongside validity checks, tags, and occurrences
3. **Regularly review and refine** - Update your priority matrix as you learn more about your environment
4. **Document decisions** - Keep track of how you handle different categories to improve future response

## Limitations

- **Not all generic incidents can be enriched**: Incidents with insufficient context may not receive enriched names and will retain their generic detector names
- **Provider availability**: Provider-level enrichment (e.g., "Redis") is available for more incidents than specific enriched names
- **Context-based analysis**: Enrichments are based on contextual ML analysis and may not be 100% accurate in all cases
- **Continuous improvement**: New categories, providers, and enriched names are continuously being added to improve coverage
- **Enriched vs. Specific**: Enriched incidents remain classified as "generic" from a detection standpoint but display specific names for usability

:::tip
Our goal is for every workspace to have zero truly "generic" secretsâall incidents should have maximum definition possible through either specific detectors or ML-powered enrichment.
:::

*This reference guide helps you understand and effectively use enriched names and GSE categories for incident prioritization. For more information on using the Secret Enricher, see the [Machine Learning](./machine_learning) documentation.*
