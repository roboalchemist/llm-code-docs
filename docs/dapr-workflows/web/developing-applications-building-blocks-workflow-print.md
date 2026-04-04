# Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/_print/

Title: Workflow

URL Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/_print/

Markdown Content:
Dapr Docs
Homepage
GitHub
Blog
Discord
Community
v1.17 (latest)
English
Search
K

This is the multi-page printable view of this section. Click here to print.

Return to the regular view of this page.

Workflow
Orchestrate logic across various microservices
1: Workflow overview
2: Features and concepts
3: Workflow versioning
4: Workflow patterns
5: Workflow architecture
6: How to: Author a workflow
7: How to: Manage workflows
8: Multi Application Workflows
9: History Retention Policy
10: Workflow Execution Concurrency
More about Dapr Workflow

Learn more about how to use Dapr Workflow:

Try the Workflow quickstart.
Explore workflow via any of the supporting Dapr SDKs.
Review the Workflow API reference documentation.
1 - Workflow overview
Overview of Dapr Workflow

Dapr workflow makes it easy for developers to write business logic and integrations in a reliable way. Since Dapr workflows are stateful, they support long-running and fault-tolerant applications, ideal for orchestrating microservices. Dapr workflow works seamlessly with other Dapr building blocks, such as service invocation, pub/sub, state management, and bindings.

The durable, resilient Dapr Workflow capability:

Offers a built-in workflow runtime for driving Dapr Workflow execution.
Provides SDKs for authoring workflows in code, using any language.
Provides HTTP and gRPC APIs for managing workflows (start, query, pause/resume, raise event, terminate, purge).

Some example scenarios that Dapr Workflow can perform are:

Order processing involving orchestration between inventory management, payment systems, and shipping services.
HR onboarding workflows coordinating tasks across multiple departments and participants.
Orchestrating the roll-out of digital menu updates in a national restaurant chain.
Image processing workflows involving API-based classification and storage.
Features
Workflows and activities

With Dapr Workflow, you can write activities and then orchestrate those activities in a workflow. Workflow activities are:

The basic unit of work in a workflow
Used for calling other (Dapr) services, interacting with state stores, and pub/sub brokers.
Used for calling external third party services.

Learn more about workflow activities.

Child workflows

In addition to activities, you can write workflows to schedule other workflows as child workflows. A child workflow has its own instance ID, history, and status that is independent of the parent workflow that started it, except for the fact that terminating the parent workflow terminates all of the child workflows created by it. Child workflow also supports automatic retry policies.

Learn more about child workflows.

Multi-application workflows

Multi-application workflows, enable you to orchestrate complex business processes that span across multiple applications. This allows a workflow to call activities or start child workflows in different applications, distributing the workflow execution while maintaining the security, reliability and durability guarantees of Dapr’s workflow engine.

Learn more about multi-application workflows.

Timers and reminders

Same as Dapr actors, you can schedule reminder-like durable delays for any time range.

Learn more about workflow timers and reminders

Workflow HTTP calls to manage a workflow

When you create an application with workflow code and run it with Dapr, you can call specific workflows that reside in the application. Each individual workflow can be:

Started or terminated through a POST request
Triggered to deliver a named event through a POST request
Paused and then resumed through a POST request
Purged from your state store through a POST request
Queried for workflow status through a GET request

Learn more about how manage a workflow using HTTP calls.

Workflow patterns

Dapr Workflow simplifies complex, stateful coordination requirements in microservice architectures. The following sections describe several application patterns that can benefit from Dapr Workflow.

Learn more about different types of workflow patterns

Workflow SDKs

The Dapr Workflow authoring SDKs are language-specific SDKs that contain types and functions to implement workflow logic. The workflow logic lives in your application and is orchestrated by the Dapr Workflow engine running in the Dapr sidecar via a gRPC stream.

Supported SDKs

You can use the following SDKs to author a workflow.

Language stack	Package
Python	dapr-ext-workflow
JavaScript	DaprWorkflowClient
.NET	Dapr.Workflow
Java	io.dapr.workflows
Go	workflow
Try out workflows
Quickstarts and tutorials

Want to put workflows to the test? Walk through the following quickstart and tutorials to see workflows in action:

Quickstart/tutorial	Description
Workflow quickstart	Run a workflow application with four workflow activities to see Dapr Workflow in action
Workflow Python SDK example	Learn how to create a Dapr Workflow and invoke it using the Python dapr-ext-workflow package.
Workflow JavaScript SDK example	Learn how to create a Dapr Workflow and invoke it using the JavaScript SDK.
Workflow .NET SDK example	Learn how to create a Dapr Workflow and invoke it using ASP.NET Core web APIs.
Workflow Java SDK example	Learn how to create a Dapr Workflow and invoke it using the Java io.dapr.workflows package.
Workflow Go SDK example	Learn how to create a Dapr Workflow and invoke it using the Go workflow package.
Start using workflows directly in your app

Want to skip the quickstarts? Not a problem. You can try out the workflow building block directly in your application. After Dapr is installed, you can begin using workflows, starting with how to author a workflow.

Managing Workflows

Dapr provides comprehensive workflow management capabilities through both the HTTP API and the CLI.

Workflow Lifecycle Operations

Start Workflows

dapr workflow run MyWorkflow --app-id myapp --input '{"key": "value"}'


Monitor Workflows

# List active workflows for a given application

dapr workflow list --app-id myapp --filter-status RUNNING



# View execution history

dapr workflow history <instance-id> --app-id myapp


Control Workflows

# Suspend, resume, or terminate

dapr workflow suspend <instance-id> --app-id myapp

dapr workflow resume <instance-id> --app-id myapp

dapr workflow terminate <instance-id> --app-id myapp


Maintenance Operations

# Purge completed workflows

dapr workflow purge --app-id myapp --all-older-than 720h


See How-To: Manage workflows for detailed instructions.

Limitations
State stores: You can only use state stores which support workflows, as described here.
Azure Cosmos DB has payload and workflow complexity limitations.
AWS DynamoDB has workflow complexity limitations.
Watch the demo

Watch this video for an overview on Dapr Workflow:

Next steps
Workflow features and concepts >>
Related links
Workflow API reference
Try out the full SDK examples:
Python example
JavaScript example
.NET example
Java example
Go example
2 - Features and concepts
Learn more about the Dapr Workflow features and concepts

Now that you’ve learned about the workflow building block at a high level, let’s deep dive into the features and concepts included with the Dapr Workflow engine and SDKs. Dapr Workflow exposes several core features and concepts which are common across all supported languages.

Note
For more information on how workflow state is managed, see the workflow architecture guide.
Workflows

Dapr Workflows are functions you write that define a series of tasks to be executed in a particular order. The Dapr Workflow engine takes care of scheduling and execution of the tasks, including managing failures and retries. If the app hosting your workflows is scaled out across multiple machines, the workflow engine load balances the execution of workflows and their tasks across multiple machines.

There are several different kinds of tasks that a workflow can schedule, including

Activities for executing custom logic
Durable timers for putting the workflow to sleep for arbitrary lengths of time
Child workflows for breaking larger workflows into smaller pieces
External event waiters for blocking workflows until they receive external event signals. These tasks are described in more details in their corresponding sections.
Workflow Instance Management
Querying Workflow State

You can query workflow instances using the CLI:

# Find all running workflows

dapr workflow list --app-id myapp --filter-status RUNNING



# Find workflows by name

dapr workflow list --app-id myapp --filter-name OrderProcessing



# Find recent workflows (last 2 hours)

dapr workflow list --app-id myapp --filter-max-age 2h



# Get detailed JSON output

dapr workflow list --app-id myapp --output json

Workflow History

View the complete execution history:

dapr workflow history wf-12345 --app-id myapp --output json


This shows all events, activities, and state transitions.

External Events
Raising Events via CLI
dapr workflow raise-event wf-12345/ApprovalReceived \

  --app-id myapp \

  --input '{"approved": true, "comments": "Approved by manager"}'

Workflow Suspension and Resumption
Using the CLI
# Suspend for manual intervention

dapr workflow suspend wf-12345 \

  --app-id myapp \

  --reason "Awaiting customer response"



# Resume when ready

dapr workflow resume wf-12345 \

  --app-id myapp \

  --reason "Customer responded"

Workflow identity

Each workflow you define has a type name, and individual executions of a workflow require a unique instance ID. Workflow instance IDs can be generated by your app code, which is useful when workflows correspond to business entities like documents or jobs, or can be auto-generated UUIDs. A workflow’s instance ID is useful for debugging and also for managing workflows using the Workflow APIs.

Only one workflow instance with a given ID can exist at any given time. However, if a workflow instance completes or fails, its ID can be reused by a new workflow instance. Note, however, that the new workflow instance effectively replaces the old one in the configured state store.

Workflow replay

Dapr Workflows maintain their execution state by using a technique known as event sourcing. Instead of storing the current state of a workflow as a snapshot, the workflow engine manages an append-only log of history events that describe the various steps that a workflow has taken. When using the workflow SDK, these history events are stored automatically whenever the workflow “awaits” for the result of a scheduled task.

When a workflow “awaits” a scheduled task, it unloads itself from memory until the task completes. Once the task completes, the workflow engine schedules the workflow function to run again. This second workflow function execution is known as a replay.

When a workflow function is replayed, it runs again from the beginning. However, when it encounters a task that already completed, instead of scheduling that task again, the workflow engine:

Returns the stored result of the completed task to the workflow.
Continues execution until the next “await” point.

This “replay” behavior continues until the workflow function completes or fails with an error.

Using this replay technique, a workflow is able to resume execution from any “await” point as if it had never been unloaded from memory. Even the values of local variables from previous runs can be restored without the workflow engine knowing anything about what data they stored. This ability to restore state makes Dapr Workflows durable and fault tolerant.

Note
The workflow replay behavior described here requires that workflow function code be deterministic. Deterministic workflow functions take the exact same actions when provided the exact same inputs. Learn more about the limitations around deterministic workflow code.
Infinite loops and eternal workflows

As discussed in the workflow replay section, workflows maintain a write-only event-sourced history log of all its operations. To avoid runaway resource usage, workflows must limit the number of operations they schedule. For example, ensure your workflow doesn’t:

Use infinite loops in its implementation
Schedule thousands of tasks.

You can use the following two techniques to write workflows that may need to schedule extreme numbers of tasks:

Use the continue-as-new API: Each workflow SDK exposes a continue-as-new API that workflows can invoke to restart themselves with a new input and history. The continue-as-new API is especially ideal for implementing “eternal workflows”, like monitoring agents, which would otherwise be implemented using a while (true)-like construct. Using continue-as-new is a great way to keep the workflow history size small.

The continue-as-new API truncates the existing history, replacing it with a new history.

Use child workflows: Each workflow SDK exposes an API for creating child workflows. A child workflow behaves like any other workflow, except that it’s scheduled by a parent workflow. Child workflows have:

Their own history
The benefit of distributing workflow function execution across multiple machines.

If a workflow needs to schedule thousands of tasks or more, it’s recommended that those tasks be distributed across child workflows so that no single workflow’s history size grows too large.

Updating workflow code

Because workflows are long-running and durable, updating workflow code must be done with extreme care. As discussed in the workflow determinism limitation section, workflow code must be deterministic. Updates to workflow code must preserve this determinism if there are any non-completed workflow instances in the system. Otherwise, updates to workflow code can result in runtime failures the next time those workflows execute.

