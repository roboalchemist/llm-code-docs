# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/perform-common-actions.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/build-and-manage-q-and-a-skill/perform-common-actions.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/perform-common-actions.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/perform-common-actions.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/perform-common-actions.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/perform-common-actions.md

# Perform common actions

You can perform the following actions in the skill flow editor:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Kw1BKjY52OCbXt7d9%2F-M-Kx6TaJl4MhJQpdXdU%2Fdialog-perform-actions.png?alt=media\&token=8a878485-dc94-45ba-8339-67de86d2608e)

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can build and manage dialogs (conversational flow) immediately after creating a Dialog Skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.
* If you wish to edit skills in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * In the **Agent** page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

## Edit Dialog skill

You can edit the skill to update the skill name and description as required.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0Uclj7jHjRGtHHUhC%2F-Mb0WNR-oVMmbQtsbkrV%2F5.7-edit-dialog-skill.png?alt=media\&token=ddca22af-6d89-4b98-9aba-99eb7cc56107)

* In the **Dialog skill** page, click **Edit** to unlock the skill.
* Click the **pencil icon** at the top-left corner next to the skill name.
* Edit the skill details.&#x20;

{% hint style="info" %}
**Note**: By default, the skill key is non-editable. Click **Edit** to edit the skill key. It is recommended to edit the skill key with caution. If you update the skill key and if the key is used say in JS code or in regression testing, then you must update the skill key manually.
{% endhint %}

* Click **Update** and click **Save** to save the skill details.

## Edit intents and responses

You can edit the intents and responses of a Dialog skill.&#x20;

* In the **Dialog Skill** page, click **Edit** to unlock the skill&#x20;
* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;
* Click the intent that you wish to edit. Edit the intent details as required and click **Save**.

{% hint style="info" %}
**Note**: By default, the **Intent key** is non-editable. Click **Edit** to edit the Intent key. It is recommended to edit the Intent key with caution. If you update the Intent key and if the key is used say in JS code or in regression testing, then you must update the Intent key manually.&#x20;
{% endhint %}

* Click the skill message that you wish to edit. Edit the [Prompt details](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses) and [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings) as required and click **Save**. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.on

## Move nodes in the flow

In the dialog skill flow editor, **right-click** on any of the nodes to perform the following actions:

<table><thead><tr><th width="162">Actions</th><th>Description</th></tr></thead><tbody><tr><td>Copy</td><td>Copies a single node or the entire branch within the same dialog flow or between agents. See <a href="#copy-node-between-agents">Copy node between agents</a>, for more information.</td></tr><tr><td>Move left</td><td>Moves the node to its left in the dialog flow. This is not enabled for the left-most node in the dialog flow and for the first node or the root node in the flow.</td></tr><tr><td>Move right</td><td>Moves the node to its right in the dialog flow. This is not enabled for the right-most node in the dialog flow and for the first node or the root node in the flow.</td></tr><tr><td>Delete</td><td>Deletes either a single node or the entire branch and for the first node or the root node in the flow. This is not enabled for the first node or the root node in the flow.</td></tr><tr><td>Paste</td><td>Paste a copied node either to a new node or to an existing node. This is enabled only when you have a node that is copied. This is not enabled for the first node or the root node in the flow.</td></tr></tbody></table>

## Copy node between Dialog skills of agents

You can copy a single node or the entire branch from the Dialog skill of one agent to the Dialog skill of another agent.&#x20;

* Navigate to the Agent -> Dialog skill -> Implementation page of the agent from which you wish to copy the node. Right-click the node and click **Copy**. Choose if you wish to copy a single node or the entire branch from the agent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fx3p64fyDmPAQWAqqD4by%2FScreenshot%202023-03-24%20at%209.38.22%20AM.png?alt=media&#x26;token=212d14a1-7f23-4ea6-81ce-fa0b3aaddf53" alt=""><figcaption></figcaption></figure>

* Navigate to the Agent -> Dialog skill -> Implementation page of the agent to which you wish to copy the node or branch. Right-click the node where you wish to copy and click **Paste**. The following prompt is displayed:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZJRHIVeaEXJK7ySdxrWc%2FScreenshot%202023-03-24%20at%209.28.26%20AM.png?alt=media&#x26;token=b6430162-b184-47a8-85cd-21ca8339a6b1" alt=""><figcaption></figcaption></figure>

* Click in the area and press either CMD/CTRL + V. The following message is displayed:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fiyy2cglX1miE7FnBxg6M%2FScreenshot%202023-03-24%20at%209.41.06%20AM.png?alt=media&#x26;token=b56701d7-e005-44bd-92e9-088422a1b1fc" alt=""><figcaption></figcaption></figure>

* Click **Paste** to complete the copy-paste of a single node or entire branch between agents

## Search, View, and Print

In the dialog skill flow editor, you can use the options provided at the right side of the editor to search, view, and print the flow.

### Search nodes

Click the **Search** icon on the right side of the editor. Start typing the intent name or the intent key that you wish to search. As you type, the results are filtered and displayed in the search.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-May5Yn7_1b-ySLXCtA9%2F-May6R2SvdAEbff0BTug%2F5.7-search-nodes.png?alt=media\&token=e493d0fb-1d00-4c12-967a-ddb3e926e23a)

Select the required node. The corresponding node is highlighted in the flow:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-May6V4q8Tof8k6g-If7%2F-May6thAIfzrYvHHBN_y%2F5.7-search-nodes-results.png?alt=media\&token=418f741f-939c-4fc3-bdb7-c2a9f40ea625)

### Other actions

You can also perform the following actions

<table><thead><tr><th width="233">Actions</th><th>Description</th></tr></thead><tbody><tr><td>Search</td><td>Search for the nodes in the dialog flow.  </td></tr><tr><td>Zoom-in and Zoom-out</td><td>Use + and - icons to zoom in and zoom out respectively.</td></tr><tr><td>Maximize and Restore</td><td>Use this to view the dialog flow in full screen and to restore it back to the normal view.</td></tr><tr><td>Print</td><td>Use this to print the dialog flow. </td></tr></tbody></table>
