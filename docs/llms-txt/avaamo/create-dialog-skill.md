# Source: https://docs.avaamo.com/user-guide/skills/dialog-skill/create-dialog-skill.md

# Create dialog skill

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/ai-agent/create-an-ai-agent), for more information.
* If you wish to edit an agent, navigate to the Agents tab in the top menu, search for the agent, and open it. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.
* Click Edit to unlock the agent before editing.
  {% endhint %}

**To create Dialog skills:**

* In the **Agent** page, navigate to the **Skills** option in the left navigation menu and click **Add Skill**.
* In the **Skill Builder** page, select **Dialog Skill** and click **Create**.
* Specify the following details and click **Create**:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMfvEciUJ4D4StFbBNuNi%2FScreenshot%202026-01-14%20at%202.43.23%E2%80%AFPM.png?alt=media&#x26;token=a8243196-e12d-4b98-8b85-49371a93acd7" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="147.953125">Parameters</th><th width="395.69140625">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Skill name</td><td>Indicates the name of the dialog skill.</td><td>50 characters</td></tr><tr><td>Skill description</td><td>Indicates the description of the dialog skill. Use this to specify the purpose of the skill.</td><td>200 characters</td></tr><tr><td>Skill key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the skill. By default, a key is provided when you create a skill. You can change it to any user-friendly identifier.​<br></p><p>Supported characters: Alphanumeric and underscore​.</p><p></p><p>It is recommended that the key be at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information.​</p><p></p><p>Note that the skill key must be unique in the agent. You can specify the same identifier in the <a href="https://app.gitbook.com/o/-LpXFbuTM3h40PfxYgao/s/-LpXFTiTgns4Ml77XGi3/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control">flow control statements</a>, such as the Goto node, and in <a href="https://app.gitbook.com/o/-LpXFbuTM3h40PfxYgao/s/-LpXFTiTgns4Ml77XGi3/how-to/build-agents/test-agents/regression-testing">regression testing</a>. It helps in easy identification and readability.</p></td><td>20 characters</td></tr></tbody></table>
