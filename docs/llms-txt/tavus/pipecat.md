# Source: https://docs.tavus.io/sections/integrations/pipecat.md

# Pipecat

> Integrate a Tavus Replica into your Pipecat application as a participant or a video feed for the bot.

<Tip>
  We recommend using Tavus’s Full Pipeline in its entirety for the lowest latency and most optimized multimodal experience. Integrations like LiveKit Agent or Pipecat only provide rendering, while our Full Pipeline includes perception, turn-taking, and rendering for complete conversational intelligence.
</Tip>

Tavus offers integration with <a href="https://www.pipecat.ai/" target="_blank">Pipecat</a>, an open-source framework for building multimodal conversational agents by Daily. You can integrate Tavus into your Pipecat application in two ways:

* Additional Tavus Participant (`TavusTransport`)
  * The Tavus agent joins as a third participant alongside the Pipecat bot and human user. It receives audio from the Pipecat pipeline’s TTS layer and renders synchronized video and audio.
* Video Layer for Pipecat Bot (`TavusVideoService`)
  * Only the Pipecat bot is present in the room. `TavusVideoService` acts as a pipeline layer, sending TTS audio to Tavus in the background. Tavus returns video and audio streams for the bot to display. No additional participant is added.

## Prerequisites

Before integrating Tavus with Pipecat, ensure you have the following:

* <a href="https://platform.tavus.io/api-keys" target="_blank">**Tavus API Key**</a>

* <a href="https://platform.tavus.io/replicas" target="_blank">**Tavus `replica_id`**</a>
  * You can use one of <a href="https://platform.tavus.io/replicas" target="_blank">Tavus's stock replicas</a> or your own custom replica.

* **Pipecat Python Application**
  * Either your own existing application, or use Pipecat’s examples:
    * <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/foundational/21-tavus-transport.py" target="_blank">`TavusTransport`</a>
    * <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/foundational/21a-tavus-video-service.py" target="_blank">`TavusVideoService`</a>

## `TavusTransport`

`TavusTransport` connects your Pipecat app to a Tavus conversation, allowing the bot to join the same virtual room as the Tavus avatar and participants. To get started, you can follow the following steps or learn more from this <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/foundational/21-tavus-transport.py" target="_blank">sample code</a>.

### Integration Guide for `TavusTransport`

<Steps>
  <Step title="Step 1: Setup and Authentication">
    1. Install the Tavus plugin for Pipecat.

    ```sh  theme={null}
    pip install pipecat-ai[tavus]
    ```

    2. In the `.env` file of your pipecat application (at `/path/to/pipecat/.env`) add:

    ```env  theme={null}
    TAVUS_API_KEY=<api_key>
    TAVUS_REPLICA_ID=<your_replica_id>
    ```

    <Note>
      * Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.

      * Replace `<your_replica_id>` with the Replica ID you want to use.
    </Note>
  </Step>

  <Step title="Step 2: Create the Tavus transport layer">
    Create an instance of `TavusTransport` by providing your bot name, Tavus API key, Replica ID, session, and additional parameters.

    ```py {6, 16-27} theme={null}
    import os
    import aiohttp
    from dotenv import load_dotenv
    from loguru import logger
    from pipecat.audio.vad.silero import SileroVADAnalyzer
    from pipecat.transports.services.tavus import TavusParams, TavusTransport
    # Other imports...

    load_dotenv(override=True)

    logger.remove(0)
    logger.add(sys.stderr, level="DEBUG")

    async def main():
        async with aiohttp.ClientSession() as session:
            transport = TavusTransport(
                bot_name="Pipecat bot",
                api_key=os.getenv("TAVUS_API_KEY"),
                replica_id=os.getenv("TAVUS_REPLICA_ID"),
                session=session,
                params=TavusParams(
                    audio_in_enabled=True,
                    audio_out_enabled=True,
                    microphone_out_enabled=False,
                    vad_analyzer=SileroVADAnalyzer(),
                ),
            )

            # stt, tts, llm...
    ```

    <Note>
      See <a href="https://pipecat-docs.readthedocs.io/en/latest/api/pipecat.transports.services.tavus.html#tavus" target="_blank">Pipecat API Reference</a> for the configuration details.
    </Note>
  </Step>

  <Step title="Step 3: Insert the Tavus transport layer into the pipeline">
    Add the Tavus transport layer to your processing pipeline.

    ```py {5, 10} theme={null}
            # stt, tts, llm...

            pipeline = Pipeline(
                [
                    transport.input(),  # Transport user input
                    stt,  # STT
                    context_aggregator.user(),  # User responses
                    llm,  # LLM
                    tts,  # TTS
                    transport.output(),  # Transport bot output
                    context_aggregator.assistant(),  # Assistant spoken responses
                ]
            )
    ```
  </Step>

  <Step title="Step 4: Run the program">
    1. Run the following command to execute the program:

    ```sh  theme={null}
    python <file-name>.py
    ```

    <Note>
      Replace the `<file-name>` with your actual Python filename.
    </Note>

    2. Use the **Tavus Daily URL** provided in the console to interact with the agent.
  </Step>
