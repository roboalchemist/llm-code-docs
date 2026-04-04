# Source: https://docs.base44.com/developers/app-code/editor/activity-monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Activity Monitor

> Monitor and debug your app's API requests and responses in realtime during development.

The Activity Monitor shows every request your app makes while you are in preview. Check which endpoints are called, see status codes and timing, and inspect request and response details to debug problems.

For each entry you can see the method, the path, when it happened, and the status code. Use the search field at the top left to filter by method, path, or other text.

## Access the Activity Monitor

To open the Activity Monitor:

1. Go to your app editor.
2. Click the **More Actions** icon (<Icon icon="ellipsis" />) at the top right.
3. Click **Activity Monitor**.

<Frame caption="Access the Activity Monitor from the More Actions menu">
    <img
      src="https://mintcdn.com/base44/sBFooTVX9PqzuSkM/images/activitymontior.png?fit=max&auto=format&n=sBFooTVX9PqzuSkM&q=85&s=fa6d4999b690a782ecdebbf74881b255"
      alt="Access the Activity Monitor from the More Actions
  menu"
      width="2530"
      height="1120"
      data-path="images/activitymontior.png"
    />
</Frame>

## Inspect a request

Click any entry in the list to see its details. The details panel has three tabs:

* **General**: Full URL, HTTP method, status code, total time, and timestamps.
* **Request**: What your app sent, including headers, query parameters, and request body.
* **Response**: What the endpoint returned, including headers, body, or error message.

<Frame caption="Inspect request details in the Activity Monitor">
    <img src="https://mintcdn.com/base44/ml9BQnGdt1cp4mqU/images/singlerequest.png?fit=max&auto=format&n=ml9BQnGdt1cp4mqU&q=85&s=2d95a171ee728780c7a7e43e6965c708" alt="Inspect request details in the Activity Monitor" width="2504" height="1146" data-path="images/singlerequest.png" />
</Frame>

Use this information to confirm your app sends the expected data and the backend returns what you expect.

For more on editing your app's code, see [Code Tab](/developers/app-code/editor/code-tab).


Built with [Mintlify](https://mintlify.com).