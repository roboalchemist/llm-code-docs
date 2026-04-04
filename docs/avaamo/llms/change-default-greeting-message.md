# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/change-default-greeting-message.md

# Change default greeting message

After creating the invocation intent, the next step is to build a conversational dialog flow. By default, a greeting node is provided for you. Start by changing the default greeting message; this is the first message displayed to the user after the skill is invoked. You can then continue to [add user intents](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent) and [build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses) as required to build the dialog flow.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

**To change the default greeting message**:

* In the **Dialog skill** page, click **Edit** to unlock the skill&#x20;
* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;
* Click the default greeting message node, in the dialog flow.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF3saJ1XWBYai6i3ytk%2F-MF3vATesRTTSoZZfM3l%2Fdialog-greeting-message-node.png?alt=media\&token=e4575c31-24ce-4cc1-aeb7-b526171701e7)

* Update the default greeting message in the **Message** box and click **OK**. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more detailed information on different skill responses and **Advanced Settings**.
* Select the channel for which you wish to add the greeting message. Using this feature, you can add different customized responses for different channels as per your requirement. If you have deployed your agent in a specific channel for which you have not configured any response, then the response as specified in the "Default" option is considered. **Example**: Consider that you have deployed your agent in Web, Android, and iOS channels and you have configured responses only for the Android channel. For the Web and iOS channel, the responses as specified in the **Default response** option is displayed.
* If you have configured languages in the skill, then a language dropdown is displayed. Select a language in which you wish to add the response.

{% hint style="success" %}
**Key Point:** With the ability to add channel-specific and language-specific skill responses, you can now add responses specific to each channel-language combination. Example: You can add a response specific to the Android channel in the French language.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO1moicGnJ_8jZlCOlP%2F-MO1qvtn-9og5LW-1_zR%2Fdialog-welcome-message.png?alt=media\&token=1a8b9eda-c926-45b7-99bd-170cc4255c0f)

* Click **Save**.&#x20;
* You can now test the skill after adding the invocation intent and updating the greeting message, using the simulator in the **Agent** page. See [Test Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/test-skill), for more information. Invoke the skill using the Invocation Intent and verify if the greeting message is displayed in the agent.&#x20;

{% hint style="info" %}
**Note**: If you have added response filters to the skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FweGcJmUFw7VM5cNIE2Au%2Fimage.png?alt=media\&token=cbad94f2-ecbb-4cdd-95da-25d04f8462f3)
