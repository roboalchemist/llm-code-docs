# Source: https://kreya.app/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md

# Operation script API reference

In operation scripts, the definitions below are available through the `kreya` namespace. Furthermore, depending on the operation type, [`kreya.rest`](/docs/scripting-and-tests/operation-scripts/rest-script-api-reference.md), [`kreya.graphql`](/docs/scripting-and-tests/operation-scripts/graphql-script-api-reference.md), [`kreya.grpc`](/docs/scripting-and-tests/operation-scripts/grpc-script-api-reference.md) or [`kreya.webSocket`](/docs/scripting-and-tests/operation-scripts/websocket-script-api-reference.md) is available. Additionally all general Kreya APIs and bundled modules are available, see [general script API reference](/docs/scripting-and-tests/general.md).

```
kreya.trace('Starting operation invocation of ' + kreya.operation.current.name);

// Wait until some other operation sets this variable
while (!kreya.variables.has('my_var')) {
  kreya.sleep(10);
}

kreya.trace('Variable my_var has been set to ' + kreya.variables.get('my_var'));
```

## Variables[​](#variables "Direct link to Variables")

### operation[​](#operation "Direct link to operation")

```
const operation: OperationContainerScriptApi;
```

[OperationContainerScriptApi](#operationcontainerscriptapi)<br /><!-- -->Kreya scripting API for operations.

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### OperationContainerScriptApi[​](#operationcontainerscriptapi "Direct link to OperationContainerScriptApi")

```
type OperationContainerScriptApi = {
  current: OperationCurrentScriptApi;
};
```

Kreya scripting API for operations.

#### Properties[​](#properties "Direct link to Properties")

##### current[​](#current "Direct link to current")

```
readonly current: OperationCurrentScriptApi;
```

The current operation.

***

### OperationCurrentScriptApi[​](#operationcurrentscriptapi "Direct link to OperationCurrentScriptApi")

```
type OperationCurrentScriptApi = {
  name: string;
};
```

APIs to access an operation.

#### Properties[​](#properties-1 "Direct link to Properties")

##### name[​](#name "Direct link to name")

```
readonly name: string;
```

The name of the operation.
