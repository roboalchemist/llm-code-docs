# Source: https://docs.port.io/guides/all/create-slack-channel-for-reported-incident.md

# Auto-create Slack channel & GitHub issue for PagerDuty incidents

This guide demonstrates how to set up an automated incident management system that creates a dedicated Slack channel and GitHub issue whenever a PagerDuty incident is reported.

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

Once implemented:

* A new Slack channel will be automatically created for each incident, providing a dedicated space for team communication.
* A GitHub issue will be automatically created to document the incident and track progress.
* The incident entity in Port will be updated with links to both the Slack channel and GitHub issue.
* Team members will receive immediate notifications and have a centralized place to collaborate.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Real-time incident response**: Automatically create communication channels when incidents are reported.
* **Incident documentation**: Ensure every incident is properly documented in your issue tracking system.
* **Team collaboration**: Provide dedicated spaces for teams to discuss and resolve incidents.
* **Audit trail**: Maintain a complete record of incident response activities.
* **Automated workflows**: Reduce manual steps in incident management processes

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* GitHub (Legacy)
* GitHub (Ocean)

- Install Port's [GitHub app](https://github.com/apps/getport-io) in your GitHub organization.
- [Ingest GitHub issues](/build-your-software-catalog/sync-data-to-catalog/git/github/examples/.md#mapping-repositories-and-issues) using Port's GitHub app.

* Install [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).
* Ingest GitHub issues using GitHub ocean (see [GitHub ocean examples](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/examples.md)).

- Install Port's [PagerDuty integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md) for real-time incident ingestion.

- Prepare your Port organization's `Client ID` and `Client Secret` ([find your credentials here](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)).

- Configure a Slack app:

  <!-- -->

  * [Create a Slack app](https://api.slack.com/start/quickstart#creating) and install it in a workspace.

  * Save the `Bot User OAuth Token` for later use.

  * [Add the following permissions](https://api.slack.com/quickstart#scopes) to the Slack app in **OAuth & Permissions** under `Bot Token Scopes`:

    <!-- -->

    * **Create channels**: `channels:manage`, `groups:write`, `im:write`, `mpim:write`
    * **Send messages**: `chat:write`

## Set up the data model[â](#set-up-the-data-model "Direct link to Set up the data model")

To support our automated incident management workflow, we need to modify the existing PagerDuty Incidents blueprint to include additional properties and relations.

### Update PagerDuty incidents blueprint

1. Go to the [data model](https://app.getport.io/settings/data-model) page of your portal.

2. Find the `pagerdutyIncident` blueprint.

3. Click on `...` and select `Edit JSON`.

4. Add the following snippet to the `properties` section:

   **Slack channel property (Click to expand)**

   ```
   "slack_channel": {
       "type": "string",
       "description": "The Slack Channel opened for troubleshooting this incident",
       "title": "Slack Channel URL",
       "icon": "Slack",
       "format": "url"
   }
   ```

5. Add the following snippet to the `relations` section:

   **Service and issue relations (Click to expand)**

   ```
   "service": {
       "title": "Service",
       "description": "The service this incident is related to",
       "target": "service",
       "required": false,
       "many": false
   },
   "issue": {
       "target": "githubIssue",
       "title": "GitHub Issue",
       "many": false,
       "required": false,
       "description": "The issue created for documenting this incident"
   }
   ```

6. Click "Save" to update the blueprint.

Service identifier mapping

For simplicity, this guide assumes that the GitHub `Service` entity identifier matches the `PagerDuty Service` identifier (lowercased and split by `-`).

For example, a PagerDuty incident for the `My Service` PagerDuty service will be related to the `my-service` GitHub service.

## Set up GitHub workflow[â](#set-up-github-workflow "Direct link to Set up GitHub workflow")

We will create a GitHub workflow that handles the incident response process. This workflow will create the Slack channel, send notifications, and create the GitHub issue.

### Add GitHub repository secrets

1. Go to your GitHub repository settings.

2. Navigate to **Secrets and variables** â **Actions**.

3. Add the following secrets:

   * `PORT_CLIENT_ID` - Your Port client ID
   * `PORT_CLIENT_SECRET` - Your Port client secret
   * `ORG_ADMIN_TOKEN` - Your GitHub personal access token
   * `BOT_USER_OAUTH_TOKEN` - The Slack app bot token

Existing secrets

If you've already completed the [scaffold a new service guide](/guides/all/scaffold-a-new-service.md), you should already have the first three secrets configured.

### Create incident handler workflow

1. In your GitHub repository, create the file `.github/workflows/handle-incident.yaml`.

   Dedicated repository

   We recommend using a dedicated repository for your Port actions and automations. This approach provides better organization, security, and maintainability of your workflows.

2. Copy and paste the following workflow configuration:

   **Handle incident workflow (Click to expand)**

   .github/workflows/handle-incident.yaml

   ```
   name: Handle Incident

   on:
     workflow_dispatch:
       inputs:
         port_payload:
           description: "Port's payload, including details for who triggered the action and general context (blueprint, run ID, etc...)."
           required: true

   # These permissions are required for the GitHub issue creation
   permissions:
     contents: read
     issues: write 

   jobs:
     handle-new-incident:
       runs-on: ubuntu-latest
       env:
         PD_INCIDENT_ID: ${{ fromJson(inputs.port_payload).event.diff.after.identifier }}
         PD_INCIDENT_URL: ${{ fromJson(inputs.port_payload).event.diff.after.properties.url }}
         PD_INCIDENT_TITLE: ${{ fromJson(inputs.port_payload).event.diff.after.title }}
         PORT_INCIDENT_URL: https://app.getport.io/pagerdutyIncidentEntity?identifier=${{ fromJson(inputs.port_payload).event.diff.after.identifier }}

       steps:
         - uses: actions/checkout@v4

         - name: Log GitHub Issue Creation
           uses: port-labs/port-github-action@v1
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             baseUrl: https://api.port.io
             operation: PATCH_RUN
             runId: ${{ fromJson(github.event.inputs.port_payload).run.id }}
             logMessage: "Creating a new GitHub issue for PagerDuty incident '${{ env.PD_INCIDENT_ID }}'..."

         - name: Get incident's related service
           id: get-incident-service
           uses: port-labs/port-github-action@v1
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             baseUrl: https://api.port.io
             operation: GET
             blueprint: pagerdutyService
             identifier: ${{ fromJson(inputs.port_payload).event.diff.after.relations.pagerdutyService }}
         
         # The GitHub Service entity identifier is defined as PagerDuty title lowercased and split by '-'
         - name: Extract related service
           id: get-service-info
           run: |
             service_title=$(echo '${{ steps.get-incident-service.outputs.entity }}' | jq -r '.title')
             echo "SERVICE_TITLE=$service_title" >> $GITHUB_OUTPUT
             echo "SERVICE_IDENTIFIER=$(echo $service_title | tr '[:upper:] ' '[:lower:]-')" >> $GITHUB_OUTPUT

         - name: Create GitHub issue
           uses: dacbd/create-issue-action@main
           id: create-github-issue
           with:
             token: ${{ secrets.ORG_ADMIN_TOKEN }}
             repo: ${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}
             title: PagerDuty incident - ID ${{ env.PD_INCIDENT_ID }}
             labels: bug, incident, pagerduty
             body: |
               PagerDuty incident issue reported.
               Port Incident Entity URL: ${{ env.PORT_INCIDENT_URL }}.
               PagerDuty incident URL: ${{ env.PD_INCIDENT_URL }}.

         - name: Report GitHub issue to Port
           uses: port-labs/port-github-action@v1
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             identifier: ${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}-${{ steps.create-github-issue.outputs.number }}
             blueprint: githubIssue
             relations: |
               {
                 "service": "${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}"
               }

         - name: Log Executing Request to Open Channel
           uses: port-labs/port-github-action@v1
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             baseUrl: https://api.port.io
             operation: PATCH_RUN
             runId: ${{ fromJson(github.event.inputs.port_payload).run.id }}
             logMessage: | 
               GitHub issue created successfully - ${{ steps.create-github-issue.outputs.html_url }}
               Creating a new Slack channel for this incident...

         - name: Create Slack Channel
           id: create-slack-channel
           env:
             CHANNEL_NAME: incident-${{ env.PD_INCIDENT_ID }}
             SLACK_TOKEN: ${{ secrets.BOT_USER_OAUTH_TOKEN }}
           run: |
             channel_name=$(echo "${{ env.CHANNEL_NAME }}" | tr '[:upper:]' '[:lower:]')
             response=$(curl -s -X POST "https://slack.com/api/conversations.create" \
               -H "Authorization: Bearer ${{ env.SLACK_TOKEN }}" \
               -H "Content-Type: application/json" \
               -d "{\"name\":\"$channel_name\"}")
           
             # Check if the channel was created successfully
             ok=$(echo $response | jq -r '.ok')
             
             if [ "$ok" == "true" ]; then
               echo "Channel '$channel_name' created successfully."
               channel_id=$(echo $response | jq -r '.channel.id')
               echo "SLACK_CHANNEL_ID=$channel_id" >> $GITHUB_OUTPUT
             else
               error=$(echo $response | jq -r '.error')
               echo "Error creating channel: $error"
               echo "SLACK_ERROR=$error" >> $GITHUB_OUTPUT
               exit 1
             fi
             
         - name: Log failed Slack channel creation
           if: failure()
           uses: port-labs/port-github-action@v1
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             baseUrl: https://api.port.io
             operation: PATCH_RUN
             runId: ${{ fromJson(github.event.inputs.port_payload).run.id }}
             logMessage: "Failed to create slack channel: ${{ steps.create-slack-channel.outputs.SLACK_ERROR }} â"

         - name: Log successful Slack channel creation
           if: success()
           uses: port-labs/port-github-action@v1
           env:
             SLACK_CHANNEL_URL: https://slack.com/app_redirect?channel=${{ steps.create-slack-channel.outputs.SLACK_CHANNEL_ID }}
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             baseUrl: https://api.port.io
             operation: PATCH_RUN
             runId: ${{ fromJson(github.event.inputs.port_payload).run.id }}
             logMessage: |
               Channel created successfully - ${{ env.SLACK_CHANNEL_URL }} â

         - name: Send Slack Message
           uses: archive/github-actions-slack@v2.9.0
           env:
             SVC_ENTITY_URL: https://app.getport.io/serviceEntity?identifier=${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}
             SVC_ENTITY_TITLE: ${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}
           id: send-message
           with:
             slack-function: send-message
             slack-bot-user-oauth-access-token: ${{ secrets.BOT_USER_OAUTH_TOKEN }}
             slack-channel: ${{ steps.create-slack-channel.outputs.SLACK_CHANNEL_ID }}
             slack-text: | 
               :rotating_light: New Incident reported - ${{ env.PD_INCIDENT_TITLE }} :rotating_light:
                 Urgency: `${{ fromJson(inputs.port_payload).event.diff.after.properties.urgency }}`
                 Service: <${{ env.SVC_ENTITY_URL }}|${{ env.SVC_ENTITY_TITLE }}>
                 Manage incident :point_right::skin-tone-4: <${{ env.PORT_INCIDENT_URL }}|here>!

                 Please use this Slack channel to report any updates, ideas, or root-cause ideas related to this incident :thread:

         - name: Update incident entity with new information
           uses: port-labs/port-github-action@v1
           env:
             SLACK_CHANNEL_URL: https://slack.com/app_redirect?channel=${{ steps.create-slack-channel.outputs.SLACK_CHANNEL_ID }}
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             identifier: ${{ env.PD_INCIDENT_ID }}
             baseUrl: https://api.port.io
             blueprint: pagerdutyIncident
             properties: |
               {
                 "slack_channel": "${{ env.SLACK_CHANNEL_URL }}"
               }
             relations: | 
               {
                 "githubIssue": "${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}-${{ steps.create-github-issue.outputs.number }}",
                 "service": "${{ steps.get-service-info.outputs.SERVICE_IDENTIFIER }}"
               }

         - name: Log Successful Action
           if: success()
           uses: port-labs/port-github-action@v1
           with:
             clientId: ${{ secrets.PORT_CLIENT_ID }}
             clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
             baseUrl: https://api.port.io
             operation: PATCH_RUN
             runId: ${{ fromJson(github.event.inputs.port_payload).run.id }}
             logMessage: |
               Done handling the new incident ðªð»
   ```

   Selecting a Port API URL by account region

   The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

   * **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
   * **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Set up automation[â](#set-up-automation "Direct link to Set up automation")

Now we need to create an automation in Port that will trigger our GitHub workflow whenever a new PagerDuty incident is created.

### Create the incident management automation

1. Navigate to your [Automations](https://app.getport.io/settings/automations) page.

2. Click on the `+ New automation` button.

3. Copy and paste the following automation configuration:

   **Incident management automation (Click to expand)**

   This automation will be triggered when a new `pagerdutyIncident` entity is created.

   **Replace the `org` value with your GitHub organization name, and the `repo` value with your GitHub repository.**

   Create in Port

   ```
   {
     "identifier": "handle_new_incident",
     "title": "Handle new PagerDuty incident",
     "icon": "pagerduty",
     "description": "Create Slack channel for incident troubleshooting, and GitHub issue for documentation",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_CREATED",
         "blueprintIdentifier": "pagerdutyIncident"
       }
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB ORG>",
       "repo": "<GITHUB REPOSITORY>",
       "workflow": "handle-incident.yaml",
       "workflowInputs": {
         "port_payload": "{{ . }}"
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false,
     "publish": true
   }
   ```

4. Click `Save` to create the automation.

## Let's test it[â](#lets-test-it "Direct link to Let's test it")

1. Go to your PagerDuty account.

2. Create a new PagerDuty incident.

3. Navigate to the [runs audit page](https://app.getport.io/settings/AuditLog?activeTab=4).

4. Look for `Handle new PagerDuty incident` automation run.

5. Go back to your [PagerDuty Incidents](https://app.getport.io/pagerdutyIncidents) page.

6. Click on the incident entity you created.

7. Verify that the `Slack Channel URL` property and `GitHub Issue` relation are populated.

   ![](/img/guides/slackIncidentGuide/updatedIncidentEntity.png)

## Summary[â](#summary "Direct link to Summary")

Using Port as the automation orchestrator, we've created a comprehensive incident management flow that automatically:

* Creates a dedicated Slack channel for each incident
* Sends immediate notifications to team members
* Creates a GitHub issue for documentation and tracking
* Updates the incident entity with all relevant links and information

This automation enables faster notification and response times when handling new incidents, while providing a centralized place to track the troubleshooting process and maintain communication.

## Next steps[â](#next-steps "Direct link to Next steps")

This guide provides a solid foundation for automated incident management. You can enhance it further by:

* **Adding incident resolution workflows**: Create a DAY-2 `Resolve incident` Port action that resolves the GitHub issue and sends updates to the Slack channel
* **Implementing urgency filtering**: Filter the automation trigger to only run for high-urgency incidents
* **Adding team notifications**: Automatically add service owners and on-call engineers to the Slack channel
* **Creating incident dashboards**: Build dashboards to visualize incident metrics and response times
* **Integrating with other tools**: Extend the workflow to create Jira tickets, send email notifications, or update status pages

For more advanced incident management workflows, check out the [resolve PagerDuty incident guide](/guides/all/resolve-pagerduty-incident.md).