See known limitations

Workflow activities

Workflow activities are the basic unit of work in a workflow and are the tasks that get orchestrated in the business process. For example, you might create a workflow to process an order. The tasks may involve checking the inventory, charging the customer, and creating a shipment. Each task would be a separate activity. These activities may be executed serially, in parallel, or some combination of both.

Unlike workflows, activities aren’t restricted in the type of work you can do in them. Activities are frequently used to make network calls or run CPU intensive operations. An activity can also return data back to the workflow.

The Dapr Workflow engine guarantees that each called activity is executed at least once as part of a workflow’s execution. Because activities only guarantee at-least-once execution, it’s recommended that activity logic be implemented as idempotent whenever possible.

Child workflows

In addition to activities, workflows can schedule other workflows as child workflows. A child workflow has its own instance ID, history, and status that is independent of the parent workflow that started it.

Child workflows have many benefits:

You can split large workflows into a series of smaller child workflows, making your code more maintainable.
You can distribute workflow logic across multiple compute nodes concurrently, which is useful if your workflow logic otherwise needs to coordinate a lot of tasks.
You can reduce memory usage and CPU overhead by keeping the history of parent workflow smaller.

The return value of a child workflow is its output. If a child workflow fails with an exception, then that exception is surfaced to the parent workflow, just like it is when an activity task fails with an exception. Child workflows also support automatic retry policies.

Terminating a parent workflow terminates all of the child workflows created by the workflow instance. See the terminate workflow api for more information.

Durable timers

Dapr Workflows allow you to schedule reminder-like durable delays for any time range, including minutes, days, or even years. These durable timers can be scheduled by workflows to implement simple delays or to set up ad-hoc timeouts on other async tasks. More specifically, a durable timer can be set to trigger on a particular date or after a specified duration. There are no limits to the maximum duration of durable timers, which are internally backed by internal actor reminders. For example, a workflow that tracks a 30-day free subscription to a service could be implemented using a durable timer that fires 30-days after the workflow is created. Workflows can be safely unloaded from memory while waiting for a durable timer to fire.

Note
Some APIs in the workflow authoring SDK may internally schedule durable timers to implement internal timeout behavior.
Retry policies

Workflows support durable retry policies for activities and child workflows. Workflow retry policies are separate and distinct from Dapr resiliency policies in the following ways.

Workflow retry policies are configured by the workflow author in code, whereas Dapr Resiliency policies are configured by the application operator in YAML.
Workflow retry policies are durable and maintain their state across application restarts, whereas Dapr Resiliency policies are not durable and must be re-applied after application restarts.
Workflow retry policies are triggered by unhandled errors/exceptions in activities and child workflows, whereas Dapr Resiliency policies are triggered by operation timeouts and connectivity faults.

Retries are internally implemented using durable timers. This means that workflows can be safely unloaded from memory while waiting for a retry to fire, conserving system resources. This also means that delays between retries can be arbitrarily long, including minutes, hours, or even days.

Note
The actions performed by a retry policy are saved into a workflow’s history. Care must be taken not to change the behavior of a retry policy after a workflow has already been executed. Otherwise, the workflow may behave unexpectedly when replayed. See the notes on updating workflow code for more information.

It’s possible to use both workflow retry policies and Dapr Resiliency policies together. For example, if a workflow activity uses a Dapr client to invoke a service, the Dapr client uses the configured resiliency policy. See Quickstart: Service-to-service resiliency for more information with an example. However, if the activity itself fails for any reason, including exhausting the retries on the resiliency policy, then the workflow’s resiliency policy kicks in.

Note
Using workflow retry policies and resiliency policies together can result in unexpected behavior. For example, if a workflow activity exhausts its configured retry policy, the workflow engine will still retry the activity according to the workflow retry policy. This can result in the activity being retried more times than expected.

Because workflow retry policies are configured in code, the exact developer experience may vary depending on the version of the workflow SDK. In general, workflow retry policies can be configured with the following parameters.

Parameter	Description
Maximum number of attempts	The maximum number of times to execute the activity or child workflow. If set to 0, no attempts will be made.
First retry interval	The amount of time to wait before the first retry.
Backoff coefficient	The coefficient used to determine the rate of increase of back-off. For example a coefficient of 2 doubles the wait of each subsequent retry.
Maximum retry interval	The maximum amount of time to wait before each subsequent retry. If set to 0, no retries will happen.
Retry timeout	The global timeout for retries, regardless of any configured max number of attempts. No further attempts are made executing activities after this timeout expires.
External events

Sometimes workflows will need to wait for events that are raised by external systems. For example, an approval workflow may require a human to explicitly approve an order request within an order processing workflow if the total cost exceeds some threshold. Another example is a trivia game orchestration workflow that pauses while waiting for all participants to submit their answers to trivia questions. These mid-execution inputs are referred to as external events.

External events have a name and a payload and are delivered to a single workflow instance. Workflows can create “wait for external event” tasks that subscribe to external events and await those tasks to block execution until the event is received. The workflow can then read the payload of these events and make decisions about which next steps to take. External events can be processed serially or in parallel. External events can be raised by other workflows or by workflow code.

Workflows can also wait for multiple external event signals of the same name, in which case they are dispatched to the corresponding workflow tasks in a first-in, first-out (FIFO) manner. If a workflow receives an external event signal but has not yet created a “wait for external event” task, the event will be saved into the workflow’s history and consumed immediately after the workflow requests the event.

Learn more about external system interaction.

Purging

Workflow state can be purged from a state store, purging all its history and removing all metadata related to a specific workflow instance. The purge capability is used for workflows that have run to a COMPLETED, FAILED, or TERMINATED state.

Learn more in the workflow API reference guide.

Versioning

Workflow code is long-running and must remain deterministic during updates. For details on patching and named workflow versioning, see Workflow versioning.

Limitations
Workflow determinism and code restraints

To take advantage of the workflow replay technique, your workflow code needs to be deterministic. For your workflow code to be deterministic, you may need to work around some limitations.

Workflow functions must call deterministic APIs

APIs that generate random numbers, random UUIDs, or the current date are non-deterministic. To work around this limitation, you can:

Use these APIs in activity functions, or
(Preferred) Use built-in equivalent APIs offered by the SDK. For example, each authoring SDK provides an API for retrieving the current time in a deterministic manner.

For example, instead of this:

.NET
Java
JavaScript
Go
// DON'T DO THIS!

DateTime currentTime = DateTime.UtcNow;

Guid newIdentifier = Guid.NewGuid();

string randomString = GetRandomString();


Do this:

.NET
Java
JavaScript
Go
// Do this!!

DateTime currentTime = context.CurrentUtcDateTime;

Guid newIdentifier = context.NewGuid();

string randomString = await context.CallActivityAsync<string>(nameof("GetRandomString")); //Use "nameof" to prevent specifying an activity name that does not exist in your application

Workflow functions must only interact indirectly with external state.

External data includes any data that isn’t stored in the workflow state. Workflows must not interact with global variables, environment variables, the file system, or make network calls.

Instead, workflows should interact with external state indirectly using workflow inputs, activity tasks, and through external event handling.

For example, instead of this:

.NET
Java
JavaScript
Go
// DON'T DO THIS!

string configuration = Environment.GetEnvironmentVariable("MY_CONFIGURATION")!;

string data = await new HttpClient().GetStringAsync("https://example.com/api/data");


Do this:

.NET
Java
JavaScript
Go
// Do this!!

string configuration = workflowInput.Configuration; // imaginary workflow input argument

string data = await context.CallActivityAsync<string>(nameof("MakeHttpCall"), "https://example.com/api/data");

Workflow functions must execute only on the workflow dispatch thread.

The implementation of each language SDK requires that all workflow function operations operate on the same thread (goroutine, etc.) that the function was scheduled on. Workflow functions must never:

Schedule background threads, or
Use APIs that schedule a callback function to run on another thread.

Failure to follow this rule could result in undefined behavior. Any background processing should instead be delegated to activity tasks, which can be scheduled to run serially or concurrently.

For example, instead of this:

.NET
Java
JavaScript
Go
// DON'T DO THIS!

Task t = Task.Run(() => context.CallActivityAsync("DoSomething"));

await context.CreateTimer(5000).ConfigureAwait(false);


Do this:

.NET
Java
JavaScript
Go
// Do this!!

Task t = context.CallActivityAsync(nameof("DoSomething"));

await context.CreateTimer(5000).ConfigureAwait(true);

Updating workflow code

Make sure updates you make to the workflow code maintain its determinism. Here are a few example of code updates that can break workflow determinism:

Changing the workflow function signature: Changing the name, input, or output of a workflow or activity is considered a breaking change and must be avoided.
Changing the number or order of workflow tasks: Changing the number or order of workflow tasks causes a workflow’s history to no longer match the workflow code and may result in runtime errors or other unexpected behavior.

To work around these constraints, use the workflow versioning concepts described in the versioning guide to patch and introduce new named workflow versions to incorporate changes to your workflows deterministically.

Next steps
Workflow patterns >>
Related links
Try out Dapr Workflow using the quickstart
Workflow overview
Workflow API reference
Try out the following examples:
Python
JavaScript
.NET
Java
Go
3 - Workflow versioning
Version workflows safely as code evolves
Versioning

There are many scenarios where it is necessary to introduce changes to workflow code while workflows are actively running. In cases where these changes are non-deterministic, a versioning strategy is required so that existing workflows can continue executing with the original code, while new workflows use the updated version.

Workflows can be versioned using two complementary approaches and it’s intended that both are used in conjunction with one another. These are:

Patching
Named workflow versioning
Note

In either versioning strategy, workflows can reach the stalled state. This typically occurs during rollouts, when both old and new versions of the workflow code are running at the same time.

A versioned workflow will become stalled when it is started on a new replica, but a subsequent replay is attempted on an old replica.

Workflows can remain stalled for the entire duration of the rollout, until there are only new replicas available. Once a stalled workflow is scheduled on a new replica, it will continue executing.

If a workflow never continues it means the conditions for getting stalled are still present and will need to be addressed. See the specific reasons for getting stalled in the each of the versioning approaches below.

What Does Versioning Solve?

To best understand how versioning works and how to use it effectively, it helps to first understand what it’s solving and why versioning is necesssary at all. Workflows are required to be deterministic meaning that every time they are run, they produce precisely the same output as the last time.

This is a key concept because Dapr Workflows are implemented to use an event sourcing approach to persist the workflow state. As activities and child workflows are executed within the workflow, Dapr is maintaining a history that logs the inputs and outputs at each of those boundary executions. As each completes, we persist the updated event history then re-invoke the workflow from the top (this is called a “replay”). This time, when it hits one of these activities or child workflows, it substitutes in the already-realized output and skips re-executing it and repeats.

Because of this, it’s critical that no code be arbitrarily introduced into a workflow while it’s in-flight because when the engine replays the workflow, your changes risk the workflow no longer matching with its history and failing.

Patching

Patches are the first of our two versioning approaches that allow you to introduce changes to your workflow while keeping it deterministic between replays. It works by allowing you to insert branched logic associated with named identifiers via if statements. The workflow history keeps track of where these named identifiers have been observed while replaying the workflow ensuring that a consistent logical path is followed between replays.

This enables you to apply targeted changes to your workflow code in only those specific places where a tweak is necessary.

