# Source: https://braintrust.dev/docs/core/functions/tools.md

# Tools

Tool functions in Braintrust allow you to define general-purpose code that can be invoked by LLMs to add complex logic or external operations to your workflows.
Tools are reusable and composable, making it easy to iterate on assistant-style agents and more advanced applications. You can create tools in TypeScript or
Python and deploy them across the UI and API via prompts.

## Create a tool

Currently, you must define tools via code and push them to Braintrust with `braintrust push`. To define a tool,
use [`project.tool.create`](/reference/sdks/typescript#toolbuilder) and pick a name and
unique slug. Then push the tool to Braintrust with `braintrust push`.

<Tabs>
  <Tab title="TypeScript">
    ```typescript title="calculator.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import * as braintrust from "braintrust";
    import { z } from "zod";

    // Get a handle to the project (creates if it doesn't exist)
    const project = braintrust.projects.create({ name: "calculator" });

    project.tools.create({
      handler: ({ op, a, b }) => {
        switch (op) {
          case "add":
            return a + b;
          case "subtract":
            return a - b;
          case "multiply":
            return a * b;
          case "divide":
            return a / b;
        }
      },
      name: "Calculator method",
      slug: "calculator",
      description:
        "A simple calculator that can add, subtract, multiply, and divide.",
      parameters: z.object({
        op: z.enum(["add", "subtract", "multiply", "divide"]),
        a: z.number(),
        b: z.number(),
      }),
      returns: z.number(),
      ifExists: "replace",
    });
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust push calculator.ts
    ```
  </Tab>

  <Tab title="Python">
    ```python title="calculator.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    from typing import Literal

    import braintrust
    import requests
    from pydantic import BaseModel, RootModel

    # Get a handle to the project (creates if it doesn't exist)
    project = braintrust.projects.create(name="calculator")

    class CalculatorInput(BaseModel):
        op: Literal["add", "subtract", "multiply", "divide"]
        a: float
        b: float

    class CalculatorOutput(RootModel[float]):
        pass

    def calculator(op, a, b):
        match op:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b

    project.tools.create(
        handler=calculator,
        name="Calculator method",
        slug="calculator-2",
        description="A simple calculator that can add, subtract, multiply, and divide.",
        parameters=CalculatorInput,  # You can also provide raw JSON schema here if you prefer
        returns=CalculatorOutput,
    )
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust push calculator.py
    ```
  </Tab>
</Tabs>

### Dependencies

Braintrust will take care of bundling the dependencies your tool needs. In TypeScript, Braintrust uses `esbuild` to bundle your code and its dependencies together. This works for most dependencies, but it does not support native (compiled) libraries like SQLite. In Python, Braintrust uses `uv` to cross-bundle a specified list of dependencies to the target platform (Linux). This works for binary dependencies except for libraries that require on-demand compilation.

If you have trouble bundling your dependencies, [file an issue in the braintrust-sdk repo](https://github.com/braintrustdata/braintrust-sdk/issues).

## Use tools in the UI

Once you define a tool in Braintrust, you can access it through the UI and [API](/api-reference/functions/invoke-function). However,
the real advantage lies in calling a tool from an LLM. Most models support tool calling, which allows them to select a tool from a list of available
options. Normally, it's up to you to execute the tool, retrieve its results, and re-run the model with the updated context.

Braintrust simplifies this process dramatically by:

* Automatically passing the tool's definition to the model
* Running the tool securely in a sandbox environment when called
* Re-running the model with the tool's output
* Streaming the whole output along with intermediate progress to the client

### View tools in the UI

Available tools are listed on the **Tools** page.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/tools/tool-ui.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/tools/tool-ui.mp4?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=21831e85c348db63ac6bcda322fba27b" type="video/mp4" data-path="images/core/tools/tool-ui.mp4" />
</video>

You can run single datapoints right inside the tool to test its functionality.

### Add tools to a prompt

To add a tool to a prompt, select it in the **Tools** dropdown in your Prompt window. Braintrust will automatically:

* Include it in the list of available tools to the model
* Invoke the tool if the model calls it, and append the result to the message history
* Call the model again with the tool's result as context
* Continue for up to (default) 5 iterations or until the model produces a non-tool result

This example defines a tool that looks up information about the most recent commit in a GitHub repository and pushes it to Braintrust.

<Tabs>
  <Tab title="TypeScript">
    ```typescript title="github.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import * as braintrust from "braintrust";
    import { z } from "zod";

    // Get a handle to the project (creates if it doesn't exist)
    const project = braintrust.projects.create({ name: "github" });

    project.tools.create({
      handler: async ({ org, repo }: { org: string; repo: string }) => {
        const url = `https://api.github.com/repos/${org}/${repo}/commits?per_page=1`;
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.length > 0) {
          return data[0];
        } else {
          return null;
        }
      },
      name: "Get latest commit",
      slug: "get-latest-commit",
      description: "Get the latest commit in a repository",
      parameters: z.object({
        org: z.string(),
        repo: z.string(),
      }),
      ifExists: "replace",
    });
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust push github.ts
    ```
  </Tab>

  <Tab title="Python">
    ```python title="github.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import braintrust
    import requests
    from pydantic import BaseModel

    # Get a handle to the project (creates if it doesn't exist)
    project = braintrust.projects.create(name="github")

    class Args(BaseModel):
        org: str
        repo: str

    def handler(org, repo):
        url = f"https://api.github.com/repos/{org}/{repo}/commits?per_page=1"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        if len(data) > 0:
            return data[0]
        return None

    project.tools.create(
        handler=handler,
        name="Get latest commit",
        slug="get-latest-commit",
        description="Get the latest commit in a repository",
        parameters=Args,
    )
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust push github.py
    ```
  </Tab>
</Tabs>

Once the command completes, the tool is listed in the Library's **Tools** tab.

<img src="https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=f9f5f622980547b4e1ac2cf5fbb0348b" alt="Tool code in library" data-og-width="1520" width="1520" data-og-height="1542" height="1542" data-path="core/tools/github-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?w=280&fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=b209e58b531f6417eea28800fefe34ec 280w, https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?w=560&fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=d5d2e6a4e9b8c711c5ae03bc3b149ee5 560w, https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?w=840&fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=7e83312bb79b228de1d10104269a617a 840w, https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?w=1100&fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=bcff83a94d35ba09e46f4e866bb7d0ca 1100w, https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?w=1650&fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=0a375a5e5776ca2af22d1727a950aee1 1650w, https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/github-tool.png?w=2500&fit=max&auto=format&n=ccw_GHv3EEm5M_id&q=85&s=fd77996784b594c3b5ef2ab197a390e6 2500w" />

Then, you can add the tool to your prompt and run it.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/tools/invoke-github-tool.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/tools/invoke-github-tool.mp4?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=4a633a88b1d0bff38ea1bbd0a3a508b9" type="video/mp4" data-path="images/core/tools/invoke-github-tool.mp4" />
</video>

### Embed tool calls into a prompt

In addition to selecting from the tool menu to add a tool to a prompt, you can also add a tool call directly from the **Assistant** or **Tool** messages within a prompt.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/tools/tools-in-prompt.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/tools/tools-in-prompt.mp4?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=e9e70bb1c6ceddf012f94e8ba5edef21" type="video/mp4" data-path="images/core/tools/tools-in-prompt.mp4" />
</video>

To add a tool call to an Assistant prompt, select **Assistant** from the dropdown menu. Then select the <Icon icon="pocket-knife" /> **Toggle tool calls** icon to add the tool code directly into the prompt editor.

You can also select **Tool** from the dropdown menu to enter a tool call ID, such as `{{input.3.function_responses.0.id}}`.

### Structured outputs

Another use case for tool calling is to coerce a model into producing structured outputs that match a given JSON schema. You can do this
without creating a tool function, and instead use the **Raw** tab in the **Tools** dropdown.

Enter an array of tool definitions following the [OpenAI tool format](https://platform.openai.com/images/guides/function-calling):

<img src="https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/raw-tools.gif?s=a84c5dc061855697da579f9d118ada9b" alt="Raw tools" data-og-width="800" width="800" data-og-height="696" height="696" data-path="core/tools/raw-tools.gif" data-optimize="true" data-opv="3" />

Braintrust supports two different modes for executing raw tools:

* `auto` returns the arguments of the first tool call as a JSON object. This is the default mode.
* `parallel` returns an array of all tool calls including both function names and arguments.

<img src="https://mintcdn.com/braintrust/ccw_GHv3EEm5M_id/core/tools/invoke-raw-tools.gif?s=7b74ebe2ff4668b60c7757350c5abdd5" alt="Invoke raw tool" data-og-width="800" width="800" data-og-height="696" height="696" data-path="core/tools/invoke-raw-tools.gif" data-optimize="true" data-opv="3" />

<Note>
  `response_format: { type: "json_object" }` does not get parsed as a JSON object and will be returned as a string.
</Note>

## Use tools in code

You can also attach a tool to a prompt defined in code. This example defines a tool and a prompt that uses it and pushes both to Braintrust.

<Tabs>
  <Tab title="TypeScript">
    ```typescript title="github.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import * as braintrust from "braintrust";
    import { z } from "zod";

    // Get a handle to the project (creates if it doesn't exist)
    const project = braintrust.projects.create({ name: "github" });

    const latestCommit = project.tools.create({
      handler: async ({ org, repo }: { org: string; repo: string }) => {
        const url = `https://api.github.com/repos/${org}/${repo}/commits?per_page=1`;
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.length > 0) {
          return data[0];
        } else {
          return null;
        }
      },
      name: "Get latest commit",
      slug: "get-latest-commit",
      description: "Get the latest commit in a repository",
      parameters: z.object({
        org: z.string(),
        repo: z.string(),
      }),
    });

    project.prompts.create({
      model: "gpt-4o-mini",
      name: "Commit bot",
      slug: "commit-bot",
      messages: [
        {
          role: "system",
          content: "You are a helpful assistant that can help with GitHub.",
        },
        {
          role: "user",
          content: "{{{question}}}",
        },
      ],
      tools: [latestCommit],
    });
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust push github.ts
    ```
  </Tab>

  <Tab title="Python">
    ```python title="commit-bot.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import braintrust
    import requests
    from pydantic import BaseModel

    # Get a handle to the project (creates if it doesn't exist)
    project = braintrust.projects.create(name="github")

    class Args(BaseModel):
        org: str
        repo: str

    def handler(org, repo):
        url = f"https://api.github.com/repos/{org}/{repo}/commits?per_page=1"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        if len(data) > 0:
            return data[0]
        return None

    latest_commit = project.tools.create(
        handler=handler,
        name="Get latest commit",
        slug="get-latest-commit",
        description="Get the latest commit in a repository",
        parameters=Args,
    )

    project.prompts.create(
        model="gpt-4o-mini",
        name="Commit bot",
        slug="commit-bot",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that can help with GitHub.",
            },
            {
                "role": "user",
                "content": "{{{question}}}",
            },
        ],
        tools=[latest_commit],
    )
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust push commit-bot.py
    ```
  </Tab>
</Tabs>

You can also define the tool and prompt in separate files and push them together by pushing the prompt file. Note that the Python interpreter only supports relative imports from within a package,
so you must either define the tool in the same file as the prompt or use a package structure.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt