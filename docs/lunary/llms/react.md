# Source: https://docs.lunary.ai/docs/integrations/javascript/react.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage with React

<Steps>
  <Step n="1" title="Import">
    Install the package and import the necessary functions from our React export:

    ```ts  theme={null}
    import lunary, { useChatMonitor } from 'lunary/react';
    ```
  </Step>

  <Step n="2" title="Initialize lunary">
    Initialize the SDK with your application's tracking ID:

    ```ts  theme={null}
    lunary.init({
      publicKey: "0x0",
    })
    ```
  </Step>

  <Step n="3" title="Use the `useChatMonitor` hook">
    The `useChatMonitor` hook exposes the following functions:

    ```ts  theme={null}
    const { 
      restart, 
      trackFeedback, 
      trackMessage
    } = useChatMonitor();
    ```

    Here's an example of how you would it into your Chat component.

    ```ts  theme={null}
    import { useState, useEffect } from "react";

    const App = () => {
      const [input, setInput] = useState("");
      const [messages, setMessages] = useState([]);

      const { restart: restartMonitor, trackFeedback, trackMessage } = useChatMonitor();
      
      // Step 4: Use Effects for Initialization
      useEffect(() => {
        restartMonitor();
      }, []);

      // Step 5: Define Your Message Handlers
      const askBot = async (query) => { 

        // Track the user message and keep the message ID in reference
        const messageId = trackMessage({
          role: 'user',
          content: query,
        });

        setMessages([...messages, { id: messageId, role: "user", content: query }]);

        const answer = await fetchBotResponse(query, messages);

        setMessages([...messages, { role: "assistant", content: answer }]);

        // Track the bot answer
        trackMessage({
          role: 'assistant',
          content: answer,
        });
      }

      // Your message logic
      const fetchBotResponse = async (query, messages) => {
        const response = await fetch("https://...", {
          method: "POST",
          body: JSON.stringify({ messages }),
        });
        return await response.text();
      };

      const restartChat = () => { 
        setMessages([]);
        restartMonitor();
      }

      // Step 6: Render UI
      return (
        <>
          <div>
            {messages.map((message) => (
              <div key={message.id}>
                <div>{message.role}</div>
                <div>{message.text}</div>
              </div>
            ))}
          </div>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                askBot(input);
                setInput("");
              }
            }}
          />
        </>
      );
    }
    ```
  </Step>

  <Step n="4" title="Reconcile calls on your backend">
    Make sure to pass the message IDs to your backend to reconcile with the backend calls and agents.
  </Step>
</Steps>

# Vercel AI SDK Integration

Effortlessly integrate the Vercel AI SDK into your Next.js app using lunary We've built a custom hook that makes tracking your AI-driven chats a breeze.

<Note>
  ### Other frameworks

  This assumes you are using Next.js. If you are using another framework, contact us and we'll help you integrate.
</Note>

<Steps>
  <Step n="1" title="Import and Initialize">
    Import lunary and the AI SDK helper hook, then initialize the monitor with your app ID.

    ```ts  theme={null}
    import lunary, { useMonitorVercelAI } from "lunary/react"

    lunary.init({
      publicKey: "0x0"
    })
    ```
  </Step>

  <Step n="2" title="Wrap the useChat hook">
    ```tsx  theme={null}
    export default function Chat() {
      const ai = useChat({
        // This is necessary to reconcile LLM calls made on the backend
        sendExtraMessageFields: true
      })

      // Use the hook to wrap and track the AI SDK
      const {
        trackFeedback, // this a new function you can use to track feedback
        messages,
        input,
        handleInputChange,
        handleSubmit
      } = useMonitorVercelAI(ai)

      // Optional: Identify the user
      useEffect(() => {
        lunary.identify("elon", {
          name: "Elon Musk",
          email: "elon@tesla.com",
        })
      }, [])

      return (
        // ... your chat UI ...
      )
    }
    ```
  </Step>

  <Step n="3" title="Setup the monitor on the backend">
    We'll need to reconcile the OpenAI calls made in the backend, with messages sent from the frontend. To do this, we'll need to use the backend version of the lunary.

    ```ts  theme={null}
    import lunary from "lunary";
    import { monitorOpenAI } from "lunary/openai";

    lunary.init({
      publicKey: "0x0",
    })

    // Create an OpenAI API client and monitor it
    const openai = monitorOpenAI(
      new OpenAI({
        apiKey: process.env.OPENAI_API_KEY
      })
    );
    ```
  </Step>

  <Step n="4" title="Reconcile messages with OpenAI calls">
    Once your openai client is monitored, you can use the `setParent` method to reconcile the frontend message IDs with the backend call:

    ```ts  theme={null}
    const response = await openai.chat.completions
      .create({
        model: "gpt-4",
        stream: true,
        messages: messages,
      })
      // The setParent method reconcilates the frontend call with the backend call
      .setParent(lastMessageId);
    ```

    ### Full API Function Example

    <Note>
      Make sure you've enabled `sendExtraMessageFields` on the  `useChat` hook so that message IDs are also sent.
    </Note>

    ```ts  theme={null}
    // ./app/api/chat/route.ts
    import OpenAI from "openai";
    import { OpenAIStream, StreamingTextResponse } from "ai";

    // Import the backend version of the monitor
    import lunary, { monitorOpenAI } from "lunary/openai";

    lunary.init({
      publicKey: "0x0",
    })

    // Create an OpenAI API client and monitor it
    const openai = monitorOpenAI(
      new OpenAI({
        apiKey: process.env.OPENAI_API_KEY
      })
    );

    export const runtime = "edge";

    export async function POST(req: Request) {
      const data = await req.json()
      const { messages: rawMessages } = data

      // Keep only the content and role of each message, otherwise OpenAI throws an error
      const messages = rawMessages.map(({ content, role }) => ({ role, content }))

      // Get the last message's run ID
      const lastMessageId = rawMessages[rawMessages.length - 1].id

      // Ask OpenAI for a streaming chat completion given the prompt
      const response = await openai.chat.completions
        .create({
          model: "gpt-4",
          stream: true,
          messages: messages,
        })
        // The setParent method reconcilates the frontend call with the backend call
        .setParent(lastMessageId);


      const stream = OpenAIStream(response);


      return new StreamingTextResponse(stream);
    }
    ```
  </Step>
</Steps>
