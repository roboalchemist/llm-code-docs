# Source: https://docs.port.io/guides/all/setup-slack-reminders.md

# Slack reminders for scorecards

This guide will walk you through creating a self-service action that sends a Slack reminder for uncompleted [scorecard rules](https://docs.port.io/scorecards/overview#what-is-a-scorecard). In reality, such an action can be used by R\&D managers / Platform engineers to remind developers of unmet standards.

Once implemented:

* Developers will be notified about policies set by the platform engineer that need to be fixed.
* R\&D managers & Platform engineers will be able to remind developers about unmet requirements in the services.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Initiate changes in the organization using scorecards.
* Automate Slack reminders using Port's self-service actions.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* The [Git Integration](/build-your-software-catalog/sync-data-to-catalog/git/.md) that is relevant for you needs to be installed.
* A repository in your Git provider in which you can create a workflow/pipeline.

## Implementation[â](#implementation "Direct link to Implementation")

### Set up the action's frontend[â](#set-up-the-actions-frontend "Direct link to Set up the action's frontend")

1. Head to the [Self-service page](https://app.getport.io/self-serve) of your portal.

2. Click on the `+ Action` button on the top left corner :

   ![](/img/guides/addActionIcon.png)

3. Fill in the action's details as shown below:

   * **Title**: `Send scorecard reminder`
   * **Description**: `Send a scorecard reminder to your team on slack`
   * **Operation**: `Create`
   * **Blueprint**: `Service`
   * **icon**: `Slack`

   This Self-service has no user inputs, click on the `Next` button twice to proceed to the `Backend` tab.

   ![](/img/guides/slackActionDetails.png)

#### Define backend type[â](#define-backend-type "Direct link to Define backend type")

Now we'll define the backend of the action. Port supports multiple invocation types, depending on the Git provider you are using.

* Github
* GitLab

Fill out the form with your values:

* Replace the `Organization` and `Repository` values with your values (this is where the workflow will reside and run).

* Name the workflow `port-slack-reminder.yml`.

* Fill out your workflow details:

  ![](/img/guides/slackReminderBackend.png)

  <br />

* Scroll down to the `Configure the invocation payload` section.<br /><!-- -->This is where you can define which data will be sent to your backend each time the action is executed.

  For this action, our backend only needs to know the id of the action run, so let's send it.<br /><!-- -->Copy the following JSON snippet and paste it in the payload code box:

  ```
  {
    "runId": "{{ .run.id }}"
  }
  ```

The last step is customizing the action's permissions. For simplicity's sake, we will use the default settings. For more information, see the [permissions](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/.md) page. Click `Create`.

Fill out the form:

* Choose `Trigger Webhook URL` as the `Invocation type`.

* Leave `Endpoint URL` blank for now, we will create it in the next section and come back to update it.

* Fill the rest of the form out like this, then click `Next`:

  ![](/img/guides/slackReminderBackendGitLab.png)

* Scroll down to the `Configure the invocation payload` section.<br /><!-- -->This is where you can define which data will be sent to your backend each time the action is executed.

  For this action, our backend only needs to know the id of the action run, so let's send it.<br /><!-- -->Copy the following JSON snippet and paste it in the payload code box:

  ```
  {
    "runId": "{{ .run.id }}"
  }
  ```

The last step is customizing the action's permissions. For simplicity's sake, we will use the default settings. For more information, see the [permissions](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/.md) page. Click `Create`.

The action's frontend is now ready ð¥³

<br />

### Set up the action's backend[â](#set-up-the-actions-backend "Direct link to Set up the action's backend")

Now we want to write the logic that our action will trigger:

* Github
* GitLab

First, let's create the necessary token and secrets:

* Go to your desired Slack channel and [setup incoming webhooks](https://api.slack.com/messaging/webhooks). Make sure you copy the webhook URL, we will use it in the Github workflow.

* Go to your [Port application](https://app.getport.io/), click on the `...` in the top right corner, then click `Credentials`. Copy your `Client ID` and `Client secret`.

In the repository where your workflow will reside, create 3 new secrets under `Settings -> Secrets and variables -> Actions`:

* `SLACK_WEBHOOK_URL` - the Slack Webhook URL of the destination channel.

* `PORT_CLIENT_ID` - the client ID you copied from your Port app.

* `PORT_CLIENT_SECRET` - the client secret you copied from your Port app.

  ![](/img/guides/repositorySecretSlack.png)

<br />

<br />

Now let's create the workflow file that contains our logic.<br /><!-- -->Under `.github/workflows`, create a new file named `port-slack-reminder.yml` and use the following snippet as its content:

**Github workflow (click to expand)**

```
# port-slack-reminder.yml

name: Generate Scorecards Reminders
on:
  workflow_dispatch:
    inputs:
      runId:
        description: 'The id of the action run'
        required: true
        type: string
jobs:
    generate-scorecards-reminders:
        runs-on: ubuntu-latest
        steps:
            - name: Generate Scorecards Reminders
              uses: port-labs/port-sender@v0.2.14
              with:
                operation_kind: scorecard_reminder
                port_client_id: ${{ secrets.PORT_CLIENT_ID }}
                port_client_secret: ${{ secrets.PORT_CLIENT_SECRET }}
                port_region: eu
                slack_webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
                blueprint: service
                scorecard: ProductionReadiness
                target_kind: slack
            - name: Report status to Port
              uses: port-labs/port-github-action@v1
              with:
                clientId: ${{ secrets.PORT_CLIENT_ID }}
                clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
                baseUrl: https://api.port.io
                operation: PATCH_RUN
                runId: ${{ inputs.runId }}
                logMessage: |
                    Slack reminder sent successfully ð
```

Port Initiatives sender Github action

This workflow uses Port's [Initiatives Sender GitHub Action](https://github.com/marketplace/actions/port-sender) to send a Slack message.

First, let's create the required webhooks and variables:

* Go to your desired Slack channel and [setup incoming webhooks](https://api.slack.com/messaging/webhooks). Make sure you copy the webhook URL, we will use it in the Github workflow.

* Go to your [Port application](https://app.getport.io/), click on the `...` in the top right corner, then click `Credentials`. Copy your `Client ID` and `Client secret`.

In the GitLab project where your pipeline will reside, create 3 new variables under `Settings->CI/CD->Variables`:

* `SLACK_WEBHOOK_URL` - the Slack Webhook URL of the destination channel.

* `PORT_CLIENT_ID` - the client ID you copied from your Port app.

* `PORT_CLIENT_SECRET` - the client secret you copied from your Port app.

  ![](/img/guides/repositorySecretSlackGitLab.png)

Create a webhook in GitLab for triggering your GitLab:

* Create a [pipeline trigger token](https://docs.gitlab.com/ee/ci/triggers);
* Construct the [pipeline trigger webhook URL](https://docs.gitlab.com/ee/ci/triggers/#use-a-webhook) with your project details.
* Back in Port, edit your action and in its `backend` step paste the **webhook URL** in the `Endpoint URL` field.

Now let's create the pipeline file that contains our logic. In your GitLab project create a new file named `gitlab-ci.yaml` and use the following snippet as its content:

**GitLab pipeline (click to expand)**

```
image: python:3.10.0-alpine

stages:
  - fetch-port-access-token
  - send_reminders
  - post-run-logs
  - update-run-status

fetch-port-access-token: # Example - get the Port API access token and RunId
  stage: fetch-port-access-token
  except:
    - pushes
  before_script:
    - apk update
    - apk add jq curl -q
  script:
    - |
      accessToken=$(curl -X POST \
        -H 'Content-Type: application/json' \
        -d '{"clientId": "'"$PORT_CLIENT_ID"'", "clientSecret": "'"$PORT_CLIENT_SECRET"'"}' \
        -s 'https://api.port.io/v1/auth/access_token' | jq -r '.accessToken')
      echo "ACCESS_TOKEN=$accessToken" >> data.env
      runId=$(cat $TRIGGER_PAYLOAD | jq -r '.context.runId')
      echo "RUN_ID=$runId" >> data.env
  artifacts:
    reports:
      dotenv: data.env

generate-scorecards-reminders:
  stage: send_reminders
  image: docker:24.0.7
  services:
    - docker:24.0.7-dind
  script:
    - image_name="ghcr.io/port-labs/port-sender:$VERSION"
    - echo "Generate Scorecards Reminders"
    - |
      docker run -i --rm --platform="linux/arm64/v8" \
      -e INPUT_PORT_CLIENT_ID=$PORT_CLIENT_ID \
      -e INPUT_PORT_CLIENT_SECRET=$PORT_CLIENT_SECRET \
      -e INPUT_SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL \
      -e INPUT_OPERATION_KIND="scorecard_reminder" \
      -e INPUT_BLUEPRINT="service" \
      -e INPUT_SCORECARD="ProductionReadiness" \
      -e INPUT_TARGET_KIND="slack" \
      $image_name
    - echo "Report status to Port"

post-run-logs:
  stage: post-run-logs
  except:
    - pushes
  image: curlimages/curl:latest
  script:
    - |
      curl -X POST \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $ACCESS_TOKEN" \
        -d '{"message": "Slack reminder sent successfully ð"}' \
        "https://api.port.io/v1/actions/runs/$RUN_ID/logs"
update-run-status:
  stage: update-run-status
  except:
    - pushes
  image: curlimages/curl:latest
  script:
    - |
      curl -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $ACCESS_TOKEN" \
        -d '{"status":"SUCCESS", "message": {"run_status": "Created Merge Request for '"$bucket_name"' successfully! Merge Request URL: '"$MR_URL"'"}}' \
        "https://api.port.io/v1/actions/runs/$RUN_ID"
    
variables:
  PORT_CLIENT_ID: $PORT_CLIENT_ID
  PORT_CLIENT_SECRET: $PORT_CLIENT_SECRET
  SLACK_WEBHOOK_URL: $SLACK_WEBHOOK_URL
  VERSION: "0.2.3"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

All done! The action is ready to be used ð

### Execute the action[â](#execute-the-action "Direct link to Execute the action")

After creating an action, it will appear under the `Self-service` tab of your Port application:

![](/img/guides/selfServiceAfterReminderCreation.png)

1. Click on `Create` to begin executing the action.

2. Click `Execute`. A small popup will appear, click on `View details`:

   ![](/img/guides/executionDetailsSlack.png)

   <br />

   <br />

3. This page provides details about the action run. As you can see, the backend returned `Success` and the repo was successfully created:

   ![](/img/guides/runStatusReminder.png)

   <br />

   <br />

   Logging action progress

   ð¡ Note the `Log stream` at the bottom, this can be used to report progress, results and errors. Click [here](https://docs.port.io/actions-and-automations/reflect-action-progress/) to learn more.

   <br />

4. You can now enter your Slack channel and view the scorecard reminder:

   ![](/img/guides/slackReminderExample.png)

### Conclusion[â](#conclusion "Direct link to Conclusion")

Creating scorecards is the first step in setting standards in our development lifecycle. However, to ensure these standards are met, we need to turn rule violations into action items. By automating Slack reminders and the creation of Jira tasks, we can drive change across the entire organization using familiar tools to combine it natively within our delivery lifecycle.

### More Examples[â](#more-examples "Direct link to More Examples")

* [Open/Close JIRA issues based on scorecards](/scorecards/manage-using-3rd-party-apps/jira.md)
* [Send a scorecard report on Slack](/scorecards/manage-using-3rd-party-apps/slack.md#slack-scorecard-report-example)
