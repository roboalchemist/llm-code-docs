# Write scripts to test API response data in Postman

You can use post-response scripts in Postman to run JavaScript after a request runs. By including code in the **Scripts > Post-response** tab for a request, collection, or folder, you can write and validate API tests. You can also use post-response scripts for debugging your tests.

## Testing in Postman

Some of the most common approaches to [API testing](https://www.postman.com/api-platform/api-testing/) are contract testing, unit testing, end-to-end testing, and load testing. Tests confirm that your API is working as expected, that integrations between services function reliably, and that any changes haven't broken existing functionality.

You can write tests for your Postman API requests in JavaScript in the **Post-response** tab. You can also use test code to aid the debugging process when something goes wrong with your API project. For example, you might write a test to validate your API's error handling by sending a request with incomplete data or wrong parameters.

The **Pre-request** and **Post-response** tabs use the Postman Sandbox, a runtime based on Node.js that enables you to add dynamic behavior to requests and collections.

* The **Scripts > Pre-request** tab enables you to do any processing needed before sending a request, like setting variable values. Any code here runs before the request is sent. To learn more, see [Write pre-request scripts to add dynamic behavior in Postman](/docs/tests-and-scripts/write-scripts/pre-request-scripts/).
* The **Scripts > Post-response** tab provides for any post-processing after a request is sent and includes the ability to write tests for assessing response data. The **Post-response** tab has the [Chai.js](https://www.chaijs.com/api/bdd/) library built in, so you can use Chai's behavior-driven development (BDD) syntax to create readable test assertions.

Select ![Image 1: Code icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-code-stroke.svg#icon) **Snippets** at the lower right of the code editor to view a list of test snippets. You can search for and select snippets to inject pre-written blocks of code. Some will help you retrieve data from variables, some are boilerplate tests, and some perform common utility functions. You can also ask Postman's AI assistant Postbot to [write tests for you](#write-tests-using-postbot).

## Add a post-response test

You can add tests to [requests](/docs/sending-requests/create-requests/create-requests/), [collections](/docs/sending-requests/create-requests/intro-to-collections/), and folders in a collection. Postman includes code snippets you add and then change to suit your test logic.

To add a test, open the request, collection, or folder and enter your code in the **Scripts > Post-response** tab. You can write your own JavaScript. You can also select ![Image 2: Code icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-code-stroke.svg#icon) **Snippets** at the lower right of the code editor and select a snippet. To make your code more readable, you can select ![Image 3: Pretty icon](https://assets.postman.com/postman-docs/aether-icons/action-pretty-stroke.svg#icon) **Beautify** in the lower right of the code editor.

Post-response scripts can use dynamic variables, carry out test assertions on response data, and pass data between requests. Tests run after the request runs and a response is received from the API. The output appears in the response's **Test Results** tab.

In the **Test Results** tab, you can click ![Image 4: Refresh icon](https://assets.postman.com/postman-docs/aether-icons/action-refresh-stroke.svg#icon) **Refresh results** in the upper right of the response pane to refresh your test results. This gives you the option to refresh your test results without re-sending the request.

![Request Test Tab](https://assets.postman.com/postman-docs/v11/request-test-tab-v11.45.1.jpg)

Your scripts can include as many tests as you need and will be saved along with the request details when you select ![Image 5: Save icon](https://assets.postman.com/postman-docs/aether-icons/action-save-stroke.svg#icon) **Save**. If you share a collection, publish documentation, or use the **Run in Postman** button, your test code will be included for anyone who views or imports your collection.

### Add a test to a gRPC request

You can add tests to a gRPC request before invoke, when the client receives a message, or after response. All hooks are available for all gRPC requests regardless of the method type (unary, client streaming, server streaming, or bidirectional streaming).

To add a test to a gRPC request, do the following:

1. Go to the **Scripts** tab in your gRPC request.
2. Select the hook (**Before invoke**, **On message**, or **After response**) you want to add a test to.
3. Select ![Image 6: Code icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-code-stroke.svg#icon) **Snippets** at the lower right of the code editor to add a test. You can also write a custom assertion.

When you select **Invoke**, tests run before, during, or after the request is invoked. Once you invoke your gRPC request, updates to scripts in the **On message** tab won't take effect until the next time you invoke the request. If you select **Cancel**, the request and any further script runs are stopped.

If there are any errors in your **Before invoke** script, the request will stop.

## Validate responses

To validate the data returned by a request, you can use the `pm.response` object in a test. Define tests using the `pm.test` function. Provide a name and function that returns a boolean (`true` or `false`) value to indicate if the test passed or failed. Use Chai.js BDD syntax and `pm.expect` in your assertions to test the response detail.

The first parameter for the `.test` function is a text string that appears in the test result output. Use this to identify your tests and communicate the purpose of a test to anyone viewing the results.

For example, enter the following in the **Post-response** tab of a request to test if the response status code is `200`:

```js
pm.test("Status test", function () {
    pm.response.to.have.status(200);
});
```

Select **Send** to run your request, then select the **Test Results** tab in the response. The tab header displays how many tests passed and how many ran in total. You can also select the **Filter Results** dropdown list to view the test results by type: **Passed**, **Skipped**, and **Failed**.

If the request returned a `200` status code, the test passes. To find out what happens with a different status code, change the expected status code in your post-response script and run the request again.

## Format test result messages using pm.expect

Using the `pm.expect` syntax gives your test result messages a different format. Experiment with the options to get the output you find most useful.

Fork the [Intro to writing tests collection](https://www.postman.com/postman/postman-team-collections/collection/9fqcfpk/intro-to-writing-tests-with-examples?action=share&creator=16724969) to import templates containing some example post-response scripts into Postman and experiment with the code.

Your code can test the request [environment](/docs/sending-requests/variables/managing-environments/), as in the following example:

```js
pm.test("environment to be production", function () {
    pm.expect(pm.environment.get("env")).to.equal("production");
});
```

You can use different syntax variations to write your tests in a way that you find readable, and that suits your application and testing logic. For example:

```js
pm.test("response should be okay to process", function () {
    pm.response.to.not.be.error;
    pm.response.to.have.jsonBody("");
    pm.response.to.not.have.jsonBody("error");
});
```

Your tests can validate request responses using syntax that you tailor to the response data format. For example:

```js
pm.test("response must be valid and have a body", function () {
    pm.response.to.be.ok;
    pm.response.to.be.withBody;
    pm.response.to.be.json;
});
```

## Test collections and folders

You can add post-response scripts to a collection, a folder, or a single request within a collection. A post-response script associated with a collection will run after every request in the collection. A post-response script associated with a folder will run after every direct child request in the folder. This enables you to reuse commonly run tests after requests. The run order for each request will be collection tests, folder tests and then request tests.

You can also [store post-response scripts in the Postman Package Library](/docs/tests-and-scripts/write-scripts/packages/package-library/). This enables you to maintain commonly used scripts and tests in a single location, share them with your team, and reuse them in your internal workspaces.

Adding scripts to collections and folders enables you to test the workflows in your API project. This helps to ensure that your requests cover typical scenarios, providing a reliable experience for application users.

To add or edit collection and folder tests, select a collection or folder in the sidebar, then select the **Scripts > Post-response** tab.

When you [run a collection](/docs/collections/running-collections/intro-to-collection-runs/), the collection runner displays the results for all tests. The test results include the response time in milliseconds and details about whether a specific request in the collection passed or failed its tests.

![Collection Tests](https://assets.postman.com/postman-docs/v11/collection-tests-run-v11.45.1.jpg)

You can write scripts to control the order in which your requests run using [branching and looping](/docs/collections/running-collections/building-workflows/).

## Write tests using Postbot

You can use Postman's AI assistant [Postbot](/docs/getting-started/basics/about-postbot/) to write tests for your requests. Tell Postbot what to do in natural language, and Postbot generates post-response scripts for you. Use Postbot to add a new set of tests, visualize responses, save a field from a response, or fix your existing tests.

To write tests with Postbot, do the following:

1. Open a request and select **Send** so it has a response.
2. Select the **Scripts > Post response** tab.
3. (Optional) Select code you'd like Postbot to help with.
4. Select ![Image 7: Postbot icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-postbot-stroke.svg#icon) **Open Postbot** in the code editor. You can also select **Control+Option+P** or **Ctrl+Alt+P** to open Postbot.
5. Tell Postbot what you want to do and select **Enter**.

    ![Write tests with Postbot](https://assets.postman.com/postman-docs/v11/postbot-write-tests-v11-41.jpg)

You can also work with Postbot in the following ways:

* Postbot can offer suggestions based on your request and the response data. Select the down arrow (â) on your keyboard and select one of Postbot's suggestions.

    ![Get test suggestions from Postbot](https://assets.postman.com/postman-docs/v11/postbot-test-suggestions-v11-41.jpg)

* Postbot understands context. Select part of a script or the response body, then tell Postbot what you want to do or change based on the selection.

    ![Postbot understands context](https://assets.postman.com/postman-docs/v11/postbot-test-context-v11-41.jpg)

* You can also select part of a JSON response, right-click, then select ![Image 8: Postbot icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-postbot-stroke.svg#icon) **Use Postbot**. You can tell Postman to generate tests based on the selection. For example, go to a response, select a property, and ask Postbot to generate a test to verify that it exists. Or select specific values in a response and ask Postbot to visualize only that data.

    ![Postbot understands context](https://assets.postman.com/postman-docs/v11/postbot-inline-response-v11.45.1.jpg)

* Postbot also powers autocomplete in the post-response script editor. If youâve [enabled Postbot](/docs/getting-started/basics/about-postbot/#get-started-with-postbot), youâll see code suggestions as you type. Select the **Tab** key to accept the suggestion. If youâve already paid for Postbot, you get unlimited suggestions and acceptances. For everyone else, feature usage is capped at 200 suggestion acceptance events per month.

To learn more about what you can do with Postbot, go to [About Postbot](/docs/getting-started/basics/about-postbot/).

## Add documentation to post-response scripts

Postman supports JSDoc for documenting JavaScript functions in your post-response scripts. Documentation added to your functions using JSDoc will display in a popup window when you call your functions. You can use the official [JSDoc documentation](https://jsdoc.app/) to learn how to add documentation to your post-response scripts.

The following example has documentation for the `logger` function using JSDoc. The documentation explains what the function does, and defines what the `data` parameter is used for and that it accepts a string data type.

```js
/**
 * This function prints a string to the Postman Console.
 * @param {string} data - The text to print to the Postman Console.
 */
function logger(data) {
    console.log(`Logging information to the console, ${data}`)
}
```

## Debug your tests

If you're having trouble with your tests, do the following:

* Check if there are any errors in your scripts. A red underline will highlight possible errors. Hover over the error and select **View Problem** to get help. You can also check the response viewer for specific errors.
* Debug your tests using [log statements](/docs/sending-requests/response-data/troubleshooting-api-requests/#using-log-statements) to ensure that you are asserting on correct data.

## Next steps

After writing your first tests in Postman, you can write more complex tests and use them with other Postman tools.

* For more information about what you can do with the `pm` object, check out some post-response script [examples](/docs/tests-and-scripts/write-scripts/test-examples/) and visit the [Postman Sandbox API reference](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/overview/).
* To learn how to use tests with Postman Monitors and check the health and performance of your API, go to [Monitor health and performance of your APIs in Postman](/docs/monitoring-your-api/intro-monitors/).
* To learn how to [automate your testing](https://www.postman.com/api-platform/api-test-automation/) by integrating collection runs within your CI/CD configuration, go to [Integrate CI tools in Postman](/docs/integrations/ci-integrations/).
* For more information about storing and reusing commonly used scripts and tests, learn about [the package library](/docs/tests-and-scripts/write-scripts/packages/package-library/) in Postman.