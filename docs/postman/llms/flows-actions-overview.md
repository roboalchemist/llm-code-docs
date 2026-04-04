# Flows actions overview

An *action* is a flow that's deployed in the Postman cloud. Unlike [*flow modules*](/docs/postman-flows/get-started/build-your-first-flow/), which must be run manually, actions can be triggered with automatic schedules, or with requests from webhooks, third-party apps, or other APIs. Actions are useful for running automations and exposing functionality as an API or as an AI tool for MCP servers.

Actions can process incoming data and return structured responses. Once deployed, a request-triggered action gets a unique cloud-hosted URL. An action's URL is useful for tasks like automating business logic, handling webhooks, integrating with external services, or powering AI-driven tools on MCP servers.

## Local and deployed actions run in the Postman cloud and don't support private APIs.

Actions are available in Postman version 11.42.3 and later.

To learn about creating and deploying actions, see [Deploy flows as actions in Postman Flows](/docs/postman-flows/build-flows/structure/actions/).

## Manage long-running actions

Actions typically send out any data they produce as HTTP response bodies. This holds true for any action that finishes running in less than the **Timeout** duration. The data flows through the **Response** block.

The maximum **Timeout** is 30 seconds. If your action requires longer to run, [contact Postman support](/docs/administration/domain-verification-and-capture/enable-domain-capture/#contact-support-to-manage-accounts) to request an increase of the maximum timeout value to 60 seconds.

Once the **Timeout** interval has elapsed, the **Response** block sends out a 408 Request Timeout error. The action will continue running for up to 60 minutes, at which point it will automatically stop.

If your action requires over 60 seconds to run, it won't be able to send out data from the **Response** block. Instead, design your action to be [asynchronous](#synchronous-and-asynchronous-actions).

## Deploy actions with snapshots

Actions can be *deployed* in the Postman cloud. Once deployed, a request-triggered action has a unique URL. You and other users can send requests to the action's URL and receive responses from it.

As with flow modules, you can create and restore different [snapshots](/docs/postman-flows/build-flows/configure/snapshots/) of an action. Snapshots are like different versions of an action. When you deploy an action to make it publicly available in the Postman cloud, you can deploy a new snapshot or an existing one.

If you deploy an existing snapshot, the local version of your action doesn't automatically restore the snapshot when you deploy it. To learn about restoring snapshots and more, see [Version flows with snapshots](/docs/postman-flows/build-flows/configure/snapshots/).

## Schedule actions to run automatically

You can automate actions to run at regular intervals or at specific times. Automated actions can be useful for testing and other scheduled events in your API workflow. To learn more, see [Schedule an action to run automatically](/docs/postman-flows/build-flows/structure/actions/#schedule-an-action-to-run-automatically).

## Bearer tokens in actions

You can configure actions to authorize requests with a [*bearer token*](/docs/sending-requests/authorization/authorization-types/#bearer-token). Bearer tokens make actions more secure by only granting access to requests that include the token.

Learn how to [enforce bearer token authorization for actions](/docs/postman-flows/build-flows/structure/actions/#enforce-bearer-token-authorization-for-actions).

## Synchronous and asynchronous actions

You can design your actions to be *synchronous* (sync) or *asynchronous* (async). In a sync action, all the blocks complete their functions before the action sends a response. An async action sends a response before its blocks finish running.

For example, if an AI block in your action takes several seconds to complete a task, you may choose to send the response first. Async actions are useful when integrating with webhooks from services that expect a quick response, like Slack.

Here's an example of an async action:

![Async action](https://assets.postman.com/postman-docs/v11/flows-async-action-v11-40.jpg)

In this action, a **Validate** block checks the request data against a schema. If the request data is valid, the action simultaneously sends a Status Code 200 response and triggers the **Create with AI** block. The **Create with AI** block may complete after the action's timeout setting elapses. By making the action async, it can send a response before completing its workflow.

## How actions parse received data

Flows actions parse incoming data as a structured data object. Each field in the object maps to a list of string values. For example, when an action receives the following data:

```bash
token=9XqPLt7mKaRjVh2NbzC4f5Yw&team_id=T91H6Z2LK&team_domain=acme&channel_id=C72DF1XRK9&channel_name=integration-testing&user_id=U18ABZQXPR&user_name=jane.doe&command=/flows&text=status&api_app_id=A45K9L72QM&is_enterprise_install=false&enterprise_id=E55YT9QWKV&enterprise_name=AcmeCorp&response_url=https://hooks.slack.com/commands/T91H6Z2LK/3399128457101/HgT9yW3aKpLvQ8RbFsXe5JdM&trigger_id=3399128462830.8451991626.a1bc
```

it parses the data like this:

```json
{
  "token": ["9XqPLt7mKaRjVh2NbzC4f5Yw"],
  "team_id": ["T91H6Z2LK"],
  "team_domain": ["acme"],
  "channel_id": ["C72DF1XRK9"],
  "channel_name": ["integration-testing"],
  "user_id": ["U18ABZQXPR"],
  "user_name": ["jane.doe"],
  "command": ["/flows"],
  "text": ["status"],
  "api_app_id": ["A45K9L72QM"],
  "is_enterprise_install": ["false"],
  "enterprise_id": ["E55YT9QWKV"],
  "enterprise_name": ["AcmeCorp"],
  "response_url": ["https://hooks.slack.com/commands/T91H6Z2LK/3399128457101/HgT9yW3aKpLvQ8RbFsXe5JdM"],
  "trigger_id": ["3399128462830.8451991626.a1bcde230ab982f3d451f9bce67d041d"]
}
```