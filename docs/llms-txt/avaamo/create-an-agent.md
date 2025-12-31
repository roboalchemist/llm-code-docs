# Source: https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent.md

# Create agent

Avaamo Platform is a robust, flexible, and easy-to-use platform that allows you to build a wide variety of agents for different domains with just a few clicks. This section walks you through the steps of quickly creating a basic agent in the Avaamo Platfor&#x6D;**.**

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites) before creating a new agent.
{% endhint %}

{% hint style="success" %}
**Key point**: As you start building your first agent in the Avaamo Conversational AI Platform, it is also recommended to know a few simple commands that are very useful. See [Agent commands](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/skill-commands), for more information.
{% endhint %}

## Build an agent

Consider that you are required to build a Pizza agent for "MacPizza - a Quick Service Restaurant", where you can place online orders for pizzas. Your first step is to build a simple "Hello" or "Welcome" greeting message to the user. Iteratively, you can enhance the agent by adding additional skills and other functionalities, as required. See the [Next steps](#next-steps), for more information.

Once you login to the Avaamo Platform, building an agent is just a 3-step process:

1. [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent)
2. [Add greeting message to agent](#step-2-add-greeting-message-to-agent)
3. [Test and view agent in action](#step-3-test-and-view-agent-in-action)

{% embed url="<https://youtu.be/nt69KsGpHSY>" %}

### Step 1: Create agent

An agent is an intelligent dialogue system that interprets and responds to the user’s conversation in natural language. It is a container of skills, each specialized to understand and handle a specific task in the user conversation flow. **Example**: In the Pizza agent, you can create an "Order Pizza" skill responsible for handling all pizza orders, similarly you can create a "FAQ" skill to handle all the Mac Pizza FAQs.

**To build an agent**:

* In the Avaamo Platform UI, click the **Agents** option in the top menu, navigate to the **My agents -> Development** tab, click **Create agent**.
* Enter the following required details and click **Create agent**:
  * **Name**: Indicates the display name of your agent.
  * **Description**: Indicates a brief description of your agent.

{% hint style="info" %}
**Note**: Since this is your first agent, specify only the required details and skip the other details for now. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more detailed information.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-9O49kPNpSyyTEEhxz%2F-M-9PCx5ZJmb0bHZl-yL%2Fqs-create-pizza-agent.png?alt=media\&token=860318a8-767a-4c05-9b46-684462f6bb4b)

A new empty agent is created. The next step is to add a greeting message and other custom skills as per your business needs.

### Step 2: Add greeting message to agent

A new agent in the Avaamo Platform is already available with certain built-in skills. See [Built-in skills](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent#built-in-skills), for more information.

You can also create various custom skills using an interactive skill builder as per your business needs. See [Build skills](https://docs.avaamo.com/user-guide/how-to/build-skills), for more information.

For the welcome message, you can use the pre-built Greeting skill already available in the agent.

**To add a greeting message to the agent**:

* In the **Agent** page, navigate to the **Skills** option in the left navigation menu.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-8dQjXl0dh5OfxjsoK%2F-M-8dlrcUymNQl22RHj5%2Fqs-create-pizza-agent-greeting.png?alt=media\&token=b67d98f1-14a6-451b-bf22-eda5e1fb8b5a)

* Your agent is already available with certain sample skills. Click Greeting skill.
* In the **Skill message** pop-up, customize the message as required and click OK. You can add different types of responses (card, quick reply, carousel, etc..) in the message with response filters and tags. Since this is your first agent, you can just add a simple text message.
* Click **Save**. Your first agent is ready for testing now.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOk1q_Mjhbh738Spjhk%2F-MOk6ilcNCU1tgKD4vjg%2Fagent-welcome-message-simple.png?alt=media\&token=520be672-7cfb-407b-867d-1f35ab399989)

### Step 3: Test and view agent in action

In the **Agent** page, click the agent icon in the bottom-right corner. You can view your customized welcome message in the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-8eWMN39BXr74g0KM-%2F-M-8fHSkKlUiHFCjF3WJ%2Fqs-greeting-message-result.png?alt=media\&token=4946305c-f7df-4353-ab67-46b61f6d45aa)

## Next steps

Now that you have successfully built the first agent with a welcome message, you can dig deeper to learn the rich features available in the Avaamo Platform, and enhance the agent conversational flow to provide a great user experience. This document is built around the MacPizza agent use case. The next steps enable you to add and test the following skills in the agent:

* [Add Answers skill](https://docs.avaamo.com/user-guide/quick-start-tutorials/add-answers-skill)
* [Add LLaMB skill](https://docs.avaamo.com/user-guide/quick-start-tutorials/add-llamb-skill)
* [Add Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a)
* [Add Smalltalk skill](https://docs.avaamo.com/user-guide/quick-start-tutorials/add-smalltalk-skill)
* [Add Dialog skill](https://docs.avaamo.com/user-guide/quick-start-tutorials/add-dialog-skill)
