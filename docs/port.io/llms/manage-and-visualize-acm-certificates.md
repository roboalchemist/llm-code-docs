# Source: https://docs.port.io/guides/all/manage-and-visualize-acm-certificates.md

# Manage and visualize your ACM certificates

This guide demonstrates how to bring your AWS ACM certificate management experience into Port. You will learn how to:

* Ingest ACM certificate data into Port's software catalog using **Port's AWS** integration.
* Set up **self-service actions** to manage ACM certificates (request new certificates, renew certificates, and delete certificates).
* Build **dashboards** in Port to monitor and take action on your ACM resources.

![](/img/guides/acmDashboard1.png) ![](/img/guides/acmDashboard2.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Monitor the status and expiration of all ACM certificates across accounts from a single view.
* Empower platform teams to automate certificate lifecycle management via GitHub workflows.
* Streamline certificate requests and renewals through self-service actions.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [AWS integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/) is installed in your account.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

When installing the AWS integration in Port, the `AWS Account` blueprint is created by default.<br /><!-- -->However, the `ACM Certificate` blueprint is not created automatically so we will need to create it manually.

### Create the ACM certificate blueprint[â](#create-the-acm-certificate-blueprint "Direct link to Create the ACM certificate blueprint")

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add this JSON schema:

   **AWS ACM Certificate blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "acmCertificate",
     "description": "This blueprint represents an SSL/TLS certificates for your Amazon Web Services-based websites and applications",
     "title": "ACM Certificate",
     "icon": "AWS",
     "schema": {
       "properties": {
         "createdAt": {
           "icon": "DefaultProperty",
           "type": "string",
           "title": "Created At",
           "format": "date-time"
         },
         "inUse": {
           "icon": "DefaultProperty",
           "type": "boolean",
           "title": "In Use"
         },
         "keyAlgorithm": {
           "icon": "DefaultProperty",
           "type": "string",
           "title": "Key Algorithm"
         },
         "expirationDate": {
           "type": "string",
           "title": "Expiration Date",
           "format": "date-time"
         },
         "renewalEligibility": {
           "icon": "DefaultProperty",
           "title": "Renewal Eligibility",
           "type": "string",
           "enum": [
             "ELIGIBLE",
             "INELIGIBLE"
           ],
           "enumColors": {
             "ELIGIBLE": "green",
             "INELIGIBLE": "red"
           }
         },
         "status": {
           "icon": "DefaultProperty",
           "title": "Status",
           "type": "string",
           "enum": [
             "ISSUED",
             "EXPIRED",
             "PENDING_VALIDATION",
             "INACTIVE",
             "FAILED",
             "REVOKED",
             "VALIDATION_TIMED_OUT"
           ],
           "enumColors": {
             "ISSUED": "green",
             "EXPIRED": "red",
             "PENDING_VALIDATION": "lightGray",
             "INACTIVE": "red",
             "FAILED": "red",
             "REVOKED": "gold",
             "VALIDATION_TIMED_OUT": "gold"
           }
         },
         "type": {
           "icon": "DefaultProperty",
           "type": "string",
           "title": "Type"
         },
         "arn": {
           "type": "string",
           "title": "Arn"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "account": {
         "title": "Account",
         "target": "awsAccount",
         "required": false,
         "many": false
       }
     }
   }
   ```

5. Click `Save` to create the blueprint.

### Update the integration mapping[â](#update-the-integration-mapping "Direct link to Update the integration mapping")

1. Go to the [Data Sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Select the AWS integration.

3. Add the following YAML block into the editor to ingest ACM certificates from your AWS account:

   **AWS integration configuration (Click to expand)**

   ```
   deleteDependentEntities: true
   createMissingRelatedEntities: true
   enableMergeEntity: true
   resources:
     - kind: AWS::Organizations::Account
       selector:
         query: 'true'
       port:
         entity:
           mappings:
             identifier: .Id
             title: .Name
             blueprint: '"awsAccount"'
             properties:
               arn: .Arn
               email: .Email
               status: .Status
               joined_method: .JoinedMethod
               joined_timestamp: .JoinedTimestamp | sub(" "; "T")
     - kind: AWS::ACM::Certificate
       selector:
         query: 'true'
       port:
         entity:
           mappings:
             identifier: .CertificateArn
             title: .DomainName
             blueprint: '"acmCertificate"'
             properties:
               status: .Status
               type: .Type
               arn: .CertificateArn
               renewalEligibility: .RenewalEligibility
               keyAlgorithm: .KeyAlgorithm
               inUse: .InUse
               createdAt: .CreatedAt
               expirationDate: .NotAfter
             relations:
               account: .__AccountId
   ```

4. Click `Save & Resync` to apply the mapping.

## Set up self-service actions[â](#set-up-self-service-actions "Direct link to Set up self-service actions")

Now let us create self-service actions to manage your ACM certificates directly from Port using GitHub Actions. You will implement workflows to:

1. Request a new ACM certificate.
2. Renew an eligible ACM certificate.
3. Delete an ACM certificate.

To implement these use-cases, follow the steps below:

### Add GitHub secrets

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `PORT_CLIENT_ID` - Port Client ID [learn more](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#get-api-token).
* `PORT_CLIENT_SECRET` - Port Client Secret [learn more](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#get-api-token).
* `AWS_ACCESS_KEY_ID` - AWS IAM user's access key.
* `AWS_SECRET_ACCESS_KEY` - AWS IAM user's secret access key.
* `AWS_REGION` - AWS region (e.g., `us-east-1`).

Required permissions

The AWS IAM user must have the following permissions to manage ACM certificates:

* `acm:RequestCertificate`
* `acm:RenewCertificate`
* `acm:DeleteCertificate`

### Request a new ACM certificate[â](#request-a-new-acm-certificate "Direct link to Request a new ACM certificate")

#### Add GitHub workflow

Create the file `.github/workflows/request-acm-cert.yaml` in the `.github/workflows` folder of your repository.

**Request ACM Certificate GitHub workflow (Click to expand)**

```
name: Request ACM Certificate

on:
  workflow_dispatch:
    inputs:
      domain_name:
        required: true
        description: 'The fully qualified domain name (FQDN) that you want to secure with an ACM certificate'
        type: string
      validation_method:
        required: true
        description: 'The method you want to use to validate that you own or control domain'
        type: string
      port_context:
        required: true
        description: 'Action and general context (blueprint, entity, run id, etc...)'
        type: string

jobs:
  request-acm:
    runs-on: ubuntu-latest
    steps:
      - name: Inform Port of workflow start
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).runId}}
          logMessage: Configuring AWS credentials to request public ACM cert with domain name ${{ inputs.domain_name }}

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Request ACM certificate
        run: aws acm request-certificate --domain-name ${{ inputs.domain_name }} --validation-method ${{ inputs.validation_method }}

      - name: Inform Port about ACM certificate success
        if: success()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'SUCCESS'
          logMessage: â ACM certificate for domain ${{ inputs.domain_name }} requested successfully
          summary: ACM certificate requested successfully

      - name: Inform Port about ACM certificate failure
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'FAILURE'
          logMessage: â Failed to request ACM certificate for domain ${{ inputs.domain_name }}
          summary: ACM certificate request failed
