# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/voice.md

# Voice

{% hint style="info" %}
**Note**: Digital voice feature is enabled only on-demand. Contact Avaamo Support, for further assistance.
{% endhint %}

In this section, you can enable a digital voice assistant to your web channel that can engage the users in intelligent conversations by understanding and interpreting the dialects and accents of the users.&#x20;

Voice assistants can provide real-time transcriptions in the selected locale of your voice messages.  Voice capability coupled with security that can be managed at each web channel instance, enables enterprise-wide deployment of agents with multiple levels of authentication and authorization options. See [Deploy in multiple web channel instances](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/deploy-and-test-web-channel), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbM2454dgPHQJyUC-ax%2F-MbM2LMdsSUQajRYXMPm%2F5.7-web-channel-voice.png?alt=media\&token=6ac826cb-c49c-4981-9ee9-672e3a61a606)

{% hint style="info" %}
**Before configuring voice in the web channel**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

### Enable voice

This option allows you to enable real-time transcriptions of the agent messages in the selected locale.

**To enable voice**:

* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Voice** section, slide the toggle **Enable voice** to **Yes**. By default, this option is disabled.
* Click **Save.**

{% hint style="info" %}
**Notes**:&#x20;

* This feature is enabled only on-demand. Contact Avaamo Support, for further assistance.

* When you enable voice, you can also add a response specifically for the voice messages. See [Voice response](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#voice-response), for more information.

* You can also configure voice hints and playback voice of the voice assistant in the web channel. See [Voice settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings), for more information.

* See [Voice - Supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/voice-supported-languages), for more information on languages supported for voice-enabled assistants.
  {% endhint %}

* Click **Test** to test the agent. A test link is displayed in the new window. Click the agent icon to test.&#x20;

* You can now see that a speaker icon :speaker:  and the mic icon :microphone2: is displayed in the agent chat widget.&#x20;
  * By default, the speaker icon is muted. Click the speaker icon to unmute and test voice responses.
  * Click the microphone and talk to the agent. If you have configured your agent in different languages, then you can select the language from the dropdown to switch the language.&#x20;
    * See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on how to add languages to agents.&#x20;
    * See [Voice - Supported languages](applewebdata://A1481F33-5936-4FC2-8002-1EDF872E2E7C/@avaamo/s/avaamo/~/drafts/-MdvcAchJH77OfMz93JB/how-to/build-agents/configure-agents/deploy/voice-supported-languages), for more information on languages supported for voice-enabled assistants.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfmHBeTBTAapMWB4Km6oJ%2Fimage.png?alt=media\&token=8d22162c-029f-4f73-b97f-55a68f2629a4)

* You can talk to the agent in the selected language. The text you speak is automatically transcripted by the agent and displayed in the text box.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FoBsvCxLMFQQ9eWqQztyr%2Fimage.png?alt=media\&token=04ffd666-ab94-48af-b7bd-4394e773b5ee)

* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Send the voice message automatically

This option allows the voice messages to be sent without requiring you to click **Send** in the agent chat widget.&#x20;

By default, when you speak using the microphone in the agent chat widget, the messages are displayed in the text box but not sent until you click **Send** button.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FL6DPojLGq0TCLrtXJc10%2Fimage.png?alt=media\&token=6c747283-dd3e-4f15-9e56-e27c2f1b43bc)

**To enable this feature**:

* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Voice** section, slide the toggle **Enable voice** to **Yes**. By default, this option is disabled.
* Click **Save** and click **Test** to test the skill. A test link is displayed in the new window. Click the agent icon to test. Click the microphone and talk to the agent. Your messages are sent to the agent without requiring you to click **Send** in the agent chat widget.&#x20;
