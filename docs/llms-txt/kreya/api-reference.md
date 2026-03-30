# Source: https://kreya.app/docs/scripting-and-tests/invoker-scripts/api-reference.md

# Script API reference

In scripts, the definitions below are available through the `kreya` object. Additionally all general Kreya APIs and bundled modules are available, see [general script API reference](/docs/scripting-and-tests/general.md).

```
kreya.trace('Starting script invocation of ' + kreya.script.current.name);

await kreya.invokeOperation('my-gRPC-operation');

let success = false;
while (!success) {
  const result = await kreya.invokeOperation('my-rest-operation');
  success = result.success;

  kreya.sleep(100);
}
```

## Variables[​](#variables "Direct link to Variables")

### script[​](#script "Direct link to script")

```
const script: InvokerScriptContainerScriptApi;
```

[InvokerScriptContainerScriptApi](#invokerscriptcontainerscriptapi)<br /><!-- -->Kreya scripting API for scripts.

## Functions[​](#functions "Direct link to Functions")

### invokeOperation()[​](#invokeoperation "Direct link to invokeOperation()")

```
function invokeOperation(operationPath: string): Promise<ScriptOperationResult>;
```

Invoke an operation.

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter       | Type     | Description                                                          |
| --------------- | -------- | -------------------------------------------------------------------- |
| `operationPath` | `string` | The path of the operation to invoke. Must be relative to the script. |

#### Returns[​](#returns "Direct link to Returns")

`Promise`<[`ScriptOperationResult`](#scriptoperationresult)>

Returns the result of the operation invocation.

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### InvokerScriptContainerScriptApi[​](#invokerscriptcontainerscriptapi "Direct link to InvokerScriptContainerScriptApi")

```
type InvokerScriptContainerScriptApi = {
  current: InvokerScriptCurrentScriptApi;
};
```

Kreya scripting API for scripts.

#### Properties[​](#properties "Direct link to Properties")

##### current[​](#current "Direct link to current")

```
readonly current: InvokerScriptCurrentScriptApi;
```

The current script.

***

### InvokerScriptCurrentScriptApi[​](#invokerscriptcurrentscriptapi "Direct link to InvokerScriptCurrentScriptApi")

```
type InvokerScriptCurrentScriptApi = {
  name: string;
};
```

APIs to access a script.

#### Properties[​](#properties-1 "Direct link to Properties")

##### name[​](#name "Direct link to name")

```
readonly name: string;
```

The name of the script.

***

### ScriptOperationResult[​](#scriptoperationresult "Direct link to ScriptOperationResult")

```
type ScriptOperationResult = {
  status?: ScriptOperationStatus;
  success: boolean;
};
```

The result of an operation invocation.

#### Properties[​](#properties-2 "Direct link to Properties")

##### status?[​](#status "Direct link to status?")

```
optional status: ScriptOperationStatus;
```

Detailed information about the response status.

##### success[​](#success "Direct link to success")

```
success: boolean;
```

If the operation contains tests, this returns true if all tests were successful. If the operation does not contain tests, this returns true if the response status code indicates success.

***

### ScriptOperationStatus[​](#scriptoperationstatus "Direct link to ScriptOperationStatus")

```
type ScriptOperationStatus = {
  code: number;
  detailMessage?: string;
  statusName: string;
  success: boolean;
};
```

The status of an operation response.

#### Properties[​](#properties-3 "Direct link to Properties")

##### code[​](#code "Direct link to code")

```
code: number;
```

The response status code, ex. 200 for a successful REST response.

##### detailMessage?[​](#detailmessage "Direct link to detailMessage?")

```
optional detailMessage: string;
```

An optional detail message about the status, received from the server.

##### statusName[​](#statusname "Direct link to statusName")

```
statusName: string;
```

The response status name, ex. OK for a successful REST response.

##### success[​](#success-1 "Direct link to success")

```
success: boolean;
```

True if the status indicates success.