To add a patch, select a stable, unique name that identifies the patch. This can be something descriptive like use-sms that characterizes what the patch changes or something that’s inherently different like the current timestamp or date. The specific value you use doesn’t matter so long as you don’t use an identifier that you’ve already deployed into production. You’ll insert the patch by adding an if statement that evaluates if the workflow has applied this patch or not - if so, the patch’s code is used and if not, the original code path is taken.

The uniqueness requirement for the patch identifier only extends to this workflow; patches between workflows are not evaluated, so a duplicate identifier can be used across multiple workflows without conflict.

The following example demonstrates this by checking if the use-sms patch has been applied to this workflow instance. If so, ths SendSMS activity is executed; otherwise, it falls back to the original path and uses the SendEmail activity.

.NET
Go
Python
public sealed class MyWorkflow : Workflow<string, object?>

{

    public overrride async Task<object?> RunAsync(WorkflowContext context, string input)

    {

        // ...

        if (context.IsPatched("use-sms"))

        {

            // Patched code

            await context.CallActivityAsync(nameof(SendSMS), input);

        }

        else {

            // Original code

            await context.CallActivityAsync(nameof(SendEmail), input);

        }

        return null;

    }

}


Using this approach, new workflow instances will take the patched code path but existing workflows that are in-flight when the patch is introduced will continue to use the original code path. Patch checks are recorded in the workflow instance history the first time they are evaluated, meaning that it’s safe to use the same identifier in different places throughout your workflow.

Again, it’s imperative that once your patched workflow is running in production, you do not repurpose that identifier again though. Once deployed, it should be assumed that the engine will handle the workflow deterministically, but adding a new patch with a previously used identifier would break that contract: if your new code was inserted earlier than an in-flight workflow instance had evaluated to that point, when it replayed, it would take your patch branch, but your changes may no longer match the existing workflow history and cause the workflow to stall indefinitely (at least until you removed the new or updated it to use a different unique identifier).

The list of patches applied to a workflow are stored in the workflow’s history, so it’s important to be mindful that the more patches you use, the larger your workflow state history. This will increasingly have a negative impact on workflow performance because it needs to be retrieved every replay and as the state grows, this incurs added retrieval and parsing overhead.

Validating stalls

In addition to the re-use of an identifier as described above, there are several other reasons for workflows to stall when using patches:

Removing (or renaming) a patch identifier
Changing the order of patches

You can use the workflow commands in the Dapr CLI to check for stalled workflows. For example, the following is what the dapr workflow list command would look like if a workflow is stalled:

> dapr workflow list

NAME           ID          STATUS     AGE

workflow       <ID>        STALLED    9m39s


The following is what the dapr workflow history command would look like when a workflow is stalled:

> dapr workflow history <ID> -k -o wide

PLAY  TYPE                 NAME      TIMESTAMP    ELAPSED    STATUS   DETAILS        ROUTER     EXECUTION ID  ATTRS

0     ExecutionStarted     workflow  <TIMESTAMP>  Age:15.8h  RUNNING  workflowStart  workflows  <EXEC_ID>     input=2026-01-22T14:44:02.728101

1     OrchestratorStarted            <TIMESTAMP>  25.3ms     RUNNING  replay                                  versionName=workflow_v1

1     ExecutionStalled               <TIMESTAMP>  8.9m       STALLED                                          reason=VERSION_NAME_MISMATCH;description=Version not available: workflow_v1

Patching best practices

The following represents some additional suggestions that should be considered to eliminate the possibility of a stalled or failed workflow as a result of using patches:

The original code must remain available and unchanged when applying a patch so it’s present for in-flight workflows to evaluate in the same way.
Patches should be applied in an additive way meaning that once they’re added and your application deployed, you should never move nor remove them from your workflow. They must exist to retain in-flight workflow determinism.
As covered above, you must not re-use a patch identifier that you’ve used in previous deployments as this will break the determinism guarantee. However, you’re welcome to use that same identifier within the same deployment in multiple places and without concern across different workflows.
If you can avoid using an else branch when applying your patch, it will make it easier to apply future patches. While this generally can’t be avoided if you’re replacing existing code, it’s certainly manageable if you’re simply adding new logic to your workflow.
If you must nest patches, you must do so within existing patches. For example your new patch cannot wrap an existing patch else in the else branch. Doing so would other mean that the originally code cannot be accessed by in-flight workflows, breaking the determinism guarantee.
Named Workflow Versioning

Named workflow versioning represents our second approach to facilitating a means of versioning your workflows in a deterministically safe way. In this approach, you introduce a new workflow version by duplicating an existing workflow and assigning it a new “versioned” name. Because you can then refactor your workflow logic from scratch to remove any patches and otherwise introduce any other changes you want, this approach offers a clean break from previous workflows versions.

While the particulars of how this is achieved will vary depending on the language SDK you’re using, generally, the idea is that you’ll duplicate your latest workflow, assign it a unique name that reflects the newer version and register this with your SDK. A registry will be built of each workflow so that at runtime, Dapr will call in with a workflow name to execute and the SDK will either route to the old workflow (if in-flight) or to the newer version.

Do note that across all SDKs, the runtime does not migrate workflows between versions sequentially. Rather, when the SDKs receive a request to run a new workflow, it chooses to run the latest version, not simply the “next” one, so there’s is no need to handle any compensation logic between versions.

The language SDKs may expose a way to register versions when using the same workflow name, but this varies by SDK, so refer to the documentation for a specific SDK for more information. For example, some may use a mechanism by which you would explicitly supply an is_latest flag to indicate which version is the latest.

When the SDK receives a request to run a workflow in a version that is not registered, the workflow will stall. This can happen naturally during application rollouts, but can also happen if a version is removed while some workflow instances are still using it. The recommendation is that older named workflow versions should not be deleted at all unless you’ve independently confirmed that there are no outstanding (in-flight or dormant) workflow instances that are running against that version.

.NET
Go
Python

.NET uses a source generator to automatically identify and register your workflow versions, so no manual registration of workflows is necessary (the activities do need to be registered). By default, .NET uses a built-in and configurably numerical versioning strategy where the version is provided as a suffix on the name. See the .NET SDK documentation on how to change versioning strategies or configuration and how to set up versioning in your application.

Since .NET applications do not allow multiple types to exist with the same name, that’s not an option in this SDK.

To create a new named workflow version, duplicate an existing workflow and modify the name of the class to use the same prefix, but change the version identifier in the suffix to reflect a later version. Rebuild your application and the SDK will automatically handle the rest.

Versioning Process Guidance

Because named workflows are fully compatible with patches, the approach is that changes to your workflow are initially made by applying patches to your existing workflow logic. Eventually you’ll hit one of the following problems after applying several patches:

You’re concerned about the overhead to your workflow state history because of the number of applied patches;
The golden path through your workflow logic is hard to follow;
You need to make another workflow tweak, but can’t figure out how to apply a patch that doesn’t break the determinism guarantee.

At this point, the recommendation is that you introduce a named version of your workflow. Copy your existing workflow, change its name to reflect whatever versioning strategy you’re using in your SDK and refactor to remove all your patches and retain only your intended “latest” logic. Apply your new changes (no need for a patch here – it’s a new workflow) and deploy it.

Here, apply patches again as needed to address future changes and when necessary, introduce another named workflow version and continue. Repeat this process indefinitely.

It is recommended that you retain old workflow versions until you’re completely confident that nothing is in-flight (including deferred with a long-running timer) that uses any of your old workflow versions.

Workflow versioning doesn’t address changing the types of inputs and outputs of the workflows themselves. As general guidance, it is recommended to either return serialized values like strings (making the consumer of the output responsible for being able to deserialize different outputs over time) or adopt complex types that incorporate optional properties to include new expected output values.

4 - Workflow patterns
Write different types of workflow patterns

Dapr Workflows simplify complex, stateful coordination requirements in microservice architectures. The following sections describe several application patterns that can benefit from Dapr Workflows.

Task chaining

In the task chaining pattern, multiple steps in a workflow are run in succession, and the output of one step may be passed as the input to the next step. Task chaining workflows typically involve creating a sequence of operations that need to be performed on some data, such as filtering, transforming, and reducing.

In some cases, the steps of the workflow may need to be orchestrated across multiple microservices. For increased reliability and scalability, you’re also likely to use queues to trigger the various steps.

While the pattern is simple, there are many complexities hidden in the implementation. For example:

What happens if one of the microservices are unavailable for an extended period of time?
Can failed steps be automatically retried?
If not, how do you facilitate the rollback of previously completed steps, if applicable?
Implementation details aside, is there a way to visualize the workflow so that other engineers can understand what it does and how it works?

Dapr Workflow solves these complexities by allowing you to implement the task chaining pattern concisely as a simple function in the programming language of your choice, as shown in the following example.

Python
JavaScript
.NET
Java
Go
import dapr.ext.workflow as wf





def task_chain_workflow(ctx: wf.DaprWorkflowContext, wf_input: int):

    try:

        result1 = yield ctx.call_activity(step1, input=wf_input)

        result2 = yield ctx.call_activity(step2, input=result1)

        result3 = yield ctx.call_activity(step3, input=result2)

    except Exception as e:

        yield ctx.call_activity(error_handler, input=str(e))

        raise

    return [result1, result2, result3]





def step1(ctx, activity_input):

    print(f'Step 1: Received input: {activity_input}.')

    # Do some work

    return activity_input + 1





def step2(ctx, activity_input):

    print(f'Step 2: Received input: {activity_input}.')

    # Do some work

    return activity_input * 2





def step3(ctx, activity_input):

    print(f'Step 3: Received input: {activity_input}.')

    # Do some work

    return activity_input ^ 2





def error_handler(ctx, error):

    print(f'Executing error handler: {error}.')

    # Apply some compensating work


Note Workflow retry policies will be available in a future version of the Python SDK.

As you can see, the workflow is expressed as a simple series of statements in the programming language of your choice. This allows any engineer in the organization to quickly understand the end-to-end flow without necessarily needing to understand the end-to-end system architecture.

Behind the scenes, the Dapr Workflow runtime:

Takes care of executing the workflow and ensuring that it runs to completion.
Saves progress automatically.
Automatically resumes the workflow from the last completed step if the workflow process itself fails for any reason.
Enables error handling to be expressed naturally in your target programming language, allowing you to implement compensation logic easily.
Provides built-in retry configuration primitives to simplify the process of configuring complex retry policies for individual steps in the workflow.
Fan-out/fan-in

In the fan-out/fan-in design pattern, you execute multiple tasks simultaneously across potentially multiple workers, wait for them to finish, and perform some aggregation on the result.

In addition to the challenges mentioned in the previous pattern, there are several important questions to consider when implementing the fan-out/fan-in pattern manually:

How do you control the degree of parallelism?
How do you know when to trigger subsequent aggregation steps?
What if the number of parallel steps is dynamic?

Dapr Workflows provides a way to express the fan-out/fan-in pattern as a simple function, as shown in the following example:

# Start the workflow

dapr workflow run DataProcessingWorkflow \

  --app-id processor \

  --input '{"items": ["item1", "item2", "item3"]}'



# Monitor parallel execution

dapr workflow history <instance-id> --app-id processor --output json

Python
JavaScript
.NET
Java
Go
import time

from typing import List

import dapr.ext.workflow as wf





