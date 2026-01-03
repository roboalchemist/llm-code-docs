# Source: https://braintrust.dev/docs/reference/sdks/typescript.md

# TypeScript SDK

> TypeScript API reference for Braintrust SDK

## Installation

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  npm install braintrust
  ```

  ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pnpm add braintrust
  ```
</CodeGroup>

## Functions

### BaseExperiment

Use this to specify that the dataset should actually be the data from a previous (base) experiment.
If you do not specify a name, Braintrust will automatically figure out the best base experiment to
use based on your git history (or fall back to timestamps).

<ParamField path="options" type="Object" />

<ParamField path="options.name" type="string">
  The name of the base experiment to use. If unspecified, Braintrust will automatically figure out the best base
  using your git history (or fall back to timestamps).
</ParamField>

### BraintrustMiddleware

Creates a Braintrust middleware for AI SDK v2 that automatically traces
generateText and streamText calls with comprehensive metadata and metrics.

<ParamField path="config" type="MiddlewareConfig">
  Configuration options for the middleware
</ParamField>

### buildLocalSummary

buildLocalSummary function

<ParamField path="evaluator" type="EvaluatorDef" />

<ParamField path="evaluator.evalName" type="string" required />

<ParamField path="evaluator.projectName" type="string" required />

<ParamField path="evaluator.baseExperimentId" type="string">
  An optional experiment id to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment. This takes precedence over `baseExperimentName` if specified.
</ParamField>

<ParamField path="evaluator.baseExperimentName" type="string">
  An optional experiment name to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment.
</ParamField>

<ParamField path="evaluator.data" type="EvalData" required>
  A function that returns a list of inputs, expected outputs, and metadata.
</ParamField>

<ParamField path="evaluator.description" type="string">
  An optional description for the experiment.
</ParamField>

<ParamField path="evaluator.errorScoreHandler" type="ErrorScoreHandler">
  Optionally supply a custom function to specifically handle score values when tasks or scoring functions have errored.
  A default implementation is exported as `defaultErrorScoreHandler` which will log a 0 score to the root span for any scorer that was not run.
</ParamField>

<ParamField path="evaluator.experimentName" type="string">
  An optional name for the experiment.
</ParamField>

<ParamField path="evaluator.gitMetadataSettings" type="Object">
  Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="evaluator.isPublic" type="boolean">
  Whether the experiment should be public. Defaults to false.
</ParamField>

<ParamField path="evaluator.maxConcurrency" type="number">
  The maximum number of tasks/scorers that will be run concurrently.
  Defaults to undefined, in which case there is no max concurrency.
</ParamField>

<ParamField path="evaluator.metadata" type="Record">
  Optional additional metadata for the experiment.
</ParamField>

<ParamField path="evaluator.parameters" type="Parameters">
  A set of parameters that will be passed to the evaluator.
  Can contain array values that will be converted to single values in the task.
</ParamField>

<ParamField path="evaluator.projectId" type="string">
  If specified, uses the given project ID instead of the evaluator's name to identify the project.
</ParamField>

<ParamField path="evaluator.repoInfo" type="null | Object">
  Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
</ParamField>

<ParamField path="evaluator.scores" type="EvalScorer[]" required>
  A set of functions that take an input, output, and expected value and return a score.
</ParamField>

<ParamField path="evaluator.signal" type="AbortSignal">
  An abort signal that can be used to stop the evaluation.
</ParamField>

<ParamField path="evaluator.state" type="BraintrustState">
  If specified, uses the logger state to initialize Braintrust objects. If unspecified, falls back
  to the global state (initialized using your API key).
</ParamField>

<ParamField path="evaluator.summarizeScores" type="boolean">
  Whether to summarize the scores of the experiment after it has run.
  Defaults to true.
</ParamField>

<ParamField path="evaluator.task" type="EvalTask" required>
  A function that takes an input and returns an output.
</ParamField>

<ParamField path="evaluator.timeout" type="number">
  The duration, in milliseconds, after which to time out the evaluation.
  Defaults to undefined, in which case there is no timeout.
</ParamField>

<ParamField path="evaluator.trialCount" type="number">
  The number of times to run the evaluator per input. This is useful for evaluating applications that
  have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the
  variance in the results.
</ParamField>

<ParamField path="evaluator.update" type="boolean">
  Whether to update an existing experiment with `experiment_name` if one exists. Defaults to false.
</ParamField>

<ParamField path="results" type="EvalResult[]" />

### createFinalValuePassThroughStream

Create a stream that passes through the final value of the stream. This is
used to implement `BraintrustStream.finalValue()`.

<ParamField path="onFinal" type="Object">
  A function to call with the final value of the stream.
</ParamField>

<ParamField path="onError" type="Object" />

### currentExperiment

