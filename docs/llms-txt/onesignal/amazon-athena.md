# Source: https://documentation.onesignal.com/docs/en/amazon-athena.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon Athena

> Sync custom events from Amazon Athena to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Athena"

export const DATA_TYPE_0 = "table columns"

export const COLUMN_HEADER_0 = "Athena Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata from S3 data lake"

## Overview

The OneSignal + Amazon Athena integration enables automatic syncing of custom events from your Athena data lake directly to OneSignal's Custom Events API. This allows you to trigger automated Journeys and personalized messaging campaigns based on real user behavior stored in your AWS data infrastructure.

You can sync events like purchases, product views, subscription changes, or any custom user actions to automatically trigger onboarding sequences, re-engagement campaigns, transactional messages, and targeted promotions across push notifications, email, in-app messages, and SMS.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Amazon Athena

* **AWS Account** with Athena access
* **Athena Workgroup** configured (default: "primary")
* **S3 Query Results Bucket** for Athena query outputs
* **IAM Permissions** for Athena, S3, and AWS Glue access
* **Event data** stored in S3 and cataloged in AWS Glue

***

## Setup

### Configure AWS permissions

OneSignal needs specific permissions to query your event data through Athena. Create an IAM policy with the following permissions:

<Steps>
  <Step title="Create IAM policy">
    Create an IAM policy that includes these permissions:

    ```json  theme={null}
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "athena:StartQueryExecution",
                    "athena:GetQueryExecution",
                    "athena:GetQueryResultsStream",
                    "athena:GetQueryResults",
                    "athena:CreatePreparedStatement",
                    "athena:DeletePreparedStatement",
                    "glue:GetTable",
                    "glue:GetTables",
                    "glue:GetDatabase",
                    "glue:GetDatabases",
                    "s3:PutObject",
                    "s3:GetObject",
                    "s3:ListBucket",
                    "s3:GetBucketLocation"
                ],
                "Resource": [
                    "arn:aws:glue:<region>:<aws-account-id>:table/<database>/*",
                    "arn:aws:glue:<region>:<aws-account-id>:database/<database>",
                    "arn:aws:glue:<region>:<aws-account-id>:catalog",
                    "arn:aws:athena:<region>:<aws-account-id>:workgroup/<workgroup>",
                    "arn:aws:s3:::<query-results-bucket>",
                    "arn:aws:s3:::<query-results-bucket>/*",
                    "arn:aws:s3:::<event-data-bucket>",
                    "arn:aws:s3:::<event-data-bucket>/*"
                ]
            }
        ]
    }
    ```

    <Info>
      Replace the placeholders with your actual AWS region, account ID, database name, workgroup, and bucket names.
    </Info>
  </Step>

  <Step title="Create IAM user or role">
    Create an IAM user for OneSignal and attach the policy created above, or prepare to use role-based access.
  </Step>

  <Step title="Note connection details">
    Collect the following information:

    * **AWS Access Key ID** and **Secret Access Key** (if using IAM user)
    * **S3 Query Results Bucket** URL
    * **AWS Region**
    * **Athena Workgroup** (default: "primary")
  </Step>
</Steps>

### Configure OneSignal Athena connection

<Steps>
  <Step title="Navigate to integrations">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.
  </Step>

  <Step title="Select Amazon Athena">
    Choose **Amazon Athena** from the list of available integrations.
  </Step>

  <Step title="Enter connection details">
    Provide your Athena connection information:

    * **AWS Access Key ID**: Your IAM user access key
    * **AWS Secret Access Key**: Your IAM user secret key
    * **AWS Region**: Your Athena region
    * **S3 Query Results Bucket**: URL for query outputs
    * **Athena Workgroup**: Your workgroup name
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your Athena instance and execute queries.
  </Step>
</Steps>

### Alternative: Role-based access

For enhanced security, you can use IAM roles instead of access keys:

<Steps>
  <Step title="Enable role-based access">
    In the Athena connection settings, check **Use Role** and leave the access keys blank.
  </Step>

  <Step title="Create IAM role">
    In the AWS Console, create an IAM role with:

    * **Trusted Entity**: Another AWS Account
    * **Account ID**: `341876425553` (OneSignal's AWS account)
    * **External ID**: The ID shown in OneSignal (appears after initial connection attempt)
    * **Permissions**: The IAM policy created above
  </Step>

  <Step title="Complete the connection">
    Enter the Role ARN in OneSignal and test the connection.
  </Step>
</Steps>

***

## Event Data Mapping

Once connected, you'll need to map your Athena tables to OneSignal custom event fields:

<Steps>
  <Step title="Select event tables">
    Choose the tables or views containing your event data that you want to sync to OneSignal.
  </Step>

  <Step title="Map required event fields">
    Map the required fields for custom events:

    * **Event Name**: Column containing the event type (e.g., "purchase", "signup")
    * **User Identifier**: External User ID, Email, or Phone Number column
    * **Event Timestamp**: When the event occurred (optional)
  </Step>

  <Step title="Map event payload data">
    Map additional columns to event payload properties:

    * Custom event properties (product\_id, price, category, etc.)
    * Contextual data (source, campaign, etc.)
    * Behavioral metrics (value, quantity, etc.)
  </Step>

  <Step title="Configure sync settings">
    Set your event processing frequency and delivery preferences.
  </Step>
</Steps>

***

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

***

## Limitations

* **Query Performance**: Athena charges per query and data scanned - optimize your event tables
* **S3 Dependencies**: Requires properly configured S3 buckets and Glue catalog
* **Data Freshness**: Event sync frequency depends on how often your S3 data is updated

***

## FAQ

### What happens if my Athena queries fail?

OneSignal will log query errors and retry failed queries. Check your IAM permissions and S3 bucket access if you encounter persistent failures.

### How often does OneSignal sync events?

OneSignal checks for new events based on your configured sync frequency, with a minimum interval of 15 minutes.

***

## Need help?

Contact our support team at `support@onesignal.com` or use the in-app chat for assistance with your Athena integration setup.

Built with [Mintlify](https://mintlify.com).