def batch_processing_workflow(ctx: wf.DaprWorkflowContext, wf_input: int):

    # get a batch of N work items to process in parallel

    work_batch = yield ctx.call_activity(get_work_batch, input=wf_input)



    # schedule N parallel tasks to process the work items and wait for all to complete

    parallel_tasks = [ctx.call_activity(process_work_item, input=work_item) for work_item in work_batch]

    outputs = yield wf.when_all(parallel_tasks)



    # aggregate the results and send them to another activity

    total = sum(outputs)

    yield ctx.call_activity(process_results, input=total)





def get_work_batch(ctx, batch_size: int) -> List[int]:

    return [i + 1 for i in range(batch_size)]





def process_work_item(ctx, work_item: int) -> int:

    print(f'Processing work item: {work_item}.')

    time.sleep(5)

    result = work_item * 2

    print(f'Work item {work_item} processed. Result: {result}.')

    return result





def process_results(ctx, final_result: int):

    print(f'Final result: {final_result}.')


The key takeaways from this example are:

The fan-out/fan-in pattern can be expressed as a simple function using ordinary programming constructs
The number of parallel tasks can be static or dynamic
The workflow itself is capable of aggregating the results of parallel executions

Furthermore, the execution of the workflow is durable. If a workflow starts 100 parallel task executions and only 40 complete before the process crashes, the workflow restarts itself automatically and only schedules the remaining 60 tasks.

It’s possible to go further and limit the degree of concurrency using simple, language-specific constructs. The sample code below illustrates how to restrict the degree of fan-out to just 5 concurrent activity executions:

.NET


//Revisiting the earlier example...

// Get a list of N work items to process in parallel.

object[] workBatch = await context.CallActivityAsync<object[]>("GetWorkBatch", null);



const int MaxParallelism = 5;

var results = new List<int>();

var inFlightTasks = new HashSet<Task<int>>();

foreach(var workItem in workBatch)

{

  if (inFlightTasks.Count >= MaxParallelism)

  {

    var finishedTask = await Task.WhenAny(inFlightTasks);

    results.Add(finishedTask.Result);

    inFlightTasks.Remove(finishedTask);

  }



  inFlightTasks.Add(context.CallActivityAsync<int>("ProcessWorkItem", workItem));

}

results.AddRange(await Task.WhenAll(inFlightTasks));



var sum = results.Sum(t => t);

await context.CallActivityAsync("PostResults", sum);


You can process workflow activities in parallel while putting an upper cap on concurrency by using the following extension methods on the WorkflowContext:

.NET
//Revisiting the earlier example...

// Get a list of work items to process

var workBatch = await context.CallActivityAsync<object[]>("GetWorkBatch", null);



// Process deterministically in parallel with an upper cap of 5 activities at a time

var results = await context.ProcessInParallelAsync(workBatch, workItem => context.CallActivityAsync<int>("ProcessWorkItem", workItem), maxConcurrency: 5);



var sum = results.Sum(t => t);

await context.CallActivityAsync("PostResults", sum);


Limiting the degree of concurrency in this way can be useful for limiting contention against shared resources. For example, if the activities need to call into external resources that have their own concurrency limits, like a databases or external APIs, it can be useful to ensure that no more than a specified number of activities call that resource concurrently.

Async HTTP APIs

Asynchronous HTTP APIs are typically implemented using the Asynchronous Request-Reply pattern. Implementing this pattern traditionally involves the following:

A client sends a request to an HTTP API endpoint (the start API)
The start API writes a message to a backend queue, which triggers the start of a long-running operation
Immediately after scheduling the backend operation, the start API returns an HTTP 202 response to the client with an identifier that can be used to poll for status
The status API queries a database that contains the status of the long-running operation
The client repeatedly polls the status API either until some timeout expires or it receives a “completion” response

The end-to-end flow is illustrated in the following diagram.

The challenge with implementing the asynchronous request-reply pattern is that it involves the use of multiple APIs and state stores. It also involves implementing the protocol correctly so that the client knows how to automatically poll for status and know when the operation is complete.

The Dapr workflow HTTP API supports the asynchronous request-reply pattern out-of-the box, without requiring you to write any code or do any state management.

The following curl commands illustrate how the workflow APIs support this pattern.

curl -X POST http://localhost:3500/v1.0/workflows/dapr/OrderProcessingWorkflow/start?instanceID=12345678 -d '{"Name":"Paperclips","Quantity":1,"TotalCost":9.95}'


The previous command will result in the following response JSON:

{"instanceID":"12345678"}


The HTTP client can then construct the status query URL using the workflow instance ID and poll it repeatedly until it sees the “COMPLETE”, “FAILURE”, or “TERMINATED” status in the payload.

curl http://localhost:3500/v1.0/workflows/dapr/12345678


The following is an example of what an in-progress workflow status might look like.

{

  "instanceID": "12345678",

  "workflowName": "OrderProcessingWorkflow",

  "createdAt": "2023-05-03T23:22:11.143069826Z",

  "lastUpdatedAt": "2023-05-03T23:22:22.460025267Z",

  "runtimeStatus": "RUNNING",

  "properties": {

    "dapr.workflow.custom_status": "",

    "dapr.workflow.input": "{\"Name\":\"Paperclips\",\"Quantity\":1,\"TotalCost\":9.95}"

  }

}


As you can see from the previous example, the workflow’s runtime status is RUNNING, which lets the client know that it should continue polling.

If the workflow has completed, the status might look as follows.

{

  "instanceID": "12345678",

  "workflowName": "OrderProcessingWorkflow",

  "createdAt": "2023-05-03T23:30:11.381146313Z",

  "lastUpdatedAt": "2023-05-03T23:30:52.923870615Z",

  "runtimeStatus": "COMPLETED",

  "properties": {

    "dapr.workflow.custom_status": "",

    "dapr.workflow.input": "{\"Name\":\"Paperclips\",\"Quantity\":1,\"TotalCost\":9.95}",

    "dapr.workflow.output": "{\"Processed\":true}"

  }

}


As you can see from the previous example, the runtime status of the workflow is now COMPLETED, which means the client can stop polling for updates.

Monitor

The monitor pattern is recurring process that typically:

Checks the status of a system
Takes some action based on that status - e.g. send a notification
Sleeps for some period of time
Repeat

The following diagram provides a rough illustration of this pattern.

Depending on the business needs, there may be a single monitor or there may be multiple monitors, one for each business entity (for example, a stock). Furthermore, the amount of time to sleep may need to change, depending on the circumstances. These requirements make using cron-based scheduling systems impractical.

Dapr Workflow supports this pattern natively by allowing you to implement eternal workflows. Rather than writing infinite while-loops (which is an anti-pattern), Dapr Workflow exposes a continue-as-new API that workflow authors can use to restart a workflow function from the beginning with a new input.

Python
JavaScript
.NET
Java
Go
from dataclasses import dataclass

from datetime import timedelta

import random

import dapr.ext.workflow as wf





@dataclass

class JobStatus:

    job_id: str

    is_healthy: bool





def status_monitor_workflow(ctx: wf.DaprWorkflowContext, job: JobStatus):

    # poll a status endpoint associated with this job

    status = yield ctx.call_activity(check_status, input=job)

    if not ctx.is_replaying:

        print(f"Job '{job.job_id}' is {status}.")



    if status == "healthy":

        job.is_healthy = True

        next_sleep_interval = 60  # check less frequently when healthy

    else:

        if job.is_healthy:

            job.is_healthy = False

            ctx.call_activity(send_alert, input=f"Job '{job.job_id}' is unhealthy!")

        next_sleep_interval = 5  # check more frequently when unhealthy



    yield ctx.create_timer(fire_at=ctx.current_utc_datetime + timedelta(minutes=next_sleep_interval))



    # restart from the beginning with a new JobStatus input

    ctx.continue_as_new(job)





def check_status(ctx, _) -> str:

    return random.choice(["healthy", "unhealthy"])





def send_alert(ctx, message: str):

    print(f'*** Alert: {message}')


A workflow implementing the monitor pattern can loop forever or it can terminate itself gracefully by not calling continue-as-new.

Note
This pattern can also be expressed using actors and reminders. The difference is that this workflow is expressed as a single function with inputs and state stored in local variables. Workflows can also execute a sequence of actions with stronger reliability guarantees, if necessary.
External system interaction

In some cases, a workflow may need to pause and wait for an external system to perform some action. For example, a workflow may need to pause and wait for a payment to be received. In this case, a payment system might publish an event to a pub/sub topic on receipt of a payment, and a listener on that topic can raise an event to the workflow using the raise event workflow API.

Another very common scenario is when a workflow needs to pause and wait for a human, for example when approving a purchase order. Dapr Workflow supports this event pattern via the external events feature.

Here’s an example workflow for a purchase order involving a human:

A workflow is triggered when a purchase order is received.
A rule in the workflow determines that a human needs to perform some action. For example, the purchase order cost exceeds a certain auto-approval threshold.
The workflow sends a notification requesting a human action. For example, it sends an email with an approval link to a designated approver.
The workflow pauses and waits for the human to either approve or reject the order by clicking on a link.
If the approval isn’t received within the specified time, the workflow resumes and performs some compensation logic, such as canceling the order.

The following diagram illustrates this flow.

The following example code shows how this pattern can be implemented using Dapr Workflow.

Python
JavaScript
.NET
Java
Go
from dataclasses import dataclass

from datetime import timedelta

import dapr.ext.workflow as wf





@dataclass

class Order:

    cost: float

    product: str

    quantity: int



    def __str__(self):

        return f'{self.product} ({self.quantity})'





@dataclass

class Approval:

    approver: str



    @staticmethod

    def from_dict(dict):

        return Approval(**dict)





def purchase_order_workflow(ctx: wf.DaprWorkflowContext, order: Order):

    # Orders under $1000 are auto-approved

    if order.cost < 1000:

        return "Auto-approved"



    # Orders of $1000 or more require manager approval

    yield ctx.call_activity(send_approval_request, input=order)



    # Approvals must be received within 24 hours or they will be canceled.

    approval_event = ctx.wait_for_external_event("approval_received")

    timeout_event = ctx.create_timer(timedelta(hours=24))

    winner = yield wf.when_any([approval_event, timeout_event])

    if winner == timeout_event:

        return "Cancelled"



    # The order was approved

    yield ctx.call_activity(place_order, input=order)

    approval_details = Approval.from_dict(approval_event.get_result())

    return f"Approved by '{approval_details.approver}'"





def send_approval_request(_, order: Order) -> None:

    print(f'*** Sending approval request for order: {order}')





def place_order(_, order: Order) -> None:

    print(f'*** Placing order: {order}')


The code that delivers the event to resume the workflow execution is external to the workflow. Workflow events can be delivered to a waiting workflow instance using the raise event workflow management API, as shown in the following example:

Python
JavaScript
.NET
Java
Go
from dapr.clients import DaprClient

from dataclasses import asdict



with DaprClient() as d:

    d.raise_workflow_event(

        instance_id=instance_id,

        workflow_component="dapr",

        event_name="approval_received",

        event_data=asdict(Approval("Jane Doe")))


External events don’t have to be directly triggered by humans. They can also be triggered by other systems. For example, a workflow may need to pause and wait for a payment to be received. In this case, a payment system might publish an event to a pub/sub topic on receipt of a payment, and a listener on that topic can raise an event to the workflow using the raise event workflow API.

Compensation

The compensation pattern (also known as the saga pattern) provides a mechanism for rolling back or undoing operations that have already been executed when a workflow fails partway through. This pattern is particularly important for long-running workflows that span multiple microservices where traditional database transactions are not feasible.

