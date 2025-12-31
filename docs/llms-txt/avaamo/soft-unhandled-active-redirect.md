# Source: https://docs.avaamo.com/user-guide/llamb/soft-unhandled-active-redirect.md

# Soft unhandled (Active redirect)

LLaMB provides the capability to gracefully redirect users when faced with unhandled responses, a feature known as `Soft Unhandled`.&#x20;

In instances where the agent fails to comprehend a user query, it defaults to an unhandled intent response, stating, "*I am sorry. I don't have an answer for that.*" The `Soft Unhandled` feature maintains the acknowledgment of the agent's inability to provide an answer but does so with a courteous and polished response.&#x20;

{% hint style="info" %}
**Note:** Soft unhandled messages are now supported in multiple languages.
{% endhint %}

### How does this help?

This feature aims to enhance user interaction by:

* Creating a pleasant user experience during interactions.&#x20;
* Establishing a soft and reassuring tone in the agent's response.
* Conveying the impression that, although unable to address certain queries, the agent is still actively assisting with those it can answer.

|                                                                                                    Soft Unhandled                                                                                                   |                                                                                                      Unhandled                                                                                                      |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7LvpKk9x6XAxq7EMzKta%2Fimage.png?alt=media\&token=2ed81bd5-b35f-4ebe-8911-921c0b7ef2a0) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FgVsuWrJHNvwsBcwhTkmH%2Fimage.png?alt=media\&token=e72b5db7-6f28-4d7f-a166-11c687a469c9) |

### How does it work?

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
* To edit an agent, navigate to the Agents tab in the top menu, search, and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
* Click Edit to unlock the agent before editing.
  {% endhint %}

**To enable the Soft unhandled feature in your LLaMB agent**:

* In the `Agent -> Skills` page, click `Unhandled` skill.
* In the `Skill message` pop-up,&#x20;
  * Click the `Delete` icon next to the existing default text message to delete the message.
  * Add a `Javascript response` and add the following code. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.

```javascript
if(!context.unhandled_stream_url){
  return "I am sorry. I don't have an answer for that."
}
return {stream: {url: context.unhandled_stream_url}}
```

* Click `Save` and test your agent. When testing your agents, based on the context or relevance soft-unhandled response is displayed. If the user query is irrelevant and out of context, then the agent still displays an unhandled response. See [Test your agent](https://docs.avaamo.com/user-guide/llamb/get-started/step-3-test-your-agent), for more information.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7LvpKk9x6XAxq7EMzKta%2Fimage.png?alt=media\&token=2ed81bd5-b35f-4ebe-8911-921c0b7ef2a0)

### Feedback on Soft-Unhandled response

By default, feedback options - thumbs up and thumbs down are not displayed for soft-unhandled responses. If you wish to configure the feedback option for soft-unhandled response:

* Retain the default unhandled response as-is.
* Add a Dialog skill with `Pre-unhandled intent` , in the invocation intent, specify the following code:

```javascript
if(!context.unhandled_stream_url){
  return false;
}
return true;
```

See [Pre-unhandled intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent#id-5.-pre-unhandled-intent-handler), for more information.

* In the first node of the `Pre-unhandled Dialog skill`, add the following code:

```javascript
return {stream: {url: context.unhandled_stream_url}}
```

* Enable the `Collect feedback` option in the `Advanced Settings` section. See [Advanced Settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#collect-feedback), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxuMUhhwDMTBsh36jns9V%2Fimage.png?alt=media&#x26;token=64c27127-0f57-4167-a5ba-57c81b557480" alt=""><figcaption></figcaption></figure>

* Test the agent to view the thumbs-up and thumbs-down options on soft-unhandled responses:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPDOlRBIC4oCRKIEVIYD0%2Fimage.png?alt=media\&token=5f40628e-729e-4e26-be00-e7c41d2f9f29)

### Soft unhandled multilingual support

The Avaamo platform supports **soft unhandled messages in multiple languages**, enhancing user experience for multilingual audiences. When a user’s query is related to the document but does not match any exact information, the system now returns the soft unhandled message in the user’s selected conversation language.

The image below illustrates a soft unhandled message displayed in Hindi.

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FgBYxmrPfkchTsONBowmB%2Fimage.png?alt=media&#x26;token=77b527fb-0b8d-4417-b0e8-c6fbcbfda86c" alt="" width="375"><figcaption></figcaption></figure></div>
