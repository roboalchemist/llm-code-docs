# Source: https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.3.x/release-notes-v6.3.0.md

# Release notes v6.3.0

The Avaamo Conversational AI Platform v6.3.0 release includes 8 **enhancements** and in order to make the navigation around the enhancements easier, they are classified as follows based on the modules in the Avaamo Conversational AI Platform:

<table><thead><tr><th width="189.95869549449768">Module</th><th width="590.4285714285713">Enhancements</th></tr></thead><tbody><tr><td>SMS channel v2.0 </td><td><ul><li><a href="#deploy-one-agent-across-multiple-sms-channel-instances">Deploy "one" agent across multiple SMS channel instances</a></li><li><a href="#authenticate-users-before-sending-sms-messages">Authenticate users before sending SMS messages</a></li><li><a href="#new-sms-channel-outbound-api">New SMS channel outbound API </a></li><li><a href="#sms.send-function-update-to-include-from_phone">SMS.send function update to include "from_phone"  </a></li></ul></td></tr><tr><td>MS Teams </td><td><ul><li><a href="#hero-card-support">Hero card support</a></li><li><a href="#translation-support-in-hero-cards">Translation support in Hero cards</a></li></ul></td></tr><tr><td>Live agent</td><td><a href="#live-agent-avatar">Add a unique live agent avatar to easily distinguish it from your virtual assistant</a></td></tr><tr><td>Agent</td><td><a href="#parallel-development">Parallel development of Agents</a></td></tr></tbody></table>

