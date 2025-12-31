# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/training-phrases.md

# Training Phrases

For an agent to respond to user queries, each intent must be trained with specific sentences that are used as representative phrases for user queries. This set of sentences is referred to as the **Training phrases.**

### Before you begin

Before you begin to add user intents in the Dialog skill conversational flow, it is recommended to have a thorough understanding of the following concepts:

* [Intents and Training data](https://docs.avaamo.com/user-guide/overview-and-concepts/intents)
* [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types)
* [Slots](https://docs.avaamo.com/user-guide/overview-and-concepts/slots)
* [Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence)
* [Best practices of designing a skill](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill)

### What are training phrases?

These are the inline user intents (utterances or phrases) in the conversation flow.  **Example**: I want to order pizza, I want a pizza delivery.

### How to use training phrases in user intents?

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

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7oJJMIGrrsVHK3ep75yr%2Fimage.png?alt=media\&token=1b56452d-6c82-4125-a518-d514121dc865)

* Click the red call-out bubble above "Add agent Response" to add an Intent and specify the following details:

<table><thead><tr><th width="150">Parameters</th><th width="363.0111826850367">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent name</td><td><p>Indicates the name of the intent. </p><p></p><p>Each intent name must be unique within the skill.</p></td><td align="center"><p>192 </p><p>characters</p></td></tr><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. </p><p></p><p>By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p><p></p></td><td align="center"></td></tr><tr><td>Intent type</td><td>Indicates the type of user intent. Select Training phrases.</td><td align="center">N/A</td></tr><tr><td>Training Phrases</td><td>Enter the training phrase and click <strong>Add</strong>. You can continue to add multiple training phrases, as required. Based on the training phrases, the slots are automatically filtered for you. </td><td align="center">Each training pharse can be maxium of 300 charactersClick <strong>Save</strong>. </td></tr><tr><td>Add training set</td><td><p>This allows you to add training data in different languages. It is not required to train your skill in English only, you can train your skill in different languages. </p><ul><li>Add language in <strong>Configuration -> Languages</strong> and save the agent. See <a href="../../../../../build-agents/configure-agents/add-languages">Add languages</a>, for more information.</li><li>Click <strong>Add training set.</strong></li><li>Select the required language and add the training set in the selected language.</li></ul></td><td align="center">N/A</td></tr><tr><td>Post-processing </td><td><p>Indicates any JS that is executed after the intent is invoked and before displaying the skill response. </p><p></p><p>Use this to dynamically reroute the flow and skip the current intent. <strong>Example</strong>:<br><code>if(context.variables.hasId==true){</code><br> <code>return goto_output(2)</code><br><code>}</code></p><p>See <a href="../../../customize-your-skill">Build skill responses using script and code</a>, for more information.</p></td><td align="center">N/A</td></tr></tbody></table>

### Key points

* If you want training data that must match specific and generic queries, then it is recommended to provide generic training data. **Example**: If you wish to match "I want my fund value" and "I want fund value", then it is recommended to use "I want fund value" in the training data.
* See [Intent and training phrases](https://docs.avaamo.com/user-guide/how-to/design-skill#intent-and-training-phrases-training-utterances-or-training-data), for more information on recommended best practices for using training phrases.
* See [Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence), for more information on intent execution priority
