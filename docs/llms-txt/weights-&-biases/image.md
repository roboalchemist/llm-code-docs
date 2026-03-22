# Source: https://docs.wandb.ai/models/ref/python/data-types/image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Image

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/sdk/data_types/image.py" />

## <kbd>class</kbd> `Image`

A class for logging images to W\&B.

### <kbd>method</kbd> `Image.__init__`

```python  theme={null}
__init__(
    data_or_path: 'ImageDataOrPathType',
    mode: 'str | None' = None,
    caption: 'str | None' = None,
    grouping: 'int | None' = None,
    classes: 'Classes | Sequence[dict] | None' = None,
    boxes: 'dict[str, BoundingBoxes2D] | dict[str, dict] | None' = None,
    masks: 'dict[str, ImageMask] | dict[str, dict] | None' = None,
    file_type: 'str | None' = None,
    normalize: 'bool' = True
) → None
```

Initialize a `wandb.Image` object.

This class handles various image data formats and automatically normalizes pixel values to the range \[0, 255] when needed, ensuring compatibility with the W\&B backend.

* Data in range \[0, 1] is multiplied by 255 and converted to uint8 \* Data in range \[-1, 1] is rescaled from \[-1, 1] to \[0, 255] by mapping
  -1 to 0 and 1 to 255, then converted to uint8 \* Data outside \[-1, 1] but not in \[0, 255] is clipped to \[0, 255] and  converted to uint8 (with a warning if values fall outside \[0, 255]) \* Data already in \[0, 255] is converted to uint8 without modification

**Args:**

* `data_or_path`:  Accepts NumPy array/pytorch tensor of image data,  a PIL image object, or a path to an image file. If a NumPy  array or pytorch tensor is provided,  the image data will be saved to the given file type.  If the values are not in the range \[0, 255] or all values are in the range \[0, 1],  the image pixel values will be normalized to the range \[0, 255]  unless `normalize` is set to `False`.
  * pytorch tensor should be in the format (channel, height, width)
  * NumPy array should be in the format (height, width, channel)
* `mode`:  The PIL mode for an image. Most common are "L", "RGB", "RGBA".
* `Full Pillow docs for more information https`: //pillow\.readthedocs.io/en/stable/handbook/concepts.html#modes
* `caption`:  Label for display of image.
* `grouping`:  The grouping number for the image.
* `classes`:  A list of class information for the image,  used for labeling bounding boxes, and image masks.
* `boxes`:  A dictionary containing bounding box information for the image.
* `see https`: //docs.wandb.ai/ref/python/data-types/boundingboxes2d/
* `masks`:  A dictionary containing mask information for the image.
* `see https`: //docs.wandb.ai/ref/python/data-types/imagemask/
* `file_type`:  The file type to save the image as.  This parameter has no effect if `data_or_path` is a path to an image file.
* `normalize`:  If `True`, normalize the image pixel values to fall within the range of \[0, 255].  Normalize is only applied if `data_or_path` is a numpy array or pytorch tensor.

**Examples:**
Create a wandb.Image from a numpy array

```python  theme={null}
import numpy as np
import wandb

with wandb.init() as run:
    examples = []
    for i in range(3):
         pixels = np.random.randint(low=0, high=256, size=(100, 100, 3))
         image = wandb.Image(pixels, caption=f"random field {i}")
         examples.append(image)
    run.log({"examples": examples})
```

Create a wandb.Image from a PILImage

```python  theme={null}
import numpy as np
from PIL import Image as PILImage
import wandb

with wandb.init() as run:
    examples = []
    for i in range(3):
         pixels = np.random.randint(
             low=0, high=256, size=(100, 100, 3), dtype=np.uint8
         )
         pil_image = PILImage.fromarray(pixels, mode="RGB")
         image = wandb.Image(pil_image, caption=f"random field {i}")
         examples.append(image)
    run.log({"examples": examples})
```

Log .jpg rather than .png (default)

```python  theme={null}
import numpy as np
import wandb

with wandb.init() as run:
    examples = []
    for i in range(3):
         pixels = np.random.randint(low=0, high=256, size=(100, 100, 3))
         image = wandb.Image(
             pixels, caption=f"random field {i}", file_type="jpg"
         )
         examples.append(image)
    run.log({"examples": examples})
```

***

### <kbd>property</kbd> Image.image

***
