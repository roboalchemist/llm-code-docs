# Source: https://braintrust.dev/docs/evaluate/write-prompts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Write prompts

> Create, test, and version prompts for your AI application

Prompts are the instructions that guide model behavior. Braintrust lets you create prompts, test them in playgrounds, use them in code, and track their performance over time.

## Create prompts

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    Create prompts directly in the Braintrust UI:

    1. Go to **Prompts** and click **+ Prompt**

    2. Configure the prompt:
       * **Name**: Descriptive display name
       * **Slug**: Unique identifier for code references (remains constant across updates)
       * **Model and parameters**: Model selection, temperature, max tokens, etc.
       * **Messages**: System, user, assistant, or tool messages with text or images
       * **Templating syntax**: Mustache or Nunjucks for variable substitution
       * **Response format**: Freeform text, JSON object, or structured JSON schema
       * **Description**: Optional context about the prompt's purpose
       * **Metadata**: Optional additional information

    3. Click **Save as custom prompt**
  </Tab>

  <Tab title="SDK" icon="terminal">
    Define prompts in code and push to Braintrust:

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
        model: "claude-sonnet-4-5-20250929",
        params: {
          temperature: 0.7,
          max_tokens: 1000,
          response_format: { type: "json_object" },
        },
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
        metadata: { version: "1.0" },
      });
      ```

      ```python title="summarizer.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      project = braintrust.projects.create(name="Summarizer")

      summarizer = project.prompts.create(
          name="Summarizer",
          slug="summarizer",
          description="Summarize text",
          model="claude-sonnet-4-5-20250929",
          params={
              "temperature": 0.7,
              "max_tokens": 1000,
              "response_format": {"type": "json_object"},
          },
          messages=[
              {"role": "system", "content": "You are a helpful assistant that can summarize text."},
              {"role": "user", "content": "{{{text}}}"},
          ],
          metadata={"version": "1.0"},
      )
      ```
    </CodeGroup>

    Push to Braintrust:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust push summarizer.ts
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust push summarizer.py
    ```
  </Tab>
</Tabs>

## Use templating

