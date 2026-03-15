# Source: https://docs.firehydrant.com/docs/circleci-event-source.md

# CircleCI Event Source

The CircleCI Integration for Signals allows users to create events in FireHydrant from webhooks configured in CircleCI. Anytime that CircleCI sends an event to FireHydrant, we’ll evaluate the signal to see if if matches a rule setup by one of your teams. If it matches that rule, we’ll alert the team. Learn more about Alert Rules here.

## Configuring CircleCI Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL that you will use when creating a webhook in CircleCI

   <Image align="center" width="800px" src="https://files.readme.io/8ae14e5-circle-webhook.jpg" />
2. In CircleCI, navigate to a project's settings page. In the left navigation, find the webhooks option. On the webhooks page, click Add Webhook.
3. Add the URL from step 1 to your webhook.
4. Select the events that you want to trigger Signals in FireHydrant.
5. Click “Add” to save your webhook.

You can learn more about CircleCI webhooks by reading their Webhooks documentation.

## Testing your CircleCI Webhook

1. When editing your webhook, click "Test Ping Event" to send a sample payload to FireHydrant.
2. Confirm that FireHydrant received your webhook by visiting Alerting > Webhook Logs in the web app. You should see a new Signal created. You can open the drawer to see the full payload from CircleCI.

## Field Mappings

FireHydrant's CircleCI transposer will map the following data to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

| CircleCI Parameter                                                                                   | FireHydrant Parameter                                                                                                          |
| :--------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| `{payload.pipeline.vcs.origin_repository_url}-{payload.workflow.name}-{payload.pipeline.vcs.branch}` | `idempotency_key` - Specifically FireHydrant appends together the repo URL, workflow name, and branch of the build with dashes |
| `Build {payload.workflow.status} on {payload.project.slug}`                                          | `summary` - The summary will always be a statement about the build status on the particular CircleCI project                   |
| `Branch {payload.pipeline.vcs.branch} revision {payload.pipeline.vcs.revision}`                      | `body` - The body will always list the branch and the revision                                                                 |
| `payload.workflow.status`                                                                            | `status` - Closed when `status` is "success", otherwise Open                                                                   |
| `payload.workflow.status`                                                                            | `level` - ERROR (2) when `status` is "failed", otherwise INFO (1)                                                              |
| `payload.workflow.url`                                                                               | `links` - FireHydrant will insert the link back to the workflow in CircleCI                                                    |
| `payload.pipeline.vcs.revision`                                                                      | `annotations['signals.firehydrant.com/vcs-revision']`                                                                          |
| `payload.pipeline.vcs.branch`                                                                        | `annotations['signals.firehydrant.com/vcs-branch']`                                                                            |
| `payload.pipeline.vcs.origin_repository_url`                                                         | `annotations['signals.firehydrant.com/vcs-repository_url']`                                                                    |
| `payload.workflow.name`                                                                              | `annotations['signals.firehydrant.com/ci-workflow']`                                                                           |
| `payload.workflow.status`                                                                            | `annotations['signals.firehydrant.com/ci-status']`                                                                             |

These mappings mean that an inbound webhook from Alertmanager with the following content

```json CircleCI Payload
{
  "type": "workflow-completed",
  "id": "da1b101c-9ef4-11ee-8c90-0242ac120002",
  "happened_at": "2022-12-15T23:42:01.681Z",
  "webhook": {
    "id": "78d48601-60f5-4a33-adb9-afc84b6a85af",
    "name": "webhook.site test - dan"
  },
  "workflow": {
    "id": "654e21ca-2823-4324-af3c-4651eb458edc",
    "name": "build_and_test",
    "created_at": "2022-12-15T23:42:01.681Z",
    "stopped_at": "2022-12-15T23:51:36.596Z",
    "url": "https://app.circleci.com/pipelines/github/firehydrant/laddertruck/46498/workflows/654e21ca-2823-4324-af3c-4651eb458edc",
    "status": "failed"
  },
  "pipeline": {
    "id": "7421ff24-6a8d-4369-991f-cf26aca17bb5",
    "number": 46498,
    "created_at": "2022-12-15T23:42:01.420Z",
    "trigger": {
      "type": "webhook"
    },
    "vcs": {
      "provider_name": "github",
      "origin_repository_url": "https://github.com/firehydrant/laddertruck",
      "target_repository_url": "https://github.com/firehydrant/laddertruck",
      "revision": "a9bb2ee29ef511ee8c900242ac120002",
      "commit": {
        "subject": "[SC-43590] Add Incident Resolution to data exports (#6942)",
        "body": "",
        "author": {
          "name": "John Smith",
          "email": "jsmith@example.com"
        },
        "authored_at": "2022-12-15T23:41:59Z",
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com"
        },
        "committed_at": "2022-12-15T23:41:59Z"
      },
      "branch": "main"
    }
  },
  "project": {
    "id": "0d498e3f-357d-4cb0-8990-e0c663a5f95c",
    "name": "laddertruck",
    "slug": "github/firehydrant/laddertruck"
  },
  "organization": {
    "id": "5f10c055-047f-4d95-9875-38ba21788024",
    "name": "firehydrant"
  }
}
```

...will result in the following mapped Signal on FireHydrant:

```json Transposed Signal
{
  "summary": "Build failed on github/firehydrant/laddertruck",
  "body": "Branch main, revision a9bb2ee29ef511ee8c900242ac120002",
  "level": 2,
  "links": [
    {
      "href": "https://app.circleci.com/pipelines/github/firehydrant/laddertruck/46498/workflows/654e21ca-2823-4324-af3c-4651eb458edc",
      "text": "CircleCI Workflow"
    }
  ],
  "annotations": {
    "signals.firehydrant.com/vcs-revision": "a9bb2ee29ef511ee8c900242ac120002",
    "signals.firehydrant.com/vcs-branch": "main",
    "signals.firehydrant.com/vcs-repository_url": "https://github.com/firehydrant/laddertruck",
    "signals.firehydrant.com/ci-workflow": "build_and_test",
    "signals.firehydrant.com/ci-status": "failed"
  },
  "idempotency_key": "https://github.com/firehydrant/laddertruck-build_and_test-main",
  "status": 0
}
```