# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/mcp-server-config.md

# MCP Server Config

Use MCP servers to extend Tabnine CLI with extra tools and context providers. This page shows where MCP config lives and how scope and overrides work. It also covers `tabnine mcp` commands and runtime flags for selecting servers.

## **Configuring MCP for Tabnine CLI**

### **Overview**

The Tabnine CLI supports MCP (Model Context Protocol) servers, which allow you to extend the CLI's capabilities with additional tools and context providers. This guide explains how to configure and manage MCP servers.

### **Prerequisites**

* Tabnine CLI installed (available at `~/.local/bin/tabnine`)
* Node.js/npm (for npx-based MCP servers)
* Python (for Python-based MCP servers, optional)

### **MCP Management Commands**

#### **Adding an MCP Server**

**Syntax:**

```bash
tabnine mcp add <name> <commandOrUrl> [args...]
```

**Parameters:**

* `<name>`: A unique identifier for your MCP server
* `<commandOrUrl>`: The command to run the server or a URL to connect to it
* `[args...]`: Optional arguments to pass to the server command

#### **Other Management Commands**

```shell
# List all configured MCP servers
tabnine mcp list

# Enable an MCP server
tabnine mcp enable <name>

# Disable an MCP server
tabnine mcp disable <name>

# Remove an MCP server
tabnine mcp remove <name>
```

### **Common MCP Server Examples**

#### **Filesystem server (local)**

```bash
tabnine mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /path/to/repo
​tabnine mcp enable filesystem


```

#### **GitHub server (local process)**

```bash
tabnine mcp add github npx -y @modelcontextprotocol/server-github
tabnine mcp enable github

```

#### **Custom server (any command)**

```bash
# Node
​
tabnine mcp add local-dev node /path/to/your/mcp-server/index.js
tabnine mcp enable local-dev

```

### **Using MCP Servers in Tabnine CLI**

#### **Running Tabnine with Specific MCP Servers**

Once you've configured MCP servers, you can specify which ones to use when running Tabnine:

```shell
# Run with specific MCP servers
tabnine --allowed-mcp-server-names filesystem github

# Run with multiple servers
tabnine --allowed-mcp-server-names server1 server2 server3
```

#### **Using in Interactive Mode**

```shell
# Start interactive session with MCP servers
tabnine --allowed-mcp-server-names filesystem

# Start with a prompt and MCP servers
tabnine --prompt-interactive "Help me analyze this project" --allowed-mcp-server-names filesystem
```

#### **Using in Non-Interactive Mode**

```shell
# Run a single prompt with MCP servers
tabnine --prompt "List all files in the project" --allowed-mcp-server-names filesystem
```

### **Complete Workflow Example**

Here's a complete example of setting up and using a filesystem MCP server:

```shell
# 1. Add the filesystem server for your project
tabnine mcp add my-project npx -y @modelcontextprotocol/server-filesystem ~/myproject

# 2. Verify it was added
tabnine mcp list

# 3. Enable the server (if not already enabled)
tabnine mcp enable my-project

# 4. Run Tabnine with the MCP server
tabnine --allowed-mcp-server-names my-project

# 5. In the chat, you can now ask questions like:
#    - "What files are in this project?"
#    - "Read the contents of package.json"
#    - "Analyze the code structure"
```

### **Configuration Storage**

MCP server configurations are stored in the Tabnine agent directory:

* Location: `~/.tabnine/agent/`
* Settings file: `~/.tabnine/agent/settings.json`

### **Additional Options**

#### **Auto-Approval Modes**

When using MCP servers, you can control how tool calls are approved:

```shell
# Default mode (prompt for approval)
tabnine --allowed-mcp-server-names filesystem

# Auto-approve edit tools only
tabnine --approval-mode auto_edit --allowed-mcp-server-names filesystem

# Auto-approve all tools (YOLO mode)
tabnine --approval-mode yolo --allowed-mcp-server-names filesystem
# OR
tabnine --yolo --allowed-mcp-server-names filesystem

# Read-only mode (plan mode)
tabnine --approval-mode plan --allowed-mcp-server-names filesystem
```

#### **Allow Specific Tools**

You can also allow specific tools to run without confirmation:

```shell
tabnine --allowed-tools read_file list_directory --allowed-mcp-server-names filesystem
```

### **Troubleshooting**

#### **Check if MCP servers are configured**

```shell
tabnine mcp list
```

#### **Debug mode**

```shell
tabnine --debug --allowed-mcp-server-names filesystem
```

#### **Verify Tabnine CLI version**

```shell
tabnine --help
```

### **Popular MCP Servers**

Here are some popular MCP servers you might want to configure:

1. `@modelcontextprotocol/server-filesystem` - File system access
2. `@modelcontextprotocol/server-github` - GitHub integration
3. `@modelcontextprotocol/server-slack` - Slack integration
4. `@modelcontextprotocol/server-postgres` - PostgreSQL database access
5. `@modelcontextprotocol/server-memory` - Persistent memory/notes
6. `@modelcontextprotocol/server-brave-search` - Web search capabilities
7. `@modelcontextprotocol/server-google-maps` - Google Maps integration

To explore more MCP servers, visit: <https://github.com/modelcontextprotocol>

### **Best Practices**

1. **Use descriptive names** for your MCP servers (e.g., `project-files`, `company-github`)
2. **Enable only the servers you need** to reduce overhead
3. **Use approval modes carefully** - avoid `--yolo` mode unless you fully trust the operations
4. **Test servers individually** before combining multiple servers
5. **Keep MCP server packages updated** using `npm update` or `pip install --upgrade`