```

#### Create Port action

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Request ACM Certificate action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "request_acm_certificate",
     "title": "Request ACM Certificate",
     "icon": "AWS",
     "description": "Requests an ACM certificate for use with other Amazon Web Services services",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "domain_name": {
             "icon": "DefaultProperty",
             "type": "string",
             "title": "Domain Name",
             "description": "The fully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate"
           },
           "validation_method": {
             "icon": "DefaultProperty",
             "title": "Validation Method",
             "description": "The method you want to use if you are requesting a public certificate to validate that you own or control domain",
             "type": "string",
             "default": "DNS",
             "enum": [
               "EMAIL",
               "DNS"
             ],
             "enumColors": {
               "EMAIL": "lightGray",
               "DNS": "lightGray"
             }
           }
         },
         "required": [
           "domain_name",
           "validation_method"
         ],
         "order": [
           "domain_name",
           "validation_method"
         ]
       }
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB-ORG>",
       "repo": "<GITHUB-REPO>",
       "workflow": "request-acm-cert.yaml",
       "workflowInputs": {
         "{{ spreadValue() }}": "{{ .inputs }}",
         "port_context": {
           "runId": "{{ .run.id }}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Request ACM Certificate` action in the self-service page. ð

### Renew an ACM certificate[â](#renew-an-acm-certificate "Direct link to Renew an ACM certificate")

