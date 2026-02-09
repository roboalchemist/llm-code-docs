# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/quickstart.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

    ```python  theme={null}
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

    ```python  theme={null}
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

    ```TypeScript  theme={null}
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
      <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d024d2fd6b57b29b361b311d4c54c257" data-og-width="396" width="396" data-og-height="392" height="392" data-path="images/quick-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cff645e65c8c0460cf6b8bd97addd8cb 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ac8fea41a955cfe1bbf56b17a452e781 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b6b32ae5606942f61cf3222295e3e5c6 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0e1827e0864478ee54efb08b0f5731a0 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=7785452466dccf1a47e544996f5fdf7e 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-1.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=855fd3e8bb771c8d947f00954c4a095d 2500w" />
    </Frame>
  </Step>

  <Step title="Select Create a new key">
    <Frame>
      <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=9bb9901d25f3629058f2808229622282" data-og-width="187" width="187" data-og-height="42" height="42" data-path="images/quick-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f503b1a25f27374ba09f2b4130ce94c1 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cef0293d1c117f3e9e3bf1b3797d007c 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2705694d716580bdc24b2d09371b2ced 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=83b726e8461da5ff5635efeb53e8b86c 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2b94d636def9339cd905396aae83dac6 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/quick-3.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=942b1aa5516b1d06b012a726bc2adffb 2500w" />
    </Frame>
  </Step>

  <Step title="Give your key a distinct name and hit Create">
    <Frame>
      <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=37f06f83b6a0108b8fc9f6fab0f4eadf" data-og-width="552" width="552" data-og-height="314" height="314" data-path="images/api-key-name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=bdf0ea22dc2f8d5e6d211051ce5d8085 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=88433ca62271cc80790b3a906150a1b6 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=8e305e0e3ac45b41e5e7219b74ed85b5 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=7553934479ff9b645f7a7cacac9954fe 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=368110e06cf2351d5977c90740f147f8 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/api-key-name.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=b92e02ee217a06c04f7b940d202306f5 2500w" />
    </Frame>
  </Step>
</Steps>

### Running your first eval

First, create an [eval set](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/create-an-evaluation-set). Once you have your eval set, you're ready to start your first evaluation run:

* If you have not written any code yet and are looking to evaluate a model and template for your use case, check out [Creating Prompt Runs](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-prompts).
  * If you want to try multiple templates or model combinations in one go, check out [Prompt Sweeps](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/experiment-with-multiple-prompts)

* If you have an application or prototype you'd like to evaluate, check out [Integrating Evaluate into my existing application](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart/integrate-evaluate-into-my-existing-application-with-python).
