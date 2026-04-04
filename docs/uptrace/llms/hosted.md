# Source: https://uptrace.dev/raw/get/hosted.md

# Uptrace Editions

> Compare Community, Premium, Managed, and Cloud editions, including licensing, support levels, and deployment options.

## Introduction

Uptrace offers several editions designed to meet different needs and budgets:

- [Community Edition](/get/hosted/install). Our free version with core functionality and community support through GitHub issues. Perfect for getting started or smaller projects.
- [Premium Edition](#premium-edition). Full-featured version at $200/month, including complete functionality and dedicated email support for your team.
- [Managed Edition](#managed-edition). Premium service where our team handles everything for you. Includes comprehensive 16/5 support via Slack, Telegram, or email, plus complete infrastructure management.
- [Uptrace Cloud](https://app.uptrace.dev/join). Our premium cloud-hosted solution with flexible, usage-based [pricing](/pricing). Get all the power of Premium Edition without managing your own infrastructure.

Each edition can be hosted on your own servers (except Cloud), giving you full control over your monitoring data and infrastructure.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Community
    </th>
    
    <th>
      Premium
    </th>
    
    <th>
      Managed
    </th>
    
    <th>
      Cloud
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Custom data retention
    </td>
    
    <td>
      14 days
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
  </tr>
  
  <tr>
    <td>
      Role-based access control
    </td>
    
    <td>
      â
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
  </tr>
  
  <tr>
    <td>
      Single Sign-On using OIDC and SAML
    </td>
    
    <td>
      â
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
  </tr>
  
  <tr>
    <td>
      Two-factor authentication
    </td>
    
    <td>
      â
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
  </tr>
  
  <tr>
    <td>
      High-availability setup
    </td>
    
    <td>
      â
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
  </tr>
  
  <tr>
    <td>
      Managed by Uptrace
    </td>
    
    <td>
      â
    </td>
    
    <td>
      â
    </td>
    
    <td>
      âï¸
    </td>
    
    <td>
      âï¸
    </td>
  </tr>
</tbody>
</table>

## Premium Edition

To access premium features, you'll need to purchase a license:

- Create an account at [app.uptrace.dev](https://app.uptrace.dev/join).
- Navigate to "Organization" -> "Licenses" and click the "New license" button.

![New license](/get/editions/new-license.png)

There are two types of licenses to fit your needs:

- **Monthly license**. Pay monthly with automatic renewals. Your Uptrace instance will periodically connect to api.uptrace.dev to validate your license status.
- **Prepaid license**. Pay upfront for 3-12 months and enjoy completely offline operation. Uptrace won't make any external requests with this license type.

Please note that both license types are tied to the specific domain you provide during license creation. This domain will automatically override the `site.url` setting in your Uptrace configuration.

## Managed Edition

Our managed edition includes everything you need to get started:

- **Free one-month trial**. Explore all our features with no commitment.
- **Personalized configuration**. Custom indexing and pre-aggregation rules tailored specifically to your requirements.
- **Comprehensive support**. Start with our standard 16/5 assistance, with the flexibility to upgrade to 24/7 coverage. Reach us through tickets, Slack, or email â whatever works best for your team

Our support team will guide you through:

- **Seamless onboarding**. Complete OpenTelemetry setup and configuration for Uptrace.
- **Custom dashboard creation**. Build monitoring views that match your workflow.
- **Integration setup**. Configure all your essential tools including PagerDuty, Opsgenie, Okta, SAML, OIDC, and more.

We handle all scaling and maintenance to ensure 99.95% availability. Please note that our uptime is inherently limited by your hosting provider's [performance](https://awsmaniac.com/aws-outages/) â if your cloud provider experiences downtime, it will affect Uptrace as well.

## Still have questions?

To learn more, feel free to [contact](mailto:support@uptrace.dev) support or [schedule](https://calendly.com/vmihailenco/30min) a call.