#### Add GitHub workflow

Create the file `.github/workflows/renew-acm-cert.yaml` in the `.github/workflows` folder of your repository.

**Renew ACM Certificate GitHub workflow (Click to expand)**

```
name: Renew ACM Certificate

on:
  workflow_dispatch:
    inputs:
      port_context:
        required: true
        description: 'Action and general context (blueprint, entity, run id, etc...)'
        type: string

jobs:
  renew-acm-cert:
    runs-on: ubuntu-latest
    steps:
      - name: Inform Port of workflow start
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).runId}}
          logMessage: Configuring AWS credentials to Renew ACM certificate with domain ${{ fromJson(inputs.port_context).entity.title }}

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Renew ACM certificate
        run: aws acm renew-certificate --certificate-arn ${{ fromJson(inputs.port_context).entity.properties.arn }}

      - name: Inform Port about ACM certificate renewal success
        if: success()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'SUCCESS'
          logMessage: â ACM certificate with domain name ${{ fromJson(inputs.port_context).entity.title }} renewed successfully
          summary: ACM certificate renewal completed successfully

      - name: Inform Port about ACM certificate renewal failure
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'FAILURE'
          logMessage: â Failed to Renew ACM certificate with domain name ${{ fromJson(inputs.port_context).entity.title }}
          summary: ACM certificate renewal failed
```

