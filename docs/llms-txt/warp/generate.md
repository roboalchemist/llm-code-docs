# Source: https://docs.warp.dev/agents/generate.md

# Generate (Legacy)

## What is Generate?

Generate helps turn natural language queries into precise commands as terminal input or contextual suggestions inside interactive commands and programs, whether you're using psql, gdb, git, mysql, or any other CLI tool.

Generate is backed by Large Language Models from API providers like OpenAI and Anthropic, and are completely opt-in.

{% hint style="info" %}
Currently, you need to be online to use this feature. If this feature doesn't work, your ISP or firewall may be blocking the calls to `app.warp.dev`
{% endhint %}

## Ways to Generate with AI

### Generate commands as command line input

Type `#` on the command line input to generate command suggestions.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-7b0133ba50eb0441f47f6a75516f9779ec294e95%2FScreenshot%202024-06-15%20at%205.05.29%E2%80%AFPM.png?alt=media&#x26;token=a3885336-4e7e-4f40-9c47-0929743c4704" alt=""><figcaption><p>Typing '#' on the command line opens the suggestions interface</p></figcaption></figure>

{% embed url="<https://www.loom.com/share/424a763ef0c8455e8269e541301968f2>" %}
Generating commands as command line input demo
{% endembed %}

1. Press `` CTRL-` `` or type `#` into the text input editor to search using natural language.
2. Type in the input box what you'd like to do. For example, "replace a string in a file."
3. Results are generated in real-time, and you can keep the current prompt or modify the prompt to generate new commands.
4. When you've found the command you want to execute, it can be run or saved as a Workflow onto Warp Drive to easily recall it in the future.

### \[Legacy] Generate text and contextual suggestions in interactive CLIs

{% hint style="warning" %}
**Our legacy Generate feature which works in interactive CLIs has been replaced by** [full-terminal-use](https://docs.warp.dev/agents/full-terminal-use "mention")**, where Warp’s agent can now run and control long-running or full-screen terminal applications**. This includes debuggers, database shells, installers, and system monitors.\
\
The agent can provide input when prompted, navigate interactive screens, and continue execution without stalling.
{% endhint %}

In interactive CLI applications, you can generate input using natural language.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-871566298096cf5d5a414d6447ee934ad9a5f288%2Fgenerate-psql.png?alt=media" alt=""><figcaption><p>Generate a SQL query</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-338c694a332b866a25c1bde9795ac0bb733a0260%2Fgenerate-vim.png?alt=media" alt=""><figcaption><p>Generate Vim input</p></figcaption></figure>

{% tabs %}
{% tab title="macOS" %}

1. Inside a long-running, interactive command, press `CMD-I` when you see the hint text appear.
2. Type what you would like to generate in the input box. For example, "show me all tables in my Postgres database" or in Vim, "generate a recursive Fibonacci function and save it to the file."
3. Results are generated in real time using the [LLM of your choice](#supported-interactive-cli-models).
4. To refine or follow up on your query, press `CMD-Y`. You can then either edit your last message by pressing `UP ↑` or add a follow-up by typing in new text.
5. When you've found the text you want to add or execute, press `Enter` or click the Accept button.
   {% endtab %}

{% tab title="Windows" %}

1. Inside a long-running, interactive command, press `CTRL-SHIFT-I` when you see the hint text appear.
2. Type what you would like to generate in the input box. For example, "show me all tables in my Postgres database" or in Vim, "generate a recursive Fibonacci function and save it to the file."
3. Results are generated in real time using the [LLM of your choice](#supported-interactive-cli-models)
4. To refine or follow up on your query, press `CTRL-SHIFT-Y`. You can then either edit your last message by pressing `UP ↑` or add a follow-up by typing in new text.
5. When you've found the text you want to add or execute, press `Enter` or click the Accept button.
   {% endtab %}

{% tab title="Linux" %}

1. Inside a long-running, interactive command, press `CTRL-SHIFT-I` when you see the hint text appear.
2. Type what you would like to generate in the input box. For example, "show me all tables in my Postgres database" or in Vim, "generate a recursive Fibonacci function and save it to the file."
3. Results are generated in real time using the [LLM of your choice](#supported-interactive-cli-models)
4. To refine or follow up on your query, press `CTRL-SHIFT-Y`. You can then either edit your last message by pressing `UP ↑` or add a follow-up by typing in new text.
5. When you've found the text you want to add or execute, press `Enter` or click the Accept button.
   {% endtab %}
   {% endtabs %}

A couple of other examples of interactive CLIs where you can invoke Generate:

* **Database REPL** (e.g. `psql`, `mysql`, `sqlite`): Generate SQL queries such as "create a table to store user data" or "show me all the rows in orders for the last month"
* **Text editors** (e.g. `vim`, `nano`): Quickly generate text such as a markdown header, a code block comment, or a boilerplate CSS class.
* **Python REPL** (e.g. `ipython`, `python`): Quickly generate Python snippets such as "create a simple plot of x" or "write a unit test for this function"
* **Debugger tools** (e.g. `gdb`, `lldb`): Get commands for setting breakpoints or inspecting memory
* **Version control** (e.g. `git rebase -i`): Speed up complex git commands by describing your goal such as "interactively rebase master onto feature-branch"
* **Cloud provider shells** (e.g. `gcloud`, `aws cli`): faster setup or resource management such as "create a new Kubernetes cluster" or "provision a new RDS instance"

{% hint style="warning" %}
If you experience any issues with Generate, please visit known issues for [troubleshooting steps](https://docs.warp.dev/support-and-billing/known-issues#online-features-dont-work).
{% endhint %}
