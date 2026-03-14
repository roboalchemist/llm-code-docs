# Source: https://uat.rive.app/docs/scripting/api-reference/interfaces/enum-values.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# EnumValues

## Methods

### `__len`

Get the number of enum values.

```lua highlight={7} theme={null}
local vmi = context:viewModel()
if vmi then
    local textAlignment = vmi:getEnum('textAlignment')

    if textAlignment then
        local values = textAlignment:values()
        print('count: ', #values)
    end
end
```
