# Visualize request responses using Postman Visualizer

The _Postman Visualizer_ provides a programmable way to visually represent your request [responses](/docs/sending-requests/response-data/responses/). You can also use Postman's AI assistant Postbot to automate your visualization. If you add a visualization script to the **Scripts** tab of your request, the result renders in the **Visualization** tab for the response body. If you don't create a Visualizer script, you can select **Visualize** to get Postbot to generate the visualization.

![Response visualization](https://assets.postman.com/postman-docs/v11/response-pane-visualization-v11.23.jpg)

The Visualizer enables you to present your response data in ways that help to make sense of it. You can use this to model and highlight the information that's relevant to your project, instead of having to read through raw response data. When you [share a Postman Collection](/docs/collaborating-in-postman/sharing/), other people on your team can also understand your visualizations within the context of each request.

## Visualize response data

To visualize your response data, add code to the **Pre-request** or **Post-response** [script](/docs/tests-and-scripts/write-scripts/intro-to-scripts/) for the request. The `pm.visualizer.set()` method will apply your Visualizer code to the data and present it in the **Visualization** tab when the request runs.

### Add Visualizer code

The `pm.visualizer.set()` method accepts a [Handlebars](https://handlebarsjs.com/) template string as its first parameter. The second parameter is the data you want to use the template to display. Read on to learn how you can build a Handlebars template and pass data to it.

To see an example of the Visualizer in action, select **Run in Postman** and fork the enclosing collection in Postman.

![Run in Postman](https://run.pstmn.io/button.svg)

In the first request, the example endpoint responds with a list of names and email addresses with the following JSON response body structure:

```js
[
    {
        "name": "Alice",
        "email": "alice@example.com"
    },
    {
        "name": "Jack",
        "email": "jack@example.com"
    },
    // ... and so on
]
```

The Visualizer code creates a Handlebars template to render a table displaying the names and email addresses by looping over an array. Handlebars can do this with the `{{#each}}` tag. The following runs as a **Post-response** script in the request:

```js
var template = `
<table bgcolor="#FFFFFF">
<tr>
<th>Name</th>
<th>Email</th>
</tr>

{{#each response}}
<tr>
<td>{{name}}</td>
<td>{{email}}</td>
</tr>
{{/each}}
</table>
`;
```

The variable names inside the double curly braces in the template will be substituted by the data passed to the `pm.visualizer.set()` method. To apply the template, the following code completes the **Post-response** script:

```js
// Set visualizer
pm.visualizer.set(template, {
    // Pass the response body parsed as JSON as `data`
    response: pm.response.json()
});
```

The `template` variable is the template string created earlier. The second argument passed is an object defined as the `response` propertyâthis is the variable that the template expects in the `{{#each response}}` loop. The value assigned to the `response` property is the response JSON data from the request parsed as an object.

### View visualizations

**Send** the request in Postman and select the **Visualization** tab. Postman renders the table as HTML, as it would be in a web browser.

![Visualize a table](https://assets.postman.com/postman-docs/v11/visualizer-table-v11.23.jpg)

### Add styling and interaction to visualizations

You can load an external stylesheet using `<link>` tags in your HTML template code, using the same technique as adding a stylesheet to a web page. You can also add stylesheets as `<style>` tags. Similarly, you can add interactions using JavaScript code in `<script>` tags inside your template HTML code.

Visualizer doesn't support interactions that download resources.

### Use your own libraries

You can use any of the libraries in the [Postman Sandbox](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/overview/) to programmatically generate the layout template. To import another external JavaScript library, add the URL to a `<script>` tag in the template code, just as you would to load JavaScript into an HTML file. This lets you render your request data using the visualization tool of your choice (for example D3.js).

### Access data inside the template

Any `<script>` elements inside your template can access the data passed in the second argument to `pm.visualizer.set()` by calling the `pm.getData(callback)` method. This is only applicable to JavaScript code in the template, for example if your template includes code to render a chart.

The `pm.getData(callback)` method takes a callback function as its parameter. This callback accepts two parameters: `error` and `data`. The second parameter is the `data` that was passed to `pm.visualizer.set()`.

## Use Postbot to create visualizations

Not sure how to write a visualization for your request? Ask Postbot! Tell Postbot what you want to do using plain language, and Postman uses artificial intelligence to generate a visualization for you. Use Postbot to create a new visualization, change the type of visualization, fix your existing visualization, and more.

To create a visualization with Postbot, do the following:

1. Send your request so it has a response.
1. In the **Body** tab of the response, select the down arrow next to **Visualize**.
1. In the menu, select a table, linear chart, or bar graph. You can also select **Set up with a prompt** to visualize your response in another format.

    ![Visualize with Postbot](https://assets.postman.com/postman-docs/v11/postbot-visualizer-v11.23.jpg)

When you select **Set up with a prompt**, you can complete a preset prompt _Visualize response as_ or enter your own, for example, _Create a pie chart_.

Once you create a visualization or close the Postbot window, you can access **Postbot** again from the [footer](/docs/getting-started/basics/navigating-postman/#footer) or the **Scripts** tab.

![Interact with Postbot](https://assets.postman.com/postman-docs/v11/postbot-interaction-v11.23.jpg)

You can help improve Postbot by sharing your feedback with Postman. Selecting **Share Details** opens up a GitHub issue request.

For more information on Postbot, visit [About Postbot](/docs/getting-started/basics/about-postbot/).

## Try it out

For more examples of Visualizer code in action, add any of the following collections to your workspace by [forking the collection](/docs/collaborating-in-postman/using-version-control/forking-elements/). You can also [export and then import](/docs/getting-started/importing-and-exporting/importing-and-exporting-overview/) the collection. After you fork or import the collection, open a request from **Collections** in the sidebar, then select **Send**. Postman will display the rendered data in the **Visualization** tab.

* [DIY collection that renders a bar chart using ChartJS](https://www.postman.com/postman/postman-team-collections/collection/8wlm25q/visualizer-diy-bar-chart?action=share&creator=16724969)
* [Heat map visualization](https://www.postman.com/postman/postman-team-collections/collection/ahu13nu/visualizer-d3-heatmap-demo?action=share&creator=16724969)
* [Various chart and graph examples](https://www.postman.com/postman/published-postman-templates/collection/hu7uwj7/visualizer-feature-templates?action=share&creator=16724969)

## Visualizer API

You can access the Visualizer from the [Postman API](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-visualizer/). The `pm.visualizer.set()` method takes three parameters:

* `layout` (required): The first parameter is a [Handlebars](https://handlebarsjs.com/) HTML template string.
* `data` (optional): The second parameter is data that you can bind to the template. The properties of this object can be accessed in the template.
* `options` (optional): The third argument is an `options` object for [`Handlebars.compile()`](https://handlebarsjs.com/api-reference/). You can use this to control how Handlebars compiles the template.

Postman uses the information you pass to `pm.visualizer.set()` to render an HTML page in the sandbox for the Visualizer. Select the **Visualization** tab for the rendered HTML page. The `layout` string is inserted into the `<body>` of the rendered page, including any JavaScript, CSS, and HTML that the template has.

## Debugging the Visualizer

You can debug a visualization in Postman by right-clicking in the **Visualization** area and selecting **Inspect visualization**. This will open the Visualizer Developer Tools attached to the sandbox. You can use it in the same way as debugging a web page.

The Visualizer Developer Tools are only available in the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/).

![Debugging visualizers in Postman](https://assets.postman.com/postman-docs/v11/inspect-vis-v11.23.jpg)

## Next steps

Now that you've learned about visualizing responses in Postman, you can start creating visualizations of your own.

* To get started, you can experiment with the [More Visualizer examples](https://www.postman.com/postman/e9bb1adb-2f2e-4ace-a482-38c570d65275/overview) workspace. Run the example requests, then adjust the code to get the results you need for your own data.
* For more information about how Postman provides access to your response data inside scripts, visit [Postman test script examples](/docs/tests-and-scripts/write-scripts/test-examples/).