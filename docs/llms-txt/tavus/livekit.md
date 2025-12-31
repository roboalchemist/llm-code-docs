# Source: https://docs.tavus.io/sections/integrations/livekit.md

# LiveKit Agent

> Integrate a Tavus Replica into LiveKit as the conversational video avatar.

<Tip>
  We recommend using Tavus’s Full Pipeline in its entirety for the lowest latency and most optimized multimodal experience. Integrations like LiveKit Agent or Pipecat only provide rendering, while our Full Pipeline includes perception, turn-taking, and rendering for complete conversational intelligence. The Livekit integration also does not support interactions (“app messages”) like echo messages.
</Tip>

Tavus enables AI developers to create realistic video avatars powered by state-of-the-art speech synthesis, perception, and rendering pipelines. Through its integration with the <a href="https://docs.livekit.io/agents/" target="_blank">**LiveKit Agents**</a> application, you can seamlessly add conversational avatars to real-time voice AI systems.

## Prerequisites

Make sure you have the following before starting:

* <a href="https://platform.tavus.io/replicas" target="_blank">**Tavus `replica_id`**</a>
  * You can use <a href="https://platform.tavus.io/replicas" target="_blank">Tavus's stock Replicas</a> or your own custom replica.

- **LiveKit Voice Assistant Python App**
  * Your own existing application.
  * Or follow <a href="https://docs.livekit.io/agents/start/voice-ai/" target="_blank">LiveKit quickstart</a> to create one.

## Integration Guide

<Steps>
  <Step title="Step 1: Setup and Authentication">
    1. Install the plugin from PyPI:

    ```bash  theme={null}
    pip install "livekit-agents[tavus]~=1.0"
    ```

    2. Set `TAVUS_API_KEY` in your `.env` file.
  </Step>

  <Step title="Step 2: Configure Replica and Persona">
    1. Create a persona with LiveKit support using the Tavus API:

    ```bash {7, 10} theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/personas \
      -H "Content-Type: application/json" \
      -H "x-api-key: <api_key>" \
      -d '{
      "persona_name": "Customer Service Agent",
      "pipeline_mode": "echo",
      "layers": {
        "transport": {
                "transport_type": "livekit"
        }
      }
    }'
    ```

    <Note>
      * Replace `<api_key>` with your actual Tavus API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
      * Set `pipeline_mode` to `echo`.
      * Set `transport_type` to `livekit`.
    </Note>

    2. Save your the `persona_id`.
    3. Choose a replica from the [Stock Library](/sections/replica/stock-replicas) or browse available options on the <a href="https://platform.tavus.io/replicas" target="_blank" rel="noopener noreferrer">Developer Portal</a>.

    <Tip>
      We recommend using **Phoenix-3 PRO Replicas**, which are optimized for low-latency, real-time applications.
    </Tip>
  </Step>

  <Step title="Step 3: Add AvatarSession to AgentSession">
    In your LiveKit Python app, create a `tavus.AvatarSession` alongside your `AgentSession`:

    ```python {12-16, 18} theme={null}
    from livekit import agents
    from livekit.agents import AgentSession, RoomOutputOptions
    from livekit.plugins import tavus

    async def entrypoint(ctx: agents.JobContext):
        await ctx.connect()

        session = AgentSession(
            # Add STT, LLM, TTS, and other components here
        )

        avatar = tavus.AvatarSession(
            replica_id="your-replica-id",
            persona_id="your-persona-id",
            # Optional: avatar_participant_name="Tavus-avatar-agent"
        )

        await avatar.start(session, room=ctx.room)

        await session.start(
            room=ctx.room,
            room_output_options=RoomOutputOptions(
                audio_enabled=False  # Tavus handles audio separately
            )
        )
    ```

    | Parameter                                    | Description                                                                           |
    | -------------------------------------------- | ------------------------------------------------------------------------------------- |
    | `replica_id` (string)                        | ID of the Tavus replica to render and speak through                                   |
    | `persona_id` (string)                        | ID of the persona with the correct pipeline and transport configuration               |
    | `avatar_participant_name` (string, optional) | Display name for the avatar participant in the room. Defaults to `Tavus-avatar-agent` |
  </Step>
</Steps>

<Note>
  Try out the integration using this <a href="https://github.com/livekit-examples/python-agents-examples/tree/main/avatars/tavus" target="_blank">sample app</a>.
</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavus.io/llms.txt