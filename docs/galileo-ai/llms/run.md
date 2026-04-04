# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/concepts/run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Run

> Runs in Galileo are experiments or iterations done within a [project](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/project).

What is a Galileo run?

These enable users to quickly test or create examples that match the project's goal. Trying different [templates](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/template) or models in each run is an effective way to see which combination is most effective based on Galileo's [metrics](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/metrics). This is because runs can be viewed side-by-side in order to see how their metrics compare to one another. Runs might also have different outputs, and again this is another area where comparing multiple runs can be helpful to find the best output for your use case.

Runs can be either single step or multi-step. A single step run would have just a template and a model. You can quickly iterate over data in your template, but as far as execution, the chain would include a single input for the model and an output by the model. Data can be added manually in the Playground, by uploading a .csv file, or by executing a single step chain programmatically. Selecting multiple single step runs in a project allows you to compare runs.

A multi-step run contains multiple interactions. A simple example is a retrieval augmented generation (RAG) based system, where specific data is provided to create a more concise response by the model. In this case, the chain would take an input, retrieve relevant context from a database based on this input, and supply it to the model in order to generate a more concise response.

To export or delete runs, select them from within a project and click the option that appears at the top of the project.

## Creating a Run

Runs can be created either from the Console, or via code.

Creating runs from code:

```py  theme={null}
from promptquality import Scorers
from promptquality import SupportedModels
from datetime import datetime

metrics = [
    Scorers.context_adherence, #hallucinations
]

template = """Explain {x} to a {y} year old."""

pq.run(
    project_name="test_project",
    run_name="test_run",
    dataset='data/explain.csv', # CSV has 2 columns, X and Y
    scorers=metrics,
    settings=pq.Settings(model_alias=SupportedModels.azure_chat_gpt_16k)
)
```
