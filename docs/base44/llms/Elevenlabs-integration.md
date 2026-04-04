# Source: https://docs.base44.com/Integrations/Elevenlabs-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ElevenLabs Integration

> Connect your Base44 app with ElevenLabs to create lifelike audio using state-of-the-art voice models for content, voiceovers, accessibility, and more

<Info>
  <u>Note</u>: ElevenLabs integration is available on Builder tier and above. If you're on the Free tier, you'll need to upgrade your app to use backend functions and payment features.
</Info>

## Step-by-step setup

### Part 1: The ElevenLabs side

If you already have your ElevenLab secrets, you can skip ahead to "[Part 2 - The Base44 side](https://docs.base44.com/Integrations/Elevenlabs-integration#part-2%3A-the-base44-side)" setup

<Steps>
  <Step title=" Get your ElevenLabs API key and Voice ID">
    1. Sign in to ElevenLabs and go to: Profile → API Keys → Create key.

       <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/11labs-createapi.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=a7fa228cf1a47abc6ea4d9eb6a954905" alt="11labs Createapi Pn" width="1904" height="861" data-path="images/11labs-createapi.png" />
    2. Copy and save the key somewhere secure, but also keep it handy as you’ll need to paste it into Base44 later.
    3. While creating the key, turn on Restrict Key and choose which features this key can use:

       <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/11labs-text2speech.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=93a145a3d7edd5c7cc7a81f8a676af51" alt="11labs Text2speech Pn" width="1903" height="865" data-path="images/11labs-text2speech.png" />

       <Info>
         **At a minimum, enable Text to Speech.** Keep all other features set to “No access” unless you specifically plan to use them (e.g., Speech to Speech, Speech to Text, Sound Effects, Dubbing, etc.).
       </Info>

       <Tip>
         Set a **Credit Limit** for this key and scope it to a **Project** if you use projects.
       </Tip>
  </Step>

  <Step title="Choose a voice ID">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/11labs.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=32132e6fd8179d8c1381cfb9c656f525" alt="11labs Pn" width="1908" height="869" data-path="images/11labs.png" />

    You can pick any voice available to your account whether it's stock/public voices, your own custom or cloned voices, or shared/community voices.

    <Tip>
      <u>Tip</u>: Add the voice to *My Voices*, then copy its Voice ID (for example: `Bella EXAVITQu4vr4xnSDxMaL`). If you want users to switch voices, store multiple Voice IDs and display them in a dropdown.
    </Tip>

    <Info>
      <u>Important</u>: Each API request uses your ElevenLabs credits. All billing happens directly with ElevenLabs, not through Base44.
    </Info>
  </Step>
</Steps>

### Part 2: The Base44 side

Once you have your ElevenLabs API keys, there are two ways to use this integration in Base44.

Click the option below to expand and view the instructions.

<Accordion title="Option 1: Creating an app from scratch (preferred)" icon="sparkles">
  This option uses our ready-made integration, available in the[ integrations catalog](https://app.base44.com/integrations-catalog)

  1. Head over to Base44 and click on Integrations.

     <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />

     <Info>
       Make sure you're logged into Base44 to view the [Integrations catalog page](https://app.base44.com/integrations-catalog)
     </Info>
  2. Select ElevenLabs and click on "Use this integration"

     <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Screenshot2025-08-14at10.38.28PM.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=88cf6528cab925c67eba8694190cf6ab" alt="11labs" width="1570" height="782" data-path="images/Screenshot2025-08-14at10.38.28PM.png" />
  3. When prompted, type out your prompt and paste your ELEVENLABS\_API\_KEY and VOICE\_ID.  The integration will handle the backend wiring to ElevenLabs.

     <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/11labspromptkey.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=ab6aef6cfe96081c57fe0186dd9ffad4" alt="11labspromptkey Pn" width="1871" height="871" data-path="images/11labspromptkey.png" />

     <Info>
       You don’t need to manually activate backend functions. Ready-Made integrations enable them automatically.
     </Info>
</Accordion>

<Accordion title="Option 2: Working with an existing app" icon="browser">
  1. In your app Dashboard, click on **App Settings** and [Enable Backend Functions](/Integrations/Using-integrations#activating-backend-functions).
  2. Use the AI chat to connect ElevenLabs and add your secrets.

     <Card title="Example: Personal trainer app">
       \*\*Let's use a training app as an example: \*\*

       `Build a personal trainer app for daily workouts. I choose a muscle group, you auto-generate 3-6 exercises with sets, reps, and rest. Show one exercise at a time with work/rest timers.`

       \*\*App prompt to conect ElevenLabs: \*\*

       `Connect this app to ElevenLabs Text-to-Speech as an Instant integration. Ask me for ELEVENLABS_API_KEY and VOICE_ID and save them as Secrets. Create a backend function that calls ElevenLabs and returns MP3 as a Base44 data URL.`
     </Card>
  3. In the AI chat, click on "Set secrets" and paste your API key and voice ID.

     <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/11labssecretsapi.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=a57bb76e8bb9525c242703e353403dcd" alt="11labssecretsapi Pn" width="1578" height="810" data-path="images/11labssecretsapi.png" />

     <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/11labs-secrets.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=c0e4dfa765e66c8d0888bf7b31004ea7" alt="11labs Secrets Pn" width="1594" height="813" data-path="images/11labs-secrets.png" />
</Accordion>

## **Popular Use Cases for ElevenLabs in Base44 Apps**

* **Interactive Learning Tools** – Read lessons, quizzes, or language exercises aloud with natural voices.
* **Fitness & Wellness Coaches** – Deliver spoken workout instructions, meditation guides, or mindfulness prompts.
* **Accessibility Features** – Provide audio versions of on-screen text for visually impaired users.
* **Customer Support Bots** – Speak responses instead of only showing text, for a more human-like experience.
* **Storytelling & Audiobooks** – Narrate stories, podcasts, or news articles in engaging voices.
* **Games & Entertainment** – Add character voices, mission briefings, or dynamic commentary.
* **E-commerce Guides** – Give audio product descriptions, guided tours, or checkout instructions.
* **Event & Tour Apps** – Offer spoken directions, exhibit descriptions, or venue overviews.
* **Language Learning** – Model pronunciation and practice dialogues in different languages.
* **Custom Brand Voice** – Use a consistent cloned or custom voice for your app’s personality.

## FAQ

<AccordionGroup>
  <Accordion title="Do I need an ElevenLabs subscription to use this integration?">
    Yes. You must have an active ElevenLabs account with credits to process audio. All billing goes through ElevenLabs, not Base44.
  </Accordion>

  <Accordion title="Will API usage consume ElevenLabs credits?">
    Yes, each generation of audio via the API uses your ElevenLabs credits. The number of credits depends on the model and text length
  </Accordion>

  <Accordion title="Can I use ElevenLabs for commercial use?">
    Yes, but only on a **paid plan**. Free-tier accounts are **limited to non-commercial use**. Paid plans (starting with Starter) enable commercial usage
  </Accordion>

  <Accordion title="Can I clone someone else's voice?">
    No. You can only create professional voice clones of **your own voice**, even with their permission. A verification process is required to confirm the voice belongs to you
  </Accordion>

  <Accordion title="Can I adjust the voice style, speed, or pitch?">
    Yes. The ElevenLabs API lets you modify elements like style, stability, similarity, and speed to make the audio sound more natural.
  </Accordion>

  <Accordion title="How do I securely store my API key and Voice ID?">
    Paste them into the **Secrets** fields when configuring the integration. Base44 encrypts and securely stores secrets.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).