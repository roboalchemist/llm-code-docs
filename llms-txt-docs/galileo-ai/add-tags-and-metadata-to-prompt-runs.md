# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/add-tags-and-metadata-to-prompt-runs.md

# Add Tags and Metadata to Prompt Runs

> While you are experimenting with your prompts you will probably be tuning many parameters.

Maybe you will run experiments with different models, model versions, vector stores, embedding models, etc.

Run Tags are an easy way to log any details of your run, that you want to view later in the Galileo Evaluation UI.

## Adding tags with `promptquality`

A tag has three key components:

* key: the name of your tag i.e model name

* value: the value in your run i.e. gpt-4

* tag\_type: the type of the tag. Currently tags can be RAG or GENERIC

If we wanted to run an experiment, using gpt with a 16k token max, we could create a tag, noting that our max tokens is 16k:

```bash

max_tokens_tag = pq.RunTag(key="Max Tokens", value="16k", tag_type=pq.TagType.GENERIC)
```

We could then add our tag to our run, however we are choosing to create a run:

### Logging Workflows

If you are using a workflow, you can add tags to your workflow by adding the tag to the [EvaluateRun](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateRun) object.

```py
evaluate_run = pq.EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics, run_tags=[max_tokens_tag])
```

### Prompt Run

We can add tags to a simple Prompt run. For info on creating Prompt runs, see [Getting Started](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart)

```py
pq.run(project_name='my_project_name',
       template=template,
       dataset=data,
       run_tags=[max_tokens_tag]
       settings=pq.Settings(model_alias='ChatGPT (16K context)',
                            temperature=0.8,
                            max_tokens=400))
```

### Prompt Sweep

We can also add tags across a Prompt sweep, with multiple templates and/or models. For info on creating Prompt sweeps, see [Prompt Sweeps](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/experiment-with-multiple-prompts)

```py

pq.run_sweep(project_name='my_project_name',
             templates=templates,
             dataset='my_dataset.csv',
             scorers=metrics,
             model_aliases=models,
             run_tags=[max_tokens_tag]
             execute=True)
```

### LangChain Callback

We can even add tags, through the GalileoPromptCallback, to more complex chain runs, with LangChain. For info on using Prompt with chains, see [Using Prompt with Chains or multi-step workflows](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents--chains-or-multi-step-workflows)

```py

pq.GalileoPromptCallback(project_name='my_project_name',
                         scorers=[<list-of-scorers>],
                         run_tags=[max_tokens_tag])
```

## Viewing Tags in the Galileo Evaluation UI

You can then view your tags in the Galileo Evaluation UI:

![Viewing Tags in the Galileo Evaluation UI](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/tags-metadata.png)
