# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/queries/basequery.md

# BaseQuery

## cdf.queries. BaseQuery

Static Abstract

Defines the base query type used by default by any dashboard.

While loading this class's module, the static function `setBaseQuery` is executed in order to make this class the default base query class for any dashboard.

Additional query types might extend from this class, if no valid constructor is provided during the new query type registration.

Please use the dashboard function `getQuery` to create new queries.

\*\*Source:\*\*queries/BaseQuery.js, line 170

## Members

| Name                                                    | Description                                                    |
| ------------------------------------------------------- | -------------------------------------------------------------- |
| \_label : `string`Constant Protected                    | The class label.                                               |
| \_name : `string`Constant Protected                     | The class name.                                                |
| dashboard : `cdf.dashboard.Dashboard`Protected          | A reference to the dashboard instance.                         |
| deepProperties : ``Array.<`string`>``Constant Protected | A list of properties to be extended to the registered queries. |
| defaults : `Object`Protected                            | The default properties.                                        |
| interfaces : `Object`Protected                          | The default interfaces.                                        |

## Methods

| Name                                                          | Description                                                                   |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| buildQueryDefinition(overrides)Abstract                       | Builds the query definition `object`.                                         |
| dispose()                                                     | Dispose the query object.                                                     |
| doQuery(successCallback, errorCallback)                       | Executes a server-side query.                                                 |
| exportData()Abstract                                          | Exports the data represented by the query.                                    |
| fetchData(params, successCallback, errorCallback) : `Object`  | Fetches the data.                                                             |
| getErrorHandler(callback) : `function`                        | Gets the error callback handler.                                              |
| getOption(prop) : `Object`                                    | Gets an option (fallback for when the OptionManager is not available).        |
| getPage(targetPage, outsideCallback) : `boolean` \| `Object`  | Gets the set of results for the page at index `targetPage` (0-indexed).       |
| getSuccessHandler(callback) : `function`                      | Gets the success callback handler.                                            |
| init(opts)Abstract                                            | Initialization function.                                                      |
| initPage(pageSize, outsideCallback) : `boolean` \| `Object`   | Sets the page size and gets the first page of results.                        |
| lastProcessedResults() : `Object`                             | Gets the last retrieved result after being processed by postFetch.            |
| lastResults() : `Object`                                      | Gets the last retrieved result.                                               |
| nextPage(outsideCallback) : `Object`                          | Gets the next page of results, as controlled by the `pageSize` option.        |
| pageStartingAt(page, outsideCallback) : `boolean` \| `Object` | Runs the query, setting a starting page before doing so.                      |
| previousPage(outsideCallback) : `Object`                      | Gets the previous page of results, as controlled by the `pageSize` option.    |
| reprocessLastResults(outerCallback) : `Object`                | Reruns the success callback on the last retrieved result set from the server. |
| reprocessResults(outsideCallback) : `Object`                  | Alias for `reprocessLastResults`.                                             |
| setAjaxOptions(newOptions)                                    | Sets the jQuery.ajax options for the query.                                   |
| setCallback(callback)                                         | Sets the success callback for the query.                                      |
| setErrorCallback(callback)                                    | Sets the error callback for the query.                                        |
| setOption(prop, value)                                        | Sets an option (fallback for when the OptionManager is not available).        |
| setPageSize(pageSize)                                         | Sets the page size.                                                           |
| setPageStartingAt(targetPage) : `boolean`                     | Sets the starting page for later executions of the query.                     |
| setParameters(params)                                         | Sets query parameters.                                                        |
| setSearchPattern(pattern)                                     | Sets the search pattern for the query.                                        |
| setSortBy(sortBy)Abstract                                     | Sets the sorting options.                                                     |
| sortBy(sortBy, outsideCallback)Abstract                       | Sorts the data and executes a callback.                                       |

## Members Details

| \_label: `string`Constant Protected                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------- |
| <p>The class label.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 50</p><p><strong>Default Value:</strong>"Base Query"</p> |

| \_name: `string`Constant Protected                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------- |
| <p>The class name.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 35</p><p><strong>Default Value:</strong>"baseQuery"</p> |

