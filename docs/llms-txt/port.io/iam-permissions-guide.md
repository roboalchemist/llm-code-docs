# Source: https://docs.port.io/guides/all/iam-permissions-guide.md

# IAM permission management

## Overview[â](#overview "Direct link to Overview")

Developers often require access to various cloud resources daily. With all your essential AWS resources integrated into Port, you can streamline the process by allowing developers to request IAM permissions directly from Port.

It's crucial to track the permissions allocated to your developers, including who requested them and what permissions were granted.

In this step-by-step guide, we will create Port blueprints and actions that enable you to request and revoke IAM permissions for different AWS resources. Additionally, you'll be able to monitor which permissions were requested and by whom.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* **Prepare Your Credentials:** Have your Port organization's Client ID and Client Secret ready. You can find your Port credentials [here](/build-your-software-catalog/custom-integration/api/.md#find-your-port-credentials).

* **Set Up AWS IAM User:** In your AWS console, [create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) called `port-iam-management-user` with the following IAM permissions policy:

  IAM policy json

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "iam:CreateRole",
                  "iam:UpdateRole",
                  "iam:DeleteRole",
                  "iam:CreatePolicy",
                  "iam:DeletePolicy",
                  "iam:AttachRolePolicy",
                  "iam:DetachRolePolicy"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

* **Create Access Credentials:** Generate [access credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)\*\* for this IAM user (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).

* **GitHub Repository:** Create a repository named `port-iam-permissions` in your GitHub organization. This repository will store workflows and dependency files.

* **Install Port's GitHub App** Install the app [here](https://github.com/apps/getport-io/installations/new) and grant it permissions for the `port-iam-permissions` repository.

* **Create GitHub Secrets:** Add the following [Github Action secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) in the port-iam-permissions repository:

  * `PORT_CLIENT_ID` - Your Port Client ID.
  * `PORT_CLIENT_SECRET` - Your Port Client Secret.
  * `AWS_ACCOUNT_ID` - The AWS account ID you want to manage.
  * `AWS_ACCESS_KEY_ID` - The AWS access key ID for the `port-iam-management-user` IAM user.
  * `AWS_SECRET_ACCESS_KEY` - The AWS secret access key for the `port-iam-management-user` IAM user.
  * `AWS_REGION` - Your primary AWS region (use us-east-1 if unsure).

## Data Model[â](#data-model "Direct link to Data Model")

Create [blueprints]() to manage AWS resources and track IAM permission requests from developers.

**Blueprints to create:**

`AWS Resource` blueprint

The entities of this blueprint represent different AWS resources we want to manage IAM permissions for (S3 buckets, EC2 instances, etc.).

Create in Port

```
{
    "identifier": "aws_resource",
    "title": "AWS Resource",
    "icon": "AWS",
    "schema": {
        "properties": {
            "tags": {
                "items": {
                    "type": "object"
                },
                "title": "Tags",
                "type": "array",
                "icon": "DefaultProperty"
            },
            "resource_type": {
                "icon": "DefaultProperty",
                "title": "Resource Type",
                "type": "string",
                "enum": [
                    "S3",
                    "EC2"
                ],
                "enumColors": {
                    "S3": "blue",
                    "EC2": "green"
                }
            }
        },
        "required": ["resource_type"]
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {}
}
```

`IAM Permissions` blueprint

The entities of this blueprint represent different AWS IAM permissions that can be associated to an IAM Policy (`s3:DeleteBucket`, `s3:PutObject`, `ec2:StopInstances`, `ec2:TerminateInstances`, etc.).

Create in Port

```
{
    "identifier": "iam_permissions",
    "title": "IAM Permissions",
    "icon": "Lock",
    "schema": {
        "properties": {
            "resource_type": {
                "icon": "AWS",
                "title": "Resource Type",
                "type": "string",
                "enum": [
                    "S3",
                    "EC2"
                ],
                "enumColors": {
                    "S3": "blue",
                    "EC2": "green"
                }
            }
        },
        "required": ["resource_type"]
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {}
}
```

`Provisioned Permissions` blueprint

The entities of this blueprint represent the permissions which were created and managed using Port.

Create in Port

```
{
    "identifier": "provisioned_permissions",
    "description": "This blueprint represents a set of provisioned permissions for some AWS resource",
    "title": "Provisioned Permissions",
    "icon": "Lock",
    "schema": {
        "properties": {
            "requester": {
                "title": "Requester",
                "type": "string",
                "format": "user",
                "icon": "DefaultProperty"
            },
            "iam_policy": {
                "title": "IAM Policy",
                "type": "object",
                "icon": "Lock",
                "description": "The IAM policy given for this temporary permission"
            },
            "sign_in_url": {
                "icon": "DefaultProperty",
                "title": "Sign-in URL",
                "type": "string",
                "description": "The sign-in URL for this temporary permission",
                "format": "url"
            },
            "policy_arn": {
                "title": "Policy ARN",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "role_arn": {
                "title": "Role ARN",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "expiry_time": {
              "title": "Expiry Time",
              "icon": "DefaultProperty",
              "description": "When the provisioned permission will expire",
              "type": "string",
              "format": "timer"
            }
        },
        "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
        "permissions": {
            "title": "Permissions",
            "target": "iam_permissions",
            "required": false,
            "many": true
        },
        "aws_resource": {
            "title": "AWS Resource",
            "target": "aws_resource",
            "required": false,
            "many": false
        }
    }
}
```

AWS Resource Types

For simplicity, the blueprints above include pre-defined options for resource types, such as `EC2` and `S3`.

You can modify the blueprints to support any type of AWS resource by adding additional options to the `resource_type` properties in both the `AWS Resource` and `IAM Permissions` blueprints.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-data-model.png)

