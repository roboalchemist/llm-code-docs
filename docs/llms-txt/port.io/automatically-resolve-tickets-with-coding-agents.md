# Source: https://docs.port.io/guides/all/automatically-resolve-tickets-with-coding-agents.md

# Automatically resolve tickets with coding agents

Coding agents can significantly speed up development, but crucial engineering context often gets lost in the process. This guide shows how to automate the flow from Jira ticket to GitHub issue to coding agent (e.g. GitHub Copilot) and back to Jira.

You can implement this in one of two ways:

1. **Workflow** â a single Port workflow runs when a Jira ticket moves to In Progress: it enriches the ticket with catalog context, creates a GitHub issue, triggers Copilot, and comments on Jira with the issue link.

2. **Actions & Automations** â an AI agent creates GitHub issues from Jira tickets (with catalog context), and automations trigger the agent and add the PR link to Jira when Copilot opens a pull request.

Both approaches use the same data model and external setup; only the implementation (workflow vs. actions + automations + AI agent) differs.

![Automatic ticket resolution with coding agents](/img/guides/automatic-ticket-resolution-architecture.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Auto-create PRs for bug fixes** to minimize manual work.
* **Integrate with Copilot** for teams not relying on GitHub Issues.
* **Link Jira tickets to PRs** to improve cross-platform collaboration.
* **Generate GitHub issues from Jira** for faster prototyping.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* [Port's GitHub app](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/) is installed in your account.
* [Port's Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/) is installed in your account.
* You have completed the setup in the [Trigger GitHub Copilot from Port guide](https://docs.port.io/guides/all/trigger-github-copilot-from-port), so that Copilot is automatically assigned to GitHub issues created through this guide.
* For the **Actions & Automations** option: you have access to [create and configure AI agents](https://docs.port.io/ai-interfaces/ai-agents/overview#getting-started-with-ai-agents) in Port.
* For the **Workflow** option: you have access to [workflows](https://docs.port.io/workflows/overview) in Port. Workflows are currently in closed beta and may undergo breaking changes and occasional downtime without prior notice.

Alternative integrations and coding agents

While this guide uses GitHub and Jira, you can adapt it for other Git providers (e.g. GitLab, Azure DevOps) and project management tools (e.g. Linear). You can also use other coding agents (e.g. Claude Code, Devin) instead of GitHub Copilot for similar automation.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

We will configure the necessary blueprints to support our AI-enhanced coding workflow. This involves updating the Jira issue blueprint with necessary relations.

### Update Jira issue blueprint[â](#update-jira-issue-blueprint "Direct link to Update Jira issue blueprint")

When you install Port's Jira integration, the Jira project and issue blueprints are created by default. However, we need to update the Jira issue blueprint to add the pull request relation and create a mirror property for the PR link.

1. Go to the [builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find and select your existing Jira issue blueprint (e.g. `jiraIssue`).

3. Click on `{...} Edit JSON`.

4. Add the following relation to the `relations` section:

   **Pull request relation (click to expand)**

   ```
   "pull_request": {
     "target": "githubPullRequest",
     "required": false,
     "many": false
   }
   ```

5. Add the following mirror property to the `mirrorProperties` section:

   **Pull request link mirror property (click to expand)**

   ```
   "pull_request_link": {
     "title": "Pull Request Link",
     "path": "pull_request.link"
   }
   ```

6. Click `Save` to update the blueprint.

### Update GitHub integration mapping[â](#update-github-integration-mapping "Direct link to Update GitHub integration mapping")

To track pull requests opened by Copilot that are meant to fix Jira issues, we need to update the GitHub integration mapping so that a pull request can be linked to the corresponding Jira issue using the Jira issue key in the PR title.

1. Go to the [builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find and select your existing GitHub integration configuration.

3. Click on `{...} Edit JSON`.

4. Add the following mapping to the `mappings` section:

   **Pull request mapping (click to expand)**

   ```
   - kind: pull-request
     selector:
       query: ((.title // "") | test("[A-Z]+-[0-9]+")) and (.user.login == "Copilot")
     port:
       entity:
         mappings:
           identifier: (.title // "") | match("[A-Z]+-[0-9]+").string
           blueprint: '"jiraIssue"'
           properties: {}
           relations:
             pull_request: .id|tostring
   ```

5. Click `Save` to update the integration configuration.

## Set up external tools[â](#set-up-external-tools "Direct link to Set up external tools")

We need Jira API access so that the workflow or automations can add comments to Jira issues.

### Set up Jira API access[â](#set-up-jira-api-access "Direct link to Set up Jira API access")

1. Log in to your Jira instance.

2. Generate an API token:

   <!-- -->

   * Go to [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens).
   * Click **Create API token**. Ensure the token has permission to update issues and add comments.
   * Copy the generated token (you will need it for the Port secret).

## Add Port secrets[â](#add-port-secrets "Direct link to Add Port secrets")

To add secrets to your portal:

1. Click **...** in the top right corner of your Port application.

2. Click **Credentials**.

3. Click the **Secrets** tab.

4. Click **+ Secret** and add the following secrets:

   * `GITHUB_TOKEN` â A [GitHub fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) with read and write permissions for **Issues**, **Metadata**, and **Pull requests**, and **Actions** (write) for workflow dispatch. Required for the **Workflow** option; the **Actions & Automations** option may need it if you use an action that creates GitHub issues via the API.

## Implementation in Port[â](#implementation-in-port "Direct link to Implementation in Port")

Choose one implementation. The data model and external setup above are the same for both.

* **Workflow** â One workflow runs when a Jira issue moves to In Progress with the required label. It calls Port AI for context, creates a GitHub issue, triggers the Copilot assignment workflow, and comments on the Jira issue with the GitHub link. No separate AI agent; the flow is deterministic and visible in the workflow editor.
* **Actions & Automations** â You create an AI agent that generates GitHub issues from Jira tickets, and two automations: one that invokes the agent when a Jira ticket moves to In Progress with the **copilot** label, and one that adds the PR link to the Jira ticket when a related pull request is created.

- Workflow
- Actions & Automations

## Build the workflow

Use Port's workflow to run the full sequence: trigger on Jira update â enrich with AI context â create GitHub issue â trigger Copilot â comment on Jira. You can build it with the AI assistant or paste the JSON template.

1. Go to the [workflows page](https://app.getport.io/settings/workflows) of your portal.

2. Click **+ Workflow**.

3. In the dialog, click **Skip to editor**.

   ![Create new workflow dialog](/img/guides/createNewWorkflow.png)

4. Copy and paste this JSON template directly into the workflow editor.

   **Automatically resolve ticket workflow template (click to expand)**

   ```
   {
     "identifier": "automatic_ticket_resolution_workflow",
     "title": "Autonomous Ticket Resolution With AI",
     "icon": "Jira",
     "description": "Automatically generate GitHub issues from Jira tickets with rich organizational context when tickets move to In Progress, assign to GitHub Copilot, and link PRs back to Jira",
     "allowAnyoneToViewRuns": true,
     "nodes": [
       {
         "identifier": "comment_on_jira_ai_failure",
         "title": "Comment on Jira â AI Context Failed",
         "icon": "Jira",
         "description": "Adds a comment to the Jira issue explaining that automated GitHub issue creation was skipped because AI context extraction failed, and suggests next steps.",
         "config": {
           "type": "WEBHOOK",
           "url": "https://<YOUR_JIRA_ORGANIZATION_URL>/rest/api/3/issue/{{ .outputs.trigger.jira_key }}/comment",
           "agent": false,
           "synchronized": true,
           "method": "POST",
           "headers": {
             "Accept": "application/json",
             "Content-Type": "application/json",
             "Authorization": "Basic {{ .secrets._JIRA_ATLASSIAN_USER_EMAIL + \":\" + .secrets._JIRA_ATLASSIAN_USER_TOKEN | @base64 }}"
           },
           "body": {
             "body": {
               "type": "doc",
               "content": [
                 {
                   "type": "paragraph",
                   "content": [
                     {
                       "text": "â ï¸ Automated GitHub issue creation was skipped because context enrichment failed.",
                       "type": "text"
                     }
                   ]
                 },
                 {
                   "type": "paragraph",
                   "content": [
                     {
                       "text": "What this means:\nâ¢ The Jira ticket was detected correctly\nâ¢ The AI step did not return usable context\nâ¢ No GitHub issue was created to avoid low-quality or incomplete data",
                       "type": "text"
                     }
                   ]
                 },
                 {
                   "type": "paragraph",
                   "content": [
                     {
                       "text": "Next steps:\nâ¢ You can retry the automation\nâ¢ Or manually create a GitHub issue if work should proceed immediately",
                       "type": "text"
                     }
                   ]
                 }
               ],
               "version": 1
             }
           }
         },
         "variables": {}
       },
       {
         "identifier": "create_github_issue",
         "title": "Create GitHub Issue",
         "icon": "Github",
         "description": "Creates a new GitHub issue using the Jira issue details and AI-generated context",
         "config": {
           "type": "WEBHOOK",
           "url": "https://api.github.com/repos/<GITHUB_ORG>/<GITHUB_REPO>/issues",
           "agent": false,
           "synchronized": true,
           "method": "POST",
           "headers": {
             "Accept": "application/vnd.github+json",
             "Authorization": "Bearer {{ .secrets.GITHUB_TOKEN }}",
             "X-GitHub-Api-Version": "2022-11-28"
           },
           "body": {
             "body": "{{ .outputs.extract_context_with_ai.ai_response }}",
             "title": "{{ .outputs.trigger.jira_key + \" - \" + .outputs.trigger.jira_title }}",
             "labels": [
               "auto_assign"
             ]
           }
         },
         "variables": {
           "issue_url": "{{ .response.data.html_url }}",
           "issue_number": "{{ .response.data.number }}"
         }
       },
       {
         "identifier": "extract_context_with_ai",
         "title": "Extract Context with Port AI",
         "icon": "AI",
         "description": "Invokes Port AI to enrich the Jira issue with contextual data from the Port catalog",
         "config": {
           "type": "AI",
           "userPrompt": "A Jira issue has moved to In Progress.\n\nIssue Details:\n- Key: {{ .outputs.trigger.jira_key }}\n- Title: {{ .outputs.trigger.jira_title }}\n- Type: {{ .outputs.trigger.jira_type }}\n- Description: {{ .outputs.trigger.jira_description }}\n\nRelated Jira Project:\n- Key: {{ .outputs.trigger.jira_project_key }}\n\nYour task:\nQuery the Port catalog using MCP tools (e.g list_entities) to find any related services or repositories connected to this Jira issue.\n\n- Always fetch ALL available properties for each entity\n- Do not limit properties unless explicitly required\n\nExtract ONLY context that actually exists and is directly related via Port relationships.\n\n### Core service context (if available)\n- Service description and tier based on the README\n- Owning team(s)\n- Deployment environments (e.g. prod)\n- Key dependencies (upstream/downstream services)\n\n### Relationship-heavy context (AGGREGATE, DO NOT LIST)\nFor the related service/repository, summarize:\n- PagerDuty incidents: total number of open incidents\n- Deployments: number of deployments, environments deployed to, most recent deployment timestamp (if available)\n- Security vulnerabilities: number of open vulnerabilities, breakdown by severity (e.g. critical / high / medium)\n\nDo NOT include: raw logs, \"None found\" bullet lists. Only mention a category if at least one related entity exists.\n\nThen prepare:\n1. A GitHub issue title that starts with the Jira key in this exact format: {{ .outputs.trigger.jira_key }} - <what needs to be done>\n2. A GitHub issue body that clearly summarizes the Jira issue in developer-friendly language, adds concise business-relevant Port context (ownership, risk, stability, deploy state), uses aggregated facts not exhaustive lists, avoids assumptions or inferred data, and is fully self-contained.",
           "systemPrompt": "You are a helpful assistant that extracts contextual information from the Port catalogue.",
           "tools": [
             "^(list|get|search|track|describe)_.*"
           ]
         },
         "variables": {
           "ai_error": "{{ .error }}",
           "ai_response": "{{ .response }}"
         }
       },
       {
         "identifier": "has_ai_context",
         "title": "Has AI Response",
         "icon": null,
         "description": "Checks whether the AI context extraction completed successfully and returned a non-empty response. Prevents downstream actions when AI invocation fails or returns no usable output.",
         "config": {
           "type": "CONDITION",
           "options": [
             {
               "identifier": "yes",
               "title": "AI context available",
               "expression": "(.outputs.extract_context_with_ai.ai_error == null and .outputs.extract_context_with_ai.ai_response != null)"
             },
             {
               "identifier": "no",
               "title": "AI failed or returned no context",
               "expression": ".outputs.extract_context_with_ai.ai_error != null"
             }
           ]
         },
         "variables": {}
       },
       {
         "identifier": "trigger",
         "title": "On Jira Ticket Updated",
         "icon": "Jira",
         "description": "Listens for Jira issue updates and triggers the workflow when a ticket transitions from 'To Do' to 'In Progress', is product-approved, and has an assignee.",
         "config": {
           "type": "EVENT_TRIGGER",
           "event": {
             "type": "ENTITY_UPDATED",
             "blueprintIdentifier": "jiraIssue"
           },
           "condition": {
             "type": "JQ",
             "expressions": [
               ".diff.before.properties.status == \"To Do\"",
               ".diff.after.properties.status == \"In Progress\"",
               "(.diff.after.properties.labels | index(\"copilot\")) != null"
             ],
             "combinator": "and"
           }
         },
         "variables": {
           "jira_key": "{{ .diff.after.identifier }}",
           "jira_url": "{{ .diff.after.properties.url }}",
           "jira_type": "{{ .diff.after.properties.issueType }}",
           "jira_title": "{{ .diff.after.title }}",
           "assignee_email": "{{ .diff.after.relations.assignee }}",
           "jira_description": "{{ .diff.after.properties.description }}",
           "jira_project_key": "{{ .diff.after.relations.project }}"
         }
       },
       {
         "identifier": "trigger_copilot_assignment",
         "title": "Trigger Copilot Assignment Workflow",
         "icon": "Github",
         "description": "Triggers a GitHub Actions workflow that assigns the newly created GitHub issue to GitHub Copilot, enabling AI-assisted implementation.",
         "config": {
           "type": "WEBHOOK",
           "url": "https://api.github.com/repos/<GITHUB_ORG>/<GITHUB_REPO>/actions/workflows/assign_to_copilot.yml/dispatches",
           "agent": false,
           "synchronized": true,
           "method": "POST",
           "headers": {
             "Accept": "application/vnd.github+json",
             "Authorization": "Bearer {{ .secrets.GITHUB_TOKEN }}",
             "X-GitHub-Api-Version": "2022-11-28"
           },
           "body": {
             "ref": "main",
             "inputs": {
               "issue_number": "{{.outputs.create_github_issue.issue_number | tostring}}",
               "repository_name": "<GITHUB_REPO>",
               "repository_owner": "<GITHUB_ORG>"
             }
           }
         },
         "variables": {}
       },
       {
         "identifier": "update_jira_with_github_link",
         "title": "Add Comment to Jira Issue",
         "icon": "Jira",
         "description": "Adds a comment to the original Jira ticket containing a direct link to the created GitHub issue, ensuring traceability between Jira and GitHub.",
         "config": {
           "type": "WEBHOOK",
           "url": "https://<YOUR_JIRA_ORGANIZATION_URL>/rest/api/3/issue/{{.outputs.trigger.jira_key}}/comment",
           "agent": false,
           "synchronized": true,
           "method": "POST",
           "headers": {
             "Accept": "application/json",
             "Content-Type": "application/json",
             "Authorization": "Basic {{ .secrets._JIRA_ATLASSIAN_USER_EMAIL + \":\" + .secrets._JIRA_ATLASSIAN_USER_TOKEN | @base64 }}"
           },
           "body": {
             "body": {
               "type": "doc",
               "content": [
                 {
                   "type": "paragraph",
                   "content": [
                     {
                       "text": "â GitHub issue created and assigned to Copilot: ",
                       "type": "text"
                     },
                     {
                       "text": "{{ .outputs.create_github_issue.issue_url }}",
                       "type": "text",
                       "marks": [
                         {
                           "type": "link",
                           "attrs": {
                             "href": "{{ .outputs.create_github_issue.issue_url }}"
                           }
                         }
                       ]
                     }
                   ]
                 }
               ],
               "version": 1
             }
           }
         },
         "variables": {}
       }
     ],
     "connections": [
       {
         "description": "Triggered when a Jira issue meets the workflow criteria and begins AI-based context enrichment.",
         "sourceIdentifier": "trigger",
         "targetIdentifier": "extract_context_with_ai"
       },
       {
         "description": "Routes the AI invocation result into a conditional gate to determine whether downstream actions should proceed.",
         "sourceIdentifier": "extract_context_with_ai",
         "targetIdentifier": "has_ai_context"
       },
       {
         "description": "Continues workflow execution only when AI context extraction succeeds",
         "sourceIdentifier": "has_ai_context",
         "targetIdentifier": "create_github_issue",
         "sourceOptionIdentifier": "yes"
       },
       {
         "description": "Uses the newly created GitHub issue to trigger Copilot assignment.",
         "sourceIdentifier": "create_github_issue",
         "targetIdentifier": "trigger_copilot_assignment"
       },
       {
         "description": "Finalizes the workflow by linking the GitHub issue back to the originating Jira ticket.",
         "sourceIdentifier": "trigger_copilot_assignment",
         "targetIdentifier": "update_jira_with_github_link"
       },
       {
         "description": "Notifies Jira that AI context extraction failed and GitHub issue creation was intentionally skipped.",
         "sourceIdentifier": "has_ai_context",
         "targetIdentifier": "comment_on_jira_ai_failure",
         "sourceOptionIdentifier": "no"
       }
     ]
   }
   ```

5. Click **Publish** in the top right corner of the editor. If you encounter validation errors, refer to the [workflows troubleshooting page](https://docs.port.io/workflows/troubleshooting).

## Configure the workflow

After publishing, replace placeholder values in the workflow nodes.

### Specify Jira URL and auth

* In the **Comment on Jira â AI Context Failed** (`comment_on_jira_ai_failure`) and **Add Comment to Jira Issue** (`update_jira_with_github_link`) nodes:
  <!-- -->
  * Replace `<YOUR_JIRA_ORGANIZATION_URL>` in the webhook URL with your Jira organization URL (e.g. `example.atlassian.net`).

### Configure the GitHub integration

* In the **Create GitHub Issue** (`create_github_issue`) node:

  <!-- -->

  * Replace `<GITHUB_ORG>` with your GitHub organization or username.
  * Replace `<GITHUB_REPO>` with your repository name.

* In the **Trigger Copilot Assignment Workflow** (`trigger_copilot_assignment`) node:

  <!-- -->

  * Replace `<GITHUB_ORG>` and `<GITHUB_REPO>` in the webhook URL with the same values.
  * Update the `repository_name` and `repository_owner` inputs to match.

## Create AI agent

We will create an AI agent that generates GitHub issues from Jira tickets with appropriate context and labels.

### Configure the GitHub issue creation AI agent

1. Go to the [AI Agents](https://app.getport.io/_ai_agents) page of your portal.

2. Click on `+ AI Agent`.

3. Toggle `Json mode` on.

4. Copy and paste the following JSON schema:

   **GitHub issue creation AI agent configuration (click to expand)**

   ```
   {
     "identifier": "work_item_synchronizer",
     "title": "Work Item Synchronizer",
     "icon": "Details",
     "team": [],
     "properties": {
       "description": "Ensures seamless workflow continuity across development tools",
       "status": "active",
       "prompt": "Create a GitHub issue that builds on the context of a linked Jira ticket.\n\nThe GitHub issue should:\n1.\tSummarize and clearly explain the task, using the Jira description as a base.\n2.\tAugment the description with relevant insights from the repository â such as the README, setup or contribution instructions, existing issues, or implementation notes â to make the issue fully self-contained.\n3.\tThe **issue title MUST start with the Jira ticket key**, using the format: `<Jira-Ticket-ID> - <what needs to be done>` (e.g., `JIRA-1234 - Add missing lint configuration`). This ensures PRs created by Copilot are linkable back to Jira.\n4.\tAdd GitHub labels, including one with the Jira ticket key (e.g., `JIRA-1234`), and any additional relevant labels (e.g., bug, enhancement, infra).\n5.\tAlso include a label named `auto_assign` in all creations.\n6. The GitHub issue body should end with the following directive:\nð¨ **IMPORTANT NOTE FOR COPILOT**: When creating the pull request to resolve this issue:\n    1. You **must ALWAYS include the Jira ticket ID** (e.g., `JIRA-1234`) in the **PR title**.\n    2. Do **not** rename the PR title or remove the Jira ticket reference.\n    3. Add GitHub labels with the Jira ticket key (e.g., `JIRA-1234`) to the PR.\n\nIf no direct match can be confidently made (e.g., across multiple repos), make a best guess, and clearly state any assumptions in the issue body.",
       "execution_mode": "Automatic",
       "conversation_starters": [],
       "tools": [
         "^(list|search|track|describe)_.*",
         "run_create_github_issue"
       ]
     },
     "relations": {}
   }
   ```

   MCP enhanced capabilities

   The AI agent uses MCP (Model Context Protocol) enhanced capabilities to discover relevant blueprint entities via its tools. The `^(list|search|track|describe)_.*` pattern lets the agent access and analyze related entities in your software catalog. We also add `run_create_github_issue` so the agent can create GitHub issues from Jira tickets.

5. Click `Create` to save the agent.

## Set up automations

We will create two automations:

1. Trigger the AI agent when Jira tickets move to **In Progress** with the **copilot** label.
2. Comment on the Jira ticket with the related pull request link when a PR is linked.

### Automation to trigger AI agent

Multiple approaches

This automation can be configured to trigger on different criteria (e.g. label, properties, or ownership), such as: automatically fix small bugs, fix security issues with critical SLA, or only tasks in repositories that are onboarded to the AI agents and are considered low-risk.

1. Go to the [automations](https://app.getport.io/settings/automations) page of your portal.

2. Click on `+ Automation`.

3. Copy and paste the following JSON schema:

   **Create GitHub issue from Jira automation (click to expand)**

   Create in Port

   ```
   {
     "identifier": "create_github_issue_from_jira",
     "title": "Create a GitHub issue from Jira ticket",
     "description": "When Jira issue moves to In Progress with Copilot label, create a GitHub issue",
     "icon": "Github",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_UPDATED",
         "blueprintIdentifier": "jiraIssue"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.after.properties.status == \"In Progress\"",
           ".diff.before.properties.status == \"To Do\"",
           "(.diff.after.properties.labels | index(\"copilot\")) != null"
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.port.io/v1/agent/work_item_synchronizer/invoke",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Content-Type": "application/json"
       },
       "body": {
         "prompt": "Jira Task title: \"{{.event.diff.after.title}}\"\n. Jira Task identifier: \"{{.event.diff.after.identifier}}\"\n Jira Task description: \"{{.event.diff.after.properties.description}}\"\nRepository:{{.event.diff.after.relations.repository}}.",
         "labels": {
           "source": "create_github_issue_automation",
           "jira_issue_id": "{{ .event.diff.after.identifier }}"
         }
       }
     },
     "publish": true
   }
   ```

4. Click `Create` to save the automation.

### Automation to comment on the Jira ticket with the PR link

This automation adds a comment to the Jira ticket when a new pull request is linked (e.g. by the GitHub integration), so the ticket shows the PR link.

1. Go back to the [automations](https://app.getport.io/settings/automations) page of your portal.

2. Click on `+ Automation`.

3. Copy and paste the following JSON schema:

   **Add PR link to Jira issue automation (click to expand)**

   Atlassian domain replacement

   Replace `<YOUR_ATLASSIAN_DOMAIN>` with your actual Atlassian domain in the webhook URL.

   Create in Port

   ```
   {
     "identifier": "add_pr_link_to_jira_issue",
     "title": "Add PR Link to Jira Issue",
     "description": "An automation that adds the PR link to the Jira issue as a comment",
     "icon": "GitPullRequest",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_UPDATED",
         "blueprintIdentifier": "jiraIssue"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.after.relations.pull_request != .diff.before.relations.pull_request"
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://<YOUR_ATLASSIAN_DOMAIN>.atlassian.net/rest/api/3/issue/{{  .event.diff.before.identifier }}/comment",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Authorization": "Basic {{ .secrets._JIRA_ATLASSIAN_USER_EMAIL + \":\" + .secrets._JIRA_ATLASSIAN_USER_TOKEN | @base64 }}",
         "Content-Type": "application/json"
       },
       "body": {
         "body": {
           "type": "doc",
           "version": 1,
           "content": [
             {
               "type": "paragraph",
               "content": [
                 {
                   "type": "text",
                   "text": "A new pull request identified for this ticket. Find the link below:"
                 }
               ]
             },
             {
               "type": "paragraph",
               "content": [
                 {
                   "type": "text",
                   "text": "View Pull Request",
                   "marks": [
                     {
                       "type": "link",
                       "attrs": {
                         "href": "{{ .event.diff.after.properties.pull_request_link }}"
                       }
                     },
                     {
                       "type": "strong"
                     }
                   ]
                 }
               ]
             }
           ]
         }
       }
     },
     "publish": true
   }
   ```

4. Click `Create` to save the automation.

## Test the implementation[â](#test-the-implementation "Direct link to Test the implementation")

After you complete either the Workflow or the Actions & Automations setup, use the steps below to verify that ticket resolution runs correctly.

### Trigger a test Jira ticket update[â](#trigger-a-test-jira-ticket-update "Direct link to Trigger a test Jira ticket update")

1. Go to your Jira instance and find a test ticket.

2. Add the required label:

   <!-- -->

   * **Workflow**: add the **product\_approved** label and ensure the ticket has an assignee.
   * **Actions & Automations**: add the **copilot** label.

3. Move the ticket status from **To Do** to **In Progress**.

### Verify GitHub issue creation[â](#verify-github-issue-creation "Direct link to Verify GitHub issue creation")

1. Go to your GitHub repository.
2. Verify that a new issue was created with the appropriate title (starting with the Jira key), description, and labels.
3. Check that the issue has the `auto_assign` label.

### Test pull request linking[â](#test-pull-request-linking "Direct link to Test pull request linking")

1. Verify that the GitHub issue is automatically assigned to Copilot.
2. Confirm that a pull request is created (with the Jira ticket key in the title for the Actions & Automations flow).
3. Check the Jira ticket for a comment: **Workflow** adds the GitHub issue link; **Actions & Automations** adds the PR link when the PR is linked to the Jira issue.

![Test workflow result](/img/guides/auto-resolve-jira-ticket-test-workflow.png)

## Related guides[â](#related-guides "Direct link to Related guides")

* [Set up the Task Manager AI agent](https://docs.port.io/guides/all/setup-task-manager-ai-agent).
* [Auto-assign bugs to owners with AI](https://docs.port.io/guides/all/auto-assign-bugs-to-owners/).
* [Improve specifications with Port AI](https://docs.port.io/guides/all/triage-tickets-to-coding-agents/).
* [Orchestrate incident response with AI](https://docs.port.io/guides/all/orchestrate-incident-response-with-ai).