| dashboard: `cdf.dashboard.Dashboard`Protected                                                    |
| ------------------------------------------------------------------------------------------------ |
| <p>A reference to the dashboard instance.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 76</p> |

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>deepProperties: <code>Array.&#x3C;`string`></code>Constant Protected</td></tr><tr><td><p>A list of properties to be extended to the registered queries that do not provide their own constructor function.</p><p>**Source:**queries/BaseQuery.js, line 67</p><p><strong>Default Value:</strong></p><pre><code>`["defaults","interfaces"]`
</code></pre><p><strong>See also:</strong><code>registerQuery</code></p></td></tr></tbody></table>

| defaults: `Object`Protected                                                       |                           |                                                         |
| --------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------- |
| <p>The default properties.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 94</p> |                           |                                                         |
| Name                                                                              | Default Value             | Description                                             |
| successCallback : `function`                                                      |                           | Default success callback.                               |
| errorCallback : `function`                                                        |                           | Default error callback.                                 |
| lastResultSet : `Object`                                                          | null                      | The last resultset returned by the query.               |
| lastProcessedResultSet : `Object`                                                 | null                      | The last resultset returned by the query and processed. |
| page : `number`                                                                   | 0                         | The page number.                                        |
| pageSize : `number`                                                               | 0                         | The page size.                                          |
| params : `Object`                                                                 | {}                        | The query parameters.                                   |
| ajaxOptions : `Object`                                                            | {async:false,type:"POST"} | The jQuery.ajax options for the query.                  |
| url : `string`                                                                    | ""                        | The target URL.                                         |

| interfaces: `Object`Protected                                                      |                             |                              |
| ---------------------------------------------------------------------------------- | --------------------------- | ---------------------------- |
| <p>The default interfaces.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 138</p> |                             |                              |
| Name                                                                               | Default Value               | Description                  |
| params : `Object`                                                                  |                             | Parameter interfaces.        |
| Name                                                                               | Default Value               | Description                  |
| reader : `string`                                                                  | "propertiesObject"          | Parameter reader.            |
| validator : `string`                                                               | "isObjectOrPropertiesArray" | Parameter validator.         |
| successCallback : `Object`                                                         |                             | Success callback interfaces. |
| Name                                                                               | Default Value               | Description                  |
| validator : `string`                                                               | "isFunction"                | Success callback validator.  |
| errorCallback : `Object`                                                           |                             | Error callback interfaces.   |
| Name                                                                               | Default Value               | Description                  |
| validator : `string`                                                               | "isFunction"                | Error callback validator.    |
| pageSize : `Object`                                                                |                             | Page size interfaces.        |
| Name                                                                               | Default Value               | Description                  |
| validator : `string`                                                               | "isPositive"                | Page size validator.         |

\## Methods Details

| **buildQueryDefinition**(overrides)Abstract                                                                 |               |                                          |
| ----------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------- |
| <p>Builds the query definition <code>object</code>.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 217</p> |               |                                          |
| Name                                                                                                        | Default Value | Summary                                  |
| overrides : `object`Optional                                                                                |               | Options that override the existing ones. |

| **dispose**()                                                                        |
| ------------------------------------------------------------------------------------ |
| <p>Dispose the query object.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 668</p> |

| **doQuery**(successCallback, errorCallback)                                              |               |                   |
| ---------------------------------------------------------------------------------------- | ------------- | ----------------- |
| <p>Executes a server-side query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 268</p> |               |                   |
| Name                                                                                     | Default Value | Summary           |
| successCallback : `function`Optional                                                     |               | Success callback. |
| errorCallback : `function`Optional                                                       |               | Error callback.   |

| **exportData**()Abstract                                                                              |
| ----------------------------------------------------------------------------------------------------- |
| <p>Exports the data represented by the query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 289</p> |

| **fetchData**(params, successCallback, errorCallback) : `Object`             |                                                               |                           |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------- |
| <p>Fetches the data.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 350</p> |                                                               |                           |
| Name                                                                         | Default Value                                                 | Summary                   |
| params : `Object`                                                            |                                                               | Parameters for the query. |
| successCallback : `function`                                                 |                                                               | Success callback.         |
| errorCallback : `function`                                                   |                                                               | Error callback.           |
| Name                                                                         | Description                                                   |                           |
| `Object`                                                                     | The result of calling `doQuery` with the specified arguments. |                           |
| Name                                                                         | Description                                                   |                           |
| `InvalidInput`                                                               | If the arguments are not correct.                             |                           |

