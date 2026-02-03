# Source: https://docs.asapp.com/generativeagent/integrate/sip-transfers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SIP Transfers

> Choose between API-based or SIP headers approaches for integrating GenerativeAgent with SIP

ASAPP's SIP Transfers enable businesses to integrate GenerativeAgent Voice using Session Initiation Protocol (SIP) instead of traditional phone numbers. This approach provides more control over the call flow and can be more cost-effective for certain use cases.

We have dedicated connector integrations for some platforms ([Genesys](/generativeagent/integrate/genesys-audiohook), [Amazon Connect](/generativeagent/integrate/amazon-connect)), but not every platform allows native integrations. SIP transfers allow you to use SIP protocol to connect your users to GenerativeAgent while keeping you in control of the call the entire time.

## Choose Your Integration Approach

<CardGroup cols={2}>
  <Card title="API-based Transfers" href="/generativeagent/integrate/sip-transfers-api" icon="code">
    **For rich context data**

    * Unlimited context data via API calls
    * Requires API integration
  </Card>

  <Card title="SIP Headers Transfer" href="/generativeagent/integrate/sip-transfers-headers" icon="phone">
    **For basic context data**

    * Context in SIP headers (1024 char limit)
    * No API calls needed
  </Card>
</CardGroup>

## SIP Requirements

ASAPP uses Twilio as our telephony provider. To ensure successful integration, your SIP infrastructure must meet the following requirements when transferring calls to GenerativeAgent:

### Network Configuration

**Media IP Range**: Twilio voice media uses the global IP range `168.86.128.0/18` with UDP ports `10000-60000`. Configure your firewall to allow traffic from this range.

**Codec Support**: Twilio supports the following audio codecs for media transmission:

* G.711 μ-law (PCMU)
* G.711 A-law (PCMA)

### Security

**TLS Encryption**: We strongly recommend using Transport Layer Security (TLS) for SIP signaling. Twilio uses signed certificates and supports specific TLS ciphers. For detailed TLS configuration requirements, refer to the [Twilio SIP interface documentation](https://www.twilio.com/docs/voice/api/sip-interface#securing-sip-traffic-using-tls).

<Warning>
  Ensure your SIP infrastructure can handle the specified IP range and port requirements. Firewall misconfigurations are a common cause of connection failures.
</Warning>

## Next Steps

Choose your preferred integration approach above to get started with implementation.
