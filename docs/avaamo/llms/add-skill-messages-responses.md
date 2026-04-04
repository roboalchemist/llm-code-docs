# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses.md

# Add skill messages (responses)

You can add rich responses to user queries in a Dialog skill. This can be as simple as a text message, card, quick reply, or complex JavaScript.&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can build and manage dialogs (conversational flow) immediately after creating a Dialog Skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.
* If you wish to edit a skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

{% hint style="success" %}
**Key point**: If the agent response contains sensitive PII data such as name, account number, password, then it is recommended to mask the agent responses to protect user privacy. See [Agent response masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#masking-agent-responses), for more information.
{% endhint %}

**To add a skill response**:

* In the **Dialog skill** page, click **Edit** to unlock the skill&#x20;
* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;
* In the conversation flow tree, click **Add agent response** in the node where you wish to add the skill response.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma8WwQrzv4nKCrqpodZ%2F-Ma8XNepZjRik04aQcKL%2F5.7-add-skill-messages.png?alt=media\&token=f7e20fda-f196-4413-8395-3d116ee6afb6)

* In the **Skill message** pop-up, on the left panel, click the plus (+) icon to open the list of skill responses and select the response type.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MQAexPslzeIUN6-wEcB%2F-MQAi0AQGa0CQ1J21Ppl%2Fskill-response-types.png?alt=media\&token=cb11370d-78cd-489e-81a4-0575f7d1bcac)

* In the **Prompt details** tab,&#x20;
  * Specify details according to each response type - [Agent voice](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#agent-voice), [Voice menu](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#voice-menu), [Text](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#text), [Quick Reply](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#quick-reply), [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#card), [Carousel](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#carousel), [ListView](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/list-view), [JavaScript](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#javascript), [Integrations](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#integrations), [Audio](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#audio), [Video](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#video), [Files](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#files), and [Switch Persona](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#switch-persona).
  * Skip Translation: Check if you wish to skip the translation of this message when displayed to the user. By default, all the responses are translated into the detected languages.
* Set [Advanced Settings ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings)as required.&#x20;
* Click **OK** to save the skill response.&#x20;

### Agent voice

{% hint style="info" %}
**Note**: This option is enabled only if you have deployed your agent in the C-IVR channel. See the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
{% endhint %}

You can use "Agent voice" to add SSML tags as agent responses in your C-IVR channel. When you add the SSML tags, the text is read out by the agent to the user in the C-IVR channel.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO1t8ZKuklYSfvhZWUG%2F-MO1vCKS8hyDd6eZYoE9%2Fagent-voice.png?alt=media\&token=55095f06-b675-43ae-b39a-b2b50dc322ce)

