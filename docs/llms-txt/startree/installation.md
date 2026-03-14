# Source: https://docs.startree.ai/corecapabilities/ai/mcp/installation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation

# MCP Server Installation

This guide covers installing and configuring the StarTree MCP Server for Apache Pinot & StarTree Cloud

## Prerequisites

### System Requirements

* **Python 3.9+** installed on your system
* **Apache Pinot cluster & StarTree Cloud**
* **Git** for cloning the repository

### Install uv Package Manager

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver, written in Rust. It's designed to be a drop-in replacement for pip with significantly better performance.

```bash  theme={null}
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload your shell configuration
source ~/.bashrc  # or ~/.zshrc

# Alternatively, restart your terminal

# Verify installation
uv --version
```

## Installation Steps

### 1. Clone the Repository

```
git clone https://github.com/startreedata/mcp-pinot.git
cd mcp-pinot
```

### 2. Install Dependencies

```bash  theme={null}
# Install the MCP server
uv pip install -e .

# For development (includes testing tools)
uv pip install -e .[dev]
```

### 3. Configure Pinot Connection

The MCP server requires a `.env` file to configure the Pinot cluster connection.

```bash  theme={null}
# Copy the example configuration
cp .env.example .env
```

Edit the `.env` file with your Pinot cluster details:

#### Local Pinot Quickstart

```
# .env file for local Pinot
PINOT_CONTROLLER_URL=http://localhost:9000
PINOT_BROKER_HOST=localhost 
PINOT_BROKER_PORT=8000 
PINOT_BROKER_SCHEME=http
PINOT_USE_MSQE=true
```

#### StarTree Cloud

```
# .env file for StarTree Cloud
PINOT_CONTROLLER_URL=https://pinot.celpxu.cp.s7e.startree.cloud
PINOT_BROKER_HOST=broker.pinot.celpxu.cp.s7e.startree.cloud
PINOT_BROKER_PORT=443
PINOT_BROKER_SCHEME=https
PINOT_TOKEN=Bearer <token generated from startree cloud>
PINOT_USE_MSQE=true
PINOT_DATABASE=ws_2kc8eddzzb0 (startree workspace id)
```

### 4. Run the MCP Server

```
uv --directory . run mcp_pinot/server.py
```

You should see logs indicating that the server is running and listening on STDIO:

```
INFO: MCP server started successfully
INFO: Listening on STDIO for MCP connections
```

### 5. Verify

With your MCP server running, test the connection in another terminal:

```bash  theme={null}
uv --directory . run tests/test_service/test_pinot_quickstart.py
```

Expected output:

```
✓ MCP server connection successful
✓ Available tools discovered: ['list-tables', 'read-query', ...]
✓ Sample query executed successfully
✓ All tests passed
```

## Configure MCP Clients

With your MCP server installed and running, the final step is to configure your MCP client of choice to connect and start querying your data with natural language.

<CardGroup cols={2}>
  <Card title="Claude Desktop" icon="desktop" iconType="light" href="/corecapabilities/ai/mcp/claude">
    Claude Desktop is a desktop application that interacts with LLMs and connects to the StarTree MCP server.
  </Card>

  <Card title="LibreChat" icon="desktop" iconType="light" href="/corecapabilities/ai/mcp/librechat">
    LibreChat is a self-hosted chat interface that interacts with private LLMs (including AWS Bedrock models) and connects to the StarTree MCP server for secure, on-premises AI analytics.
  </Card>

  <Card title="Cursor IDE" icon="desktop" iconType="light" href="/corecapabilities/ai/mcp/cursor">
    Cursor IDE is an AI-powered code editor that integrates MCP pinot servers with your broader development workflow
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