</Steps>

## `TavusVideoService`

You can use `TavusVideoService` to enable real-time AI-driven video interactions in your Pipecat app. To get started, you can follow the following steps or refer from this <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/foundational/21a-tavus-video-service.py" target="_blank">sample code</a>.

### Integration Guide for `TavusVideoService`

<Steps>
  <Step title="Step 1: Setup and Authentication">
    1. Install the Tavus plugin for Pipecat.

    ```sh  theme={null}
    pip install pipecat-ai[tavus]
    ```

    2. In the `.env` file of your pipecat application (at `/path/to/pipecat/.env`) add:

    ```env  theme={null}
    TAVUS_API_KEY=<api_key>
    TAVUS_REPLICA_ID=<your_replica_id>
    ```

    <Note>
      * Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.

      * Replace `<your_replica_id>` with the Replica ID you want to use.
    </Note>
  </Step>

  <Step title="Step 2: Create the Tavus Video Service">
    Create an instance of `TavusVideoService` by providing your Tavus API key and Tavus Replica ID.

    ```py {6, 15-19} theme={null}
    import argparse
    import os
    import aiohttp
    from dotenv import load_dotenv
    from loguru import logger
    from pipecat.services.tavus.video import TavusVideoService
    from pipecat.transports.base_transport import BaseTransport
    # Other imports...

    load_dotenv(override=True)

    async def run_example(transport: BaseTransport, _: argparse.Namespace, handle_sigint: bool):
        logger.info(f"Starting bot")
        async with aiohttp.ClientSession() as session:
            tavus = TavusVideoService(
                api_key=os.getenv("TAVUS_API_KEY"),
                replica_id=os.getenv("TAVUS_REPLICA_ID"),
                session=session,
            )

            # stt, tts, llm...
    ```

    <Note>
      See <a href="https://docs.pipecat.ai/server/services/video/tavus" target="_blank">Pipecat Tavus Service</a> for the configuration details.
    </Note>
  </Step>

  <Step title="Step 3: Insert the Tavus Video Service into the timeline">
    Insert the `TavusVideoService` into the pipeline by adding the `tavus` service after the TTS processor in the pipeline.

    ```py {10} theme={null}
            # stt, tts, llm...

            pipeline = Pipeline(
                [
                    transport.input(),  # Transport user input
                    stt,  # STT
                    context_aggregator.user(),  # User responses
                    llm,  # LLM
                    tts,  # TTS
                    tavus,  # Tavus output layer
                    transport.output(),  # Transport bot output
                    context_aggregator.assistant(),  # Assistant spoken responses
                ]
            )
    ```
  </Step>

  <Step title="Step 4: Run the program">
    1. Run the following command to execute the program:

    ```sh  theme={null}
    python <file-name>.py
    ```

    <Note>
      Replace the `<file-name>` with your actual Python filename.
    </Note>

    2. Use the **localhost URL** provided in the console to interact with the agent.
  </Step>
</Steps>
