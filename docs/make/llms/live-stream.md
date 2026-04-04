# Source: https://developers.make.com/custom-apps-documentation/debug-your-app/make-devtool/live-stream.md

# Live Stream

Live Stream displays what is happening in the background once you've hit the **Run once** button.

You can view the following information for each module in your scenario:

* **Request Headers** (API endpoint URL, HTTP method, time and date the request has been called, request headers, and query string)
* **Request Body**
* **Response Headers**
* **Response Body**

After you run a scenario, select **Live Stream** from the left-side panel and click one of the tabs in the right panel of Make DevTool to view the desired information.

<div align="center"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-911a135472a1cf90dcdda564a97df02b8df73a8c%2Flivestream_devtool.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

## Search in Logs

Enter the search term in the search field in the left panel of Make DevTool to only display requests and responses that contain the search term.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-54bab6a70c37f881f3e1cc964a3357583c084afe%2Fcustomapps_makedevltool_livestream2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## **Clear the list of recorded requests**

To clear the list of requests recorded by Make DevTool, click the bin icon next to the search field.

## **Enable console logging**

To enable logging in the console, click the computer icon next to the search field.

When logging is enabled, the color of the computer icon switches to green.

![](https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-239d4a71220cffe75b97d5da6b0375f1eb7bb0d0%2FScreen%20Shot%202022-08-22%20at%2016.41.31.png?alt=media)

Click the same icon again if you want to disable logging. The icon turns gray when the feature is disabled.

## **Retrieve the request in the raw JSON format or cURL**

To retrieve the raw JSON content of the request, click the **Copy RAW** icon in the top-right corner of the DevTool's panel.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-37e34fa4bcf412b2c62b7aa3229f2a9e84e0fd5e%2Fcustomapps_makedevltool_livestream3.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Similarly, you can retrieve cURL using the **Copy cURL** button next to the **Copy RAW** button in the top-right corner of the Make DevTool's panel.
