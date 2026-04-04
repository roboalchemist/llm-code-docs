# Source: https://docs.luciq.ai/getting-started/luciq-ai-integration.md

# Integrate Luciq SDK Using AI Coding Agents

### Introduction

We now offer customers the ability to instrument the Luciq SDK using their favorite AI coding agents like Cursor or Claude. This is done through a guided, agent-driven workflow that fetches & integrates the latest Luciq SDK end-to-end, then wires mandatory & optional configurations to your application — all while asking for confirmation before altering your code.

### How It Works?

The workflow consists of `.md` instruction files for each platform, they can be found at:

* [Android AI Integration Guide](https://app.gitbook.com/s/zyyZGn3dXyNyX4fbdQmV/set-up-luciq-for-android/integrate-luciq-on-android/luciq-ai-android-guide)
* [iOS AI Integration Guide](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/integrate-luciq-on-ios/luciq-ai-ios-guide)

These `.md` files can then be used to prompt the coding agent to explicitly follow them, for example, tell your agent something like:

integrate luciq ios sdk following the instructions at \[link to ios guide]

{% hint style="warning" %}
Although the more recommended and less hallucination-prone approach is to copy the `.md` contents of the two guides linked above into your agent conversation directly for it to follow.
{% endhint %}

Then ride the flow, answer the decision prompts, and verify your integration at the end.

### What It Does?

{% stepper %}
{% step %}

#### Core workflow

* Finds your app token
  * Reads from Luciq MCP when available, or
  * Prompts you to paste the token (with guidance on where to find it in the dashboard).
* Detects how your app is built
  * iOS: detects SPM / CocoaPods / Carthage / manual.
  * Android: detects Gradle.
  * If multiple/none, it asks you which one to use.
* Pins and installs the SDK
  * Fetches the latest released version from GitHub Releases.
  * Adds the Luciq dependency using that exact version.
* Initializes the SDK with your preferred invocation
  * Lets you choose from: shake, screenshot, floatingButton, or manual only.
  * Defaults to shake + screenshot if no selection is made.
    {% endstep %}

{% step %}

#### Optional flow (user prompted)

* Initializes the SDK with your preferred invocation
  * Lets you choose from: shake, screenshot, floatingButton, or manual only.
  * Defaults to shake + screenshot if no selection is made.
* Network logging & redaction
  * Turn automatic capture on/off.
  * Configure masking rules for headers (e.g. Authorization, Cookies) and body fields (e.g. password, token).
  * Installs the right interceptor/handler so those fields are redacted.
* Screenshot masking for ReproSteps
  * Configure which UI elements to blur in screenshots:
    * Text inputs
    * Labels/buttons
    * Images/media
    * Or a combination of the above.
* User identification
  * Helps the agent find login and logout flows.
  * Adds identifyUser(id, email, name) for these events so reports are tied back to your users.
* Wrap-up & validation
  * Runs the appropriate build command.
  * Prints a config summary and prompts you to:
    * Trigger Luciq in the app (shake/screenshot/floating button).
    * Submit a test report.
    * Verify it in the Luciq dashboard.
      {% endstep %}
      {% endstepper %}

Example on optional feature prompting:

![](https://content.gitbook.com/content/Cha1KrkvNKPdcC0aGvuB/blobs/yJQBTPNG2kQ5C0Z2Tfk6/d098f0355907644453fd1c0a1fd2fb0cad5dd20fc183af09cbb9f69f7ee1fa9b%20image.png)

### Prerequisites

* You have a Luciq project & app token.
* You’re using a supported package manager:
  * Android: Gradle
  * iOS: SPM, CocoaPods, Carthage, or XCFramework manual integration
* (Optional but recommended): [Luciq MCP Server](https://docs.luciq.ai/getting-started/broken-reference) installed & configured — also helps the agent auto-discover app tokens.
* You’re running an AI coding agent that can read project files and .md instructions (e.g. Cursor, Claude Code).
