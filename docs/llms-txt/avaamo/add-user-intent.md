# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent.md

# Add user intent

You can build a conversational dialog flow by adding nodes with user intents and skill responses in the Dialog skill page.&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
* The quality of the intents and their training determines the quality of the agent's accuracy in understanding the user queries. See [Design skill](https://docs.avaamo.com/user-guide/how-to/design-skill#intent-and-training-phrases), for more information on intent training guidelines.
  {% endhint %}

{% hint style="success" %}
**Key point:** See [Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence), for more information on intent execution priority.
{% endhint %}

**To add user intents**:

* In the **Dialog skill** page, click **Edit** to unlock the skill.
* Click the **Implementation** option in the left navigation pane.&#x20;
* Add user intents by creating a new node in one of the following ways:
  * Click the **plus (+)** icon to add a new user intent and skill response in the node below the current node.
  * Click the **fork** icon to add a new user intent and skill response as a forked branch to the current node.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma7bIuRq5MKOQJmzUGc%2F-Ma80SBNObJgy5nLYK_I%2F5.7-dialog-add-user-intent.png?alt=media\&token=f7fcc81f-4e3e-4252-a631-32b3b94aaba9)

* Click the red call-out bubble above "Add agent Response" to add an Intent.
* Specify the following details in the user intent:

<table><thead><tr><th width="188.16438356164383">Parameters</th><th width="357.3506614495994">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent name</td><td><p>Indicates the name of the intent. </p><p></p><p>Each intent name must be unique within the skill.</p></td><td align="center">192 characters</td></tr><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. </p><p></p><p>By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p><p></p></td><td align="center"></td></tr><tr><td>Intent type</td><td>Indicates the type of user intent. You can add one of the following intent types - <a href="#training-phrases">Training Phrases,</a> <a href="#existing-entity">Existing Entity</a>, <a href="#system-intent">System Intent</a>, and <a href="#custom-code">Custom Code</a>, based on your business requirements.</td><td align="center">N/A</td></tr><tr><td>Post-processing</td><td>Indicates any JS that is executed after the intent is invoked and before displaying the skill response. See <a href="../../customize-your-skill">Build skill responses using script and code</a>, for more information.</td><td align="center">N/A</td></tr></tbody></table>

## Intent types

In a Dialog skill, you can add the following types of intent for a node in the flow - Training Phrase, Existing Entity, System Intent, or Custom Code.

### Training Phrases

These are the inline user intents (utterances or phrases) in the conversation flow.&#x20;

**Example**: I want to order pizza, I want a pizza delivery.

* **Intent Type**: Select Training phrases.
* **Training Phrases**: Enter the training phrase and click Add. You can continue to add multiple training phrases, as required. Based on the training phrases, the slots are automatically filtered for you.&#x20;
* **Add training set**: This allows you to add training data in different languages. It is not required to train your skill in English only, you can train your skill in different languages.&#x20;
  * Add language in **Configuration -> Languages** and save the skill.&#x20;
  * Click **Add training set** in Invocation Intent.&#x20;
  * Select the required language and add the training set in the selected language.
* Click **Save**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb11TIV2288hWmBqzf6%2F-Mb12ndAu6V0DAkKjxaN%2F5.7-dialog-intent-training-phrase.png?alt=media\&token=85ac114a-fd5f-46d2-aa58-2c1cda62cc16)

{% hint style="info" %}
**Notes**:&#x20;

* You can specify Training phrases upto 300 characters.
* If you want training data that must match specific and generic queries, then it is recommended to provide generic training data. **Example**: If you wish to match "I want my fund value" and "I want fund value", then it is recommended to use "I want fund value" in the training data.
  {% endhint %}

### Existing Entity

