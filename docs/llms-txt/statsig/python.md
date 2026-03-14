# Source: https://docs.statsig.com/ai-evals/python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Python AI SDK

> Statsig's Python SDK for AI Application Configuration & Telemetry

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-ai-python" target="_blank" rel="noreferrer">Python AI SDK on Github</a>,
  <a href="https://pypi.org/project/statsig-ai" target="_blank" rel="noreferrer">PyPI Package</a>
</Callout>

<Warning>
  This SDK is available in an open beta, and its methods may change. We encourage you to reach out on [Slack](https://statsig.com/slack) for help getting setup, and so we can communicate changes.
</Warning>

## Overview

The Statsig Python AI SDK lets you manage your prompts, online and offline evals, and debug your LLM applications in production. It depends upon the [Statsig Python Server SDK](/server-core/python-core), but provides convenient hooks for AI-specific functionality.

<Steps>
  <Step title="Install the SDK">
    <CodeGroup>
      ```python pip theme={null}
      pip install statsig-ai
      ```

      ```python poetry theme={null}
      poetry add statsig-ai
      ```

      ```python pipenv theme={null}
      pipenv install statsig-ai
      ```
    </CodeGroup>
  </Step>

  <Step title="Initialize the SDK">
    <Tip>
      For initialization requirements in forking and WSGI servers, see the [Statsig Python Server SDK](/server-core/python-core) docs.
    </Tip>

    If you already have a Statsig instance, you can pass it into the SDK. Otherwise, we'll create an instance for you internally.

    <Tabs>
      <Tab title="Don't use Statsig">
        Initialize the AI SDK with a Server Secret Key from the Statsig console.

        <Warning>
          Server Secret Keys should always be kept private. If you expose one, you can
          disable and recreate it in the Statsig console.
        </Warning>

        ```python  theme={null}
        from statsig_ai import StatsigAI, StatsigCreateConfig

        statsig_ai = StatsigAI(statsig_source=StatsigCreateConfig(server_secret_key='YOUR_SERVER_SECRET_KEY'))
        statsig_ai.initialize().
        ```

        <Accordion title="Initializing With Options">
          Optionally, you can configure [StatsigOptions](/server-core/python-core#statsig-options) for your Statsig instance:

          ```python  theme={null}
          from statsig_ai import StatsigAI
          from statsig_python_core import StatsigOptions

          # if you want to configure any statsig options, this is optional:
          statsig_options = StatsigOptions()
          statsig_options.environment = 'production'

          statsig_ai_options.statsig_options = statsig_options

          statsig_ai = StatsigAI(statsig_source=StatsigCreateConfig(server_secret_key='YOUR_SERVER_SECRET_KEY', statsig_options=statsig_options))
          statsig_ai.initialize()

          # if you would like to use any statsig methods, you can access the statsig instance from the statsig_ai instance:
          gate = statsig_ai.get_statsig().check_gate(statsig_user, 'my_gate')
          ```
        </Accordion>
      </Tab>

      <Tab title="Already have Statsig instance">
        After installation, initialize the SDK with a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

        <Warning>
          Server Secret Keys should always be kept private. If you expose one, you can
          disable and recreate it in the Statsig console.
        </Warning>

        If you initialize this way, the AI SDK won’t handle initialization, flushing, or shutdown.

        ```python  theme={null}
        from statsig_python_core import Statsig
        from statsig_ai import StatsigAI, StatsigAttachConfig

        statsig = Statsig('YOUR_SERVER_SECRET_KEY')
        statsig.initialize()

        statsig_ai = StatsigAI(statsig_source=StatsigAttachConfig(statsig=statsig))
        statsig_ai.initialize()
        ```

        <Accordion title="Initializing With Options">
          Optionally, you can configure [StatsigOptions](/server-core/python-core#statsig-options):

          ```python  theme={null}
          from statsig_python_core import Statsig, StatsigOptions
          from statsig_ai import StatsigAI, StatsigAttachConfig

          options = StatsigOptions()
          options.environment = 'production'

          statsig = Statsig('YOUR_SERVER_SECRET_KEY', options)
          statsig.initialize()

          statsig_ai = StatsigAI(statsig_source=StatsigAttachConfig(statsig=statsig))
          statsig_ai.initialize()
          ```
        </Accordion>
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Using the SDK

### Getting a Prompt

Statsig can act as the control plane for your LLM prompts, allowing you to version and change them without deploying code. For more information, see the [Prompts](/ai-evals/prompts) documentation.

```python  theme={null}
from statsig_ai import StatsigUser

# Create a user object
user = StatsigUser(user_id='a-user')

# Get the prompt
my_prompt = statsig_ai.get_prompt(user, 'my_prompt')

# Use the live version of the prompt
live_version = my_prompt.get_live()

# Get the candidate versions of the prompt
candidate_versions = my_prompt.get_candidates()

# Use the live version of the prompt in a completion
response = openai.chat.completions.create(
    model=live_version.get_model(fallback='gpt-4'),  # optional fallback
    temperature=live_version.get_temperature(),
    max_tokens=live_version.get_max_tokens(),
    messages=[{'role': 'user', 'content': 'Your prompt here'}],
)
```

### Logging Eval Results

When running an [online eval](/ai-evals/online-evals), you can log results back to Statsig for analysis.
Provide a score between 0 and 1, along with the grader name and any useful metadata (e.g., session IDs).
Currently, you must provide the grader manually — future releases will support automated grading options.

```python  theme={null}
from statsig_ai import StatsigUser

live_prompt_version = statsig_ai.get_prompt(user, 'my_prompt').get_live()
# Create a user object
user = StatsigUser(user_id='a-user')

# Log the results of the eval
statsig_ai.log_eval_grade(user, live_prompt_version, 0.5, 'my_grader', {
    'session_id': '1234567890',
})

# flush eval grade events to statsig
statsig_ai.flush().wait()
```

### Programmatic Evaluation

Programmatic evaluation allows you to run evaluations on datasets programmatically, automatically scoring outputs and sending results to Statsig for analysis.

With programmatic evaluation, you can:

* **Run evaluations on datasets**: Process arrays, iterators, or async generators of input/expected pairs
* **Define custom tasks**: Create functions that generate outputs from inputs (supports both sync and async)
* **Score outputs**: Use single or multiple named scorer functions to evaluate outputs (supports boolean, numeric, or metadata-rich scores)
* **Use parameters**: Pass dynamic parameters to tasks using Zod schemas (Node) or dictionaries (Python)
* **Categorize data**: Group evaluation records by categories for better analysis
* **Compute summary scores**: Aggregate results across all records with custom summary functions
* **Handle errors gracefully**: Task and scorer errors are caught and reported without stopping the evaluation

The evaluation automatically sends results to Statsig, where you can view them in the console alongside your other eval data.

<Note>
  Tasks and scorers can be async functions. Data can also be provided as async
  functions, promises, or async iterators. The `expected` field in data records
  is optional; scorers can evaluate outputs without expected values. Task and
  scorer errors are automatically caught and reported in the results.
</Note>

```python  theme={null}
from statsig_ai import Eval, EvalScorerArgs, EvalDataRecord, EvalHook

# Basic evaluation with a single scorer
result = Eval(
    name='greeting_task',
    data=[
        {'input': 'world', 'expected': 'Hello world'},
        {'input': 'test', 'expected': 'Hello test'},
    ],
    task=lambda input: f'Hello {input}',
    scorer=lambda args: args.output == args.expected,
    eval_run_name='run-123',
)

# Multiple named scorers
result2 = Eval(
    name='multi_scorer_task',
    data=[
        {'input': 'world', 'expected': 'Hello world'},
        {'input': 'test', 'expected': 'Hello test'},
    ],
    task=lambda input: f'Hello {input}',
    scorer={
        'correctness': lambda args: args.output == args.expected,
        'starts_with_hello': lambda args: args.output.startswith('Hello'),
        'length_check': lambda args: len(args.output) > 5,
    },
)

# Using parameters
def task_with_params(input: str, hook: EvalHook) -> str:
    prefix = hook.parameters.get('prefix', 'Hello')
    return f'{prefix} {input}'

result3 = Eval(
    name='parameterized_task',
    data=[
        {'input': 'world', 'expected': 'Hi world'},
    ],
    task=task_with_params,
    scorer=lambda args: args.output == args.expected,
    parameters={'prefix': 'Hi', 'suffix': '!', 'number': 123},
)

# Extras: Categories and summary scores
def summary_scorer(results):
    correct = sum(1 for r in results if r.scores.get('correctness', 0.0) == 1.0)
    return {
        'accuracy': correct / len(results) if results else 0.0,
        'total': len(results),
    }

result4 = Eval(
    name='categorized_with_summary',
    data=[
        {'input': 'world', 'expected': 'Hello world', 'category': 'greeting'},
        {'input': 'test', 'expected': 'Hello test', 'category': ['greeting', 'test']},
        {'input': 'foo', 'expected': 'Goodbye foo', 'category': 'farewell'},
    ],
    task=lambda input: f'Hello {input}',
    scorer={
        'correctness': lambda args: args.output == args.expected,
    },
    summary_score_fn=summary_scorer,
)

# Using EvalDataRecord dataclass
result5 = Eval(
    name='dataclass_records',
    data=[
        EvalDataRecord(input='world', expected='Hello world'),
        EvalDataRecord(input='test', expected='Hello test'),
    ],
    task=lambda input: f'Hello {input}',
    scorer=lambda args: args.output == args.expected,
)
```

### OpenTelemetry (OTEL)

The AI SDK works with OpenTelemetry for sending telemetry to Statsig.
You can enable OTel tracing by calling the `initializeTracing` function.
You can also provide a custom `TracerProvider` to the `initializeTracing` function if you want to customize the tracing behavior.
More advanced OTel configuration and exporter support are on the way.

Otel is not supported in the Python AI SDK yet. Coming soon!

### Wrapping OpenAI

The Statsig OpenAI Wrapper automatically adds tracing and log events to your OpenAI SDK usage, giving you in-console visibility with minimal setup.

OpenAI wrapper is not supported in the Python AI SDK yet. Coming soon!

## Using other SDK methods

Whether you passed in a Statsig instance or not, you can access the Statsig instance from the statsig\_ai instance, and use its many methods:

```python  theme={null}
# Check a gate value
gate = statsig_ai.get_statsig().check_gate(statsig_user, 'my_gate')

# Log an event
statsig_ai.get_statsig().log_event(statsig_user, 'my_event', value=1)
```

Refer to the [Statsig Python SDK](/server-core/python-core) docs for more information on how to use the Core Statsig SDK methods, plus information on advanced setup + singleton usage.


Built with [Mintlify](https://mintlify.com).