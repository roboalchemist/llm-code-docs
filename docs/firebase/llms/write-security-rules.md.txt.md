# Source: https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules.md.txt

<br />

> [!WARNING]
> **Preview:** The prompt described on this page is a **Preview** release. This means that the functionality might change in backward-incompatible ways or have limited support. A preview release is not subject to any SLA or deprecation policy.

This prompt can help your AI assistant (like the
[Gemini CLI](https://github.com/google-gemini/gemini-cli))
generate and refine Firebase Security Rules for your app. You can use the prompt
to draft Security Rules for common use cases, such as granting user-specific
access, implementing role-based permissions, and validating data.

This prompt focuses on generating Security Rules for:

- **Cloud Firestore**: Secure collections and documents based on your app's logic.
- **Cloud Storage for Firebase**: Validate access permissions for your stored files.

Using this prompt can help you get started with a strong security posture, but
you should always test your Security Rules thoroughly before deploying to
production. For more information about testing Security Rules, review
[Get started with Firebase Security Rules: Test your Security Rules](https://firebase.google.com/docs/rules/get-started#test_your_rules).

> [!WARNING]
> **Important:**
>
>
> Your Firebase Security Rules are not automatically updated. The Firebase extension for
> Gemini CLI described in this guide runs one time to create your
> Security Rules based on your project's current state. It does not
> continuously monitor your app or file system. It won't automatically update
> your Security Rules as you develop new features.
>
>
> You must manually update your Security Rules every time you:
>
> - Add a new database collection or path
> - Change your data's structure or schema
> - Change your file storage structure
>
>
> **To update your Security Rules, you must either re-run the prompt to
> rebuild your Security Rules or edit them manually.**
>
>
> If you add new features without updating your Security Rules, you risk
> creating:
>
> - **Security gaps**: Your new data may be left unsecured and publicly readable/writable.
> - **Broken features**: Your app may be blocked from accessing the new data, causing it to fail.

## Prerequisites

- Familiarize yourself with [Firebase Security Rules best practices](https://firebase.google.com/docs/rules/insecure-rules).
- To run unit tests for Firebase Security Rules and use the Firebase Local Emulator Suite, [install Node.js](https://nodejs.org/en/download/) and the [Firebase CLI](https://firebase.google.com/docs/cli#install_the_cli). For full instructions, refer to [Install, configure, and integrate Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure).
- *Recommended:* If you haven't already, [install Gemini CLI](https://github.com/google-gemini/gemini-cli). The following instructions explain how to install and use the Firebase extension for Gemini CLI to generate Security Rules. If you prefer to use another AI assistant, you can copy and paste the prompt for [Cloud Firestore](https://github.com/firebase/firebase-tools/tree/master/src/mcp/prompts/firestore) or [Cloud Storage for Firebase](https://github.com/firebase/firebase-tools/tree/master/src/mcp/prompts/storage) from the `firebase-tools` repository into your chosen AI assistant.
- The Firebase extension for Gemini CLI connects to the Firebase MCP server to access prompts that generate and validate Firebase Security Rules, and help with testing and deployment of Security Rules. [Install the Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server) before using the extension to generate Firebase Security Rules.

## Limitations

We are actively improving this experience, so this list of limitations may
change. Check back often for updates.

- The prompt is designed to generate Firebase Security Rules for Cloud Firestore and
  Cloud Storage for Firebase. It's not yet capable of generating
  Security Rules for Firebase Realtime Database.

- Firebase Security Rules are not called when accessing your database or bucket from a server
  or other backend environment, such as when using the Firebase Admin SDK. If
  you're using the Admin SDK, you're responsible for managing authorization
  and data validation in your backend code.

- [Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase) within the
  Firebase console is unable to generate Firebase Security Rules, even when using this
  prompt. Instead, use an alternate AI assistant that has access to your
  codebase, such as Gemini CLI (which is described on this page).

## Use the prompt

> [!NOTE]
> **Note:** The instructions in this section describe how to use this prompt through the Firebase extension for Gemini CLI. If you'd rather use a different AI assistant, or if you want to review the full prompt behind this extension, you can view the prompt for [Cloud Firestore](https://github.com/firebase/firebase-tools/tree/master/src/mcp/prompts/firestore) or [Cloud Storage for Firebase](https://github.com/firebase/firebase-tools/tree/master/src/mcp/prompts/storage) in the `firebase-tools` repository.

This prompt is available through the Security Rules capability within the
[Firebase extension for Gemini CLI](https://github.com/gemini-cli-extensions/firebase)
to generate your Security Rules and tests. This extension analyzes your source
code to help identify data schemas and access patterns for Cloud Firestore and
Cloud Storage. It's designed to draft Security Rules based on the principle of
least privilege and attempts to uncover vulnerabilities through iterative
"attack" simulations. To assist with final verification, it provides a starting
unit test suite using `@firebase/rules-unit-testing`, allowing you to verify
your security logic locally using the Firebase Local Emulator Suite.

Using this extension requires three steps which are described in this section:

1. [Generate your Security Rules and tests](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules#generate-rules).

2. [Review Security Rules validation and test results](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules#review-rules).

3. [Deploy Security Rules to your Firebase project](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules#deploy-rules).

> [!WARNING]
> **Important:**
>
> Keep the following in mind when using generative AI with your app:
>
> - Generative AI can make mistakes. Always check its changes or output before deploying to production.
> - Frequently commit snapshots of your code, especially before making major changes to your app.
> - Use this AI-assisted approach at your own risk. Google and Firebase are not liable for any security vulnerabilities in AI-generated Security Rules. It's your responsibility to review and test the generated Security Rules before deploying them to production.

> [!NOTE]
> **Note:** This extension is in **preview** . We welcome feedback and contributions! If you have suggestions or improvements, [submit an issue or pull request](https://github.com/gemini-cli-extensions/firebase) in the GitHub repository.

### **Step 1** : Generate Security Rules and tests

Install and run the extension:

1. Install the Firebase extension for Gemini CLI:

       gemini extensions install https://github.com/gemini-cli-extensions/firebase

2. Start Gemini CLI:

       gemini

   > [!NOTE]
   > **Note:** Before generating Security Rules, make sure that you're connected to the [Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server).

3. From the root of your project, run the extension to generate Security Rules
   for either Cloud Firestore or Cloud Storage:

   - **Generate Security Rules for Cloud Firestore:**

         /firestore:generate_security_rules

     In the parent directory, the extension creates a `firestore.rules` file
     and a new `security_rules_test_firestore` directory that contains a
     Node.js project with unit tests for the generated Security Rules.
   - **Generate Security Rules for Cloud Storage for Firebase:**

         /storage:generate_security_rules

     In the parent directory, the extension creates a `storage.rules` file and
     a new `security_rules_test_storage` directory that contains a Node.js
     project with unit tests for the generated Security Rules.

### **Step 2** : Review Security Rules validation and test results

1. Make sure the following are done by your AI assistant. You should get a
   generated summary after the extension runs.

   - **Syntax validation** : After generating Security Rules, Gemini CLI
     automatically validates syntax using the
     `firebase_validate_security_rules` command from the Firebase MCP server.

   - **Unit tests** : After validating syntax, Gemini CLI attempts to run
     the generated unit tests using the Firebase Local Emulator Suite.

2. If tests don't run automatically,
   [start the Firebase Local Emulator Suite in a separate terminal](https://firebase.google.com/docs/emulator-suite/install_and_configure),
   then use one of the following options to run the tests:

   - Option 1: Instruct Gemini CLI to run tests:

         Firebase Emulator Suite is running in a separate terminal. Please execute the tests.

   - Option 2: Run tests manually by following the instructions in the
     `README.md` file in the `rules_test` or `storage_rules_test` directory.

### **Step 3** : Deploy Security Rules to your Firebase project

When you're satisfied with the result of your generated Security Rules, use
the following Firebase CLI commands to deploy the Security Rules to your
Firebase project:

- **Cloud Firestore**

      firebase deploy --only firestore:rules

- **Cloud Storage for Firebase**

      firebase deploy --only storage

## Additional resources

- For additional help with your security posture, you can also use the [security extension for Gemini CLI](https://github.com/gemini-cli-extensions/security), an open-source extension that analyzes code changes to identify security risks and vulnerabilities.