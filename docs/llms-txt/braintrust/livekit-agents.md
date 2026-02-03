# Source: https://braintrust.dev/docs/integrations/agent-frameworks/livekit-agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LiveKit Agents

[LiveKit Agents](https://livekit.io/) is a framework for building real-time voice and video AI applications. Braintrust traces LiveKit Agents applications using OpenTelemetry to capture voice interactions, agent sessions, and realtime model usage.

## Setup

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" livekit-agents livekit-plugins-openai opentelemetry-sdk
  ```

  ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add @braintrust/otel @livekit/agents @livekit/agents-plugin-openai @livekit/agents-plugin-silero @opentelemetry/sdk-trace-node @opentelemetry/resources @opentelemetry/semantic-conventions dotenv
  # npm
  npm install @braintrust/otel @livekit/agents @livekit/agents-plugin-openai @livekit/agents-plugin-silero @opentelemetry/sdk-trace-node @opentelemetry/resources @opentelemetry/semantic-conventions dotenv
  ```
</CodeGroup>

<Note>
  The `@braintrust/otel` package supports both OpenTelemetry v1 and v2. For the best experience, use the same OpenTelemetry versions that LiveKit Agents uses to avoid compatibility issues.
</Note>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:livekit-demo
OPENAI_API_KEY=your-openai-api-key
```

## Trace with LiveKit Agents

Configure Braintrust's span processor and set it as LiveKit's tracer provider.

<CodeGroup dropdown>
  ```python title="livekit_agent.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust.otel import BraintrustSpanProcessor
  from livekit import agents
  from livekit.agents import Agent, AgentSession, RoomInputOptions
  from livekit.agents.telemetry import set_tracer_provider
  from livekit.plugins import noise_cancellation, openai
  from opentelemetry.sdk.trace import TracerProvider

  def setup_braintrust_telemetry():
      """Setup Braintrust OTEL telemetry for agent monitoring"""
      trace_provider = TracerProvider()
      trace_provider.add_span_processor(BraintrustSpanProcessor())
      set_tracer_provider(trace_provider)

  class Assistant(Agent):
      def __init__(self) -> None:
          super().__init__(instructions="You are a helpful voice AI assistant.")

  async def entrypoint(ctx: agents.JobContext):
      # Setup telemetry
      setup_braintrust_telemetry()

      # Create agent session with OpenAI realtime model
      session = AgentSession(llm=openai.realtime.RealtimeModel(voice="coral"))

      # Start session with assistant agent
      await session.start(
          room=ctx.room,
          agent=Assistant(),
          room_input_options=RoomInputOptions(
              noise_cancellation=noise_cancellation.BVC(),
          ),
      )

  # Run script locally with `python livekit_agent.py console`
  if __name__ == "__main__":
      agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
  ```

  ```typescript title="livekit_agent.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import "dotenv/config.js";
  import { fileURLToPath } from "url";
  import { BraintrustSpanProcessor, setupOtelCompat } from "@braintrust/otel";
  import {
    cli,
    defineAgent,
    JobContext,
    JobProcess,
    ServerOptions,
    telemetry,
    voice,
  } from "@livekit/agents";
  import * as openai from "@livekit/agents-plugin-openai";
  import * as silero from "@livekit/agents-plugin-silero";
  import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
  import { Resource } from "@opentelemetry/resources";
  import {
    ATTR_SERVICE_NAME,
    ATTR_SERVICE_VERSION,
  } from "@opentelemetry/semantic-conventions";

  function setupBraintrustTelemetry() {
    // Setup OTEL compatibility for bidirectional interoperability
    setupOtelCompat();

    // Create BraintrustSpanProcessor with configuration
    const spanProcessor = new BraintrustSpanProcessor({
      apiKey: process.env.BRAINTRUST_API_KEY,
      apiUrl: process.env.BRAINTRUST_API_URL,
      parent: process.env.BRAINTRUST_PARENT,
      filterAISpans: true,
    });

    const provider = new NodeTracerProvider({
      resource: new Resource({
        [ATTR_SERVICE_NAME]: "livekit-agent",
        [ATTR_SERVICE_VERSION]: "1.0.0",
      }),
      spanProcessors: [spanProcessor as any],
    });

    // Register the provider with OpenTelemetry's global API
    provider.register();

    // Configure LiveKit to use our tracer provider
    telemetry.setTracerProvider(provider, {
      metadata: {
        component: "livekit-agent",
      },
    });
  }

  export default defineAgent({
    prewarm: async (proc: JobProcess) => {
      proc.userData.vad = await silero.VAD.load();
    },
    entry: async (ctx: JobContext): Promise<void> => {
      // Setup telemetry
      setupBraintrustTelemetry();

      const session = new voice.AgentSession({
        vad: ctx.proc.userData.vad! as silero.VAD,
        stt: new openai.STT({ model: "whisper-1" }),
        tts: new openai.TTS({ voice: "coral" }),
        llm: new openai.realtime.RealtimeModel({
          model: "gpt-realtime",
          voice: "coral",
          temperature: 0.8,
          turnDetection: null,
        }),
      });

      await session.start({
        agent: new voice.Agent({
          instructions: `You are a helpful and friendly voice AI assistant`,
        }),
        room: ctx.room,
      });

      // Greet participant when they join
      const greetParticipant = async () => {
        session.say("Hello! I'm your voice assistant. How can I help you today?");
      };

      let greeted = ctx.room.remoteParticipants.size > 0;
      if (greeted) greetParticipant();

      ctx.room.once("participantConnected", () => {
        if (!greeted) {
          greeted = true;
          greetParticipant();
        }
      });

      // Wait for room to disconnect
      function waitForRoomDisconnect(room: typeof ctx.room) {
        return new Promise<void>((resolve) => {
          room.once("disconnected", () => resolve());
        });
      }

      await waitForRoomDisconnect(ctx.room);
    },
  });

  // Run the agent
  cli.runApp(
    new ServerOptions({
      agent: fileURLToPath(import.meta.url),
    })
  );
  ```
</CodeGroup>

The `BraintrustSpanProcessor` automatically captures all LiveKit agent spans, including:

* Voice interactions and audio processing
* OpenAI Realtime API calls
* Agent session lifecycle events
* Custom spans you create with `tracer.start_as_current_span()` (Python) or `tracer.startActiveSpan()` (TypeScript)

You can add attributes to spans using `span.set_attribute()` (Python) or `span.setAttribute()` (TypeScript) to enrich your traces with custom metadata, making it easier to debug and analyze your agent's behavior in Braintrust.

## Next steps

Learn more about building with LiveKit Agents and tracing with Braintrust:

**LiveKit Agents**

* [LiveKit Agents Overview](https://docs.livekit.io/agents/) - Introduction to the LiveKit Agents framework
* [Building Voice Agents](https://docs.livekit.io/agents/build/overview/) - Guide to creating voice-enabled agents
* [Agent Plugins](https://docs.livekit.io/agents/plugins/overview/) - Available plugins for STT, TTS, and LLM providers
* [Deployment Guide](https://docs.livekit.io/agents/deployment/) - Deploy your agents to production

**Braintrust Tracing**

* [OpenTelemetry Integration](/integrations/sdk-integrations/opentelemetry) - Deep dive into Braintrust's OpenTelemetry support
* [Custom Tracing Guide](/instrument/custom-tracing) - Add custom spans and attributes to your traces
* [Logging and Observability](/instrument/logging) - Monitor and debug your AI applications
