# Source: https://firebase.google.com/docs/studio/try-gemini.md.txt

# Try Gemini in Firebase within Firebase Studio

<br />

Gemini in Firebase within Firebase Studio offers AI assistance to
streamline your coding workflow---inline within your code editor, through
the command line interface (CLI), and using chat.
Gemini in Firebase can provide code suggestions, generate code,
explain code concepts, update project files, run terminal commands, and
interpret command output.

Without any setup, you can start using Gemini in Firebase right away:

- [Chat with Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini#chat).
- [Get inline help with Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini#inline).
- [Chat with Gemini using Gemini CLI](https://firebase.google.com/docs/studio/try-gemini#cli).

Be aware that ***inline code completion and codebase indexing are
on by default*** . Learn how to
[adjust their settings](https://firebase.google.com/docs/studio/set-up-gemini).

Gemini in Firebase is available when you're
in Code view. You can use it with apps that you start in
Firebase Studio, apps that you import into Firebase Studio, and apps
built by the App Prototyping agent.

## Chat with Gemini in Firebase

Firebase Studio facilitates your development workflows with AI-assisted
chat.
**Important:** Gemini can
generate output that seems plausible but is
factually incorrect. It may respond with inaccurate information
that doesn't represent Google's views. Validate all output from
Gemini before you use it and do not use untested
generated code in production. Do not enter personally-identifiable
information (PII) or user data into the chat.

### Get started with chat

1. Open or create a workspace in
   [Firebase Studio](http:https://studio.firebase.google.com/).

   > [!NOTE]
   > **Note:** If you're using the App Prototyping agent in Prototyper view, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) **Switch to Code** to open Code view.

2. Click spark**Gemini**
   at the bottom of the workspace.

   > [!NOTE]
   > **Note:** Apps created with the App Prototyping agent default to the Prototyper chat in Code view. To use Gemini interactive chat instead, under **Gemini** , click **+** , then select **New Chat** . To return to Prototyper chat, click history **Recent chats** , and then choose **Prototyper chat**.

3. Start chatting with Gemini.

4. *(Optional)* Send a multimodal prompt to Gemini by clicking
   ![Attach icon](https://firebase.google.com/static/docs/studio/images/icons/attach.svg) **Attach**
   and select one of the following options:

   - **Drawing:** Use the drawing tools to design your intended design, then type your prompt and click **Send**.
   - **Image:** Upload an image, add your prompt, then click **Send**.
   - **File:** Select a file from your workspace to use as context, add your prompt, then click **Send**.

   > [!TIP]
   > **Tip:** To add a file from your local computer to your workspace, right-click on the folder you want to upload to in Explorer, then click **Upload...**

5. *(Optional)* Change the mode Gemini uses to respond to requests:

   - **Ask:** Create a plan. In this mode, Gemini answers questions without proposing code changes.
   - **Agent:** Make changes to your app. In this mode, Gemini proposes changes to your app, but doesn't apply them without your confirmation.
   - **Agent (Auto-run):** Auto-apply changes to your app. In this mode, Gemini automatically makes changes to your code based on your requests, but will still ask for confirmation to run terminal commands.
6. *(Optional)* Add your own Gemini API key and choose a different
   Gemini model. Learn more at [Bring your own key: Use other
   Gemini models in chat](https://firebase.google.com/docs/studio/set-up-gemini#byok).

7. *(Optional)* Customize how Gemini in Firebase helps you by adjusting
   its settings and adding AI rules files.
   [Learn more](https://firebase.google.com/docs/studio/set-up-gemini).

In the chat panel, you can ask
Gemini questions and get code suggestions. In Agent mode,
Gemini can even update your project configuration files and
code and can run terminal commands for you, directly within your workspace.
Gemini might ask if it can do any of the following for you:

- **Modify files:** Gemini can add a feature, fix a bug, or
  refactor code. When Gemini proposes changes to a file,
  you'll see two options:

  - **Update File:** Directly update the file with Gemini's proposed changes.
  - **Review Changes:** Open the proposed changes in another window for review before applying them.

  > [!NOTE]
  > **Note:** If you prefer, Gemini in Firebase can auto-apply proposed changes. In the chat window, use the mode drop-down to select **Agent (Auto-run)** mode.

- **Run terminal commands:** Gemini can run commands like
  installing dependencies or starting a development server. It might propose
  these commands itself, or you can ask Gemini to run them.
  After Gemini proposes a command, the **Run Terminal
  Command** button appears. Click it to execute the command in a terminal
  within Firebase Studio. Gemini will run the command
  and interpret the results for you in the chat window, and will help
  determine next steps.

  > [!NOTE]
  > **Note:** For long-running commands (for example, running a server with `npm run dev`), a **Detach** button appears. Click **Detach** to allow the command to continue running in the terminal while regaining access to chat.

### Complete complex tasks with chat

Gemini in Firebase can help you complete complex development
tasks, like:

- **Documenting your code:** Gemini can automatically generate documentation in the appropriate format for your code when you ask it to "Write my docs."
- **Writing test cases:** Gemini can automatically update and generate unit tests. If you ask Gemini to "write my tests," Gemini finds an existing unit test file and can add missing tests to the file. If it doesn't find existing unit test files, it creates the unit test for you to review, iterate on, and accept---you can even ask Gemini to run it!
- **Managing dependencies:** You can ask Gemini to detect missing dependencies in your code and resolve them directly from the chat interface.
- **Refactoring code:** You can ask Gemini to refactor code on your behalf, for example, extracting a function, or renaming a variable across multiple files. Gemini will generate a list of proposed changes and, after reviewing and applying changes, you can ask Gemini to update and execute unit tests to verify the refactor and ensure tests continue to pass.
- **Generating and running Docker workflows:** If you've [enabled Docker in
  your workspace](https://firebase.google.com/docs/studio/customize-workspace#common-services), you can quickly containerize your application by asking Gemini to create a Dockerfile (for example, "Create a Dockerfile for my app"). After Gemini generates the Dockerfile, it can build and run the container for you.
- **Run unit and integration tests:** You can initiate test execution by asking Gemini to run specific test suites (for example, "Run my unit tests" or "Run integration tests"). Gemini will execute the appropriate command for your project (for example, `npm test` or a specific test runner command) and will display the test results within the chat interface.

### Use slash commands in chat

You can guide the output Gemini in Firebase chat provides by using
slash commands, shortcuts prefaced with a forward slash (`/`). Enter `/`
at the beginning of your Gemini chat prompt and select the
action you want from the list of available slash commands.

For a full list of slash commands, type `/` in chat.

For example, `/generate` followed by a short description of what you want
is a prompt shortcut to generate code snippets.

Here's an example of the return for running
`/generate css for a black background`:

    body {
      background-color: black;
    }

    /* This CSS code sets the background color of the <body> element to black. This will make the background of the entire web page black. */

### Refer to specific files and folders in chat

To provide additional context for requests and questions you ask
Gemini in Firebase, you can refer to specific files and folders using
the `@` symbol.

For example, `Explain what's contained within the @src/ai directory.`

### Manage chat history

You can keep different topics separate in your Gemini in Firebase chats
by starting different threads. You can then refer back to earlier threads
based on topic.

> [!TIP]
> **Tip:** Selecting a previous chat thread is especially useful after resetting your workspace or starting a new session: You can quickly start from where you left off in chat.

To start a new chat:

1. Click **New Chat** in the chat header bar.

2. Enter your prompt.

To switch to another chat thread:

1. Click **Recent chats** in the chat header bar.

2. Select the chat thread you want to access.

3. Continue that chat thread or refer back to previous chats with
   Gemini.

To delete a chat thread:

1. Select the chat thread you want to delete from **Recent chats** in
   the chat header bar.

2. Click **Delete chat** in the chat header bar. Confirm that you want
   to delete the chat thread from chat history.

### View code citations in chat

To help you verify the code suggestions, Firebase Studio shares
information about the original source and associated licenses. You can see
a complete log of code citations from the chat
window by clicking the License Log icon in the chat header bar.

![License log icon in the chat header
bar](https://firebase.google.com/static/docs/studio/images/license-log-icon.png)

To learn more about Google code citations, see
[Generative Code
Assistance](https://support.google.com/legal/answer/13505487).

## Get inline help from Gemini in Firebase

Firebase Studio boosts your productivity with AI-assisted code
suggestions from
Gemini.
**Important:** Gemini can
generate output that seems plausible but is
factually incorrect. It may respond with inaccurate information
that doesn't represent Google's views. Validate all output from
Gemini before you use it and do not use untested
generated code in production. Do not enter personally-identifiable
information (PII) or user data into the chat.

Be aware that ***code completion is turned on by default*** . Learn how to
[adjust its settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete).

### Get code suggestions from Gemini in Firebase

Gemini generates complete blocks of possible code
inline. To use the
Gemini inline code assistance, follow these steps:

1. Open a workspace in
   [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

2. Go to the file or line of code you want help with and press
   `Ctrl+I` (`Cmd+I` on MacOS).

3. Enter a description of what you want and Gemini
   generates a suggestion. You can also use [actions as
   shortcuts](https://firebase.google.com/docs/studio/ai-chat#slash-commands) to guide the suggestions.
   For example, enter `/fixError` for help fixing errors in inline code.

4. Choose to do any of the following options:

   - To keep the generated code, click **Accept**.
   - To paste the suggestion somewhere else or move it to a new file, select the corresponding option from the drop-down menu on the **Discard** button.
   - To generate a new suggestion, click **Regenerate**.
   - To remove the suggestion completely, click **Discard**.
5. *(Optional)* Customize how Gemini in Firebase helps you by adjusting
   its settings and adding AI rules files.
   [Learn more](https://firebase.google.com/docs/studio/set-up-gemini).

> [!TIP]
> **Tip:** You can also use [chat](https://firebase.google.com/docs/studio/try-gemini#ai-chat) to instruct Gemini in natural language to perform actions directly in your workspace on your behalf, like updating code and running commands.

### View Gemini in Firebase commands inline

1. To view Gemini commands inline for specific code,
   select and right-click the code you want help with.

2. Select spark**Gemini**
   from the menu and then select the action you want to perform.

### Use Gemini-suggested code completion

To help you write code, Firebase Studio provides AI code
completion that predicts and autofills code in any open file as soon as you
begin to type.

Be aware that ***code completion is turned on by default***.

To toggle code completion on or off, adjust your code completion settings using
one of the following methods:

- If you use a `settings.json` file, set
  `"IDX.aI.enableInlineCompletion"` to `true` or `false`.

- To update settings in the Firebase Studio workspace:

  1. Click ![Gear icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-gear.svg)
     **Manage** (located at the bottom left of the workspace), then choose
     Settings, or press `Ctrl+,` (`Cmd+,` on Mac).

     If you're using the App Prototyping agent in
     Prototyper view, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) **Switch to Code** to open Code view.
  2. Select the **Workspace** tab, then search for the
     **Firebase Studio \> AI \> Enable Inline
     Completion** setting.

  3. To turn off code completion, deselect the
     **Enable inline code completion as you type** option.

> [!TIP]
> **Tip:** To retain this setting across all of your workspaces, configure the setting in the **User** tab. This ensures your settings are applied on every workspace you access with your user account. If sharing your workspace, you'll still need to configure the Workspace setting.

## Chat with Gemini using Gemini CLI

Gemini CLI is an open-source AI agent that brings the power of Google's
Gemini models directly into your terminal. Gemini CLI
performs similar tasks to Gemini in Firebase, but you might prefer to
use Gemini CLI if you're a developer who spends a significant amount of time
in the terminal for tasks like code generation, debugging, executing commands,
or managing project files.

### Get started with Gemini CLI

To access Gemini CLI in Firebase Studio:

1. **Swap to Code view** : If you're working in Prototyper mode, ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) **Switch to Code** to open Code view.

2. **Access the terminal** : Open the ![menu icon](https://firebase.google.com/static/docs/studio/images/icons/menu-icon.png)
   menu \> **Terminal** \> **New Terminal**.

3. **Open Gemini CLI**: In the terminal, enter the following command:

       gemini

   > [!NOTE]
   > **Note:** If your Firebase Studio workspace was created before July 9, 2025, Gemini CLI isn't preinstalled. If the `gemini` command isn't found, install Gemini CLI with the command: `npm install -g @google/gemini-cli`

4. **Customize** : Pick a color theme by using the arrow keys on your keyboard,
   then press **Enter**.

5. **Authenticate** : Select an authentication method. To receive a free
   Gemini Code Assist license with an allowance of 60 model requests
   per minute and 1,000 requests per day at no charge, choose
   **Login with Google.** For more information about authentication, review
   [the documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/authentication.md).

In the future, all you need to do is enter `gemini` in the terminal to access
Gemini CLI.

Alternatively, you can run Gemini CLI in non-interactive
mode, which is useful for scripting and automation. In this mode, Gemini CLI
automatically exits after executing the command you enter. To use this mode, use
the `--prompt` or `-p` flag. For example:

    gemini -p "Create a markdown file that explains my app's architecture"

### Use commands with Gemini CLI

You can chat with Gemini CLI to issue questions or requests. You could ask
it:

- **`explain [file_name.js]`** : If you encounter unfamiliar code, use this command to request an explanation. Simply replace `[file_name.js]` with the relevant path or paste the code directly into the prompt.
- **`refactor [code_snippet]`** : Enhance your code's structure or efficiency by prompting Gemini to suggest refactoring improvements.
- **`debug "Error: Module not found: 'firebase-admin'"`** : When you encounter errors, give the error message to Gemini for insights and potential solutions.
- **`summarize "Key features of Firebase Realtime Database"`** : Gemini can provide rapid research and concise content summarization.

It also supports several built-in commands to help you manage your session,
customize the interface, and control its behavior, such as:

- **`/help`**: Enter this command to view a comprehensive list of available commands and options, serving as an excellent starting point for exploration.
- **`/chat`**: Save and resume conversation history in order to create branching conversations or resume a previous state from a later session.
- **`/tools`** : Display a list of tools that are available within Gemini CLI.
- **`/restore`**: Restores the project files to the state they were in just before a tool was executed. This is particularly useful for undoing file edits made by a tool.

Review the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md)
for a full list of commands.