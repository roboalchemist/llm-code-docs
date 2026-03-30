# Source: https://docs.port.io/guides/all/visualize-your-aws-storage-configuration.md

# Manage and visualize your AWS S3 buckets and RDS instances

This guide demonstrates how to set up a monitoring solution to gain visibility into security configurations from your AWS S3 and RDS instances using Port's **AWS** integration. You will learn how to:

* Ingest AWS S3 and RDS data into Port's software catalog using **Port's AWS** integration.
* Set up **self-service actions** to manage RDS instances (reboot and delete).
* Build **dashboards** in Port to monitor and take action on your AWS storage resources.

![](/img/guides/awsStorageAndSecurityDashboard.png) ![](/img/guides/awsStorageAndSecurityDashboard2.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Identify publicly accessible S3 buckets to prevent accidental data exposure.
* Track RDS instances with weak or missing encryption settings.
* Empower platform teams to automate day-2 operations via GitHub workflows.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [AWS integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/) is installed in your account.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

When installing the AWS integration in Port, the `AWS Account` blueprint is created by default.<br /><!-- -->However, the `S3` and `RDS Instance` blueprints are not created automatically so we will need to create them manually.

### Create the S3 blueprint[â](#create-the-s3-blueprint "Direct link to Create the S3 blueprint")

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add this JSON schema:

   **AWS S3 blueprint (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "awsS3Bucket",
       "description": "This blueprint represents an AWS S3 bucket in our software catalog",
       "title": "S3",
       "icon": "Bucket",
       "schema": {
           "properties": {
           "link": {
               "type": "string",
               "format": "url",
               "title": "Link"
           },
           "regionalDomainName": {
               "type": "string",
               "title": "Regional Domain Name"
           },
           "versioningStatus": {
               "type": "string",
               "title": "Versioning Status",
               "enum": [
               "Enabled",
               "Suspended"
               ]
           },
           "encryption": {
               "type": "array",
               "title": "Encryption"
           },
           "lifecycleRules": {
               "type": "array",
               "title": "Lifecycle Rules"
           },
           "publicAccessConfig": {
               "type": "object",
               "title": "Public Access"
           },
           "tags": {
               "type": "array",
               "title": "Tags"
           },
           "arn": {
               "type": "string",
               "title": "ARN"
           },
           "region": {
               "type": "string",
               "title": "Region"
           },
           "blockPublicAccess": {
               "type": "boolean",
               "title": "Block Public Access"
           }
           },
           "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {
           "account": {
           "title": "account",
           "target": "awsAccount",
           "required": false,
           "many": false
           }
       }
   }
   ```

5. Click `Save` to create the blueprint.

### Create the RDS instance blueprint[â](#create-the-rds-instance-blueprint "Direct link to Create the RDS instance blueprint")

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add this JSON schema:

   **AWS RDS instance blueprint (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "rdsInstance",
       "description": "This blueprint represents an AWS RDS DBInstance in our software catalog",
       "title": "RDS Instance",
       "icon": "AWS",
       "schema": {
           "properties": {
           "link": {
               "type": "string",
               "format": "url",
               "title": "Link"
           },
           "dbInstanceClass": {
               "type": "string",
               "title": "DB Instance Class"
           },
           "dbInstanceStatus": {
               "type": "string",
               "title": "DB Instance Status"
           },
           "engine": {
               "type": "string",
               "title": "Engine"
           },
           "storageType": {
               "type": "string",
               "title": "Storage Type"
           },
           "engineVersion": {
               "type": "string",
               "title": "Engine Version"
           },
           "port": {
               "type": "number",
               "title": "Port"
           },
           "allocatedStorage": {
               "type": "number",
               "title": "Allocated Storage"
           },
           "endpoint": {
               "type": "string",
               "title": "Endpoint"
           },
           "multiAZ": {
               "type": "boolean",
               "title": "Multi-AZ"
           },
           "deletionProtection": {
               "type": "boolean",
               "title": "Deletion Protection"
           },
           "availabilityZone": {
               "type": "string",
               "title": "Availability Zone"
           },
           "masterUsername": {
               "type": "string",
               "title": "Master Username"
           },
           "publicAccess": {
               "type": "boolean",
               "title": "Public Access"
           },
           "vpcSecurityGroups": {
               "type": "array",
               "items": {
               "type": "string"
               },
               "title": "VPC Security Groups"
           },
           "arn": {
               "type": "string",
               "title": "ARN"
           },
           "storageEncrypted": {
               "type": "boolean",
               "title": "Storage Encrypted"
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
           "required": true,
           "many": false
           }
       }
   }
   ```

5. Click `Save` to create the blueprint.

### Update integration mapping[â](#update-integration-mapping "Direct link to Update integration mapping")

1. Go to the [Data Sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Select the AWS integration.

3. Add the following YAML block into the editor to ingest storage data from AWS:

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
       - kind: AWS::S3::Bucket
           selector:
           query: 'true'
           useGetResourceAPI: true
           port:
           entity:
               mappings:
               identifier: .Identifier
               title: .Identifier
               blueprint: '"awsS3Bucket"'
               properties:
                   regionalDomainName: .Properties.RegionalDomainName
                   encryption: .Properties.BucketEncryption.ServerSideEncryptionConfiguration
                   lifecycleRules: .Properties.LifecycleConfiguration.Rules
                   publicAccessConfig: .Properties.PublicAccessBlockConfiguration
                   blockPublicAccess: >-
                   .Properties.PublicAccessBlockConfiguration | (.BlockPublicAcls and
                   .IgnorePublicAcls and .BlockPublicPolicy and
                   .RestrictPublicBuckets)
                   tags: .Properties.Tags
                   arn: .Properties.Arn
                   region: .Properties.RegionalDomainName | capture(".*\\.(?<region>[^\\.]+)\\.amazonaws\\.com") | .region
                   link: .Properties | select(.Arn != null) | "https://console.aws.amazon.com/go/view?arn=" + .Arn
               relations:
                   account: .__AccountId
   - kind: AWS::RDS::DBInstance
       selector:
       query: 'true'
       useGetResourceAPI: 'true'
       port:
       entity:
           mappings:
           identifier: .Identifier
           title: .Properties.DBInstanceIdentifier
           blueprint: '"rdsInstance"'
           properties:
               link: 'https://console.aws.amazon.com/go/view?arn=' + .Properties.DBInstanceArn
               dbInstanceClass: .Properties.DBInstanceClass
               dbInstanceStatus: .Properties.DBInstanceStatus
               engine: .Properties.Engine
               storageType: .Properties.StorageType
               engineVersion: .Properties.EngineVersion
               port: .Properties.Endpoint.Port
               allocatedStorage: .Properties.AllocatedStorage
               endpoint: .Properties.Endpoint.Address
               multiAZ: .Properties.MultiAZ
               deletionProtection: .Properties.DeletionProtection
               availabilityZone: .Properties.AvailabilityZone
               masterUsername: .Properties.MasterUsername
               publicAccess: .Properties.PubliclyAccessible
               vpcSecurityGroups: .Properties.VpcSecurityGroups
               arn: .Properties.DBInstanceArn
               storageEncrypted: .Porperties.StorageEncrypted
           relations:
               account: .__AccountId
   ```

4. Click `Save & Resync` to apply the mapping.

## Set up self-service actions[â](#set-up-self-service-actions "Direct link to Set up self-service actions")

Now let us create self-service actions to manage your RDS instances directly from Port using GitHub Actions. You will implement workflows to:

1. Reboot an RDS instance.
2. Delete an RDS instance.

To implement these use-cases, follow the steps below:

### Add GitHub secrets[â](#add-github-secrets "Direct link to Add GitHub secrets")

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `PORT_CLIENT_ID` - Port Client ID [learn more](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#get-api-token).
* `PORT_CLIENT_SECRET` - Port Client Secret [learn more](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#get-api-token).
* `AWS_ACCESS_KEY_ID` - AWS IAM user's access key.
* `AWS_SECRET_ACCESS_KEY` - AWS IAM user's secret access key.
* `AWS_REGION` - AWS region (e.g., `us-east-1`).

### Reboot an RDS instance[â](#reboot-an-rds-instance "Direct link to Reboot an RDS instance")

#### Add GitHub workflow[â](#add-github-workflow "Direct link to Add GitHub workflow")

Create the file `.github/workflows/reboot-rds-instance.yaml` in the `.github/workflows` folder of your repository.

**Reboot RDS GitHub workflow (Click to expand)**

```
name: Reboot RDS Instance

on:
  workflow_dispatch:
    inputs:
      port_context:
        required: true
        description: 'Action and general context (blueprint, entity, run id, etc...)'
        type: string

jobs:
  reboot-rds-instance:
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
          logMessage: Configuring AWS credentials to reboot RDS instance with ID ${{ fromJson(inputs.port_context).entity.identifier }}

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Reboot RDS instance
        run: aws rds reboot-db-instance --db-instance-identifier ${{ fromJson(inputs.port_context).entity.identifier }}

      - name: Inform Port about RDS reboot success
        if: success()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'SUCCESS'
          logMessage: â RDS instance with ID ${{ fromJson(inputs.port_context).entity.identifier }} rebooted successfully
          summary: RDS instance reboot completed successfully

      - name: Inform Port about RDS reboot failure
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'FAILURE'
          logMessage: â Failed to reboot RDS instance with ID ${{ fromJson(inputs.port_context).entity.identifier }}
          summary: RDS instance reboot failed
```

#### Create Port action[â](#create-port-action "Direct link to Create Port action")

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Reboot RDS instance action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "reboot_rds_instance",
     "title": "Reboot RDS Instance",
     "icon": "AmazonRDS",
     "description": "Reboot an RDS Instance",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {},
         "required": []
       },
       "blueprintIdentifier": "rdsInstance"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB-ORG>",
       "repo": "<GITHUB-REPO>",
       "workflow": "reboot-rds-instance.yaml",
       "workflowInputs": {
         "port_context": {
           "entity": "{{ .entity }}",
           "blueprint": "{{ .action.blueprint }}",
           "runId": "{{ .run.id }}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Reboot RDS Instance` action in the self-service page. ð

### Delete an RDS instance[â](#delete-an-rds-instance "Direct link to Delete an RDS instance")

#### Add GitHub workflow[â](#add-github-workflow-1 "Direct link to Add GitHub workflow")

Create the file `.github/workflows/delete-rds-instance.yaml` in the `.github/workflows` folder of your repository.

**Delete RDS GitHub workflow (Click to expand)**

```
name: Delete RDS Instance

on:
  workflow_dispatch:
    inputs:
      port_context:
        required: true
        description: 'Action and general context (blueprint, entity, run id, etc...)'
        type: string
      should_create_db_snapshot:
        required: true
        description: 'Specifies whether to skip the creation of a final DB snapshot before deleting the instance'
        type: string

jobs:
  delete-rds-instance:
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
          logMessage: Configuring AWS credentials to delete RDS instance with ID ${{ fromJson(inputs.port_context).entity.identifier }}

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Delete RDS instance
        run: aws rds delete-db-instance --db-instance-identifier ${{ fromJson(inputs.port_context).entity.identifier }} ${{ inputs.should_create_db_snapshot }}

      - name: Inform Port about RDS delete success
        if: success()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'SUCCESS'
          logMessage: â RDS instance with ID ${{ fromJson(inputs.port_context).entity.identifier }} deleted successfully
          summary: RDS instance delete completed successfully

      - name: Inform Port about RDS delete failure
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId }}
          status: 'FAILURE'
          logMessage: â Failed to delete RDS instance with ID ${{ fromJson(inputs.port_context).entity.identifier }}
          summary: RDS instance delete failed
```

#### Create Port action[â](#create-port-action-1 "Direct link to Create Port action")

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Delete RDS instance action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "delete_rds_instance",
     "title": "Delete RDS Instance",
     "icon": "AmazonRDS",
     "description": "Delete an RDS instance",
     "trigger": {
       "type": "self-service",
       "operation": "DELETE",
       "userInputs": {
         "properties": {
           "skip_db_snapshot": {
             "type": "boolean",
             "title": "Skip DB snapshot",
             "description": "Specifies whether to skip the creation of a final DB snapshot before deleting the instance",
             "default": false
           }
         },
         "required": [
           "skip_db_snapshot"
         ],
         "order": [
           "skip_db_snapshot"
         ]
       },
       "blueprintIdentifier": "rdsInstance"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB-ORG>",
       "repo": "<GITHUB-REPO>",
       "workflow": "delete-rds-instance.yaml",
       "workflowInputs": {
         "should_create_db_snapshot": "{{ if .inputs.skip_db_snapshot == true then \"--skip-final-snapshot\" else \"--no-skip-final-snapshot\" end }}",
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

Now you should see the `Delete RDS Instance` action in the self-service page. ð

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

Once the AWS storage data is synced, we can create a dedicated dashboard in Port to monitor and analyze security configurations and access controls using customizable widgets.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page of your portal.
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **AWS Storage Security Overview**.
5. Input `Monitor and manage AWS S3 buckets and RDS instances security configurations` under **Description**.
6. Select the `AWS` icon.
7. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize security insights from our AWS storage.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**RDS by availability zone (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `RDS by availability zone` (add the `AmazonRDS` icon).

3. Choose the **RDS Instance** blueprint.

4. Under `Breakdown by property`, select the **Availability Zone** property

   ![](/img/guides/RDSByAvailabilityZone.png)

5. Click **Save**.

**RDS by public access (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `RDS by public access` (add the `AmazonRDS` icon).

3. Choose the **RDS Instance** blueprint.

4. Under `Breakdown by property`, select the **Public Access** property

   ![](/img/guides/RDSByPublicAccess.png)

5. Click **Save**.

**Unprotected RDS by engine (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Unprotected RDS by engine` (add the `AmazonRDS` icon).

3. Choose the **RDS Instance** blueprint.

4. Under `Breakdown by property`, select the **Engine** property.

5. Add this JSON to the **Additional filters** editor to filter unprotected RDS instances:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"deletionProtection",
                   "operator":"=",
                   "value":false
               }
           ]
       }
   ]
   ```

   ![](/img/guides/RDSByEngine.png)

6. Click **Save**.

**RDS without SSL (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `RDS without SSL` (add the `AmazonRDS` icon).

3. Select `Count entities` **Chart type** and choose **RDS Instance** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter RDS instances without SSL configuration:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"storageEncrypted",
                   "operator":"=",
                   "value":false
               }
           ]
       }
   ]
   ```

   ![](/img/guides/RDSWithoutSSL.png)

6. Click `Save`.

**S3 buckets by public access (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `S3 by public access` (add the `S3` icon).

3. Choose the **S3** blueprint.

4. Under `Breakdown by property`, select the **Block Public Access** property

   ![](/img/guides/S3ByPublicAccess.png)

5. Click **Save**.

**Unencrypted S3 buckets (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Unencrypted S3 buckets` (add the `S3` icon).

3. Select `Count entities` **Chart type** and choose **S3** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter S3 buckets without encryption configurations:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"encryption",
                   "operator":"isNotEmpty"
               }
           ]
       }
   ]
   ```

   ![](/img/guides/UnencryptedS3.png)

6. Click `Save`.

**Insecure RDS instances table (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **Insecure RDS Instances**.

3. Choose the **RDS Instance** blueprint

4. Add this JSON to the **Additional filters** editor to filter insecure RDS instances:
   <!-- -->
   ```
   [
       {
           "combinator":"or",
           "rules":[
               {
                   "property":"storageEncrypted",
                   "operator":"=",
                   "value":false
               },
               {
                   "property":"deletionProtection",
                   "operator":"=",
                   "value":false
               },
               {
                   "property":"publicAccess",
                   "operator":"=",
                   "value":true
               }
           ]
       }
   ]
   ```

5. Click **Save** to add the widget to the dashboard.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on `Manage Properties` and add the following properties:

   <!-- -->

   * **DB Instance Status**: The current status of the RDS instance.
   * **Engine**: The database engine type.
   * **Storage Encrypted**: Whether storage encryption is enabled.
   * **Deletion Protection**: Whether deletion protection is enabled.
   * **Public Access**: Whether the instance is publicly accessible.
   * **Account**: The name of each related AWS account.

8. Click on the **save icon** in the top right corner of the widget to save the customized table.
