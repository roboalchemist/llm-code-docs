# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/tools.md

# Tools

Configure tools and capabilities available to your AI agents.

![Tools Management](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-6f323fca00bd31bc1b4c38c0800e105a51991959%2Ftools_list_view.png?alt=media)

## Overview

The Tools Management section allows you to manage AI tools, MCP servers, and custom integrations that your agents can use to perform tasks and interact with external systems.

## Tools Dashboard

The dashboard displays key metrics at a glance:

**Summary Cards**:

* **Total Tools**: Total number of tools configured
* **Active**: Number of active tools
* **Disabled**: Number of disabled tools

## Tool List View

The tools table shows all available tools with the following information:

**Columns**:

* **Tool**: Tool name and icon
* **Type**: Tool type with color-coded badges (Custom, MCP, Built-in)
* **Agent**: Associated agent name
* **Status**: Current status (Active, Disabled, Pending)
* **Created**: Creation date
* **Updated**: Last update date
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by tool name
* Filter by Type (Custom, MCP, Built-in)
* Filter by Status (Active, Disabled, Pending)
* Filter by Agent

## Creating a Tool

Navigate to **Agent Configuration** → **Tools** → Click **Create**

![Create Tool](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-885b4dc8c7f2144f8cfbb9f7ba136f48bfc09390%2Ftool_create_form.png?alt=media)

### Basic Information

**Tool Name**\* (Required)

* A descriptive name for this tool
* Example: `Ticket Manager`
* Helper text: "A descriptive name for this tool"

**Tool Type**\* (Required)

* Select from dropdown: Custom, MCP, Built-in
* Default: `Custom`
* Helper text: "Type of tool integration"

**Status**\* (Required)

* Select from dropdown: Active, Disabled, Pending
* Default: `Active`
* Helper text: "Current status of this tool"

### Configuration

Click to expand the Configuration section for tool-specific settings.

**Search Engine**

* Search engine to use
* Dropdown selection
* Helper text: "Search engine to use"

**Max Results**

* Maximum number of search results
* Example: (empty or numeric value)
* Helper text: "Maximum number of search results"

**Allowed File Extensions**

* Comma-separated list of allowed file extensions
* Example: (empty or ".pdf,.doc,.txt")
* Helper text: "Comma-separated list of allowed file extensions"

**Max File Size (bytes)**

* Maximum file size in bytes (e.g., 10485760 = 10MB)
* Example: (empty or numeric value)
* Helper text: "Maximum file size in bytes (e.g., 10485760 = 10MB)"

**Base Path**

* Base directory path for file operations
* Example: (empty or "/path/to/directory")
* Helper text: "Base directory path for file operations"

**Connection String**

* Database connection string
* Example: (empty or connection string)
* Helper text: "Database connection string"

**Timeout (ms)**

* Operation timeout in milliseconds
* Example: (empty or numeric value)
* Helper text: "Operation timeout in milliseconds"

**API Endpoint**

* External API endpoint URL
* Example: `https://api.zendesk.com/v2`
* Helper text: "External API endpoint URL"

**Rate Limit (per minute)**

* Maximum requests per minute
* Example: `100`
* Helper text: "Maximum requests per minute"

**Retry Count**

* Number of retry attempts on failure
* Example: `3`
* Helper text: "Number of retry attempts on failure"

### Actions

* **Cancel**: Discard and close
* **Create Tool**: Save the tool

## Viewing Tool Details

To view detailed information about a tool:

1. Navigate to **Agent Configuration** → **Tools**
2. Click on a tool from the list
3. View comprehensive details in the modal dialog

![View Tool Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-7e71af86884d542e281f95ae43449c9cb2d9d9c9%2Ftool_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Tool Name**: e.g., "Ticket Manager"
* **Tool Type**: Custom, MCP, or Built-in
* **Status**: Active, Disabled, or Pending

**Configuration** (Expandable): All configuration fields are displayed in read-only mode:

* Search Engine
* Max Results
* Allowed File Extensions
* Max File Size (bytes)
* Base Path
* Connection String
* Timeout (ms)
* API Endpoint
* Rate Limit (per minute)
* Retry Count

## Editing a Tool

To update a tool:

1. Open tool details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Tool modal

![Edit Tool Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-a8b9155d88c5a8cec2093a0f3c6e007a21fe5242%2Ftool_edit_form.png?alt=media)

4. Click **Update Tool** to save changes

> \[!NOTE] The Edit form is identical to the Create/View form, but with an "Update Tool" button.

**Editable Fields**:

* ✅ Tool Name
* ✅ Status (Active ↔ Disabled ↔ Pending)
* ✅ All configuration fields
* ❌ Tool Type (cannot edit after creation)

## Tool Types

**Custom Tools**:

* User-defined integrations
* Custom API connections
* Specific business logic
* Orange badge in list view

**MCP (Model Context Protocol) Tools**:

* Standardized protocol tools
* Pre-built integrations
* Community-maintained
* Purple badge in list view

**Built-in Tools**:

* Platform-provided tools
* Core functionality
* Maintained by Kaisar AI
* Blue badge in list view

## Tool Configuration Fields

Different tool types may have different configuration fields:

**API Integration Tools**:

* API Endpoint
* Rate Limit
* Retry Count
* Timeout

**File Management Tools**:

* Base Path
* Allowed File Extensions
* Max File Size

**Database Tools**:

* Connection String
* Timeout
* Retry Count

**Search Tools**:

* Search Engine
* Max Results

## Managing Tools

### Enabling/Disabling Tools

To change tool status:

1. Edit the tool
2. Change Status field
3. Save changes

**Active**: Tool is available for agents to use **Disabled**: Tool is not available **Pending**: Tool is being configured or tested

### Assigning Tools to Agents

Tools can be assigned to:

* **Specific agents**: Only that agent can use the tool
* **All Agents**: Available to all agents in the organization

### Deleting a Tool

To remove a tool:

1. Navigate to tool details or list
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] Deleting a tool will affect any agents using it. Make sure to update agent configurations before deleting.

## Best Practices

**Tool Configuration**:

* Set appropriate rate limits
* Configure timeouts properly
* Validate API endpoints
* Test before enabling

**Security**:

* Use secure API endpoints (HTTPS)
* Store credentials securely
* Limit file access paths
* Validate file extensions

**Performance**:

* Set reasonable timeouts
* Configure retry logic
* Monitor tool usage
* Optimize rate limits

**Maintenance**:

* Keep tools updated
* Monitor error rates
* Review logs regularly
* Disable unused tools

**Testing**:

* Test tools before activation
* Verify error handling
* Check rate limits
* Validate outputs

## Tool Usage Monitoring

**Metrics to Track**:

* Number of calls per tool
* Success/failure rates
* Average response time
* Error types and frequency

**Alerts**:

* Rate limit exceeded
* High error rates
* Timeout issues
* API endpoint failures

## Next Steps

* Configure [Instructions](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/instructions) for tool usage
* Set up [Platform Connections](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/platform-connections) for API access
* Define [Routes](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/routes) that use these tools
* Assign tools to agents in [Organization → Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents)
