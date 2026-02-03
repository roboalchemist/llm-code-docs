# Configure and run performance tests in Postman

Use the _Collection Runner_ to test the performance of your API with the same requests and collections you use for [functional API tests](/docs/collections/running-collections/intro-to-collection-runs/). When you run a performance test, Postman uses the requests in the selected collection to simulate the activity of your API users.

In the Collection Runner, you can set the duration of the test and the number of _virtual users_. Each virtual user runs the requests in the specified order in a repeating loop. All of the virtual users operate in parallel to simulate real-world load on your API. You can choose whether the number of virtual users is fixed for the duration of the test or ramps up and down during the test.

## Configure a performance test

> **Use the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/) to configure and run performance tests.** You can't use the Postman web app for performance testing. During a performance test, all requests are sent from the host computer where you are running the Postman desktop app.

Before you configure a performance test, [create a collection](/docs/collections/use-collections/create-collections/) or [add a folder](/docs/collections/use-collections/manage-collections/#add-folders-to-a-collection) with the requests you want to use to simulate user activity. Each virtual user runs the selected requests in the specified order and repeats the sequence throughout the test. Multiple virtual users all operate in parallel to simulate real-world usage of your API.

To configure a performance test in the Postman desktop app, do the following:

1. Click **Collections** in the sidebar and select the collection or folder you want to use for performance testing.
2. On the **Overview** tab, click \[![Image 1: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon)\] **Run**.
3. ![Image 2: Click Run from the collection overview](https://assets.postman.com/postman-docs/v11/collection-runner-button-v11.jpg)
    
    You can also click \[![Image 3: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon)\] **Runner** from the Postman footer and drag a collection from **Collections** or **History** in the sidebar.
4. Select the **Performance** tab.
5. (Optional) Change the order in which the requests are run by dragging a request to a new location. To skip a request, clear the checkbox next to its name.
6. Select a **Load profile**.
    * **Fixed** - The maximum number of virtual users is used throughout the test.
    * **Ramp up** - Enter an **Initial load** and drag the handles to adjust the length of the ramp up period. During the ramp up period, the number of virtual users increases from the initial load to the maximum.
    * **Spike** - Enter a **Base load** and drag the handles to adjust the duration of the spike. During the spike, the number of virtual users increases from the base load to the maximum, then decreases back to the base load.
    * **Peak** - Enter a **Base load** and drag the handles to adjust the duration of the peak. During the peak, the number of virtual users increases from the base load to the maximum, holds steady, then decreases back to the base load.
7. Enter the number of **Virtual users**. While the test is running, each virtual user runs the selected requests in the specified order in a repeating loop. A higher number of virtual users puts increased load on your API.
8. Enter the **Test duration** in minutes.
9. (Optional) Select a **Data file** with custom values to use for each virtual user. The file must be in CSV or JSON format. Learn more about [using a data file to simulate virtual users](/docs/collections/performance-testing/performance-test-data-files/).
10. (Optional) Click **Pass test if** to set a metric, condition, and value that determines whether the test passes or fails.
    * **Metric** - Select the performance metric:
        * **Avg. Response Time** - The response time of all requests averaged together, in milliseconds.
        * **p90** - The 90th percentile of response times, in milliseconds.
        * **p95** - The 95th percentile of response times, in milliseconds.
        * **p99** - The 99th percentile of response times, in milliseconds.
        * **Error %** - The percentage of requests that result in an error. Errors indicate runtime issues such as timeouts, connection or TLS failures, or uncaught exceptions in user scripts.
        * **Requests per second** - The number of requests sent each second during the performance test.
    * **Condition** - Select the condition that must be met for the test to pass.
    * **Value** - Enter a number that must be met for the test to pass.
    
    Later performance runs with the same collection will have the metric, condition, and value autofilled from the previous run.
    
11. When you're ready to begin the performance test, click **Run**.
    
    * You can view real-time performance metrics while the test is running. Learn more about [viewing performance test metrics](/docs/collections/performance-testing/performance-test-metrics/).
    * After the test completes, you can view details for any [errors](/docs/collections/performance-testing/performance-test-errors/) or [test assertion failures](/docs/collections/performance-testing/performance-test-failures/) that occurred during the performance test.
    
    ![Image 4: Configuring a performance test](https://assets.postman.com/postman-docs/v11/performance-test-configure-v11-40.jpg)
    
    Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of performance runs you can use each month. A message will display in the Collection Runner when you're approaching your usage limit. Learn more about [resource usage](/docs/billing/resource-usage/#performance-test-limit) in Postman.
    
## Virtual users and system resources

The number of virtual users a performance test can simulate depends on available system resources and the collection used for the test. Using pre-request or post-response scripts will reduce the number of virtual users that can be simulated.

Attempting to simulate a higher number of virtual users than your system resources can support may cause inaccurate metrics and reduced throughput (requests per second). Try running a small test with 10 to 20 virtual users and observing system resource usage.

During a performance test, an in-app notification may warn you that your system resources are approaching their threshold. If your system resources exceed their threshold, you'll receive an in-app notification with this warning and the performance test stops running.

If you have a problem with the performance testing feature, contact the [Postman support team](https://support.postman.com/hc/en-us). Make sure to attach your [Postman logs](https://support.postman.com/hc/en-us/articles/360025298633-How-to-get-logs-from-the-Postman-Desktop-app) in your support request.

## Rename a performance run

You can change the name of a performance run while it's in progress, or you can rename a past run. Rename a performance run to help you identify runs later, for example, when [comparing performance runs](/docs/collections/performance-testing/performance-test-metrics/#compare-two-performance-runs).

To rename a performance run, [start a new run](#configure-a-performance-test) or [open a past run](#view-past-performance-runs). Click the name of the performance run and enter a new name.

![Image 5: Rename a performance run](https://assets.postman.com/postman-docs/v10/performance-test-rename-v10-24.jpg)

## View past performance runs

You can view a list of past performance runs for a collection. Open the collection, select the **Runs** tab, and then select the **Performance** tab.

You can view metrics for each run, including the number of virtual users (VUs), duration, total number of requests, requests per second, average response time, and error rate. Click the run to [view a graph and full details](/docs/collections/performance-testing/performance-test-metrics/) for the performance run.