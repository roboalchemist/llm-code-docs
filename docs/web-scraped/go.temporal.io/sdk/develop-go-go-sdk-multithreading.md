# Source: https://docs.temporal.io/develop/go/go-sdk-multithreading

Title: Temporal Go SDK multithreading | Temporal Platform Documentation

URL Source: https://docs.temporal.io/develop/go/go-sdk-multithreading

Published Time: Sun, 01 Mar 2026 18:05:43 GMT

Markdown Content:
Temporal Go SDK multithreading | Temporal Platform Documentation
===============

[Skip to main content](https://docs.temporal.io/develop/go/go-sdk-multithreading#__docusaurus_skipToContent_fallback)

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
*   Multithreading

On this page

Temporal Go SDK multithreading
==============================

Copy for LLM View as Markdown

The Temporal Go SDK allows you to create additional goroutines (threads) in your Workflows by calling `workflow.Go()`. Native Go threading is never allowed in Workflow code, as it would create determinism errors.

You might sometimes need to execute multiple Activities or Child Workflows in parallel and then await the result of all of them. Normally, this would require a lock or [mutex](https://en.wikipedia.org/wiki/Lock_(computer_science)) around some shared data structure to avoid race conditions that could occur when multiple asynchronous operations try to modify the data structure.

Although Temporal Workflows run Asynchronously in Go, there is a control in place that ensures only one thread can access at the time.

How multithreading works[​](https://docs.temporal.io/develop/go/go-sdk-multithreading#how-multithreading-works "Direct link to How multithreading works")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Temporal's Go SDKs contains a deterministic runner to control the thread execution. This deterministic runner will decide which Workflow thread to run in the right order, and one at a time. Each task will execute in a loop until all threads are blocked.

`workflow.Go()` creates a new thread and adds it to this runner. This significantly minimizes the likelihood of race conditions, and eliminates the need to use a mutex.

For a complex example, refer to the [Go Particle Swarm Operation Sample](https://github.com/temporalio/samples-go/tree/main/pso).

For an example using Signals, refer to the [Go Await Signal Sample](https://github.com/temporalio/samples-go/tree/main/await-signals)

Static analysis with the workflowcheck tool[​](https://docs.temporal.io/develop/go/go-sdk-multithreading#static-analysis-with-the-workflowcheck-tool "Direct link to Static analysis with the workflowcheck tool")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Temporal Go SDK also provides a command line tool called [`workflowcheck`](https://github.com/temporalio/sdk-go/blob/master/contrib/tools/workflowcheck/README.md) to statically analyze Workflow Definitions. This can help eliminate potential instances of non-determinism.

**Tags:**
*   [Temporal SDKs](https://docs.temporal.io/tags/temporal-sd-ks)
*   [Go SDK](https://docs.temporal.io/tags/go-sdk)
*   [Concepts](https://docs.temporal.io/tags/concepts)

Help us make Temporal better. Contribute to our [documentation](https://github.com/temporalio/documentation).

[Previous Temporal Client](https://docs.temporal.io/develop/go/temporal-client)[Next Namespaces](https://docs.temporal.io/develop/go/namespaces)

*   [How multithreading works](https://docs.temporal.io/develop/go/go-sdk-multithreading#how-multithreading-works)
*   [Static analysis with the workflowcheck tool](https://docs.temporal.io/develop/go/go-sdk-multithreading#static-analysis-with-the-workflowcheck-tool)

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
