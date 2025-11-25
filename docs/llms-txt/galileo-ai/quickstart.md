# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/quickstart.md

# Quickstart Guide | Galileo Evaluate

> Start using Galileo Evaluate with this quickstart guide, covering prompt engineering, AI evaluation, and integrating tools into existing workflows.

## How to get started with Galileo Evaluate

### Create a Galileo Account

1. Go to your **Galileo console page** (a link that looks something like "console.galileo.yourcompany.com"). Speak to your **Galileo Admin**, or send a Slack on your shared Galileo slack channel if you don't know the URL.

2. Create an account by asking your Admin to send you an invite or directly via the Console homepage.

### Install the Galileo Client

<Tabs>
  <Tab title="Python">
    1. Open a Python notebook or any python environment where you want to install Galileo

    2. Install the python client via **pip install** `promptquality`

    3. Next, run the following code to create your first run. Replace YOUR\_GALILEO\_URL with your Galileo console page URL (looks something like "console.galileo.yourcompany.com").

    ```python
    import promptquality as pq

    MY_GALILEO_URL = # e.g. "console.galileo.yourcompany.com"
    pq.login(MY_GALILEO_URL)

    template = "Explain {{topic}} to me like I'm a 5 year old"

    data = {"topic": ["Quantum Physics", "Politics", "Large Language Models"]}

    pq.run(project_name='my_first_project',
          template=template,
          dataset=data,
          settings=pq.Settings(model_alias='ChatGPT (16K context)',
                                temperature=0.8,
                                max_tokens=400))
    ```

    ### **Authentication**

    By default, `pq.login()` will take the user to the Galileo console to copy and paste a short term token.

    Alternatively, it is possible to programmatically authenticate a user by setting the `GALILEO_API_KEY` environment variable.

    ```python
    import os

    os.environ['GALILEO_API_KEY']="Your Galileo API key"

    MY_GALILEO_URL = # e.g. "console.galileo.yourcompany.com"
    pq.login(MY_GALILEO_URL)

    template = ...
    ```
  </Tab>

  <Tab title="TypeScript">
    1. Open a TypeScript project where you want to install Galileo

    2. Install the client via npm with `npm install @rungalileo/galileo`

    *If you are not using [Observe Callback](/galileo/gen-ai-studio-products/galileo-observe/getting-started#integrating-with-langchain) features you can use the `--no-optional` flag to avoid extraneous dependencies.*

    3. Add your **console URL** (*GALILEO\_CONSOLE\_URL*) and [API key](#getting-an-api-key) (*GALILEO\_API\_KEY*) to your environment variables in your `.env` file.

    ```
    GALILEO_CONSOLE_URL="https://console.galileo.yourcompany.com"
    GALILEO_API_KEY="Your API Key"

    # Alternatively, you can also use username/password.
    GALILEO_USERNAME="Your Username"
    GALILEO_PASSWORD="Your Password"
    ```

    ```TypeScript
    import { GalileoEvaluateWorkflow } from "@rungalileo/galileo";

    // Initialize and create project
    const evaluateWorkflow = new GalileoEvaluateWorkflow("Evaluate Project"); // Project Name
    await evaluateWorkflow.init();
    ```
  </Tab>
</Tabs>

### Getting an API Key

To create an API key:

<Steps>
  <Step title="Go to your Galileo Console settings and select API Keys">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/quick-1.png" />
    </Frame>
  </Step>

  <Step title="Select Create a new key">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/quick-3.png" />
    </Frame>
  </Step>

  <Step title="Give your key a distinct name and hit Create">
    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/api-key-name.png" />
    </Frame>
  </Step>
</Steps>

### Running your first eval

First, create an [eval set](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/create-an-evaluation-set). Once you have your eval set, you're ready to start your first evaluation run:

* If you have not written any code yet and are looking to evaluate a model and template for your use case, check out [Creating Prompt Runs](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-prompts).

  * If you want to try multiple templates or model combinations in one go, check out [Prompt Sweeps](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/experiment-with-multiple-prompts)

* If you have an application or prototype you'd like to evaluate, check out [Integrating Evaluate into my existing application](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart/integrate-evaluate-into-my-existing-application-with-python).
