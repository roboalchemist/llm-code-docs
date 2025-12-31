# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/collect-feedback.md

# Collect feedback

You can allow users to provide feedback on their conversational experience with your agent. Feedback provided by users is used to learn and analyse the experience of the user when they are interacting with your agent. You can enable the collect feedback option for specific skills to provide users the option to provide feedback.

When you enable the collect feedback option, the thumbs up and thumbs down option to provide negative and positive feedback is displayed after the agent response is displayed.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FBofbMTLj4uNSWGpPWoEP%2FcollFeed.png?alt=media\&token=a0bfe57e-4acc-41cc-9a08-c84aa5050f87)

When a user clicks thumbs down, a pop-up form is displayed, which allows users to provide more details on the negative feedback. This information can be used in [Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics) to continuously improve user experience.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fu5J0nKcTtnaVAKLa07GV%2FThumbsDown.png?alt=media\&token=0dbbd891-42b9-413f-829b-acf972ba74fc)

### Enabling Feedback

Feedback can be enabled at the skill level for the Answer's skill and the Dynamic Q\&A skill. When feedback is enabled at the skill level, feedback will be requested after every single response.

If you want feedback to be requested only at certain junctions or locations in a workflow, or only for certain responses, you can enable skill at the response level.  &#x20;

<table><thead><tr><th width="150" align="center">Skill</th><th width="150">At the skill level</th><th width="231.71428571428567">At the response level</th><th>Refer</th></tr></thead><tbody><tr><td align="center">Dialog skill</td><td>No</td><td>Yes. Using the Advanced Settings tab for a response or using the JS script</td><td> <a href="../../../how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#collect-feedback">Feedback for dialog skill</a></td></tr><tr><td align="center">Dynamic Q&#x26;A</td><td>Yes</td><td>Yes. Using the JS script function collectFeedback</td><td><a href="../../how-to/build-skills/create-skill/dynamic-q-and-a/create-a-new-dynamic-q-and-a-skill">Create a new Dynamic Q&#x26;A</a></td></tr><tr><td align="center">Smalltalk</td><td>No</td><td>Using the JS script function collectFeedback</td><td><a href="../../how-to/build-skills/create-skill/customize-your-skill/how-to/add-feedback">Add feedback (JS)</a> </td></tr><tr><td align="center">Answers</td><td>Yes</td><td>No</td><td><a href="../../how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill">Configuring Answers</a></td></tr></tbody></table>

### Customizing feedback form

The feedback form for thumbs up or thumbs down can be customized. See [Customizing feedback form](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback) for more information.
