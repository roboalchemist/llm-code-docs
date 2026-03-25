# Source: https://uat.rive.app/docs/scripting/api-reference/image/image.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image

Represents an image asset that can be drawn by the [Renderer](/scripting/api-reference/renderer/renderer).

```lua highlight={2,7,15} theme={null}
type DrawImage = {
  myImage: Image?,
  sampler: ImageSampler?,
}

function init(self: DrawImage, context: Context): boolean
  self.myImage = context:image('myImage')
  self.sampler = ImageSampler('clamp', 'clamp', 'bilinear')

  return true
end

function draw(self: DrawImage, renderer: Renderer)
  if self.myImage and self.sampler then
    renderer:drawImage(self.myImage, self.sampler, 'srcOver', 1)
  end
end

return function(): Node<DrawImage>
  return {
    myImage = nil,
    sampler = nil,
    init = init,
    draw = draw,
  }
end
```

## Fields

### `width`

Width of the image.

```lua highlight={4} theme={null}
self.myImage = context:image('myImage')

if self.myImage then
    print("myImage width:", self.myImage.width)
end
```

### `height`

Height of the image.

```lua highlight={4} theme={null}
self.myImage = context:image('myImage')

if self.myImage then
    print("myImage height:", self.myImage.height    )
end
```
