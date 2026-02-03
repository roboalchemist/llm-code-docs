# Source: https://docs.tavus.io/sections/conversational-video-interface/faq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs

> Frequently asked questions about Tavus's Conversational Video Interface.

<AccordionGroup>
  <Accordion title="Memories">
    <AccordionGroup>
      <Accordion title="What are Memories, and how do they work?">
        Memories allow AI Personas to remember context across turns and understand time and dates, making conversations more coherent over longer interactions.

        Memories are enabled using a unique memory\_stores that acts as the memory key. Information collected during conversations is associated with this participant and can be referenced in future interactions.
      </Accordion>

      <Accordion title="Do Memories work across conversations?">
        Yes. Cross-conversation Memories are supported as part of this update.
      </Accordion>

      <Accordion title="What's the primary benefit of Memories?">
        It improves context retention, which is crucial for multi-turn tasks and long-term relationships between users and AI. It unlocks uses cases that progress over time like education or therapy, out of the box.
      </Accordion>

      <Accordion title="How do I enable Memories in the UI?">
        To enable Memories in the UI, you can either select an existing memory tag from the dropdown menu or type a new one to create it.
      </Accordion>

      <Accordion title="How do I enable Memories via the API?">
        Use the `memory_stores` field in the Create Conversation API call. This should be a stable, unique identifier for the user (e.g. user email, CRM ID, etc.). Example:

        ```json  theme={null}
        {
          "replica_id": "rb17cf590e15",
          "conversation_name": "Follow-up Chat",
          "memory_stores": ["user_123"]
        }
        ```

        Full example here: [Memories API Docs](/api-reference/conversations/create-conversation)
      </Accordion>

      <Accordion title="Can I see or edit the Memories data?">
        Not yet. Editing and reviewing Memories is not supported in this early release. Retrieval endpoints are under development and will be available in a future update.
      </Accordion>

      <Accordion title="Are Memories required for every conversation?">
        No. Memories are optional. If you don't include a memory\_stores, the AI Persona will behave statelessly—like a standard LLM—with no memory across sessions.
      </Accordion>

      <Accordion title="Can multiple participants share the same Memories?">
        No. Memories are tied to unique memory\_stores. Sharing this ID across users would cause memory crossover. Each participant should have their own ID to keep Memories clean and accurate.
      </Accordion>

      <Accordion title="What about customers who have already built their own Memories?">
        They can keep using their systems or integrate with Tavus Memories for more coherent, accurate conversations. Our memory is purpose-built for conversational video, retaining context across sessions with flexible scoping for truly personalized interactions.
      </Accordion>

      <Accordion title="In a situation where a user says, 'I said ABC,' but the AI Persona responded with 'DEF,' how can we investigate what was actually stored in Memories and understand why the AI Persona produced that response?">
        Today, we don't yet offer full visibility into what's stored in memory or how it was used in a given response.
      </Accordion>

      <Accordion title="For how long do Memories persist between interactions?">
        Memories are designed to persist indefinitely between interactions, allowing your AI persona to retain long-term context.
      </Accordion>

      <Accordion title="Where can I find more information about Memories?">
        Head to the [Memories Documentation site](https://docs.tavus.io/sections/conversational-video-interface/memories#api-setup).
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Knowledge Base">
    <AccordionGroup>
      <Accordion title="What is Knowledge Base and how does it work?">
        Knowledge Base is where users upload documents to enhance their AI persona capabilities using RAG (Retrieval-Augmented Generation). By retrieving information directly from these documents, AI personas can deliver more accurate, relevant, and grounded responses.
      </Accordion>

      <Accordion title="What happens during a conversation when using RAG?">
        Using RAG, the Knowledge Base system continuously:

        * Analyzes the conversation context
        * Retrieves relevant information from your document base
        * Augments the AI's responses with this contextual knowledge from your documents
      </Accordion>

      <Accordion title="How long does it take for knowledge to be retrieved?">
        With our industry-leading RAG, responses arrive in just 30 ms, up to 15× faster than other solutions. Conversations feel instant, natural, and friction-free.
      </Accordion>

      <Accordion title="What about customers who have already built their own Knowledge Base?">
        Yes, users can keep using their systems, but we strongly recommend they integrate with the Tavus Knowledge Base. Our Knowledge Base isn't just faster: it's the fastest RAG on the market, delivering answers in just 30 ms. That speed means conversations flow instantly, without awkward pauses or lagging. These interactions feel natural in a way user-built systems can't match.
      </Accordion>

      <Accordion title="Can you give an example of a Knowledge Base use case?">
        An AI recruiter can reference a candidate's resume uploaded via PDF and provide more accurate responses to applicant questions, using the resume content as grounding.
      </Accordion>

      <Accordion title="What's the customer value of Knowledge Base?">
        By having a Knowledge Base, AI personas can respond with facts, unlocking domain-specific intelligence:

        * Faster onboarding (just upload the docs)
        * More trustworthy answers, especially in regulated or high-stakes environments
        * Higher task completion for users, thanks to grounded knowledge
      </Accordion>

      <Accordion title="What formats are supported for upload?">
        Supported file types (uploaded to a publicly accessible URL like S3):

        * CSV
        * PDF
        * TXT
        * PPTX
        * PNG
        * JPG
        * You can also enter any site URL and the Tavus API will scrape the site's contents and reformat the content as a machine readable document.
      </Accordion>

      <Accordion title="Where can I find more information about Knowledge Base?">
        Head to the [Knowledge Base Documentation site](https://docs.tavus.io/sections/conversational-video-interface/knowledge-base).
      </Accordion>

      <Accordion title="Are there any access limitations when using a document ID?">
        Yes. Documents are linked to the API key that was used to upload them. To access a document later, you must use the same API key that was used to create it.
      </Accordion>

      <Accordion title="How do I use Knowledge Base through the API?">
        Once your documents have been uploaded and processed, include their IDs in your conversation request. Here's how:

        ```bash  theme={null}
        curl --location 'https://tavusapi.com/v2/conversations/' \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: '<API KEY>' \
        --data '{
            "persona_id": "<Persona ID>",
            "replica_id": "<Replica ID>",
            "document_ids": ["Document ID"]
        }'
        ```

        Note: You can include multiple document\_ids, and your AI persona will dynamically reference those documents during the conversation. You can also attach a document to a Persona.
      </Accordion>

      <Accordion title="How do I upload documents using API?">
        Upload files by providing a downloadable URL using the Create Documents endpoint. Tags are also supported for organization. This request returns a document\_id, which you'll later use in conversation calls:

        ```bash  theme={null}
        curl --location 'https://tavusapi.com/v2/documents/' \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: '<API Key>' \
        --data '{
            "document_url": "<publically accessible link>",
            "document_name": "slides_new.pdf",
            "tags": ["<tag-1>", "<tag-2>"]
        }'
        ```
      </Accordion>

      <Accordion title="What error codes might users encounter when uploading, accessing, or deleting documents, and what do they mean?">
        * `file_size_too_large` – File exceeds the maximum allowed upload size.
        * `file_format_unsupported` – This file type isn't supported for upload.
        * `invalid_file_url` – Provided file link is invalid or inaccessible.
        * `file_empty` – The uploaded file contains no readable content.
        * `website_processing_failed` – Website content could not be retrieved or processed.
        * `chunking_failed` – System couldn't split file into processable parts.
        * `embedding_failed` – Failed to generate embeddings for your file content.
        * `vector_store_failed` – Couldn't save data to the vector storage system.
        * `s3_storage_failed` – Error storing file in S3 cloud storage.
        * `contact_support` – An error occurred; please reach out for help.
      </Accordion>

      <Accordion title="How can I check the logs to see which document an AI persona referenced in a response to a customer?">
        Conversation.rag.observability tool call will be sent, which will fire if the conversational LLM decides to use any of the document chunks in its response, returning the document IDs and document names of the chunks
      </Accordion>

      <Accordion title="What are the document_retrieval_strategy options?">
        When creating a conversation with documents, you can optimize how the system searches through your knowledge base by specifying a retrieval strategy. This strategy determines the balance between search speed and the quality of retrieved information, allowing you to fine-tune the system based on your specific needs.

        You can choose from three different strategies:

        * **Speed**: Optimizes for faster retrieval times for minimal latency.
        * **Balanced (default)**: Provides a balance between retrieval speed and quality.
        * **Quality**: Prioritizes finding the most relevant information, which may take slightly longer but can provide more accurate responses.
      </Accordion>

      <Accordion title="How long does it take for documents to be uploaded and usable?">
        Maximum of 5 mins.
      </Accordion>

      <Accordion title="Do we support all languages for the knowledge base?">
        No. Currently, we only support documents written in English.
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Objectives and Guardrails">
    <AccordionGroup>
      <Accordion title="Objectives - What are they? How do they work?">
        Users need AI that can drive conversations to clear outcomes. With Objectives, users can now can define objectives with measurable completion criteria, branch automatically based on user responses, and track progress in real time. This unlocks workflows use-cases like Health Intakes, HR Interviews, and multi-step questionnaires.
      </Accordion>

      <Accordion title="How do I add Objectives to my Persona?">
        Objectives must be added or updated via API only. You cannot configure objectives during persona creation in the UI. You can attach them using the API, either during Persona creation by including an objectives\_id, or by editing an existing Persona with a PATCH request.
      </Accordion>

      <Accordion title="What use cases are Objectives good for?">
        Objectives are good for very templated one-off conversational use cases. For example, job interviews or health care intake, where there is a very defined path that the conversation should take. These kinds of use cases usually show up with our Enterprise API customers, where they have repetitive use cases at scale.

        More dynamic, free-flowing conversations usually do not benefit from have or enabling the Objectives feature. For example, talking with a Travel advisor where the conversation is very open ended, would usually not benefit from Objectives.

        Objectives are good for very defined workflows. Complex multi-session experiences don't fit current Objectives framework.
      </Accordion>

      <Accordion title="Where can I find more information about Objectives?">
        Head to the [Objectives Documentation site](https://docs.tavus.io/sections/conversational-video-interface/persona/objectives).
      </Accordion>

      <Accordion title="Guardrails - What are they? How do they work?">
        Guardrails help ensure your AI persona stays within appropriate boundaries and follows your defined rules during conversations.
      </Accordion>

      <Accordion title="How do I add Guardrails to my persona?">
        Guardrails must be added or updated via API only. You cannot configure guardrails during persona creation in the UI. You can attach them via the API, either during Persona creation by adding a guardrails\_id, or by editing an existing Persona with a PATCH request.
      </Accordion>

      <Accordion title="Can I create different Guardrails for different Personas?">
        Yes. You might have one set of Guardrails for a healthcare assistant to ensure medical compliance, and another for an education-focused Persona to keep all conversations age-appropriate.
      </Accordion>

      <Accordion title="Where can I find more information about Guardrails?">
        Head to the [Guardrails Documentation site](https://docs.tavus.io/sections/conversational-video-interface/persona/guardrails).
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="General Tavus Q&A">
    <AccordionGroup>
      <Accordion title="What are PALs?">
        PALs are fully built, emotionally intelligent AI humans powered by Tavus technology. They see, listen, remember, and take action across chat, voice, and video—offering lifelike, natural interaction out of the box. Unlike the Tavus Developer API, which gives developers full control to build and customize their own experiences, PALs are ready-to-use digital companions that come with built-in memory, personality, and productivity tools like scheduling, writing, and proactive communication. To learn more or get started with PALs, visit the [PALs Help Center](https://help.tavus.io).
      </Accordion>

      <Accordion title="What is Daily?">
        **Daily** is a platform that offers prebuilt video call apps and APIs, allowing you to easily integrate video chat into your web applications. You can embed a customizable video call widget into your site with just a few lines of code and access features like screen sharing and recording. **Tavus partners with Daily to power video conversations with our replicas.**
      </Accordion>

      <Accordion title="Do I need a Daily account?">
        * You **do not** need to sign up for a Daily account to use Tavus's Conversational Video Interface.
        * All you need is the Daily room URL (called `conversation_url` in our system) that is returned by the Tavus API. You can serve this link directly to your end users or embed it.
      </Accordion>

      <Accordion title="How do I embed the conversation using Daily's Prebuilt UI?">
        You can use Daily Prebuilt if you want a full-featured call UI and JavaScript control over the conversation. Once you have the Daily room URL (`conversation_url`) ready, replace `DAILY_ROOM_URL` in the code snippet below with your room URL.

        ```html  theme={null}
        <html>
          <script crossorigin src="https://unpkg.com/@daily-co/daily-js"></script>
          <body>
            <script>
              call = window.Daily.createFrame();
              call.join({ url: 'DAILY_ROOM_URL' });
            </script>
          </body>
        </html>
        ```

        That's it! For more details and options for embedding, check out <a href="https://docs.daily.co/guides/products/prebuilt#step-by-step-guide-embed-daily-prebuilt" target="_blank">Daily's documentation.</a> or [our implementation guides](https://docs.tavus.io/sections/integrations/embedding-cvi#how-can-i-reduce-background-noise-during-calls).
      </Accordion>

      <Accordion title="How do I embed the conversation using an iframe?">
        You can use an iframe if you just want to embed the conversation video with minimal setup. Once you have the Daily room URL (`conversation_url`) ready, replace `YOUR_TAVUS_MEETING_URL` in the iframe code snippet below with your room URL.

        ```html  theme={null}
        <html>
          <body>
            <iframe
              src="YOUR_TAVUS_MEETING_URL"
              allow="camera; microphone; fullscreen; display-capture"
              style="width: 100%; height: 500px; border: none;">
            </iframe>
          </body>
        </html>
        ```

        That's it! For more details and options for embedding, check out <a href="https://docs.daily.co/guides/products/prebuilt#step-by-step-guide-embed-daily-prebuilt" target="_blank">Daily's documentation.</a> or [our implementation guides](https://docs.tavus.io/sections/integrations/embedding-cvi#how-can-i-reduce-background-noise-during-calls).
      </Accordion>

      <Accordion title="How can I add custom LLM layers?">
        To add a custom LLM layer, you'll need the model name, base URL, and API key from your LLM provider. Then, include the LLM config in your `layers` field when creating a persona using the <a href="/api-reference/personas/create-persona" target="_blank">Create Persona API</a>. Example configuration:

        ```json {8-13} theme={null}
        {
          "persona_name": "Storyteller",
          "system_prompt": "You are a storyteller who entertains people of all ages.",
          "context": "Your favorite stories include Little Red Riding Hood and The Three Little Pigs.",
          "pipeline_mode": "full",
          "default_replica_id": "r665388ec672",
          "layers": {
            "llm": {
              "model": "gpt-3.5-turbo",
              "base_url": "https://api.openai.com/v1",
              "api_key": "your-api-key",
              "speculative_inference": true
            }
          }
        }
        ```

        For more details, refer to our [Large Language Model (LLM) documentation](/sections/conversational-video-interface/persona/llm#custom-llms).
      </Accordion>

      <Accordion title="How do I modify TTS voices?">
        You can integrate with third-party TTS providers by configuring the tts object in your persona. Supported engines include:

        * Cartesia
        * ElevenLabs

        Example configuration:

        ```json  theme={null}
        {
          "layers": {
            "tts": {
              "api_key": "your-tts-provider-api-key",
              "tts_engine": "cartesia",
              "external_voice_id": "your-voice-id",
              "voice_settings": {
                "speed": "normal",
                "emotion": ["positivity:high", "curiosity"]
              },
              "tts_emotion_control": true,
              "tts_model_name": "sonic"
            }
          }
        }
        ```

        For more details, read more on [our TTS documentation](/sections/conversational-video-interface/persona/tts).
      </Accordion>

      <Accordion title="How do I add call-back URLs?">
        You need to create a webhook endpoint that can receive POST requests from Tavus. This endpoint will receive the callback events for the visual summary after the conversation ended. Then, add `callback_url` property when creating the conversation

        ```sh {8} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
          "persona_id": "p596401c2cf9",
          "replica_id": "rf4703150052",
          "callback_url": "your_webhook_url"
        }'
        ```
      </Accordion>

      <Accordion title="How do I get transcripts for my conversation?">
        You need to create a webhook endpoint that can receive `POST` requests from Tavus. This endpoint will receive the callback events for the transcripts after the conversation ended. Then, add `callback_url` property when creating the conversation.

        ```sh {8} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
          "persona_id": "p596401c2cf9",
          "replica_id": "rf4703150052",
          "callback_url": "your_webhook_url"
        }'
        ```

        Your backend then will receive an event with properties `event_type = application.transcription_ready` when the transcript is ready.

        ```json application.transcription_ready [expandable] theme={null}
        {
          "properties": {
            "replica_id": "<replica_id>",
            "transcript": [
              {
                "role": "system",
                "content": "You are in a live video conference call with a user. You will get user message with two identifiers, 'USER SPEECH:' and 'VISUAL SCENE:', where 'USER SPEECH:' is what the person actually tells you, and 'VISUAL SCENE:' is what you are seeing when you look at them. Only use the information provided in 'VISUAL SCENE:' if the user asks what you see. Don't output identifiers such as 'USER SPEECH:' or 'VISUAL SCENE:' in your response. Reply in short sentences, talk to the user in a casual way.Respond only in english.   "
              },
              {
                "role": "user",
                "content": " Hello, tell me a story. "
              },
              {
                "role": "assistant",
                "content": "I've got a great one about a guy who traveled back in time.  Want to hear it? "
              },
              {
                "role": "user",
                "content": "USER_SPEECH:  Yeah I'd love to hear it.  VISUAL_SCENE: The image shows a close-up of a person's face, focusing on their forehead, eyes, and nose. In the background, there is a television screen mounted on a wall. The setting appears to be indoors, possibly in a public or commercial space."
              },
              {
                "role": "assistant",
                "content": "Let me think for a sec.  Alright, so there was this mysterious island that appeared out of nowhere,  and people started disappearing when they went to explore it.  "
              },
            ]
          },
          "conversation_id": "<your_conversation_id>",
          "webhook_url": "<your_webhook_url>",
          "message_type": "application",
          "event_type": "application.transcription_ready",
          "timestamp": "2025-02-10T21:30:06.141454Z"
        }
        ```
      </Accordion>

      <Accordion title="How do I get visual summary for my conversation?">
        You need to create a webhook endpoint that can receive `POST` requests from Tavus. This endpoint will receive the callback events for the visual summary after the conversation ended. Then, add `callback_url` property when creating the conversation.

        ```sh {8} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
          "persona_id": "p596401c2cf9",
          "replica_id": "rf4703150052",
          "callback_url": "your_webhook_url"
        }'
        ```

        Your backend then will receive an event with properties `event_type = application.perception_analysis` when the summary is ready.

        ```json application.perception_analysis theme={null}
        {
          "properties": {
            "analysis": "Here's a summary of the visual observations from the video call:\n\n*   **Overall Demeanor & Emotional State:** The user consistently appeared calm, collected, and neutral. They were frequently described as pensive, contemplative, or focused, suggesting they were often engaged in thought or listening attentively. No strong positive or negative emotions were consistently detected.\n\n*   **Appearance:**\n    *   The user is a young Asian male, likely in his early 20s, with dark hair.\n    *   He consistently wore a black shirt, sometimes specifically identified as a black t-shirt. One observation mentioned a \"1989\" print on the shirt.\n    *   He was consistently looking directly at the camera.\n\n*   **Environment:** The user was consistently in an indoor setting, most likely an office or home. Common background elements included:\n    *   White walls.\n    *   Windows or glass panels/partitions, often with black frames.\n    *   Another person was partially visible in the background for several observations.\n\n*   **Actions:**\n    *   The user was seen talking and gesturing with his hand in one observation, indicating he was actively participating in a conversation.\n\n*   **Ambient Awareness Queries:**\n    *   **Acne:** Acne was initially detected on the user's face in one observation, but later observations did not detect it. This suggests that acne may have been visible at one point but not throughout the entire call.\n    *   **Distress/Discomfort:** No signs of distress or discomfort were observed at any point during the call."
          },
          "conversation_id": "<your_conversation_id>",
          "webhook_url": "<your_webhook_url>",
          "message_type": "application",
          "event_type": "application.perception_analysis",
          "timestamp": "2025-06-19T06:57:32.480826Z"
        }
        ```
      </Accordion>

      <Accordion title="What LLM (Large Language Model) does Tavus use to power the conversational replicas?">
        Tavus offers flexibility in choosing the LLM (Large Language Model) to power your conversational replicas. You can either use one of Tavus's own models or bring your own!

        * **Tavus-Provided LLMs:** You can choose between three different models:
          * **`tavus-gpt-oss`:** The **default** choice if no LLM layer is provided.
          * **`tavus-gpt-4o`:** Another viable option for complex interactions.
          * **`tavus-gpt-4o-mini`:** Faster than `tavus-gpt-4o` at the slight cost of performance.

        * **No LLM Layer:** If you don't include an LLM layer, Tavus will automatically default to a Tavus-provided model.

        This allows you to tailor the conversational experience to your specific needs, whether you prioritize speed, intelligence, or a balance of both.
      </Accordion>

      <Accordion title="What is the maximum context window supported by the default LLM?">
        * The default LLM, `tavus-gpt-oss`, has a **limit of 32,000 tokens**.
        * Contexts over **25,000 tokens** will experience noticeable performance degradation (slower response times).

        <Tip>
          1 token ≈ 4 characters; therefore 32,000 tokens ≈ 128,000 characters (including spaces and punctuation).
        </Tip>
      </Accordion>

      <Accordion title="What are some recording tips for producing high quality conversational replica training footage?">
        When recording footage for training conversational replicas, here are some key tips to ensure high quality:

        1. **Minimal Head Movement:** Aim to keep your head and body as still as possible during the recording. This helps in maintaining consistency and improves the overall quality of the training data.
        2. **Pause and Be Still:** It's recommended to stop, stay still, and remain silent for at least 5 seconds at regular intervals throughout the script. These pauses are crucial for helping the replica appear natural during moments of silence in a conversation.
        3. **Use a Laptop Camera:** Recording on a laptop camera, as if you were on a Zoom call, often yields the most natural results. This setup mimics a familiar conversational setting, enhancing the naturalness of the footage.
      </Accordion>

      <Accordion title="How do I add perception tool calls?">
        You can configure perception tools in the `layers.perception` object when creating a persona:

        ```json [expandable] theme={null}
        {
          "layers": {
            "perception": {
              "perception_model": "raven-0",
              "ambient_awareness_queries": [
                "Is the user showing an ID card?",
                "Is the user wearing a mask?"
              ],
              "perception_tool_prompt": "You have a tool to notify the system when an ID card is detected, named `notify_if_id_shown`. You MUST use this tool when a bright outfit is detected.",
              "perception_tools": [
                {
                  "type": "function",
                  "function": {
                    "name": "notify_if_id_shown",
                    "description": "Use this function when a drivers license or passport is detected in the image with high confidence",
                    "parameters": {
                      "type": "object",
                      "properties": {
                        "id_type": {
                          "type": "string",
                          "description": "best guess on what type of ID it is"
                        }
                      },
                      "required": ["id_type"]
                    }
                  }
                }
              ]
            }
          }
        }
        ```

        Or modify perception tools using the [Update Persona API](/api-reference/personas/patch-persona):

        ```sh [expandable] theme={null}
        curl --request PATCH \
          --url https://tavusapi.com/v2/personas/{persona_id} \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api-key>' \
          --data '[
            {
              "op": "replace",
              "path": "/layers/perception/perception_tools",
              "value": [
                {
                  "type": "function",
                  "function": {
                    "name": "detect_glasses",
                    "description": "Trigger this function if the user is wearing glasses",
                    "parameters": {
                      "type": "object",
                      "properties": {
                        "glasses_type": {
                          "type": "string",
                          "description": "Type of glasses (e.g., reading, sunglasses)"
                        }
                      },
                      "required": ["glasses_type"]
                    }
                  }
                }
              ]
            }
          ]'
        ```

        Read more on this [page](/sections/conversational-video-interface/persona/perception)
      </Accordion>

      <Accordion title="Do I need to invite the replica to the meeting room?">
        No, it will automatically join as soon as it's ready!
      </Accordion>

      <Accordion title="For CVI, what's customizable vs. out of the box?">
        Out of the box, Tavus handles the complex backend infrastructure for you: LLMs, rendering, video delivery, and conversational intelligence are all preconfigured and production-ready.

        From there, nearly everything else is customizable:
        • What your AI Persona sees
        • How they look and sound
        • How they behave in conversation

        Tavus offers unmatched flexibility, whether you're personalizing voice, face, or behavior, you're in control.
      </Accordion>

      <Accordion title="How does Tavus deliver real-time responsiveness?">
        Tavus uses WebRTC to power real-time, face-to-face video interactions with extremely low latency.

        Unlike other platforms that piece together third-party tools, we built the entire pipeline (from LLM to rendering) to keep latency low and responsiveness high. Ironically, by minimizing reliance on multiple APIs, we've made everything faster.
      </Accordion>

      <Accordion title="What's behind the scenes of CVI?">
        Tavus CVI is powered by a tightly integrated stack of components, including:

        * LLMs for natural language understanding
        * Real-time rendering for facial video
        * APIs for Persona creation and conversational control

        You can explore key APIs here:
        • [Create a Persona](/api-reference/personas/create-persona)
        • [Create a Conversation](/api-reference/conversations/create-conversation)
      </Accordion>

      <Accordion title="How many languages does Tavus support?">
        Tavus supports over 30 spoken languages through a combination of Cartesia (our default TTS engine) and ElevenLabs. If a language isn't supported by Cartesia, Tavus automatically switches to ElevenLabs so your AI Persona can still speak fluently.

        Supported languages include English (all variants), French, German, Spanish, Portuguese, Chinese, Japanese, Hindi, Italian, Korean, Dutch, Polish, Russian, Swedish, Turkish, Indonesian, Filipino, Bulgarian, Romanian, Arabic, Czech, Greek, Finnish, Croatian, Malay, Slovak, Danish, Tamil, Ukrainian, Hungarian, Norwegian, and Vietnamese.

        View the [full supported language list](https://docs.tavus.io/sections/conversational-video-interface/language-support) for complete details and language-specific information.
      </Accordion>

      <Accordion title="Can Tavus support different accents or dialects?">
        Yes to accents. Not quite for regional dialects.

        When you generate a voice using Tavus, the system will default to the accent used in training. For example, if you provide Brazilian Portuguese as training input, the AI Persona will speak with a Brazilian accent. Tavus' TTS providers auto-detect and match accordingly.
      </Accordion>

      <Accordion title="What can Tavus do when it comes to orchestration (calendars, email tools, HubSpot, DocuSign, etc.)?">
        Tavus supports full orchestration through function calling. That means your AI persona can interact with external tools—calendar apps, CRMs, email systems, and more—based on your setup. Just define the function endpoints and let your AI persona take action.

        Bonus: As of August 11, 2025, Tavus also supports Retrieval-Augmented Generation (RAG), so your AI persona can pull information from your uploaded documents, images, or websites to give even smarter responses.

        Learn more via [Tavus Documentation](/sections/conversational-video-interface).
      </Accordion>

      <Accordion title="What makes a good prompt? How much does Tavus help with that?">
        A good prompt is short, clear, and specific, like giving directions to a 5-year-old. Avoid data dumping. Instead, guide the AI with context and intent.

        Tavus helps by offering system prompt templates, use-case guidance, and API fields to structure your instructions.
      </Accordion>

      <Accordion title="How do I add a custom LLM to CVI?">
        You can bring your own LLM by configuring the layers field in the Create Persona API. Here's an example:

        ```json  theme={null}
        {
          "persona_name": "Storyteller",
          "system_prompt": "You are a storyteller who entertains people of all ages.",
          "context": "Your favorite stories include Little Red Riding Hood and The Three Little Pigs.",
          "pipeline_mode": "full",
          "default_replica_id": "r665388ec672",
          "layers": {
            "llm": {
              "model": "gpt-3.5-turbo",
              "base_url": "https://api.openai.com/v1",
              "api_key": "your-api-key",
              "speculative_inference": true
            }
          }
        }
        ```

        More info here: [LLM Documentation](https://docs.tavus.io/sections/conversational-video-interface/persona/llm#custom-llms)
      </Accordion>

      <Accordion title="How customizable is the user interface? What does Tavus provide?">
        Think of it this way: Tavus is the engine, and you design the car. The UI is 100% up to you.

        To make it easier, we offer a full [Component Library](/sections/conversational-video-interface/component-library) you can copy and paste into your build—video frames, mic/camera toggles, and more.
      </Accordion>

      <Accordion title="How do I change the AI Persona's voice?">
        You can use third-party text-to-speech (TTS) providers like Cartesia or ElevenLabs. Just pass your voice settings in the tts object during Persona setup:

        ```json  theme={null}
        {
          "layers": {
            "tts": {
              "api_key": "your-tts-provider-api-key",
              "tts_engine": "cartesia",
              "external_voice_id": "your-voice-id",
              "voice_settings": {
                "speed": "normal",
                "emotion": ["positivity:high", "curiosity"]
              },
              "tts_emotion_control": true,
              "tts_model_name": "sonic"
            }
          }
        }
        ```

        Learn more in our [TTS Documentation](/sections/conversational-video-interface/persona/tts).
      </Accordion>

      <Accordion title="How can I reduce background noise during calls?">
        Tavus uses Daily's video engine, which includes built-in noise cancellation. You can enable this through the updateInputSettings() method in the Daily API.
      </Accordion>

      <Accordion title="Can I track events in the video call?">
        Yes! Daily supports event listeners you can hook into. Track actions like participants joining, leaving, screen sharing, and more. Great for analytics or triggering workflows.
      </Accordion>

      <Accordion title="How do you change or customize backgrounds or AI Persona?">
        Within the create convo API, there's this property:

        image.jpeg
      </Accordion>

      <Accordion title="What compliance and security standards does Tavus meet?">
        Tavus is built with enterprise-grade security in mind. We're:

        * SOC 2 compliant
        * GDPR compliant
        * HIPAA compliant
        * BAA compliant

        This ensures your data is handled with the highest levels of care and control.
      </Accordion>
    </AccordionGroup>
  </Accordion>
</AccordionGroup>
