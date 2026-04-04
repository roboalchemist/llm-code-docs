# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback.md

# User feedback

The **User feedback** page displays the feedback received by the agent from the users for the selected date range. It displays the Intent, User Comments, Feedback, and Node. This feature is used to learn and analyze the experience of the user when they are interacting with your agent.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F16E5NIxstlpYzHM2qINj%2Fimage.png?alt=media\&token=c7f6c0d9-52af-44da-a372-0dc2ea482491)

See [Collect feedback](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/collect-feedback), for more information on understanding the concept and various ways in which you can collect feedback from the users.

**To view feedback**:

* Navigate to the **Agents** tab on the top menu.
* Search and click any agent for which you wish to view user feedback. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents#search-agents), for more information.
* In the **Agent's** page, click **Learning -> User feedback**. By default, user feedback for the last 7 days is displayed.&#x20;
* Click the **Date picker** to specify a custom date range. A list of user feedback for the agent in the selected date range is displayed.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUck5ZPmpHj1YlVnXXKc8%2Fimage.png?alt=media\&token=158246ee-c373-4f80-9e65-0d5343a10b2f)

* For each intent where the feedback is collected, the following details are displayed:
  * **User**: Indicates the identifier of the user who provided the feedback.
  * **Step**: This is the `<<Skill_key>>:<<Intent_key>>` of the node in Dialog skill where the feedback is collected. For the Q\&A skill, the step is always 1. See [Flow designer](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/dialog-designer-overview), for more details on the skill key and intent key.
  * **Intent**: Indicates the intent name provided in the respective skill for which the feedback is collected.
  * **Intent Type**: Indicates the type of intent such as Inline, Entity, or Q\&A for which the feedback is collected.
  * **Skill**: Indicates the name of the skill for which the feedback is given.
  * **Positive**: Indicates if the feedback by the user is positive or negative.
  * **Message**: Indicates any message submitted by the user while providing feedback.&#x20;
* Click the arrow icon for the feedback where you wish to view the conversation history. You can use this to analyze the conversational flow for any troubleshooting.
* Click **Export** to download the user feedback in a CSV format. This can be used as a reference and for further analysis.
