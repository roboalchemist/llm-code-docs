# Source: https://docs.tavus.io/sections/conversational-video-interface/overview-cvi.md

# Overview

> CVI enables real-time, human-like video interactions through configurable lifelike replicas.

<Frame>
    <img src="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=bee9bb67ae9ebd516af34537f3e29b32" alt="" data-og-width="1440" width="1440" data-og-height="842" height="842" data-path="images/devmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?w=280&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=f39e8bd562e564cd54c709074c991736 280w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?w=560&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=74dc4dd63c2d8d1e5138ad256e6fd970 560w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?w=840&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=b2c5335c452e42b311bc9496f51767c8 840w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?w=1100&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=8c85ae338cc56704dc9f3b1570c8020a 1100w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?w=1650&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=871b3f5b1afb20a0ba920da4daa893c5 1650w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/devmode.png?w=2500&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=4287a41a81c524a57a900a3662ca7fac 2500w" />
</Frame>

Conversational Video Interface (CVI) is a framework for creating real-time multimodal video interactions with AI. It enables an AI agent to see, hear, and respond naturally, mirroring human conversation.

CVI is the world’s fastest interface of its kind. It allows you to map a human face and conversational ability onto your AI agent. With CVI, you can achieve utterance-to-utterance latency with SLAs under 1 second. This is the full round-trip time for a participant to say something and the replica to reply.

CVI provides a comprehensive solution, with the option to plug in your existing components as required.

## Key Concepts

CVI is built around three core concepts that work together to create real-time, humanlike interactions with an AI agent:

<CardGroup cols={3}>
  <Card title="Persona" icon="heart-pulse" href="/sections/conversational-video-interface/persona/overview">
    The **Persona** defines the agent’s behavior, tone, and knowledge. It also configures the CVI layer and pipeline.
  </Card>

  <Card title="Replica" icon="user-group" href="/sections/replica/overview">
    The **Replica** brings the persona to life visually. It renders a photorealistic human-like avatar using the **Phoenix-3** model.
  </Card>

  <Card title="Conversation" icon="video" href="/sections/conversational-video-interface/conversation/overview">
    A **Conversation** is a real-time video session that connects the persona and replica through a WebRTC connection.
  </Card>
</CardGroup>

## Key Features

<CardGroup cols={2}>
  <Card title="Natural Interaction" icon="face-smile-beam">
    CVI uses facial cues, body language, and real-time turn-taking to enable natural, human-like conversations.
  </Card>

  <Card title="Modular pipeline" icon="layer-group">
    Customize the Perception, STT, LLM and TTS layers to control identity, behavior, and responses.
  </Card>

  <Card title="Lifelike AI replicas" icon="user-robot">
    Choose from over 100+ hyper-realistic digital twins or customize your own with human-like voice and expression.
  </Card>

  <Card title="Multilingual support" icon="globe">
    Hold natural conversations in 30+ languages using the supported TTS engines.
  </Card>

  <Card title="World's lowest latency" icon="bolt">
    Experience real-time interactions with \~600ms response time and smooth turn-taking.
  </Card>
</CardGroup>

## Layers

The Conversational Video Interface (CVI) is built on a modular layer system, where each layer handles a specific part of the interaction. Together, they capture input, process it, and generate a real-time, human-like response.

Here’s how the layers work together:

<AccordionGroup>
  <Accordion title="1. Transport" icon="right-left">
    Handles real-time audio and video streaming using WebRTC (powered by Daily). This layer captures the user's microphone and camera input and delivers output back to the user.

    This layer is always enabled. You can configure input/output for audio (mic) and video (camera).
  </Accordion>

  <Accordion title="2. Perception" icon="eye">
    Uses **Raven** to analyze user expressions, gaze, background, and screen content. This visual context helps the replica understand and respond more naturally.

    [Click here to learn how to configure the Perception layer.](/sections/conversational-video-interface/persona/perception)
  </Accordion>

  <Accordion title="3. Speech Recognition (STT)" icon="ear-listen">
    Powered by **Sparrow**, this layer transcribes user speech in real time with lexical and semantic awareness. It enables smart, natural turn-taking through fast, intelligent interruptions.

    [Click here to learn how to configure the Speech Recognition (STT) layer.](/sections/conversational-video-interface/persona/stt)
  </Accordion>

  <Accordion title="4. Large Language Model (LLM)" icon="brain">
    Processes the user's transcribed speech and visual input using a low-latency LLM. Tavus provides ultra-low latency optimized LLMs or lets you integrate your own.

    [Click here to learn how to configure the Large Language Model (LLM) layer.](/sections/conversational-video-interface/persona/llm)
  </Accordion>

  <Accordion title="5. Text-to-Speech (TTS)" icon="volume-high">
    Converts the LLM response into speech using the supported TTS Engines (Cartesia **(Default)**, ElevenLabs).

    [Click here to learn how to configure the Text-to-Speech (TTS) layer.](/sections/conversational-video-interface/persona/tts)
  </Accordion>

  <Accordion title="6. Realtime Replica" icon="face-smile">
    Delivers a high-quality, synchronized digital human response using Tavus's real-time avatar engine powered by **Phoenix**.

    [Click here to learn more about the Replica layer.](/sections/replica/overview)
  </Accordion>
