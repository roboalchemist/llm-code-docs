# Source: https://docs.base44.com/developers/references/sdk/docs/interfaces/functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# functions

***

## Overview

Functions module for invoking custom backend functions.

This module allows you to invoke the custom backend functions defined in the app.

### Authentication Modes

This module is available to use with a client in all authentication modes:

* **Anonymous or User authentication** (`base44.functions`): Functions are invoked with the current user's permissions. Anonymous users invoke functions without authentication, while authenticated users invoke functions with their authentication context.
* **Service role authentication** (`base44.asServiceRole.functions`): Functions are invoked with elevated admin-level permissions. The function code receives a request with admin authentication context.

### Generated Types

If you're working in a TypeScript project, you can generate types from your backend functions to get autocomplete on function names when calling `invoke()`. See the [Dynamic Types](/developers/references/sdk/getting-started/dynamic-types) guide to get started.

## Methods

### invoke()

> **invoke**(`functionName`, `data?`): `Promise`\<`any`>

Invokes a custom backend function by name.

Calls a custom backend function deployed to the app.
The function receives the provided data as named parameters and returns
the result. If any parameter is a `File` object, the request will automatically be
sent as `multipart/form-data`. Otherwise, it will be sent as JSON.

#### Parameters

<Accordion title="Properties">
  <ParamField body="functionName" type="string" required>
    The name of the function to invoke.
  </ParamField>

  <ParamField body="data" type="Record<string, any>">
    An object containing named parameters for the function.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise resolving to the function's response. The `data` property contains the data returned by the function, if there is any.

#### Examples

<CodeGroup>
  ```typescript Basic function call theme={null}
  const result = await base44.functions.invoke('calculateTotal', {
    items: ['item1', 'item2'],
  });
  console.log(result.data.total);
  ```

  ```typescript Function with file upload in React theme={null}
  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const processedImage = await base44.functions.invoke('processImage', {
        image: file,
        filter: 'grayscale',
        quality: 80
      });
    }
  };
  ```
</CodeGroup>

## Type Definitions

### FunctionName

***

> **FunctionName** = keyof `FunctionNameRegistry` *extends* `never` ? `string` : keyof `FunctionNameRegistry`

Union of all function names from the [`FunctionNameRegistry`](#functionnameregistry). Defaults to `string` when no types have been generated.

#### Example

<CodeGroup>
  ```typescript Using generated function name types theme={null}
  // With generated types, you get autocomplete on function names
  await base44.functions.invoke('calculateTotal', { items: ['item1', 'item2'] });
  ```
</CodeGroup>

### FunctionNameRegistry

***

Registry of function names. The [`types generate`](/developers/references/cli/commands/types-generate) command fills this registry, then [`FunctionName`](#functionname) resolves to a union of the keys.


Built with [Mintlify](https://mintlify.com).