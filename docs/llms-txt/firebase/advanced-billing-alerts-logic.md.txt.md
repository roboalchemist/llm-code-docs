# Source: https://firebase.google.com/docs/projects/billing/advanced-billing-alerts-logic.md.txt

# Set up advanced billing alerts and logic

While [simple budget alert emails](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills)
are a relatively easy way to receive billing updates, there may be times when
you want to create more sophisticated alerts that include more customized logic.
Here are two approaches to consider:

- Use Cloud Monitoring to create more sophisticated and timely alerts

- Use a billing Pub/Sub notification along with a corresponding
  Cloud Function to create custom behavior in response to changes in your
  spending

While both of these techniques require more work on your part, they give you the
power to control exactly what kinds of alerts you're receiving and how to
respond to them.

This page offers an overview for each of these approaches.

> [!NOTE]
> All Firebase projects are actually Google Cloud projects behind the scenes, which means billing is shared across Firebase and Google Cloud and you can view the same project in both the Firebase console and the Google Cloud console.

> [!CAUTION]
> When your project is on the Blaze pricing plan, [**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) using the console. You can use the [Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator) to estimate your monthly costs.
>
> Be aware that **budget alerts do *not* cap your usage or
> charges** --- they are *alerts* about your costs so that you can
> take action, if needed. For example, you might consider
> [using
> budget notifications to programmatically disable Cloud Billing on a
> project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

## Create more sophisticated alerts with Cloud Monitoring

Simple budget alert emails let you know when your overall billing has reached
certain thresholds. However, you might also be interested in knowing whether
individual services are increasing unexpectedly --- before they've had a chance
to significantly affect your budget. For more sophisticated use cases like this,
we recommend learning about Cloud Monitoring, which is a Google Cloud tool
available for your Firebase project.

Cloud Monitoring is useful for several different types of alerts:

- If a resource that your project relies upon is unavailable (for both
  Firebase and Google Cloud services, but even for external services, like
  AWS)

- If services like Cloud Functions are taking longer than expected to
  respond

- If your Cloud Storage bucket, Realtime Database instance, or
  Cloud Firestore instance is rejecting too many requests (an indication that your
  Firebase Security Rules might be incorrect).

- If the amount of resources used by some of your Firebase products
  have increased above a certain threshold

Alerts created through Cloud Monitoring are usually sent more quickly than
simple budget alert emails, which are typically sent once per day. Alerts can
take the form of SMS messages, Slack channel messages, PagerDuty notifications,
webhooks, and more. These options enable you to send alerts with higher and more
actionable levels of visibility.

### Using Cloud Monitoring

To get started with Cloud Monitoring, we recommend starting with the
[Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer),
which allows you to create graphs of custom metrics within your
Firebase/Google Cloud project and visualize their usage.

Specifically, you can look at resources such as your Cloud Firestore,
Realtime Database, or Cloud Function instances. You can view usage information about
these products (like number of document reads, bytes sent, or function
invocations) that would have an effect on your billing.

After you're comfortable visualizing your resource usage in the Metrics
Explorer, we recommend creating an
[alerting policy](https://cloud.google.com/monitoring/alerts) on the
metrics you care about most. Here are some example alerting policies:

- If the number of document reads in a 30-minute time period is greater than a
  particular value

- If the usage of a specific resource (like a function invocation) seems to be
  increasing too quickly in a certain timeframe

## Create additional billing logic

Budget alerts send out emails automatically when your budget reaches certain
thresholds, but for more sophisticated alerting or programmatic reactions to
spending increases, you might consider setting up additional custom logic based
on Google Cloud Pub/Sub messages.

For example, you can send alerts to Slack channels or via text message, or you
make programmatic changes to your app or project depending on spend levels.

Pub/Sub is a message-passing service that allows other services to send
messages --- usually in the form of JSON data --- in an asynchronous manner
through channels known as Pub/Sub topics. You can set up authorized
services, like Cloud Functions, to listen to messages in these topics and
act on the data appropriately.

Note that Pub/Sub notifications for billing are sent about once every
20 minutes whether or not your billing usage has changed, and they are
stateless (meaning that they provide no context as to what preceded them). If
you want to keep track of unusual increases in spending over time, or compare
your spending to the previous cycle, you will need to manage that historical
data yourself using a database like Cloud Firestore or the Realtime Database.

### Using Pub/Sub topics with Cloud Functions

You can set up a Pub/Sub topic for your billing data by visiting the
budget associated with your Firebase project in the Google Cloud console (under
*Billing* \> *Budgets and alerts* ), then clicking the checkbox for
**Connect a Pub/Sub topic to this budget** . This will create a
Pub/Sub topic that you can listen to later. For detailed steps, refer to
the [full documentation](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications).

After you've created your Pub/Sub billing topic, you can write a
Cloud Function to listen to this topic and act on the data accordingly. The
data is sent as JSON data and includes helpful information like the amount
you've spent so far, your budget amount, and the start date of your current
billing cycle.

The Google Cloud documentation has full details on how to receive this data
using a Cloud Function. However, if you're using Cloud Functions for Firebase to
deploy your functions, the general process is a little simpler (check out
the [Firebase documentation](https://firebase.google.com/docs/functions/pubsub-events)).
You can also refer to [this video](https://www.youtube.com/watch?v=NWrZwXK92IM)
for a sample walkthrough of the process.

Once you've received this data, there are a number of different ways you can
respond to it. Here are some options:

- [Sending alerts to Slack channels](https://cloud.google.com/billing/docs/how-to/notify#set_up_a_slack_channel_and_permissions),
  Discord channels, or sending text messages when your spending has reached a
  certain threshold.

- Analyzing your spending compared to historical data and alerting you if
  anything seems out of the ordinary

- [Making changes to your app via
  Remote Config](https://firebase.google.com/docs/remote-config/automate-rc)
  if billing levels have gotten too high

- Disabling your Firebase project entirely by
  [programmatically removing your billing service](https://cloud.google.com/billing/docs/how-to/notify#cap_disable_billing_to_stop_usage)
  from your account