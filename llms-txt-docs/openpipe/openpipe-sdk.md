# Source: https://docs.openpipe.ai/getting-started/openpipe-sdk.md

# Installing the SDK

Use the OpenPipe SDK as a drop-in replacement for the generic OpenAI package. Calls sent through the OpenPipe SDK will be recorded by default for later training. You'll use this same SDK to call your own fine-tuned models once they're deployed.

<Tabs>
  <Tab title="Python">
    Find the SDK at [https://pypi.org/project/openpipe/](https://pypi.org/project/openpipe/)

    ## Installation

    ```bash
    pip install openpipe
    ```

    ## Simple Integration

    Add `OPENPIPE_API_KEY` to your environment variables.

    ```bash
    export OPENPIPE_API_KEY=opk-<your-api-key>
    # Or you can set it in your code, see "Complete Example" below
    ```

    Replace this line

    ```python
    from openai import OpenAI
    ```

    with this one

    ```python
    from openpipe import OpenAI
    ```

    ## Adding Searchable Metadata Tags

    OpenPipe follows OpenAI’s concept of metadata tagging for requests. You can use metadata tags in the [Request Logs](/features/request-logs) view to narrow down the data your model will train on.
    We recommend assigning a unique metadata tag to each of your prompts.
    These tags will help you find all the input/output pairs associated with a certain prompt and fine-tune a model to replace it.

    Here's how you can use the tagging feature:

    ## Complete Example

    ```python
    from openpipe import OpenAI
    import os

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="My API Key",
        openpipe={
            # defaults to os.environ.get("OPENPIPE_API_KEY")
            "api_key": "My OpenPipe API Key",
            # optional, defaults to process.env["OPENPIPE_BASE_URL"] or https://api.openpipe.ai/api/v1 if not set
            "base_url": "My URL",
        }
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "count to 10"}],
        metadata={"prompt_id": "counting", "any_key": "any_value"},
    )

    ```
  </Tab>

  <Tab title="NodeJS (ESM)">
    Find the SDK at [https://www.npmjs.com/package/openpipe](https://www.npmjs.com/package/openpipe)

    ## Installation

    ```bash
    npm install --save openpipe
    # or
    yarn add openpipe
    ```

    ## Simple Integration

    Add `OPENPIPE_API_KEY` to your environment variables.

    ```bash
    export OPENPIPE_API_KEY=opk-<your-api-key>
    # Or you can set it in your code, see "Complete Example" below
    ```

    Replace this line

    ```typescript
    import OpenAI from "openai";
    ```

    with this one

    ```typescript
    import OpenAI from "openpipe/openai";
    ```

    ## Adding Searchable Metadata Tags

    OpenPipe follows OpenAI’s concept of metadata tagging for requests. You can use metadata tags in the [Request Logs](/features/request-logs) view to narrow down the data your model will train on.
    We recommend assigning a unique metadata tag to each of your prompts.
    These tags will help you find all the input/output pairs associated with a certain prompt and fine-tune a model to replace it.

    Here's how you can use the tagging feature:

    ## Complete Example

    ```typescript
    import OpenAI from "openpipe/openai";
    // Fully compatible with original OpenAI initialization
    const openai = new OpenAI({
      apiKey: "my api key", // defaults to process.env["OPENAI_API_KEY"]
      // openpipe key is optional
      openpipe: {
        apiKey: "my api key", // defaults to process.env["OPENPIPE_API_KEY"]
        baseUrl: "my url", // defaults to process.env["OPENPIPE_BASE_URL"] or https://api.openpipe.ai/api/v1 if not set
      },
    });

    const completion = await openai.chat.completions.create({
      messages: [{ role: "user", content: "Count to 10" }],
      model: "gpt-4o",
      // optional
      metadata: {
        prompt_id: "counting",
        any_key: "any_value",
      },
      store: true, // Enable/disable data collection. Defaults to true.
    });
    ```
  </Tab>

  <Tab title="NodeJS (CJS)">
    Find the SDK at [https://www.npmjs.com/package/openpipe](https://www.npmjs.com/package/openpipe)

    ## Installation

    ```bash
    npm install --save openpipe
    # or
    yarn add openpipe
    ```

    ## Simple Integration

    Add `OPENPIPE_API_KEY` to your environment variables.

    ```bash
    export OPENPIPE_API_KEY=opk-<your-api-key>
    # Or you can set it in your code, see "Complete Example" below
    ```

    Replace this line

    ```typescript
    const OpenAI = require("openai");
    ```

    with this one

    ```typescript
    const OpenAI = require("openpipe/openai").default;
    ```

    ## Adding Searchable Metadata Tags

    OpenPipe follows OpenAI’s concept of metadata tagging for requests. You can use metadata tags in the [Request Logs](/features/request-logs) view to narrow down the data your model will train on.
    We recommend assigning a unique metadata tag to each of your prompts.
    These tags will help you find all the input/output pairs associated with a certain prompt and fine-tune a model to replace it.

    Here's how you can use the tagging feature:

    ## Complete Example

    ```typescript
    import OpenAI from "openpipe/openai";
    // Fully compatible with original OpenAI initialization
    const openai = new OpenAI({
      apiKey: "my api key", // defaults to process.env["OPENAI_API_KEY"]
      // openpipe key is optional
      openpipe: {
        apiKey: "my api key", // defaults to process.env["OPENPIPE_API_KEY"]
        baseUrl: "my url", // defaults to process.env["OPENPIPE_BASE_URL"] or https://api.openpipe.ai/api/v1 if not set
      },
    });

    const completion = await openai.chat.completions.create({
      messages: [{ role: "user", content: "Count to 10" }],
      model: "gpt-4o",
      // optional
      metadata: {
        prompt_id: "counting",
        any_key: "any_value",
      },
      store: true, // Enable/disable data collection. Defaults to true.
    });
    ```
  </Tab>
</Tabs>

## Should I Wait to Enable Logging?

We recommend keeping request logging turned on from the beginning. If you change your prompt you can just set a new `prompt_id` metadata tag so you can select just the latest version when you're ready to create a dataset.
