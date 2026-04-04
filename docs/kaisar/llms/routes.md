# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/routes.md

# Routes

Define workflows and routing logic for your AI agents.

![Routes Management](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-069fda3ff91ed399fe4730229a1c02e40215d1f7%2Froutes_list_view.png?alt=media)

## Overview

Routes Management allows you to configure and manage API routes, webhooks, and endpoint routing for your AI agents. Define how incoming requests are handled, processed, and responded to.

## Routes Dashboard

The dashboard displays key metrics at a glance:

**Summary Cards**:

* **Total Routes**: Total number of routes configured
* **Active**: Number of active routes
* **Error**: Number of routes with errors

## Route List View

The routes table shows all configured routes with the following information:

**Columns**:

* **Route**: Route name and path
* **Method**: HTTP method (POST, GET, etc.)
* **Type**: Route type (Webhook, API, File, Redirect, Health)
* **Status**: Current status (Active, Inactive)
* **Priority**: Priority level (1-10)
* **Requests**: Total number of requests
* **Avg Response**: Average response time
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by route name or path
* Filter by Method (POST, GET, PUT, DELETE, etc.)
* Filter by Type (Webhook, API, File, Redirect, Health)
* Filter by Status (Active, Inactive)

## Creating a Route

Navigate to **Agent Configuration** → **Routes** → Click **Create**

![Create Route](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-c2f801db666e23305f9feb776bf3e63603d9d0cc%2Froute_create_form.png?alt=media)

### Basic Information

**Route Name**\* (Required)

* Descriptive name for this route
* Example: `Discord Webhook`
* Helper text: "Descriptive name for this route"

**Path**\* (Required)

* URL path pattern (use {param} for variables)
* Example: `/webhook/discord/{server_id}`
* Helper text: "URL path pattern (use {param} for variables)"

**HTTP Method**\* (Required)

* Select from dropdown: POST, GET, PUT, DELETE, PATCH
* Helper text: "HTTP method for this route"

**Route Type**\* (Required)

* Select from dropdown: Webhook, API, File, Redirect, Health
* Helper text: "Type of route endpoint"

**Description**

* Optional description
* Example: "Webhook endpoint for Discord bot integration"
* Helper text: "Optional description"

### Configuration

Expandable section for route configuration.

**Priority**\* (Required)

* Route matching priority (lower = higher priority)
* Example: `1`
* Helper text: "Route matching priority (lower = higher priority)"

**Timeout (ms)**\* (Required)

* Request timeout in milliseconds
* Example: `30000`
* Helper text: "Request timeout in milliseconds"

**Retry Attempts**\* (Required)

* Number of retry attempts on failure
* Example: `3`
* Helper text: "Number of retry attempts on failure"

**Enabled**

* Checkbox to enable/disable the route
* Default: Unchecked

**Authentication Required**

* Checkbox to require authentication
* Default: Unchecked

### Handler Configuration

Expandable section for handler-specific settings.

**Response Type**

* Type of response to return
* Dropdown selection: JSON, Text, HTML, XML, etc.
* Helper text: "Type of response to return"

**Status Code**

* HTTP status code for success
* Example: `200`
* Helper text: "HTTP status code for success"

**Agent Prompt**

* Prompt for AI agent processing
* Large text area
* Example: "You are a helpful Discord bot assistant. Respond professionally and concisely."
* Helper text: "Prompt for AI agent processing"

### Security

Expandable section for security settings.

**Require Authentication**

* Checkbox to require authentication

**Enable Rate Limiting**

* Checkbox to enable rate limiting

**Requests Limit**

* Number of requests allowed
* Example: `100`
* Helper text: "Number of requests allowed"

**Time Window (ms)**

* Time window in milliseconds
* Example: `60000`
* Helper text: "Time window in milliseconds"

### Rate Limits

Expandable section for detailed rate limiting.

**Requests per Minute**

* Maximum requests per minute
* Example: `100`
* Helper text: "Maximum requests per minute"

**Requests per Hour**

* Maximum requests per hour
* Example: `2000`
* Helper text: "Maximum requests per hour"

**Requests per Day**

* Maximum requests per day
* Example: `10000`
* Helper text: "Maximum requests per day"

**Burst Limit**

* Maximum burst of requests
* Example: `10`
* Helper text: "Maximum burst of requests"

### Actions

* **Cancel**: Discard and close
* **Create Route**: Save the route

## Viewing Route Details

To view detailed information about a route:

1. Navigate to **Agent Configuration** → **Routes**
2. Click on a route from the list
3. View comprehensive details in the modal dialog

