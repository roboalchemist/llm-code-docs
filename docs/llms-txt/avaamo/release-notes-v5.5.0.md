# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.5.x/release-notes-v5.5.0.md

# Release notes v5.5.0

The Avaamo Conversational AI Platform v5.5.0 release includes 4 enhancements and 2 changes distributed as follows:

**Enhancements**: This release includes enhancements in the following areas:

* [Integrated Conversational-IVR (C-IVR) or Phone channel](#integrated-conversational-ivr-c-ivr-or-phone-channel): As a part of C-IVR integration, the following enhancements have been introduced in this release:
  * [Ability to add agent responses using rich SSML tag support](#ability-to-add-agent-responses-using-rich-ssml-tag-support)
  * [Ability to add voice hints at agent level and skill level](#ability-to-add-voice-hints-at-agent-level-and-skill-level)
  * [Ability to test agent in C-IVR channel using agent simulator](#ability-to-test-agent-in-c-ivr-channel-using-agent-simulator)
* [Ability to add channel-specific skill responses directly in the UI without using JS](#channel-specific-skill-responses)
* [Ability to view regular expression entity related errors in the Debug -> JS errors page](#debug-greater-than-js-errors)

{% hint style="success" %}
**Key Point:** With the ability to add channel-specific and language-specific skill responses, you can now add responses specific to each channel-language combination in the UI itself without using Javascript code. Example: You can add a response specific to the Android channel in the French language.
{% endhint %}

**Changes**: This release also includes changes related to the channel availability in your account or company, UI text change in the Q\&A intent pop-up, and system entity extraction in the Platform. See [Changes](#changes), for more information.

## Component-wise distribution

The following table lists the component-wise distribution of new feature, enhancements, and changes in the v5.5.0 release:

{% tabs %}
{% tab title="Enhancements" %}
The following lists the usage of the enhancements across different components in the platform:

| Enhancement                                                                                                                              | Components                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p></p><p><a href="#integrated-conversational-ivr-c-ivr-or-phone-channel">Integrated Conversational-IVR (C-IVR) or Phone channel</a></p> | <p></p><ol><li>Deploy your agent to the C-IVR channel in the current 5.x platform. </li><li>Add agent responses to C-IVR channel using - Agent voice, Voice menu, and Call forward response types.</li><li>Configure voice hints at the agent level.</li><li>Agent simulator - Ability to test your agent in C-IVR channel using agent simulator</li></ol> |
| [Channel specific skill responses](#channel-specific-skill-responses)                                                                    | <p>Add channel-specific skill responses directly in the UI:</p><ol><li>Greeting skill</li><li>Unhandled skill</li><li>Dialog skill</li><li>Dynamic Q\&A</li><li>Smalltalk</li><li>Q\&A</li></ol>                                                                                                                                                           |
| [Debug -> JS errors](#debug-greater-than-js-errors)                                                                                      | Debug regular expression entity related errors from the Debug -> JS errors page.                                                                                                                                                                                                                                                                           |
| {% endtab %}                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                            |

{% tab title="Changes" %}
The following lists the changes across different components in the platform:

| Component                                    | Change                                                                                                                           |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [Channels](#1-channels)                      | You can deploy your agents in only those channels that are enabled for your account. Other channels are disabled and grayed out. |
| [Q\&A intent pop-up](#q-and-a-intent-pop-up) | Cancel button text in the Q\&A intent pop-up is changed to Exit.                                                                 |
| {% endtab %}                                 |                                                                                                                                  |
| {% endtabs %}                                |                                                                                                                                  |

## Enhancements

### Integrated Conversational-IVR (C-IVR) or Phone channel

In this release, the channel integration has been enhanced to include Conversational-IVR (C-IVR) or Phone channel in the current 5.x platform. If the C-IVR channel is enabled for your account or company, you can now deploy the agents built on the Avaamo Platform into your phone channel from the Configuration -> Channels page.&#x20;

Since the C-IVR channel is natively integrated with the rest of the 5.x platform, you build both voice and text virtual assistants in a single account. The agents built and deployed on the C-IVR channel take full advantage of rich features available in the 5.x platform. See [Conversational IVR (C-IVR) or Phone](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOe2kxfHRSmXb6P4TB3%2F-MOe3IDPKIVjrYDf2cpH%2Fwn-5.5-channel.png?alt=media\&token=9a1af9a4-76b4-4045-84bb-8023ece63e42)

In the previous release, the agents requiring the C-IVR channel had to be built and deployed separately in a 4.x platform.&#x20;

As a part of this enhancement, the following enhancements have been introduced:

* [Ability to add agent responses using rich SSML tag support](#ability-to-add-agent-responses-using-rich-ssml-tag-support)
* [Ability to add voice hints at agent level and skill level](#ability-to-add-voice-hints-at-agent-level-and-skill-level)
* [Ability to test agent in C-IVR channel using agent simulator](#ability-to-test-agent-in-c-ivr-channel-using-agent-simulator)

#### **Ability to add agent responses using rich SSML tag support**

In this release, three new agent response types have been added - [Agent voice](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#agent-voice), [Voice menu](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#voice-menu), and [Call forward](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#call-forward). These response types enable you to build a conversational flow for your C-IVR channel using rich support of SSML tags that are available out-of-the-box in the Platform. See [Supported SSML tags](https://docs.avaamo.com/user-guide/ref/speech-synthesis-markup-language-ssml), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOe2kxfHRSmXb6P4TB3%2F-MOe6rrZvShVI4CjxJZN%2Fwn-5.5-agent-responses.png?alt=media\&token=5e91ba76-91ec-475c-9c63-76ec144a20e8)

#### **Ability to add voice hints at agent level and skill level**&#x20;

In this release, an additional option to add Voice hints has been introduced. Voice hints allow you to specify certain keywords or phrases that can provide better interpretation or recognition of the user response in the conversational IVR interaction. Providing voice hints can significantly improve user interaction with your agent and help to redirect conversation flow smoothly.&#x20;

The following lists a few use-cases where voice hints can be used:

* To help agents understand certain nuances of dialects or accents of users.&#x20;
* To provide clues or hints to the agent indicating that the user can provide such similar inputs at the specified node when the response is read out to the user.&#x20;

Example: In the following illustration, there is an agent response asking for the user to confirm the order number. You can provide voice hints to help the agent understand and interpret the nuances of user responses as illustrated here:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOeC3p2QeXFZz-_HiBd%2F-MOeCdaQtGjNrxRPkld-%2Fwn-5.5-voice-hints.png?alt=media\&token=1a71ac27-b0d7-4e83-8a4a-0dff851799f8)

* This option is available for each response node in the Dialog skills -> Advanced settings tab. See [Voice hints in Advanced settings, ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#voice-hints)for more information.
* This option is also available at the agent level in the Configuration section. See [Add voice hints](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings#configure-voice-hints), for more information.

#### **Ability to test agent in C-IVR channel using agent simulator**

In this release, a new option **IVR / phone** has been added in the agent simulator along with the Web channel. This allows you to choose and test your agent in either C-IVR or the web channel.&#x20;

Note that this option is displayed only when you have deployed your agent in the C-IVR channel and is available across all the pages where the agent simulator is displayed. See [Agent simulator](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/simulator), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MN8KHRCRxPxcH_jLXrm%2F-MNC9bSw4NGI3z7gB4LD%2Fc-ivr-agent-simulator.png?alt=media\&token=96bd9f8e-25d5-43d8-af59-4f8427ab27e0)

### Channel-specific skill responses

In this release, you can add skill responses specific to each channel directly in the UI without using any JavaScript code. It helps in rapid agent development and easy maintainability as customized channel-specific skill responses can be added directly in the UI.&#x20;

This enhancement is available across all the skill responses - Greeting, Unhandled, Dialog skills,  Smalltalk skills, Dynamic Q\&A, and Q\&A skills.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOeQHbCZ8NiJOUXvQGj%2F-MOeRuB7anlFwVZJCsN7%2Fwn-5.5.-channel-responses.png?alt=media\&token=70155270-3f15-4094-b665-9e31ee053324)

See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#channel-specific-responses), for more information.

In the Dynamic Q\&A, Smalltalk, and Q\&A skills, you can add or edit customized responses for the Q\&A for each Channel using the Channel dropdown available in the Implementation -> Questions & Answers page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOo3JmShl0cfKDW0WH6%2F-MOo9Dn8s3oQS5EYUecG%2Fwn-5.5-channel-qa.png?alt=media\&token=46e6dc3a-f217-434a-90e6-88309240573f)

In the previous release, to add channel-specific responses in the skill, you had to write JS code to achieve the same functionality, hence, it was not user-friendly and was difficult to maintain.

### Debug -> JS errors

In this release, you can view errors related to the regular expression entity in the **Debug -> JS errors** page. You can use this information for further troubleshooting to analyze and fix the errors related to the regular expression entity. Note that the error is displayed only when you use the entity in the conversation flow.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOer7zQM8sW_5Itsgrp%2F-MOey62ppMPTHxDp3Lwb%2Fwn-5.5-debug-js-errors.png?alt=media\&token=5b85467b-2b45-44a8-bc95-0a6526c43b9d)

See [Debug agents](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents), for more information.

In the previous release, it was difficult to understand and debug if a flow was not working due to an error in the regular expression entity.&#x20;

## Changes

### Channels

In this release, you will be able to connect to a channel only if it is enabled for your account. All the channels that are not enabled for your account are disabled and grayed out. If you wish to enable a channel for your account, then contact Avaamo Support for further assistance.&#x20;

{% hint style="info" %}
**Note**: By default, only Web channel is enabled for an account.
{% endhint %}

Here, for this account, IMI Connect, Facebook Workplace, SMS, and Facebook Messenger channels are disabled for this account and hence grayed out. You will not be able to connect to these channels unless they are enabled for your account.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MNNAHFCPyeXJsfSVA2a%2F-MNNJu0Qh6JsavAouvCp%2Fwn-channel-disabled.png?alt=media\&token=905d5044-f570-4657-8d59-410ef88a8e9e)

### Q\&A intent pop-up

In this release, the "Cancel" text in the Q\&A intent pop-up has been changed to "Exit". You can view this change when you add, edit, or delete Q\&A from the Dynamic Q\&A, Smalltalk, or Q\&A skills.

#### Previous release:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOkz82l32qqindS91p9%2F-MOl-42Y5GHIX85h80zd%2Fwn-5.5-cancel-previous-release.png?alt=media\&token=809b159b-31a9-4116-9a1e-82f51c159358)

#### Current release:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOkz82l32qqindS91p9%2F-MOl-uzGF6iTmY5SanyJ%2Fwn-5.5-exit-current-release.png?alt=media\&token=c53d70ad-ad0d-4f54-bc03-c692e5033b55)

### System entity extraction

In this release, system entities are extracted only if they are a part of the agent. To include system entities as a part of the agent, you must either:

1. Add a training data to any skill (Dialog, Dynamic Q\&A, Smalltalk) that uses the system entity&#x20;
2. Add system entities in the Invocation intent of the Dialog skill using **Add entity** option (if you have intent type as Custom code or Pre-Unhandled intent). See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.

In the previous release, system entities were getting extracted even though they were not a part of the agent and hence resulted in confusion.
