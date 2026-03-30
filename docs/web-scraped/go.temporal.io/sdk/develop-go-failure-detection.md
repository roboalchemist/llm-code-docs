# Source: https://docs.temporal.io/develop/go/failure-detection

Title: Failure detection - Go SDK | Temporal Platform Documentation

URL Source: https://docs.temporal.io/develop/go/failure-detection

Published Time: Sat, 28 Feb 2026 00:31:48 GMT

Markdown Content:
This page shows how to do the following:

*   [Set Workflow timeouts](https://docs.temporal.io/develop/go/failure-detection#workflow-timeouts)
*   [Set a Workflow Retry Policy](https://docs.temporal.io/develop/go/failure-detection#workflow-retries)
*   [Set Activity timeouts](https://docs.temporal.io/develop/go/failure-detection#activity-timeouts)
*   [Set a custom Activity Retry Policy](https://docs.temporal.io/develop/go/failure-detection#activity-retries)

Workflow timeouts[​](https://docs.temporal.io/develop/go/failure-detection#workflow-timeouts "Direct link to Workflow timeouts")
--------------------------------------------------------------------------------------------------------------------------------

**How to set Workflow timeouts using the Temporal Go SDK**

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

Workflow timeouts are set when [starting the Workflow Execution](https://docs.temporal.io/develop/go/failure-detection#workflow-timeouts).

Before we continue, we want to note that we generally do not recommend setting Workflow Timeouts, because Workflows are designed to be long-running and resilient. Instead, setting a Timeout can limit its ability to handle unexpected delays or long-running processes. If you need to perform an action inside your Workflow after a specific period of time, we recommend using a Timer.

*   **[Workflow Execution Timeout](https://docs.temporal.io/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)** - restricts the maximum amount of time that a single Workflow Execution can be executed.
*   **[Workflow Run Timeout](https://docs.temporal.io/encyclopedia/detecting-workflow-failures#workflow-run-timeout):** restricts the maximum amount of time that a single Workflow Run can last.
*   **[Workflow Task Timeout](https://docs.temporal.io/encyclopedia/detecting-workflow-failures#workflow-task-timeout):** restricts the maximum amount of time that a Worker can execute a Workflow Task.

Create an instance of [`StartWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/client#StartWorkflowOptions) from the `go.temporal.io/sdk/client` package, set a timeout, and pass the instance to the `ExecuteWorkflow` call.

Available timeouts are:

*   `WorkflowExecutionTimeout`
*   `WorkflowRunTimeout`
*   `WorkflowTaskTimeout`

`workflowOptions := client.StartWorkflowOptions{  // ...  // Set Workflow Timeout duration  WorkflowExecutionTimeout: 24 * 365 * 10 * time.Hour,  // WorkflowRunTimeout: 24 * 365 * 10 * time.Hour,  // WorkflowTaskTimeout: 10 * time.Second,  // ...}workflowRun, err := c.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflowDefinition)if err != nil {  // ...}`

### Workflow Retry Policy[​](https://docs.temporal.io/develop/go/failure-detection#workflow-retries "Direct link to Workflow Retry Policy")

**How to set a Workflow Retry policy using the Go SDK.**

A Retry Policy can work in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Use a [Retry Policy](https://docs.temporal.io/encyclopedia/retry-policies) to retry a Workflow Execution in the event of a failure.

Workflow Executions do not retry by default, and Retry Policies should be used with Workflow Executions only in certain situations.

Create an instance of a [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy) from the `go.temporal.io/sdk/temporal` package and provide it as the value to the `RetryPolicy` field of the instance of `StartWorkflowOptions`.

*   Type: [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy)
*   Default: None

`retrypolicy := &temporal.RetryPolicy{  InitialInterval:    time.Second,  BackoffCoefficient: 2.0,  MaximumInterval:    time.Second * 100,}workflowOptions := client.StartWorkflowOptions{  RetryPolicy: retrypolicy,  // ...}workflowRun, err := temporalClient.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflowDefinition)if err != nil {  // ...}`

How to set Activity timeouts[​](https://docs.temporal.io/develop/go/failure-detection#activity-timeouts "Direct link to How to set Activity timeouts")
------------------------------------------------------------------------------------------------------------------------------------------------------

**How to set Activity timeouts using the Go SDK.**

Each Activity timeout controls the maximum duration of a different aspect of an Activity Execution.

The following timeouts are available in the Activity Options.

*   **[Schedule-To-Close Timeout](https://docs.temporal.io/encyclopedia/detecting-activity-failures#schedule-to-close-timeout):** is the maximum amount of time allowed for the overall [Activity Execution](https://docs.temporal.io/activity-execution).
*   **[Start-To-Close Timeout](https://docs.temporal.io/encyclopedia/detecting-activity-failures#start-to-close-timeout):** is the maximum time allowed for a single [Activity Task Execution](https://docs.temporal.io/tasks#activity-task-execution).
*   **[Schedule-To-Start Timeout](https://docs.temporal.io/encyclopedia/detecting-activity-failures#schedule-to-start-timeout):** is the maximum amount of time that is allowed from when an [Activity Task](https://docs.temporal.io/tasks#activity-task) is scheduled to when a [Worker](https://docs.temporal.io/workers#worker) starts that Activity Task.

An Activity Execution must have either the Start-To-Close or the Schedule-To-Close Timeout set.

To set an Activity Timeout in Go, create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the Activity Timeout field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

Available timeouts are:

*   `StartToCloseTimeout`
*   `ScheduleToClose`
*   `ScheduleToStartTimeout`

`activityoptions := workflow.ActivityOptions{  // Set Activity Timeout duration  ScheduleToCloseTimeout: 10 * time.Second,  // StartToCloseTimeout: 10 * time.Second,  // ScheduleToStartTimeout: 10 * time.Second,}ctx = workflow.WithActivityOptions(ctx, activityoptions)var yourActivityResult YourActivityResulterr = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)if err != nil {  // ...}`

### Set a custom Activity Retry Policy[​](https://docs.temporal.io/develop/go/failure-detection#activity-retries "Direct link to Set a custom Activity Retry Policy")

**How to set a custom Activity Retry Policy using the Go SDK.**

A Retry Policy works in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Activity Executions are automatically associated with a default [Retry Policy](https://docs.temporal.io/encyclopedia/retry-policies) if a custom one is not provided.

To set a [RetryPolicy](https://docs.temporal.io/encyclopedia/retry-policies), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `RetryPolicy` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

*   Type: [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy)
*   Default:

`retrypolicy := &temporal.RetryPolicy{  InitialInterval:    time.Second,  BackoffCoefficient: 2.0,  MaximumInterval:    time.Second * 100, // 100 * InitialInterval  MaximumAttempts: 0, // Unlimited  NonRetryableErrorTypes: []string, // empty}`

Providing a Retry Policy here is a customization, and overwrites individual Field defaults.

`retrypolicy := &temporal.RetryPolicy{  InitialInterval:    time.Second,  BackoffCoefficient: 2.0,  MaximumInterval:    time.Second * 100,}activityoptions := workflow.ActivityOptions{  RetryPolicy: retrypolicy,}ctx = workflow.WithActivityOptions(ctx, activityoptions)var yourActivityResult YourActivityResulterr = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)if err != nil {  // ...}`

### Overriding the retry interval with Next Retry Delay[​](https://docs.temporal.io/develop/go/failure-detection#next-retry-delay "Direct link to Overriding the retry interval with Next Retry Delay")

You may return an [Application Failure](https://docs.temporal.io/references/failures#application-failure) with the `NextRetryDelay` field set. This value will replace and override whatever the Retry interval would be on the Retry Policy.

For example, if in an Activity, you want to base the interval on the number of attempts:

`attempt := activity.GetInfo(ctx).Attempt;return temporal.NewApplicationErrorWithOptions(fmt.Sprintf("Something bad happened on attempt %d", attempt), "NextDelay", temporal.ApplicationErrorOptions{  NextRetryDelay: 3 * time.Second * delay,})`

Activity Heartbeats[​](https://docs.temporal.io/develop/go/failure-detection#activity-heartbeats "Direct link to Activity Heartbeats")
--------------------------------------------------------------------------------------------------------------------------------------

**How to Heartbeat an Activity using the Go SDK.**

An [Activity Heartbeat](https://docs.temporal.io/encyclopedia/detecting-activity-failures#activity-heartbeat) is a ping from the [Worker Process](https://docs.temporal.io/workers#worker-process) that is executing the Activity to the [Temporal Service](https://docs.temporal.io/temporal-service). Each Heartbeat informs the Temporal Service that the [Activity Execution](https://docs.temporal.io/activity-execution) is making progress and the Worker has not crashed. If the Temporal Service does not receive a Heartbeat within a [Heartbeat Timeout](https://docs.temporal.io/encyclopedia/detecting-activity-failures#heartbeat-timeout) time period, the Activity will be considered failed and another [Activity Task Execution](https://docs.temporal.io/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

Heartbeats may not always be sent to the Temporal Service—they may be [throttled](https://docs.temporal.io/encyclopedia/detecting-activity-failures#throttling) by the Worker.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat. Activities that don't Heartbeat can't receive a Cancellation. Heartbeat throttling may lead to Cancellation getting delivered later than expected.

Heartbeats can contain a `details` field describing the Activity's current progress. If an Activity gets retried, the Activity can access the `details` from the last Heartbeat that was sent to the Temporal Service.

To [Heartbeat](https://docs.temporal.io/encyclopedia/detecting-activity-failures#activity-heartbeat) in an Activity in Go, use the `RecordHeartbeat` API.

`import (    // ...    "go.temporal.io/sdk/workflow"    // ...)func YourActivityDefinition(ctx, YourActivityDefinitionParam) (YourActivityDefinitionResult, error) {    // ...    activity.RecordHeartbeat(ctx, details)    // ...}`

When an Activity Task Execution times out due to a missed Heartbeat, the last value of the `details` variable above is returned to the calling Workflow in the `details` field of `TimeoutError` with `TimeoutType` set to `Heartbeat`.

You can also Heartbeat an Activity from an external source:

`// The client is a heavyweight object that should be created once per process.temporalClient, err := client.Dial(client.Options{})// Record heartbeat.err := temporalClient.RecordActivityHeartbeat(ctx, taskToken, details)`

The parameters of the `RecordActivityHeartbeat` function are:

*   `taskToken`: The value of the binary `TaskToken` field of the `ActivityInfo` struct retrieved inside the Activity.
*   `details`: The serializable payload containing progress information.

If an Activity Execution Heartbeats its progress before it failed, the retry attempt will have access to the progress information, so that the Activity Execution can resume from the failed state. Here's an example of how this can be implemented:

`func SampleActivity(ctx context.Context, inputArg InputParams) error {    startIdx := inputArg.StartIndex    if activity.HasHeartbeatDetails(ctx) {        // Recover from finished progress.        var finishedIndex int        if err := activity.GetHeartbeatDetails(ctx, &finishedIndex); err == nil {            startIdx = finishedIndex + 1 // Start from next one.        }    }    // Normal Activity logic...    for i:=startIdx; i<inputArg.EndIdx; i++ {        // Code for processing item i goes here...        activity.RecordHeartbeat(ctx, i) // Report progress.    }}`

### Set a Heartbeat Timeout[​](https://docs.temporal.io/develop/go/failure-detection#heartbeat-timeout "Direct link to Set a Heartbeat Timeout")

**How to set a Heartbeat Timeout for an Activity using the Go SDK.**

A [Heartbeat Timeout](https://docs.temporal.io/encyclopedia/detecting-activity-failures#heartbeat-timeout) works in conjunction with [Activity Heartbeats](https://docs.temporal.io/encyclopedia/detecting-activity-failures#activity-heartbeat).

To set a [Heartbeat Timeout](https://docs.temporal.io/encyclopedia/detecting-activity-failures#heartbeat-timeout), Create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `RetryPolicy` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

`activityoptions := workflow.ActivityOptions{  HeartbeatTimeout: 10 * time.Second,}ctx = workflow.WithActivityOptions(ctx, activityoptions)var yourActivityResult YourActivityResulterr = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)if err != nil {  // ...}`
