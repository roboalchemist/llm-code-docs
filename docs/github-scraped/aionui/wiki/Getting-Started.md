# Source: https://github.com/iOfficeAI/AionUi/wiki/Getting-Started

# 🚀 AionUi Quick Start Guide

Welcome to AionUi! This guide will help you install, configure, and start using AionUi in just 5 minutes.

**[English](Getting-Started)** | [简体中文](Getting-Started-Chinese)

## 📥 Step 1: Download and Install

### System Requirements
- **macOS**: macOS 10.14 or higher
- **Windows**: Windows 10 or higher  
- **Linux**: Ubuntu 18.04+ or other mainstream distributions
- **Memory**: At least 4GB RAM
- **Storage**: At least 500MB available space

### Download Methods
1. Visit [AionUi GitHub Releases](https://github.com/iOfficeAI/AionUi/releases)
2. Choose the version suitable for your operating system:
   - **macOS**: Download `.dmg` file (Apple Silicon or Intel)
   - **Windows**: Download `.exe` installer
   - **Linux**: Download `.deb` or `.AppImage` file

### Installation Steps
- **macOS**: Double-click the `.dmg` file and drag AionUi to the Applications folder
- **Windows**: Run the `.exe` installer and follow the prompts
- **Linux**: Install the `.deb` file using package manager, or run the `.AppImage` directly

---

## 🎯 Step 2: First Launch Configuration

### Launch the Application
After installation, launch AionUi. You'll see the welcome interface on first startup:

![Welcome interface screenshot - showing main interface and model selection](assets/Images/hello%20screen.png)

### Choose AI Agent Mode
The default interface you see is Gemini CLI mode, which is AionUi's built-in Agent (used by default after download). AionUi also supports Multi-Agent Mode, including external CLI tools (requires users to install themselves). For detailed information, please refer to the [Multi-Agent Mode Configuration Tutorial](ACP-Setup).

---

## ⚙️ Step 3: Configure Authentication

### Method 1: Google Account Login (Recommended)

1. **Enter Settings**
   - Click the "Settings" icon in the left sidebar

2. **Configure Google Authentication**
   - In the "Gemini Settings" page
       - **Network Proxy Settings** (if needed):
         - If you have a network proxy, recommend setting VPN to US
         - Enter proxy address in proxy settings
       - Click the "Google Login" button
       - Complete Google account login in the popup browser window
       - After successful login, the interface will display your Google account

   **💡 Login Troubleshooting**:
   - **Network Issues**: Ensure VPN is set to US, enter proxy address
   - **Project ID Issues**: Need to create Google Cloud Project, see detailed tutorial below

![Google login configuration screenshot - showing login button and account info](assets/Images/login%20setting.png)

### 📋 Google Cloud Project ID Creation Detailed Tutorial

If you encounter Project ID issues, follow these steps to create a Google Cloud Project:

#### Step 1: Access Google Cloud Console
1. Open your browser and visit [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account

#### Step 2: Create New Project
1. At the top of the page, click the project selector (dropdown menu showing current project name)
2. Click **"New Project"** button
3. Fill in project information:
   - **Project Name**: Enter a descriptive name (e.g., "AionUi-Gemini-Project")
   - **Organization**: Select your organization (if any)
   - **Location**: Choose project location
4. Click **"Create"** button

#### Step 3: Get Project ID
1. After project creation, you can see the newly created project in the project selector
2. Click the project name to enter the project details page
3. In the project information card, find **"Project ID"** (format like: `my-project-123456`)
4. Copy this Project ID

#### Step 4: Configure in AionUi
1. Return to AionUi's Gemini settings page
2. Paste the copied Project ID in the Project ID input box
3. Click save configuration

#### Step 5: Enable Required APIs (Optional)
To ensure complete functionality, it's recommended to enable the following APIs:
1. In Google Cloud Console, click **"APIs & Services"** > **"Library"** in the left menu
2. Search and enable:
   - **Generative Language API**
   - **AI Platform API**
   - **Vertex AI API**

**Reference Documentation**: [Gemini CLI Authentication Documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/authentication.md#workspace-gca)

### Method 2: API Key Configuration

If you prefer using API keys, you can configure multiple platforms:

1. **Enter Model Settings**
   - Click the "Settings" icon in the left sidebar
   - Select "Model Settings"

2. **Add Platform**
   - Click the "Add Model" button
   - Select platform type (Gemini, OpenAI, ModelScope, OpenRouter, etc.)
   - Enter API key and configuration information

![Model configuration screenshot - showing platform selection and API key input](assets/Images/llm%20setting.png)

**Detailed Configuration**: See the [LLM Configuration Tutorial](LLM-Configuration) for detailed configuration steps for each platform.

---

## 💬 Step 4: Start Your First Conversation

### Create New Conversation
1. **Return to Main Interface**
   - Click the "Chat" icon in the left sidebar

2. **Select Model**
   - Choose the AI model to use in the bottom left of the input box
   - If using Google login, you'll see "Gemini Google Auth" option

3. **Enter Message**
   - Type your question or request in the input box
   - You can upload files or select a working directory

![Conversation interface screenshot - showing input box, model selection, and send button](assets/gifs/file-management/file-organization.gif)

### Example Conversations
Try these simple conversations:

```
Hello, please introduce yourself
```

```
Help me write a Python function to calculate Fibonacci sequence
```

```
Please help me analyze the content of this file
```

---

## 🔧 Step 5: Basic Feature Experience

### File Upload
- **Drag and Drop**: Directly drag files to the input box
- **Click Upload**: Click the "+" button to select files or folders
- **Supported Formats**: Text files, images, code files, etc.

### Multi-Session Management
- **Create New Session**: Click "New Conversation" button
- **Switch Sessions**: Click different sessions in the left session list

### Working Directory Association
- **Associate Working Directory**: Click the "+" button in the input box, select "Open Folder" from the dropdown
- **Workspace Display**: After association, the "workspace" area will appear on the right side of the session, showing a directory tree
- **File Selection**: You can quickly view and select files to add to the dialog
- **Session Lock**: After working directory association, it cannot be modified during the session

---

## ❓ Common Questions

### Q: No models visible after startup?
**A**: Please ensure authentication is configured:
- Use Google login, or
- Add at least one platform's API key in "Model Settings"

### Q: Image generation not working?
**A**: Check the following configuration:
- Image generation is enabled in "Tool Configuration"
- A model supporting image generation is selected
- Refer to [Image Generation Configuration Guide](AionUi-Image-Generation-Tool-Model-Configuration-Guide)

### Q: How to switch between different AI models?
**A**: Model switching is not currently supported. Switching to different agents will automatically use their default models:
- Gemini CLI mode: Uses configured default models
- Multi-Agent mode: Choose different agents on the welcome page, each agent uses its default model

### Q: Where are conversation histories saved?
**A**: All conversations are saved locally:
- **macOS**: `~/Library/Application Support/AionUi/`
- **Windows**: `%APPDATA%/AionUi/`
- **Linux**: `~/.config/AionUi/`

---

## 🎉 Congratulations!

You have successfully completed the basic configuration of AionUi! Now you can:

- ✅ Use Gemini CLI mode for daily AI conversations
- ✅ Upload files for AI analysis and processing
- ✅ Use image generation features to create images
- ✅ Manage multiple conversation sessions

## 📚 Next Steps

- **Deep Learning**: Check out [LLM Configuration Tutorial](LLM-Configuration)
- **Advanced Features**: Learn about [Multi-Agent Mode Configuration](ACP-Setup)
- **Practical Cases**: Browse [Application Case Library](Use-Cases-Overview)
- **Troubleshooting**: Refer to [FAQ](FAQ)

---

**Need Help?** 
- 📖 [Complete Documentation](Home)
- 🐛 [Report Issues](https://github.com/iOfficeAI/AionUi/issues)
- 💬 [Community Discussions](https://github.com/iOfficeAI/AionUi/discussions)

*Let AI become your work assistant, making every day easier and more efficient!*