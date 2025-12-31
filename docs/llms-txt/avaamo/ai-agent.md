# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/ai-agent.md

# AI Agent

{% hint style="danger" %}
Note: This option applies only to `AI agents`. Refer to [Configure web channel](https://docs.avaamo.com/user-guide/configuration/channels/web-enabled-by-default) for more information.
{% endhint %}

You can use the script provided in the **`Deployment`** section to deploy your agent in any web channel.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUreEy22RUXgydOJ2hT3X%2FScreenshot%202025-11-20%20at%203.42.41%E2%80%AFPM.png?alt=media\&token=51eee2b0-fb63-4250-9c83-8a91167a2f0d)

### Enable User Form

This option allows you to collect user details before the user begins a conversation with the agent. Select the checkbox to enable this feature.

### ASR Configuration

The v6 ASR model is now the default. Contact Avaamo Support if you need to change this configuration or enable additional model options.

## Deployment

You can use the script provided in the **`Deployment`** section to deploy your agent in any web channel.

The **AI Agent** tab provides options to configure and deploy your agent on the web channel. From this tab, you can set up user interaction requirements, choose voice processing capabilities, and use the deployment script to integrate the agent into your website.

* Click the copy icon in the text area to copy the script provided in "Copy your embed code".

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fx84M5JCtR67kXziGyNhO%2FScreenshot%202025-11-20%20at%203.43.07%E2%80%AFPM.png?alt=media\&token=2b030253-77dd-47d3-a03f-77929653628c)

{% hint style="info" %}
**Key point:**

The copied code contains,

```
var widget = new AvaamoAgentic({url: "https://cx.avaamo. com/web_channel/channel/53f80
xxx-xxxx-xxxx-xxx950b245/agentic_agents/widget.js", container: "#mobile-container"});
```

Where `container` can be any valid selector where you want the widget to appear.&#x20;

For example, if set to `'body'`, the widget attaches to the `<body>` of the page.
{% endhint %}

* Right-click anywhere on your website, open the HTML document, scroll down to the end of the page, and copy the script provided in the web channel detail page, immediately above the end of the body tag in your HTML page.
