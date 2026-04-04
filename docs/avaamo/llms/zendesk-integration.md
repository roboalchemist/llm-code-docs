# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent/zendesk-integration.md

# Zendesk integration

You can integrate the Avaamo Platform with Zendesk for live agent interactions, for scenarios, when there is a need for human intervention. When integrated with the Avaamo Platform, if the user requests, or if the agent senses dissatisfaction, frustration, or anger, or if the agent has defined intents for transfer, it seamlessly transfers the conversation to Zendesk.

### Pre-requisites

* You must have an account set up with Zendesk for a chat. &#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-FBOS1tR1ha-ctSSia%2F-M-FGYtVQs12z-2t1yz3%2Fhowto-zendesk-chat.png?alt=media\&token=feca1494-48b2-4c81-9c6e-40148b29dffe)

* Once that chat is set up, click the profile icon -> Check connection to find the account key.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-mW7Lrj31dsm5OVNZk%2F-M-mXgxb2JEAaj_D_76x%2Fzendesk-check-connection.png?alt=media\&token=98b4243b-4f55-42d0-a1dc-c30c204f9f94)

* Make a note of the account key.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-mW7Lrj31dsm5OVNZk%2F-M-mYiYqke3ZsJxgpSpb%2Fhowto-zendesk-account-key.png?alt=media\&token=395e1b8e-ee36-4d9f-9b2c-9c5972e0f21b)

See [How do I find my Chat Account Key?](https://support.zendesk.com/hc/en-us/articles/203661666-Setting-up-Zendesk-Chat-in-Zendesk-Support#topic_sdz_2hq_sgb) for more information.

### Integrate with Zendesk

* In the **Agent** page, navigate to the **Configure -> Live agent** option in the left navigation menu.
* Specify the account key, in the **API key** text box provided for Zendesk integration.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPPbw9ie5O6l6YJfdKSsd%2FScreenshot%2006-04-2025%20at%2015.20.png?alt=media\&token=79039ecf-9cd0-4945-9fc6-3fb325fbdd01)

* Click **Save**.

### Test your integration

* In the **Agent** page, navigate to the **Test -> Simulator** option in the left navigation menu. Alternatively, you can also test using the **agent icon** in the bottom-right corner.&#x20;
* Transfer the chat to the live agent. For testing purposes, you can use the skill command **#transfer to agent or #talk to agent.**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEgBFQ0xQGsSgwICcqbka%2Fzendesk.png?alt=media\&token=0fff8116-0d8c-4435-9d2a-f4cfd020944b)

* In the Zendesk dashboard, a message to serve the request is displayed. Click the message.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-FkDIwc9-7Eaqs0cSN%2F-M-FvJWp28e3KewBVaTt%2Fhowto-zendesk-serve.png?alt=media\&token=258f9811-fa59-4482-8562-74fbeffc65b9)

* Type a message in the agent. You can view the response in the Zendesk chat window.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-FkDIwc9-7Eaqs0cSN%2F-M-FyWVOVrHi_S9xyV99%2Fhowto-zendesk-response.png?alt=media\&token=2a0b81f1-8695-497a-b763-63d90b43ed0b)

* Type a message in Zendesk. You can view the text in the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-FkDIwc9-7Eaqs0cSN%2F-M-FyjAG99iob2GHvyy9%2Fhowto-zendesk-reply.png?alt=media\&token=d23fd9aa-9b62-47fb-8f70-19aef3824524)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXCtVuNiQKkG0S9ImCCpi%2Fimage.png?alt=media\&token=ff58ab17-4111-40b7-91a3-8f922ca78559)
