# Customize Conversation UI

Experience a conversation in a custom Daily UI — styled to match your preference.

You can **customize your conversation interface** to match your style by updating Daily's Prebuilt UI. Here’s an example showing how to customize the conversation UI by adding leave and fullscreen buttons, changing the language, and adjusting the UI color.

>Note`
For more options, check the [Daily theme configuration reference](https://docs.daily.co/guides/products/prebuilt/customizing-daily-prebuilt-calls-with-color-themes) and [Daily Call Properties](https://docs.daily.co/reference/daily-js/daily-call-client/properties).

## Customization Example Guide

1. In this example, we will use stock replica ID ***rfe12d8b9597*** (Nathan) and stock persona ID ***pdced222244b*** (Sales Coach).

   Use the following request body example:

   ```sh
   theme={null}
   curl --request POST \
     --url https://tavusapi.com/v2/conversations \
     --header 'Content-Type: application/json' \
     --header 'x-api-key: <api_key>' \
     --data '{
     "replica_id": "rfe12d8b9597",
     "persona_id": "pdced222244b"
     }'
   ```

   Replace `<api_key>` with your actual API key. You can generate one in the [Developer Portal](https://platform.tavus.io/api-keys).

2. Make a new `index.html` file.

3. Paste the following code into the file, replace `DAILY_ROOM_URL` in the code with your own room URL from step above.

   ```html
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

4. Start the application by opening the file in the browser.

   ![Customized Conversation UI](https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/customui.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=f07bcdeb02c067bdb441ceea8a194eaf)