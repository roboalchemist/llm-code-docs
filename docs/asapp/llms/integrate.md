# Source: https://docs.asapp.com/generativeagent/integrate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GenerativeAgent Integration Overview

> High-level guide to integrating GenerativeAgent with your systems - channel integration and backend connections

GenerativeAgent integration involves two main components that work together to create a complete conversational AI solution:

<CardGroup cols={2}>
  <Card title="Voice Channel Integration" icon="comments" href="#channel-integration-methods">
    Connect your voice channels to GenerativeAgent to enable real-time conversations with end users.
  </Card>

  <Card title="Backend System Connections" icon="database" href="#backend-system-connections">
    Connect your APIs and backend systems to GenerativeAgent so it can perform actions and access data on behalf of users.
  </Card>

  <Card title="Web SDK" icon="globe" href="/generativeagent/integrate/web-sdk">
    Add GenerativeAgent chat to your website with a customizable SDK that works alongside your existing chat systems.
  </Card>
</CardGroup>

## Channel Integration Methods

Channel integration is how conversation data is sent back and forth between the end user and GenerativeAgent. Connect your existing voice platform to enable real-time conversations.

## Call Transfers

Transfer calls to GenerativeAgent while maintaining control over the call flow. Transferring with SIP or PSTN works with virtually any voice platform.

<CardGroup>
  <Card title="SIP Transfers" href="/generativeagent/integrate/sip-transfers" icon="server">
    Transfer calls using SIP protocol with API-based or SIP headers approaches.
  </Card>

  <Card title="Transfer over PSTN" href="/generativeagent/integrate/call-transfer-pstn" icon="phone">
    Transfer calls using temporary phone numbers for maximum platform compatibility.
  </Card>
</CardGroup>

## Connectors

We support out-of-the-box connectors to enable GenerativeAgent on contact center platforms:

### Platform-Specific Voice Integration

Integration guides for popular voice platforms:

<CardGroup>
  <Card title="Amazon Connect" href="/generativeagent/integrate/amazon-connect">Step-by-step guide for integrating using AWS components.</Card>
  <Card title="Genesys Audiohook" href="/generativeagent/integrate/genesys-audiohook">One-click installation and configuration for Genesys Cloud.</Card>
  <Card title="Twilio Voice" href="/generativeagent/integrate/twilio-streams">Step-by-step guide for integrating Twilio Voice.</Card>
  <Card title="Zendesk Talk" href="/generativeagent/integrate/zendesk-talk">Step-by-step guide for integrating Zendesk Talk.</Card>
</CardGroup>

<Note>
  Don't see your platform? Let us know what platform you'd like us to build an integration for.
</Note>

### Web SDK

For web-based chat integrations, we provide a ready-to-use SDK:

<Card title="ASAPP SDK (Web)" href="/generativeagent/integrate/web-sdk">Quickly integrate GenerativeAgent chat into your website with our customizable web SDK. Works alongside existing chat systems like Salesforce Chat or Zendesk.</Card>

## Direct API

### Direct Voice Integration

Send conversation transcript directly to GenerativeAgent:

<Card title="Direct API Integration" href="/generativeagent/integrate/text-only-generativeagent">Send conversation transcript directly to GenerativeAgent using your own ASR or voice processing.</Card>

## Backend System Integrations

GenerativeAgent needs to interact with your business systems, but exposing APIs directly to LLMs often fail.

Most APIs are designed for **human developers** who can:

* read documentation
* experiment with trial and error
* get human support in order to get an API working.

**LLMs don't have the same luxury**, and instead make a single API request for a given action, only relying on its current context.

In order to have an **LLM successfully call an API**, we need to provide **simple** and **focused actions** instead of complex, inconsistent interfaces.

Our **API Connection** tooling enables you to define the specific interface to GenerativeAgent while using tooling to map it to the more complex underlying API.

<CardGroup cols={2}>
  <Card title="API Connections" icon="code" href="/generativeagent/configuring/connect-apis">
    Perform single, JSON API requests.

    Works for most modern APIs and SaaS platforms like Salesforce, HubSpot, and Zendesk.
  </Card>

  <Card title="Custom Code Connections" icon="terminal" href="/generativeagent/configuring/connect-apis/code-api-connections">
    Concatenate multiple API calls as one action

    API formats such as HTTP Form Posts and SOAP

    Complex business workflows
  </Card>
</CardGroup>

## Next Steps

<CardGroup>
  <Card title="Call Transfer over PSTN" href="/generativeagent/integrate/call-transfer-pstn">
    Learn how to connect your voice platform using Call Transfer over PSTN.
  </Card>

  <Card title="Connect your APIs" href="/generativeagent/configuring/connect-apis">
    Set up API connections and functions for your business systems.
  </Card>

  <Card title="Building a GenerativeAgent" href="/generativeagent/build-overview">
    Learn how GenerativeAgent works and the key components you'll configure.
  </Card>

  <Card title="Go Live" href="/generativeagent/go-live">
    Deploy your integration to production.
  </Card>
</CardGroup>