| **getErrorHandler**(callback) : `function`                                                                                                                      |                         |                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------ |
| <p>Gets the error callback handler that executes the provided callback when the query fails to execute.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 253</p> |                         |                                      |
| Name                                                                                                                                                            | Default Value           | Summary                              |
| callback : `function`                                                                                                                                           |                         | Callback to call if the query fails. |
| Name                                                                                                                                                            | Description             |                                      |
| `function`                                                                                                                                                      | Error callback handler. |                                      |

| **getOption**(prop) : `Object`                                                                                                    |                       |                                             |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------- |
| <p>Gets an option (fallback for when the OptionManager is not available).</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 183</p> |                       |                                             |
| Name                                                                                                                              | Default Value         | Summary                                     |
| prop : `string`                                                                                                                   |                       | The property from where to get the options. |
| Name                                                                                                                              | Description           |                                             |
| `Object`                                                                                                                          | Value for the option. |                                             |

| **getPage**(targetPage, outsideCallback) : `boolean` \| `Object`                                                                              |                                                                                                    |                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| <p>Gets the set of results for the page at index <code>targetPage</code> (0-indexed).</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 580</p> |                                                                                                    |                                                         |
| Name                                                                                                                                          | Default Value                                                                                      | Summary                                                 |
| targetPage : `number`                                                                                                                         |                                                                                                    | Index of the page to get, starting at index 0.          |
| outsideCallback : `function`                                                                                                                  |                                                                                                    | Success callback to execute when the page is retrieved. |
| Name                                                                                                                                          | Description                                                                                        |                                                         |
| `boolean` \| `Object`                                                                                                                         | `false` if the page is already the current one, otherwise returns the result of calling `doQuery`. |                                                         |
| Name                                                                                                                                          | Description                                                                                        |                                                         |
| `InvalidPage`                                                                                                                                 | If `targetPage` is not a positive number.                                                          |                                                         |

| **getSuccessHandler**(callback) : `function`                                                                                                                           |                           |                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------- |
| <p>Gets the success callback handler that executes the provided callback when the query executes successfully.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 230</p> |                           |                                                 |
| Name                                                                                                                                                                   | Default Value             | Summary                                         |
| callback : `function`                                                                                                                                                  |                           | Callback to call after the query is successful. |
| Name                                                                                                                                                                   | Description               |                                                 |
| `function`                                                                                                                                                             | Success callback handler. |                                                 |

| **init**(opts)Abstract                                                              |               |                               |
| ----------------------------------------------------------------------------------- | ------------- | ----------------------------- |
| <p>Initialization function.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 206</p> |               |                               |
| Name                                                                                | Default Value | Summary                       |
| opts : `Object`                                                                     |               | The query definition options. |

| **initPage**(pageSize, outsideCallback) : `boolean` \| `Object`                                                   |                                                                            |                                                       |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------- |
| <p>Sets the page size and gets the first page of results.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 652</p> |                                                                            |                                                       |
| Name                                                                                                              | Default Value                                                              | Summary                                               |
| pageSize : `number`                                                                                               |                                                                            | Page Size.                                            |
| outsideCallback : `function`                                                                                      |                                                                            | Success callback to execute after query is retrieved. |
| Name                                                                                                              | Description                                                                |                                                       |
| `boolean` \| `Object`                                                                                             | `false` if pageSize is invalid, otherwise the result of calling `doQuery`. |                                                       |
| Name                                                                                                              | Description                                                                |                                                       |
| `InvalidPageSize`                                                                                                 | If the page size is not a positive number.                                 |                                                       |

| **lastProcessedResults**() : `Object`                                                                                         |                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| <p>Gets the last retrieved result after being processed by postFetch.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 432</p> |                                                                                                     |
| Name                                                                                                                          | Description                                                                                         |
| `Object`                                                                                                                      | A deep copy of the the last result set obtained from the server after being processed by postFetch. |
| Name                                                                                                                          | Description                                                                                         |
| `NoCachedResults`                                                                                                             | If there have not been previous calls to the server.                                                |

