# Source: https://docs.pentaho.com/analyzer-external-javascript-api/cv-apis-pentaho-analyzer-external-javascript-api-cp/utility-apis-pentaho-analyzer-external-javascript-api.md

# Utility APIs

The utility system definition for `cv.api` class (`cv.api.util`). Contains all utility related API calls.

## Constructor

| Name         | Description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| `new util()` | Utility definition for `cv.api` class. Contains all utility related API calls. |

## Methods

| Name                                               | Description                                                                                                                                |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `parseMDXExpression(formula, escapeHTML) : string` | Given an MDX formula, `parseMDXExpression` returns the last token in the formula. For example, `[Product].[Trucks]` would return 'Trucks'. |

## Constructor Details

| `new util()`                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Utility definition for <code>cv.api</code> class.</p><ul><li><strong>Source</strong></li></ul><p><a href="https://github.com/pentaho/pentaho-analyzer/tree/master/b/pentaho/p-analyzer/client/src/main/javascript/scripts/cv_api_util.js#L28">javascript/scripts/cv\_api\_util.js, line 28</a></p> |

\## Methods Details

<table data-header-hidden><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><code>parseMDXExpression(formula, escapeHTML) : string</code></td><td></td><td></td></tr><tr><td><p>Given an MDX formula, <code>parseMDXExpression</code> returns the last token in the formula. For example,<code>[Product].[Trucks]</code> would return 'Trucks'.- <strong>Since</strong></p><p>5.4</p><ul><li><strong>Source</strong></li></ul><p><a href="https://github.com/pentaho/pentaho-analyzer/tree/master/b/pentaho/p-analyzer/client/src/main/javascript/scripts/cv_api_util.js#L317">javascript/scripts/cv_api_util.js, line 317</a></p><ul><li><strong>Parameters</strong></li><li><strong>Returns</strong></li><li><p><strong>Example</strong></p><pre class="language-javascript"><code class="lang-javascript">
</code></pre></li></ul><p>cv.api.util.parseMDXExpression("[Product].[Truck]")</p><p>// Return Value: "Truck"</p><pre><code>```
</code></pre></td><td></td><td></td></tr><tr><td>Name</td><td>Default Value</td><td>Summary</td></tr><tr><td><code>formula : string</code></td><td></td><td>This is the MDX formula to be parsed by the function.</td></tr><tr><td><code>escapeHTML : boolean</code></td><td></td><td>This is an optional parameter. If provided, the string parsed from the MDX expression will be returned with HTML reserved characters as escaped.</td></tr><tr><td>Name</td><td>Description</td><td></td></tr><tr><td><code>string</code></td><td>This is the MDX formula parsed as a string.</td><td></td></tr></tbody></table>
