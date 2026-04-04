# Source: https://firebase.google.com/docs/projects/billing/avoid-surprise-bills.md.txt

Whether you're just starting out developing your app or you have a full-blown production app, you want to make sure you understand your costs and how to avoid surprise bills.

If you haven't already, check out the[Firebase pricing plans](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans)to understand how billing for works for Firebase.
**Important:** **Firebase pricing plans apply to the entire project, not just to individual apps registered in the project.** When you're determining which pricing plan is right for you, consider the usage from*all the apps* registered in the same project. Learn more about[best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices)for when to add multiple apps to the same Firebase project.  

This page guides you through important aspects of understanding and monitoring your usage and spend levels, including:

- [Testing your code](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#test-code)
- [Viewing your usage and spending levels](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#view-usage-and-spending-levels)
- [Setting up budget alert emails](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)

*** ** * ** ***

## Test your code

Testing your code before deploying to production is a great idea for many reasons, like catching errors that might cost you significant amounts of money. As you're building the infrastructure for your app,**we highly recommend first testing locally using the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite)**.

TheLocal Emulator Suiteallows you to run instances ofCloud Functions,Cloud Firestore, theRealtime Databaseand more all locally on your desktop machine. This not only makes it easier for you to quickly iterate on new functionality --- particularlyCloud Functions--- but it also ensures that you don't incur any Firebase costs that might result from testing against services in production.

As you're testing, check for these common causes of exceeding expected usage and spend:

- Forgetting to add a limit to a database query with millions of results

- Combinations ofCloud Functionsthat cause excessive fan-out workloads or even infinite loops

<br />

*** ** * ** ***

<br />

## View your usage and spending levels

You need to know what normal usage patterns look like for your app and make sure you're staying within thresholds important to you.
| Most Firebase products provide product-specific documentation about usage, quotas, and pricing. They also often provide usage-to-billing examples for the product. Visit a product's section in the Firebase documentation to find this type of information.
|
| For example, here's documentation to[understand billing forCloud Firestore](https://firebase.google.com/docs/firestore/pricing).

### View individual product usage

You can view individual product usage in the "Usage" tab for many products in theFirebaseconsole.

- You can view specific date ranges in these dashboards.

- Product-level dashboards are available for[Authentication](https://console.firebase.google.com/project/_/authentication/usage)and all the infrastructure products:[Realtime Database](https://console.firebase.google.com/project/_/database/usage),[Cloud Firestore](https://console.firebase.google.com/project/_/firestore/usage),[Cloud Storage](https://console.firebase.google.com/project/_/storage/usage),[Cloud Functions](https://console.firebase.google.com/project/_/functions/usage), and[Hosting](https://console.firebase.google.com/project/_/hosting/usage).

### View overall project usage

You can view your project's overall usage in the[*Usage and billing*dashboard](https://console.firebase.google.com/project/_/usage)in theFirebaseconsole (go to*Project Settings* \>*Usage and billing*).

- You can view your monthly usage and how your usage levels are measuring up to the allocated no-cost usage quota.

- Click into any product to review a daily summary of usage and how it measures up to the allocated no-cost usage quota.

Remember that each product has different usage quotas and thus different timelines, for example:

- Cloud FirestoreandCloud Storageusage are calculated daily.

- Cloud Functionsusage is calculated monthly.

<br />

*** ** * ** ***

<br />

## Set up budget alert emails

Avoid surprises on your bill by creating budgets inGoogleCloud Billingand setting up budget alerts.

- *Budgets*are general monetary amounts that you plan on spending each month.

- *Budget alerts*are email notifications sent to your team if your project exceeds a set spending threshold.

| Be aware that**budgets and budget alerts do*not*cap your usage or charges** and that there's a delay between incurring costs and receiving a budget alert (depending on the service, up to a few days). Budgets and budget alerts are intended to help you monitor your spending and to*alert* you about your costs so that you can take action, if needed. For example, you might consider[using budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

By default, Firebase andGoogle Clouddon't turn off services and usage based on your budget and thresholds because although you*might*have a bug in your app causing an increase in charges, you might just be experiencing unexpected positive growth of your app. You don't want your app to shut down unexpectedly when you need it to work the most.

You might already have a budget alert if you upgraded to a Blaze pricing plan recently. But if you want to learn more about budget alerts, set up a new alert, or modify an existing alert, this section is for you!
| [All Firebase projects are actuallyGoogle Cloudprojects](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship)behind the scenes, which means billing is shared across Firebase andGoogle Cloudand you can view the same project in both theFirebaseconsole and theGoogle Cloudconsole.

### Set up a budget and a basic budget alert

This section describes budgets and budget alerts at a high-level with a Firebase-context. For detailed information, make sure to check out[Set budget alerts](https://cloud.google.com/billing/docs/how-to/budgets)in theGoogle Clouddocumentation.
| **Note:** To set up a budget or a budget alert, you need to be an Owner of the associatedCloud Billingaccount.

Here's how to set up a budget and a basic budget alert:

1. Navigate to the budget settings:

   1. Access your project in theFirebaseconsole, then go to the**Usage and billing** \>[**Details \& settings**page](https://console.firebase.google.com/u/0/project/_/usage/details).

   2. In the**Budgets \& Alerts** section, click**Create first budget** . This takes you to the**Budgets \& alerts** page in theCloudconsole.

      Note that if you already have a budget set up, you'll see it here instead of the "Create first budget" link.
2. Complete the following steps to set up a budget and an emailed budget alert:

   1. Select an existing budget or create a new one.

   2. Give your budget a descriptive name.

   3. Set the scope for the budget alert, including the project(s) and service(s) that you want the budget alert to apply to. You probably want to select*All services*when getting started with budget alerts.

   4. Set the*Amount* \>*Budget type*using one of these options:

      - **A set amount of money**-- use this type when you're first starting out or testing your app

      - **An amount equal to what your project spent last month**-- use this type when your app is growing steadily and you don't want to keep updating the budget amount every month

   5. Set up*Percent of budget*alerts.

      - For initial testing, try out several percentages, like 1%, 2%, 5%, and 50% of*Actual*.

      - For production apps, try out pivotal percentages, like 50% and 100% of*Actual* as well as 150% of*Forecasted*.

      | **Tip:**Set a limited number of alert thresholds for your production apps. You want to be informed, but you don't want so many email notifications that you stop paying attention to them.
   6. Set up who should get emails.

      - By default, anyone with the appropriate billing permissions gets the notification email (by default, Billing Account Administrators and Billing Account Users on the associatedCloud Billingaccount).

      - You can also send emails to other people on your team. This requires creating aCloud MonitoringWorkspace and then adding an email-based notification channel to the*Alerting* section of the workspace. For more information about this setup, visit[Set up advanced billing alerts and logic](https://firebase.google.com/docs/projects/billing/advanced-billing-alerts-logic).

If you set up a notification for a low*Percent of budget*(like 1%), you should get an email within a couple hours or a couple of days telling you that your project has hit that threshold.

## Next steps

- Consider using[budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

- Visit[Set up advanced billing alerts and logic](https://firebase.google.com/docs/projects/billing/advanced-billing-alerts-logic)to learn how to do the following:

  - UseCloud Monitoringto create more sophisticated alerts for billing and usage, including custom alerts that send notifications to other mediums, like Slack.

  - Create additional billing logic based onGoogle CloudPub/Sub.