| **lastResults**() : `Object`                                                               |                                                              |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| <p>Gets the last retrieved result.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 416</p> |                                                              |
| Name                                                                                       | Description                                                  |
| `Object`                                                                                   | A deep copy of the last result set obtained from the server. |
| Name                                                                                       | Description                                                  |
| `NoCachedResults`                                                                          | If there have not been previous calls to the server.         |

| **nextPage**(outsideCallback) : `Object`                                                                                                     |                                                   |                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------- |
| <p>Gets the next page of results, as controlled by the <code>pageSize</code> option.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 534</p> |                                                   |                                                                         |
| Name                                                                                                                                         | Default Value                                     | Summary                                                                 |
| outsideCallback : `function`                                                                                                                 |                                                   | Success callback to execute when the next page of results is retrieved. |
| Name                                                                                                                                         | Description                                       |                                                                         |
| `Object`                                                                                                                                     | The result of calling `doQuery`.                  |                                                                         |
| Name                                                                                                                                         | Description                                       |                                                                         |
| `InvalidPageSize`                                                                                                                            | If the page size option is not a positive number. |                                                                         |

| **pageStartingAt**(page, outsideCallback) : `boolean` \| `Object`                                                                                                                                                                        |                                                                                  |                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| <p>Runs the query, setting a starting page before doing so. If the starting page matches the already selected one, the query run is canceled and <code>false</code> is returned.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 624</p> |                                                                                  |                                                                       |
| Name                                                                                                                                                                                                                                     | Default Value                                                                    | Summary                                                               |
| page : `number`                                                                                                                                                                                                                          |                                                                                  | Starting page index.                                                  |
| outsideCallback : `function`                                                                                                                                                                                                             |                                                                                  | Success callback to execute after the server-side query is processed. |
| Name                                                                                                                                                                                                                                     | Description                                                                      |                                                                       |
| `boolean` \| `Object`                                                                                                                                                                                                                    | `false` if the query run is canceled, otherwise the result of calling `doQuery`. |                                                                       |

| **previousPage**(outsideCallback) : `Object`                                                                                                     |                                   |                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | --------------------------------------------------------------------------- |
| <p>Gets the previous page of results, as controlled by the <code>pageSize</code> option.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 555</p> |                                   |                                                                             |
| Name                                                                                                                                             | Default Value                     | Summary                                                                     |
| outsideCallback : `function`                                                                                                                     |                                   | Success callback to execute when the previous page of results is retrieved. |
| Name                                                                                                                                             | Description                       |                                                                             |
| `Object`                                                                                                                                         | The result of calling `doQuery`.  |                                                                             |
| Name                                                                                                                                             | Description                       |                                                                             |
| `AtBeginning`                                                                                                                                    | If current page is the first one. |                                                                             |

| **reprocessLastResults**(outerCallback) : `Object`                                                                                                                                                     |                                                      |                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- | ----------------- |
| <p>Reruns the success callback on the last retrieved result set from the server.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 449</p><p><strong>See also:</strong><code>reprocessResults</code></p> |                                                      |                   |
| Name                                                                                                                                                                                                   | Default Value                                        | Summary           |
| outerCallback : `function`                                                                                                                                                                             |                                                      | Success callback. |
| Name                                                                                                                                                                                                   | Description                                          |                   |
| `Object`                                                                                                                                                                                               | The result of calling the specified callback.        |                   |
| Name                                                                                                                                                                                                   | Description                                          |                   |
| `NoCachedResults`                                                                                                                                                                                      | If there have not been previous calls to the server. |                   |

| **reprocessResults**(outsideCallback) : `Object`                                                                                                                          |                                                      |                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------- |
| <p>Alias for <code>reprocessLastResults</code>.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 474</p><p><strong>See also:</strong><code>reprocessLastResults</code></p> |                                                      |                   |
| Name                                                                                                                                                                      | Default Value                                        | Summary           |
| outsideCallback : `function`                                                                                                                                              |                                                      | Success callback. |
| Name                                                                                                                                                                      | Description                                          |                   |
| `Object`                                                                                                                                                                  | The result of calling the specified callback.        |                   |
| Name                                                                                                                                                                      | Description                                          |                   |
| `NoCachedResults`                                                                                                                                                         | If there have not been previous calls to the server. |                   |

