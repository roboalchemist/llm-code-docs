# Source: https://docs.deepconverse.com/product-docs/chatbots/deploy/open-chatbot-via-javascript.md

# Open chatbot via Javascript

You can trigger opening of the chatbot on click of a button or an external event. To do so use the following Javascript

```javascript
window.dispatchEvent(new CustomEvent('dc.bot.show'));
```
