# Source: https://docs.port.io/guides/all/create-workload-profile.md

# Create Workload Profile

## Overview[â](#overview "Direct link to Overview")

This self service guide provides a comprehensive walkthrough on how to create a workload profile in Humanitec from Port using Port's self service actions.

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

This step is not required for this example, but it will create all the blueprint boilerplate for you, and also ingest and update the catalog in real time with your Humanitec Workload Profile.

**Humanitec Workload Blueprint (Click to expand)**

Create in Port

```

{
  "identifier": "humanitecWorkload",
  "title": "Workload",
  "icon": "Cluster",
  "schema": {
    "properties": {
      "class": {
        "title": "Class",
        "description": "The class of the workload",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "driverType": {
        "title": "Driver Type",
        "description": "The driver type of the workload",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "definitionId": {
        "title": "Definition ID",
        "description": "The definition ID of the workload",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "definitionVersionId": {
        "title": "Definition Version ID",
        "description": "The definition version ID of the workload",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "status": {
        "title": "Status",
        "description": "The status of the workload",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "updatedAt": {
        "title": "Update Date",
        "description": "The date and time when the workload was last updated",
        "type": "string",
        "format": "date-time",
        "icon": "DefaultProperty"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "humanitecEnvironment": {
      "title": "Environment",
      "target": "humanitecEnvironment",
      "required": false,
      "many": false
    }
  }
}
```

## GitHub Workflow[â](#github-workflow "Direct link to GitHub Workflow")

Create the file `.github/workflows/create-humanitec-workload-profile.yaml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

GitHub Workflow

create-humanitec-workload-profile.yaml

```
name: Create Humanitec Workload Profile
on:
  workflow_dispatch:
    inputs:
      id:
        description: 'The workload profile ID'
        required: true
        type: string
      spec_definition:
        description: 'Workload specification definition'
        required: true
      workload_profile_chart_id:
        description: 'Workload Profile Chart ID'
        required: true
        type: string
      workload_profile_chart_version:
        description: 'Workload Profile Chart Version'
        required: true
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  create-workload-profile:
    runs-on: ubuntu-latest
    steps:
      - name: Create Workload Profile
        id : create_workload_profile
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.humanitec.io/orgs/${{secrets.HUMANITEC_ORG_ID}}/workload-profiles'
          method: 'POST'
          customHeaders: '{"Content-Type": "application/json", "Authorization": "Bearer ${{ secrets.HUMANITEC_API_KEY }}"}'
          data: >-
            {
              "id": "${{ github.event.inputs.id }}",
              "spec_definition": ${{ github.event.inputs.spec_definition }},
              "workload_profile_chart": {
                "id": "${{ github.event.inputs.workload_profile_chart_id }}",
                "version": "${{ github.event.inputs.workload_profile_chart_version }}"
                }
              }
          
      - name: Log Create Workload Profile Request Failure 
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Request to create workload profile failed ..."
          
      - name: Log Request Success
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
             Humanitech workload profile created! â
             Reporting created entity to port ... ð´ââï¸

      - name: UPSERT Humanitec Workload Profile
        uses: port-labs/port-github-action@v1
        with:
          identifier: "${{ fromJson(steps.create_workload_profile.outputs.response).id }}" 
          title: "${{ fromJson(steps.create_workload_profile.outputs.response).id }}"
          icon: Microservice
          blueprint: "${{fromJson(inputs.port_context).blueprint}}"
          properties: |-
            {
              "description": "${{ fromJson(steps.create_workload_profile.outputs.response).description }}",
              "version": "${{ fromJson(steps.create_workload_profile.outputs.response).version }}",
              "createdAt": "${{ fromJson(steps.create_workload_profile.outputs.response).created_at }}",
              "specDefinition": ${{ toJson(fromJson(steps.create_workload_profile.outputs.response).spec_definition) }}
            }
          relations: "{}"
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: UPSERT
          runId: ${{fromJson(inputs.port_context).run_id}}

      - name: Log After Upserting Entity
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
              Upserting was successful â
```

## Port Configuration[â](#port-configuration "Direct link to Port Configuration")

Create a new self service action using the following JSON configuration.

**Create Workload Profile (click to expand)**

Modification Required

Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

Create in Port

```
{
  "identifier": "create_workload_profile",
  "title": "Create Workload Profile",
  "icon": "Cluster",
  "description": "Create a workload profile in humanitec",
  "trigger": {
    "type": "self-service",
    "operation": "CREATE",
    "userInputs": {
      "properties": {
        "spec_definition": {
          "icon": "DefaultProperty",
          "type": "object",
          "title": "Spec Definition",
          "description": "Workload spec definition"
        },
        "workload_profile_chart_id": {
          "type": "string",
          "title": "Workload Profile Chart ID",
          "description": "Workload Profile Chart ID"
        },
        "workload_profile_chart_version": {
          "type": "string",
          "title": "Workload Profile Chart Version",
          "description": "Workload profile chart version. References a workload profile chart."
        },
        "workload_profile_id": {
          "type": "string",
          "title": "Workload Profile Id",
          "description": "Workflow profile ID",
          "icon": "Cluster"
        }
      },
      "required": [
        "workload_profile_chart_id",
        "workload_profile_chart_version",
        "spec_definition"
      ],
      "order": [
        "workload_profile_id",
        "spec_definition",
        "workload_profile_chart_id",
        "workload_profile_chart_version"
      ]
    },
    "blueprintIdentifier": "humanitecWorkload"
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<GITHUB_ORG>",
    "repo": "<GITHUB_REPO>",
    "workflow": "create-workload-profile.yaml",
    "workflowInputs": {
      "id": "{{ .inputs.\"id\" }}",
      "spec_definition": "{{ .inputs.\"spec_definition\" }}",
      "workload_profile_chart_id": "{{ .inputs.\"workload_profile_chart_id\" }}",
      "workload_profile_chart_version": "{{ .inputs.\"workload_profile_chart_version\" }}",
      "port_context": {
        "entity": "{{.entity.identifier}}",
        "blueprint": "{{.action.blueprint}}",
        "run_id": "{{.run.id}}"
      }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

Now you should see the `Create Workload Profile` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Go to the [Self Service page](https://app.getport.io/self-serve) of your portal.
2. Click on the `Create Workload Profile` action
3. Enter the required details for `Workload Profile ID`, `Spec Definition`, `Workload Profile Chart ID`,and `Workload Profile Chart Version`.
4. Click on `Execute`
5. Done! wait for the workload profile to be created in Humanitec

## More Self Service Humanitec Actions Examples[â](#more-self-service-humanitec-actions-examples "Direct link to More Self Service Humanitec Actions Examples")

* [Create Humanitec application](/guides/all/create-humanitec-application.md)
* [Deploy Humanitec application](/guides/all/deploy-humanitec-application.md)
* [Delete Humanitec application](/guides/all/delete-humanitec-application.md)
