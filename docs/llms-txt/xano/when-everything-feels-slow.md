# Source: https://docs.xano.com/troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# When Everything Feels Slow

## When every request feels slow

### Step 1. - Check if your server is being overloaded with requests

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/338254ca-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=7db153e5d89ddfa108f866e08debfb21" width="1648" height="466" data-path="images/338254ca-image.jpeg" />
</Frame>

**A. Look at Instance Usage** - When you log into Xano, the Instance Dashboard will reflect where there might be a usage spike based on your capacity. This is a near real-time graph (delayed by a few min) of the last 24 hours. Ideally, you want to keep things below 50% at all times, but if you aren't on the appropriate Scale plan, usage spikes could push your Database and API capacity up.

* **If Database usage is high** - When the Database (blue) request line is high as shown above, this usually means that your Database is not optimized or indexed properly. Please visit the [Database performance](/the-database/database-performance-and-maintenance) section to look at ways to fix the tables that are being queried. Usually, API usage goes hand-in-hand with Database usage, so it isn't surprising to see them at the same level in the above example. Once fixed, you should see both Database and API usage go down.

* **If API usage is high** - When the API usage is high on its own, this usually indicates that there is a traffic spike and your server is running out of capacity. This normally happens when multiple users are trying to request data from your API at the same time. You can increase your capacity by upgrading to a different Scale package.

If you need hands-on private help diagnosing this, you can schedule a [premium support call](/troubleshooting-and-support/getting-help) with one of our Xano team members.

**B.** **Instance Stats** You can see the volume of requests happening across all your workspaces here. This is also across a 24-hour window and is updated every hour. If you see a large volume of requests as pictured above, proceed to step 2 to see where it's coming from.

To dig deeper into the details of each request, you can proceed to Step 2 below.

### Step 2. Look at the API requests for each workspace

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d9d5a943-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=cb60b135a5d01831231ab09dea47f935" width="1693" height="1162" data-path="images/d9d5a943-image.jpeg" />
</Frame>

Each workspace has a dashboard item of request history. **Click DETAILS** at the top right of the graph to see each request.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2b464148-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=3bdd4c05e0b96077bb9bf356f13fd41b" width="508" height="851" data-path="images/2b464148-image.jpeg" />
</Frame>

\*\*A. \*\*You can filter down the requests that are taking the longest. Select the magnifying class to do this. A good rule of thumb is to select requests that are **greater than 5s**.

**B.** You can click the refresh button to ensure you're getting the latest data.

**C.** Click on the request that takes a long time to show the details. [*How to diagnose a slow API endpoint*](/troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow#when-a-single-api-endpoint-feels-slow)


Built with [Mintlify](https://mintlify.com).