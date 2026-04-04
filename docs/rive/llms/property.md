# Source: https://uat.rive.app/docs/scripting/api-reference/data-value/property.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Property

Represents a mutable property that stores a value and supports change listeners.

## Fields

### `value`

The current value of the property.

You can both read and assign to this field.

```lua highlight={4,5} theme={null}
local health = vm:getNumber("health")

if health then
  print(health.value) -- read
  health.value = 100  -- write
end
```

### `addListener`

Registers a listener that is called whenever the property’s value changes.

```lua highlight={8,10} theme={null}
local health = vm:getNumber("health")

if health then
  local function onHealthChanged(prop)
    print("New health:", prop.value)
  end

  health:addListener(onHealthChanged)

  health.value = 50 -- Triggers listener
end
```

### `removeListener`

Removes a previously registered listener.

```lua highlight={6} theme={null}
local health = vm:getNumber("health")

if health then
  local function onHealthChanged(prop)
    print("New health:", prop.value)
    health:removeListener(onHealthChanged)
  end

  health:addListener(onHealthChanged)

  health.value = 50 -- Triggers listener
end
```
