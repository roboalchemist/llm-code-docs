# Source: https://developers.make.com/custom-apps-documentation/app-components/rpcs.md

# Remote Procedure Calls

Remote Procedure Calls are used to retrieve live data from a service for an input field.

You can use RPCs to retrieve dynamic options in a field to clarify the expected input for a user. For example, selecting a country in a dropdown could trigger an RPC to retrieve corresponding states or cities.

These requests are invoked while the user interacts with the modules when building a scenario.

## Types of RPCs

* [Dynamic fields RPCs](https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-fields-rpc) generate dynamic fields inside a module.
* [Dynamic options RPCs](https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-options-rpc) dynamically fill the fields in a module.
* [Dynamic sample RPCs](https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-sample-rpc) replace hard-coded samples that might become outdated quickly.

## Components

### Communication

Communication can be [request-less](https://developers.make.com/custom-apps-documentation/component-blocks/api/request-less-communication).

As with modules, you can use [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination) in RPCs to iterate the records.

### Parameters

[Parameters](https://developers.make.com/custom-apps-documentation/block-elements/parameters) from the modules are passed automatically to linked RPCs.

## Available IML variables

The following IML variables are available to use anywhere in a module within IML strings.

<table><thead><tr><th width="236.22216796875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>now</code></td><td valign="top">Current date and time with milliseconds in UTC timezone, in ISO 8601 format: <code>YYYY-MM-DDTHH:mm:ss.sssZ</code>.</td></tr><tr><td valign="top"><code>environment</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>temp</code></td><td valign="top">Contains custom variables created using the <code>temp</code> directive.<br>Example:<br><code>"temp": {</code><br><code>"id": 123</code><br><code>},</code><br><code>"url": "/user/{{temp.id}}" // url === "/user/123"</code></td></tr><tr><td valign="top"><code>parameters</code></td><td valign="top">The module's input parameters collection (<a href="../component-blocks/parameters">static</a> and <a href="../component-blocks/mappable-parameters">mappable</a>).. The keys are the parameter `name` values, and the values are the data mapped by the user.</td></tr><tr><td valign="top"><code>connection</code></td><td valign="top">The connection data collection (access token or API key and other values).</td></tr><tr><td valign="top"><code>common</code></td><td valign="top">The collection defined in the app's <a href="../base#common-data">Base common data</a>. This will typically include the module 'timeout' limit and Client ID and secret when using <a href="connections/oauth2">OAuth 2.0</a> code grant connections.</td></tr><tr><td valign="top"><code>data</code></td><td valign="top">The module's data collection.</td></tr><tr><td valign="top"><code>scenario</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>metadata.expect</code></td><td valign="top">The module's raw <a href="../component-blocks/mappable-parameters">mappable parameters</a> as they were specified in the configuration.</td></tr><tr><td valign="top"><code>metadata.interface</code></td><td valign="top">The module’s raw <a href="../component-blocks/interface">interface</a> array the way you have specified it in the configuration.</td></tr></tbody></table>

Additional variables available within the `response` collection:

<table><thead><tr><th width="143.629638671875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>output</code></td><td valign="top">When using the <a href="../component-blocks/api/handling-responses">wrapper directive</a>, the 'output' variable represents the result of the output directive.</td></tr></tbody></table>

Additional variables available when using the `iterate` directive, for example within the wrapper or [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination) collections:

<table><thead><tr><th width="238.44439697265625" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>iterate.container.first</code></td><td valign="top">The first item of the iterated array.</td></tr><tr><td valign="top"><code>iterate.container.last</code></td><td valign="top">The last item of the iterated array.</td></tr></tbody></table>

Additional variables available within the [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination) and [response](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses) collections:

<table><thead><tr><th width="157.70367431640625" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>body</code></td><td valign="top">The response body received from the last request.</td></tr><tr><td valign="top"><code>headers</code></td><td valign="top">The response headers received from the last request.</td></tr><tr><td valign="top"><code>item</code></td><td valign="top">When using the <code>iterative</code> directive, this variable represents the current item that is being iterated.</td></tr></tbody></table>

Additional variables available in the webhook [attach](https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated/attached) RPC.

<table><thead><tr><th width="164.74078369140625" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>webhook.id</code></td><td valign="top">Internal webhook ID.</td></tr><tr><td valign="top"><code>webhook.url</code></td><td valign="top">The webhook URL that you can use to automatically register the webhook in the external platform via the API, when it's supported.</td></tr></tbody></table>

Additional variables available in the webhook [detach](https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated/not-attached) RPC and in the `expect` [mappable parameter](https://developers.make.com/custom-apps-documentation/component-blocks/mappable-parameters) and the [interface](https://developers.make.com/custom-apps-documentation/component-blocks/interface) section of an instant trigger module.

<table><thead><tr><th width="153.62957763671875" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>webhook</code></td><td valign="top">The webhook’s data collection.</td></tr></tbody></table>

## Limits

<table><thead><tr><th valign="top">Name</th><th valign="top">Total limit of...</th><th valign="top">Value</th></tr></thead><tbody><tr><td valign="top">Max Execution Timeout</td><td valign="top">... seconds</td><td valign="top">40</td></tr></tbody></table>

<table><thead><tr><th width="173.33333333333331" valign="top">Name</th><th width="234" valign="top">Recommended limit of ...</th><th valign="top">Value</th></tr></thead><tbody><tr><td valign="top">Request Count</td><td valign="top">... calls performed by RPC</td><td valign="top">3</td></tr><tr><td valign="top">Record Count</td><td valign="top">... paginated records</td><td valign="top">3 * number of objects per page</td></tr></tbody></table>

## Best Practices

Review the [best practices for RPCs](https://developers.make.com/custom-apps-documentation/best-practices/remote-procedure-calls).
