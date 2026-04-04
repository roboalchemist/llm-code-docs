# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-tags.md

# Tags

Tags help you to understand the usage of agents by categorizing the user intents distributed across different skill responses. It helps you to analyze the top used intent categories and the way users are interacting with the agent. It gives a different perspective of viewing and understanding the user-agent interactions. See [View analytics of top tags](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#top-tags), for more information on the "Top Tags" Analytics board.

You can define and add any number of tags to a skill response. **Example**: In an HR-Payroll agent, you can define and add a "Bonus" tag for all bonus-related responses. See the following topics for more information on how to add tags to skill responses:

* [Build skill responses](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#tags)
* [Add tags using JS](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js)

{% hint style="info" %}
**Notes**:&#x20;

* Currently, you cannot associate tags to Answers skill responses.
* The tag name can be upto 192 characters. Special characters are allowed in the tag name.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MER0HF8Glape3e7O6rT%2F-MER3C3_GMlaAAG57eJ9%2Fadd_tags.gif?alt=media\&token=5b8a67a9-2231-4a6f-af3c-4e074b14ef13)

Make a note of the following before you add, edit, or delete tags in agents.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add languages to the agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

### Types of Tags

The following tag types are available in the Avaamo Platform:

* **System tags**: In-built reserved system tags that are internally generated and managed by the platform. All system tags are prefixed with `System::` keyword. Currently, there is only one system tag - `System::Agent::Transfer` that is used to track all the agent interventions. See [Agent intervention](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#agent-intervention), for more information.
* **Custom tags**: User-defined custom tags that represent the ways in which you wish to track data related to your business. Few examples of customized tags in an HR agent - Bonus, Payroll.

{% hint style="info" %}
**Note**: In the Configuration -> Tags page only custom tags are displayed.&#x20;
{% endhint %}

### Add tag

* In the Agent page, navigate to the **Configuration -> Tags** option in the left navigation menu.
* Click **Add tag** and specify the tag name.&#x20;
* Continue adding multiple tags as required. Note that the tag name must be unique to an agent. You cannot begin a tag with the `System::` keyword, as it is a reserved tag.&#x20;

### Edit tag

* In the Agent page, navigate to the **Configuration -> Tags** option in the left navigation menu.&#x20;
* A list of all the custom tags is displayed. Click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Edit.**
* Update the tag name and click **Update**. If the tag is used in responses, then all the tags in the responses are also updated.

### Delete tag

* In the Agent page, navigate to the **Configuration -> Tags** option in the left navigation menu.
* Click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Delete.**

{% hint style="info" %}
**Note**: You can only delete a tag that is not used in any skill response. If a tag is used in any skill response, then a warning message is displayed. You must first remove the tags in all the skill responses before deleting the tag.
{% endhint %}

### Next steps

* Add the defined tags in your agent to your skill responses as per the business requirement. See [Build skill responses](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#tags), for more information.
* You can also add tags using JS to the skill responses. See [Add tags using JS](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js), for more information.
* Once you add tags with the skill response and a user query hits the node, all the corresponding tags added to the node are associated with the user query. You can view the top tags in the Analytics board. See [View analytics of top tags](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#top-tags), for more information on the "Top Tags" Analytics board.
