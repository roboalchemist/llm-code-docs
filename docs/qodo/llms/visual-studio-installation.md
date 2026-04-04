# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/getting-started/setup-and-installation/visual-studio-installation.md

# Visual Studio Installation

## Install Qodo

### Requirements & Limitations

* **Windows only**: Qodo IDE Plugin for Visual Studio **requires a Windows machine**.
* Some advanced features available in other IDEs [are not yet supported in Visual Studio](#current-capabilities).

### Installation

Qodo IDE Plugin is available as a Visual Studio extension.

To install it:

1. Open Visual Studio on your Windows machine.
2. Go to the top menu and select **Extensions > Manage Extensions**.
3. In the **Online** tab, search for **Qodo**.
4. Click **Download**. The extension will be installed after you restart Visual Studio.

Alternatively, you can install directly from the Visual Studio Marketplace by searching for **Qodo**  and clicking **Install**.

***

### Activation

After installation:

1. Restart Visual Studio.
2. The **Qodo** icon will appear in the **Solution Explorer sidebar**.
3. Click the icon to open the Qodo panel and start working with the agent.

***

### Current Capabilities

Qodo IDE Plugin for Visual Studio is currently available in a limited feature set compared to JetBrains IDEs.

* [**Agent support**](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/what-is-an-agent) (with access to [file system and terminal](https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/built-in-tools-mcps)).
* [**Local RAG and Remote RAG** support](https://docs.qodo.ai/qodo-documentation/qodo-gen/code-intelligence/context-engine).
* **Basic chat**: [only `/test` command](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows/available-workflows) and [free-text chat](https://docs.qodo.ai/qodo-documentation/qodo-gen/chat) are available.

> Other capabilities will be added in future releases.
