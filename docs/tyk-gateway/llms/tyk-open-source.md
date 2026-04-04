# Source: https://tyk.io/docs/tyk-open-source.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk Open Source

> This page serves as a comprehensive guide to Tyk Open Source

export const linkStyle = {
  fontWeight: 'normal',
  textDecoration: 'none',
  borderBottom: 'none',
  color: 'rgb(var(--primary))',
  transition: 'border-bottom 0.2s ease'
};

export const handleMouseEnter = e => {
  e.target.style.borderBottom = '1px solid rgb(var(--primary))';
};

export const handleMouseLeave = e => {
  e.target.style.borderBottom = 'none';
};

## What is Tyk Open Source

Open source is at the heart of what we do. Anything that is API Gateway-related lives in the Gateway, or is critical for the Gateway to work is open and freely available via our [Github](https://github.com/TykTechnologies/tyk).

The Tyk Gateway is fully open-source.  It's all the same Gateway that's used by you (the community!), by our enterprise products, as well as our SaaS.

Our commitment to open source also delivers a host of benefits for our users: sign up for free with Tyk, receive securely packaged open source packages, get started guides, access to our community and all of the latest open source information.

<Note>
  Tyk OSS, Tyk Open Source, Tyk Gateway, Tyk CE
</Note>

<img src="https://mintcdn.com/tyk/SM-tkHpBDkTR2XlA/img/diagrams/oss-flow.png?fit=max&auto=format&n=SM-tkHpBDkTR2XlA&q=85&s=a94c28cc9bc258925b89ceed14411710" alt="OSS-Guide" width="582" height="631" data-path="img/diagrams/oss-flow.png" />

## What Does Tyk Open Source Include?

The Tyk Team has created and maintains the following components, which are fully Open Source and available under Mozilla Public License 2.0 (MPL). Star the Tyk components you use by clicking the appropriate button:

<Columns cols={2}>
  <Card title="Tyk Gateway" href="https://github.com/TykTechnologies/tyk" cta="⭐️ Github" arrow={true}>
    Fully fledged API Gateway.

    <a href="/tyk-oss-gateway" style={linkStyle} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>Learn more</a>
  </Card>

  <Card title="Tyk Pump" href="https://github.com/TykTechnologies/tyk-pump" cta="⭐️ Github" arrow={true}>
    Send API analytics data to your chosen backend.

    <a href="/api-management/tyk-pump" style={linkStyle} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>Learn more</a>
  </Card>

  <Card title="Tyk Identity Broker" href="https://github.com/TykTechnologies/tyk-identity-broker" cta="⭐️ Github" arrow={true}>
    Connect your third-party IdP systems.

    <a href="/api-management/external-service-integration#what-is-tyk-identity-broker-tib" style={linkStyle} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>Learn more</a>
  </Card>

  <Card title="Tyk Helm Chart" href="https://github.com/TykTechnologies/tyk-charts" cta="⭐️ Github" arrow={true}>
    Deploy Tyk in K8S.

    <a href="/product-stack/tyk-charts/overview" style={linkStyle} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>Learn more</a>
  </Card>
</Columns>

MPL is a copyleft license that is easy to comply with. You must make the source code for any of your changes available under MPL, but you can combine the MPL software with proprietary code, as long as you keep the MPL code in separate files. Version 2.0 is, by default, compatible with LGPL and GPL version 2 or greater. You can distribute binaries under a proprietary license, as long as you make the source available under MPL. This is just a brief overview of MPL, you should refer to the MPL license in full and if you are in any doubt about how this license impacts you, please contact us to discuss.

You can find additional FAQs regarding the MPL license [here](https://www.mozilla.org/en-US/MPL/2.0/FAQ/).

Built with [Mintlify](https://mintlify.com).
