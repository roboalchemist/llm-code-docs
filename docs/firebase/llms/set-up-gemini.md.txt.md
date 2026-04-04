# Source: https://firebase.google.com/docs/studio/set-up-gemini.md.txt

# Configure Gemini in Firebase within workspaces

<br />

Firebase Studio facilitates your development workflows with the following
AI-assisted code features:

- Suggested code completion as you type.

- AI assistance with chat or through the command line
  interface (CLI), which is workspace-aware and fully-integrated with your
  code. It can generate, translate, and explain code. And, with your review
  and approval, Gemini in Firebase can directly interact with your
  workspace to update files, run terminal commands, interpret command output,
  and determine next steps. Learn more at [Try
  chat with Gemini within Firebase Studio](https://firebase.google.com/docs/studio/try-gemini).

- Inline actions that you can take on selected pieces of code. For
  example, you can ask Gemini to make the selected
  code more readable.

- Inline code assistance.

> [!IMPORTANT]
> **Important:** This guide describes the default Gemini interactive chat. Apps created with the App Prototyping agent default to the Prototyper chat in Code view. To use Gemini interactive chat instead, under **Gemini** , click **+** , then select **New Chat** . To return to Prototyper chat, click history **Recent chats** , and then choose **Prototyper chat** . For information about Prototyper chat, see [Get started with the App Prototyping agent](https://firebase.google.com/docs/studio/get-started-ai).

You can customize how Gemini in Firebase helps you by adjusting its
settings and adding AI rules files:

- [Adjust code completion settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete).
- [Adjust your codebase indexing settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing).
- [Customize instructions for Gemini with an AI rules
  file](https://firebase.google.com/docs/studio/set-up-gemini#custom-instructions).
- [Exclude files from Gemini with `.aiexclude`
  files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files).
- [Bring your own key: Use other Gemini models in chat](https://firebase.google.com/docs/studio/set-up-gemini#byok)
- [Adjust how Gemini suggests or applies code changes](https://firebase.google.com/docs/studio/try-gemini#ai-chat).

**Important:** Gemini can
generate output that seems plausible but is
factually incorrect. It may respond with inaccurate information
that doesn't represent Google's views. Validate all output from
Gemini before you use it and do not use untested
generated code in production. Do not enter personally-identifiable
information (PII) or user data into the chat.

## Use Gemini in Firebase in your workspace

Use Gemini in Firebase to boost your coding productivity through the
[chat panel](https://firebase.google.com/docs/studio/try-gemini#chat),
[terminal](https://firebase.google.com/docs/studio/try-gemini#cli), or
[inline code](https://firebase.google.com/docs/studio/try-gemini#inline-chat) assistance.

> [!NOTE]
> **Note:** If you're using the App Prototyping agent in Prototyper view, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) **Switch to Code** to open Code view.

1. Use either chat or inline code assistance in your
   workspace:

   - To use chat: In your open workspace, click
     spark **Gemini** at
     the bottom of the workspace.

   - To use Gemini CLI: Open the terminal and enter `gemini` for the
     Gemini CLI interface, or use the command `gemini -p` to use
     Gemini CLI in [non-interactive mode](https://firebase.google.com/docs/studio/try-gemini#non-interactive).

   - To use inline code assistance: Start typing your code and press `Tab` to
     accept suggestions.

2. Be aware that the following two options are enabled by default:

   - **Suggestions as you type**, which provides inline code completion.
   - **Codebase indexing**, which provides better customization and more helpful responses.

   To change these selections for your workspace settings in the
   future:
   - To update code completion settings, see [Adjust your code completion settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete).
   - To update code indexing settings, see [Adjust your code indexing settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing).

   You can also exclude specific files and directories from AI indexing. See
   [Exclude files from Gemini with `.aiexclude` files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files).

### Gemini in Firebase shortcuts

To quickly open chat with Gemini: press
`Ctrl+Shift+Space` (or `Cmd+Shift+Space` on MacOS).

To view Gemini commands from the command palette:

1. Open the command palette by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on
   MacOS).

2. Search for **Gemini**.

   A list of Gemini commands appears.

## Adjust your code completion settings


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

## Adjust your codebase indexing settings

You can control whether Gemini indexes your code.
Indexing your code provides more helpful results when using chat or inline
AI assistance.

Be aware that ***codebase indexing is turned on by default***.

> [!TIP]
> **Tip:** You can control which files Gemini in Firebase indexes. Learn more at [Exclude files from Gemini with `.aiexclude`
> files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files).

To toggle code indexing on or off, adjust your codebase indexing settings using
one of the following methods:

- If you use a `settings.json` file, set
  `"IDX.aI.enableCodebaseIndexing"`
  to `true` or `false`.

- To update settings in the Firebase Studio workspace:

  1. Click ![Gear icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-gear.svg)
     **Manage** (located at the bottom left of the workspace), then choose
     Settings, or pres `Ctrl+,` (`Cmd+,` on Mac).

     If you're using the App Prototyping agent in
     Prototyper view, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) **Switch to Code** to open Code view.
  2. Select the **Workspace** tab, then search for the
     **Firebase Studio \> AI \> Enable Inline Completion** setting.

  3. Select **Firebase Studio** \> **AI: Enable Codebase
     Indexing**.

  4. To turn off code indexing, deselect **AI: Enable Codebase Indexing**.
     You must update code indexing settings for each of your workspaces.

> [!TIP]
> **Tip:** To retain this setting across all of your workspaces, configure the setting in the **User** tab. This ensures your settings are applied on every workspace you access with your user account. If sharing your workspace, you'll still need to configure the Workspace setting.

## Customize instructions for Gemini with an AI rules file

You can add context and system prompt information by creating an AI rules
file:

- Gemini CLI *only* uses `GEMINI.md`.
- Gemini in Firebase chat prioritizes `.idx/airules.md` but will use `GEMINI.md` if `.idx/airules.md` doesn't exist.

Gemini in Firebase uses your rules as system instructions and context,
customizing its responses for your use case.

Use the AI rules file to share custom prompts, best practices, and even
important context about your project with Gemini to achieve
goals like:

- Influencing Gemini's persona and specializing its expertise.
- Applying project-wide standards, like coding style, conventions, and technology preferences.
- Reducing the amount of information you need to share explicitly in code or chat by providing essential context about your project.

### Create and test your AI rules file

To create and test your AI rules file:

1. Create a new file at `~/GEMINI.md` (for Gemini CLI) or
   `.idx/airules.md` (for Gemini in Firebase chat) in your
   Firebase Studio workspace. You can use one of
   the following options:

   - From **Explorer** (`Ctrl+Shift+E`), right-click the parent directory and select **New file** . Name the file and press **Enter**.
   - From the terminal, use your preferred text editor to open `GEMINI.md` or `.idx/airules.md`.
2. Add content to the file. You may want to add information about the persona
   Gemini should use (like "You are an expert developer and
   helpful assistant who knows everything about Next.js"), coding and
   conversation standards, and context about the project. See the
   following [Example](https://firebase.google.com/docs/studio/set-up-gemini#example) for
   an example AI rules file.

3. Save the file and open [Gemini CLI](https://firebase.google.com/docs/studio/try-gemini#cli-get-started)
   or [Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini#chat).

4. To start using your AI rules, you can do one of the following:

   - Rebuild the workspace by refreshing the page. After you rebuild, Gemini will use the rules file within chat. Changes to the AI rules file should be reflected immediately.
   - If you don't want to rebuild your workspace, you can ask Gemini to `load GEMINI.md` or `load airules.md`. If you make changes to the file during the current session, you may need to re-prompt Gemini to load the rules file again.
5. Ask questions about your code. Gemini responds using
   the information you included in the rules file as context.

> [!TIP]
> **Tip:** If you've developed rules files for other AI-enabled IDEs, you can copy them directly into your Gemini rules file. While Gemini CLI only uses `GEMINI.md` as its rules file, Gemini in Firebase will use (in order of precedence) `.idx/airules.md`, `GEMINI.md`, `.gemini/styleguide.md`, `AGENTS.md`, or `cursorrules`.

### Example

The following is a basic example of a rules file that you might use for a
casual game developed with Next.js:

    # Persona

    You are an expert developer proficient in both front- and back-end development
    with a deep understanding of Node.js, Next.js, React, and Tailwind CSS. You
    create clear, concise, documented, and readable TypeScript code.

    You are very experienced with Google Cloud and Firebase services and how
    you might integrate them effectively.

    # Coding-specific guidelines

    - Prefer TypeScript and its conventions.
    - Ensure code is accessible (for example, alt tags in HTML).
    - You are an excellent troubleshooter. When analyzing errors, consider them
      thoroughly and in context of the code they affect.
    - Do not add boilerplate or placeholder code. If valid code requires more
      information from the user, ask for it before proceeding.
    - After adding dependencies, run `npm i` to install them.
    - Enforce browser compatibility. Do not use frameworks/code that are not
      supported by the following browsers: Chrome, Safari, Firefox.
    - When creating user documentation (README files, user guides), adhere to the
      Google developer documentation style guide
      (https://developers.google.com/style).

    # Overall guidelines

    - Assume that the user is a junior developer.
    - Always think through problems step-by-step.

    # Project context

    - This product is a web-based strategy game with a marine life theme.
    - Intended audience: casual game players between the ages of 17 and 100.

> [!TIP]
> **Tip:** AI rules contribute to overall context size, so we recommend keeping your AI rules file within a reasonable limit to ensure the best model performance.

## Exclude files from Gemini with `.aiexclude` files

You can control which files in your codebase should be kept hidden from
Gemini by including `.aiexclude` files in your project.
This lets you granularly control the project context you share with
Gemini.

Much like a `.gitignore` file, an `.aiexclude` file tracks files that
shouldn't be shared with Gemini, including the chat
experience as well as AI features that operate in the editor. An `.aiexclude`
file operates on files at or below the directory that contains it.

> [!NOTE]
> **Note:** Files ignored by `.gitignore` files in your repository are automatically excluded, even if they're not listed in an `.aiexclude` file.

Files covered by `.aiexclude` won't be indexed by Gemini when
**Codebase Indexing** is enabled. Additionally, `.aiexclude` will affect inline
assistance for covered files in the following ways:

- **Chat assistance** : Gemini won't be able to answer questions or offer suggestions about files covered by `.aiexclude`.
- **Code completion**: Suggested code completions will not be available when editing covered files.
- **Inline assistance**: You'll be able to generate new code, but not modify existing code when editing covered files.

Other development environments such as [Android
Studio](https://developer.android.com/studio/preview/gemini/aiexclude) may also
honor `.aiexclude` files.

### How to write `.aiexclude` files

An `.aiexclude` file follows the same syntax as a `.gitignore` file, with these
following differences:

- An empty `.aiexclude` file blocks all files in its directory and all sub-directories. This is the same as a file that contains `**/*`.
- `.aiexclude` files don't support negation (prefixing patterns with `!`).

### Examples

Here are some example `.aiexclude` file configurations:

- Block all files named `apikeys.txt` at or below the directory that contains
  the `.aiexclude` file:

      apikeys.txt

- Block all files with the `.key` file extension at or below the directory that
  contains the `.aiexclude` file:

      *.key

- Block only the `apikeys.txt` file at the in the same directory as the
  `.aiexclude`, but not any subdirectories:

      /apikeys.txt

- Block all files in the directory `my/sensitive/dir` and all subdirectories.
  The path should be relative to the directory that contains the `.aiexclude`
  file:

      my/sensitive/dir/

## Bring your own key: Use other Gemini models in chat

> [!WARNING]
> **Experimental:** This feature is experimental.

You can configure the Gemini model that [Gemini in Firebase
chat](https://firebase.google.com/docs/studio/try-gemini) uses. You have a choice of the built-in model,
models configured in the chat window, or any
Gemini model to which you have access.

For a list of all available models, see [Gemini
models](https://ai.google.dev/gemini-api/docs/models).

> [!IMPORTANT]
> **Important:** Firebase Studio AI settings are *User* settings. This means that they will stay configured for you across multiple workstations.

**To configure your key and select a different Gemini model:**

1. In your open workspace, click
   spark **Gemini** at
   the bottom of the workspace (or the **Gemini** tab).

2. From the Gemini in Firebase chat window, click
   ![AI Settings
   icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-gear.svg) **AI
   Settings** . **User Settings** appear.

3. In the **IDX \> AI: Gemini Api Key** field,
   enter your Gemini API key.

   > [!NOTE]
   > **Note:** This field may already be populated if you used the App Prototyping agent and it created a Firebase project and Gemini API key for you.

4. From the **IDX \> AI: Model Provider**
   drop-down, select **Gemini API**.

You can now select any of the pre-configured Gemini models in
chat.

**To configure a Gemini model that isn't in the drop-down:**

1. Identify the Gemini model you want to use in
   chat from the list at
   [Gemini models](https://ai.google.dev/gemini-api/docs/models).
   For example, you'd enter `gemini-3-pro-preview` to
   use the
   [Gemini 3 Pro preview
   model](https://ai.google.dev/gemini-api/docs/models#gemini-3-pro).

2. From the Gemini in Firebase chat window,
   click the model selector, then choose **Custom model ID** . **User
   Settings** opens.

3. Copy the model name you selected into the
   **IDX \> AI: Gemini Model** field.

4. Close the chat window, then re-open it by clicking
   spark **Gemini** at
   the bottom of the workspace to refresh the model list.

## Customize Gemini CLI

- **Settings** : Create a `.gemini/settings.json` file to change the theme, enable or disable the collection of usage statistics, adjust which tools Gemini CLI has access to, configure the checkpointing feature, and much more.
- **Settings** : Review the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md#available-settings-in-settingsjson) for more information on how to adjust the settings.
- **Environment variables** : Gemini CLI automatically loads environment variables from the `.env` file. This is where you should store your `GEMINI_API_KEY` (required), as well as, optionally, include which Gemini model you want to use, your Google Cloud Project ID, and more.
- **Instructions** : To adjust the context Gemini CLI uses when following instructions, create a `GEMINI.md` file. This lets you to give project-specific instructions, coding style guides, or relevant background information to Gemini, making its responses more tailored and accurate to your needs. Note that creating this file will provide the same instructions to Gemini in Firebase, unless you create a `.idx/airules.md` file as well (in which case Gemini CLI would use `GEMINI.md` and Gemini in Firebase would use `airules.md`).

Review the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md)
for more information on how to adjust the settings, environment variables, and
instructions.

## Next steps

- [Try Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini).