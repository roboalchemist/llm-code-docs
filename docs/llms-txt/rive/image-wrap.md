# Source: https://uat.rive.app/docs/scripting/api-reference/image/image-wrap.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ImageWrap

Defines how texture coordinates outside the \[0, 1] range are handled.

* `clamp`
* `repeat`
* `mirror`

See [ImageSampler](/scripting/api-reference/image/image-sampler) for usage.

```lua highlight={5,7} theme={null}
function init(self: DrawImage, context: Context): boolean
  self.myImage = context:image('myImage')
  self.sampler = ImageSampler(
    -- Image wrap X
    'clamp',
    -- Image wrap Y
    'clamp',
    'bilinear'
  )

  return true
end
```
