# Source: https://docs.xano.com/xanoscript/function-reference/actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Actions

## Call an Action

Invokes an [action](/xano-actions/what-are-actions) within your Xano workspace. The action must be imported to your workspace to be called.

```JavaScript  theme={null}
    action.call "action name" {
      input = {
        input_name          : input_value
      }
    registry = {registry_key: registry_value}
    } as $action
```

| Parameter   | Description                                                                                   | Example                       |
| ----------- | --------------------------------------------------------------------------------------------- | ----------------------------- |
| action name | The name of the action to call.                                                               | "Claude AI -> Ask a Question" |
| input       | An object containing key-value pairs for each input parameter required by the action.         | *See above.*                  |
| registry    | (Optional) An object containing key-value pairs for any registry values needed by the action. | *See above.*                  |
| \$action    | The variable to store the result of the action call.                                          | \$action                      |


Built with [Mintlify](https://mintlify.com).