# Source: https://uat.rive.app/docs/scripting/api-reference/interfaces/data-context.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DataContext

Provides access to hierarchical data and its associated ViewModel.

## Methods

### `parent`

Returns the parent DataContext, if one exists.

```lua highlight={4} theme={null}
function init(self: MyNode, context: Context): boolean
  local dc = context:dataContext()
  if dc then
     local parentDC = dc:parent()
     local vm = dc:viewModel()
  end

  return true
end
```

### `viewModel`

Returns the ViewModel associated with this context.

```lua highlight={5} theme={null}
function init(self: MyNode, context: Context): boolean
  local dc = context:dataContext()
  if dc then
     local parentDC = dc:parent()
     local vm = dc:viewModel()
  end

  return true
end
```
