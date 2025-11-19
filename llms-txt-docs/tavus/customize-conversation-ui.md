# Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/customize-conversation-ui.md

# Customize Conversation UI

> Experience a conversation in a custom Daily UI — styled to match your preference.

You can **customize your conversation interface** to match your style by updating Daily's Prebuilt UI.

Here’s an example showing how to customize the conversation UI by adding leave and fullscreen buttons, changing the language, and adjusting the UI color.

<Note>
  For more options, check the <a href="https://docs.daily.co/guides/products/prebuilt/customizing-daily-prebuilt-calls-with-color-themes" target="_blank">Daily theme configuration reference</a> and <a href="https://docs.daily.co/reference/daily-js/daily-call-client/properties" target="_blank">Daily Call Properties</a>.
</Note>

### Customization Example Guide

<Steps>
  <Step title="Step 1: Create Your Conversation">
    <Note>
      In this example, we will use stock replica ID ***rfe12d8b9597*** (Nathan) and stock persona ID ***pdced222244b*** (Sales Coach).
    </Note>

    Use the following request body example:

    ```sh  theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "replica_id": "rfe12d8b9597",
      "persona_id": "pdced222244b"
    }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Customize the Conversation UI">
    1. Make a new `index.html` file

    2. Paste following code into the file, replace `DAILY_ROOM_URL` in the code with your own room URL from step above

    ```html {6-8,16-22} theme={null}
    <html>
      <script crossorigin src="https://unpkg.com/@daily-co/daily-js"></script>
      <body>
        <script>
          call = window.Daily.createFrame({
            showLeaveButton: true,       // Leave button on bottom right
            lang: "jp",                  // Language set to Japanese
            showFullscreenButton: true,  // Fullscreen button on top left
            iframeStyle: {
              position: 'fixed',
              top: '0',
              left: '0',
              width: '100%',
              height: '100%',
            },
            theme: {
              colors: {
                accent: "#2F80ED",      // primary button and accent color
                background: "#F8F9FA",  // main background color
                baseText: "#1A1A1A",    // text color
              },
            },
          });
          call.join({ url: 'DAILY_ROOM_URL' });
        </script>
      </body>
    </html>
    ```
  </Step>

  <Step title="Step 3: Run the Application">
    Start the application by opening the file in the browser.

    <Frame>
            <img src="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=f07bcdeb02c067bdb441ceea8a194eaf" alt="" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/customui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?w=280&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=96d192b1da13e7dd92ed9a8ae8273061 280w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?w=560&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=edfcc7b095a2995b13a8bfdcb74aef1d 560w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?w=840&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=b03e4a6b21d4d6cf57946256dadd68f1 840w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?w=1100&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=d80116ce5e7a7588c80d6ba70db1bdb3 1100w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?w=1650&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=6bb76196d4e8a4c4f0d0c82e826b1dc3 1650w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?w=2500&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=5be715e84ed0f5db57175ca74f3c1684 2500w" />
    </Frame>
  </Step>
</Steps>
