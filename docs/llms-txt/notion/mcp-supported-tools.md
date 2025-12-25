# Supported tools

Learn what you can do with Notion MCP tools.

[![Image 1](https://notionapi.readme.io/_next/static/media/readme-logo.a2e6183b.svg)](https://readme.com/?ref_src=hub&project=notionapi)

Now that you have installed the Notion MCP, let's explore how AI assistants can use Notion MCP tools to create, search, and manage content in your Notion workspace.

These tools work seamlessly together through prompts, and their real power comes from combining them. With a single prompt, you can search your workspace, create new pages from the results, and update properties across multiple pages. Understanding these building blocks helps you craft efficient prompts that tackle complex tasks by combining multiple tools.

| Name | Description | Sample prompt |
| --- | --- | --- |
| `notion-search` | Search across your Notion workspace and connected tools like Slack, Google Drive, and Jira. Falls back to basic workspace search if AI features aren’t available. | • "Check slack for how we have solved this bug in the past"<br>• "Search for documents mentioning 'budget approval process'<br>• Look for meeting notes from last week with John<br>• Find all project pages that mention 'ready for dev’" |
| `notion-fetch` | Retrieves content from a Notion page or database by its URL | • "What are the product requirements still need to be implemented from this ticket <code>https://notion.so/page-url</code>?<br> |
| `notion-create-pages` | Creates one or more Notion pages with specified properties and content. If a parent is not specified, a private page will be created. | • "Create a project kickoff page under our Projects folder with agenda and team info"<br>• Make a new employee onboarding checklist in our HR database<br>• Create a meeting notes page for today's standup with action items<br>• Add a new product feature request to our feature database" |
| `notion-update-page` | Update a Notion page's properties or content. | • "Change the status of this task from 'In Progress' to 'Complete'"<br>• Add a new section about risks to the project plan page<br>• Update the due date on this project to next Friday<br>• Replace the old project timeline with the updated version" |
| `notion-move-pages` | Move one or more Notion pages or databases to a new parent. | "Move my weekly meeting notes page to the 'Team Meetings' page"<br>• Reorganize all project documents under the 'Active Projects' section |
| `notion-duplicate-page` | Duplicate a Notion page within your workspace. This action is completed async. | "Duplicate my project template page so I can use it for the new Q3 initiative"<br>• Make a copy of the meeting agenda template for next week's planning session |
| `notion-create-database` | Creates a new Notion database, initial data source, and initial view with the specified properties. | "Create a new database to track our customer feedback with fields for customer name, feedback type, priority, and status"<br>• Set up a content calendar database with columns for publish date, content type, and approval status |
| `notion-update-database` | Update a Notion data source's properties, name, description, or other attributes. | • Add a status field to track project completion<br>• Update the task database to include priority levels |
| `notion-create-comment` | Add a comment to a page<br><em>Note: block-level comments and discussions within a page are not yet supported</em>. | • Add a feedback comment to this design proposal<br>• Leave a note on the quarterly review page about budget concerns<br>• Comment on the meeting notes to clarify the action item deadlines<br>• Add my thoughts to the product roadmap discussion" |
| `notion-get-comments` | Lists all comments on a specific page, including threaded discussions. | • List comments on the project requirements section<br>• Get all feedback comments from last week's review |
| `notion-get-teams` | Retrieves a list of teams (teamspaces) in the current workspace. | • Search for teams by name, and your membership status in each team<br>• Get a team's ID to use as a filter for a search |
| `notion-get-users` | Lists all users in the workspace with their details. | • "Get contact details for the user who created this page"<br>• Look up the profile of the person assigned to this task" |
| `notion-get-user` | Retrieve your user information by ID | • "What's my email address?"<br>• "What’s my Notion user ID?" |
| `notion-get-self` | Retrieves information about your own bot user and the Notion workspace you’re connected to. | • "Which Notion workspace am I currently connected to?"<br>• "What's my file size upload limit for the current workspace?" |

> Tool names may vary for OpenAI
>
> When connecting with an OpenAI MCP client (e.g., ChatGPT), the `notion-` prefix is automatically omitted from the `notion-fetch` and `notion-create-pages` commands.
```

# Using Notion MCP Tools

Notion MCP offers a suite of AI-assisted tools that can help you create, search, and manage content in your Notion workspace. These tools work seamlessly together through prompts, allowing you to craft efficient prompts that tackle complex tasks by combining multiple tools.

| Name | Description | Sample prompt |
| --- | --- | --- |
| `notion-search` | Search across your Notion workspace and connected tools like Slack, Google Drive, and Jira. Falls back to basic workspace search if AI features aren’t available. | - "Check slack for how we have solved this bug in the past"<br>- "Search for documents mentioning 'budget approval process'"<br>- "Look for meeting notes from last week with John"<br>- "Find all project pages that mention 'ready for dev'” |
| `notion-fetch` | Retrieves content from a Notion page or database by its URL | - “What are the product requirements still need to be implemented from this ticket [https://notion.so/page-url](https://notion.so/page-url)”? |
| `notion-create-pages` | Creates one or more Notion pages with specified properties and content. If a parent is not specified, a private page will be created. | - "Create a project kickoff page under our Projects folder with agenda and team info"<br>- "Make a new employee onboarding checklist in our HR database"<br>- "Create a meeting notes page for today's standup with action items"<br>- "Add a new product feature request to our feature database” |
| `notion-update-page` | Update a Notion page's properties or content. | - "Change the status of this task from 'In Progress' to 'Complete'"<br>- "Add a new section about risks to the project plan page"<br>- "Update the due date on this project to next Friday"<br>- "Replace the old project timeline with the updated version” |
| `notion-move-pages` | Move one or more Notion pages or databases to a new parent. | - "Move my weekly meeting notes page to the 'Team Meetings' page"<br>- "Reorganize all project documents under the 'Active Projects' section" |
| `notion-duplicate-page` | Duplicate a Notion page within your workspace. This action is completed async. | - "Duplicate my project template page so I can use it for the new Q3 initiative"<br>- "Make a copy of the meeting agenda template for next week's planning session" |
| `notion-create-database` | Creates a new Notion database, initial data source, and initial view with the specified properties. | - "Create a new database to track our customer feedback with fields for customer name, feedback type, priority, and status"<br>- "Set up a content calendar database with columns for publish date, content type, and approval status" |
| `notion-update-database` | Update a Notion data source's properties, name, description, or other attributes. | - "Add a status field to track project completion"<br>- "Update the task database to include priority levels" |
| `notion-create-comment` | Add a comment to a page.<br><em>Note: block-level comments and discussions within a page are not yet supported</em>. | - "Add a feedback comment to this design proposal"<br>- "Leave a note on the quarterly review page about budget concerns"<br>- "Comment on the meeting notes to clarify the action item deadlines"<br>- "Add my thoughts to the product roadmap discussion” |
| `notion-get-comments` | Lists all comments on a specific page, including threaded discussions. | - List comments on the project requirements section<br>- Get all feedback comments from last week's review |
| `notion-get-teams` | Retrieves a list of teams (teamspaces) in the current workspace. | - Search for teams by name, and your membership status in each team<br>- Get a team's ID to use as a filter for a search |
| `notion-get-users` | Lists all users in the workspace with their details. | - "Get contact details for the user who created this page"<br>- "Look up the profile of the person assigned to this task” |
| `notion-get-user` | Retrieve your user information by ID | - "What's my email address?"<br>- ”What’s my Notion user ID?” |
| `notion-get-self` | Retrieves information about your own bot user and the Notion workspace you’re connected to. | - “Which Notion workspace am I currently connected to?”<br>- ”What's my file size upload limit for the current workspace?” |

> Tool names may vary for OpenAI
> 
> When connecting with an OpenAI MCP client (e.g., ChatGPT), the `notion-` prefix is automatically omitted from the `notion-fetch` and `notion-search` tools, making them appear as `fetch` and `search`, respectively. This is because these specific tool names are required as part of the [Deep Research specification](https://platform.openai.com/docs/guides/deep-research#remote-mcp-servers) for remote MCP servers.

## Rate limits

Standard [API request limits](/reference/request-limits) apply per user's usage of Notion MCP (totaled across all tool calls). Currently, this is an average of **180 requests per minute** (3 requests per second).

Some MCP tools have additional, tool-specific rate limits that are stricter. These are subject to change over time, but the current values are listed below for reference:

- **Search**: 30 requests per minute

### Examples

To illustrate the above limitations, you'll experience rate limit errors in your MCP client of choice in any of the following example scenarios (assuming we take the average rate over a large enough time window):

- 35 searches per minute (exceeds search-specific limit)
- 12 searches & 170 fetches per minute (exceeds general 180 requests/min limit)
- 185 fetches per second (exceeds general 180 requests/min limit)

### What to do if you're rate-limited

In most cases, the time it takes to do a complex AI-powered search across Notion and your connected tools means that sequential searches will typically stay under the rate limit. In general, if you encounter rate limit errors, prompt your LLM tool to reduce the amount of parallel searches or operations performed using Notion MCP, and/or try again later.

---

Updated about 2 months ago

---

## What’s Next

- [Security best practices](/docs/mcp-security-best-practices)
```