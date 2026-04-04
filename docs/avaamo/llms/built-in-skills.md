# Source: https://docs.avaamo.com/user-guide/skills/built-in-skills.md

# Built-in skills

## Welcome skill

AI Agents display customized welcome messages across multiple channels — including Web, Microsoft Teams, iOS, and Android. This feature lets you greet users at the start of a conversation with a personalized message, helping create an engaging, guided experience.

#### Supported message types

You can configure different types of welcome messages using the Welcome skill:

* **Text:** A simple text-based greeting or introduction.
* **Card:** A structured message containing visuals or buttons.
* **Quick-reply:** A message with suggested replies for quick user actions.
* **JavaScript:** You can leverage a set of objects and functions to customize and create enterprise skill responses using JavaScript.

**To add a welcome message to the agent**:

* In the `Agent > Skills` page, click `Welcome Message` skill.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FyjIrR7PxGT3cGxthbTLJ%2FScreenshot%202025-12-04%20at%201.19.26%E2%80%AFPM.png?alt=media&#x26;token=dd49d410-d2d2-4667-98b4-5c2e2d7754e1" alt=""><figcaption></figcaption></figure>

* In the `Welcome message` pop-up, customize the message as required, and click `OK`. You can add different types of responses in the message. You can apply the [response filter](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters) to the welcome message.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FrzdmBpXUwCLCrQaALxWu%2FScreenshot%202025-12-03%20at%202.58.24%E2%80%AFPM.png?alt=media&#x26;token=4a15579b-7904-48ab-bf1b-af7bb6c4f7a7" alt=""><figcaption></figcaption></figure>

* Once configured, users can see the welcome message when they start a conversation with the AI Agent, ensuring a smoother, more guided chat experience.

## Outro message

The `Outro message` allows you to create and send a customized message to the user after the AI agent’s primary response. This helps make conversations feel more natural and engaging by suggesting relevant next steps or follow-up actions.

For Example:

After a user books a flight from Delhi to Bangalore, the agent can display the confirmation message and then post an outro message such as:

* “Do you want to book a return ticket?”
* “Would you like to book a hotel in Bangalore?”

By using outro messages, you can guide users toward related actions or offer helpful suggestions without interrupting the main response flow.

{% hint style="info" %}
**Note:** Outro support is available only for function call responses within the prompt skill and applies exclusively to web and digital channels that support text messaging.
{% endhint %}

#### Supported message types

You can configure different types of welcome messages using the Welcome skill:

* **Text message:** A simple text-based greeting or introduction.
* **Card message:** A structured message containing visuals or buttons.
* **Quick-reply message:** A message with suggested replies for quick user actions.

**To add an outro message to the agent**:

* In the `Agent > Skills` page, click `Outro` skill.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FyjIrR7PxGT3cGxthbTLJ%2FScreenshot%202025-12-04%20at%201.19.26%E2%80%AFPM.png?alt=media&#x26;token=dd49d410-d2d2-4667-98b4-5c2e2d7754e1" alt=""><figcaption></figcaption></figure>

* In the `Outro message` pop-up, customize the message as required, and click `OK`. You can add different types of responses in the message.  You can apply the [response filter](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters) to the outro message.

{% hint style="info" %}
**Note:** Predefined response filters (`Dialog` and `LLaMB Skill`) are available for the `Outro Message Skill.`
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FX8gVwgc2VM66xkpRDmzS%2FScreenshot%202025-10-27%20at%2012.07.35%E2%80%AFPM.png?alt=media&#x26;token=a196cdfb-dd49-4a3b-a557-151c3b71c8cd" alt=""><figcaption></figcaption></figure>

### **To create an outro, follow these steps:**

1. **As a prerequisite, create a custom response filter:**

   * Navigate to **Settings** and create a custom response filter.
   * The executed tool function information will be available in the context.
   * Refer to the [Response filters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters) documentation for guidance on creating a custom response filter.

   **Example:**

   ```javascript
   console.log(context);
   return context.toolFunction.name == 'bookFlight';
   ```
2. **Add the outro response:**
   * Go to the **Skill** page and click **Outro**.
   * Add your desired outro response and attach the response filter created in step 1.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FBPXjlDQf75Wb49wZKz1K%2FScreenshot%202025-10-07%20at%204.58.28%E2%80%AFPM.png?alt=media&#x26;token=08b967da-985a-4a8b-acb4-af147e526060" alt=""><figcaption></figcaption></figure>

Once the agent executes the tool function (e.g., `bookFlight`), the outro evaluation is triggered. Based on the defined criteria in the response filter, the appropriate outro message is selected and sent to the user.
