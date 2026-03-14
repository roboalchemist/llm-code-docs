# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses.md

# Handling responses

## Response specification

Below is a list of directives controlling the processing of the response. When used, they must be placed inside the `response` collection.

<table><thead><tr><th width="131">Key</th><th width="193.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>type</code></td><td>String or type specification</td><td>Specifies how data is parsed from the body.</td></tr><tr><td><code>valid</code></td><td>IML string or object</td><td>An expression that parses whether the response is valid or not.</td></tr><tr><td><code>error</code></td><td>IML string or rrror specification</td><td>Specifies how the error is shown to the user, if it occurs.</td></tr><tr><td><code>limit</code></td><td>IML string or number</td><td>Controls the maximum number of returned items by the module.</td></tr><tr><td><code>iterate</code></td><td>IML string or iterate specification</td><td>Specifies how response items are retrieved and processed, in case of multiple.</td></tr><tr><td><code>temp</code></td><td>IML object</td><td>Creates/updates variable <code>temp</code> which you can access in subsequent requests.</td></tr><tr><td><code>output</code></td><td>Any IML type</td><td>Describes the structure of the output bundle.</td></tr></tbody></table>
