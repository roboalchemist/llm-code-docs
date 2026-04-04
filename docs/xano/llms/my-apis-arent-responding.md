# Source: https://docs.xano.com/troubleshooting-and-support/my-apis-arent-responding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What to Do If Your APIs Aren't Responding

If you find that your APIs aren't responding, follow these steps to troubleshoot and resolve the issue.

<Tip>Xano automatically monitors your instance and sends email alerts to instance admins when potential downtime is detected. If you received an **Instance Down** alert, see [What to Do If Your Instance Is Down](/troubleshooting-and-support/my-instance-is-down#instance-down-alerting) for recommended next steps.</Tip>

## Check the Xano Status Page

Visit the status page of the service to see if there are any ongoing incidents or maintenance windows that might be affecting your instance.

<Card href="https://status.xano.com" title="Xano Status Page" description="Check for any ongoing incidents or maintenance." icon="signal-bars" />

<Note>Paid Xano instances have dedicated resources, which means issues impacting Xano as a whole are not likely to affect your instance.</Note>

## Check to see if your instance is accessible

If your instance is inaccessible, there are different troubleshooting steps involved. Head to the [instance selection screen](https://app.xano.com/instance?mode=master) and click on the <Icon icon="gear" /> next to your instance, and choose 'Connect' to see if you can still access your instance. If you can, continue with the steps below. If you can't, follow the steps in [What to Do If Your Instance Is Down](/troubleshooting-and-support/my-instance-is-down).

If you're trying to access your instance via a custom domain, try accessing it using the method described above to rule out any domain-related issues.

Symptoms:

* Instance selection screen shows 'An error has occurred'
* Unable to access instance via normal URL

## Check resource usage

From the [instance selection screen](https://app.xano.com/instance?mode=master), select your instance to enter the Instance Dashboard.

This dashboard will reflect where there might be a usage spike based on your capacity. This is a near real-time graph (delayed by a few minutes) of the last 24 hours.

* **If Database usage is high in spikes** - When the Database (blue) request line is running high (high meaning 70-80% or more) in short bursts, this usually means that your Database is not optimized or indexed properly. Please visit the [Database performance](/the-database/database-performance-and-maintenance) section to look at ways to fix the tables that are being queried. Usually, API usage goes hand-in-hand with Database usage, so it isn't surprising to see them at the same level in the above example. Once fixed, you should see both Database and API usage go down.

* **If Database usage is consistently high** - When the Database (blue) request line is running high (high meaning 70-80% or more) consistently over a long period of time, this usually means that your instance is having trouble with the amount of data being stored or the number of requests being made. You can increase your capacity by upgrading to a different plan, or adding a CPU Boost addon. In addition, ensuring your queries are optimized for performance will help reduce load on the database. Please visit the [Database performance](/the-database/database-performance-and-maintenance) section to look at ways to optimize your database tables and queries.

* **If API usage is high** - When the API usage is high on its own, this usually indicates that there is a traffic spike and your server is running out of capacity. This normally happens when multiple users are trying to request data from your API at the same time.

This could mean that your application is seeing more traffic than normal, but nothing is out of the ordinary. You can increase your capacity by upgrading to a different plan or adding a CPU Boost addon.

This could also mean that you have API endpoints that are not optimized and are consuming more resources than necessary. Please visit the [When a Single API Endpoint Feels Slow](/troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow#when-a-single-api-endpoint-feels-slow) section to look at ways to optimize your API endpoints.

This could also mean that a bad actor is making excessive requests to your API endpoints. If you suspect this is the case, please reach out to our support team for assistance.

Symptoms:

* APIs not responding or timing out
* APIs responding slowly


Built with [Mintlify](https://mintlify.com).