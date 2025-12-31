# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/create-knowledge-skill.md

# Create knowledge skill

The **Knowledge skill** is designed to empower AI agents by seamlessly integrating and processing information from a variety of content sources—such as documentation, product guides, FAQs, and enterprise systems. With this capability, the agent can deliver accurate, context-aware responses grounded in the most up-to-date information.

Using `Knowledge skill`, users can now integrate a wide variety of content directly from their repositories into the skill, streamlining the content integration and management process.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fi8zlKV3QytZlOfnSrBaf%2FScreenshot%202025-12-09%20at%202.19.00%E2%80%AFPM.png?alt=media&#x26;token=d41895e2-e37e-4293-975e-ff8d5b60379f" alt=""><figcaption></figcaption></figure>

#### Key highlights

* **Content integration**: Ingest structured and unstructured information from documents, web pages, repositories, and other sources.
* **Real-time synchronization**: Connect with systems of record such as `SharePoint`, `ServiceNow`, `web platforms`, and `files` to ensure content is always current.
* **Flexible synchronization modes**: Choose between `AutoSync` for continuous updates or `Manual` synchronization, with execution history tracking for visibility and control.
* **Data management**: Improve processing and integration of information, ensuring consistency, accuracy, and reliability across the knowledge base.
* **Scalability**: Support a wide range of content formats and sources, enabling AI agents to expand knowledge effortlessly.

The Knowledge skill lays the foundation for creating intelligent, self-sufficient AI agents that scale support, reduce manual intervention, and enhance the quality of information delivered to end users.

Based on your requirements, you can create a new Knowledge skill.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/ai-agent/create-an-ai-agent), for more information.
* To edit an agent, navigate to the Agents tab in the top menu, search for the agent, and then open it. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.
* Click Edit to unlock the agent before editing.
  {% endhint %}

**To create Knowledge skills:**

* In the Agent page, navigate to the `Skills` option in the left navigation menu and click `Add Skill`.
* In the `Skill Builder` page, select `LLaMB Content Skill.`
* Specify the following details and click `Create skill`:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3oQYuDuPalZEhtWyTraL%2FScreenshot%202025-09-22%20at%203.20.19%E2%80%AFPM.png?alt=media&#x26;token=ef6af79f-cb03-4767-8c60-ab04ad8988ac" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="189.44475920679886">Parameters</th><th width="359.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Skill name</td><td>Indicates the name of the dialog skill. </td><td align="center">50 characters</td></tr><tr><td>Skill description</td><td>Indicates the description of the dialog skill. Use this to specify the purpose of the skill. </td><td align="center">200 characters</td></tr><tr><td>Skill key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the skill. By default, a key is provided when you create a skill. You can change it to any user-friendly identifier. </p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key be at least three characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. </p><p></p><p>Note that the skill key must be unique in the agent. You can specify the same identifier in the flow control prompts. It helps in easy identification and readability.</p></td><td align="center">20 characters</td></tr></tbody></table>
