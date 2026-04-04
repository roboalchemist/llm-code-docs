Source: https://docs.slack.dev/changelog/2023-08-workflow-steps-from-apps-step-back

# Workflow Steps from Apps step back

August 22, 2023

We're retiring support for traditional Slack apps providing _Steps from Apps_ to our legacy workflow builder and workflows created with it. Read on to learn whether your apps or workflows are impacted.

Beginning September 26, 2024, Slack will no longer support executing workflows containing a "step from app."

This means that all workflows containing Steps from Apps and the steps themselves will cease functioning on September 26, 2024. There is no _direct_ migration path for existing steps or workflows.

Updates to this post

Legacy Workflow Builder, legacy workflows, _and_ Workflow Builder Steps from Apps will all retire on **September 26, 2024** (previously September 12, 2024).

We've expanded the information below to explain further the impact to workflows and provide instruction to teams looking to recreate their steps on the automation platform. We've clarified the lack of a clear path for developers distributing Steps from Apps in the Slack Marketplace.

Since we originally published this article, we've introduced beta support for [custom functions](/workflows/workflow-steps) authored in Bolt for Python and Bolt for JavaScript, which can help those looking to migrate steps hosted on your own infrastructure.

Our new [automation platform](/workflows) for developers and builders features an entirely new way of building workflows and adding custom functionality.

We replaced the traditional platform's ability to build _Steps from Apps_ with a new model allowing developers to create coded [**custom functions**](/tools/deno-slack-sdk/guides/creating-custom-functions). We added a collection of [**connectors**](https://slack.com/help/articles/17542172840595-Create-a-new-workflow-in-Slack#add-steps-to-your-workflow) that run on Slack, empowering more useful workflows than previously possible.

> _What was _Steps from Apps_?_ Steps from Apps gave Slack app developers a way to add their own limited functionality to the original version of Workflow Builder. They don't work with the new version of Workflow Builder and workflows containing them cannot be automatically migrated to the new Workflow Builder.

## What's changing? {#what}

The entire workflow system, including Workflow Builder is an entirely different implementation for users, builders, and developers alike.

As far as what's changing for _Steps from Apps_ in particular: as of October 2023, apps can no longer add the `workflow:steps.execute` scope or related steps when submitting or resubmitting changes to the Slack Marketplace.

On September 26, 2024 we'll retire _Steps from Apps_ permanently:

* You will no longer be able to turn on the _Workflow Steps_ feature to your Slack apps.
* You will not be able to add subscriptions to `workflow_step_execute`, `workflow_published`, `workflow_unpublished`, `workflow_deleted`, and `workflow_step_deleted` events.
* You will also stop receiving events from your subscriptions to the above events because the workflows will no longer be executed. Any business logic you execute when these events are received will not be exercised.
* Your apps won't be able to ask for the `workflow.steps:execute` scope anymore, and users won't be able to install apps that ask for it. You'll need to stop asking for the scope to continue being installed. You should unsubscribe to the related events as well.
* Existing workflows containing _Steps from Apps_ will no longer be in an executable state by users.
* The Web API methods `workflows.stepCompleted`, `workflows.stepFailed`, and `workflows.updateStep` will all cease functioning.

Custom functions in the automation platform may serve the same purpose as "Steps from Apps" but their implementation is very different. Read on if you're interested in porting your existing functionality to the new automation platform.

## How do I prepare? {#how}

Impacted apps can be identified as those requesting the `workflow.steps:execute` scope. You'll also find that your app is subscribed to events like `workflow_step_execute`. If your app doesn't use these scopes or events, it's unlikely that it provides _Steps from Apps_.

### Steps from Apps for your team or organization {#your-org}

If you built a "step from app" with your own workspace or organization in mind, we recommend re-implementing your step as a **[custom function](/tools/deno-slack-sdk/guides/creating-custom-functions).** We currently fully support custom functions in [Deno](/tools/deno-slack-sdk/guides/installing-deno)\-flavored [Typescript](/tools/deno-slack-sdk/guides/developing-with-typescript) [deployed on Slack](/tools/deno-slack-sdk/guides/deploying-to-slack).

We are also introducing support from self-hosted custom functions using [Bolt for JavaScript and Bolt for Python](/workflows/workflow-steps). Support for self-hosted custom functions is currently beta but we encourage developers to get started today.

Porting an existing _step from app_ to custom functions is best treated as a fresh implementation project. While the business logic your step executes in the `workflow_step_execute` event is likely similar to code you would execute when a custom step is run, new workflows don't support a configuration step, nor "lifecycle events" when custom functions are added, removed, or configured.

Without a configuration step, you may want to make your function's behavior configurable through a conversational interface. Maybe your step doesn't need any configuration at all.

Your Bolt apps must be org-ready installable to make steps available -- this is because the workflow engine itself is org-ready.

Here are some tutorials to help you get started:

* [creating a new Bolt app with a custom step in JavaScript](/tools/bolt-js/tutorials/custom-steps-workflow-builder-new)

* [creating a new Bolt app with a custom step in Python](/tools/bolt-python/tutorial/custom-steps-workflow-builder-new).

### Distributed Steps from Apps {#distributed}

For existing distributed or Slack Marketplace apps, there is **no clear path forward** to continue supporting the new Workflow Builder. We've introduced a concept called [_connector functions_](/tools/deno-slack-sdk/reference/connector-functions), but at this time they cannot be developed outside of Slack.

While you can now build custom steps using Bolt for Python or Javascript, those steps cannot be distributed or published to organizations as part of your Slack apps.

If you wish to enable your customers to integrate Workflow Builder with your app or services, we recommend making code they can host and execute available so they can utilize your functionality as custom functions in the new Workflow Builder.

There is no other path to distributing custom functions as part of a distributed Slack app or as an app in the Slack Marketplace at this time.

## What if I do nothing? {#nothing}

If your Slack app doesn't support _Steps from Apps_, this change will likely not impact you.

If you use legacy workflows created by the original Workflow Builder that include any _Steps from Apps_, you won't be able to use those workflows after September 26, 2024.

If your app already supplies a step from app, that step from app will stop functioning in existing workflows and be unable to be added to future legacy workflows.

The new Workflow Builder does not reveal _Steps from Apps_ to users. Your steps will not appear in the new Workflow Builder unless you build them as custom functions.

## When does this happen? {#when}

All paid workspaces can access the new Workflow Builder today. Customers may continue building and executing legacy workflows containing _Steps from Apps_ until September 26, 2024.

On September 26, 2024 legacy workflows containing _Steps from Apps_ will stop working and users will no longer be able to add _Steps from Apps_ features to workflows. Our legacy Workflow Builder will become unavailable and only workflows created on or migrated to the automation platform will continue functioning.

We encourage you to explore the [new automation platform](/workflows) today.

* * *

Please reach out to us to us if you have any questions about these changes, or about Steps from Apps, Workflow Builder, connectors, and our new automation platform.

**Tags:**

* [Breaking change](/changelog/tags/breaking-change)
* [Deprecation](/changelog/tags/deprecation)
