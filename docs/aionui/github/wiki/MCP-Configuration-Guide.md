# Source: https://github.com/iOfficeAI/AionUi/wiki/MCP-Configuration-Guide

# 🔌 AionUi MCP Configuration Guide

Welcome to AionUi's MCP (Model Context Protocol) configuration guide! This tutorial will provide detailed instructions on how to configure and manage MCP services in AionUi, helping you easily extend your AI assistant's capabilities.

**[English](MCP-Configuration-Guide)** | [简体中文](MCP-Configuration-Guide-Chinese)

## 🌟 What is MCP?

**MCP (Model Context Protocol)** is an open standard that allows AI assistants to communicate securely and structurally with external tools and services. In AionUi, MCP enables you to:

- **Extend AI functionality**: Connect to various external tools and services
- **Unified management**: Manage all MCP services in one interface
- **Simplify configuration**: Support multiple addition methods, reducing configuration difficulty
- **Real-time monitoring**: Automatically test connection status to ensure service availability

### How MCP Works

```
AI Assistant ←→ MCP Protocol ←→ External Tools/Services
```

MCP acts as a middleware layer, allowing AI assistants to:
1. **Discover tools**: Automatically identify available tools and functions
2. **Call services**: Securely execute external operations
3. **Get results**: Receive and process data returned by services

---

## 🎯 MCP Implementation in AionUi

### Core Features

| Feature | Description | Benefits |
|---------|-------------|----------|
| **Unified Management Interface** | Centralized management of all MCP services in settings | Simple operation, clear overview |
| **Multiple Addition Methods** | Support for JSON configuration and one-click import | Flexible adaptation to different needs |
| **Automatic Connection Testing** | Automatic validation of service availability after addition | Ensures correct configuration |
| **Batch Operations** | One-click enable/disable multiple services | Improves management efficiency |
| **Status Monitoring** | Real-time display of connection status and tool lists | Facilitates troubleshooting |

### Supported Transport Methods

AionUi currently supports the following MCP transport methods:

1. **stdio**: Standard input/output (most common)
2. **sse**: Server-sent events
3. **http**: HTTP requests
4. **streamable-http**: Streamable HTTP

---

## 🚀 Quick Start

### Prerequisites

Before starting MCP configuration, ensure:

- ✅ AionUi is properly installed and running
- ✅ At least one AI model is configured (Gemini, OpenAI, etc.)
- ✅ Basic understanding of JSON configuration format (optional)

### Accessing MCP Management Interface

1. **Open AionUi**
2. **Enter Settings Page**
   - Click the "Settings" icon in the left sidebar
3. **Select Tools Settings**
   - Choose "Tools Settings" in the settings page
4. **Find MCP Management**
   - Locate the "MCP Management" section in tools settings

![MCP Settings Entry Interface](assets/Images/mcp%20setting%20entrance.png)

---

## 📋 Configuration Methods

### Method 1: Add via JSON Configuration

This is the most flexible configuration method, suitable for experienced users:

#### Step 1: Prepare JSON Configuration

The JSON configuration format for MCP services is as follows:

```json
{
  "mcpServers": {
    "service-name": {
      "description": "Service description",
      "command": "command",
      "args": ["arg1", "arg2"],
      "env": {
        "ENV_VAR_NAME": "env_var_value"
      }
    }
  }
}
```

#### Step 2: Add Service

1. **Click Add Button**
   - Click "Add MCP Service" button in MCP management interface
   - Select "Add via JSON"

2. **Input Configuration**
   - Paste JSON configuration in the popup dialog
   - Click "Confirm" button

3. **Automatic Testing**
   - AionUi will automatically test the connection
   - Successfully connected services will show green checkmark

![JSON Configuration Interface](assets/Images/mcp%20import%20from%20JSON.png)

### Method 2: One-Click Import from CLI

If you have already configured MCP in CLI tools, you can use the one-click import feature:

#### Step 1: Select CLI Tool

1. **Click Add Button**
   - Click "Add MCP Service" button in MCP management interface
   - Select "Import from CLI"

2. **Choose CLI**
   - Select the CLI tool with configured MCP from the dropdown
   - Supported CLIs: Gemini CLI, Claude Code, Qwen Code, etc.

#### Step 2: Import Configuration

1. **Click Import Button**
   - After selecting CLI, click "Import from CLI" button
   - AionUi will automatically read the CLI's MCP configuration

2. **Confirm Import**
   - Review the imported service list
   - Click "Save" to complete the import

![CLI One-Click Import Interface](assets/Images/MCP%20import%20form%20CLI.png)

---

## ⚙️ Service Management

### View Service Status

In the MCP management interface, each service displays:

- **Service Name**: MCP service identifier
- **Connection Status**:
  - ✅ **Connected**: Service running normally
  - ❌ **Connection Failed**: Service unavailable
  - 🔄 **Testing**: Testing connection
  - ⚪ **Disconnected**: Service not started
- **Tool List**: Click to expand and view available tools

### Management Operations

