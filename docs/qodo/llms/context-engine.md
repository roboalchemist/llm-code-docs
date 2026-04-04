# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/code-intelligence/context-engine.md

# Context Engine

{% hint style="info" %}
This feature is available for **Enterprise users** only.
{% endhint %}

## What is Qodo's Context Engine?

Qodo Context Engine is the code intelligence engine behind the Qodo platform. It connects to all your repos, analyzes architecture and patterns, and powers AI agents that help you search, understand, and solve technical problems.

Think of it as an AI-powered Principal Engineer, that understands your entire system and helps you move faster with confidence.

### Why should I use it?

When used inside Qodo IDE Plugin, Qodo Context Engine brings deep, architecture-level understanding directly into your IDE.

You ask the questions, and Qodo Context Engine finds the answers from across your entire codebase.

### How does it work?

Qodo Context Engine uses Retrieval-Augmented Generation (RAG) and agentic reasoning to understand your codebase:

* **Indexing** – Builds a deep internal map of your code
* **Retrieval** – Pulls relevant code, docs, and patterns
* **Reasoning** – AI agents analyze dependencies and logic
* **Generation** – Produces grounded, accurate responses

***

## What can Qodo Context Engine do?

Qodo Context Engine uses two types of AI agents to answer your questions. You can switch between the agents, depending on the complexity of the task.

You can **switch agents** by clicking the **Qodo Context Engine** button above the chatbox.

### Ask Agent

* Best for quick, targeted codebase Q\&A.
* Use it to understand functions, trace logic, or ask how a specific component works.

**Example:**\
`"Where is this middleware used in the login flow?"`

### Deep Research Agent

* Ideal for complex planning, refactoring, and architecture questions.
* Performs multi-step reasoning across services and layers of your system.

**Example:**\
`"What are all the components affected if we refactor how session tokens are handled?"`

***

## Using Qodo Context Engine

### Tag Your Codebase

To enable Qodo Context Engine, you first need to **tag the repositories** you want it to understand. This gives the AI the context it needs to generate accurate, grounded responses.

You can tag one repository or your entire codebase.

#### **1. Tag your repositories**

Option 1: **Quick Tag via Chat**

* Type `@` in the chatbox.
* From the menu, select **Company's Codebase.**

Option 2: **Use the @ Button**

* Click the **@** button above the chatbox.
* From the menu, select **Company's Codebase**.

Search and select the repositories you want to include in Qodo Context Engine.

Once tagged, Qodo Context Engine is automatically activated for those repositories, meaning it acquires deep understanding about them and is able to answer complex questions.

***

### What Happens After Tagging?

Once you've tagged your repositories:

* Qodo Context Engine indexes and maps the selected codebases.
* It understands how components relate across files, services, and versions.
* It uses that deep understanding to answer your questions and suggest change, just like an experienced engineer who knows your code inside and out.

***

### Tips for Getting the Most Out of Qodo Context Engine

* **Be specific** in your prompts when working on complex systems. It’ll trace the logic or dependencies for you.
* **Try Deep Research Agent** when planning a refactor, migration, or major feature change.

***

## Example Usage

<table data-header-hidden><thead><tr><th width="248.515625">Use Case</th><th width="284.23046875">Description</th><th width="220.16015625">Prompt Example</th></tr></thead><tbody><tr><td><p>New hires</p><p>New domain</p><p>New projects</p><p>Working with unfamiliar coding language</p></td><td><ul><li>Quickly learn code behaviors</li><li>Get overview of functions or files</li><li>Map coding patterns across the codebase</li></ul></td><td><strong>"How does acme handle API errors and retries?"</strong></td></tr><tr><td>Cross-Repo Feature Planning</td><td>Plan features spanning multiple repositories by understanding dependencies and integration points.</td><td><strong>"Plan rate limiting for login flow across all our repos"</strong></td></tr><tr><td>Reducing Duplicated Code</td><td>Search within organization codebase for semantic similarities to reduce code duplication</td><td><strong>“Where do we already use a function like this?”</strong></td></tr><tr><td>Coding patterns</td><td>Suggest code that follows patterns and standards</td><td><p></p><p><strong>"Show me an example of how pagination is implemented in the user-service."</strong></p></td></tr><tr><td>Detecting dependencies and breaking changes</td><td>Search within organization codebase for components that may break from the changes</td><td><strong>“Review diff with remote codebase and identify components that are affected or may break”</strong></td></tr></tbody></table>