</AccordionGroup>

<Note>
  Most layers are configurable via the [Persona](/sections/conversational-video-interface/persona/overview).
</Note>

## Getting Started

You can quickly create a conversation by using the <a href="https://platform.tavus.io/" target="_blank">Developer Portal</a> or following the steps in the [Quickstart](/sections/conversational-video-interface/quickstart/use-the-full-pipeline) guide.

<div style={{display: 'flex', alignItems: 'center', gap: '8px', marginTop: '4px'}}>
  <span>If you use Cursor, use this pre-built prompt to get started faster:</span>

  <button
    onClick={() => {
    const promptText = document.querySelector('.cursor-prompt-content').textContent;
    navigator.clipboard.writeText(promptText).then(() => {
      const button = document.activeElement;
      const originalText = button.textContent;
      button.textContent = 'Copied!';
      setTimeout(() => {
        button.textContent = originalText;
      }, 2000);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  }}
    style={{
    backgroundColor: '#FA3862',
    color: 'white',
    padding: '6px 16px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontWeight: '500',
    fontSize: '14px',
    lineHeight: '1.5',
    width: '80px',
    textAlign: 'center'
  }}
  >
    <span> Copy </span>
  </button>
</div>

<div style={{display: 'none'}} className="cursor-prompt-content">
  ## ✅ **System Prompt for AI: React (Vite) + Tavus CVI Integration**

  **Purpose:**
  Generate **React (TypeScript)** apps with Tavus CVI using **Vite**, following the official docs and GitHub examples:
  [https://docs.tavus.io/sections/integrations/embedding-cvi](https://docs.tavus.io/sections/integrations/embedding-cvi)

  ***

  ### ✅ **AI MUST ALWAYS DO THE FOLLOWING:**

  #### **1. Setup React App Using Vite**

  ```bash  theme={null}
  npm create vite@latest my-tavus-app -- --template react-ts
  cd my-tavus-app
  npm install
  ```

  ***

  #### **2. Install Tavus CVI UI Components**

  ```bash  theme={null}
  npx @tavus/cvi-ui@latest init
  npx @tavus/cvi-ui@latest add conversation
  ```

  ✅ This creates:

  ```
  src/components/cvi/components/
    cvi-provider.tsx
    conversation.tsx
  ```

  ***

  #### **3. Wrap App with `CVIProvider`**

  Update `src/App.tsx`:

  ```tsx  theme={null}
  import { CVIProvider } from "./components/cvi/components/cvi-provider";

  function App() {
    return <CVIProvider>{/* Your app content */}</CVIProvider>;
  }
  ```

  ***

  #### **4. Create Conversation API Call**

  Always use this pattern:

  ```ts  theme={null}
  const response = await fetch("https://tavusapi.com/v2/conversations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": import.meta.env.VITE_TAVUS_API_KEY || "",
    },
    body: JSON.stringify({
      replica_id: import.meta.env.VITE_REPLICA_ID || "rfe12d8b9597",  // Default
      persona_id: import.meta.env.VITE_PERSONA_ID || "pdced222244b",  // Default
    }),
  });

  const data = await response.json();
  setConversationUrl(data.conversation_url);
  ```

  ✅ **Explain:** `conversation_url` from API response is used inside `<Conversation>`.

  ***

  #### **5. Render `Conversation` Inside `CVIProvider`**

  ```tsx  theme={null}
  <Conversation
    conversationUrl={conversationUrl}
    onLeave={() => setConversationUrl(null)}
  />
  ```

  ***

  #### **6. Add Environment Variable**

  Create `.env` in the **`my-tavus-app`** folder (if not already there):

  ```
  VITE_TAVUS_API_KEY=your_api_key_here
  VITE_REPLICA_ID=rfe12d8b9597   // Default replica_id, can be overridden in .env
  VITE_PERSONA_ID=pdced222244b  // Default persona_id, can be overridden in .env
  ```

  * **Important**: **DO NOT** create `.env` outside of the `my-tavus-app` folder. It must be inside your project directory where `src` exists.

  Access via:

  ```ts  theme={null}
  import.meta.env.VITE_TAVUS_API_KEY
  import.meta.env.VITE_REPLICA_ID
  import.meta.env.VITE_PERSONA_ID
  ```

  ***

  #### **7. Create `cvi-components.json` by Default**

  Ensure that the `cvi-components.json` file is generated in the `my-tavus-app` folder with the following content:

  ```json  theme={null}
  {
    "tsx": true
  }
  ```

  ***

  ### ✅ **Expected AI Output Example**

  **`src/App.tsx`:**

  ```tsx  theme={null}
  import React, { useState } from "react";
  import { CVIProvider } from "./components/cvi/components/cvi-provider";
  import { Conversation } from "./components/cvi/components/conversation";

  const App: React.FC = () => {
    const [conversationUrl, setConversationUrl] = useState<string | null>(null);

    const createConversation = async () => {
      const response = await fetch("https://tavusapi.com/v2/conversations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": import.meta.env.VITE_TAVUS_API_KEY || "",
        },
        body: JSON.stringify({
          replica_id: import.meta.env.VITE_REPLICA_ID || "rfe12d8b9597",
          persona_id: import.meta.env.VITE_PERSONA_ID || "pdced222244b",
        }),
      });

      const data = await response.json();
      setConversationUrl(data.conversation_url);
    };

    return (
      <CVIProvider>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            width: "100vw",
            height: "100vh",
            backgroundColor: "#1e1e1e",
            color: "#fff",
            textAlign: "center",
            flexDirection: "column",
            margin: 0,
            padding: 0,
          }}
        >
          <h1 style={{ marginBottom: "1rem" }}>Tavus CVI Integration (Vite)</h1>
          {!conversationUrl ? (
            <button
              onClick={createConversation}
              style={{
                padding: "0.75rem 1.5rem",
                fontSize: "1rem",
                background: "#6a0dad",  // Purple for light and dark modes
                color: "#fff",
                border: "none",
                borderRadius: "6px",
                cursor: "pointer",
              }}
            >
              Start Conversation
            </button>
          ) : (
            <div style={{ width: "100%", maxWidth: "800px" }}>
              <Conversation
                conversationUrl={conversationUrl}
                onLeave={() => setConversationUrl(null)}
              />
            </div>
          )}
        </div>
      </CVIProvider>
    );
  };

  export default App;
  ```

  ***

  ### ✅ **Checklist for AI Output**

  * ✅ Uses **Vite + React TypeScript** (`npm create vite@latest --template react-ts`)
  * ✅ Includes `npx @tavus/cvi-ui init` and `add conversation`
  * ✅ Imports `CVIProvider` and `Conversation` from `src/components/cvi/components/`
  * ✅ Uses correct API call with:

    * `https://tavusapi.com/v2/conversations`
    * Headers: `Content-Type`, `x-api-key`
    * Body: `replica_id` & `persona_id`
  * ✅ Uses `import.meta.env.VITE_TAVUS_API_KEY`
  * ✅ Renders `<Conversation>` inside `<CVIProvider>`
  * ✅ Purple button is visible in both light and dark modes
  * ✅ `.env` is created inside the correct project folder (`my-tavus-app`)
  * ✅ `cvi-components.json` is created by default with `{ "tsx": true }`

  ***

  ### Keep things in mind:

  * If you're already in the `my-tavus-app` folder, avoid running `cd my-tavus-app` again. Check your current folder before running commands.
  * After running the necessary setup, remember to run `npm run dev` to start your app.
  * Do **NOT** place the `.env` file outside of the project folder. It must reside within the `my-tavus-app` directory.
</div>