Returns the currently-active experiment (set by [`init`](#init)). Returns undefined if no current experiment has been set.

<ParamField path="options" type="OptionalStateArg" />

### currentLogger

Returns the currently-active logger (set by [`initLogger`](#initlogger)). Returns undefined if no current logger has been set.

<ParamField path="options" type="unknown" />

### currentSpan

Return the currently-active span for logging (set by one of the `traced` methods). If there is no active span, returns a no-op span object, which supports the same interface as spans but does no logging.

See [`Span`](#span) for full details.

<ParamField path="options" type="OptionalStateArg" />

### deepCopyEvent

Creates a deep copy of the given event. Replaces references to user objects
with placeholder strings to ensure serializability, except for
[`Attachment`](#attachment) and [`ExternalAttachment`](#externalattachment) objects, which are preserved
and not deep-copied.

<ParamField path="event" type="T" />

### defaultErrorScoreHandler

defaultErrorScoreHandler function

<ParamField path="args" type="Object" />

<ParamField path="args.data" type="EvalCase" required />

<ParamField path="args.rootSpan" type="Span" required />

<ParamField path="args.unhandledScores" type="string[]" required />

### deserializePlainStringAsJSON

deserializePlainStringAsJSON function

<ParamField path="s" type="string" />

### devNullWritableStream

devNullWritableStream function

### Eval

Eval function

<ParamField path="name" type="string" />

<ParamField path="evaluator" type="Evaluator" />

<ParamField path="evaluator.baseExperimentId" type="string">
  An optional experiment id to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment. This takes precedence over `baseExperimentName` if specified.
</ParamField>

<ParamField path="evaluator.baseExperimentName" type="string">
  An optional experiment name to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment.
</ParamField>

<ParamField path="evaluator.data" type="EvalData" required>
  A function that returns a list of inputs, expected outputs, and metadata.
</ParamField>

<ParamField path="evaluator.description" type="string">
  An optional description for the experiment.
</ParamField>

<ParamField path="evaluator.errorScoreHandler" type="ErrorScoreHandler">
  Optionally supply a custom function to specifically handle score values when tasks or scoring functions have errored.
  A default implementation is exported as `defaultErrorScoreHandler` which will log a 0 score to the root span for any scorer that was not run.
</ParamField>

<ParamField path="evaluator.experimentName" type="string">
  An optional name for the experiment.
</ParamField>

<ParamField path="evaluator.gitMetadataSettings" type="Object">
  Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="evaluator.isPublic" type="boolean">
  Whether the experiment should be public. Defaults to false.
</ParamField>

<ParamField path="evaluator.maxConcurrency" type="number">
  The maximum number of tasks/scorers that will be run concurrently.
  Defaults to undefined, in which case there is no max concurrency.
</ParamField>

<ParamField path="evaluator.metadata" type="Record">
  Optional additional metadata for the experiment.
</ParamField>

<ParamField path="evaluator.parameters" type="Parameters">
  A set of parameters that will be passed to the evaluator.
  Can contain array values that will be converted to single values in the task.
</ParamField>

<ParamField path="evaluator.projectId" type="string">
  If specified, uses the given project ID instead of the evaluator's name to identify the project.
</ParamField>

<ParamField path="evaluator.repoInfo" type="null | Object">
  Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
</ParamField>

<ParamField path="evaluator.scores" type="EvalScorer[]" required>
  A set of functions that take an input, output, and expected value and return a score.
</ParamField>

<ParamField path="evaluator.signal" type="AbortSignal">
  An abort signal that can be used to stop the evaluation.
</ParamField>

<ParamField path="evaluator.state" type="BraintrustState">
  If specified, uses the logger state to initialize Braintrust objects. If unspecified, falls back
  to the global state (initialized using your API key).
</ParamField>

<ParamField path="evaluator.summarizeScores" type="boolean">
  Whether to summarize the scores of the experiment after it has run.
  Defaults to true.
</ParamField>

<ParamField path="evaluator.task" type="EvalTask" required>
  A function that takes an input and returns an output.
</ParamField>

<ParamField path="evaluator.timeout" type="number">
  The duration, in milliseconds, after which to time out the evaluation.
  Defaults to undefined, in which case there is no timeout.
</ParamField>

<ParamField path="evaluator.trialCount" type="number">
  The number of times to run the evaluator per input. This is useful for evaluating applications that
  have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the
  variance in the results.
</ParamField>

<ParamField path="evaluator.update" type="boolean">
  Whether to update an existing experiment with `experiment_name` if one exists. Defaults to false.
</ParamField>

<ParamField path="reporterOrOpts" type="string | ReporterDef | EvalOptions" />

### flush

Flush any pending rows to the server.

<ParamField path="options" type="OptionalStateArg" />

### getContextManager

getContextManager function

### getIdGenerator

Factory function that creates a new ID generator instance each time.

This eliminates global state and makes tests parallelizable.
Each caller gets their own generator instance.

### getPromptVersions

Get the versions for a prompt.

<ParamField path="projectId" type="string">
  The ID of the project to query
</ParamField>

<ParamField path="promptId" type="string">
  The ID of the prompt to get versions for
</ParamField>

### getSpanParentObject

Mainly for internal use. Return the parent object for starting a span in a global context.
Applies precedence: current span > propagated parent string > experiment > logger.

<ParamField path="options" type="unknown" />

<ParamField path="options.parent" type="string" />

### init

Log in, and then initialize a new experiment in a specified project. If the project does not exist, it will be created.

<ParamField path="options" type="Readonly">
  Options for configuring init().
</ParamField>

<ParamField path="options.project" type="string" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.baseExperiment" type="string" />

<ParamField path="options.baseExperimentId" type="string" />

<ParamField path="options.dataset" type="AnyDataset" />

<ParamField path="options.description" type="string" />

<ParamField path="options.experiment" type="string" />

<ParamField path="options.gitMetadataSettings" type="GitMetadataSettings" />

<ParamField path="options.isPublic" type="boolean" />

<ParamField path="options.metadata" type="Record" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.repoInfo" type="RepoInfo" />

<ParamField path="options.setCurrent" type="boolean" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.update" type="boolean" />

### initDataset

Create a new dataset in a specified project. If the project does not exist, it will be created.

<ParamField path="options" type="Readonly">
  Options for configuring initDataset().
</ParamField>

<ParamField path="options.project" type="string" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.dataset" type="string" />

<ParamField path="options.description" type="string" />

<ParamField path="options.metadata" type="Record" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.version" type="string" />

### initExperiment

Alias for init(options).

<ParamField path="options" type="Readonly" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.baseExperiment" type="string" />

<ParamField path="options.baseExperimentId" type="string" />

<ParamField path="options.dataset" type="AnyDataset" />

<ParamField path="options.description" type="string" />

<ParamField path="options.experiment" type="string" />

<ParamField path="options.gitMetadataSettings" type="GitMetadataSettings" />

<ParamField path="options.isPublic" type="boolean" />

<ParamField path="options.metadata" type="Record" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.repoInfo" type="RepoInfo" />

<ParamField path="options.setCurrent" type="boolean" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.update" type="boolean" />

### initFunction

Creates a function that can be used as a task or scorer in the Braintrust evaluation framework.
The returned function wraps a Braintrust function and can be passed directly to Eval().

When used as a task:

```ts  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const myFunction = initFunction({projectName: "myproject", slug: "myfunction"});
await Eval("test", {
  task: myFunction,
  data: testData,
  scores: [...]
});
```

When used as a scorer:

```ts  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const myScorer = initFunction({projectName: "myproject", slug: "myscorer"});
await Eval("test", {
  task: someTask,
  data: testData,
  scores: [myScorer]
});
```

<ParamField path="options" type="Object">
  Options for the function.
</ParamField>

<ParamField path="options.projectName" type="string" required>
  The project name containing the function.
</ParamField>

<ParamField path="options.slug" type="string" required>
  The slug of the function to invoke.
</ParamField>

<ParamField path="options.version" type="string">
  Optional version of the function to use. Defaults to latest.
</ParamField>

### initLogger

Create a new logger in a specified project. If the project does not exist, it will be created.

<ParamField path="options" type="Readonly">
  Additional options for configuring init().
</ParamField>

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.orgProjectMetadata" type="OrgProjectMetadata" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.projectName" type="string" />

<ParamField path="options.setCurrent" type="boolean" />

<ParamField path="options.state" type="BraintrustState" />

### invoke

Invoke a Braintrust function, returning a `BraintrustStream` or the value as a plain
Javascript object.

<ParamField path="args" type="unknown">
  The arguments for the function (see [`InvokeFunctionArgs`](#invokefunctionargs) for more details).
</ParamField>

<ParamField path="args.function_id" type="string">
  The ID of the function to invoke.
</ParamField>

<ParamField path="args.globalFunction" type="string">
  The name of the global function to invoke.
</ParamField>

<ParamField path="args.input" type="Input" required>
  The input to the function. This will be logged as the `input` field in the span.
</ParamField>

<ParamField path="args.messages" type="Object | Object | Object | Object | Object | Object | Object[]">
  Additional OpenAI-style messages to add to the prompt (only works for llm functions).
</ParamField>

<ParamField path="args.metadata" type="Record">
  Additional metadata to add to the span. This will be logged as the `metadata` field in the span.
  It will also be available as the \{\{metadata}} field in the prompt and as the `metadata` argument
  to the function.
</ParamField>

<ParamField path="args.mode" type="null | &#x22;auto&#x22; | &#x22;parallel&#x22;">
  The mode of the function. If "auto", will return a string if the function returns a string,
  and a JSON object otherwise. If "parallel", will return an array of JSON objects with one
  object per tool call.
</ParamField>

<ParamField path="args.parent" type="string | Exportable">
  The parent of the function. This can be an existing span, logger, or experiment, or
  the output of `.export()` if you are distributed tracing. If unspecified, will use
  the same semantics as `traced()` to determine the parent and no-op if not in a tracing
  context.
</ParamField>

<ParamField path="args.projectName" type="string">
  The name of the project containing the function to invoke.
</ParamField>

<ParamField path="args.promptSessionFunctionId" type="string">
  The ID of the function in the prompt session to invoke.
</ParamField>

<ParamField path="args.promptSessionId" type="string">
  The ID of the prompt session to invoke the function from.
</ParamField>

<ParamField path="args.schema" type="unknown">
  A Zod schema to validate the output of the function and return a typed value. This
  is only used if `stream` is false.
</ParamField>

<ParamField path="args.slug" type="string">
  The slug of the function to invoke.
</ParamField>

<ParamField path="args.state" type="BraintrustState">
  (Advanced) This parameter allows you to pass in a custom login state. This is useful
  for multi-tenant environments where you are running functions from different Braintrust
  organizations.
</ParamField>

<ParamField path="args.stream" type="Stream">
  Whether to stream the function's output. If true, the function will return a
  `BraintrustStream`, otherwise it will return the output of the function as a JSON
  object.
</ParamField>

<ParamField path="args.strict" type="boolean">
  Whether to use strict mode for the function. If true, the function will throw an error
  if the variable names in the prompt do not match the input keys.
</ParamField>

<ParamField path="args.tags" type="string[]">
  Tags to add to the span. This will be logged as the `tags` field in the span.
</ParamField>

<ParamField path="args.version" type="string">
  The version of the function to invoke.
</ParamField>

<ParamField path="args.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="args.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="args.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="args.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="args.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="args.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="args.forceLogin" type="boolean" />

### loadPrompt

Load a prompt from the specified project.

<ParamField path="options" type="LoadPromptOptions">
  Options for configuring loadPrompt().
</ParamField>

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.defaults" type="DefaultPromptArgs" />

<ParamField path="options.environment" type="string" />

<ParamField path="options.id" type="string" />

<ParamField path="options.noTrace" type="boolean" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.projectName" type="string" />

<ParamField path="options.slug" type="string" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.version" type="string" />

### log

Log a single event to the current experiment. The event will be batched and uploaded behind the scenes.

<ParamField path="event" type="ExperimentLogFullArgs">
  The event to log. See `Experiment.log` for full details.
</ParamField>

<ParamField path="event.input" type="unknown" required />

<ParamField path="event.id" type="string" required />

### logError

logError function

<ParamField path="span" type="Span" />

<ParamField path="span.id" type="string" required>
  Row ID of the span.
</ParamField>

<ParamField path="span.kind" type="&#x22;span&#x22;" required />

<ParamField path="span.rootSpanId" type="string" required>
  Root span ID of the span.
</ParamField>

<ParamField path="span.spanId" type="string" required>
  Span ID of the span.
</ParamField>

<ParamField path="span.spanParents" type="string[]" required>
  Parent span IDs of the span.
</ParamField>

<ParamField path="error" type="unknown" />

### login

Log into Braintrust. This will prompt you for your API token, which you can find at
[https://www.braintrust.dev/app/token](https://www.braintrust.dev/app/token). This method is called automatically by `init()`.

<ParamField path="options" type="unknown">
  Options for configuring login().
</ParamField>

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean">
  Login again, even if you have already logged in (by default, this function will exit quickly if you have already logged in)
</ParamField>

### loginToState

loginToState function

<ParamField path="options" type="LoginOptions" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

### newId

newId function

### parseCachedHeader

parseCachedHeader function

<ParamField path="value" type="undefined | null | string" />

### permalink

Format a permalink to the Braintrust application for viewing the span
represented by the provided `slug`.

Links can be generated at any time, but they will only become viewable after
the span and its root have been flushed to the server and ingested.

If you have a `Span` object, use `Span.link` instead.

<ParamField path="slug" type="string">
  The identifier generated from `Span.export`.
</ParamField>

<ParamField path="opts" type="Object">
  Optional arguments.
</ParamField>

<ParamField path="opts.appUrl" type="string">
  The app URL to use. If not provided, the app URL will be inferred from the state.
</ParamField>

<ParamField path="opts.orgName" type="string">
  The org name to use. If not provided, the org name will be inferred from the state.
</ParamField>

<ParamField path="opts.state" type="BraintrustState">
  The login state to use. If not provided, the global state will be used.
</ParamField>

### promptDefinitionToPromptData

promptDefinitionToPromptData function

<ParamField path="promptDefinition" type="unknown" />

<ParamField path="promptDefinition.model" type="string" required />

<ParamField path="promptDefinition.params" type="objectOutputType | objectOutputType | objectOutputType | objectOutputType | objectOutputType" />

<ParamField path="rawTools" type="Object[]" />

### renderMessage

renderMessage function

<ParamField path="render" type="Object" />

<ParamField path="message" type="T" />

### renderPromptParams

renderPromptParams function

<ParamField path="params" type="undefined | objectOutputType | objectOutputType | objectOutputType | objectOutputType | objectOutputType" />

<ParamField path="args" type="Record" />

<ParamField path="options" type="Object" />

<ParamField path="options.strict" type="boolean" />

### Reporter

Reporter function

<ParamField path="name" type="string" />

<ParamField path="reporter" type="ReporterBody" />

### reportFailures

reportFailures function

<ParamField path="evaluator" type="EvaluatorDef" />

<ParamField path="evaluator.evalName" type="string" required />

<ParamField path="evaluator.projectName" type="string" required />

<ParamField path="evaluator.baseExperimentId" type="string">
  An optional experiment id to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment. This takes precedence over `baseExperimentName` if specified.
</ParamField>

<ParamField path="evaluator.baseExperimentName" type="string">
  An optional experiment name to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment.
</ParamField>

<ParamField path="evaluator.data" type="EvalData" required>
  A function that returns a list of inputs, expected outputs, and metadata.
</ParamField>

<ParamField path="evaluator.description" type="string">
  An optional description for the experiment.
</ParamField>

<ParamField path="evaluator.errorScoreHandler" type="ErrorScoreHandler">
  Optionally supply a custom function to specifically handle score values when tasks or scoring functions have errored.
  A default implementation is exported as `defaultErrorScoreHandler` which will log a 0 score to the root span for any scorer that was not run.
</ParamField>

<ParamField path="evaluator.experimentName" type="string">
  An optional name for the experiment.
</ParamField>

<ParamField path="evaluator.gitMetadataSettings" type="Object">
  Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="evaluator.isPublic" type="boolean">
  Whether the experiment should be public. Defaults to false.
</ParamField>

<ParamField path="evaluator.maxConcurrency" type="number">
  The maximum number of tasks/scorers that will be run concurrently.
  Defaults to undefined, in which case there is no max concurrency.
</ParamField>

<ParamField path="evaluator.metadata" type="Record">
  Optional additional metadata for the experiment.
</ParamField>

<ParamField path="evaluator.parameters" type="Parameters">
  A set of parameters that will be passed to the evaluator.
  Can contain array values that will be converted to single values in the task.
</ParamField>

<ParamField path="evaluator.projectId" type="string">
  If specified, uses the given project ID instead of the evaluator's name to identify the project.
</ParamField>

<ParamField path="evaluator.repoInfo" type="null | Object">
  Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
</ParamField>

<ParamField path="evaluator.scores" type="EvalScorer[]" required>
  A set of functions that take an input, output, and expected value and return a score.
</ParamField>

<ParamField path="evaluator.signal" type="AbortSignal">
  An abort signal that can be used to stop the evaluation.
</ParamField>

<ParamField path="evaluator.state" type="BraintrustState">
  If specified, uses the logger state to initialize Braintrust objects. If unspecified, falls back
  to the global state (initialized using your API key).
</ParamField>

<ParamField path="evaluator.summarizeScores" type="boolean">
  Whether to summarize the scores of the experiment after it has run.
  Defaults to true.
</ParamField>

<ParamField path="evaluator.task" type="EvalTask" required>
  A function that takes an input and returns an output.
</ParamField>

<ParamField path="evaluator.timeout" type="number">
  The duration, in milliseconds, after which to time out the evaluation.
  Defaults to undefined, in which case there is no timeout.
</ParamField>

<ParamField path="evaluator.trialCount" type="number">
  The number of times to run the evaluator per input. This is useful for evaluating applications that
  have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the
  variance in the results.
</ParamField>

<ParamField path="evaluator.update" type="boolean">
  Whether to update an existing experiment with `experiment_name` if one exists. Defaults to false.
</ParamField>

<ParamField path="failingResults" type="EvalResult[]" />

<ParamField path="__namedParameters" type="ReporterOpts" />

### runEvaluator

runEvaluator function

<ParamField path="experiment" type="null | Experiment" />

<ParamField path="evaluator" type="EvaluatorDef" />

<ParamField path="evaluator.evalName" type="string" required />

<ParamField path="evaluator.projectName" type="string" required />

<ParamField path="evaluator.baseExperimentId" type="string">
  An optional experiment id to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment. This takes precedence over `baseExperimentName` if specified.
</ParamField>

<ParamField path="evaluator.baseExperimentName" type="string">
  An optional experiment name to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment.
</ParamField>

<ParamField path="evaluator.data" type="EvalData" required>
  A function that returns a list of inputs, expected outputs, and metadata.
</ParamField>

<ParamField path="evaluator.description" type="string">
  An optional description for the experiment.
</ParamField>

<ParamField path="evaluator.errorScoreHandler" type="ErrorScoreHandler">
  Optionally supply a custom function to specifically handle score values when tasks or scoring functions have errored.
  A default implementation is exported as `defaultErrorScoreHandler` which will log a 0 score to the root span for any scorer that was not run.
</ParamField>

<ParamField path="evaluator.experimentName" type="string">
  An optional name for the experiment.
</ParamField>

<ParamField path="evaluator.gitMetadataSettings" type="Object">
  Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="evaluator.isPublic" type="boolean">
  Whether the experiment should be public. Defaults to false.
</ParamField>

<ParamField path="evaluator.maxConcurrency" type="number">
  The maximum number of tasks/scorers that will be run concurrently.
  Defaults to undefined, in which case there is no max concurrency.
</ParamField>

<ParamField path="evaluator.metadata" type="Record">
  Optional additional metadata for the experiment.
</ParamField>

<ParamField path="evaluator.parameters" type="Parameters">
  A set of parameters that will be passed to the evaluator.
  Can contain array values that will be converted to single values in the task.
</ParamField>

<ParamField path="evaluator.projectId" type="string">
  If specified, uses the given project ID instead of the evaluator's name to identify the project.
</ParamField>

<ParamField path="evaluator.repoInfo" type="null | Object">
  Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
</ParamField>

<ParamField path="evaluator.scores" type="EvalScorer[]" required>
  A set of functions that take an input, output, and expected value and return a score.
</ParamField>

<ParamField path="evaluator.signal" type="AbortSignal">
  An abort signal that can be used to stop the evaluation.
</ParamField>

<ParamField path="evaluator.state" type="BraintrustState">
  If specified, uses the logger state to initialize Braintrust objects. If unspecified, falls back
  to the global state (initialized using your API key).
</ParamField>

<ParamField path="evaluator.summarizeScores" type="boolean">
  Whether to summarize the scores of the experiment after it has run.
  Defaults to true.
</ParamField>

<ParamField path="evaluator.task" type="EvalTask" required>
  A function that takes an input and returns an output.
</ParamField>

<ParamField path="evaluator.timeout" type="number">
  The duration, in milliseconds, after which to time out the evaluation.
  Defaults to undefined, in which case there is no timeout.
</ParamField>

<ParamField path="evaluator.trialCount" type="number">
  The number of times to run the evaluator per input. This is useful for evaluating applications that
  have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the
  variance in the results.
</ParamField>

<ParamField path="evaluator.update" type="boolean">
  Whether to update an existing experiment with `experiment_name` if one exists. Defaults to false.
</ParamField>

<ParamField path="progressReporter" type="ProgressReporter" />

<ParamField path="filters" type="Filter[]" />

<ParamField path="stream" type="undefined | Object" />

<ParamField path="parameters" type="InferParameters" />

### setFetch

Set the fetch implementation to use for requests. You can specify it here,
or when you call `login`.

<ParamField path="fetch" type="Object">
  The fetch implementation to use.
</ParamField>

### setMaskingFunction

Set a global masking function that will be applied to all logged data before sending to Braintrust.
The masking function will be applied after records are merged but before they are sent to the backend.

<ParamField path="maskingFunction" type="null | Object">
  A function that takes a JSON-serializable object and returns a masked version.
  Set to null to disable masking.
</ParamField>

### spanComponentsToObjectId

spanComponentsToObjectId function

<ParamField path="__namedParameters" type="Object" />

<ParamField path="__namedParameters.components" type="SpanComponentsV3" required />

<ParamField path="__namedParameters.state" type="BraintrustState" />

### startSpan

Lower-level alternative to `traced`. This allows you to start a span yourself, and can be useful in situations
where you cannot use callbacks. However, spans started with `startSpan` will not be marked as the "current span",
so `currentSpan()` and `traced()` will be no-ops. If you want to mark a span as current, use `traced` instead.

See [`traced`](#traced) for full details.

<ParamField path="args" type="unknown" />

<ParamField path="args.event" type="StartSpanEventArgs" />

<ParamField path="args.name" type="string" />

<ParamField path="args.parent" type="string" />

<ParamField path="args.parentSpanIds" type="ParentSpanIds | MultiParentSpanIds" />

<ParamField path="args.propagatedEvent" type="StartSpanEventArgs" />

<ParamField path="args.spanAttributes" type="Record" />

<ParamField path="args.spanId" type="string" />

<ParamField path="args.startTime" type="number" />

<ParamField path="args.type" type="SpanType" />

### summarize

Summarize the current experiment, including the scores (compared to the closest reference experiment) and metadata.

<ParamField path="options" type="Object">
  Options for summarizing the experiment.
</ParamField>

<ParamField path="options.comparisonExperimentId" type="string">
  The experiment to compare against. If None, the most recent experiment on the origin's main branch will be used.
</ParamField>

<ParamField path="options.summarizeScores" type="boolean">
  Whether to summarize the scores. If False, only the metadata will be returned.
</ParamField>

### traceable

A synonym for `wrapTraced`. If you're porting from systems that use `traceable`, you can use this to
make your codebase more consistent.

<ParamField path="fn" type="F" />

<ParamField path="args" type="unknown" />

<ParamField path="args.event" type="StartSpanEventArgs" />

<ParamField path="args.name" type="string" />

<ParamField path="args.parent" type="string" />

<ParamField path="args.parentSpanIds" type="ParentSpanIds | MultiParentSpanIds" />

<ParamField path="args.propagatedEvent" type="StartSpanEventArgs" />

<ParamField path="args.spanAttributes" type="Record" />

<ParamField path="args.spanId" type="string" />

<ParamField path="args.startTime" type="number" />

<ParamField path="args.type" type="SpanType" />

<ParamField path="args.setCurrent" type="boolean" />

### traced

Toplevel function for starting a span. It checks the following (in precedence order):

* Currently-active span
* Currently-active experiment
* Currently-active logger

and creates a span under the first one that is active. Alternatively, if `parent` is specified, it creates a span under the specified parent row. If none of these are active, it returns a no-op span object.

See `Span.traced` for full details.

<ParamField path="callback" type="Object" />

<ParamField path="args" type="unknown" />

<ParamField path="args.event" type="StartSpanEventArgs" />

<ParamField path="args.name" type="string" />

<ParamField path="args.parent" type="string" />

<ParamField path="args.parentSpanIds" type="ParentSpanIds | MultiParentSpanIds" />

<ParamField path="args.propagatedEvent" type="StartSpanEventArgs" />

<ParamField path="args.spanAttributes" type="Record" />

<ParamField path="args.spanId" type="string" />

<ParamField path="args.startTime" type="number" />

<ParamField path="args.type" type="SpanType" />

<ParamField path="args.setCurrent" type="boolean" />

### updateSpan

Update a span using the output of `span.export()`. It is important that you only resume updating
to a span once the original span has been fully written and flushed, since otherwise updates to
the span may conflict with the original span.

<ParamField path="__namedParameters" type="unknown" />

<ParamField path="__namedParameters.exported" type="string" required />

### withCurrent

Runs the provided callback with the span as the current span.

<ParamField path="span" type="Span" />

<ParamField path="span.id" type="string" required>
  Row ID of the span.
</ParamField>

<ParamField path="span.kind" type="&#x22;span&#x22;" required />

<ParamField path="span.rootSpanId" type="string" required>
  Root span ID of the span.
</ParamField>

<ParamField path="span.spanId" type="string" required>
  Span ID of the span.
</ParamField>

<ParamField path="span.spanParents" type="string[]" required>
  Parent span IDs of the span.
</ParamField>

<ParamField path="callback" type="Object" />

<ParamField path="state" type="undefined | BraintrustState" />

### withDataset

withDataset function

<ParamField path="project" type="string" />

<ParamField path="callback" type="Object" />

<ParamField path="options" type="Readonly" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.dataset" type="string" />

<ParamField path="options.description" type="string" />

<ParamField path="options.metadata" type="Record" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.version" type="string" />

### withExperiment

withExperiment function

<ParamField path="project" type="string" />

<ParamField path="callback" type="Object" />

<ParamField path="options" type="Readonly" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.baseExperiment" type="string" />

<ParamField path="options.baseExperimentId" type="string" />

<ParamField path="options.dataset" type="AnyDataset" />

<ParamField path="options.description" type="string" />

<ParamField path="options.experiment" type="string" />

<ParamField path="options.gitMetadataSettings" type="Object" />

<ParamField path="options.isPublic" type="boolean" />

<ParamField path="options.metadata" type="Record" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.repoInfo" type="null | Object" />

<ParamField path="options.setCurrent" type="boolean" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.update" type="boolean" />

<ParamField path="options.setCurrent" type="boolean" />

### withLogger

withLogger function

<ParamField path="callback" type="Object" />

<ParamField path="options" type="Readonly" />

<ParamField path="options.apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="options.appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="options.fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="options.noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="options.onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="options.orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

<ParamField path="options.forceLogin" type="boolean" />

<ParamField path="options.orgProjectMetadata" type="OrgProjectMetadata" />

<ParamField path="options.projectId" type="string" />

<ParamField path="options.projectName" type="string" />

<ParamField path="options.setCurrent" type="boolean" />

<ParamField path="options.state" type="BraintrustState" />

<ParamField path="options.setCurrent" type="boolean" />

### withParent

withParent function

<ParamField path="parent" type="string" />

<ParamField path="callback" type="Object" />

<ParamField path="state" type="undefined | BraintrustState" />

### wrapAISDK

Wraps Vercel AI SDK methods with Braintrust tracing. Returns wrapped versions
of generateText, streamText, generateObject, and streamObject that automatically
create spans and log inputs, outputs, and metrics.

<ParamField path="aiSDK" type="any" />

<ParamField path="options" type="WrapAISDKOptions" />

### wrapAISDKModel

Wrap an ai-sdk model (created with `.chat()`, `.completion()`, etc.) to add tracing. If Braintrust is
not configured, this is a no-op

<ParamField path="model" type="T" />

### wrapAnthropic

Wrap an `Anthropic` object (created with `new Anthropic(...)`) to add tracing. If Braintrust is
not configured, nothing will be traced. If this is not an `Anthropic` object, this function is
a no-op.

Currently, this only supports the `v4` API.

<ParamField path="anthropic" type="T" />

### wrapClaudeAgentSDK

Wraps the Claude Agent SDK with Braintrust tracing. This returns wrapped versions
of query and tool that automatically trace all agent interactions.

<ParamField path="sdk" type="T">
  The Claude Agent SDK module
</ParamField>

### wrapGoogleGenAI

Wrap a Google GenAI module (imported with `import * as googleGenAI from '@google/genai'`) to add tracing.
If Braintrust is not configured, nothing will be traced.

<ParamField path="googleGenAI" type="T">
  The Google GenAI module
</ParamField>

### wrapMastraAgent

wrapMastraAgent function

<ParamField path="agent" type="T" />

<ParamField path="_options" type="Object" />

<ParamField path="_options.name" type="string" />

<ParamField path="_options.span_name" type="string" />

### wrapOpenAI

Wrap an `OpenAI` object (created with `new OpenAI(...)`) to add tracing. If Braintrust is
not configured, nothing will be traced. If this is not an `OpenAI` object, this function is
a no-op.

Currently, this supports both the `v4` and `v5` API.

<ParamField path="openai" type="T" />

### wrapOpenAIv4

wrapOpenAIv4 function

<ParamField path="openai" type="T" />

### wrapTraced

Wrap a function with `traced`, using the arguments as `input` and return value as `output`.
Any functions wrapped this way will automatically be traced, similar to the `@traced` decorator
in Python. If you want to correctly propagate the function's name and define it in one go, then
you can do so like this:

```ts  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const myFunc = wrapTraced(async function myFunc(input) {
 const result = await client.chat.completions.create({
   model: "gpt-3.5-turbo",
   messages: [{ role: "user", content: input }],
 });
 return result.choices[0].message.content ?? "unknown";
},
// Optional: if you're using a framework like NextJS that minifies your code, specify the function name and it will be used for the span name
{ name: "myFunc" },
);
```

Now, any calls to `myFunc` will be traced, and the input and output will be logged automatically.
If tracing is inactive, i.e. there is no active logger or experiment, it's just a no-op.

<ParamField path="fn" type="F">
  The function to wrap.
</ParamField>

<ParamField path="args" type="unknown">
  Span-level arguments (e.g. a custom name or type) to pass to `traced`.
</ParamField>

<ParamField path="args.event" type="StartSpanEventArgs" />

<ParamField path="args.name" type="string" />

<ParamField path="args.parent" type="string" />

<ParamField path="args.parentSpanIds" type="ParentSpanIds | MultiParentSpanIds" />

<ParamField path="args.propagatedEvent" type="StartSpanEventArgs" />

<ParamField path="args.spanAttributes" type="Record" />

<ParamField path="args.spanId" type="string" />

<ParamField path="args.startTime" type="number" />

<ParamField path="args.type" type="SpanType" />

<ParamField path="args.setCurrent" type="boolean" />

## Classes

### AISpanProcessor

A span processor that filters spans to only export filtered telemetry.

Only filtered spans and root spans will be forwarded to the inner processor.
This dramatically reduces telemetry volume while preserving important observability.

<span class="text-sm">Methods</span>

`forceFlush()`, `onEnd()`, `onStart()`, `shutdown()`

### Attachment

Represents an attachment to be uploaded and the associated metadata.
`Attachment` objects can be inserted anywhere in an event, allowing you to
log arbitrary file data. The SDK will asynchronously upload the file to
object storage and replace the `Attachment` object with an
`AttachmentReference`.

<span class="text-sm">Properties</span>

<ParamField path="reference" type="Object">
  The object that replaces this `Attachment` at upload time.
</ParamField>

<span class="text-sm">Methods</span>

`data()`, `debugInfo()`, `upload()`

### BaseAttachment

BaseAttachment class

<span class="text-sm">Properties</span>

<ParamField path="reference" type="Object | Object" />

<span class="text-sm">Methods</span>

`data()`, `debugInfo()`, `upload()`

### BraintrustExporter

A trace exporter that sends OpenTelemetry spans to Braintrust.

This exporter wraps the standard OTLP trace exporter and can be used with
any OpenTelemetry setup, including @vercel/otel's registerOTel function,
NodeSDK, or custom tracer providers. It can optionally filter spans to
only send AI-related telemetry.

Environment Variables:

* BRAINTRUST\_API\_KEY: Your Braintrust API key
* BRAINTRUST\_PARENT: Parent identifier (e.g., "project\_name:test")
* BRAINTRUST\_API\_URL: Base URL for Braintrust API (defaults to [https://api.braintrust.dev](https://api.braintrust.dev))

<span class="text-sm">Methods</span>

`export()`, `forceFlush()`, `shutdown()`

### BraintrustSpanProcessor

A span processor that sends OpenTelemetry spans to Braintrust.

This processor uses a BatchSpanProcessor and an OTLP exporter configured
to send data to Braintrust's telemetry endpoint. Span filtering is disabled
by default but can be enabled with the filterAISpans option.

Environment Variables:

* BRAINTRUST\_API\_KEY: Your Braintrust API key
* BRAINTRUST\_PARENT: Parent identifier (e.g., "project\_name:test")
* BRAINTRUST\_API\_URL: Base URL for Braintrust API (defaults to [https://api.braintrust.dev](https://api.braintrust.dev))

<span class="text-sm">Methods</span>

`forceFlush()`, `onEnd()`, `onStart()`, `shutdown()`

### BraintrustState

BraintrustState class

<span class="text-sm">Properties</span>

<ParamField path="apiUrl" type="null | string" />

<ParamField path="appPublicUrl" type="null | string" />

<ParamField path="appUrl" type="null | string" />

<ParamField path="currentExperiment" type="undefined | Experiment" />

<ParamField path="currentLogger" type="undefined | Logger" />

<ParamField path="currentParent" type="IsoAsyncLocalStorage" />

<ParamField path="currentSpan" type="IsoAsyncLocalStorage" />

<ParamField path="fetch" type="Object" />

<ParamField path="gitMetadataSettings" type="Object" />

<ParamField path="id" type="string" />

<ParamField path="loggedIn" type="boolean" />

<ParamField path="loginToken" type="null | string" />

<ParamField path="orgId" type="null | string" />

<ParamField path="orgName" type="null | string" />

<ParamField path="promptCache" type="PromptCache" />

<ParamField path="proxyUrl" type="null | string" />

<ParamField path="contextManager" type="unknown" />

<ParamField path="idGenerator" type="unknown" />

<span class="text-sm">Methods</span>

`apiConn()`, `appConn()`, `bgLogger()`, `copyLoginInfo()`, `disable()`, `enforceQueueSizeLimit()`, `httpLogger()`, `login()`, `loginReplaceApiConn()`, `proxyConn()`, `resetIdGenState()`, `resetLoginInfo()`, `serialize()`, `setFetch()`, `setMaskingFunction()`, `setOverrideBgLogger()`, `toJSON()`, `toString()`, `deserialize()`

### BraintrustStream

A Braintrust stream. This is a wrapper around a ReadableStream of `BraintrustStreamChunk`,
with some utility methods to make them easy to log and convert into various formats.

<span class="text-sm">Methods</span>

`[asyncIterator]()`, `copy()`, `finalValue()`, `toReadableStream()`, `parseRawEvent()`, `serializeRawEvent()`

### CodeFunction

CodeFunction class

<span class="text-sm">Properties</span>

<ParamField path="description" type="string" />

<ParamField path="handler" type="Fn" />

<ParamField path="ifExists" type="&#x22;replace&#x22; | &#x22;error&#x22; | &#x22;ignore&#x22;" />

<ParamField path="metadata" type="Record" />

<ParamField path="name" type="string" />

<ParamField path="parameters" type="ZodType" />

<ParamField path="project" type="Project" />

<ParamField path="returns" type="ZodType" />

<ParamField path="slug" type="string" />

<ParamField path="type" type="&#x22;tool&#x22; | &#x22;task&#x22; | &#x22;scorer&#x22; | &#x22;llm&#x22; | &#x22;custom_view&#x22;" />

<span class="text-sm">Methods</span>

`key()`

### CodePrompt

CodePrompt class

<span class="text-sm">Properties</span>

<ParamField path="description" type="string" />

<ParamField path="functionType" type="&#x22;tool&#x22; | &#x22;task&#x22; | &#x22;scorer&#x22; | &#x22;llm&#x22; | &#x22;custom_view&#x22;" />

<ParamField path="id" type="string" />

<ParamField path="ifExists" type="&#x22;replace&#x22; | &#x22;error&#x22; | &#x22;ignore&#x22;" />

<ParamField path="metadata" type="Record" />

<ParamField path="name" type="string" />

<ParamField path="project" type="Project" />

<ParamField path="prompt" type="Object" />

<ParamField path="slug" type="string" />

<ParamField path="toolFunctions" type="Object | Object | GenericCodeFunction[]" />

<span class="text-sm">Methods</span>

`toFunctionDefinition()`

### ContextManager

ContextManager class

<span class="text-sm">Methods</span>

`getCurrentSpan()`, `getParentSpanIds()`, `runInContext()`

### Dataset

A dataset is a collection of records, such as model inputs and expected outputs, which represent
data you can use to evaluate and fine-tune models. You can log production data to datasets,
curate them with interesting examples, edit/delete records, and run evaluations against them.

You should not create `Dataset` objects directly. Instead, use the `braintrust.initDataset()` method.

<span class="text-sm">Properties</span>

<ParamField path="id" type="unknown" />

<ParamField path="loggingState" type="unknown" />

<ParamField path="name" type="unknown" />

<ParamField path="project" type="unknown" />

<span class="text-sm">Methods</span>

`[asyncIterator]()`, `clearCache()`, `close()`, `delete()`, `fetch()`, `fetchedData()`, `flush()`, `getState()`, `insert()`, `summarize()`, `update()`, `version()`, `isDataset()`

### EvalResultWithSummary

EvalResultWithSummary class

<span class="text-sm">Properties</span>

<ParamField path="results" type="EvalResult[]" />

<ParamField path="summary" type="ExperimentSummary" />

<span class="text-sm">Methods</span>

`toJSON()`, `toString()`

### Experiment

An experiment is a collection of logged events, such as model inputs and outputs, which represent
a snapshot of your application at a particular point in time. An experiment is meant to capture more
than just the model you use, and includes the data you use to test, pre- and post- processing code,
comparison metrics (scores), and any other metadata you want to include.

Experiments are associated with a project, and two experiments are meant to be easily comparable via
their `inputs`. You can change the attributes of the experiments in a project (e.g. scoring functions)
over time, simply by changing what you log.

You should not create `Experiment` objects directly. Instead, use the `braintrust.init()` method.

<span class="text-sm">Properties</span>

<ParamField path="dataset" type="AnyDataset" />

<ParamField path="kind" type="&#x22;experiment&#x22;" />

<ParamField path="id" type="unknown" />

<ParamField path="loggingState" type="unknown" />

<ParamField path="name" type="unknown" />

<ParamField path="project" type="unknown" />

<span class="text-sm">Methods</span>

`[asyncIterator]()`, `clearCache()`, `close()`, `export()`, `fetch()`, `fetchBaseExperiment()`, `fetchedData()`, `flush()`, `getState()`, `log()`, `logFeedback()`, `startSpan()`, `summarize()`, `traced()`, `updateSpan()`, `version()`

### ExternalAttachment

Represents an attachment that resides in an external object store and the associated metadata.

`ExternalAttachment` objects can be inserted anywhere in an event, similar to
`Attachment` objects, but they reference files that already exist in an external
object store rather than requiring upload. The SDK will replace the `ExternalAttachment`
object with an `AttachmentReference` during logging.

<span class="text-sm">Properties</span>

<ParamField path="reference" type="Object">
  The object that replaces this `ExternalAttachment` at upload time.
</ParamField>

<span class="text-sm">Methods</span>

`data()`, `debugInfo()`, `upload()`

### FailedHTTPResponse

FailedHTTPResponse class

<span class="text-sm">Properties</span>

<ParamField path="data" type="string" />

<ParamField path="status" type="number" />

<ParamField path="text" type="string" />

### IDGenerator

Abstract base class for ID generators

<span class="text-sm">Methods</span>

`getSpanId()`, `getTraceId()`, `shareRootSpanId()`

### JSONAttachment

Represents a JSON object that should be stored as an attachment.

`JSONAttachment` is a convenience function that creates an `Attachment`
from JSON data. It's particularly useful for large JSON objects that
would otherwise bloat the trace size.

The JSON data is automatically serialized and stored as an attachment
with content type "application/json".

<span class="text-sm">Properties</span>

<ParamField path="reference" type="Object">
  The object that replaces this `Attachment` at upload time.
</ParamField>

<span class="text-sm">Methods</span>

`data()`, `debugInfo()`, `upload()`

### LazyValue

LazyValue class

<span class="text-sm">Properties</span>

<ParamField path="hasSucceeded" type="unknown" />

<span class="text-sm">Methods</span>

`get()`, `getSync()`

### Logger

Logger class

<span class="text-sm">Properties</span>

<ParamField path="kind" type="&#x22;logger&#x22;" />

<ParamField path="asyncFlush" type="unknown" />

<ParamField path="id" type="unknown" />

<ParamField path="loggingState" type="unknown" />

<ParamField path="org_id" type="unknown" />

<ParamField path="project" type="unknown" />

<span class="text-sm">Methods</span>

`export()`, `flush()`, `log()`, `logFeedback()`, `startSpan()`, `traced()`, `updateSpan()`

### NoopSpan

A fake implementation of the Span API which does nothing. This can be used as the default span.

<span class="text-sm">Properties</span>

<ParamField path="id" type="string">
  Row ID of the span.
</ParamField>

<ParamField path="kind" type="&#x22;span&#x22;" />

<ParamField path="rootSpanId" type="string">
  Root span ID of the span.
</ParamField>

<ParamField path="spanId" type="string">
  Span ID of the span.
</ParamField>

<ParamField path="spanParents" type="string[]">
  Parent span IDs of the span.
</ParamField>

<span class="text-sm">Methods</span>

`close()`, `end()`, `export()`, `flush()`, `link()`, `log()`, `logFeedback()`, `permalink()`, `setAttributes()`, `startSpan()`, `startSpanWithParents()`, `state()`, `toString()`, `traced()`

### OTELIDGenerator

ID generator that generates OpenTelemetry-compatible IDs
Uses hex strings for compatibility with OpenTelemetry systems

<span class="text-sm">Methods</span>

`getSpanId()`, `getTraceId()`, `shareRootSpanId()`

### Project

Project class

<span class="text-sm">Properties</span>

<ParamField path="id" type="string" />

<ParamField path="name" type="string" />

<ParamField path="prompts" type="PromptBuilder" />

<ParamField path="scorers" type="ScorerBuilder" />

<ParamField path="tools" type="ToolBuilder" />

<span class="text-sm">Methods</span>

`addCodeFunction()`, `addPrompt()`, `publish()`

### ProjectNameIdMap

ProjectNameIdMap class

<span class="text-sm">Methods</span>

`getId()`, `getName()`, `resolve()`

### Prompt

Prompt class

<span class="text-sm">Properties</span>

<ParamField path="id" type="unknown" />

<ParamField path="name" type="unknown" />

<ParamField path="options" type="unknown" />

<ParamField path="projectId" type="unknown" />

<ParamField path="prompt" type="unknown" />

<ParamField path="promptData" type="unknown" />

<ParamField path="slug" type="unknown" />

<ParamField path="version" type="unknown" />

<span class="text-sm">Methods</span>

`build()`, `buildWithAttachments()`, `fromPromptData()`, `isPrompt()`, `renderPrompt()`

### PromptBuilder

PromptBuilder class

<span class="text-sm">Methods</span>

`create()`

### ReadonlyAttachment

A readonly alternative to `Attachment`, which can be used for fetching
already-uploaded Attachments.

<span class="text-sm">Properties</span>

<ParamField path="reference" type="Object | Object">
  Attachment metadata.
</ParamField>

<span class="text-sm">Methods</span>

`asBase64Url()`, `data()`, `metadata()`, `status()`

### ReadonlyExperiment

A read-only view of an experiment, initialized by passing `open: true` to `init()`.

<span class="text-sm">Properties</span>

<ParamField path="id" type="unknown" />

<ParamField path="loggingState" type="unknown" />

<ParamField path="name" type="unknown" />

<span class="text-sm">Methods</span>

`[asyncIterator]()`, `asDataset()`, `clearCache()`, `fetch()`, `fetchedData()`, `getState()`, `version()`

### ScorerBuilder

ScorerBuilder class

<span class="text-sm">Methods</span>

`create()`

### SpanImpl

Primary implementation of the `Span` interface. See [`Span`](#span) for full details on each method.

We suggest using one of the various `traced` methods, instead of creating Spans directly. See `Span.startSpan` for full details.

<span class="text-sm">Properties</span>

<ParamField path="kind" type="&#x22;span&#x22;" />

<ParamField path="id" type="unknown">
  Row ID of the span.
</ParamField>

<ParamField path="rootSpanId" type="unknown">
  Root span ID of the span.
</ParamField>

<ParamField path="spanId" type="unknown">
  Span ID of the span.
</ParamField>

<ParamField path="spanParents" type="unknown">
  Parent span IDs of the span.
</ParamField>

<span class="text-sm">Methods</span>

`close()`, `end()`, `export()`, `flush()`, `link()`, `log()`, `logFeedback()`, `permalink()`, `setAttributes()`, `setSpanParents()`, `startSpan()`, `startSpanWithParents()`, `state()`, `toString()`, `traced()`

### TestBackgroundLogger

TestBackgroundLogger class

<span class="text-sm">Methods</span>

`drain()`, `flush()`, `log()`, `setMaskingFunction()`

### ToolBuilder

ToolBuilder class

<span class="text-sm">Methods</span>

`create()`

### UUIDGenerator

ID generator that uses UUID4 for both span and trace IDs

<span class="text-sm">Methods</span>

`getSpanId()`, `getTraceId()`, `shareRootSpanId()`

## Interfaces

### AttachmentParams

AttachmentParams interface

<span class="text-sm">Properties</span>

<ParamField path="contentType" type="string" />

<ParamField path="data" type="string | ArrayBuffer | Blob" />

<ParamField path="filename" type="string" />

<ParamField path="state" type="BraintrustState" />

### BackgroundLoggerOpts

BackgroundLoggerOpts interface

<span class="text-sm">Properties</span>

<ParamField path="noExitFlush" type="boolean" />

<ParamField path="onFlushError" type="Object" />

### ContextParentSpanIds

ContextParentSpanIds interface

<span class="text-sm">Properties</span>

<ParamField path="rootSpanId" type="string" />

<ParamField path="spanParents" type="string[]" />

### DatasetSummary

Summary of a dataset's scores and metadata.

<span class="text-sm">Properties</span>

<ParamField path="dataSummary" type="undefined | DataSummary">
  Summary of the dataset's data.
</ParamField>

<ParamField path="datasetName" type="string">
  Name of the dataset.
</ParamField>

<ParamField path="datasetUrl" type="string">
  URL to the experiment's page in the Braintrust app.
</ParamField>

<ParamField path="projectName" type="string">
  Name of the project that the dataset belongs to.
</ParamField>

<ParamField path="projectUrl" type="string">
  URL to the project's page in the Braintrust app.
</ParamField>

### DataSummary

Summary of a dataset's data.

<span class="text-sm">Properties</span>

<ParamField path="newRecords" type="number">
  New or updated records added in this session.
</ParamField>

<ParamField path="totalRecords" type="number">
  Total records in the dataset.
</ParamField>

### EvalHooks

EvalHooks interface

<span class="text-sm">Properties</span>

<ParamField path="expected" type="Expected">
  The expected output for the current evaluation.
</ParamField>

<ParamField path="meta" type="Object" />

<ParamField path="metadata" type="unknown">
  The metadata object for the current evaluation. You can mutate this object to add or remove metadata.
</ParamField>

<ParamField path="parameters" type="InferParameters">
  The current parameters being used for this specific task execution.
  Array parameters are converted to single values.
</ParamField>

<ParamField path="reportProgress" type="Object">
  Report progress that will show up in the playground.
</ParamField>

<ParamField path="span" type="Span">
  The task's span.
</ParamField>

<ParamField path="tags" type="undefined | string[]">
  The tags for the current evaluation.
</ParamField>

<ParamField path="trialIndex" type="number">
  The index of the current trial (0-based). This is useful when trialCount > 1.
</ParamField>

### Evaluator

Evaluator interface

<span class="text-sm">Properties</span>

<ParamField path="baseExperimentId" type="string">
  An optional experiment id to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment. This takes precedence over `baseExperimentName` if specified.
</ParamField>

<ParamField path="baseExperimentName" type="string">
  An optional experiment name to use as a base. If specified, the new experiment will be summarized
  and compared to this experiment.
</ParamField>

<ParamField path="data" type="EvalData">
  A function that returns a list of inputs, expected outputs, and metadata.
</ParamField>

<ParamField path="description" type="string">
  An optional description for the experiment.
</ParamField>

<ParamField path="errorScoreHandler" type="ErrorScoreHandler">
  Optionally supply a custom function to specifically handle score values when tasks or scoring functions have errored.
  A default implementation is exported as `defaultErrorScoreHandler` which will log a 0 score to the root span for any scorer that was not run.
</ParamField>

<ParamField path="experimentName" type="string">
  An optional name for the experiment.
</ParamField>

<ParamField path="gitMetadataSettings" type="Object">
  Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
</ParamField>

<ParamField path="isPublic" type="boolean">
  Whether the experiment should be public. Defaults to false.
</ParamField>

<ParamField path="maxConcurrency" type="number">
  The maximum number of tasks/scorers that will be run concurrently.
  Defaults to undefined, in which case there is no max concurrency.
</ParamField>

<ParamField path="metadata" type="Record">
  Optional additional metadata for the experiment.
</ParamField>

<ParamField path="parameters" type="Parameters">
  A set of parameters that will be passed to the evaluator.
  Can contain array values that will be converted to single values in the task.
</ParamField>

<ParamField path="projectId" type="string">
  If specified, uses the given project ID instead of the evaluator's name to identify the project.
</ParamField>

<ParamField path="repoInfo" type="null | Object">
  Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
</ParamField>

<ParamField path="scores" type="EvalScorer[]">
  A set of functions that take an input, output, and expected value and return a score.
</ParamField>

<ParamField path="signal" type="AbortSignal">
  An abort signal that can be used to stop the evaluation.
</ParamField>

<ParamField path="state" type="BraintrustState">
  If specified, uses the logger state to initialize Braintrust objects. If unspecified, falls back
  to the global state (initialized using your API key).
</ParamField>

<ParamField path="summarizeScores" type="boolean">
  Whether to summarize the scores of the experiment after it has run.
  Defaults to true.
</ParamField>

<ParamField path="task" type="EvalTask">
  A function that takes an input and returns an output.
</ParamField>

<ParamField path="timeout" type="number">
  The duration, in milliseconds, after which to time out the evaluation.
  Defaults to undefined, in which case there is no timeout.
</ParamField>

<ParamField path="trialCount" type="number">
  The number of times to run the evaluator per input. This is useful for evaluating applications that
  have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the
  variance in the results.
</ParamField>

<ParamField path="update" type="boolean">
  Whether to update an existing experiment with `experiment_name` if one exists. Defaults to false.
</ParamField>

### ExperimentSummary

Summary of an experiment's scores and metadata.

<span class="text-sm">Properties</span>

<ParamField path="comparisonExperimentName" type="string">
  The experiment scores are baselined against.
</ParamField>

<ParamField path="experimentId" type="string">
  ID of the experiment. May be `undefined` if the eval was run locally.
</ParamField>

<ParamField path="experimentName" type="string">
  Name of the experiment.
</ParamField>

<ParamField path="experimentUrl" type="string">
  URL to the experiment's page in the Braintrust app.
</ParamField>

<ParamField path="metrics" type="Record" />

<ParamField path="projectId" type="string" />

<ParamField path="projectName" type="string">
  Name of the project that the experiment belongs to.
</ParamField>

<ParamField path="projectUrl" type="string">
  URL to the project's page in the Braintrust app.
</ParamField>

<ParamField path="scores" type="Record">
  Summary of the experiment's scores.
</ParamField>

### Exportable

Exportable interface

### ExternalAttachmentParams

ExternalAttachmentParams interface

<span class="text-sm">Properties</span>

<ParamField path="contentType" type="string" />

<ParamField path="filename" type="string" />

<ParamField path="state" type="BraintrustState" />

<ParamField path="url" type="string" />

### FunctionEvent

FunctionEvent interface

<span class="text-sm">Properties</span>

<ParamField path="description" type="string" />

<ParamField path="function_data" type="Object | Object | Object | Object | Object" />

<ParamField path="function_type" type="&#x22;tool&#x22; | &#x22;task&#x22; | &#x22;scorer&#x22; | &#x22;llm&#x22; | &#x22;custom_view&#x22;" />

<ParamField path="if_exists" type="&#x22;replace&#x22; | &#x22;error&#x22; | &#x22;ignore&#x22;" />

<ParamField path="metadata" type="Record" />

<ParamField path="name" type="string" />

<ParamField path="project_id" type="string" />

<ParamField path="prompt_data" type="Object" />

<ParamField path="slug" type="string" />

### InvokeFunctionArgs

Arguments for the `invoke` function.

<span class="text-sm">Properties</span>

<ParamField path="function_id" type="string">
  The ID of the function to invoke.
</ParamField>

<ParamField path="globalFunction" type="string">
  The name of the global function to invoke.
</ParamField>

<ParamField path="input" type="Input">
  The input to the function. This will be logged as the `input` field in the span.
</ParamField>

<ParamField path="messages" type="Object | Object | Object | Object | Object | Object | Object[]">
  Additional OpenAI-style messages to add to the prompt (only works for llm functions).
</ParamField>

<ParamField path="metadata" type="Record">
  Additional metadata to add to the span. This will be logged as the `metadata` field in the span.
  It will also be available as the \{\{metadata}} field in the prompt and as the `metadata` argument
  to the function.
</ParamField>

<ParamField path="mode" type="null | &#x22;auto&#x22; | &#x22;parallel&#x22;">
  The mode of the function. If "auto", will return a string if the function returns a string,
  and a JSON object otherwise. If "parallel", will return an array of JSON objects with one
  object per tool call.
</ParamField>

<ParamField path="parent" type="string | Exportable">
  The parent of the function. This can be an existing span, logger, or experiment, or
  the output of `.export()` if you are distributed tracing. If unspecified, will use
  the same semantics as `traced()` to determine the parent and no-op if not in a tracing
  context.
</ParamField>

<ParamField path="projectName" type="string">
  The name of the project containing the function to invoke.
</ParamField>

<ParamField path="promptSessionFunctionId" type="string">
  The ID of the function in the prompt session to invoke.
</ParamField>

<ParamField path="promptSessionId" type="string">
  The ID of the prompt session to invoke the function from.
</ParamField>

<ParamField path="schema" type="unknown">
  A Zod schema to validate the output of the function and return a typed value. This
  is only used if `stream` is false.
</ParamField>

<ParamField path="slug" type="string">
  The slug of the function to invoke.
</ParamField>

<ParamField path="state" type="BraintrustState">
  (Advanced) This parameter allows you to pass in a custom login state. This is useful
  for multi-tenant environments where you are running functions from different Braintrust
  organizations.
</ParamField>

<ParamField path="stream" type="Stream">
  Whether to stream the function's output. If true, the function will return a
  `BraintrustStream`, otherwise it will return the output of the function as a JSON
  object.
</ParamField>

<ParamField path="strict" type="boolean">
  Whether to use strict mode for the function. If true, the function will throw an error
  if the variable names in the prompt do not match the input keys.
</ParamField>

<ParamField path="tags" type="string[]">
  Tags to add to the span. This will be logged as the `tags` field in the span.
</ParamField>

<ParamField path="version" type="string">
  The version of the function to invoke.
</ParamField>

### LoginOptions

Options for logging in to Braintrust.

<span class="text-sm">Properties</span>

<ParamField path="apiKey" type="string">
  The API key to use. If the parameter is not specified, will try to use the `BRAINTRUST_API_KEY` environment variable.
</ParamField>

<ParamField path="appUrl" type="string">
  The URL of the Braintrust App. Defaults to [https://www.braintrust.dev](https://www.braintrust.dev). You should not need
  to change this unless you are doing the "Full" deployment.
</ParamField>

<ParamField path="fetch" type="Object">
  A custom fetch implementation to use.
</ParamField>

<ParamField path="noExitFlush" type="boolean">
  By default, the SDK installs an event handler that flushes pending writes on the `beforeExit` event.
  If true, this event handler will *not* be installed.
</ParamField>

<ParamField path="onFlushError" type="Object">
  Calls this function if there's an error in the background flusher.
</ParamField>

<ParamField path="orgName" type="string">
  The name of a specific organization to connect to. Since API keys are scoped to organizations, this parameter is usually
  unnecessary unless you are logging in with a JWT.
</ParamField>

### LogOptions

LogOptions interface

<span class="text-sm">Properties</span>

<ParamField path="asyncFlush" type="IsAsyncFlush" />

<ParamField path="computeMetadataArgs" type="Record" />

### MetricSummary

Summary of a metric's performance.

<span class="text-sm">Properties</span>

<ParamField path="diff" type="number">
  Difference in metric between the current and reference experiment.
</ParamField>

<ParamField path="improvements" type="number">
  Number of improvements in the metric.
</ParamField>

<ParamField path="metric" type="number">
  Average metric across all examples.
</ParamField>

<ParamField path="name" type="string">
  Name of the metric.
</ParamField>

<ParamField path="regressions" type="number">
  Number of regressions in the metric.
</ParamField>

<ParamField path="unit" type="string">
  Unit label for the metric.
</ParamField>

### ObjectMetadata

ObjectMetadata interface

<span class="text-sm">Properties</span>

<ParamField path="fullInfo" type="Record" />

<ParamField path="id" type="string" />

<ParamField path="name" type="string" />

### ParentExperimentIds

ParentExperimentIds interface

<span class="text-sm">Properties</span>

<ParamField path="experiment_id" type="string" />

### ParentProjectLogIds

ParentProjectLogIds interface

<span class="text-sm">Properties</span>

<ParamField path="log_id" type="&#x22;g&#x22;" />

<ParamField path="project_id" type="string" />

### ReporterBody

ReporterBody interface

### ScoreSummary

Summary of a score's performance.

<span class="text-sm">Properties</span>

<ParamField path="diff" type="number">
  Difference in score between the current and reference experiment.
</ParamField>

<ParamField path="improvements" type="number">
  Number of improvements in the score.
</ParamField>

<ParamField path="name" type="string">
  Name of the score.
</ParamField>

<ParamField path="regressions" type="number">
  Number of regressions in the score.
</ParamField>

<ParamField path="score" type="number">
  Average score across all examples.
</ParamField>

### Span

A Span encapsulates logged data and metrics for a unit of work. This interface is shared by all span implementations.

We suggest using one of the various `traced` methods, instead of creating Spans directly. See `Span.traced` for full details.

<span class="text-sm">Properties</span>

<ParamField path="id" type="string">
  Row ID of the span.
</ParamField>

<ParamField path="kind" type="&#x22;span&#x22;" />

<ParamField path="rootSpanId" type="string">
  Root span ID of the span.
</ParamField>

<ParamField path="spanId" type="string">
  Span ID of the span.
</ParamField>

<ParamField path="spanParents" type="string[]">
  Parent span IDs of the span.
</ParamField>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt