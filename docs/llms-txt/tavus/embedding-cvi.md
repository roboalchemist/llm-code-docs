# Source: https://docs.tavus.io/sections/integrations/embedding-cvi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Embed Conversational Video Interface

> Learn how to embed Tavus's Conversational Video Interface (CVI) into your site or app.

## Overview

Tavus CVI delivers AI-powered video conversations directly in your application. You can integrate it using:

| Method                | Best For                           | Complexity | Customization |
| --------------------- | ---------------------------------- | ---------- | ------------- |
| **@tavus/cvi-ui**     | React apps, advanced features      | Low        | High          |
| **iframe**            | Static websites, quick demos       | Low        | Low           |
| **Vanilla JS**        | Basic dynamic behavior             | Low        | Medium        |
| **Node.js + Express** | Backend apps, dynamic embedding    | Medium     | High          |
| **Daily SDK**         | Full UI control, advanced features | High       | Very High     |

## Implementation Steps

<Tabs>
  <Tab title="@tavus/cvi-ui (Component Library)">
    This method provides a full-featured React component library. It offers pre-built, customizable components and hooks for embedding Tavus CVI in your app.

    ## Overview

    The Tavus Conversational Video Interface (CVI) React component library provides a complete set of pre-built components and hooks for integrating AI-powered video conversations into your React applications. This library simplifies setting up Tavus in your codebase, allowing you to focus on your application's core features.

    Key features include:

    * **Pre-built video chat components**
    * **Device management** (camera, microphone, screen sharing)
    * **Real-time audio/video processing**
    * **Customizable styling** and theming
    * **TypeScript support** with full type definitions

    ***

    ## Quick Start

    ### Prerequisites

    Before getting started, ensure you have a React project set up.

    Alternatively, you can start from our example project: [CVI UI Haircheck Conversation Example](https://github.com/Tavus-Engineering/tavus-examples/tree/main/examples/cvi-ui-haircheck-conversation) - this example already has the HairCheck and Conversation blocks set up.

    ### 1. Initialize CVI in Your Project

    ```bash  theme={null}
    npx @tavus/cvi-ui@latest init
    ```

    * Creates a `cvi-components.json` config file
    * Prompts for TypeScript preference
    * Installs npm dependencies (@daily-co/daily-react, @daily-co/daily-js, jotai)

    ### 2. Add CVI Components

    ```bash  theme={null}
    npx @tavus/cvi-ui@latest add conversation
    ```

    ### 3. Wrap Your App with the CVI Provider

    In your root directory (main.tsx or index.tsx):

    ```tsx  theme={null}
    import { CVIProvider } from './components/cvi/components/cvi-provider';

    function App() {
      return <CVIProvider>{/* Your app content */}</CVIProvider>;
    }
    ```

    ### 4. Add a Conversation Component

    Learn how to create a conversation URL at [https://docs.tavus.io/api-reference/conversations/create-conversation](https://docs.tavus.io/api-reference/conversations/create-conversation).

    **Note:** The Conversation component requires a parent container with defined dimensions to display properly.

    <Info>
      Ensure your body element has full dimensions (`width: 100%` and `height:
        100%`) in your CSS for proper component display.
    </Info>

    ```tsx  theme={null}
    import { Conversation } from './components/cvi/components/conversation';

    function CVI() {
      const handleLeave = () => {
        // handle leave
      };
      return (
        <div
          style={{
            width: '100%',
            height: '100%',
            maxWidth: '1200px',
            margin: '0 auto',
          }}
        >
          <Conversation
            conversationUrl='YOUR_TAVUS_MEETING_URL'
            onLeave={handleLeave}
          />
        </div>
      );
    }
    ```

    ***

    ## Documentation Sections

    * **[Overview](/sections/conversational-video-interface/component-library/overview)** – Overview of the CVI component library
    * **[Blocks](/sections/conversational-video-interface/component-library/blocks)** – High-level component compositions and layouts
    * **[Components](/sections/conversational-video-interface/component-library/components)** – Individual UI components
    * **[Hooks](/sections/conversational-video-interface/component-library/hooks)** – Custom React hooks for managing video call state and interactions
  </Tab>

  <Tab title="iframe ">
    This is the simplest approach requiring no coding. It leverages Tavus’s prebuilt interface with limited customization options.

    1. Create a conversation using the Tavus API.
    2. Replace `YOUR_TAVUS_MEETING_URL` below with your actual conversation URL:

    ```html  theme={null}
    <!DOCTYPE html>
    <html>
      <head><title>Tavus CVI</title></head>
      <body>
        <iframe
          src="YOUR_TAVUS_MEETING_URL"
          allow="camera; microphone; fullscreen; display-capture"
          style="width: 100%; height: 500px; border: none;">
        </iframe>
      </body>
    </html>
    ```
  </Tab>

  <Tab title="Vanilla JavaScript">
    This method provides basic customizations and dynamic room management for apps without framework.

    1. Add the following script tag to your HTML `<head>`:

    ```html  theme={null}
    <head>
      <script src="https://unpkg.com/@daily-co/daily-js"></script>
    </head>
    ```

    2. Use the following script, replacing `'YOUR_TAVUS_MEETING_URL'` with your actual conversation URL:

    ```html  theme={null}
    <body>
      <div id="video-call-container"></div>
      <script>
        // Create a Daily iframe with custom settings
        const callFrame = window.Daily.createFrame({
          iframeStyle: {
            width: '100%',
            height: '500px',
          },
        });

        // Join the Tavus CVI meeting
        callFrame.join({ url: 'YOUR_TAVUS_MEETING_URL' });

        // Append the iframe to the container
        document.getElementById('video-call-container').appendChild(callFrame.iframe());
      </script>
    </body>

    ```
  </Tab>

  <Tab title="Node.js + Express">
    This method serves dynamic pages that embed Tavus CVI within Daily rooms.

    1. Install Express:

    ```bash  theme={null}
    npm install express
    ```

    2. Create `server.js` and implement the following Express server:

    ```js  theme={null}
    const express = require('express');
    const app = express();
    const PORT = 3000;

    app.get('/room', (req, res) => {
      const meetingUrl = req.query.url || 'YOUR_TAVUS_MEETING_URL';
      res.send(`
        <!DOCTYPE html>
        <html>
          <head>
            <script src="https://unpkg.com/@daily-co/daily-js"></script>
          </head>
          <body>
            <div id="video-call-container"></div>
            <script>
              // Create the Daily iframe for the Tavus CVI room
              const callFrame = window.Daily.createFrame({
                iframeStyle: {
                  width: '100%',
                  height: '500px',
                },
              });

              // Join the room
              callFrame.join({ url: '${meetingUrl}' });

              // Append the iframe to the container
              document.getElementById('video-call-container').appendChild(callFrame.iframe());
            </script>
          </body>
        </html>
      `);
    });

    app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
    ```

    3. Run the server:

    ```bash  theme={null}
    node server.js
    ```

    4. Visit: `http://localhost:3000/room?url=YOUR_TAVUS_MEETING_URL`

    <Note>
      ### Notes

      * Supports dynamic URLs.
      * Can be extended with authentication and other logic using Tavus's API.
    </Note>
  </Tab>

  <Tab title="Daily JS SDK">
    This method offers complete control over the user experience and allows you to build a fully custom interface for Tavus CVI.

    1. Install SDK:

    ```bash  theme={null}
    npm install @daily-co/daily-js
    ```

    2. Use the following script to join the Tavus CVI meeting:

    ```js [expandable] theme={null}
    import React, { useEffect, useRef, useState } from 'react';
    import DailyIframe from '@daily-co/daily-js';


    const getOrCreateCallObject = () => {
      // Use a property on window to store the singleton
      if (!window._dailyCallObject) {
        window._dailyCallObject = DailyIframe.createCallObject();
      }
      return window._dailyCallObject;
    };


    const App = () => {
      const callRef = useRef(null);
      const [remoteParticipants, setRemoteParticipants] = useState({});


      useEffect(() => {
        // Only create or get one call object per page
        const call = getOrCreateCallObject();
        callRef.current = call;


        // Join meeting
        call.join({ url: "YOUR_TAVUS_MEETING_URL" });


        // Handle remote participants
        const updateRemoteParticipants = () => {
          const participants = call.participants();
          const remotes = {};
          Object.entries(participants).forEach(([id, p]) => {
            if (id !== 'local') remotes[id] = p;
          });
          setRemoteParticipants(remotes);
        };


        call.on('participant-joined', updateRemoteParticipants);
        call.on('participant-updated', updateRemoteParticipants);
        call.on('participant-left', updateRemoteParticipants);


        // Cleanup
        return () => {
          call.leave();
        };
      }, []);


      // Attach remote video and audio tracks
      useEffect(() => {
        Object.entries(remoteParticipants).forEach(([id, p]) => {
          // Video
          const videoEl = document.getElementById(`remote-video-${id}`);
          if (videoEl && p.tracks.video && p.tracks.video.state === 'playable' && p.tracks.video.persistentTrack
          ) {
            videoEl.srcObject = new MediaStream([p.tracks.video.persistentTrack]);
          }
          // Audio
          const audioEl = document.getElementById(`remote-audio-${id}`);
          if (
            audioEl && p.tracks.audio && p.tracks.audio.state === 'playable' && p.tracks.audio.persistentTrack
          ) {
            audioEl.srcObject = new MediaStream([p.tracks.audio.persistentTrack]);
          }
        });
      }, [remoteParticipants]);


      // Custom UI
      return (
        <div className="min-h-screen bg-gray-900 text-white flex flex-col">
          <header className="bg-gray-800 p-4 flex justify-between items-center">
            <span className="font-semibold">Meeting Room (daily-js custom UI)</span>
          </header>
          <main className="flex-1 p-4 grid grid-cols-2 md:grid-cols-4 gap-2">
          {Object.entries(remoteParticipants).map(([id, p]) => (
            <div
              key={id}
              className="relative bg-gray-800 rounded-lg overflow-hidden aspect-video w-48"
            >
              <video
                id={`remote-video-${id}`}
                autoPlay
                playsInline
                className="w-1/3 h-1/3 object-contain mx-auto"
              />
              <audio id={`remote-audio-${id}`} autoPlay playsInline />
              <div className="absolute bottom-2 left-2 bg-black bg-opacity-50 px-2 py-1 rounded text-sm">
                {p.user_name || id.slice(-4)}
              </div>
            </div>
          ))}
        </main>
        </div>
      );
    };


    export default App;
    ```

    3. Customize the conversation UI in the script above (Optional). See the <a href="https://docs.daily.co/guides/customizing-in-call-ui" target="_blank">Daily JS SDK</a> for details.
  </Tab>
</Tabs>

## FAQs

<AccordionGroup>
  <Accordion title="How can I reduce background noise during calls?" defaultOpen="true">
    Daily provides built-in noise cancellation which can be enabled via their <a href="https://docs.daily.co/reference/daily-js/instance-methods/update-input-settings#audio-processor" target="_blank">updateInputSettings()</a> method.

    ```js  theme={null}
    callFrame.updateInputSettings({
      audio: {
        processor: {
          type: 'noise-cancellation',
        },
      },
    });
    ```
  </Accordion>

  <Accordion title="Can I add event listeners to the call client?" defaultOpen="true">
    Yes, you can attach <a href="https://docs.daily.co/reference/daily-js/events" target="_blank">Daily event listeners</a> to monitor and respond to events like participants joining, leaving, or starting screen share.
  </Accordion>
</AccordionGroup>
