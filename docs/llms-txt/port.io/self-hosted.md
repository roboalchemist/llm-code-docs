# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/installation/self-hosted.md

# Source: https://docs.port.io/actions-and-automations/setup-backend/gitlab-pipeline/self-hosted.md

# Self-hosted GitLab

If you use the self-hosted version of GitLab in your organization, you will need to use the Port execution agent to trigger your pipelines from Port.

![](/img/self-service-actions/setup-backend/gitlab-pipeline/gitlab-pipeline-agent-architecture.jpg)

<br />

<br />

The steps shown in the image above are as follows:

1. Port publishes an invoked `action` message containing the pipeline details to a Kafka topic.
2. A secure topic (`ORG_ID.runs`) holds all the action invocations.
3. Port's execution agent pulls the new trigger event from your Kafka topic, and triggers your GitLab Pipeline.

This page will introduce the agent and guide you through the installation and configuration processes.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Connection credentials to Kafka are required. To obtain them, contact us using chat/Slack/support site at [support.port.io](http://support.port.io/).
* [Helm](https://helm.sh) must be installed in order to install the relevant chart.
* In order to trigger a GitLab Pipeline, you need to have a [GitLab trigger token](https://docs.gitlab.com/ee/ci/triggers/).

Trigger Tokens

To provide your trigger token to the agent, pass the helm chart an environment variable with a name that is the combination of the `GitLab group` and `GitLab project`, separated by an underscore (`_`). The name is case sensitive.

For example: `group_project=token`

You can load multiple trigger tokens, for different groups and projects in your GitLab environment.

## Installing the agent[â](#installing-the-agent "Direct link to Installing the agent")

1. Add Port's Helm repo by using the following command:

   ```
   helm repo add port-labs https://port-labs.github.io/helm-charts
   ```

   Ensure you have the latest charts

   If you already added this repo earlier, run `helm repo update` to retrieve the latest versions of the charts.<br /><!-- -->You can then run `helm search repo port-labs` to see the charts.

2. Install the `port-agent` chart using the following command:

   ```
   helm install my-port-agent port-labs/port-agent \
       --create-namespace --namespace port-agent \
       --set env.normal.PORT_ORG_ID=YOUR_ORG_ID \
       --set env.normal.KAFKA_CONSUMER_GROUP_ID=YOUR_KAFKA_CONSUMER_GROUP \
       --set env.secret.PORT_CLIENT_ID=YOUR_PORT_CLIENT_ID \
       --set env.secret.PORT_CLIENT_SECRET=YOUR_PORT_CLIENT_SECRET \
       --set env.secret.<YOUR GITLAB GROUP>_<YOUR GITLAB PROJECT>=YOUR_GITLAB_TOKEN \
       --set env.normal.GITLAB_URL=YOUR_GITLAB_URL
   ```

   To get your Port credentials, go to your [Port application](https://app.getport.io), click on the `...` button in the top right corner, and select `Credentials`. Here you can view and copy your `CLIENT_ID` and `CLIENT_SECRET`:

   ![](/img/software-catalog/credentials-modal.png)

   <br />

Done! **Port's execution agent** is now running in your environment and will trigger any GitLab pipeline that you have configured.

## Configure the backend[â](#configure-the-backend "Direct link to Configure the backend")

Once the agent is installed, we can finish setting up the backend in Port.

1. Make sure that `Run Gitlab Pipeline` is selected as the backend type.

2. Now all we need is to provide the following details:

   ![](/img/create-self-service-experiences/setup-backend/gitlab/gitlab-backend.png)

   <br />

* **Project** - the name of the GitLab project.
  <br />
  <!-- -->
  The name can be obtained from your project URL: `https://gitlab.com/GROUP/SUBGROUP/PROJECT`.
* **Group/subgroup** - the group and/or subgroup that the project belongs to.
  <br />
  <!-- -->
  Can also be obtained from the project URL: `https://gitlab.com/GROUP/SUBGROUP/PROJECT`.
* **Default ref** - the branch/tag name we want the action/automation to use.

Create action/automation via API

If you wish to create a self-service action or automation via [Port's API](https://docs.port.io/api-reference/create-an-action-automation), choose the `gitlab` backend type under the `invocationMethod` object.

### Configure the payload[â](#configure-the-payload "Direct link to Configure the payload")

The payload is the data sent to the webhook URL every time the action/automation is executed. It is defined by the action/automation creator and can include any data that is needed by the GitLab pipeline.

When using the `GitLab` backend, the payload is defined under the `pipelineVariables` field.

* For more information about defining a payload for **self-service actions**, click [here](/actions-and-automations/create-self-service-experiences/setup-the-backend/.md#define-the-actions-payload).
* For more information about defining a payload for **automations**, click [here](/actions-and-automations/define-automations/setup-action.md#define-the-payload).
