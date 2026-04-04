# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/add-tags-and-metadata-to-prompt-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

```bash  theme={null}

max_tokens_tag = pq.RunTag(key="Max Tokens", value="16k", tag_type=pq.TagType.GENERIC)
```

We could then add our tag to our run, however we are choosing to create a run:

### Logging Workflows

If you are using a workflow, you can add tags to your workflow by adding the tag to the [EvaluateRun](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateRun) object.

```py  theme={null}
evaluate_run = pq.EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics, run_tags=[max_tokens_tag])
```

### Prompt Run

We can add tags to a simple Prompt run. For info on creating Prompt runs, see [Getting Started](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart)

```py  theme={null}
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

```py  theme={null}

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

```py  theme={null}

pq.GalileoPromptCallback(project_name='my_project_name',
                         scorers=[<list-of-scorers>],
                         run_tags=[max_tokens_tag])
```

## Viewing Tags in the Galileo Evaluation UI

You can then view your tags in the Galileo Evaluation UI:

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a634b28ab6cc53496e3a83b1e8fd516f" alt="Viewing Tags in the Galileo Evaluation UI" data-og-width="1792" width="1792" data-og-height="640" height="640" data-path="images/tags-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b6e80324e9d3ec7ab0e2a567b196413a 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=95c88e3924f912dbdf50dcce3bb5fcc8 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cd47cd95117f2f00f5f80330e8d5df24 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=051effd123861657c3cabe9ad43d97ee 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=7e22da2c74985369c54c017b70a24c46 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/tags-metadata.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=36f0555f820d04dd58e53574b1760679 2500w" />
