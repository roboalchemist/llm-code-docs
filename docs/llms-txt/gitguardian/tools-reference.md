# Source: https://docs.gitguardian.com/platform/agent/tools-reference.md

# Agent tools reference

> :::warning[Alpha]
The GitGuardian Agent is currently in **private alpha**. Features and behavior may change. Contact us at [support@gitguardian.com](mailto:support@gitguardian.com) or reach out to your CSM or account manager to request access.
:::

:::warning[Alpha]
The GitGuardian Agent is currently in **private alpha**. Features and behavior may change. Contact us at [support@gitguardian.com](mailto:support@gitguardian.com) or reach out to your CSM or account manager to request access.
:::

The GitGuardian Agent uses a collection of specialized tools to help you manage secret incidents. Each tool is designed for a specific purpose and operates within your workspace's security context.

## Understanding Agent tools

When you ask the Agent a question or make a request, it automatically selects the appropriate tool(s) to fulfill your needs. You don't need to specify which tool to use - simply describe what you want to accomplish in natural language.

### Tool approval

Some tools that modify your data require your explicit approval before executing. When the Agent needs to perform a write action (such as assigning an incident or updating tags), it will present the action and its parameters for your review. You can then approve or reject the action before it is carried out.

Read-only tools (such as listing incidents or searching documentation) are executed automatically without requiring approval.

## Available tools

