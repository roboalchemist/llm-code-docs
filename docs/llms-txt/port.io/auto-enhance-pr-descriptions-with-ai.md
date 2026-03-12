# Source: https://docs.port.io/guides/all/auto-enhance-pr-descriptions-with-ai.md

# Auto-enhance PR descriptions with AI

This guide demonstrates how to automatically enhance GitHub pull request descriptions using Port's AI agents and coding assistants. When a PR is created with a minimal or empty description, a Port AI agent intelligently gathers **business context and organizational knowledge** from your software catalog that coding agents can't access on their own - like Jira requirements, service architecture, team ownership, and PR templates. Port then passes this enriched context to a coding agent to generate a comprehensive, context-aware PR description.

This guide supports multiple AI coding agents:

* Claude Code
* GitHub Copilot
* Google Gemini

AI-powered coding assistant by Anthropic follow the [â Setup guide](/guides/all/trigger-claude-code-from-port.md)

GitHub's native AI coding assistant follow the [â Setup guide](/guides/all/trigger-github-copilot-from-port.md)

Google's AI coding assistant follow the [â Setup guide](/guides/all/trigger-gemini-assistant-from-port.md)

<br />

![](/img/ai-agents/improvePRDescriptionRM.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Template compliance**: Automatically generate descriptions that match organization-specific PR templates.
* **Business context integration**: Link PRs to related Jira/Linear issues and pull business requirements.
* **Architectural context**: Explain how changes fit into broader system architecture with service dependencies.
* **Change impact analysis**: Describe what problems the PR solves and potential impacts on the system.
* **Review guidance**: Provide context specifically helpful for human and AI code reviewers.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before starting this guide, ensure you have:

* A Port account with the [onboarding process](https://docs.port.io/getting-started/overview) completed
* [Port's GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) installed in your account
* Access to [create and configure AI agents](/ai-interfaces/ai-agents/overview.md) in Port
* Completed one of the above coding agents guides

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

We'll create a PR Template blueprint to store your organization's PR templates and configure the GitHub integration to ingest these templates from your repositories.

### Create PR template blueprint[â](#create-pr-template-blueprint "Direct link to Create PR template blueprint")

This blueprint will store your organization's pull request templates.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Copy and paste the following JSON schema:

   **PR Template blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "prTemplate",
     "title": "PR Template",
     "icon": "GitPullRequest",
     "schema": {
       "properties": {
         "content": {
           "title": "Template Content",
           "type": "string",
           "format": "markdown",
           "description": "The PR template content in markdown format"
         },
         "repository": {
           "title": "Repository",
           "type": "string",
           "description": "Repository where this template is defined"
         },
         "path": {
           "title": "File Path",
           "type": "string",
           "description": "Path to the template file in the repository"
         }
       },
       "required": ["content"]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

5. Click `Create` to save the blueprint.

### Update pull request blueprint[â](#update-pull-request-blueprint "Direct link to Update pull request blueprint")

Now we'll add a relation from the pull request blueprint to the PR template blueprint.This relation will allow us to link PRs to their templates and have a broader context lake through the related tickets, issues, etc linked to the PR.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page.

2. Find and click on your `Pull Request` blueprint (usually named `githubPullRequest`).

3. Click on `{...} Edit JSON`.

4. Add the following relation to the `relations` section:

   **PR Template relation (Click to expand)**

   ```
   "prTemplate": {
     "title": "PR Template",
     "target": "prTemplate",
     "required": false,
     "many": false
   }
   ```

5. Click `Save` to update the blueprint.

### Configure GitHub integration to ingest PR templates[â](#configure-github-integration-to-ingest-pr-templates "Direct link to Configure GitHub integration to ingest PR templates")

Now we'll configure the GitHub integration to ingest PR template files from your repositories.

1. Go to the [Data sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Find your GitHub integration and click on it.

3. Go to the `Mapping` tab.

4. Add the following YAML configuration to ingest PR template files:

   **GitHub PR template mapping (Click to expand)**

   ```
   - kind: file
     selector:
       query: "true"
       files:
         - path: ".github/pull_request_template.md"
     port:
       entity:
         mappings:
           identifier: .repo.name + "-pr-template"
           title: .repo.name + " PR Template"
           blueprint: '"prTemplate"'
           properties:
             content: .file.content
             repository: .repo.name
             path: .file.path
   ```

   Alternative template paths

   If your organization uses different PR template paths, you can modify the `files.path` configuration:

   * Multiple templates: `- path: ".github/PULL_REQUEST_TEMPLATE/*.md"`
   * Docs folder: `- path: "docs/pull_request_template.md"`
   * Root level: `- path: "pull_request_template.md"`

5. Click `Save` to update the integration configuration.

6. Wait for the integration to re-sync, or manually trigger a resync. Your PR templates will appear in the catalog under the `PR Template` blueprint.

   ![](/img/ai-agents/PRTemplateIngested.png) ![](/img/ai-agents/PRTemplateSampleDetail.png)

### Update pull request integration mapping[â](#update-pull-request-integration-mapping "Direct link to Update pull request integration mapping")

Update the GitHub pull request mapping to connect PRs to their templates and optionally to Jira issues for business context.

1. In the same GitHub integration mapping, locate the `pull-request` kind section.

2. Add the `prTemplate` relation and optional `jiraIssue` relation to the `relations` section:

   **Updated pull request mapping (Click to expand)**

   ```
   - kind: pull-request
     selector:
       query: "true"
     port:
       entity:
         mappings:
           identifier: .id|tostring
           title: .title
           blueprint: '"githubPullRequest"'
           properties:
             status: .status
             prNumber: .number
             ... other properties ...
           relations:
             prTemplate: .head.repo.name + "-pr-template"
             jiraIssue: .title | match("[A-Z]+-[0-9]+") .string
   ```

   Business context integration

   The `jiraIssue` relation is optional and extracts Jira issue keys from PR titles (e.g., "JIRA-1234: Add caching layer"). This enables the automation to pull business requirements and acceptance criteria from Jira issues.

   This is very helpful since it gives us a full picture of project, issues and tasks related to the pull request, enriching the context of the description with the **what** and **why** of the changes.

   This business context is invisible to coding agents but crucial for reviewers. It explains *why* the code changes matter and *what* business problem they solve.

   * If you haven't already installed [Port's Jira integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md), you can do so now.
   * Follow a convention of including Jira keys in PR titles (e.g., "PROJ-1234: Add user authentication")
   * See the [Connect GitHub PR with Jira Issue guide](/guides/all/connect-github-pr-with-jira-issue.md) for detailed setup

3. Click `Save` to update the configuration.

## Create the PR Enhancement AI agent[â](#create-the-pr-enhancement-ai-agent "Direct link to Create the PR Enhancement AI agent")

Now we'll create an AI agent that monitors for new PRs, intelligently gathers context from your software catalog, and triggers your chosen coding agent to enhance empty PR descriptions.

1. Go to the [AI Agents](https://app.getport.io/_ai_agents) page of your portal.

2. Click on `+ AI Agent`.

3. Toggle `Json mode` on.

4. Copy and paste the following JSON configuration:

   **PR Enhancement AI agent configuration (Click to expand)**

   ```
   {
     "identifier": "pr_description_enhancement_agent",
     "title": "PR Description Enhancement Agent",
     "icon": "GitPullRequest",
     "properties": {
       "description": "Analyzes pull requests and enhances descriptions with template-compliant, context-rich content",
       "status": "active",
       "prompt": "You are a PR enhancement assistant that enriches PR descriptions with business context from Port's software catalog.\n\nWhen a new PR is created:\n\n1. Check if the PR description is empty, minimal (< 50 chars), or just an untouched template\n\n2. If enhancement is needed, use Port AI tools to gather BUSINESS CONTEXT that coding agents can't access:\n   - The PR template from the catalog (organizational standards)\n   - Linked Jira/Linear issues with user stories and acceptance criteria (business requirements)\n   - Service/application information: purpose, team ownership, dependencies (organizational knowledge)\n   - Related architectural decisions or documentation (context)\n\n3. Call the appropriate coding agent action with a comprehensive prompt that includes:\n   - All the business context you gathered from Port\n   - Clear instructions: 'Analyze the code changes in this PR and combine them with the following business context from our software catalog...'\n   - Request a description that explains BOTH what changed technically AND why it matters to the business\n   - Follow the PR template structure\n   - Emphasize that reviewers need both technical and business understanding\n\nBe intelligent about which coding agent action to call based on what's available in the tools list. use claude code preferably to prevent openining a new issue with descriptions which needs manual copying into the pr that needs modification in it's description, use claude code so that you can work on the same PR.",
       "execution_mode": "Automatic",
       "conversation_starters": [],
       "tools": [
         "^(list|search)_.*",
         "run_trigger_claude_code",
         "run_assign_to_copilot",
         "run_trigger_gemini_assistant"
       ]
     },
     "relations": {}
   }
   ```

   Customize the agent prompt and tools

   You can customize the agent's behavior by modifying the `prompt` field:

   * Add specific requirements for your team's PR standards.

   * Emphasize security, performance, or testing considerations.

   Only include the coding agent tools you've actually configured - remove any unused tools from the list (e.g., if you only set up Claude Code, remove the Copilot and Gemini tools).

5. Click `Create` to save the agent.

## Create automation to trigger the agent[â](#create-automation-to-trigger-the-agent "Direct link to Create automation to trigger the agent")

Now create an automation that triggers the AI agent whenever a new PR is created:

1. Go to the [Automations](https://app.getport.io/settings/automations) page of your portal.

2. Click on `+ Automation`.

3. Copy and paste the following JSON configuration:

   **Trigger PR Enhancement Agent automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "trigger_pr_description_enhancement_agent",
     "title": "Trigger PR Description Enhancement Agent",
     "description": "Automatically triggers the PR enhancement AI agent when a new PR is created",
     "icon": "GitPullRequest",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_CREATED",
         "blueprintIdentifier": "githubPullRequest"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.after.properties.status == \"open\""
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.port.io/v1/agent/pr_description_enhancement_agent/invoke",
       "agent": false,
       "synchronized": false,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json"
       },
       "body": {
         "prompt": "Analyze PR #{{ .event.diff.after.properties.prNumber }} in repository {{ .event.diff.after.properties.link | split(\"/\") | .[3] + \"/\" + .[4] }}. Title: '{{ .event.diff.after.title }}'. Check if the description needs enhancement and if so, gather context and trigger the coding agent to enhance it.",
         "labels": {
           "source": "automation",
           "pr_number": "{{ .event.diff.after.properties.prNumber | tostring }}",
           "repository": "{{ .event.diff.after.properties.link | split(\"/\") | .[3] + \"/\" + .[4] }}"
         }
       }
     },
     "publish": true
   }
   ```

4. Click `Create` to save the automation.

## How it works[â](#how-it-works "Direct link to How it works")

This Port-native approach combines organizational knowledge with code analysis:

1. **PR Created** â When a new PR is synced to Port, the automation triggers.

2. **AI Agent Analyzes** â The agent checks if the description needs enhancement.

3. **Port Gathers Business Context** â Uses Port AI to intelligently gather context that coding agents can't access:

   <!-- -->

   * **PR template** from your catalog (organizational standards)
   * **Business requirements** from linked Jira/Linear issues (user stories, acceptance criteria)
   * **Service context** including architecture, dependencies, and ownership
   * **Team information** and related projects from your software catalog

4. **Triggers Coding Agent with Context** â Calls your configured coding agent action with Port's enriched context.

5. **Coding Agent Analyzes Code** â The coding agent examines the actual code changes in the PR.

6. **Description Enhanced** â Combines Port's business context with code analysis to create a comprehensive, context-aware PR description.

Port's unique value

**What Port provides:** Business requirements, organizational context, service architecture, team ownership - information that exists in your software catalog but isn't visible to coding agents working directly with code repositories.

**What the coding agent provides:** Technical code analysis, implementation details, file changes - information derived from examining the actual code diff.

**Together:** A PR description that explains both *what* changed in the code AND *why* it matters to the business.

## Example workflow[â](#example-workflow "Direct link to Example workflow")

Here's what happens when a PR is created in your repository:

* Claude Code
* GitHub Copilot
* Google Gemini

If you completed the [Trigger Claude Code from Port guide](/guides/all/trigger-claude-code-from-port.md), the agent will:

1. **Port gathers context**: Fetches PR template, linked Jira requirements, service architecture, and team information from your catalog.

2. **Triggers Claude Code**: Calls the `trigger_claude_code` action with a prompt containing all the business context from Port.

3. **Claude analyzes code**: Checks out the PR branch, examines file changes, and understands technical implementation.

4. **Creates enriched description**: Combines Port's business context with code analysis to generate a comprehensive description.

5. **Updates PR**: Posts the enhanced description directly via GitHub API.

If you completed the [Trigger GitHub Copilot from Port guide](/guides/all/trigger-github-copilot-from-port.md), the agent will:

1. **Port gathers context**: Fetches PR template, linked Jira requirements, service architecture, and team information from your catalog.

2. **Creates GitHub issue**: Calls the `assign_to_copilot` action to create an issue containing all the business context from Port.

3. **Copilot assignment**: Issue is automatically assigned to GitHub Copilot (via `auto_assign` label).

4. **Copilot analyzes**: Examines the code changes in the PR and reads the business context from the issue.

5. **Creates enriched description**: Combines Port's business context with code analysis and updates the PR description.

If you completed the [Trigger Gemini Assistant from Port guide](/guides/all/trigger-gemini-assistant-from-port.md), the agent will:

1. **Port gathers context**: Fetches PR template, linked Jira requirements, service architecture, and team information from your catalog.

2. **Triggers Gemini**: Calls the `trigger_gemini_assistant` action with a prompt containing all the business context from Port.

3. **Gemini analyzes code**: Checks out the PR branch, examines file changes, and understands technical implementation.

4. **Creates enriched description**: Combines Port's business context with code analysis to generate a comprehensive description.

5. **Updates PR**: Posts the enhanced description directly via GitHub API.

### Pull Request Context Lake

When a PR is created, it is linked to its template, Jira issues, and other related entities in your software catalog. This creates a context lake that can be used to enrich the PR description.

![](/img/ai-agents/PRContextLake.png)

## Test the setup[â](#test-the-setup "Direct link to Test the setup")

Now let's test the complete setup and see how Port enriches PR descriptions with business context.

1. In a repository integrated with Port, create a new pull request with a minimal description (e.g., "WIP").

2. The PR will sync to Port as a `githubPullRequest` entity.

3. Go to the [AI Agents](https://app.getport.io/_ai_agents) page and find the `PR Description Enhancement Agent`.

4. Check the agent's conversation history to see its analysis and actions.

5. Refresh your GitHub PR - the description should now be enhanced with both business context and technical details.

### Before Enhancement

The PR starts with just an empty template - no business context, no explanation of what the code does or why it matters.

![](/img/ai-agents/PRDescriptionRAWPRTemplate.png)

### During Enhancement: Port Gathers Business Context

Port's AI agent analyzes the PR and gathers organizational context that the coding agent can't access directly. Notice how Port identifies:

* **Repository Context**: Understanding that this is the `port-product-experiments` repository for internal tools (not an e-commerce backend as the PR title might suggest)
* **Missing Context Issues**: Identifying what business information is needed
* **Template Compliance**: Noting that the PR doesn't follow the established template
* **Enhancement Requirements**: Specifying what context should be added based on organizational knowledge

This business context is what makes the final description meaningful - it's not just about the code changes, but about how they fit into Port's product strategy and internal tooling.

![](/img/ai-agents/AIInvocationOnDescriptionFillWIP.png)

### After Enhancement: Business Context + Code Analysis

The enhanced PR description now combines:

**From Port (Business Context):**

* Clear explanation of the business purpose: "enabling the creation of new product entries in the product catalog"
* Organizational context: "experimental e-commerce application within Port's product team experimentation repository"
* How it fits with existing tools: "complementing the existing GET /products endpoints"
* Why this matters: "part of an experimental e-commerce backend built with FastAPI, designed to demonstrate API development patterns"

**From the Coding Agent (Technical Analysis):**

* Technical implementation details of the endpoint
* Code structure and patterns used
* File changes and specific functions added
* Validation and model information

Together, this creates a complete picture for reviewers who need to understand both the business rationale AND the technical implementation.

![](/img/ai-agents/PRTemplateEnhanced.png) ![](/img/ai-agents/PRTemplateEnhanced2.png)

Notice the difference

Without Port, a coding agent would only see the code changes and might incorrectly assume this is a production e-commerce feature. Port's catalog knowledge adds the crucial context that this is an internal experimentation tool, changing how reviewers approach the PR.

## Related guides[â](#related-guides "Direct link to Related guides")

* [Trigger Claude Code from Port](/guides/all/trigger-claude-code-from-port.md)
* [Trigger GitHub Copilot from Port](/guides/all/trigger-github-copilot-from-port.md)
* [Trigger Gemini Assistant from Port](/guides/all/trigger-gemini-assistant-from-port.md)
* [Enrich pull requests using AI](/guides/all/setup-pr-enricher-ai-agent.md)
* [Track AI-driven pull requests](/guides/all/track-ai-driven-pull-requests.md)
* [Connect GitHub PR with Jira Issue](/guides/all/connect-github-pr-with-jira-issue.md)
