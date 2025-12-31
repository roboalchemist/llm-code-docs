# Source: https://docs.asapp.com/agent-desk/integrations/whatsapp-business.md

# WhatsApp Business

WhatsApp Business is a service that enables your organization to communicate directly with your customers in WhatsApp through your Customer Service Platform (CSP), which in this case will be ASAPP.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a61e4afea331f6974e9776a9bee783f5" data-og-width="980" width="980" data-og-height="650" height="650" data-path="image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2b5fcaa573c8affad17b068c4678a9d2 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2c48ac9c6e10a416ed0e8c0415a06988 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=6ea9e9fb1035bc821cb92eb4f6439852 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a6375ce3eca78064643d8765cf1cfdd9 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=018ea06cede5d6d3a9dd838dee4692e5 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8fc6036-09ca-5466-d058-e0276eec7922.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=04e48720e8ee7674c07f11eadfe88c11 2500w" />
</Frame>

## Quick Start Guide

1. Create a Business Manager (BM) Account with Meta
2. Create WhatsApp Business Accounts (WABA) in AI-Console
3. Modify Flows and Test
4. Create and Implement Entry Points
5. Determine Launch and Throttling Strategy

### Create a Business Manager (BM) Account

Before integrating with ASAPP's WhatsApp adapter, you must create a Business Manager (BM) account with Meta - visit [this page for account creation](https://www.facebook.com/business/help/1710077379203657?id=180505742745347).

Following account creation, Meta will also request you follow a [business verification](https://www.facebook.com/business/help/1095661473946872?id=180505742745347) process before proceeding.

### Create WhatsApp Business Accounts (WABAs)

Once a Business Manager account is created and verified, proceed to set up WhatsApp Business Accounts (WABAs) using Meta's embedded signup flow in AI-Console's **Messaging Channels** section.

<Note>
  Five total WABAs need to be created: three for lower environments, one for the demo (testing) environment and one for production. Your ASAPP account team can assist with creation of WABAs for lower environments if needed - please reach out with your teams to coordinate account creation.
</Note>

In this signup flow, you will set up an account name, time zone and payment method for the WABA and assign full control permissions to the `ASAPP (System User)`.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=dd2b8c23d3d067b07c7ce9f2acbfc670" data-og-width="551" width="551" data-og-height="493" height="493" data-path="image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f40e2e575ebc8b0e98bf21b62f65fcf9 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4fc3843964d367241dbc07949870313c 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=46ca0b3af38c419f6a2b7cd330dedf81 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=86816639d40f13f7839dac0f04b5a21e 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1687a8ea92822d48c8b0ce0b1d5ca847 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15bf96-9209-4bd7-25cc-67e5ee695259.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2325f7eaac3c3ade6475b69d3d79464a 2500w" />
</Frame>

#### Register Phone Numbers

As part of the signup flow, each WABA must have at least one phone number assigned to it (multiple phone #s per WABA are supported). Before adding a number, you must also create a profile display name, **which must match the name of the Business Manager (BM) account.**

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0b72c603d4520f8b75af6ede0327bbbe" data-og-width="736" width="736" data-og-height="443" height="443" data-path="image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=b5f98447efda9c0bb0ebf0d08112a5b7 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a3f662a0011483101c21e8e436957667 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=78a92c32eaab1feb9d03f2c5e72311a2 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=b30df0b819c5ade33469424fdf492053 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=c3f3fe8b95fef263ef43a322fedf6dfd 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3d34fe68-0d11-0120-d9b2-4a95c1a9ad46.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=43fea3b561dfcf2af52c8149fc57c802 2500w" />
</Frame>

<Note>
  For implementation speed, ASAPP recommends using ASAPP-provisioned phone numbers for the three lower environment WABAs. Your ASAPP account team can guide you through this process.
  All provisioned phone numbers registered to WABAs need to meet [requirements specified by Meta](https://developers.facebook.com/docs/whatsapp/phone-numbers#pick-number).
</Note>

### Modify Flows and Test

The WhatsApp customer experience is distinct from ASAPP SDKs in several ways - some elements of the Virtual Agent are displayed differently while others are not supported. Your ASAPP account team will work with you to implement intent routing and flows to account for nodes with unsupported elements and to validate expected behaviors during testing before launch.

#### Buttons and Forms

All buttons with external links are displayed using message text with a link for each button. See below for an example of two buttons (**Hello, I open a link** and **Hello, I open a view**) that each render as a message with a link:

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=94c991aabedbb17d3773bb14a217781a" data-og-width="646" width="646" data-og-height="1061" height="1061" data-path="image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=835e9405882b2f37baf017c3af9b491c 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d3183a87786c14eb74f267755f897185 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=01bd195905a9bb93eb5c5a270685360a 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=83aa9c41de9847c68e017e98c4b33705 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7d15dcca5a4d0bf5773283020bf38fea 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738af325-85a2-2ecd-3052-7770b9b5ab32.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=cb5a27c724f81219505bd3caec1624ce 2500w" />
</Frame>

Similarly, forms sent by agents and feedback forms at the end of chat also send messages with links to a separate page to complete the survey. Once the survey is completed, users are redirected back to WhatsApp.

#### Quick Reply Limitations

Quick replies in WhatsApp also have different limitations from other ASAPP SDKs:

* Each node may only include up to three quick reply options; a node with more than three replies will be truncated and only the first three replies will be shown.
* Each quick reply may only include up to 20 characters; a quick reply with more than 20 characters will be truncated and only show the first 17 characters, followed by an ellipsis
* Sending a node that includes both a button in the message and quick replies is not recommended, as the links will be sent to the customer out of order

#### Authentication

The WhatsApp Cloud API currently **does not support authentication**. As such, login nodes should not be used in flows that can be reached by users on WhatsApp.

#### Attachments Cards

Nodes that include attachments, such as cards and carousels, are not supported in this channel.

<Note>
  In addition to differences in the Virtual Agent experience, the live chat experience with an agent also excludes some features that are typically supported:

  * **Images**: Agents will not be able to view images sent by customers. The same is true of voice messages and emojis, which are also part of the WhatsApp interface.
  * **Typing preview and indicators**: Agents will not see typing previews or indicators while the customer is typing. The customer will not see a typing indicator while the agent is typing.
  * **Co-browsing**: This capability is not currently supported in WhatsApp
</Note>

### Create and Implement Entry Points

Entry points are where your customers start conversations with your business. You have the option to embed a WhatsApp entry point into your websites in multiple ways: a clickable logo, text link, on-screen QR code, etc.

You can also direct to WhatsApp from social media pages or using Meta's Ads platform to provide an entry point. Ads are fully configurable within the Meta suite of products and will result in no costs incurred for conversations that originate via interactions with them.

<Note>
  ASAPP does not currently support [Chat Instead](/agent-desk/integrations/chat-instead "Chat Instead") functionality for WhatsApp.
</Note>

### Determine Launch and Throttling Strategy

Depending on the entry points configured, your ASAPP account team will share launch best practices and throttling strategies.
