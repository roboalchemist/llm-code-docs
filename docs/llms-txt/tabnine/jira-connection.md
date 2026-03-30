# Source: https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/jira-connection.md

# Jira Connection as Context

## What is the Jira Connection?

Tabnine's AI Chat allows you to connect to Atlassian Jira and extend the context of your chat with Jira issues. This capability enables you to ask Tabnine chat how to implement specific Jira issues or to validate whether your implementation aligns with the requirements detailed in those Jira issues. By bringing Jira into your IDE, you can streamline your workflow and minimize context-switching between different tools.

{% hint style="info" %}
**Note**

Tabnine Enterprise customers can integrate with either[ Jira Cloud or Jira Data Center](https://docs.tabnine.com/main/welcome/readme/integrations/atlassian-jira#supported-matrix). While the setup process differs for the Enterprise admin, the workflow and experience remain the same for end-users, as outlined on this page. **We do support multiple instances for Jira Cloud**.
{% endhint %}

## How to Use the Jira connection

### Step 1: Connect to Jira

First, you need to connect your Tabnine plugin in the IDE to your Jira account:

1. In your IDE, navigate to **Chat** **Settings.**
2. Under Settings, find the Jira section and click <mark style="background-color:green;">**Connect**</mark>**.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0ee02e41922711ecbec95c5b6e9f280acdc6c55c%2FJira-%20settings.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Troubleshooting**\
If the browser doesn’t open automatically for the next step, manually paste the following URL into your browser:

`<Tabnine server URL>/app/auth/jira`\
For example: [`https://console.tabnine.com/app/auth/jira`](https://console.tabnine.com/app/auth/jira)
{% endhint %}

3. Next, authorize access to Jira. A browser window will open, directing you to your Jira account. You’ll be prompted to give Tabnine access to your Jira workspace. Click <mark style="background-color:blue;">**Accept**</mark> to confirm connecting Tabnine to your Jira workspace.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c1f96ab90f87085d365726b8d5865ebd094f2675%2FJira%20-%20accept.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

4. After authorization, you’ll be redirected to the Tabnine web application.

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-442e1fa6afedc96430afa11b2a7deb44384f42a7%2FJira%20success.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
5. Return to your IDE. In the chat settings, you can see that Jira has been successfully connected. There will also be an option to <mark style="color:red;">Disconnect</mark>.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a046d33a4f1f4b00c266d7374265fa41798eefe6%2FJira%20disconnect.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Demo**

{% embed url="<https://youtu.be/KuTECwe1cv8?si=TjZRtm0RYDnk9kUr>" %}

You’re now ready to start using Jira in Tabnine Chat!

### Step 2: Mentioning Jira Issues in Tabnine Chat

Once the connection is established, all the Jira issues assigned to you as an individual user are available in Tabnine. Tabnine uses the existing Jira user permissions to ensure that only the issues assigned to you are available.

You can start referencing Jira issues in your chat prompts using any of these three triggers:

1. **Jira button:** Click the Jira button ( <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2b3f0eada1aa273584aac69b56b003f67f5ba6a8%2FJira%20icon.png?alt=media" alt="" data-size="line"> ) in Tabnine Chat.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-bb9407d2ca187c98240097de9aa0dd017ac87b6d%2FJira%20-%20jira%20cta.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

2. **Mention button:** Click the mention button ( <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5e91fc4af3ed25d4c926ed43ef63c7c7b33d2137%2FMention%20icon.png?alt=media" alt="" data-size="line"> ) and choose Jira from the menu.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e0507034382f7e1dba4d2ef7da29e99b47750e0a%2FJira%20-%20menu%20CTA.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

3. **Type directly:** Manually type **`@Jira:`** in the chat prompt.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a61834414c51431b658aecb04a60e297e48fff59%2FJira%20-%20type.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

**For all triggers:**

* You’ll see a list of assigned Jira issues ordered by the last update.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-70fabc395228d42000ad9e48bbf492241448dcfe%2FJira%20-%20show%20issues.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* You can filter the list by typing a prefix.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b1186e4484d14da77db9dd5c294eb2254aa8f551%2FJira%20-%20prefix.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* **Hover for details:** See the issue title when hovering.
* **Multiple mentions:** Add more than one issue to a single prompt.

### Does the Jira connection work with any issue format?

The Jira connection is flexible and doesn’t require issues to follow a strict template, but certain formats are more effective for producing relevant results. Here are some guidelines:

**Optimized for:**

* Self-contained, smaller scope tasks
* Specific tasks that include enough detail
* Jira issues written in both formal and informal formats

**Not optimized for:**

* Large, broad issues that lack specificity
* General tasks without concrete details
* Complex, multistep tasks without clear breakdowns

#### Examples

**Not a good fit:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fa41cd9bf4938123ebd153f4b7a910fac46a16b4%2FJira%20bad%20example%202.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-bd7e437fac1e3b9feb62eec49b64d810b220ea6b%2FJira%20-%20bad%20example%201.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

**Yes a good fit:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-72b57b316d18cc092c5029329e8d48707999fba7%2FJira%20good%20example%203.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-88bd78a04f8d907fa100cb9e24bd57e1850709f9%2FJira%20-%20good%20example%201.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-31fb6bd81bbaf3150c1ad2c8b0e6394ecffd66ac%2FJira%20-%20good%20example%202.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Use Cases for Jira Mentions

#### Implementing a Jira Issue:

Possible prompts:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f5a1874856998b909aaa2c77da3df045fb674805%2FJira%20implememnt%201.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9003e8dd286a8df8f9965b4758e83b75c256bf3f%2FJira%20apply.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9e8b1569fd98ec95991c73a9013e6e17f23065fe%2FImplement.png?alt=media" alt=""><figcaption></figcaption></figure>

Demo:

{% embed url="<https://youtu.be/d8i7MEdvG2U?si=W5J7uGvKMZEvTVC3>" %}

#### Code Validation:

Possible prompts:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a70771497b38c601f1df98409f8590b4bc424526%2FJira%20review.png?alt=media" alt=""><figcaption></figcaption></figure>

Demo:

{% embed url="<https://youtu.be/Gv_M8OVNB5I?si=c67pJXa3odTiPwzM>" %}

#### Multiple Issue Mentions:

Possible prompts:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d08cff92c8942f956ffa22b08d7d3b16c89a32c7%2Fmultiple.png?alt=media" alt=""><figcaption></figcaption></figure>
