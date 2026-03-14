# Source: https://docs.gitguardian.com/platform/deployment-model/deployment-models.md

# Overview

> Overview of GitGuardian's deployment options including SaaS, self-hosted, and hybrid architectures with the ggbridge relay.

# GitGuardian Deployment Models

GitGuardian offers flexible deployment options to meet diverse organizational needs, from cloud-first companies to enterprises with strict security and compliance requirements. Choose the deployment model that best fits your infrastructure, security posture, and operational preferences.

## Available deployment models

### GitGuardian SaaS
**Fully managed cloud solution**

GitGuardian SaaS is our cloud-hosted platform that provides immediate access to all GitGuardian features without any infrastructure management overhead.

**Best for Organizations:**
- Requiring faster time-to-value
- Without dedicated DevOps or Infrastructure resources
- Comfortable with SaaS infrastructure

**Key Benefits:**
- Instant setup and deployment
- Automatic updates and maintenance
- Global availability and performance
- No infrastructure costs or management
- Access to latest features first
- [Service status monitoring](https://status.gitguardian.com)

**Available Regions:**
- **USA**: us-west-2 (Oregon) - Available for all plans
- **Europe**: eu-central-1 (Frankfurt) - Available for [Business and Enterprise customers](https://www.gitguardian.com/pricing#plan-details)

[**Get started with SaaS â**](../getting-started/account-creation.md)

---

### GitGuardian Bridge
**SaaS with secure private network access**

GitGuardian Bridge extends GitGuardian SaaS with secure, encrypted tunnels to your private infrastructure, enabling you to scan and monitor self-hosted services without exposing them to the internet.

**Best for:**
- Organizations using both cloud and on-premise infrastructure
- Companies wanting SaaS benefits while accessing private systems
- Teams with mixed infrastructure environments
- Enterprises requiring secure private network integration

**Key Benefits:**
- Full SaaS platform benefits with private network access
- Secure, outbound-only connections
- Scan private repositories and services
- No inbound firewall rules required
- Multiple network support

[**Learn about GitGuardian Bridge â**](./ggbridge.md)

---

### GitGuardian Self-Hosted
**Complete control in your environment**

GitGuardian Self-Hosted runs entirely within your infrastructure, giving you complete control over data, security, and compliance while maintaining all core platform capabilities.

**Best for:**
- Organizations with strict data residency requirements
- Enterprises with custom compliance frameworks
- Companies requiring air-gapped environments
- Teams with existing Kubernetes/container infrastructure

**Key Benefits:**
- Complete data control and residency
- Custom security and compliance configurations
- Integration with existing infrastructure
- Air-gap deployment support

[**Explore self-hosted option â**](./self-hosted.md)

## Comparison matrix

| Feature | SaaS | SaaS + GG Bridge | Self-Hosted |
|---------|------|------------------|-------------|
| **Setup Time** | Minutes | Hours | Hours to Days |
| **Infrastructure Management** | None | Minimal | Full |
| **Data Location** | GitGuardian Cloud | GitGuardian Cloud | Your Infrastructure |
| **Firewall Requirements** | Inbound/Outbound | Outbound only | N/A |
| **Maintenance** | Automatic | Minimal | Manual |
| **Feature Access** | Latest | Latest | Monthly |

## Need help deciding?

Our team can help you evaluate the best deployment model for your specific requirements: [Contact our team](https://www.gitguardian.com/contact-us) for personalized guidance.
