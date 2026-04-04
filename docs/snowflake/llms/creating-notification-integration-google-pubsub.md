# Source: https://docs.snowflake.com/en/user-guide/notifications/creating-notification-integration-google-pubsub.md

# Creating a notification integration to send notifications to a Google Cloud Pub/Sub topic

To send notifications to a Google Cloud Pub/Sub topic, you must create a notification integration for that topic. To do this:

1. Create a Pub/Sub topic.
2. Create a Pub/Sub subscription.
3. Create a notification integration.
4. Grant Snowflake access to the Pub/Sub subscription.

> **Note:**
>
> Currently, this feature is limited to Snowflake accounts hosted on Google Cloud (GC).

## Create the Pub/Sub topic

Create a Pub/Sub topic that can receive error notification messages from Snowflake, or reuse an existing topic. You can create
the topic using [Cloud Shell](https://cloud.google.com/shell) or [Cloud SDK](https://cloud.google.com/sdk). For more
information, see [Create and use topics](https://cloud.google.com/pubsub/docs/admin) in the Pub/Sub documentation.

For example, execute the following command to create an empty topic:

```bash
gsutil notification create -t <topic>
```

If the topic already exists, the command uses it; otherwise, a new topic is created.

## Create the Pub/Sub subscription

Optionally, create a subscription to the Pub/Sub topic to retrieve notifications. You can create a subscription with pull
delivery using the Cloud Console, `gcloud` command-line tool, or the Cloud Pub/Sub API. For instructions, see
[Managing topics and subscriptions](https://cloud.google.com/pubsub/docs/admin) in the Pub/Sub documentation.

## Create a notification integration in Snowflake

Run the [CREATE NOTIFICATION INTEGRATION](../../sql-reference/sql/create-notification-integration-queue-outbound-gcp.md) command to
create a notification integration. An integration is a Snowflake object that references the Pub/Sub topic you created.

Snowflake associates the notification integration with a Google Cloud (GC) service account created for your account.
Snowflake creates a single service account that is referenced by all GCP notification integrations in your Snowflake account.
The GCP service account for notification integrations is different from the service account created for storage integrations.

When running the command, set GCP_PUBSUB_TOPIC_NAME to the name of the
topic that you created earlier.

For example:

```sqlexample
CREATE NOTIFICATION INTEGRATION my_notification_int
  ENABLED = TRUE
  DIRECTION = OUTBOUND
  TYPE = QUEUE
  NOTIFICATION_PROVIDER = GCP_PUBSUB
  GCP_PUBSUB_TOPIC_NAME = 'projects/sdm-prod/topics/mytopic';
```

## Grant Snowflake access to the Pub/Sub subscription

1. Execute the [DESCRIBE NOTIFICATION INTEGRATION](../../sql-reference/sql/desc-notification-integration.md) command to display the properties of the notification
   that you just created.

   For example, to display the properties of the notification integration named `my_notification_int`:

   ```sqlexample
   DESC NOTIFICATION INTEGRATION my_notification_int;
   ```

2. Record the value of the GCP_PUBSUB_SERVICE_ACCOUNT property (the service account name), which has the following format:

   ```none
   <service_account>@<project_id>.iam.gserviceaccount.com
   ```

3. Log into the Google Cloud console as a project editor.
4. From the home dashboard, choose Big Data » Pub/Sub » Subscriptions.
5. Select the subscription to configure for access.
6. Select SHOW INFO PANEL in the upper-right corner. The information panel for the subscription slides out.
7. In the Add members field, search for the service account name you recorded.
8. From the Select a role dropdown, select Pub/Sub Publisher.
9. Select Add.

   The service account name is added to the Pub/Sub Publisher role dropdown in the information panel.
