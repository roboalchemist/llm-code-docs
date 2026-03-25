# Source: https://docs-containers.back4app.com/docs/local-development/local-debugging.md

---
title: Debug Cloud Functions
slug: docs/local-development/local-debugging
description: Learn how to debug your cloud code functions locally with Parse Server.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-25T15:38:39.372Z
updatedAt: 2026-01-26T17:21:13.058Z
---

After creating and developing your application using Parse Cloud Code functions, there’s always room for improvement when it comes to testing and debugging. This guide will show you how to integrate your code editor with Node.js to debug your functions using a local Parse Server instance, simulating the Back4app environment.

## Goal

Enable you to debug your Parse Cloud Code locally in your preferred code editor.

## 1 - Preparing Your Project Files

If you are already hosting your application on Back4app or have set up Cloud Code via the dashboard, your project should follow this structure:

- `cloud`**&#x20;Directory**: Contains the `main.js` file where your Cloud Code functions are defined.
- `public`**&#x20;Directory**: Holds your static content such as HTML and JavaScript files, typically including an index.html file.

If your app is new or not yet deployed, replicate this structure to ensure the local Parse Server runs correctly.

## 2 - Running Your Parse Server Locally

To start a local instance of the Parse Server:

1. Navigate to your project directory in the terminal.
2. Run the following command to launch the server with a test database and your Cloud Code:

:::BlockQuote
parse-server --appId YOUR\_APP\_ID --clientKey YOUR\_CLIENT\_KEY --masterKey YOUR\_MASTER\_KEY --databaseURI mongodb://localhost/test --cloud ./cloud/main.js --verbose
:::

- Replace the placeholder values (`YOUR_APP_ID`, etc.) with random values. Avoid using your production keys.

1. Verify that the server is running by opening `http://localhost:1337/parse` in your browser. An "unauthorized" error means the server is running but the request lacks authentication keys.

## 3 - Setting Up and Testing Cloud Code

Ensure all your Cloud Code functions are located in the `cloud/main.js` file. For example:

:::CodeblockTabs
main.js

```javascript
Parse.Cloud.define("debugTest", (request) => {
  return "Testing!";
});
```
:::

Restart the Parse Server to load the new function:

:::BlockQuote
CTRL+C # to stop the server
parse-server --appId ... # rerun the command
:::

Now, test the function using cURL in the terminal:

```curl
curl -X POST \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-Client-Key: YOUR_CLIENT_KEY" \
http://localhost:1337/parse/functions/debugTest
```

If configured correctly, the terminal will display the response `"Testing!"`.

## 4- Debugging the Code with Node.js

You can use Node.js's debugging features, integrated with Visual Studio Code (or a similar IDE), to debug your functions step by step.

### Setting up VS Code

1. Open the **Run and Debug** panel on the left sidebar and click **Create a launch.json file**.
2. Choose **Node.js** as the environment.

This creates a basic debug configuration. To enhance it:

1. Click **Add Configuration...** and select **Node.js: Attach to Process**.
2. Choose the **Attach by Process ID** action and attach it to the Parse Server's node process.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OcGhOu8TVvhUkKu44bWbg_image.png)

### Debugging the Code

1. Open main.js and set a **breakpoint** on the line return "Testing!"; by clicking to the left of the line number.
2. Run the same cURL command as before. The debugger will pause execution at the breakpoint.
3. While paused, inspect environment variable values and the call stack in the debugger panel.

This approach lets you analyze your code’s behavior in detail.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fzlOtXOTnUjcT0VujaAN__image.png)

## Conclusion

By following this guide, you’ll be able to debug all aspects of your Parse integration and Cloud Code functions locally, improving your development workflow with Back4app.