![View Route Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4d4b1c8a7d671e5b3370403722d1a11da302b5ca%2Froute_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Route Name**: e.g., "Discord Webhook"
* **Path**: e.g., `/webhook/discord/{server_id}`
* **HTTP Method**: POST, GET, etc.
* **Route Type**: Webhook, API, File, etc.
* **Description**: Full description

**Configuration**:

* **Priority**: Route matching priority
* **Timeout (ms)**: Request timeout
* **Retry Attempts**: Number of retry attempts
* **Enabled**: Checkbox status
* **Authentication Required**: Checkbox status

**Handler Configuration**:

* **Response Type**: JSON, Text, HTML, etc.
* **Status Code**: HTTP status code
* **Agent Prompt**: Full prompt text

**Security**:

* **Require Authentication**: Checkbox status
* **Enable Rate Limiting**: Checkbox status
* **Requests Limit**: Number of requests allowed
* **Time Window (ms)**: Time window

**Rate Limits**:

* **Requests per Minute**: Maximum per minute
* **Requests per Hour**: Maximum per hour
* **Requests per Day**: Maximum per day
* **Burst Limit**: Maximum burst

## Editing a Route

To update a route:

1. Open route details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Route modal

![Edit Route Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-6b88f7f267ed0b09aa19eb89e92dd442bf38063b%2Froute_edit_form.png?alt=media)

4. Click **Update Route** to save changes

> \[!NOTE] The Edit form is identical to the Create/View form, but with an "Update Route" button.

**Editable Fields**:

* ✅ Route Name
* ✅ Description
* ✅ Priority
* ✅ Timeout
* ✅ Retry Attempts
* ✅ Enabled (checkbox)
* ✅ Authentication Required (checkbox)
* ✅ Handler Configuration (Response Type, Status Code, Agent Prompt)
* ✅ Security settings
* ✅ Rate Limits
* ❌ Path (cannot edit after creation)
* ❌ HTTP Method (cannot edit after creation)
* ❌ Route Type (cannot edit after creation)

## Route Types

**Webhook**:

* Receive webhooks from external services
* Process incoming webhook payloads
* Respond with custom data

**API**:

* RESTful API endpoints
* Handle API requests and responses
* Integrate with agent processing

**File**:

* File upload/download endpoints
* Handle file operations
* Process file content

**Redirect**:

* URL redirection routes
* Forward requests to other endpoints
* Handle legacy URLs

**Health**:

* Health check endpoints
* Monitor service status
* Return system health information

## HTTP Methods

**POST** (Blue badge):

* Create new resources
* Submit data
* Trigger actions

**GET** (Green badge):

* Retrieve data
* Read resources
* Query information

**PUT**:

* Update entire resources
* Replace data

**PATCH**:

* Partial updates
* Modify specific fields

**DELETE**:

* Remove resources
* Delete data

## Route Priority

**How Priority Works**:

* Lower number = Higher priority
* Routes are matched in priority order
* First matching route handles the request

**Priority Guidelines**:

* 1-3: Critical routes (webhooks, authentication)
* 4-6: Standard API routes
* 7-9: Utility routes (redirects, static files)
* 10+: Health checks, monitoring

## Managing Routes

### Enabling/Disabling Routes

To change route status:

1. Edit the route
2. Check/uncheck the **Enabled** checkbox
3. Save changes

**Enabled**: Route is active and accepting requests **Disabled**: Route is not available

### Testing Routes

To test a route:

1. Use API testing tools (Postman, curl)
2. Send requests to the route path
3. Verify response and behavior
4. Check logs for errors

**Example curl command**:

```bash
curl -X POST https://ai.kaisar.io/webhook/discord/12345 \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from Discord"}'
```

### Monitoring Route Performance

**Metrics to Track**:

* Total requests
* Average response time
* Error rate
* Success rate

**Performance Optimization**:

* Set appropriate timeouts
* Configure retry logic
* Implement caching
* Use rate limiting

### Deleting a Route

To remove a route:

1. Navigate to route details or list
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] Deleting a route will break any integrations using it. Make sure to update external services before deleting.

## Security Best Practices

**Authentication**:

* Enable authentication for sensitive routes
* Use API keys or tokens
* Validate credentials on every request

**Rate Limiting**:

* Protect against abuse
* Prevent DDoS attacks
* Set reasonable limits

**Input Validation**:

* Validate all input data
* Sanitize user input
* Reject malformed requests

**Error Handling**:

* Don't expose sensitive information in errors
* Log errors securely
* Return appropriate status codes

## Rate Limiting Configuration

**Per Minute Limits**:

* For high-frequency endpoints
* Quick burst protection
* Example: 100 requests/minute

**Per Hour Limits**:

* For moderate usage
* Sustained traffic control
* Example: 2000 requests/hour

**Per Day Limits**:

* For overall usage caps
* Prevent excessive usage
* Example: 10000 requests/day

**Burst Limits**:

* Allow temporary spikes
* Handle sudden traffic
* Example: 10 concurrent requests

## Troubleshooting

**Route Not Responding**:

* Check if route is enabled
* Verify path pattern
* Check authentication settings
* Review error logs

**Timeout Errors**:

* Increase timeout value
* Optimize agent processing
* Check external dependencies
* Review retry settings

**Rate Limit Exceeded**:

* Adjust rate limits
* Implement request queuing
* Contact administrator
* Review usage patterns

**Authentication Failures**:

* Verify credentials
* Check authentication settings
* Review API keys
* Update tokens if expired

## Next Steps

* Configure [Instructions](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/instructions) for route handlers
* Enable [Tools](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/tools) for route processing
* Set up [Platform Connections](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/platform-connections) for webhooks
* Link routes to agents in [Organization → Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents)
