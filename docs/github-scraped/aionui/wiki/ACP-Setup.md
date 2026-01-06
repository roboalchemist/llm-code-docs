# Source: https://github.com/iOfficeAI/AionUi/wiki/ACP-Setup

# 🤖 AionUi Multi-Agent Mode Configuration Tutorial

This tutorial will detail how to configure and use Multi-Agent Mode in AionUi, including integration with external CLI tools like Claude Code, Qwen Code, CodeX, iFlow CLI, etc. These external tools are integrated through ACP (Agent Communication Protocol) for unified interface management.

**[English](ACP-Setup)** | [简体中文](ACP-Setup-Chinese)

## 🎯 Multi-Agent Mode Overview

Multi-Agent Mode is one of AionUi's core features, allowing you to use different AI agents in a unified interface. These external CLI tools are integrated through ACP (Agent Communication Protocol) with the following characteristics:

- **Unified Interface Management**: All agents operate in the same interface
- **Independent Functionality**: Each agent maintains its original features and capabilities
- **Protocol Standardization**: Standardized communication through ACP protocol
- **Flexible Extension**: Supports integration of more CLI tools that comply with ACP protocol


### Supported External Agents

| Agent | CLI Command | Authentication Required | Status |
|-------|-------------|------------------------|--------|
| **Claude Code** | `claude` | ✅ | ✅ Supported |
| **Qwen Code** | `qwen` | ✅ | ✅ Supported |
| **CodeX** | `codex` | ✅ | ✅ Supported |
| **iFlow CLI** | `iflow` | ✅ | ✅ Supported |
| **Gemini CLI** | Built into AionUi | ✅ | ✅ Enabled by default |

### Multi-Agent Mode vs Gemini CLI Mode

| Feature | Gemini CLI Mode | Multi-Agent Mode |
|---------|-----------------|----------------|
| **Installation Requirements** | **Built into AionUi, users get it by default after downloading** | **Requires users to download and install themselves, then AionUi recognizes and integrates** |
| **Technical Architecture** | AionUi built-in Agent, based on Google Gemini CLI | External CLI tools integrated via ACP protocol |
| **Feature Completeness** | Complete features (image generation, tool scheduling, multi-API key rotation, etc.) | Currently relatively simple, mainly GUI management of conversations and workspaces |
| **Configuration Integration** | Direct access to all AionUi configuration features | Currently cannot directly use AionUi's LLM configuration, image generation, and other built-in features |
| **Future Development** | Most complete functionality, continuous optimization | ACP-integrated tools will gradually catch up, unified management features planned |
| **Use Cases** | Daily use, complete AI functionality experience | Professional users, specific CLI tool requirements |

---

## 🚀 Step 1: Install CLI Tools

Before configuring Multi-Agent Mode, you need to install the corresponding CLI tools first.

### Claude Code Installation

1. **Install Claude CLI**
   ```bash
   # Install globally with npm
   npm install -g @anthropic-ai/claude-code
   ```

2. **Verify Installation**
   ```bash
   claude --version
   ```

3. **Authentication Configuration**
   ```bash
   # Login to Claude account
   claude login
   ```

