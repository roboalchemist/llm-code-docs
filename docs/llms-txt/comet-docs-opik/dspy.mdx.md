# Source: https://www.comet.com/docs/opik/integrations/dspy.mdx

***

description: >-
Start here to integrate Opik into your DSPy-based genai application for
end-to-end LLM observability, unit testing, and optimization.
headline: DSPy | Opik Documentation
'og:description': >-
Learn to integrate Opik with DSPy for detailed logging of all DSPy calls,
enhancing your language model programming experience.
'og:site\_name': Opik Documentation
'og:title': Integrate DSPy with Opik for Enhanced Logging
title: Observability for DSPy with Opik
---------------------------------------

[DSPy](https://dspy.ai/) is the framework for programming—rather than prompting—language models.

In this guide, we will showcase how to integrate Opik with DSPy so that all the DSPy calls are logged as traces in Opik.

## Account Setup

[Comet](https://www.comet.com/site?from=llm\&utm_source=opik\&utm_medium=colab\&utm_content=dspy\&utm_campaign=opik) provides a hosted version of the Opik platform, [simply create an account](https://www.comet.com/signup?from=llm\&utm_source=opik\&utm_medium=colab\&utm_content=dspy\&utm_campaign=opik) and grab your API Key.

> You can also run the Opik platform locally, see the [installation guide](https://www.comet.com/docs/opik/self-host/overview/?from=llm\&utm_source=opik\&utm_medium=colab\&utm_content=dspy\&utm_campaign=opik) for more information.

## Getting Started

### Installation

First, ensure you have both `opik` and `dspy` installed:

```bash
pip install opik dspy
```

### Configuring Opik

Configure the Opik Python SDK for your deployment type. See the [Python SDK Configuration guide](/tracing/sdk_configuration) for detailed instructions on:

* **CLI configuration**: `opik configure`
* **Code configuration**: `opik.configure()`
* **Self-hosted vs Cloud vs Enterprise** setup
* **Configuration files** and environment variables

### Configuring DSPy

In order to configure DSPy, you will need to have your LLM provider API key. For this example, we'll use OpenAI. You can [find or create your OpenAI API Key in this page](https://platform.openai.com/settings/organization/api-keys).

You can set it as an environment variable:

```bash
export OPENAI_API_KEY="YOUR_API_KEY"
```

Or set it programmatically:

```python
import os
import getpass

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
```

## Logging DSPy calls

In order to log traces to Opik, you will need to set the `opik` callback:

```python
import dspy
from opik.integrations.dspy.callback import OpikCallback

lm = dspy.LM("openai/gpt-4o-mini")

project_name = "DSPY"
opik_callback = OpikCallback(project_name=project_name, log_graph=True)

dspy.configure(lm=lm, callbacks=[opik_callback])

cot = dspy.ChainOfThought("question -> answer")
cot(question="What is the meaning of life?")
```

The trace is now logged to the Opik platform:

<Frame>
  <img src="https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/9e102d28b88ac9ea759ba05fb00b0e4ce50b1e0d9fffd37ec4b4d2218415a73c/img/cookbook/dspy_trace_cookbook.png" />
</Frame>

If you set `log_graph` to `True` in the `OpikCallback`, then each module graph is also displayed in the "Agent graph" tab:

<Frame>
  <img src="https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/eb45869d2e7ea0a1884e7fdb582c359a54a872a24e6532b9591cb7700d09b073/img/cookbook/dspy_trace_cookbook_with_agent_graph.png" />
</Frame>
