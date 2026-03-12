# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/installations/live-events.md

# Live events setup

Port's AWS integration supports real-time event processing, allowing for accurate representation of your AWS infrastructure inside Port. This guide explains how to set up live events for your AWS resources.

Supported account type

Live events are currently only available for **Single account installations** (not multi-account).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before setting up live events, ensure you have:

* Complete the [AWS integration installation](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/installations/installation.md).
* Your Port API key for authentication.
* Permissions to create EventBridge rules on your AWS account.

Terraform vs Manual Installation

* **Terraform users**: Use the provided Terraform module for automated setup.
* **Manual installation users**: Follow the AWS console setup steps.

## Live-events flow[â](#live-events-flow "Direct link to Live-events flow")

The live events flow is comprised of the following steps:

1. **AWS Services** generate events when resources change.

2. **CloudTrail** captures these events.

3. **EventBridge Rules** filter and route specific events.

4. **API Gateway** receives the events and forwards them to Port.

5. Your **Port Integration** processes the events and updates your software catalog.

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/live-events-diagram.svg)

<br />

## Setup methods[â](#setup-methods "Direct link to Setup methods")

* Terraform (Recommended)
* Manual AWS Console Setup

If you installed the AWS integration using Terraform, use the provided module to set up live events.

### Supported resource types

The default Terraform module supports live events for these resource types:

* **EC2 Instances** (`AWS::EC2::Instance`)
* **S3 Buckets** (`AWS::S3::Bucket`)
* **CloudFormation Stacks** (`AWS::CloudFormation::Stack`)

### Add custom resource types

To add live events for additional resource types (like SSM Parameters), use the `aws_event_rule` module:

**AWS event rule module (click to expand)**

```
module "aws_event_rule" {
  source = "port-labs/integration-factory/ocean//modules/aws_helpers/event"
  
  name        = "port-aws-ocean-sync-ssm-parameters"
  description = "Capture Parameter Store change events"
  
  event_pattern = {
    source      = ["aws.ssm"]
    detail-type = ["Parameter Store Change"]
  }
  
  input_paths = {
    resource_type = "AWS::SSM::Parameter"
    account_id    = "$.account"
    aws_region    = "$.region"
    event_name    = "$.detail-type"
    identifier    = "$.resources.0"
  }

  api_key_param = "<live_events_api_key>"
  target_arn    = "<api_gateway_arn>/production/POST/integration/webhook"
}
```

**Configuration parameters (click to expand)**

| Parameter       | Description                                 | Example                                                              |
| --------------- | ------------------------------------------- | -------------------------------------------------------------------- |
| `name`          | EventBridge rule name                       | `"port-aws-ocean-sync-ssm-parameters"`                               |
| `description`   | Rule description                            | `"Capture Parameter Store change events"`                            |
| `event_pattern` | AWS event pattern to match                  | `{ source = ["aws.ssm"], detail-type = ["Parameter Store Change"] }` |
| `input_paths`   | JSON path mappings for event transformation | See example above                                                    |
| `api_key_param` | Port API key parameter                      | `"<live_events_api_key>"`                                            |
| `target_arn`    | API Gateway target ARN                      | `"<api_gateway_arn>/production/POST/integration/webhook"`            |

If you installed the AWS integration manually, follow these steps to create EventBridge rules in the AWS console:

### Step 1: Create a rule

1. Go to **EventBridge** â **Rules** â **Create rule**.
2. **Rule name**: Give it a descriptive name (e.g., `port-live-updates-ssm`).
3. Click **Next**.

### Step 2: Define the event pattern

1. **Event source**: Select "AWS events or services".
2. **Event service**: Select the relevant AWS service (e.g., "Systems Manager").
3. **Event type**: Select the type of event (e.g., "Parameter Store").
4. **Event Type Specification**: Select "Specific detail type(s)" and choose the event type (e.g., "Parameter Store Change").
5. Click **Next**.

### Step 3: Configure the target

1. **Target type**: Select "AWS Service".
2. **Target**: Select "API Gateway".
3. **Target location**: Select "Target in this account".
4. **API**: Select the API Gateway created for your integration.
5. **Deployment stage**: Select "production".
6. **Integration target**: Enter `/integration/webhook` (HTTP POST).

### Step 4: Add required headers

Add these required headers:

| Header Name                | Value                                      |
| -------------------------- | ------------------------------------------ |
| `Content-Type`             | `application/json`                         |
| `x-port-aws-ocean-api-key` | `<your-api-key>` (replace with actual key) |

### Step 5: Transform the Event Data

Port expects a simplified payload. Use Input Transformer to map the raw AWS event:

**Input Path (mapping):**

```
{
  "accountId": "$.account",
  "awsRegion": "$.region", 
  "eventName": "$.detail-type",
  "identifier": "$.resources.0"
}
```

**Template (output):**

```
{
  "resource_type": "AWS::SSM::Parameter",
  "accountId": "<accountId>",
  "awsRegion": "<awsRegion>",
  "eventName": "<eventName>",
  "identifier": "<identifier>"
}
```

Resource Type Mapping

Replace `"AWS::SSM::Parameter"` with the appropriate AWS resource type:

* EC2 Instances: `"AWS::EC2::Instance"`
* S3 Buckets: `"AWS::S3::Bucket"`
* CloudFormation Stacks: `"AWS::CloudFormation::Stack"`

### Step 6: Review & Create

1. Click **Next** â **Next** â **Create rule**.
2. AWS will now forward matching events to Port automatically.

## Supported AWS services[â](#supported-aws-services "Direct link to Supported AWS services")

The complete list of AWS services that support live events can be found [here](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/supported-resources.html).

### Add other services[â](#add-other-services "Direct link to Add other services")

To add live events for additional AWS services, follow these steps:

1. Identify the service's event source and detail type.
2. Create an EventBridge rule with the appropriate pattern.
3. Configure the input transformer with the correct resource type.

Default Terraform installation

The default setup comes preconfigured with support for three AWS resource types:

* `EC2 Instances`.
* `S3 Buckets`.
* `CloudFormation Stacks`.
