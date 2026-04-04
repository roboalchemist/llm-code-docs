# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent.md

# Add skills to agent

Skill is part of an agent that is specialized to understand and handle a specific task in the user conversation flow. **Example**: 'Order Pizza' skill in a Pizza agent is responsible for taking the user through a conversation to capture data necessary to order a pizza. &#x20;

A new agent in the Avaamo Platform is already available with certain [built-in skills](#built-in-skills) (**Greeting**, **Unhandled**). You can also create various [custom skills](#custom-skills) from scratch using an interactive skill builder as per your business needs or [import a skill](#import-skills) closest to your business and edit the imported skill, as required.

{% hint style="success" %}
**Key Point**: Although you can specify the unhandled prompt response at an individual skill level, specifying in the built-in skills at the agent level provides a centralized approach to compare results across multiple skills and then generate a response. **Example:** In a **Pizza agent**, for an unhandled skill, you can check for a specific skill type (Order skill) and then display an unhandled message "Sorry, I am unable to understand your request. Can I connect you to a customer service representative for ordering a pizza?".&#x20;
{% endhint %}

See [Manage skills](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill), for more information on how to edit, update, delete, and publish skills to the Skill store.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills to the agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
  * In the **Agent** page, navigate to the **Skills** option in the left navigation menu to view all the pre-built skills and custom skills.&#x20;
    {% endhint %}

## Built-in skills

The following lists the pre-built skills available in the agent. You can customize these skills as required:

* [Greeting skill](#greeting-skill)
* [Unhandled skill](#unhandled-skill)
* [Smalltalk ](#smalltalk)
* [Frustration](#frustration)
* [Outro Skill](#outro-skill)

### Greeting skill

You can use the prebuilt **Greeting** skill in the agent for adding a customized welcome message to the user.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M14VuSNtEuXySBMsOPX%2F-M14XcaV2Bf4gMY38_58%2FGreeting%20Skill.gif?alt=media\&token=81f21400-65ba-45e3-881b-9f695d1f4ebd)

**To add greeting message to agent**:

* In the **Agent -> Skills** page, click **Greeting** skill.
* In the **Greeting message** pop-up, customize the message as required and click **OK**. You can add different types of responses (a card, quick reply, carousel, etc..) in the message. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOlUs1Wpd70H3-45t6e%2F-MOlVhanSQiTzyDoix4A%2F5.5-greeting-skill-message.png?alt=media\&token=2f5eec23-8725-4756-92ff-419d0618eefa)

* Click **Save.**
* Click the agent icon in the bottom-right corner to view the customized welcome message. Note that if you have deployed the agent in C-IVR channel, then you get the option to choose Web or C-IVR channel

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-8eWMN39BXr74g0KM-%2F-M-8fHSkKlUiHFCjF3WJ%2Fqs-greeting-message-result.png?alt=media\&token=4946305c-f7df-4353-ab67-46b61f6d45aa)

### Unhandled skill

You can use pre-built **Unhandled** skill in the agent for adding a customized response for unhandled user queries.

When a user query is not understood by the agent, it responds with the unhandled intent. By default, "***I am sorry. I don't have an answer for that.**"* is the unhandled response by the agent. However, you can customize the response in your agent by adding other options for linking to different pages, additional questions, or search on different pages, or even detect spam in the **Unhandled** skill.

**To add an unhandled message to the agent**:

* In the **Agent** **-> Skills** page, click **Unhandled** skill.
* In the **Skill message** pop-up, customize the message as required and click **OK**. You can add different types of responses (a card, quick reply, carousel, etc..) in the message. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.
* Click **Save.**

**Example**: Consider that in the **Pizza** **agent,** you are required to process the unhandled intent as follows:

1. For any unhandled query during a pizza order, you wish to redirect the user to the website for more options to search.&#x20;
2. For all other unhandled queries, you wish to provide an option to the user for transferring to a live agent.&#x20;

You can write JS code in the **Unhandled skill** to handle such scenarios.

### Smalltalk

Avaamo Platform provides a built-in Smalltalk skill with the most frequently encountered casual conversations the users can have with the agent.&#x20;

This is a **read-only** skill. If you wish to customize the Smalltalk, then you can create a custom Smalltalk skill according to your business requirements. See [Build skills using Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* Smalltalk does not participate in disambiguation. See [Disambiguation](https://docs.avaamo.com/user-guide/overview-and-concepts/intents#disambiguation), for more information.
* If you have the same intent in the system Smalltalk and custom Smalltalk, then the response from the custom Smalltalk takes precedence.
  {% endhint %}

### Frustration

Avaamo Platform provides a built-in frustration Smalltalk skill to detect and respond to user frustration queries. This is a **read-only skill**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOkaU0s3NAIReCG4ebz%2F-MOkdtd3uvd_WO4Reuys%2Ffrustration-smalltalk.png?alt=media\&token=2a6969e0-4981-4edc-a501-22c46eeebffa)

Click **Talk to Customer Rep** to view the skill response.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOkenhijbLqlR5q_yjd%2F-MOkf1XyALchPWK4qQyw%2Ftalk-to-customer-rep.png?alt=media\&token=50151739-06ab-40b5-b99b-69c6520c3fa0)

If you wish to customize the Smalltalk, then you can create a custom Smalltalk skill according to your business requirements. See [Build skills using Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer), for more information.&#x20;

Note that you must first remove the system frustration Smalltalk from the Live agent settings, for the customized frustration Smalltalk responses to get triggered. See [Live agent transfer rules in Pre-built live agent](https://docs.avaamo.com/user-guide/how-to/configure-agents/switch-to-live-agent/pre-built-live-agent#live-agent-transfer-rules), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEwLhDmAtO8Efh0G3pQ%2F-MEwM5hExri12Mm9G7vj%2FScreenshot%202020-08-17%20at%205.44.29%20PM.png?alt=media\&token=dd57f47e-0fa9-4e39-9027-3b972e880305)

### Outro skill

The Outro skill allows you to create and post a customized message to the user after an agent’s response. It can be used in skills that produce single-instance responses, such as [Dynamic Q\&A, ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a)[Dialog](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer),[ ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a)and [LLaMB](https://docs.avaamo.com/user-guide/llamb) skills. It improves the user experience by providing a clear, standardized message after the agent responds as per your business requirements. It helps to streamline and provide consistent communication across all interactions.&#x20;

A common use case is to post disclaimers or system-generated messages, such as `This is a system-generated message, please do not reply` after the agent's response say in a Dynamic Q\&A skill.&#x20;

{% hint style="success" %}
**Key points:**&#x20;

1. The Outro Message is not displayed after the Dynamic Q\&A response if an [Outro message](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-avaamo-answers-1/intro-outro-messages#outro-messages) is already added within the Dynamic Q\&A skill
2. This feature is available only for [Classic](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills) and [Advanced](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced) Agents.
3. The Outro message is displayed after the agent's response only when there is no idle prompt configured for that particular node/intent.
4. These are not applicable for `Custom small talk.`
   {% endhint %}

**To create an Outro skill:**

* In the `Agent page`, navigate to the `Skills` option in the left navigation menu.
* On the Skill Builder page, select `Outro` in the `Built-in Skills` section.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKkMsFqyncKw8XlbT7CFb%2FScreenshot%202024-08-20%20at%2011.44.27%E2%80%AFAM.png?alt=media&#x26;token=7535a1f4-1813-4ff9-bf06-d36f128ec20d" alt=""><figcaption></figcaption></figure>

* Customize the message as required in the Outro message pop-up and click `OK`. You can add different types of responses (a card, quick reply, carousel, etc..) in the message.  See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.
* You can apply the Outro skill to different skills using a response filter. After adding the response, assign the response filter such as [Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a), [LLaMB](https://docs.avaamo.com/user-guide/llamb), or [Dialog](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer). The outro message is displayed only for the agent responses of that selected skill.  To apply the outro message for all the skill responses, leave the response filter blank.

**Case 1:** In the following illustration, a outro message is configured to be displayed for all the Dynamic Q\&A responses:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FpdsNJ4V1B31kYepEKKtp%2Fimage.png?alt=media&#x26;token=e88457cb-6b67-4ea4-8132-5fb8f3f45212" alt=""><figcaption></figcaption></figure>

In the agent response, the message configured in the outro skill is displayed providing an enriched experience to the user.

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXmvIMOwgPLRq7YGyQjHE%2Fimage.png?alt=media&#x26;token=0c24f5c7-750a-4452-901c-c25ea8c23cbe" alt="" width="375"><figcaption></figcaption></figure></div>

**Case 2**: You can utilize custom code to create a specific dialog skill as a response filter. This allows you to apply Outro messages to a particular skill.

In the following example, `view_bookings` is used as the skill key. Implement the custom code `return (context.insights.skill_key == "<<skill_key>>");` to define the dialog skill as the response filter.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FTBlATUTgCrUoF0qhdIg4%2FScreenshot%202024-08-21%20at%201.55.35%E2%80%AFPM.png?alt=media&#x26;token=af5b34e5-e7ee-40ef-802d-a9ff08ea8498" alt=""><figcaption></figcaption></figure>

When configuring the Outro skill, you can select this response filter as demonstrated below.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FRBYu5rGFbYJTnDZMHSOW%2FScreenshot%202024-08-21%20at%202.18.42%E2%80%AFPM.png?alt=media&#x26;token=2a7f3267-0fe4-4722-a3c0-582289c79347" alt=""><figcaption></figcaption></figure>

**Example 1: Simple Outro Skill**

* Messag&#x65;**:** "Thank you for chatting with us. Have a great day!"
* Response filters: No response filters selected.
* Applicatio&#x6E;**:** Applied to all the responses for all the skills like LLaMB, Dialog, and Dynamic Q\&A.&#x20;

**Example 2: Customized Outro for Specific Skill Type**

* Messag&#x65;**:** "This concludes our session on product information. If you have more questions, feel free to ask!"
* Response filters: Dynamic Q\&A
* Applicatio&#x6E;**:** Applied to all the responses of the Dynamic Q\&A skill.

## Custom skills

Based on your business requirements, you can create either a new skill from scratch or by importing from any of the sample skills. See [Import skills](#import-skills), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ft18M3veUqeO3QvZQgJ4n%2FScreenshot%202025-06-27%20at%2011.50.59%E2%80%AFAM.png?alt=media\&token=e6128c8d-32fe-4974-8b14-7591c49804f5)

{% hint style="success" %}
**Key point**: &#x20;
{% endhint %}

**To create a new custom skill in an agent**:

* In the **Agent -> Skills** page, click **Add skill**.
* You can add the following types of skills on the **Skill builder** page:

  * [Dialog](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer): Use this skill to build a multi-step conversational flow. You can create, design, and edit conversational flows quickly with minimal technical expertise. Typically, the Dialog skill is used for any custom skill that cannot be built using other skill types. **Example**: Create complex multi-turn conversations such as building flow for diagnosing a patient using symptoms.
  * [Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a):  Use this skill to create responses for one-off questions and answers. Upload questions and answers or create a custom response to user queries in CSV format. **Example**: Create custom responses in a simple CSV format to certain specific queries on a pizza making, delivery for a **Pizza agent**. Upload the CSV file to enrich your agent and provide accurate responses to user queries.&#x20;
  * [Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk): Use this skill to create responses for informal or casual user conversations. **Example**: Responses for the following sentences:

  ```
  "What is your name?"
  "How was your day?". 
  ```

  * [Answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1): Use this skill to provide answers from your enterprise content. You can create, design, and edit conversational flows quickly with minimal technical expertise.&#x20;
  * [LLaMB](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/llamb): LLaMB: Use this skill to generate AI-powered responses based on enterprise content and context. **Example:** Responses to queries like “What’s the refund policy?” or “How does your product work?”

## Import skills

Instead of creating skills from scratch, you can import from any available published skills in the skill store that is closest to your business and then edit the skill as required. When you import a skill, an exact clone of the skill is created in the agent. Users with the required roles can work on the imported skill in the agent without affecting the skill in the skill store. See [Manage skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M14N5Jwhgc_MSuhEh0v%2F-M14RAyjPeQRpESlvbwH%2FImport%20Skill.gif?alt=media\&token=47a75f68-fa34-4035-9ddc-e50bca27ef74)

**To import a skill**:

* In the **Agent** **-> Skills** page, click **Import skill**.
* In the **Import skill** pop-up, a list of all the skills that are not already imported in the agent is displayed.
* Search and select a skill. Click **Import to Agent**.&#x20;

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-IzXGjsfZj3ekSuT6X%2F-M-J0NppL0bO9_tKZxee%2Fhowto-skill-import.png?alt=media&#x26;token=85d66bc1-688c-4fdf-af99-deb6a2c29394" alt=""></div>

* You can view a copy of the imported skill in the **Custom skills** section.

{% hint style="info" %}
**Notes**:&#x20;

* When you import a skill, an exact independent clone of the skill is created in the agent. Users with the required roles can edit the imported skill in the agent without affecting the skill in the skill store.&#x20;
* Only users with **Edit, Publish,** or **Owner** permission for the agents can import a skill from skills store.&#x20;
* If you import a skill with duplicate entities, then a warning message is displayed. Click Continue to retain the agent copy.
  {% endhint %}
