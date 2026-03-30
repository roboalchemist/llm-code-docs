# Source: https://tyk.io/docs/apim.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk API Management Deployment Options

> How to decide on which Tyk deployment option is best for you

export const ButtonLeft = ({href, color, content}) => {
  const buttonStyle = {
    display: 'inline-block',
    padding: '5px 16px',
    fontSize: '14px',
    fontWeight: '500',
    textDecoration: 'none',
    borderRadius: '25px',
    transition: 'all 0.2s ease',
    cursor: 'pointer',
    border: '1.2px solid black'
  };
  const colorStyles = {
    green: {
      backgroundColor: '#20EDBA',
      color: 'black'
    },
    red: {
      backgroundColor: '#dc2626',
      color: 'white'
    },
    black: {
      backgroundColor: '#1f2937',
      color: 'white'
    }
  };
  const hoverStyle = {
    transform: 'translateY(-1px)',
    boxShadow: '0 4px 8px rgba(0,0,0,0.15)'
  };
  const finalStyle = {
    ...buttonStyle,
    ...colorStyles[color] || colorStyles.black
  };
  return <a href={href} style={finalStyle} onMouseEnter={e => {
    Object.assign(e.target.style, hoverStyle);
  }} onMouseLeave={e => {
    e.target.style.transform = 'translateY(0)';
    e.target.style.boxShadow = 'none';
  }}>
      {content}
    </a>;
};

Tyk API Platform offers various deployment options, consisting of both [open source and proprietary](/tyk-stack)
components.

Choosing the right one for your organization depends on your specific requirements and preferences.
<br />Don’t hesitate to contact us for assistance <ButtonLeft href="https://tyk.io/contact/" color="green" content="Contact us" />

|                                                                                                                                                                                                            | [Open Source](/tyk-open-source) | [Self-Managed](/tyk-self-managed/install) | [Cloud](https://account.cloud-ara.tyk.io/signup) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------- | ------------------------------------------------ |
| API Gateway Capabilities <br /> <ul><li>Rate Limiting</li><li>Authentication</li> <li>API Versioning</li><li>Granular Access Control</li><li>GraphQL</li>  <li>and [much more](/tyk-open-source)</li></ul> | ✅                               | ✅                                         | ✅                                                |
| [Version Control](/api-management/automations/sync) Integration                                                                                                                                            | -                               | ✅                                         | ✅                                                |
| [API Analytics Exporter](/api-management/tyk-pump)                                                                                                                                                         | ✅                               | ✅                                         | ✅                                                |
| [Tyk Dashboard](/api-management/dashboard-configuration)                                                                                                                                                   | -                               | ✅                                         | ✅                                                |
| [Single Sign On (SSO)](/api-management/external-service-integration#single-sign-on-sso)                                                                                                                    | -                               | ✅                                         | ✅                                                |
| [RBAC and API Teams](/api-management/user-management#)                                                                                                                                                     | -                               | ✅                                         | ✅                                                |
| [Universal Data Graph](/api-management/data-graph#overview)                                                                                                                                                | -                               | ✅                                         | ✅                                                |
| [Multi-Tenant](/api-management/dashboard-configuration#organizations)                                                                                                                                      | -                               | ✅                                         | ✅                                                |
| [Multi-Data Center](/api-management/mdcb#managing-geographically-distributed-gateways-to-minimize-latency-and-protect-data-sovereignty)                                                                    | -                               | ✅                                         | ✅                                                |
| [Developer Portal](/portal/overview/intro)                                                                                                                                                                 | -                               | ✅                                         | ✅                                                |
| [Developer API Analytics](/api-management/dashboard-configuration#traffic-analytics)                                                                                                                       | -                               | ✅                                         | ✅                                                |
| Hybrid Deployments                                                                                                                                                                                         | -                               | -                                         | ✅                                                |
| Fully-Managed SaaS                                                                                                                                                                                         | -                               | -                                         | ✅                                                |
| [HIPAA, SOC2, PCI](https://tyk.io/governance-and-auditing/)                                                                                                                                                | ✅                               | ✅                                         | -                                                |

## Licensing

### Self-managed (On-Prem)

Tyk Self-Managed is the easiest way to install Tyk Full Lifecycle API Management solution in your infrastructure. There is no calling home, and there are no usage limits. You have complete control.

You can quickly [get started](/getting-started/quick-start) with a self-managed trial license by completing the registration on our [website](https://tyk.io/self-managed-trial). After registering, you’ll receive an email containing your license key.

To continue using Tyk Self-Managed after your trial, please contact our [team](https://tyk.io/contact/) to discuss licensing options.

<ButtonLeft href="https://tyk.io/contact/" color="green" content="Contact us" />

If you'd rather have guided assistance, we recommend checking out our [Tyk Technical PoC Guide](https://tyk.io/customer-engineering/poc/technical-guide/).

### Cloud (Software as a Service / SaaS)

Tyk cloud is a fully managed service that makes it easy for API teams to create, secure, publish and maintain APIs at any scale, anywhere in the world. Tyk Cloud includes everything you need to manage your global API ecosystem.

Get your free account [here](https://tyk.io/sign-up/).

### Open Source (OSS)

The Tyk Gateway is the backbone of all our solutions and can be deployed for free, forever. It offers various [installation options](/apim/open-source/installation) to suit different needs.

Visit the [OSS section](/tyk-open-source) for more information on it and other open source components.

Explore the various open and closed source [Tyk components](/tyk-stack) that are part of the Tyk platform solutions.


Built with [Mintlify](https://mintlify.com).