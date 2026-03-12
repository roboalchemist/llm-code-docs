# Source: https://docs.port.io/guides/all/visualize-and-manage-gitlab-deployments.md

# Visualize and manage your GitLab deployments

This guide demonstrates how to bring your GitLab deployment experience into Port. You will learn how to:

* Ingest GitLab pipeline data into Port's software catalog using **Port's GitLab** integration.
* Set up **self-service actions** to manage deployments (trigger, retry, and cancel).
* Build **dashboards** in Port to monitor and take action on your GitLab deployments.

![](/img/guides/gitLabDeploymentDashboard1.png) ![](/img/guides/gitLabDeploymentDashboard2.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Monitor the status and health of all GitLab deployments across accounts from a single dashboard.
* Empower platform teams to automate day-2 operations via webhooks.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [GitLab integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab-v2/) is installed in your account.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

The `GitLab Pipeline` blueprint is not created automatically when installing the GitLab integration, so we will need to create it manually.

### Create the GitLab pipeline blueprint[â](#create-the-gitlab-pipeline-blueprint "Direct link to Create the GitLab pipeline blueprint")

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add this JSON schema:

   **GitLab Pipeline blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "gitlabPipeline",
     "title": "GitLab Pipeline",
     "icon": "GitLab",
     "schema": {
       "properties": {
         "createdAt": {
           "type": "string",
           "title": "Created At",
           "format": "date-time",
           "description": "When the pipeline was created"
         },
         "updatedAt": {
           "type": "string",
           "title": "Updated At",
           "format": "date-time",
           "description": "When the pipeline was last updated"
         },
         "link": {
           "type": "string",
           "title": "Link",
           "format": "url",
           "description": "URL to the pipeline in GitLab"
         },
         "status": {
           "type": "string",
           "title": "Status",
           "enum": [
             "failed",
             "success",
             "canceled"
           ],
           "enumColors": {
             "failed": "red",
             "success": "green",
             "canceled": "darkGray"
           }
         },
         "targetBranch": {
           "type": "string",
           "title": "Branch"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "project": {
         "title": "Project",
         "target": "service",
         "required": false,
         "many": false
       }
     }
   }
   ```

5. Click `Save` to create the blueprint.

## Update the integration mapping[â](#update-the-integration-mapping "Direct link to Update the integration mapping")

1. Go to the [Data Sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Select the integration.

3. Add the following YAML block into the editor to ingest pipelines from your GitLab account:

   **GitLab integration configuration (Click to expand)**

   ```
   deleteDependentEntities: true
   createMissingRelatedEntities: true
   enableMergeEntity: true
   resources:
     - kind: project
       selector:
         query: 'true'
         includeLanguages: true
       port:
         entity:
           mappings:
             identifier: .id | tostring
             title: .name
             blueprint: '"service"'
             properties:
               url: .web_url
               readme: file://README.md
               language: .__languages | to_entries | max_by(.value) | .key
     - kind: pipeline
       selector:
         query: 'true'
       port:
         entity:
           mappings:
             identifier: .id | tostring
             title: (.project_id | tostring) + "-" + (.id | tostring)
             blueprint: '"gitlabPipeline"'
             properties:
               status: .status
               createdAt: .created_at
               updatedAt: .updated_at
               targetBranch: .ref
               link: .web_url
             relations:
               project: .project_id | tostring
   ```

4. Click `Save & Resync` to apply the mapping.

## Set up self-service actions[â](#set-up-self-service-actions "Direct link to Set up self-service actions")

We will create self-service actions in Port to directly interact with the GitLab API. These actions let users:

1. Trigger a new pipeline.

2. Retry failed or canceled jobs in a pipeline.

3. Cancel a running pipeline.

Each action will be configured via JSON and triggered using **synced webhooks** secured with secrets. To implement these use-cases, follow the steps below:

### Add Port secrets

To add a secret to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secret:

   * `GITLAB_TRIGGER_TOKEN`: The token used to authenticate the request. To obtain this token, [see the documentation](https://docs.port.io/actions-and-automations/setup-backend/gitlab-pipeline/saas#create-the-webhook-url).

### Trigger a new pipeline[â](#trigger-a-new-pipeline "Direct link to Trigger a new pipeline")

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Trigger a new pipeline action (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "trigger_pipeline",
     "title": "Trigger Pipeline",
     "icon": "GitLab",
     "description": "Triggers a Gitlab pipeline in the specified repository",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "environment": {
             "icon": "DefaultProperty",
             "title": "Environment",
             "type": "string",
             "default": "test",
             "enum": [
               "test",
               "staging",
               "production"
             ],
             "enumColors": {
               "test": "lightGray",
               "staging": "lightGray",
               "production": "lightGray"
             }
           }
         },
         "required": [],
         "order": [
           "environment"
         ]
       },
       "blueprintIdentifier": "service"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://gitlab.com/api/v4/projects/{{.entity.identifier}}/ref/main/trigger/pipeline?token={{.secrets.GITLAB_TRIGGER_TOKEN}}",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Content-Type": "application/json"
       },
       "body": {
         "{{ spreadValue() }}": "{{ .inputs }}",
         "port_context": {
           "runId": "{{ .run.id }}",
           "blueprint": "{{ .action.blueprint }}",
           "entity": "{{ .entity }}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Trigger Pipeline` action in the self-service page. ð

### Retry jobs in a pipeline[â](#retry-jobs-in-a-pipeline "Direct link to Retry jobs in a pipeline")

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Retry jobs in a pipeline action (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "retry_pipeline",
     "title": "Retry Pipeline",
     "icon": "Pipeline",
     "description": "Retry failed or canceled jobs in a pipeline",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {},
         "required": [],
         "order": []
       },
       "condition": {
         "type": "SEARCH",
         "rules": [
           {
             "property": "status",
             "operator": "in",
             "value": [
               "failed",
               "cancelled"
             ]
           }
         ],
         "combinator": "and"
       },
       "blueprintIdentifier": "gitlabPipeline"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://gitlab.com/api/v4/projects/{{.entity.relations.project}}/pipelines/{{.entity.identifier}}/retry",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Content-Type": "application/json",
         "PRIVATE-TOKEN": "{{.secrets.GITLAB_TRIGGER_TOKEN}}"
       },
       "body": {
         "{{ spreadValue() }}": "{{ .inputs }}",
         "port_context": {
           "runId": "{{ .run.id }}",
           "blueprint": "{{ .action.blueprint }}",
           "entity": "{{ .entity }}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Retry Pipeline` action in the self-service page. ð

### Cancel a running pipeline[â](#cancel-a-running-pipeline "Direct link to Cancel a running pipeline")

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Cancel a running action (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "cancel_pipeline",
     "title": "Cancel Pipeline",
     "icon": "Unavailable",
     "description": "Cancel all jobs for a pipeline",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {},
         "required": [],
         "order": []
       },
       "blueprintIdentifier": "gitlabPipeline"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://gitlab.com/api/v4/projects/{{.entity.relations.project}}/pipelines/{{.entity.identifier}}/cancel",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Content-Type": "application/json",
         "PRIVATE-TOKEN": "{{.secrets.GITLAB_TRIGGER_TOKEN}}"
       },
       "body": {
         "{{ spreadValue() }}": "{{ .inputs }}",
         "port_context": {
           "runId": "{{ .run.id }}",
           "blueprint": "{{ .action.blueprint }}",
           "entity": "{{ .entity }}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Cancel Pipeline` action in the self-service page. ð

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

With pipelines ingested and actions configured, the next step is building a dashboard to monitor GitLab data directly in Port. We can visualize all pipeline details using customizable widgets. In addition, we can trigger remediation workflows right from your dashboard.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page of your portal.
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **Gitlab Deployment Manager**.
5. Input `A dashboard to view, retry, and cancel deployments in Gitlab` under **Description**.
6. Select the `GitLab` icon.
7. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize insights from our GitLab deployments. In this guide, we define deployments as pipelines created against the `main` branch of the repository.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Total deployments created in the last 3 months (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Total deployments` (add the `Deployment` icon).

3. Select `Count entities` **Chart type** and choose **GitLab Pipeline** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter deployments created in the last 3 months:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"targetBranch",
                   "operator":"=",
                   "value":"main"
               },
               {
                   "property":"createdOn",
                   "operator":"between",
                   "value":{
                   "preset":"last3Months"
                   }
               }
           ]
       }
   ]
   ```

6. Select `custom` as the **Unit** and input `deployments` as the **Custom unit**

   ![](/img/guides/totalGitLabDeployments.png)

7. Click `Save`.

**Deployment by status (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Deployments by state` (add the `Deployment` icon).

3. Choose the **GitLab Pipeline** blueprint.

4. Under `Breakdown by property`, select the **Status** property

5. Add this JSON to the **Additional filters** editor to filter deployments:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "targetBranch",
         "operator": "=",
         "value": "main"
       },
       {
         "operator": "=",
         "value": "gitlabPipeline",
         "property": "$blueprint"
       }
     ]
   }
   ```

   ![](/img/guides/GitlabDeploymentByState.png)

6. Click **Save**.

**Trigger pipeline action (click to expand)**

1. Click **`+ Widget`** and select **Action card**.

2. Choose the **Trigger Pipeline** action we created in this guide

   ![](/img/guides/gitlabTriggerPipelineAction.png)

3. Click **Save**.

**All GitLab deployments view (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **All Deployments**.

3. Choose the **GitLab Pipeline** blueprint.

4. Add this JSON to the **Additional filters** editor to filter deployments:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "targetBranch",
         "operator": "=",
         "value": "main"
       },
       {
         "operator": "=",
         "value": "gitlabPipeline",
         "property": "$blueprint"
       }
     ]
   }
   ```

   ![](/img/guides/allGitLabDeployments.png)

5. Click **Save** to add the widget to the dashboard.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on `Manage Properties` and add the following properties:

   * **Status**: The status of the pipeline.
   * **Link**: The URL to the pipeline.
   * **Branch**: The target branch of the pipeline.
   * **Created At**: The date the pipeline was created in GitLab.
   * **Repository**: The related GitLab project.

8. Click on the **save icon** in the top right corner of the widget to save the customized table.
