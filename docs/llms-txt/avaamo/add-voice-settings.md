# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings.md

# Voice settings

In the **Voice settings** section, you can specify voice hints and add playback voice for your digital voice assistants.

{% hint style="info" %}
**Note**: You can add voice hints and playback voice for only those languages configured in your agent and supported for voice assistants. See [Voice - Supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/voice-supported-languages), for more information.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FAAEXNR6K7iQKj4lzXyki%2Fvoice_settings_6.0.png?alt=media\&token=0713322c-e581-4179-b00d-0215a1318373)

## Speech recognition

You can specify certain keywords or phrases as **Voice hints** in the agent configuration that can help in providing better interpretation or recognition of the user response in voice interaction. This is useful when you wish to deploy your agents in the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone) or wish to enable voice in [web](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), or [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels.

It helps in understanding the nuances of the dialect and provides clues or hints to the agent for better recognition. See [Understanding Voice hints](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/voice-hints), for more details on the concept and common FAQs.

### When to use?

You can use agent-level voice hints when you have voice hints to be used commonly by different skills in an agent.&#x20;

{% hint style="info" %}
**Note**: Adding all the voice hints at the agent level impacts the accuracy of the response, hence, it is recommended to carefully evaluate before adding voice hints at the agent level.
{% endhint %}

**Example**: Consider that you have added an inbuilt voice hint `expecting_number` to recognize numbers better at the agent level, so that similar sounding phonetics such as "won" -> "one", "four" -> "for"  get interpreted as numbers accurately. Now, since you have added this at the agent level, even when the user is actually trying to say "for", it gets recognized as "four" and this can lead to incorrect matches. In this case, adding a voice hint at the node level is a better option.

Hence, when you require better accuracy or recognition at a specific node, it is recommended to provide voice hints at the node level. These voice hints are only applicable to that node where it is specified. See [Advanced Settings -> Voice hints](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#voice-hints), for more information.&#x20;

### Configure voice hints

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can configure permissions immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

**Example 1**: Consider that your agent is deployed on the C-IVR channel with en-IN as the default language. An Indian user is interacting with your agent and trying to say "Mail account". Because of a different accent/dialect, the agent is understanding the phrase "Male account" and "Mail account" phrase is used in multiple skills. In such cases, you can add a "Mail account" voice hint in the "en-IN" language in the **Agent Configuration -> Voice settings** page. &#x20;

* In the **Agent** page, navigate to the **Configuration -> Voice hints** option in the left navigation menu.
* In the **Speech recognition** section, all the languages configured in your agent and supported for voice are displayed. For each language, the number of hints configured is also displayed.&#x20;
  * See [Voice - Supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/voice-supported-languages), for more information.
  * See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on how to add languages to your agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MboILSvf580kyky5NUx%2F-MboNh2tbKnntRZiS-qo%2F5.7-voice-settings-hints.png?alt=media\&token=cdac7b36-af51-4e18-8830-40c6b2216a0a)

* Click **Manage hints** in the **Actions** column to add or remove voice hints for a language.&#x20;
* In the pop-up, you can either add or delete the voice hints:
  * **Add**: Enter the voice hint in the text box and click the plus icon. Note that you cannot add duplicate voice hints.
  * **Delete**: Click the cross icon for the voice hints that are no longer required and you wish to remove.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MboNjYywEPLwoS9WNGK%2F-MboOElfB9yNTKpEv_IL%2F5.7-voice-settings-hints-language.png?alt=media\&token=8b8222e4-cb44-436c-a1fb-ba55388d4931)

* Close the pop-up and click **Save** to save the Voice settings configurations. For each language, the number of hints configured is updated and displayed

{% hint style="info" %}
**Note**: Voice hints provided in the **Speech recognition** section is applicable across [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps), and [C-IVR](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone) channel.
{% endhint %}

## Synthesis

In this section, you can configure the voice or the persona to be used by your agent, when you enable voice in [web](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), or [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels. For the C-IVR channel, you can specify the voice or persona in the C-IVR channel settings. See [C-IVR](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.

In the **Synthesis** section, all the languages configured in your agent and supported for voice are displayed. For each language, the default persona selected is also displayed.&#x20;

* See [Voice - Supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/voice-supported-languages), for more information.
* See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on how to add languages to your agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fre1zAmnvli1n3jCo7S6w%2Fvoice_synthesis_6.0.png?alt=media\&token=e6608efc-7be0-4056-8922-5cf2ac8f30c5)

Each language has a different set of voice personas that you can choose from. Select the persona from the options provided in the **Voice - Playback voice** section:

To hear the voice preview, type any text in the text area **Sample text for voice playback** and click the play button. You can also download the voice preview if required.

{% hint style="info" %}
**Note**: Playback voice provided in the **Synthesis** section is applicable across [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channel.
{% endhint %}
