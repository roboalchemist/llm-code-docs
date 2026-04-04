# Source: https://docs.avaamo.com/user-guide/llamb/get-started/step-1-create-llamb-content-skill.md

# Step 1: Create LLaMB Content skill

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
* To edit an agent, navigate to the Agents tab in the top menu, search, and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
* Click Edit to unlock the agent before editing.
* You can apply the Outro messages to the LLaMB skill. Refer [Global Outro skill](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent#global-outro-skill), for more information.
  {% endhint %}

{% hint style="warning" %}
**Key point:** PII data is masked by default in all LLaMB responses.
{% endhint %}

**To create LLaMB Content skill:**

* In the Agent page, navigate to the Skills option in the left navigation menu, and click `Add skill` in the Agent Skills page.
* In the `Skill builder` page, click `LLaMB Content`.&#x20;
* Specify the following details and click `Create`:&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FYZ09s3fEbZs1JwhzIrrD%2FScreenshot%202026-01-28%20at%203.34.48%E2%80%AFPM.png?alt=media&#x26;token=fffb30ba-0443-4133-abe9-f9aae853c255" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="169.34445446348062">Parameters</th><th width="421.3333333333333">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Skill name</td><td>Indicates the name of the skill. </td><td align="center">50 characters</td></tr><tr><td>Skill description</td><td>Indicates the description of the skill. Use this to specify the purpose of the skill. </td><td align="center">200 characters</td></tr><tr><td>Skill key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the skill. </p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. </p><p></p><p>Note that the skill key must be unique in the agent. You can specify the same identifier in the <a href="../../how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control">flow control statements</a> such as Goto node. It helps in easy identification and readability.</p></td><td align="center">20 characters</td></tr><tr><td>Collect Feedback</td><td>Indicates whether you wish to enable user feedback. By default, it is set to true. Use the slider for setting to false.</td><td align="center">NA</td></tr></tbody></table>

&#x20;A new empty `LLaMB Content` skill is created. The next step is to add documents or URLs to the skill.

### Next Steps

You can start by [ingesting any of the supported file formats](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1) into your `LLaMB Content` skill. Once some content is uploaded successfully, you have created a knowledge base and your `LLaMB Content` skill is ready for [testing](https://docs.avaamo.com/user-guide/llamb/get-started/step-3-test-your-agent).

You can then continue to fine-tune and edit the knowledge base by adding vocabularies and acronyms. See [Edit knowledge base](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge), for more information.