* In the **SSML response text area**, you can click the tags provided under SSML and add or modify the responses as required. See [Speech Synthesis Markup Language (SSML) Version 1](https://www.w3.org/TR/speech-synthesis11/#S3.1.), for more information.
* In the Avaamo Platform, all standard SSML tags such as Speak, Break, Lang, Emphasis, Say As, Phoneme, and Sentence are supported: See [Supported SSML tags](https://docs.avaamo.com/user-guide/ref/speech-synthesis-markup-language-ssml), for more information.
* You can use the play button to play and preview the response. You can also download the file if required.

{% hint style="info" %}
**Note**: You can view a list of all invalid SSML errors in the JS Errors page when a user query triggers a response from the node where SSML is configured and is invalid. See [JS Errors](https://docs.avaamo.com/user-guide/build-agents/debug-agents#using-js-errors), for more information.
{% endhint %}

### Voice menu

{% hint style="info" %}
**Note**: This option is enabled only if you have deployed your agent in the C-IVR channel. See the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
{% endhint %}

You can use the "Voice menu" to add menu options as agent responses for your C-IVR channel. When you add the voice menu option, the agent reads out the voice options in the format - "Press 1 or say <\<button name specified>>".

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MQB3d08k7bLnZsPlu9a%2F-MQB480l6ivNgiiTxjQ_%2F5.5-voice-menu-options.png?alt=media\&token=cf41d920-e63a-407b-9935-0c6de40a270f)

* Click the **+** icon to add voice menu options:
  * For each option, specify the button name that is read out in your voice menu option.
  * **Voice command:** Executes the command and provides the response, if any. The voice command must be one of the invocation intent in the Dialog skill or intent in Q\&A and Smalltalk skill.&#x20;
  * **Goto node**: Transfers the flow to the specified node number. As you type, the node number if available is displayed in the list. Select a node to transfer the flow. Specify in the format - <\<Skill number>>.<\<node number>>. Example: If you specify 4.2, then the flow is transferred to node 2 of skill number 4.
  * **Goto main menu**: Transfers the flow to the main menu.
  * **Spacing**: Indicates the number of seconds the agent waits before repeating the menu option. The default value is 0 seconds.
  * **Repeat menu**: Indicates the number of times the menu is repeated. Enter 0 to not repeat the menu options. The default value is 0.
* You can also add SSML tags along with the voice menu options. The text in the SSML tag is read out in the agent response before the voice menu option. This is optional. In the Avaamo Platform, all standard SSML tags such as Speak, Break, Lang, Emphasis, Say As, Phoneme, and Sentence are supported. See [Supported SSML tags](https://docs.avaamo.com/user-guide/ref/speech-synthesis-markup-language-ssml), for more information. You can use the play button to play and preview the response. You can also download the file if required.

{% hint style="success" %}
**Key Points**:

* In the case of an unhandled response: The Agent voice or Voice menu configured in the unhandled response is read out to the user.&#x20;
* In the case of disambiguation: The disambiguation menu options are read out to the user to proceed further.
  {% endhint %}

### Call forward

{% hint style="info" %}
**Notes**:&#x20;

* This option is enabled only if you have deployed your agent in the C-IVR channel. See the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
* Call forward works only with real devices. Currently, the Call forward option is not supported in the agent simulator.
  {% endhint %}

You can use a **Call forward** response to forward the call to another number such as a help center number or a call center number, in case the user requires any further assistance in the C-IVR flow.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO2-WSuJa0jQ6BB9sNV%2F-MO4qiMYM-Pyjj1pEqeH%2Fcall-forward.png?alt=media\&token=32bece0a-a3d5-4e7a-acec-bad944808652)

* In the Phone No. text box, provide the complete phone number with a country code.
* In the **Message text box**, specify any message that you wish to be read out to the user before forwarding the call to the number.&#x20;

{% hint style="info" %}
**Note**: You can also add a call forward using a JS method. See [Forward call (C-IVR)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/forward-call-c-ivr-channel), for more information.
{% endhint %}

### Text

You can use this to add simple display text. Example: Greeting message, Welcome message. In the Text response, enter the required text in the Message box.

{% hint style="info" %}
**Note**: You can also access a context attribute using ${context.<\<attributes>>} in a text message. See [Use Context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context), for more examples.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO1moicGnJ_8jZlCOlP%2F-MO1qvtn-9og5LW-1_zR%2Fdialog-welcome-message.png?alt=media\&token=1a8b9eda-c926-45b7-99bd-170cc4255c0f)

### Quick reply

You can use a quick reply to add an acknowledgment to the user's questions or responses with buttons to provide any further options. Example: "Thank you", "you are welcome", "That sounds good". In the Quick Reply response, specify the following details:

* **Message**: Enter the required text in the Message box. You can also access a context attribute using ${context.<\<attributes>>} in the quick reply message. See [Use Context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context), for more examples.
* **Add Button**: Add buttons in the quick reply message, as required. See [Add Buttons](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-buttons), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO2-WSuJa0jQ6BB9sNV%2F-MO4rBOjzH52e1VZAIOD%2Fdialog-skill-quick-reply.png?alt=media\&token=ef363b41-2e21-41fb-a911-9c61c9a275a9)

### Card&#x20;

You can use the card to add a rich detailed skill response with Title, Image, Description, Buttons, and Elements. Example: A card with a pizza image and a button to select a pizza size. In the Card response, specify the following details:

* **Aspect ratio**: Select the aspect ratio. This is the ratio of the width to the height of an image.&#x20;
* **Title**: Enter the title of the card message.
* **Showcase Image (Optional)**: Upload an image for your card. This is optional.
  * Recommended image types: PNG, JPEG
  * Recommended image size: 800px \* 420px (width to height)

{% hint style="info" %}
**Notes**:&#x20;

* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.

* In MS teams channel,
  * Buttons on the card can show the label up to 45 characters.
  * Embedded HTML for labels (HTML code inside title or description of a card) is not supported.
  * See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.&#x20;
    {% endhint %}

* **Description**: Enter the description of the card message.

* **Add Button**: Add buttons in the card message, as required. See [Add Buttons](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-buttons), for more information.

* **Add Element (Optional)**: Add form element in the card message, as required. You can add upto 25 form elements to the card. See [Add Form Elements](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-form-elements), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO53RsjtoQOaTEewtQH%2F-MO7ANQi8GW4ZuZDid3M%2Fdialog-skill-card.png?alt=media\&token=27ea2bee-56ab-472f-a5fc-44562cfe5481)

