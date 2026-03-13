# Source: https://docs.sinch.com/ia-conversational/untitled-8/action.md

# Action

## Clear Session <a href="#clear-session" id="clear-session"></a>

Often, at the end of a flow, an API backend call will be configured to, for example, save a train ticket in the ticket ordering system. Afterwards users should be able to book a new ticket to a different location.

You can achieve this with the 'clear session' action. This action removes the values of set session variables. This is useful when a user asks to correct a value, or to start over and delete all variables.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LV37Zkd0k6v1aYEycFQ%2F-LV3aGDou1TkM9YA4Oo_%2Fimage.png?alt=media\&token=707756be-6db6-46fa-82a2-73dd3b290fb1)

## Send to offload provider <a href="#send-to-offload-provider" id="send-to-offload-provider"></a>

A user that reaches this action will be offloaded to a human customer support agent. For this to work, you need to enable offloading.

Depending on your selected offloading provider, additional configuration may be required.

## API <a href="#api" id="api"></a>

This action can be used to integrate back-end services into your bot. More details can be found in [our tutorial](https://docs.chatlayer.ai/integrations/custom-back-end-integrations).

## Code <a href="#code" id="code"></a>

The code editor allows developers to quickly build custom logic on top of the bot by writing their own Javascript code blocks. Typically, the code editor is used to perform requests to external systems, or to do operations with variables.

You can find more information about the code editor here: [Code Editor/integrations/code-action](https://docs.chatlayer.ai/integrations/code-action)

There are also two tutorials in which we show you how the code editor can be used:

[Retrieving data from Airtable (GET)/integrations/code-action/retrieving-data-from-airtable-get](https://docs.chatlayer.ai/integrations/code-action/retrieving-data-from-airtable-get)

[Sending data to Airtable (POST)/integrations/code-action/airtable](https://docs.chatlayer.ai/integrations/code-action/airtable)

## iframe <a href="#iframe" id="iframe"></a>

An iframe is a custom element that can be used to show a different web page in the chat conversation. It can also be used to communicate with the parent window using the [postMessage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).

Have a look at this basic example:

```
<!DOCTYPE html><html lang="en">	<head>		<meta charset="UTF-8">		</head>		<body>			<button onClick="window.parent.postMessage(JSON.stringify({target:'CL_API',type:'SEND_MESSAGE', payload:{text: 'You clicked the button'} }),'*')">         SEND_MESSAGE        </button>		</body></html>
```

If this block of code is hosted and embedded within our iframe plugin, it will send the user a chat message when they click the button.

The postMessage API can also handle `UPDATE_SESSION` and `GO_TO_DIALOGSTATE` events.

## JSON Builder <a href="#json-builder" id="json-builder"></a>

If your bot is published on the [Webhook API](https://docs.chatlayer.ai/channels/webhook-api) channel, you can use the JSON Builder action to send messages to the conversation that don't need to result in an actual message to the user. Typically, it's used to send information about the user or bot conversation to the website the bot is published on.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M1dw5eMqNDrpjDngOe6%2F-M1dx9mzFppiXljhS6k-%2Fimage.png?alt=media\&token=3ef5dcd0-6d98-4e2d-9d95-631beacaa858)

### Website window events  <a href="#website-window-events" id="website-window-events"></a>

**You can use the JSON builder action** **in combination with the webwidget channel** to receive window events on your webpage. These events will contain the data as configured in your JSON builder action.

Here's an example: Configure your JSON builder action to send a **language** key, with a variable retrieved from the session, and the "Send config to parent window" toggled on.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MKa3vnvkdS2-AigosWt%2F-MKa57sjNNmEoWB6CO2l%2Fimage.png?alt=media\&token=c4e9711d-7541-4f47-8ff3-4db02a33cd6b)

Your widget will trigger an event for that configuration to its parent window as a MessageEvent. The MessageEvent will contain a \`data\` field which contains the stringified result of the JSON builder configuration. Here's an example on how to listen to these events:

```
// Chatlayer JSON Builder Event Handlerwindow.addEventListener('message', (event) => {    const data = event && event.data && JSON.parse(event.data) || {}    const { type, payload } = data    if (type !== 'CL_DISPATCH_EVENT') return;    console.log('Chatlayer language received: ' + payload.language)})
```

[<br>](https://docs.chatlayer.ai/bot-answers/dialog-state/user-input-bot-dialog)
