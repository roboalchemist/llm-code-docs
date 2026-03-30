# Source: https://momentic.ai/docs/mobile-cli/setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setup

> This guide will walk you through building your first mobile test locally and integrating into CI/CD

## Prerequisites

<Info>
  If you already have these installed, skip to the verification steps below.
</Info>

The Momentic CLI requires the following tools:

* Node.js: version 20.19.0 or later
* Java JDK: version 24 recommended
* Android Studio: latest stable version, including platform tools.
  * `ANDROID_HOME` must be set in your shell to your SDK install folder.

### Install Node.js

Download [Node.js 20.19.0 or later](https://nodejs.org/en/download). To verify
your installation:

```bash  theme={null}
node -v  # v20.19.0 or later
```

### Install Java

Download [JDK version 24](https://www.oracle.com/java/technologies/downloads/)
from Oracle.

To verify your installation:

```bash  theme={null}
java --version  # should show JDK 24
```

<Info>
  If `java --version` is not found, re-open your terminal or ensure
  `JAVA_HOME/bin` is in your PATH.
</Info>

### Install Android Studio (+ SDK + Platform Tools)

Download [Android Studio](https://developer.android.com/studio) and complete the
first-run setup wizard. If prompted, ensure you include the following tools:

* Android SDK Platform-Tools (ADB)
* Android Emulator

### Set ANDROID\_HOME

Set the `ANDROID_HOME` environment variable in your shell. This should point to
the root of your Android SDK installation.

Typical installation locations are listed below:

* macOS: `/Users/<username>/Library/Android/sdk`
* Windows: `C:\\Users\\<username>\\AppData\\Local\\Android\\Sdk`
* Linux: `/home/<username>/Android/Sdk`

<Tabs>
  <Tab title="macOS (zsh)">
    ```bash  theme={null}
    echo 'export ANDROID_HOME="$HOME/Library/Android/sdk"' >> ~/.zshrc
    echo 'export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
  </Tab>

  <Tab title="Linux (bash/zsh)">
    Adjust the path if your SDK is elsewhere:

    ```bash  theme={null}
    echo 'export ANDROID_HOME="$HOME/Android/Sdk"' >> ~/.bashrc
    echo 'export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```
  </Tab>

  <Tab title="Windows">
    Follow the official guidance to set `ANDROID_HOME`:
    [https://developer.android.com/tools/variables](https://developer.android.com/tools/variables)
  </Tab>
</Tabs>

### Verify your setup

Run the following commands; all should succeed without errors:

```bash  theme={null}
node -v                # expect v20.19.0 or later
java --version         # expect JDK 24
echo $ANDROID_HOME     # prints your SDK path
```

If any check fails:

* Re-open your terminal or source your profile after editing it.
* Ensure Platform-Tools are installed via Android Studio’s SDK Manager.
* Confirm `ANDROID_HOME` matches your actual SDK path.
* On Windows, ensure environment variables are set in System Properties and
  restart your shell.

## Installation

### Get your API key

To get started, log in to
[Momentic Cloud](https://app.momentic.ai/settings/api-keys) and generate an API
key.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

You can export the API key in your shell configuration file (usually `.bashrc`
or `.zshrc`) like so:

```bash  theme={null}
export MOMENTIC_API_KEY=your-api-key
```

### Install the CLI

Before proceeding, ensure a `package.json` file already exists in your project.
If you don’t, run `npm init`, `yarn init`, or `pnpm init` to create the file
beforehand.

Install the [momentic-mobile](https://www.npmjs.com/package/momentic-mobile) CLI
by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npm install momentic-mobile --save-dev
  ```

  ```bash yarn theme={null}
  yarn add momentic-mobile --dev --ignore-workspace-root-check
  ```

  ```bash pnpm theme={null}
  pnpm add momentic-mobile --save-dev --ignore-workspace-root-check
  ```
</CodeGroup>

## Start building locally

### Install Chromium

To automate webviews, Momentic uses a headless browser. You can install it using
the following command:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-browsers chromium
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-browsers chromium
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-browsers chromium
  ```
</CodeGroup>

### Enable Android WebView debugging in your app

If your app renders content inside an Android `WebView`, enable WebView
debugging so Momentic can attach and interact with elements inside the webview.

Add the following in your app startup code before the relevant `WebView` is
used:

```java  theme={null}
WebView.setWebContentsDebuggingEnabled(true);
```

<Warning>
  If this is not enabled, Momentic cannot attach to the WebView. Interactions
  against elements inside that WebView may fail with `InternalWebAgentError: No
    browser controller is attached to the requested webview.`
</Warning>

### Initialize a new project

<Info>
  If you already have a `momentic.config.yaml` file for browser testing, you can
  skip this step and reuse the same project.
</Info>

Create a new Momentic project by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile init
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile init
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile init
  ```
</CodeGroup>

## Start the local app

Start the local app UI by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile app
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile app
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile app
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).