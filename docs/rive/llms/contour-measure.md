# Source: https://uat.rive.app/docs/scripting/api-reference/path/contour-measure.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ContourMeasure

A ContourMeasure is a way to measure and manipulate a single contour within a path.
A contour is one continuous drawing sequence that starts with a `moveTo` and continues until the next `moveTo` (or the end of the path).

## Fields

### `next`

Returns the next [ContourMeasure](/scripting/api-reference/path/contour-measure) in the path, or nil if this is the last
contour. Use this to iterate through all contours in a path after calling
path:contours().

```lua  theme={null}
local contour = pathData:contours()
while contour do
  print(contour.length)
  contour = contour.next
end
```
