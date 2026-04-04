# Source: https://uat.rive.app/docs/scripting/api-reference/path/command-type.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CommandType

Describes the type of drawing command stored in a [PathCommand](/scripting/api-reference/path/path-command).

For more information on the following command types, see [Path](/scripting/api-reference/path/path).

* `none` – Placeholder command with no effect. You should not normally see this.
* `moveTo`
* `lineTo`
* `cubicTo`
* `quadTo`
* `close`

```lua highlight={5} theme={null}
local path = Path.new()
path:moveTo(Vector.xy(0, 0))
path:lineTo(Vector.xy(10, 0))

for i, command in ipairs(path) do
  print(i, command.type)
end
-- 1 moveTo
-- 2 lineTo
```
