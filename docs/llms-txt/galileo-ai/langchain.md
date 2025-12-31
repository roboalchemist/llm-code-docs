# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/integrations/langchain.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/langchain.md

# LangChain Integration | Galileo Evaluate

> Galileo allows you to integrate with your Langchain application natively through callbacks

Galileo supports the logging of chains from `langchain`. To log these chains, we require using the callback from our Python client [`promptquality`](https://docs.rungalileo.io/galileo/python-clients/index).

For logging your data, first login:

```py
import promptquality as pq

pq.login()
```

After that, you can set up the `GalileoPromptCallback`:

```py
from promptquality import Scorers
scorers = [Scorers.context_adherence_luna,
           Scorers.completeness_luna,
           Scorers.pii,
           ...]

galileo_handler = pq.GalileoPromptCallback(
    project_name=<project-name>, scorers=scorers,
)
```

* project\_name: each "run" will appear under this project. Choose a name that'll help you identify what you're evaluating

* scorers: This is the list of metrics you want to evaluate your run over. Check out [Galileo Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) and [Custom Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics) for more information.

### Executing and Logging

Next, run your chain over your Evaluation set and log the results to Galileo.

When you execute your chain (with `run`, `invoke` or `batch`), just include the callback instance created earlier in the callbacks as:

If using `.run()`:

```py
chain.run(<inputs>, callbacks=[galileo_handler])
```

If using `.invoke()`:

```py
chain.invoke(inputs, config=dict(callbacks=[galileo_handler]))
```

If using `.batch()`:

```py
.batch(..., config=dict(callbacks=[galileo_handler]))
```

**Important**: Once you complete executing for your dataset, tell Galileo the run is complete by:

```py
galileo_handler.finish()
```

The `finish` step uploads the run to Galileo and starts the execution of the scorers server-side. This step will also display the link you can use to interact with the run on the Galileo console.

A full example can be found [here](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents-chains-or-multi-step-workflows/examples-with-langchain).

***Note 1:*** Please make sure to set the callback at *execution* time, not at definition time so that the callback is invoked for all nodes of the chain.

***Note 2:*** We recommend using `.invoke` instead of `.batch` because `langchain` reports latencies for the *entire* batch instead of each individual chain execution.