## Actions[â](#actions "Direct link to Actions")

To provision and revoke permissions for AWS resources via Port, you'll need to create [actions]() and set up the actions' backends.

### Actions backend - GitHub Workflows[â](#actions-backend---github-workflows "Direct link to Actions backend - GitHub Workflows")

As mentioned in the [prerequisites](#prerequisites), you'll use GitHub Actions as the backend for your Port actions. To do this, you will create two GitHub workflow files which will interact with AWS via the [CLI](https://aws.amazon.com/cli/) to create the necessary IAM permissions, and two JSON files which will be used as templates for the IAM permissions.

Create the following files in the `port-iam-permissions` repository you set up in the [prerequisites](#prerequisites) section using the correct path as it appears in each filename:

`Create permissions for AWS resource` GitHub workflow

This workflow is responsible for creating new IAM permissions for an AWS resource.

.github/workflows/create-iam-permissions.yaml

```
name: Create permissions for AWS resource
on:
  workflow_dispatch:
    inputs:
      properties:
        type: string
        required: true
        description: The form inputs
      port_context:
        type: string
        required: true
        description: The Port context for triggering this action                  

jobs:
  create-iam-permissions:
    name: Create IAM permissions
    runs-on: ubuntu-latest
    env:
      POLICY_NAME: Permission-${{github.run_id}}
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: true
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}
      - name: Create JSON for permissions
        id: create-jsons
        run: |
          permissions=$(echo '${{ inputs.properties }}' | jq -c -r '[.permissions[].identifier]')
          echo "PERMISSIONS_ARRAY=${permissions}" >> $GITHUB_OUTPUT
          jq -r --argjson permissions "${permissions}" --arg resource "${{fromJson(inputs.port_context).entity.identifier}}/*" '.Statement[0].Action=$permissions | .Statement[0].Resource=$resource' .github/templates/iamPolicyDocument.json > temp_policy_document.json
          jq -r --arg aws_acc_id "${{ secrets.AWS_ACCOUNT_ID }}" '.Statement[0].Principal.AWS="arn:aws:iam::"+$aws_acc_id+":root"' .github/templates/iamTrustPolicy.json > temp_trust_policy.json
      - name: Apply policies and attachments
        id: apply-policies
        run: |
          # Create the policy
          policy_arn=$(aws iam create-policy --policy-name $POLICY_NAME --policy-document file://temp_policy_document.json --no-cli-pager | jq '.Policy.Arn')
          echo ${policy_arn}
          echo "POLICY_ARN=${policy_arn}" >> $GITHUB_OUTPUT
          # Create the role with assume-role policy
          echo "ROLE_ARN=$(aws iam create-role --role-name $POLICY_NAME --assume-role-policy-document file://temp_trust_policy.json --no-cli-pager | jq '.Role.Arn')" >> $GITHUB_OUTPUT
          # Attach policy to the role
          aws iam attach-role-policy --role-name $POLICY_NAME --policy-arn arn:aws:iam::${{ secrets.AWS_ACCOUNT_ID }}:policy/$POLICY_NAME
      - name: Create variables
        id: create-variables
        run: |
          echo "POLICY=$(cat temp_policy_document.json | jq -c '.')" >> $GITHUB_OUTPUT
          echo "SIGN_IN_URL=https://signin.aws.amazon.com/switchrole?account=${{ secrets.AWS_ACCOUNT_ID }}&roleName=${{ env.POLICY_NAME }}&displayName=${{ env.POLICY_NAME }}" >> $GITHUB_OUTPUT
      - name: "Report permission to Port ð¢"
        uses: port-labs/port-github-action@v1
        with:
            clientId: ${{ secrets.PORT_CLIENT_ID }}
            clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
            baseUrl: https://api.port.io
            identifier: ${{ env.POLICY_NAME }}
            title: ${{ env.POLICY_NAME }}
            blueprint: provisioned_permissions
            properties: |
              {
                "iam_policy": ${{ steps.create-variables.outputs.POLICY }},
                "requester": "${{ fromJson(inputs.port_context).trigger.by.user.email }}",
                "sign_in_url": "${{ steps.create-variables.outputs.SIGN_IN_URL }}",
                "role_arn": ${{ steps.apply-policies.outputs.ROLE_ARN }},
                "policy_arn": ${{ steps.apply-policies.outputs.POLICY_ARN }}
              }
            relations: |
              {
                "aws_resource": "${{ fromJson(inputs.port_context).entity.identifier }}",
                "permissions": ${{ steps.create-jsons.outputs.PERMISSIONS_ARRAY }}
              }
      - uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          status: "SUCCESS"
          runId: ${{ fromJson(inputs.port_context).runId}}
          logMessage: |
            Created permission for the AWS resource "${{ fromJson(inputs.port_context).entity.identifier }}"ð
            Requester for this permission is: ${{ fromJson(inputs.port_context).trigger.by.user.email }}
            The sign-in URL: ${{ steps.create-variables.outputs.SIGN_IN_URL }}
```

`Revoke permissions for AWS resource` GitHub workflow

This workflow is responsible for revoking IAM permissions for an AWS resource.

.github/workflows/delete-iam-permissions.yaml

```
name: Delete IAM permissions for AWS resource
on:
  workflow_dispatch:
    inputs:
      properties:
        type: string
        required: true
        description: The Port Payload for triggering this action
      port_context:
        type: string
        required: true
        description: The Port context for triggering this action                

jobs:
  delete-permissions:
    name: Delete IAM permissions
    runs-on: ubuntu-latest
    env:
      POLICY_ARN: ${{ fromJson(inputs.port_context).entity.properties.policy_arn }}
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: true
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}
      - name: Delete policies
        id: delete-policies
        run: |
          # Detach the policy from the role
          aws iam detach-role-policy --role-name ${{ fromJson(inputs.port_context).entity.identifier }} --policy-arn ${{ env.POLICY_ARN }}
          # Delete the policy
          aws iam delete-policy --policy-arn "${{ env.POLICY_ARN }}" --no-cli-pager
          # Delete the role
          aws iam delete-role --role-name ${{ fromJson(inputs.port_context).entity.identifier }} --no-cli-pager
      - name: "Delete permission from Port ð¢"
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          identifier: ${{ fromJson(inputs.port_context).entity.identifier }}
          operation: DELETE
          blueprint: provisioned_permissions
      - uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).runId}}
          logMessage: |
            Permission "${{ fromJson(inputs.port_context).entity.identifier }}" has been deleted.
            To get more information regarding this deletion, contact "${{ fromJson(inputs.port_context).trigger.by.user.email }}".
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

`IAM policy JSON` template file

This file will act as a template for the generated IAM policies.

.github/templates/iamPolicyDocument.json

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [],
            "Resource": ""
        }
    ]
}
```

`IAM trust policy JSON` template file

This file will act as a template for the generated IAM trust policies.

***Replace the `<YOUR_AWS_ACCOUNT_ID>` with the AWS account ID you want to allocate permissions for.***

.github/templates/iamTrustPolicy.json

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_ID>:root"}, 
            "Action": "sts:AssumeRole"
        }
    ]
}
```

### Creating Port actions[â](#creating-port-actions "Direct link to Creating Port actions")

After setting up the backend in GitHub, create Port actions to trigger these workflows. Use the Port UI to create the following actions:

`Request permissions` Port action

This is a `DAY-2` action on the `AWS Resource` blueprint for requesting and provisioning new IAM permissions.

***Replace the `<YOUR_GITHUB_ORG>` placeholder with your GitHub organization.***

Create in Port

```
{
  "identifier": "request_permissions",
  "title": "Request permissions",
  "icon": "DefaultProperty",
  "description": "Request permissions for an AWS resource",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "userInputs": {
      "properties": {
        "permissions": {
          "title": "Permissions",
          "type": "array",
          "items": {
            "type": "string",
            "format": "entity",
            "blueprint": "iam_permissions",
            "dataset": {
              "combinator": "and",
              "rules": [
                {
                  "property": "resource_type",
                  "operator": "=",
                  "value": {
                    "jqQuery": ".entity.properties.resource_type"
                  }
                }
              ]
            }
          }
        }
      },
      "required": [
        "permissions"
      ],
      "order": []
    },
    "blueprintIdentifier": "aws_resource"
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<YOUR_GITHUB_ORG>",
    "repo": "port-iam-permissions",
    "workflow": "create-iam-permissions.yaml",
    "workflowInputs": {
      "properties": "{{ .inputs }}",
      "port_context": {
        "blueprint": "{{.action.blueprint}}",
        "entity": "{{.entity}}",
        "runId": "{{.run.id}}",
        "trigger": "{{ .trigger }}"
      }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

Creating Actions with JSON

Don't know how to create actions via the Port UI? Click [here](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/.md)!

`Revoke permissions` Port action

This is a `DELETE` action on the `Provisioned Permissions` blueprint for revoking IAM permissions.

***Replace the `<YOUR_GITHUB_ORG>` placeholder with your GitHub organization.***

Create in Port

```
{
  "identifier": "revoke_permissions",
  "title": "Revoke permissions",
  "icon": "Alert",
  "trigger": {
    "type": "self-service",
    "operation": "DELETE",
    "userInputs": {
      "properties": {},
      "required": [],
      "order": []
    },
    "blueprintIdentifier": "provisioned_permissions"
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<YOUR_GITHUB_ORG>",
    "repo": "port-iam-permissions",
    "workflow": "delete-iam-permissions.yaml",
    "workflowInputs": {
      "properties": "{{ .inputs }}",
      "port_context": {
        "blueprint": "{{ .action.blueprint }}",
        "entity": "{{.entity }}",
        "runId": "{{ .run.id }}",
        "trigger": "{{ .trigger }}"
      }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

## Managing permissions[â](#managing-permissions "Direct link to Managing permissions")

Before provisioning and revoking permissions, we need to complete two tasks:

1. Define the AWS resources for which we want to provision permissions.
2. Specify the permissions we want our developers to be able to request and provision.

### Defining AWS resources[â](#defining-aws-resources "Direct link to Defining AWS resources")

Managing the AWS resources we want to provision permissions for will be done using Port entities. Navigate to the [AWS Resources](https://app.getport.io/aws_resources) catalog page to create some example entities.

Simple Permissions to Get Started

For simplicity, we will be creating AWS resource entities manually. This can also be done using Port's [AWS Exporter](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/.md). Go to the [Next Steps](#next-steps) section to read more.

In the `AWS Resources` catalog page, click `Manually add AWS Resource` or click the `+ AWS Resource` button to create an entity. The entity's identifier is the `AWS ARN` of the AWS resource. Ensure sure you toggle off the `Autogenerate` for the identifier.

Create two `AWS Resource` entities:

1. `S3` Bucket:

   * Title: `My awesome S3 bucket`
   * Identifier: `arn:aws:s3:::my-s3-bucket`
   * Resource Type: `S3`

2. `EC2` Instance:

   * Title: `My awesome EC2 machine`
   * Identifier: `arn:aws:ec2:us-east-1:12345678:instance/i-abc123456789`
   * Resource Type: `EC2`

Adding More IAM Permissions

Feel free to add more AWS resources of your own, just ensure the entity's identifier matches the AWS ARN of the resource you want to add.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-create-aws-resource-entity.png)

### Defining allowed IAM permissions[â](#defining-allowed-iam-permissions "Direct link to Defining allowed IAM permissions")

To manage the IAM permissions we want our developers to provision, we will use Port entities. Navigate to the [IAM Permissions](https://app.getport.io/iam_permissions) catalog page to create example entities

In the `IAM Permissions` catalog page, click `Manually add IAM Permission` or click the `+ IAM Permissions` button to create an entity. The entity's identifier should be the IAM permission you want to allow (e.g., `s3:PutObject`). Ensure you toggle off the `Autogenerate` option for the identifier.

Create two `IAM Permissions` entities:

1. `S3` Permission:

   * Title: `Put S3 objects`
   * Identifier: `s3:PutObject`
   * Resource Type: `S3`

2. `EC2` Permission:

   * Title: `Stop EC2 Instance`
   * Identifier: `ec2:StopInstances`
   * Resource Type: `EC2`

Add More IAM Permissions

Feel free to add more IAM permissions of your own, just ensure the entity's identifier matches the IAM permission you want to add.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-create-iam-permissions-entity.png)

We are all set!

### Managing permissions[â](#managing-permissions-1 "Direct link to Managing permissions")

Now that we finished setting up our Port environment, actions, and actions' backends, we are ready to manage IAM permissions for our AWS resources!

#### Provision permissions[â](#provision-permissions "Direct link to Provision permissions")

Start by creating new temporary permissions for our S3 bucket `my-s3-bucket`. Navigate to the bucket's [entity page](https://app.getport.io/aws_resourceEntity?identifier=arn%3Aaws%3As3%3A%3A%3Amy-s3-bucket).

1. Click the `...` at the top right of the entity screen.
2. Select `Request permissions`.
3. Choose the `s3:PutObject` permission.
4. Click `Execute`.

This will trigger a new action run which will appear in the action runs bar on the right. Click on the action run to navigate to the run page.

Once the Port action run is complete, you will see action logs showing:

* The AWS resource for which the IAM permissions were provisioned.
* Who requested the IAM permissions.
* The sign-in URL for the provisioned role.

The action will also create a new `Provisioned Permissions` entity, visible in the [Provisioned Permissions](https://app.getport.io/provisioned_permissions) catalog page.

To test your new temporary permissions, copy the sign-in URL and paste it to your browser's URL bar. Click the `Switch Role` button.

You are now signed in to your new role, which has permissions as defined in the Port action! ð¥³

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-provision-permissions-action.png)

#### Revoke permissions[â](#revoke-permissions "Direct link to Revoke permissions")

Now, we want to revoke the permissions provisioned for our S3 bucket `my-s3-bucket`. Start by navigating to the new `Provisioned Permission` entity.

1. Go to the [Provisioned Permissions](https://app.getport.io/provisioned_permissions) catalog page.
2. Click on the new `Permission-XXXXXXXX` entity.

About Provisioned Permissions

On the `Provisioned Permissions` entity page, you can view crucial information about the provisioned permissions, such as the generated IAM policy and the requester of the permissions.

In the `Related entities` section, you can see which permissions were provisioned and to which resource.

Visit the [Provisioned Permissions](https://app.getport.io/provisioned_permissions) catalog page to view all active permissions. There, you can find detailed information, including the requesters of permissions, IAM policies, sign-in URLs, and more.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-provisioned-permissions-page.png)

Once you're in the provisioned permission entity you created:

1. Click the `...` at the top right of the entity screen.
2. Click `Revoke permissions`.
3. Click `Delete`.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-provisioned-permissions-entity-revoke-permissions.png)

This will trigger a new action run which will appear in the action runs bar on the right. Click on the action run to access its details page.

Upon completion of the Port action run, you will receive action logs containing:

* Information about the deleted IAM Permission.
* Identification of the individual responsible for the deletion.

Furthermore, the action will remove the `Provisioned Permissions` entity generated during the permissions provisioning.

Attempting to use the previous sign-in URL again will demonstrate that the permission is no longer functional â.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-revoke-permissions-action.png)

#### Remove permissions with automations[â](#remove-permissions-with-automations "Direct link to Remove permissions with automations")

With the [automations](https://docs.port.io/actions-and-automations/define-automations) feature, you can automatically trigger actions using events from the catalog.

For instance, your HR system can automatically trigger an event to revoke permissions via Port when an employee departs the company. In this guide, we will utilize the timer expired event to initiate the revoke permissions action, ensuring temporary permissions expire as required by your security or compliance teams.

Note that `Provisioned Permissions` blueprint we deployed earlier has a timer property to specify when a permission will expire.

```
"expiry_time": {
  "title": "Expiry Time",
  "icon": "DefaultProperty",
  "description": "When the provisioned permission will expire",
  "type": "string",
  "format": "timer"
  }
```

The automation you will create will monitor events related to `Provisioned Permissions` entities in your catalog. It will check if these events are triggered by the `expiry_time` timer property expiring and then execute the `Delete IAM Permissions` GitHub workflow described earlier in this guide.

Building Automations

Need help building automations? Check out our [guide](https://docs.port.io/actions-and-automations/define-automations/) on creating automations!

Next, proceed to deploy the automation outlined below. Remember to replace `YOUR_GITHUB_ORG` in the JSON with your GitHub Organization ID.

Revoke Expired Permissions Automation

Create in Port

```
{
  "identifier": "automation",
  "title": "Automation",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "TIMER_PROPERTY_EXPIRED",
      "blueprintIdentifier": "provisioned_permissions",
      "propertyIdentifier": "expiry_time"
    }
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<YOUR_GITHUB_ORG>",
    "repo": "port-iam-permissions",
    "workflow": "delete-iam-permissions.yaml",
    "workflowInputs": {
      "properties": "{{ .inputs }}",
      "port_context": {
        "blueprint": "{{ .event.context.blueprintIdentifier }}",
        "entity": "{{.event.diff.after }}",
        "runId": "{{ .run.id }}",
        "trigger": "{{ .event.trigger }}"
      }
    },
    "reportWorkflowStatus": true
  },
  "publish": true
}
```

Please note that the automation's JSON structure differs from that of the self-service `Revoke permissions` action JSON outlined earlier in this guide. Specifically, the `workflowInputs` are populated with data from the Timer Expired event (such as `.event.context.blueprintIdentifier` or `.event.trigger`), rather than from user input or the self-service action.

Once our automation is deployed, we will manually configure the expiry time for a provisioned permission through the Port UI. In a real-world scenario, this would typically be programmatically set based on your organization's permissions time-to-live policy or defined by the developer during the permission creation via self-service action.

To proceed, execute the `Request Permissions` self-service action on the S3 bucket entity created earlier, selecting `s3:PutObject` from the `Permissions` dropdown. Then, navigate to the `Provisioned Permissions` tab in the catalog and set an expiry time five minutes into the future for the newly created entity.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-provisioned-permissions-entity-add-expiry-time.png)

Next, click on the `Builder` button located at the top right. Then, navigate to the `Audit Log` tab on the left sidebar. After five minutes have elapsed, you should observe a `Timer Expired` event logged for a `provisioned_permissions` blueprint. This event is automatically generated by Port when the manually set expiry time for the `Provisioned Permissions` entity is reached.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-provisioned-permissions-timer-expired-event.png)

Now, navigate to the `Automations` tab on the left sidebar. Next, click on the `Runs history` button located at the top right. Select the latest automation run. You should observe that the automation run completed successfully and the permission was deleted.

![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/iam-permissions-expired-permissions-removal-automation-run.png)

## Summary[â](#summary "Direct link to Summary")

That concludes the setup for managing IAM permissions across your AWS resources using Port! ð

Feel free to explore further by adding additional `IAM Permissions` and `AWS Resources` entities. You can expand the range of resource types by adjusting the `resource_type` property within the `IAM Permissions` and `AWS Resources` blueprints.

Refer to the [Next Steps](#next-steps) section to discover how to enhance this guide further within your Port environment.

## Next Steps[â](#next-steps "Direct link to Next Steps")

* **Install Port's [AWS exporter](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/.md)**: Utilize Port's AWS exporter to automatically populate your software catalog with AWS resources from your environment. This tool enables you to populate your `AWS Resources` blueprints with various AWS resources.

* **Enforce [manual approval](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/.md#configure-manual-approval-for-actions) for your Port actions**: Gain control over provisioning and revoking permissions by implementing manual approval for your actions. This setup establishes a request-approve workflow for managing permissions using Port.
