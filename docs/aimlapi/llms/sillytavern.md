# Source: https://docs.aimlapi.com/integrations/sillytavern.md

# SillyTavern

## About

[SillyTavern](https://github.com/SillyTavern/SillyTavern) is a locally installed user interface that allows you to interact with text generation LLMs, image generation engines, and TTS voice models. Integration with the AI/ML API currently applies only to LLMs.

***

## Installing SillyTavern (Fresh Setup)

{% hint style="info" %}
Adapted from the official SillyTavern [README / Installation](https://github.com/SillyTavern/SillyTavern?tab=readme-ov-file#-installation)
{% endhint %}

### Windows (Recommended: SillyTavern Launcher)

{% hint style="warning" %}
**Warning:**

* Do **not** install into any Windows‑controlled folder (Program Files, System32, etc.).
* Do **not** run `Start.bat` with administrator permissions.
* Windows 7 is **not** supported (requires Node.js 18.16+).
  {% endhint %}

1. Make sure **Node.js** (latest LTS) and **Git** are installed.
2. Open **Run** (`Win + R`) and execute:

   ```bash
   cmd /c winget install -e --id Git.Git
   ```
3. In **File Explorer**, navigate to a non‑system folder (e.g. `C:\SillyTavern`), click the address bar, type `cmd` and press Enter.
4. Clone the release branch and launch SillyTavern:

   {% code overflow="wrap" %}

   ```bash
   git clone https://github.com/SillyTavern/SillyTavern -b release
   cd SillyTavern
   start Start.bat
   ```

   {% endcode %}
5. After the installer finishes, a browser window will open with the SillyTavern interface.

***

### Linux / macOS

1. Install **Git** and **Node.js** (via your distro’s package manager or Homebrew).
2. In a terminal, run:

   ```bash
   # Clone the release branch
   git clone https://github.com/SillyTavern/SillyTavern -b release
   cd SillyTavern
   ```
3. Make the startup script executable and run it:

   ```bash
   chmod +x start.sh
   ./start.sh
   ```
4. Open your browser to the URL shown in the console (default: `http://localhost:8000`).

{% hint style="success" %}
For Docker, Termux, GitHub Desktop, and other installation methods, see the full [Installation section](https://github.com/SillyTavern/SillyTavern?tab=readme-ov-file#-installation) in the upstream README.
{% endhint %}

***

## Connecting AI/ML API in SillyTavern

### Step 1. Launch SillyTavern → Set Persona

* On first launch you'll see "Welcome to SillyTavern"
* Enter `AI/ML API` as the **Persona Name** for example
* Click **Save**

> This step is required to unlock the chat UI.

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-1e7464cdb4d4d403ed9f1407d0b09952c3f382cc%2Fsillytavern-step1.png?alt=media" alt=""><figcaption></figcaption></figure></div>

### Step 2. Go to Connection Settings

* Open ⚙ **Settings** tab → **Connection Profile** (Second tab)
* Configure:
  * `API`: Chat Completion
  * `Chat Completion Source`: AI/ML API

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4c87138b9ff3521a4d26883d8738d9859efc3cba%2Fsillytavern-step2.png?alt=media" alt=""><figcaption></figcaption></figure></div>

### Step 3. Enter API Key

1. Copy your API key from [https://aimlapi.com/app/keys](https://aimlapi.com/app/keys?utm_source=sillytavern\&utm_medium=github\&utm_campaign=integration)
2. Paste into the **AI/ML API Key** field.
3. Click 🔑 icon to save — it should show a timestamp.

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-d9b21862d6fa2ec9fea53f18dc543750a3b0ee80%2Fsillytavern-step3.png?alt=media" alt=""><figcaption></figcaption></figure></div>

### Step 4. Choose a model

Click the dropdown next to **AI/ML Model** and pick any model such as:

* `gpt-4o-mini-2024-07-18`
* `claude-3-5-sonnet`
* `gemini-1.5-flash`

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-639d27e3e409da62359b154e0de6a5e11a92872f%2Fsillytavern-step4.png?alt=media" alt=""><figcaption></figcaption></figure></div>

### Step 5. Test Connection

Click **Connect** and then the **Test Message**.

* You should see `API connection successful`.
* 🟢 Status: `Valid`.

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-0284073151449ca486dd3d0dc12dfe95f2eb7709%2Fsillytavern-step5.png?alt=media" alt=""><figcaption></figcaption></figure></div>

### 💬 Step 6. Send a Message

Use the input box below to send a test message:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-27d9b5a5317bfd4c27e50c7fc340080a07e88121%2Fsillytavern-step6.png?alt=media" alt=""><figcaption></figcaption></figure>

If all is set up, you’ll see the assistant reply like this:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a5e1b19c948ba975c9c20cd9ead7c910f03ca41a%2Fsillytavern-step7.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### 🎉 Step 7. Done – You’re All Set!

You’re now connected to AI/ML API and can start chatting with any of 200+ models.

{% hint style="success" %}
Tip: Try Claude 3.5, GPT-4o, Gemini 1.5 or explore more in [Model Playground](https://aimlapi.com/app?utm_source=sillytavern\&utm_medium=github\&utm_campaign=integration)
{% endhint %}

***

## ✅ Config checklist

| Field   | Value                       |
| ------- | --------------------------- |
| API     | Chat Completion             |
| Source  | AI/ML API                   |
| API Key | `********` (saved)          |
| Model   | `gpt-4o-mini-2024-07-18`    |
| Status  | ✅ API connection successful |

***

## 🔗 Internal Links

* [AI/ML API Model Catalog](https://aimlapi.com/models?utm_source=sillytavern\&utm_medium=github\&utm_campaign=integration)
* [Your API Keys Page](https://aimlapi.com/app/keys?utm_source=sillytavern\&utm_medium=github\&utm_campaign=integration)
* [Community & Feedback](https://aimlapi.com/community?utm_source=sillytavern\&utm_medium=github\&utm_campaign=integration)
