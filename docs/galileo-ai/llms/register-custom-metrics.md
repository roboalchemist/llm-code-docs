# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Register Custom Metrics

> Galileo GenAI Studio supports Custom Metrics (programmatic or GPT-based) for all your Evaluate and Observe projects. Depending on where, when, and how you want these metrics to be executed, you have the option to choose between **Custom Scorers** and **Registered Scorers**.

## Registered Scorers

We support registering a scorer such that it can be reused across various runs, projects, modules, and users within your organization. Registered Scorers are run in the backend in an [isolated environment](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics#execution-environment) that has access to a predefined set of libraries and packages.

### Creating Your Registered Scorer

To define a registered scorer, create a Python file that has at least 2 functions and follow the function signatures as described below:

1. `scorer_fn`: The scorer function is provided the row-wise inputs and is expected to generate outputs for each response. The expected signature for this function is:

```py  theme={null}

 def scorer_fn(*, index: Union[int, str], node_input: str, node_output: str, **kwargs: Any) -> Union[float, int, bool, str, None]:
    ...
```

We support output of a floating points, integers, boolean values, and strings. Your `scorer_fn` must accept `**kwargs` as the last parameter so that your registered scorer is forward-compatible.

Here is an example with the full list of parameters supported currently. This example checks the output vs the ground truth and returns the absolute difference in length:

```py  theme={null}

 def scorer_fn(*, index: Union[int, str], node_input: str, node_output: str, node_name: Optional[str], node_type: Optional[str], node_id: Optional[UUID], tools: Optional[List[Dict[str, Any]]], dataset_variables: Dict[str, str], **kwargs: Any) -> Union[float, int, bool, str, None]:
    ground_truth = dataset_variables.get("target", "") # ground truth for row if it was provided.
    return abs(len(node_output) - len(ground_truth))
```

`node_name`, `node_type`, `node_id` and `tools` are all specific to workflows/multi step chains. `dataset_variables` contains key-value pairs of variables that are passed in from the dataset in prompt evaluation runs, but can also be used to get the target/ground truth in multi step runs. Dataset variables are not available for Evaluate workflows / Observe.

The `index` parameter is the index of the row in the dataset, `node_input` is the input to the node, and `node_output` is the output from the node.

2. `aggregator_fn`: The aggregator function is only used in Evaluate, *not Observe*. The aggregator function takes in an array of the row-wise outputs from your scorer and allows you to generate aggregates from those. The expected signature for the aggregator function is:

   ```py  theme={null}

       def aggregator_fn(*, scores: List[Union[float, int, bool, str, None]]) -> Dict[str, Union[float, int, bool, str, None]]:
           ...
   ```

   For aggregated values that you want to output from your scorer, return them as key-value pairs with the key corresponding to the label and the value.

3. (Optional, but recommended) `score_type`: The scorer\_type function is used to define the `Type` of the score that your scorer generates. The expected signature for this function is:

   ```py  theme={null}

       def score_type() -> Type[float] | Type[int] | Type[str] | Type[bool]:
       ...
   ```

   Note that the return type is a `Type` object like `float`, not the actual type itself. Defining this function is necessary for sorting and filtering by scores to work correctly. If you don't define this function, the scorer is assumed to generate `float` scores by default.

4. (Optional) `scoreable_node_types_fn`: If you want to restrict your scorer to only run on specific node types, you can define this function which returns a list of node types that your scorer should run on. The expected signature for this function is:

   ```py  theme={null}
   def scoreable_node_types_fn() -> List[str]:
           ...
   ```

   If you don't define this function, your scorer will run on `llm` and `chat` nodes by default.

   Here's an example of a `scoreable_node_types_fn` that restricts the scorer to only run on `retriever` nodes:

   ```py  theme={null}
   def scoreable_node_types_fn() -> List[str]:
       return ["retriever"]
   ```

5. (Optional) `include_llm_credentials`: If you want access to the LLM credentials for the user who created the Observe project / Evaluate run during the execution of the registered scorer. This is expected to be set as a boolean value. OpenAI credentials are the only ones that are currently supported. By default, it is assumed to be `False`. The expected signature for this property is:

   ```
   include_llm_credentials = True
   ```

   If you don't define this function, your scorer will not have access to the LLM credentials by default. If you do enable it, the credentials will be included in calls to `scorer_fn` at the keyword argument `credentials`. The credentials will be a dictionary with the keys as the name of the integration, if available, and values as the credentials. For example, if the user has an OpenAI integration, the credentials will be:

   ```json  theme={null}
   {
     "openai": {
       "api_key": "foo", // str
       "organization": "my-org-id" // Optional[str]
     }
   }
   ```

6. (Optional) `chain_aggregation`: Set this field to one of `sum`, `average`, `first` or `last` to specify how the scores across each sub-node in a chain should be aggregated to the chain-level. The aggregation This is only applicable if your scorer is used in a multi-step chain. If not specified, the default is no aggregation.

   ```py  theme={null}
   chain_aggregation = "average"
   ```

### Registering Your Scorer

Once you've created your scorer file, you can register it with the name and the scorer file:

```py  theme={null}

    registered_scorer = pq.register_scorer(scorer_name="my-scorer", scorer_file="/path/to/scorer/file.py")
```

The name you choose here will be the name with which the values for this scorer appear in the UI later.

### Using Your Registered Scorer

To use your scorer during a prompt run (or sweep), simply pass it in alongside any of the other scorers:

```py  theme={null}

    pq.run(..., scorers=[registered_scorer])
```

If you created your registered scorer in a previous session, you can also just pass in the name to the scorer instead of the object as:

```py  theme={null}

    pq.run(..., scorers=["my-scorer"])
```

### Example

For example, let's say we wanted to create a custom metric that measured the length of the response. In our Python environment, we would define a `scorer_fn` function, and an `aggregator_fn` function.

1. Create a `scorer.py` file:

```py  theme={null}
from typing import List, Dict, Type


def scorer_fn(*, response: str, **kwargs) -> int:
    return len(response)


def aggregator_fn(*, scores: List[str]) -> Dict[str, int]:
    return {
        "Total Response Length": sum(scores),
        "Average Response Length": sum(scores) / len(scores),
    }

def score_type() -> Type:
    return int

def scoreable_node_types_fn() -> List[str]:
    return ["llm", "chat"]
```

1. Register the scorer:

   ```py  theme={null}
       pq.register_scorer("response_length", "scorer.py")
   ```

2. Use the scorer in your prompt run:

   ```py  theme={null}
       pq.run(..., scorers=["response_length"])
   ```

### Execution Environment

Your scorer will be executed in a Python 3.10 environment. You can arbitrarily add additional Python libraries with the following comment snippet at the top of your scorer, with the `openai` library as an example:

```py  theme={null}
# /// script
# dependencies = [
#   "openai",
# ]
# ///
```

Please note that we regularly update the minor and patch versions of these packages. Major version updates are infrequent but if a library is critical to your scorer, please let us know and we'll provide 1+ week of warning before updating the *major* versions for those.

### What if I need to use other libraries or packages?

If you need to use other libraries or packages, you may use 'Custom Scorers'. Custom Scorers are run on your notebook environment. Because they run locally, they *won't be available* for runs created from the UI or for Observe projects.

|                                 | Registered Scorers                                                          | Custom Scorers                                          |
| ------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------- |
| Creating the custom metric      | Created from the Python client, can be activated through the UI.            | Created via the Python client                           |
| Sharing across the organization | Accessible within the Galileo console across different projects and modules | Outside Galileo, accessible only to the current project |
| Accessible modules              | Evaluate and Observe                                                        | Evaluate                                                |
| Scorer Definition               | As an independent Python file                                               | Within the notebook                                     |
| Execution Environment           | Server-side                                                                 | Within your Python environment                          |
| Python Libraries available      | Limited to a Galileo provided execution environment                         | Any library within your virtual environment             |
| Execution Resources             | Restricted by Galileo                                                       | Any resources available to your local instance          |

### How do I create a local "Custom Scorer"?

Custom scorers can be created from two Python functions (`executor` and `aggrator` function as defined below). Common types include:

1. Heuristics/custom rules: checking for regex matches or presence/absence of certain keywords or phrases.

2. model-guided: utilizing a pre-trained model to check for specific entities (e.g. PERSON, ORG), or asking an LLM to grade the quality of the output.

For example, for that registered scorer we created to calculate response length, here is the custom scorer equivalent:

Note that the naming of the functions are different: they are `**executor**` and `**aggregator**` instead of `scorer_fn` and `aggregator_fn`.

```py  theme={null}
from typing import Dict, List
from promptquality import PromptRow

def executor(row: PromptRow) -> float:
    return len(row.response)

def aggregator_fn(scores: float, indices: List[int]) -> Dict[str, float]:
    return {'Total Response Length': sum(scores),
            # You can have multiple aggregate summaries for your metric.
            'Average Response Length': sum(scores)/len(scores)}
```

```py  theme={null}
my_scorer = pq.CustomScorer(name='Response Length', executor=executor, aggregator=aggregator_fn)
```

To use your scorer, you can just pass it through your `scorers` parameter inside `pq.run` or `pq.run_sweep`, `pq.EvaluateRun`, or `pq.GalileoPromptCallback`:

```py  theme={null}

template = "Explain {{topic}} to me like I'm a 5 year old"

data = {"topic": ["Quantum Physics", "Politics", "Large Language Models"]}

pq.run(template = template, dataset = data, scorers=[my_scorer])
```

Note that custom scorer can **only** be used in the Evaluate module - if you want to use a custom metric to evaluate live traffic (Observe module), you'll need to use the registered scorers below.