{% hint style="danger" %}
**Removal notice**: In this release, the **FB camera effect** feature support is removed from the Avaamo Conversational AI Platform. See [Removal notice](#removal-notice), for more information.
{% endhint %}

## SMS Channel v2.0

In this release, a new version of the SMS channel - **SMS channel v2.0** has been introduced. The new version of the SMS channel is a significant revamp of the existing SMS channel. The following are the key highlights of the SMS channel v2.0:

* [Deploy "one" agent across multiple SMS channel instances](#deploy-one-agent-across-multiple-sms-channel-instances)
* [Authenticate users before sending SMS messages](#authenticate-users-before-sending-sms-messages)
* [New SMS channel outbound API](#new-sms-channel-outbound-api)
* [SMS.send function update to include "from\_phone"  ](#sms.send-function-update-to-include-from_phone)

### Deploy "one" agent across multiple SMS channel instances

In this release, you can deploy "one agent" across multiple instances of an SMS channel. The following lists a few use cases where this feature can be useful:

**Use-case 1: Collect unified analytics:** Provide unified analytics cutting across different instances of SMS channels. See [Channel analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#channels), for more information,

**Use-case 2: Maintain different user sessions:** For security reasons, you can deploy your agent across multiple instances of an SMS channel with different authentication mechanisms. See [Custom user authentication](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sms#custom-user-authentication), for more information.

The following illustration depicts two SMS channels configured for the same agent. One SMS channel has custom user authentication enabled and the other channel is without custom user authentication:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7WyCzGziaUTGaofxSKcM%2F6.3-multiple-SMS-channel.png?alt=media&#x26;token=0f767c2f-d0a8-470d-89b1-8c4e9e8af930" alt=""><figcaption></figcaption></figure>

See [Deploy in multiple SMS channel instances](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sms#deploy-in-multiple-sms-channel-instances), for more information.

### Authenticate users before sending SMS messages

In this release, the SMS channel configuration has been enhanced with the **Custom user authentication** option. You can use this option along with the new [SMS channel outbound API](#new-sms-channel-outbound-api) to authenticate users in the [User authentication handler](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#user-authentication-handler) before sending an SMS. This helps secure communication between the user and the agent via the SMS channel.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGvQ8mAuoG8ryuLwDNvSx%2F6.3-custom-user-authentication-sms.png?alt=media&#x26;token=ddbeb6b4-8a9a-421f-9315-fed68b78f43d" alt=""><figcaption></figcaption></figure>

See [SMS channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sms), for more information. Also see [Custom user authentication](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#sms-channel), for an example.

### New SMS channel outbound API

In this release, as a part of SMS channel enhancement, a new REST API - **SMS channel outbound API** has been introduced.&#x20;

Using this API, you can post an agent's greeting message as an SMS to the specified phone number. The recipient can respond back to the SMS channel, and based on the way you have implemented your agent it can initiate a conversational dialogue with your agent.&#x20;

This API also allows you to pass any custom parameters as per your requirement in the body payload that can be used to authenticate users before sending SMS messages. See [Authenticate users before sending SMS messages](#authenticate-users-before-sending-sms-messages), for more information.&#x20;

{% code overflow="wrap" %}

```json
// API Signature

https://cx.avaamo.com/sms/<<channel_uuid>>/send.json

// Sample cURL request

curl --location --request POST 'https://cx.avaamo.com/sms/3ad87fb7-c43e-4f00-8441-xxxxx/send.json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "John",
    "last_name": "Jacob",
    "emp_id": "1234",
    "to_phone": "+1 (xxx) xxx-xxxx"
  }'

```

{% endcode %}

See [SMS Send API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/sms-send-api), for more information.

### SMS.send function update to include "from\_phone"

In this release, the `SMS.send` built-in function has been enhanced to include optional `from_phone` parameter. This helps users to identify the number from which the SMS was sent to the user.

{% code overflow="wrap" %}

```javascript
// SMS.send signature

SMS.send("message", ["phoneNumber1","phoneNumber2",...],*{from_phone: channelPhone});

// SMS.send example

SMS.send("Successfully placed your order", ["+16503835663", "+919999988888"], {from_phone: "+19809890090"});

```

{% endcode %}

See [SMS.send](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/notifications#sms.send), for more information.

## MS Teams channel enhancements

In this release, the MS Teams channel has been enhanced with the following features:&#x20;

* Add customized cards such as **Hero cards**. With this enhancement, you can now create rich text responses in the MS Teams channel.&#x20;
* Translate the responses of Hero cards based on the language switched to during the agent conversation. With this enhancement, you can render rich card elements using Hero cards in all the languages supported in the Avaamo Platform.&#x20;

### Hero card support

In this release, the MS Teams channel has been enhanced with the ability to add customized cards such as **Hero cards**. With this enhancement, you can now create rich text responses such as Cards, ListView, and Carousels in the MS Teams channel.&#x20;

The format to use the Hero cards remains the same as supported in the MS teams. The only addition is to wrap the JSON of Hero cards in `CustomTeamsMessage`  object. See [Hero cards in MS teams](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#hero-card), for more information.&#x20;

The following is a sample Hero card JSON structure to render a simple card:

{% code overflow="wrap" %}

```json
return {
  "CustomTeamsMessage": {
    "type": "message",
    "attachments": [
      {
        "contentType": "application/vnd.microsoft.card.hero",
        "content": {
          "title": "Special offers!!!",
          "subtitle": "Avail some of the best course offers of the season",
          "text": "<div class='tabular-disp'> <div class='section-title'>Free course</div> <div class='section'> <div class='property'><div class='prop-name 'style='background-color: #add8e6;'>Course 1: Introduction to Machine Learning</div><div class='prop-value '>John Miller </div><div class='prop-value '>Date: Dec 2nd and Dec 10th </div></div><div class='property'><div class='prop-name 'style='background-color: #add8e6;'>Course 2: How to build a Chatbot?</div><div class='prop-value '>Mark Smith </div><div class='prop-value '>Date: Dec 12th and Dec 15th </div></div></div></div>"
        } 
      }
    ]
  }
}
```

{% endcode %}

The following illustration represents how the card is rendered in the MS teams channel:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FonkHSGytEHwbtdpEP42P%2F6.3-hero-card.png?alt=media&#x26;token=7336409e-9c68-4386-bccb-76d069160bc4" alt=""><figcaption></figcaption></figure>

See [Hero card support](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#hero-card-support), for more information and examples.

In the earlier release, Hero cards were not supported in the MS Teams channel, hence there was limited support in rendering rich card elements.&#x20;

### Translation support in Hero cards

In this release, the MS teams channel has been enhanced with the ability to **translate the responses of Hero cards** based on the language switched to during the agent conversation. Note that you can only switch to those[ languages configured](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages) in your agent.&#x20;

With this enhancement, you can render rich card elements using Hero cards in all the languages supported in the Avaamo Platform. See [Supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages), for more information.

Consider that you have configured your agent in the French language. In the agent conversation, you switched the language to French. The following illustration represents the Hero card response rendered in the MS teams channel in the French language:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FavFlO7IQvv0WLrGRBtw0%2F6.3-hearo-card-translation.png?alt=media&#x26;token=dde6ffa2-96a7-4086-a942-3b25270ffbd0" alt=""><figcaption></figcaption></figure>

See [Hero card support](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#hero-card-support), for more information and examples.

## Parallel development&#x20;

For an enterprise agent, as the demand and usage of the agent increase, the number of use cases required to build in the agent also increases substantially. To ensure faster adoption of the increasing agent demand, it is critical to build and deliver the agents faster. Hence, parallel development, which allows multiple developers to work on the agent simultaneously is a key factor in rapid agent development and reduces the turnaround time to build the agent.

Earlier, in the Avaamo Platform as a part of promoting parallel development of agents, the ability to allow parallel development of Dynamic Q\&A, Q\&A, and Smalltalk skills was introduced in release v5.4.0. See [Release notes v5.4.0](https://docs.avaamo.com/user-guide/v5.0-to-v5.8.x-releases/v5.4.x/release-notes-5.4.0#2.-ability-to-allow-parallel-development-of-dynamic-q-and-a-q-and-a-and-smalltalk-skills), for more information.

In this release, the parallel development of an agent has been further enhanced to include two main components of the platform -  Dialog skills and JS files. At a high level, the following changes have been implemented in this release:

* **Ability to independently work on Dialog skills without locking the entire agent**: There is no agent-level lock required to work on a Dialog skill. A lock is now available at the Dialog skill level.
* **Ability to independently work on JS files without locking the entire agent**: No agent-level lock is required to work on a JS file. A lock is now available at the JS file module level. This allows developers to work on multiple JS files parallelly since the lock is at the JS file level and not at the agent level.
* **Activity Monitor - Ability to view details of the developers working on the agent**: Activity monitor is available for every agent that shows the list of users editing the agent at any given point in time. This allows developers to collaborate and work efficiently, thus promoting rapid agent development.

With these improvements, developers can now work parallelly on different skills in the agent.

The following **Activity Monitor** illustration depicts two users simultaneously working on the same agent. One user - John Miller is working on the Dialog skill and another user Tom Wilson is working on a Q\&A intent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNltMqNhsXdvbffoPQnFl%2F6.3-activity-monitor.png?alt=media&#x26;token=c9a3b2a4-e5eb-4b70-a264-5e08e7fc1fde" alt=""><figcaption></figcaption></figure>

Refer to the following topics for a more in-depth understanding:

* [Dialog skills](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer)
* [JS files](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-js-files)
* [Promote and Pull updates](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates)
* [Activity monitor](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/activity-monitor)

In the previous release, the only way to work on a Dialog skill or JS file was to obtain the lock at the agent level. This prevented other developers from working on different skills in the agent. This resulted in slower development and subsequently affected the agent development and delivery time.

## Live agent avatar&#x20;

In this release, the live agent configuration has been enhanced with the ability to add a unique live agent avatar in the **Configuration -> Live agent** page. This feature helps:&#x20;

* Users to easily distinguish a real virtual agent from a virtual assistant.&#x20;
* Developers to abide by the privacy regulations of an organization as in certain organizations there can be a legal requirement to have a different avatar for a real virtual agent versus a virtual assistant.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FToGp3ym5zoWnj7Ym0DzJ%2F6.3-live-agent-avatar.png?alt=media&#x26;token=f9d48275-9b67-49a9-99c3-6316b8626a1a" alt=""><figcaption></figcaption></figure>

The following is an illustration where you can view the live agent avatar when a user initiates chat with a live agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZWuDW43dEyD8kYkNUg4f%2F6.3-live-agent-avatar-chat.png?alt=media\&token=712b357d-9040-4d08-a8f6-ddf26b840123)

See [Live agent avatar](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#live-agent-avatar), for more information.

In the previous release, there was no option to add a different live agent avatar. Hence, it was not clear to the users whether they were having a conversation with the virtual assistant or with a live agent.

## Removal notice

In this release, the **FB camera effect** feature support has been removed from the Avaamo Conversational AI Platform due to a lack of usage.&#x20;

There is no usage observed for this feature since its inception in the v5.0 release dated Jan 15th, 2020, and hence the **FB camera effect** button option is removed for the Card, Carousel, and ListView response types:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2Uk1KwsyVj0Jo4HLRJ82%2F6.3-fb-camera-effect.png?alt=media&#x26;token=4f8d1fe7-33c7-4d6a-8677-6a7ebaa9276f" alt=""><figcaption></figcaption></figure>
