# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/language-pack.md

# Language pack

Typically, in any global business, it is a necessity to design and build assistants or agents that can interact with the users in their local language. The Avaamo platform provides multilingual support for agent development in different languages, with English (en-US) as the default language.

In the Avaamo Platform, you can add multiple languages to the agent, so that the agent can respond in different languages as per your business requirement both in text and voice.

## How does it work?

Adding a language to your agent is a simple three-step process:

* [Step 1: Configure or add languages in your agent](#step-1-configure-or-add-languages-in-your-agent)
* [Step 2: Customize translations](#step-2-customize-translations)
* [Step 3: Test your agent](#step-3-test-your-agent)

{% hint style="success" %}
**Key Point**: Agent conversation starts with one language and continues in the same language. If you wish to change the language of the agent response, say, based on the user's request or response, then you can identify and switch the language in your agent.&#x20;

See [Step 3: Test your agent](#step-3-test-your-agent), for more information.
{% endhint %}

### Step 1: Configure or add languages in your agent

The first step is to add languages to your agent in the **Agent -> Configuration -> Languages** page. Consider that in your Pizza agent, you wish to add the French language to your agent.&#x20;

* In the **Agent page**, navigate to the **Configuration -> Language** tab option in the left navigation menu.&#x20;
* Click **Add languages** and select the **French** language from the dropdown.&#x20;
* Click **Save** to save the agent language configurations.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjZoEZrVBhvpFB9bFo7sk%2FScreenshot%202021-10-29%20at%2012.23.33%20PM.png?alt=media\&token=7872bbdb-9093-4cd0-920f-8f86c2171d6a)

* When you add a language, all the agent responses are automatically translated into the corresponding language. **Example**: In the Pizza agent, you can check the translated response of the Greeting skill.

  * Click the **Greetings skill**.
  * In the skill response, change the language to French (fr-FR). You can view the translated response of the greetings message.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzeHrY2lzdNaxtPuWeFne%2F6.1-language-agent-greeting.png?alt=media\&token=a8df6a4b-53fa-4a3e-ba7c-fc31f29552e0)

See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages) for more information on how to add and manage languages in your agent.

### Step 2: Customize translations

You can add custom translations to the response based on your requirement. Custom translation can be added in the following ways:

<table><thead><tr><th width="189">Where?</th><th width="567.0997679814386">When?</th></tr></thead><tbody><tr><td><a href="../../../how-to/build-agents/configure-agents/add-languages#add-translation">Agent -> Configuration -> Languages page</a></td><td><ul><li>Use this to provide translations for all sentences and texts used by the agent. Examples: text used in skills, persistent menu, live agent, etc.</li><li>Note that in all the cases, node-level translation has the highest priority. This implies that if you have the same translated text at the agent and the node-level, then the node-level translated response is displayed.</li></ul></td></tr><tr><td><a href="../../../how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#language-specific-responses">Skill responses</a></td><td><p></p><ul><li><p>Use this to provide translation for the selected skill responses. </p><p>See <a href="../../../how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#language-specific-responses">Language-specific responses</a>, for more information.</p></li></ul></td></tr></tbody></table>

Consider that you wish to customize the greeting message in your Pizza agent. The default greeting message in English is "Welcome to MacPizza. How can I help you today?" and this is translated to "Bienvenue à MacPizza. Comment puis-je vous aider aujourd'hui?". You wish to customize to "Bonjour, bienvenue chez MacPizza. Comment puis-je vous aider aujourd'hui?."

* In the **Agent page**, navigate to the **Configuration -> Language** tab.
* Click **Add translation** to enter the English text and corresponding translated text.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ft9CofjDCT6GsidyWc0l7%2FScreenshot%202021-10-29%20at%2012.26.51%20PM.png?alt=media\&token=430390a7-21f3-430b-bca1-adf7deba0b20)

{% hint style="info" %}
**Note**: To customize the response of the Greeting skill, instead of adding the custom translation in the **Agent -> Configuration -> Languages** page, you can add the same in the Greeting skill response. See [Language-specific responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#language-specific-responses), for more information.
{% endhint %}

### Step 3: Test your agent

You can use the **Language.switch** command to switch the language as required. Note that you can only switch to those languages that are configured in your agent. See [Language.switch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/language.switch), for more information.

Consider that in your Pizza agent, based on certain criteria you wish to switch language to French.&#x20;

* Add a JS node in the Greeting message and switch the language as required - `Language.switch('fr-FR');`

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVDm2s2s9uq4jrzE6YZiZ%2F6.1-language-pack-switch-language.png?alt=media\&token=63d060d7-339d-4ab7-b1e7-3a28b35f105c)

* Click OK.
* Click **Save** to save your agent
* Test your agent using the **Agent simulator** from the bottom-right corner. You can now view the custom-translated greeting message in French.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FqsFosJD7FsMYPY0pKRp6%2F6.1-language-pack-test.png?alt=media\&token=fa473ad4-c295-447d-a52b-8f3d6a3ef73a)<br>

## Skip translation

When an agent is multi-lingual, then there can be scenarios, where even though the user is asking the question is a specific language say, French, you still want the agent to respond back in English for certain responses. This can be achieved using the **Skip translation** option available in the response pop-up window.&#x20;

**Example**: Consider the following scenario,

* You have added the French language to the agent.&#x20;
* In the response pop-up window, you checked the **Skip translation** option for French language response.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FTlosfx88mXHndsunaWcR%2Fskip-translation.png?alt=media&#x26;token=d62e92b5-afc2-4ace-85f9-fbe85c6a0cab" alt=""><figcaption></figcaption></figure>

* Now, when the user asks the question in French matching this intent, then the response is displayed in English.&#x20;

&#x20;![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FBQS3jPn71gByuEJiJD26%2Fskip-translation-response.png?alt=media\&token=d8616646-764c-4775-a2ee-08f4a59be762)

## Supported languages

Avaamo platform supports 110+ languages in the web channel such as French, Arabic, Chinese, Polish, and many more. See [Web - supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages), for a complete list
