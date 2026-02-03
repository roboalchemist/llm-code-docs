# Source: https://braintrust.dev/docs/deploy/environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage environments

> Separate dev, staging, and production configurations

Environments let you maintain different versions of prompts, functions, and configurations across your development lifecycle. Test changes in development before promoting them to production.

## Create an environment

Environments are defined at the project level:

1. Navigate to **Configuration** > **Environments**.
2. Click **+ Environment**.
3. Enter a name (e.g., "production", "staging", "dev").
4. Optionally set as the default environment.
5. Click **Create**.

Every project starts with no environments. When no environment is specified, the latest version of each prompt or function is used.

## Assign versions

Assign specific prompt or function versions to environments:

<Tabs>
  <Tab title="Prompts" icon="message-square">
    1. Open a prompt in the editor.
    2. Click **Environments** in the sidebar.
    3. Select an environment from the dropdown.
    4. Choose which version to assign.
    5. Click **Save**.

    The assigned version will be used when calling the prompt with that environment parameter.
  </Tab>

  <Tab title="Functions" icon="function-square">
    1. Navigate to **Tools**, **Scorers**, or **Workflows**.
    2. Open a function.
    3. Click **Environments** in the sidebar.
    4. Select an environment and version.
    5. Click **Save**.
  </Tab>
</Tabs>

## Use environments in code

Specify the environment when calling prompts or functions:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";

  const result = await invoke({
    projectName: "My Project",
    slug: "summarizer",
    environment: "production",
    input: { text: "Long text to summarize..." },
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  result = invoke(
      project_name="My Project",
      slug="summarizer",
      environment="production",
      input={"text": "Long text to summarize..."},
  )
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require 'braintrust'

  result = Braintrust.invoke(
    project_name: 'My Project',
    slug: 'summarizer',
    environment: 'production',
    input: { text: 'Long text to summarize...' }
  )
  ```
</CodeGroup>

Without an environment parameter, the latest version is used.

### Load prompts with environments

Use `loadPrompt` to load prompt configurations with environment parameters:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { loadPrompt } from "braintrust";

  // Load from specific environment
  const prompt = await loadPrompt({
    projectName: "My Project",
    slug: "my-prompt-slug",
    environment: "production",
  });

  // Use conditional versioning
  const prompt = await loadPrompt({
    projectName: "My Project",
    slug: "my-prompt-slug",
    version: process.env.NODE_ENV === "production" ? "5878bd218351fb8e" : undefined,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import load_prompt
  import os

  # Load from specific environment
  prompt = load_prompt(
      project="My Project",
      slug="my-prompt-slug",
      environment="production"
  )

  # Use conditional versioning
  prompt = load_prompt(
      "My Project",
      "my-prompt-slug",
      version="5878bd218351fb8e" if os.environ.get("NODE_ENV") == "production" else None,
  )
  ```
</CodeGroup>

### Use the REST API

Load prompts with environment parameters via HTTP:

<CodeGroup dropdown>
  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # Load by project ID and slug
  curl "https://api.braintrust.dev/v1/prompt?slug=my-prompt-slug&project_id=PROJECT_ID&environment=production" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY"

  # Load by prompt ID
  curl "https://api.braintrust.dev/v1/prompt/PROMPT_ID?environment=production" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY"
  ```
</CodeGroup>

## Promote versions

Move tested versions from development to production:

1. Test a new prompt version in the "dev" environment.
2. Run experiments to validate performance.
3. Once satisfied, assign the same version to "staging".
4. After final validation, assign to "production".

This workflow ensures changes are validated before reaching production users.

## Set default environments

Mark an environment as default to use it when no environment is specified:

1. Navigate to **Configuration** > **Environments**.
2. Click the **···** menu next to an environment.
3. Select **Set as default**.

The default environment is used when calling prompts without an explicit environment parameter.

## Filter by environment

In the Logs page, filter by environment to view requests from specific contexts:

* Use the filter bar: `environment = "production"`.
* Use the **Environment** filter dropdown.
* Group by environment to compare metrics across environments.

## Monitor environment changes

Set up [environment alerts](/admin/automations/alerts#create-an-environment-alert) to get notified via webhook or Slack when prompt versions are assigned to or removed from environments. Use these to track deployments, maintain audit trails, or trigger downstream CI/CD workflows.

## Common patterns

### Three-tier deployment

Maintain dev, staging, and production environments:

* **dev**: Latest changes, frequent updates, used by developers.
* **staging**: Pre-release testing, stable versions.
* **production**: Customer-facing, only validated versions.

### Feature flags

Use environments to control feature rollouts:

* Create an environment for each feature flag.
* Assign different prompt versions based on flag state.
* Gradually roll out by changing environment assignments.

### A/B testing

Test prompt variations by environment:

* Create environments for each variant (e.g., "variant-a", "variant-b").
* Assign different prompt versions to each.
* Route users to different environments based on A/B test assignment.
* Compare performance using environment filters.

## Next steps

* [Deploy prompts](/deploy/prompts) that use environments
* [Monitor deployments](/deploy/monitor) filtered by environment
* [View logs](/observe/view-logs) separated by environment
* [Compare experiments](/evaluate/compare-experiments) across environment versions
