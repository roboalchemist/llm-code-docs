# Automate collection runs on a schedule

Instead of running collections manually, Postman can run collections for you on a schedule. Use the Collection Runner to select a collection and configure a schedule. For example, you can run a collection that tests the functionality of your API every day at a specific time.

When you schedule a collection run with the Collection Runner, the scheduled run is added to the **Runs > Scheduled** tab in the collection. From here you can view, pause, edit, and delete scheduled collection runs.

You can also schedule collection runs with [monitors](/docs/collections/running-collections/scheduling-collection-runs-monitors/). Schedule runs with monitors when you want to set up alerts, like triggering on-call alerts for failures. For all other use cases, such as automating API tests, schedule runs with the Collection Runner.

## About scheduled collection runs

When working with scheduled collection runs, keep in mind the following:

- Scheduled collections run in the Postman Cloud, not locally.
- Scheduled runs don't support requests that use files in your local [working directory](/docs/getting-started/installation/settings/#working-directory) to send [body data](/docs/sending-requests/create-requests/parameters/). Instead, [upload your test data files](/docs/sending-requests/create-requests/test-data/) to make them available for scheduled runs in the cloud.
- Schedules share permissions with their collections. For example, if you have permission to edit a collection, you can edit that collection's schedules.
- You can schedule collection runs in personal, private, and team [workspaces](/docs/collaborating-in-postman/using-workspaces/create-workspaces/).
- If you import or export a collection, its schedules don't import or export with it. However, if you delete a collection, its schedules are also deleted.
- Scheduled collection runs share the same [usage limits as monitors](/docs/monitoring-your-api/monitor-usage/).
- Scheduled runs don't support OAuth 2.0 authentication. To learn how to use an OAuth 2.0 token with scheduled runs, see [OAuth 2.0 overview](/docs/sending-requests/authorization/oauth-20/#oauth-20-overview).

You can run collections with scripts that import packages from your team's [Postman Package Library](/docs/tests-and-scripts/write-scripts/packages/package-library/). Learn how to [add packages](/docs/tests-and-scripts/write-scripts/packages/package-library/#add-a-package) to the package library, and [import packages](/docs/tests-and-scripts/write-scripts/packages/package-library/#import-a-package) into your scripts.

## Schedule a collection run

