# Source: https://docs.asapp.com/ai-productivity/ai-transcribe.md

# AI Transcribe

> Transcribe your audio with best in class accuracy

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=213209fe61701072b425563903f87554" data-og-width="1408" width="1408" data-og-height="594" height="594" data-path="images/autotranscribe/autotranscribe-home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=247963602b67975934e51ea3e577a3d4 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7d4259df4d0d08a1f47a43a68ff4aa1d 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=debbed2d71fd65eda485153f84a9046e 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8059454f1720301fe4f18d8dc4b3849b 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=780eecea2d8271cdc226a1c4c83cd882 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autotranscribe/autotranscribe-home.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=afaee730bbb96c708a6e8c4bfc77af4c 2500w" />
</Frame>

ASAPP AI Transcribe converts speech to text in real-time for live call audio streams and audio recordings.

Use AI Transcribe for voice interactions between contact center agents and their customers, in support of a broad range of use cases including real-time guidance, topical analysis, coaching, and quality management

ASAPP's AI Transcribe service is powered by a speech recognition model that transforms spoken form to written forms in real-time, along with punctuation and capitalization. To optimize performance, the model can be customized to support domain-specific needs by training on historical call audio and adding custom vocabulary to further boost recognition accuracy.

## How it Works

ASAPP's AI Transcribe service is powered by a speech recognition model that transforms spoken form to written forms in real-time, along with punctuation and capitalization.

To optimize performance, the model can be customized to support domain-specific needs by training on historical call audio and adding custom vocabulary to further boost recognition accuracy

AI Transcribe was also designed to be fast enough to show an agent what was said immediately after every utterance.

AI Transcribe can be implemented in three main integration patterns:

1. **WebSocket API**: All audio streaming, call signaling, and returned transcripts use a WebSocket API, preceded by an authentication mechanism using a REST API.
2. **IPREC Media Gateway**: Audio streaming sent to ASAPP media gateway and call signaling sent via a dedicated API; transcripts are returned either in real-time or post call.
3. **Third Party CCaaS**: Audio is sent to ASAPP media gateway by a third party contact center as a service (CCaaS) vendor and call signaling sent via API; transcripts are returned either in real-time or post call.

<Card title="AI Transcribe Product Guide" href="/ai-productivity/ai-transcribe/product-guide">Learn more about AI Transcribe in the Product Guide</Card>

## Get Started

To get started with AI Transcribe, you need to:

1. Follow the [Developer Quickstart](/getting-started/developers) to get your API Credentials
2. Choose the integration that best fits your use case:

### Platform Connectors

<CardGroup>
  <Card title="Media Gateway: SIPRec" href="/ai-productivity/ai-transcribe/siprec">Transcribe audio from your SIPRec system using the ASAPP Media Gateway</Card>
  <Card title="Media Gateway: Twilio" href="/ai-productivity/ai-transcribe/twilio">Transcribe audio from your Twilio system using the ASAPP Media Gateway</Card>
  <Card title="Media Gateway: Amazon Connect" href="/ai-productivity/ai-transcribe/amazon-connect">Transcribe audio from your Amazon Connect system using the ASAPP Media Gateway</Card>
  <Card title="Media Gateway: Genesys" href="/ai-productivity/ai-transcribe/genesys-audiohook">Transcribe audio from your Genesys system using the ASAPP Media Gateway</Card>
</CardGroup>

### Direct Integration

<Card title="Direct WebSocket" href="/ai-productivity/ai-transcribe/direct-websocket">Use a websocket to send audio directly to AI Transcribe and receive the transcriptions</Card>

## Next Steps

<CardGroup>
  <Card title="AI Transcribe Product Guide" href="/ai-productivity/ai-transcribe/product-guide">Learn more about AI Transcribe in the Product Guide</Card>
  <Card title="Developer Quickstart" href="/getting-started/developers">Get started with the Developer Quickstart Guide</Card>
  <Card title="Feature Releases" href="/ai-productivity/ai-transcribe/feature-releases">See a list of feature releases for AI Transcribe</Card>
</CardGroup>
