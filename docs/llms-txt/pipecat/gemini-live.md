# Source: https://docs.pipecat.ai/server/services/s2s/gemini-live.md

# Source: https://docs.pipecat.ai/guides/features/gemini-live.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Building with Gemini Live

> Create real-time voice AI agents using Google's Gemini Live API and Pipecat

Gemini Live is Google's speech-to-speech API that enables natural, real-time voice conversations with AI. With Pipecat, you can build production-ready voice agents that leverage Gemini Live for telephony, web, and mobile applications.

<CardGroup cols={2}>
  <Card title="API Reference" icon="book" href="/server/services/s2s/gemini-live">
    Gemini Live service documentation
  </Card>

  <Card title="Pipecat CLI" icon="terminal" href="/cli/overview">
    Scaffold and deploy projects
  </Card>
</CardGroup>

## Capabilities

Pipecat's Gemini Live integration supports multiple modalities and deployment targets:

<CardGroup cols={2}>
  <Card title="Voice" icon="microphone">
    Real-time speech-to-speech conversations with natural turn-taking and voice activity detection
  </Card>

  <Card title="Vision" icon="eye">
    Process video and screenshare alongside audio for multimodal interactions
  </Card>

  <Card title="Telephony" icon="phone">
    Build phone-based voice agents with Twilio WebSocket integration
  </Card>

  <Card title="Tool Use" icon="wrench">
    Function calling support for external integrations and dynamic responses
  </Card>
</CardGroup>

### Architecture

Pipecat manages connections between your client and Gemini Live:

<Frame><img src="https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=af85a896b9d5d5d74b507492035ce543" alt="Gemini Live Architecture" data-og-width="2110" width="2110" data-og-height="484" height="484" data-path="images/gemini-live-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?w=280&fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=eefd4bbc48e1d83cf4b21d391db47fab 280w, https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?w=560&fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=5d059414d6a89ff3abf37e8cb350de30 560w, https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?w=840&fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=ebfcd44e5feefd35c8e39eb7ac2fb66d 840w, https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?w=1100&fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=720298eb0705ce18ef895beb6e651f2d 1100w, https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?w=1650&fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=535f1afd22b3e1ddcd290b8e9ce2d2bb 1650w, https://mintcdn.com/daily/jHf4uyQMOanEqe_B/images/gemini-live-architecture.png?w=2500&fit=max&auto=format&n=jHf4uyQMOanEqe_B&q=85&s=7ae2588872eee308dd9c9c14be4163fb 2500w" /></Frame>

The Pipecat server handles media streaming with clients via WebRTC (web/mobile) or WebSockets (telephony), while maintaining a persistent connection to Gemini Live for real-time AI processing.

## Quick Start

The fastest way to start building is with the Pipecat CLI:

```bash  theme={null}
# Install the CLI
uv tool install pipecat-ai-cli

# Create a new project
pipecat init
```

The CLI will guide you through selecting:

* **Bot type**: Gemini Live (speech-to-speech)
* **Transport**: Daily WebRTC, Twilio, or others
* **Deployment target**: Local development or Pipecat Cloud

<Tip>
  All CLI commands can use either `pipecat` or the shorter `pc` alias.
</Tip>

## Starter Projects

These complete examples demonstrate Gemini Live in production scenarios. Each includes local development setup and Pipecat Cloud deployment configuration.

### Phone Bot (Twilio)

A telephone-based voice agent using Gemini Live with Twilio WebSockets. The demo plays "Two Truths and a Lie" to showcase natural conversation flow.

<Card title="Phone Bot Starter" icon="phone" href="https://github.com/pipecat-ai/pipecat-examples/tree/main/gemini-live-starters/phone-bot">
  Build a production phone agent with Twilio integration
</Card>

**Try it now**: Call **1-970-LIVE-API** (1-970-548-3274) to talk to a live demo.

**What you'll learn**:

* Twilio WebSocket transport configuration
* Google STT/TTS integration alongside Gemini Live
* TwiML setup for incoming calls
* Pipecat Cloud deployment with telephony

### Web Bot (Vision)

A browser-based agent with screensharing and vision capabilities, built with the Pipecat Voice UI Kit and Daily WebRTC transport.

<Card title="Web Bot Starter" icon="browser" href="https://github.com/pipecat-ai/pipecat-examples/tree/main/gemini-live-starters/web-bot">
  Build a web agent with vision and screensharing
</Card>

**What you'll learn**:

* Daily WebRTC transport for web clients
* Vision/screenshare processing with Gemini Live
* Next.js client with Voice UI Kit components
* Resizable panels and event logging

## Deployment

Both starter projects include configuration for [Pipecat Cloud](/deployment/pipecat-cloud/introduction), which handles scaling, monitoring, and global deployment.

```bash  theme={null}
# Authenticate with Pipecat Cloud
pipecat cloud auth login

# Build and push your Docker image
pipecat cloud docker build-push

# Deploy your agent
pipecat cloud deploy
```

Each starter includes a `pcc-deploy.toml` file with sensible defaults for agent configuration and scaling.

<Card title="Pipecat Cloud Deployment" icon="cloud" href="/deployment/pipecat-cloud/fundamentals/deploy">
  Learn more about deploying to production
</Card>

## Next Steps

<CardGroup cols={2}>
  <Card title="Function Calling" icon="code" href="/guides/learn/function-calling">
    Add external integrations and dynamic responses
  </Card>

  <Card title="React Client SDK" icon="react" href="/client/react/introduction">
    Build custom web interfaces
  </Card>

  <Card title="Telephony Guide" icon="phone-volume" href="/deployment/pipecat-cloud/guides/telephony/twilio-websocket">
    Deep dive into phone integrations
  </Card>

  <Card title="Core Concepts" icon="graduation-cap" href="/guides/learn/overview">
    Understand Pipecat pipelines and processors
  </Card>
</CardGroup>
