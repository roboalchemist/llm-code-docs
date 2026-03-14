# Source: https://uat.rive.app/docs/scripting/api-reference/interfaces/property-enum.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PropertyEnum

PropertyEnum is a [Property](/scripting/api-reference/data-value/property) with additional enum-specific APIs.

## Methods

### `values`

The [EnumValues](/scripting/api-reference/interfaces/enum-values) of the enum.

```lua highlight={6} theme={null}
local vmi = context:viewModel()
if vmi then
    local textAlignment = vmi:getEnum('textAlignment')

    if textAlignment then
        local values = textAlignment:values()
    end
end
```