| Tool | Description | Approval required |
|------|-------------|:-----------------:|
| [List Incidents](#list-incidents) | Search and filter incidents in your workspace | No |
| [Get Incident](#get-incident) | Get full details for a specific incident | No |
| [List Repo Occurrences](#list-repo-occurrences) | View where a secret appears across repositories | No |
| [List Users](#list-users) | Browse workspace members | No |
| [Get Member](#get-member) | Get details about a specific workspace member | No |
| [List Sources](#list-sources) | View monitored repositories and integrations | No |
| [List Detectors](#list-detectors) | View available secret detectors | No |
| [Read Custom Tags](#read-custom-tags) | View tags applied to an incident | No |
| [Write Custom Tags](#write-custom-tags) | Set custom tags on an incident | Yes |
| [Update Or Create Incident Custom Tags](#update-or-create-incident-custom-tags) | Batch add or update tags across incidents | Yes |
| [Manage Private Incident](#manage-private-incident) | Update incident status or properties | Yes |
| [Assign Incident](#assign-incident) | Assign an incident to a team member | Yes |
| [Get Attack Pattern Guidance](#get-attack-pattern-guidance) | Understand why a secret exposure is risky | No |
| [Get Remediation Plan Guidance](#get-remediation-plan-guidance) | Get a step-by-step remediation plan | No |
| [Search GitGuardian Documentation](#search-gitguardian-documentation) | Search GitGuardian docs and knowledge base | No |

---

## Tool details

### List Incidents

Searches for incidents matching your criteria and returns incident details including status, severity, metadata, detection date, source, and associated tags.

**Example questions:**
- "Show me all open incidents from last week"
- "Find incidents related to AWS credentials"
- "List high-severity incidents assigned to my team"

:::note
By default, the Agent filters out low-severity incidents, false positives, and test files to focus on the most relevant results. You can ask for specific filters to override this behavior.
:::

---

### Get Incident

Fetches comprehensive details for a single incident, including all occurrences and their locations, validity and presence check results, tags, and assignments.

**Example questions:**
- "Tell me more about incident #12345"
- "What's the status of this incident?"
- "Show me the details of the current incident"

---

### List Repo Occurrences

Lists all locations where a secret has been found, including which repositories, branches, and commits are affected. Helps assess the exposure scope of an incident.

**Example questions:**
- "Where does this secret appear in our codebase?"
- "Show me all occurrences for this incident"
- "Which repositories contain this leaked credential?"

---

### List Users

Returns a list of workspace members. Useful for identifying who to assign incidents to.

**Example questions:**
- "Who are the members of my workspace?"
- "List all users"

---

### Get Member

Retrieves detailed information about a specific member of your workspace, such as their role and permissions.

**Example questions:**
- "Show me details about John"
- "What role does Sarah have?"
- "Who is the owner of this workspace?"

---

### List Sources

Shows which repositories and integrations are monitored by GitGuardian in your workspace.

**Example questions:**
- "What sources are being monitored?"
- "Show me the list of connected repositories"

---

### List Detectors

Shows which types of secrets GitGuardian can detect and provides information about detector categories.

**Example questions:**
- "What types of secrets can GitGuardian detect?"
- "Show me available detectors"

---

### Read Custom Tags

Returns the custom tags currently applied to an incident. Useful for understanding how an incident has been categorized before making changes.

**Example questions:**
- "What tags are on this incident?"
- "Show me the tags for incident #12345"
- "Is this incident tagged as high-priority?"

---

### Write Custom Tags

Sets custom tags on a specific incident. Creates new tags if they don't already exist in your workspace.

**Example requests:**
- "Tag this as 'reviewed-by-security-team'"
- "Set the tags to 'production' and 'database-access'"
- "Replace the tags on this incident with 'urgent'"

:::note
This action requires your approval before executing.
:::

---

### Update Or Create Incident Custom Tags

Adds or updates custom tags across one or more incidents. Supports batch operations for organizing multiple incidents at once.

**Example requests:**
- "Add the 'high-priority' tag to all open AWS incidents"
- "Tag these three incidents with 'sprint-42'"
- "Add 'needs-rotation' to all critical incidents from last week"

**Common tagging strategies:**
- **By team**: `frontend-team`, `backend-team`, `infra-team`
- **By project**: `project-alpha`, `payment-service`, `user-auth`
- **By status**: `needs-review`, `in-progress`, `waiting-rotation`
- **By priority**: `urgent`, `high-priority`, `can-wait`

:::note
This action requires your approval before executing.
:::

---

### Manage Private Incident

Updates incident properties such as status through natural language commands. All changes are logged for audit purposes.

**Example requests:**
- "Mark this incident as resolved"
- "Ignore this incident - it's a false positive"
- "Reopen incident #12345"

:::note
This action requires your approval before executing. The Agent will show you the proposed changes for confirmation.
:::

---

### Assign Incident

Assigns one or more incidents to a user in your workspace. Helps distribute remediation work across the team. All assignments are logged for tracking purposes.

**Example requests:**
- "Assign this incident to John"
- "Who can handle this? Assign it to someone from the backend team"
- "Assign all open AWS incidents to me"

:::note
This action requires your approval before executing.
:::

---

### Get Attack Pattern Guidance

Analyzes the type of secret exposed and provides a detailed explanation of potential attack vectors, impact of unauthorized access, risk factors specific to your incident, and references to relevant security resources.

**Example questions:**
- "Why is this AWS key dangerous?"
- "Explain the threat posed by this incident"
- "What could an attacker do with this secret?"

---

### Get Remediation Plan Guidance

Generates a step-by-step remediation plan tailored to a specific incident, including guidance on secret rotation, best practices for secure storage, recommendations for preventing future exposures, and integration suggestions.

**Example questions:**
- "How should I remediate this incident?"
- "Create a remediation plan for this AWS key exposure"
- "What steps should I take to fix this?"

---

### Search GitGuardian Documentation

Searches GitGuardian documentation and knowledge base to find relevant articles, best practice guidance, and product feature information.

**Example questions:**
- "How do I set up Slack notifications?"
- "What is validity checking?"
- "How do Secret Manager integrations work?"

## Tool permissions

The Agent executes all actions using your own permissions. It can only read and modify data that you have access to in the GitGuardian dashboard. If you don't have permission to perform an action manually, the Agent won't be able to do it on your behalf either.

Write actions (such as assigning incidents, updating status, or managing tags) additionally require your explicit approval before the Agent executes them.

## Best practices

### Be specific

The more specific your request, the better the Agent can help:

- "Show me open AWS credential incidents from the last 30 days"
- Avoid: "Show me some incidents"

### Use natural language

You don't need to know technical details - just describe what you need:

- "Help me understand why this database password is risky"
- Avoid: "Execute explain_threat tool with incident_id parameter"

### Review write actions carefully

When the Agent asks for approval on a write action:

- Review the proposed changes and their parameters
- Verify the target incidents are correct, especially for bulk operations
- Reject and clarify if the action doesn't match your intent

## Feedback and improvements

If a tool doesn't work as expected:

1. Rate the response to indicate the issue
2. Provide specific feedback on what went wrong
3. Include details about what you expected

Your feedback helps improve tool accuracy and reliability.
