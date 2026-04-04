# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-feedback.md

# Add feedback (JS)

You can add feedback in any response (Dialog, Q\&A, Smalltalk) using a JavaScript`collectFeedback()`method.&#x20;

{% hint style="info" %}
**Notes**:

* Typically, feedback is collected in the last node of a flow. Hence, `collectFeedback()` method must be specified in the last JS block response.
* You must always return a message after `collectFeeback()` method in the JS code.
* Currently, the **Collect feedback** functionality is not supported in Facebook Messenger.
  {% endhint %}

Consider that you wish to add feedback only for certain specific Q\&A intents. You can&#x20;

* Disable **Collect feedback** slider for the Q\&A skill. See [Edit Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/perform-common-actions#edit-skill), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVPilcb6lDmpCGlScRjSo%2FScreenshot%202024-08-21%20at%208.02.19%E2%80%AFPM.png?alt=media\&token=01769d42-728b-4d72-84cd-a7bfc444b825)

* Add a JS node in the Q\&A response where you wish to collect feedback and use `collectFeedback()` method in the JS.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEgfMGxbLcyIifxwRjc%2F-MEgjc1lbLUDDQoXxd4Z%2Frn-collect-feedback.png?alt=media\&token=50d33ee9-2b94-42e8-9bd4-17ab6446b2a4)

* Click **OK** to save the response and **Save** to save the agent changes.
* Click the agent chat widget at the bottom-right corner to test the agent. Provide a user query in the agent to trigger the Q\&A response. You can see that the feedback is displayed only for this Q\&A response.