These are intents with entities. Note that only the entities added to the skill in the **Invocation intent** page are displayed in the list. See [Invocation Intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information on adding entities to the skill.&#x20;

**Example**: Consider that in the Order Pizza skill, the first message asks the user for the type of pizza - veg, non-veg. In return, you can specify an intent with these entities to process the user response and proceed further in the conversation flow.

* **Intent type**: Select an Existing Entity.
* **Select entity**: Start entering the entity type and the results are automatically filtered out in the list. Choose an entity from the list. You can add only one entity to user intent.&#x20;
* **Select entity value (Optional)**: Choose the values from the selected entity type. Only these values are matched in the user intent. Example: Consider the "pizza\_type" entity type with cheese, corn, and pineapple as values. You have selected "pizza\_type" in the user intent and only cheese and corn in the entity value. In this case, a user intent "I want to order veg pineapple pizza" is not matched to this node.
* **Training data (Optional)**: Enter the training phrase and click Add. You can continue to add multiple training phrases, as required. You can add a combination of training data with an existing entity. This enables you to specify a stricter or restricted match of a user query that contains the selected entity. See [What if I have both training phrases and an existing entity in a user intent? How is the behavior defined?](#1.-what-if-i-have-both-training-phrases-and-an-existing-entity-in-a-user-intent-how-is-the-behavior) for more information on how matching is defined with an example.
* Click **Save**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb11TIV2288hWmBqzf6%2F-Mb13C9z_VypruSg1D7l%2Fdialog-user-intent-entity.png?alt=media\&token=50ee764a-7be3-4a71-8599-3d1cf3bd47ef)

### System intent

These are the system intents with pre-defined training phrases already available in the platform. The following system intents are supported in the platform - yes, no, frustration, live agent, cancel, repeat, go back, thank you.&#x20;

**Example**: Consider that you wish to respond to the user's frustration by transferring to a live agent or via collecting feedback. You can create a user intent with frustration system intent and add a skill response to transfer to a live agent.

* Select the **Intent type** as **System**.
* In **Select entity**, you can start entering the entity type and the results are automatically filtered out in the list. You can add only one entity to a user intent
* Choose the entity type from the list and click **Save**.&#x20;

### Custom Code

These are intents with custom JavaScript code.&#x20;

**Example**: You can create a custom intent with a regular expression to match the pizza order number entered by the user. Alternatively, you can also create an entity with a regular expression. Note that goto\_node is not supported in the custom intent handler, you must return true or false in this handler.&#x20;

* Select the **Intent type** as **Custom code**.
* Provide JavaScript in the Custom intent handler and click **Save**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb13EdXe79533aZbVXP%2F-Mb13ViuJ4MB7uMvfyq5%2F5.7-dialog-user-intent-custom-code.png?alt=media\&token=42546463-239a-46ff-82b4-48d28e4871c2)

## Frequently asked questions (FAQs)

### 1. What if I have both training phrases and an existing entity in a user intent? How is the behavior defined?

Consider that you have specified both a training phrase and an existing entity in a user intent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb13loCjFcAEE_RE9oo%2F-Mb13rm1G7wN6TXl68vz%2F5.7-dialog-user-intent-entity-plus-training-phrase.png?alt=media\&token=85cb06ea-ddc5-4dee-a4b3-b1cfb9808476)

The following table depicts how the intent matching to a user query works in this case:

| User query                                                                                                                  | User intent match |
| --------------------------------------------------------------------------------------------------------------------------- | :---------------: |
| With just date entity value. Example: Today, Tomorrow, 04 Jan 2000                                                          |        Yes        |
| Training data with entity value. Example: "I celebrate my birthday today"                                                   |        Yes        |
| Training data without entity value. Example: "I celebrate my birthday"                                                      |         No        |
| A user query other than those mentioned in the training data with entity value. Example: "I celebrate my anniversary today" |         No        |

### 2. What is the maximum length of the training phrases?

You can specify Training phrases up to 300 characters.&#x20;

### 3. What are the best practices of training phrases or training data?

The quality of the intents and their training determines the quality of the agent's accuracy in understanding the user queries. See [Design skill](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill), for more information on intent training guidelines.

### 4. What is the intent execution sequence in a Dialog skill?

When a user posts a query to an agent, the agent understands and classifies the input and then selects an appropriate skill to engage with the user. Avaamo Platform evaluates all the intents and the intent with the best possible match is considered. There are three skills considered during intent execution - Dialog, Q\&A, and Smalltalk.&#x20;

If a Dialog skill is invoked at the agent level, then there is a specific order in which the intent within the Dialog skill gets executed. See [Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence), for more information.
