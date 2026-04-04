# Source: https://docs.avaamo.com/user-guide/skills/prompt-skill/create-prompt-skill.md

# Create prompt skill

The **Prompt Skill** enables you to create responses using simple effective prompts without any extensive training. It guides the AI agents to interpret, process, and respond to user queries.&#x20;

It is ideal for handling open-ended queries where a structured multi-step dialog is not required. Prompt Skill leverages AI-driven completions to generate contextual responses based on user input.

Examples: The Prompt skill can be used in scenarios such as:

* To book a flight ticket or a doctor's appointment
* Providing an informational response, like FAQs or knowledge base answers.
* Retrieving and displaying dynamic information based on a single input.

In the Avaamo Platform, you can easily create and customize Prompt skills using a simple interface, allowing you to configure specific responses to be triggered by a user’s input. The platform enables seamless integration of the Prompt skill into various workflows with minimal technical effort.

Based on your requirements, you can create a new Prompt skill.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/ai-agent/create-an-ai-agent), for more information.
* If you wish to edit an agent, then navigate to the Agents tab in the top menu, search, and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.
* Click Edit to unlock the agent before editing.
  {% endhint %}

**To create Prompt skills:**

* In the **Agent** page, navigate to the **Skills** option in the left navigation menu and click **Add Skill**.
* In the **Skill Builder** page, select **Prompt Skill** and click **Create**.
* Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F62eHSyzPFXJRFgM1sRPA%2FScreenshot%202025-03-28%20at%204.32.42%E2%80%AFPM.png?alt=media&#x26;token=15432267-f955-4b74-9025-b4ea12741b32" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="123.14111328125">Parameters </th><th width="470.0718994140625">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Set as Entry Point</td><td><p>Click the checkbox to enable this option. When enabled, the skill is triggered at the <code>start of the conversation.</code></p><p><br>If multiple skills are configured, enabling this option designates it as the <code>starting skill</code>, initiating the conversation from the agent.<br><br><strong>Note:</strong> When there is only one Prompt Skill, this option is enabled automatically.</p></td><td>NA</td></tr><tr><td>Skill Avatar</td><td><p>You can upload an image to represent the digital avatar of the agent.</p><p>A built-in crop tool is available to adjust the image size as needed.</p></td><td>The file size should be 2MB maximum.</td></tr><tr><td>Skill name</td><td>Indicates the name of the prompt skill</td><td>190 characters</td></tr><tr><td>Skill description</td><td>Indicates the description of the prompt skill. Use this to specify the purpose of the skill.</td><td>2000 characters</td></tr><tr><td>Skill instructions</td><td>A set of predefined phrases to be displayed on the UAT page.</td><td>1000 characters for each instruction</td></tr><tr><td>Skill key</td><td>A unique identifier assigned to the skill for programmatic identification. It is used for functionalities such as skill transfer and other integrations.</td><td>190 characters</td></tr></tbody></table>
