# Source: https://docs.port.io/actions-and-automations/setup-backend/gitlab-pipeline/saas.md

# GitLab SaaS

If you use the cloud (SaaS) version of GitLab in your organization, the simplest way to trigger your pipelines from Port is to use the [webhook backend](/actions-and-automations/setup-backend/webhook/.md).

GitLab allows you to create webhooks URLs that can be triggered from external services, such as Port, causing a pipeline to run in your GitLab project.

## Configure the backend[â](#configure-the-backend "Direct link to Configure the backend")

Choose `Trigger Webhook URL` as the backend type when creating a new self-service action or automation.

When using the webhook backend, you need to configure several parameters:

![](/img/create-self-service-experiences/setup-backend/gitlab/webhook-backend.png)

<br />

<br />

* Since we are using GitLab SaaS, the `Use self-hosted agent` option should be set to `No`.
* Read about the `Request type` in the [webhook backend](/actions-and-automations/setup-backend/webhook/.md#request-type---sync-vs-async) page.
* The `Method` field should be set to `POST`.
* The `Endpoint URL` field should be filled with the webhook URL you create in GitLab (see below).

Create action/automation via API

If you wish to create a self-service action or automation via [Port's API](https://docs.port.io/api-reference/create-an-action-automation), choose the `webhook` backend type under the `invocationMethod` object.

### Create the webhook URL[â](#create-the-webhook-url "Direct link to Create the webhook URL")

A webhook URL used to trigger a pipeline in GitLab looks like this:

```
https://gitlab.com/api/v4/projects/{GITLAB_PROJECT_ID}/ref/main/trigger/pipeline?token={GITLAB_TRIGGER_TOKEN}
```

As you can see, there are two parameters that need to be filled in:

* **`{GITLAB_PROJECT_ID}`** - The ID of the GitLab project containing your pipeline file.<br /><!-- -->To obtain the project ID, navigate to your project in GitLab, click on the `â®` button in the top right corner, and select `Copy project ID`.

* **`{GITLAB_TRIGGER_TOKEN}`** - The token used to authenticate the request.

  To create a new trigger token, follow these steps:

  * Navigate to your GitLab project page.
  * Go to `Settings` -> `CI/CD`.
  * Expand `Pipeline trigger tokens`.
  * Select `Add new token`.
  * Add a description and click `Create pipeline trigger token`.

  **Note:** You must have (at least) the `Maintainer` role in the project to create a new trigger token.

### Webhook security[â](#webhook-security "Direct link to Webhook security")

For increased security, you can [validate the webhook signature](/actions-and-automations/setup-backend/webhook/signature-verification.md).

### Configure the payload[â](#configure-the-payload "Direct link to Configure the payload")

The payload is the data sent to the webhook URL every time the action/automation is executed. It is defined by the action/automation creator and can include any data that is needed by the GitLab pipeline.

When using the `webhook` backend, the payload is defined under the `headers` and `body` fields.

* For more information about defining a payload for **self-service actions**, click [here](/actions-and-automations/create-self-service-experiences/setup-the-backend/.md#define-the-actions-payload).
* For more information about defining a payload for **automations**, click [here](/actions-and-automations/define-automations/setup-action.md#define-the-payload).

## Examples[â](#examples "Direct link to Examples")

For guides and examples of self-service actions using a GitLab pipeline as the backend, check out the [**guides section**](/guides/.md?tags=GitLab\&tags=Actions).
