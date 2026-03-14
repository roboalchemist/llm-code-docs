# Source: https://docs.together.ai/docs/inference-web-interface.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Playground

> Guide to using Together AI's web playground for interactive AI model inference across chat, image, video, audio, and transcribe models.

There are five playgrounds for interacting with different types of models:

1. **Chat Playground** Chat with models like DeepSeek R1-0528 in a conversational interface. Adjust model behavior with system prompts.
2. **Image Playground** Create stunning images from text or from existing images using FLUX.1 \[schnell] or other image generations models. This playground can also be useful for using instruction-tuned models and providing few-shot prompts.
3. **Video Playground** Produce engaging videos with Kling 1.6 Standard and other advanced models from text prompts.
4. **Audio Playground** Generate lifelike audio for synthesis or editing from text using models like Cartesia Sonic 2.
5. **Transcribe Playground** Turn audio into text with Whisper large-v3 or other transcription models.

## Instructions

1. Log in to [api.together.xyz](https://api.together.xyz/playground) with your username and password
2. Navigate through the different playgrounds we offer using the left sidebar
3. Select a model (either one that we offer, or one you have fine-tuned yourself)
4. Adjust the modifications and parameters (more details below)

### Modifications

From the right side panel you can access **modifications** to control the stop sequence or system prompt. The stop sequence controls when the model will stop outputting more text. The system prompt instructs the model how to behave. There are several default system prompts provided and you can add your own. To edit a system prompt you added, hover over the prompt in the menu and click the pencil icon.

### Parameters

Edit inference parameter settings from the right side panel. For more information on how to set these settings see [inference parameters](/docs/inference-parameters)


Built with [Mintlify](https://mintlify.com).