In distributed microservice architectures, you often need to coordinate operations across multiple services. When these operations cannot be wrapped in a single transaction, the compensation pattern provides a way to maintain consistency by defining compensating actions for each step in the workflow.

The compensation pattern addresses several critical challenges:

Distributed Transaction Management: When a workflow spans multiple microservices, each with their own data stores, traditional ACID transactions are not possible. The compensation pattern provides transactional consistency by ensuring operations are either all completed successfully or all undone through compensation.
Partial Failure Recovery: If a workflow fails after some steps have completed successfully, the compensation pattern allows you to undo those completed steps gracefully.
Business Process Integrity: Ensures that business processes can be properly rolled back in case of failures, maintaining the integrity of your business operations.
Long-Running Processes: For workflows that may run for hours, days, or longer, traditional locking mechanisms are impractical. Compensation provides a way to handle failures in these scenarios.

Common use cases for the compensation pattern include:

E-commerce Order Processing: Reserve inventory, charge payment, and ship orders. If shipping fails, you need to release the inventory and refund the payment.
Financial Transactions: In a money transfer, if crediting the destination account fails, you need to rollback the debit from the source account.
Resource Provisioning: When provisioning cloud resources across multiple providers, if one step fails, you need to clean up all previously provisioned resources.
Multi-Step Business Processes: Any business process that involves multiple irreversible steps that may need to be undone in case of later failures.

Dapr Workflow provides support for the compensation pattern, allowing you to register compensation activities for each step and execute them in reverse order when needed.

Here’s an example workflow for an e-commerce process:

A workflow is triggered when an order is received.
A reservation is made for the order in the inventory.
The payment is processed.
The order is shipped.
If any of the above actions results in an error, the actions are compensated with another action:
The shipment is cancelled.
The payment is refunded.
The inventory reservation is released.

The following diagram illustrates this flow.

Java
public class PaymentProcessingWorkflow implements Workflow {



    @Override

    public WorkflowStub create() {

        return ctx -> {

            ctx.getLogger().info("Starting Workflow: " + ctx.getName());

            var orderId = ctx.getInput(String.class);

            List<String> compensations = new ArrayList<>();



            try {

                // Step 1: Reserve inventory

                String reservationId = ctx.callActivity(ReserveInventoryActivity.class.getName(), orderId, String.class).await();

                ctx.getLogger().info("Inventory reserved: {}", reservationId);

                compensations.add("ReleaseInventory");



                // Step 2: Process payment

                String paymentId = ctx.callActivity(ProcessPaymentActivity.class.getName(), orderId, String.class).await();

                ctx.getLogger().info("Payment processed: {}", paymentId);

                compensations.add("RefundPayment");



                // Step 3: Ship order

                String shipmentId = ctx.callActivity(ShipOrderActivity.class.getName(), orderId, String.class).await();

                ctx.getLogger().info("Order shipped: {}", shipmentId);

                compensations.add("CancelShipment");



            } catch (TaskFailedException e) {

                ctx.getLogger().error("Activity failed: {}", e.getMessage());



                // Execute compensations in reverse order

                Collections.reverse(compensations);

                for (String compensation : compensations) {

                    try {

                        switch (compensation) {

                            case "CancelShipment":

                                String shipmentCancelResult = ctx.callActivity(

                                    CancelShipmentActivity.class.getName(),

                                    orderId,

                                    String.class).await();

                                ctx.getLogger().info("Shipment cancellation completed: {}", shipmentCancelResult);

                                break;



                            case "RefundPayment":

                                String refundResult = ctx.callActivity(

                                    RefundPaymentActivity.class.getName(),

                                    orderId,

                                    String.class).await();

                                ctx.getLogger().info("Payment refund completed: {}", refundResult);

                                break;



                            case "ReleaseInventory":

                                String releaseResult = ctx.callActivity(

                                    ReleaseInventoryActivity.class.getName(),

                                    orderId,

                                    String.class).await();

                                ctx.getLogger().info("Inventory release completed: {}", releaseResult);

                                break;

                        }

                    } catch (TaskFailedException ex) {

                        ctx.getLogger().error("Compensation activity failed: {}", ex.getMessage());

                    }

                }

                ctx.complete("Order processing failed, compensation applied");

            }



			// Step 4: Send confirmation

			ctx.callActivity(SendConfirmationActivity.class.getName(), orderId, Void.class).await();

            ctx.getLogger().info("Confirmation sent for order: {}", orderId);



            ctx.complete("Order processed successfully: " + orderId);

        };

    }

}



// Example activities

class ReserveInventoryActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to reserve inventory

        String reservationId = "reservation_" + orderId;

        System.out.println("Reserved inventory for order: " + orderId);

        return reservationId;

    }

}



class ReleaseInventoryActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String reservationId = ctx.getInput(String.class);

        // Logic to release inventory reservation

        System.out.println("Released inventory reservation: " + reservationId);

        return "Released: " + reservationId;

    }

}



class ProcessPaymentActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to process payment

        String paymentId = "payment_" + orderId;

        System.out.println("Processed payment for order: " + orderId);

        return paymentId;

    }

}



class RefundPaymentActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String paymentId = ctx.getInput(String.class);

        // Logic to refund payment

        System.out.println("Refunded payment: " + paymentId);

        return "Refunded: " + paymentId;

    }

}



class ShipOrderActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to ship order

        String shipmentId = "shipment_" + orderId;

        System.out.println("Shipped order: " + orderId);

        return shipmentId;

    }

}



class CancelShipmentActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String shipmentId = ctx.getInput(String.class);

        // Logic to cancel shipment

        System.out.println("Canceled shipment: " + shipmentId);

        return "Canceled: " + shipmentId;

    }

}



class SendConfirmationActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to send confirmation

        System.out.println("Sent confirmation for order: " + orderId);

        return null;

    }

}


The key benefits of using Dapr Workflow’s compensation pattern include:

Compensation Control: You have full control over when and how compensation activities are executed.
Flexible Configuration: You can implement custom logic for determining which compensations to run.
Error Handling: Handle compensation failures according to your specific business requirements.
Simple Implementation: No additional framework dependencies - just standard workflow activities and exception handling.

The compensation pattern ensures that your distributed workflows can maintain consistency and recover gracefully from failures, making it an essential tool for building reliable microservice architectures.

Next steps
Workflow architecture >>
Related links
Try out Dapr Workflows using the quickstart
Workflow overview
Workflow API reference
Try out the following examples:
Python
JavaScript
.NET
Java
Go
5 - Workflow architecture
The Dapr Workflow engine architecture

Dapr Workflows allow developers to define workflows using ordinary code in a variety of programming languages. The workflow engine runs inside of the Dapr sidecar and orchestrates workflow code deployed as part of your application. Dapr Workflows are built on top of Dapr Actors providing durability and scalability for workflow execution.

This article describes:

The architecture of the Dapr Workflow engine
How the workflow engine interacts with application code
How the workflow engine fits into the overall Dapr architecture
How different workflow backends can work with workflow engine

For more information on how to author Dapr Workflows in your application, see How to: Author a workflow.

The Dapr Workflow engine is internally powered by Dapr’s actor runtime. The following diagram illustrates the Dapr Workflow architecture in Kubernetes mode:

To use the Dapr Workflow building block, you write workflow code in your application using the Dapr Workflow SDK, which internally connects to the sidecar using a gRPC stream. This registers the workflow and any workflow activities, or tasks that workflows can schedule.

The engine is embedded directly into the sidecar and implemented using the durabletask-go framework library. This framework allows you to swap out different storage providers, including a storage provider created for Dapr that leverages internal actors behind the scenes. Since Dapr Workflows use actors, you can store workflow state in state stores.

Sidecar interactions

When a workflow application starts up, it uses a workflow authoring SDK to send a gRPC request to the Dapr sidecar and get back a stream of workflow work items, following the server streaming RPC pattern. These work items can be anything from “start a new X workflow” (where X is the type of a workflow) to “schedule activity Y with input Z to run on behalf of workflow X”.

The workflow app executes the appropriate workflow code and then sends a gRPC request back to the sidecar with the execution results.

All interactions happen over a single gRPC channel and are initiated by the application, which means the application doesn’t need to open any inbound ports. The details of these interactions are internally handled by the language-specific Dapr Workflow authoring SDK.

Differences between workflow and application actor interactions

If you’re familiar with Dapr actors, you may notice a few differences in terms of how sidecar interactions works for workflows compared to application defined actors.

Actors	Workflows
Actors created by the application can interact with the sidecar using either HTTP or gRPC.	Workflows only use gRPC. Due to the workflow gRPC protocol’s complexity, an SDK is required when implementing workflows.
Actor operations are pushed to application code from the sidecar. This requires the application to listen on a particular app port.	For workflows, operations are pulled from the sidecar by the application using a streaming protocol. The application doesn’t need to listen on any ports to run workflows.
Actors explicitly register themselves with the sidecar.	Workflows do not register themselves with the sidecar. The embedded engine doesn’t keep track of workflow types. This responsibility is instead delegated to the workflow application and its SDK.
Workflow distributed tracing

The durabletask-go core used by the workflow engine writes distributed traces using Open Telemetry SDKs. These traces are captured automatically by the Dapr sidecar and exported to the configured Open Telemetry provider, such as Zipkin.

Each workflow instance managed by the engine is represented as one or more spans. There is a single parent span representing the full workflow execution and child spans for the various tasks, including spans for activity task execution and durable timers.

Workflow activity code currently does not have access to the trace context.

Workflow actors

Upon the workflow client connecting to the sidecar, there are two types of actors that are registered in support of the workflow engine:

dapr.internal.{namespace}.{appID}.workflow
dapr.internal.{namespace}.{appID}.activity

The {namespace} value is the Dapr namespace and defaults to default if no namespace is configured. The {appID} value is the app’s ID. For example, if you have a workflow app named “wfapp”, then the type of the workflow actor would be dapr.internal.default.wfapp.workflow and the type of the activity actor would be dapr.internal.default.wfapp.activity.

The following diagram demonstrates how workflow actors operate in a Kubernetes scenario:

Just like user-defined actors, workflow actors are distributed across the cluster by the hashing lookup table provided by the actor placement service. They also maintain their own state and make use of reminders. However, unlike actors that live in application code, these workflow actors are embedded into the Dapr sidecar. Application code is completely unaware that these actors exist.

Note

The workflow actor types are only registered after an app has registered a workflow using a Dapr Workflow SDK. If an app never registers a workflow, then the internal workflow actors are never registered.

Workflow actors

There are 2 different types of actors used with workflows: workflow actors and activity actors. Workflow actors are responsible for managing the state and placement of all workflows running in the app. A new instance of the workflow actor is activated for every workflow instance that gets scheduled. The ID of the workflow actor is the ID of the workflow. This workflow actor stores the state of the workflow as it progresses, and determines the node on which the workflow code executes via the actor lookup table.

As workflows are based on actors, all workflow and activity work is randomly distributed across all replicas of the application implementing workflows. There is no locality or relationship between where a workflow is started and where each work item is executed.

Each workflow actor saves its state using the following keys in the configured actor state store:

