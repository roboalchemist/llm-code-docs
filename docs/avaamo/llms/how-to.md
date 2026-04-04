# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to.md

# How-to

All the scenarios are based on the MacPizza agent use case, where you are building a skill for Mac Pizza - a Quick Service Restaurant to place orders for pizzas.&#x20;

## Before you begin

The following are generic steps for all the How-to topics listed in this section:

* Ensure you have met all the [pre-requisites](applewebdata://E72AA735-5E27-4FEA-9818-F9DC6DD2ACD7/@avaamo/s/avaamo/~/drafts/-LwMqtgHWkBhIW87lD6g/quick-start-tutorials/pre-requisites).
* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](applewebdata://E72AA735-5E27-4FEA-9818-F9DC6DD2ACD7/@avaamo/s/avaamo/~/drafts/-LwMqtgHWkBhIW87lD6g/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9ae47367-043d-436a-bab1-053a8b89e2a1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.
  * Click **Edit** to unlock the agent before editing.
  * In the **Agent** page, navigate to the **Skills** option in the left navigation menu. Search and open the required skill. See [Search skill](applewebdata://E72AA735-5E27-4FEA-9818-F9DC6DD2ACD7/@avaamo/s/avaamo/~/drafts/-LwMqtgHWkBhIW87lD6g/how-to/build-skills/manage-skill#search-skill), for more information.

{% hint style="success" %}
**Key Point**: It is recommended to have a good working knowledge of JavaScript, HTML, and CSS.
{% endhint %}

## Learn how-to&#x20;

This section describes how-to customize skills with a rich set of objects and functions provided in the Avaamo Platform using certain common scenarios.

### Use Context

The following scenarios are covered to explain the usage of the context object :

* [Get user details](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/to-get-user-details)
* [Get last message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-last-message)&#x20;
* [Get entity and slot details](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-domain-entity-details)
* [Create context variables ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-variables)
* [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties)
* [Detect user device](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/detect-channel)
* [Switch user’s language](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/switch-users-language)
* [Transfer to live agent](https://docs.google.com/document/d/1kLeCPObAeXeon6viGnywY3_9HQxSmfs-YS-xB561Ekg/edit#heading=h.b0a7f5vp0nz8)
* [Get skill conversation insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-insights)

See [context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context), for more information on attributes supported in the context object.

### Use Storage

&#x20;The following scenarios are covered to explain the usage of the storage object :

* [Set and get global variables](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/using-storage#set-and-get-global-variables)
* [Set and get user variables](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/using-storage#set-and-get-user-variables)

See [storage](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/storage), for more information on attributes supported in the storage object.

### Control Skill Flow

You can control the navigation of skill flow in one of the following ways:

* [Using post processing](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/controlling-skill-flow#using-post-processing)
* [Using JS output](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/controlling-skill-flow#using-js-output)

See [Flow Control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more information on various functions supported to control skill navigation flow.

### Send Notifications

You can send SMS and email notifications to the users from skill. The following scenarios are covered:

* [Using Email](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/sending-notifications#email-notification)
* [Using SMS](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/sending-notifications#sms-notification)

### Customize Skill UI&#x20;

You can programmatically customize skill UI in the following ways:

* [Build dynamic skill response](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
* [Create custom HTML web view](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/create-custom-html-web-views)
* [Define custom intents](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/define-matching-rules-using-custom-intents)

### Integrate with API

Seamlessly integrate skill response with [REST](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/integrate-with-api-1#rest-api) and [SOAP](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/integrate-with-api-1#soap-api) API using a simple fetch call.&#x20;