> 📖 **Official Documentation**: [Claude Code GitHub](https://github.com/anthropics/claude-code)


### Qwen Code Installation

1. **Install Qwen CLI**
   ```bash
   # Install globally with npm
   npm install -g @qwen-code/qwen-code
   ```

2. **Verify Installation**
   ```bash
   qwen --version
   ```

3. **Authentication Configuration**
   ```bash
   # Login to Qwen account
   qwen login
   ```

> 📖 **Official Documentation**: [Qwen Code GitHub](https://github.com/QwenLM/qwen-code)


### CodeX Installation

1. **Install CodeX CLI**
   ```bash
   # Install globally with npm
   npm install -g @openai/codex
   ```

2. **Verify Installation**
   ```bash
   # Check version
   codex --version
   ```

3. **Authentication Configuration**
   ```bash
   # Login to OpenAI account
   codex login
   ```

> 📖 **Official Documentation**: [OpenAI Codex CLI](https://developers.openai.com/codex/cli/)


### iFlow CLI Installation

1. **Install iFlow CLI**
   ```bash
   # Install globally with npm
   npm install -g @iflow-ai/iflow-cli
   ```

2. **Verify Installation**
   ```bash
   iflow --version
   ```

3. **Authentication Configuration**
   ```bash
   # Login to iFlow account
   iflow login
   ```

> 📖 **Official Documentation**: [iFlow CLI GitHub](https://github.com/iflow-ai/iflow-cli)


---

## 💬 Step 2: Using Multi-Agent Mode

### Create Multi-Agent Conversation

1. **Select Agent**
   - Choose the external agent to use on the welcome interface
   - System will display detected available agents (integrated via ACP protocol)

2. **Create Conversation**
   - Enter message content
   - Select working directory (optional)
   - Click send to start conversation

![ACP conversation creation screenshot - showing agent selection and conversation creation](assets/Images/ACP.png)

### Conversation Features

1. **Real-time Connection Status**
   - Shows agent connection status
   - Automatic reconnection mechanism
   - Connection error prompts

2. **Permission Management**
   - CLI tools will request file operation permissions
   - Confirm or deny permission requests in AionUi
   - Supports one-time or permanent authorization


3. **Tool Calling**
   - Supports CLI tool's native functionality
   - File read/write operations
   - Code execution and debugging

---



## ❓ Common Questions

### Q: What's the difference between Multi-Agent Mode and Gemini CLI mode?
**A**: Main differences:
- **Gemini CLI Mode**: AionUi's built-in core functionality, users get it by default after downloading, supports image generation, tool scheduling and other complete features
- **Multi-Agent Mode**: Requires users to install external CLI tools themselves, AionUi recognizes and integrates them through ACP protocol, currently relatively simple functionality, will develop MCP settings functionality to enhance integration in the future

### Q: When to choose Multi-Agent Mode?
**A**: Selection recommendations:
- **Daily Use**: Recommend Gemini CLI mode, most complete functionality, ready to use out of the box
- **Professional Needs**: If you need specific CLI tool functionality (like Claude Code, Qwen Code, etc.), you can choose Multi-Agent Mode
- **Future Planning**: MCP functionality will let Multi-Agent Mode enjoy more unified features

### Q: How to know if Multi-Agent Mode is working properly?
**A**: Check methods:
- Can see agent options on welcome interface
- Can connect normally when creating conversations
- Can receive replies when sending messages
- Permission requests display normally

### Q: What features does Multi-Agent Mode support?
**A**: Current features:
- Basic conversation functionality
- File operation permission management
- CLI tool's native functionality
- Working directory management

---

## 🔧 Troubleshooting

### Q: Multi-Agent Mode not detected?
**A**: Check steps:

1. **Confirm CLI tool is properly installed**
   ```bash
   # macOS/Linux
   which claude
   which qwen
   which iflow
   
   # Windows
   where claude
   where qwen
   where iflow
   ```

2. **Verify CLI is in system PATH**
   - Ensure CLI tools are in system environment variable PATH
   - Restart terminal or command line window

3. **Check CLI tool version**
   ```bash
   claude --version
   qwen --version
   iflow --version
   ```

4. **Restart AionUi to re-detect**
   - AionUi automatically scans system PATH on startup
   - Detects installed external CLI tools
   - Shows available Multi-Agent options on welcome interface

### Q: Authentication failed?
**A**: Solutions:
1. Run `claude login` or `qwen login` in terminal
2. Complete CLI tool authentication process
3. Restart AionUi to reconnect

### Q: Connection timeout?
**A**: Possible reasons:
1. Network connection issues
2. CLI tool service unavailable
3. Firewall blocking connection
4. CLI tool version too old

### Q: Permission requests not showing?
**A**: Check configuration:
1. Confirm Multi-Agent Mode is properly connected
2. Check AionUi permission settings
3. Restart conversation to re-establish connection

---

## 📚 Related Documentation

- **Quick Start**: [Getting Started](Getting-Started)
- **LLM Configuration**: [LLM Configuration](LLM-Configuration)
- **Image Generation Configuration**: [Image Generation Setup](AionUi-Image-Generation-Tool-Model-Configuration-Guide)
- **Common Questions**: [FAQ](FAQ)

---

**Need Help?**
- 🐛 [Report Issues](https://github.com/iOfficeAI/AionUi/issues)
- 💬 [Community Discussions](https://github.com/iOfficeAI/AionUi/discussions)
- 📖 [Complete Documentation](Home)

*Multi-Agent Mode lets you enjoy the powerful functionality of multiple AI tools in AionUi!*