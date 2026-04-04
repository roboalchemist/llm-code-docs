# Source: https://docs.asapp.com/ai-productivity/ai-transcribe.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Transcribe

> Transcribe your audio with best in class accuracy

<Frame>
  <img src="https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=379f9beb474d6dc61545b53f38dafac8" data-og-width="2112" width="2112" data-og-height="891" height="891" data-path="images/autotranscribe/aitranscribe-home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?w=280&fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=9640573f9aedf00374b068172f32300a 280w, https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?w=560&fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=5b07df1eba29970fe3ddb1eee5e1da89 560w, https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?w=840&fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=8872259057b3bb655716ba97946909b3 840w, https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?w=1100&fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=e541d8c6722c2898b36b6a35b65eb3dc 1100w, https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?w=1650&fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=367db1bb9d3fe4b4070a217f495988b0 1650w, https://mintcdn.com/asapp/aCHMKq7AVTQocNEN/images/autotranscribe/aitranscribe-home.png?w=2500&fit=max&auto=format&n=aCHMKq7AVTQocNEN&q=85&s=6fe59a8196b7b317429f9db8d3efcfd2 2500w" />
</Frame>

ASAPP AI Transcribe converts speech to text in real-time for live call audio streams and audio recordings.

Use AI Transcribe for voice interactions between contact center agents and their customers, in support of a broad range of use cases including real-time guidance, topical analysis, coaching, and quality management

A speech recognition model that transforms spoken form to written forms in real-time powers ASAPP's AI Transcribe service, along with punctuation and capitalization. To optimize performance, you can customize the model to support domain-specific needs by training on historical call audio and adding custom vocabulary to further boost recognition accuracy.

## How it Works

A speech recognition model that transforms spoken form to written forms in real-time powers ASAPP's AI Transcribe service, along with punctuation and capitalization.

To optimize performance, you can customize the model to support domain-specific needs by training on historical call audio and adding custom vocabulary to further boost recognition accuracy

ASAPP designed AI Transcribe to be fast enough to show an agent what was said immediately after every utterance.

You can implement AI Transcribe in three main integration patterns:

1. **WebSocket API**: All audio streaming, call signaling, and returned transcripts use a WebSocket API, preceded by an authentication mechanism that uses a REST API.
2. **SIPREC Media Gateway**: The ASAPP media gateway receives audio streaming, and a dedicated API receives call signaling; the system returns transcripts either in real-time or post-call.
3. **Third-Party CCaaS**: A third-party contact center as a service (CCaaS) vendor sends audio to the ASAPP media gateway, and an API sends call signaling; the system returns transcripts either in real-time or post-call.

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