Key	Description
inbox-NNNNNN	A workflow’s inbox is effectively a FIFO queue of messages that drive a workflow’s execution. Example messages include workflow creation messages, activity task completion messages, etc. Each message is stored in its own key in the state store with the name inbox-NNNNNN where NNNNNN is a 6-digit number indicating the ordering of the messages. These state keys are removed once the corresponding messages are consumed by the workflow.
history-NNNNNN	A workflow’s history is an ordered list of events that represent a workflow’s execution history. Each key in the history holds the data for a single history event. Like an append-only log, workflow history events are only added and never removed (except when a workflow performs a “continue as new” operation, which purges all history and restarts a workflow with a new input).
customStatus	Contains a user-defined workflow status value. There is exactly one customStatus key for each workflow actor instance.
metadata	Contains meta information about the workflow as a JSON blob and includes details such as the length of the inbox, the length of the history, and a 64-bit integer representing the workflow generation (for cases where the instance ID gets reused). The length information is used to determine which keys need to be read or written to when loading or saving workflow state updates.
Warning
Workflow actor state remains in the state store even after a workflow has completed.


Creating a large number of workflows could result in unbounded storage usage. To address this either purge workflows using their ID or directly delete entries in the workflow DB store.

The following diagram illustrates the typical lifecycle of a workflow actor.

To summarize:

A workflow actor is activated when it receives a new message.
New messages then trigger the associated workflow code (in your application) to run and return an execution result back to the workflow actor.
Once the result is received, the actor schedules any tasks as necessary.
After scheduling, the actor updates its state in the state store.
Finally, the actor goes idle until it receives another message. During this idle time, the sidecar may decide to unload the workflow actor from memory.
Activity actors

Activity actors are responsible for managing the state and placement of all workflow activity invocations. A new instance of the activity actor is activated for every activity task that gets scheduled by a workflow. The ID of the activity actor is the ID of the workflow combined with a sequence number (sequence numbers start with 0), as well as the “generation” (incremented during instances of rerunning from using continue as new). For example, if a workflow has an ID of 876bf371 and is the third activity to be scheduled by the workflow, it’s ID will be 876bf371::2::1 where 2 is the sequence number, and 1 is the generation. If the activity is scheduled again after a continue as new, the ID will be 876bf371::2::2.

No state is stored by activity actors, and instead all resulting data is sent back to the parent workflow actor.

The following diagram illustrates the typical lifecycle of an activity actor.

Activity actors are short-lived:

Activity actors are activated when a workflow actor schedules an activity task.
Activity actors then immediately call into the workflow application to invoke the associated activity code.
Once the activity code has finished running and has returned its result, the activity actor sends a message to the parent workflow actor with the execution results.
The activity actor then deactivates itself.
Once the results are sent, the workflow is triggered to move forward to its next step.
Reminder usage and execution guarantees

The Dapr Workflow ensures workflow fault-tolerance by using actor reminders to recover from transient system failures. Prior to invoking application workflow code, the workflow or activity actor will create a new reminder. These reminders are made “one shot”, meaning that they will expire after successful triggering. If the application code executes without interruption, the reminder is triggered and expired. However, if the node or the sidecar hosting the associated workflow or activity crashes, the reminder will reactivate the corresponding actor and the execution will be retried, forever.

State store usage

Dapr Workflows use actors internally to drive the execution of workflows. Like any actors, these workflow actors store their state in the configured actor state store. This is done by specifying a state store component in your Dapr configuration and then referencing that state store in the actorStateStore property of the configuration’s actors section. Read the state API reference and the actors API reference to learn more about state stores for actors.

Any state store that supports actors implicitly supports Dapr Workflow.

As discussed in the workflow actors section, workflows save their state incrementally by appending to a history log. The history log for a workflow is distributed across multiple state store keys so that each “checkpoint” only needs to append the newest entries.

The size of each checkpoint is determined by the number of concurrent actions scheduled by the workflow before it goes into an idle state. Sequential workflows will therefore make smaller batch updates to the state store, while fan-out/fan-in workflows will require larger batches. The size of the batch is also impacted by the size of inputs and outputs when workflows invoke activities or child workflows.

Different state store implementations may implicitly put restrictions on the types of workflows you can author. For example, the Azure Cosmos DB state store limits item sizes to 2 MB of UTF-8 encoded JSON (source). The input or output payload of an activity or child workflow is stored as a single record in the state store, so a item limit of 2 MB means that workflow and activity inputs and outputs can’t exceed 2 MB of JSON-serialized data.

Similarly, if a state store imposes restrictions on the size of a batch transaction, that may limit the number of parallel actions that can be scheduled by a workflow.

Workflow state can be purged from a state store, including all its history. Each Dapr SDK exposes APIs for purging all metadata related to specific workflow instances.

State store record count

The number of records which are saved as history in the state store per workflow run is determined by its complexity or “shape”. In other words, the number of activities, timers, sub-workflows etc. The following table shows a general guide to the number of records that are saved by different workflow tasks. This number may be larger or smaller depending on retries or concurrency.

Task type	Number of records saved
Start workflow	5 records
Call activity	3 records
Timer	3 records
Raise event	3 records
Start child workflow	8 records
Query Workflow History
dapr workflow --app-id myapp list

dapr workflow --app-id myapp history <instance-id>

Supported State Stores

The workflow engine supports these state stores:

PostgreSQL
MySQL
SQL Server
SQLite
Oracle Database
CockroachDB
MongoDB
Redis
Workflow scalability

Because Dapr Workflows are internally implemented using actors, Dapr Workflows have the same scalability characteristics as actors. The placement service:

Doesn’t distinguish between workflow actors and actors you define in your application
Will load balance workflows using the same algorithms that it uses for actors

The expected scalability of a workflow is determined by the following factors:

The number of machines used to host your workflow application
The CPU and memory resources available on the machines running workflows
The scalability of the state store configured for actors
The scalability of the actor placement service and the reminder subsystem

The implementation details of the workflow code in the target application also plays a role in the scalability of individual workflow instances. Each workflow instance executes on a single node at a time, but a workflow can schedule activities and child workflows which run on other nodes.

Workflows can also schedule these activities and child workflows to run in parallel, allowing a single workflow to potentially distribute compute tasks across all available nodes in the cluster.

You can configure the maximum concurrency of workflows and activities using the Dapr configuration as described in the next section.

Important
By default, there are no global limits imposed on workflow and activity concurrency. A runaway workflow could therefore potentially consume all resources in a cluster if it attempts to schedule too many tasks in parallel. Use care when authoring Dapr Workflows that schedule large batches of work in parallel.
Important
The Dapr Workflow engine requires that all instances of a workflow app register the exact same set of workflows and activities. In other words, it’s not possible to scale certain workflows or activities independently. All workflows and activities within an app must be scaled together.

Workflows don’t control the specifics of how load is distributed across the cluster. For example, if a workflow schedules 10 activity tasks to run in parallel, all 10 tasks may run on as many as 10 different compute nodes or as few as a single compute node. The actual scale behavior is determined by the actor placement service, which manages the distribution of the actors that represent each of the workflow’s tasks.

Workflow latency

In order to provide guarantees around durability and resiliency, Dapr Workflows frequently write to the state store and rely on reminders to drive execution. Dapr Workflows therefore may not be appropriate for latency-sensitive workloads. Expected sources of high latency include:

Latency from the state store when persisting workflow state.
Latency from the state store when rehydrating workflows with large histories.
Latency caused by too many active reminders in the cluster.
Latency caused by high CPU usage in the cluster.

See the Reminder usage and execution guarantees section for more details on how the design of workflow actors may impact execution latency.

Increasing scheduling throughput

By default, when a client schedules a workflow, the workflow engine waits for the workflow to be fully started before returning a response to the client. Waiting for the workflow to start before returning can decrease the scheduling throughput of workflows. When scheduling a workflow with a start time, the workflow engine does not wait for the workflow to start before returning a response to the client. To increase scheduling throughput, consider adding a start time of “now” when scheduling a workflow. An example of scheduling a workflow with a start time of “now” in the Go SDK is shown below:

client.ScheduleNewWorkflow(ctx, "MyCoolWorkflow", workflow.WithStartTime(time.Now()))

Workflows cluster deployment when using Dapr Shared with workflow
Note
The following feature is only available when the Workflows Clustered Deployment preview feature is enabled.

When using Dapr Shared, it can be the case that there are multiple daprd sidecars running behind a single load balancer or service. As such, the instance to which a worker receiving work, may not be the same instance that receives the work result. Dapr creates a third actor type to handle this scenario: dapr.internal.{namespace}.{appID}.executor to handle routing of the worker results back to the correct workflow actor to ensure correct operation.

Next steps
Author workflows >>
Related links
Workflow overview
Workflow API reference
Try out the Workflow quickstart
Try out the following examples:
Python
JavaScript example
.NET
Java
Go example
6 - How to: Author a workflow
Learn how to develop and author workflows

This article provides a high-level overview of how to author workflows that are executed by the Dapr Workflow engine.

Note
If you haven’t already, try out the workflow quickstart for a quick walk-through on how to use workflows.
Author workflows as code

Dapr Workflow logic is implemented using general purpose programming languages, allowing you to:

Use your preferred programming language (no need to learn a new DSL or YAML schema).
Have access to the language’s standard libraries.
Build your own libraries and abstractions.
Use debuggers and examine local variables.
Write unit tests for your workflows, just like any other part of your application logic.

The Dapr sidecar doesn’t load any workflow definitions. Rather, the sidecar simply drives the execution of the workflows, leaving all the workflow activities to be part of the application.

Write the workflow activities

Workflow activities are the basic unit of work in a workflow and are the tasks that get orchestrated in the business process.

Python
JavaScript
.NET
Java
Go

Define the workflow activities you’d like your workflow to perform. Activities are a function definition and can take inputs and outputs. The following example creates a counter (activity) called hello_act that notifies users of the current counter value. hello_act is a function derived from a class called WorkflowActivityContext.

@wfr.activity(name='hello_act')

def hello_act(ctx: WorkflowActivityContext, wf_input):

    global counter

    counter += wf_input

    print(f'New counter value is: {counter}!', flush=True)


See the task chaining workflow activity in context.

Write the workflow

Next, register and call the activites in a workflow.

Python
JavaScript
.NET
Java
Go

The hello_world_wf function is a function derived from a class called DaprWorkflowContext with input and output parameter types. It also includes a yield statement that does the heavy lifting of the workflow and calls the workflow activities.

@wfr.workflow(name='hello_world_wf')

def hello_world_wf(ctx: DaprWorkflowContext, wf_input):

    print(f'{wf_input}')

    yield ctx.call_activity(hello_act, input=1)

    yield ctx.call_activity(hello_act, input=10)

    yield ctx.call_activity(hello_retryable_act, retry_policy=retry_policy)

    yield ctx.call_child_workflow(child_retryable_wf, retry_policy=retry_policy)



    # Change in event handling: Use when_any to handle both event and timeout

    event = ctx.wait_for_external_event(event_name)

    timeout = ctx.create_timer(timedelta(seconds=30))

    winner = yield when_any([event, timeout])



    if winner == timeout:

        print('Workflow timed out waiting for event')

        return 'Timeout'



    yield ctx.call_activity(hello_act, input=100)

    yield ctx.call_activity(hello_act, input=1000)

    return 'Completed'


See the hello_world_wf workflow in context.

Write the application

Finally, compose the application using the workflow.

Python
JavaScript
.NET
Java
Go

In the following example, for a basic Python hello world application using the Python SDK, your project code would include:

A Python package called DaprClient to receive the Python SDK capabilities.
A builder with extensions called:
WorkflowRuntime: Allows you to register the workflow runtime.
DaprWorkflowContext: Allows you to create workflows
WorkflowActivityContext: Allows you to create workflow activities
API calls. In the example below, these calls start, pause, resume, purge, and completing the workflow.
from datetime import timedelta

from time import sleep

from dapr.ext.workflow import (

    WorkflowRuntime,

    DaprWorkflowContext,

    WorkflowActivityContext,

    RetryPolicy,

    DaprWorkflowClient,

    when_any,

)

from dapr.conf import Settings

from dapr.clients.exceptions import DaprInternalError



settings = Settings()



counter = 0

retry_count = 0

child_orchestrator_count = 0

child_orchestrator_string = ''

child_act_retry_count = 0

instance_id = 'exampleInstanceID'

child_instance_id = 'childInstanceID'

workflow_name = 'hello_world_wf'

child_workflow_name = 'child_wf'

input_data = 'Hi Counter!'

event_name = 'event1'

event_data = 'eventData'

non_existent_id_error = 'no such instance exists'



retry_policy = RetryPolicy(

    first_retry_interval=timedelta(seconds=1),

    max_number_of_attempts=3,

    backoff_coefficient=2,

    max_retry_interval=timedelta(seconds=10),

    retry_timeout=timedelta(seconds=100),

)



wfr = WorkflowRuntime()





@wfr.workflow(name='hello_world_wf')

def hello_world_wf(ctx: DaprWorkflowContext, wf_input):

    print(f'{wf_input}')

    yield ctx.call_activity(hello_act, input=1)

    yield ctx.call_activity(hello_act, input=10)

    yield ctx.call_activity(hello_retryable_act, retry_policy=retry_policy)

    yield ctx.call_child_workflow(child_retryable_wf, retry_policy=retry_policy)



    # Change in event handling: Use when_any to handle both event and timeout

    event = ctx.wait_for_external_event(event_name)

    timeout = ctx.create_timer(timedelta(seconds=30))

    winner = yield when_any([event, timeout])



    if winner == timeout:

        print('Workflow timed out waiting for event')

        return 'Timeout'



    yield ctx.call_activity(hello_act, input=100)

    yield ctx.call_activity(hello_act, input=1000)

    return 'Completed'





@wfr.activity(name='hello_act')

def hello_act(ctx: WorkflowActivityContext, wf_input):

    global counter

    counter += wf_input

    print(f'New counter value is: {counter}!', flush=True)





@wfr.activity(name='hello_retryable_act')

def hello_retryable_act(ctx: WorkflowActivityContext):

    global retry_count

    if (retry_count % 2) == 0:

        print(f'Retry count value is: {retry_count}!', flush=True)

        retry_count += 1

        raise ValueError('Retryable Error')

    print(f'Retry count value is: {retry_count}! This print statement verifies retry', flush=True)

    retry_count += 1





@wfr.workflow(name='child_retryable_wf')

def child_retryable_wf(ctx: DaprWorkflowContext):

    global child_orchestrator_string, child_orchestrator_count

    if not ctx.is_replaying:

        child_orchestrator_count += 1

        print(f'Appending {child_orchestrator_count} to child_orchestrator_string!', flush=True)

        child_orchestrator_string += str(child_orchestrator_count)

    yield ctx.call_activity(

        act_for_child_wf, input=child_orchestrator_count, retry_policy=retry_policy

    )

    if child_orchestrator_count < 3:

        raise ValueError('Retryable Error')





@wfr.activity(name='act_for_child_wf')

def act_for_child_wf(ctx: WorkflowActivityContext, inp):

    global child_orchestrator_string, child_act_retry_count

    inp_char = chr(96 + inp)

    print(f'Appending {inp_char} to child_orchestrator_string!', flush=True)

    child_orchestrator_string += inp_char

    if child_act_retry_count % 2 == 0:

        child_act_retry_count += 1

        raise ValueError('Retryable Error')

    child_act_retry_count += 1





def main():

    wfr.start()

    wf_client = DaprWorkflowClient()



    print('==========Start Counter Increase as per Input:==========')

    wf_client.schedule_new_workflow(

        workflow=hello_world_wf, input=input_data, instance_id=instance_id

    )



    wf_client.wait_for_workflow_start(instance_id)



    # Sleep to let the workflow run initial activities

    sleep(12)



    assert counter == 11

    assert retry_count == 2

    assert child_orchestrator_string == '1aa2bb3cc'



    # Pause Test

    wf_client.pause_workflow(instance_id=instance_id)

    metadata = wf_client.get_workflow_state(instance_id=instance_id)

    print(f'Get response from {workflow_name} after pause call: {metadata.runtime_status.name}')



    # Resume Test

    wf_client.resume_workflow(instance_id=instance_id)

    metadata = wf_client.get_workflow_state(instance_id=instance_id)

    print(f'Get response from {workflow_name} after resume call: {metadata.runtime_status.name}')



    sleep(2)  # Give the workflow time to reach the event wait state

    wf_client.raise_workflow_event(instance_id=instance_id, event_name=event_name, data=event_data)



    print('========= Waiting for Workflow completion', flush=True)

    try:

        state = wf_client.wait_for_workflow_completion(instance_id, timeout_in_seconds=30)

        if state.runtime_status.name == 'COMPLETED':

            print('Workflow completed! Result: {}'.format(state.serialized_output.strip('"')))

        else:

            print(f'Workflow failed! Status: {state.runtime_status.name}')

    except TimeoutError:

        print('*** Workflow timed out!')



    wf_client.purge_workflow(instance_id=instance_id)

    try:

        wf_client.get_workflow_state(instance_id=instance_id)

    except DaprInternalError as err:

        if non_existent_id_error in err._message:

            print('Instance Successfully Purged')



    sleep(10000)

    wfr.shutdown()





if __name__ == '__main__':

    main()

Important
Because of how replay-based workflows execute, you’ll write logic that does things like I/O and interacting with systems inside activities. Meanwhile, the workflow method is just for orchestrating those activities.
Run the workflow & inspect the workflow execution with the Diagrid Dashboard