#### Enable/Disable Service

1. **Toggle Switch**
   - Click the switch button on the right side of the service
   - After enabling, it will automatically sync to all CLI tools

2. **View Sync Status**
   - After successful enabling, CLI icons will appear next to the service name
   - Indicates the service has been synced to corresponding CLI tools

#### Test Connection

1. **Manual Test**
   - Click the refresh button on the right side of the service
   - Re-test the service connection status

2. **View Results**
   - Status icon will be updated after testing
   - Error information will be displayed if failed

#### Edit Service

1. **Enter Edit Mode**
   - Click the edit button on the right side of the service
   - Modify service configuration

2. **Save Changes**
   - Click save after modifications
   - System will automatically re-test the connection

#### Delete Service

1. **Confirm Deletion**
   - Click the delete button on the right side of the service
   - Click "Confirm" in the confirmation dialog

2. **Clean Sync**
   - After deletion, it will automatically remove from all CLI tools
   - Ensures configuration consistency

---

## 🛠️ Usage Examples

### Example 1: File Management Tools

After configuring filesystem MCP service, you can:

```
User: Help me organize the files on my desktop
AI: I'll help you organize your desktop files. Let me first check what files are on your desktop...

[Calling filesystem MCP]
- Scan desktop directory
- Categorize by file type
- Create organized folder structure
- Move files to corresponding folders

Organization complete! I've categorized and organized your desktop files by type.
```

### Example 2: Browser Automation

After configuring Chrome DevTools MCP, you can:

```
User: Help me open GitHub and search for AionUi project
AI: I'll help you open GitHub and search for the AionUi project.

[Calling chrome-devtools MCP]
- Open Chrome browser
- Navigate to GitHub.com
- Enter "AionUi" in search box
- Execute search operation

Search complete! I've opened GitHub and searched for the AionUi project for you.
```

### Example 3: Git Operations

After configuring Git MCP service, you can:

```
User: Help me check the commit history of the current project
AI: I'll help you check the project's commit history.

[Calling git MCP]
- Connect to Git repository
- Get commit history records
- Format and output commit information

Commit History:
commit abc123 - Fix login functionality (2024-01-15)
commit def456 - Add user management module (2024-01-14)
commit ghi789 - Initialize project (2024-01-13)
```

### Example 4: Memory Management

After configuring Memory MCP service, you can:

```
User: Help me remember this important information: project deadline is next Friday
AI: I'll help you remember this important information.

[Calling memory MCP]
- Store important information in memory
- Set reminder tags
- Confirm save success

Information saved! I've remembered "project deadline is next Friday" as important information.
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Service Connection Failed

**Problem**: MCP service shows red X, cannot connect

**Possible Causes**:
- Incorrect command path
- Dependencies not installed
- Network connection issues
- Insufficient permissions

**Solutions**:
1. **Check Command**: Ensure `command` and `args` configuration is correct
2. **Install Dependencies**: Run `npm install -g package-name` to install required packages
3. **Check Network**: Ensure network connection is normal
4. **Permission Check**: Ensure sufficient system permissions

#### 2. Empty Tool List

**Problem**: Service connects successfully, but tool list is empty

**Possible Causes**:
- MCP service doesn't properly implement tool interface
- Service version incompatibility
- Missing configuration parameters

**Solutions**:
1. **Check Service**: Ensure MCP service implementation is correct
2. **Update Version**: Use the latest version of the service
3. **Complete Configuration**: Add necessary environment variables

#### 3. CLI Sync Failed

**Problem**: Service works normally in AionUi, but CLI tools cannot use it

**Possible Causes**:
- CLI tool version is too old
- Configuration format incompatibility
- CLI tool not properly installed

**Solutions**:
1. **Update CLI**: Upgrade to the latest version
2. **Re-sync**: Disable and re-enable the service
3. **Check Installation**: Ensure CLI tool is properly installed

---

## 🔗 Related Resources

### Official Documentation

- **[MCP Official Specification](https://modelcontextprotocol.io/)** - Official MCP protocol documentation
- **[AionUi GitHub](https://github.com/iOfficeAI/AionUi)** - AionUi project homepage
- **[MCP Server List](https://github.com/modelcontextprotocol/servers)** - Official MCP servers

### Community Resources

- **[GitHub Discussions](https://github.com/iOfficeAI/AionUi/discussions)** - Community discussions and feedback
- **[Issue Reports](https://github.com/iOfficeAI/AionUi/issues)** - Report bugs and feature requests
- **[Release Notes](https://github.com/iOfficeAI/AionUi/releases)** - View latest versions and updates

### Learning Resources

- **[Quick Start Guide](Getting-Started)** - AionUi basic configuration
- **[LLM Configuration](LLM-Configuration)** - AI model configuration tutorial
- **[Multi-Agent Mode Setup](ACP-Setup)** - CLI tool integration tutorial
- **[FAQ](FAQ)** - Q&A and troubleshooting

---

**Start your MCP journey and make your AI assistant more powerful!** 🚀
