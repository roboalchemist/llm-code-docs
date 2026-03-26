# Source: https://docs.tabnine.com/main/getting-started/tabnine-agent/how-to-use-tabnine-agent.md

# How to Use Tabnine Agent

### **Quick Start Guide**

When you open Tabnine in your IDE, look up to the top of the app and select <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-834a667f9b7e818024bd6df966912c00e085f0c9%2Ficon%3Dmagic%20wands%402x.png?alt=media" alt="" data-size="line">**Agent**.

Then, before you type into the prompt box at the bottom, select which model you want from the dropdown menu beneath the top menu.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-04f32762eafa8ef79818c6c3a4f09aa66ff0ef9b%2FAgent%20Model%20dropdown.gif?alt=media" alt=""><figcaption></figcaption></figure>

Before you prompt, make sure to have a project folder open in your IDE. This is so that Agent has a place to save new project files. Without it, Agent won't work properly.

#### Prompt

Scroll down to the prompt box and **describe** your goal in plain language. Agent's strength is evaluating your end goal and describing what it will to do get you there.

It is a *best practice* to ask Agent to review its plan with your ***before*** jumping into code generation. This will let you understand exactly what Agent plans to do and precisely how it plans to structure your project.

In this example, we ask Agent to plan out a simple translation application. We are explicit though to let us review the plan before coding begins.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e57bc8abaf55a26f89c6725242d384a85471e355%2FAgent%20Plan.gif?alt=media" alt=""><figcaption></figcaption></figure>

You’ll initially be met by a brief “Working…” message below the red Tabnine logo, followed by a description of what Agent intends to do with its response:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f6d54f678687447ca558ed11828974968ef011f0%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Confirm

You can see its description of the plan is thorough. It lays out its reasons for each file, shows what the project directory will look like, then asks if we would like it to continue.

Once you confirm via the prompt box, Agent will generate the files.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e57bc8abaf55a26f89c6725242d384a85471e355%2FAgent%20Plan.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Approve

It will then ask you for confirmation to <mark style="background-color:blue;">**Run**</mark> or <mark style="color:blue;">**Reject**</mark> the file generation for each file (unless you change this to automatic in the Settings).

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-46cd570f1671a08f371305164cc78ff0d1e0e143%2FCreate%20all%20files.gif?alt=media" alt=""><figcaption></figcaption></figure>

When it generates the code for a file, you can create that file by hitting the **Apply** button.

To approve changes to a new version of an existing file, select the circled, green checkmark <mark style="color:green;">✓⃝</mark> above the document window (or reject by hitting the red x mark <mark style="color:red;">ⓧ</mark>).

{% hint style="success" %}
This option will only appear if
{% endhint %}

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-63d95ae429eec498a83eba9522f6df6cccaa5df9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
*Do I have to approve “changes” to the file if it’s a new file (i.e., click the green checkmark)?*

No. On the initial creation, you can do without clicking it because there are no additional changes — the file now exists. For edits, absolutely. Once you click the checkmark, it will automatically close both the original file and the window comparing the original file code (in <mark style="color:red;">red</mark>) to highlighted changes (in <mark style="color:green;">green</mark>).
{% endhint %}

***

#### Reject

If you select <mark style="color:blue;">Reject</mark> the request for whatever reason, Tabnine Agent will then clarify it is unable to finish the task, then list a number of other options.

In this case, the terminal command was rejected because it identified the wrong folder.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fcaf6322cfd28e0c4830ba020f0aa8cb594ab65f%2FReject%20command.gif?alt=media" alt=""><figcaption></figcaption></figure>

***

Once complete, you can see all the files in your profile folder:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-99a446abcbcc5bec60708bba623649ba0a906173%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Native Tools

Tabnine Agent contains several Native Tools that help it access your project files, create new ones, edit current ones, or search your project context. All of these can be edited in [Settings](https://docs.tabnine.com/main/getting-started/tabnine-agent/agent-settings).

You’ll be met with the following options:

1. Read Project Files
2. Create Project Files
3. Apply Code
4. Read Terminal
5. Run Command
6. List Directory
7. Get Diagnostics
8. Workspace Search

{% hint style="info" %}
You will see indicators for the different Native Tools for most steps of the process. This will help you keep track of Agent’s own workflow. They will appear like this in the conversation with the Agent:

<mark style="color:orange;">•</mark> Exploring and <mark style="color:green;">•</mark> Explored

<mark style="color:orange;">•</mark> Creating and <mark style="color:green;">•</mark> Created

<mark style="color:orange;">•</mark> Reading and <mark style="color:green;">•</mark> Read

<mark style="color:orange;">•</mark> Applying and <mark style="color:green;">•</mark> Applied
{% endhint %}

### Edits

You can directly request changes from Tabnine Agent in the prompt window, specifying what you would like to change and in what way, as seen in this example below:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2635ab6d2bc7898085c96af4afefef40adbdf89c%2FEdit%20Agent.gif?alt=media" alt=""><figcaption></figcaption></figure>

### Predefined Slash Commands

(Introduced in [**5.27.0**](https://docs.tabnine.com/main/administering-tabnine/release-notes#v5.27.0)) When the user inputs “/” at the beginning of a new message (at the beginning or middle of a conversation), it opens a dropdown list of pre-defined slash commands for Tabnine Agent.&#x20;

When the relevant command is selected, it will have the “command” background.

Current predefined commands include the following:<br>

* `/code-review`&#x20;
* `/test`
  * Generates focused test cases and implementations for the relevant code changes (This replaces the current “Test” tab)
* `/describe-pr`

  * Drafts a structured, reviewer-ready pull request description for your changes

  <br>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoPj4tO8WDDiK2xBX5E0F%2Funknown.png?alt=media&#x26;token=2cf5d8ea-f22b-41d6-9a9f-de0bcadaae5d" alt=""><figcaption></figcaption></figure>

<br>
