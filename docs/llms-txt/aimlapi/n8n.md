# Source: https://docs.aimlapi.com/integrations/n8n.md

# n8n

## About

[**n8n**](https://n8n.io/) is an open-source workflow automation tool that lets you connect various services and automate tasks without writing full integrations manually.

**Key features**:

* **No-code / low-code interface:** Build workflows visually using a drag-and-drop editor.
* **Extensive integrations:** Comes with 350+ prebuilt nodes for popular services like Slack, GitHub, Google Sheets, OpenAI, and many others.
* **Flexible logic:** You can inject custom JavaScript at any point in the flow for more control.
* **Self-hosting:** Run it locally or on your own server—no need to send data to external clouds.
* **Extensibility:** Easily create custom nodes or connect to any API.

n8n is popular with developers, product teams, and analysts who want to automate repetitive tasks, streamline processes, or create event-driven workflows—without building everything from scratch.

***

## Installation

### What installation type should I use?

| Feature                      | Option 1: Community Node | Option 2: npm Install |
| ---------------------------- | ------------------------ | --------------------- |
| Setup Complexity             | 🟢 Very Easy             | 🟡 Medium             |
| Requires Restart             | ❌ Usually not            | ✅ Yes                 |
| Model Catalog Access         | ✅ Full (chat only)       | ✅ Full (chat only)    |
| Supports Cloud & Self-Hosted | ✅ Yes                    | ✅ Self-hosted only    |
| Recommended For              | Most users               | DevOps & power users  |

***

### ✅ Option 1: Use AI/ML API with Community Node Plugin (Recommended)

This is the easiest and most reliable way to use AI/ML API in n8n. It requires no coding and gives you access to a dedicated **AIMLAPI** node directly in the n8n workflow editor.

You will go from account creation to receiving your first AI response in just a few steps.

***

**Step 1: Sign up for AI/ML API**

* Visit <https://aimlapi.com/app>.
* Register an account with Google or email.
* After logging in, navigate to [your dashboard](https://aimlapi.com/app/keys).
* Create and copy your **API key**.

***

**Step 2: Set up your n8n account**

* Go to <https://n8n.io/> and click **Sign Up**.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-98bf88ce2a405ead2937958421c08bb426325ba8%2Fstep-1.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* Fill out the registration form.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-f82eed5f9884af2b5d49680d9a605375d4e96fb9%2Fstep-2.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
* Wait while your workspace is created.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4be813d4ae3ef374f6653adc303ad97afd5fc0b9%2Fstep-3.png?alt=media" alt="" width="512"><figcaption></figcaption></figure></div>
* You will be redirected to your personal n8n workspace.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-8d8702e7998a862c6a37b0824a9f2b8a4cc918c3%2Fstep-4.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* Click **Start from scratch** to open the editor.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-165ff840f398e37e3aea0962b6936dbc9b15436d%2Fstep-5.png?alt=media" alt=""><figcaption></figcaption></figure></div>

  \ <img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-c4f5db1fe2185becde3b0af84c4e536a1bd5bc03%2Fstep-6.png?alt=media" alt="" data-size="original">\\
* Click **Add first step** to begin building your workflow.\ <img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-9cf568607872665317ab661f5dac1afbbabceae1%2Fstep-7.png?alt=media" alt="" data-size="original">\\
* Select the node **When chat message completed** as a trigger.\
  ![](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-8e93b60f0fe924893cb01ca5d4207f1ea68fa186%2Fstep-8.png?alt=media)\\

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-1d15ce969975fdc754eb674837ca91cc6a4431ab%2Fstep-9.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

**Step 3: Add and install the AI/ML API Node**

* Click the **+** button on the right side of the trigger node.\
  Search for **AI/ML API**.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-115b442797f9687f3e9907a68ffe3f610db01480%2Fstep-10.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

  \
  ![](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-72cc31b887774b8cd4fe700660faf197c5177513%2Fstep-11.png?alt=media)\\
* Click on **AI/ML API**, then click **Install node** → **Add to workflow**.\
  ![](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-53dc681881adc45de8eef59a163c9fe5236dd336%2Fstep-12.png?alt=media)\\
* The node will appear in your workspace.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-f304c665c282989169e62971ed4d2d576ef80fa1%2Fstep-13.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

**Step 4: Connect your API Key**

* Click **Create new credentials** in the AI/ML API node.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a45621df3f900123d533683f27318f0d89039ea5%2Fstep-14.png?alt=media" alt=""><figcaption></figcaption></figure></div>

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-7410d658b68ee47f98cd0e2e0b6ce5ff67260284%2Fstep-15.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* Paste your **API key**.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-bdbab04a65cda1f1b2cd95ac4d99893a3502812d%2Fstep-16.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* Click **Save**.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-b65e3ca708c444b8a76889d4977f546caaf87575%2Fstep-17.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

**Step 5: Configure the model and the input**

* Select the model (e.g. `GPT 4o`) in the **Model Name or ID** field.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-868f20f6220c667ec23bbfc83322d6e8aab2b796%2Fstep-18.png?alt=media" alt="" width="307"><figcaption></figcaption></figure></div>
* Click **Execute previous node** to simulate user input and activate the chat input panel.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-9c5e883eacb9ae4a4a4361df28c241e22d2a3a0a%2Fstep-19.png?alt=media" alt=""><figcaption></figcaption></figure></div>

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-8e81dcfe92d5d1688e4fee05524c8e55210405cc%2Fstep-20.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* Type a test message in the input field (e.g. “Tell me a fun fact”) and click **Send**.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-bbbdf38f17e6615d8cacd3234d3337afa97a9c80%2Fstep-21.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

**Step 6: Pass the input to AI/ML API**

* Go back to the **AI/ML API node**, select the **Prompt** field.\
  Click the **Expression** button.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6bded6c4a26aec03bb4889c70decb5a43631d868%2Fstep-22.png?alt=media" alt=""><figcaption></figcaption></figure></div>

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-f844e9951436cce2f9ece89a6919016784bb0fd9%2Fstep-23.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* In the expression editor, expand **chatInput** on the left.\
  Drag and drop it into the **Prompt** field.

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-3b27e5b23b0b580f8eb5706d5b3c8b9856dcd467%2Fstep-24.png?alt=media" alt=""><figcaption></figcaption></figure></div>

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-3f89758c6a4e5c35ea5696a1e23b8430e9a94d7a%2Fstep-25-full.png?alt=media" alt=""><figcaption></figcaption></figure></div>

#### **Step 7: Run the flow**

* Exit the node editor and click **Execute Node** (or the full workflow ▶️ button).

  <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-abafc645f0b1d5e8c1c29bdfdf7874996af6df2a%2Fstep-26.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* You will see the AI/ML API response in the **Output** tab.\
  ![](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-c257c9e929ba2d26195eed5932407aac5f68a32f%2Fstep-27.png?alt=media)

***

🎉 **You’re all set!**\
You’ve successfully built a working chat interaction using AI/ML API and n8n.

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-98fc90a6a54358f660fb75bdc3599ce924f2441c%2Fstep-28.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

### 🛠 Option 2: Use AI/ML API via npm Package (Manual, Self-Hosted)

If you're running **n8n in a custom/self-hosted setup** and prefer to manage dependencies manually, you can install the AI/ML API plugin using `npm`.

> ✅ **Note:** This option gives you **exactly the same features and interface** as Option 1.\
> The only difference is how the plugin is installed. Once it's added, the node usage, credentials, prompts, and output are identical.

***

#### 📝 Installation via npm

1. Navigate to your self-hosted n8n directory
2. Run:

```bash
npm install n8n-nodes-aimlapi
```

If you’re using Docker:

* Mount the plugin as a volume into `/home/node/.n8n/custom`, or
* Extend your `Dockerfile` and include the plugin in `package.json`.

📦 [Plugin on npm](https://www.npmjs.com/package/n8n-nodes-aimlapi)

3. Restart your n8n instance to register the new node.

***

#### 🧩 Continue with Setup from [Option 1](#option-1-use-ai-ml-api-with-community-node-plugin-recommended)

Once the plugin is installed and n8n restarted, continue from the following steps:

* **Step 3**: Add and install the AI/ML API Node
* **Step 4**: Connect your API Key
* **Step 5**: Configure the model and the input
* **Step 6**: Pass the input to AI/ML API
* **Step 7**: Run the flow

Everything works the same as in Option 1 — including system/user messages, prompt injection, and output formatting.

***

## How to Use the AI/ML API in n8n

After completing the installation and setup steps described above, you can start using the configured model node in your workflows — for example, to build chatbots. For guidance on building different types of workflows, refer to [the official n8n documentation](https://docs.n8n.io/).

You can also test the model's responses in the **Chat** window located at the bottom left of the editor.

{% hint style="warning" %}
Please note that this chat is intended for debugging purposes only. It does not represent the actual experience your end users will have. The formatting here is optimized for development and may include special tags or symbols. Your users will see clean, properly formatted responses as expected.
{% endhint %}

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-f38f26af42e1f41f6776c6e4f9deabb955b7298d%2Ffull-with-chat.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

## 💬 Example Settings

#### [GPT 4o](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)

<table><thead><tr><th width="305">Field</th><th>Value</th></tr></thead><tbody><tr><td>Model</td><td><code>openai/gpt-4o</code></td></tr><tr><td>User Message</td><td><code>"Give me ideas for YouTube channels"</code></td></tr><tr><td>Temperature</td><td><code>0.7</code></td></tr></tbody></table>

#### [Gemini 2.0 Flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash)

<table><thead><tr><th width="305">Field</th><th>Value</th></tr></thead><tbody><tr><td>Model</td><td><code>google/gemini-2.0-flash</code></td></tr><tr><td>User Message</td><td><code>"Write a summary of the latest Apple event"</code></td></tr></tbody></table>

***

## 📎 Links

* 🔑 [Get your API key](https://aimlapi.com/app/keys?utm_source=n8n\&utm_medium=github\&utm_campaign=integration)
* 🧪 [Model playground](https://aimlapi.com/app?utm_source=n8n\&utm_medium=github\&utm_campaign=integration)
* 💬 [Join the community](https://aimlapi.com/community?utm_source=n8n\&utm_medium=github\&utm_campaign=integration)

Let us know what you build — we’d love to feature your workflows!
