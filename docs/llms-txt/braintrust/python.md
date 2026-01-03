# Source: https://braintrust.dev/docs/reference/sdks/python.md

# Python SDK

> Python API reference for Braintrust SDK

For complete Python documentation, examples, and API reference, please see the [Braintrust SDK on GitHub](https://github.com/braintrustdata/braintrust-sdk).

## Installation

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust
```

## Functions

### Eval

A function you can use to define an evaluator. This is a convenience wrapper around the `Evaluator` class.

<ParamField path="name" type="str">
  The name of the evaluator. This corresponds to a project name in Braintrust.
</ParamField>

<ParamField path="data" type="EvalData[Input, Output]">
  Returns an iterator over the evaluation dataset. Each element of the iterator should be a `EvalCase`.
</ParamField>

<ParamField path="task" type="EvalTask[Input, Output]">
  Runs the evaluation task on a single input. The `hooks` object can be used to add metadata to the evaluation.
</ParamField>

<ParamField path="scores" type="Sequence[EvalScorer[Input, Output]]">
  A list of scorers to evaluate the results of the task. Each scorer can be a Scorer object or a function
</ParamField>

<ParamField path="experiment_name" type="Optional[str]">
  (Optional) Experiment name. If not specified, a name will be generated automatically.
</ParamField>

<ParamField path="trial_count" type="int">
  The number of times to run the evaluator per input. This is useful for evaluating applications that
</ParamField>

<ParamField path="metadata" type="Optional[Metadata]">
  (Optional) A dictionary with additional data about the test example, model outputs, or just about
</ParamField>

<ParamField path="is_public" type="bool">
  (Optional) Whether the experiment should be public. Defaults to false.
</ParamField>

<ParamField path="update" type="bool" />

<ParamField path="reporter" type="Optional[ReporterDef[Input, Output, EvalReport]]">
  (Optional) A reporter that takes an evaluator and its result and returns a report.
</ParamField>

<ParamField path="timeout" type="Optional[float]">
  (Optional) The duration, in seconds, after which to time out the evaluation.
</ParamField>

<ParamField path="max_concurrency" type="Optional[int]" />

<ParamField path="project_id" type="Optional[str]">
  (Optional) If specified, uses the given project ID instead of the evaluator's name to identify the project.
</ParamField>

<ParamField path="base_experiment_name" type="Optional[str]">
  An optional experiment name to use as a base. If specified, the new experiment will be
</ParamField>

<ParamField path="base_experiment_id" type="Optional[str]">
  An optional experiment id to use as a base. If specified, the new experiment will be
</ParamField>

<ParamField path="git_metadata_settings" type="Optional[GitMetadataSettings]">
  Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="git_metadata_settings.collect" type="Literal['all', 'none', 'some']" required />

<ParamField path="git_metadata_settings.fields" type="NotRequired[Sequence[Literal['commit', 'branch', 'tag', 'dirty', 'author_name', 'author_email', 'commit_message', 'commit_time', 'git_diff']]]" />

<ParamField path="repo_info" type="Optional[RepoInfo]">
  Optionally explicitly specify the git metadata for this experiment. This takes precedence over `git_metadata_settings` if specified.
</ParamField>

<ParamField path="repo_info.commit" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.branch" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.tag" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.dirty" type="NotRequired[Optional[bool]]" />

<ParamField path="repo_info.author_name" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.author_email" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.commit_message" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.commit_time" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.git_diff" type="NotRequired[Optional[str]]" />

<ParamField path="error_score_handler" type="Optional[ErrorScoreHandler]">
  Optionally supply a custom function to specifically handle score values when tasks or scoring functions have errored.
</ParamField>

<ParamField path="description" type="Optional[str]">
  An optional description for the experiment.
</ParamField>

<ParamField path="summarize_scores" type="bool">
  Whether to summarize the scores of the experiment after it has run.
</ParamField>

<ParamField path="no_send_logs" type="bool">
  Do not send logs to Braintrust. When True, the evaluation runs locally
</ParamField>

<ParamField path="parameters" type="Optional[EvalParameters]">
  A set of parameters that will be passed to the evaluator.
</ParamField>

<ParamField path="on_start" type="Optional[Callable[[ExperimentSummary], None]]">
  An optional callback that will be called when the evaluation starts. It receives the
</ParamField>

<ParamField path="stream" type="Optional[Callable[[SSEProgressEvent], None]]">
  A function that will be called with progress events, which can be used to
</ParamField>

<ParamField path="parent" type="Optional[str]">
  If specified, instead of creating a new experiment object, the Eval() will populate
</ParamField>

<ParamField path="state" type="Optional[BraintrustState]">
  Optional BraintrustState to use for the evaluation. If not specified, the global login state will be used.
</ParamField>

### Reporter

A function you can use to define a reporter. This is a convenience wrapper around the `ReporterDef` class.

<ParamField path="name" type="str">
  The name of the reporter.
</ParamField>

<ParamField path="report_eval" type="Callable[[Evaluator[Input, Output], EvalResultWithSummary[Input, Output], bool, bool], Union[EvalReport, Awaitable[EvalReport]]]">
  return str(result.summary)
</ParamField>

<ParamField path="report_run" type="Callable[[List[EvalReport], bool, bool], Union[bool, Awaitable[bool]]]">
  return True
</ParamField>

### current\_experiment

Returns the currently-active experiment (set by `braintrust.init(...)`). Returns None if no current experiment has been set.

### current\_logger

Returns the currently-active logger (set by `braintrust.init_logger(...)`). Returns None if no current logger has been set.

### current\_span

Return the currently-active span for logging (set by running a span under a context manager). If there is no active span, returns a no-op span object, which supports the same interface as spans but does no logging.

### flush

Flush any pending rows to the server.

### get\_prompt\_versions

Get the versions for a specific prompt.

<ParamField path="project_id" type="str">
  The ID of the project to query
</ParamField>

<ParamField path="prompt_id" type="str">
  The ID of the prompt to get versions for
</ParamField>

### get\_span\_parent\_object

Mainly for internal use. Return the parent object for starting a span in a global context. Applies precedence: current span > propagated parent string > experiment > logger.

<ParamField path="parent" type="Optional[str]" />

<ParamField path="state" type="Optional[BraintrustState]" />

### init

Log in, and then initialize a new experiment in a specified project. If the project does not exist, it will be created.

<ParamField path="project" type="Optional[str]">
  The name of the project to create the experiment in. Must specify at least one of `project` or `project_id`.
</ParamField>

<ParamField path="experiment" type="Optional[str]">
  The name of the experiment to create. If not specified, a name will be generated automatically.
</ParamField>

<ParamField path="description" type="Optional[str]">
  (Optional) An optional description of the experiment.
</ParamField>

<ParamField path="dataset" type="Optional['Dataset']">
  (Optional) A dataset to associate with the experiment. The dataset must be initialized with `braintrust.init_dataset` before passing
</ParamField>

<ParamField path="open" type="bool">
  If the experiment already exists, open it in read-only mode. Throws an error if the experiment does not already exist.
</ParamField>

<ParamField path="base_experiment" type="Optional[str]">
  An optional experiment name to use as a base. If specified, the new experiment will be summarized and compared to this experiment. Otherwise, it will pick an experiment by finding the closest ancestor on the default (e.g. main) branch.
</ParamField>

<ParamField path="is_public" type="bool">
  An optional parameter to control whether the experiment is publicly visible to anybody with the link or privately visible to only members of the organization. Defaults to private.
</ParamField>

<ParamField path="app_url" type="Optional[str]">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev).
</ParamField>

<ParamField path="api_key" type="Optional[str]">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable. If no API
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  (Optional) The name of a specific organization to connect to. This is useful if you belong to multiple.
</ParamField>

<ParamField path="metadata" type="Optional[Metadata]">
  (Optional) a dictionary with additional data about the test example, model outputs, or just about anything else that's relevant, that you can use to help find and analyze examples later. For example, you could log the `prompt`, example's `id`, or anything else that would be useful to slice/dice later. The values in `metadata` can be any JSON-serializable type, but its keys must be strings.
</ParamField>

<ParamField path="git_metadata_settings" type="Optional[GitMetadataSettings]">
  (Optional) Settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="git_metadata_settings.collect" type="Literal['all', 'none', 'some']" required />

<ParamField path="git_metadata_settings.fields" type="NotRequired[Sequence[Literal['commit', 'branch', 'tag', 'dirty', 'author_name', 'author_email', 'commit_message', 'commit_time', 'git_diff']]]" />

<ParamField path="set_current" type="bool">
  If true (the default), set the global current-experiment to the newly-created one.
</ParamField>

<ParamField path="update" type="Optional[bool]">
  If the experiment already exists, continue logging to it. If it does not exist, creates the experiment with the specified arguments.
</ParamField>

<ParamField path="project_id" type="Optional[str]">
  The id of the project to create the experiment in. This takes precedence over `project` if specified.
</ParamField>

<ParamField path="base_experiment_id" type="Optional[str]">
  An optional experiment id to use as a base. If specified, the new experiment will be summarized and compared to this. This takes precedence over `base_experiment` if specified.
</ParamField>

<ParamField path="repo_info" type="Optional[RepoInfo]">
  (Optional) Explicitly specify the git metadata for this experiment. This takes precedence over `git_metadata_settings` if specified.
</ParamField>

<ParamField path="repo_info.commit" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.branch" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.tag" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.dirty" type="NotRequired[Optional[bool]]" />

<ParamField path="repo_info.author_name" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.author_email" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.commit_message" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.commit_time" type="NotRequired[Optional[str]]" />

<ParamField path="repo_info.git_diff" type="NotRequired[Optional[str]]" />

<ParamField path="state" type="Optional[BraintrustState]">
  (Optional) A BraintrustState object to use. If not specified, will use the global state. This is for advanced use only.
</ParamField>

### init\_dataset

Create a new dataset in a specified project. If the project does not exist, it will be created.

<ParamField path="project" type="Optional[str]" />

<ParamField path="name" type="Optional[str]">
  The name of the dataset to create. If not specified, a name will be generated automatically.
</ParamField>

<ParamField path="description" type="Optional[str]">
  An optional description of the dataset.
</ParamField>

<ParamField path="version" type="Optional[Union[str, int]]">
  An optional version of the dataset (to read). If not specified, the latest version will be used.
</ParamField>

<ParamField path="app_url" type="Optional[str]">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev).
</ParamField>

<ParamField path="api_key" type="Optional[str]">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable. If no API
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  (Optional) The name of a specific organization to connect to. This is useful if you belong to multiple.
</ParamField>

<ParamField path="project_id" type="Optional[str]">
  The id of the project to create the dataset in. This takes precedence over `project` if specified.
</ParamField>

<ParamField path="metadata" type="Optional[Metadata]">
  (Optional) a dictionary with additional data about the dataset. The values in `metadata` can be any JSON-serializable type, but its keys must be strings.
</ParamField>

<ParamField path="use_output" type="bool">
  (Deprecated) If True, records will be fetched from this dataset in the legacy format, with the "expected" field renamed to "output". This option will be removed in a future version of Braintrust.
</ParamField>

<ParamField path="_internal_btql" type="Optional[Dict[str, Any]]">
  (Internal) If specified, the dataset will be created with the given BTQL filters.
</ParamField>

<ParamField path="state" type="Optional[BraintrustState]">
  (Internal) The Braintrust state to use. If not specified, will use the global state. For advanced use only.
</ParamField>

### init\_experiment

Alias for `init`

<ParamField path="args" type="Any" />

<ParamField path="kwargs" type="Any" />

### init\_function

Creates a function that can be used as either a task or scorer in the Eval framework. When used as a task, it will invoke the specified Braintrust function with the input. When used as a scorer, it will invoke the function with the scorer arguments.

<ParamField path="project_name" type="str">
  The name of the project containing the function.
</ParamField>

<ParamField path="slug" type="str">
  The slug of the function to invoke.
</ParamField>

<ParamField path="version" type="Optional[str]">
  Optional version of the function to use. Defaults to latest.
</ParamField>

### init\_logger

Create a new logger in a specified project. If the project does not exist, it will be created.

<ParamField path="project" type="Optional[str]">
  The name of the project to log into. If unspecified, will default to the Global project.
</ParamField>

<ParamField path="project_id" type="Optional[str]">
  The id of the project to log into. This takes precedence over project if specified.
</ParamField>

<ParamField path="async_flush" type="bool">
  If true (the default), log events will be batched and sent asynchronously in a background thread. If false, log events will be sent synchronously. Set to false in serverless environments.
</ParamField>

<ParamField path="app_url" type="Optional[str]">
  The URL of the Braintrust API. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev).
</ParamField>

<ParamField path="api_key" type="Optional[str]">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable. If no API
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  (Optional) The name of a specific organization to connect to. This is useful if you belong to multiple.
</ParamField>

<ParamField path="force_login" type="bool">
  Login again, even if you have already logged in (by default, the logger will not login if you are already logged in)
</ParamField>

<ParamField path="set_current" type="bool">
  If true (the default), set the global current-experiment to the newly-created one.
</ParamField>

<ParamField path="state" type="Optional[BraintrustState]" />

### invoke

Invoke a Braintrust function, returning a `BraintrustStream` or the value as a plain Python object.

<ParamField path="function_id" type="Optional[str]">
  The ID of the function to invoke.
</ParamField>

<ParamField path="version" type="Optional[str]">
  The version of the function to invoke.
</ParamField>

<ParamField path="prompt_session_id" type="Optional[str]">
  The ID of the prompt session to invoke the function from.
</ParamField>

<ParamField path="prompt_session_function_id" type="Optional[str]">
  The ID of the function in the prompt session to invoke.
</ParamField>

<ParamField path="project_name" type="Optional[str]">
  The name of the project containing the function to invoke.
</ParamField>

<ParamField path="slug" type="Optional[str]">
  The slug of the function to invoke.
</ParamField>

<ParamField path="global_function" type="Optional[str]">
  The name of the global function to invoke.
</ParamField>

<ParamField path="input" type="Any">
  The input to the function. This will be logged as the `input` field in the span.
</ParamField>

<ParamField path="messages" type="Optional[List[Any]]">
  Additional OpenAI-style messages to add to the prompt (only works for llm functions).
</ParamField>

<ParamField path="metadata" type="Optional[Dict[str, Any]]">
  Additional metadata to add to the span. This will be logged as the `metadata` field in the span.
</ParamField>

<ParamField path="tags" type="Optional[List[str]]">
  Tags to add to the span. This will be logged as the `tags` field in the span.
</ParamField>

<ParamField path="parent" type="Optional[Union[Exportable, str]]">
  The parent of the function. This can be an existing span, logger, or experiment, or
</ParamField>

<ParamField path="stream" type="bool">
  Whether to stream the function's output. If True, the function will return a
</ParamField>

<ParamField path="mode" type="Optional[ModeType]">
  The response shape of the function if returning tool calls. If "auto", will return
</ParamField>

<ParamField path="strict" type="Optional[bool]">
  Whether to use strict mode for the function. If true, the function will throw an
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  The name of the Braintrust organization to use.
</ParamField>

<ParamField path="api_key" type="Optional[str]">
  The API key to use for authentication.
</ParamField>

<ParamField path="app_url" type="Optional[str]">
  The URL of the Braintrust application.
</ParamField>

<ParamField path="force_login" type="bool">
  Whether to force a new login even if already logged in.
</ParamField>

### load\_prompt

Loads a prompt from the specified project.

<ParamField path="project" type="Optional[str]">
  The name of the project to load the prompt from. Must specify at least one of `project` or `project_id`.
</ParamField>

<ParamField path="slug" type="Optional[str]">
  The slug of the prompt to load.
</ParamField>

<ParamField path="version" type="Optional[Union[str, int]]">
  An optional version of the prompt (to read). If not specified, the latest version will be used.
</ParamField>

<ParamField path="project_id" type="Optional[str]">
  The id of the project to load the prompt from. This takes precedence over `project` if specified.
</ParamField>

<ParamField path="id" type="Optional[str]">
  The id of a specific prompt to load. If specified, this takes precedence over all other parameters (project, slug, version).
</ParamField>

<ParamField path="defaults" type="Optional[Mapping[str, Any]]">
  (Optional) A dictionary of default values to use when rendering the prompt. Prompt values will override these defaults.
</ParamField>

<ParamField path="no_trace" type="bool">
  If true, do not include logging metadata for this prompt when build() is called.
</ParamField>

<ParamField path="environment" type="Optional[str]">
  The environment to load the prompt from. Cannot be used together with version.
</ParamField>

<ParamField path="app_url" type="Optional[str]">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev).
</ParamField>

<ParamField path="api_key" type="Optional[str]">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable. If no API
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  (Optional) The name of a specific organization to connect to. This is useful if you belong to multiple.
</ParamField>

### log

Log a single event to the current experiment. The event will be batched and uploaded behind the scenes.

<ParamField path="event" type="Any" />

### login

Log into Braintrust. This will prompt you for your API token, which you can find at [https://www.braintrust.dev/app/token](https://www.braintrust.dev/app/token). This method is called automatically by `init()`.

<ParamField path="app_url" type="Optional[str]">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev).
</ParamField>

<ParamField path="api_key" type="Optional[str]">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable. If no API
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  (Optional) The name of a specific organization to connect to. This is useful if you belong to multiple.
</ParamField>

<ParamField path="force_login" type="bool">
  Login again, even if you have already logged in (by default, this function will exit quickly if you have already logged in)
</ParamField>

### parent\_context

Context manager to temporarily set the parent context for spans.

<ParamField path="parent" type="Optional[str]">
  The parent string to set during the context
</ParamField>

<ParamField path="state" type="Optional[BraintrustState]">
  Optional BraintrustState to use. If not provided, uses the global state.
</ParamField>

### parse\_stream

Parse a BraintrustStream into its final value.

<ParamField path="stream" type="BraintrustStream">
  The BraintrustStream to parse.
</ParamField>

### patch\_litellm

Patch LiteLLM to add Braintrust tracing.

### permalink

Format a permalink to the Braintrust application for viewing the span represented by the provided `slug`.

<ParamField path="slug" type="str">
  The identifier generated from `Span.export`.
</ParamField>

<ParamField path="org_name" type="Optional[str]">
  The org name to use. If not provided, the org name will be inferred from the global login state.
</ParamField>

<ParamField path="app_url" type="Optional[str]">
  The app URL to use. If not provided, the app URL will be inferred from the global login state.
</ParamField>

### prettify\_params

Clean up parameters by filtering out NOT\_GIVEN values and serializing response\_format.

<ParamField path="params" type="dict[str, Any]" />

### serialize\_response\_format

Serialize response format for logging.

<ParamField path="response_format" type="Any" />

### set\_http\_adapter

Specify a custom HTTP adapter to use for all network requests. This is useful for setting custom retry policies, timeouts, etc. Braintrust uses the `requests` library, so the adapter should be an instance of `requests.adapters.HTTPAdapter`. Alternatively, consider sub-classing our `RetryRequestExceptionsAdapter` to get automatic retries on network-related exceptions.

<ParamField path="adapter" type="HTTPAdapter">
  The adapter to use.
</ParamField>

### set\_masking\_function

Set a global masking function that will be applied to all logged data before sending to Braintrust. The masking function will be applied after records are merged but before they are sent to the backend.

<ParamField path="masking_function" type="Optional[Callable[[Any], Any]]">
  A function that takes a JSON-serializable object and returns a masked version.
</ParamField>

### set\_thread\_pool\_max\_workers

Set the maximum number of threads to use for running evaluators. By default, this is the number of CPUs on the machine.

<ParamField path="max_workers" type="Any" />

### span\_components\_to\_object\_id

Utility function to resolve the object ID of a SpanComponentsV4 object. This function may trigger a login to braintrust if the object ID is encoded lazily.

<ParamField path="components" type="SpanComponentsV4" />

### start\_span

Lower-level alternative to `@traced` for starting a span at the toplevel. It creates a span under the first active object (using the same precedence order as `@traced`), or if `parent` is specified, under the specified parent row, or returns a no-op span object.

<ParamField path="name" type="Optional[str]" />

<ParamField path="type" type="Optional[SpanTypeAttribute]" />

<ParamField path="span_attributes" type="Optional[Union[SpanAttributes, Mapping[str, Any]]]" />

<ParamField path="start_time" type="Optional[float]" />

<ParamField path="set_current" type="Optional[bool]" />

<ParamField path="parent" type="Optional[str]" />

<ParamField path="propagated_event" type="Optional[Dict[str, Any]]" />

<ParamField path="state" type="Optional[BraintrustState]" />

<ParamField path="event" type="Any" />

### summarize

Summarize the current experiment, including the scores (compared to the closest reference experiment) and metadata.

<ParamField path="summarize_scores" type="bool">
  Whether to summarize the scores. If False, only the metadata will be returned.
</ParamField>

<ParamField path="comparison_experiment_id" type="Optional[str]">
  The experiment to compare against. If None, the most recent experiment on the comparison\_commit will be used.
</ParamField>

### traced

Decorator to trace the wrapped function when used without parentheses.

<ParamField path="f" type="F" />

### update\_span

Update a span using the output of `span.export()`. It is important that you only resume updating to a span once the original span has been fully written and flushed, since otherwise updates to the span may conflict with the original span.

<ParamField path="exported" type="str">
  The output of `span.export()`.
</ParamField>

<ParamField path="event" type="Any" />

### wrap\_anthropic

Wrap an `Anthropic` object (or AsyncAnthropic) to add tracing. If Braintrust is not configured, this is a no-op. If this is not an `Anthropic` object, this function is a no-op.

<ParamField path="client" type="Any" />

### wrap\_litellm

Wrap the litellm module to add tracing. If Braintrust is not configured, nothing will be traced.

<ParamField path="litellm_module" type="Any">
  The litellm module
</ParamField>

### wrap\_openai

Wrap the openai module (pre v1) or OpenAI instance (post v1) to add tracing. If Braintrust is not configured, nothing will be traced. If this is not an `OpenAI` object, this function is a no-op.

<ParamField path="openai" type="Any">
  The openai module or OpenAI object
</ParamField>

## Classes

### AsyncResponseWrapper

Wrapper that properly preserves async context manager behavior for OpenAI responses.

<span class="text-sm">Methods</span>

`__init__()`

### AsyncScorerLike

Protocol for asynchronous scorers that implement the eval\_async interface. The framework will prefer this interface if available.

### Attachment

Represents an attachment to be uploaded and the associated metadata.

<span class="text-sm">Methods</span>

`__init__()`, `reference()`, `data()`, `upload()`, `debug_info()`

### BaseExperiment

Use this to specify that the dataset should actually be the data from a previous (base) experiment. If you do not specify a name, Braintrust will automatically figure out the best base experiment to use based on your git history (or fall back to timestamps).

<span class="text-sm">Properties</span>

<ParamField path="name" type="Optional[str]" />

### BraintrustConsoleChunk

A console chunk from a Braintrust stream.

<span class="text-sm">Properties</span>

<ParamField path="message" type="str" />

<ParamField path="stream" type="Literal['stderr', 'stdout']" />

<ParamField path="type" type="Literal['console']" />

### BraintrustErrorChunk

An error chunk from a Braintrust stream.

<span class="text-sm">Properties</span>

<ParamField path="data" type="str" />

<ParamField path="type" type="Literal['error']" />

### BraintrustInvokeError

An error that occurs during a Braintrust stream.

### BraintrustJsonChunk

A chunk of JSON data from a Braintrust stream.

<span class="text-sm">Properties</span>

<ParamField path="data" type="str" />

<ParamField path="type" type="Literal['json_delta']" />

### BraintrustProgressChunk

A progress chunk from a Braintrust stream.

<span class="text-sm">Properties</span>

<ParamField path="data" type="str" />

<ParamField path="id" type="str" />

<ParamField path="object_type" type="str" />

<ParamField path="format" type="str" />

<ParamField path="output_type" type="str" />

<ParamField path="name" type="str" />

<ParamField path="event" type="Literal['json_delta', 'text_delta', 'reasoning_delta']" />

<ParamField path="type" type="Literal['progress']" />

### BraintrustStream

A Braintrust stream. This is a wrapper around a generator of `BraintrustStreamChunk`, with utility methods to make them easy to log and convert into various formats.

<span class="text-sm">Methods</span>

`__init__()`, `copy()`, `final_value()`

### BraintrustTextChunk

A chunk of text data from a Braintrust stream.

<span class="text-sm">Properties</span>

<ParamField path="data" type="str" />

<ParamField path="type" type="Literal['text_delta']" />

### CodeFunction

A generic callable, with metadata.

<span class="text-sm">Properties</span>

<ParamField path="project" type="'Project'" />

<ParamField path="handler" type="Callable[..., Any]" />

<ParamField path="name" type="str" />

<ParamField path="slug" type="str" />

<ParamField path="type_" type="str" />

<ParamField path="description" type="Optional[str]" />

<ParamField path="parameters" type="Any" />

<ParamField path="returns" type="Any" />

<ParamField path="if_exists" type="Optional[IfExists]" />

<ParamField path="metadata" type="Optional[Dict[str, Any]]" />

### CodePrompt

A prompt defined in code, with metadata.

<span class="text-sm">Properties</span>

<ParamField path="project" type="'Project'" />

<ParamField path="name" type="str" />

<ParamField path="slug" type="str" />

<ParamField path="prompt" type="PromptData" />

<ParamField path="tool_functions" type="List[Union[CodeFunction, SavedFunctionId]]" />

<ParamField path="description" type="Optional[str]" />

<ParamField path="function_type" type="Optional[str]" />

<ParamField path="id" type="Optional[str]" />

<ParamField path="if_exists" type="Optional[IfExists]" />

<ParamField path="metadata" type="Optional[Dict[str, Any]]" />

<span class="text-sm">Methods</span>

`to_function_definition()`

### CompletionWrapper

Wrapper for LiteLLM completion functions with tracing support.

<span class="text-sm">Methods</span>

`__init__()`, `completion()`

### DataSummary

Summary of a dataset's data.

<span class="text-sm">Properties</span>

<ParamField path="new_records" type="int" />

<ParamField path="total_records" type="int" />

### Dataset

A dataset is a collection of records, such as model inputs and outputs, which represent data you can use to evaluate and fine-tune models. You can log production data to datasets, curate them with interesting examples, edit/delete records, and run evaluations against them.

<span class="text-sm">Methods</span>

`__init__()`, `id()`, `name()`, `data()`, `project()`, `logging_state()`, `insert()`, `update()`, `delete()`, `summarize()`, `close()`, `flush()`

### DatasetSummary

Summary of a dataset's scores and metadata.

<span class="text-sm">Properties</span>

<ParamField path="project_name" type="str" />

<ParamField path="dataset_name" type="str" />

<ParamField path="project_url" type="str" />

<ParamField path="dataset_url" type="str" />

<ParamField path="data_summary" type="Optional[DataSummary]" />

### EmbeddingWrapper

Wrapper for LiteLLM embedding functions.

<span class="text-sm">Methods</span>

`__init__()`, `embedding()`

### EvalCase

An evaluation case. This is a single input to the evaluation task, along with an optional expected output, metadata, and tags.

<span class="text-sm">Properties</span>

<ParamField path="input" type="Input" />

<ParamField path="expected" type="Optional[Output]" />

<ParamField path="metadata" type="Optional[Metadata]" />

<ParamField path="tags" type="Optional[Sequence[str]]" />

<ParamField path="id" type="Optional[str]" />

<ParamField path="created" type="Optional[str]" />

### EvalHooks

An object that can be used to add metadata to an evaluation. This is passed to the `task` function.

<span class="text-sm">Methods</span>

`metadata()`, `expected()`, `span()`, `trial_index()`, `tags()`, `report_progress()`, `meta()`, `parameters()`

### EvalResult

The result of an evaluation. This includes the input, expected output, actual output, and metadata.

<span class="text-sm">Properties</span>

<ParamField path="input" type="Input" />

<ParamField path="output" type="Output" />

<ParamField path="scores" type="Dict[str, Optional[float]]" />

<ParamField path="expected" type="Optional[Output]" />

<ParamField path="metadata" type="Optional[Metadata]" />

<ParamField path="tags" type="Optional[List[str]]" />

<ParamField path="error" type="Optional[Exception]" />

<ParamField path="exc_info" type="Optional[str]" />

### EvalScorerArgs

Arguments passed to an evaluator scorer. This includes the input, expected output, actual output, and metadata.

<span class="text-sm">Properties</span>

<ParamField path="input" type="Input" />

<ParamField path="output" type="Output" />

<ParamField path="expected" type="Optional[Output]" />

<ParamField path="metadata" type="Optional[Metadata]" />

### Evaluator

An evaluator is an abstraction that defines an evaluation dataset, a task to run on the dataset, and a set of scorers to evaluate the results of the task. Each method attribute can be synchronous or asynchronous (for optimal performance, it is recommended to provide asynchronous implementations).

<span class="text-sm">Properties</span>

<ParamField path="project_name" type="str" />

<ParamField path="eval_name" type="str" />

<ParamField path="data" type="EvalData[Input, Output]" />

<ParamField path="task" type="EvalTask[Input, Output]" />

<ParamField path="scores" type="List[EvalScorer[Input, Output]]" />

<ParamField path="experiment_name" type="Optional[str]" />

<ParamField path="metadata" type="Optional[Metadata]" />

<ParamField path="trial_count" type="int" />

<ParamField path="is_public" type="bool" />

<ParamField path="update" type="bool" />

<ParamField path="timeout" type="Optional[float]" />

<ParamField path="max_concurrency" type="Optional[int]" />

<ParamField path="project_id" type="Optional[str]" />

<ParamField path="base_experiment_name" type="Optional[str]" />

<ParamField path="base_experiment_id" type="Optional[str]" />

<ParamField path="git_metadata_settings" type="Optional[GitMetadataSettings]" />

<ParamField path="repo_info" type="Optional[RepoInfo]" />

<ParamField path="error_score_handler" type="Optional[ErrorScoreHandler]" />

<ParamField path="description" type="Optional[str]" />

<ParamField path="summarize_scores" type="bool" />

<ParamField path="parameters" type="Optional[EvalParameters]" />

### Experiment

An experiment is a collection of logged events, such as model inputs and outputs, which represent a snapshot of your application at a particular point in time. An experiment is meant to capture more than just the model you use, and includes the data you use to test, pre- and post- processing code, comparison metrics (scores), and any other metadata you want to include.

<span class="text-sm">Methods</span>

`__init__()`, `id()`, `name()`, `data()`, `project()`, `logging_state()`, `log()`, `log_feedback()`, `start_span()`, `update_span()`, `fetch_base_experiment()`, `summarize()`, `export()`, `close()`, `flush()`

### ExperimentSummary

Summary of an experiment's scores and metadata.

<span class="text-sm">Properties</span>

<ParamField path="project_name" type="str" />

<ParamField path="project_id" type="Optional[str]" />

<ParamField path="experiment_id" type="Optional[str]" />

<ParamField path="experiment_name" type="str" />

<ParamField path="project_url" type="Optional[str]" />

<ParamField path="experiment_url" type="Optional[str]" />

<ParamField path="comparison_experiment_name" type="Optional[str]" />

<ParamField path="scores" type="Dict[str, ScoreSummary]" />

<ParamField path="metrics" type="Dict[str, MetricSummary]" />

### ExternalAttachment

Represents an attachment that resides in an external object store and the associated metadata.

<span class="text-sm">Methods</span>

`__init__()`, `reference()`, `data()`, `upload()`, `debug_info()`

### JSONAttachment

A convenience class for creating attachments from JSON-serializable objects.

<span class="text-sm">Methods</span>

`__init__()`

### LiteLLMWrapper

Main wrapper for the LiteLLM module.

<span class="text-sm">Methods</span>

`__init__()`, `completion()`, `responses()`, `embedding()`, `moderation()`

### MetricSummary

Summary of a metric's performance.

<span class="text-sm">Properties</span>

<ParamField path="name" type="str" />

<ParamField path="metric" type="Union[float, int]" />

<ParamField path="unit" type="str" />

<ParamField path="improvements" type="Optional[int]" />

<ParamField path="regressions" type="Optional[int]" />

<ParamField path="diff" type="Optional[float]" />

### ModerationWrapper

Wrapper for LiteLLM moderation functions.

<span class="text-sm">Methods</span>

`__init__()`, `moderation()`

### NamedWrapper

Wrapper that preserves access to the original wrapped object's attributes.

<span class="text-sm">Methods</span>

`__init__()`

### Project

A handle to a Braintrust project.

<span class="text-sm">Methods</span>

`__init__()`, `add_code_function()`, `add_prompt()`, `publish()`

### ProjectBuilder

Creates handles to Braintrust projects.

<span class="text-sm">Methods</span>

`create()`

### Prompt

A prompt object consists of prompt text, a model, and model parameters (such as temperature), which can be used to generate completions or chat messages. The prompt object supports calling `.build()` which uses mustache templating to build the prompt with the given formatting options and returns a plain dictionary that includes the built prompt and arguments. The dictionary can be passed as kwargs to the OpenAI client or modified as you see fit.

<span class="text-sm">Methods</span>

`__init__()`, `from_prompt_data()`, `id()`, `name()`, `slug()`, `prompt()`, `version()`, `options()`, `build()`

### PromptBuilder

Builder to create a prompt in Braintrust.

<span class="text-sm">Methods</span>

`__init__()`, `create()`, `create()`, `create()`

### ReadonlyAttachment

A readonly alternative to `Attachment`, which can be used for fetching already-uploaded Attachments.

<span class="text-sm">Methods</span>

`__init__()`, `data()`, `metadata()`, `status()`

### ReadonlyExperiment

A read-only view of an experiment, initialized by passing `open=True` to `init()`.

<span class="text-sm">Methods</span>

`__init__()`, `id()`, `logging_state()`, `as_dataset()`

### RepoInfo

Information about the current HEAD of the repo.

<span class="text-sm">Properties</span>

<ParamField path="commit" type="Optional[str]" />

<ParamField path="branch" type="Optional[str]" />

<ParamField path="tag" type="Optional[str]" />

<ParamField path="dirty" type="Optional[bool]" />

<ParamField path="author_name" type="Optional[str]" />

<ParamField path="author_email" type="Optional[str]" />

<ParamField path="commit_message" type="Optional[str]" />

<ParamField path="commit_time" type="Optional[str]" />

<ParamField path="git_diff" type="Optional[str]" />

### ReporterDef

A reporter takes an evaluator and its result and returns a report.

<span class="text-sm">Properties</span>

<ParamField path="name" type="str" />

<ParamField path="report_eval" type="Callable[[Evaluator[Input, Output], EvalResultWithSummary[Input, Output], bool, bool], Union[EvalReport, Awaitable[EvalReport]]]" />

<ParamField path="report_run" type="Callable[[List[EvalReport], bool, bool], Union[bool, Awaitable[bool]]]" />

### ResponsesWrapper

Wrapper for LiteLLM responses functions with tracing support.

<span class="text-sm">Methods</span>

`__init__()`, `responses()`

### RetryRequestExceptionsAdapter

An HTTP adapter that automatically retries requests on connection exceptions.

<span class="text-sm">Methods</span>

`__init__()`, `send()`

### SSEProgressEvent

A progress event that can be reported during task execution, specifically for SSE (Server-Sent Events) streams. This is a subclass of TaskProgressEvent with additional fields for SSE-specific metadata.

<span class="text-sm">Properties</span>

<ParamField path="id" type="str" />

<ParamField path="object_type" type="str" />

<ParamField path="origin" type="ObjectReference" />

<ParamField path="name" type="str" />

### ScoreSummary

Summary of a score's performance.

<span class="text-sm">Properties</span>

<ParamField path="name" type="str" />

<ParamField path="score" type="float" />

<ParamField path="improvements" type="Optional[int]" />

<ParamField path="regressions" type="Optional[int]" />

<ParamField path="diff" type="Optional[float]" />

### ScorerBuilder

Builder to create a scorer in Braintrust.

<span class="text-sm">Methods</span>

`__init__()`, `create()`, `create()`, `create()`, `create()`

### Span

A Span encapsulates logged data and metrics for a unit of work. This interface is shared by all span implementations.

<span class="text-sm">Methods</span>

`id()`, `log()`, `log_feedback()`, `start_span()`, `export()`, `link()`, `permalink()`, `end()`, `flush()`, `close()`, `set_attributes()`, `set_current()`, `unset_current()`

### SpanIds

The three IDs that define a span's position in the trace tree.

<span class="text-sm">Properties</span>

<ParamField path="span_id" type="str" />

<ParamField path="root_span_id" type="str" />

<ParamField path="span_parents" type="Optional[List[str]]" />

### SpanImpl

Primary implementation of the `Span` interface. See the `Span` interface for full details on each method.

<span class="text-sm">Properties</span>

<ParamField path="can_set_current" type="bool" />

<span class="text-sm">Methods</span>

`__init__()`, `id()`, `set_attributes()`, `log()`, `log_internal()`, `log_feedback()`, `start_span()`, `end()`, `export()`, `link()`, `permalink()`, `close()`, `flush()`, `set_current()`, `unset_current()`

### SyncScorerLike

Protocol for synchronous scorers that implement the callable interface. This is the most common interface and is used when no async version is available.

<span class="text-sm">Methods</span>

`__call__()`

### TaskProgressEvent

Progress event that can be reported during task execution.

<span class="text-sm">Properties</span>

<ParamField path="format" type="FunctionFormat" />

<ParamField path="output_type" type="FunctionOutputType" />

<ParamField path="event" type="Literal['reasoning_delta', 'text_delta', 'json_delta', 'error', 'console', 'start', 'done', 'progress']" />

<ParamField path="data" type="str" />

### ToolBuilder

Builder to create a tool in Braintrust.

<span class="text-sm">Methods</span>

`__init__()`, `create()`

### TracedMessageStream

TracedMessageStream wraps both sync and async message streams. Obviously only one makes sense at a time

<span class="text-sm">Methods</span>

`__init__()`


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt