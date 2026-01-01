# Source: https://braintrust.dev/docs/core/functions/prompts.md

# Prompts

Prompt engineering is a core activity in AI engineering. Braintrust allows you to create prompts, test them out in the playground,
use them in your code, update them, and track their performance over time.

## Create a prompt

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To create a prompt in the UI:

    1. Go to <Icon icon="message-circle" /> **Prompts** and click <Icon icon="plus" /> **Prompt**.

    2. Specify the following:

       * **Name**: A descriptive display name for the prompt.

       * **Slug**: A unique, stable identifier used to reference the prompt in code. The slug remains constant even when you update the prompt's content or name.

       * **Model and parameters**: The model to use, along with model-specific parameters to configure, such as temperature to control randomness and max tokens to limit response length.

       * **Messages**: The messages to send to the model to generate a response. Each message has a role (system, user, assistant, or tool) to help the model understand who is speaking and how to respond. Messages can contain text or include images (for vision-capable models).

       * **Templating syntax**: The templating syntax to use for variables in your prompt message that get substituted with actual values when the prompt is invoked. Braintrust supports Mustache and Nunjucks templating syntax. For more details, see [Use templating](#use-templating).

       * **Response format**: By default, prompts return freeform text, but you can also return a JSON object or define a specific JSON schema for structured outputs (OpenAI models only). Structured outputs correspond to the `response_format.json_schema` argument in the [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create).

       * **Description** (optional): Context about what the prompt does and when to use it.

       * **Metadata** (optional): Additional information to attach to the prompt.

    3. Click **Save as custom prompt**.
  </Tab>

  <Tab title="SDK" icon="terminal">
    To create a prompt in code, write a script and `push` it to Braintrust from the command line:

    <CodeGroup dropdown>
      ```typescript title="summarizer.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      const project = braintrust.projects.create({
      name: "Summarizer",
      });

      export const summarizer = project.prompts.create({
        name: "Summarizer",
        slug: "summarizer",
        description: "Summarize text",
        model: "claude-3-5-sonnet-latest",
        temperature: 0.7,
        max_tokens: 1000,
        messages: [
          {
            role: "system",
            content: "You are a helpful assistant that can summarize text.",
          },
          {
            role: "user",
            content: "{{{text}}}",
          },
        ],
        response_format: { type: "json_object" },
        metadata: { version: "1.0", purpose: "text-summarization" }
      });
      ```

      ```python title="summarizer.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      project = braintrust.projects.create(name="Summarizer")

      summarizer = project.prompts.create(
          name="Summarizer",
          slug="summarizer",
          description="Summarize text",
          model="claude-3-5-sonnet-latest",
          temperature=0.7,
          max_tokens=1000,
          messages=[
              {"role": "system", "content": "You are a helpful assistant that can summarize text."},
              {"role": "user", "content": "{{{text}}}"},
          ],
          response_format={"type": "json_object"},
          metadata={"version": "1.0", "purpose": "text-summarization"}
      )
      ```
    </CodeGroup>

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    # Typescript
    npx braintrust push summarizer.ts

    # Python
    braintrust push summarizer.py
    ```

    | Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `name`                   | A descriptive display name for the prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | `slug`                   | A unique, stable identifier used to reference the prompt in code. The slug remains constant even when you update the prompt's content or name.                                                                                                                                                                                                                                                                                                                            |
    | `description` (optional) | Context about what the prompt does and when to use it.                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | `model`                  | The model to use, along with model-specific parameters to configure, such as `temperature` to control randomness, `max_tokens` to limit response length.                                                                                                                                                                                                                                                                                                                  |
    | `messages`               | The messages to send to the model to generate a response. Each message has a role (system, user, assistant, or tool) to help the model understand who is speaking and how to respond. Messages can contain text or include images (for vision-capable models).                                                                                                                                                                                                            |
    | `response_format`        | The format of the prompt response. By default, prompts return freeform text, but you can also return a JSON object or define a specific JSON schema for structured outputs (OpenAI models only). Structured outputs correspond to the `response_format.json_schema` argument in the [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create). For more details, see the [OpenAI integration guide](/integrations/ai-providers/openai#structured-outputs). |
    | `metadata` (optional)    | Additional information to attach to the prompt.                                                                                                                                                                                                                                                                                                                                                                                                                           |

    To push a prompt directly from your code instead, add the `project.publish()` method:

    <CodeGroup dropdown>
      ```typescript title="summarizer.ts" {9-11} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      const project = braintrust.projects.create({
      name: "Summarizer",
      });

      ...

      async function main() {
      await project.publish();
      }

      main().catch(console.error);

      ```

      ```python title="summarizer.py" {7-8} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      project = braintrust.projects.create(name="Summarizer")

      ...

      if __name__ == "__main__":
          project.publish()
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Add tools

[Tools](/core/functions/tools) extend your prompt's capabilities by allowing the LLM to call functions during execution. This enables prompts to:

* Query external APIs or databases
* Perform calculations or data transformations
* Retrieve information from vector stores or search engines
* Execute custom business logic

When you add a tool to a prompt, the LLM can decide when to call it based on the user's input, making your prompts more dynamic and capable.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To add tools to a prompt in the UI:

    1. When creating or editing a prompt, click <Icon icon="bolt" /> **Tools**.
    2. Select tool functions from your library or add a raw tools as JSON. Raw tools corresponds to the `tools` argument in the [OpenAI API](https://platform.openai.com/docs/guides/function-calling?api-mode=chat).
    3. Click **Save tools**.
  </Tab>

  <Tab title="SDK" icon="terminal">
    To add tools to a prompt in code, use to the `tools` parameter.

    <Note>
      In Python, the prompt and the tool are defined in the same file and pushed to
      Braintrust together. In TypeScript, they can be defined and pushed separately.
    </Note>

    <CodeGroup dropdown>
      ```typescript {21} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      const project = braintrust.projects.create({
      name: "RAG app",
      });

      export const docSearch = project.prompts.create({
        name: "Doc Search",
        slug: "document-search",
        model: "gpt-4o-mini",
        messages: [
          {
            role: "system",
            content: "You are a helpful assistant that can answer questions about the Braintrust documentation.",
          },
          {
            role: "user",
            content: "{{{question}}}",
          },
        ],
        tools: [toolRAG],
      });
      ```

      ```python {19} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      project = braintrust.projects.create(name="RAG app")

      doc_search = project.prompts.create(
          name="Doc Search",
          slug="document-search",
          model="gpt-4o-mini",
          messages=[
              {
                  "role": "system",
                  "content": "You are a helpful assistant that can answer questions about the Braintrust documentation.",
              },
              {
                  "role": "user",
                  "content": "{{{question}}}",
              },
          ],
          tools=[tool_rag],
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Use templating

To make your prompts dynamic and reusable, you can use variables that get substituted with actual values when the prompt is invoked. Braintrust supports the [Mustache](https://mustache.github.io/) and [Nunjucks](https://mozilla.github.io/nunjucks/templating.html) templating syntax for variables:

* **Mustache** (default): Simple variable substitution and basic logic
* **Nunjucks**: Advanced templating with loops, conditionals, and filters

<Note>
  Nunjucks is a UI-only feature. It works in playgrounds but not when [invoked](#invoke-directly) via SDK.
</Note>

### Mustache

[Mustache](https://mustache.github.io/) is the default templating language. It's simple, widely supported, and sufficient for most use cases.

<Accordion title="Basic variable substitution">
  Use `{{variable}}` to insert values:

  ```
  Hello {{name}}! Your account balance is ${{balance}}.
  ```
</Accordion>

<Accordion title="Nested properties">
  Access nested object properties with dot notation:

  ```
  User: {{user.name}}
  Email: {{user.profile.email}}
  City: {{user.profile.address.city}}
  ```
</Accordion>

<Accordion title="Sections and iteration">
  Use sections to iterate over arrays or conditionally show content:

  ```
  {{#items}}
  - {{name}}: ${{price}}
  {{/items}}

  {{#user}}
  Welcome back, {{name}}!
  {{/user}}
  ```
</Accordion>

<Accordion title="Inverted sections">
  Use `^` to show content when a value is falsy or empty:

  ```
  {{^items}}
  No items found.
  {{/items}}
  ```
</Accordion>

<Accordion title="Comments">
  Use `{{! comment }}` for comments that won't appear in output:

  ```
  {{! This is a comment explaining the template }}
  Hello {{name}}!
  ```

  <Tip>
    For complete Mustache syntax, see the [Mustache
    documentation](https://mustache.github.io/mustache.5.html).
  </Tip>
</Accordion>

<Accordion title="Preserve special characters">
  If you want to preserve double curly brackets `{{` and `}}` as plain text in your prompts when using Mustache, change the delimiter tags to any custom string of your choosing. For example, if you want to change the tags to `<%` and `%>`, insert `{{=<% %>=}}` into the message, and all strings below in the message block will respect these delimiters:

  ```
  {{=<% %>=}}
  Return the number in the following format: {{ number }}

  <% input.formula %>
  ```

  <Note>Dataset edits in playgrounds edit the original dataset.</Note>
</Accordion>

<Accordion title="Strict mode">
  Mustache supports strict mode, which throws an error when required template variables are missing:

  <CodeGroup dropdown>
    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    const result = prompt.build(
      { name: "Alice" },
      {
        strict: true, // Throws if any required variables are missing
      },
    );
    ```

    ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    result = prompt.build(
        {"name": "Alice"},
        strict=True,  # Throws if any required variables are missing
    )
    ```
  </CodeGroup>
</Accordion>

### Nunjucks

For more complex templating needs, you can use [Nunjucks](https://mozilla.github.io/nunjucks/templating.html), a powerful templating language that supports loops, conditionals, filters, and more. Nunjucks implements the Jinja2 templating syntax in JavaScript. If you're familiar with Jinja templates from Python, the syntax will be familiar.

<Note>
  Nunjucks is a UI-only feature. It works in playgrounds but not when [invoked](#invoke-directly) via SDK.
</Note>

<Accordion title="Loops">
  Process arrays and iterate over data:

  ```
  {% for item in items %}
  - {{ item.name }}: {{ item.description }}
  {% endfor %}
  ```

  Loop variables provide useful metadata:

  ```
  {% for product in products %}
  {{ loop.index }}. {{ product.name }}{% if not loop.last %}, {% endif %}
  {% endfor %}
  ```

  Available loop variables: `loop.index` (1-indexed), `loop.index0` (0-indexed), `loop.first`, `loop.last`, `loop.length`
</Accordion>

<Accordion title="Conditionals">
  Add logic to your prompts:

  ```
  {% if user.age >= 18 %}
  You are eligible to vote.
  {% elif user.age >= 16 %}
  You can get a driver's license.
  {% else %}
  You are a minor.
  {% endif %}
  ```

  Combine conditionals with loops:

  ```
  {% for product in products %}
    {% if product.inStock %}
  Available: {{ product.name }} - ${{ product.price }}
    {% endif %}
  {% endfor %}
  ```
</Accordion>

<Accordion title="Filters">
  Transform data with built-in filters:

  ```
  Hello {{ name | upper }}!
  Your email is {{ email | lower }}.
  Items: {{ items | join(", ") }}
  ```

  Common filters:

  * `upper`, `lower`: Change case
  * `title`, `capitalize`: Capitalize text
  * `join(separator)`: Join array elements
  * `length`: Get array or string length
  * `default(value)`: Provide default value
  * `replace(old, new)`: Replace text
</Accordion>

<Accordion title="String operations">
  Concatenate strings with `~`:

  ```
  {{ greeting ~ " " ~ name }}!
  Full name: {{ firstName ~ " " ~ lastName }}
  ```
</Accordion>

<Accordion title="Nested data access">
  Access nested properties and array elements:

  ```
  {{ user.profile.address.city }}
  {{ items[0].name }}
  {{ data.results[2].score }}
  ```
</Accordion>

<Tip>
  For more information on Nunjucks syntax and features, see the [Nunjucks templating documentation](https://mozilla.github.io/nunjucks/templating.html).
</Tip>

## Add MCP servers

You can use public [MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction) servers to give your prompts access to external tools and data. This is useful for:

* Evaluating complex tool calling workflows
* Experimenting with external APIs and services
* Tuning public MCP servers

MCP servers must be public and support OAuth authentication.

<Note>
  MCP servers are a UI-only feature. They work in playgrounds and experiments
  but not when [invoked](#invoke-directly) via SDK.
</Note>

### Add to a prompt

To add an MCP server to a prompt:

1. When creating or editing a prompt, directly or in a playground or experiment, click <Icon icon="plug" /> **MCP**.
2. Enable any available [project-wide servers](#add-to-a-project).
3. To add a prompt-specific MCP server, click <Icon icon="plus" /> **MCP server**:
   * Provide a name, the public URL of the server, and an optional description.
   * Click **Add server**.
   * Authenticate the MCP server in your browser.

For each MCP server, you'll see a list of available tools. Tools are enabled by default, but you can click individual tools to disable them or click **Disable all** to disable all tools in an MCP.

After testing a prompt-specific MCP server, you can promote it to a project-wide server by clicking **...** > **Save to project MCP servers**.

### Add to a project

Project-wide MCP servers are accessible across all projects in your organization. To add a project-wide MCP server:

1. Go to **Configuration** > <Icon icon="plug" /> **MCP**.

2. Click <Icon icon="plus" /> **MCP server** and provide a name, the public URL of the server, and an optional description.

3. Click **Authenticate** to authenticate the MCP server in your browser.

   After authenticating, you'll see a list of tools that will available to prompts using the MCP server.

4. Click **Save**.

## Version a prompt

Every time you save changes to a prompt, Braintrust creates a new version with a unique identifier (e.g., `5878bd218351fb8e`). This versioning system allows you to:

* Track the evolution of your prompts over time
* Pin specific versions in production code
* Roll back to previous versions if needed
* Compare performance across different versions

You can manage different versions of prompts across your development lifecycle by assigning them to environments. For more information about environments and deployment strategies, see the [Environments guide](/guides/environments).

## Test in a playground

[<Icon icon="shapes" /> Playgrounds](/core/playground) provide an interactive environment for testing and refining prompts before deploying them. You can:

* Test prompts with real-world inputs
* Adjust parameters like temperature and max tokens in real-time
* Compare outputs from different models
* Save new versions once you're satisfied with the results

To open a prompt in a playground, click the playground icon in the prompt editor or select a prompt from the prompts list.

<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/playground.gif?s=c2d169830e2e375d25ed7e3b4cf1dc00" alt="Playground" data-og-width="800" width="800" data-og-height="533" height="533" data-path="core/prompts/playground.gif" data-optimize="true" data-opv="3" />

Playgrounds also support structured outputs with visual schema builders, making it easy to configure and validate JSON schemas.

<img src="https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=98937f2bce07f4f044c16f65fac7f126" alt="Schema builder" data-og-width="1816" width="1816" data-og-height="1312" height="1312" data-path="reference/release-notes/schema-builder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?w=280&fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=c534497bccd175ec3088a2a1358cf0f4 280w, https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?w=560&fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=f7bf0a78ee3be7d1c462987cd214653e 560w, https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?w=840&fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=9957a0d336219b0e82e819dd2df0b45e 840w, https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?w=1100&fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=72191336e455409d923d73a3f5710965 1100w, https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?w=1650&fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=127e88832880447eb41ea5659da63d59 1650w, https://mintcdn.com/braintrust/Wf4hRmYD6DWdckGQ/reference/release-notes/schema-builder.png?w=2500&fit=max&auto=format&n=Wf4hRmYD6DWdckGQ&q=85&s=27d42d5e8484f54bcc65760c59989bbf 2500w" />

For more information about playgrounds, see the [Playground guide](/core/playground).

## Use in an experiment

Experiments allow you to systematically evaluate prompt performance across multiple test cases. When using prompts in experiments, you can:

* Test prompts against datasets of inputs and expected outputs
* Compare multiple prompt versions or configurations side-by-side
* Measure performance using built-in or custom scoring functions
* Identify regressions or improvements as you iterate

Experiments provide rigorous, data-driven insights into prompt quality and help you make informed decisions about which versions to deploy.

For more information about experiments, see the [Experiments guide](/core/experiments).

## Use in code

### Invoke directly

In Braintrust, a prompt is a simple function that can be invoked directly through the SDK and [REST API](/api-reference/functions/invoke-function). When invoked, prompt functions leverage the [proxy](/guides/proxy) to access a wide range of providers and models with managed secrets, and are automatically traced and logged to your Braintrust project.

<Tip>
  Functions are a broad concept that encompass prompts, code snippets, HTTP
  endpoints, and more. When using the functions API, you can use a prompt's slug
  or ID as the function's slug or ID, respectively. To learn more about
  functions, see the [functions reference](/reference/functions).
</Tip>

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";

  async function main() {
  const result = await invoke({
  projectName: "your project name",
  slug: "your prompt slug",
  input: {
  // These variables map to the template parameters in your prompt.
  question: "1+1",
  },
  });
  console.log(result);
  }

  main();

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  result = invoke(project_name="your project name", slug="your prompt slug", input={"question": "1+1"})
  print(result)
  ```
</CodeGroup>

The return value, `result`, is a string unless you have tool calls, in which case it returns the arguments
of the first tool call. In TypeScript, you can assert this by using the [`schema`](/reference/sdks/typescript#invokefunctionargsschema) argument, which ensures your
code matches a particular zod schema.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";
  import { z } from "zod";

  async function main() {
  const result = await invoke({
  projectName: "your project name",
  slug: "your prompt slug",
  input: {
  question: "1+1",
  },
  schema: z.string(),
  });
  console.log(result);
  }

  main();

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  result = invoke(project_name="your project name", slug="your prompt slug", input={"question": "1+1"})

  print(result)
  ```
</CodeGroup>

### Load a prompt

The [`loadPrompt()`](/reference/sdks/typescript#loadprompt)/[`load_prompt()`](/reference/sdks/python#load-prompt)
function loads a prompt into a simple format that you can pass along to the OpenAI client.
`loadPrompt` also caches prompts with a two-layered cache
and attempts to use this cache if the prompt cannot be fetched from the Braintrust server:

1. A memory cache, which stores up to `BRAINTRUST_PROMPT_CACHE_MEMORY_MAX` prompts in memory.
   This defaults to 1024.
2. A disk cache, which stores up to `BRAINTRUST_PROMPT_CACHE_DISK_MAX` prompts on disk.
   This defaults to 1048576.

You can also configure the directory used by disk cache
by setting the `BRAINTRUST_PROMPT_CACHE_DIR` environment variable.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import { initLogger, loadPrompt, wrapOpenAI } from "braintrust";

  const logger = initLogger({ projectName: "your project name" });

  // wrapOpenAI will make sure the client tracks usage of the prompt.
  const client = wrapOpenAI(
  new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  }),
  );

  async function runPrompt() {
  // Replace with your project name and slug
  const prompt = await loadPrompt({
  projectName: "your project name",
  slug: "your prompt slug",
  defaults: {
  // Parameters to use if not specified
  model: "gpt-3.5-turbo",
  temperature: 0.5,
  },
  });

  // Render with parameters
  return client.chat.completions.create(
  prompt.build({
  question: "1+1",
  }),
  );
  }

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust import init_logger, load_prompt, wrap_openai
  from openai import OpenAI

  logger = init_logger(project="your project name")

  def run_prompt():
      # Replace with your project name and slug
      prompt = load_prompt(
          "your project name", "your prompt slug", defaults=dict(model="gpt-3.5-turbo", temperature=0.5)
      )

      # wrap_openai will make sure the client tracks usage of the prompt.
      client = wrap_openai(OpenAI(api_key=os.environ["OPENAI_API_KEY"]))

      # Render with parameters
      return client.chat.completions.create(**prompt.build(question="1+1"))
  ```
</CodeGroup>

<Note>
  To use another model provider, use the [Braintrust proxy](/guides/proxy) to
  access a wide range of models using the OpenAI format. You can also grab the
  `messages` and other parameters directly from the returned object to use a
  model library of your choice.
</Note>

### Pin a specific version

When loading a prompt, you can reference a specific version:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const prompt = await loadPrompt({
    projectName: "your project name",
    slug: "your prompt slug",
    version: "5878bd218351fb8e",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  prompt = load_prompt("your project name", "your prompt slug", version="5878bd218351fb8e")
  ```
</CodeGroup>

### Get all versions

To retrieve a list of all available versions, use the `getPromptVersions()` function:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { getPromptVersions } from "braintrust";

  const versions = await getPromptVersions("<project-id>", "<prompt-id>");
  // Returns: ["5878bd218351fb8e", "a1b2c3d4e5f6789", ...]

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import get_prompt_versions

  versions = get_prompt_versions(project_id="<project-id>", prompt_id="<prompt-id>")
  # Returns: ["5878bd218351fb8e", "a1b2c3d4e5f6789", ...]
  ```
</CodeGroup>

### Add extra messages

If you're building a chat app, it's often useful to send back additional messages of context as you gather them. You can provide
OpenAI-style messages to the `invoke` function by adding `messages`, which are appended to the end of the built-in messages.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";
  import { z } from "zod";

  async function reflection(question: string) {
  const result = await invoke({
  projectName: "your project name",
  slug: "your prompt slug",
  input: {
  question,
  },
  schema: z.string(),
  });
  console.log(result);

  const reflectionResult = await invoke({
  projectName: "your project name",
  slug: "your prompt slug",
  input: {
  question,
  },
  messages: [
  { role: "assistant", content: result },
  { role: "user", content: "Are you sure about that?" },
  ],
  });
  console.log(reflectionResult);
  }

  reflection("What is larger the Moon or the Earth?");

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  def reflection(question: str):
      result = invoke(project_name="your project name", slug="your prompt slug", input={"question": question})
      print(result)

      reflection_result = invoke(
          project_name="your project name",
          slug="your prompt slug",
          input={"question": question},
          messages=[
              {"role": "assistant", "content": result},
              {"role": "user", "content": "Are you sure about that?"},
          ],
      )
      print(reflection_result)

  reflection("What is larger the Moon or the Earth?")
  ```
</CodeGroup>

### Stream results

You can also stream results in an easy-to-parse format.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";

  async function main() {
  const result = await invoke({
  projectName: "your project name",
  slug: "your prompt slug",
  input: {
  question: "1+1",
  },
  stream: true,
  });

  for await (const chunk of result) {
  console.log(chunk);
  // { type: "text_delta", data: "The answer "}
  // { type: "text_delta", data: "is 2"}
  }
  }

  main();

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  result = invoke("your project name", "your prompt slug", input={"question": "1+1"}, stream=True)
  for chunk in result:
      print(chunk)
  ```
</CodeGroup>

If you're using Next.js and the [Vercel AI SDK](https://sdk.vercel.ai/docs), you can use the Braintrust
adapter by installing the `@braintrust/vercel-ai-sdk` package and converting the stream to Vercel's format.

```typescript title="vercel-braintrust-adapter.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { invoke } from "braintrust";
import { BraintrustAdapter } from "@braintrust/vercel-ai-sdk";

export async function POST(req: Request) {
  const stream = await invoke({
    projectName: "your project name",
    slug: "your prompt slug",
    input: await req.json(),
    stream: true,
  });

  return BraintrustAdapter.toDataStreamResponse(stream);
}
```

You can also use `streamText` to leverage the Vercel AI SDK directly. Configure the [OpenTelemetry environment variables](/integrations/sdk-integrations/vercel) to log these requests to Braintrust.

```typescript title="vercel-braintrust-streamtext.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";

export async function POST(req: Request) {
  const { prompt } = await req.json();

  const result = await streamText({
    model: openai("gpt-4o-mini"),
    prompt,
    experimental_telemetry: { isEnabled: true },
  });

  return result.toDataStreamResponse();
}
```

### Log spans

`invoke` uses the active logging state of your application, just like any function decorated with `@traced` or `wrapTraced`.
This means that if you initialize a logger while calling `invoke`, it will automatically log spans to Braintrust. By default, `invoke` requests will log to a root span, but you can customize the name of a span using the `name` argument.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke, initLogger, traced } from "braintrust";

  initLogger({
  projectName: "My project",
  });

  async function main() {
  const result = await traced(
  async (span) => {
  span.log({
  tags: ["foo", "bar"],
  });
  const res = await invoke({
  projectName: "Joker",
  slug: "joker-3c10",
  input: {
  theme: "silicon valley",
  },
  });
  return res;
  },
  {
  name: "My name",
  type: "function",
  },
  );
  console.log(result);
  }

  main().catch(console.error);

  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust

  @braintrust.traced(name="My name", type="function")
  def run_joker():
      braintrust.current_span().log(tags=["foo", "bar"])
      braintrust.invoke(
          project_name="Joker",
          slug="joker-3c10",
          input={"theme": "silicon valley"},
      )

  def main():
      braintrust.init_logger(project="My project")
      run_joker()

  if __name__ == "__main__":
      main()
  ```
</CodeGroup>

<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=182c4932bf6ccf133751824141776d8f" alt="Logs with invoke" data-og-width="2616" width="2616" data-og-height="860" height="860" data-path="core/prompts/invoke-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?w=280&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=40e9241785a922146dfa1bedd843b52b 280w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?w=560&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=b7f520716c3bfb72f4876f289f21b82f 560w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?w=840&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=70062aa8ff51db3ab21f6a94a9cbbecd 840w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?w=1100&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=8e6c926376f05c2845cc6b7bc5c71733 1100w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?w=1650&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=8aeaa023f4f785eceb73823e106b3b55 1650w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/invoke-log.png?w=2500&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=5a618dadaa03a26be19eed3235bfc7b9 2500w" />

You can also pass in the `parent` argument, a string that you can
derive from `span.export()` while doing [distributed tracing](/guides/traces/customize#distributed-tracing).

### Set chat/completion format

In Python, `prompt.build()` returns a dictionary with chat or completion parameters, depending on the prompt type. In TypeScript, however,
`prompt.build()` accepts an additional parameter (`flavor`) to specify the format. This allows `prompt.build` to be used in a more type-safe
manner. When you specify a flavor, the SDK also validates that the parameters are correct for that format.

```typescript title="typescript-chat-completion.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const chatParams = prompt.build(
  {
    question: "1+1",
  },
  {
    // This is the default
    flavor: "chat",
  },
);

const completionParams = prompt.build(
  {
    question: "1+1",
  },
  {
    // Pass "completion" to get completion-shaped parameters
    flavor: "completion",
  },
);
```

## Download a prompt

Use version control to download prompts to your local filesystem and ensure you're using a specific version. Use the `pull` command to:

* Download prompts to public projects so others can use them
* Pin your production environment to a specific version without running them through Braintrust on the request path
* Review changes to prompts in pull requests

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
$ npx braintrust pull --help
usage: cli.js pull [-h] [--output-dir OUTPUT_DIR] [--project-name PROJECT_NAME] [--project-id PROJECT_ID] [--id ID] [--slug SLUG] [--version VERSION] [--force]

optional arguments:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        The directory to output the pulled resources to. If not specified, the current directory is used.
  --project-name PROJECT_NAME
                        The name of the project to pull from. If not specified, all projects are pulled.
  --project-id PROJECT_ID
                        The id of the project to pull from. If not specified, all projects are pulled.
  --id ID               The id of a specific function to pull.
  --slug SLUG           The slug of a specific function to pull.
  --version VERSION     The version to pull. Will pull the latest version of each prompt that is at or before this version.
  --force               Overwrite local files if they have uncommitted changes.
```

<Warning>Currently, `braintrust pull` only supports TypeScript.</Warning>

When you run `braintrust pull`, you can specify a project name, prompt slug, or version to pull. If you don't specify
any of these, all prompts across projects will be pulled into a separate file per project. For example, using this command
to retrieve a project named `Summary` will generate the following file:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
$ npx braintrust pull --project-name "Summary"
```

```typescript title="summary.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// This file was automatically generated by braintrust pull. You can
// generate it again by running:
//  $ braintrust pull --project-name "Summary"
// Feel free to edit this file manually, but once you do, you should make sure to
// sync your changes with Braintrust by running:
//  $ braintrust push "braintrust/summary.ts"

import braintrust from "braintrust";

const project = braintrust.projects.create({
  name: "Summary",
});

export const summaryBot = project.prompts.create({
  name: "Summary bot",
  slug: "summary-bot",
  model: "gpt-4o",
  messages: [
    { content: "Summarize the following passage.", role: "system" },
    { content: "{{content}}", role: "user" },
  ],
});
```

<Note>
  To pin your production environment to a specific version, run `braintrust
    pull` with the `--version` flag.
</Note>

## Open from traces

When you use a prompt in your code, Braintrust automatically links spans to the prompt used to generate them. This allows
you to select a span to open it in the playground, and see the prompt that generated it alongside the input variables. You can
even test and save a new version of the prompt directly from the playground.

<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/prompts/debug.gif?s=f512fff377432957cb1a6f9c2d4cd664" alt="Open from traces" data-og-width="1977" width="1977" data-og-height="1152" height="1152" data-path="core/prompts/debug.gif" data-optimize="true" data-opv="3" />

This workflow is very powerful. It effectively allows you to debug, iterate, and publish changes to your prompts directly
within Braintrust. And because Braintrust flexibly allows you to load the latest prompt, a specific version, or even a version
controlled artifact, you have a lot of control over how these updates propagate into your production systems.

## Using the API

The full lifecycle of prompts - creating, retrieving, modifying, etc. - can be managed through the REST API. See the [API docs](https://www.braintrust.dev/docs/api-reference#prompts) for
more details.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt