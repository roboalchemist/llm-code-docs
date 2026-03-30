# Source: https://docs.port.io/guides/all/tag-azure-resource.md

# Add Tags to Azure Resource

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

* GitHub (Legacy)
* GitHub (Ocean)

In the following guide, you are going to create a self-service action in Port that executes a [GitHub workflow](/actions-and-automations/setup-backend/github-workflow/.md) to add tags to a [storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview).

In the following guide, you are going to create a self-service action in Port that executes a [GitHub workflow](/actions-and-automations/setup-backend/github-ocean/.md) to add tags to a [storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview).

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

Organize and manage your Azure resources effectively by adding tags directly through Port.

* **Cost Accounting**: Categorize resources by department, project, or cost center for accurate billing analysis.
* **Governance**: Label resources based on criticality, compliance requirements, or ownership.
* **Search & Filtering**: Use tags to link the azure resource to other objects in your Port account. :::

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. **Azure Subscription**: An active Azure subscription is required to deploy the storage account.

2. **Port Actions Knowledge**: Understanding how to create and use Port actions is necessary. Learn the basics [here](https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/).

3. Install the GitHub integration relevant to you:

   * GitHub (Legacy)
   * GitHub (Ocean)

   Install Port's GitHub app by clicking [here](https://github.com/apps/getport-io/installations/new).

   Install [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

4. **GitHub Repository**: A repository to store your GitHub workflow file for this action.

### GitHub Secrets[â](#github-secrets "Direct link to GitHub Secrets")

To successfully execute this workflow, we will add the following secrets to the GitHub repository containing the workflow:

**1. GitHub Action Secrets**

* Navigate to your GitHub repository's "Settings" tab.

* Select "Secrets" and then "Actions" from the side menu.

* Create the following secrets:

  <!-- -->

  * `PORT_CLIENT_ID`: Your Port Client ID [learn more](https://docs.port.io/build-your-software-catalog/custom-integration/api/#get-api-token).
  * `PORT_CLIENT_SECRET`: Your Port Client Secret [learn more](https://docs.port.io/build-your-software-catalog/custom-integration/api/#get-api-token).

**2. Azure Cloud Credentials**

**Important**:

For secure Azure interactions, we'll use a Service Principal. If you need help creating one, follow this [guide](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-cloud-shell-bash?tabs=bash#create-a-service-principal)

* Once you have your Service Principal, create these GitHub Action secrets:

  <!-- -->

  * `ARM_CLIENT_ID`: Service Principal Application (Client) ID
  * `ARM_CLIENT_SECRET`: Service Principal Password
  * `ARM_SUBSCRIPTION_ID`: Your Azure Subscription ID
  * `ARM_TENANT_ID`: Your Azure [Tenant ID](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id)

## Port Configuration[â](#port-configuration "Direct link to Port Configuration")

Import Azure Resources

Import Azure resources into your Port account using the [Azure Exporter](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/.md)

1. Create the `azureStorage` blueprint.

   <!-- -->

   * Head to the [Builder](https://app.getport.io/settings/data-model) page.
   * Click on the `+ Blueprint` button.
   * Click on the `{...} Edit JSON` button.
   * Copy and paste the following JSON configuration into the editor.

Port Blueprint: Azure Storage Account

note

Keep in mind that this can be any blueprint you require; the provided example is just for reference.

Create in Port

```
{
    "identifier": "azureStorage",
    "title": "Azure Storage Account",
    "icon": "Azure",
    "schema": {
        "properties": {
            "storage_name": {
                "title": "Account Name",
                "type": "string",
                "minLength": 3,
                "maxLength": 63,
                "icon": "DefaultProperty"
            },
            "storage_location": {
                "icon": "DefaultProperty",
                "title": "Location",
                "type": "string"
            },
            "url": {
                "title": "URL",
                "format": "url",
                "type": "string",
                "icon": "DefaultProperty"
            }
        },
        "required": [
            "storage_name",
            "storage_location"
        ]
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "relations": {}
}
```

<br />

2. To create the Port action:

   <!-- -->

   * Head to the [self-service](https://app.getport.io/self-serve) page.
   * Click on the `+ New Action` button.
   * Click on the `{...} Edit JSON` button.
   * Copy and paste the following JSON configuration into the editor.

Port Action: Add Tags to Azure Storage

tip

* `<GITHUB-ORG>` - your GitHub organization or user name.
* `<GITHUB-REPO-NAME>` - your GitHub repository name.
* `<GITHUB_OCEAN_INSTALLATION_ID>` - your GitHub ocean installation id (only relevant if you use GitHub ocean).

- GitHub (Legacy)
- GitHub (Ocean)

Create in Port

```
{
  "identifier": "service_add_tags_to_azure_storage",
  "title": "Add Tags to Azure Storage",
  "icon": "Azure",
  "description": "Add tags to azure storage account",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "userInputs": {
      "properties": {
        "tags": {
          "title": "Tags",
          "type": "object"
        }
      },
      "required": [
        "tags"
      ],
      "order": []
    },
    "blueprintIdentifier": "azureStorage"
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<GITHUB-ORG>",
    "repo": "<GITHUB-REPO-NAME>",
    "workflow": "tag-azure-resource.yml",
    "workflowInputs": {
      "tags": "{{ .inputs.\"tags\" }}",
      "port_context": {
        "entity": "{{ .entity }}",
        "blueprint": "{{ .action.blueprint }}",
        "runId": "{{ .run.id }}",
        "trigger": "{{ .trigger }}"
      }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

Create in Port

```
{
  "identifier": "service_add_tags_to_azure_storage",
  "title": "Add Tags to Azure Storage",
  "icon": "Azure",
  "description": "Add tags to azure storage account",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "userInputs": {
      "properties": {
        "tags": {
          "title": "Tags",
          "type": "object"
        }
      },
      "required": [
        "tags"
      ],
      "order": []
    },
    "blueprintIdentifier": "azureStorage"
  },
  "invocationMethod": {
    "type": "INTEGRATION_ACTION",
    "installationId": "<GITHUB_OCEAN_INSTALLATION_ID>",
    "integrationActionType": "dispatch_workflow",
    "org": "<GITHUB-ORG>",
    "repo": "<GITHUB-REPO-NAME>",
    "workflow": "tag-azure-resource.yml",
    "workflowInputs": {
      "tags": "{{ .inputs.\"tags\" }}",
      "port_context": {
        "entity": "{{ .entity }}",
        "blueprint": "{{ .action.blueprint }}",
        "runId": "{{ .run.id }}",
        "trigger": "{{ .trigger }}"
      }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

## GitHub Workflow[â](#github-workflow "Direct link to GitHub Workflow")

* Terraform
* Azure CLI

3. Update the following Terraform templates in the `terraform` folder at the root of your GitHub repository:

   tip

   Fork our [example repository](https://github.com/port-labs/pipelines-terraform-azure) to get started.

   1. `main.tf` - Include a tags field within the configuration of the storage account resource.
   2. `variables.tf` â Introduce a new variable named `resource_tags`.

**main.tf**

main.tf

```
...

resource "azurerm_storage_account" "storage_account" {
    name                = var.storage_account_name
    resource_group_name = var.resource_group_name

    location                 = var.location
    account_tier             = "Standard"
    account_replication_type = "LRS"
    account_kind             = "StorageV2"
    tags                     = var.resource_tags
}

...
```

**variables.tf**

variables.tf

```
// ...
variable "resource_tags" {
  type = map(string)
  default = {
    Environment = "Production"
  }
}
// ...
```

<br />

4. Create a workflow file under `.github/workflows/tag-azure-resource.yml` with the following content:

GitHub workflow script

note

Replace the following variables for the `terraform init` step:

1. `RESOURCE_GROUP_NAME` with a resource group from your Azure account. Check this [guide](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) to find your resource groups.
2. `STORAGE_ACCOUNT_NAME`: The storage account containing.
3. `TF_STATE_CONTAINER`: The name of the container used for storing the Terraform state files.
4. `TF_STATE_KEY`: Indicate the key that uniquely identifies the configuration file.

tag-azure-resource.yml

```
name: "Tag Azure Resource"

on: 
  workflow_dispatch:
    inputs:
      tags:
        required: true
        type: string
      port_context:
        required: true
        type: string
        description: >-
          Action and general context (blueprint, run id, etc...)

env: 
  TF_LOG: INFO
  TF_INPUT: false

jobs:
  terraform:
    name: "Add Tags to Azure Resource"
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
        working-directory: ./terraform

    steps:
      - name: Inform starting of action
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          logMessage: |
            Starting a GitHub workflow to tag the Azure resource: ${{ fromJson(inputs.port_context).entity.identifier }} ... â´ï¸

      - name: Checkout the repository to the runner
        uses: actions/checkout@v4

      - name: Setup Terraform with specified version on the runner
        uses: hashicorp/setup-terraform@v2
        with:
          terraform_version: 1.6.0
      
      - name: Terraform init
        id: init
        env:
          ARM_CLIENT_ID: ${{ secrets.ARM_CLIENT_ID }}
          ARM_CLIENT_SECRET: ${{ secrets.ARM_CLIENT_SECRET }}
          ARM_TENANT_ID: ${{ secrets.ARM_TENANT_ID }}
          ARM_SUBSCRIPTION_ID: ${{ secrets.ARM_SUBSCRIPTION_ID }}
          RESOURCE_GROUP_NAME: YourResourceGroup
          STORAGE_ACCOUNT_NAME: YourStorageAccount
          TF_STATE_CONTAINER: tfstate
          TF_STATE_KEY: terraform.tfstate
        run: |
          terraform init \
            -backend-config="resource_group_name=$RESOURCE_GROUP_NAME" \
            -backend-config="storage_account_name=$STORAGE_ACCOUNT_NAME" \
            -backend-config="container_name=$TF_STATE_CONTAINER" \
            -backend-config="key=$TF_STATE_KEY" \
            -input=false

      - name: Terraform format
        id: fmt
        run: terraform fmt -check
      
      - name: Terraform validate
        id: validate
        run: terraform validate

      - name: Run Terraform Plan and Apply (Azure)
        id: plan-azure
        env: 
            ARM_CLIENT_ID: ${{ secrets.ARM_CLIENT_ID }}
            ARM_CLIENT_SECRET: ${{ secrets.ARM_CLIENT_SECRET }}
            ARM_TENANT_ID: ${{ secrets.ARM_TENANT_ID }}
            ARM_SUBSCRIPTION_ID: ${{ secrets.ARM_SUBSCRIPTION_ID }}
            TF_VAR_port_client_id: ${{ secrets.PORT_CLIENT_ID }}
            TF_VAR_port_client_secret: ${{ secrets.PORT_CLIENT_SECRET }}
            TF_VAR_port_run_id: ${{ fromJson(inputs.port_context).runId }}
            TF_VAR_storage_account_name: ${{ fromJson(inputs.port_context).entity.identifier }}
            TF_VAR_resource_tags: ${{ github.event.inputs.tags }}
        run: |
          terraform plan \
            -input=false \
            -out=tfazure-${GITHUB_RUN_NUMBER}.tfplan

          terraform apply -auto-approve -input=false tfazure-${GITHUB_RUN_NUMBER}.tfplan

      - name: Create a failure log message
        if: steps.plan-azure.outcome == 'failure'
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).runId}}
          logMessage: Failed to tag azure resource ${{ fromJson(inputs.port_context).entity.identifier }}


      - name: Create a log message
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).runId}}
          logMessage: Added tags to ${{ fromJson(inputs.port_context).entity.identifier }}
```

3. Create a GitHub Action secret `AZURE_CREDENTIALS` with the value like below: (Refer to [Using secrets in GitHub Actions](https://github.com/Azure/login?tab=readme-ov-file#login-with-a-service-principal-secret:~:text=below%3A%20\(Refer%20to-,Using%20secrets%20in%20GitHub%20Actions,-.\)).)

```
AZURE_CREDENTIALS = {
  "clientSecret":  "******",
  "subscriptionId":  "******",
  "tenantId":  "******",
  "clientId":  "******"
}
```

4. Create a workflow file under `.github/workflows/tag-azure-resource.yml` with the following content:

GitHub workflow script

note

Replace the `RESOURCE_GROUP_NAME` with a resource group from your Azure account. Check this [guide](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) to find your resource groups.

tag-azure-resource.yml

```
name: "Tag Azure Resource CLI"

on: 
  workflow_dispatch:
    inputs:
      tags:
        required: true
        type: string
      port_context:
        required: true
        description:
            Details for who triggered the action and general context (blueprint, run id, etc...)
        type: string


jobs:
    build-and-deploy:
      runs-on: ubuntu-latest
      steps:
  
      - name: Inform starting of action
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          logMessage: |
            Starting a GitHub workflow to tag the Azure resource: ${{fromJson(inputs.port_context).entity.identifier}} ... â´ï¸

  
      - uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
  
      - name: Azure CLI script
        uses: azure/CLI@v1
        env: 
          RESOURCE_GROUP: YourResourceGroup
          STORAGE_NAME: ${{ fromJson(inputs.port_context).entity.identifier }}
          TAGS: ${{ github.event.inputs.tags }}
        with:
          azcliversion: latest
          inlineScript: |
            az account show
            resource=$(az resource show -g ${RESOURCE_GROUP} -n ${STORAGE_NAME} --resource-type Microsoft.Storage/storageAccounts --query "id" --output tsv)
            tags=$(echo ${TAGS} | jq -r 'to_entries|map("\(.key)=\(.value|tojson)")|join(" ")')
            az tag create --resource-id $resource --tags $tags

      - name: Create a log message
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).runId}}
          logMessage: Added tags to ${{fromJson(inputs.port_context).entity.identifier}}
```

## Let's Test It\![â](#lets-test-it "Direct link to Let's Test It!")

* On the [self-service](https://app.getport.io/self-serve) page, select the action and fill in the properties.
* Click the execute button to trigger the GitHub workflow.

## More relevant guides[â](#more-relevant-guides "Direct link to More relevant guides")

1. [Add tags to S3 Bucket](/guides/all/add-tags-to-s3-bucket.md)
2. [Add tags to ECR Repository](/guides/all/add-tags-to-ecr-repository.md)
