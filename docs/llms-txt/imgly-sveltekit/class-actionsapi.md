# Class: ActionsAPI

ActionsAPI provides a centralized way to manage and customize actions for various user interactions in the Creative Engine SDK.

This API allows you to:

*   Register custom actions for events (export, load, download, etc.)
*   Use default implementations when no custom action is registered
*   Maintain consistent behavior across different UI components

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`ActionsAPI`

## Methods[#](#methods)

### register()[#](#register)

  

Registers a custom action for a specific event type.

#### Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` _extends_ [`ActionId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionid/) |

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `actionId` | `T` | The event type to register an action for |
| `action` | [`ActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionfunction/)<`T`\> | The custom action function |

#### Returns[#](#returns)

`void`

#### Example[#](#example)

```
actionsAPI.register('downloadFile', async (blob, mimeType) => {  // Custom download logic  await customDownloadAction(blob, mimeType);});
```

#### Signature[#](#signature)

```
register(actionId: T, action: ActionFunction<T>): void
```

* * *

### get()[#](#get)

  

Returns the custom export video action if registered, otherwise returns the default.

#### Type Parameters[#](#type-parameters-1)

| Type Parameter | Default type |
| --- | --- |
| `T` _extends_ [`ActionId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionid/) | \- |
| `C` | [`CustomActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/customactionfunction/) |

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `actionId` | `T` | The event type to get an action for |

#### Returns[#](#returns-1)

[`ActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionfunction/)<`T`, `C`\>

#### Example[#](#example-1)

```
const exportAction = actionsAPI.get('export');if (exportAction) {  const result = await exportAction(options);}
```

#### Signature[#](#signature-1)

```
get(actionId: T): ActionFunction<T, C>
```

* * *

### run()[#](#run)

  

Executes a registered action with the provided parameters. Throws an error if the action is not registered.

#### Type Parameters[#](#type-parameters-2)

| Type Parameter | Default type |
| --- | --- |
| `T` _extends_ [`ActionId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionid/) | \- |
| `C` | [`CustomActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/customactionfunction/) |

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `actionId` | `T` | The event type to execute |
| …`args` | [`ActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionfunction/)<`T`, `C`\> _extends_ [`CustomActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/customactionfunction/) ? `Parameters`<[`ActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionfunction/)<[`ActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionfunction/)<`T`, `C`\>>> : `never`\[\] | The arguments to pass to the action |

#### Returns[#](#returns-2)

`Promise`<[`ActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionfunction/)<`T`, `C`\> _extends_ (…`args`) => `R` ? `R` : `never`\>

The result of the action execution

#### Throws[#](#throws)

Error if the action is not registered

#### Example[#](#example-2)

```
try {  const result = await actionsAPI.run('exportDesign', exportOptions);  console.log('Export completed', result);} catch (error) {  console.error('Export action not registered');}
```

#### Signature[#](#signature-2)

```
run(actionId: T, args: ActionFunction<T, C> extends CustomActionFunction ? Parameters<ActionFunction<ActionFunction<T, C>>> : never[]): Promise<ActionFunction<T, C> extends (args: any[]) => R ? R : never>
```

* * *

### list()[#](#list)

  

Returns all registered action IDs.

This method retrieves a list of all action identifiers that are available.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `matcher?`: `string`; } | Optional configuration object with the following properties: - `matcher`: Optional pattern to match against. Use `*` for wildcard matching. |
| `options.matcher?` | `string` | \- |

#### Returns[#](#returns-3)

[`ActionId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionid/)\[\]

An array of action IDs currently registered in the store

#### Example[#](#example-3)

```
const registeredActions = actionsAPI.list();console.log('Available actions:', registeredActions);// Output: ['saveScene', 'exportDesign', 'customAction1', ...]
// Find all export-related actions using wildcardconst exportActions = actionsAPI.list({ matcher: 'export*' });console.log('Export actions:', exportActions);// Output: ['exportDesign', 'exportScene', ...]
```

#### Signature[#](#signature-3)

```
list(options?: object): ActionId[]
```

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/userinterface)