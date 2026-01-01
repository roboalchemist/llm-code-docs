# Source: https://braintrust.dev/docs/guides/environments.md

# Environments

> Manage different versions of prompts across development, staging, and production

Environments in Braintrust allow you to manage different versions of prompts across your development lifecycle. You can pin specific versions of prompts to environments like development, staging, and production, enabling controlled deployment and testing workflows.

## Overview

An environment is a named collection that associates specific versions of prompts with a deployment context. This enables you to:

* **Maintain version control**: Pin stable prompt versions to production while testing new versions in development
* **Enable staged deployments**: Promote prompt versions through dev/staging/production pipelines
* **Support A/B testing**: Compare different prompt versions across environments
* **Isolate changes**: Test prompt modifications without affecting production systems

Currently, environments work with **prompts only**.

## Create environments

Environments are configured through the Braintrust UI in your organization settings. Each environment has:

* **Name**: A human-readable name (e.g., "Development", "Production")
* **Slug**: A unique identifier used in API calls (e.g., "dev", "prod")
* **Description**: Optional details about the environment's purpose

To create an environment:

1. Navigate to your organization settings
2. Go to the **Environments** section
3. Select **Add Environment**
4. Enter the name, slug, and optional description
5. Save the environment

## Associate prompts with environments

<img src="https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=343a6d94a55e8b6f84ed2ce25cc53ff3" alt="Environments" data-og-width="1378" width="1378" data-og-height="646" height="646" data-path="images/guides/environments/environments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?w=280&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=a305eea5cf065e91236816e22cad858a 280w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?w=560&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=4c8ba1d8b494982b81aec77d2ec3bc5a 560w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?w=840&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=f6794be1a83017c4e9cb8151a9592beb 840w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?w=1100&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=289df531f60260c6934a1315998c95ec 1100w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?w=1650&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=54bec2093bbdc6b826d6733a03c72b7c 1650w, https://mintcdn.com/braintrust/XgLT3_1J-B3_G0Of/images/guides/environments/environments.png?w=2500&fit=max&auto=format&n=XgLT3_1J-B3_G0Of&q=85&s=3b7725fc0179ce37682f051199becee1 2500w" />

Once you have environments set up, you can associate specific versions of prompts with them. This creates a mapping that tells Braintrust which version of a prompt to return when queried with an environment parameter.

You can make the association using the activity tab on the prompt view.

## Load prompts with environments

### Using the SDK

The Braintrust SDK supports loading prompts with environment parameters:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { loadPrompt } from "braintrust";

  // Load a prompt from a specific environment
  (async () => {
    const prompt = await loadPrompt({
      projectId: "my-project",
      slug: "my-prompt-slug",
      environment: "production",
    });
  })();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust

  # Load a prompt from a specific environment
  prompt = braintrust.load_prompt(project="my-project", slug="my-prompt-slug", environment="production")
  ```
</CodeGroup>

To use different versions of a prompt in different environments (e.g., latest version in staging and specific version in production), you can conditionally pass a version to `loadPrompt()`/`load_prompt()` based on the environment:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const prompt = await loadPrompt({
    projectName: "your project name",
    slug: "your prompt slug",
    version:
      process.env.NODE_ENV === "production" ? "5878bd218351fb8e" : undefined,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  prompt = load_prompt(
      "your project name",
      "your prompt slug",
      version="5878bd218351fb8e" if os.environ["NODE_ENV"] == "production" else None,
  )
  ```
</CodeGroup>

### Using the REST API

You can load prompts with environment parameters directly via HTTP:

```typescript load-prompts-rest.ts theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
(async () => {
  // TODO: Fill these in as needed
  const promptSlug = "";
  const apiKey = "";
  const projectId = "";
  const promptId = "";

  // Load by project id and prompt slug
  const r1 = await fetch(
    `https://api.braintrust.dev/v1/prompt?slug=${promptSlug}&project_id=${projectId}&environment=production`,
    {
      headers: {
        Authorization: "Bearer " + apiKey,
      },
    },
  );

  // Load by prompt ID + environment
  const r2 = await fetch(
    `https://api.braintrust.dev/v1/prompt/${promptId}?environment=production`,
    {
      headers: {
        Authorization: "Bearer " + apiKey,
      },
    },
  );
})();
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt