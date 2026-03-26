# Source: https://docs.tabnine.com/main/getting-started/tabnine-chat/interact.md

# Interacting with Tabnine Chat

How to interact with Tabnine Chat

You can interact and trigger Tabnine Chat in three ways:

1. [Free-form natural language prompts](#option-1-free-form-natural-language-prompt)
2. [Quick actions (global)](#option-2-quick-actions-global)
   * [User-defined quick actions (custom commands)](#user-defined-quick-actions)
3. [CodeLens (method scope)](#option-3-codelens-method-scope)
4. [Personalizing Tabnine Chat](#personalizing-tabnine-chat)

### Option 1: Free-form natural language prompt

Go to the bottom of the Tabnine Chat panel, enter a free text question or instruction, and then click **Enter**.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5b08ab41fc54266a25e17ce54c8053f9e690bf55%2Fimage.png?alt=media" alt=""><figcaption><p>Write a prompt in natural language and click <strong>Enter</strong></p></figcaption></figure>

Tabnine Chat's answer will be rendered quickly:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-593a3b297b0c205e2d605d3f43f5370b1232943d%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Another recommended option is to select a block of code from the current open file and then ask a question regarding this code. This draws Tabnine Chat's attention to the relevant code:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-062ae77bb46af8346b0b860c2f98ccbf94495191%2Fimage%20(81).png?alt=media" alt=""><figcaption><p>Select a code block and give a relevant instruction</p></figcaption></figure>

You can ask anything you want, but keep in mind that Tabnine Chat was designed to answer questions related to code. If you write good prompts that are specific, detailed, and to the point, you increase the chances of getting an accurate and useful result.

#### Mentions

In the natural language prompt, you can use Mentions.

Mentions (using the @ mark) are a way to ask Tabnine Chat to use a specific code element (type, method, or class) from the workspace in the query context. Mentions allow the user to leverage their domain knowledge and help the AI by explicitly focusing it on relevant context from the workspace.

Notes:

1. Mentions work for each language with Language Server Protocol (LSP) support in the IDE.
2. Type 2-3 characters after the “@” to view the available code elements.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d37ae7c633b169582240debd13e66c482fe78c21%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Learn more about the [Tabnine Chat context](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-context-window) and [prompt engineering](https://docs.tabnine.com/main/getting-started/tabnine-chat/prompt).

#### Symbols

You can now use Mentions for "symbols." Symbols represent additional resources that you want to add to the chat context.

To add, use the % sign and then type the file you want.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-6f62d5b2c4a1960794684c419d4540c84f7eb9fc%2FCensored%20Symbols.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="55.0087890625"></th><th></th></tr></thead><tbody><tr><td></td><td><strong>Language Availability for Symbol Mentions</strong></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-051bf254ad782820627890ef2b0e06fbae63dc6e%2FJava.svg?alt=media" alt="" data-size="line"></td><td>Java</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e0e096a24e59fb9f1e501899389e3905c6c27cd7%2FPython.svg?alt=media" alt="" data-size="line"></td><td>Python</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7975261bd47d0112fab7f5a376e1293e56a55584%2FJavaScript.svg?alt=media" alt="" data-size="line"></td><td>JavaScript</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e1db5f196597f0815d315dfacf4191bb3df75fa4%2FTypeScript.svg?alt=media" alt="" data-size="line"></td><td>TypeScript</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d0841f2e61ed3d92232b9cd2c1fbfb4dff4853a1%2FC.svg?alt=media" alt="" data-size="line"></td><td>C</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-acc487eb512c10a78f653a41a72c3f77400bf660%2FC%23%20(CSharp).svg?alt=media" alt="" data-size="line"></td><td>C#</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-6cae2226d09d9b41d074169a19955cbffa104698%2FC%2B%2B%20(CPlusPlus).svg?alt=media" alt="" data-size="line"></td><td>C++</td></tr></tbody></table>

### Option 2: Quick Actions (Global)

Some tasks or instructions are common, so Tabnine Chat includes them as built-in actions.

The following actions operate on the selected code:

* **explain-code:** Explains what the selected code is doing
* **generate-test-for-code:** Writes tests for the selected code
* **document-code:** Suggests documentation for the selected code
* **fix-code:** Fixes the errors (detected by the IDE) for the selected code

You can trigger quick actions by clicking the relevant links when you start a new chat session:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-aa7970facaea1655cd4fe35d67d5d241ec4285f3%2Fimage.png?alt=media" alt=""><figcaption><p>Click quick action links on new chat</p></figcaption></figure>

Another option is to use "/" to view the available quick actions. Select the action you want and click **Enter.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c3db460aa106ace8a981d8f2ff33332dafe19498%2Fimage.png?alt=media" alt=""><figcaption><p>Click "/" to view the available actions</p></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-10db62bf378506de52200a0a8ff61737e6126f0d%2Fimage.png?alt=media" alt=""><figcaption><p>Example of "Explain code" action</p></figcaption></figure>

#### User-defined quick actions

In addition to the predefined commands provided by Tabnine, you can define your own custom commands. This can be useful for repetitive tasks that are specific to your domain:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-949356f6a853293986b6bc5aca45b08086773aeb%2FCustom%20command%20edited_20.gif?alt=media" alt=""><figcaption></figcaption></figure>

To define your own quick action, follow these steps:

1. Click on the **Settings** (<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea60b94769e5eb824538aa287767025a86c830a4%2Fimage.png?alt=media" alt="" data-size="line">) icon in Tabnine Chat.
2. On the Chat settings tab, click **Add** in the **Define custom commands** section.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-da946908380200a94e64e7c8f4797a87c3d66932%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

3. Fill in the slash command name, description, and prompt template fields in the **Define new Command** dialog. Use **$** to include a reference to the **selected code** or **open file** and save the custom command.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c02149ad6a6cbab6c513024c7b2e5069568341a4%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

4. Use the slash ("/") to trigger your custom commands in the chat prompt.

{% hint style="info" %}
Note: Custom commands are personal and saved on the local machine, per IDE. They're not shared between different users or between different IDEs on the same machine. However, they can be shared through an SCM tool.
{% endhint %}

#### Sharing Custom Commands

1. You can then choose to share with your team members, which will prompt Tabnine to create a .tabnine\_commands file within each repository.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ef5b5b433c7b573a8f1f8848d4975ed74e015a22%2Fcommands.png?alt=media" alt=""><figcaption></figcaption></figure>

Users can easily create, edit, and delete commands through this file. The shared file is the single source of truth for commands, making collaboration more seamless and efficient. Each team will be responsible for managing this file. At this time, shared commands do not support mentions.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ed23ad04746bc9379c1931d765f430639266e7a3%2F03%20Sharing%20Custom%20Commands_768_456%20(1).gif?alt=media" alt=""><figcaption></figcaption></figure>

### Option 3: CodeLens (method scope)

{% hint style="info" %}
Available in these IDEs (for these languages):

* **VS Code** (Java, Python, TypeScript & TSX, JavaScript & JSX, Ruby, Go, Rust, Swift, C/C++, C#, PHP)
* **JetBrains** (Java, Python, TypeScript, Rust, Kotlin, PHP, GO, C/CPP, C#)
* **Visual Studio** (all supported languages)
  {% endhint %}

You can trigger the quick actions for the scope of a specific method by clicking the floating Tabnine quick actions:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b562aa55fa180f0caa91043a99b366052af3fe11%2Fquick%20actions%20-%20method%20scope%20(1).gif?alt=media" alt=""><figcaption></figcaption></figure>

### Personalizing Tabnine Chat

#### Chat Response Length

You can now customize your Tabnine AI Chat experience even further, allowing for more control over chat response length and style. Users can pick between “Concise” for a shorter answer, and “Comprehensive” for a longer, further explanation to your prompts in Chat.

1. Click on the **Settings** (<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea60b94769e5eb824538aa287767025a86c830a4%2Fimage.png?alt=media" alt="" data-size="line">) icon in Tabnine Chat.
2. On the Chat settings tab, click the **Response Length** section.

From there, you can select either Concise or Comprehensive.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-81c3126fd962b9949b05b60d2fa854b80ddc38cb%2F02%20Chat%20response%20length_768_456.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Concise is the default Chat Response Length.
{% endhint %}

#### Custom chat behaviors

You can specify how Tabnine AI Chat will behave in certain ways (e.g., “Respond like a mentor with step-by-step instructions and examples” or “Respond in German/Spanish”).

Follow these steps to define your custom chat behavior:

1. Click on the **Settings** (<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea60b94769e5eb824538aa287767025a86c830a4%2Fimage.png?alt=media" alt="" data-size="line">) icon in Tabnine Chat.
2. On the Chat settings tab, click **Set** in the **Define custom behavior** section.

From there, you can determine how Tabnine will act before you prompt the AI Chat.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-3032d313a84ba7ff18f80617bed05bae15a9c29c%2F01%20Custom%20chat%20behaviors%20768_456.gif?alt=media" alt=""><figcaption></figcaption></figure>
