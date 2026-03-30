# Source: https://docs.temporal.io/develop/go/asynchronous-activity-completion

Title: Asynchronous Activity completion - Go SDK | Temporal Platform Documentation

URL Source: https://docs.temporal.io/develop/go/asynchronous-activity-completion

Published Time: Sat, 28 Feb 2026 15:41:16 GMT

Markdown Content:
Asynchronous Activity completion - Go SDK | Temporal Platform Documentation
===============

[Skip to main content](https://docs.temporal.io/develop/go/asynchronous-activity-completion#__docusaurus_skipToContent_fallback)

[![Image 1: Temporal logo](https://docs.temporal.io/img/assets/temporal-logo-dark.svg)](https://temporal.io/)[Home](https://docs.temporal.io/)[Courses](https://learn.temporal.io/getting_started/)[SDKs](https://docs.temporal.io/develop)[AI Cookbook](https://docs.temporal.io/ai-cookbook)[Code Exchange](https://temporal.io/code-exchange)[Temporal Cloud](https://docs.temporal.io/cloud)

Ask AI

Search

*   [Home](https://docs.temporal.io/)
*   [Quickstarts](https://docs.temporal.io/quickstarts)
*   [Evaluate](https://docs.temporal.io/evaluate/) 
*   [Develop](https://docs.temporal.io/develop/) 
    *   [Go SDK](https://docs.temporal.io/develop/go/) 
        *   [Quickstart](https://docs.temporal.io/develop/go/set-up-your-local-go)
        *   [Core application](https://docs.temporal.io/develop/go/core-application)
        *   [Temporal Client](https://docs.temporal.io/develop/go/temporal-client)
        *   [Multithreading](https://docs.temporal.io/develop/go/go-sdk-multithreading)
        *   [Namespaces](https://docs.temporal.io/develop/go/namespaces)
        *   [Testing](https://docs.temporal.io/develop/go/testing-suite)
        *   [Failure detection](https://docs.temporal.io/develop/go/failure-detection)
        *   [Messages](https://docs.temporal.io/develop/go/message-passing)
        *   [Interrupt a Workflow Execution](https://docs.temporal.io/develop/go/cancellation)
        *   [Asynchronous Activity Completion](https://docs.temporal.io/develop/go/asynchronous-activity-completion)
        *   [Versioning](https://docs.temporal.io/develop/go/versioning)
        *   [Observability](https://docs.temporal.io/develop/go/observability)
        *   [Benign exceptions](https://docs.temporal.io/develop/go/benign-exceptions)
        *   [Enriching the UI](https://docs.temporal.io/develop/go/enriching-ui)
        *   [Debugging](https://docs.temporal.io/develop/go/debugging)
        *   [Schedules](https://docs.temporal.io/develop/go/schedules)
        *   [Converters and encryption](https://docs.temporal.io/develop/go/converters-and-encryption)
        *   [Durable Timers](https://docs.temporal.io/develop/go/timers)
        *   [Temporal Nexus](https://docs.temporal.io/develop/go/nexus)
        *   [Child Workflows](https://docs.temporal.io/develop/go/child-workflows)
        *   [Continue-As-New](https://docs.temporal.io/develop/go/continue-as-new)
        *   [Side Effects](https://docs.temporal.io/develop/go/side-effects)
        *   [Selectors](https://docs.temporal.io/develop/go/selectors)
        *   [Sessions](https://docs.temporal.io/develop/go/sessions)

    *   [Java SDK](https://docs.temporal.io/develop/java/) 
    *   [PHP SDK](https://docs.temporal.io/develop/php/) 
    *   [Python SDK](https://docs.temporal.io/develop/python/) 
    *   [TypeScript SDK](https://docs.temporal.io/develop/typescript/) 
    *   [.NET SDK](https://docs.temporal.io/develop/dotnet/) 
    *   [Ruby SDK](https://docs.temporal.io/develop/ruby/) 
    *   [Environment configuration](https://docs.temporal.io/develop/environment-configuration)
    *   [Activity retry simulator](https://docs.temporal.io/develop/activity-retry-simulator)
    *   [Worker performance](https://docs.temporal.io/develop/worker-performance)
    *   [Safe deployments](https://docs.temporal.io/develop/safe-deployments)
    *   [Plugins guide](https://docs.temporal.io/develop/plugins-guide)

*   [Temporal Cloud](https://docs.temporal.io/cloud) 
*   [Deploy to production](https://docs.temporal.io/production-deployment) 
*   [CLI (temporal)](https://docs.temporal.io/cli) 
*   [References](https://docs.temporal.io/references/) 
*   [Troubleshooting](https://docs.temporal.io/troubleshooting/) 
*   [Best practices](https://docs.temporal.io/best-practices/) 
*   [Encyclopedia](https://docs.temporal.io/encyclopedia/) 
*   [Glossary](https://docs.temporal.io/glossary)
*   [Use with AI](https://docs.temporal.io/with-ai)

*   [](https://docs.temporal.io/)
*   [Develop](https://docs.temporal.io/develop/)
*   [Go SDK](https://docs.temporal.io/develop/go/)
*   Asynchronous Activity Completion

Asynchronous Activity completion - Go SDK
=========================================

Copy for LLM View as Markdown

[Asynchronous Activity Completion](https://docs.temporal.io/activity-execution#asynchronous-activity-completion) enables the Activity Function to return without the Activity Execution completing.

There are three steps to follow:

1.   The Activity provides the external system with identifying information needed to complete the Activity Execution. Identifying information can be a [Task Token](https://docs.temporal.io/activity-execution#task-token), or a combination of Namespace, Workflow Id, and Activity Id.

2.   The Activity Function completes in a way that identifies it as waiting to be completed by an external system.

3.   The Temporal Client is used to Heartbeat and complete the Activity.

4.   Provide the external system with a Task Token to complete the Activity Execution. To do this, use the `GetInfo()` API from the `go.temporal.io/sdk/activity` package.

`// Retrieve the Activity information needed to asynchronously complete the Activity.activityInfo := activity.GetInfo(ctx)taskToken := activityInfo.TaskToken// Send the taskToken to the external service that will complete the Activity.`

1.   Return an `activity.ErrResultPending` error to indicate that the Activity is completing asynchronously.

`return "", activity.ErrResultPending`

1.   Use the Temporal Client to complete the Activity using the Task Token.

`// Instantiate a Temporal service client.// The same client can be used to complete or fail any number of Activities.// The client is a heavyweight object that should be created once per process.temporalClient, err := client.Dial(client.Options{})// Complete the Activity.temporalClient.CompleteActivity(context.Background(), taskToken, result, nil)`

The following are the parameters of the `CompleteActivity` function:

*   `taskToken`: The value of the binary `TaskToken` field of the `ActivityInfo` struct retrieved inside the Activity.
*   `result`: The return value to record for the Activity. The type of this value must match the type of the return value declared by the Activity function.
*   `err`: The error code to return if the Activity terminates with an error.

If `err` is not null, the value of the `result` field is ignored.

To fail the Activity, you would do the following:

`// Fail the Activity.client.CompleteActivity(context.Background(), taskToken, nil, err)`

**Tags:**
*   [Activities](https://docs.temporal.io/tags/activities)
*   [Go SDK](https://docs.temporal.io/tags/go-sdk)
*   [Temporal SDKs](https://docs.temporal.io/tags/temporal-sd-ks)

Help us make Temporal better. Contribute to our [documentation](https://github.com/temporalio/documentation).

[Previous Interrupt a Workflow Execution](https://docs.temporal.io/develop/go/cancellation)[Next Versioning](https://docs.temporal.io/develop/go/versioning)

*   [GitHub](https://github.com/temporalio)
*   [Twitter](https://twitter.com/temporalio)
*   [YouTube](https://www.youtube.com/c/Temporalio)
*   [About the docs](https://github.com/temporalio/documentation/blob/master/README.md)

*   [Temporal Cloud](https://temporal.io/cloud)
*   [Meetups](https://temporal.io/community#events)
*   [Workshops](https://temporal.io/community#workshops)
*   [Support forum](https://community.temporal.io/)
*   [Ask an expert](https://pages.temporal.io/ask-an-expert)

*   [Learn Temporal](https://learn.temporal.io/)
*   [Blog](https://temporal.io/blog)
*   [Use cases](https://temporal.io/use-cases)
*   [Newsletter signup](https://pages.temporal.io/newsletter-subscribe)

*   [Security](https://docs.temporal.io/security)
*   [Privacy policy](https://temporal.io/global-privacy-policy)
*   [Terms of service](https://docs.temporal.io/pdf/temporal-tos-2021-07-24.pdf)
*   [We're hiring](https://temporal.io/careers)

[![Image 2: Temporal logo](https://docs.temporal.io/img/favicon.png)](https://temporal.io/)

Copyright © 2026 Temporal Technologies Inc.

Feedback![Image 3](https://static.scarf.sh/a.png?x-pxid=6fb132d3-92f6-455f-bf17-eb3d6937bdea)
