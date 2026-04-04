# Source: https://docs.xano.com/the-function-stack/functions/apis-and-lambdas/realtime-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Realtime Functions

While Realtime is fully functional without implementing anything in your function stacks, you may find yourself wanting to build function stacks to extend the functionality of Realtime.

This is possible with the new **Realtime Event** function, located under APIs & Lambdas in the function panel.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6294324a-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=bdfcb1773a7b84eef496c17a578704ea" width="754" height="239" data-path="images/6294324a-image.jpeg" />
</Frame>

### Using the Realtime Event Function

This function sends a message of type 'event' to the channel specified. Remember, a message can be anything from plain text to a JSON object for even further flexibility.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/97a79538-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=a07d56a8c7b267cc6f8337d283ca446a" width="594" height="451" data-path="images/97a79538-image.jpeg" />
</Frame>

**Channel** - The channel to send the event to

**Data** - The payload of the event

**Database** - If this channel requires authentication, select the corresponding database that handles your authentication here

You can use variables for Channel and Data to make the event behave dynamically.

<Info>
  Please note that Event is different than Message, and will need to be handled accordingly by your frontend.
</Info>

### Example

Realtime connections do not log message history. This means that once a user leaves our Marvel chat room, if they come back, they won't be able to see any of the previous messages. So, we want to store our messages in a database table as they are sent to the channel.

We could approach this in a couple of different ways.

1. Have our frontend send an API request at the same time a message is sent to the channel to log the message.
2. Have our frontend only send an API request, and our API can handle delivering the message once it is stored.

For this example, we will use the second option. We need to first modify our frontend code to send the API request, instead of sending the message directly to the channel. We'll do this by defining a new function and then calling it when our button is clicked.

```javascript  theme={null}
function sendMessageToRealtime(channel, message) {
        fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json'
           },
        body: JSON.stringify({
        channel: 'your_channel_name',
        message: 'your_message'
    })
  });
}

document.getElementById('form').addEventListener('submit', (event) => {
         event.preventDefault();
         sendMessageToRealtime('marvel_chat_room', document.getElementById(message.value))
         event.target.message.value = '';
});
```

<Accordion title="Code Explanation">
  First, we define the function and make sure we define two parameters: channel for the channel to send the message to, and message for the message body.

  ```js  theme={null}
  function sendMessageToRealtime(channel, message) {
  ```

  After that, we're using fetch, a Javascript function to send API requests, to our endpoint. We don't need to worry much about the technical details here if you aren't comfortable, but you may need to change the method and/or add new parameters to the body of the request depending on your use case. For this example, all our API needs is that channel name and message.

  ```js  theme={null}
  fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
          method: 'POST',
          headers: {
             'Content-Type': 'application/json'
             },
          body: JSON.stringify({
          channel: channel,
          message: message
      })
    });
  ```

  Now, we need to handle what happens when our Send button is clicked. We'll start by looking for that element and adding an event listener to it. It just looks for our form, which has an ID of form, and a submit button inside of it.

  ```js  theme={null}
  document.getElementById('form').addEventListener('submit', (event) => {
  ```

  We'll add a line to ensure that no 'default' behavior occurs when a user clicks the send button.

  ```js  theme={null}
  event.preventDefault();
  ```

  Next, we'll call our sendMessageToRealtime function and give it our 'marvel-chat-room' channel name and the value of the message input box. Right after that, we clear the input to prepare for the next message.

  ```js  theme={null}
  sendMessageToRealtime('marvel_chat_room', document.getElementById(event.target.message.value))
  event.target.message.value = '';
  ```
</Accordion>

We need to set up a database table to log the messages.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e1f5062e-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=93093b16a9cc80e069afbf37eed83c35" width="1332" height="446" data-path="images/e1f5062e-image.jpeg" />
</Frame>

Here's the API endpoint we are sending these requests to.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d7ca69b7-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=d72de995b7f62c429d69bfa0dd65170e" width="1922" height="1402" data-path="images/d7ca69b7-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/bf291629-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=e3b85d0131b0a318b4f3b7f76bae9874" width="2304" height="1138" data-path="images/bf291629-image.jpeg" />
</Frame>

This endpoint takes in the channel name and message data, fires our Realtime Event function, and then stores the message in the database table.

At this point, we have modified our frontend code and set up the API in Xano to handle the requests. Now, when our users send messages, they will be logged in the database table, and we still get all of the benefits of utilizing the realtime connection.


Built with [Mintlify](https://mintlify.com).