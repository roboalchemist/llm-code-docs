# Source: https://docs.xano.com/realtime/realtime-in-webflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Realtime In Webflow

<Warning>
  **Realtime is in beta, and this documentation can change at any time.**
</Warning>

## Getting Started

* Make sure you've reviewed the Realtime documentation [here](/realtime/realtime-in-xano), as it is helpful to understand the process and how to use the Xano SDK before continuing.

* You need to be comfortable adding and modifying custom code in your Webflow project.

## Building a Live Chat in Webflow (Example)

Head to your Site Settings.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1d67eb35-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=74bf6bda57a8296cdf9313068cef2616" width="813" height="532" data-path="images/1d67eb35-image.jpeg" />
</Frame>

In the Custom Code section, paste the following line of code. This loads the Xano SDK and enables us to use it in the rest of our project. It also defines our 'xanoClient', which we'll call in our separate pages to enable Realtime functionality. Make sure to place your API group base URL and realtime canonical in the appropriate places, and click Save.

If you prefer, you can change the variable name `const ``xanoClient` to something else. Please note that any of our examples here will continue to use `xanoClient`, and you'll need to update them accordingly.

```html  theme={null}
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@xano/js-sdk@latest/dist/xano.min.js"></script>

<script type="text/javascript">
  const xanoClient = new XanoClient({
  apiGroupBaseUrl: 'YOUR BASE URL HERE',
  realtimeCanonical: 'YOUR REALTIME CANONICAL HERE',
});
</script>
```

<Info>
  At this point, Webflow will ask you to publish your site to see the changes. Please note that you may need to view a published version of the site to verify that Realtime is enabled and working as expected.
</Info>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9b7f9135-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=8399219d48d8603aa1564dff8118f7e8" width="1306" height="596" data-path="images/9b7f9135-image.jpeg" />
</Frame>

Head back to the Designer, and we can start building realtime functionality into our project.

For this example, we've set up a simple chat application, similar to the example prepared in the main Realtime documentation.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/a07adc19-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=700d31fa2723c9fdec5fd6f52b81a6fe" width="1652" height="749" data-path="images/a07adc19-image.jpeg" />
</Frame>

We know that we want this page to connect to a specific channel, so let's head to our page settings and add some custom code.

```html  theme={null}
<script type="text/javascript">
const marvelChannel = xanoClient.channel("marvel-chat-room");
marvelChannel.on((message) => {
  switch (message.action) {
    case 'message':
      messageReceived(message.body);
      break;
    default:
      console.info(message);
  }
});
</script>
```

<Info>
  Please note that when it comes to how you want to handle realtime implementation for your specific project, your custom code and configuration may look vastly different. The code provided in this section is for demonstration purposes only. Typically when performing an action like this in Webflow, it follows a basic structure, where we...

  1. Create an element on our page to serve as a template, and assign it a class.

  2. Once you have styled the element to your liking, give it a subclass. Change the properties of the subclass to set Display to None.

  3. In your custom code, when it's time to render a message, you'll need to generate a copy of the original element containing the message or other content to show.
</Info>

This piece of code, placed in the 'before \</body> tag' section, tells the page that we want to connect to the marvel-chat-room channel and listen for messages. Any time we receive a new message, we want to execute another function called messageReceived, which will handle rendering the new message on the page.

Now that we've set up actually connecting to the realtime server, we can start working with our messages. This is an example code snippet that lives right above our \</body> tag to render new messages on the page.

```javascript  theme={null}
function messageReceived(payload) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
  const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';
  const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) {
    chatbox.appendChild(messageDiv);
  }
}
```

<Accordion title="Code Explanation">
  In this code, we start by defining our function and the data it needs to run.

  ```js  theme={null}
  function messageReceived(payload) {
  ```

  We then define a couple of variables, messageDiv and messageText, targeting newly created div elements to contain our message. We're also applying some styling to the message block to make sure it displays.

  ```js  theme={null}
  const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
  const messageText = document.createElement("div");
    messageText.classList.add("message-text");
    messageText.textContent = payload;
    messageDiv.appendChild(messageText);
    messageDiv.style.display = 'block';
  ```

  In the final section, we look for the element on our page with the class of 'chatbox' and place the new div inside of it.

  ```js  theme={null}
  const chatboxes = document.getElementsByClassName("chatbox");
    for (const chatbox of chatboxes) {
      chatbox.appendChild(messageDiv);
    }
  }
  ```
</Accordion>

We're almost there. The last thing we need to do is add the ability to send new messages.

```javascript  theme={null}
function sendMessage() {
      const message = document.getElementById("messageInput").value;
      marvelChannel.message(message);
      document.getElementById("messageInput").value = "";
    }

    document.getElementById("sendButton").addEventListener("click", sendMessage);
```

<Accordion title="Code Explanation">
  First, we define a new function called sendMessage that is triggered every time we need to send a new message to the channel.

  ```js  theme={null}
  function sendMessage() {
  ```

  Inside of this function, we define our message as the value of our input.

  ```js  theme={null}
  const message = document.getElementById("messageInput").value;
  ```

  We can then send our message to the channel, and then clear the input value to prepare for a new message.

  ```js  theme={null}
       marvelChannel.message(message);
        document.getElementById("messageInput").value = "";
      }
  ```

  The last line of the code adds an event listener to our sendButton. This makes sure that every time the button is clicked, the function is executed.

  ```js  theme={null}
    document.getElementById("sendButton").addEventListener("click", sendMessage);
  ```
</Accordion>

And with that, you've just built live chat in your Webflow site. Publish your changes and check it out!

### View the sample Webflow project [here](https://preview.webflow.com/preview/realtime-b964af?utm_medium=preview_link\&utm_source=designer\&utm_content=realtime-b964af\&preview=c483fbe91f630dec469a273e58c9c8c6\&workflow=preview).

You'll want to clone this project so you can fill in your API group base URL and realtime canonical in the site settings.


Built with [Mintlify](https://mintlify.com).