Start the workflow application via your IDE or the Dapr CLI (Dapr multi-app run if you want to start multiple applications, or regular Dapr run command for one application, and schedule a new workflow instance.

Use the local Diagrid Dashboard to visualize and inspect your workflow state, and drill down to see detailed workflow execution history. The dashboard runs as a container and is connected to the state store that is used by Dapr workflows (by default a local Redis instance).




Start the Diagrid Dashboard container using Docker:

docker run -p 8080:8080 ghcr.io/diagridio/diagrid-dashboard:latest

Note
If you’re using another state store than the default Redis instance, you need to provide some additional arguments to run the container, see the Diagrid Dashboard reference docs.

Open the dashboard in a browser at http://localhost:8080.

Testing the workflow via the Dapr CLI

After authoring the workflow, you can test it using the Dapr CLI:

Python
Javascript
.NET
Java
Go
Run the workflow application
dapr run --app-id workflow-app python3 app.py


Make sure the application is running:

dapr list

Run the workflow
dapr workflow run hello_world_wf --app-id workflow-app --input 'hello world' --instance-id test-run

Check the workflow status
dapr workflow list --app-id workflow-app -o wide

Check completed workflows
dapr workflow list --app-id workflow-app --filter-status COMPLETED -o wide

View workflow history
dapr workflow history --app-id workflow-app test-run

Monitor Workflow Execution
dapr workflow list --app-id workflow-app --filter-status RUNNING -o wide

dapr workflow list --app-id workflow-app --filter-status FAILED -o wide

dapr workflow list --app-id workflow-app --filter-status COMPLETED -o wide

Test External Events
# Raise an event your workflow is waiting for

dapr workflow raise-event <instance-id>/ApprovalReceived \

  --app-id workflow-app \

  --input '{"approved": true, "approver": "manager@company.com"}'

Debug Failed Workflows
# List failed workflows

dapr workflow list --app-id workflow-app --filter-status FAILED --output wide



# Get detailed history of a failed workflow

dapr workflow history <failed-instance-id> --app-id workflow-app --output json



# Re-run the workflow after fixing issues

dapr workflow rerun <failed-instance-id> --app-id workflow-app --input '<new-input-json-data>'

Next steps

Now that you’ve authored a workflow, learn how to manage it.

Manage workflows >>
Related links
Workflow overview
Try out the full SDK examples:
Python example
JavaScript example
.NET example
Java example
Go example
7 - How to: Manage workflows
Manage and run workflows

Now that you’ve authored the workflow and its activities in your application, you can start, terminate, rerun, and get information about the workflow using the CLI or API calls.

CLI
Python
JavaScript
.NET
Java
Go
HTTP
Managing Workflows with the Dapr CLI

The Dapr CLI provides commands for managing workflow instances in both self-hosted and Kubernetes environments.

See also Workflow Retention Policy for information on how to configure retention policies for completed workflows.

Basic Workflow Operations
Start a Workflow
# Using the `orderprocessing` application, start a new workflow instance with input data

dapr workflow run OrderProcessingWorkflow \

  --app-id orderprocessing \

  --input '{"orderId": "12345", "amount": 100.50}'



# Start with a new workflow with a specific instance ID

dapr workflow run OrderProcessingWorkflow \

  --app-id orderprocessing \

  --instance-id order-12345 \

  --input '{"orderId": "12345"}'



# Schedule a new workflow to start at 10:00:00 AM on December 25, 2024, Coordinated Universal Time (UTC).

dapr workflow run OrderProcessingWorkflow \

  --app-id orderprocessing \

  --start-time "2024-12-25T10:00:00Z"

List Workflow Instances
# List all workflows for an app

dapr workflow list



# Filter by status

dapr workflow list --filter-status RUNNING



# Filter by workflow name and app ID

dapr workflow list --app-id orderprocessing --filter-name OrderProcessingWorkflow



# Filter by age (workflows started in last 24 hours)

dapr workflow list --filter-max-age 24h



# Get detailed output

dapr workflow list -o wide

View Workflow History
# Get execution history

dapr workflow history order-12345



# Get history in JSON format on a particular app ID.

dapr workflow history order-12345 --app-id orderprocessing --output json

Control Workflow Execution
# Suspend a running workflow

dapr workflow suspend order-12345 \

  --app-id orderprocessing \

  --reason "Waiting for manual approval"



# Resume a suspended workflow

dapr workflow resume order-12345 \

  --app-id orderprocessing \

  --reason "Approved by manager"



# Terminate a workflow

dapr workflow terminate order-12345 \

  --app-id orderprocessing \

  --output '{"reason": "Cancelled by customer"}'

Raise External Events
# Raise an event for a waiting workflow

dapr workflow raise-event order-12345/PaymentReceived \

  --app-id orderprocessing \

  --input '{"paymentId": "pay-67890", "amount": 100.50}'

Re-run Workflows
# Re-run from the beginning

dapr workflow rerun order-12345



# Re-run from a specific event ID, discovered via the history command

dapr workflow rerun order-12345 --event-id 5



# Re-run with a new specified instance ID

dapr workflow rerun order-12345 --new-instance-id order-12345-retry

Purge Completed Workflows

Note that purging a workflow from the CLI will also delete all associated Scheduler reminders.

Important
<p>It is required that a workflow client is running in the application to perform purge operations.</p>


The workflow client connection is required in order to preserve the workflow state machine integrity and prevent corruption. Errors like the following suggest that the workflow client is not running:

failed to purge orchestration state: rpc error: code = FailedPrecondition desc = failed to purge orchestration state: failed to lookup actor: api error: code = FailedPrecondition desc = did not find address for actor


It is possible to purge a workflow without a workflow application running by using the --force flag; however, this should only be used when you are certain that no workflow instances are currently running, as it will otherwise corrupt the workflow state machine.

# Purge a specific instance

dapr workflow purge order-12345



# Purge all completed workflows older than 30 days

dapr workflow purge --all-older-than 720h



# Purge all terminal workflows (use with caution!)

dapr workflow purge --app-id orderprocessing --all



# Force a purge without a running workflow client (use with extreme caution!)

dapr workflow purge order-12345 --force

Kubernetes Operations

All commands support the -k flag for Kubernetes deployments:

# List workflows in Kubernetes

dapr workflow list \

  --kubernetes \

  --namespace production \

  --app-id orderprocessing



# Suspend a workflow in Kubernetes

dapr workflow suspend order-12345 \

  --kubernetes \

  --namespace production \

  --app-id orderprocessing \

  --reason "Maintenance window"

Listing Workflows

In self-hosted mode, simply run:

dapr workflow list


In Kubernetes mode, specify the --kubernetes/-k flag along with the namespace and app ID:

dapr workflow list -k

Workflow Management Best Practices

Monitor Running Workflows: Use filtered lists to track long-running instances

dapr workflow list --app-id orderprocessing --filter-status RUNNING --filter-max-age 24h


Use Instance IDs: Assign meaningful instance IDs for easier tracking

dapr workflow run OrderWorkflow --app-id orderprocessing --instance-id "order-$(date +%s)"


Export for Analysis: Export workflow data for analysis

dapr workflow list --app-id orderprocessing --output json > workflows.json

Managing Workflow Reminders with the Dapr CLI

Workflow reminders are stored in the Scheduler and can be managed using the dapr scheduler CLI.

List workflow reminders
dapr scheduler list --filter workflow

NAME                                           BEGIN     COUNT  LAST TRIGGER

workflow/my-app/instance1/timer-0-ABC123       +50.0h    0

workflow/my-app/instance2/timer-0-XYZ789       +50.0h    0


Get reminder details

dapr scheduler get workflow/my-app/instance1/timer-0-ABC123 -o yaml

Delete workflow reminders

Delete a single reminder:

dapr scheduler delete workflow/my-app/instance1/timer-0-ABC123


Delete all reminders for a given workflow app"

dapr scheduler delete-all workflow/my-app


Delete all reminders for a specific workflow instance:

dapr scheduler delete-all workflow/my-app/instance1

Backup and restore reminders

Export all reminders:

dapr scheduler export -o workflow-reminders-backup.bin


Restore from a backup file:

dapr scheduler import -f workflow-reminders-backup.bin

Next steps

Now that you’ve learned how to manage workflows, learn how to execute workflows across multiple applications

Multi Application Workflows>>
Related links
Try out the Workflow quickstart
Try out the full SDK examples:
Python example
JavaScript example
.NET example
Java example
Go example
8 - Multi Application Workflows
Executing workflows across multiple applications

It is often the case that a single workflow spans multiple applications, microservices, or programming languages. This is where an activity or a child workflow will be executed on a different application than the one hosting the parent workflow.

Some scenarios where this is useful include:

A Machine Learning (ML) training activity must be executed on GPU-enabled machines, while the rest of the workflow runs on CPU-only orchestration machines.
Activities need access to sensitive data or credentials that are only available to particular identities or locales.
Different parts of the workflow need to be executed in different trust zones or networks.
Different parts of the workflow need to be executed in different geographic regions due to data residency requirements.
An involved business process spans multiple teams or departments, each owning their own application.
Implementation of a workflow spans different programming languages based on team expertise or existing codebases.
Different team boundaries or microservice ownership.

The diagram below shows an example scenario of a complex workflow that orchestrates across multiple applications that are written in different languages. Each applications’ main steps and activities are:

• App1: Main Workflow Service - Top-level orchestrator that coordinates the entire ML pipeline

Starts the process
Calls data processing activities on App2
Calls ML training child workflow on App3
Calls model deployment on App4
Ends the complete workflow
Language: Java

• App2: Data Processing Pipeline - GPU activities only

Data Ingesting Activity (GPU-accelerated)
Feature Engineering Activity (GPU-accelerated)
Returns completion signal to Main Workflow
Language: Go

• App3: ML Training Child Workflow - Contains a child workflow and activities

Child workflow orchestrates:
Data Processing Activity
Model Training Activity (GPU-intensive)
Model Validation Activity
Triggered by App2’s activities completing
Returns completion signal to Main Workflow
Language: Java

• App4: Model Serving Service - Beefy GPU app with activities only

Model Loading Activity (GPU memory intensive)
Inference Setup Activity (GPU-accelerated inference)
Triggered by App3’s workflow completing
Returns completion signal to Main Workflow
Language: Go
Multi-application workflows

Workflow execution routing is based on the App ID of the hosting Dapr application. By default, the full workflow execution is hosted on the app ID that started the workflow. This workflow can be executed across any replicas of that app ID, not just the single replica which scheduled the workflow.

It is possible to execute activities and child workflows on different app IDs by specifying the target app ID parameter, inside the workflow execution code. Upon execution, the target app ID executes the activity or child workflow, and returns the result to the parent workflow of the originating app ID.

The entire Workflow execution may be distributed across multiple app IDs with no limit, with each activity or child workflow specifying the target app ID. The final history of the workflow will be saved by the app ID that hosts the very parent (or can consider it the root) workflow.

Restrictions
Like other API building blocks and resources in Dapr, workflows are scoped to a single namespace. This means that all app IDs involved in a multi-application workflow must be in the same namespace. Similarly, all app IDs must use the same workflow (or actor) state store. Finally, the target app ID must have the activity or child workflow defined and registered, otherwise the parent workflow retries indefinitely.
Note
Multi-application workflows require Dapr runtime v1.16.0 or later. .NET SDK support is available starting with v1.17.0.
Important Limitations

SDKs supporting multi-application workflows - Multi-application workflows are used via the SDKs. Currently the following are supported:

Java (only activity calls)
Go (both activity and child workflow calls)
Python (both activity and child workflow calls)
.NET (both activity and child workflow calls, requires .NET SDK v1.17.0+)
JavaScript SDK support is planned for a future release
Error handling

When calling multi-application activities or child workflows:

If the target application does not exist, the call will be retried using the provided retry policy.
If the target application exists but doesn’t contain the specified activity or workflow, the call will return an error.
Standard workflow retry policies apply to multi-application calls.

It is paramount that there is coordination between the teams owning the different app IDs to ensure that the activities and child workflows are defined and available when needed.

Durable Activity Results

It is often the case that Activities take some amount of time to complete, or similarly are expensive to execute in resource or dollar cost. It is therefore undesirable to execute these activities more than once for the same round, even in unhappy paths. Before 1.17 in multi-application scenarios, Activities would publish responses over a network call to the other application which is hosting the owning Workflow. In the case where the hosting workflow application is down or otherwise unreachable, the result would be lost and the Activity would be retried, leading to duplicate execution of the Activity.

In 1.17, enabling the `WorkflowsRemoteActivityReminder feature gate will make the activity result be sent to the owning workflow application with a reminder in the event that the workflow application is offline or unreachable, ensuring that the result is not lost and duplicate execution is avoided. This option should be enabled by all users who are using Dapr version 1.17 on all applications. It has been disabled by default for backwards compatibility between Dapr versions, but will be enabled by default in a future release.

Multi-application activity example

The following example shows how to execute the activity ActivityA on the target app App2.

Go
Java
Python
.NET
func BusinessWorkflow(ctx *workflow.WorkflowContext) (any, error) {

	var output string

	err := ctx.CallActivity("ActivityA",

		workflow.WithActivityInput("my-input"),

		workflow.WithActivityAppID("App2"), // Here we set the target app ID which will execute this activity.

	).Await(&output)



	if err != nil {

		return nil, err

	}



	return output, nil

}

Multi-application child workflow example

The following example shows how to execute the child workflow Workflow2 on the target app App2.

Go
Python
.NET
func BusinessWorkflow(ctx *workflow.WorkflowContext) (any, error) {

	var output string

	err := ctx.CallChildWorkflow("Workflow2",

		workflow.WithChildWorkflowInput("my-input"),

		workflow.WithChildWorkflowAppID("App2"), // Here we set the target app ID which will execute this child workflow.

	).Await(&output)



	if err != nil {

		return nil, err

	}



	return output, nil

}

Related links
Try out Dapr Workflows using the quickstart
Workflow overview
Workflow API reference
Multi-application workflows in .NET
Try out the following examples:
Python
JavaScript
.NET
Java
Go
9 - History Retention Policy
Define retention policy to manage workflow state history state

Dapr workflow state is stored in the [actor state store]{{ %ref workflow-architecture.md#state-store-usage %}}. By default, Dapr Workflows retains the complete history of workflow state changes indefinitely. This means historical workflows can be queried and inspected at any time. Running many workflows or workflows which generate large amounts of state change history can lead to increased storage usage, which can eventually fill up the state store disk space.

To help manage storage usage, Dapr Workflows supports configuring a history retention policy. The retention policy defines how long to retain workflow state change history before it is deleted. Workflows will only be eligible for deletion once it has reached a terminal state (Completed, Failed, or Terminated). Each workflow terminal state can have a custom retention duration, as well as a default retention duration for any terminal states not explicitly configured. The duration is defined as a Go duration string (for example, 72h for 72 hours, or 30m for 30 minutes).

Note
It can be useful to configure a short retention duration for Completed workflows, while retaining Failed and Terminated workflows for longer periods to allow for investigation.

The following example configuration sets each of the terminal states. The anyTerminal property set here would take no effect as all terminal states are explicitly configured, however it is included for reference.

See the Dapr Configuration documentation for more information on how to apply configuration to your Dapr applications.

kind: Configuration
metadata:
  name: appconfig
spec:
  workflow:
    stateRetentionPolicy:
      anyTerminal: "360h"
      completed: "1m"
      failed: "720h"
      terminated: "360h"

Related links
Try out Dapr Workflows using the quickstart
Workflow overview
Workflow API reference
Try out the following examples:
Python
JavaScript
.NET
Java
Go
10 - Workflow Execution Concurrency
Configure concurrency for Dapr Workflows to rate limit workflow and activity executions.

You can configure the maximum concurrent workflows and activities that can be executed at any one time with the following configuration. These limits are imposed on a per sidecar basis, meaning that if you have 10 replicas of your workflow app, the effective limit is 10 times the configured value.

Setting these limits can help prevent resource exhaustion on your Dapr sidecar and application, or to drain down a backlog of workflows if there had been a spike in activity causing resource contention. These limits do not distinguish between different workflow or activity definitions, so they apply to all workflows and activities running in the sidecar.

See the Dapr Configuration documentation for more information on how to apply configuration to your Dapr applications.

apiVersion: dapr.io/v1alpha1

kind: Configuration

metadata:

  name: appconfig

spec:

  workflow:

    maxConcurrentWorkflowInvocations: 100 # Default is infinite

    maxConcurrentActivityInvocations: 1000 # Default is infinite

Related links
Try out Dapr Workflows using the quickstart
Workflow overview
Workflow API reference
Try out the following examples:
Python
JavaScript
.NET
Java
Go
© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our Trademark Usage page.