| **setAjaxOptions**(newOptions)                                                                         |               |                           |
| ------------------------------------------------------------------------------------------------------ | ------------- | ------------------------- |
| <p>Sets the jQuery.ajax options for the query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 299</p> |               |                           |
| Name                                                                                                   | Default Value | Summary                   |
| newOptions : `Object`                                                                                  |               | Ajax options to be added. |

| **setCallback**(callback)                                                                           |               |                                |
| --------------------------------------------------------------------------------------------------- | ------------- | ------------------------------ |
| <p>Sets the success callback for the query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 494</p> |               |                                |
| Name                                                                                                | Default Value | Summary                        |
| callback : `function`                                                                               |               | The success callback function. |

| **setErrorCallback**(callback)                                                                    |               |                              |
| ------------------------------------------------------------------------------------------------- | ------------- | ---------------------------- |
| <p>Sets the error callback for the query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 504</p> |               |                              |
| Name                                                                                              | Default Value | Summary                      |
| callback : `function`                                                                             |               | The error callback function. |

| **setOption**(prop, value)                                                                                                        |               |                                               |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------- |
| <p>Sets an option (fallback for when the OptionManager is not available).</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 194</p> |               |                                               |
| Name                                                                                                                              | Default Value | Summary                                       |
| prop : `string`                                                                                                                   |               | The property for which the value will be set. |
| value : `Object`                                                                                                                  |               | Value for the property.                       |

| **setPageSize**(pageSize)                                                      |               |                   |
| ------------------------------------------------------------------------------ | ------------- | ----------------- |
| <p>Sets the page size.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 638</p> |               |                   |
| Name                                                                           | Default Value | Summary           |
| pageSize : `number`                                                            |               | Page size to set. |

| **setPageStartingAt**(targetPage) : `boolean`                                                                        |                                                                                              |                           |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------- |
| <p>Sets the starting page for later executions of the query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 602</p> |                                                                                              |                           |
| Name                                                                                                                 | Default Value                                                                                | Summary                   |
| targetPage : `number`                                                                                                |                                                                                              | Index of the page to get. |
| Name                                                                                                                 | Description                                                                                  |                           |
| `boolean`                                                                                                            | `true` if the page is correctly set, `false` if the target page is already the selected one. |                           |
| Name                                                                                                                 | Description                                                                                  |                           |
| `InvalidPage`                                                                                                        | If the page number is not a positive number.                                                 |                           |

| **setParameters**(params)                                                         |               |                       |
| --------------------------------------------------------------------------------- | ------------- | --------------------- |
| <p>Sets query parameters.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 484</p> |               |                       |
| Name                                                                              | Default Value | Summary               |
| params : `Object`                                                                 |               | The query parameters. |

| **setSearchPattern**(pattern)                                                                     |               |                     |
| ------------------------------------------------------------------------------------------------- | ------------- | ------------------- |
| <p>Sets the search pattern for the query.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 514</p> |               |                     |
| Name                                                                                              | Default Value | Summary             |
| pattern : `string`                                                                                |               | The search pattern. |

| **setSortBy**(sortBy)Abstract                                                        |               |                  |
| ------------------------------------------------------------------------------------ | ------------- | ---------------- |
| <p>Sets the sorting options.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 322</p> |               |                  |
| Name                                                                                 | Default Value | Summary          |
| sortBy : `string`                                                                    |               | Sorting options. |

| **sortBy**(sortBy, outsideCallback)Abstract                                                                                                         |               |                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------- |
| <p>Sorts the data, specifying a callback that will be called after the sorting takes place.</p><p>\*\*Source:\*\*queries/BaseQuery.js, line 334</p> |               |                     |
| Name                                                                                                                                                | Default Value | Summary             |
| sortBy : `string`                                                                                                                                   |               | Sorting options.    |
| outsideCallback : `function`                                                                                                                        |               | Post-sort callback. |
