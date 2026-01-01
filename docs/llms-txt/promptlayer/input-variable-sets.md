# Source: https://docs.promptlayer.com/features/prompt-registry/input-variable-sets.md

# Input Variable Sets

Input Variable Sets allow you to save and reuse collections of input variables across prompts and agents. Instead of re-entering the same variable values repeatedly, you can create named sets and apply them wherever needed.

## What are Input Variable Sets?

An Input Variable Set is a named collection of key-value pairs that can be stored in your workspace and reused across different contexts. Think of them as saved inputs for your prompt templates.

For example, if you frequently test prompts with the same customer data or use cases, you can save those variable values as a set and quickly apply them to any prompt template.

## Creating Input Variable Sets

You can create Input Variable Sets from several locations in PromptLayer:

### From the Prompt Editor

1. Open any prompt template with [template variables](/features/prompt-registry/template-variables)
2. Fill in your input variables with the values you want to save
3. Click the **Save** button in the input variables section
4. Name your variable set and choose a folder location
5. Click **Save** to create the set

<img src="https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=3f61da0377d20fbd2814ba49e59eb32e" alt="Saving input variables from prompt editor" data-og-width="1568" width="1568" data-og-height="863" height="863" data-path="images/save-input-variable-set.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?w=280&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=8570d2b16409bda54d4e78e6d28547a1 280w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?w=560&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=975ebee023cdfb18f9cd5031c49fa802 560w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?w=840&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=b6526ebabb3ab4b468f560cc1805a086 840w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?w=1100&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=9f62921f77c603fff07abb7add92a078 1100w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?w=1650&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=5016a1ad39447ec4ebef1e5d86d57d5b 1650w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/save-input-variable-set.png?w=2500&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=8f510bfaea8b537aa5964c1a0f6c7110 2500w" />

### From the Registry

You can also create Input Variable Sets directly from the Registry:

1. Navigate to the **Registry** section
2. Click **New** → **Input Variable Set**
3. Enter a name and configure your variables
4. Save to your chosen folder

<img src="https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=cd9f8e399d51e96f1772be81120d7031" alt="Creating input variable set from registry" data-og-width="1248" width="1248" data-og-height="852" height="852" data-path="images/create-input-variable-set-registry.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?w=280&fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=2895808513d1d6fc1650e81473b45b99 280w, https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?w=560&fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=45c5de1dee95c74bf90a0da1eaf2f7b7 560w, https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?w=840&fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=153f0c9518218fe1847432f347757cdf 840w, https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?w=1100&fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=6352f0f1f7058e0024e31668d552b634 1100w, https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?w=1650&fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=4f333d3e4cb7417f5b491a32a95e4300 1650w, https://mintcdn.com/promptlayer/2GbY0c4-bPoLOUuk/images/create-input-variable-set-registry.png?w=2500&fit=max&auto=format&n=2GbY0c4-bPoLOUuk&q=85&s=e818ce7807840195b2da8428efe1b35b 2500w" />

## Using Input Variable Sets

Once created, you can load saved variable sets in the prompt editor by clicking the **Load** button in the input variables section. Variable sets also work with agent executions, allowing you to apply consistent inputs for test runs and evaluations.

<img src="https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=6201294825e0fdf78df35a6e13df97f5" alt="Loading a saved input variable set" data-og-width="1220" width="1220" data-og-height="831" height="831" data-path="images/load-input-variable-set.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?w=280&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=851f75f1503c6db92fa15a6e44fbfea1 280w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?w=560&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=03a7602dbff1733ac8314f2a600c2968 560w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?w=840&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=406211b1ba2c2015d5174a07932b12e2 840w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?w=1100&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=2c402000fc1b2bbede1dfa064f858f78 1100w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?w=1650&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=3be469c87fa78589a0c3c85c817513f5 1650w, https://mintcdn.com/promptlayer/W45xF-IPqpKadK7x/images/load-input-variable-set.png?w=2500&fit=max&auto=format&n=W45xF-IPqpKadK7x&q=85&s=21734da27729fbb5674fdd3f4c21a5fa 2500w" />

## Importing and Exporting

You can import variables from various sources:

* **From Datasets**: Import variables from evaluation datasets
* **From Request Logs**: Use actual request data as variable sets
* **From Files**: Upload JSON or CSV files with variable data

Export options allow you to:

* Save sets to files for backup
* Share between workspaces
* Version control your test data

## Integration with Template Variables

Input Variable Sets work seamlessly with both [f-string and Jinja2 template formats](/features/prompt-registry/template-variables):

* Sets automatically match variable names in your templates
* Missing variables are highlighted
* Extra variables in sets are safely ignored

For more information on how to structure your template variables, see the [Template Variables documentation](/features/prompt-registry/template-variables).

## Related Documentation

* [Template Variables](/features/prompt-registry/template-variables) - Learn how to create dynamic prompts with variables
* [Datasets](/features/evaluations/datasets) - Use datasets for comprehensive evaluation
* [Playground](/why-promptlayer/playground) - Test prompts with different variable configurations


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt