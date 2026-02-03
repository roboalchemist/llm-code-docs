# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/quick-overview.md

# Source: https://docs.avaamo.com/user-guide/skills/dialog-skill/quick-overview.md

# Quick overview

The Dialog skill in AI agents enables you to build agents that behave `deterministically` while still retaining `agentic flexibility`. It combines the structured reliability of dialog flows with the intelligence and spontaneity of AI-driven prompts, making it suitable for complex, real-world conversational scenarios.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxSyiYf35sgCcaKednsfY%2FScreenshot%202026-01-14%20at%202.32.49%E2%80%AFPM.png?alt=media&#x26;token=389d0042-6ed8-40a6-89ef-6d0129589f45" alt=""><figcaption></figcaption></figure>

### How does dialog skill works

A dialog skill is built using two key components:

1. **Prompt skill (orchestrator)**\
   Acts as the entry point for every conversation. It decides `which dialog flow to invoke` based on user input.
2. **Dialog skills (flows)**\
   Handle structured conversations such as ordering, tracking, or support flows. These follow deterministic dialog logic similar to classic dialog skills.

**Conversation flow**

1. User message is first handled by the **prompt skill**.
2. The prompt (orchestrator) identifies the intent using instructions.
3. A function call transfers control to the relevant **dialog skill**.
4. Subsequent messages are handled by that dialog flow.
5. If the dialog skill cannot handle a message, control returns to the orchestrator.

### Key concepts in dialog skill

#### Instructions (replacing training data)

Flow skill replaces rigid training data with **instructions**.

* Instructions define *when* a dialog flow should be invoked.
* They are flexible and expressive (for example, “invoke this flow if the user chooses any non-veg item”).
* This removes the need to maintain long lists of sample utterances.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FF7GqwWbMOXwLM8Qu4D0d%2FScreenshot%202026-01-15%20at%2010.58.48%E2%80%AFAM.png?alt=media&#x26;token=1e5e0f50-c89d-47bf-b201-d44ab7429d57" alt=""><figcaption></figcaption></figure>

Refer [Instructions](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/instructions), for more information.

#### Agentic text&#x20;

Flow skill contains a new response type called **Agentic Text**.

* Instead of static responses, the agent uses instructions to generate responses dynamically.
* Example:\
  \&#xNAN;*“Ask the user what size of pizza they want.”*

This enables more natural, less repetitive conversations.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZCOdcxR1maCaGKmEvG3t%2FScreenshot%202026-01-15%20at%2010.46.44%E2%80%AFAM.png?alt=media&#x26;token=ea7cf07d-a4ca-45c6-af6a-5d12133893aa" alt=""><figcaption></figcaption></figure>

Refer [Agentic text](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#agentic-text), for more information.

#### Entity definition

Entity handling in the dialog skill is simplified and more flexible.

Entities can be defined in one of the following ways:

**Entity**

* Define an entity with a name and a description.
* The description is passed to the LLM to extract the entity value from user input.

Example:

Name: *pizza\_type*

Description: *This is the size of the pizza, which can be small, medium, or large*

**Entity extraction script**

* Use a **JavaScript (JS) block** to extract entities.

{% hint style="info" %}
**Note:** If provided, the extraction script takes precedence over name and description.
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSpP2F52kPnpetIbeiUYO%2FScreenshot%202026-01-15%20at%2010.52.10%E2%80%AFAM.png?alt=media&#x26;token=bdc0f013-015c-432a-98ca-8e8a96438f42" alt=""><figcaption></figcaption></figure>

Refer [Invocation](https://docs.avaamo.com/user-guide/skills/dialog-skill/add-invocation), for more information.
