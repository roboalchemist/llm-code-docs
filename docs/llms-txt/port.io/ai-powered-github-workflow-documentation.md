# Source: https://docs.port.io/guides/all/ai-powered-github-workflow-documentation.md

# Auto-generate GitHub workflow documentation

This guide demonstrates how to automatically generate and maintain clear, developer-friendly documentation for GitHub Actions workflows using Port's AI agents and automation system. When workflows are ingested or updated in Port, an AI agent analyzes the YAML configuration and generates markdown documentation explaining what the workflow does and how developers can use it.

![](/img/guides/aiPoweredGithubWorkflowDocumentation.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

This solution addresses several key challenges:

* **Self-Maintaining Documentation** - Documentation stays in sync with workflow changes automatically.
* **Consistent Quality** - Every workflow gets comprehensive, standardized documentation.
* **Developer Experience** - Clear explanations reduce confusion and support requests.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes you have:

* Port's [GitHub integration](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) installed and configured.
* [AI agents feature enabled](/ai-interfaces/ai-agents/overview.md#access-to-the-feature) in your Port account.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

### Update GitHub Workflow blueprint[â](#update-github-workflow-blueprint "Direct link to Update GitHub Workflow blueprint")

The `githubWorkflow` blueprint stores workflow metadata and AI-generated documentation. We need to add two properties to store the workflow YAML content and the AI-generated explanation.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find and open the `githubWorkflow` blueprint.

3. Click on the `{...} Edit JSON` button.

4. Add the following properties to the `schema.properties` section:

   **Properties to add (Click to expand)**

   ```
   {
     "yamlContent": {
       "title": "YAML Content",
       "type": "string",
       "description": "The full YAML content of the workflow file"
     },
     "explanation": {
       "title": "Explanation",
       "type": "string",
       "format": "markdown",
       "description": "AI-generated human-readable explanation of what the workflow does, when it runs, and how to use it"
     }
   }
   ```

5. Click `Save` to update the blueprint.

### Configure GitHub integration mapping[â](#configure-github-integration-mapping "Direct link to Configure GitHub integration mapping")

The GitHub integration needs to be configured to fetch workflow file contents and map them to the `yamlContent` property. The `workflow` kind doesn't provide file content directly, so we'll use the `file` kind to fetch the actual YAML files.

1. Go to [Data Sources](https://app.getport.io/settings/data-sources) in Port.

2. Find your **GitHub** integration and click on it.

3. Go to the **Mapping** tab.

4. Add the following YAML configuration to fetch workflow file contents:

   **Workflow file mapping configuration (Click to expand)**

   ```
   resources:
     # Keep your existing workflow mapping for metadata (status, dates, etc.)
     - kind: workflow
       selector:
         query: "true"
       port:
         entity:
           mappings:
             identifier: ".repo + \"/\" + .path"
             title: ".name"
             blueprint: '"githubWorkflow"'
             properties:
               path: ".path"
               status: ".state"
               createdAt: ".created_at"
               updatedAt: ".updated_at"
               link: ".html_url"
             relations:
               repository: ".repo"

     # File mapping - to add the yamlContent
     - kind: file
       selector:
         query: "true"
         files:
           - path: ".github/workflows/*.yml"
           - path: ".github/workflows/*.yaml"
       skipParsing: true
       port:
         entity:
           mappings:
             identifier: ".repo.name + \"/\" + .file.path"
             title: ".file.name"
             blueprint: '"githubWorkflow"'
             properties:
               path: ".file.path"
               yamlContent: .file.content | tostring 
             relations:
               repository: ".repo.name"
   ```

5. Click `Save & Resync` to save the mapping and trigger a sync.

![](/img/guides/ingestedYamlContent.png)

## Create workflow explanation update action[â](#create-workflow-explanation-update-action "Direct link to Create workflow explanation update action")

Before setting up the AI agent, we need to create a self-service action that the agent can invoke to update the workflow explanation property.

1. Go to [Self-Service](https://app.getport.io/self-serve).

2. Click `+ New Action`.

3. Click `{...} Edit JSON`.

4. Copy and paste the following configuration:

   **Update Workflow Explanation action (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "update_workflow_explanation",
     "title": "Update Workflow Explanation",
     "icon": "Github",
     "description": "Update the explanation property of a GitHub workflow entity",
     "trigger": {
       "type": "self-service",
       "blueprintIdentifier": "githubWorkflow",
       "userInputs": {
         "properties": {
           "explanation": {
             "title": "Explanation",
             "type": "string",
             "format": "markdown",
             "description": "The markdown documentation for this workflow"
           }
         },
         "required": ["explanation"]
       },
       "operation": "DAY-2"
     },
     "invocationMethod": {
       "type": "UPSERT_ENTITY",
       "blueprintIdentifier": "githubWorkflow",
       "mapping": {
         "identifier": "{{ .entity.identifier }}",
         "properties": {
           "explanation": "{{ .inputs.explanation }}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save` to create the action.

## Create AI agent for documentation[â](#create-ai-agent-for-documentation "Direct link to Create AI agent for documentation")

Create an AI agent that analyzes workflow YAML and generates comprehensive documentation.

1. Go to [AI Agents](https://app.getport.io/ai-agents).

2. Click `+ AI Agent`.

3. Click `{...} Edit JSON`.

4. Copy and paste the following configuration:

   **Workflow Documentation AI Agent (Click to expand)**

   ```
   {
     "identifier": "workflow_documentation_agent",
     "title": "Workflow Documentation Agent",
     "icon": "AI",
     "properties": {
       "description": "AI agent that automatically generates human-readable documentation for GitHub Actions workflows by analyzing YAML configurations",
       "status": "active",
       "prompt": "You are a GitHub Actions workflow documentation agent. Analyze workflow YAML files and generate clear markdown documentation.\n\n**Your Task**: Generate developer-friendly documentation covering:\n\n## 1. Overview\nBrief summary (2-3 sentences) of what the workflow does and its purpose.\n\n## 2. Triggers\n- When the workflow runs (push, PR, schedule, manual)\n- Branch and path filters\n- How to trigger manually (if applicable)\n\n## 3. Jobs & Steps\nFor each job, explain:\n- Job purpose and runner environment\n- Key steps and what they do\n- Dependencies between steps\n\n## 4. Configuration Requirements\n- **Secrets**: List required secrets and their purpose\n- **Permissions**: GitHub permissions needed\n- **Inputs**: Required workflow inputs (if any)\n\n## 5. Outputs\n- What the workflow produces (artifacts, deployments)\n- Where to find results\n\n## 6. Usage\nHow developers can:\n- Use this workflow\n- Set up required secrets\n- Trigger and monitor runs\n\n**Guidelines**:\n- Write clearly for all developer skill levels\n- Explain security considerations (secrets, permissions)\n- Use markdown formatting (headers, lists, code blocks)\n- Keep it concise but comprehensive\n\n**Action**: Invoke the 'update_workflow_explanation' action to update the workflow entity's explanation property with your generated markdown documentation.",
       "execution_mode": "Automatic",
       "tools": [
         "^(list|search|track|describe)_.*",
         "run_update_workflow_explanation"
       ]
     },
     "relations": {}
   }
   ```

5. Click `Create` to save the agent.

## Trigger documentation generation[â](#trigger-documentation-generation "Direct link to Trigger documentation generation")

You can trigger documentation generation either manually or automatically:

* Manual (On-Demand)
* Automated (On Workflow Changes)

### Create self-service action

Create a self-service action that developers can trigger to generate documentation on demand.

1. Go to [Self-Service](https://app.getport.io/self-serve).

2. Click `+ New Action`.

3. Click `{...} Edit JSON`.

4. Copy and paste the following configuration:

   **Generate Workflow Documentation action (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "generate_workflow_documentation",
     "title": "Generate Workflow Documentation",
     "icon": "Github",
     "description": "Trigger the AI agent to analyze a GitHub Actions workflow and generate human-readable documentation",
     "trigger": {
       "type": "self-service",
       "blueprintIdentifier": "githubWorkflow",
       "userInputs": {
         "properties": {},
         "required": []
       },
       "operation": "DAY-2"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.port.io/v1/agent/workflow_documentation_agent/invoke",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Content-Type": "application/json"
       },
       "body": {
         "prompt": "Analyze the GitHub Actions workflow with identifier {{ .entity.identifier }} and generate comprehensive documentation. First, retrieve the workflow entity using list_entities with blueprint 'githubWorkflow' and identifiers ['{{ .entity.identifier }}']. Read the workflow's YAML content from the yamlContent property and metadata to create a detailed explanation and update the workflow entity's 'explanation' property with the generated content as a markdown string.",
         "labels": {
           "source": "self_service_action",
           "workflow_id": "{{ .entity.identifier }}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save` to create the action.

### Set up automation

Create automation to automatically generate documentation when workflows are created or updated.

1. Go to [Automations](https://app.getport.io/automations).

2. Click `+ Automation`.

3. Click `{...} Edit JSON`.

4. Copy and paste the following configuration:

   **Auto-Generate Workflow Documentation automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "auto_generate_workflow_documentation",
     "title": "Auto-Generate Workflow Documentation",
     "description": "Automatically triggers AI agent to generate documentation when a GitHub Actions workflow is created or updated",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ANY_ENTITY_CHANGE",
         "blueprintIdentifier": "githubWorkflow"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".event.diff.after.properties.yamlContent != null",
           ".event.diff.after.properties.yamlContent != \"\"",
           ".event.diff.before.properties.yamlContent != .event.diff.after.properties.yamlContent || .event.diff.before == null"
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.port.io/v1/agent/workflow_documentation_agent/invoke",
       "agent": false,
       "synchronized": false,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Content-Type": "application/json"
       },
       "body": {   
         "labels": {
           "source": "auto_workflow_documentation",
           "workflow_id": "{{ .event.diff.after.identifier }}",
           "workflow_path": "{{ .event.diff.after.properties.path }}"
         }
       }
     },
     "publish": true
   }
   ```

5. Click `Create` to save the automation.

![](/img/guides/workflowTriggeredExplanationUpdate.png) ![](/img/guides/workflowTriggeredExplanationPropertyUpdate.png)

## Customization examples[â](#customization-examples "Direct link to Customization examples")

**Example 1: Technical deep-dive style**

Modify the AI agent prompt to generate more technical documentation:

```
{
  "prompt": "...\n\n### Documentation Style\nGenerate technical deep-dive documentation suitable for senior engineers:\n- Include implementation details\n- Explain YAML structure and syntax\n- Provide advanced troubleshooting\n- Reference GitHub Actions documentation\n\n..."
}
```

![](/img/guides/workflowTriggeredExplanationUpdateTechnicalDeepDive.png)

**Example 2: Business stakeholder focus**

Generate high-level, business-focused explanations:

```
{
  "prompt": "...\n\n### Documentation Style\nGenerate business-focused documentation:\n- Focus on outcomes and business value\n- Minimize technical jargon\n- Explain impact on development velocity\n- Highlight compliance and security benefits\n\n..."
}
```

![](/img/guides/workflowTriggeredExplanationUpdateBusinessStakeholderFocus.png)

**Example 3: Security-focused explanations**

For security-critical workflows:

```
{
  "prompt": "...\n\n### Documentation Style\nGenerate security-focused documentation:\n- Highlight security implications of each step\n- Explain secret management requirements\n- Document permission requirements and why they're needed\n- Provide security best practices\n- Include compliance considerations\n\n..."
}
```

![](/img/guides/workflowTriggeredExplanationUpdateSecurityFocused.png)

**Example 4: Filter specific workflows**

Only auto-document production workflows:

```
{
  "condition": {
    "type": "JQ",
    "expressions": [
      ".event.diff.after.properties.path | contains(\"production\") || .event.diff.after.properties.path | contains(\"prod\")"
    ],
    "combinator": "or"
  }
}
```

![](/img/guides/workflowTriggeredExplanationUpdateFilterSpecificWorkflows.png)

**Example 5: Add team-specific context**

Include team conventions in the prompt:

```
{
  "prompt": "...\n\n### Team Context\nOur organization follows these conventions:\n- All production deployments require approval\n- Security scans run on every PR\n- We use semantic versioning for releases\n- Slack notifications are sent to #deployments channel\n\nIncorporate these conventions into the documentation.\n\n..."
}
```

![](/img/guides/workflowTriggeredExplanationUpdateAddTeamSpecificContext.png)

## Related guides[â](#related-guides "Direct link to Related guides")

* [Port GitHub Integration Documentation](/build-your-software-catalog/sync-data-to-catalog/git/github/.md)
* [Port AI Agents Guide](/ai-interfaces/ai-agents/overview.md)
* [Port Automations Documentation](/actions-and-automations/define-automations/.md)
* [GitHub Actions Documentation](https://docs.github.com/en/actions)
