# Source: https://lynxjs.org/api/lynx-api/nodes-ref/nodes-ref-invoke.md

# NodesRef: invoke() method

<APISummary />

Execute the UI method of the selected node.

Please note that the UI function is a function provided by the client, usually directly controlling UI functions, such as the play or stop of the player.
`invoke` cannot be used to call a js function of a custom component.

## Syntax

```ts
invoke(options: Record<string, any>): SelectorQuery;
```

### Parameters

### options

The `options` parameter is a `Record<string, any>`, which contains the information needed for the execution of the UI method. Its key list is as follows:

- `method`

- A `string`, the name of the UI method to be called

- `params` (optional)

- A `Record<string, any>`, the parameters of the UI method to be called

- `success` (optional)

- A callback function that is called when the UI method is successfully executed, with the first parameter being the result returned by the UI method

- `fail` (optional)

- A callback function that is called when the UI method fails to execute, with the first parameter type being `{code: number, data: any}`, which contains the error code and error message returned by the UI method.

- If no fail callback function is provided, a red screen error will be generated when the UI method fails to execute.

### Return Value

Contains the `SelectorQuery` object for this task. Call `exec()` to execute the task.

## Examples

```javascript
var params = {
  method: 'seekTo',
  params: {
    duration: 1000,
  },
  success: function (res) {
    console.log(res);
  },
  fail: function (data) {
    console.log(data.code, data.data);
  },
};

lynx.createSelectorQuery().select('#video').invoke(params).exec();
```

## Compatibility

**Compatibility Table**
**Query:** `lynx-api.nodes-ref.invoke`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 2.2 | Does not support usage on `NodesRef` created through `SelectorQuery.proptotype.selectAll()`.; ⚠️ Partial implementation |
| iOS | 2.2 | Does not support usage on `NodesRef` created through `SelectorQuery.proptotype.selectAll()`.; ⚠️ Partial implementation |
| HarmonyOS | 3.4 | Does not support usage on `NodesRef` created through `SelectorQuery.proptotype.selectAll()`.; ⚠️ Partial implementation |
| Web | 1.0 | Does not support usage on `NodesRef` created through `SelectorQuery.proptotype.selectAll()`.; ⚠️ Partial implementation |

**Description:** Execute the UI method of the selected node.

