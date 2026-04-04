# Source: https://firebase.google.com/docs/projects/billing/advanced-billing-alerts-logic.md.txt

While[simple budget alert emails](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills)are a relatively easy way to receive billing updates, there may be times when you want to create more sophisticated alerts that include more customized logic. Here are two approaches to consider:

- UseCloud Monitoringto create more sophisticated and timely alerts

- Use a billingPub/Subnotification along with a corresponding Cloud Function to create custom behavior in response to changes in your spending

While both of these techniques require more work on your part, they give you the power to control exactly what kinds of alerts you're receiving and how to respond to them.

This page offers an overview for each of these approaches.
| All Firebase projects are actuallyGoogle Cloudprojects behind the scenes, which means billing is shared across Firebase andGoogle Cloudand you can view the same project in both theFirebaseconsole and theGoogle Cloudconsole.
| When your project is on the Blaze pricing plan,[**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)using the console. You can use the[Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator)to estimate your monthly costs.
|
| Be aware that**budget alerts do*not*cap your usage or charges** --- they are*alerts* about your costs so that you can take action, if needed. For example, you might consider[using budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

## Create more sophisticated alerts withCloud Monitoring

Simple budget alert emails let you know when your overall billing has reached certain thresholds. However, you might also be interested in knowing whether individual services are increasing unexpectedly --- before they've had a chance to significantly affect your budget. For more sophisticated use cases like this, we recommend learning aboutCloud Monitoring, which is aGoogle Cloudtool available for your Firebase project.

Cloud Monitoringis useful for several different types of alerts:

- If a resource that your project relies upon is unavailable (for both Firebase andGoogle Cloudservices, but even for external services, like AWS)

- If services likeCloud Functionsare taking longer than expected to respond

- If yourCloud Storagebucket,Realtime Databaseinstance, orCloud Firestoreinstance is rejecting too many requests (an indication that yourFirebase Security Rulesmight be incorrect).

- If the amount of resources used by some of your Firebase products have increased above a certain threshold

Alerts created throughCloud Monitoringare usually sent more quickly than simple budget alert emails, which are typically sent once per day. Alerts can take the form of SMS messages, Slack channel messages, PagerDuty notifications, webhooks, and more. These options enable you to send alerts with higher and more actionable levels of visibility.

### UsingCloud Monitoring

To get started withCloud Monitoring, we recommend starting with the[Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer), which allows you to create graphs of custom metrics within your Firebase/Google Cloudproject and visualize their usage.

Specifically, you can look at resources such as yourCloud Firestore,Realtime Database, or Cloud Function instances. You can view usage information about these products (like number of document reads, bytes sent, or function invocations) that would have an effect on your billing.

After you're comfortable visualizing your resource usage in the Metrics Explorer, we recommend creating an[alerting policy](https://cloud.google.com/monitoring/alerts)on the metrics you care about most. Here are some example alerting policies:

- If the number of document reads in a 30-minute time period is greater than a particular value

- If the usage of a specific resource (like a function invocation) seems to be increasing too quickly in a certain timeframe

## Create additional billing logic

Budget alerts send out emails automatically when your budget reaches certain thresholds, but for more sophisticated alerting or programmatic reactions to spending increases, you might consider setting up additional custom logic based onGoogle CloudPub/Submessages.

For example, you can send alerts to Slack channels or via text message, or you make programmatic changes to your app or project depending on spend levels.

Pub/Subis a message-passing service that allows other services to send messages --- usually in the form of JSON data --- in an asynchronous manner through channels known asPub/Subtopics. You can set up authorized services, likeCloud Functions, to listen to messages in these topics and act on the data appropriately.

Note thatPub/Subnotifications for billing are sent about once every 20 minutes whether or not your billing usage has changed, and they are stateless (meaning that they provide no context as to what preceded them). If you want to keep track of unusual increases in spending over time, or compare your spending to the previous cycle, you will need to manage that historical data yourself using a database likeCloud Firestoreor theRealtime Database.

### UsingPub/Subtopics withCloud Functions

You can set up aPub/Subtopic for your billing data by visiting the budget associated with your Firebase project in theGoogle Cloudconsole (under*Billing* \>*Budgets and alerts* ), then clicking the checkbox for**Connect aPub/Subtopic to this budget** . This will create aPub/Subtopic that you can listen to later. For detailed steps, refer to the[full documentation](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications).

After you've created yourPub/Subbilling topic, you can write a Cloud Function to listen to this topic and act on the data accordingly. The data is sent as JSON data and includes helpful information like the amount you've spent so far, your budget amount, and the start date of your current billing cycle.

TheGoogle Clouddocumentation has full details on how to receive this data using a Cloud Function. However, if you're usingCloud Functions for Firebaseto deploy your functions, the general process is a little simpler (check out the[Firebase documentation](https://firebase.google.com/docs/functions/pubsub-events)). You can also refer to[this video](https://www.youtube.com/watch?v=NWrZwXK92IM)for a sample walkthrough of the process.

Once you've received this data, there are a number of different ways you can respond to it. Here are some options:

- [Sending alerts to Slack channels](https://cloud.google.com/billing/docs/how-to/notify#set_up_a_slack_channel_and_permissions), Discord channels, or sending text messages when your spending has reached a certain threshold.

- Analyzing your spending compared to historical data and alerting you if anything seems out of the ordinary

- [Making changes to your app viaRemote Config](https://firebase.google.com/docs/remote-config/automate-rc)if billing levels have gotten too high

- Disabling your Firebase project entirely by[programmatically removing your billing service](https://cloud.google.com/billing/docs/how-to/notify#cap_disable_billing_to_stop_usage)from your account