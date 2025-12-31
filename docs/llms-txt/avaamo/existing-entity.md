# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/existing-entity.md

# Existing entity

{% hint style="success" %}
**Key point**: You can add an existing entity only when you have trained a sample query with the required entity extracted in the Invocation intent of the respective skill. For example: If you wish to use say a regex entity `order_number` in your implementation, then

* Create an entity with the required regex. See [Add entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type), for more information.
* Add a user query with the order number in the invocation intent. Example: `I want to check the status of my order 6BFC86`, the order\_number entity is extracted and available in the Invocation intent. See [Add Invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information
* Next, in the Dialog skill implementation, you can add order\_number as an existing entity in the user intent.
  {% endhint %}

If an intent refers to a verb or the action in the user query, then an entity refers to a noun (the object on which the action is performed) in the user query. **Example**: In the user query "I want to book tickets from San Francisco to New York", San Francisco and New York represent entities of type Location. See [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types), for more information.

To respond to user queries accurately, it is important to extract the right entities from the user query to interpret the user's intent correctly.

### Before you begin

Before you begin to add user intents in the Dialog skill conversational flow, it is recommended to have a thorough understanding of the following concepts:

* [Intents and Training data](https://docs.avaamo.com/user-guide/overview-and-concepts/intents)
* [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types)
* [Slots](https://docs.avaamo.com/user-guide/overview-and-concepts/slots)
* [Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence)
* [Best practices of designing a skill](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill)

### What is an Existing entity in user intent?

Existing entities are intents with entities. This helps to extract accurate entities from the user query in the conversation flow.&#x20;

**Example**: Consider that in the Order Pizza skill, the first message asks the user for the type of pizza - veg, non-veg. You can create "pizza\_types" as an entity, and in the subsequent node, add an intent with this entity to process the user response and proceed further in the conversation flow.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-NqZZF5UwTnocz-Uz2%2F-M-O-kVDf5DmaF_5DYns%2Fhowto-entitytype-flow-1.png?alt=media\&token=a382e47e-f237-471c-81d3-95c30988ed5f)

### Why use an Existing entity in user intent?

Using existing entities in user intent helps in:

* **Improving the accuracy** of responding to user queries, since the entities are detected properly in from user's query.
* **Maintainability and Scalability**, since you just have to specify only one training phrase with an entity value, and the system automatically replaces it with other entity values of the same entity type in the training phrase. Example: In a Health assistant -> Appointment booking skill, the training phrases can be

  1. I want to book an appointment with a Cardiologist
  2. I want to book an appointment with a Neurologist
  3. I want to book an appointment with a Physician, and so on

  If you have created an entity type say "Speciality" with values as Cardiologist, Neurologist, and Physician,  you just have to specify training phrase - " I want to book an appointment with a Cardiologist" and the system automatically matches if the user utterance is "I want to book an appointment with a Physician" or any other entity value. It is not required for the agent to be trained in all such occurrences. Hence it is easy to maintain and scale. You can continue to add further values in your entity type, without having to modify your training phrase.
* Automatically detect the entities in a user query and skip asking questions to the users for which the answers are already available in the initial query. This is referred to as [Entity skipping](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/entity-skipping).
* Re-using the entities across different virtual assistants or different skills in the same virtual assistant instead of requiring to train such common phrases repeatedly.

### When to use Existing entity?

Use the "Existing entity" option in the user intent when you expect an entity to be extracted at a specific point in the conversation flow.

### How to use Existing entity in user intents?

{% hint style="success" %}
**Key point**: Only the entities added to the skill in the **Invocation intent** page are displayed in the list. See [Invocation Intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information on adding entities to the skill.&#x20;
{% endhint %}

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.

* If you wish to edit skills in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;

* The quality of the intents and their training determines the quality of the agent's accuracy in understanding the user queries. See [Design skill](https://docs.avaamo.com/user-guide/how-to/design-skill#intent-and-training-phrases), for more information on intent training guidelines.
  {% endhint %}

* In the **Dialog skill** page, click **Edit** to unlock the skill.

* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;

* Add user intents by creating a new node in one of the following ways:
  * Click the **plus (+)** icon to add a new user intent and skill response in the node below the current node.
  * Click the **fork** icon to add a new user intent and skill response as a forked branch to the current node.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma7bIuRq5MKOQJmzUGc%2F-Ma80SBNObJgy5nLYK_I%2F5.7-dialog-add-user-intent.png?alt=media\&token=f7fcc81f-4e3e-4252-a631-32b3b94aaba9)

* Click the red call-out bubble above "Add agent Response" to add an Intent and specify the following details:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb11TIV2288hWmBqzf6%2F-Mb13C9z_VypruSg1D7l%2Fdialog-user-intent-entity.png?alt=media\&token=50ee764a-7be3-4a71-8599-3d1cf3bd47ef)

<table><thead><tr><th width="147.90434698745716">Parameters</th><th width="441.118609301048">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent name</td><td><p>Indicates the name of the intent. </p><p></p><p>Each intent name must be unique within the skill.</p></td><td align="center"><p>192 </p><p>characters</p></td></tr><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. </p><p></p><p>By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p><strong>Supported characters</strong>: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p><p></p></td><td align="center"></td></tr><tr><td>Intent type</td><td>Indicates the type of user intent. Select <strong>Existing entity</strong>.</td><td align="center">N/A</td></tr><tr><td>Select entity</td><td><p>Start entering the entity type and the results are automatically filtered out in the list. </p><p></p><p>Choose an entity from the list. You can add only one entity to user intent. </p></td><td align="center">N/A</td></tr><tr><td>Select entity value (Optional)</td><td><p>Choose the values from the selected entity type. Only these values are matched in the user intent. </p><p></p><p><strong>Example</strong>: Consider the "pizza_type" entity type with cheese, corn, and pineapple as values. You have selected "pizza_type" in the user intent and only cheese and corn in the entity value. In this case, a user intent "I want to order veg pineapple pizza" is not matched to this node.</p></td><td align="center">N/A</td></tr><tr><td>Training data (Optional)</td><td><p>Enter the training phrase and click <strong>Add</strong>. </p><p></p><ul><li>You can continue to add multiple training phrases, as required. </li><li>You can add a combination of training data with an existing entity. This enables you to specify a stricter or restricted match of a user query that contains the selected entity. </li><li>See <a href="..#1-what-if-i-have-both-training-phrases-and-an-existing-entity-in-a-user-intent-how-is-the-behavior-defined">What if I have both training phrases and an existing entity in a user intent? How is the behavior defined?</a> for more information on how matching is defined with an example.</li></ul></td><td align="center">N/A</td></tr><tr><td>Post-processing </td><td><p>Indicates any JS that is executed after the intent is invoked and before displaying the skill response. </p><p></p><p>Use this to dynamically reroute the flow and skip the current intent. <strong>Example</strong>:<br><code>if(context.variables.hasId==true){</code><br> <code>return goto_output(2)</code><br><code>}</code></p><p>See <a href="../../../customize-your-skill">Build skill responses using script and code</a>, for more information.</p></td><td align="center">N/A</td></tr></tbody></table>

* Click **Save**.&#x20;
