# View monitor results

[Monitors](/docs/monitoring-your-api/setting-up-monitor/) continuously track the health and performance of your APIs. With Postman, you can stay up to date on what's happening across all monitors in your workspace. Or you can review individual monitors to examine test results and performance over time.

You can view your monitors in Postman by navigating to your workspace and clicking **Monitors** in the sidebar. Select your monitor to open a tab detailing its latest performance.

![View monitor in tab](https://assets.postman.com/postman-docs/v11/view-monitor-in-tab-v11.png)

Monitors are visible to all members of the workspace.

## Monitor summary

You can use the monitor summary to understand how your APIs have performed over time. Each monitor run is represented by a bar in the graph. By default, this displays the monitor's **Run summary** view.

The upper section charts your monitor's average response time for each run, while the lower section visualizes the number of failed tests for each run across all regions. To view the exact values for failed percentage and response time, hover over each run individually.

![Monitor summary](https://assets.postman.com/postman-docs/v11/monitor-summary-with-hover-v11.jpg)

A red bar indicates that either tests failed or errors occurred during the run. For more information, view your [Console Log](/docs/monitoring-your-api/viewing-monitor-results/#console-log).

### Individual requests

You can select **Individual requests** to break down your monitor summary into separate requests.

![Request split](https://assets.postman.com/postman-docs/v11/monitors-individual-requests-v11.jpg)

## Filters

You can use filters to identify recurring patterns in your monitoring runs by selecting particular requests, run types, results, and regions (if applicable).

You can **Clear Filters** to return to your original dashboard view.

### Filter by request

You can filter by request to compare an individual request's response time in different runs. Select **All Requests** under **Filter By**, then select your request.

### Filter by type

You can filter by run type to compare how the response time changes between manual runs, scheduled runs, webhook runs, and Postman CLI runs. Click **Type: All**, then select the type of run you'd like to analyze further.

Manual runs are initiated in Postman or are triggered by the [Postman API](https://www.postman.com/postman/postman-public-workspace/request/80oupaf/run-a-monitor). Scheduled runs are initiated by the schedule you set when creating or editing your monitor. Webhook runs are initiated by integrations you've created. Postman CLI runs are triggered by the [`postman monitor run` command](/docs/postman-cli/postman-cli-options/#postman-monitor-run).

### Filter by run result

Each run is labeled based on its result:

* **Successful** - Your monitor completed the run with no issues and passed all tests.
* **Failure** - Your monitor completed the run, however one or more tests failed.
* **Error** - Your monitor was unable to complete its run due to an error. An error can occur if there is a syntax error in the code you've written, a network error, or for various other reasons. If you get an error, your [Console Log](#console-log) will help you identify what caused it.
* **Abort** - Your monitor timed out because it didn't complete its run within the allotted 10 minutes (Postman Free plans) or 15 minutes (Postman paid plans).

You can filter by run result to compare how your runs with the same result have differed. Click **Run result: All**, then select one or more types of run results to view.

### Filter by region or runner

You can filter by [regions or runners](/docs/monitoring-your-api/setting-up-monitor/#add-regions-and-runners) to compare API health or performance across multiple geographic regions or networks. Click **All Runners**, then select a region or runner to view its results.

This feature is available if you selected multiple regions or runners when you created or last edited your monitor. Learn more about [regions and runners](/docs/monitoring-your-api/setting-up-monitor/#add-regions-and-runners).

### Filter by formula

You can filter by mathematical formula to view the average, sum, minimum, and maximum response time for each run:

* **Average** - The average of the total response time across all regions.
* **Sum** - The sum of the response time across all regions.
* **Minimum** - The minimum total response time for a run across all regions.
* **Maximum** - The maximum total response time for a run across all regions.

Click **Average** to open the menu, then select an option. To view the calculated response time value, you can hover over each run individually.

## Time traverse

You can review past run results to understand what happened at a particular point in time. To do so, click **Go to** in the upper-left corner of the monitor summary or request split graph. Select the time and date, then click **Apply** to view a specific run.

![Time traverse](https://assets.postman.com/postman-docs/v11/monitors-time-traverse-v11.jpg)

To revert the view to your most recent runs, select the time and date you defined in the upper-left corner of the graph, then click **Reset**.

## Test results

Click **All Tests** to get more detailed information on your tests, including which passed or failed, the response codes, the response times, and any failed test assertions.

![Test results](https://assets.postman.com/postman-docs/v11/view-monitor-results-test-v11-75.png)

To learn more about the test results for each request, you can view the following:

* View the test results for a particular region by selecting it from the **Region** dropdown list. You can select a different region if your monitor is configured to run in multiple regions.
* Click the **All Tests** tab to view all requests in the monitor with tests that passed or failed, including requests without any tests. Click the **Passed**, or **Failed** tab to only view requests with tests in that category. The number of tests in that category appears next to each tab.
* Next to each request you can view the response code, time, and size.
* Next to each request you can view the number of tests that passed (green background) or failed (red background). Hover over one of these numbers to view a detailed breakdown of the tests in the request.
* Click a request to view which tests passed or failed.
* Click the name of a request to open the request in a new tab.
* If your requests are in a folder, click the name of the folder to open it in a new tab.

## Errors

* Click the **Errors** tab to filter results by requests that encountered errors. Note that _errors_ indicate runtime issues like timeout or TLS handshake errors. _Failed_ requests occur when one or more user-specified checks (like post-request scripts) don't match expectations.
* The requests in your collection run that have errors appear in the run results page with an error badge and the error message. Badges identify errors as related to **NETWORK**, **REQUEST**, or **SCRIPT** issues.

    ![Monitor errors](https://assets.postman.com/postman-docs/v11/monitor-errors-v11-75.png)

## Console log

Click the **Console Log** tab to view and search monitor run details along with the [`console.log`](/docs/sending-requests/response-data/troubleshooting-api-requests/) statements that run as part of your pre-request and post-response scripts in the Postman Console. Run details specify the various stages of a monitor run such as preparing run, running, rerunning ([if applicable](/docs/monitoring-your-api/setting-up-monitor/#use-retry-on-failure)), and the run result, along with error and test failure information. Selecting a request in the Console log will open it in a tab, allowing you to review and edit the request as needed.

If your monitor is configured to run in multiple regions, you can view the Console logs for a particular region by selecting it from **Region**.

![Console log](https://assets.postman.com/postman-docs/v11/monitor-view-console-log-v11-75-1.png)

You can use the Console to both troubleshoot issues and learn more about an individual run's behavior.

Find specific strings with the Console log's search feature. Searching enables you to highlight and cycle through error messages and codes automatically instead of scanning the log manually.

Click **Search console logs** and enter a string. Matches are highlighted in the log, and you can click ![Down Large icon](https://assets.postman.com/postman-docs/aether-icons/direction-down-large.svg#icon) **Next match** and ![Up Large icon](https://assets.postman.com/postman-docs/aether-icons/direction-up-large.svg#icon) **Previous match** to cycle through them. Click ![Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) **Clear search** to clear the search field and results.

**Monitor run logs are retained for a period of six months.** If you select a monitor run that's outside the retention period, you can view the number of failed tests and errors. Other monitor run details will no longer be available. To request this information, contact [Postman support](https://www.postman.com/support/).

## Activity feed

You can view a monitor's activity by clicking the activity feed icon ![Activity feed icon](https://assets.postman.com/postman-docs/icon-activity-feed-v9.jpg#icon) in the upper-right corner.

![Activity feed](https://assets.postman.com/postman-docs/v11/monitor-activity-feed-v11.jpg)

You can check these logs to learn when a monitor was created, edited, paused, or resumed running, and which team member performed each action.

## Monitor details

You can view details about a monitor by clicking the information icon ![Information icon](https://assets.postman.com/postman-docs/icon-information-v9-5.jpg#icon) in the upper-right corner. Here you can view a monitor's ID, creator, creation date and time, collection, environment, and integration options.

![Monitor details](https://assets.postman.com/postman-docs/v11/monitor-information-v11.jpg)

## Troubleshooting

Learn how to [troubleshoot your monitors](/docs/monitoring-your-api/troubleshooting-monitors/) and check out [Postman monitoring FAQs](/docs/monitoring-your-api/faqs-monitors/).