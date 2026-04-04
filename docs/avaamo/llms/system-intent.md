# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/system-intent.md

# System intent

An **intent** is an action in the user query that indicates what the user wishes to do. The same intent can be expressed in different ways by the user. Certain intents, such as repetition and politer, are all part of natural language in human conversation and are common in any conversational flow. For example,&#x20;

* In a Travel assistant, if the user wishes to confirm a booking, the user might say, Yes, Yeah.
* Similarly, in a Health assistant, the same intent for confirmation such as yes, Yeah, Okay, and many such variations of "Yes" can be used to confirm refilling a prescription.

Instead of re-training the same phrases repeatedly, it is efficient and faster to have a set of pre-defined training phrases to capture such common user intents. These are referred to as System intents.

### Before you begin

Before you begin to add user intents in the Dialog skill conversational flow, it is recommended to have a thorough understanding of the following concepts:

* [Intents and Training data](https://docs.avaamo.com/user-guide/overview-and-concepts/intents)
* [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types)
* [Slots](https://docs.avaamo.com/user-guide/overview-and-concepts/slots)
* [Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence)
* [Best practices of designing a skill](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill)

### What are system intents?

System intents are intents with pre-defined training phrases capturing the most common user intents in the conversational flow.&#x20;

**Example**: Consider that you wish to respond to the user's frustration by transferring to a live agent or via collecting feedback. You can create a user intent with frustration system intent and add a  response to transfer to a live agent.

### Why use system intents?

System intents hence help in:

* Efficiently capturing different variations of the same intent that are commonly used in the conversational flow.
* Reusing the system intents across different virtual assistants or different skills in the same virtual assistant instead of requiring to train such common phrases repeatedly.
* Building conversational flow faster since it does not require any coding to be done by the users to build agents.
* Improving the accuracy of recognizing such common intents in the conversational flow thereby providing a good user experience.

### List of system intents

The following system intents are supported in the platform - yes, no, frustration, live agent, cancel, repeat, go back, thank you.

### When and Where to use System intents?

System intents are like "fillers" in the middle of a conversational flow. They help in continuing further conversations with the users. Hence, system intents are available in Dialog skill that helps in building multi-turn conversational flows.

For example, In a "Refill prescription" skill of a Health assistant, you can build a conversational flow with system intents such as:

* Yes, No -> To get confirmation from the user to proceed with refilling the prescription.
* Repeat -> To repeat the prescription
* Frustration -> To detect any frustration from the user and transfer to an agent.

### How to use system intents?

You can choose intent type as **System intent** when you add user intents to any node of the Dialog skill based on your conversational flow design. For example, in this **User intent**, "Yes" system intent is selected:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJOrgCeVnZIaL7nBmYzvU%2Fimage.png?alt=media\&token=dd85b3cb-f483-4203-999b-6df3f3d95e33)

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

* In the **Dialog skill** page, click **Edit** to unlock the skill&#x20;

* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;

* Add user intents by creating a new node in one of the following ways:
  * Click the **plus (+)** icon to add a new user intent and skill response in the node below the current node.
  * Click the **fork** icon to add a new user intent and skill response as a forked branch to the current node.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma7bIuRq5MKOQJmzUGc%2F-Ma80SBNObJgy5nLYK_I%2F5.7-dialog-add-user-intent.png?alt=media\&token=f7fcc81f-4e3e-4252-a631-32b3b94aaba9)

* Click the red call-out bubble above "Add agent Response" to add an Intent and specify the following details:

<table><thead><tr><th width="168">Parameters</th><th width="363.0111826850367">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent name</td><td><p>Indicates the name of the intent. </p><p></p><p>Each intent name must be unique within the skill.</p></td><td align="center"><p>192 </p><p>characters</p></td></tr><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. </p><p></p><p>By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p><p></p></td><td align="center"></td></tr><tr><td>Intent type</td><td>Indicates the type of user intent. Select Training phrases.</td><td align="center">N/A</td></tr><tr><td>Training Phrases</td><td>Enter the training phrase and click <strong>Add</strong>. You can continue to add multiple training phrases, as required. Based on the training phrases, the slots are automatically filtered for you. </td><td align="center">Each training pharse can be maxium of 300 characters</td></tr><tr><td>Add training set</td><td><p>This allows you to add training data in different languages. It is not required to train your skill in English only, you can train your skill in different languages. </p><ul><li>Add language in <strong>Configuration -> Languages</strong> and save the agent. See <a href="../../../../../build-agents/configure-agents/add-languages">Add languages</a>, for more information.</li><li>Click <strong>Add training set.</strong></li><li>Select the required language and add the training set in the selected language.</li></ul></td><td align="center">N/A</td></tr><tr><td>Post-processing </td><td><p>Indicates any JS that is executed after the intent is invoked and before displaying the skill response. </p><p></p><p>Use this to dynamically reroute the flow and skip the current intent. <strong>Example</strong>:<br><code>if(context.variables.hasId==true){</code><br> <code>return goto_output(2)</code><br><code>}</code></p><p>See <a href="../../../customize-your-skill">Build skill responses using script and code</a>, for more information.</p></td><td align="center">N/A</td></tr></tbody></table>

* Click **Save**.&#x20;