#### Create Port action

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Renew ACM Certificate action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "renew_acm_certificate",
     "title": "Renew ACM Certificate",
     "icon": "AWS",
     "description": "Renews an eligible ACM certificate",
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
             "property": "renewalEligibility",
             "operator": "=",
             "value": "ELIGIBLE"
           }
         ],
         "combinator": "and"
       },
       "blueprintIdentifier": "acmCertificate"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB-ORG>",
       "repo": "<GITHUB-REPO>",
       "workflow": "renew-acm-cert.yaml",
       "workflowInputs": {
         "port_context": {
           "runId": "{{ .run.id }}",
           "entity": "{{ .entity }}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Renew ACM Certificate` action in the self-service page. ð

Conditional visibility

The renew action will only be visible for certificates that have `renewalEligibility` set to `ELIGIBLE`. This ensures users can only renew certificates that are actually eligible for renewal.

### Delete an ACM certificate[â](#delete-an-acm-certificate "Direct link to Delete an ACM certificate")

#### Add GitHub workflow

Create the file `.github/workflows/delete-acm-cert.yaml` in the `.github/workflows` folder of your repository.

**Delete ACM Certificate GitHub workflow (Click to expand)**

```
name: Delete ACM Certificate

on:
  workflow_dispatch:
    inputs:
      port_context:
        required: true
        description: 'Action and general context (blueprint, entity, run id, etc...)'
        type: string

jobs:
  delete-acm-cert:
    runs-on: ubuntu-latest
    steps:
      - name: Inform Port of workflow start
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).runId}}
          logMessage: Configuring AWS credentials to delete ACM certificate with domain ${{ fromJson(inputs.port_context).entity.title }}

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Delete ACM certificate
        run: aws acm delete-certificate --certificate-arn ${{ fromJson(inputs.port_context).entity.properties.arn }}

      - name: Inform Port about ACM certificate deletion success
        if: success()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'SUCCESS'
          logMessage: â ACM certificate with domain name ${{ fromJson(inputs.port_context).entity.title }} deleted successfully
          summary: ACM certificate deletion completed successfully

      - name: Inform Port about ACM certificate deletion failure
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'FAILURE'
          logMessage: â Failed to delete ACM certificate with domain name ${{ fromJson(inputs.port_context).entity.title }}
          summary: ACM certificate deletion failed
```

#### Create Port action

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Delete ACM Certificate action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "delete_acm_certification",
     "title": "Delete ACM Certification",
     "icon": "AWS",
     "description": "Deletes a certificate and its associated private key.",
     "trigger": {
       "type": "self-service",
       "operation": "DELETE",
       "userInputs": {
         "properties": {},
         "required": [],
         "order": []
       },
       "blueprintIdentifier": "acmCertificate"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB-ORG>",
       "repo": "<GITHUB-REPO>",
       "workflow": "delete-acm-cert.yaml",
       "workflowInputs": {
         "port_context": {
           "runId": "{{ .run.id }}",
           "entity": "{{ .entity }}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Delete ACM Certification` action in the self-service page. ð

Data loss risk

The delete action permanently removes the certificate and its associated private key. This operation cannot be undone, so use it carefully.

## Visualize certificate metrics[â](#visualize-certificate-metrics "Direct link to Visualize certificate metrics")

With your data and actions in place, we can create a dedicated dashboard in Port to visualize all ACM certificates by status, usage, and expiration. In addition, we can trigger actions (request new certificate, renew, delete) directly from the dashboard.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page of your portal.
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **ACM Certificate Management**.
5. Input `Monitor and manage your AWS ACM certificates` under **Description**.
6. Select the `AWS` icon.
7. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize insights from our AWS ACM certificates.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Certificates not in use (click to expand)**

1. Click **`+ Widget`** and select **Number Chart**.
2. Title: `Certificates not in use` (add the `AWS` icon).
3. Select `Count entities` **Chart type** and choose **ACM Certificate** as the **Blueprint**.
4. Select `count` for the **Function**.
5. Add this JSON to the **Additional filters** editor to filter certificates not in use:
   <!-- -->
   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"inUse",
                   "operator":"=",
                   "value": false
               }
           ]
       }
   ]
   ```
6. Select `custom` as the **Unit** and input `certificates` as the **Custom unit**.
7. Click **Save**.

**Certificates by status (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.
2. Title: `Certificates by status` (add the `AWS` icon).
3. Choose the **ACM Certificate** blueprint.
4. Under `Breakdown by property`, select the **Status** property.
5. Click **Save**.

**Expired certificates table (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `Expired certificates` (add the `AWS` icon).

3. Choose the **ACM Certificate** blueprint.

4. Add this JSON to the **Additional filters** editor to filter expired certificates:
   <!-- -->
   ```
   {
     "combinator":"and",
     "rules":[
         {
           "operator":"=",
           "value":"acmCertificate",
           "property":"$blueprint"
         },
         {
           "operator":"=",
           "value":"EXPIRED",
           "property":"status"
         }
     ]
   }
   ```

5. Click **Save** to add the widget to the dashboard.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on `Manage Properties` and add the following properties:

   <!-- -->

   * **Title**: The certificate domain name.
   * **Status**: The current status of the certificate.
   * **Expiration Date**: When the certificate expired.
   * **Account**: The name of each related AWS account.
   * **In Use**: Whether the certificate is currently in use.

8. Click on the **save icon** in the top right corner of the widget to save the customized table.

**Request new certificate action (click to expand)**

1. Click **`+ Widget`** and select **Action card**.
2. Choose the **Request ACM Certificate** action we created in this guide.
3. Click **Save**.
