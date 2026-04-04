# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/js-errors.md

# JS errors

In case you have included JavaScript code in your agent, you can check for script errors (if any) in the **JS errors** page. Here, you can view errors related to SSML, live agent, channel, Regex entities, and JS errors across nodes. The link to the **JS errors** page is under **Debug** on the left navigation pane.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfrPMBOXxYiRplyNuh0WH%2Fimage%20copy.png?alt=media&#x26;token=60b9d431-fd0d-4f27-a72a-de36f468ef50" alt=""><figcaption></figcaption></figure>

Details provided about each of the errors in the list:

* **Type:** Indicates whether the JavaScript execution resulted in an Error or a Warning.
* **Message**: Indicates the message in the skill at the point of error.
* **Step**: Indicates the node number in the flow that caused the error.
* **Sender**: Indicates the details of the user or agent who sent the message.
* **Time**: Indicates the time the error was created, as per the system time.
* **JS error**: Indicates the details of the JS error.

Using the details displayed in the **JS errors** page, you can correct the JS errors in the conversation flow.

### Filter JS errors

**To filter the JS errors based on a date range**:

You can filter the error list to view only errors that occurred within a specific date range, up to 90 days.&#x20;

{% hint style="info" %}
**Note**: By default, errors that occurred in the last 30 days are displayed in the JS errors page.
{% endhint %}

1. Click on the date selection box to select a date range.&#x20;
2. The first three options allow you to select errors for the last 30 days, the previous 15 days, or the current date. The fourth option, which is a custom range, allows you to select errors for a date range that you specify.
3. To select errors for a custom date range, select the **Custom Range** option. In the calendar window, click on the start date of the date range. Then drag the mouse (do not click and drag; simply drag) to the end date of the date range, and click it. You have selected the date range. Finally, click **Apply**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fw1fTSNxgl7tDvEoQ9I0M%2Fimage.png?alt=media\&token=d71f2d14-aeb3-411a-8a74-8b8172336ab5)

The total number of errors for the agent is displayed at the top of the page. However, only 25 errors are listed per page. Use pagination to navigate and view other errors.

{% hint style="info" %}
**Notes**:

* You can use the **Clear All** option to clear all JS errors.
* The error messages are sorted in descending order by error creation time.
* All errors get displayed only when the specific cases are triggered in the conversation flow with a user query. For example, Regex entity error is displayed only when you use the entity in the conversation flow and it gets triggered in the conversation flow.
  {% endhint %}

**Filtering JS errors by type:**

You can filter the JS error list to view only **Errors** or only **Warnings**.\
To apply the filter, click the dropdown and select the desired error type, **Error** or **Warning**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfrPMBOXxYiRplyNuh0WH%2Fimage%20copy.png?alt=media&#x26;token=60b9d431-fd0d-4f27-a72a-de36f468ef50" alt=""><figcaption></figcaption></figure>

### Export JS errors to a CSV file

Using the **Export** option, you can download all the errors on the current page and other pages to a single CSV file. This can be used as a reference and for further analysis.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FN1SEMACSlQfSV2oRSizR%2FScreenshot%202022-04-20%20at%203.11.22%20PM.png?alt=media\&token=78023c57-8ccf-41a9-b4a8-82aed4001c55)

**To export JS errors to a CSV file**:

1. You can first filter the required data using the date range. See [Filter JS errors based on date range](#filter-js-errors-based-on-a-date-range), for more information.
2. Click **Export.**  A copy of the error file is downloaded to your local machine. Note that the **Time** for each error in the downloaded CSV file is in UTC timezone.
3. File exports include only the log results that match the currently applied filter.
