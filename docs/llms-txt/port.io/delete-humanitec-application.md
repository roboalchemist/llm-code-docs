# Source: https://docs.port.io/guides/all/delete-humanitec-application.md

# Delete Application In Humanitec

## Overview[â](#overview "Direct link to Overview")

This self service guide provides a comprehensive walkthrough on how to delete an application in Humanitec from Port using Port's self service actions.

Prerequisites

1. [Port's GitHub app](https://github.com/apps/getport-io) needs to be installed.

2. In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

   <!-- -->

   * `HUMANITEC_API_KEY` - [Humanitec API Key](https://developer.humanitec.com/platform-orchestrator/reference/api-references/#authentication)
   * `HUMANITEC_ORG_ID` - [Humanitec Organization ID](https://developer.humanitec.com/concepts/organizations/)
   * `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
   * `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

3. Optional - Install Port's Humanitec integration [learn more](/guides/all/humanitec-integration.md)

Humanitec Integration

This step is not required for this example, but it will create all the blueprint boilerplate for you, and also ingest and update the catalog in real time with your Humanitec Application.

**Humanitec Application Blueprint (Click to expand)**

Create in Port

```
{
  "identifier": "humanitecApplication",
  "description": "Humanitec Application",
  "title": "humanitecApplication",
  "icon": "Apps",
  "schema": {
    "properties": {
      "createdAt": {
        "type": "string",
        "title": "Created At",
        "format": "date-time"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

## GitHub Workflow[â](#github-workflow "Direct link to GitHub Workflow")

Create the file `.github/workflows/delete-humanitec-application.yaml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

GitHub Workflow

delete-humanitec-application.yaml

```
name: Delete Humanitec Application
on:
  workflow_dispatch:
    inputs:
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  delete-application:
    runs-on: ubuntu-latest
    steps:
      - name: Delete Application
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.humanitec.io/orgs/${{secrets.HUMANITEC_ORG_ID}}/apps/${{fromJson(inputs.port_context).entity}}'
          method: 'DELETE'
          customHeaders: '{"Content-Type": "application/json", "Authorization": "Bearer ${{ secrets.HUMANITEC_API_KEY }}"}'

      - name: Log Delete Application Request Failure 
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Request to delete application failed ..."

      - name: Log Delete Application Request Success
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
             Humanitech application has been successfully deleted! â
             Deleting entity from port

      - name: Get Port Token
        id: port_access_token
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.port.io/v1/auth/access_token'
          method: 'POST'
          customHeaders: '{"Content-Type": "application/json", "accept": "application/json"}'
          data: |
            {
              "clientId": "${{ secrets.PORT_CLIENT_ID }}",
              "clientSecret": "${{ secrets.PORT_CLIENT_SECRET }}"
            }
          
      - name: Delete Application From Port
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.port.io/v1/blueprints/${{fromJson(inputs.port_context).blueprint}}/entities/${{fromJson(inputs.port_context).entity}}?delete_dependents=false'
          method: 'DELETE'
          customHeaders: '{"Content-Type": "application/json", "Authorization": "Bearer ${{ fromJson(steps.port_access_token.outputs.response).accessToken }}"}'
  
      - name: Log Delete Application From Port Request Failure 
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Request to delete application failed ..."
          
      - name: Log Delete Application Entity From Port
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
              Application has been successfully deleted from port â
```

## Port Configuration[â](#port-configuration "Direct link to Port Configuration")

Create a new self service action using the following JSON configuration.

**Delete application In Humanitec (click to expand)**

Modification Required

Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

Create in Port

```
{
  "identifier": "delete_application",
  "title": "Delete Application",
  "icon": "Microservice",
  "description": "Delete an application on humanitec",
  "trigger": {
    "type": "self-service",
    "operation": "DELETE",
    "userInputs": {
      "properties": {},
      "required": [],
      "order": []
    },
    "blueprintIdentifier": "humanitecApplication"
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<GITHUB_ORG>",
    "repo": "<GITHUB_REPO>",
    "workflow": "delete-humanitec-application.yaml",
    "workflowInputs": {
      "port_context": {
        "entity": "{{.entity.identifier}}",
        "blueprint": "{{.action.blueprint}}",
        "run_id": "{{.run.id}}",
        "relations": "{{.entity.relations}}"
      }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

Now you should see the `Delete Application` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Go to the [Self Service page](https://app.getport.io/self-serve) of your portal.
2. Click on the `Delete Application` action
3. Choose the humanitec application you want to delete (In case you didn't install the [Humanitec integration](/guides/all/humanitec-integration.md), it means you don't have any Humanitec applications in Port yet, so you will need to create one manually in Port to test this action)
4. Click on `Execute`
5. Done! wait for the application to be deleted in Humanitec

## More Self Service Humanitec Actions Examples[â](#more-self-service-humanitec-actions-examples "Direct link to More Self Service Humanitec Actions Examples")

* [Create Humanitec application](/guides/all/create-humanitec-application.md)
* [Deploy Humanitec application](/guides/all/deploy-humanitec-application.md)
