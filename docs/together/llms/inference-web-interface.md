# Source: https://docs.together.ai/docs/inference-web-interface.md

# Playground

> Guide to using Together AI's web playground for interactive AI model inference across chat, image, video, audio, and transcribe models.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=32e0ec9eaa26cddc360564de6445c3c7" alt="" data-og-width="2916" width="2916" data-og-height="2276" height="2276" data-path="images/guides/47.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f4e2e510c437e43081112e8400bb440e 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=84f808f3a40a73d4a9d5eef2d7206876 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=608c4badaaf5a622288b3dd3eb5ff0e6 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=96d66ef9d9fabb9b55517f9b2ec49b4a 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d115ed41a431ba5d035115547c0b880e 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c7e7e2ae253943d76faf71edaa0ce5b4 2500w" />
</Frame>

There are five playgrounds for interacting with different types of models:

1. **Chat Playground**
   Chat with models like DeepSeek R1-0528 in a conversational interface. Adjust model behavior with system prompts.

2. **Image Playground**
   Create stunning images from text or from existing images using FLUX.1 \[schnell] or other image generations models. This playground can also be useful for using instruction-tuned models and providing few-shot prompts.

3. **Video Playground**
   Produce engaging videos with Kling 1.6 Standard and other advanced models from text prompts.

4. **Audio Playground**
   Generate lifelike audio for synthesis or editing from text using models like Cartesia Sonic 2.

5. **Transcribe Playground**
   Turn audio into text with Whisper large-v3 or other transcription models.

## Instructions

1. Log in to [api.together.xyz](https://api.together.xyz/playground) with your username and password
2. Navigate through the different playgrounds we offer using the left sidebar
3. Select a model (either one that we offer, or one you have fine-tuned yourself)
4. Adjust the modifications and parameters (more details below)

### Modifications

From the right side panel you can access **modifications** to control the stop sequence or system prompt. The stop sequence controls when the model will stop outputting more text. The system prompt instructs the model how to behave. There are several default system prompts provided and you can add your own. To edit a system prompt you added, hover over the prompt in the menu and click the pencil icon.

### Parameters

Edit inference parameter settings from the right side panel. For more information on how to set these settings see [inference parameters](/docs/inference-parameters).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt