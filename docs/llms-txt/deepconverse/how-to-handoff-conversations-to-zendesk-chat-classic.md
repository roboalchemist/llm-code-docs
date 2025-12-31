# Source: https://docs.deepconverse.com/product-docs/chatbots/advanced-functionality/channel-specific-functionality/zendesk-chat-classic/how-to-handoff-conversations-to-zendesk-chat-classic.md

# How to handoff conversations to Zendesk Chat (Classic) ?

In a chat conversation you can escalate to Zendesk Chat agents by connecting the conversation from the chatbot to Zendesk Classic Chat widget.

In order to achieve this you will drag the **Zendesk Chat Widget Handover** add on and connect to the flow. For initiating the handover you will need the **name** and **email** of the customer. An example flow with the configuration is shown below.

For the link to the zendesk snippet.js you can find it by following the steps - [Link](https://support.zendesk.com/hc/en-us/articles/4408881932698-Adding-the-Zendesk-Chat-widget-to-your-website)&#x20;

&#x20;

![mceclip0.png](https://help.deepconverse.com/hc/article_attachments/9130265331476/mceclip0.png)

### Widget Configuration

To support the seamless handoff we will need to add some minor configurations in our trigger function. Here is an example trigger function.

```
addScript("https://static.zdassets.com/ekr/snippet.js?key=4c9db6e3-9bc0-4d01-9207-438668af2578", 'ze-snippet', 'window.zE(\'webWidget\', \'hide\');'); 
window.zESettings = { cookies: true }; 

/** Emit event botWidgetInit to initialize**/ 
document.dispatchEvent(new CustomEvent("botWidgetInit", {"detail": {zendeskClassicChatEnabled: true}}));

```

### User Experience

{% embed url="<https://www.loom.com/share/660244a0168a457cb50e312f204cb2bc?sid=6515300d-adf0-46c2-ad79-19b476cbb1f1>" %}