### Carousel

You can use the carousel to add a set or series of cards, each with a Title, Image, Description, Buttons, and Elements. See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#card), for more information. Click the plus (+) icon on the left to add more cards to the carousel. Example: A carousel of starter cards in a pizza order.

{% hint style="info" %}
**Note**: You can add upto 25 cards to the carousel.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO53RsjtoQOaTEewtQH%2F-MO7Atlsa-uyh000KkdC%2Fdialog-skill-carousel.png?alt=media\&token=66dfeb23-fd79-4b63-a5a4-8f34ddd55e08)

### Agentic text

You can use this to add simple text to the display. Instead of static responses, the agent uses this to generate responses dynamically.

* Example:\
  \&#xNAN;*“Ask the user what size of pizza they want.”*

This enables more natural, less repetitive conversations.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fsu4qD8BZ5aEmE8VvvNnT%2FScreenshot%202026-01-15%20at%2012.16.17%E2%80%AFPM.png?alt=media&#x26;token=9bd9e15b-13be-4f1f-bf6f-50ffec8df6b9" alt=""><figcaption></figcaption></figure>

### ListView

You can add a list of items or options with Title, Image, Description, and Buttons. Example: A list of special offer options in a pizza order. In the ListView response, specify the following details:

* **Top Element Style**: Style for the first item in the list. By default, it is Large. A large element style provides more space at the top. Select Compact if this is not required.
* **Items**: Add an item to the list. You can add upto 50 items in the ListView. Each item contains:
  * **Title**: Specify the title of the item.
  * **Subtitle (Optional)**: Specify the sub-title of the item.
  * **Image (Optional)**: Upload any image for the item.
  * **Add button**: Add button for the list item, as required. See [Add Buttons](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-buttons), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.

* In the Microsoft Teams channel, the ListView top element style is only supported when an image is passed to the item due to the limitation on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
  {% endhint %}

* **Add button (Optional)**: Add button for the entire list view, as required. See [Add Buttons](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-buttons), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO7AyUYwemXQWznFF6h%2F-MO7BMhPxNFok3Wb8pfd%2Fdialog-skill-list-view.png?alt=media\&token=1a93c526-54bf-4652-85dc-b3c9af816830)

### JavaScript

You can leverage Avaamo Platform's robust library with a rich set of objects and functions to customize and create enterprise skill responses using JavaScript.&#x20;

* See [Using Script and Code](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill), for an exhaustive list of functionality that can be achieved using JS.
* Use `CTRL+ENTER` key to toggle between fullscreen mode. You can view the complete list of built-in functions with syntax and examples in the Built-in functions window available in the JS editor. See [Built-in functions window](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/built-in-functions-window), for more information.

{% hint style="info" %}
**Note**: Any JS block must execute within 30 seconds and return a response back. If there is a JS block that takes more than 30 seconds, then you must consider reviewing the code and improving the response time.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO7AyUYwemXQWznFF6h%2F-MO7BggGs2Cc0dDhNuXX%2Fdialog-skill-js.png?alt=media\&token=7d7a91ff-9623-4b0d-b8f3-e3eaac9a3a38)

### Integrations

You can integrate skills with other third-party services such as Oracle Right Now, Zendesk, Hybrid SDK (to name a few). The most common integrations is via API (REST, SOAP) or using Hybrid SDK. See [Integrate](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/integrate-with-api-1), for more information.

### Audio

You can add an audio file to your skill response. **Example**: A set of instructions or notice. In the Audio response, click Upload mp3 to upload an mp3 audio file. &#x20;

{% hint style="info" %}
**Notes**:

* You can upload only one file at a time.
* Each file size can be upto 25MB.
* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF4D4MvGfXokBXeXjKb%2F-MF4K9lmZ0Tj7fk4D30R%2Fdialog-skill-audio.png?alt=media\&token=9345e13d-530d-4b60-ae14-742e2f65ac91)

### Video

You can add a video file to your skill response. Example: A demo of the product. In the Video response, click Upload video file to upload a video file.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* You can upload only one file at a time.
* Each file size can be upto 25MB.
* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.
  {% endhint %}

### Files&#x20;

You can add a file to your skill response. **Example**: A form. In the **Files** response, click the **Upload file** to upload the file.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* You can upload only one file at a time.
* Each file size can be upto 25MB.
* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.
  {% endhint %}

### Delay

You can add this to include a delay between two responses. This helps the user to read the responses that are verbose, instead of displaying all the responses at once and hence provides a better conversational experience. By default, the value is displayed as 3 seconds. You can increase the time upto 30 seconds if required.&#x20;
