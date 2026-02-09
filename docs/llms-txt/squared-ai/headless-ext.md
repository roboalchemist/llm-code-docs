# Source: https://docs.squared.ai/activation/data-apps/browser-extension/headless-ext.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Headless Extension

The **Headless Extension** is a lightweight Chrome extension package that allows advanced users to run AI models directly on webpages without embedding anything in the page itself. This is ideal for internal use cases where you want automation, harvesting, or insight overlay without platform and closed environments.

This guide walks through the steps to enable, install, and run `.air` model files via the headless mode.

## Enable the Headless Extension

1. Go to **Settings > Organization > Headless** tab.

<img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6b6ce19eae7a1ceee5c688a0ced7779f" alt="title" data-og-width="2880" width="2880" data-og-height="1670" height="1670" data-path="images/headless/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=e669b4573b5a7bdd6895f9dc1ee6b8d2 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=693d5c08ef45e35d9f787069c408363c 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=adce86c6ae4fb8e2e7cd8bba30d60be3 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=3bf90a86ed0994268ac56106085555a8 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=dc4834ed466a877be6fa3a936b18afdb 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=990043435fb93b629dd2b15d006eb95d 2500w" />

2. Toggle **Enable Headless Extension** to ON.

<img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6b6ce19eae7a1ceee5c688a0ced7779f" alt="title" data-og-width="2880" width="2880" data-og-height="1670" height="1670" data-path="images/headless/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=e669b4573b5a7bdd6895f9dc1ee6b8d2 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=693d5c08ef45e35d9f787069c408363c 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=adce86c6ae4fb8e2e7cd8bba30d60be3 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=3bf90a86ed0994268ac56106085555a8 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=dc4834ed466a877be6fa3a936b18afdb 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/headless/1.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=990043435fb93b629dd2b15d006eb95d 2500w" />

## Install the Headless Chrome Extension

> The Headless Extension must be installed in Developer Mode.

### Step 1: Download Extension

* Click the download link to get the `.zip` file.

### Step 2: Unzip and Prepare

* Extract the contents of the `.zip` file to a local folder.

### Step 3: Load as Unpacked Extension

1. Open Chrome and navigate to: `chrome://extensions`
2. Enable **Developer Mode** (top right)
3. Click **Load Unpacked** and select the extracted folder (must include `manifest.json`)

***

## Upload an AIR File

To run a model, you need to upload a valid `.air` file to the extension.

1. Open the extension (puzzle icon → AI Squared)
2. Click the **settings gear** ⚙️
3. Use the **Upload Model Card** view to drag/drop or browse for your `.air` file

***

## Run the Model

Once uploaded:

1. You’ll see your model listed as a **Model Card** (e.g. *Building Damage Detector*)
2. Click **Run** to activate it on the current page
3. The extension will display the results inline or in a results panel

***

Watch the complete demo video for headless extension setup

<video autoPlay muted loop playsInline className="w-full aspect-video rounded-xl" src="https://res.cloudinary.com/da3470iir/video/upload/v1753923660/headless_a4rjez.mov" />

## ✅ You're Done!

Once set up, the extension will:

* Load the `.air` model automatically (if Auto Run is enabled)
* Harvest insights from the active tab based on the model logic
* Show results directly in the browser

You can manage, re-upload, or delete model cards anytime from the extension settings.

***

## File Format

* Supported: `.air` model files
* Make sure `manifest.json` is at the root of the extension folder when loading

***
