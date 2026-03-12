# Source: https://pipedream.com/docs/glossary.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pipedream Glossary

Below you’ll find a glossary of Pipedream-specific terms. We use these in the product, docs, and other content, so if you’re seeing a term for the first time, you’ll probably find it below.

All terms that aren’t in this doc hold their standard technical meaning. If you see a term missing, please [reach out](https://pipedream.com/support).

[0-9](/glossary/#0---9) | [A](/glossary/#a) | [B](/glossary/#b) | [C](/glossary/#c) | [D](/glossary/#d) | [E](/glossary/#e) | [F](/glossary/#f) | [G](/glossary/#g) | [H](/glossary/#h) | [I](/glossary/#i) | [J](/glossary/#j) | [K](/glossary/#k) | [L](/glossary/#l) | [M](/glossary/#m) | [N](/glossary/#n) | [O](/glossary/#o) | [P](/glossary/#p) | [Q](/glossary/#q) | [R](/glossary/#r) | [S](/glossary/#s) | [T](/glossary/#t) | [U](/glossary/#u) | [V](/glossary/#v) | [W-Z](/glossary/#w-z)

## 0 - 9

### 2FA

Short for [two-factor authentication](/glossary/#two-factor-authentication-2fa).

## A

### Account

Synonym for [connected account](/glossary/#connected-account).

### Action

Actions are reusable code steps, written as [Pipedream components](/glossary/#component).

### Advanced plan

Pipedream’s plan for individuals and teams running production workflows. [See the pricing page](https://pipedream.com/pricing) for more details.

### Auto-retry

[A workflow setting](/workflows/building-workflows/settings/#auto-retry-errors) that lets you automatically retry an execution from the failed step when it encounters an error.

## B

### Bash runtime

Pipedream’s internal code in the [execution environment](/glossary/#execution-environment) responsible for running Bash code.

### Basic plan

Pipedream’s plan for individuals who need higher limits and the option to scale usage. [See the pricing page](https://pipedream.com/pricing) for more details.

### Bi-directional GitHub sync

When you configure [GitHub Sync](/glossary/#github-sync), you can make changes in Pipedream and push them to GitHub, or make changes locally, push to GitHub, and deploy to Pipedream. Since changes can be made in each system and communicated to the other, the sync is bi-directional.

### Branch

Short for [Git branch](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell). When using [Pipedream GitHub Sync](/glossary/#github-sync), you can sync a GitHub repository to a Pipedream project and manage changes to code in a branch.

### Builder

The Pipedream UI where you build, edit, and test workflows.

### Business plan

Pipedream’s plan for teams with security, compliance, and support needs. [See the pricing page](https://pipedream.com/pricing) for more details.

## C

### Changelog

Synonym for [project changelog](/glossary/#project-changelog).

### Code step

[Steps](/glossary/#step) that let users run [custom code](/workflows/building-workflows/code/) in a workflow.

### Cold start

A cold start refers to the delay between the invocation of workflow and the execution of the workflow code. Cold starts happen when Pipedream spins up a new [execution environment](/glossary/#execution-environment) to handle incoming events.

### Commit

Short for [Git commit](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository). When using [Pipedream GitHub Sync](/glossary/#github-sync), you commit changes to a branch before deploying the workflow to production.

### Component

Components are Node.js modules that run on Pipedream’s serverless infrastructure. [Sources](/glossary/#source) and [actions](/glossary/#action) are two types of components. See [the component API](/components/contributing/api/) for more details.

### Component API

The programming interface for creating [components](/glossary/#component) in Pipedream.

### Component guidelines

Guidelines applied to components submitted to [the Pipedream component registry](/glossary/#component-registry).

### Component registry

The public registry of [components](/glossary/#component) available to Pipedream users, [available on GitHub](https://github.com/PipedreamHQ/pipedream).

### Concurrency

[A workflow setting](/workflows/building-workflows/settings/concurrency-and-throttling/#concurrency) that lets users configure the number of concurrent [workers](/glossary/#worker) available to process events.

### Connected account

A specific account or credentials used to connect to a Pipedream [integration](/glossary/#integrations). If both you and your team member have an account with OpenAI, for example, you would connect each account as a distinct connected account. [See the docs](/apps/connected-accounts/) for more details.

### Connected account access control

You can restrict access to connected accounts to specific individuals or share with the entire workspace. [See the docs](/apps/connected-accounts/#access-control) for more details.

### Credit

Pipedream charges one credit per 30 seconds of compute time at 256MB megabytes of memory (the default) per workflow execution. Credits are also charged for [dedicated workers](/glossary/#dedicated-workers). [See the docs](/pricing/#credits-and-billing) for more details.

### Custom domain

By default, [HTTP endpoints](/glossary/#http-endpoint) are served from the `*.m.pipedream.net` domain. You can configure a [custom domain](/workflows/domains/) if you want to host that endpoint on your own domain.

### Custom source

An [event source](/glossary/#event-source) that you create using custom code, or by modifying a [registry source](/glossary/#registry-source).

## D

### Data retention

A workflow setting that allows you to configure how long Pipedream stores event data and logs associated with [executions](/glossary/#execution). [See the docs](/workflows/building-workflows/settings/#data-retention-controls) for more details.

### Dedicated workers

[Workers](/glossary/#worker) that remain available to process events, even when the workflow is not running. This can help reduce [cold starts](/glossary/#cold-start) and improve performance for workflows that require low latency. [See the docs](/workflows/building-workflows/settings/#eliminate-cold-starts) for more details.

### Deduper

[Event sources](/glossary/#event-source) can receive duplicate requests tied to the same event. Pipedream’s infrastructure supports [deduplication](/components/contributing/api/#dedupe-strategies) to ensure that only unique events are emitted by a source.

### Delay

[A built-in service](/workflows/building-workflows/control-flow/delay/) that lets you pause a workflow for a specified amount of time. You can delay workflows using pre-built actions, or delay in code.

### Destination

[Destinations](/workflows/data-management/destinations/) are built-in services that abstract the delivery and connection logic required to send events to services like Amazon S3, or targets like HTTP and email.

### Domain

Synonym for [custom domain](/glossary/#custom-domain).

### Data store

[Data stores](/workflows/data-management/data-stores/) are Pipedream’s built-in key-value store.

### Deploy key

When you configure [GitHub Sync](/glossary/#github-sync), you can use a deploy key to authenticate Pipedream with your GitHub repository. [See the docs](/workflows/git/#create-a-new-project-and-enable-github-sync) for more details.

## E

### Editor

The built-in code editor in the [builder](/glossary/#builder).

### Email trigger

A [workflow trigger](/glossary/#trigger) that listens for incoming email. This trigger exposes a workflow-specific email address that you can use to send email to the workflow.

### Emit

[Event sources](/glossary/#event-source), [workflow triggers](/glossary/#trigger), and even workflows themselves can emit [events](/glossary/#event) that trigger other [listeners](/glossary/#listener). Since sources have a built-in [deduper](/glossary/#deduper), not all requests are emitted as events.

### Emitter

A resource that [emits](/glossary/#emit) [events](/glossary/#event). Emitters can be [event sources](/glossary/#event-source), [workflow triggers](/glossary/#trigger), or even workflows themselves.

### Error notification

When a workflow execution encounters an error, Pipedream sends an [error notification](/workflows/building-workflows/errors/) to the configured error [listeners](/glossary/#listener).

### Environment variable

Pipedream supports two types of environment variables:

* [Project variables](/glossary/#project-variable), available within a specific project
* [Workspace variables](/glossary/#workspace-variable), available across all projects in a workspace

### Event

Events are emitted by [sources](/glossary/#event-source) and consumed by workflows. Events can be triggered by a variety of sources, including HTTP requests, cron schedules, and third-party APIs. Events can be passed to actions, which can process the event data and perform a variety of operations, including making HTTP requests, sending emails, and interacting with third-party APIs.

### Event context

Metadata about a workflow execution, including the timestamp of the event, the event ID, and more. Exposed in [`steps.trigger.context`](/workflows/building-workflows/triggers/#stepstriggercontext).

### Event data

The content of the event, exposed in [`steps.trigger.event`](/workflows/building-workflows/triggers/).

### Event history

A log of all workflow events and executions, available in the [event inspector](/glossary/#inspector) or the global [event history UI](/workflows/event-history/).

### Event queue

When using built-in [concurrency](/glossary/#concurrency) or [throttling](/glossary/#throttling) controls, events are queued in a workflow-specific queue and processed by available [workers](/glossary/#worker).

### Event source

[Components](/glossary/#component) that watch for events from a third-party data source, emitting those events to [listeners](/glossary/#listener).

### Execution

When a workflow is triggered by an event, the running instance of the workflow on that event is called an execution.

### Execution environment

[The virtual machine](/privacy-and-security/#execution-environment) and internal Pipedream platform code that runs a workflow execution. An instance of an execution environment is called a [worker](/glossary/#worker).

### Execution rate controls

The workflow setting that allows users to configure the number of executions a workflow can process per unit time. Also known as throttling. [See the docs](/workflows/building-workflows/settings/concurrency-and-throttling/#throttling) for more details.

### Export

Depending on the context, **export** can function as a noun or verb:

* **Noun**: A synonym for [step export](/glossary/#step-export)
* **Verb**: The act of exporting data from a step using Pipedream primitives like [`$.export`](/workflows/building-workflows/code/nodejs/#using-export) or `return`.

### Expression

In programming, expressions are code that resolve to a value. In Pipedream, [you can use expressions within props forms](/workflows/building-workflows/using-props/#entering-expressions) to reference prior steps or compute custom values at runtime.

### External credentials

[Connected accounts](/glossary/#connected-account) are accounts that users link directly in Pipedream. External credentials are credentials that users store in their own database or service, and reference in Pipedream at runtime. [See the docs](/apps/external-auth/) for more details.

## F

### File store

[File stores](/workflows/data-management/file-stores/) are filesystems scoped to projects. Any files stored in the file store are available to all workflows in the project.

### Filter

[Built-in actions](https://pipedream.com/apps/filter) that let you continue or stop a workflow based on a condition.

### Folder

Within projects, you can organize workflows into folders.

### Free plan

Pipedream’s free plan. [See the limits docs](/workflows/limits/) for more details.

## G

### Global search

Press `Ctrl + K` or `Cmd + K` to open the global search bar in the Pipedream UI.

### GitHub Sync

When enabled on a [project](/glossary/#project), GitHub Sync syncs the project’s workflow code with a GitHub repository. [See the docs](/workflows/git/) for more details.

### Golang runtime

Pipedream’s internal code in the [execution environment](/glossary/#execution-environment) responsible for running Go code.

## H

### Helper functions

[Built-in actions](https://pipedream.com/apps/helper-functions) that convert data types, format dates, and more.

### Hooks

[Hooks](/components/contributing/api/#hooks) are functions executed as a part of the [event source](/glossary/#event-source) lifecycle. They can be used to perform setup tasks before the source is deployed, or teardown tasks after the source is destroyed.

### HTTP endpoint

The URL tied to a [workflow HTTP trigger](/glossary/#http-trigger) or HTTP-triggered [event source](/glossary/#event-source).

### HTTP trigger

A [workflow trigger](/glossary/#trigger) that listens for incoming HTTP requests. This trigger exposes a unique URL that you can use to send HTTP requests to the workflow.

## I

### Inspector

The Pipedream UI that displays a specific workflow’s event history. [See the docs](/workflows/building-workflows/inspect/) for more details.

### Integrations

When Pipedream adds a new third-party service to our marketplace of apps, we often have to handle details of the OAuth process and authentication, and build [sources](/glossary/#event-source) and [actions](/glossary/#action) for the API. These details are abstracted from the user, and the app configuration is referred to as an **integration**.

## J

## K

### Key-based account

A [connected account](/glossary/#connected-account) that uses static credentials, like API keys.

## L

### Listener

A resource that listens for events emitted by [emitters](/glossary/#emitter). Listeners can be [workflows](/glossary/#workflow), [event sources](/glossary/#event-source), webhook URLs, and more.

### Logs

Standard output and error logs generated by steps during a workflow execution. Logs are available as a part of the step execution details in the [event inspector](/glossary/#inspector) or the global [event history UI](/workflows/event-history/).

## M

### Merge

When you configure [GitHub Sync](/glossary/#github-sync), you can merge changes from a branch into the production branch of your GitHub repository, deploying those changes to Pipedream.

## N

### Node.js runtime

Pipedream’s internal code in the [execution environment](/glossary/#execution-environment) responsible for running Node.js code.

## O

### Organization

Synonym for [workspaces](/glossary/#workspace).

### OAuth account

A [connected account](/glossary/#connected-account) that uses OAuth to authenticate with a third-party service.

## P

### Premium apps

Pipedream’s built-in [integrations](/glossary/#integrations) that require a paid plan to use. [See the pricing page](https://pipedream.com/pricing) for more details and the [full list of premium apps](/apps/#premium-apps).

### Project

A container for workflows, secrets, and other resources in Pipedream. Projects can be synced with a GitHub repository using [GitHub Sync](/glossary/#github-sync). [See the docs](/projects/) for more details.

### Project-based access control

You can restrict access to projects to specific individuals or share with the entire workspace. [See the docs](/projects/access-controls/) for more details.

### Project changelog

When using [Pipedream GitHub Sync](/glossary/#github-sync), the changelog shows the history of changes made to a project.

### Project file

A file stored in a [file store](/glossary/#file-store).

### Project secret

Users can add both standard project variables and secrets to a project. The values of secrets are encrypted and cannot be read from the UI once added.

### Project settings

Configure GitHub Sync and other project-specific configuration in a project’s settings.

### Project variable

Project-specific environment variables, available to all workflows in a project.

### Props

[Props](/workflows/building-workflows/using-props/) allow you to pass input to [components](/glossary/#component).

### Python runtime

Pipedream’s internal code in the [execution environment](/glossary/#execution-environment) responsible for running Python code.

### Object explorer

The [builder](/glossary/#builder) UI that allows you to search objects [exported](/glossary/#export) from prior steps. [See the docs](/workflows/building-workflows/using-props/#use-the-object-explorer) for more details.

## Q

## R

### Registry

Synonym for [component registry](/glossary/#component-registry).

### Registry source

An [event source](/glossary/#event-source) available in the [component registry](/glossary/#component-registry). Registry sources are reviewed and approved by Pipedream.

## S

### Schedule trigger

A [workflow trigger](/glossary/#trigger) that runs on a schedule. This trigger exposes a cron-like syntax that you can use to schedule the workflow.

### Single sign-on (SSO)

Users can [configure SSO](/workspaces/sso/) to authenticate with Pipedream using their identity provider.

### Source

Synonym for [event source](/glossary/#event-source).

### Step

[Steps](/workflows/#steps) are the building blocks used to create workflows. Steps can be [triggers](/glossary/#trigger), [actions](/glossary/#action), or [code steps](/glossary/#code-step).

### Step export

JSON-serializable data returned from steps, available in future steps of a workflow. [See the docs](/workflows/#step-exports) for more details.

### Step notes

[Step notes](/workflows/#step-notes) are Markdown notes you can add to a step to document its purpose.

### Subscription

A connection between a [listener](/glossary/#listener) and an [emitter](/glossary/#emitter) that allows the listener to receive events from the emitter.

### Suspend

Workflow [executions](/glossary/#execution) are suspended when you [delay](/glossary/#delay) or use functions like [`$.flow.suspend`](/workflows/building-workflows/code/nodejs/rerun/#flowsuspend) to pause the workflow.

## T

### Throttling

Synonym for [execution rate controls](/glossary/#execution-rate-controls).

### Timeout

All workflows have [a default timeout](/workflows/limits/#time-per-execution). You can configure a custom timeout in the [workflow settings](/workflows/building-workflows/settings/#execution-timeout-limit).

### `/tmp` directory

A directory available to the workflow’s [execution environment](/glossary/#execution-environment) for storing files. Files stored in `/tmp` are only guaranteed to be available for the duration of the workflow execution, and are not accessible across [workers](/glossary/#worker).

### Trigger

Triggers process data from third-party APIs and [emit](/glossary/#emit) [events](/glossary/#event) that run workflows. Triggers can be [HTTP triggers](/glossary/#http-trigger), [schedule triggers](/glossary/#schedule-trigger), [email triggers](/glossary/#email-trigger), [event sources](/glossary/#event-source), and more.

### Two-factor authentication (2FA)

Two-factor authentication. [Configure 2FA](/account/user-settings/#two-factor-authentication) to add an extra layer of security to your Pipedream account.

## U

## V

### VPC (Virtual Private Cloud)

VPCs are customer-specific private networks where workflows can run. [See the docs](/workflows/vpc/) for more details.

## W-Z

### Worker

An instance of a workflow [execution environment](/glossary/#execution-environment) available to processes [events](/glossary/#event).

### Workspace

You create a workspace when you sign up for Pipedream. Workspaces contain projects, workflows, and other resources. [See the docs](/workspaces/) for more details.

### Workspace admin

A workspace can have multiple [admins](/workspaces/#promoting-a-member-to-admin), who can administer the workspace, manage billing, and more.

### Workspace member

A user invited to a workspace. Members can create projects, workflows, and other resources in the workspace, but cannot manage billing or administer the workspace.

### Workspace owner

The user who created the workspace.

### Workflow serialization

When you use [GitHub Sync](/glossary/#github-sync), Pipedream serializes the workflow configuration to a YAML file. Optionally, if your workflow contains custom code, Pipedream serializes the code to a separate file.

### Workspace settings

[Workspace settings](/glossary/#workspace-settings) let [workspace admins](/glossary/#workspace-admin) configure settings like membership, [SSO](/glossary/#single-sign-on-sso), and more.

### Workflow template

When you [share a workflow](/workflows/building-workflows/sharing/), you create a template that anyone can copy and run.

### Workspace variable

An environment variable available across all projects in a workspace.

### Workflow

Workflows are the primary resource in Pipedream. They process events from [triggers](/glossary/#trigger) and run [steps](/glossary/#step) to perform actions like making HTTP requests, sending emails, and more.

[Troubleshooting](/troubleshooting/ "Troubleshooting")

Built with [Mintlify](https://mintlify.com).
