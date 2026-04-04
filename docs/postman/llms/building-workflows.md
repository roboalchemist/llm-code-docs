# Customize request order in a collection run

By default, when you [run a collection](/docs/collections/running-collections/intro-to-collection-runs/), Postman runs all requests in the order they appear in your collection. Requests in folders run first, followed by requests in the root of the collection. To dynamically change the order of requests during a collection run, use the `pm.execution.setNextRequest()` function in a post-response [script](/docs/tests-and-scripts/write-scripts/intro-to-scripts/).

Instead of manually changing the order of requests each time you start a collection run, you can automate this behavior. Add `pm.execution.setNextRequest()` to your post-response scripts to specify which request Postman runs next, following the current request. With this function, you can build workflows that chain requests, running them one after the other in a custom order.

## Set the next request

To specify the request to run next, add the following code on the **Scripts > Post-response** tab of a request. Replace `request_name` with the name or ID of the request you want to run next, in quotes.

```js
pm.execution.setNextRequest("request_name");
```

Postman runs the specified request after completing the current request.

## Loop over a request

If you pass the name or ID of the current request to the `setNextRequest` function, Postman will run the current request again after it's completed.

> **Important:** To prevent the request from looping indefinitely, add extra logic to the `setNextRequest` function. For example, you can set the request to exit the loop after a certain number of iterations or when another condition is met. Otherwise, to end the loop, you can force close the Collection Runner. For example, use the following post-response script in a request in a collection. When the collection is run, it runs the request three times, then exits.

```js
var i = !pm.variables.get("i") ? 1 : pm.variables.get("i");
if (i < 3) {
    console.log("this is run " + i + " for request " + pm.execution.location.current);
    pm.execution.setNextRequest(pm.execution.location.current)
    i++;
    pm.variables.set("i", i);
} else {
    pm.execution.setNextRequest(null);
}
```

## Stop a workflow

To stop a workflow, you can enter "null" as the `pm.execution.setNextRequest()` function's argument in your post-response script. The collection run stops after the current request runs. If your collection run is configured to run more than one iteration, Postman stops each iteration after the current request runs.

```js
pm.execution.setNextRequest(null);
```

> You can also skip a request using the `pm.execution.skipRequest()` method in your post-response script. Learn more about [skipping requests from pre-request scripts](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-execution/#pmexecutionskipRequest).

## Tips for building request workflows

Keep the following tips in mind when using the `pm.execution.setNextRequest()` function.

### Use setNextRequest() when you run an entire collection

Use the `pm.execution.setNextRequest()` function when running a collection with the Collection Runner, the Postman CLI, or Newman. It has no effect when you run a request in Postman using **Send**.

### Use setNextRequest() in pre-request or post-response scripts

You can use `pm.execution.setNextRequest()` in the pre-request script or the post-response script of a request. If more than one value is assigned, the last value that's set takes precedence.

### Specify the next request using the request ID

A request's name may change, but changing its name doesn't change its ID. For this reason, it's best to use the request ID when you specify the next request. When specifying the ID, it must be in quotes. For example: `pm.execution.setNextRequest("1ab12345-4ab4-4124-c000-12341abc1234");`

To get the request ID of the currently running request, use `pm.info.requestId`. For example, run `console.log(pm.info.requestId)` to see the current request's ID. To learn more, see [Script Workflows](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-info/).

You can also get the request ID in Postman. Open the request and, from the right sidebar, click \[![Image 1: Info icon](https://assets.postman.com/postman-docs/aether-icons/state-info-stroke.svg#icon)\] **Info**. The request ID is prepended with your user ID (the first block of characters).

### setNextRequest() always runs last

The `pm.execution.setNextRequest()` function always runs at the completion of the current request, regardless of its location in the script. If you put code in the pre-request script or post-response script after this function, the code blocks will still run before `pm.execution.setNextRequest()`.

### setNextRequest() scope is limited to the collection

The scope of `pm.execution.setNextRequest()` is the source of your collection run.

* If you run an entire collection, you can set any request in the collection as the next request, even requests inside folders.
* If you run a folder, the scope of `pm.execution.setNextRequest()` is limited to that folder. In this case, you can set any request in the same folder as the next request, but not requests located in other folders or at the root of the collection.

Learn more about [running collections or folders](/docs/collections/running-collections/intro-to-collection-runs/).

## Next steps

After learning about how to build request workflows, you can write some scripts.

* To learn more about writing pre-request and post-response scripts, visit [Use scripts to add logic and tests to Postman requests](/docs/tests-and-scripts/write-scripts/intro-to-scripts/).