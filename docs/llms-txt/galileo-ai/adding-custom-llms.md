# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms/adding-custom-llms.md

# Adding Custom LLM APIs / Fine Tuned LLMs

> Showcases how to use Galileo with any LLM API or custom fine-tuned LLMs, not supported out-of-the-box by Galileo.

Galileo comes pre-configured with dozens of LLM integrations across various platforms including OpenAI, Azure OpenAI, Sagemaker, and Bedrock.

However, if you're using an LLM service or custom model that Galileo doesn't have support for, you can still get all that Galileo has to offer by simply using our workflow loggers.

In this guide, we showcase how to leverage Anthropic's `claude-3-sonnet` LLM without Galileo, and then use Galileo to do deep evaluations and analysis.

First, install the required libraries. In this example - Galileo, Anthropic, and Langchain.

```py

    pip install --upgrade promptquality langchain langchain-anthropic
```

Here's a simple code snippet showing you how to query **any LLM of your choice** (in this case we're going with an Anthropic LLM) and log your results to Galileo.

```py


    import os
    import promptquality as pq
    from promptquality import NodeType, NodeRow
    from langchain_anthropic import ChatAnthropic
    from datetime import datetime
    from uuid import uuid4

    os.environ['GALILEO_CONSOLE_URL'] = "https://your.galileo.console.url"
    os.environ["ANTHROPIC_API_KEY"] = "Your Anthropic Key"

    MY_PROJECT_NAME = "my-custom-logging-project"
    MY_RUN_NAME = f'custom-logging-{datetime.now().strftime("%b %d %Y %H_%M_%S")}'

    config = pq.login(os.environ['GALILEO_CONSOLE_URL'])

    model_name = "claude-3-sonnet-20240229"
    chat_model = ChatAnthropic(model=model_name)

    query = "Tell me a joke about bears!"
    response = chat_model.invoke(query)

    # Create the run for logging to Galileo.
    evaluate_run = pq.EvaluateRun(run_name=MY_RUN_NAME, project_name=MY_PROJECT_NAME, scorers=[pq.Scorers.context_adherence_plus])

    # Add the workflow to the run.
    evaluate_run.add_single_step_workflow(input=query, output=response.content, model=model_name, duration_ns=2000)

    # Log the run to Galileo.
    evaluate_run.finish()
```

You should see a result like shown below:

```py

    👋 You have logged into 🔭 Galileo (https://your.galileo.console.url/) as galileo@rungalileo.io.
    Processing complete!
    Initial job complete, executing scorers asynchronously. Current status:
    cost: Computing 🚧
    toxicity: Computing 🚧
    pii: Computing 🚧
    latency: Done ✅
    groundedness: Computing 🚧
    🔭 View your prompt run on the Galileo console at: https://your.galileo.console.url/foo/bar/
```