Use templates to inject variables into prompts at runtime. Braintrust supports [Mustache](https://mustache.github.io/) and [Nunjucks](https://mozilla.github.io/nunjucks/templating.html) templating:

* **Mustache** (default): Simple variable substitution and basic logic
* **Nunjucks**: Advanced templating with loops, conditionals, and filters

<Note>
  Nunjucks is a UI-only feature. It works in playgrounds but not when invoked via SDK.
</Note>

### Mustache

[Mustache](https://mustache.github.io/) is the default templating language.

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
</Accordion>

<Accordion title="Preserve special characters">
  If you want to preserve double curly brackets `{{` and `}}` as plain text when using Mustache, change the delimiter tags:

  ```
  {{=<% %>=}}
  Return the number in the following format: {{ number }}

  <% input.formula %>
  ```
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

For more complex templating needs, use [Nunjucks](https://mozilla.github.io/nunjucks/templating.html), which implements Jinja2 syntax in JavaScript.

<Note>
  Nunjucks is a UI-only feature. It works in playgrounds but not when invoked via SDK.
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
  For complete Mustache syntax, see the [Mustache documentation](https://mustache.github.io/mustache.5.html). For Nunjucks syntax and features, see the [Nunjucks templating documentation](https://mozilla.github.io/nunjucks/templating.html).
</Tip>

## Add tools

[Tools](/deploy/functions#deploy-tools) extend your prompt's capabilities by allowing the LLM to call functions during execution:

* Query external APIs or databases
* Perform calculations or data transformations
* Retrieve information from vector stores or search engines
* Execute custom business logic

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To add tools to a prompt in the UI:

    1. When creating or editing a prompt, click **Tools**.
    2. Select tool functions from your library or add raw tools as JSON.
    3. Click **Save tools**.
  </Tab>

  <Tab title="SDK" icon="terminal">
    To add tools to a prompt in code, use the `tools` parameter:

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

## Add MCP servers

Use public [MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction) servers to give your prompts access to external tools and data:

* Evaluate complex tool calling workflows
* Experiment with external APIs and services
* Tune public MCP servers

MCP servers must be public and support OAuth authentication.

<Note>
  MCP servers are a UI-only feature. They work in playgrounds and experiments but not when invoked via SDK.
</Note>

### Add to a prompt

To add an MCP server to a prompt:

1. When creating or editing a prompt, click **MCP**.
2. Enable any available project-wide servers.
3. To add a prompt-specific MCP server, click **+ MCP server**:
   * Provide a name, the public URL of the server, and an optional description.
   * Click **Add server**.
   * Authenticate the MCP server in your browser.

For each MCP server, you'll see a list of available tools. Tools are enabled by default, but you can disable individual tools or click **Disable all**.

After testing a prompt-specific MCP server, you can promote it to a project-wide server by clicking **...** > **Save to project MCP servers**.

### Add to a project

Project-wide MCP servers are accessible across all projects in your organization:

1. Go to **Configuration** > **MCP**.
2. Click **+ MCP server** and provide a name, the public URL of the server, and an optional description.
3. Click **Authenticate** to authenticate the MCP server in your browser.
4. Click **Save**.

## Use in code

Reference prompts by slug to use them in your application:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  const result = await logger.invoke("summarizer", {
    input: { text: "Long article text here..." },
  });

  console.log(result.output);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger

  logger = init_logger(project="My Project")

  result = logger.invoke("summarizer", input={"text": "Long article text here..."})

  print(result.output)
  ```
</CodeGroup>

Using prompts this way:

* Automatically logs inputs and outputs
* Tracks which prompt version was used
* Enables A/B testing different prompt versions
* Lets you update prompts without code changes

### Load a prompt

The `loadPrompt()`/`load_prompt()` function loads a prompt with caching support:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import { initLogger, loadPrompt, wrapOpenAI } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });
  const client = wrapOpenAI(new OpenAI());

  async function runPrompt() {
    const prompt = await loadPrompt({
      projectName: "My Project",
      slug: "summarizer",
      defaults: {
        model: "gpt-4o",
        temperature: 0.5,
      },
    });

    return client.chat.completions.create(
      prompt.build({ text: "Article to summarize..." }),
    );
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger, load_prompt, wrap_openai
  from openai import OpenAI

  logger = init_logger(project="My Project")
  client = wrap_openai(OpenAI())

  def run_prompt():
      prompt = load_prompt(
          "My Project",
          "summarizer",
          defaults=dict(model="gpt-4o", temperature=0.5)
      )

      return client.chat.completions.create(
          **prompt.build(text="Article to summarize...")
      )
  ```
</CodeGroup>

### Pin a specific version

Reference a specific version when loading prompts:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const prompt = await loadPrompt({
    projectName: "My Project",
    slug: "summarizer",
    version: "5878bd218351fb8e",
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  prompt = load_prompt("My Project", "summarizer", version="5878bd218351fb8e")
  ```
</CodeGroup>

### Stream results

Stream prompt responses for real-time output:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";

  async function main() {
    const result = await invoke({
      projectName: "My Project",
      slug: "summarizer",
      input: { text: "Article text..." },
      stream: true,
    });

    for await (const chunk of result) {
      console.log(chunk);
      // { type: "text_delta", data: "The summary "}
      // { type: "text_delta", data: "is..."}
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  result = invoke("My Project", "summarizer", input={"text": "Article text..."}, stream=True)
  for chunk in result:
      print(chunk)
  ```
</CodeGroup>

### Add extra messages

Append additional messages to prompts for multi-turn conversations:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { invoke } from "braintrust";

  async function reflection(question: string) {
    const result = await invoke({
      projectName: "My Project",
      slug: "assistant",
      input: { question },
    });

    const reflectionResult = await invoke({
      projectName: "My Project",
      slug: "assistant",
      input: { question },
      messages: [
        { role: "assistant", content: result },
        { role: "user", content: "Are you sure about that?" },
      ],
    });

    return reflectionResult;
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import invoke

  def reflection(question: str):
      result = invoke("My Project", "assistant", input={"question": question})

      reflection_result = invoke(
          "My Project",
          "assistant",
          input={"question": question},
          messages=[
              {"role": "assistant", "content": result},
              {"role": "user", "content": "Are you sure about that?"},
          ],
      )

      return reflection_result
  ```
</CodeGroup>

## Test in playgrounds

Playgrounds provide a no-code environment for rapid prompt iteration:

1. Create or select a prompt
2. Add a dataset or enter test inputs
3. Run the prompt and view results
4. Adjust parameters or messages
5. Compare different versions side-by-side

See [Use playgrounds](/evaluate/playgrounds) for details.

## Version prompts

Every prompt change creates a new version automatically. This lets you:

* Compare performance across versions
* Roll back to previous versions
* Pin experiments to specific versions
* Track which version is used in production

View version history in the prompt editor and select any version to restore or compare.

## Optimize with Loop

Use Loop to generate and improve prompts:

Example queries:

* "Generate a prompt for a chatbot that can answer questions about the product"
* "Add few-shot examples based on project logs"
* "Optimize this prompt to be friendlier and more engaging"
* "Improve this prompt based on the experiment results"

Loop analyzes your data and suggests improvements automatically.

## Best practices

**Start simple**: Begin with clear, direct instructions. Add complexity only when needed.

**Use few-shot examples**: Include 2-3 examples in your prompt to guide model behavior.

**Be specific**: Define exactly what you want, including format, tone, and constraints.

**Test with real data**: Use production logs to build test datasets that reflect actual usage.

**Iterate systematically**: Change one thing at a time and measure impact with experiments.

**Version everything**: Save prompt changes so you can track what works and roll back if needed.

## Next steps

* [Write scorers](/evaluate/write-scorers) to evaluate prompt quality
* [Run evaluations](/evaluate/run-evaluations) to compare prompt versions
* [Use playgrounds](/evaluate/playgrounds) for rapid iteration
* [Use the Loop](/observe/loop) to optimize prompts
