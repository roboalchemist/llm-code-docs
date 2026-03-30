# Source: https://firebase.google.com/docs/ai-assistance/gcli-extension.md.txt

<br />

Firebase has an integration with the Gemini CLI, which is Google's open-source
coding agent that brings the power of Gemini models directly into your terminal.
You can install the Firebase extension to give the Gemini CLI more
Firebase-specific capabilities and expertise.

If you already have the Gemini CLI installed, you can run this command to
install the Firebase extension:

    gemini extensions install https://github.com/gemini-cli-extensions/firebase/

This guide describes the Firebase extension as well as details for installing
and using the Gemini CLI with the extension.

## Benefits of the extension

![The Firebase extension in action](https://firebase.google.com/static/docs/ai-assistance/images/gemini-cli.gif)

The Firebase extension for Gemini CLI is an easy-to-install package that does
the following:

- Automatically installs and configures the [Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server) for use in your workspace. The Firebase MCP server gives the Gemini CLI several new features:
  - A library of pre-written prompts optimized for developing and running an app with Firebase. You can run these prompts using Gemini CLI slash commands.
  - The ability for the Gemini CLI to use tools to work directly with your Firebase project and perform tasks on your behalf, such as creating databases and deploying apps. See the Firebase MCP server documentation for a complete list of tools.
  - An interface that allows the Gemini CLI to look up Firebase documentation in an LLM-friendly resource format.
- Adds a Firebase-specific context file to your project. This context file, also known as a rules file, provides agentic development tools (like the Gemini CLI) with additional prompts and hints that maximize its ability to help you develop apps with Firebase.

## Install the Firebase extension for Gemini CLI

1. If you haven't already, install the Gemini CLI.

   If you're not sure which authentication option to use, just start the Gemini
   CLI, and it will guide you through signing in with your Google Account. This
   method of authentication is adequate for most users, particularly if you're
   just starting out with the Gemini CLI.
2. Install the Firebase extension by running the following command from a shell
   prompt (not from the Gemini CLI prompt!):

       gemini extensions install https://github.com/gemini-cli-extensions/firebase/

3. Once installed, the extension will be available to all Gemini CLI
   workspaces.

   If needed, you can disable the extension for specific workspaces:

       gemini extensions disable firebase --scope=workspace

### Update the extension

The Firebase extension is updated frequently, so you should regularly update the
installed version:

    gemini extensions update firebase

## Next steps

Once you've installed the extension, the Gemini CLI will automatically make use
of the context, tools, and resources provided by the extension. Combined, these
features greatly improve the Gemini CLI's ability to assist you with developing
and running Firebase apps.

As the next step, try running some of the pre-written prompts the Firebase
extension makes available to you. For example:

- To start a new Firebase app project:

      /firebase:init

  This prompt can help you with various common development goals:
  - [**Set up a backend**](https://firebase.google.com/docs/ai-assistance/prompt-catalog/set-up-backend):
    Helps set up Firestore as your database and Firebase Authentication as a way
    to secure your app and your user's data. It also helps you to deploy your
    app in one go!

  - [**Add AI features**](https://firebase.google.com/docs/ai-assistance/prompt-catalog/add-ai-features):
    Sets up Firebase AI Logic and writes the code to easily and securely access
    the Gemini API directly from your mobile and web apps.

- To deploy an existing web app:

      /firebase:deploy

  This prompt
  [deploys your application to a Firebase hosting service](https://firebase.google.com/docs/ai-assistance/prompt-catalog/deploy-to-hosting)
  regardless of whether it's a static app or a full-stack app. The prompt
  instructs the AI to analyze your code and choose the correct Firebase hosting
  service based on the app's needs. No more decision-making or misconfigured
  services.
- To prioritize and fix issues in your mobile app:

      /crashlytics:connect

  This prompt can help you
  [prioritize and fix issues in your mobile apps](https://firebase.google.com/docs/ai-assistance/prompt-catalog/prioritize-fix-issues)
  that have already integrated Crashlytics.