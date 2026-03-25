# Source: https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops

Title: Enable AI assistance with the Azure DevOps MCP Server - Azure Boards

URL Source: https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops

Markdown Content:
**Azure DevOps Services**

Consider asking your AI assistant "Get my current sprint work items, then identify which ones might be at risk" and getting instant access to your actual Azure DevOps data. The Azure DevOps Model Context Protocol (MCP) Server provides your AI assistant with secure access to work items, pull requests, builds, test plans, and documentation from your Azure DevOps organization.

Unlike cloud-based solutions that require sending your data externally, the Azure DevOps MCP Server runs locally within your secure environment, ensuring your sensitive project information never leaves your network while still delivering enterprise-grade AI capabilities.

Important

*   The Azure DevOps MCP Server is free to use. However, standard Azure DevOps pricing applies to your organization and any data access through the service. AI assistant usage might have separate costs depending on your chosen AI platform.
*   The Azure DevOps MCP Server requires your AI assistant to operate in agent-mode to access Azure DevOps data and perform operations.

**System requirements:**[Node.js 20.0+](https://nodejs.org/) and an active [Azure DevOps organization](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/create-organization?view=azure-devops)

The Azure DevOps MCP Server integrates with various development environments and AI assistants. Choose your preferred environment for instructions. The prerequisites listed in the table are environment-specific requirements in addition to the system requirements previously listed.

| Environment | Prerequisites | Installation | Features |
| --- | --- | --- | --- |
| **Visual Studio Code (recommended)** | [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) or [Claude Dev](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) extension | [**One-click install**](https://insiders.vscode.dev/redirect/mcp/install?name=ado&config=%7B%20%22type%22%3A%20%22stdio%22%2C%20%22command%22%3A%20%22npx%22%2C%20%22args%22%3A%20%5B%22-y%22%2C%20%22%40azure-devops%2Fmcp%22%2C%20%22%24%7Binput%3Aado_org%7D%22%5D%7D&inputs=%5B%7B%22id%22%3A%20%22ado_org%22%2C%20%22type%22%3A%20%22promptString%22%2C%20%22description%22%3A%20%22Azure%20DevOps%20organization%20name%20%20%28e.g.%20%27contoso%27%29%22%7D%5D) | Extensive MCP support with multiple AI assistant options |
| **Visual Studio (2022 and later)** | [GitHub Copilot component](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-install-and-states) | [Visual Studio setup guide](https://github.com/microsoft/azure-devops-mcp/blob/main/README.md#visual-studio) | Full IntelliSense integration with Azure DevOps data |
| **Cursor** | Built-in AI assistant (no extensions needed) | [Cursor setup guide](https://github.com/microsoft/azure-devops-mcp/blob/main/README.md#cursor) | Native MCP integration |
| **Claude Desktop** | Claude Desktop application | [Claude Desktop setup guide](https://github.com/microsoft/azure-devops-mcp/blob/main/README.md#claude-desktop) | Standalone application with full Azure DevOps integration |
| **JetBrains IDEs** | Compatible AI assistant plugin | [JetBrains setup guide](https://github.com/microsoft/azure-devops-mcp/blob/main/README.md#jetbrains) | IDE-specific integration via plugins |
| **Other environments** | Varies by environment | [Azure DevOps MCP Server docs repository](https://github.com/microsoft/azure-devops-mcp) | See repository for all options |

Traditional AI assistants lack context about your specific projects, work items, and team processes. They can help with generic coding questions but can't answer "What's blocking our current sprint?" or "Which pull requests need my review?" The Azure DevOps MCP Server bridges this gap by connecting your AI assistant directly to your Azure DevOps data.

The Azure DevOps MCP Server provides contextual intelligence based on your actual project data, not generic responses. You can ask natural language questions about your work items, sprints, and releases, and receive insights that understand your team's specific processes and terminology. This process eliminates context switching between tools, provides instant answers without navigating through the Azure DevOps web interface, and automates routine project management tasks through natural language.

The Azure DevOps MCP Server prioritizes data security and privacy:

*   **Local execution**: No data leaves your environment - everything runs locally within your secure network
*   **No external API calls**: The server doesn't make external API calls that could expose sensitive project information
*   **User control**: You maintain full control over what data your AI assistant can access
*   **Secure integration**: Works seamlessly with your existing AI coding environments without compromising security
*   **Private data handling**: Your sensitive project information never leaves your network while still delivering enterprise-grade AI capabilities

The Azure DevOps MCP Server enables a two-step process: **data retrieval** and **AI analysis**.

The server provides secure access to your Azure DevOps data:

*   **Projects and teams**: Organization structure and team information
*   **Work items**: Assigned tasks, bugs, user stories, and their details
*   **Pull requests**: Code review status, changes, and linked work items
*   **Builds and pipelines**: CI/CD status, test results, and deployment information
*   **Test plans**: Test cases, results, and coverage data

Your AI assistant processes this data to provide:

*   **Intelligent summaries**: Sprint progress, team velocity, and project health
*   **Actionable insights**: Risk identification, bottleneck analysis, and recommendations
*   **Context-aware responses**: Answers that understand your specific projects and processes

**Example**: You ask "What's blocking our sprint?" → MCP Server retrieves your current work items → Your AI assistant analyzes the data and identifies specific blockers with recommendations.

For more examples, see [Example usage](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/EXAMPLES.md).

Tip

To avoid using stale or cached data from previous queries, add to your prompt, "Do not use previously fetched data."

**Component**

**Description**

* * *

**MCP Server provides**

Access to your assigned work items and recent updates

* * *

**AI assistant action**

Analyzes the data to help you prepare for standup

* * *

**Example prompt**

"Get my work items for project MyProject and help me prepare for standup - what did I complete, what am I working on, and what's blocked?"

* * *

**Query translation**

WIQL query to retrieve your assigned work items, filtered by project and excluding removed items, ordered by most recent changes

* * *

**Raw data result**

Six work items including bugs, tasks, user stories, and features with their current states (Resolved, Done, Active, New, Blocked)

* * *

**AI assistant output**

| Status | Work Items |
| --- | --- |
| ✅ **Completed** | Bug #4521: "Sign in page crashes on mobile Safari" - Resolved yesterday Task #4498: "Update API documentation for v2.1" - Completed 2 days ago |
| 🔄 **In Progress** | User Story #4456: "Implement two-factor authentication" - In Progress (three days) └── Subtasks: Database schema (Done), UI components (In Progress), Testing (Not Started) Bug #4534: "Performance issue with large datasets" - Active (one day) |
| ⚠️ **Blocked** | Feature #4423: "Integration with external payment gateway" - Blocked └── Waiting for: Security team approval (blocked five days) └── Action needed: Follow up with Sarah from InfoSec team Task #4467: "Deploy to staging environment" - Impediment └── Issue: Staging server maintenance scheduled today 2-4 PM |
| **Summary for standup** | - Yesterday: Resolved mobile Safari sign-in issue, completed API docs. - Today: Continue 2FA implementation, investigate dataset performance issue. - Blockers: Need security approval for payment integration, staging deployment delayed due to maintenance. |

* * *

**Component**

**Description**

* * *

**MCP Server provides**

Access to backlog items, team data, and work item details

* * *

**AI assistant action**

Helps analyze capacity and plan the sprint

* * *

**Example prompt**

"Get all work items in the product backlog for MyProject and prioritize them for a two-week sprint with three developers"

* * *

**Query translation**

WIQL query to retrieve backlog items with story points, priority, and state information, ordered by priority and stack rank

* * *

**Raw data result**

Nine backlog items including epics, features, user stories, bugs, and tasks with story points and dependencies, plus team metrics (three developers, 14-day sprint, 60-point velocity)

* * *

**AI assistant output**

| Category | Work Items | Points |
| --- | --- | --- |
| ✅ **Recommended** | Epic #3401: "User Profile Enhancement" - High business value, no dependencies Bug #3456: "Search results time out on large datasets" - Critical user impact Feature #3378: "Export dashboard to PDF" - Frequently requested Story #3489: "Implement password reset flow" - Security priority Task #3512: "Upgrade React components to v18" - Technical debt Story #3467: "Add dark mode toggle" - Quick win | **60 total** (13 + 8 + 13 + 8 + 13 + 5) |
| ⏳ **Deferred** | Epic #3234: "Mobile app rewrite" - Too large for single sprint Feature #3445: "AI-powered recommendations" - Waiting for data science team Story #3523: "Integration with external CRM" - Blocked by vendor API | 34, 21, 13 |
| **Planning recommendations** | - **Balance**: Mix of features (3), bugs (1), technical debt (1), quick wins (1) - **Risk level**: Low-medium risk items for predictable delivery - **Dependencies**: All selected items have resolved dependencies - **Skills**: Work distribution matches current team expertise - **Business value**: Prioritized customer-facing features and critical fixes |  |

* * *

**Component**

**Description**

* * *

**MCP Server provides**

Pull request details and linked work item information

* * *

**AI assistant action**

Provides business context for technical changes

* * *

**Example prompt**

"Get details for pull request #67 and its linked work items and help me understand the business effect of these code changes"

* * *

**API translation**

REST API calls to retrieve pull request details and linked work item information with expanded relations

* * *

**Raw data result**

Pull request #67 (caching layer implementation, eight files changed, +156/-42 lines) and two linked work items (performance user story and settings bug)

* * *

**AI assistant output**

| Component | Details |
| --- | --- |
| **Pull Request** | PR #67: "Implement caching layer for user preferences" Author: Christie Church, Status: Active (awaiting review) Files: 8 changed (+156, -42 lines), Created: Two days ago |
| **Linked Work Items** | 🎯 User Story #2847: "Improve app performance for returning users" (High priority) └── Target: Page load time < 2 seconds for logged-in users 🐛 Bug #2901: "Settings page loads slowly for users with many preferences" (Medium severity) └── Impact: Affects 15% of premium users, causing support tickets |
| **Business impact summary** | - 💼 **Strategic Alignment**: Supports Q3 user retention goal (20% improvement) Addresses premium user experience issues affecting revenue Enables future personalization features - 📊 **Expected Outcomes**: Performance: 60% reduction in preference loading time (2.5s → 1.0s) User Experience: Eliminates loading delays in settings and profile pages Support Impact: Expected 40% reduction in performance-related tickets - 🔍 **Review Focus Areas**: Cache invalidation logic (data consistency) Error handling for cache unavailability Performance monitoring implementation Security considerations for cached user data |

* * *
