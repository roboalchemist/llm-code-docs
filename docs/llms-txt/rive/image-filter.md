# Source: https://uat.rive.app/docs/scripting/api-reference/image/image-filter.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ImageFilter

Defines how image sampling is performed when scaling or transforming the
image.

* `bilinear`
* `nearest`

See [ImageSampler](/scripting/api-reference/image/image-sampler) for usage.

```lua highlight={6} theme={null}
function init(self: DrawImage, context: Context): boolean
  self.myImage = context:image('myImage')
  self.sampler = ImageSampler(
    'clamp',
    'clamp',
    'bilinear'
  )

  return true
end
```