You can schedule a run for the requests in a [collection](/docs/collections/use-collections/create-collections/) or a [folder](/docs/collections/use-collections/manage-collections/#add-folders-to-a-collection).

1. Click **Collections** in the sidebar and select the collection or folder you want to schedule.
2. Click ![Image 1: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Run**.
3. ![Image 2: Select Run from the collection overview](https://assets.postman.com/postman-docs/v11/collection-runner-button-v11.jpg)
    
    You can also click ![Image 3: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Runner** from the Postman footer and drag a collection from **Collections** or **History** in the sidebar.
    
4. On the **Functional** tab, click **Schedule runs**.
    
    ![Schedule runs](https://assets.postman.com/postman-docs/v10/schedule-runs-v10-13.jpg)
    
5. Choose any configuration options:
    
    - **Schedule name** - A name for your scheduled run.
    - **Run Frequency** - When and how often you want the collection to run.
    - **Environment** - (Optional) The [environment](/docs/sending-requests/variables/managing-environments/) with variables you want the collection to use.
    - **Iterations** - The number of times to run the collection.
    - **Data** - A [data file](/docs/collections/running-collections/working-with-data-files/) for the scheduled run.
    - **Notification recipients** - Up to five team members who will receive notifications for the scheduled run.
    
    - **Advanced settings**
        - **Retry if run fails** - Select this checkbox to retry a request after it fails, and enter the number of times to retry the request. Each retry counts toward your [monitoring usage](/docs/billing/resource-usage/#monitoring-usage).
        - **Set request timeout** - Select this checkbox to skip a request after it times out, and enter the timeout period in milliseconds. A scheduled run can't exceed a total duration of 15 minutes.
        - **Set delay before requests** - Select this checkbox to wait before sending requests, and enter the interval delay in milliseconds.
        - **Follow redirects** - Clear this checkbox to prevent requests that return a 3xx series response from automatically redirecting.
        - **Enable SSL validation** - Clear this checkbox to prevent Postman from checking the validity of SSL certificates when making requests.
    
6. By default, your requests run in the sequence they're listed in the collection. If you need to change the run order, click and drag a request to its new location in the order. You can also remove an individual request from the run by clearing the checkbox next to its name. For more information, see [Change run order](#change-run-order).
7. Click **Schedule Run**.

Requests sent by scheduled collection runs are deducted from your maximum number of monitoring API calls. For more information about checking your monitor usage, see [Manage monitor usage in Postman](/docs/monitoring-your-api/monitor-usage/).

## View a scheduled run

You can view the results of past scheduled runs.

1. Click **Collections** in the sidebar and select the collection with the scheduled run you want to view.
2. Select the **Runs > Scheduled** tab.
3. Hover over a scheduled run and click **View**.
    
    ![Runs tab](https://assets.postman.com/postman-docs/v11/scheduled-runs-tab-view-v11-10b.jpg)
    
4. Each column in the graph represents an individual run. Click a column to view test results and the Console log for that run. For more information see [View scheduled collection runs in Postman](/docs/collections/running-collections/viewing-scheduled-collection-runs/).
    
    ![Scheduled runs view results](https://assets.postman.com/postman-docs/v11/view-scheduled-run-results-v11a.jpg)

## Manually run a scheduled run

When a scheduled run is triggered manually, it runs in the Postman Cloud. Running scheduled runs manually is useful when you are fixing bugs or reproducing issues.

1. Click **Collections** in the sidebar and select the collection with the scheduled run you want to run manually.
2. Select the **Runs > Scheduled** tab.
3. Hover over a scheduled run and click **View**.
    
    ![Scheduled runs tab](https://assets.postman.com/postman-docs/v11/scheduled-runs-tab-view-v11-10b.jpg)
    
4. Click **Run**.
    
## Pause or resume a scheduled run

When you pause a scheduled run, Postman won't run the collection again until you resume the schedule.

1. Click **Collections** in the sidebar and select the collection with the scheduled run you want to pause or resume.
2. Select the **Runs > Scheduled** tab.
3. Hover over a scheduled run, click ![Image 10: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** and select **Pause** or **Resume**.
    
    ![Scheduled runs tab](https://assets.postman.com/postman-docs/v11/scheduled-runs-more-actions-v11-10b.jpg)
    
## Edit a scheduled run

1. Click **Collections** in the sidebar and select the collection with the schedule you want to edit.
2. Select the **Runs > Scheduled** tab.
3. Hover over a scheduled run, click ![Image 11: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**, and click **Edit**.
    
    ![Scheduled runs tab](https://assets.postman.com/postman-docs/v11/scheduled-runs-more-actions-v11-10b.jpg)
    
4. Make any changes to the scheduled run, then click **Save Changes**.
    
## Change run order

You can send the requests in a collection in different combinations or sequences to simulate various workflows. In the Collection Runner, change the order of requests by dragging them, or clear the checkbox next to a request to skip it.

When you schedule a collection run, you can change the order of your requests and save the custom order to run on a schedule. In this way, you can use the same collection to automate multiple tests scenarios.

To change the request order in a scheduled run, do the following:

1. Click **Collections** in the sidebar and select the collection or folder you want to schedule.
2. Click ![Image 12: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Run**.
    
    ![Image 13: Click Run from the collection overview](https://assets.postman.com/postman-docs/v11/collection-runner-button-v11.jpg)
    
    You can also click ![Image 14: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Runner** from the Postman footer and drag a collection from **Collections** or **History** in the sidebar.
    
3. On the **Functional** tab, click **Schedule runs**.
    
    ![Image 15: Schedule runs](https://assets.postman.com/postman-docs/v10/schedule-runs-v10-13.jpg)
    
4. Under **Run Order**, change the order by dragging and dropping requests. Skip a request by clearing its checkbox.
    
    ![Image 16: Custom run order](https://assets.postman.com/postman-docs/v11/scr-custom-order-v11.gif)
    
5. Click **Schedule Run**.

On the **Runs > Scheduled** tab, the message **Custom run order** indicates a scheduled run uses a custom request order. If a request is added or deleted from a scheduled collection, a **Review Changes** link appears next to the scheduled run. Click the link to review and edit the changes.