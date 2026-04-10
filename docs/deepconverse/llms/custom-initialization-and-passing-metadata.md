# Source: https://docs.deepconverse.com/product-docs/chatbots/deploy/custom-initialization-and-passing-metadata.md

# Custom Initialization and Passing Metadata

By default the chatbot script is configured to show the chatbot on load. In cases you need customization on which pages does the chatbot show on or pass specific metadata you can override the trigger function and initialize the chatbot on your webpage.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FV6bKtBsSfRFQvvHI8P22%2Fimage.png?alt=media&#x26;token=98a3123c-322e-4a48-b44a-3dcb1d39304c" alt=""><figcaption></figcaption></figure>

You can find the **Trigger Function** under **Features**

### Initializing the chatbot

The chatbot works based on events passed through the script. You can fire the following event to show the chatbot on a page. You can customize when the event is sent based on the origin, button click or any other action on the page to show the chatbot.

```javascript
document.dispatchEvent(new CustomEvent("botWidgetInit", {"detail": {"origin": "support"}}));
```

### Passing Metadata

To make decisions in the flow you can pass metadata to the chatbot. This metadata live in the conversation context and is available to use in routing/api and other actions.

```javascript
let metadata = {
    "origin": "support",
    "tags": ["ios", "vip"]
}
document.dispatchEvent(new CustomEvent("botWidgetInit", {"detail": metadata}));
```
